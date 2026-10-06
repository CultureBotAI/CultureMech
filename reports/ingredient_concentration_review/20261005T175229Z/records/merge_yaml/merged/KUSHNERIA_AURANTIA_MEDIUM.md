# Ingredient Concentration Review

- Record: data/merge_yaml/merged/KUSHNERIA_AURANTIA_MEDIUM.yaml
- ID: CultureMech:003330
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 17fb012c1214949f7fc4b484e657f59d8d86b3ecd6184c077090976450252576
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/9
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/archaea/KOMODO_1184_medium_FOR_HALOPHILIC_ARCHAEA.yaml
- data/normalized_yaml/archaea/KOMODO_1194_HALORUBRUM_CALIFORNIENSE_medium.yaml
- data/normalized_yaml/archaea/halorubrum_californiense_medium.yaml
- data/normalized_yaml/archaea/medium_for_halophilic_archaea.yaml
- data/normalized_yaml/bacterial/JCM_J980_KUSHNERIA_AURANTIA_MEDIUM.yaml
- data/normalized_yaml/bacterial/KOMODO_1195_KUSHNERIA_AURANTIA_medium.yaml
- data/normalized_yaml/bacterial/KOMODO_1213_THALASSOBACILLUS_CYRI_medium.yaml
- data/normalized_yaml/bacterial/TOGO_M1033_Kushneria_Aurantia_Medium.yaml
- data/normalized_yaml/bacterial/kushneria_aurantia_medium.yaml
- data/normalized_yaml/bacterial/thalassobacillus_cyri_medium.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Yeast extract | {"value": "5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / KCl | {"value": "5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / MgCl2 x 6 H2O | {"value": "32.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / MgSO4 x 7 H2O | {"value": "50.8", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / CaCl2 x 2 H2O | {"value": "0.8", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / NaHCO3 | {"value": "0.16", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[6].concentration / NaBr | {"value": "0.6", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[7].concentration / NaCl | {"value": "195", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[8].concentration / Agar | {"value": "20", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=980

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
