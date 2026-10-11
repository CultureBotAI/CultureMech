"""Preview and guarded application of four source-specific medium323 repairs."""

import argparse
import copy
import importlib.util
import json
import subprocess
from pathlib import Path

import review_solution_concentration_evidence as runner

from culturemech.curate.curation_event import now_iso, record_curation_event
from culturemech.validation.write_validated import validate_recipe

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "reports/ingredient_concentration_curation/20261009-medium323"
PLAN_PATH = HERE / "plan-v2.json"
spec = importlib.util.spec_from_file_location("medium323_ingredient_audit", HERE / "audit.py")
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


def preview(root=ROOT):
    candidates = audit.reviewed()
    sources, _ = audit.sources()
    plan = {
        "version": 1,
        "action": audit.ACTION,
        "created_at": now_iso(),
        "commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=root, text=True
        ).strip(),
        "draft_sha256": audit.DRAFT_SHA,
        "capture_sha256": audit.CAPTURE_SHA,
        "records": [],
    }
    for key, candidate in candidates.items():
        raw = (root / candidate["path"]).read_bytes()
        assert runner.sha(raw) == candidate["before_sha256"], "Record drift; new review required"
        before = runner.load_yaml(raw)
        assert before["id"] == candidate["id"]
        cls = candidate["target_class"]
        assert not validate_recipe(before, target_class=cls)
        after = runner.load_yaml(candidate["proposed_text"])
        assert after["curation_history"][:-1] == before["curation_history"]
        after["curation_history"].pop()
        for _, node in audit.walk(after):
            for field in ("notes", "explanation"):
                if isinstance(node.get(field), str):
                    node[field] = (
                        node[field]
                        .replace("The draft now", "The record now")
                        .replace("this pinned draft", "the pinned review")
                    )
        if key in {"K323", "D323"}:
            if key == "K323":
                audit.finish_identity_review(before, after)
            target = candidates["D323" if key == "K323" else "K323"]
            link = {
                "id": target["id"],
                "name": before["name"],
                "path": target["path"],
                "relationship": "UNCERTAIN",
                "notes": audit.LINK_REASON,
                "evidence": [audit.relationship_evidence()],
            }
            if key == "K323":
                after["parent_media"] = link
                after["variant_relationship"] = "UNCERTAIN"
                after["variant_modifications"] = copy.deepcopy(audit.MODIFICATIONS)
            else:
                after["variant_children"] = [link]
                komodo = runner.load_yaml(candidates["K323"]["proposed_text"])
                after["references"].append(copy.deepcopy(komodo["references"][0]))
        changes = audit.operations(before, after)
        notes = audit.history_notes(key)
        record_curation_event(
            after,
            curator="codex",
            action=audit.ACTION,
            timestamp=plan["created_at"],
            source=sources[key]["metadata"]["url"],
            notes=notes,
            changes=json.dumps(audit.event_changes(before, after)),
        )
        assert not validate_recipe(after, target_class=cls)
        output = runner.render(raw.decode(), after)
        claims = copy.deepcopy(candidate["old_quantity_claims"])
        item = {
            "key": key,
            "path": candidate["path"],
            "id": candidate["id"],
            "target_class": cls,
            "action": audit.ACTION,
            "before_text": raw.decode(),
            "after_text": output.decode(),
            "before_sha256": runner.sha(raw),
            "after_sha256": runner.sha(output),
            "claims": claims,
            "field_changes": changes,
            "history_notes": notes,
            "unresolved": audit.limitations(key),
            "publication_identity_resolved": False,
        }
        audit.check(before, after, item)
        plan["records"].append(item)
    runner.safe_targets(root, plan)
    return plan


def safe_path(root, path):
    target = root / path
    parts = Path(path).parts
    assert target.resolve().is_relative_to(root / "data/normalized_yaml")
    assert not any(root.joinpath(*parts[:i]).is_symlink() for i in range(1, len(parts) + 1))
    return target


def apply(plan, root=ROOT, *, verify=False):
    root = root.resolve()
    assert plan["action"] == audit.ACTION
    assert plan["draft_sha256"] == audit.DRAFT_SHA and plan["capture_sha256"] == audit.CAPTURE_SHA
    assert len(plan["records"]) == 4 and {r["key"] for r in plan["records"]} == audit.KEYS
    runner.safe_targets(root, plan)
    pending = []
    for item in plan["records"]:
        target = safe_path(root, item["path"])
        before, after = (runner.load_yaml(item[field]) for field in ("before_text", "after_text"))
        audit.check(before, after, item)
        assert not validate_recipe(before, target_class=item["target_class"])
        assert not validate_recipe(after, target_class=item["target_class"])
        current = target.read_bytes()
        if runner.sha(current) == item["after_sha256"]:
            continue
        assert not verify and runner.sha(current) == item["before_sha256"], "Concurrent record edit"
        pending.append((target, current, item["after_text"].encode()))
    for target, original, _ in pending:
        safe_path(root, target.relative_to(root))
        assert target.read_bytes() == original, "Concurrent edit during preflight"
    for target, original, output in pending:
        safe_path(root, target.relative_to(root))
        assert target.read_bytes() == original, "Concurrent edit during write"
        target.write_bytes(output)
        assert target.read_bytes() == output, "Readback mismatch"
    return {"changed": len(pending), "already_applied": 4 - len(pending)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, default=PLAN_PATH)
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
        with args.plan.open("x") as stream:
            stream.write(json.dumps(plan, indent=2) + "\n")
        print(json.dumps({"reviewed": len(plan["records"]), "records_edited": 0}))


if __name__ == "__main__":
    main()
