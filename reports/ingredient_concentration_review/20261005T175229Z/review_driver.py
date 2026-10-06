"""Read-only inventory; structural evidence candidates are NEVER source verification."""
import argparse
import collections
import csv
import datetime
import gzip
import hashlib
import json
import re
import subprocess
import sys
from decimal import Decimal, InvalidOperation
from pathlib import Path

ROOT = Path.cwd()
sys.path.insert(0, str(ROOT / "scripts"))
import yaml
from audit_concentration_plausibility import check_ingredient
from record_kinds import has_solution_shape, is_solution_record

SCHEMA = yaml.load((ROOT / "src/culturemech/schema/culturemech.yaml").read_text(), Loader=yaml.CSafeLoader)
UNITS = set(SCHEMA["enums"]["ConcentrationUnitEnum"]["permissible_values"])
URL = re.compile(r"https?://[^\s<>\"']+|doi:10\.\d{4,9}/[^\s<>\"']+|PMID:\d+", re.I)
DOI = re.compile(r"^(?:doi:|https?://(?:dx\.)?doi\.org/)?10\.\d{4,9}/\S+$", re.I)


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def refs_in(value):
    if isinstance(value, str):
        return sorted(set(x.rstrip(".,;)") for x in URL.findall(value)))
    if isinstance(value, dict):
        value = list(value.values())
    if isinstance(value, list):
        return sorted({ref for child in value for ref in refs_in(child)})
    return []


def reference_shape(ref):
    if not isinstance(ref, str):
        return False
    return bool(DOI.fullmatch(ref.strip()) or re.match(r"^https?://[^/\s]+/\S+", ref.strip()))


def evidence_list(value):
    return [e for e in value if isinstance(e, dict)] if isinstance(value, list) else []


def candidate(e):
    return (reference_shape(e.get("reference")) and e.get("supports") == "SUPPORT"
            and bool(str(e.get("snippet") or "").strip())
            and bool(str(e.get("explanation") or "").strip()))


def concentration_checks(node):
    if "concentration" not in node or node["concentration"] is None:
        return ["MISSING_CONCENTRATION"]
    c = node["concentration"]
    if not isinstance(c, dict):
        return ["MALFORMED_CONCENTRATION"]
    flags = []
    value = c.get("value")
    unit = c.get("unit")
    if value is None or str(value).strip() == "":
        flags.append("MISSING_VALUE")
    elif not isinstance(value, str):
        flags.append("VALUE_NOT_STRING")
    if unit not in UNITS:
        flags.append("INVALID_OR_MISSING_UNIT")
    try:
        n = Decimal(str(value))
        if not n.is_finite():
            flags.append("NONFINITE_VALUE")
        elif n < 0:
            flags.append("NEGATIVE_VALUE")
    except InvalidOperation:
        if unit != "VARIABLE":
            flags.append("RANGE_OR_NONNUMERIC_REQUIRES_SOURCE")
    if unit == "VARIABLE":
        flags.append("VARIABLE_REQUIRES_SOURCE")
    basis = str(c.get("per_volume") or "").lower().strip()
    if basis and unit in {"G_PER_L", "MG_PER_L", "MICROG_PER_L", "ML_PER_L"}:
        match = re.fullmatch(r"(?:per\s+)?([\d.]+)\s*(ml|l|liters?|litres?)", basis)
        if match:
            volume = Decimal(match[1]) / (1000 if match[2] == "ml" else 1)
            if volume != 1:
                flags.append("PER_L_UNIT_WITH_DIFFERENT_VOLUME_BASIS")
    return flags


