# Ingredient Concentration Review

- Record: data/merge_yaml/merged/half_strength_murashige_skoog_medium_for_arabidopsis_growth.yaml
- ID: CultureMech:015433
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 8d9bdffbec7a31a46fe592f38781b370393a70e03ae4002d7f92c851cdbeadc5
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/3
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/specialized/Half_strength_Murashige_Skoog_medium_for_Arabidopsis_growth.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Murashige-Skoog basal salts | {"value": "0.5", "unit": "VARIABLE"} | unscoped_context_evidence_needs_review; VARIABLE_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Sucrose | {"value": "1.0", "unit": "PERCENT_W_V"} | unscoped_context_evidence_needs_review;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Agar | {"value": "0.8", "unit": "PERCENT_W_V"} | unscoped_context_evidence_needs_review;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- doi:10.1038/nature16192

## Unscoped Context Evidence

```json
[
  {
    "reference": "doi:10.1038/nature16192",
    "supports": "SUPPORT",
    "snippet": "Using defined bacterial communities and a gnotobiotic Arabidopsis plant system we show that the isolates form assemblies resembling natural microbiota on their cognate host organs, but are also capable of ectopic leaf or root colonization",
    "explanation": "Auto-filled placeholder: explanation not supplied by upstream import."
  }
]
```

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
