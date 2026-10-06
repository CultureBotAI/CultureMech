# Ingredient Concentration Review

- Record: data/merge_yaml/merged/inorganic_salts_starch_agar_isp_4_with_0_05_yeast_extract.yaml
- ID: CultureMech:008702
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 3a84f6d38147afc48a0b38ce77cabdf0d91551a89f9448317ab1cccef4a33053
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/2
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/inorganic_salts_starch_agar_isp_4_with_0_05_yeast_extract.yaml
- data/normalized_yaml/fungal/inorganic_salts_starch_agar_isp_4_with_0_05_yeast_extract.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Yeast extract | {"value": "0.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[0].concentration / Inorganic salts--starch agar (ISP--4) (see Medium [M50]) | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://togomedium.org/medium/M210
- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=217

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
