# Ingredient Concentration Review

- Record: data/merge_yaml/merged/asw_300_barley__009bee0b.yaml
- ID: CultureMech:000404
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: eeacdcf85af61174765407a1b3f2542f0ff547caa1450778844408d1487a0b1d
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/5
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/algae/CCAP_ASW 150 + barley  + barley grain_).yaml
- data/normalized_yaml/algae/CCAP_ASW 225 + barley  + barley grain_).yaml
- data/normalized_yaml/algae/CCAP_ASW 300 + barley  + barley grain_).yaml
- data/normalized_yaml/algae/asw_150_barley.yaml
- data/normalized_yaml/algae/asw_225_barley.yaml
- data/normalized_yaml/algae/asw_300_barley.yaml
- data/normalized_yaml/bacterial/asw_150_barley.yaml
- data/normalized_yaml/bacterial/asw_225_barley.yaml
- data/normalized_yaml/bacterial/asw_300_barley.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / NaCl | {"value": "136", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / KCl | {"value": "3.8", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / MgCl2 x 6 H2O | {"value": "8.9", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / MgSO4 x 7 H2O | {"value": "0.9", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / CaCl2 x 2 H2O | {"value": "0.65", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://www.ccap.ac.uk/wp-content/uploads/MR_ASW_300.pdf

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
