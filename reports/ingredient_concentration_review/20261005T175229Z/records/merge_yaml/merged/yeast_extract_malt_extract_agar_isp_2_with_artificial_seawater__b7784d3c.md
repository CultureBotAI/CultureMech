# Ingredient Concentration Review

- Record: data/merge_yaml/merged/yeast_extract_malt_extract_agar_isp_2_with_artificial_seawater__b7784d3c.yaml
- ID: CultureMech:008374
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: b75830c4682254537bc3facdbb5b56fb39ce55ede419d8083c65f8df02dd5c3a
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/5
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/TOGO_M573_Yeast_Extract-Malt_Extract_Agar_ISP-2_With_Artificial_Seawater.yaml
- data/normalized_yaml/bacterial/TOGO_M73_Alkaline_Yeast_Extract-Malt_Extract_Agar.yaml
- data/normalized_yaml/bacterial/alkaline_yeast_extract_malt_extract_agar.yaml
- data/normalized_yaml/bacterial/yeast_extract_malt_extract_agar_isp_2_with_artificial_seawater.yaml
- data/normalized_yaml/fungal/alkaline_yeast_extract_malt_extract_agar.yaml
- data/normalized_yaml/fungal/yeast_extract_malt_extract_agar_isp_2_with_artificial_seawater.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Bacto Malt Extract (Difco) | {"value": "10", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Artificial seawater | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Glucose | {"value": "4", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Agar | {"value": "15", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / Bacto Yeast Extract (Difco) | {"value": "4", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://togomedium.org/medium/M1804
- https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1030

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
