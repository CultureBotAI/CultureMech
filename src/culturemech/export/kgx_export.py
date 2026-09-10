"""
KGX edge exporter for CultureMech.

Transforms media recipe YAML files into KGX-format edges for the knowledge graph.
Follows the dismech pattern and cmm-ai-automation semantic modeling.

Semantic Model (following cmm-ai-automation):
==============================================

Primary Edges:
--------------
1. Organism (NCBITaxon) → grows_in_medium (METPO:2000517) → Medium
   - Subject: Organism/Taxon
   - Predicate: METPO:2000517 (grows in)
   - Object: Medium
   - Qualifiers: strain, growth_phase

2. Medium → has_part (biolink:has_part) → Solution
   - Subject: Medium
   - Predicate: biolink:has_part
   - Object: Solution
   - Qualifiers: concentration (volume added)

3. Solution → has_part (biolink:has_part) → Ingredient (MIM-resolved identity)
   - Subject: Solution
   - Predicate: biolink:has_part
   - Object: Ingredient (MIM-resolved ontology or registry CURIE)
   - Qualifiers: concentration, role

4. Medium → has_part (biolink:has_part) → Ingredient (MIM-resolved identity)
   - Subject: Medium
   - Predicate: biolink:has_part
   - Object: Ingredient (MIM-resolved ontology or registry CURIE)
   - Qualifiers: concentration, role

5. Medium → has_attribute (biolink:has_attribute) → Medium Type
   - Subject: Medium
   - Predicate: biolink:has_attribute
   - Object: Type node (e.g., CultureMech:medium_type_COMPLEX)
   - Qualifiers: attribute_type = "medium_type"

Legacy Edges (for backward compatibility):
-------------------------------------------
6. Medium → has_application → Use case
7. Medium → has_physical_state → State
8. Dataset → uses_medium → Medium
9. Medium → has_database_reference → Database ID
10. Variant → variant_of → Base Medium
"""

import hashlib
import os
import re
import uuid
from collections.abc import Callable, Iterator, Mapping
from dataclasses import asdict, dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any

from culturemech.ingredients.mim_label_index import GroundingDecision, resolve_ingredient

try:
    import koza
    from koza import KozaTransform

    KOZA_AVAILABLE = True
except ImportError:
    KOZA_AVAILABLE = False
    print("Warning: Koza not installed. Install with: pip install koza")

# No biolink import. The export used to route every edge through
# `biolink_model`'s `Association`, which is exactly what broke it: that class
# declares `qualifiers: list[str] | None`, so each of our qualifier dicts raised
# and the edge was dropped. Rows are plain dataclasses now (see `Node` and
# `Edge`), the biolink vocabulary lives in the category and predicate strings,
# and the module no longer needs the package at import time.

KNOWLEDGE_SOURCE = "infores:culturemech"
# The one CURIE prefix for every id this export mints. Record nodes carry the
# record's own `CultureMech:NNNNNN`, so the auxiliary nodes use the same prefix
# rather than a lower-cased twin of it (#440). The schema's `culturemech:` is the
# LinkML class-URI prefix, a different artifact; both expand to
# https://w3id.org/culturemech/, which is the mapping kg-microbe should register.
PREFIX = "CultureMech"
NAMESPACE_UUID = uuid.uuid5(uuid.NAMESPACE_URL, "https://w3id.org/culturemech")

# A standalone stock-solution record is recognised by the same two explicit
# signals scripts/record_kinds.py uses: a curated `record_kind: SOLUTION`, or an
# upstream solution id in `term.id`. Shape heuristics would also match malformed
# media, so neither side uses them.
_SOLUTION_TERM_PREFIXES = ("mediadive.solution:", "MediaIngredientMech:")


def record_node_id(record: dict[str, Any]) -> str:
    """The node id for a record: its own permanent CultureMech identifier.

    Until #438 this was ``culturemech:{sanitized name}``, and node emission dedupes
    on id, so records sharing a name collapsed into one node with merged edges:
    3,181 media and 4,787 solutions on the 2026-09-09 corpus. The 4,784 MediaDive
    solution records carry ``preferred_term`` and no ``name`` at all, so every one
    of them sanitized to the empty string and none emitted a node.

    ``id`` is required by the schema, immutable, never reused, and pinned by
    ``just check-id-catalog``; it is the only identifier a node can safely carry.
    A record without one is a data error, not a case to paper over with a name.
    """
    record_id = record.get("id")
    if not isinstance(record_id, str) or not record_id.strip():
        raise ValueError(
            f"record has no id (name={record.get('name')!r}, "
            f"preferred_term={record.get('preferred_term')!r}); every record must "
            "carry its permanent CultureMech identifier"
        )
    return record_id.strip()


def record_label(record: dict[str, Any]) -> str:
    """Display label: ``name`` for media, ``preferred_term`` for solution records."""
    for key in ("name", "preferred_term", "original_name"):
        value = record.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return record_node_id(record)


