#!/usr/bin/env python3
"""Freeze audited #683 successor edges for historical provenance (#772).

Date: 2026-11-16. Inputs: fixed base/applied Git commits and six reviewed proposals.
Output: exact-byte plan.json, created exclusively or verified byte-for-byte;
no recipes, prior receipts, history or scientific claims are changed.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from audit_variant_ingredient_successor import (  # noqa: E402
    BASE,
    PLAN,
    RESULT,
    check,
    expected_item,
    proposal_records,
)


def main():
    records = []
    for path in sorted(proposal_records()):
        item = expected_item(path)
        before, after = (
            yaml.load(item[label + "_text"], Loader=yaml.CSafeLoader)
            for label in ("before", "after")
        )
        check(before, after, item)
        records.append(item)
    plan = {
        "base_commit": BASE,
        "applied_commit": RESULT,
        "issue": "https://github.com/CultureBotAI/CultureMech/issues/772",
        "scope": "Exact reviewed variant additions; all original recipe/source audits retained",
        "records": records,
    }
    text = json.dumps(plan, ensure_ascii=False, indent=2) + "\n"
    PLAN.parent.mkdir(parents=True, exist_ok=True)
    if PLAN.exists():
        assert PLAN.read_text(encoding="utf-8") == text, "Refusing to overwrite a different plan"
    else:
        with PLAN.open("x", encoding="utf-8") as stream:
            stream.write(text)
    assert PLAN.read_text(encoding="utf-8") == text
    print(
        f"Verified {len(records)} exact reviewed variant successors: {PLAN.relative_to(PLAN.parents[3])}"
    )


if __name__ == "__main__":
    main()
