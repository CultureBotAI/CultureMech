# Ingredient Concentration Review

- Record: data/normalized_yaml/bacterial/TOGO_M455_Alkali-Reinforced_Clostridial_Agar.yaml
- ID: CultureMech:009842
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 42ea3ad0c8e46a9e4842df153d37e3aac44148fff251eb9e26a962beff7ca8ae
- Layer: normalized
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/4
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/TOGO_M455_Alkali-Reinforced_Clostridial_Agar.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Reinforced clostridial agar (Sigma) | {"value": "51.0", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Distilled water | {"value": "900.0", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[0].concentration / 10% Na2CO3 solution | {"value": "100.0", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[0].composition[0].concentration / Na2CO3 | {"value": "10.0", "unit": "PERCENT_W_V"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://mediadive.dsmz.de/medium/J455
- https://togomedium.org/medium/M455
- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=455

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
