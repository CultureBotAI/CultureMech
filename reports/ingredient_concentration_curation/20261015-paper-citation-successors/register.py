"""Reproduce the ten reviewed citation successors from immutable git revisions."""

import hashlib
import json
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
from audit_paper_citation_successor import check  # noqa: E402

BASE = "75036611d15404c10e444777c10520c8845d3bd4"
RESULT = "4e83113f2d77f61e49ff2bc941050c440afee416"
NAMES = (
    "r2a_medium",
    "magnetovibrio_medium",
    "mannitol_soya_flour_medium",
    "ajs",
    "2asw",
    "eg_jm",
    "f_2",
    "jm",
    "r2a_agar",
    "vr_salts_b",
)


def main():
    records = []
    for name in NAMES:
        path = f"data/normalized_yaml/bacterial/{name}.yaml"
        item = {"path": path, "action": "REGISTERED_PAPER_CITATION_SUCCESSOR"}
        for label, revision in (("before", BASE), ("after", RESULT)):
            raw = subprocess.check_output(["git", "show", f"{revision}:{path}"], cwd=ROOT)
            item[label + "_text"] = raw.decode()
            item[label + "_sha256"] = hashlib.sha256(raw).hexdigest()
        before, after = [yaml.safe_load(item[label + "_text"]) for label in ("before", "after")]
        item["id"] = after["id"]
        check(before, after, item)
        records.append(item)
    plan = {
        "base_commit": BASE,
        "citation_commit": RESULT,
        "scope": "Structural citation successors; original recipe/source audits retained",
        "issue": "https://github.com/CultureBotAI/CultureMech/issues/626",
        "records": records,
    }
    output = Path(__file__).with_name("plan.json")
    text = json.dumps(plan, indent=2) + "\n"
    if output.exists():
        assert output.read_text() == text, "Refusing to replace a different receipt"
    else:
        output.write_text(text)
    print(f"Verified {len(records)} citation successors")


if __name__ == "__main__":
    main()
