# Ingredient Concentration Review

- Record: data/merge_yaml/merged/YPD_MEDIUM.yaml
- ID: CultureMech:005177
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 418327a6d24d0131e57eef4663c27d37e092a3bb6e4d2c0c236786173450e403
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/3
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/KOMODO_1199_K7_medium.yaml
- data/normalized_yaml/bacterial/KOMODO_21_SARCINA_medium.yaml
- data/normalized_yaml/bacterial/KOMODO_393_YPD_medium.yaml
- data/normalized_yaml/bacterial/TOGO_M1434_YPD_Medium.yaml
- data/normalized_yaml/bacterial/for_dsm_19966.yaml
- data/normalized_yaml/bacterial/for_dsm_25088.yaml
- data/normalized_yaml/bacterial/k7_medium.yaml
- data/normalized_yaml/bacterial/sarcina_medium.yaml
- data/normalized_yaml/bacterial/ypd_medium.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Glucose | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Yeast extract | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Peptone | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.


## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
