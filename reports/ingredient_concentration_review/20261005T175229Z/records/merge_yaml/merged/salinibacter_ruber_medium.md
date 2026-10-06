# Ingredient Concentration Review

- Record: data/merge_yaml/merged/salinibacter_ruber_medium.yaml
- ID: CultureMech:006858
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: cfec2102bf967a7f1b6d33d21c58d007cb2b716f9c6a78d6437cc5a81c056df5
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/8
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/archaea/KOMODO_1138_HALOPIGER_medium.yaml
- data/normalized_yaml/archaea/TOGO_M2294_Halopiger_Medium.yaml
- data/normalized_yaml/archaea/halopiger_medium.yaml
- data/normalized_yaml/bacterial/KOMODO_936_SALINIBACTER_RUBER_medium.yaml
- data/normalized_yaml/bacterial/TOGO_M1068_SW-7.5_Medium.yaml
- data/normalized_yaml/bacterial/TOGO_M1069_SW-7.5_Medium.yaml
- data/normalized_yaml/bacterial/TOGO_M629_SW-20_Medium.yaml
- data/normalized_yaml/bacterial/TOGO_M630_SW-20_Medium.yaml
- data/normalized_yaml/bacterial/TOGO_M831_SW-10_Medium.yaml
- data/normalized_yaml/bacterial/TOGO_M832_SW-10_Medium.yaml
- data/normalized_yaml/bacterial/halophile_yeast_extract_medium.yaml
- data/normalized_yaml/bacterial/salinibacter_ruber_medium.yaml
- data/normalized_yaml/bacterial/sw_10_medium.yaml
- data/normalized_yaml/bacterial/sw_20_medium.yaml
- data/normalized_yaml/bacterial/sw_7_5_medium.yaml
- data/normalized_yaml/fungal/halophile_yeast_extract_medium.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / NaCl | {"value": "195", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / MgCl2 x 6 H2O | {"value": "32.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / MgSO4 x 7 H2O | {"value": "50.8", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / CaCl2 x 2 H2O | {"value": "0.8", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / KCl | {"value": "5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / NaHCO3 | {"value": "0.16", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[6].concentration / NaBr | {"value": "0.6", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[7].concentration / Yeast extract | {"value": "5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.


## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