def is_solution_record(record: dict[str, Any]) -> bool:
    """True for a standalone stock-solution record (see scripts/record_kinds.py)."""
    if record.get("record_kind") == "SOLUTION":
        return True
    term = record.get("term")
    tid = term.get("id") if isinstance(term, dict) else None
    return isinstance(tid, str) and tid.startswith(_SOLUTION_TERM_PREFIXES)


# Predicates following cmm-ai-automation schema
GROWS_IN_MEDIUM = "METPO:2000517"  # grows in
HAS_PART = "biolink:has_part"  # For medium→ingredient, solution→ingredient
HAS_SOLUTION_COMPONENT = "biolink:has_part"  # For medium→solution (also uses has_part)


# ================================================================
# PURE TRANSFORM FUNCTION (testable without Koza)
# ================================================================


IngredientResolver = Callable[[Mapping[str, Any]], GroundingDecision]


def transform(
    record: dict[str, Any],
    ingredient_resolver: IngredientResolver = resolve_ingredient,
) -> Iterator[dict[str, Any]]:
    """
    Pure transform function - testable without Koza.

    Extracts edges from a media recipe following cmm-ai-automation semantic modeling:
    1. organism → medium (grows_in_medium: METPO:2000517)
    2. medium → solution (has_part)
    3. solution → ingredient (has_part)
    4. medium → ingredient (has_part); a solution record's own composition too
    5. medium → type (as node attribute via has_attribute)
    6. Medium → has_application → Use case (legacy)
    7. Medium → has_physical_state → State (legacy)
    8. Dataset → uses_medium → Medium (legacy)
    9. Medium → has_database_reference → Database ID (legacy)
    10. Variant → variant_of → Base Medium (legacy)
    """
    medium_id = record_node_id(record)

    # NEW: Edge Type 1: Organism → Medium (grows_in_medium)
    for organism in record.get("target_organisms", []):
        edge = organism_grows_in_medium_edge(organism, medium_id)
        if edge:
            yield edge

    # NEW: Edge Type 2: Medium → Solution (has_solution_component)
    for solution in record.get("solutions", []):
        target, minted = nested_solution_target(solution)
        if not target:
            continue
        edge = medium_to_solution_edge(medium_id, solution, target)
        if edge:
            yield edge

        # NEW: Edge Type 3: Solution → Ingredient (has_part). Only for a node we
        # mint here: a solution record exports its own composition (#442), and
        # the nested references that resolve to one carry none anyway (#441).
        if not minted:
            continue
        for ingredient in solution.get("composition", []):
            edge = solution_to_ingredient_edge(
                target, ingredient, ingredient_resolver=ingredient_resolver
            )
            if edge:
                yield edge

    # Edge Type 4: Medium → Ingredient (has_part)
    for ingredient in record.get("ingredients", []):
        edge = medium_to_ingredient_edge(
            medium_id, ingredient, ingredient_resolver=ingredient_resolver
        )
        if edge:
            yield edge

    # Edge Type 4b: a stock-solution record's own composition (has_part). A
    # SolutionRecipe-shaped record keeps its reagents in top-level `composition`,
    # not `ingredients`; the 4,784 MediaDive solution records carry 35,009 such
    # rows, all grounded, and until #442 none reached the graph. Their
    # `ingredients` list is a single ungrounded placeholder, so walking both
    # emits nothing twice.
    for ingredient in record.get("composition", []) or []:
        edge = medium_to_ingredient_edge(
            medium_id, ingredient, ingredient_resolver=ingredient_resolver
        )
        if edge:
            yield edge

    # NEW: Edge Type 5: Medium → Type (as node attribute). A medium's attribute,
    # so a stock-solution record (202 carry a medium_type) does not get one (#442).
    medium_type = record.get("medium_type")
    if medium_type and not is_solution_record(record):
        edge = medium_to_type_edge(medium_id, medium_type)
        if edge:
            yield edge

    # LEGACY: Edge Type 6: Medium → Applications
    for application in record.get("applications", []):
        edge = application_to_edge(medium_id, application)
        if edge:
            yield edge

    # LEGACY: Edge Type 7: Medium → Physical State
    physical_state = record.get("physical_state")
    if physical_state:
        edge = physical_state_to_edge(medium_id, physical_state)
        if edge:
            yield edge

    # LEGACY: Edge Type 8: Dataset → Medium
    for dataset in record.get("datasets", []):
        edge = dataset_to_edge(medium_id, dataset)
        if edge:
            yield edge

    # LEGACY: Edge Type 9: Medium → Database Reference
    media_term = record.get("media_term", {})
    if media_term.get("term"):
        edge = database_reference_to_edge(medium_id, media_term["term"])
        if edge:
            yield edge

    # LEGACY: Edge Type 10: Variant → Base Medium
    for variant in record.get("variants", []):
        edge = variant_to_edge(medium_id, variant)
        if edge:
            yield edge


