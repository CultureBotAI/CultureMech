"""Apply the one-run pre-save record08 metadata precision amendment.

Provenance date: 2026-11-15.
Context: CultureMech #750 (record08 assessment) and #752 (retain provenance
helpers and exact predecessors). This changes draft metadata, not recipe science.

Required inputs: no CLI arguments; explicit checkout-root working directory,
Python/PyYAML, and the exact record08/review.yaml with SHA256 beginning
746d4673, plus claim-inventory.json, its referenced current YAMLs and raw source
objects under .temp/batch079-scientific-20261114. The full required draft digest
is asserted in main; all inventory values and source locators are rechecked.
Outputs: exclusive review.pre-metadata-precision.yaml and
metadata-precision-audit.json in record08; review.yaml is replaced with the
bounded timestamp, PDF-page locator and historical-check-summary amendment.
The console prints the amendment audit.

Replay limits: valid only for that exact pre-save draft and absent archive/audit
outputs. Do not rerun on a saved review or remove the predecessor guards. The
helper executes no native validator or saver and changes no scientific YAML,
quantity decision or source capture. Retain both draft versions and this source;
the subsequent saved immutable bundle is a separate parent-owned operation.
"""

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / ".temp/batch079-scientific-20261114/record08"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def main():
    assert Path.cwd().resolve() == ROOT
    draft = D / "review.yaml"
    before = draft.read_bytes()
    assert (
        hashlib.sha256(before).hexdigest()
        == "746d4673eb6dd676eb4cbb178530887d4e249919658e676ee5adeb9084afa865"
    )
    inventory = json.loads((D / "claim-inventory.json").read_text())

    def locate(obj, path):
        for key, index in re.findall(r"([A-Za-z_]\w*)|\[(\d+)\]", path.removeprefix("$.")):
            obj = obj[key] if key else obj[int(index)]
        return obj

    count = 0
    for row in inventory["rows"]:
        current = yaml.safe_load((ROOT / row["document"]).read_text())
        assert locate(current, row["field"]) == row["retained_value"]
        for source in row["sources"]:
            raw = (ROOT / source["source"]).read_bytes()
            assert hashlib.sha256(raw).hexdigest() == source["sha256"]
            expected = source["exact_object"] if "exact_object" in source else source["exact_value"]
            assert locate(json.loads(raw), source["locator"]) == expected
            count += 1
    with (D / "review.pre-metadata-precision.yaml").open("xb") as h:
        h.write(before)
    review = yaml.safe_load(before)
    review["started_at"] = "2026-11-15T08:09:02.141437Z"
    now = datetime.now(timezone.utc)
    review["finished_at"] = now.isoformat().replace("+00:00", "Z")
    review["review_id"] = now.strftime("%Y%m%dT%H%M%SZ") + "-batch079-record08-desulfotignum"
    for evidence in review["evidence"]:
        if evidence["evidence_id"] == "E-primary-383a":
            evidence["locator"] = (
                "Pages 1–2: generic A–E recipe, preparation and embedded stock tables"
            )
        if evidence["evidence_id"] == "E-primary-383":
            evidence["locator"] = (
                "Pages 1–3: generic A–E recipe, preparation and embedded stock tables; strain-specific substitutions read but excluded from transfer"
            )
        if evidence["evidence_id"] in {
            "E-native-schema",
            "E-native-strict",
            "E-native-terms",
            "E-native-references",
        }:
            evidence["summary"] = (
                "Full original log read on byte-identical current target/owners/schema; historical receipt retained. Fresh execution is recorded separately."
            )
    review["notes"].append(
        "started_at uses the earliest durable timed record08 evidence activity, the fresh CHEBI:50144 capture. Full-file reading began earlier without a persisted start timestamp. The author-plan time 2026-11-15T08:15:25.868310Z marks draft construction and input binding, not the start of scientific assessment; reused record07 captures retain their original times. Parent applied only timestamp/locator/history-summary precision before save; substantive decisions are unchanged."
    )
    draft.write_text(
        yaml.dump(review, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=True, width=100)
    )
    audit = {
        "original_draft_sha256": hashlib.sha256(before).hexdigest(),
        "final_draft_sha256": hashlib.sha256(draft.read_bytes()).hexdigest(),
        "review_id": review["review_id"],
        "verified_local_fields": len(inventory["rows"]),
        "verified_source_locators": count,
        "native_validation_before_precision": "20261115T081557533818Z-record08-validate.json; exit0",
        "prior_parent_read_attempts": [
            {
                "exit": 1,
                "error": "AssertionError: $.solutions[0].steps[0]",
                "cause": "Ad hoc reader only handled recipe arrays; no native or scientific failure.",
            },
            {
                "exit": 1,
                "error": "KeyError: 'exact_object'",
                "cause": "Ad hoc reader omitted pH exact_value representation; no native or scientific failure.",
            },
        ],
        "changes": [
            "start/finish/review_id timestamps",
            "two document-specific PDF locators",
            "historical diagnostic summary clarification",
            "timestamp provenance note",
        ],
    }
    with (D / "metadata-precision-audit.json").open("x") as h:
        json.dump(audit, h, indent=2)
        h.write("\n")
    print(json.dumps(audit))


if __name__ == "__main__":
    main()
