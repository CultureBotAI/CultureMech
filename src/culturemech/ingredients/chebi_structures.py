"""Read-only access to the packaged ChEBI structure table.

`chemical_formula` and `molecular_weight` exist on `IngredientDescriptor` but
are populated on 0 of 170,007 ingredients, so the rendered ingredient tables
carried no chemical information at all. 85% of those ingredients do carry a
ChEBI id, and those ids collapse to 640 distinct terms.

A formula is a property of the ChEBI term, not of the recipe citing it, so it
lives here once rather than being copied into every record that cites the term.
Build the table with `scripts/fetch_chebi_properties.py`.

A record that asserts its own `chemical_formula` still wins: `structure_for`
prefers what the record says over what the table knows, because a record can
legitimately describe a hydrate or a specific salt the generic term does not.
"""

from __future__ import annotations

import csv
from collections.abc import Mapping
from dataclasses import dataclass
from functools import lru_cache
from importlib import resources
from typing import Any

# Traversed from the `culturemech` package rather than named as
# `culturemech.data.chebi`: the data directories carry no `__init__.py`, so
# they are not importable packages. This mirrors `mim_label_index.from_package`.
_RESOURCE_DIR = ("data", "chebi")
_INDEX_NAME = "structure_index.csv"
HEADER = ["chebi_id", "label", "formula", "molecular_weight", "charge"]


@dataclass(frozen=True)
class Structure:
    """What ChEBI asserts about one term. Empty strings mean "not asserted"."""

    chebi_id: str
    label: str
    formula: str
    molecular_weight: str
    charge: str

    def __bool__(self) -> bool:
        """Falsy when there is nothing worth rendering."""
        return bool(self.formula or self.molecular_weight)


class StructureIndexError(RuntimeError):
    """The packaged table is missing or malformed."""


@lru_cache(maxsize=1)
def load() -> dict[str, Structure]:
    """The packaged table, keyed by CHEBI CURIE. Cached; the file is immutable."""
    root = resources.files("culturemech")
    for component in _RESOURCE_DIR:
        root = root.joinpath(component)
    try:
        text = root.joinpath(_INDEX_NAME).read_text(encoding="utf-8")
    except (FileNotFoundError, ModuleNotFoundError) as error:
        raise StructureIndexError(
            f"culturemech/{'/'.join(_RESOURCE_DIR)}/{_INDEX_NAME} is not packaged. "
            f"Build it with scripts/fetch_chebi_properties.py --apply."
        ) from error

    reader = csv.DictReader(text.splitlines())
    if reader.fieldnames != HEADER:
        raise StructureIndexError(
            f"{_INDEX_NAME} header is {reader.fieldnames}, expected {HEADER}"
        )

    table: dict[str, Structure] = {}
    for row in reader:
        identifier = (row.get("chebi_id") or "").strip()
        if not identifier:
            continue
        table[identifier] = Structure(
            chebi_id=identifier,
            label=(row.get("label") or "").strip(),
            formula=(row.get("formula") or "").strip(),
            molecular_weight=(row.get("molecular_weight") or "").strip(),
            charge=(row.get("charge") or "").strip(),
        )
    return table


def structure_for(ingredient: Mapping[str, Any] | None) -> Structure | None:
    """The structure to display for one ingredient, or None when there is none.

    What the record itself asserts takes precedence over the shared term, since
    a record may name a hydrate or a particular salt the generic ChEBI term
    does not distinguish.
    """
    if not isinstance(ingredient, Mapping):
        return None

    identifier = ""
    term = ingredient.get("term")
    if isinstance(term, Mapping):
        identifier = str(term.get("id") or "")

    shared = load().get(identifier) if identifier.startswith("CHEBI:") else None

    own_formula = str(ingredient.get("chemical_formula") or "").strip()
    own_weight = ingredient.get("molecular_weight")
    own_weight = "" if own_weight is None else str(own_weight).strip()
    if not own_formula and not own_weight:
        return shared or None

    return Structure(
        chebi_id=identifier,
        label=shared.label if shared else "",
        formula=own_formula or (shared.formula if shared else ""),
        molecular_weight=own_weight or (shared.molecular_weight if shared else ""),
        charge=shared.charge if shared else "",
    )
