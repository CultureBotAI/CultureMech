#!/usr/bin/env python3
"""Recover NBRC composition tables from the preserved source HTML (#299).

62 NBRC records lost their composition on import. The symptoms the audit reports
(`just audit-unparsed-composition`) are all one failure:

    ingredients:
    - preferred_term: ''                                  # name is empty
      concentration: {value: MgSO4·7H2O, unit: G_PER_L}   # the name is HERE
    solutions:
    - preferred_term: MgSO4·7H2O0.5g(NH4)2SO40.4gK2HPO40.2g...
      composition: []                                     # the recipe is gone

## Why this is recovery and not re-parsing

`data/raw/nbrc/nbrc_media.json` is corrupt in exactly the same way — its
`ingredients[0].name` is the same concatenated blob — so the defect is in the
scraper, not the normalizer, and re-importing from the JSON reproduces it.

The scraper's own HTML captures survived, and they are clean. NBRC serves the
composition as a nested table with one cell per field:

    <td colspan='4'>MgSO<sub>4</sub>&middot;7H<sub>2</sub>O</td>
    <td align='right'>0.5</td>
    <td align='left'>g</td>

The blob is what `get_text()` produces from that when called without a separator.
So the delimiters were never in the data we normalized — they are still in the
HTML, and the table is fully reconstructable.

## How rows are classified

By cell count, which is structural rather than a guess about the text:

    3 cells   an ingredient: name, quantity, unit          (1,051 rows)
    1 cell    preparation prose ("Adjust pH to 2.0 ...")     (188 rows)
    0 cells   a spacer                                       (139 rows)

The prose is preserved in `notes` rather than discarded: it is the real
preparation detail, and the generic `preparation_steps` these records carry
("Dissolve ingredients in distilled water") is boilerplate the importer invented.

## Scope

Recovers composition only. The recovered ingredients are **ungrounded** — no
`term`, because a name is not a grounding — so they add no KGX edges by
themselves. What the KG gains immediately is the removal of the blob
`solutions[]` entry, which was minting a garbage node with an edge (31 of them).
Grounding the recovered names is separate work, and `just audit-mim-sssom` is
where it becomes visible.

Dry-run by default. Usage::

    just recover-nbrc-composition                # show what would change
    just recover-nbrc-composition --limit 1      # canary one record
    just recover-nbrc-composition --apply
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml
from bs4 import BeautifulSoup

sys.path.insert(0, str(Path(__file__).resolve().parent))
from record_io import write_record  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
NORMALIZED = REPO_ROOT / "data" / "normalized_yaml"
SCRAPED = REPO_ROOT / "data" / "raw" / "nbrc" / "scraped"
RAW_JSON = REPO_ROOT / "data" / "raw" / "nbrc" / "nbrc_media.json"

CURATOR = "recover_nbrc_composition.py"

# NBRC's unit strings -> ConcentrationUnitEnum. `L` is a real enum member, meant
# for exactly the "Distilled water 1 L" final-volume marker these tables end with.
UNITS = {
    "g": ("G_PER_L", 1),
    "mg": ("MG_PER_L", 1),
    "ml": ("ML_PER_L", 1),
    "l": ("L", 1),
    "mm": ("MILLIMOLAR", 1),
    # No MICROL_PER_L in the enum, and one row in the whole corpus uses it.
    # Converting to ml keeps the quantity exact rather than inventing a unit.
    "μl": ("ML_PER_L", 0.001),
    "ul": ("ML_PER_L", 0.001),
}


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


# A one-cell line opens a sub-section two ways: starred (`*Vitamin solution`,
# `**Trace element solution`) or colon-terminated (`Trace elements:`). NBRC uses
# both, and keying only on the star flattened NBRC_1185's trace-element stock
# into the medium.
#
# Neither marker proves it is a sub-RECIPE. Some starred lines are supplier notes
# ("*Wako Pure Chemical Ind., Ltd., Osaka, Japan") or instructions ("*Sterilize
# separately by filtration."), and colon lines include prose like "Heterotrophic
# growth on yeast extract:". What settles it is whether ingredient rows follow,
# so a section with none is emitted as prose instead.
_SECTION = re.compile(r"^(?:\*+\s*(?P<starred>\S.*)|(?P<titled>\S.*):)$")


def parse_composition(html: str) -> tuple[list[dict[str, Any]],
                                          list[dict[str, Any]], list[str]]:
    """Return ``(ingredients, solutions, prose)`` from one NBRC medium page.

    NBRC nests stock solutions rather than inlining them. A page reads:

        Vitamin solution*            2  ml     <- the medium REFERENCES it
        Trace element solution**     2  ml
        Distilled water              1  L
        *Vitamin solution                      <- then DEFINES it
        Biotin                     0.5  mg
        ...

    Flattening those sub-recipes into the medium's ingredient list is the
    flattened-cocktail defect #150 exists to catch, and it does: a first version
    of this script did exactly that and `audit-concentration-plausibility` gained
    21 rows, `FeCl3·6H2O 1.35 G_PER_L` among them — trace-element STOCK strength
    presented as a final medium concentration, 1000x out.
    """
    soup = BeautifulSoup(html, "html.parser")
    holder = soup.find(id="medium-comp")
    if holder is None:
        return [], [], []
    table = holder.find("table")
    if table is None:
        return [], [], []

    # Split the table into sections at each starred footnote header.
    sections: list[tuple[str | None, list[dict[str, Any]], list[str]]] = [(None, [], [])]
    for row in table.find_all("tr"):
        cells = [clean(cell.get_text()) for cell in row.find_all("td")]
        cells = [cell for cell in cells if cell and cell != "\xa0"]
        if not cells:
            continue
        if len(cells) == 1:
            header = _SECTION.match(cells[0])
            if header:
                title = header.group("starred") or header.group("titled")
                sections.append((title.rstrip(":").strip(), [], []))
            else:
                sections[-1][2].append(cells[0])
            continue
        if len(cells) == 3:
            entry = _ingredient(*cells)
            if entry:
                sections[-1][1].append(entry)
                continue
        # Anything else is text we do not model; keep it rather than drop it.
        sections[-1][2].append(" ".join(cells))

    ingredients = sections[0][1]
    prose = list(sections[0][2])
    solutions: list[dict[str, Any]] = []
    for title, rows, notes in sections[1:]:
        if rows:
            solutions.append({"preferred_term": title, "composition": rows,
                              "name": title})
            prose.extend(notes)
        else:
            # A footnote with no ingredients is a supplier note or an
            # instruction, not a solution.
            prose.append(f"{title} {' '.join(notes)}".strip())
    return ingredients, solutions, prose


def _ingredient(name: str, quantity: str, unit: str) -> dict[str, Any] | None:
    """One ingredient row, or None when the cells are not actually a measurement."""
    mapped = UNITS.get(unit.strip().casefold())
    if not mapped or not name:
        return None
    enum_unit, factor = mapped
    try:
        value = float(quantity.replace(",", ""))
    except ValueError:
        return None
    value *= factor
    # Keep integers integral so the corpus does not gain `1.0` where it had `1`.
    rendered = f"{value:g}"
    return {
        "preferred_term": name,
        "concentration": {"value": rendered, "unit": enum_unit},
    }


def media_number_index(raw_json: Path) -> dict[str, str]:
    """``{record name -> NBRC media number}``.

    The two differ: the page at ``NO=1002`` is titled medium ``1003``, and the
    normalized record takes the title. The HTML files are named by number, so the
    join has to go through this index rather than the record name.
    """
    entries = json.loads(raw_json.read_text(encoding="utf-8"))
    return {str(e.get("media_name")): str(e.get("media_number")) for e in entries
            if e.get("media_name") and e.get("media_number")}


def needs_recovery(doc: dict[str, Any]) -> bool:
    """True when this record shows the #299 signature.

    Deliberately narrow: an empty ingredient name, or a solution whose
    composition is empty while its name carries an amount welded to the next
    reagent. A record that merely looks untidy is left alone.
    """
    for ingredient in doc.get("ingredients") or []:
        if isinstance(ingredient, dict):
            name = ingredient.get("preferred_term")
            if isinstance(name, str) and not name.strip():
                return True
    for solution in doc.get("solutions") or []:
        if not isinstance(solution, dict):
            continue
        name = solution.get("preferred_term") or ""
        if not (solution.get("composition") or []) and len(name) >= 60:
            if re.search(r"\d(?:\.\d+)?\s*(?:mg|ml|kg|g|L|l)(?=[A-Za-z(])", name):
                return True
    return False


def blob_solutions(doc: dict[str, Any]) -> list[int]:
    """Indexes of `solutions[]` entries that are an unparsed table, not a solution."""
    out = []
    for index, solution in enumerate(doc.get("solutions") or []):
        if not isinstance(solution, dict):
            continue
        name = solution.get("preferred_term") or ""
        if not (solution.get("composition") or []) and len(name) >= 60:
            if re.search(r"\d(?:\.\d+)?\s*(?:mg|ml|kg|g|L|l)(?=[A-Za-z(])", name):
                out.append(index)
    return out


def _grounding_index(doc: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """``{normalized name: {term/chebi_term/...}}`` from the record's current rows.

    Four of the 62 records (NBRC_815, 1038, 1245, 1298) carry a fully curated,
    grounded ingredient list alongside the corrupt row that flagged them. A
    wholesale replacement destroyed 26 groundings across them — verified by
    diffing the KGX export, where `has_part` edges to CHEBI, MICRO, FOODON and
    UBERON disappeared alongside the 31 intended blob removals.
    """
    index: dict[str, dict[str, Any]] = {}
    for ingredient in doc.get("ingredients") or []:
        if not isinstance(ingredient, dict):
            continue
        name = ingredient.get("preferred_term")
        if not isinstance(name, str) or not name.strip():
            continue
        carried = {key: ingredient[key] for key in CARRIED_SLOTS if key in ingredient}
        if carried:
            index[_match_key(name)] = carried
    return index


def _match_key(name: str) -> str:
    return re.sub(r"[\s\-_]+", " ", name.strip().casefold())


# Curation that belongs to the ingredient, not to the composition table, and so
# must survive a re-parse of the table.
CARRIED_SLOTS = ("term", "chebi_term", "mediaingredientmech_chebi_term",
                 "mediaingredientmech_term", "nutritional_roles",
                 "physicochemical_roles", "cellular_metabolic_roles", "evidence")


def has_curated_composition(doc: dict[str, Any]) -> bool:
    """True when the record already holds a real, grounded ingredient list.

    Four of the 62 (NBRC_815, 1038, 1245, 1298) do, and for them the HTML is a
    DOWNGRADE rather than a recovery: NBRC_1245 carries a curated expansion —
    `Calf brains`, `Beef heart`, `Proteose peptone`, `Dextrose` — where the NBRC
    page lists only the commercial premix, `Bacto Brain Heart Infusion (Difco)`.
    Replacing that destroyed 26 groundings, which the KGX export made visible as
    `has_part` edges to CHEBI, MICRO, FOODON and UBERON vanishing alongside the
    31 intended blob removals.

    Grounding is the signal, not row count. In the other 58 records the only
    "named" ingredient IS the blob — `Tryptone5gYeast extract3gNaCl10g...` with a
    VARIABLE concentration — so there is nothing to preserve.
    """
    for ingredient in doc.get("ingredients") or []:
        if not isinstance(ingredient, dict):
            continue
        name = ingredient.get("preferred_term")
        if not isinstance(name, str) or not name.strip():
            continue
        if (ingredient.get("term") or {}).get("id") or \
                (ingredient.get("chebi_term") or {}).get("id"):
            return True
    return False


def recover(doc: dict[str, Any], ingredients: list[dict[str, Any]],
            solutions: list[dict[str, Any]], prose: list[str],
            number: str) -> tuple[dict[str, Any], str]:
    """Apply the fix in place; return the record and which mode was used."""
    if has_curated_composition(doc):
        # Surgical: strip only the corrupt rows, keep the curated list.
        mode = "surgical"
        doc["ingredients"] = [
            i for i in doc.get("ingredients") or []
            if not (isinstance(i, dict)
                    and isinstance(i.get("preferred_term"), str)
                    and not i["preferred_term"].strip())
        ]
    else:
        mode = "recovered"
        existing = _grounding_index(doc)
        for ingredient in ingredients:
            match = existing.get(_match_key(ingredient["preferred_term"]))
            if match:
                ingredient.update(match)
        doc["ingredients"] = ingredients

    dropped = blob_solutions(doc)
    if dropped:
        doc["solutions"] = [s for i, s in enumerate(doc["solutions"])
                            if i not in set(dropped)]
        if not doc["solutions"]:
            del doc["solutions"]

    # Attach the sub-recipes NBRC defines as footnotes, nested rather than
    # flattened into the medium. Only in recovery mode: a curated record's own
    # solutions are not ours to replace.
    if mode == "recovered" and solutions:
        doc["solutions"] = list(doc.get("solutions") or []) + solutions

    if prose and mode == "recovered":
        text = " ".join(prose)
        existing = str(doc.get("notes") or "").strip()
        doc["notes"] = f"{existing} {text}".strip() if existing else text

    doc.setdefault("curation_history", []).append({
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "curator": CURATOR,
        "action": ("Recovered composition from source HTML" if mode == "recovered"
                   else "Removed corrupt rows, kept curated composition"),
        "notes": ((f"Re-parsed the NBRC medium {number} composition table from the "
                   f"preserved scrape; {len(doc['ingredients'])} ingredient(s) "
                   f"restored, {len(solutions)} stock solution(s) nested rather "
                   f"than flattened, {len(dropped)} unparsed solution blob(s) "
                   f"removed (#299).") if mode == "recovered" else
                  (f"Record already held a grounded ingredient list, so the NBRC "
                   f"medium {number} page was NOT used — it lists only the "
                   f"commercial premix. Dropped the empty-name row and "
                   f"{len(dropped)} unparsed solution blob(s) (#299).")),
    })
    return doc, mode


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--scraped-dir", type=Path, default=SCRAPED)
    parser.add_argument("--raw-json", type=Path, default=RAW_JSON)
    parser.add_argument("--limit", type=int, default=0,
                        help="Stop after N records. Use 1 to canary.")
    parser.add_argument("--apply", action="store_true",
                        help="Write the records. Without this, nothing is changed.")
    args = parser.parse_args(argv if argv is not None else sys.argv[1:])

    if not args.scraped_dir.is_dir():
        raise SystemExit(
            f"Preserved scrape not found at {args.scraped_dir}.\n"
            "It is gitignored, so this recovery only runs on a machine that has it."
        )
    index = media_number_index(args.raw_json)

    changed = skipped = missing = surgical = 0
    for path in sorted(args.normalized_dir.glob("*/*.yaml")):
        if not path.name.startswith("NBRC_"):
            continue
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(doc, dict) or not needs_recovery(doc):
            continue

        number = index.get(str(doc.get("name")))
        page = args.scraped_dir / f"media_{number}.html" if number else None
        if page is None or not page.exists():
            print(f"  MISSING PAGE  {path.name} (name={doc.get('name')!r})")
            missing += 1
            continue

        ingredients, solutions, prose = parse_composition(
            page.read_text(encoding="utf-8"))
        if not ingredients:
            print(f"  NO TABLE      {path.name}")
            skipped += 1
            continue

        before = len(doc.get("ingredients") or [])
        _doc, mode = recover(doc, ingredients, solutions, prose, number)
        changed += 1
        if mode == "surgical":
            surgical += 1
        nested = len(solutions) if mode == "recovered" else 0
        print(f"  {path.name:<22} {before} -> {len(doc['ingredients'])} ingredients"
              f"{f', {nested} nested solution(s)' if nested else ''}  [{mode}]")
        if args.apply:
            write_record(path, doc)
        if args.limit and changed >= args.limit:
            break

    verb = "Recovered" if args.apply else "Would recover"
    print(f"\n{verb} {changed} record(s): {changed - surgical} re-parsed from the "
          f"preserved HTML, {surgical} repaired surgically because they already "
          f"held a grounded list. {skipped} without a table, {missing} without a "
          f"page.")
    if not args.apply:
        print("Dry run — nothing written. Re-run with --apply.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
