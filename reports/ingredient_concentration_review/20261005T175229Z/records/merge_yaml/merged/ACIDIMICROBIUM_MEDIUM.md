# Ingredient Concentration Review

- Record: data/merge_yaml/merged/ACIDIMICROBIUM_MEDIUM.yaml
- ID: CultureMech:003043
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: bcbc0cfaa1f1051913222f30e78b3a8c90309af82e60f9b73fa4f2f9e0227fae
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/6
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/JCM_J698_ACIDIMICROBIUM_MEDIUM.yaml
- data/normalized_yaml/bacterial/KOMODO_709_ACIDIMICROBIUM_medium.yaml
- data/normalized_yaml/bacterial/TOGO_M1783_Acidimicrobium_Medium.yaml
- data/normalized_yaml/bacterial/TOGO_M1784_Acidimicrobium_Medium.yaml
- data/normalized_yaml/bacterial/TOGO_M2332_Acidimicrobium_Medium.yaml
- data/normalized_yaml/bacterial/TOGO_M718_Acidimicrobium_Medium.yaml
- data/normalized_yaml/bacterial/TOGO_M719_Acidimicrobium_Medium.yaml
- data/normalized_yaml/bacterial/acidimicrobium_medium.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / MgSO4 x 7 H2O | {"value": "0.4", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / (NH4)2SO4 | {"value": "0.2", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / KCl | {"value": "0.1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / K2HPO4 | {"value": "0.1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / FeSO4 x 7 H2O | {"value": "25", "unit": "G_PER_L"} | missing_attached_evidence; PLAUSIBILITY_TRACE_SALT_AS_STOCK | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / Yeast extract | {"value": "0.16", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=698

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
