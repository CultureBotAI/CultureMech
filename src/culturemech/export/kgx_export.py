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
from typing import Any, Dict, Iterator, List, Optional

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

# Predicates following cmm-ai-automation schema
GROWS_IN_MEDIUM = "METPO:2000517"  # grows in
HAS_PART = "biolink:has_part"  # For medium→ingredient, solution→ingredient
HAS_SOLUTION_COMPONENT = "biolink:has_part"  # For medium→solution (also uses has_part)


# ================================================================
# PURE TRANSFORM FUNCTION (testable without Koza)
# ================================================================

def transform(record: Dict[str, Any]) -> Iterator[Dict[str, Any]]:
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
    medium_id = f"culturemech:{record.get('name', '').replace(' ', '_')}"

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
# EDGE EXTRACTION FUNCTIONS (following cmm-ai-automation semantic model)
# ================================================================

def organism_grows_in_medium_edge(organism: Dict, medium_id: str) -> Optional[dict]:
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
        qualifiers.append({
            "qualifier_type_id": "biolink:strain",
            "qualifier_value": strain
        })

    # Add growth phase as qualifier if present
    growth_phase = organism.get("growth_phase")
    if growth_phase:
        qualifiers.append({
            "qualifier_type_id": "biolink:growth_phase",
            "qualifier_value": growth_phase
        })

    pubs, _ = _format_evidence(organism.get("evidence"))

    return _make_association(
        subject=org_id,  # Organism is subject
        predicate=GROWS_IN_MEDIUM,  # METPO:2000517
        obj=medium_id,  # Medium is object
        qualifiers=qualifiers if qualifiers else None,
        publications=pubs if pubs else None,
    )


def medium_to_solution_edge(medium_id: str, solution: Dict) -> Optional[dict]:
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
            qualifiers.append({
                "qualifier_type_id": "biolink:concentration",
                "qualifier_value": f"{val} {unit}"
            })

    return _make_association(
        subject=medium_id,
        predicate=HAS_SOLUTION_COMPONENT,  # biolink:has_part
        obj=solution_id,
        qualifiers=qualifiers if qualifiers else None,
    )


def solution_to_ingredient_edge(solution_id: str, ingredient: Dict) -> Optional[dict]:
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
            qualifiers.append({
                "qualifier_type_id": "biolink:concentration",
                "qualifier_value": f"{val} {unit}"
            })

    # Add role if present
    roles = ingredient.get("role")
    if roles:
        if isinstance(roles, list):
            roles_str = ", ".join(roles)
        else:
            roles_str = roles
        qualifiers.append({
            "qualifier_type_id": "biolink:role",
            "qualifier_value": roles_str
        })

    return _make_association(
        subject=solution_id,
        predicate=HAS_PART,  # biolink:has_part
        obj=chem_id,
        qualifiers=qualifiers if qualifiers else None,
    )


def medium_to_ingredient_edge(medium_id: str, ingredient: Dict) -> Optional[dict]:
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
            qualifiers.append({
                "qualifier_type_id": "biolink:concentration",
                "qualifier_value": f"{val} {unit}"
            })

    # Add role if present
    roles = ingredient.get("role")
    if roles:
        if isinstance(roles, list):
            roles_str = ", ".join(roles)
        else:
            roles_str = roles
        qualifiers.append({
            "qualifier_type_id": "biolink:role",
            "qualifier_value": roles_str
        })

    pubs, _ = _format_evidence(ingredient.get("evidence"))

    return _make_association(
        subject=medium_id,
        predicate=HAS_PART,  # biolink:has_part
        obj=chem_id,
        qualifiers=qualifiers if qualifiers else None,
        publications=pubs if pubs else None,
    )


def medium_to_type_edge(medium_id: str, medium_type: str) -> Optional[dict]:
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
        qualifiers=[{
            "qualifier_type_id": "biolink:attribute_type",
            "qualifier_value": "medium_type"
        }],
    )


def ingredient_to_edge(medium_id: str, ingredient: Dict) -> Optional[dict]:
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


def organism_to_edge(medium_id: str, organism: Dict) -> Optional[dict]:
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


def dataset_to_edge(medium_id: str, dataset: Dict) -> Optional[dict]:
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


def database_reference_to_edge(medium_id: str, term: Dict) -> Optional[dict]:
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


def variant_to_edge(medium_id: str, variant: Dict) -> Optional[dict]:
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


def _get_term_id(data: Dict, path: List[str]) -> Optional[str]:
    """Safely extract nested term ID."""
    current = data
    for key in path:
        if not isinstance(current, dict):
            return None
        current = current.get(key)
        if current is None:
            return None
    return current


def _format_evidence(evidence_items: Optional[List[Dict]]) -> tuple:
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


def _create_solution_id(solution_name: str) -> str:
    """Create a CURIE for a solution."""
    sanitized = _sanitize_id(solution_name)
    return f"culturemech:solution_{sanitized}"


def _make_association(
    subject: str,
    predicate: str,
    obj: str,
    qualifiers: Optional[List[Dict]] = None,
    publications: Optional[List[str]] = None,
) -> Dict:
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
    def koza_transform(koza_ctx: KozaTransform, record: Dict[str, Any]) -> None:
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
