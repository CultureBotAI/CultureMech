"""
KGX edge exporter for CultureMech.

Transforms media recipe YAML files into KGX-format edges for the knowledge graph.
Follows the dismech pattern: pure transform function + Koza decorator wrapper.
"""

import uuid
from typing import Any, Iterator, Optional

try:
    import koza
    from koza import KozaTransform
    KOZA_AVAILABLE = True
except ImportError:
    KOZA_AVAILABLE = False
    print("Warning: Koza not installed. Install with: pip install koza")

try:
    from biolink_model.datamodel.pydanticmodel_v2 import (
        AgentTypeEnum,
        Association,
        KnowledgeLevelEnum,
    )
    BIOLINK_AVAILABLE = True
except ImportError:
    BIOLINK_AVAILABLE = False
    print("Warning: biolink-model not installed. Install with: pip install biolink-model")

KNOWLEDGE_SOURCE = "infores:culturemech"
NAMESPACE_UUID = uuid.uuid5(uuid.NAMESPACE_URL, "https://w3id.org/culturemech")


# ================================================================
# PURE TRANSFORM FUNCTION (testable without Koza)
# ================================================================

def transform(record: dict[str, Any]) -> Iterator[dict[str, Any]]:
    """
    Pure transform function - testable without Koza.

    Extracts 7 edge types from a media recipe:
    1. Medium → has_part → Chemical (CHEBI)
    2. Medium → supports_growth_of → Organism (NCBITaxon)
    3. Medium → has_application → Use case
    4. Medium → has_physical_state → State
    5. Dataset → uses_medium → Medium
    6. Medium → has_database_reference → Database ID
    7. Variant → variant_of → Base Medium
    """
    medium_id = f"culturemech:{record.get('name', '').replace(' ', '_')}"

    # Edge Type 1: Medium → Chemical Ingredients
    for ingredient in record.get("ingredients", []):
        edge = ingredient_to_edge(medium_id, ingredient)
        if edge:
            yield edge

    # Edge Type 2: Medium → Target Organisms
    for organism in record.get("target_organisms", []):
        edge = organism_to_edge(medium_id, organism)
        if edge:
            yield edge

    # Edge Type 3: Medium → Applications
    for application in record.get("applications", []):
        edge = application_to_edge(medium_id, application)
        if edge:
            yield edge

    # Edge Type 4: Medium → Physical State
    physical_state = record.get("physical_state")
    if physical_state:
        edge = physical_state_to_edge(medium_id, physical_state)
        if edge:
            yield edge

    # Edge Type 5: Dataset → Medium
    for dataset in record.get("datasets", []):
        edge = dataset_to_edge(medium_id, dataset)
        if edge:
            yield edge

    # Edge Type 6: Medium → Database Reference
    media_term = record.get("media_term", {})
    if media_term.get("term"):
        edge = database_reference_to_edge(medium_id, media_term["term"])
        if edge:
            yield edge

    # Edge Type 7: Variant → Base Medium
    for variant in record.get("variants", []):
        edge = variant_to_edge(medium_id, variant)
        if edge:
            yield edge


# ================================================================
# EDGE EXTRACTION FUNCTIONS
# ================================================================

def ingredient_to_edge(medium_id: str, ingredient: dict) -> Optional[dict]:
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
            qualifiers.append({
                "qualifier_type_id": "biolink:concentration",
                "qualifier_value": f"{val} {unit}"
            })

    pubs, _ = _format_evidence(ingredient.get("evidence"))

    return _make_association(
        subject=medium_id,
        predicate="biolink:has_part",
        obj=chem_id,
        qualifiers=qualifiers if qualifiers else None,
        publications=pubs if pubs else None,
    )


