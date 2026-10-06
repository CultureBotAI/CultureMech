# Ingredient Concentration Review

- Record: data/merge_yaml/merged/oatmeal_agar_ph_6_0.yaml
- ID: CultureMech:003034
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 003444394bc4f1e6b233fee953d239c60ea3be5d38110d51deca626726a71fac
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/5
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/TOGO_M394_Acidic_Oatmeal_Agar_pH_5.0.yaml
- data/normalized_yaml/bacterial/TOGO_M42_Oatmeal_Agar_ISP-3.yaml
- data/normalized_yaml/bacterial/TOGO_M709_Oatmeal_Agar_pH_6.0.yaml
- data/normalized_yaml/bacterial/acidic_oatmeal_agar_ph_5_0.yaml
- data/normalized_yaml/bacterial/oatmeal_agar_a_isp_3.yaml
- data/normalized_yaml/bacterial/oatmeal_agar_isp_3.yaml
- data/normalized_yaml/bacterial/oatmeal_agar_ph_6_0.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Oatmeal | {"value": "19.98", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Agar | {"value": "17.982", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / FeSO4 x 7 H2O | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence; PLAUSIBILITY_TRACE_SALT_AS_STOCK | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / MnCl2 x 4 H2O | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence; PLAUSIBILITY_TRACE_SALT_AS_STOCK | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / ZnSO4 x 7 H2O | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence; PLAUSIBILITY_TRACE_SALT_AS_STOCK | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=689

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
