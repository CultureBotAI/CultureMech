# Ingredient Concentration Review

- Record: data/merge_yaml/merged/isp_medium_2_with_5_nacl.yaml
- ID: CultureMech:006155
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: e798e24da5887a52c4d4ff0b4f8b260dddf0168e48e6dc0b89b37885f957f48d
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/5
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/KOMODO_636_ISP_medium_2_WITH_5_NaCl.yaml
- data/normalized_yaml/bacterial/isp_medium_2_with_5_nacl.yaml
- data/normalized_yaml/bacterial/medium_636_modified_for_dsm_14598.yaml
- data/normalized_yaml/bacterial/medium_636_modified_for_dsm_18447.yaml
- data/normalized_yaml/bacterial/medium_636_modified_for_dsm_45264.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Yeast extract | {"value": "4", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Malt extract | {"value": "10", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Dextrose | {"value": "4", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Agar | {"value": "20", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / NaCl | {"value": "50", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.


## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