# ================================================================
# NODE EXTRACTION (#294)
# ================================================================
#
# The transform used to yield edges only, so every id CultureMech mints itself
# was a dangling reference in any nodes.tsv — four of the five distinct ids in a
# single lb_broth record.
#
# We declare nodes for the six id shapes we mint and NOTHING else. CHEBI,
# NCBITaxon, MICRO, FOODON and TOGO objects are supplied by KG-Microbe's ontology
# ingests, which carry the authoritative labels; minting half-populated rows for
# them here would put a competing, name-less node into the merge.
#
# Categories are taken from the consumer rather than invented. kg-microbe fixes
# them in kg_microbe/transform_utils/constants.py, and a medium node that does
# not match what the loader expects is worse than no node at all.

GROWTH_MEDIUM = "biolink:GrowthMedium"
CHEMICAL_MIXTURE = "biolink:ChemicalMixture"
COMPLEX_MOLECULAR_MIXTURE = "biolink:ComplexMolecularMixture"
ATTRIBUTE = "biolink:Attribute"

# medium_type -> (medium node category, medium-type node category), mirroring
# kg-microbe's MEDIUM_DEFINED_CATEGORY / MEDIUM_COMPLEX_CATEGORY pair. Values
# outside this table (BUFFER, NEGATIVE_CONTROL, and the functional-role values
# MediumTypeEnum still permits) fall back to the generic categories rather than
# guessing at a composition they do not assert.
_MEDIUM_TYPE_CATEGORIES = {
    "DEFINED": ([GROWTH_MEDIUM, CHEMICAL_MIXTURE], [CHEMICAL_MIXTURE]),
    "COMPLEX": ([GROWTH_MEDIUM, COMPLEX_MOLECULAR_MIXTURE], [COMPLEX_MOLECULAR_MIXTURE]),
}
_DEFAULT_MEDIUM_CATEGORY = [GROWTH_MEDIUM]
_DEFAULT_MEDIUM_TYPE_CATEGORY = [CHEMICAL_MIXTURE]


@dataclass
class Node:
    """A KGX node row.

    Deliberately a plain dataclass rather than a biolink pydantic model. The
    installed biolink_model has no ``GrowthMedium`` class, and its classes pin
    ``category`` to a per-class literal, so ``NamedThing(category=[...])`` raises
    for every value we need. Koza supports this: ``KGXConverter.convert_node``
    falls back to ``asdict()`` for non-BaseModel entities, and ``split_entities``
    classifies anything carrying ``id`` and ``name`` (and no
    subject/predicate/object) as a node.
    """

    id: str
    category: list[str]
    name: str
    provided_by: str = KNOWLEDGE_SOURCE


# Qualifier CURIE -> KGX column. The transform models qualifiers as
# `{"qualifier_type_id": ..., "qualifier_value": ...}` dicts, which is the
# in-memory shape the unit tests assert on, but biolink's `Association.qualifiers`
# is `list[str] | None` — so `Association(**edge_dict)` raised for every qualified
# edge and the wrapper swallowed it with a print. The koza path had never run, so
# nobody saw it: a 249-record canary produced 10 edges out of ~1,500.
#
# Flattening into named columns rather than stuffing `key=value` strings into
# `qualifiers` keeps the values usable from a TSV, which is the point of the
# export.
_QUALIFIER_COLUMNS = {
    "biolink:concentration": "concentration",
    "biolink:role": "role",
    "biolink:strain": "strain",
    "biolink:growth_phase": "growth_phase",
    "biolink:attribute_type": "attribute_type",
    "biolink:relationship_type": "relationship_type",
}


@dataclass
class Edge:
    """A KGX edge row, with qualifiers flattened into columns.

    A plain dataclass for the same reason as ``Node``: koza's
    ``convert_association`` falls back to ``asdict()`` for non-BaseModel
    entities, and ``split_entities`` classifies anything with
    subject/object/predicate as an edge. Going through biolink's ``Association``
    would drop every qualified edge.
    """

    id: str
    subject: str
    predicate: str
    object: str
    category: str = "biolink:Association"
    primary_knowledge_source: str = KNOWLEDGE_SOURCE
    knowledge_level: str = "knowledge_assertion"
    agent_type: str = "manual_validation_of_automated_agent"
    publications: list[str] | None = None
    concentration: str | None = None
    # The quantity as two typed columns, the shape kg-microbe already ingests
    # from the MediaDive transform (#445). `concentration` keeps the joined
    # string for one release so no reader breaks on the same day.
    value: str | None = None
    unit: str | None = None
    role: str | None = None
    strain: str | None = None
    growth_phase: str | None = None
    attribute_type: str | None = None
    relationship_type: str | None = None


def to_edge(edge_dict: dict[str, Any]) -> Edge:
    """Turn one ``transform`` dict into a writable KGX edge row.

    Unknown qualifier types are dropped rather than silently mangled into an
    existing column; ``_QUALIFIER_COLUMNS`` is the declared contract and
    ``test_every_qualifier_type_has_a_column`` fails if the transform grows a
    type this does not cover.
    """
    columns: dict[str, Any] = {}
    for qualifier in edge_dict.get("qualifiers") or []:
        column = _QUALIFIER_COLUMNS.get(qualifier.get("qualifier_type_id", ""))
        if column:
            columns[column] = qualifier.get("qualifier_value")
    return Edge(
        id=edge_dict["id"],
        subject=edge_dict["subject"],
        predicate=edge_dict["predicate"],
        object=edge_dict["object"],
        publications=edge_dict.get("publications") or None,
        value=edge_dict.get("value"),
        unit=edge_dict.get("unit"),
        **columns,
    )


