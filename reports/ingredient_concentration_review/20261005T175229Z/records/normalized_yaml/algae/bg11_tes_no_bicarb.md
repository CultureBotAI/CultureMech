# Ingredient Concentration Review

- Record: data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml
- ID: CultureMech:015453
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 8b47248a8605be05777c32a1034484710f0962dd91350dc66b994ee97656d815
- Layer: normalized
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/14
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/algae/bg11_tes_no_bicarb.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Sodium nitrate | {"value": "17.6", "unit": "MILLIMOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Potassium phosphate dibasic | {"value": "0.2", "unit": "MILLIMOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Magnesium Sulfate Heptahydrate | {"value": "0.3", "unit": "MILLIMOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Calcium chloride dihydrate | {"value": "0.24", "unit": "MILLIMOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / Citric Acid | {"value": "28.5", "unit": "MICROMOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / Ferric ammonium citrate | {"value": "0.006", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[6].concentration / EDTA (disodium salt) | {"value": "2.4", "unit": "MICROMOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[7].concentration / Boric Acid | {"value": "0.00286", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[8].concentration / Manganese (II) chloride tetrahydrate | {"value": "0.0018100000000000002", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[9].concentration / Zinc sulfate heptahydrate | {"value": "0.000222", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[10].concentration / Sodium Molybdate Dihydrate | {"value": "0.00039000000000000005", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[11].concentration / Copper (II) sulfate pentahydrate | {"value": "7.9e-05", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[12].concentration / Cobalt(II) nitrate hexahydrate | {"value": "0.0494", "unit": "MG_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[13].concentration / TES | {"value": "20", "unit": "MILLIMOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://github.com/CultureBotAI/CultureBotHT

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
