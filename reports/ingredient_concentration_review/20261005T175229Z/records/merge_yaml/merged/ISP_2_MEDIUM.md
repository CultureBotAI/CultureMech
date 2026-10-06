# Ingredient Concentration Review

- Record: data/merge_yaml/merged/ISP_2_MEDIUM.yaml
- ID: CultureMech:002169
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: cf78946b817576f1ca6cae5a485dcb14122ac9a66d38f2ec4f49c1abb9d3aabe
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/4
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/isp2_medium.yaml
- data/normalized_yaml/bacterial/isp_2_medium.yaml
- data/normalized_yaml/bacterial/medium_987_modified_for_dsm_15665.yaml
- data/normalized_yaml/bacterial/medium_987_modified_for_dsm_41839.yaml
- data/normalized_yaml/bacterial/medium_987_modified_for_dsm_44928.yaml
- data/normalized_yaml/bacterial/medium_987_modified_for_dsm_45080.yaml
- data/normalized_yaml/bacterial/medium_987_modified_for_dsm_45096.yaml
- data/normalized_yaml/bacterial/medium_987_modified_for_dsm_45452.yaml
- data/normalized_yaml/bacterial/medium_987_modified_for_dsm_45783.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Yeast extract | {"value": "4", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Malt extract | {"value": "10", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Dextrose | {"value": "4", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Agar | {"value": "20", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium987.pdf

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