def nodes(record: dict[str, Any]) -> Iterator[dict[str, Any]]:
    """Every node this record mints, as dicts. Companion to ``transform``.

    Yields duplicates across records by design — ``CultureMech:medium_type_COMPLEX``
    belongs to all 8,850 COMPLEX media. Deduplication is the writer's job (see
    ``koza_transform``), because it is a property of the run, not of the record.
    """
    medium_id = record_node_id(record)
    name = record_label(record)
    medium_type = record.get("medium_type")

    medium_category, type_category = _MEDIUM_TYPE_CATEGORIES.get(
        str(medium_type or ""),
        (_DEFAULT_MEDIUM_CATEGORY, _DEFAULT_MEDIUM_TYPE_CATEGORY),
    )
    # A stock-solution record is a mixture, not a growth medium, matching the
    # `mediadive.solution:*` nodes kg-microbe already carries (#374).
    solution = is_solution_record(record)
    if solution:
        medium_category = [CHEMICAL_MIXTURE]

    yield asdict(Node(id=medium_id, category=medium_category, name=name))

    if medium_type and not solution:
        yield asdict(
            Node(
                id=f"{PREFIX}:medium_type_{medium_type}",
                category=type_category,
                name=str(medium_type),
            )
        )

    for solution in record.get("solutions", []) or []:
        target, minted = nested_solution_target(solution)
        if target and minted:
            yield asdict(
                Node(
                    id=target,
                    category=[CHEMICAL_MIXTURE],
                    name=str(solution.get("preferred_term")),
                )
            )

    for application in record.get("applications", []) or []:
        if application:
            yield asdict(
                Node(
                    id=f"{PREFIX}:application_{_sanitize_id(str(application))}",
                    category=[ATTRIBUTE],
                    name=str(application),
                )
            )

    physical_state = record.get("physical_state")
    if physical_state:
        yield asdict(
            Node(
                id=f"{PREFIX}:state_{str(physical_state).lower()}",
                category=[ATTRIBUTE],
                name=str(physical_state),
            )
        )

    # A variant is itself a medium, so it takes the generic medium category — the
    # variant entry carries no medium_type of its own to refine it with.
    for variant in record.get("variants", []) or []:
        variant_name = variant.get("name")
        if variant_name:
            yield asdict(
                Node(
                    id=f"{PREFIX}:variant_{_sanitize_id(str(variant_name))}",
                    category=_DEFAULT_MEDIUM_CATEGORY,
                    name=str(variant_name),
                )
            )


# ================================================================
# EDGE EXTRACTION FUNCTIONS (following cmm-ai-automation semantic model)
# ================================================================


def organism_grows_in_medium_edge(organism: dict, medium_id: str) -> dict | None:
    """
    Organism (NCBITaxon) → grows_in_medium (METPO:2000517) → Medium

    Following cmm-ai-automation pattern:
    - subject: organism (NCBITaxon ID from organism.term.id)
    - predicate: METPO:2000517 (grows in)
    - object: medium (culturemech ID)

    Data preserved: Organism ID, strain info (as qualifier), evidence
    """
    org_id = _get_term_id(organism, ["term", "id"])
    if not org_id:
        return None

    qualifiers = []

    # Add strain as qualifier if present
    strain = organism.get("strain")
    if strain:
        qualifiers.append({"qualifier_type_id": "biolink:strain", "qualifier_value": strain})

    # Add growth phase as qualifier if present
    growth_phase = organism.get("growth_phase")
    if growth_phase:
        qualifiers.append(
            {"qualifier_type_id": "biolink:growth_phase", "qualifier_value": growth_phase}
        )

    pubs, _ = _format_evidence(organism.get("evidence"))

    return _make_association(
        subject=org_id,  # Organism is subject
        predicate=GROWS_IN_MEDIUM,  # METPO:2000517
        obj=medium_id,  # Medium is object
        qualifiers=qualifiers if qualifiers else None,
        publications=pubs if pubs else None,
    )


def medium_to_solution_edge(
    medium_id: str, solution: dict, solution_id: str | None = None
) -> dict | None:
    """
    Medium → has_solution_component (biolink:has_part) → Solution

    Following cmm-ai-automation pattern:
    - subject: medium
    - predicate: biolink:has_part
    - object: solution

    Qualifiers:
    - concentration: volume added per liter

    Data preserved: Solution reference, concentration
    """
    if solution_id is None:
        solution_id, _minted = nested_solution_target(solution)
    if not solution_id:
        return None

    qualifiers, value, unit = _quantity(solution.get("concentration"))

    return _make_association(
        subject=medium_id,
        predicate=HAS_SOLUTION_COMPONENT,  # biolink:has_part
        obj=solution_id,
        qualifiers=qualifiers if qualifiers else None,
        value=value,
        unit=unit,
    )


