# Ingredient Concentration Review

- Record: data/normalized_yaml/bacterial/yeast_extract_malt_extract_agar_isp_2_with_5_nacl.yaml
- ID: CultureMech:008596
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 29e47bf0bfd01d06fa0440cae59f853777d5c0a286f72ae39eb515fec9b94c1c
- Layer: normalized
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/2
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/yeast_extract_malt_extract_agar_isp_2_with_5_nacl.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / NaCl | {"value": "50", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[0].concentration / Yeast extract-malt extract agar (ISP-2) | {"value": "1000", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://togomedium.org/medium/M200
- https://togomedium.org/medium/M35
- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=207
- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=43

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
