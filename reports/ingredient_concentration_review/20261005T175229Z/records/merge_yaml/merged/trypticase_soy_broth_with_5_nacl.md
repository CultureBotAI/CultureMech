# Ingredient Concentration Review

- Record: data/merge_yaml/merged/trypticase_soy_broth_with_5_nacl.yaml
- ID: CultureMech:010326
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 31329f334984b8fb7a98b3f8b0e93ba56d04be519f0328d75e940be53f502f11
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/9
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/TOGO_M2515_tryptic_soy_broth.yaml
- data/normalized_yaml/bacterial/TOGO_M2516_tryptic_soy_agar.yaml
- data/normalized_yaml/bacterial/TOGO_M2834_tryptic_soy_agar.yaml
- data/normalized_yaml/bacterial/TOGO_M907_Trypticase_Soy_Broth_With_5_NaCl.yaml
- data/normalized_yaml/bacterial/full_media_trypticase_soy_broth_medium.yaml
- data/normalized_yaml/bacterial/tryptic_soy_agar.yaml
- data/normalized_yaml/bacterial/tryptic_soy_broth.yaml
- data/normalized_yaml/bacterial/tryptic_soy_broth_without_glucose_difco_media.yaml
- data/normalized_yaml/bacterial/tsa_ph_5_5.yaml
- data/normalized_yaml/bacterial/tsb_ph5_5.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Distilled water | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / NaCl | {"value": "30", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Agar | {"value": "15", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Pancreatic digest of casein | {"value": "17.0", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / Peptic digest of soybean meal | {"value": "3.0", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / Glucose | {"value": "2.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[6].concentration / Sodium chloride | {"value": "5.0", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[7].concentration / Dipotassium phosphate | {"value": "2.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[8].concentration / Agar | {"value": "15.0", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://en.wikipedia.org/wiki/Tryptic_soy_broth
- https://togomedium.org/medium/M907
- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=869

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
