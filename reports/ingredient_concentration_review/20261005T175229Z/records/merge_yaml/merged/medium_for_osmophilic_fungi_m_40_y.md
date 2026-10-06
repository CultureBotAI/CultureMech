# Ingredient Concentration Review

- Record: data/merge_yaml/merged/medium_for_osmophilic_fungi_m_40_y.yaml
- ID: CultureMech:004211
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 3259d0f5fd098746e8f41d300c44ff0018f468ad783097b1b9e7ae8c3f71c8bf
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/4
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/KOMODO_187_medium_FOR_OSMOPHILIC_FUNGI_M_40_Y.yaml
- data/normalized_yaml/bacterial/TOGO_M26_M40Y_Agar.yaml
- data/normalized_yaml/bacterial/TOGO_M27_M60Y_Agar.yaml
- data/normalized_yaml/bacterial/TOGO_M3048_M40Y_agar.yaml
- data/normalized_yaml/bacterial/m40y_agar.yaml
- data/normalized_yaml/bacterial/m60y_agar.yaml
- data/normalized_yaml/bacterial/medium_for_osmophilic_fungi_m_40_y.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Sucrose | {"value": "400", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Malt extract | {"value": "20", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Yeast extract | {"value": "5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Agar | {"value": "20", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.


## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
