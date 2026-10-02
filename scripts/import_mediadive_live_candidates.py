#!/usr/bin/env python3
"""Import selected live MediaDive API records missing from normalized YAML."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
SOURCE_URL = "https://mediadive.dsmz.de/rest/medium/{media_id}"

TARGETS: dict[str, tuple[str, str]] = {
    "71a": ("bacterial", "acidithiobacillus_marinus_medium"),
    "1783": ("bacterial", "chloracidobacterium_thermophilum_midnight_medium_ctm"),
    "1873": ("bacterial", "glucose_agar_mediadive_1873"),
    "1894": ("bacterial", "mannitol_soya_flour_medium"),
    "1895": ("bacterial", "hs_rfb_borrelia_miyamotoi_medium"),
    "1897": ("bacterial", "starch_casein_nitrate_agar"),
}

UNIT_MAP = {
    None: "G_PER_L",
    "g": "G_PER_L",
    "mg": "MG_PER_L",
    "ml": "ML_PER_L",
    "ul": "ML_PER_L",
    "µl": "ML_PER_L",
    "μl": "ML_PER_L",
}


def fmt(value: Any) -> str:
    if isinstance(value, float):
        return f"{value:.6g}"
    return str(value)


def concentration(item: dict[str, Any], volume_ml: float | None) -> dict[str, str]:
    amount = item.get("g_l")
    unit = "g" if amount is not None else item.get("unit")

    if amount is None:
        amount = item.get("amount")

    if amount is None:
        return {"value": "variable", "unit": "VARIABLE"}

    value = float(amount)
    if item.get("g_l") is None and volume_ml and volume_ml > 0:
        value *= 1000.0 / volume_ml
    if unit in {"ul", "µl", "μl"}:
        value /= 1000.0

    return {"value": fmt(value), "unit": UNIT_MAP.get(unit, "G_PER_L")}


def notes_for_item(item: dict[str, Any]) -> str | None:
    parts = []
    if item.get("attribute"):
        parts.append(str(item["attribute"]))
    if item.get("condition"):
        parts.append(str(item["condition"]))
    if item.get("optional"):
        parts.append("MediaDive marks this component optional.")
    return " ".join(parts) or None


def ingredient_from_item(item: dict[str, Any], volume_ml: float | None) -> dict[str, Any]:
    out: dict[str, Any] = {
        "preferred_term": item["compound"],
        "concentration": concentration(item, volume_ml),
    }
    if item.get("compound_id"):
        out["term"] = {
            "id": f"mediadive.compound:{item['compound_id']}",
            "label": item["compound"],
        }
    if notes := notes_for_item(item):
        out["notes"] = notes
    return out


def solution_dose_from_item(item: dict[str, Any], volume_ml: float | None) -> dict[str, str]:
    return concentration({"amount": item.get("amount"), "unit": item.get("unit")}, volume_ml)


def ordered_recipe(solution: dict[str, Any]) -> list[dict[str, Any]]:
    return sorted(solution.get("recipe") or [], key=lambda item: item.get("recipe_order") or 0)


def solution_steps(solution: dict[str, Any]) -> str | None:
    steps = []
    for step in solution.get("steps") or []:
        text = str(step.get("step") or "")
        text = re.sub(r"<[^>]+>", "", text)
        text = re.sub(r"\s+", " ", text).strip()
        if text:
            steps.append(text)
    return "\n".join(steps) or None


def convert_solution(
    solution: dict[str, Any],
    *,
    dose: dict[str, str],
    solutions_by_id: dict[int, dict[str, Any]],
) -> dict[str, Any]:
    out: dict[str, Any] = {
        "preferred_term": solution["name"],
        "source": f"MediaDive solution {solution['id']}",
        "concentration": dose,
        "composition": [],
    }
    child_solutions: list[dict[str, Any]] = []

    volume_ml = solution.get("volume")
    for item in ordered_recipe(solution):
        if item.get("compound"):
            out["composition"].append(ingredient_from_item(item, volume_ml))
            continue

        child = solutions_by_id.get(item.get("solution_id"))
        if not child:
            continue
        child_dose = solution_dose_from_item(item, volume_ml)
        if child.get("recipe") or child.get("steps"):
            child_solutions.append(
                convert_solution(
                    child,
                    dose=dict(child_dose),
                    solutions_by_id=solutions_by_id,
                )
            )
        else:
            out["composition"].append(
                {
                    "preferred_term": item["solution"],
                    "concentration": child_dose,
                }
            )

    if child_solutions:
        out["solutions"] = child_solutions
    if notes := solution_steps(solution):
        out["preparation_notes"] = notes
    return out


def source_medium(data: dict[str, Any]) -> dict[str, Any]:
    medium = data.get("medium")
    if not isinstance(medium, dict):
        raise ValueError("MediaDive detail payload has no data.medium object")
    return medium


def physical_state(ingredients: list[dict[str, Any]]) -> str:
    return (
        "SOLID_AGAR"
        if any("agar" in entry["preferred_term"].lower() for entry in ingredients)
        else "LIQUID"
    )


def build_record(media_id: str, payload: dict[str, Any]) -> dict[str, Any]:
    data = payload["data"]
    medium = source_medium(data)
    category, slug = TARGETS[media_id]
    solutions = data.get("solutions") or []
    if not solutions:
        raise ValueError(f"{media_id} has no MediaDive solutions")

    solutions_by_id = {int(solution["id"]): solution for solution in solutions}
    main = solutions[0]
    ingredients: list[dict[str, Any]] = []
    child_solutions: list[dict[str, Any]] = []

    for item in ordered_recipe(main):
        if item.get("compound"):
            ingredients.append(ingredient_from_item(item, main.get("volume")))
            continue

        child = solutions_by_id.get(item.get("solution_id"))
        if not child:
            continue
        dose = solution_dose_from_item(item, main.get("volume"))
        ingredients.append({"preferred_term": item["solution"], "concentration": dict(dose)})
        if child.get("recipe") or child.get("steps"):
            child_solutions.append(
                convert_solution(child, dose=dict(dose), solutions_by_id=solutions_by_id)
            )

    now = datetime.now(timezone.utc).isoformat()
    record: dict[str, Any] = {
        "name": slug,
        "original_name": medium["name"],
        "category": category,
        "medium_type": "COMPLEX" if medium.get("complex_medium") == "yes" else "DEFINED",
        "physical_state": physical_state(ingredients),
        "media_term": {
            "preferred_term": f"MediaDive Medium {media_id}",
            "term": {
                "id": f"mediadive.medium:{media_id}",
                "label": medium["name"],
            },
        },
        "notes": f"Source: MediaDive | Link: {SOURCE_URL.format(media_id=media_id)}",
        "ingredients": ingredients,
        "preparation_steps": [
            {
                "step_number": idx,
                "action": "MIX",
                "description": text,
            }
            for idx, text in enumerate((solution_steps(main) or "").splitlines(), start=1)
            if text
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [
            {
                "timestamp": now,
                "curator": "mediadive-live-gap-import",
                "action": "Imported from live MediaDive API",
                "source": SOURCE_URL.format(media_id=media_id),
                "notes": (
                    f"Direct import from MediaDive medium {media_id}. Recipe rows "
                    "captured from the live API detail payload."
                ),
            }
        ],
        "references": [{"reference": SOURCE_URL.format(media_id=media_id)}],
    }

    min_ph = medium.get("min_pH")
    max_ph = medium.get("max_pH")
    if min_ph is not None and max_ph is not None:
        if float(min_ph) == float(max_ph):
            record["ph_value"] = float(min_ph)
        else:
            record["ph_range"] = {"min": float(min_ph), "max": float(max_ph)}

    if child_solutions:
        record["solutions"] = child_solutions

    description = medium.get("description")
    if description:
        record["description"] = re.sub(r"\s+", " ", str(description)).strip()

    return record


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source-dir",
        type=Path,
        default=Path("/tmp/culturemech_mediadive_missing"),
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=REPO / "data" / "normalized_yaml",
    )
    args = parser.parse_args()

    for media_id, (category, slug) in TARGETS.items():
        payload = json.loads((args.source_dir / f"{media_id}.json").read_text())
        record = build_record(media_id, payload)
        path = args.output_dir / category / f"{slug}.yaml"
        if path.exists():
            raise FileExistsError(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as stream:
            yaml.safe_dump(record, stream, sort_keys=False, allow_unicode=True)
        print(path)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
