# Ingredient Concentration Review

- Record: data/merge_yaml/merged/nitrogen_free_medium_for_leptospirillum_ferrodiazotrophum.yaml
- ID: CultureMech:015436
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 19249c9d9948cbcd4ec02e570c62f4775049577926355d248ebadafb9e200cf8
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/3
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/Nitrogen_Free_Medium_for_Leptospirillum_ferrodiazotrophum.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Iron(II) sulfate | {"value": "30.0", "unit": "G_PER_L"} | unscoped_context_evidence_needs_review;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Magnesium sulfate | {"value": "0.4", "unit": "G_PER_L"} | unscoped_context_evidence_needs_review;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Monopotassium phosphate | {"value": "0.05", "unit": "G_PER_L"} | unscoped_context_evidence_needs_review;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- PMID:16204553

## Unscoped Context Evidence

```json
[
  {
    "reference": "PMID:16204553",
    "supports": "SUPPORT",
    "snippet": "An AMD biofilm sample naturally abundant in Leptospirillum group III cells was homogenized, filtered, and serially diluted into a nitrogen-free liquid medium. The resulting culture in the terminal dilution grew autotrophically to a maximum cell density of approximately 10(6) cells/ml, oxidizing ferrous iron as the sole energy source",
    "explanation": "Describes selective cultivation strategy and growth characteristics of L. ferrodiazotrophum"
  },
  {
    "reference": "PMID:16204553",
    "supports": "SUPPORT",
    "snippet": "Based on the prediction that this organism is solely responsible for nitrogen fixation in the community, we pursued a selective isolation strategy to obtain the organism in pure culture",
    "explanation": "Explains nitrogen-free medium design rationale for isolating the nitrogen fixer"
  },
  {
    "reference": "PMID:16204553",
    "supports": "SUPPORT",
    "snippet": "We propose the name Leptospirillum ferrodiazotrophum sp. nov. for this iron-oxidizing, free-living diazotroph",
    "explanation": "Confirms successful cultivation and characterization as iron-oxidizing diazotroph"
  }
]
```

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
