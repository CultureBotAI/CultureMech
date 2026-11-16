#!/usr/bin/env python3
"""Read-only fragment-width diagnosis for #683, 2026-11-16.

Inputs: base02e/current f9 corpus, native record_io and frozen renderer.
Outputs: exclusive ignored summary/diffs for the exact Random(3) 300-record
sample and all changed records. Simulates width=80-indent in a compiled local
AST copy only; never edits recipes or the maintained writer/renderer.
"""

import argparse
import ast
import difflib
import json
import random
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import curate_variant_ingredients as curate  # noqa: E402
import record_io  # noqa: E402
from record_kinds import is_solution_record  # noqa: E402

BASE = "02e005db42246b8a04ece9df4b5657e036fa5697"
CANDIDATE = "f9dee2d216"


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def adjusted_renderer():
    source = ast.parse(git("show", CANDIDATE + ":scripts/curate_variant_ingredients.py"))
    functions = [
        node
        for node in source.body
        if isinstance(node, ast.FunctionDef) and node.name == "render_additions"
    ]
    if len(functions) != 1:
        raise ValueError("expected one pinned renderer")
    tree = ast.Module(body=functions, type_ignores=[])
    changed = 0
    for node in ast.walk(tree):
        if (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and node.func.attr == "safe_dump"
        ):
            node.keywords.append(
                ast.keyword(
                    arg="width",
                    value=ast.BinOp(
                        left=ast.Constant(80),
                        op=ast.Sub(),
                        right=ast.Name(id="indent", ctx=ast.Load()),
                    ),
                )
            )
            changed += 1
    if changed != 1:
        raise ValueError("expected exactly one fragment serializer")
    namespace = dict(curate.__dict__)
    exec(
        compile(ast.fix_missing_locations(tree), "<read-only-width-simulation>", "exec"), namespace
    )
    return namespace["render_additions"]


def canonical(raw):
    text = raw.decode("utf-8", errors="replace")
    return record_io.dump_record(yaml.safe_load(text)) == text


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", type=Path, required=True)
    args = parser.parse_args()
    out = args.output_directory
    out.mkdir(parents=True, exist_ok=False)
    changed = git("diff", "--name-only", BASE, "--", "data/normalized_yaml").decode().splitlines()
    if git("diff", "--name-only", CANDIDATE, "--", "data/normalized_yaml").strip():
        raise ValueError("current corpus differs from f9 candidate")
    all_paths = sorted((ROOT / "data/normalized_yaml").rglob("*.yaml"))
    tracked = (
        git("ls-tree", "-r", "--name-only", BASE, "data/normalized_yaml").decode().splitlines()
    )
    if {str(path.relative_to(ROOT)) for path in all_paths} != {
        path for path in tracked if path.endswith(".yaml")
    }:
        raise ValueError("base/current path membership differs")
    base_raw = {path: git("show", BASE + ":" + path) for path in changed}
    current_raw = {path: (ROOT / path).read_bytes() for path in changed}
    loader = getattr(yaml, "CSafeLoader", yaml.SafeLoader)
    media_paths = []
    for path in all_paths:
        relative = str(path.relative_to(ROOT))
        try:
            record = yaml.load(path.read_text(errors="replace"), Loader=loader)
        except (yaml.YAMLError, OSError):
            continue
        if relative in base_raw:
            previous = yaml.load(base_raw[relative].decode(errors="replace"), Loader=loader)
            if isinstance(previous, dict) != isinstance(record, dict) or is_solution_record(
                previous
            ) != is_solution_record(record):
                raise ValueError("classification changed, sample membership differs")
        if isinstance(record, dict) and not is_solution_record(record):
            media_paths.append(relative)
    sample = random.Random(3).sample(media_paths, min(300, len(media_paths)))
    fixed = {}
    renderer = adjusted_renderer()
    changed_report = []
    for relative in changed:
        desired = yaml.safe_load(current_raw[relative])
        event = json.loads(desired["curation_history"][-1]["changes"])
        fixed[relative] = renderer(base_raw[relative], desired, event["variants"])
        if yaml.safe_load(fixed[relative]) != desired:
            raise ValueError("simulation changed parsed content")
        item = {
            "path": relative,
            "in_sample": relative in sample,
            "base_canonical": canonical(base_raw[relative]),
            "f9_canonical": canonical(current_raw[relative]),
            "adjusted_canonical": canonical(fixed[relative]),
        }
        changed_report.append(item)
        if item["in_sample"]:
            native = record_io.dump_record(desired)
            diff = difflib.unified_diff(
                current_raw[relative].decode().splitlines(keepends=True),
                native.splitlines(keepends=True),
                fromfile="f9",
                tofile="native-default",
            )
            (out / (Path(relative).name + ".native.diff")).write_text("".join(diff))
    counts = {"base": 0, "f9": 0, "adjusted": 0}
    for relative in sample:
        current = current_raw.get(relative)
        if current is None:
            current = (ROOT / relative).read_bytes()
        counts["base"] += canonical(base_raw.get(relative, current))
        counts["f9"] += canonical(current)
        counts["adjusted"] += canonical(fixed.get(relative, current))
    for path, original in current_raw.items():
        if (ROOT / path).read_bytes() != original:
            raise ValueError("input changed during diagnosis")
    summary = {
        "base": BASE,
        "candidate": git("rev-parse", CANDIDATE).decode().strip(),
        "sample_size": len(sample),
        "sample_paths": sample,
        "media_population": len(media_paths),
        "canonical_sample_counts": counts,
        "changed_records": changed_report,
        "changed_record_counts": {
            key: sum(item[key] for item in changed_report)
            for key in ("base_canonical", "f9_canonical", "adjusted_canonical")
        },
        "limitation": "Read-only simulation, not a saved correction or changed native writer. Existing presentation is retained, so legacy noncanonical inputs can remain noncanonical.",
    }
    (out / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(
        json.dumps(
            {
                key: value
                for key, value in summary.items()
                if key not in {"sample_paths", "changed_records"}
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
