# Ingredient Concentration Review

- Record: data/normalized_yaml/bacterial/PCS_FP_medium_for_thermophilic_cellulose_degradation.yaml
- ID: CultureMech:015439
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 94c5b4306bcd2d2aebc15ac038732fa1d2232a951235ecb9ab5e1181105d9b61
- Layer: normalized
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/5
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/PCS_FP_medium_for_thermophilic_cellulose_degradation.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Filter paper (cellulose substrate) | {"value": "10.0", "unit": "G_PER_L"} | unscoped_context_evidence_needs_review;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Calcium carbonate | {"value": "2.0", "unit": "G_PER_L"} | unscoped_context_evidence_needs_review;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Yeast extract | {"value": "1.0", "unit": "G_PER_L"} | unscoped_context_evidence_needs_review;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Peptone | {"value": "5.0", "unit": "G_PER_L"} | unscoped_context_evidence_needs_review;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / Sodium chloride | {"value": "5.0", "unit": "G_PER_L"} | unscoped_context_evidence_needs_review;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- PMID:15545431
- PMID:16269746

## Unscoped Context Evidence

```json
[
  {
    "reference": "PMID:16269746",
    "supports": "SUPPORT",
    "snippet": "A cellulose-degrading defined mixed culture (designated SF356) consisting of five bacterial strains (Clostridium straminisolvens CSK1, Clostridium sp. strain FG4, Pseudoxanthomonas sp. strain M1-3, Brevibacillus sp. strain M1-5, and Bordetella sp. strain M1-6) exhibited both functional and structural stability",
    "explanation": "Establishes SF356 as a defined cellulose-degrading community (detailed medium composition in methods section includes PCS-FP medium with filter paper, yeast extract, peptone, NaCl, CaCO3 at pH 8.0, 50°C)"
  },
  {
    "reference": "PMID:15545431",
    "supports": "SUPPORT",
    "snippet": "The optimum temperature and initial pH for its growth and cellulose degradation are 50-55 degrees C and pH 7.5",
    "explanation": "Establishes optimal growth parameters for C. straminisolvens CSK1, the primary cellulolytic member"
  }
]
```

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
