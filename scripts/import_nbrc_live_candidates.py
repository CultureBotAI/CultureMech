#!/usr/bin/env python3
"""Import parseable live NBRC catalogue records missing from normalized YAML."""

from __future__ import annotations

import argparse
import html
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import urlopen

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "src"))
from culturemech.merge.fingerprint import RecipeFingerprinter  # noqa: E402

SOURCE_URL = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO={no}"
OLD_URL = "http://www.nbrc.nite.go.jp/NBRC2/NBRCMediumDetailServlet?NO={no}"

CANDIDATES: dict[int, tuple[str, str]] = {
    219: ("bacterial", "nbrc_medium_219"),
    281: ("bacterial", "nbrc_medium_281"),
    287: ("bacterial", "nbrc_medium_287"),
    355: ("bacterial", "r_cw_medium_nbrc_355"),
    367: ("bacterial", "mjypgs_medium_nbrc_367"),
    835: ("archaea", "thermoproteus_tenax_medium_nbrc_835"),
    943: ("bacterial", "modified_prosthecomicrobium_and_ancalomicrobium_medium_nbrc_943"),
    944: ("bacterial", "peptone_yeast_extract_alkaline_medium_nbrc_944"),
    1096: ("bacterial", "one_fifth_marine_agar_with_phenanthrene_nbrc_1096"),
    1195: ("bacterial", "terephthalate_medium_nbrc_1195"),
    1199: ("bacterial", "thermotoga_thermarum_medium_nbrc_1199"),
    1407: ("bacterial", "pplo_broth_for_mycoplasma_arginini_nbrc_1407"),
}

SOLUTION_HEADERS = {
    "*Trace mineral solution",
    "*Trace minerals",
    "*Vitamin solution",
    "**Modified Hutner's solution",
    "***Metal salt solution 44",
}

UNIT_MAP = {
    "g": "G_PER_L",
    "mg": "MG_PER_L",
    "ml": "ML_PER_L",
    "l": "L",
    "mm": "MILLIMOLAR",
    "mmol": "MILLIMOLAR",
}

