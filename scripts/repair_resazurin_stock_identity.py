"""Preview/apply three evidence-backed identity withdrawals; never change their doses."""

import argparse
import copy
import importlib.util
import json
import subprocess
from dataclasses import asdict
from pathlib import Path

import review_solution_concentration_evidence as runner
from curation_identity_fixtures import read_mim_capture

from culturemech.curate.curation_event import now_iso, record_curation_event
from culturemech.validation.write_validated import validate_recipe

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "reports/ingredient_concentration_curation/20261009-resazurin-stock-identity"
spec = importlib.util.spec_from_file_location("resazurin_identity_audit", HERE / "audit.py")
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


def preview(root=ROOT):
    plan = {
        "version": 1,
        "action": audit.ACTION,
        "created_at": now_iso(),
        "commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=root, text=True
        ).strip(),
        "target_class": "MediaRecipe",
        "records": [],
    }
    for target in audit.cohort():
        source = audit.source_for(target)
        raw = (root / target["record"]).read_bytes()
        assert runner.sha(raw) == target["sha256"], "Record drift; requires new review"
        before = runner.load_yaml(raw)
        assert not validate_recipe(before, target_class="MediaRecipe")
        after = copy.deepcopy(before)
        pointer = target["pointer"][:-1]
        node = runner.get_node(after, pointer)
        field = runner.field_name(target["pointer"])
        old = node.pop("term")
        page = (
            "page 1, main formulation"
            if target["id"] == "CultureMech:001100"
            else "page 2, Solution A (continued from page 1)"
        )
        explanation = (
            f"{field}: Withdrawn unsupported exact primary identity CHEBI:8806. "
            "The quoted recipe specifies a sodium-resazurin stock, whereas the local ChEBI "
            "snapshot identifies CHEBI:8806 as sodium-free Resazurin (formula C12H7NO4, "
            "charge 0; http://purl.obolibrary.org/obo/CHEBI_8806). No replacement chemical "
            "identifier or absence of a suitable ontology term is asserted. The source name, "
            "0.0005 L preparation input and all other quantities are preserved. "
            f"Locator={page}; accessed={source['metadata']['accessed_at']}; "
            f"text SHA256={target['source_sha256']}; PDF SHA256={target['source_pdf_sha256']}. "
            f"The immutable MIM label-index snapshot (SHA256={audit.MIM_SHA}) still resolves "
            "this exact label to CHEBI:8806 even without the local term. That publication-time "
            "identity conflict remains unresolved and needs an upstream mapping review; "
            "the resolver and snapshot have not been altered. Live ChEBI lookup was unavailable "
            "through the web tool; ontology-form comparison uses the local snapshot."
        )
        node["evidence"][0]["explanation"] += "\n\n" + explanation
        changes = {
            "field": field,
            "old": old,
            "new": None,
            "evidence_extended": runner.field_name(pointer + ["evidence", 0, "explanation"]),
            "all_quantities_preserved": True,
            "publication_identity_resolved": False,
        }
        record_curation_event(
            after,
            curator="codex",
            action=audit.ACTION,
            source=target["source_reference"],
            timestamp=plan["created_at"],
            notes=explanation,
            changes=json.dumps(changes),
        )
        assert not validate_recipe(after, target_class="MediaRecipe")
        rendered = runner.render(raw.decode(), after)
        item = {
            "path": target["record"],
            "id": before["id"],
            "action": audit.ACTION,
            "before_text": raw.decode(),
            "after_text": rendered.decode(),
            "before_sha256": runner.sha(raw),
            "after_sha256": runner.sha(rendered),
            "publication_identity_resolved": False,
            "resolver_after": asdict(read_mim_capture(audit.MIM_SHA).resolve(node)),
            "claims": [
                {
                    "field": field,
                    "ingredient": node["preferred_term"],
                    "old": old,
                    "new": None,
                    "status": "correct",
                    "reference": target["source_reference"],
                    "snippet": target["snippet"],
                    "explanation": explanation,
                }
            ],
        }
        audit.check(before, after, item)
        plan["records"].append(item)
    runner.safe_targets(root, plan)
    return plan


def apply(plan, root=ROOT, *, verify=False):
    root = root.resolve()
    assert plan["action"] == audit.ACTION and plan["target_class"] == "MediaRecipe"
    expected = {x["record"] for x in audit.cohort()}
    assert len(plan["records"]) == len(expected) == 3
    assert {x["path"] for x in plan["records"]} == expected
    runner.safe_targets(root, plan)
    pending = []
    for item in plan["records"]:
        target = root / item["path"]
        assert target.resolve().is_relative_to(root.resolve() / "data/normalized_yaml")
        parts = Path(item["path"]).parts
        assert not any((root.joinpath(*parts[:i])).is_symlink() for i in range(1, len(parts) + 1))
        before, after = (runner.load_yaml(item[k]) for k in ("before_text", "after_text"))
        assert not validate_recipe(before, target_class="MediaRecipe")
        assert not validate_recipe(after, target_class="MediaRecipe")
        audit.check(before, after, item)
        current = target.read_bytes()
        if runner.sha(current) == item["after_sha256"]:
            continue
        assert not verify and runner.sha(current) == item["before_sha256"], "Concurrent record edit"
        pending.append((target, current, item["after_text"].encode()))
    for target, raw, _ in pending:
        assert target.read_bytes() == raw, "Concurrent edit during preflight"
    for target, raw, output in pending:
        assert target.read_bytes() == raw, "Concurrent edit during write"
        target.write_bytes(output)
        assert target.read_bytes() == output
    return {"changed": len(pending), "already_applied": 3 - len(pending)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, default=HERE / "plan.json")
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--apply", action="store_true")
    modes.add_argument("--verify", action="store_true")
    modes.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if args.apply or args.verify:
        print(json.dumps(apply(json.loads(args.plan.read_text()), verify=args.verify)))
    else:
        assert not args.plan.exists(), "Refuse to overwrite preview"
        plan = preview()
        with args.plan.open("x") as output:
            output.write(json.dumps(plan, indent=2) + "\n")
        print(
            json.dumps(
                {"records": len(plan["records"]), "claims": [r["claims"] for r in plan["records"]]},
                indent=2,
            )
        )


if __name__ == "__main__":
    main()