def solution_to_ingredient_edge(
    solution_id: str,
    ingredient: dict,
    ingredient_resolver: IngredientResolver = resolve_ingredient,
) -> dict | None:
    """
    Solution → has_part (biolink:has_part) → Ingredient (MIM-resolved identity)

    Following cmm-ai-automation pattern:
    - subject: solution
    - predicate: biolink:has_part
    - object: ingredient (ontology, registry, or curated identity)

    Qualifiers:
    - concentration: amount in solution
    - role: functional role

    Data preserved: Chemical ID, concentration, role
    """
    chem_id = _resolved_ingredient_id(ingredient, ingredient_resolver)
    if not chem_id:
        return None

    qualifiers, value, unit = _quantity(ingredient.get("concentration"))

    # Combine role tokens across the three facet slots (facet vocabulary
    # replaced the retired flat `role: IngredientRoleEnum` slot). Preserves
    # the biolink:role qualifier surface while sourcing from the new schema.
    roles = []
    for slot in ("nutritional_roles", "physicochemical_roles", "cellular_metabolic_roles"):
        slot_values = ingredient.get(slot) or []
        if isinstance(slot_values, list):
            roles.extend(slot_values)
        else:
            roles.append(slot_values)
    if roles:
        qualifiers.append(
            {"qualifier_type_id": "biolink:role", "qualifier_value": ", ".join(roles)}
        )

    return _make_association(
        subject=solution_id,
        predicate=HAS_PART,  # biolink:has_part
        obj=chem_id,
        qualifiers=qualifiers if qualifiers else None,
        value=value,
        unit=unit,
    )


def medium_to_ingredient_edge(
    medium_id: str,
    ingredient: dict,
    ingredient_resolver: IngredientResolver = resolve_ingredient,
) -> dict | None:
    """
    Medium → has_part (biolink:has_part) → Ingredient (MIM-resolved identity)

    Following cmm-ai-automation pattern (renamed from ingredient_to_edge):
    - subject: medium
    - predicate: biolink:has_part
    - object: ingredient (ontology, registry, or curated identity)

    Qualifiers:
    - concentration: amount
    - role: functional role

    Data preserved: Chemical ID, concentration, role
    Data lost: Supplier info, preparation notes, chemical formula
    """
    chem_id = _resolved_ingredient_id(ingredient, ingredient_resolver)
    if not chem_id:
        return None

    qualifiers, value, unit = _quantity(ingredient.get("concentration"))

    # Combine role tokens across the three facet slots (facet vocabulary
    # replaced the retired flat `role: IngredientRoleEnum` slot). Preserves
    # the biolink:role qualifier surface while sourcing from the new schema.
    roles = []
    for slot in ("nutritional_roles", "physicochemical_roles", "cellular_metabolic_roles"):
        slot_values = ingredient.get(slot) or []
        if isinstance(slot_values, list):
            roles.extend(slot_values)
        else:
            roles.append(slot_values)
    if roles:
        qualifiers.append(
            {"qualifier_type_id": "biolink:role", "qualifier_value": ", ".join(roles)}
        )

    pubs, _ = _format_evidence(ingredient.get("evidence"))

    return _make_association(
        subject=medium_id,
        predicate=HAS_PART,  # biolink:has_part
        obj=chem_id,
        qualifiers=qualifiers if qualifiers else None,
        value=value,
        unit=unit,
        publications=pubs if pubs else None,
    )


def medium_to_type_edge(medium_id: str, medium_type: str) -> dict | None:
    """
    Medium → has_attribute → Medium Type

    Creates a type attribute node:
    - subject: medium
    - predicate: biolink:has_attribute
    - object: type node (e.g., CultureMech:medium_type_COMPLEX)

    Data preserved: Medium type classification (COMPLEX, DEFINED, etc.)
    """
    type_id = f"{PREFIX}:medium_type_{medium_type}"

    return _make_association(
        subject=medium_id,
        predicate="biolink:has_attribute",
        obj=type_id,
        qualifiers=[
            {"qualifier_type_id": "biolink:attribute_type", "qualifier_value": "medium_type"}
        ],
    )


def ingredient_to_edge(
    medium_id: str,
    ingredient: dict,
    ingredient_resolver: IngredientResolver = resolve_ingredient,
) -> dict | None:
    """
    Medium (CultureMech:000001) → has_part → Glucose (CHEBI:17234)

    Qualifiers:
    - concentration: 10 g/L

    Data preserved: Chemical ID, concentration
    Data lost: Supplier info, preparation notes, chemical formula
    """
    chem_id = _resolved_ingredient_id(ingredient, ingredient_resolver)
    if not chem_id:
        return None

    qualifiers, value, unit = _quantity(ingredient.get("concentration"))

    pubs, _ = _format_evidence(ingredient.get("evidence"))

    return _make_association(
        subject=medium_id,
        predicate="biolink:has_part",
        obj=chem_id,
        qualifiers=qualifiers if qualifiers else None,
        value=value,
        unit=unit,
        publications=pubs if pubs else None,
    )


