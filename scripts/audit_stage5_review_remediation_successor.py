"""Audit Stage 5 review-remediation successors (#635, #638, #640) without exempting historical recipe audits."""

from __future__ import annotations

from collections import Counter

THERMINCOLA_IDS = {
    "CultureMech:002143",
    "CultureMech:004016",
    "CultureMech:006919",
    "CultureMech:006918",
    "CultureMech:002142",
    "CultureMech:000714",
}


def _provenance_counts(node) -> Counter:
    result: Counter = Counter()
    if isinstance(node, dict):
        for key, value in node.items():
            if key in {"evidence", "references", "curation_history"} and isinstance(value, list):
                result["new_" + key] += len(value)
            else:
                result.update(_provenance_counts(value))
    elif isinstance(node, list):
        for value in node:
            result.update(_provenance_counts(value))
    return result


def check(before: dict, after: dict, item: dict) -> Counter:
    """Verify exact Stage 5 successor transformation and append-only history."""
    assert before["id"] == after["id"] == item["id"], "Successor identity mismatch"
    old_history = before.get("curation_history", [])
    new_history = after.get("curation_history", [])
    assert (
        len(new_history) == len(old_history) + 1
    ), "Expected exactly one new curation_history event"
    assert new_history[: len(old_history)] == old_history, "Prior curation_history was modified"
    assert new_history[-1].get("action") == "CURATED"
    assert new_history[-1].get("curator") == "stage5-remediation-v1.0"

    if item["id"] == "CultureMech:000252":
        allowed = {
            "ingredients",
            "solutions",
            "curation_history",
        }
        assert {k: v for k, v in before.items() if k not in allowed} == {
            k: v for k, v in after.items() if k not in allowed
        }, "Unexpected top-level field change in DSMZ 1399 successor"
        assert after["ingredients"][4]["term"] == {
            "id": "CHEBI:15377",
            "label": "water",
        }
        assert after["solutions"][0]["composition"][7]["term"] == {
            "id": "CHEBI:86254",
            "label": "iron(III) chloride hexahydrate",
        }
        assert after["solutions"][0]["composition"][8]["term"] == {
            "id": "CHEBI:15377",
            "label": "water",
        }
    elif item["id"] in THERMINCOLA_IDS:
        allowed = {
            "name",
            "ingredients",
            "parent_media",
            "variant_children",
            "curation_history",
        }
        assert {k: v for k, v in before.items() if k not in allowed} == {
            k: v for k, v in after.items() if k not in allowed
        }, f"Unexpected top-level field change in {item['path']}"
        assert len(after["ingredients"]) == len(before["ingredients"]) in {32, 33, 34}
        for b_ing, a_ing in zip(before["ingredients"], after["ingredients"], strict=True):
            assert b_ing["preferred_term"] == a_ing["preferred_term"]
            assert a_ing["concentration"]["unit"] == "G_PER_L"
    else:
        raise AssertionError(f"Unrecognized Stage 5 successor target: {item['path']}")

    delta = _provenance_counts(after)
    delta.subtract(_provenance_counts(before))
    assert delta["new_curation_history"] == 1
    assert all(v >= 0 for v in delta.values()), f"Negative provenance delta: {delta}"
    return delta
