# Ingredient Concentration Review

- Record: data/normalized_yaml/bacterial/Bold_Trace_Stock.yaml
- ID: CultureMech:015441
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 8050c406026827ab030a5b37729397d0f99fe958afbae35c0a2f13d69b6938e7
- Layer: normalized
- Record kind: SOLUTION
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/6
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/Bold_Trace_Stock.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| composition[0].concentration / Sulfuric acid (concentrated) | {"value": "10", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| composition[1].concentration / Zinc sulfate heptahydrate | {"value": "8.82", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| composition[2].concentration / Manganese chloride tetrahydrate | {"value": "1.44", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| composition[3].concentration / Molybdenum trioxide | {"value": "0.71", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| composition[4].concentration / Copper sulfate pentahydrate | {"value": "1.57", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| composition[5].concentration / Cobalt nitrate hexahydrate | {"value": "0.49", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://cccryo.fraunhofer.de/sources/files/medien/BBM.pdf
- https://utex.org/products/bbm-bold-trace-stock-solution

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
