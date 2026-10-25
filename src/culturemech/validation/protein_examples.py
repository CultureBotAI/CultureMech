"""Semantic and structural validation for typed UniProtKB ProteinExample entries.

Complements LinkML closed-schema validation (`UniProtTerm` and `ProteinExample`
in `src/culturemech/schema/culturemech.yaml`) by enforcing:

1. Canonical UniProtKB primary accession syntax on `uniprot_term.id` and
   non-empty `uniprot_term.label`.
2. Explicit `NCBITaxon` CURIE on `organism_term.id` and non-empty
   `organism_term.label`, plus taxon consistency when nested inside a
   `target_organisms[i]` entry that declares `term.id` (unless `notes`
   explicitly documents a strain/subspecies/parent-taxon relationship).
3. Claim-scoped `evidence` (non-empty list of `EvidenceItem` dicts) where each
   item carries a valid `reference` (`PMID:...`, `DOI:...`, `doi:...`, or
   `http(s)://...`), a valid `supports` enum token (with at least one
   `SUPPORT` or `PARTIAL` item per protein example), a non-empty verbatim
   `snippet`, and a non-empty `explanation`.
4. Valid optional `ec_number` (`EC:...`) and `cofactor_term` / `substrate_term`
   `(id, label)` pairs when supplied.
5. No duplicate `(uniprot_term.id, organism_term.id)` pairs within the same
   `protein_examples` list.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

from linkml.validator.report import Severity, ValidationResult

UNIPROT_CURIE_RE = re.compile(
    r"^UniProtKB:([OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9]([A-Z][A-Z0-9]{2}[0-9]){1,2})$"
)
NCBITAXON_CURIE_RE = re.compile(r"^NCBITaxon:[1-9][0-9]*$")
EC_CURIE_RE = re.compile(r"^EC:[0-9]+(\.([0-9]+|-)){0,3}$")
CHEM_CURIE_RE = re.compile(r"^(CHEBI|FOODON|MICRO|UBERON|ENVO|mediadive\.compound):\w+$")
REFERENCE_RE = re.compile(r"^(PMID:[0-9]+|DOI:10\.[^/\s]+/\S+|doi:10\.[^/\s]+/\S+|https?://\S+)$")

VALID_SUPPORTS = {"SUPPORT", "PARTIAL", "REFUTE", "NO_EVIDENCE", "WRONG_STATEMENT"}
POSITIVE_SUPPORTS = {"SUPPORT", "PARTIAL"}


@dataclass(frozen=True)
class ProteinExampleIssue:
    """Single validation issue on a `ProteinExample` entry."""

    path: str
    category: str
    detail: str
    message: str


def _non_empty_str(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def is_valid_uniprot_curie(value: Any) -> bool:
    """Return True when `value` is a canonical UniProtKB accession CURIE."""
    return _non_empty_str(value) and bool(UNIPROT_CURIE_RE.match(str(value)))


def iter_protein_example_lists(
    instance: dict[str, Any],
) -> list[tuple[str, list[Any], str | None]]:
    """Return `(json_path, protein_examples_list, enclosing_organism_taxon_id)` tuples.

    Walks all schema-supported attachment points for `protein_examples`:
    - `MediaRecipe.protein_examples`
    - `MediaRecipe.target_organisms[*].protein_examples`
    - `MediaRecipe.target_organisms[*].cofactor_requirements[*].protein_examples`
    - `MediaRecipe.target_organisms[*].cofactor_requirements[*].cofactor.protein_examples`
    - `MediaRecipe.target_organisms[*].transporters[*].protein_examples`
    - `cofactors[*].protein_examples` (reference cofactor catalog shape)
    """
    found: list[tuple[str, list[Any], str | None]] = []
    if not isinstance(instance, dict):
        return found

    top = instance.get("protein_examples")
    if isinstance(top, list):
        found.append(("protein_examples", top, None))

    for org_idx, org in enumerate(instance.get("target_organisms") or []):
        if not isinstance(org, dict):
            continue
        org_taxon_id: str | None = None
        org_term = org.get("term")
        if isinstance(org_term, dict) and isinstance(org_term.get("id"), str):
            org_taxon_id = org_term["id"].strip()

        org_pe = org.get("protein_examples")
        if isinstance(org_pe, list):
            found.append((f"target_organisms[{org_idx}].protein_examples", org_pe, org_taxon_id))

        for cr_idx, cr in enumerate(org.get("cofactor_requirements") or []):
            if not isinstance(cr, dict):
                continue
            cr_pe = cr.get("protein_examples")
            if isinstance(cr_pe, list):
                found.append(
                    (
                        f"target_organisms[{org_idx}].cofactor_requirements[{cr_idx}].protein_examples",
                        cr_pe,
                        org_taxon_id,
                    )
                )
            cof = cr.get("cofactor")
            if isinstance(cof, dict):
                cof_pe = cof.get("protein_examples")
                if isinstance(cof_pe, list):
                    found.append(
                        (
                            f"target_organisms[{org_idx}].cofactor_requirements[{cr_idx}].cofactor.protein_examples",
                            cof_pe,
                            org_taxon_id,
                        )
                    )

        for tr_idx, tr in enumerate(org.get("transporters") or []):
            if not isinstance(tr, dict):
                continue
            tr_pe = tr.get("protein_examples")
            if isinstance(tr_pe, list):
                found.append(
                    (
                        f"target_organisms[{org_idx}].transporters[{tr_idx}].protein_examples",
                        tr_pe,
                        org_taxon_id,
                    )
                )

    for cof_idx, cof in enumerate(instance.get("cofactors") or []):
        if not isinstance(cof, dict):
            continue
        cof_pe = cof.get("protein_examples")
        if isinstance(cof_pe, list):
            found.append((f"cofactors[{cof_idx}].protein_examples", cof_pe, None))

    return found


def validate_protein_example_entry(
    entry: Any,
    path: str,
    *,
    enclosing_organism_id: str | None = None,
) -> list[ProteinExampleIssue]:
    """Validate one `ProteinExample` mapping."""
    issues: list[ProteinExampleIssue] = []
    if not isinstance(entry, dict):
        issues.append(
            ProteinExampleIssue(
                path=path,
                category="protein_example_type",
                detail=type(entry).__name__,
                message=f"{path}: ProteinExample entry must be a mapping, got {type(entry).__name__}",
            )
        )
        return issues

    # 1. uniprot_term
    uterm = entry.get("uniprot_term")
    if not isinstance(uterm, dict):
        issues.append(
            ProteinExampleIssue(
                path=f"{path}.uniprot_term",
                category="missing_uniprot_term",
                detail="uniprot_term",
                message=f"{path}.uniprot_term: required UniProtTerm mapping is missing",
            )
        )
    else:
        uid = uterm.get("id")
        ulabel = uterm.get("label")
        if not _non_empty_str(uid) or not UNIPROT_CURIE_RE.match(str(uid)):
            issues.append(
                ProteinExampleIssue(
                    path=f"{path}.uniprot_term.id",
                    category="invalid_uniprot_accession",
                    detail=f"id={uid!r}",
                    message=(
                        f"{path}.uniprot_term.id: invalid UniProtKB accession {uid!r}; "
                        "expected canonical UniProtKB:<6-or-10-char accession>"
                    ),
                )
            )
        if not _non_empty_str(ulabel):
            issues.append(
                ProteinExampleIssue(
                    path=f"{path}.uniprot_term.label",
                    category="missing_uniprot_label",
                    detail="label",
                    message=f"{path}.uniprot_term.label: non-empty protein label is required",
                )
            )

    # 2. organism_term
    oterm = entry.get("organism_term")
    if not isinstance(oterm, dict):
        issues.append(
            ProteinExampleIssue(
                path=f"{path}.organism_term",
                category="missing_organism_term",
                detail="organism_term",
                message=f"{path}.organism_term: required OrganismTerm mapping is missing",
            )
        )
    else:
        oid = oterm.get("id")
        olabel = oterm.get("label")
        if not _non_empty_str(oid) or not NCBITAXON_CURIE_RE.match(str(oid)):
            issues.append(
                ProteinExampleIssue(
                    path=f"{path}.organism_term.id",
                    category="invalid_organism_taxon",
                    detail=f"id={oid!r}",
                    message=(
                        f"{path}.organism_term.id: invalid NCBITaxon CURIE {oid!r}; "
                        "expected NCBITaxon:<positive integer>"
                    ),
                )
            )
        if not _non_empty_str(olabel):
            issues.append(
                ProteinExampleIssue(
                    path=f"{path}.organism_term.label",
                    category="missing_organism_label",
                    detail="label",
                    message=f"{path}.organism_term.label: non-empty organism scientific name is required",
                )
            )
        if (
            enclosing_organism_id
            and _non_empty_str(oid)
            and str(oid) != enclosing_organism_id
            and not _non_empty_str(entry.get("notes"))
        ):
            issues.append(
                ProteinExampleIssue(
                    path=f"{path}.organism_term.id",
                    category="organism_taxon_mismatch",
                    detail=f"{oid}!={enclosing_organism_id}",
                    message=(
                        f"{path}.organism_term.id: {oid} differs from enclosing target_organisms "
                        f"taxon {enclosing_organism_id} without an explanatory `notes` entry"
                    ),
                )
            )

    # 3. Optional EC number and chemical terms
    ec_num = entry.get("ec_number")
    if ec_num is not None and (not _non_empty_str(ec_num) or not EC_CURIE_RE.match(str(ec_num))):
        issues.append(
            ProteinExampleIssue(
                path=f"{path}.ec_number",
                category="invalid_ec_number",
                detail=f"ec_number={ec_num!r}",
                message=f"{path}.ec_number: invalid EC CURIE {ec_num!r}; expected EC:<digits>",
            )
        )

    for slot_name in ("cofactor_term", "substrate_term"):
        chem = entry.get(slot_name)
        if chem is None:
            continue
        if not isinstance(chem, dict):
            issues.append(
                ProteinExampleIssue(
                    path=f"{path}.{slot_name}",
                    category="invalid_chemical_term",
                    detail=slot_name,
                    message=f"{path}.{slot_name}: expected Term mapping",
                )
            )
            continue
        cid = chem.get("id")
        clabel = chem.get("label")
        if not _non_empty_str(cid) or not CHEM_CURIE_RE.match(str(cid)):
            issues.append(
                ProteinExampleIssue(
                    path=f"{path}.{slot_name}.id",
                    category="invalid_chemical_term_id",
                    detail=f"id={cid!r}",
                    message=f"{path}.{slot_name}.id: invalid chemical term CURIE {cid!r}",
                )
            )
        if not _non_empty_str(clabel):
            issues.append(
                ProteinExampleIssue(
                    path=f"{path}.{slot_name}.label",
                    category="missing_chemical_term_label",
                    detail=slot_name,
                    message=f"{path}.{slot_name}.label: non-empty label is required when {slot_name} is provided",
                )
            )

    # 4. Claim-scoped evidence
    evidence = entry.get("evidence")
    if not isinstance(evidence, list) or len(evidence) == 0:
        issues.append(
            ProteinExampleIssue(
                path=f"{path}.evidence",
                category="missing_protein_evidence",
                detail="evidence",
                message=f"{path}.evidence: at least one claim-scoped EvidenceItem is required",
            )
        )
    else:
        has_positive_support = False
        seen_refs: set[str] = set()
        for ev_idx, ev in enumerate(evidence):
            ev_path = f"{path}.evidence[{ev_idx}]"
            if not isinstance(ev, dict):
                issues.append(
                    ProteinExampleIssue(
                        path=ev_path,
                        category="invalid_evidence_item",
                        detail=type(ev).__name__,
                        message=f"{ev_path}: EvidenceItem must be a mapping",
                    )
                )
                continue
            ref = ev.get("reference")
            supports = ev.get("supports")
            snippet = ev.get("snippet")
            explanation = ev.get("explanation")
            if not _non_empty_str(ref) or not REFERENCE_RE.match(str(ref).strip()):
                issues.append(
                    ProteinExampleIssue(
                        path=f"{ev_path}.reference",
                        category="invalid_evidence_reference",
                        detail=f"reference={ref!r}",
                        message=(
                            f"{ev_path}.reference: expected PMID:<id>, DOI:10.<prefix>/<suffix>, "
                            f"or https:// URL; got {ref!r}"
                        ),
                    )
                )
            else:
                ref_str = str(ref).strip()
                if ref_str in seen_refs:
                    issues.append(
                        ProteinExampleIssue(
                            path=f"{ev_path}.reference",
                            category="duplicate_evidence_reference",
                            detail=ref_str,
                            message=f"{ev_path}.reference: duplicate reference {ref_str} in evidence list",
                        )
                    )
                seen_refs.add(ref_str)

            if supports not in VALID_SUPPORTS:
                issues.append(
                    ProteinExampleIssue(
                        path=f"{ev_path}.supports",
                        category="invalid_evidence_supports",
                        detail=f"supports={supports!r}",
                        message=f"{ev_path}.supports: {supports!r} is not one of {sorted(VALID_SUPPORTS)}",
                    )
                )
            elif supports in POSITIVE_SUPPORTS:
                has_positive_support = True

            if not _non_empty_str(snippet):
                issues.append(
                    ProteinExampleIssue(
                        path=f"{ev_path}.snippet",
                        category="missing_evidence_snippet",
                        detail="snippet",
                        message=f"{ev_path}.snippet: non-empty supporting text snippet is required for ProteinExample",
                    )
                )

            if not _non_empty_str(explanation):
                issues.append(
                    ProteinExampleIssue(
                        path=f"{ev_path}.explanation",
                        category="missing_evidence_explanation",
                        detail="explanation",
                        message=f"{ev_path}.explanation: non-empty explanation is required for ProteinExample",
                    )
                )

        if not has_positive_support:
            issues.append(
                ProteinExampleIssue(
                    path=f"{path}.evidence",
                    category="no_supporting_evidence",
                    detail="supports",
                    message=(
                        f"{path}.evidence: at least one EvidenceItem must have supports "
                        "set to SUPPORT or PARTIAL"
                    ),
                )
            )

    return issues


def validate_recipe_protein_examples(instance: dict[str, Any]) -> list[ProteinExampleIssue]:
    """Validate all `protein_examples` lists in a recipe or reference document."""
    all_issues: list[ProteinExampleIssue] = []
    for list_path, entries, enclosing_org_id in iter_protein_example_lists(instance):
        seen_pairs: set[tuple[str, str]] = set()
        for idx, entry in enumerate(entries):
            item_path = f"{list_path}[{idx}]"
            all_issues.extend(
                validate_protein_example_entry(
                    entry,
                    item_path,
                    enclosing_organism_id=enclosing_org_id,
                )
            )
            if isinstance(entry, dict):
                ut = entry.get("uniprot_term")
                ot = entry.get("organism_term")
                uid = ut.get("id") if isinstance(ut, dict) else None
                oid = ot.get("id") if isinstance(ot, dict) else None
                if _non_empty_str(uid) and _non_empty_str(oid):
                    pair = (str(uid).strip(), str(oid).strip())
                    if pair in seen_pairs:
                        all_issues.append(
                            ProteinExampleIssue(
                                path=item_path,
                                category="duplicate_protein_example",
                                detail=f"{pair[0]}|{pair[1]}",
                                message=(
                                    f"{item_path}: duplicate (uniprot_term.id, organism_term.id) "
                                    f"pair {pair} in {list_path}"
                                ),
                            )
                        )
                    seen_pairs.add(pair)
    return all_issues


def protein_example_validation_results(instance: dict[str, Any]) -> list[ValidationResult]:
    """Convert `ProteinExampleIssue` items into LinkML `ValidationResult` objects."""
    return [
        ValidationResult(
            type="protein_examples",
            severity=Severity.ERROR,
            message=issue.message,
            context=[issue.path],
        )
        for issue in validate_recipe_protein_examples(instance)
    ]
