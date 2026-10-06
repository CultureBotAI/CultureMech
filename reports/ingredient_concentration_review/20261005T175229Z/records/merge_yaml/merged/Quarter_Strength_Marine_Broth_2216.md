# Ingredient Concentration Review

- Record: data/merge_yaml/merged/Quarter_Strength_Marine_Broth_2216.yaml
- ID: CultureMech:007635
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 4d2d4b4b2028781729feeda0c5c0e1bebf8d1b41b6fcc4ad941232aab91b92b3
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/2
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/marine_broth_2216_with_pyruvate.yaml
- data/normalized_yaml/bacterial/quarter_strength_marine_broth_2216.yaml
- data/normalized_yaml/specialized/marine_broth_2216_with_pyruvate.yaml
- data/normalized_yaml/specialized/quarter_strength_marine_broth_2216.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Distilled water | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Marine broth 2216 (BD-Difco) | {"value": "37.4", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://togomedium.org/medium/M1115
- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1049

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
