# Ingredient Concentration Review

- Record: data/normalized_yaml/bacterial/pplo_broth_without_cv_ph_7_8_with_horse_serum_not_inactivated_and_yeast_extract.yaml
- ID: CultureMech:008814
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 13bb2fd5c82b8d58a2d2e7a2d960d1875b8734dde9a271926ee4cb239de3189b
- Layer: normalized
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/4
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/pplo_broth_without_cv_ph_7_8_with_horse_serum_not_inactivated_and_yeast_extract.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / PPLO broth | {"value": "21.0", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Distilled water | {"value": "700.0", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Horse serum | {"value": "200.0", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Fresh Baker’s Yeast Extract (GIBCO 18180) | {"value": "100.0", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://togomedium.org/medium/M2226
- https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2226
- https://www.atcc.org/~/media/AD2BC56A0BA94572A40803C02D24D35A.ashx

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
