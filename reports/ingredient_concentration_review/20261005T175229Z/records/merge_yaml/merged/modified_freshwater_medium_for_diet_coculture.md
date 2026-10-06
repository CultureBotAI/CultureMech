# Ingredient Concentration Review

- Record: data/merge_yaml/merged/modified_freshwater_medium_for_diet_coculture.yaml
- ID: CultureMech:015435
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 470e6295d52e39939c9f67aee8f197d67cd53f8390e656f54a72ad17bbfb8ab7
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/3
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/specialized/Modified_Freshwater_Medium_for_DIET_Coculture.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Ethanol | {"value": "20.0", "unit": "MILLIMOLAR"} | unscoped_context_evidence_needs_review;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / L-Cysteine | {"value": "1.0", "unit": "MILLIMOLAR"} | unscoped_context_evidence_needs_review;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Sodium sulfide nonahydrate | {"value": "0.5", "unit": "MILLIMOLAR"} | unscoped_context_evidence_needs_review;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- doi:10.1039/C3EE42189A

## Unscoped Context Evidence

```json
[
  {
    "reference": "doi:10.1039/C3EE42189A",
    "supports": "SUPPORT",
    "snippet": "This possibility was further investigated in defined co-cultures of Geobacter metallireducens and Methanosaeta harundinacea which stoichiometrically converted ethanol to methane",
    "explanation": "Describes ethanol conversion to methane in defined coculture using specialized medium"
  }
]
```

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
