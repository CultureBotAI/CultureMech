# Ingredient Concentration Review

- Record: data/merge_yaml/merged/sulfolobus_medium_b.yaml
- ID: CultureMech:002532
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 4ea30eac5289333870701f548816e1b4e0149d772ec21e3b6799c70f92523a7d
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/13
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/archaea/TOGO_M165_Sulfolobus_Medium_B.yaml
- data/normalized_yaml/archaea/sulfolobus_medium_b.yaml
- data/normalized_yaml/bacterial/KOMODO_670_MS-MEDIUM.yaml
- data/normalized_yaml/bacterial/TOGO_M261_MS_Medium.yaml
- data/normalized_yaml/bacterial/TOGO_M847_Modified_Brock_s_Basal_Salts-Yeast_Extract-Tryptone_Medium.yaml
- data/normalized_yaml/bacterial/modified_brocks_basal_salts_yeast_extract_medeium_b.yaml
- data/normalized_yaml/bacterial/modified_brocks_basal_salts_yeast_extract_medium.yaml
- data/normalized_yaml/bacterial/modified_brocks_basal_salts_yeast_extract_tryptone_medium.yaml
- data/normalized_yaml/bacterial/ms_medium.yaml
- data/normalized_yaml/fungal/modified_brocks_basal_salts_yeast_extract_medeium_b.yaml
- data/normalized_yaml/fungal/modified_brocks_basal_salts_yeast_extract_medium.yaml
- data/normalized_yaml/fungal/modified_brocks_basal_salts_yeast_extract_tryptone_medium.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Yeast extract | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / (NH4)2SO4 | {"value": "1.3", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / KH2PO4 | {"value": "0.28", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / MgSO4 x 7 H2O | {"value": "0.25", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / CaCl2 x 2 H2O | {"value": "0.07", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / FeCl3 x 6 H2O | {"value": "0.002", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[6].concentration / MnCl2 x 4 H2O | {"value": "0.0018", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[7].concentration / Na2B4O7 x 10 H2O | {"value": "0.0045", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[8].concentration / ZnSO4 x 7 H2O | {"value": "0.00022", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[9].concentration / CuCl2 x 2 H2O | {"value": "5e-05", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[10].concentration / Na2MoO4 x 2 H2O | {"value": "3e-05", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[11].concentration / VOSO4 x n H2O | {"value": "3e-05", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[12].concentration / CoSO4 x 7 H2O | {"value": "1e-05", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=172

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
