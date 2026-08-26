from __future__ import annotations

import copy
import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]


def load_migration():
    path = REPO / "scripts" / "repair_togo_bsk_structure.py"
    spec = importlib.util.spec_from_file_location("repair_togo_bsk_structure", path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def pre_repair_document(migration) -> dict:
    ingredients = [
        {
            "preferred_term": name,
            "concentration": {"value": value, "unit": unit},
        }
        for name, value, unit in migration.PRE_INGREDIENTS
    ]
    ingredients[2]["term"] = {
        "id": "CHEBI:86345",
        "label": "magnesium dichloride hexahydrate",
    }
    ingredients[13]["term"] = {"id": "CHEBI:5291", "label": "gelatin"}
    solutions = [
        {
            "preferred_term": name,
            "composition": [],
            "concentration": {"value": value, "unit": unit},
            "name": "Unknown solution",
        }
        for name, value, unit, _ in migration.PRE_SOLUTIONS
    ]
    return {
        "media_term": {"term": {"id": migration.MEDIA_TERM_ID}},
        "ingredients": ingredients,
        "solutions": solutions,
        "notes": "Commercial Product: LB Medium",
        "curation_history": [],
    }


def reviewed_payload(migration) -> dict:
    """Build a hermetic fixture from the source signatures frozen by the migration."""
    components = []
    for index, (section_name, raw_items) in enumerate(migration.RAW_SIGNATURE):
        items = []
        for name, volume, unit, conc_value, conc_unit, reference_id in raw_items:
            item = {"component_name": name, "properties": [], "roles": []}
            for key, value in (
                ("volume", volume),
                ("unit", unit),
                ("conc_value", conc_value),
                ("conc_unit", conc_unit),
                ("reference_media_id", reference_id),
            ):
                if value:
                    item[key] = value
            items.append(item)
        components.append(
            {
                "paragraph_index": 1 + 2 * index,
                "subcomponent_name": section_name,
                "items": items,
            }
        )

    comment_indices = (4, 6, 8, 10, 11)
    return {
        "meta": {"gm": f"http://togomedium.org/medium/{migration.SOURCE_ID}"},
        "components": components,
        "comments": [
            {"paragraph_index": index, "comment": comment}
            for index, comment in zip(comment_indices, migration.SOURCE_COMMENTS, strict=True)
        ],
    }


def test_checked_in_payload_has_reviewed_signature() -> None:
    migration = load_migration()
    if not migration.RAW_FILE.is_file():
        pytest.skip("ignored TOGO source payload is unavailable in a standalone checkout")
    payload = migration.load_payload(migration.RAW_FILE)

    migration.validate_payload(payload)
    assert (
        migration.structured_solution_signature(
            migration._importer()._extract_assembled_solutions(payload)
        )
        == migration.EXPECTED_SOLUTIONS
    )


def test_migration_restores_bsk_structure_and_is_idempotent() -> None:
    migration = load_migration()
    payload = reviewed_payload(migration)
    repaired, changed = migration.repair_document(pre_repair_document(migration), payload)

    assert changed is True
    assert repaired["ingredients"] == []
    assert migration.structured_solution_signature(repaired["solutions"]) == (
        migration.EXPECTED_SOLUTIONS
    )
    assert repaired["ph_value"] == 7.6
    assert repaired["sterilization"] == {"method": "FILTER"}
    names = {
        ingredient["preferred_term"]
        for solution in repaired["solutions"]
        for ingredient in solution["composition"]
    }
    assert "bovine serum albumine, fract. V (important: Sigma No A9647)" in names
    assert {"Tryptone", "Yeast extract", "Sodium chloride"}.isdisjoint(names)
    water = repaired["solutions"][1]["composition"][1]
    assert water["term"] == {"id": "CHEBI:15377", "label": "water"}
    magnesium = repaired["solutions"][0]["composition"][2]
    assert magnesium["term"]["id"] == "CHEBI:86345"
    assert repaired["curation_history"][-1]["action"] == migration.ACTION
    assert migration.repair_document(repaired, payload)[1] is False


def test_migration_refuses_normalized_or_raw_drift() -> None:
    migration = load_migration()
    payload = reviewed_payload(migration)
    doc = pre_repair_document(migration)
    doc["ingredients"][0]["concentration"]["value"] = "901"
    with pytest.raises(ValueError, match="ingredient signature drifted"):
        migration.repair_document(doc, payload)

    drifted_payload = copy.deepcopy(payload)
    drifted_payload["components"][0]["items"][0]["volume"] = 999
    with pytest.raises(ValueError, match="component signature drifted"):
        migration.repair_document(pre_repair_document(migration), drifted_payload)
