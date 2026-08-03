#!/usr/bin/env python3
"""Run deep research for CultureMech media records via deep-research-client."""
from __future__ import annotations

import argparse
import os
import shlex
import subprocess
import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
MEDIA_DIR = REPO_ROOT / "data" / "normalized_yaml"
DEFAULT_TEMPLATE = REPO_ROOT / "templates" / "media_growth_research.md"
DEFAULT_RESEARCH_DIR = REPO_ROOT / "research"


def load_media(path: Path) -> dict[str, Any]:
    """Load a CultureMech MediaRecipe YAML file."""
    if not path.exists():
        raise FileNotFoundError(f"Media file not found: {path}")
    doc = yaml.safe_load(path.read_text())
    if not isinstance(doc, dict):
        raise ValueError(f"Media file is not a YAML mapping: {path}")
    return doc


def _normal_key(value: str) -> str:
    return value.strip().casefold()


def _candidate_paths(target: str) -> list[Path]:
    """All records matching `target` on any identifier. Kept for callers that want
    the full set; `resolve_media_file` ranks these rather than treating them as
    equally good."""
    return [p for tier in _tiered_candidates(target) for p in tier]


def _tiered_candidates(target: str) -> list[list[Path]]:
    """Matches grouped by how specific the match is, most specific first.

    Ranking matters because 2,291 record `name:` values are shared by more than one
    record, and every one of them is also some other record's filename. So
    `lb_broth` matches both `bacterial/lb_broth.yaml` (by filename) and
    `bacterial/TOGO_M3227_LB_broth.yaml` (by its `name:` field). Treating those as
    equally good made the resolver raise on 2,291 slugs, which blocked any
    slug-driven batch (#151).

    Tiers, in order:
      1. CultureMech id — unique by construction, guarded by tests/test_id_registry.
      2. filename stem or full filename — unique within a directory, and the
         corpus keeps filenames unique across directories except for the
         collisions tracked in #151.
      3. `name` / `original_name` / `media_term.preferred_term` — NOT unique.
    """
    target_path = Path(target)
    if target_path.exists():
        return [[target_path.resolve()]]

    normalized_target = _normal_key(target)
    by_id: list[Path] = []
    by_filename: list[Path] = []
    by_field: list[Path] = []

    for path in sorted(MEDIA_DIR.glob("*/*.yaml")):
        if _normal_key(path.stem) == normalized_target or \
                _normal_key(path.name) == normalized_target:
            by_filename.append(path)
            continue
        # Cheap reject before parsing: the identifier must appear somewhere.
        if normalized_target not in path.read_text().casefold():
            continue
        doc = load_media(path)
        if doc.get("id") is not None and \
                _normal_key(str(doc["id"])) == normalized_target:
            by_id.append(path)
            continue
        media_term = doc.get("media_term")
        identifiers = [
            doc.get("name"),
            doc.get("original_name"),
            media_term.get("preferred_term") if isinstance(media_term, dict) else None,
        ]
        if any(v is not None and _normal_key(str(v)) == normalized_target
               for v in identifiers):
            by_field.append(path)

    return [tier for tier in (by_id, by_filename, by_field) if tier]


def resolve_media_file(target: str) -> Path:
    """Resolve a path, slug, CultureMech ID, name, or original name to one media YAML.

    Takes the most specific tier that matches. Raises only when that tier is itself
    ambiguous — i.e. the target genuinely does not identify one record — rather
    than when a broader tier happens to match something else too.
    """
    tiers = _tiered_candidates(target)
    if not tiers:
        raise FileNotFoundError(f"Media target not found under {MEDIA_DIR}: {target}")
    best = tiers[0]
    if len(best) == 1:
        return best[0]
    choices = ", ".join(str(path.relative_to(REPO_ROOT)) for path in best[:20])
    raise ValueError(
        f"Target {target!r} matched multiple media records equally specifically: "
        f"{choices}. Pass a file path or a CultureMech id to disambiguate."
    )


def _join_values(values: Any) -> str:
    if values is None:
        return ""
    if isinstance(values, list):
        return ", ".join(str(value) for value in values)
    return str(values)


def _name_with_id(value: Any) -> str:
    if not isinstance(value, dict):
        return str(value)
    label = value.get("preferred_term") or value.get("name") or value.get("label") or ""
    term = value.get("term")
    if isinstance(term, dict) and term.get("id"):
        return f"{label} ({term['id']})".strip()
    return str(label)


