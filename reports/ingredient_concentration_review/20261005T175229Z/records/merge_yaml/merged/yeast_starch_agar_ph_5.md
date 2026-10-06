# Ingredient Concentration Review

- Record: data/merge_yaml/merged/yeast_starch_agar_ph_5.yaml
- ID: CultureMech:008229
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: d0e0b3a8706d9b2f9ab19c4b04862f9b3b0935199eb486aa23c42a5ec32e00d3
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/4
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/1_10_yeast_starch_agar.yaml
- data/normalized_yaml/bacterial/1_5_yeast_starch_agar.yaml
- data/normalized_yaml/bacterial/half_strength_yeast_starch_agar.yaml
- data/normalized_yaml/bacterial/yeast_extract_starch_agar.yaml
- data/normalized_yaml/bacterial/yeast_extract_starch_agar_ph_5_5.yaml
- data/normalized_yaml/bacterial/yeast_starch_agar_ph_5.yaml
- data/normalized_yaml/fungal/1_10_yeast_starch_agar.yaml
- data/normalized_yaml/fungal/1_5_yeast_starch_agar.yaml
- data/normalized_yaml/fungal/half_strength_yeast_starch_agar.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Distilled water | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Yeast extract | {"value": "0.2", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Soluble starch | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Agar | {"value": "15", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://togomedium.org/medium/M1671
- https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=876

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
