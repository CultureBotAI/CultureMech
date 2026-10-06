# Ingredient Concentration Review

- Record: data/merge_yaml/merged/yeast_extract_malt_extract_agar_isp_2_with_5_nacl_ph_9_0.yaml
- ID: CultureMech:009920
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 4581e93376555b8cfa590f12ba87af59f9fc4c2ea65838e460c54c467c9014a8
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/3
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/marine_agar_2216_with_10_nacl.yaml
- data/normalized_yaml/bacterial/marine_agar_2216_with_1_nacl.yaml
- data/normalized_yaml/bacterial/marine_agar_2216_with_3_1_nacl.yaml
- data/normalized_yaml/bacterial/marine_agar_2216_with_5_nacl.yaml
- data/normalized_yaml/bacterial/marine_agar_2216_with_8_0_nacl.yaml
- data/normalized_yaml/bacterial/marine_agar_2216_with_8_nacl.yaml
- data/normalized_yaml/bacterial/togo_medium_m61.yaml
- data/normalized_yaml/bacterial/yeast_extract_malt_extract_agar_isp_2_with_2_nacl.yaml
- data/normalized_yaml/bacterial/yeast_extract_malt_extract_agar_isp_2_with_5_nacl.yaml
- data/normalized_yaml/bacterial/yeast_extract_malt_extract_agar_isp_2_with_5_nacl_ph_9_0.yaml
- data/normalized_yaml/fungal/yeast_extract_malt_extract_agar_isp_2_with_2_nacl.yaml
- data/normalized_yaml/fungal/yeast_extract_malt_extract_agar_isp_2_with_5_nacl.yaml
- data/normalized_yaml/fungal/yeast_extract_malt_extract_agar_isp_2_with_5_nacl_ph_9_0.yaml
- data/normalized_yaml/specialized/marine_agar_2216_with_10_nacl.yaml
- data/normalized_yaml/specialized/marine_agar_2216_with_1_nacl.yaml
- data/normalized_yaml/specialized/marine_agar_2216_with_3_1_nacl.yaml
- data/normalized_yaml/specialized/marine_agar_2216_with_5_nacl.yaml
- data/normalized_yaml/specialized/marine_agar_2216_with_8_0_nacl.yaml
- data/normalized_yaml/specialized/marine_agar_2216_with_8_nacl.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / NaCl | {"value": "30", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[0].concentration / Yeast extract--malt extract agar (ISP--2) (see Medium [M35]) | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[1].concentration / Na2CO3 solution | {"value": "variable", "unit": "VARIABLE"} | missing_attached_evidence; VARIABLE_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://togomedium.org/medium/M528
- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=527

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
