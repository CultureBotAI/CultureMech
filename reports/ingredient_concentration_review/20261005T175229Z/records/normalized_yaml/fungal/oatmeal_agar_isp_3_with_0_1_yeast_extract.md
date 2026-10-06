# Ingredient Concentration Review

- Record: data/normalized_yaml/fungal/oatmeal_agar_isp_3_with_0_1_yeast_extract.yaml
- ID: CultureMech:010531
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 12ebd6d3ad29995ef3ef73cb60cf16aaaf7e047c93571fa551a3f1a54d03d6ae
- Layer: normalized
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/2
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/fungal/oatmeal_agar_isp_3_with_0_1_yeast_extract.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Yeast extract | {"value": "1.0", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[0].concentration / Oatmeal agar (ISP-3) | {"value": "1000", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=50
- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=51

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
