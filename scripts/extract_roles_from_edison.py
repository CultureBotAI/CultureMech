#!/usr/bin/env python3
"""Extract structured role assignments from Edison role-research outputs.

Consumes Edison / DRC role-research bundles produced by the Step 7b
literature lane — specifically the `role_research:` fenced YAML block in
`research/ingredients/roles/*-edison-literature.md` (or equivalent DRC
outputs) — and emits two batch JSON files:

  --out-mim → the "rich" shape consumed by MIM's `apply_role_research_results.py`:
    {"proposals": [{
       "ingredient_identifier": "CHEBI:17561",
       "ingredient_path": "data/ingredients/mapped/L-cysteine.yaml",
       "source_run": "L-cysteine-edison-literature",
       "role_assignments": {
         "nutritional_roles": [{role, confidence, evidence, ...}],
         "physicochemical_roles": [...],
         "cellular_metabolic_roles": [...]},
     }, ...]}

  --out-cm → the scalar-projection shape consumed by CultureMech's
  forthcoming `apply_ingredient_roles` (PR5). Same shape as MIM but with an
  extra `roles` block flattened to per-facet role-token lists (evidence
  intentionally not projected — CultureMech's IngredientDescriptor carries
  scalar role tokens, evidence stays on the MIM record).

DOI / PMID cross-referencing:

  When a `-citations.md` sidecar exists next to the response file (Edison
  writes one automatically), any citation entry in a role's `evidence:` list
  whose `doi:` or `pmid:` matches a sidecar entry gets its `reference_text:`
  filled in from the sidecar. This lets the Edison model report just a DOI
  without hand-typing the citation string; the extractor upgrades the
  evidence entry with the sidecar's authoritative rendering.

Usage:

    just extract-roles-from-edison ../MediaIngredientMech/research/ingredients/roles
    # → out-mim: reports/edison_role_batch_mim.json
    # → out-cm:  reports/edison_role_batch_cm.json

    # Single file:
    uv run python scripts/extract_roles_from_edison.py \\
      ../MediaIngredientMech/research/ingredients/roles/L-cysteine-edison-literature.md \\
      --out-mim /tmp/mim.json --out-cm /tmp/cm.json

Follows the "never fabricate" rule from the plan: an ingredient whose
Edison output has no parseable `role_research:` block is skipped and
recorded in `--skipped-report`; a role whose token is not in the facet's
enum permissible values (typo, hallucination, wrong facet) is dropped and
logged. The applier repeats the enum check as a defense-in-depth.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUT_MIM = REPO_ROOT / "data" / "import_tracking" / "reports" / "edison_role_batch_mim.json"
DEFAULT_OUT_CM = REPO_ROOT / "data" / "import_tracking" / "reports" / "edison_role_batch_cm.json"
DEFAULT_MIM_ROLES_SCHEMA = REPO_ROOT / "src" / "culturemech" / "schema" / "mim_roles.yaml"

FACET_SLOTS = ("nutritional_roles", "physicochemical_roles", "cellular_metabolic_roles")

# Map facet slot name → enum class name in mim_roles.yaml.
_FACET_ENUM_NAMES = {
    "nutritional_roles": "NutritionalRoleEnum",
    "physicochemical_roles": "PhysicochemicalRoleEnum",
    "cellular_metabolic_roles": "CellularMetabolicRoleEnum",
}


def load_facet_enums(schema_path: Path = DEFAULT_MIM_ROLES_SCHEMA) -> dict[str, frozenset[str]]:
    """Load {facet_slot: frozenset(permissible_values)} from the vendored mim_roles schema.

    Single source of truth: read enum permissible values from mim_roles.yaml (whose
    sha is pinned in project.justfile:verify-schema-pin). No hand-typed token lists.
    """
    if not schema_path.is_file():
        raise SystemExit(f"mim_roles schema not found at {schema_path}")
    doc = yaml.safe_load(schema_path.read_text()) or {}
    enums = (doc.get("enums") or {}) if isinstance(doc, dict) else {}
    result: dict[str, frozenset[str]] = {}
    for slot, enum_name in _FACET_ENUM_NAMES.items():
        pv = ((enums.get(enum_name) or {}).get("permissible_values") or {})
        if not isinstance(pv, dict) or not pv:
            raise SystemExit(f"{enum_name}.permissible_values missing or empty in {schema_path}")
        result[slot] = frozenset(pv.keys())
    return result

# Regex catches ```yaml … ``` blocks; case-insensitive on the language tag.
_YAML_FENCE_RE = re.compile(r"```(?:yaml|yml)\s*\n(.*?)\n```", re.DOTALL | re.IGNORECASE)

# DOI / PMID regexes for sidecar cross-reference.
_DOI_RE = re.compile(r"10\.\d{4,9}/[-._;()/:A-Za-z0-9]+", re.IGNORECASE)
_PMID_RE = re.compile(r"\bPMID[:\s]+([0-9]{4,10})\b", re.IGNORECASE)


class ExtractionError(Exception):
    """Raised for structural problems in an Edison bundle."""


def find_role_yaml_block(md_text: str) -> dict[str, Any] | None:
    """Return the parsed `role_research:` dict from the last matching fenced block.

    The template's own example lives in an early fence — the model's actual
    answer is later in the file, so LAST wins. Skips blocks that don't have
    `role_research:` at their top level; returns None if nothing matches.
    """
    matches = list(_YAML_FENCE_RE.finditer(md_text))
    for m in reversed(matches):
        block = m.group(1)
        try:
            parsed = yaml.safe_load(block)
        except yaml.YAMLError:
            continue
        if isinstance(parsed, dict) and "role_research" in parsed:
            rr = parsed["role_research"]
            if isinstance(rr, dict):
                return rr
    return None


def _load_meta_sidecar(response_md: Path) -> dict[str, Any]:
    """Load the `-meta.yaml` sidecar if present. Returns {} on any failure."""
    meta_path = response_md.with_name(response_md.stem + "-meta.yaml")
    # `.stem` on `X-literature.md` is `X-literature` — but meta is written as
    # `X-literature-meta.yaml` regardless of the .md suffix pattern used by
    # deep-research vs edison. Try both conventions.
    candidates = [
        response_md.with_name(response_md.stem + "-meta.yaml"),
        response_md.parent / f"{response_md.stem}-meta.yaml",
    ]
    for c in candidates:
        if c.is_file():
            try:
                doc = yaml.safe_load(c.read_text()) or {}
                if isinstance(doc, dict):
                    return doc
            except yaml.YAMLError:
                continue
    return {}


def _parse_citations_sidecar(sidecar: Path) -> dict[str, str]:
    """Parse the `-citations.md` sidecar into {normalized_doi_or_pmid: full_citation_line}.

    Each bullet in a citations sidecar looks like:
        - **1.** (foo pages 1-5): Author et al. Title. Journal, 2020. URL: ..., doi:10.xxxx/yyy...
    We index each line by every DOI/PMID we can extract from it, so a lookup
    by DOI can retrieve the rendered author-title-journal string.
    """
    if not sidecar.is_file():
        return {}
    lookup: dict[str, str] = {}
    for raw in sidecar.read_text().splitlines():
        line = raw.strip()
        if not line.startswith("- "):
            continue
        # Strip leading list markers/bolds for a clean citation text.
        text = re.sub(r"^\-\s+(\*\*\d+\.\*\*\s*)?(\([^)]+\):\s*)?", "", line).strip()
        for doi in _DOI_RE.findall(text):
            lookup.setdefault(doi.lower().rstrip(").,;"), text)
        for pmid in _PMID_RE.findall(text):
            lookup.setdefault(f"PMID:{pmid}", text)
    return lookup


def _upgrade_evidence(evidence: list[dict[str, Any]], citations_lookup: dict[str, str]) -> list[dict[str, Any]]:
    """Fill in `reference_text` from the sidecar when we can match on DOI/PMID."""
    upgraded: list[dict[str, Any]] = []
    for ev in evidence:
        if not isinstance(ev, dict):
            continue
        entry = dict(ev)
        if not entry.get("reference_text"):
            key = None
            if entry.get("doi"):
                key = str(entry["doi"]).lower().rstrip(").,;")
            elif entry.get("pmid"):
                key = f"PMID:{entry['pmid']}"
            if key and key in citations_lookup:
                entry["reference_text"] = citations_lookup[key]
        upgraded.append(entry)
    return upgraded


def _shape_role_entry(role_entry: Any) -> dict[str, Any] | None:
    """Coerce one role-list entry into {role, confidence, metabolic_context?, evidence[]}."""
    if isinstance(role_entry, str):
        return {"role": role_entry.strip(), "confidence": 0.7, "evidence": []}
    if not isinstance(role_entry, dict):
        return None
    role = role_entry.get("role")
    if not role or not isinstance(role, str):
        return None
    out: dict[str, Any] = {
        "role": role.strip(),
        "confidence": float(role_entry.get("confidence", 0.7)),
        "evidence": [],
    }
    if role_entry.get("metabolic_context"):
        out["metabolic_context"] = str(role_entry["metabolic_context"])
    evidence = role_entry.get("evidence") or []
    if isinstance(evidence, list):
        out["evidence"] = [ev for ev in evidence if isinstance(ev, dict)]
    return out


def _mim_relative_source_run(response_md: Path, mim_repo: Path | None) -> str:
    """Return the MIM-repo-relative path of the response file if inside `mim_repo`;
    otherwise return just the filename stem (backwards-compatible fallback)."""
    if mim_repo is not None:
        try:
            return str(response_md.resolve().relative_to(mim_repo.resolve()))
        except ValueError:
            pass
    return response_md.stem


def extract_one(
    response_md: Path,
    valid_tokens: dict[str, frozenset[str]] | None = None,
    mim_repo: Path | None = None,
    validation_errors: list[dict[str, Any]] | None = None,
) -> dict[str, Any] | None:
    """Parse one Edison response .md into a proposal dict, or None if unparseable.

    When `valid_tokens` is provided (a `{facet: frozenset(...)}` map from
    `load_facet_enums()`), each role token is validated against its facet's
    permissible values. Invalid or wrong-facet tokens are DROPPED from the
    proposal and appended to `validation_errors` (if given) as
    `{source_file, facet, role, reason, correct_facet?}` records.
    """
    md_text = response_md.read_text()
    rr = find_role_yaml_block(md_text)
    if rr is None:
        return None

    meta = _load_meta_sidecar(response_md)
    citations_lookup = _parse_citations_sidecar(
        response_md.with_name(response_md.stem + "-citations.md")
    )

    slug = rr.get("ingredient") or meta.get("slug") or response_md.stem.rsplit("-edison-", 1)[0]
    ingredient_identifier = (
        rr.get("ingredient_identifier")
        or meta.get("ingredient_id")
        or (meta.get("template_vars") or {}).get("ingredient_identifier")
    )
    ingredient_path = meta.get("ingredient_path")

    role_assignments: dict[str, list[dict[str, Any]]] = {}
    for slot in FACET_SLOTS:
        entries = rr.get(slot) or []
        if not isinstance(entries, list):
            continue
        shaped: list[dict[str, Any]] = []
        for entry in entries:
            s = _shape_role_entry(entry)
            if s is None:
                continue
            token = s["role"]

            # Token validation against the facet's enum permissible values.
            if valid_tokens is not None:
                if token in valid_tokens[slot]:
                    pass  # canonical, keep
                else:
                    # Check whether it belongs to a DIFFERENT facet (misfiling).
                    other_facet = next(
                        (other for other, allowed in valid_tokens.items()
                         if other != slot and token in allowed),
                        None,
                    )
                    if validation_errors is not None:
                        record: dict[str, Any] = {
                            "source_file": str(response_md),
                            "facet": slot,
                            "role": token,
                            "reason": "wrong_facet" if other_facet else "unknown_token",
                        }
                        if other_facet:
                            record["correct_facet"] = other_facet
                        validation_errors.append(record)
                    continue  # drop the entry either way

            s["evidence"] = _upgrade_evidence(s["evidence"], citations_lookup)
            # metabolic_context is only schema-legal on cellular_metabolic; drop elsewhere.
            if slot != "cellular_metabolic_roles":
                s.pop("metabolic_context", None)
            shaped.append(s)
        if shaped:
            role_assignments[slot] = shaped

    if not role_assignments:
        return None

    proposal: dict[str, Any] = {
        "ingredient_slug": slug,
        "source_run": _mim_relative_source_run(response_md, mim_repo),
        "role_assignments": role_assignments,
    }
    if ingredient_identifier:
        proposal["ingredient_identifier"] = ingredient_identifier
    if ingredient_path:
        proposal["ingredient_path"] = ingredient_path
    # `warnings:` from the YAML block are human-only per the applier contract —
    # they never appear in the emitted batch. If a --warnings-report is passed
    # at the CLI layer, warnings are surfaced there instead.
    return proposal


def _to_cm_shape(mim_proposal: dict[str, Any]) -> dict[str, Any]:
    """Project a rich MIM proposal to the scalar CultureMech shape."""
    ra = mim_proposal.get("role_assignments") or {}
    roles: dict[str, list[str]] = {}
    for slot in FACET_SLOTS:
        tokens = [entry.get("role") for entry in ra.get(slot, []) if entry.get("role")]
        if tokens:
            roles[slot] = tokens
    cm: dict[str, Any] = {
        "ingredient_slug": mim_proposal.get("ingredient_slug"),
        "source_run": mim_proposal.get("source_run"),
        "roles": roles,
    }
    if mim_proposal.get("ingredient_identifier"):
        cm["ingredient_identifier"] = mim_proposal["ingredient_identifier"]
    return cm


def discover_inputs(inputs: list[Path]) -> list[Path]:
    """Expand any directory in `inputs` to all *-edison-literature.md files inside."""
    out: list[Path] = []
    for p in inputs:
        if p.is_dir():
            out.extend(sorted(p.glob("*-edison-literature.md")))
            out.extend(sorted(p.glob("*-deep-research-*.md")))
        elif p.is_file():
            out.append(p)
    # Dedup while preserving order.
    seen: set[Path] = set()
    uniq: list[Path] = []
    for p in out:
        if p not in seen:
            seen.add(p)
            uniq.append(p)
    return uniq


def _collect_warnings(response_md: Path) -> list[str]:
    """Return the human-only `warnings:` list from a response.md, if any."""
    rr = find_role_yaml_block(response_md.read_text())
    if not isinstance(rr, dict):
        return []
    w = rr.get("warnings") or []
    if isinstance(w, list):
        return [str(x) for x in w]
    return [str(w)]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", type=Path, nargs="+",
                        help="One or more files or directories of *-edison-literature.md outputs.")
    parser.add_argument("--out-mim", type=Path, default=DEFAULT_OUT_MIM,
                        help="Output path for the rich MIM applier batch.")
    parser.add_argument("--out-cm", type=Path, default=DEFAULT_OUT_CM,
                        help="Output path for the scalar CultureMech applier batch.")
    parser.add_argument("--mim-repo", type=Path, default=REPO_ROOT.parent / "MediaIngredientMech",
                        help="MediaIngredientMech checkout root. Used to render `source_run` as a "
                             "MIM-repo-relative path per the applier contract.")
    parser.add_argument("--schema", type=Path, default=DEFAULT_MIM_ROLES_SCHEMA,
                        help="mim_roles.yaml with the three facet enums (source of truth for token validation).")
    parser.add_argument("--no-validate", action="store_true",
                        help="Skip token-vs-enum validation. Emits every role token unchanged. "
                             "Default: validate; drop invalid tokens; surface them in --validation-report.")
    parser.add_argument("--skipped-report", type=Path, default=None,
                        help="Optional path to write a report of files skipped with reasons.")
    parser.add_argument("--validation-report", type=Path, default=None,
                        help="Optional path to write invalid/wrong-facet token records "
                             "and the human-only `warnings:` blocks that never enter the batch.")
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args(argv)

    input_files = discover_inputs(args.inputs)
    if not input_files:
        print("No input files found. Pass a file or directory.", file=sys.stderr)
        return 2

    valid_tokens = None if args.no_validate else load_facet_enums(args.schema)
    mim_repo = args.mim_repo if args.mim_repo.is_dir() else None

    proposals: list[dict[str, Any]] = []
    skipped: list[tuple[Path, str]] = []
    validation_errors: list[dict[str, Any]] = []
    warnings_by_file: dict[str, list[str]] = {}

    for f in input_files:
        try:
            proposal = extract_one(f, valid_tokens=valid_tokens, mim_repo=mim_repo,
                                   validation_errors=validation_errors)
        except Exception as exc:
            skipped.append((f, f"error: {exc}"))
            continue
        if proposal is None:
            skipped.append((f, "no `role_research:` fenced YAML block or no valid role tokens"))
            continue
        proposals.append(proposal)
        # Collect human-only warnings for the validation report (never enter the batch).
        ws = _collect_warnings(f)
        if ws:
            warnings_by_file[str(f)] = ws
        if args.verbose:
            print(f"OK  {f.name}  → {sum(len(v) for v in proposal['role_assignments'].values())} roles")

    args.out_mim.parent.mkdir(parents=True, exist_ok=True)
    args.out_cm.parent.mkdir(parents=True, exist_ok=True)
    args.out_mim.write_text(json.dumps({"proposals": proposals}, indent=2))
    args.out_cm.write_text(json.dumps({"proposals": [_to_cm_shape(p) for p in proposals]}, indent=2))

    if args.skipped_report and skipped:
        lines = ["# Skipped Edison role-research files\n"]
        for f, reason in skipped:
            lines.append(f"- `{f}` — {reason}")
        args.skipped_report.write_text("\n".join(lines))

    if args.validation_report and (validation_errors or warnings_by_file):
        lines = ["# Extraction validation report\n"]
        if validation_errors:
            lines.append(f"## Rejected role tokens ({len(validation_errors)})\n")
            for err in validation_errors:
                corr = f" — belongs in `{err['correct_facet']}`" if err.get("correct_facet") else ""
                lines.append(f"- `{err['role']}` in `{err['facet']}` ({err['reason']}){corr}")
                lines.append(f"    source: `{err['source_file']}`")
        if warnings_by_file:
            lines.append(f"\n## Curator warnings ({sum(len(v) for v in warnings_by_file.values())})\n")
            for fpath, ws in warnings_by_file.items():
                lines.append(f"### `{fpath}`")
                for w in ws:
                    lines.append(f"- {w}")
        args.validation_report.write_text("\n".join(lines))

    print(f"Scanned {len(input_files)} input file(s)")
    print(f"Parsed {len(proposals)} proposal(s) → {args.out_mim}")
    print(f"                             → {args.out_cm}")
    if skipped:
        print(f"Skipped {len(skipped)} file(s){' (see report)' if args.skipped_report else ''}")
    if validation_errors:
        print(f"Rejected {len(validation_errors)} role token(s)"
              f"{' (see validation report)' if args.validation_report else ''}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