def organism_to_edge(medium_id: str, organism: dict) -> dict | None:
    """
    LEGACY: Medium → supports_growth_of → Organism (NCBITaxon)

    NOTE: This function is deprecated. Use organism_grows_in_medium_edge() instead,
    which follows the cmm-ai-automation pattern with correct subject/object order:
    Organism → grows_in_medium (METPO:2000517) → Medium

    Data preserved: Organism ID, evidence
    Data lost: Strain, growth phase details
    """
    org_id = _get_term_id(organism, ["term", "id"])
    if not org_id:
        return None

    pubs, _ = _format_evidence(organism.get("evidence"))

    return _make_association(
        subject=medium_id,
        predicate="biolink:affects",  # Legacy predicate
        obj=org_id,
        publications=pubs if pubs else None,
    )


def application_to_edge(medium_id: str, application: str) -> dict | None:
    """
    Medium → has_application → Use case

    Data preserved: Application description
    """
    # Create a synthetic ID for the application
    app_id = f"{PREFIX}:application_{_sanitize_id(application)}"

    return _make_association(
        subject=medium_id,
        predicate="biolink:has_attribute",
        obj=app_id,
        qualifiers=[
            {"qualifier_type_id": "biolink:attribute_type", "qualifier_value": "application"}
        ],
    )


def physical_state_to_edge(medium_id: str, physical_state: str) -> dict | None:
    """
    Medium → has_physical_state → State

    Data preserved: Physical state
    """
    state_id = f"{PREFIX}:state_{physical_state.lower()}"

    return _make_association(
        subject=medium_id,
        predicate="biolink:has_attribute",
        obj=state_id,
        qualifiers=[
            {"qualifier_type_id": "biolink:attribute_type", "qualifier_value": "physical_state"}
        ],
    )


def dataset_to_edge(medium_id: str, dataset: dict) -> dict | None:
    """
    Dataset → uses_medium → Medium

    Data preserved: Dataset ID
    """
    dataset_id = dataset.get("dataset_id")
    if not dataset_id:
        return None

    return _make_association(
        subject=dataset_id,
        predicate="biolink:related_to",
        obj=medium_id,
        qualifiers=[
            {"qualifier_type_id": "biolink:relationship_type", "qualifier_value": "uses_medium"}
        ],
    )


def database_reference_to_edge(medium_id: str, term: dict) -> dict | None:
    """
    Medium → has_database_reference → Database ID

    Data preserved: DSMZ, TOGO, ATCC, NCIT identifiers
    """
    db_id = term.get("id")
    if not db_id:
        return None

    return _make_association(
        subject=medium_id,
        predicate="biolink:same_as",
        obj=db_id,
    )


def variant_to_edge(medium_id: str, variant: dict) -> dict | None:
    """
    Variant → variant_of → Base Medium

    Data preserved: Variant relationship
    """
    variant_name = variant.get("name")
    if not variant_name:
        return None

    variant_id = f"{PREFIX}:variant_{_sanitize_id(variant_name)}"

    return _make_association(
        subject=variant_id,
        predicate="biolink:subclass_of",
        obj=medium_id,
        qualifiers=[
            {"qualifier_type_id": "biolink:relationship_type", "qualifier_value": "variant_of"}
        ],
    )


# ================================================================
# HELPER FUNCTIONS
# ================================================================


def _make_edge_id(subject: str, predicate: str, obj: str) -> str:
    """Generate deterministic UUID5-based edge ID."""
    edge_string = f"{subject}|{predicate}|{obj}"
    return f"urn:uuid:{uuid.uuid5(NAMESPACE_UUID, edge_string)}"


def _get_term_id(data: dict, path: list[str]) -> str | None:
    """Safely extract nested term ID."""
    current = data
    for key in path:
        if not isinstance(current, dict):
            return None
        current = current.get(key)
        if current is None:
            return None
    return current


def _resolved_ingredient_id(
    ingredient: Mapping[str, Any], ingredient_resolver: IngredientResolver
) -> str | None:
    """Resolve an ingredient through MIM, retaining local identity only as fallback."""

    return ingredient_resolver(ingredient).identifier


def _format_evidence(evidence_items: list[dict] | None) -> tuple:
    """Format evidence into publications list and supporting text."""
    pubs = []
    for e in evidence_items or []:
        ref = e.get("reference")
        if ref:
            pubs.append(ref)
    return pubs, []  # Supporting text deferred


# Characters dropped outright rather than turned into separators. The backslash
# and quote are load-bearing: koza's `trim()` strips the two-character sequence
# `\"` from every edge column, but `TSVWriter.write_row` restores a node's `id`
# from the raw record and so bypasses that. An id containing `\"` therefore came
# out spelled one way in the nodes file and another in the edges file, which is
# how the full-corpus run produced 2 dangling references and 2 orphan nodes:
#
#   node: CultureMech:solution_Mineral_salt_solution*_\"Hutner_Cohen-Bazire\"
#   edge: CultureMech:solution_Mineral_salt_solution*_Hutner_Cohen-Bazire
#
# Stripping them here makes both sides agree regardless of koza's asymmetry, and
# a CURIE has no business carrying a quote or an asterisk in the first place.
_ID_DROP_CHARS = '()\\"*'
_ID_SEPARATOR_CHARS = " /"

