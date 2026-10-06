# Ingredient Concentration Review

- Record: data/merge_yaml/merged/POTATO_DEXTROSE_AGAR.yaml
- ID: CultureMech:004047
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: f9937526b398859c04e7fd1d480d7ab2519e702f860d650541b0a53a32a6bd6a
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/3
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/KOMODO_129_POTATO_DEXTROSE_AGAR.yaml
- data/normalized_yaml/bacterial/TOGO_M1721_Potato_Dextrose_Agar.yaml
- data/normalized_yaml/bacterial/TOGO_M23_Potato-Dextrose_Agar.yaml
- data/normalized_yaml/bacterial/potato_dextrose_agar.yaml
- data/normalized_yaml/fungal/potato_dextrose_agar.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Glucose | {"value": "20", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Agar | {"value": "15", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Potato | {"value": "200", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.


## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
