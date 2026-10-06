# Ingredient Concentration Review

- Record: data/merge_yaml/merged/BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml
- ID: CultureMech:002203
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: b594afe75190d85f49bb29af81efbd16e4b84f31d332e1f481a8bd9167ea7284
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/7
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/JCM_J101_BACILLUS_ACIDOCALDARIUS_MEDIUM.yaml
- data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml
- data/normalized_yaml/bacterial/TOGO_M93_Bacillus_Acidocaldarius_Medium.yaml
- data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml
- data/normalized_yaml/bacterial/bryocella_elongata_medium.yaml
- data/normalized_yaml/bacterial/medium_13_modified_for_dsm_13609.yaml
- data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17974.yaml
- data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17975.yaml
- data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17978.yaml
- data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17979.yaml
- data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17980.yaml
- data/normalized_yaml/bacterial/medium_13_modified_for_dsm_17981.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Yeast extract | {"value": "2", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / (NH4)2SO4 | {"value": "0.4", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / MgSO4 x 7 H2O | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / CaCl2 x 2 H2O | {"value": "0.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / KH2PO4 | {"value": "1.2", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / Glucose | {"value": "2", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[6].concentration / Agar | {"value": "40", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=101

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
