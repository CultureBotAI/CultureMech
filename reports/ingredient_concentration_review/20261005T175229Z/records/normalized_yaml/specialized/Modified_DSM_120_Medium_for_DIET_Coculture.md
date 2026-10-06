# Ingredient Concentration Review

- Record: data/normalized_yaml/specialized/Modified_DSM_120_Medium_for_DIET_Coculture.yaml
- ID: CultureMech:015434
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: b5dc486ab945ec564b532e7eba12e371463408dfa1394c940ef02e54ac972f42
- Layer: normalized
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/6
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/specialized/Modified_DSM_120_Medium_for_DIET_Coculture.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Ethanol | {"value": "20.0", "unit": "MILLIMOLAR"} | unscoped_context_evidence_needs_review;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Sodium bicarbonate | {"value": "2.0", "unit": "G_PER_L"} | unscoped_context_evidence_needs_review;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Sodium chloride | {"value": "1.0", "unit": "G_PER_L"} | unscoped_context_evidence_needs_review;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Calcium chloride dihydrate | {"value": "0.002", "unit": "G_PER_L"} | unscoped_context_evidence_needs_review;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / L-Cysteine | {"value": "1.0", "unit": "MILLIMOLAR"} | unscoped_context_evidence_needs_review;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / Sodium sulfide | {"value": "0.5", "unit": "MILLIMOLAR"} | unscoped_context_evidence_needs_review;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- PMID:24837373

## Unscoped Context Evidence

```json
[
  {
    "reference": "PMID:24837373",
    "supports": "SUPPORT",
    "snippet": "Cocultures formed aggregates that shared electrons via DIET during the stoichiometric conversion of ethanol to methane",
    "explanation": "Confirms ethanol as electron donor and DIET mechanism in coculture"
  }
]
```

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
