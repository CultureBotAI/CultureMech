#!/usr/bin/env python3
"""Verify a quote-only proposal repair for #683/#763 (2026-11-16).

Inputs: exact before/after decision JSON. Output: optional exclusive JSON receipt.
Only EvidenceItem snippet/explanation changes are allowed; no recipe mutations.
"""

import argparse
import copy
import hashlib
import json
from pathlib import Path


def without_quotations(document):
    document = copy.deepcopy(document)
    for record in document["records"]:
        for variant in record["variants"]:
            for change in variant["ingredient_changes"]:
                for evidence in change["evidence"]:
                    evidence.pop("snippet", None)
                    evidence.pop("explanation", None)
    return document


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("before", type=Path)
    parser.add_argument("after", type=Path)
    parser.add_argument("--receipt", type=Path)
    args = parser.parse_args()
    before_raw, after_raw = args.before.read_bytes(), args.after.read_bytes()
    before, after = json.loads(before_raw), json.loads(after_raw)
    if without_quotations(before) != without_quotations(after):
        raise ValueError("repair changes fields other than evidence snippets/explanations")
    receipt = {
        "before_sha256": hashlib.sha256(before_raw).hexdigest(),
        "after_sha256": hashlib.sha256(after_raw).hexdigest(),
        "allowed_changes": [
            "ingredient_changes[].evidence[].snippet",
            "ingredient_changes[].evidence[].explanation",
        ],
        "other_fields_unchanged": True,
        "limitation": "Checks edit scope only; source accuracy requires independent reading.",
    }
    if args.receipt:
        with args.receipt.open("x") as stream:
            json.dump(receipt, stream, indent=2)
            stream.write("\n")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
