# Ingredient Concentration Review

- Record: data/normalized_yaml/specialized/Nitrogen_free_plant_nutrient_solution_for_soybean_growth.yaml
- ID: CultureMech:015438
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: fc5132d814bbb9795509f08b75072c0e7eaa86109fbfd35d8554fdc9b090370b
- Layer: normalized
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/4
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/specialized/Nitrogen_free_plant_nutrient_solution_for_soybean_growth.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Potassium phosphate | {"value": "1.0", "unit": "MILLIMOLAR"} | unscoped_context_evidence_needs_review;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Magnesium sulfate | {"value": "1.0", "unit": "MILLIMOLAR"} | unscoped_context_evidence_needs_review;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Calcium chloride | {"value": "2.0", "unit": "MILLIMOLAR"} | unscoped_context_evidence_needs_review;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Iron-EDTA | {"value": "100.0", "unit": "MICROMOLAR"} | unscoped_context_evidence_needs_review;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- PMID:40052412

## Unscoped Context Evidence

```json
[
  {
    "reference": "PMID:40052412",
    "supports": "SUPPORT",
    "snippet": "This sfSynCom based on the core-helper strategy was more effective at promoting nodulation than inoculation with BXYD3 alone and achieved effects comparable to those of a complex elite SynCom previously constructed on the basis of potential beneficial functions between microbes and plants alone",
    "explanation": "Auto-filled placeholder: explanation not supplied by upstream import."
  }
]
```

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
