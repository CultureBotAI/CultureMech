# Ingredient Concentration Review

- Record: data/normalized_yaml/specialized/nitrogen_free_b_d_medium_for_lotus_japonicus_growth.yaml
- ID: CultureMech:015437
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: a9c142d6b8fde9d0949d3e25336474eee642522b0e5ca60c21ad00c20e7330a3
- Layer: normalized
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/4
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/specialized/nitrogen_free_b_d_medium_for_lotus_japonicus_growth.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Calcium chloride | {"value": "1.0", "unit": "MILLIMOLAR"} | unscoped_context_evidence_needs_review;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Magnesium sulfate | {"value": "0.5", "unit": "MILLIMOLAR"} | unscoped_context_evidence_needs_review;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Potassium phosphate | {"value": "0.7", "unit": "MILLIMOLAR"} | unscoped_context_evidence_needs_review;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Iron-EDTA | {"value": "50.0", "unit": "MICROMOLAR"} | unscoped_context_evidence_needs_review;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- PMID:34312531

## Unscoped Context Evidence

```json
[
  {
    "reference": "PMID:34312531",
    "supports": "SUPPORT",
    "snippet": "Sequential inoculation experiments revealed priority effects during root microbiota assembly, where established communities are resilient to invasion by latecomers, and that host preference of commensal bacteria confers a competitive advantage in their cognate host",
    "explanation": "Auto-filled placeholder: explanation not supplied by upstream import."
  }
]
```

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