def summarize_ingredients(doc: dict[str, Any], limit: int = 40) -> str:
    rows = []
    for ingredient in doc.get("ingredients", []) or []:
        if not isinstance(ingredient, dict):
            continue
        name = ingredient.get("preferred_term", "")
        concentration = ingredient.get("concentration")
        if isinstance(concentration, dict):
            value = concentration.get("value", "")
            unit = concentration.get("unit", "")
            amount = f"{value} {unit}".strip()
        else:
            amount = ""
        term = ingredient.get("term")
        term_id = f" ({term['id']})" if isinstance(term, dict) and term.get("id") else ""
        rows.append(f"{name}{term_id}: {amount}".strip(": "))
    suffix = f" | ... {len(rows) - limit} more" if len(rows) > limit else ""
    return " | ".join(rows[:limit]) + suffix


def summarize_solutions(doc: dict[str, Any]) -> str:
    rows = []
    for solution in doc.get("solutions", []) or []:
        if not isinstance(solution, dict):
            continue
        rows.append(str(solution.get("name") or solution.get("description") or solution))
    return " | ".join(rows)


def summarize_target_organisms(doc: dict[str, Any]) -> str:
    rows = []
    for organism in doc.get("target_organisms", []) or []:
        if not isinstance(organism, dict):
            rows.append(str(organism))
            continue
        parts = [
            organism.get("preferred_term") or organism.get("name"),
            organism.get("strain"),
            organism.get("taxonomic_identifier"),
            organism.get("ncbi_taxonomy_id"),
        ]
        rows.append(" / ".join(str(part) for part in parts if part))
    return " | ".join(rows)


def summarize_variants(doc: dict[str, Any]) -> str:
    rows = []
    for variant in doc.get("variants", []) or []:
        if not isinstance(variant, dict):
            rows.append(str(variant))
            continue
        name = variant.get("name", "")
        description = variant.get("description", "")
        modifications = _join_values(variant.get("modifications"))
        rows.append(f"{name}: {description}; modifications={modifications}".strip("; "))
    return " | ".join(rows)


def _summarize_media_ref(ref: Any) -> str:
    """One-line summary of a MediaRecipeReference (parent_media / variant_children entry)."""
    if not isinstance(ref, dict):
        return str(ref)
    parts = [
        ref.get("name") or ref.get("id"),
        ref.get("id") if ref.get("name") else None,
        ref.get("path"),
        ref.get("relationship"),
    ]
    summary = " / ".join(str(part) for part in parts if part)
    notes = ref.get("notes")
    return f"{summary} — {notes}".strip(" —") if notes else summary


def summarize_variant_records(doc: dict[str, Any]) -> str:
    """Cross-record variant set: parent linkage + child records + this record's own variant role.

    Complements ``summarize_variants`` (which only covers inline ``variants[]``).
    Captures parent_media, variant_relationship/variant_modifications, and
    variant_children so the deep-research prompt can validate *each set of variants*.
    """
    rows = []
    parent = doc.get("parent_media")
    if parent:
        rows.append(f"PARENT: {_summarize_media_ref(parent)}")
    relationship = doc.get("variant_relationship")
    modifications = _join_values(doc.get("variant_modifications"))
    if relationship or modifications:
        own = f"THIS-RECORD-IS-VARIANT: relationship={relationship or ''}"
        if modifications:
            own += f"; modifications={modifications}"
        rows.append(own.strip("; "))
    for child in doc.get("variant_children", []) or []:
        rows.append(f"CHILD: {_summarize_media_ref(child)}")
    return " | ".join(rows)


def summarize_evidence(doc: dict[str, Any]) -> str:
    rows = []
    for evidence in doc.get("evidence", []) or []:
        if not isinstance(evidence, dict):
            continue
        source = evidence.get("source") or evidence.get("reference") or evidence.get("url") or ""
        summary = evidence.get("summary") or evidence.get("snippet") or evidence.get("description") or ""
        rows.append(f"{source}: {summary}".strip(": "))
    return " | ".join(rows)


def summarize_conditions(doc: dict[str, Any]) -> str:
    keys = [
        "ph_value",
        "ph_range",
        "temperature_value",
        "temperature_range",
        "salinity",
        "aeration",
        "incubation_atmosphere",
        "culture_vessel",
        "light_intensity",
        "light_cycle",
        "light_quality",
    ]
    return "; ".join(f"{key}={doc[key]}" for key in keys if doc.get(key) not in (None, ""))


