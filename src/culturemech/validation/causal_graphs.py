"""Semantic validator for CultureMech causal mechanism graphs (Issue #658).

Enforces CultureMech Stage 2 (``causal_graphs``) requirements beyond structural
LinkML validation:

1. ``CausalEdge.id`` must match ``^(edge_[A-Za-z0-9_.-]+|CausalEdge:[A-Za-z0-9_.-]+)$``
   and be unique within each ``causal_graphs`` list (supporting
   ``Discussion.attaches_to`` anchors such as ``causal_graphs#edge_x``).
2. ``subject_term`` and ``object_term`` must be ontology-grounded ``CausalTerm``
   mappings with a valid CURIE prefix/syntax and non-empty ``label``. Bare
   ingredient role enum tokens (e.g. ``CARBON_SOURCE``, ``BUFFER``) and
   self-loops (``subject_term.id == object_term.id``) are rejected.
3. ``predicate`` must be a member of ``CausalPredicateEnum``.
4. ``organism_term`` must be a valid ``NCBITaxon:`` CURIE with a non-empty
   label when present, is required when an edge is nested under
   ``target_organisms[i]`` or specifies ``protein_terms``, and must match the
   enclosing ``target_organisms[i].term.id`` unless ``notes`` explicitly
   documents a strain/parent-taxon relationship.
5. ``protein_terms`` (when present) must be canonical ``UniProtKB:`` accessions
   with non-empty labels and no duplicates within an edge.
6. Every ``CausalEdge`` must carry a non-empty ``evidence`` list with at least
   one ``EvidenceItem`` having ``supports: SUPPORT`` or ``PARTIAL``, a valid
   ``reference`` (``PMID:``, ``DOI:``, ``doi:``, or ``http(s)://``), a
   non-empty verbatim ``snippet``, and a non-empty ``explanation``.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

from linkml.validator.report import Severity, ValidationResult

from culturemech.validation.protein_examples import (
    EC_CURIE_RE,
    NCBITAXON_CURIE_RE,
    POSITIVE_SUPPORTS,
    REFERENCE_RE,
    UNIPROT_CURIE_RE,
    VALID_SUPPORTS,
)

CAUSAL_EDGE_ID_RE = re.compile(r"^(edge_[A-Za-z0-9_.-]+|CausalEdge:[A-Za-z0-9_.-]+)$")

CAUSAL_TERM_ID_RE = re.compile(
    r"^(CHEBI|NCBITaxon|GO|UniProtKB|EC|KEGG|METPO|ENVO|PATO|NCIT|FOODON|UBERON|MICRO|CultureMech|MediaIngredientMech):[A-Za-z0-9_.-]+$"
)

PREFIX_SPECIFIC_PATTERNS: dict[str, re.Pattern[str]] = {
    "CHEBI": re.compile(r"^CHEBI:[1-9][0-9]*$"),
    "NCBITaxon": NCBITAXON_CURIE_RE,
    "GO": re.compile(r"^GO:[0-9]{7}$"),
    "UniProtKB": UNIPROT_CURIE_RE,
    "EC": EC_CURIE_RE,
    "ENVO": re.compile(r"^ENVO:[0-9]{7,8}$"),
    "PATO": re.compile(r"^PATO:[0-9]{7}$"),
    "METPO": re.compile(r"^METPO:[0-9]+$"),
    "CultureMech": re.compile(r"^CultureMech:(?!000000)[0-9]{6}$"),
    "MediaIngredientMech": re.compile(r"^MediaIngredientMech:[0-9]{6}$"),
}

VALID_CAUSAL_PREDICATES = {
    "CAUSES",
    "POSITIVELY_REGULATES",
    "NEGATIVELY_REGULATES",
    "ENABLES_GROWTH",
    "INHIBITS_GROWTH",
    "PROVIDES_COFACTOR_FOR",
    "TRANSPORTS_SUBSTRATE",
    "AFFECTS",
}

BARE_ROLE_TOKENS = {
    "CARBON_SOURCE",
    "NITROGEN_SOURCE",
    "SULFUR_SOURCE",
    "PHOSPHATE_SOURCE",
    "IRON_SOURCE",
    "TRACE_ELEMENT",
    "VITAMIN_SOURCE",
    "AMINO_ACID_SOURCE",
    "PROTEIN_SOURCE",
    "COFACTOR_PROVIDER",
    "ENERGY_SOURCE",
    "LIGHT_SOURCE",
    "BUFFER",
    "SOLIDIFYING_AGENT",
    "CHELATOR",
    "SURFACTANT",
    "REDUCING_AGENT",
    "OXIDIZING_AGENT",
    "PH_INDICATOR",
    "REDOX_INDICATOR",
    "SELECTIVE_AGENT",
    "ANTIFOAM",
    "OSMOTIC_AGENT",
    "PRECIPITATION_INHIBITOR",
    "SUBSTRATE",
    "ELECTRON_DONOR",
    "ELECTRON_ACCEPTOR",
    "COFACTOR",
    "PROSTHETIC_GROUP_PRECURSOR",
    "MEMBRANE_COMPONENT",
    "OSMOPROTECTANT",
    "INDUCER",
    "INHIBITOR",
    "QUENCHER",
}


@dataclass(frozen=True)
class CausalGraphIssue:
    """Single validation issue on a ``CausalEdge`` entry."""

    path: str
    category: str
    detail: str
    message: str
    level: str = "ERROR"

    @property
    def rule(self) -> str:
        return self.category


def iter_causal_graph_lists(
    instance: dict[str, Any],
) -> list[tuple[str, list[Any], str | None]]:
    """Return ``(json_path, causal_graphs_list, enclosing_organism_taxon_id)`` tuples."""
    found: list[tuple[str, list[Any], str | None]] = []
    if not isinstance(instance, dict):
        return found

    top = instance.get("causal_graphs")
    if isinstance(top, list):
        found.append(("causal_graphs", top, None))

    for org_idx, org in enumerate(instance.get("target_organisms") or []):
        if not isinstance(org, dict):
            continue
        org_taxon_id: str | None = None
        org_term = org.get("term")
        if isinstance(org_term, dict) and isinstance(org_term.get("id"), str):
            org_taxon_id = org_term["id"].strip() or None
        org_edges = org.get("causal_graphs")
        if isinstance(org_edges, list):
            found.append((f"target_organisms[{org_idx}].causal_graphs", org_edges, org_taxon_id))

    return found


def _validate_causal_term(
    term: Any,
    slot_name: str,
    path: str,
    issues: list[CausalGraphIssue],
) -> str | None:
    if not isinstance(term, dict):
        issues.append(
            CausalGraphIssue(
                path=f"{path}.{slot_name}",
                category="MISSING_CAUSAL_TERM",
                detail=slot_name,
                message=f"{path}.{slot_name}: must be a mapping with id and label",
            )
        )
        return None

    term_id = str(term.get("id") or "").strip()
    term_label = str(term.get("label") or "").strip()

    if term_id in BARE_ROLE_TOKENS or (
        ":" in term_id and term_id.split(":", 1)[1] in BARE_ROLE_TOKENS
    ):
        issues.append(
            CausalGraphIssue(
                path=f"{path}.{slot_name}.id",
                category="UNGROUNDED_CAUSAL_ROLE_TOKEN",
                detail=term_id,
                message=(
                    f"{path}.{slot_name}.id: {term_id!r} uses a bare ingredient-role token; "
                    "causal edges require ontology-grounded subject and object terms"
                ),
            )
        )
        return None

    if not term_id or not CAUSAL_TERM_ID_RE.match(term_id):
        issues.append(
            CausalGraphIssue(
                path=f"{path}.{slot_name}.id",
                category="INVALID_CAUSAL_TERM_ID",
                detail=term_id,
                message=(
                    f"{path}.{slot_name}.id: {term_id!r} is not a valid CausalTerm CURIE "
                    f"(expected {CAUSAL_TERM_ID_RE.pattern})"
                ),
            )
        )
        return None

    prefix = term_id.split(":", 1)[0]
    specific_re = PREFIX_SPECIFIC_PATTERNS.get(prefix)
    if specific_re is not None and not specific_re.match(term_id):
        issues.append(
            CausalGraphIssue(
                path=f"{path}.{slot_name}.id",
                category="INVALID_CAUSAL_TERM_ID",
                detail=term_id,
                message=(
                    f"{path}.{slot_name}.id: {term_id!r} does not match expected {prefix} "
                    f"identifier pattern ({specific_re.pattern})"
                ),
            )
        )

    if not term_label:
        issues.append(
            CausalGraphIssue(
                path=f"{path}.{slot_name}.label",
                category="EMPTY_CAUSAL_TERM_LABEL",
                detail=term_id,
                message=f"{path}.{slot_name}.label: must be a non-empty canonical or domain label",
            )
        )

    return term_id


def validate_causal_edge_entry(
    entry: Any,
    path: str,
    enclosing_organism_id: str | None = None,
) -> list[CausalGraphIssue]:
    """Validate one ``CausalEdge`` dictionary."""
    issues: list[CausalGraphIssue] = []

    if not isinstance(entry, dict):
        issues.append(
            CausalGraphIssue(
                path=path,
                category="INVALID_CAUSAL_EDGE_TYPE",
                detail=type(entry).__name__,
                message=f"{path}: CausalEdge must be a mapping, got {type(entry).__name__}",
            )
        )
        return issues

    edge_id = str(entry.get("id") or "").strip()
    if not edge_id or not CAUSAL_EDGE_ID_RE.match(edge_id):
        issues.append(
            CausalGraphIssue(
                path=f"{path}.id",
                category="INVALID_CAUSAL_EDGE_ID",
                detail=edge_id,
                message=(
                    f"{path}.id: {edge_id!r} must match "
                    f"{CAUSAL_EDGE_ID_RE.pattern} (e.g. 'edge_cobalamin_enables_growth')"
                ),
            )
        )

    subject_id = _validate_causal_term(entry.get("subject_term"), "subject_term", path, issues)
    object_id = _validate_causal_term(entry.get("object_term"), "object_term", path, issues)

    if subject_id and object_id and subject_id == object_id:
        issues.append(
            CausalGraphIssue(
                path=path,
                category="SELF_LOOP_CAUSAL_EDGE",
                detail=subject_id,
                message=(
                    f"{path}: CausalEdge subject_term.id and object_term.id must not be identical "
                    f"({subject_id!r})"
                ),
            )
        )

    predicate = str(entry.get("predicate") or "").strip()
    if predicate not in VALID_CAUSAL_PREDICATES:
        issues.append(
            CausalGraphIssue(
                path=f"{path}.predicate",
                category="INVALID_CAUSAL_PREDICATE",
                detail=predicate,
                message=(
                    f"{path}.predicate: {predicate!r} must be one of "
                    f"{sorted(VALID_CAUSAL_PREDICATES)}"
                ),
            )
        )

    protein_terms = entry.get("protein_terms")
    has_proteins = isinstance(protein_terms, list) and len(protein_terms) > 0

    organism_term = entry.get("organism_term")
    if organism_term is None:
        if enclosing_organism_id is not None or has_proteins:
            issues.append(
                CausalGraphIssue(
                    path=f"{path}.organism_term",
                    category="MISSING_ORGANISM_TERM",
                    detail=enclosing_organism_id or "protein_terms",
                    message=(
                        f"{path}.organism_term: required when a CausalEdge is nested under "
                        "target_organisms or specifies protein_terms"
                    ),
                )
            )
    elif not isinstance(organism_term, dict):
        issues.append(
            CausalGraphIssue(
                path=f"{path}.organism_term",
                category="MISSING_ORGANISM_TERM",
                detail=type(organism_term).__name__,
                message=f"{path}.organism_term: must be a mapping with id (NCBITaxon:...) and label",
            )
        )
    else:
        org_id = str(organism_term.get("id") or "").strip()
        org_label = str(organism_term.get("label") or "").strip()
        if not org_id or not NCBITAXON_CURIE_RE.match(org_id):
            issues.append(
                CausalGraphIssue(
                    path=f"{path}.organism_term.id",
                    category="INVALID_ORGANISM_TAXON",
                    detail=org_id,
                    message=f"{path}.organism_term.id: {org_id!r} must match ^NCBITaxon:[1-9][0-9]*$",
                )
            )
        if not org_label:
            issues.append(
                CausalGraphIssue(
                    path=f"{path}.organism_term.label",
                    category="EMPTY_ORGANISM_LABEL",
                    detail=org_id,
                    message=f"{path}.organism_term.label: must be a non-empty taxon scientific name",
                )
            )
        if (
            enclosing_organism_id
            and org_id
            and org_id != enclosing_organism_id
            and not str(entry.get("notes") or "").strip()
        ):
            issues.append(
                CausalGraphIssue(
                    path=f"{path}.organism_term.id",
                    category="ORGANISM_CONTEXT_MISMATCH",
                    detail=f"{org_id}!={enclosing_organism_id}",
                    message=(
                        f"{path}.organism_term.id: ({org_id}) differs from enclosing "
                        f"target_organisms[].term.id ({enclosing_organism_id}) without "
                        "an explanatory notes field"
                    ),
                )
            )

    if protein_terms is not None:
        if not isinstance(protein_terms, list):
            issues.append(
                CausalGraphIssue(
                    path=f"{path}.protein_terms",
                    category="INVALID_PROTEIN_TERMS",
                    detail=type(protein_terms).__name__,
                    message=f"{path}.protein_terms: must be a list of UniProtTerm mappings",
                )
            )
        else:
            seen_proteins: set[str] = set()
            for p_idx, p_term in enumerate(protein_terms):
                p_path = f"{path}.protein_terms[{p_idx}]"
                if not isinstance(p_term, dict):
                    issues.append(
                        CausalGraphIssue(
                            path=p_path,
                            category="INVALID_PROTEIN_TERMS",
                            detail=type(p_term).__name__,
                            message=f"{p_path}: each protein_terms entry must be a mapping with id and label",
                        )
                    )
                    continue
                p_id = str(p_term.get("id") or "").strip()
                p_label = str(p_term.get("label") or "").strip()
                if not p_id or not UNIPROT_CURIE_RE.match(p_id):
                    issues.append(
                        CausalGraphIssue(
                            path=f"{p_path}.id",
                            category="INVALID_UNIPROT_ACCESSION",
                            detail=p_id,
                            message=(
                                f"{p_path}.id: {p_id!r} is not a valid "
                                "UniProtKB primary accession CURIE"
                            ),
                        )
                    )
                elif p_id in seen_proteins:
                    issues.append(
                        CausalGraphIssue(
                            path=f"{p_path}.id",
                            category="DUPLICATE_PROTEIN_TERM",
                            detail=p_id,
                            message=f"{p_path}.id: duplicate UniProtKB accession {p_id} in {path}.protein_terms",
                        )
                    )
                else:
                    seen_proteins.add(p_id)
                if not p_label:
                    issues.append(
                        CausalGraphIssue(
                            path=f"{p_path}.label",
                            category="EMPTY_UNIPROT_LABEL",
                            detail=p_id,
                            message=f"{p_path}.label: must be a non-empty protein name",
                        )
                    )

    evidence = entry.get("evidence")
    if not isinstance(evidence, list) or len(evidence) == 0:
        issues.append(
            CausalGraphIssue(
                path=f"{path}.evidence",
                category="MISSING_EVIDENCE",
                detail="",
                message=f"{path}.evidence: CausalEdge requires at least one claim-scoped EvidenceItem",
            )
        )
        return issues

    seen_refs: set[str] = set()
    has_supporting_item = False
    for idx, ev in enumerate(evidence):
        ev_path = f"{path}.evidence[{idx}]"
        if not isinstance(ev, dict):
            issues.append(
                CausalGraphIssue(
                    path=ev_path,
                    category="INVALID_EVIDENCE_ITEM",
                    detail=type(ev).__name__,
                    message=f"{ev_path}: EvidenceItem must be a mapping",
                )
            )
            continue

        ref = str(ev.get("reference") or "").strip()
        if not ref or not REFERENCE_RE.match(ref):
            issues.append(
                CausalGraphIssue(
                    path=f"{ev_path}.reference",
                    category="INVALID_EVIDENCE_REFERENCE",
                    detail=ref,
                    message=(
                        f"{ev_path}.reference: {ref!r} must be a valid "
                        "PMID:..., DOI:..., doi:..., or http(s):// reference"
                    ),
                )
            )
        elif ref in seen_refs:
            issues.append(
                CausalGraphIssue(
                    path=f"{ev_path}.reference",
                    category="DUPLICATE_EVIDENCE_REFERENCE",
                    detail=ref,
                    message=f"{ev_path}.reference: duplicate reference {ref!r} inside {path}.evidence",
                )
            )
        else:
            seen_refs.add(ref)

        supports = str(ev.get("supports") or "").strip()
        if supports not in VALID_SUPPORTS:
            issues.append(
                CausalGraphIssue(
                    path=f"{ev_path}.supports",
                    category="INVALID_EVIDENCE_SUPPORTS",
                    detail=supports,
                    message=(
                        f"{ev_path}.supports: {supports!r} must be one of "
                        f"{sorted(VALID_SUPPORTS)}"
                    ),
                )
            )
        elif supports in POSITIVE_SUPPORTS:
            has_supporting_item = True

        snippet = str(ev.get("snippet") or "").strip()
        if not snippet:
            issues.append(
                CausalGraphIssue(
                    path=f"{ev_path}.snippet",
                    category="MISSING_EVIDENCE_SNIPPET",
                    detail=ref,
                    message=(
                        f"{ev_path}.snippet: must be a non-empty verbatim quote supporting "
                        "the causal mechanism claim"
                    ),
                )
            )

        explanation = str(ev.get("explanation") or "").strip()
        if not explanation:
            issues.append(
                CausalGraphIssue(
                    path=f"{ev_path}.explanation",
                    category="MISSING_EVIDENCE_EXPLANATION",
                    detail=ref,
                    message=f"{ev_path}.explanation: must be non-empty",
                )
            )

    if not has_supporting_item:
        issues.append(
            CausalGraphIssue(
                path=f"{path}.evidence",
                category="UNSUPPORTED_CAUSAL_EDGE",
                detail="",
                message=(
                    f"{path}.evidence: CausalEdge must have at least one EvidenceItem with "
                    "supports: SUPPORT or PARTIAL"
                ),
            )
        )

    return issues


def _validate_edge_list(
    edges: Any,
    list_path: str,
    enclosing_organism_id: str | None,
    issues: list[CausalGraphIssue],
) -> None:
    if edges is None:
        return
    if not isinstance(edges, list):
        issues.append(
            CausalGraphIssue(
                path=list_path,
                category="INVALID_CAUSAL_GRAPHS_LIST",
                detail=type(edges).__name__,
                message=f"{list_path}: must be a list of CausalEdge mappings",
            )
        )
        return

    seen_ids: set[str] = set()
    seen_tuples: set[tuple[str, str, str, str]] = set()
    for idx, entry in enumerate(edges):
        item_path = f"{list_path}[{idx}]"
        issues.extend(validate_causal_edge_entry(entry, item_path, enclosing_organism_id))
        if isinstance(entry, dict):
            edge_id = str(entry.get("id") or "").strip()
            if edge_id:
                if edge_id in seen_ids:
                    issues.append(
                        CausalGraphIssue(
                            path=item_path,
                            category="DUPLICATE_CAUSAL_EDGE_ID",
                            detail=edge_id,
                            message=f"{item_path}: duplicate CausalEdge.id {edge_id!r} within {list_path}",
                        )
                    )
                else:
                    seen_ids.add(edge_id)

            subj = entry.get("subject_term") if isinstance(entry.get("subject_term"), dict) else {}
            obj = entry.get("object_term") if isinstance(entry.get("object_term"), dict) else {}
            org = entry.get("organism_term") if isinstance(entry.get("organism_term"), dict) else {}
            subj_id = str((subj or {}).get("id") or "").strip()
            pred = str(entry.get("predicate") or "").strip()
            obj_id = str((obj or {}).get("id") or "").strip()
            org_id = str((org or {}).get("id") or enclosing_organism_id or "").strip()
            if subj_id and pred and obj_id:
                key = (subj_id, pred, obj_id, org_id)
                if key in seen_tuples:
                    issues.append(
                        CausalGraphIssue(
                            path=item_path,
                            category="DUPLICATE_CAUSAL_EDGE",
                            detail="|".join(key),
                            message=(
                                f"{item_path}: duplicate CausalEdge ({subj_id}, {pred}, {obj_id}, "
                                f"{org_id or 'unscoped'}) within {list_path}"
                            ),
                        )
                    )
                else:
                    seen_tuples.add(key)


def validate_recipe_causal_graphs(data: dict[str, Any]) -> list[CausalGraphIssue]:
    """Validate all ``causal_graphs`` slots in a parsed recipe dictionary."""
    if not isinstance(data, dict):
        return []

    issues: list[CausalGraphIssue] = []

    _validate_edge_list(data.get("causal_graphs"), "causal_graphs", None, issues)

    for org_idx, org in enumerate(data.get("target_organisms") or []):
        if not isinstance(org, dict):
            continue
        org_term = org.get("term") if isinstance(org.get("term"), dict) else {}
        enclosing_org_id = str((org_term or {}).get("id") or "").strip() or None
        org_path = f"target_organisms[{org_idx}]"
        _validate_edge_list(
            org.get("causal_graphs"),
            f"{org_path}.causal_graphs",
            enclosing_org_id,
            issues,
        )

    return issues


def causal_graph_validation_results(instance: dict[str, Any]) -> list[ValidationResult]:
    """Convert ``CausalGraphIssue`` items into LinkML ``ValidationResult`` objects."""
    return [
        ValidationResult(
            type="causal_graphs",
            severity=Severity.ERROR,
            message=issue.message,
            context=[issue.path],
        )
        for issue in validate_recipe_causal_graphs(instance)
    ]