SIMPLE_TERMS = {
    "Agar": ("CHEBI:2509", "agar"),
    "Biotin": ("CHEBI:15956", "biotin"),
    "CaCO3": ("CHEBI:3311", "calcium carbonate"),
    "Cellobiose": ("CHEBI:17057", "cellobiose"),
    "Distilled water": ("CHEBI:15377", "water"),
    "Ethanol": ("CHEBI:16236", "ethanol"),
    "Folic acid": ("CHEBI:27470", "folic acid"),
    "Glucose": ("CHEBI:17234", "glucose"),
    "H3BO3": ("CHEBI:33118", "boric acid"),
    "KCl": ("CHEBI:32588", "potassium chloride"),
    "L-Arginine": ("CHEBI:16467", "L-arginine"),
    "L-Glutamine": ("CHEBI:18050", "L-glutamine"),
    "NaBr": ("CHEBI:63004", "sodium bromide"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "Phenol red": ("CHEBI:31991", "phenol red"),
    "Resazurin": ("CHEBI:8806", "Resazurin"),
    "Riboflavin": ("CHEBI:17015", "riboflavin"),
    "Soluble starch": ("CHEBI:28017", "Starch"),
    "Sodium pyruvate": ("CHEBI:50144", "sodium pyruvate"),
    "Sulfur": ("CHEBI:26833", "sulfur atom"),
    "Thiamine-HCl": ("CHEBI:49105", "thiamine(1+) chloride"),
    "Tween 80": ("CHEBI:53426", "polysorbate 80"),
    "Vitamin B12": ("CHEBI:176843", "vitamin B12"),
}

PH_RE = re.compile(
    r"\bpH\s*(?:to|of|=|:)?\s*" r"(\d+(?:\.\d+)?)" r"(?:\s*[-–]\s*(\d+(?:\.\d+)?))?",
    re.I,
)
BARE_PH_ROW_RE = re.compile(
    r"^\s*pH\s*(?:=|:)?\s*" r"\d+(?:\.\d+)?" r"(?:\s*[-–]\s*\d+(?:\.\d+)?)?" r"\s*$",
    re.I,
)


def clean_cell(raw: str) -> str:
    text = re.sub(r"<.*?>", "", raw)
    return html.unescape(text).replace("\xa0", " ").replace("℃", "C").strip()


def source_text(no: int, html_dir: Path | None) -> str:
    if html_dir is not None:
        return (html_dir / f"culturemech_nbrc_{no}.html").read_text(
            encoding="utf-8", errors="ignore"
        )
    with urlopen(OLD_URL.format(no=no), timeout=30) as response:  # noqa: S310
        return response.read().decode("utf-8", errors="ignore")


def page_title(text: str, no: int) -> str:
    match = re.search(
        r"<div align=\"left\">Medium</div>\s*</th>\s*<td width=\"80%\">(.*?)</td>",
        text,
        re.S,
    )
    if not match:
        return f"NBRC Medium {no}"
    title = clean_cell(match.group(1))
    return title or f"NBRC Medium {no}"


def composition_rows(text: str) -> list[list[str]]:
    match = re.search(r'id="medium-comp"><table.*?</table>', text, re.S)
    if not match:
        return []
    rows: list[list[str]] = []
    for row in re.findall(r"<tr.*?</tr>", match.group(0), re.S | re.I):
        cells = [clean_cell(cell) for cell in re.findall(r"<td[^>]*>(.*?)</td>", row, re.S | re.I)]
        rows.append([cell for cell in cells if cell])
    return rows


def strip_footnotes(value: str) -> str:
    value = re.sub(r"^\*+", "", value)
    return re.sub(r"\*+$", "", value).strip()


def parse_ph(text: str) -> float | dict[str, float] | None:
    if not BARE_PH_ROW_RE.fullmatch(text) and not re.search(r"\badjust\b.*\bpH\b", text, re.I):
        return None

    match = PH_RE.search(text)
    if not match:
        return None

    first = float(match.group(1))
    second = float(match.group(2)) if match.group(2) else None
    if second is not None and second != first:
        low, high = sorted((first, second))
        return {"min": low, "max": high}
    return first


def ingredient(name: str, value: str = "variable", unit: str = "VARIABLE") -> dict:
    if unit == "μl":
        value = f"{float(value) / 1000:g}"
        unit = "ML_PER_L"
    else:
        unit = UNIT_MAP.get(unit.lower(), unit)
    out: dict = {
        "preferred_term": strip_footnotes(name),
        "concentration": {"value": str(value), "unit": unit},
    }
    key = out["preferred_term"].replace(" (if needed)", "")
    key = re.sub(r" \(.*?\)$", "", key)
    if key in SIMPLE_TERMS:
        curie, label = SIMPLE_TERMS[key]
        out["term"] = {"id": curie, "label": label}
    if "if needed" in name:
        out["notes"] = "NBRC lists this component as optional when a solid medium is needed."
    return out


def solution_dose(name: str, ingredients: list[dict], solutions: list[dict]) -> dict:
    """Return the dose of a named stock from its parent ingredient entry."""
    for ingredient_entry in ingredients:
        if strip_footnotes(ingredient_entry["preferred_term"]).lower() == name.lower():
            return dict(ingredient_entry["concentration"])
    for solution_entry in solutions:
        for ingredient_entry in solution_entry.get("composition", []):
            if strip_footnotes(ingredient_entry["preferred_term"]).lower() == name.lower():
                return dict(ingredient_entry["concentration"])
    return {"value": "variable", "unit": "VARIABLE"}


def parse_composition(
    rows: list[list[str]],
) -> tuple[list[dict], list[dict], list[str], float | dict[str, float] | None]:
    ingredients: list[dict] = []
    solutions_by_name: dict[str, dict] = {}
    preparation: list[str] = []
    ph_value: float | dict[str, float] | None = None
    current_solution: dict | None = None

    for cells in rows:
        if not cells:
            current_solution = None
            continue

        text = cells[0]
        if len(cells) == 1:
            if current_solution is None:
                ph = parse_ph(text)
                if ph is not None:
                    ph_value = ph
                    if not BARE_PH_ROW_RE.fullmatch(text):
                        preparation.append(text)
                    continue
            if text in SOLUTION_HEADERS:
                solution_name = strip_footnotes(text)
                current_solution = solutions_by_name.setdefault(
                    solution_name,
                    {
                        "preferred_term": solution_name,
                        "concentration": solution_dose(
                            solution_name, ingredients, list(solutions_by_name.values())
                        ),
                        "composition": [],
                    },
                )
                continue
            if not ingredients and current_solution is None and not text.startswith("*"):
                ingredients.append(ingredient(text))
                continue
            preparation.append(text)
            continue

        if len(cells) >= 3:
            ing = ingredient(cells[0], cells[-2], cells[-1])
            if current_solution is None:
                ingredients.append(ing)
            else:
                current_solution["composition"].append(ing)

    return ingredients, list(solutions_by_name.values()), preparation, ph_value


def medium_type(ingredients: list[dict]) -> str:
    complex_terms = (
        "Agar",
        "Bacto",
        "blood",
        "Broth",
        "Casitone",
        "Peptone",
        "serum",
        "Yeast extract",
    )
    return (
        "COMPLEX"
        if any(any(term in ing["preferred_term"] for term in complex_terms) for ing in ingredients)
        else "DEFINED"
    )


def physical_state(ingredients: list[dict]) -> str:
    return (
        "SOLID_AGAR"
        if any(
            "agar" in ing["preferred_term"].lower() and "if needed" not in ing["preferred_term"]
            for ing in ingredients
        )
        else "LIQUID"
    )


def recipe(no: int, culturemech_id: str, text: str, timestamp: str) -> dict:
    category, slug = CANDIDATES[no]
    ingredients, solutions, steps, ph_value = parse_composition(composition_rows(text))
    original_name = page_title(text, no)
    out: dict = {
        "id": culturemech_id,
        "name": slug,
        "original_name": original_name,
        "category": category,
        "medium_type": medium_type(ingredients),
        "physical_state": physical_state(ingredients),
        "media_term": {
            "preferred_term": f"NBRC Medium {no}",
            "term": {"id": f"nbrc.medium:{no}", "label": original_name},
        },
        "notes": f"Source: NBRC | Link: {SOURCE_URL.format(no=no)}",
        "ingredients": ingredients,
        "preparation_steps": [
            {"step_number": i, "action": "MIX", "description": step}
            for i, step in enumerate(steps, 1)
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [
            {
                "timestamp": timestamp,
                "curator": "nbrc-live-import",
                "action": "Scraped from NBRC catalogue",
                "notes": (
                    f"Direct import from NBRC Medium {no}. Ingredients captured "
                    "verbatim from the live catalogue."
                ),
            },
            {
                "timestamp": timestamp,
                "curator": "culturemech-id-assigner-v1.0",
                "action": "Assigned CultureMech ID",
                "notes": f"Assigned stable identifier: {culturemech_id}",
            },
        ],
    }
    if isinstance(ph_value, dict):
        out["ph_range"] = ph_value
    elif ph_value is not None:
        out["ph_value"] = ph_value
    if solutions:
        out["solutions"] = solutions
    return out


def merged_recipe(recipe_data: dict, filename: str, timestamp: str) -> dict:
    out = dict(recipe_data)
    fingerprint = RecipeFingerprinter().fingerprint(out)
    out["curation_history"] = [
        *recipe_data["curation_history"],
        {
            "timestamp": timestamp,
            "curator": "merge_recipes.py",
            "action": "MERGED_RECIPES",
            "notes": f"merged 1 source recipe(s) on fingerprint {fingerprint}",
            "source": filename,
        },
    ]
    out["merge_fingerprint"] = fingerprint
    out["merged_from"] = [Path(filename).stem]
    return out


def write_yaml(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--html-dir", type=Path)
    parser.add_argument("--normalized-dir", type=Path, default=REPO / "data/normalized_yaml")
    parser.add_argument("--merged-dir", type=Path, default=REPO / "data/merge_yaml/merged")
    parser.add_argument("--start-id", type=int, default=15898)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    timestamp = datetime.now(timezone.utc).isoformat()
    for offset, no in enumerate(CANDIDATES):
        category, slug = CANDIDATES[no]
        cid = f"CultureMech:{args.start_id + offset:06d}"
        data = recipe(no, cid, source_text(no, args.html_dir), timestamp)
        if not data["ingredients"]:
            raise RuntimeError(f"NBRC Medium {no} parsed without ingredients")
        normalized = args.normalized_dir / category / f"{slug}.yaml"
        merged = args.merged_dir / f"{slug}.yaml"
        if args.dry_run:
            print(f"{cid}\t{no}\t{normalized.relative_to(REPO)}")
            continue
        write_yaml(normalized, data)
        write_yaml(merged, merged_recipe(data, normalized.name, timestamp))
        print(f"{cid}\t{no}\t{normalized.relative_to(REPO)}")


if __name__ == "__main__":
    main()
