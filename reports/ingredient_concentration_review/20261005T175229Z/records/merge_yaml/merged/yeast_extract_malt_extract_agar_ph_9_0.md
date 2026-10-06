# Ingredient Concentration Review

- Record: data/merge_yaml/merged/yeast_extract_malt_extract_agar_ph_9_0.yaml
- ID: CultureMech:010533
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 9b1d72542a4e8d964af1cfc1e990daaf79e0438b8ff1efcc9d80da0e77cbd996
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/4
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/1_10_yeast_extract_malt_extract_agar.yaml
- data/normalized_yaml/bacterial/TOGO_M73_Alkaline_Yeast_Extract-Malt_Extract_Agar.yaml
- data/normalized_yaml/bacterial/acidic_yeast_extract_malt_extract_agar_ph_5_0.yaml
- data/normalized_yaml/bacterial/alkaline_yeast_extract_malt_extract_agar.yaml
- data/normalized_yaml/bacterial/yeast_extract_malt_extract_agar_isp_2.yaml
- data/normalized_yaml/bacterial/yeast_extract_malt_extract_agar_isp_2_ph_8_5.yaml
- data/normalized_yaml/bacterial/yeast_extract_malt_extract_agar_ph_5_5.yaml
- data/normalized_yaml/bacterial/yeast_extract_malt_extract_agar_ph_6_0.yaml
- data/normalized_yaml/bacterial/yeast_extract_malt_extract_agar_ph_9_0.yaml
- data/normalized_yaml/fungal/1_10_yeast_extract_malt_extract_agar.yaml
- data/normalized_yaml/fungal/acidic_yeast_extract_malt_extract_agar_ph_5_0.yaml
- data/normalized_yaml/fungal/alkaline_yeast_extract_malt_extract_agar.yaml
- data/normalized_yaml/fungal/yeast_extract_malt_extract_agar_isp_2.yaml
- data/normalized_yaml/fungal/yeast_extract_malt_extract_agar_isp_2_ph_8_5.yaml
- data/normalized_yaml/fungal/yeast_extract_malt_extract_agar_ph_5_5.yaml
- data/normalized_yaml/fungal/yeast_extract_malt_extract_agar_ph_6_0.yaml
- data/normalized_yaml/fungal/yeast_extract_malt_extract_agar_ph_9_0.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Malt extract | {"value": "10", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Yeast extract | {"value": "4", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Glucose | {"value": "4", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Agar | {"value": "20", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=528

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
