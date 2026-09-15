"""Repair retained map routes using exact historical YAML filename identity.

Coordinates and historical metadata remain unchanged. This repairs navigation;
it does not establish provenance for the historical embedding inputs or reducer.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import tempfile
from collections import Counter, defaultdict
from pathlib import Path

import yaml

from culturemech.render_media_pages import slug_for
from culturemech.web_artifacts import load_browser_data

POPULATIONS = ("derivedData", "directData")
MAPS = ("umap.html", "umap_graph.html")
ROUTE_KEYS = {"url", "record_link_status", "record_source_file"}
NOTICE = (
    '<p id="historical-map-notice">Historical graph map: embedding input and reducer '
    "lineage are unverified. Coordinates are retained. Links use exact source-file "
    "identity where available; unresolved or ambiguous points open the media browser.</p>"
)
TOOLTIP = """<br/>
                            Record link: ${d.record_link_status === 'exact-category-source' || d.record_link_status === 'unique-source' ? 'Current record (exact source filename)' : 'Media browser (historical record unresolved or ambiguous)'}"""


def _digest(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    ).hexdigest()


def read_population(content: str, name: str):
    matches = list(re.finditer(r"\bconst\s+" + re.escape(name) + r"\s*=\s*", content))
    if len(matches) != 1:
        raise ValueError(f"expected exactly one {name} population")
    start = matches[0].end()
    value, length = json.JSONDecoder().raw_decode(content[start:])
    if not isinstance(value, list) or not all(isinstance(row, dict) for row in value):
        raise ValueError(f"invalid {name} population")
    return value, start, start + length


def _inline_json(value):
    text = json.dumps(value, ensure_ascii=False, allow_nan=False)
    for char in "<>&\u2028\u2029":
        text = text.replace(char, f"\\u{ord(char):04x}")
    return text


def _current_sources(root: Path):
    corpus = root / "data/normalized_yaml"
    # pathlib includes ignored files: completeness must not depend on gitignore.
    paths = {p.relative_to(corpus).as_posix(): p for p in corpus.rglob("*.yaml")}
    records = load_browser_data(root / "app/data.js")
    sources = [record.get("source_file") for record in records]
    if len(set(sources)) != len(records) or set(sources) != set(paths):
        raise ValueError("browser source files must cover the complete current YAML corpus once")
    by_category = defaultdict(list)
    by_stem = defaultdict(list)
    seen_ids, seen_pages = set(), set()
    source_receipt = hashlib.sha256()
    for row in sorted(records, key=lambda item: item["source_file"]):
        source = paths[row["source_file"]]
        if source.is_symlink() or not source.resolve().is_relative_to(corpus.resolve()):
            raise ValueError(f"unsafe source path: {row['source_file']}")
        raw = source.read_bytes()
        recipe = yaml.load(raw, Loader=getattr(yaml, "CSafeLoader", yaml.SafeLoader))
        if not isinstance(recipe, dict) or not recipe.get("id") or row.get("id") != recipe["id"]:
            raise ValueError(f"browser/YAML identity mismatch: {row['source_file']}")
        expected_page = "normalized/" + slug_for(recipe, source) + ".html"
        if row.get("html_page") != expected_page:
            raise ValueError(f"browser/YAML page mismatch: {row['source_file']}")
        if row["id"] in seen_ids or expected_page in seen_pages:
            raise ValueError("duplicate current record identity or page")
        seen_ids.add(row["id"])
        seen_pages.add(expected_page)
        page = root / "pages" / expected_page
        if not page.is_file() or not page.resolve().is_relative_to((root / "pages").resolve()):
            raise ValueError(f"missing or unsafe rendered page: {expected_page}")
        entry = {"source_file": row["source_file"], "url": "../pages/" + expected_page}
        by_category[(source.parent.name, source.stem)].append(entry)
        by_stem[source.stem].append(entry)
        for value in (row["source_file"].encode(), raw):
            source_receipt.update(len(value).to_bytes(8, "big"))
            source_receipt.update(value)
    if not records or not (root / "app/browser.html").is_file():
        raise ValueError("current corpus and fallback browser must exist")
    return by_category, by_stem, source_receipt.hexdigest(), len(records)


def prepare_repairs(root: Path):
    """Validate all inputs and return complete replacement bytes before any write."""
    category_sources, stem_sources, source_sha, count = _current_sources(root)
    prepared = {}
    report = {"current_records": count, "source_sha256": source_sha, "maps": {}}
    for name in MAPS:
        path = root / "app" / name
        content = path.read_text()
        replacements = []
        populations = {}
        for population in POPULATIONS:
            points, start, end = read_population(content, population)
            unchanged = [{k: v for k, v in p.items() if k not in ROUTE_KEYS} for p in points]
            before = _digest(unchanged)
            statuses = Counter()
            for point in points:
                identity = point.get("id")
                if not isinstance(identity, str) or not identity:
                    raise ValueError(f"invalid historical identity in {name}/{population}")
                candidates = category_sources.get((point.get("category"), identity), [])
                status = "exact-category-source"
                if not candidates:
                    candidates = stem_sources.get(identity, [])
                    status = "unique-source"
                if len(candidates) == 1:
                    point["url"] = candidates[0]["url"]
                    point["record_source_file"] = candidates[0]["source_file"]
                else:
                    point["url"] = "browser.html"
                    point["record_source_file"] = None
                    status = "ambiguous" if candidates else "unresolved"
                point["record_link_status"] = status
                statuses[status] += 1
            after = _digest([{k: v for k, v in p.items() if k not in ROUTE_KEYS} for p in points])
            if before != after:
                raise ValueError("historical geometry or metadata changed")
            populations[population] = {
                "points": len(points),
                "links": dict(statuses),
                "preserved_payload_sha256": before,
            }
            replacements.append((start, end, _inline_json(points)))
        for start, end, replacement in sorted(replacements, reverse=True):
            content = content[:start] + replacement + content[end:]
        content, changed = re.subn(
            r"(<header>.*?<h1>.*?</h1>\s*)<p(?:\s[^>]*)?>.*?</p>",
            lambda match: match[1] + NOTICE,
            content,
            count=1,
            flags=re.S,
        )
        if changed != 1:
            raise ValueError(f"missing historical map header in {name}")
        if "Record link: ${d.record_link_status" not in content:
            old = "Source: ${d.source_database}"
            if content.count(old) != 1:
                raise ValueError(f"unrecognized historical tooltip in {name}")
            content = content.replace(old, old + TOOLTIP)
        prepared[path] = content.encode()
        report["maps"][name] = populations
    return prepared, report


def repair(root: Path, *, apply: bool = False, check: bool = False):
    prepared, report = prepare_repairs(root)
    changed = [path for path, data in prepared.items() if path.read_bytes() != data]
    report.update(
        mode="apply" if apply else "check" if check else "preview",
        changed=[path.relative_to(root).as_posix() for path in changed],
    )
    if check and changed:
        raise ValueError("historical map routes need repair: " + ", ".join(report["changed"]))
    if apply:
        # Complete preflight above; each file replacement is atomic. This is not
        # a transaction across both retained HTML files.
        for path in changed:
            temporary = None
            try:
                with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as stream:
                    temporary = Path(stream.name)
                    stream.write(prepared[path])
                    stream.flush()
                    os.fsync(stream.fileno())
                temporary.chmod(path.stat().st_mode & 0o777)
                os.replace(temporary, path)
            finally:
                if temporary is not None:
                    temporary.unlink(missing_ok=True)
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    try:
        print(json.dumps(repair(args.root.resolve(), apply=args.apply, check=args.check), indent=2))
    except (ValueError, OSError) as error:
        parser.exit(1, f"error: {error}\n")
    return 0
