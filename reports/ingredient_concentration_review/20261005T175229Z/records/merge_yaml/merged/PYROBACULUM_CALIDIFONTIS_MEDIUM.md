# Ingredient Concentration Review

- Record: data/merge_yaml/merged/PYROBACULUM_CALIDIFONTIS_MEDIUM.yaml
- ID: CultureMech:002697
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 94edab8a0042701c54971dd33625cfa9ed73059200a071bbfeb2f7f6e1524108
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/3
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/archaea/JCM_J338_PYROBACULUM_CALIDIFONTIS_MEDIUM.yaml
- data/normalized_yaml/archaea/KOMODO_1090_PYROBACULUM_CALIDIFONTIS_medium.yaml
- data/normalized_yaml/archaea/TOGO_M2457_Pyrobaculum_Calidifontis_Medium.yaml
- data/normalized_yaml/archaea/TOGO_M333_Pyrobaculum_Calidifontis_Medium.yaml
- data/normalized_yaml/archaea/pyrobaculum_calidifontis_medium.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Tryptone | {"value": "10", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Yeast extract | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Na2S2O3 x 5 H2O | {"value": "3", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=338

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