def collect_claims(doc):
    claims = []
    record_evidence = evidence_list(doc.get("evidence"))
    source_data = doc.get("source_data")
    if isinstance(source_data, dict):
        record_evidence += evidence_list(source_data.get("evidence"))

    def claim(node, path, kind, inherited):
        local = evidence_list(node.get("evidence"))
        name = str(node.get("preferred_term") or node.get("name") or "UNNAMED")
        field = path + ".concentration" if path else "concentration"
        scoped = [e for e in inherited if field in str(e.get("explanation") or "")]
        attached = local + scoped
        flags = concentration_checks(node)
        if kind == "variant_text":
            flags = ["VARIANT_TEXT_REQUIRES_SOURCE_REVIEW"]
        if kind == "ingredient" and path.startswith("ingredients[") and not is_solution_record(doc):
            if isinstance(node.get("concentration"), dict):
                hit = check_ingredient(node)
                if hit:
                    flags.append("PLAUSIBILITY_" + hit[0])
        if node.get("concentration_candidates"):
            flags.append("UNASSERTED_CANDIDATES_NOT_PROMOTED")
        state = "missing_attached_evidence"
        if attached:
            state = "candidate_needs_source_verification" if any(candidate(e) for e in attached) else "incomplete_or_nonqualifying_attached_evidence"
        elif inherited:
            state = "unscoped_context_evidence_needs_review"
        if kind == "variant_text":
            field = path + ".modifications"
        claims.append({
            "field": field, "kind": kind, "ingredient": name,
            "identity": {k: node[k] for k in ("term", "chebi_term", "culturemech_term", "mediaingredientmech_chebi_term") if k in node},
            "old": node.get("concentration"), "notes": node.get("notes"),
            "modifications": node.get("modifications") if kind == "variant_text" else None,
            "candidates": node.get("concentration_candidates"), "flags": flags,
            "evidence_state": state, "attached_evidence": attached,
            "proposed": None, "status": "unsupported", "source_check": "not_performed",
        })

    def visit(container, path, inherited, ancestors):
        if id(container) in ancestors:
            claims.append({"field": path, "ingredient": "CYCLIC_YAML", "kind": "error", "old": None,
                           "flags": ["CYCLIC_YAML"], "status": "unsupported", "source_check": "not_performed",
                           "evidence_state": "unresolved", "attached_evidence": []})
            return
        ancestors = ancestors | {id(container)}
        for key in ("ingredients", "composition", "solutions"):
            items = container.get(key) or []
            if not isinstance(items, list):
                continue
            for i, node in enumerate(items):
                if not isinstance(node, dict):
                    continue
                p = f"{path}.{key}[{i}]" if path else f"{key}[{i}]"
                claim(node, p, "stock_addition" if key == "solutions" else "ingredient", inherited)
                visit(node, p, inherited + evidence_list(node.get("evidence")), ancestors)
        for i, node in enumerate(container.get("variants") or []):
            if isinstance(node, dict):
                p = f"{path}.variants[{i}]" if path else f"variants[{i}]"
                claim(node, p, "variant_text", inherited)
                visit(node, p, inherited + evidence_list(node.get("evidence")), ancestors)

    visit(doc, "", record_evidence, set())
    if "concentration" in doc:
        claim(doc, "", "standalone_working_dose", record_evidence)
    return claims, record_evidence


def self_test():
    assert concentration_checks({"concentration": {"value": "0", "unit": "G_PER_L"}}) == []
    assert concentration_checks({}) == ["MISSING_CONCENTRATION"]
    assert "NEGATIVE_VALUE" in concentration_checks({"concentration": {"value": "-1", "unit": "G_PER_L"}})
    e = {"reference": "https://example.org/recipe", "supports": "SUPPORT", "snippet": "amount", "explanation": "context"}
    assert candidate(e) and not candidate({**e, "reference": "PMID:123"})
    claims, _ = collect_claims({"ingredients": [{"preferred_term": "test", "evidence": [e]}]})
    assert claims[0]["status"] == "unsupported" and claims[0]["source_check"] == "not_performed"
    nested = {"solutions": [{"preferred_term": "stock", "composition": [{"preferred_term": "solute"}]}]}
    assert [r["field"] for r in collect_claims(nested)[0]] == ["solutions[0].concentration", "solutions[0].composition[0].concentration"]
    print("inventory self-checks passed", flush=True)


