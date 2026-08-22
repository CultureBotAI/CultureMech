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

3. Solution → has_part (biolink:has_part) → Ingredient (CHEBI)
   - Subject: Solution
   - Predicate: biolink:has_part
   - Object: Ingredient (CHEBI ID)
   - Qualifiers: concentration, role

4. Medium → has_part (biolink:has_part) → Ingredient (CHEBI)
   - Subject: Medium
   - Predicate: biolink:has_part
   - Object: Ingredient (CHEBI ID)
   - Qualifiers: concentration, role

5. Medium → has_attribute (biolink:has_attribute) → Medium Type
   - Subject: Medium
   - Predicate: biolink:has_attribute
   - Object: Type node (e.g., culturemech:medium_type_COMPLEX)
   - Qualifiers: attribute_type = "medium_type"

Legacy Edges (for backward compatibility):
-------------------------------------------
6. Medium → has_application → Use case
7. Medium → has_physical_state → State
8. Dataset → uses_medium → Medium
9. Medium → has_database_reference → Database ID
10. Variant → variant_of → Base Medium
"""

import uuid
from collections.abc import Iterator
from dataclasses import asdict, dataclass
from typing import Any

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
NAMESPACE_UUID = uuid.uuid5(uuid.NAMESPACE_URL, "https://w3id.org/culturemech")

# Predicates following cmm-ai-automation schema
GROWS_IN_MEDIUM = "METPO:2000517"  # grows in
HAS_PART = "biolink:has_part"  # For medium→ingredient, solution→ingredient
HAS_SOLUTION_COMPONENT = "biolink:has_part"  # For medium→solution (also uses has_part)


# ================================================================
# PURE TRANSFORM FUNCTION (testable without Koza)
# ================================================================


def transform(record: dict[str, Any]) -> Iterator[dict[str, Any]]:
    """
    Pure transform function - testable without Koza.

    Extracts edges from a media recipe following cmm-ai-automation semantic modeling:
    1. organism → medium (grows_in_medium: METPO:2000517)
    2. medium → solution (has_part)
    3. solution → ingredient (has_part)
    4. medium → ingredient (has_part)
    5. medium → type (as node attribute via has_attribute)
    6. Medium → has_application → Use case (legacy)
    7. Medium → has_physical_state → State (legacy)
    8. Dataset → uses_medium → Medium (legacy)
    9. Medium → has_database_reference → Database ID (legacy)
    10. Variant → variant_of → Base Medium (legacy)
    """
    # Sanitized, not just space-replaced: a name carrying a quote would
    # otherwise be spelled differently in the nodes and edges files (see
    # `_sanitize_id`).
    medium_id = f"culturemech:{_sanitize_id(str(record.get('name') or ''))}"

    # NEW: Edge Type 1: Organism → Medium (grows_in_medium)
    for organism in record.get("target_organisms", []):
        edge = organism_grows_in_medium_edge(organism, medium_id)
        if edge:
            yield edge

    # NEW: Edge Type 2: Medium → Solution (has_solution_component)
    for solution in record.get("solutions", []):
        edge = medium_to_solution_edge(medium_id, solution)
        if edge:
            yield edge

        # NEW: Edge Type 3: Solution → Ingredient (has_part)
        # Extract ingredients from solution composition
        solution_id = _create_solution_id(solution.get("preferred_term", ""))
        for ingredient in solution.get("composition", []):
            edge = solution_to_ingredient_edge(solution_id, ingredient)
            if edge:
                yield edge

    # Edge Type 4: Medium → Ingredient (has_part)
    for ingredient in record.get("ingredients", []):
        edge = medium_to_ingredient_edge(medium_id, ingredient)
        if edge:
            yield edge

    # NEW: Edge Type 5: Medium → Type (as node attribute)
    medium_type = record.get("medium_type")
    if medium_type:
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
        **columns,
    )


def nodes(record: dict[str, Any]) -> Iterator[dict[str, Any]]:
    """Every node this record mints, as dicts. Companion to ``transform``.

    Yields duplicates across records by design — ``culturemech:medium_type_COMPLEX``
    belongs to all 8,850 COMPLEX media. Deduplication is the writer's job (see
    ``koza_transform``), because it is a property of the run, not of the record.
    """
    name = str(record.get("name") or "")
    if not name:
        return
    medium_id = f"culturemech:{_sanitize_id(name)}"
    medium_type = record.get("medium_type")

    medium_category, type_category = _MEDIUM_TYPE_CATEGORIES.get(
        str(medium_type or ""),
        (_DEFAULT_MEDIUM_CATEGORY, _DEFAULT_MEDIUM_TYPE_CATEGORY),
    )

    yield asdict(Node(id=medium_id, category=medium_category, name=name))

    if medium_type:
        yield asdict(
            Node(
                id=f"culturemech:medium_type_{medium_type}",
                category=type_category,
                name=str(medium_type),
            )
        )

    for solution in record.get("solutions", []) or []:
        preferred_term = solution.get("preferred_term")
        if preferred_term:
            yield asdict(
                Node(
                    id=_create_solution_id(preferred_term),
                    category=[CHEMICAL_MIXTURE],
                    name=str(preferred_term),
                )
            )

    for application in record.get("applications", []) or []:
        if application:
            yield asdict(
                Node(
                    id=f"culturemech:application_{_sanitize_id(str(application))}",
                    category=[ATTRIBUTE],
                    name=str(application),
                )
            )

    physical_state = record.get("physical_state")
    if physical_state:
        yield asdict(
            Node(
                id=f"culturemech:state_{str(physical_state).lower()}",
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
                    id=f"culturemech:{_sanitize_id(str(variant_name))}",
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


def medium_to_solution_edge(medium_id: str, solution: dict) -> dict | None:
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
    solution_name = solution.get("preferred_term")
    if not solution_name:
        return None

    solution_id = _create_solution_id(solution_name)

    qualifiers = []
    concentration = solution.get("concentration", {})
    if concentration:
        val = concentration.get("value")
        unit = concentration.get("unit")
        if val and unit:
            qualifiers.append(
                {"qualifier_type_id": "biolink:concentration", "qualifier_value": f"{val} {unit}"}
            )

    return _make_association(
        subject=medium_id,
        predicate=HAS_SOLUTION_COMPONENT,  # biolink:has_part
        obj=solution_id,
        qualifiers=qualifiers if qualifiers else None,
    )


def solution_to_ingredient_edge(solution_id: str, ingredient: dict) -> dict | None:
    """
    Solution → has_part (biolink:has_part) → Ingredient (CHEBI)

    Following cmm-ai-automation pattern:
    - subject: solution
    - predicate: biolink:has_part
    - object: ingredient (CHEBI ID)

    Qualifiers:
    - concentration: amount in solution
    - role: functional role

    Data preserved: Chemical ID, concentration, role
    """
    chem_id = _get_term_id(ingredient, ["term", "id"])
    if not chem_id:
        return None

    qualifiers = []
    concentration = ingredient.get("concentration", {})
    if concentration:
        val = concentration.get("value")
        unit = concentration.get("unit")
        if val and unit:
            qualifiers.append(
                {"qualifier_type_id": "biolink:concentration", "qualifier_value": f"{val} {unit}"}
            )

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
    )


def medium_to_ingredient_edge(medium_id: str, ingredient: dict) -> dict | None:
    """
    Medium → has_part (biolink:has_part) → Ingredient (CHEBI)

    Following cmm-ai-automation pattern (renamed from ingredient_to_edge):
    - subject: medium
    - predicate: biolink:has_part
    - object: ingredient (CHEBI ID)

    Qualifiers:
    - concentration: amount
    - role: functional role

    Data preserved: Chemical ID, concentration, role
    Data lost: Supplier info, preparation notes, chemical formula
    """
    chem_id = _get_term_id(ingredient, ["term", "id"])
    if not chem_id:
        return None

    qualifiers = []
    concentration = ingredient.get("concentration", {})
    if concentration:
        val = concentration.get("value")
        unit = concentration.get("unit")
        if val and unit:
            qualifiers.append(
                {"qualifier_type_id": "biolink:concentration", "qualifier_value": f"{val} {unit}"}
            )

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
        publications=pubs if pubs else None,
    )


def medium_to_type_edge(medium_id: str, medium_type: str) -> dict | None:
    """
    Medium → has_attribute → Medium Type

    Creates a type attribute node:
    - subject: medium
    - predicate: biolink:has_attribute
    - object: type node (e.g., culturemech:medium_type_COMPLEX)

    Data preserved: Medium type classification (COMPLEX, DEFINED, etc.)
    """
    type_id = f"culturemech:medium_type_{medium_type}"

    return _make_association(
        subject=medium_id,
        predicate="biolink:has_attribute",
        obj=type_id,
        qualifiers=[
            {"qualifier_type_id": "biolink:attribute_type", "qualifier_value": "medium_type"}
        ],
    )


def ingredient_to_edge(medium_id: str, ingredient: dict) -> dict | None:
    """
    Medium (culturemech:LB_Broth) → has_part → Glucose (CHEBI:17234)

    Qualifiers:
    - concentration: 10 g/L

    Data preserved: Chemical ID, concentration
    Data lost: Supplier info, preparation notes, chemical formula
    """
    chem_id = _get_term_id(ingredient, ["term", "id"])
    if not chem_id:
        return None

    concentration = ingredient.get("concentration", {})
    qualifiers = []
    if concentration:
        val = concentration.get("value")
        unit = concentration.get("unit")
        if val and unit:
            qualifiers.append(
                {"qualifier_type_id": "biolink:concentration", "qualifier_value": f"{val} {unit}"}
            )

    pubs, _ = _format_evidence(ingredient.get("evidence"))

    return _make_association(
        subject=medium_id,
        predicate="biolink:has_part",
        obj=chem_id,
        qualifiers=qualifiers if qualifiers else None,
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
    app_id = f"culturemech:application_{_sanitize_id(application)}"

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
    state_id = f"culturemech:state_{physical_state.lower()}"

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

    variant_id = f"culturemech:{_sanitize_id(variant_name)}"

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
#   node: culturemech:solution_Mineral_salt_solution*_\"Hutner_Cohen-Bazire\"
#   edge: culturemech:solution_Mineral_salt_solution*_Hutner_Cohen-Bazire
#
# Stripping them here makes both sides agree regardless of koza's asymmetry, and
# a CURIE has no business carrying a quote or an asterisk in the first place.
_ID_DROP_CHARS = '()\\"*'
_ID_SEPARATOR_CHARS = " /"

# The colon is separate because it is the one character that is not merely ugly:
# it is the CURIE delimiter. Names like `Solution A:` produced
# `culturemech:solution_Solution_A:`, a two-colon id that any consumer splitting
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


def _create_solution_id(solution_name: str) -> str:
    """Create a CURIE for a solution."""
    sanitized = _sanitize_id(solution_name)
    return f"culturemech:solution_{sanitized}"


def _make_association(
    subject: str,
    predicate: str,
    obj: str,
    qualifiers: list[dict] | None = None,
    publications: list[str] | None = None,
) -> dict:
    """Create an Association dictionary."""
    return {
        "id": _make_edge_id(subject, predicate, obj),
        "subject": subject,
        "predicate": predicate,
        "object": obj,
        "qualifiers": qualifiers,
        "publications": publications,
        "primary_knowledge_source": KNOWLEDGE_SOURCE,
        "knowledge_level": "knowledge_assertion",
        "agent_type": "manual_validation_of_automated_agent",
    }


# ================================================================
# KOZA WRAPPER (handles I/O)
# ================================================================

# Node ids already written in this run. A medium-type or solution node is shared
# by thousands of records, so without this the nodes file would carry ~8,850 rows
# for `culturemech:medium_type_COMPLEX` alone. Run-scoped rather than per-record,
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