def template_vars(doc: dict[str, Any], media_file: Path) -> dict[str, str]:
    media_term = doc.get("media_term")
    media_path = media_file.resolve()
    return {
        "record_path": str(media_path.relative_to(REPO_ROOT)),
        "media_id": str(doc.get("id", "")),
        "media_name": str(doc.get("name", media_file.stem)),
        "original_name": str(doc.get("original_name", "")),
        "category": str(doc.get("category", media_file.parent.name)),
        "medium_type": str(doc.get("medium_type", "")),
        # The three axes that supersede medium_type. Shown alongside it rather
        # than instead of it: most records still carry only the deprecated slot.
        "composition_type": str(doc.get("composition_type", "")),
        "nutritional_class": str(doc.get("nutritional_class", "")),
        "functional_role": _join_values(doc.get("functional_role")),
        "physical_state": str(doc.get("physical_state", "")),
        "media_term": _name_with_id(media_term) if media_term else "",
        "conditions": summarize_conditions(doc),
        "applications": _join_values(doc.get("applications")),
        "synonyms": _join_values(doc.get("synonyms")),
        "ingredients": summarize_ingredients(doc),
        "solutions": summarize_solutions(doc),
        "target_organisms": summarize_target_organisms(doc),
        "variants": summarize_variants(doc),
        "variant_records": summarize_variant_records(doc),
        "evidence": summarize_evidence(doc),
        "notes": str(doc.get("notes", "")),
    }


def provider_args(provider: str) -> list[str]:
    """Mirror DisMech's cborg shortcut while allowing named providers such as falcon."""
    if provider == "cborg":
        return ["--use-cborg"]
    return ["--provider", provider]


def research_env(provider: str) -> dict[str, str]:
    """Build subprocess environment, including a FutureHouse Falcon key alias."""
    env = os.environ.copy()
    if provider == "falcon" and not env.get("EDISON_API_KEY") and env.get("FUTUREHOUSE_API_KEY"):
        env["EDISON_API_KEY"] = env["FUTUREHOUSE_API_KEY"]
    return env


def build_command(
    *,
    provider: str,
    template: Path,
    output_file: Path,
    citations_file: Path,
    variables: dict[str, str],
    passthrough_args: list[str],
    client_command: str = "deep-research-client",
) -> list[str]:
    command = [
        client_command,
        "research",
        "--template",
        str(template),
    ]
    for key, value in variables.items():
        command.extend(["--var", f"{key}={value}"])
    command.extend(provider_args(provider))
    command.extend(
        [
            "--output",
            str(output_file),
            "--separate-citations",
            str(citations_file),
        ]
    )
    command.extend(passthrough_args)
    return command


def build_provider_command(
    *,
    provider: str | None,
    client_command: str = "deep-research-client",
) -> list[str]:
    command = [client_command, "providers"]
    if provider:
        command.extend(["--provider", provider])
    return command


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--provider", help="deep-research-client provider, e.g. falcon")
    parser.add_argument("--target", help="Media YAML path, slug, ID, or name")
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument("--research-dir", type=Path, default=DEFAULT_RESEARCH_DIR)
    parser.add_argument("--client-command", default="deep-research-client")
    parser.add_argument("--list-providers", action="store_true")
    parser.add_argument("--provider-info", action="store_true")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the deep-research-client command without running it.",
    )
    parser.add_argument("passthrough_args", nargs=argparse.REMAINDER)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    if args.list_providers or args.provider_info:
        command = build_provider_command(
            provider=args.provider if args.provider_info else None,
            client_command=args.client_command,
        )
        subprocess.run(command, check=True, env=research_env(args.provider or ""))
        return 0

    if not args.provider:
        raise ValueError("--provider is required for media research")
    if not args.target:
        raise ValueError("--target is required for media research")

    media_file = resolve_media_file(args.target)
    doc = load_media(media_file)
    category_slug = str(doc.get("category") or media_file.parent.name).lower()
    media_slug = media_file.stem

    output_dir = args.research_dir / "media" / category_slug
    output_file = output_dir / f"{media_slug}-deep-research-{args.provider}.md"
    citations_file = output_file.with_suffix(output_file.suffix + ".citations.md")
    variables = template_vars(doc, media_file)
    command = build_command(
        provider=args.provider,
        template=args.template,
        output_file=output_file,
        citations_file=citations_file,
        variables=variables,
        passthrough_args=args.passthrough_args,
        client_command=args.client_command,
    )

    print(f"Researching: {variables['media_name']} ({args.provider}) -> {output_file}")
    print(f"Citations: {citations_file}")
    if args.dry_run:
        print(shlex.join(command))
        return 0

    output_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run(command, check=True, env=research_env(args.provider))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
