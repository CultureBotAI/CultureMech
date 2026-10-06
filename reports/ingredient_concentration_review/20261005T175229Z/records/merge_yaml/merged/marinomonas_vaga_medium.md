# Ingredient Concentration Review

- Record: data/merge_yaml/merged/marinomonas_vaga_medium.yaml
- ID: CultureMech:006109
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 87e2c5569c8fcf4c97e693d4e4cb37dae7671bfc6c4bc51950ea9690d9c20eb5
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/5
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/KOMODO_617_MARINOMONAS_VAGA_medium.yaml
- data/normalized_yaml/bacterial/KOMODO_617a_BLOOD_AGAR_BASE_OXOID_CM55.yaml
- data/normalized_yaml/bacterial/blood_agar_base_oxoid_cm55.yaml
- data/normalized_yaml/bacterial/for_dsm_7232.yaml
- data/normalized_yaml/bacterial/marinomonas_vaga_medium.yaml
- data/normalized_yaml/bacterial/na_medium.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Beef extract | {"value": "10", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Peptone | {"value": "10", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / NaCl | {"value": "30", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Agar | {"value": "15", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / Tap water | {"value": "1000", "unit": "G_PER_L"} | missing_attached_evidence; PLAUSIBILITY_WATER_AS_VOLUME | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.


## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