def scan(out):
    self_test()
    paths = subprocess.check_output(["git", "ls-files", "-z", "--", "data/normalized_yaml", "data/merge_yaml/merged"], text=True).split("\0")
    paths = sorted(p for p in paths if p.endswith(".yaml"))
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    meta = {"started_utc": utc(), "commit": commit, "records": len(paths), "scope": "all tracked normalized and merged YAML paths in this checkout", "upstream_main_observed": "70a34fef7032a8c024fa2bbf721156d94f19f3c0", "record_edits": 0}
    out.mkdir(parents=True, exist_ok=True)
    output = out / "inventory.jsonl"
    if output.exists():
        raise SystemExit("Refusing to overwrite an existing inventory")
    counter = collections.Counter()
    source_groups = collections.Counter()
    with output.open("x") as handle:
        for i, p in enumerate(paths, 1):
            raw = (ROOT / p).read_bytes()
            row = {"path": p, "layer": "normalized" if "/normalized_yaml/" in p else "merged", "sha256": hashlib.sha256(raw).hexdigest()}
            try:
                doc = yaml.load(raw.decode("utf-8"), Loader=yaml.CSafeLoader)
                if not isinstance(doc, dict):
                    raise ValueError("record is not a YAML mapping")
                claims, evidence = collect_claims(doc)
                row.update({"id": doc.get("id"), "name": doc.get("name") or doc.get("preferred_term"),
                            "category": doc.get("category"), "record_kind": "SOLUTION" if is_solution_record(doc) else "MEDIUM",
                            "target_class": "SolutionRecipe" if has_solution_shape(doc) else "MediaRecipe",
                            "claims": claims, "context_evidence": evidence, "merged_from": doc.get("merged_from") or [],
                            "references": doc.get("references") or [], "sources": doc.get("sources") or [],
                            "media_term": doc.get("media_term"), "source_notes": doc.get("notes"),
                            "source_data": doc.get("source_data"), "parse_error": None})
                row["source_leads"] = refs_in([row[k] for k in ("references", "sources", "media_term", "source_notes", "source_data")])
                for c in claims:
                    counter[row["layer"] + "/claims"] += c["kind"] != "variant_text"
                    counter[row["layer"] + "/" + c["evidence_state"]] += 1
                for source in row["source_leads"]:
                    source_groups[source] += 1
            except Exception as exc:
                row.update({"parse_error": f"{type(exc).__name__}: {exc}", "claims": [], "source_leads": []})
                counter["parse_failures"] += 1
            handle.write(json.dumps(row, ensure_ascii=False, default=str) + "\n")
            counter[row["layer"] + "/records"] += 1
            if i % 1000 == 0:
                print(f"inventoried {i}/{len(paths)}", flush=True)
    meta.update({"finished_inventory_utc": utc(), "counts": dict(counter)})
    (out / "run.json").write_text(json.dumps(meta, indent=2) + "\n")
    (out / "source_queue.json").write_text(json.dumps(source_groups.most_common(), indent=2) + "\n")
    print(json.dumps(meta, indent=2), flush=True)


def esc(x):
    if x is None or x == "":
        return "unknown"
    if isinstance(x, (list, dict)):
        x = json.dumps(x, ensure_ascii=False, default=str)
    return str(x).replace("|", "\\|").replace("\n", "<br>").replace("\r", "")


