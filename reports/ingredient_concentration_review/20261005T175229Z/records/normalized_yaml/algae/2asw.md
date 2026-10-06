# Ingredient Concentration Review

- Record: data/normalized_yaml/algae/2asw.yaml
- ID: CultureMech:000038
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 053eddfef16e4b36735349b8876fd3cadf9ef84eb95c134d7b77d50cff5cc4d0
- Layer: normalized
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/15
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/algae/2asw.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / NaNO | {"value": "15.00", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Na2HPO4 | {"value": "0.60", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / K2HPO4 | {"value": "0.50", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Biotin | {"value": "0.0002", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / Calcium pantothenate | {"value": "0.02", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / Cyanocobalamin | {"value": "0.004", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[6].concentration / Folic acid | {"value": "0.0004", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[7].concentration / Inositol | {"value": "1.0", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[8].concentration / Nicotinic acid | {"value": "0.02", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[9].concentration / Thiamine HCl | {"value": "0.1", "unit": "G_PER_L"} | missing_attached_evidence; PLAUSIBILITY_INDICATOR_UNIT_SLIP | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[10].concentration / Thymine | {"value": "0.6", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[11].concentration / Tricine | {"value": "0.50", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[12].concentration / NaCl | {"value": "35.00", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| variants[0].modifications / f_2asw | ["Supplement the artificial seawater base with half-strength Guillard f solution.", "Use liquid or agar-solidified F/2ASW depending on maintenance, transformation, or selection protocol.", "Reported diatom conditions include 20 deg C, continuous illumination at 30-75 umol photons m-2 s-1, and aeration with ambient air or CO2-enriched air."] | incomplete_or_nonqualifying_attached_evidence; VARIANT_TEXT_REQUIRES_SOURCE_REVIEW | unsupported; not_performed | unknown | [{"reference": "DOI:10.1104/pp.18.00453", "supports": "SUPPORT", "explanation": "Matsui et al. explicitly define F/2ASW as artificial seawater plus half-strength Guillard f solution for Phaeodactylum tricornutum UTEX 642 and Thalassiosira pseudonana CCMP1335 cultivation."}] |
| variants[1].modifications / modified_f_2asw_sodium_response | ["Supplement F/2ASW with 10 nM sodium selenite and 0.1 mM sodium metasilicate.", "Manipulate sodium by changing NaCl added to the basal artificial seawater.", "Preacclimate cells to sodium concentrations before low-sodium transfer."] | incomplete_or_nonqualifying_attached_evidence; VARIANT_TEXT_REQUIRES_SOURCE_REVIEW | unsupported; not_performed | unknown | [{"reference": "DOI:10.1007/s10126-021-10037-4", "supports": "SUPPORT", "explanation": "Tsuji et al. report Chaetoceros gracilis UTEX LB2658 growth and carbon-concentrating-mechanism experiments in modified F/2ASW with defined sodium manipulations."}] |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- DOI:10.1007/s10126-021-10037-4
- DOI:10.1104/pp.18.00453
- https://www.ccap.ac.uk/catalogue/strain-19-18
- https://www.ccap.ac.uk/wp-content/uploads/MR_2ASW.pdf

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
