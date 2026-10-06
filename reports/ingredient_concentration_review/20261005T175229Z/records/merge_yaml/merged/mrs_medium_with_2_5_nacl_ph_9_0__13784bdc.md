# Ingredient Concentration Review

- Record: data/merge_yaml/merged/mrs_medium_with_2_5_nacl_ph_9_0__13784bdc.yaml
- ID: CultureMech:003279
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: d7906ee884fbfc86bcf98ba8e438fcb6ece93702c50d4b3610eef1b5392bf852
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/3
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/TOGO_M249_MRS_Medium_With_10_NaCl.yaml
- data/normalized_yaml/bacterial/TOGO_M602_MRS_Medium_With_2.5_NaCl.yaml
- data/normalized_yaml/bacterial/TOGO_M977_MRS_Medium_With_2.5_NaCl_pH_9.0.yaml
- data/normalized_yaml/bacterial/mrs_medium_with_10_nacl.yaml
- data/normalized_yaml/bacterial/mrs_medium_with_2_5_nacl.yaml
- data/normalized_yaml/bacterial/mrs_medium_with_2_5_nacl_ph_9_0.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Lactobacilli MRS broth | {"value": "55", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / NaCl | {"value": "100", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Agar | {"value": "15", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=931

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