def render(out):
    meta = json.loads((out / "run.json").read_text())
    overrides = json.loads((out / "source_checks.json").read_text()) if (out / "source_checks.json").exists() else []
    checked = {(c["path"], c["field"]): c for c in overrides}
    failed_refs = set(json.loads((out / "unavailable_references.json").read_text())) if (out / "unavailable_references.json").exists() else set()
    def inspected(c):
        return c["source_check"].startswith("inspected_")
    errors = collections.defaultdict(list)
    validation_file = out / "strict_validation.tsv"
    if validation_file.exists():
        for row in csv.DictReader(validation_file.open(), delimiter="\t"):
            p = row["file"]
            if p.startswith(str(ROOT) + "/"):
                p = p[len(str(ROOT)) + 1:]
            errors[p].append(row)
    validation_complete = (out / "validation_complete.json").exists()
    counts = collections.defaultdict(collections.Counter)
    records = []
    inventory_path = out / "inventory.jsonl"
    source_file = inventory_path.open() if inventory_path.exists() else gzip.open(out / "inventory.jsonl.gz", "rt")
    with source_file as source:
        for line in source:
            r = json.loads(line)
            records.append(r)
    by_id = collections.defaultdict(list)
    by_name = collections.defaultdict(list)
    for r in records:
        if r["layer"] == "normalized":
            by_id[r.get("id")].append(r["path"])
            by_name[r.get("name")].append(r["path"])
    with (out / "manifest.tsv").open("w", newline="") as mf, (out / "claims.tsv").open("w", newline="") as cf:
        mw = csv.DictWriter(mf, fieldnames=["record", "id", "layer", "kind", "sha256", "claims", "source_checked_claims", "pending_claims", "schema_errors", "report"], delimiter="\t", lineterminator="\n")
        cw = csv.DictWriter(cf, fieldnames=["record", "id", "layer", "field", "ingredient", "kind", "old", "flags", "evidence_state", "status", "source_check", "proposed", "reference", "snippet", "locator", "calculation"], delimiter="\t", lineterminator="\n")
        mw.writeheader(); cw.writeheader()
        for r in records:
            claims = r["claims"]
            for c in claims:
                change = checked.get((r["path"], c["field"]))
                if change:
                    if change["expected_old"] != c.get("old"):
                        raise ValueError("Source check old-value precondition failed: " + r["path"] + c["field"])
                    c.update({k: v for k, v in change.items() if k not in {"path", "expected_old"}})
                elif c["attached_evidence"] and all(str(e.get("reference", "")).lower() in failed_refs for e in c["attached_evidence"]):
                    c["source_check"] = "retrieval_failed; exact quote and concentration not verified"
                cc = counts[r["layer"]]
                cc["claim_rows"] += 1
                cc["structured_concentration_entries"] += c["kind"] not in {"variant_text", "error"}
                cc["variant_context_rows"] += c["kind"] == "variant_text"
                cc[c["evidence_state"]] += 1
                cc[c["status"]] += 1
                cc["source_checked_claims"] += inspected(c)
                cc["source_retrieval_failed_claims"] += c["source_check"].startswith("retrieval_failed")
                for flag in c["flags"]:
                    cc[flag] += 1
                cw.writerow({k: (json.dumps(v, ensure_ascii=False, default=str) if isinstance(v, (dict, list)) else v) for k, v in {
                    "record": r["path"], "id": r.get("id"), "layer": r["layer"],
                    **{k: c.get(k, "") for k in cw.fieldnames if k not in {"record", "id", "layer"}}
                }.items()})
            cc = counts[r["layer"]]
            cc["records"] += 1
            cc["records_without_claim_rows"] += not claims
            cc["parse_errors"] += bool(r.get("parse_error"))
            checked_count = sum(inspected(c) for c in claims)
            cc["records_with_any_source_check"] += checked_count > 0
            cc["records_with_all_claims_source_checked"] += bool(claims) and checked_count == len(claims)
            cc["schema_error_records"] += bool(errors[r["path"]])
            report = Path("records") / Path(r["path"]).relative_to("data").with_suffix(".md")
            report_path = out / report
            report_path.parent.mkdir(parents=True, exist_ok=True)
            owners = set(by_id.get(r.get("id"), [])) if r["layer"] == "merged" else {r["path"]}
            for name in r.get("merged_from", []):
                owners.update(by_name.get(name, []))
            validation = f"{len(errors[r['path']])} closed-schema errors" if validation_complete else "Closed-schema validation not yet finalized"
            text = ["# Ingredient Concentration Review", "", f"- Record: {r['path']}", f"- ID: {r.get('id', 'unknown')}",
                    f"- Reviewed commit: {meta['commit']}", f"- Record SHA256: {r['sha256']}", f"- Layer: {r['layer']}",
                    f"- Record kind: {r.get('record_kind', 'unknown')}", "- Mode: read-only; no recipe edits",
                    f"- Source-checked claim rows: {checked_count}/{len(claims)}",
                    "- Verdict: source review incomplete" if checked_count < len(claims) or not claims or any(c["status"] == "unsupported" for c in claims) else "- Verdict: all listed claims source-checked; evidence not applied",
                    f"- Validation: {validation}", "", "## Ownership", "",
                    "Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):",
                    *["- " + p for p in sorted(owners)], "", "## Concentration Claims", "",
                    "Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.", "",
                    "| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |",
                    "| --- | --- | --- | --- | --- | --- |"]
            for c in claims:
                evidence = c.get("attached_evidence") or []
                if c.get("reference"):
                    evidence = [{k: c.get(k) for k in ("reference", "snippet", "locator", "calculation", "explanation") if c.get(k)}]
                text.append("| " + " | ".join(esc(x) for x in [c["field"] + " / " + c["ingredient"], c.get("old") or c.get("modifications"),
                    c["evidence_state"] + "; " + "; ".join(c["flags"]), c["status"] + "; " + c["source_check"], c.get("proposed"), evidence or "No scoped concentration evidence attached; source lookup pending"]) + " |")
            if not claims:
                text += ["", "No structured ingredient/stock claim rows. Missing composition is unresolved; this is not a verified empty recipe."]
            text += ["", "## Source Leads", "", "These references have not been fetched unless explicitly source-checked above.", "", *["- " + s for s in r.get("source_leads", [])]]
            if r.get("context_evidence"):
                text += ["", "## Unscoped Context Evidence", "", "```json", json.dumps(r["context_evidence"], ensure_ascii=False, indent=2), "```"]
            if r.get("parse_error"):
                text += ["", "## Read Failure", "", r["parse_error"]]
            if errors[r["path"]]:
                text += ["", "## Schema Findings", "", *["- " + e["message"] for e in errors[r["path"]]]]
            text += ["", "## Follow-up", "", "Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.", ""]
            report_path.write_text("\n".join(text))
            mw.writerow({"record": r["path"], "id": r.get("id"), "layer": r["layer"], "kind": r.get("record_kind"), "sha256": r["sha256"],
                         "claims": len(claims), "source_checked_claims": checked_count, "pending_claims": len(claims) - checked_count,
                         "schema_errors": len(errors[r["path"]]) if validation_complete else "pending", "report": str(report)})
    (out / "summary.json").write_text(json.dumps({"metadata": meta, "validation_finalized": validation_complete, "counts": dict(counts)}, indent=2) + "\n")
    print(json.dumps(dict(counts), indent=2), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["scan", "render"])
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    (scan if args.mode == "scan" else render)(args.output)