def organism_to_edge(medium_id: str, organism: dict) -> Optional[dict]:
    """
    Medium → supports_growth_of → Organism (NCBITaxon)

    Data preserved: Organism ID, evidence
    Data lost: Strain, growth phase details
    """
    org_id = _get_term_id(organism, ["term", "id"])
    if not org_id:
        return None

    pubs, _ = _format_evidence(organism.get("evidence"))

    return _make_association(
        subject=medium_id,
        predicate="biolink:affects",  # Or custom predicate like supports_growth_of
        obj=org_id,
        publications=pubs if pubs else None,
    )


def application_to_edge(medium_id: str, application: str) -> Optional[dict]:
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
        qualifiers=[{
            "qualifier_type_id": "biolink:attribute_type",
            "qualifier_value": "application"
        }],
    )


def physical_state_to_edge(medium_id: str, physical_state: str) -> Optional[dict]:
    """
    Medium → has_physical_state → State

    Data preserved: Physical state
    """
    state_id = f"culturemech:state_{physical_state.lower()}"

    return _make_association(
        subject=medium_id,
        predicate="biolink:has_attribute",
        obj=state_id,
        qualifiers=[{
            "qualifier_type_id": "biolink:attribute_type",
            "qualifier_value": "physical_state"
        }],
    )


def dataset_to_edge(medium_id: str, dataset: dict) -> Optional[dict]:
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
        qualifiers=[{
            "qualifier_type_id": "biolink:relationship_type",
            "qualifier_value": "uses_medium"
        }],
    )


def database_reference_to_edge(medium_id: str, term: dict) -> Optional[dict]:
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


def variant_to_edge(medium_id: str, variant: dict) -> Optional[dict]:
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
        qualifiers=[{
            "qualifier_type_id": "biolink:relationship_type",
            "qualifier_value": "variant_of"
        }],
    )


# ================================================================
# HELPER FUNCTIONS
# ================================================================

def _make_edge_id(subject: str, predicate: str, obj: str) -> str:
    """Generate deterministic UUID5-based edge ID."""
    edge_string = f"{subject}|{predicate}|{obj}"
    return f"urn:uuid:{uuid.uuid5(NAMESPACE_UUID, edge_string)}"


def _get_term_id(data: dict, path: list[str]) -> Optional[str]:
    """Safely extract nested term ID."""
    current = data
    for key in path:
        if not isinstance(current, dict):
            return None
        current = current.get(key)
        if current is None:
            return None
    return current


def _format_evidence(evidence_items: Optional[list[dict]]) -> tuple[list[str], list[str]]:
    """Format evidence into publications list and supporting text."""
    pubs = []
    for e in evidence_items or []:
        ref = e.get("reference")
        if ref:
            pubs.append(ref)
    return pubs, []  # Supporting text deferred


def _sanitize_id(text: str) -> str:
    """Convert text to valid ID component."""
    return text.replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "")


def _make_association(
    subject: str,
    predicate: str,
    obj: str,
    qualifiers: Optional[list[dict]] = None,
    publications: Optional[list[str]] = None,
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

if KOZA_AVAILABLE and BIOLINK_AVAILABLE:
    @koza.transform_record()
    def koza_transform(koza_ctx: KozaTransform, record: dict[str, Any]) -> None:
        """Koza wrapper - handles I/O."""
        for edge_dict in transform(record):
            # Convert dict to Biolink Association
            try:
                edge = Association(**edge_dict)
                koza_ctx.write(edge)
            except Exception as e:
                print(f"Error creating association: {e}")
                print(f"Edge data: {edge_dict}")


# ================================================================
# STANDALONE USAGE (for testing)
# ================================================================

if __name__ == "__main__":
    import sys
    import yaml
    import json

    if len(sys.argv) < 2:
        print("Usage: python kgx_export.py <recipe.yaml>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        recipe = yaml.safe_load(f)

    print("Edges extracted from recipe:")
    for i, edge in enumerate(transform(recipe), 1):
        print(f"\n--- Edge {i} ---")
        print(json.dumps(edge, indent=2))
