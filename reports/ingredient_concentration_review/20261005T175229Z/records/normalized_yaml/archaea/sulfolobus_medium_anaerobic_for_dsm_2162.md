# Ingredient Concentration Review

- Record: data/normalized_yaml/archaea/sulfolobus_medium_anaerobic_for_dsm_2162.yaml
- ID: CultureMech:009226
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 34c2c8e2888f6614545b81ea073636df1c911644a42db5cc0ba6659a03a3f9f9
- Layer: normalized
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/22
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/archaea/sulfolobus_medium_anaerobic_for_dsm_2162.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Distilled water | {"value": "1000.0", "unit": "G_PER_L"} | missing_attached_evidence; PLAUSIBILITY_WATER_AS_VOLUME | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / MgSO4 x 7 H2O | {"value": "0.25", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / CaCl2 x 2 H2O | {"value": "0.07", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / KH2PO4 | {"value": "0.28", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / Na2S x 9 H2O | {"value": "0.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / (NH4)2SO4 | {"value": "1.3", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[6].concentration / FeCl3 x 6 H2O | {"value": "0.02", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[7].concentration / Sulfur, powder | {"value": "10", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[8].concentration / Yeast extract (OXOID) | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[9].concentration / 1 N H2SO4 | {"value": "variable", "unit": "VARIABLE"} | missing_attached_evidence; VARIABLE_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[10].concentration / N2 gas | {"value": "variable", "unit": "VARIABLE"} | missing_attached_evidence; VARIABLE_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[11].concentration / Na2MoO4 x 2 H2O | {"value": "3", "unit": "G_PER_L"} | missing_attached_evidence; PLAUSIBILITY_TRACE_SALT_AS_STOCK | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[12].concentration / MnCl2 x 4 H2O | {"value": "180", "unit": "G_PER_L"} | missing_attached_evidence; PLAUSIBILITY_TRACE_SALT_AS_STOCK | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[13].concentration / ZnSO4 x 7 H2O | {"value": "22", "unit": "G_PER_L"} | missing_attached_evidence; PLAUSIBILITY_TRACE_SALT_AS_STOCK | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[14].concentration / CuCl2 x 2 H2O | {"value": "5", "unit": "G_PER_L"} | missing_attached_evidence; PLAUSIBILITY_TRACE_SALT_AS_STOCK | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[15].concentration / VOSO4 x 2 H2O | {"value": "3", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[16].concentration / Na2B4O7 x 10 H2O | {"value": "450", "unit": "G_PER_L"} | missing_attached_evidence; PLAUSIBILITY_TRACE_SALT_AS_STOCK | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[17].concentration / CoSO4 | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence; PLAUSIBILITY_TRACE_SALT_AS_STOCK | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[18].concentration / 1 N HCl | {"value": "variable", "unit": "VARIABLE"} | missing_attached_evidence; VARIABLE_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[0].concentration / Allen’s trace element solution | {"value": "10", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| variants[0].modifications / aerobic_brocks_salts_dsm88_sulfur_yeast_extract | ["Low-sulfate Brock's salts base (MgSO4 reduced/replaced); NH4Cl instead of (NH4)2SO4", "10 g/L elemental sulfur; species-specific 0.2-1 g/L yeast extract (or sucrose + NZ-Amine)", "AEROBIC: vented serum bottles with foam stoppers; NO Na2S reducing agent; NO N2 gas phase", "65-75C; pH 2-3 (acidified with H2SO4 or HCl)"] | candidate_needs_source_verification; VARIANT_TEXT_REQUIRES_SOURCE_REVIEW | unsupported; retrieval_failed; exact quote and concentration not verified | unknown | [{"reference": "doi:10.1128/mbio.01033-24", "supports": "SUPPORT", "explanation": "Willard et al. 2024 is the shared source for the aerobic DSM-88 variant across these strains.", "snippet": "All Sulfolobaceae species were grown in a low-sulfate formulation of Brock’s Salts (DSM-88 medium) containing:"}] |
| variants[1].modifications / reduced_anaerobic_mbsy_h2_co2 | ["Modified Brock's basal salts + 1 g/L yeast extract (MBSY)", "Reduced with Na2S (0.5 g/L) + resazurin (1 mg/L)", "Headspace H2/CO2 (80:20) at 100 kPa; optional 10 g/L elemental sulfur", "65-75C; pH 3.0"] | incomplete_or_nonqualifying_attached_evidence; VARIANT_TEXT_REQUIRES_SOURCE_REVIEW | unsupported; not_performed | unknown | [{"reference": "doi:10.1099/ijsem.0.001881", "supports": "SUPPORT", "explanation": "Sakai & Kurosawa 2017 Methods. Basal MBS recipe cited to another reference."}] |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://togomedium.org/medium/M2670
- https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium88a.pdf

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