# The colon is separate because it is the one character that is not merely ugly:
# it is the CURIE delimiter. Names like `Solution A:` produced
# `CultureMech:solution_Solution_A:`, a two-colon id that any consumer splitting
# on `:` reads wrongly — and this export exists to be consumed. 19 ids in the
# corpus were affected. Mapped to an underscore rather than dropped so
# `Autotrophic growth on ferrous sulfate:Add 13.9 g/l` does not weld two words
# together.
_ID_COLON_REPLACEMENT = "_"


def _sanitize_id(text: str) -> str:
    """Convert text to a valid CURIE local id.

    Separators (space, slash, colon) become underscores; quotes, backslashes,
    asterisks and parentheses are dropped. Runs of underscores collapse so that
    dropping a character does not leave `__` behind.
    """
    text = text.replace(":", _ID_COLON_REPLACEMENT)
    for char in _ID_SEPARATOR_CHARS:
        text = text.replace(char, "_")
    for char in _ID_DROP_CHARS:
        text = text.replace(char, "")
    while "__" in text:
        text = text.replace("__", "_")
    return text.strip("_")


# Where a run's records live, for the solution-record index below. Set by
# scripts/export_kgx.py before koza starts; koza loads this module as a fresh
# copy, so a module global set from the runner would not reach it, and the
# environment is the one channel both copies share. Unset in unit tests, where
# the index is empty and every nested solution is minted.
RECORDS_DIR_ENV = "CULTUREMECH_RECORDS_DIR"
_RECORD_ID_LINE = re.compile(r"^id: (CultureMech:\d{6})\n", re.M)
_SOLUTION_TERM_LINES = re.compile(r"^term:\n  id: (\S+)", re.M)


@lru_cache(maxsize=1)
def _solution_record_index() -> dict[str, str]:
    """Upstream solution id -> the standalone solution record that carries it.

    `term.id` sits within the first four lines of all 4,784 solution records and
    `id:` is line one, so a regex over the file text is enough; a second YAML
    parse of the corpus would double the export's cost for nothing.
    """
    root = os.environ.get(RECORDS_DIR_ENV)
    if not root:
        return {}
    index: dict[str, str] = {}
    for path in Path(root).glob("*/*.yaml"):
        head = path.read_text(errors="replace")[:600]
        record = _RECORD_ID_LINE.match(head)
        term = _SOLUTION_TERM_LINES.search(head)
        if record and term and term.group(1).startswith(_SOLUTION_TERM_PREFIXES):
            index[term.group(1)] = record.group(1)
    return index


def _solution_fingerprint(solution: dict) -> str:
    """Eight hex digits over the name and the composition as written.

    Two nested solutions with one name and different reagents are different
    stocks (`Vitamin solution` carries 15 compositions corpus-wide, #441); two
    with the same name and reagents are one stock shared by many media. Keyed on
    the record's own ids and values, not the resolver's, so the id is stable
    across MIM pins; it does move when a grounding in the record is repaired,
    which is acceptable for a node that has no permanent identifier.
    """
    rows = sorted(
        (
            str(
                (row.get("term") or {}).get("id")
                or (row.get("chebi_term") or {}).get("id")
                or row.get("preferred_term")
            ),
            str((row.get("concentration") or {}).get("value")),
            str((row.get("concentration") or {}).get("unit")),
        )
        for row in (solution.get("composition") or [])
        if isinstance(row, dict)
    )
    payload = repr((str(solution.get("preferred_term") or ""), rows)).encode()
    return hashlib.sha1(payload).hexdigest()[:8]


def nested_solution_target(solution: dict) -> tuple[str | None, bool]:
    """The node a medium's nested solution points at, and whether we mint it.

    In order:
    1. `culturemech_term.id` naming a record: that record (15 today).
    2. `term.id` matching a standalone solution record: that record (1,228 today,
       none of which carries a composition of its own, so nothing is lost).
    3. Otherwise a minted `CultureMech:solution_{name}_{fingerprint}` node.

    Until #441 every nested solution was `CultureMech:solution_{name}`, and
    emission dedupes on id, so 51 names holding several different compositions
    collapsed into union nodes and the sanitizer merged MediaDive's footnote-marked
    names (`Vitamin solution*`, `**`) on top.
    """
    name = solution.get("preferred_term")
    if not name:
        return None, False
    local = solution.get("culturemech_term")
    if isinstance(local, dict) and str(local.get("id", "")).startswith(f"{PREFIX}:"):
        return str(local["id"]), False
    term = solution.get("term")
    tid = term.get("id") if isinstance(term, dict) else None
    if isinstance(tid, str) and tid in _solution_record_index():
        return _solution_record_index()[tid], False
    return f"{_create_solution_id(str(name))}_{_solution_fingerprint(solution)}", True


def _create_solution_id(solution_name: str) -> str:
    """Create a CURIE for a solution."""
    sanitized = _sanitize_id(solution_name)
    return f"{PREFIX}:solution_{sanitized}"


