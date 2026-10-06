# Ingredient Concentration Review

- Record: data/merge_yaml/merged/YPG_MEDIUM.yaml
- ID: CultureMech:000614
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: bad6bfe2cb25a77143d178137cd67d9d44b47f2e691f028e362199813744072c
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/4
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/DSMZ_1172_YPG_MEDIUM.yaml
- data/normalized_yaml/bacterial/JCM_J349_ANCYLOBACTER-SPIROSOMA_MEDIUM.yaml
- data/normalized_yaml/bacterial/JCM_J404_YPG_MEDIUM.yaml
- data/normalized_yaml/bacterial/KOMODO_1017_YPG_medium.yaml
- data/normalized_yaml/bacterial/KOMODO_1172_YPG_medium.yaml
- data/normalized_yaml/bacterial/KOMODO_774_medium_FOR_PARACOCCUS_AMINOPHILUS_AND_P._AMINOVORANS.yaml
- data/normalized_yaml/bacterial/KOMODO_7_ANCYLOBACTER_-_SPIROSOMA_medium.yaml
- data/normalized_yaml/bacterial/TOGO_M130_PYG_Agar_A.yaml
- data/normalized_yaml/bacterial/TOGO_M2840_YPG_medium.yaml
- data/normalized_yaml/bacterial/TOGO_M344_Ancylobacter-Spirosoma_Medium.yaml
- data/normalized_yaml/bacterial/TOGO_M402_YPG_Medium.yaml
- data/normalized_yaml/bacterial/ancylobacter_spirosoma_medium.yaml
- data/normalized_yaml/bacterial/glucose_yeast_peptone_medium.yaml
- data/normalized_yaml/bacterial/medium_7_modified_for_dsm_9000.yaml
- data/normalized_yaml/bacterial/medium_for_paracoccus_aminophilus_and_p_aminovorans.yaml
- data/normalized_yaml/bacterial/pyg_agar_a.yaml
- data/normalized_yaml/bacterial/ypg_medium.yaml
- data/normalized_yaml/fungal/glucose_yeast_peptone_medium.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Yeast extract | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Peptone | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Glucose | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Agar | {"value": "15", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1172.pdf

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
