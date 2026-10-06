# Ingredient Concentration Review

- Record: data/merge_yaml/merged/glycerol_fermentation_medium_for_diet_coculture.yaml
- ID: CultureMech:015432
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 8abfc4f31f4642da9bc2500e6c7104ef8a5c01f9d73f41ff5dfd2abc6cc40656
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/9
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/specialized/Glycerol_Fermentation_Medium_for_DIET_Coculture.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Glycerol | {"value": "10.0", "unit": "G_PER_L"} | unscoped_context_evidence_needs_review;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Sodium acetate | {"value": "0.82", "unit": "G_PER_L"} | unscoped_context_evidence_needs_review;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Ammonium chloride | {"value": "2.0", "unit": "G_PER_L"} | unscoped_context_evidence_needs_review;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Sodium dihydrogen phosphate | {"value": "2.45", "unit": "G_PER_L"} | unscoped_context_evidence_needs_review;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / Disodium hydrogen phosphate | {"value": "4.58", "unit": "G_PER_L"} | unscoped_context_evidence_needs_review;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / Sodium sulfate | {"value": "0.28", "unit": "G_PER_L"} | unscoped_context_evidence_needs_review;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[6].concentration / Magnesium chloride hexahydrate | {"value": "0.26", "unit": "G_PER_L"} | unscoped_context_evidence_needs_review;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[7].concentration / Calcium chloride dihydrate | {"value": "2.9", "unit": "MG_PER_L"} | unscoped_context_evidence_needs_review;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[8].concentration / L-Cysteine | {"value": "0.5", "unit": "G_PER_L"} | unscoped_context_evidence_needs_review;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- PMID:28287150

## Unscoped Context Evidence

```json
[
  {
    "reference": "PMID:28287150",
    "supports": "SUPPORT",
    "snippet": "The present study deals with a co-culture of Geobacter sulfurreducens and Clostridium pasteurianum during glycerol fermentation",
    "explanation": "Describes glycerol fermentation medium for coculture"
  },
  {
    "reference": "PMID:28287150",
    "supports": "SUPPORT",
    "snippet": "The present study deals with a co-culture of Geobacter sulfurreducens and Clostridium pasteurianum during glycerol fermentation",
    "explanation": "Confirms glycerol fermentation medium for DIET coculture"
  },
  {
    "reference": "PMID:28287150",
    "supports": "SUPPORT",
    "snippet": "Using this mechanism could be an efficient and cost-effective way to directly control redox balances in co-culture fermentation",
    "explanation": "Establishes anaerobic requirement maintained using Hungate technique"
  }
]
```

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