def _quantity(concentration: Any) -> tuple[list[dict], str | None, str | None]:
    """The concentration of one row as (qualifiers, value, unit).

    `value` and `unit` are the typed columns kg-microbe reads from the MediaDive
    transform; the joined `biolink:concentration` qualifier is kept alongside
    (#445). Both come straight from the record: the value string as written
    (`'10'`, `'5e-05'`) and the unit as its enum token.
    """
    if not isinstance(concentration, dict):
        return [], None, None
    val = concentration.get("value")
    unit = concentration.get("unit")
    if not (val and unit):
        return [], None, None
    qualifier = {"qualifier_type_id": "biolink:concentration", "qualifier_value": f"{val} {unit}"}
    # The typed pair is for arithmetic, so it carries only a value that parses as
    # a number: 3,598 corpus rows say `variable`, `-`, or prose such as
    # `0.01 g per vessel`, and MediaDive's column is numeric. Those rows keep the
    # qualifier string and leave the pair empty rather than hand a consumer a
    # `value` that float() rejects (#301 owns the `-` placeholders).
    try:
        float(str(val))
    except ValueError:
        return [qualifier], None, None
    return [qualifier], str(val), str(unit)


def _make_association(
    subject: str,
    predicate: str,
    obj: str,
    qualifiers: list[dict] | None = None,
    publications: list[str] | None = None,
    value: str | None = None,
    unit: str | None = None,
) -> dict:
    """Create an Association dictionary."""
    return {
        "id": _make_edge_id(subject, predicate, obj),
        "subject": subject,
        "predicate": predicate,
        "object": obj,
        "qualifiers": qualifiers,
        "publications": publications,
        "value": value,
        "unit": unit,
        "primary_knowledge_source": KNOWLEDGE_SOURCE,
        "knowledge_level": "knowledge_assertion",
        "agent_type": "manual_validation_of_automated_agent",
    }


# ================================================================
# KOZA WRAPPER (handles I/O)
# ================================================================

# Node ids already written in this run. A medium-type or solution node is shared
# by thousands of records, so without this the nodes file would carry ~8,850 rows
# for `CultureMech:medium_type_COMPLEX` alone. Run-scoped rather than per-record,
# which is why it cannot live in `nodes()`.
_EMITTED_NODE_IDS: set = set()


# Edge ids already written in this run. `_make_edge_id` is a deterministic UUID5
# over subject|predicate|object, so an identical triple emitted twice gets the
# same id — and `transform()` walks each record's `solutions[]`, re-emitting a
# shared stock solution's whole composition once per referencing medium.
# `Seven vitamins solution` is referenced by 178 media, so each of its
# `has_part` edges appeared 178 times: 45,464 surplus rows, 23% of the file
# (#312). Every collision was an exact duplicate triple, so nothing is lost by
# keeping the first.
_EMITTED_EDGE_IDS: set = set()


def reset_edge_dedup() -> None:
    """Clear the run-scoped edge-id set. See `reset_node_dedup`."""
    _EMITTED_EDGE_IDS.clear()


def reset_node_dedup() -> None:
    """Clear the run-scoped node-id set.

    Not needed by ``scripts/export_kgx.py`` today: koza loads this file with
    ``importlib.util.spec_from_file_location`` "without touching sys.modules",
    so each run gets a fresh module object and a fresh, empty set. Calling this
    from the driver would clear a *different* copy of the module — the one
    imported as ``culturemech.export.kgx_export`` — and protect nothing.

    Kept for callers that import this module directly and drive ``nodes()`` in a
    loop, and as the ready-made fix if koza ever starts caching transform
    modules. ``test_a_second_run_in_the_same_process_repeats_the_output`` is what
    would catch that change.
    """
    _EMITTED_NODE_IDS.clear()


if KOZA_AVAILABLE:

    @koza.transform_record()
    def koza_transform(koza_ctx: KozaTransform, record: dict[str, Any]) -> None:
        """Koza wrapper - handles I/O."""
        for node_dict in nodes(record):
            node_id = node_dict["id"]
            if node_id in _EMITTED_NODE_IDS:
                continue
            _EMITTED_NODE_IDS.add(node_id)
            koza_ctx.write(Node(**node_dict))

        for edge_dict in transform(record):
            # Deliberately NOT wrapped in biolink's Association: its `qualifiers`
            # slot is `list[str]`, so every qualified edge raised here and was
            # swallowed by the old except-and-print. Failures now stop the run.
            edge_id = edge_dict["id"]
            if edge_id in _EMITTED_EDGE_IDS:
                continue
            _EMITTED_EDGE_IDS.add(edge_id)
            koza_ctx.write(to_edge(edge_dict))


# ================================================================
# STANDALONE USAGE (for testing)
# ================================================================

if __name__ == "__main__":
    import json
    import sys

    import yaml

    if len(sys.argv) < 2:
        print("Usage: python kgx_export.py <recipe.yaml>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        recipe = yaml.safe_load(f)

    print("Edges extracted from recipe:")
    for i, edge in enumerate(transform(recipe), 1):
        print(f"\n--- Edge {i} ---")
        print(json.dumps(edge, indent=2))
