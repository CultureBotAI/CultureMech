# Ingredient Concentration Review

- Record: data/merge_yaml/merged/sporulation_medium.yaml
- ID: CultureMech:005909
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: b2785f2b55e273fd6a7101fad968f2014b1480b779bd1e9cb32d704e05856faa
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/7
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/KOMODO_531_SPORULATION_medium.yaml
- data/normalized_yaml/bacterial/TOGO_M1868_Sporulation_Medium.yaml
- data/normalized_yaml/bacterial/medium_531_modified_for_dsm_1314.yaml
- data/normalized_yaml/bacterial/medium_531_modified_for_dsm_4332.yaml
- data/normalized_yaml/bacterial/medium_531_modified_for_dsm_4333.yaml
- data/normalized_yaml/bacterial/medium_531_modified_for_dsm_4334.yaml
- data/normalized_yaml/bacterial/medium_531_modified_for_dsm_4335.yaml
- data/normalized_yaml/bacterial/medium_531_modified_for_dsm_6800.yaml
- data/normalized_yaml/bacterial/medium_531_modified_for_dsm_6801.yaml
- data/normalized_yaml/bacterial/medium_531_modified_for_dsm_6802.yaml
- data/normalized_yaml/bacterial/medium_531_modified_for_dsm_6803.yaml
- data/normalized_yaml/bacterial/medium_531_modified_for_dsm_6804.yaml
- data/normalized_yaml/bacterial/medium_531_modified_for_dsm_6805.yaml
- data/normalized_yaml/bacterial/sporulation_medium.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Nutrient broth | {"value": "6", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Yeast extract | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Trypticase | {"value": "2", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / MnSO4 x H2O | {"value": "0.0005", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / Marine Broth | {"value": "0.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / Agar | {"value": "10", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[6].concentration / Inosin | {"value": "0.00134113", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.


## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
