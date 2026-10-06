# Ingredient Concentration Review

- Record: data/merge_yaml/merged/ignicoccus_medium_for_dsm_18386.yaml
- ID: CultureMech:009166
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: f25ea416346ec98a6f290f2ed020362239f87ebfc8895bdd653bb38ea6817abb
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/21
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/archaea/ignicoccus_medium_for_dsm_18386.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Sodium resazurin (0.1% w/v) | {"value": "0.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Distilled water | {"value": "1000", "unit": "G_PER_L"} | missing_attached_evidence; PLAUSIBILITY_WATER_AS_VOLUME | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / MgSO4 x 7 H2O | {"value": "3.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / NaCl | {"value": "13.65", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / CaCl2 x 2 H2O | {"value": "0.38", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / KH2PO4 | {"value": "0.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[6].concentration / MgCl2 x 6 H2O | {"value": "2.75", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[7].concentration / Na2S x 9 H2O | {"value": "0.2", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[8].concentration / H3BO3 | {"value": "15", "unit": "G_PER_L"} | missing_attached_evidence; PLAUSIBILITY_TRACE_SALT_AS_STOCK | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[9].concentration / KCl | {"value": "0.33", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[10].concentration / (NH4)2SO4 | {"value": "0.25", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[11].concentration / Sulfur (powdered) | {"value": "5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[12].concentration / NaBr | {"value": "0.05", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[13].concentration / 2 N H2SO4 | {"value": "variable", "unit": "VARIABLE"} | missing_attached_evidence; VARIABLE_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[14].concentration / Carbon dioxide gas | {"value": "variable", "unit": "VARIABLE"} | missing_attached_evidence; VARIABLE_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[15].concentration / N2 | {"value": "variable", "unit": "VARIABLE"} | missing_attached_evidence; VARIABLE_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[16].concentration / Hydrogen gas | {"value": "variable", "unit": "VARIABLE"} | missing_attached_evidence; VARIABLE_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[0].concentration / SrCl2 x 6 H2O solution (0.1% w/v) | {"value": "7", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[1].concentration / KI solution (0.01% w/v) | {"value": "0.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| variants[0].modifications / half_sme_s0_ignicoccus | ["Half-strength SME synthetic-seawater base", "Add elemental sulfur (S0) as electron acceptor", "Reduce with Na2S", "Additional/trace components vs parent: explicit NaHCO3, SrCl2.6H2O, KI", "H2/CO2 (80:20) headspace, ~1.5 bar; pH 5.5-6.0; 90C"] | candidate_needs_source_verification; VARIANT_TEXT_REQUIRES_SOURCE_REVIEW | unsupported; retrieval_failed; exact quote and concentration not verified | unknown | [{"reference": "doi:10.5283/epub.34741", "supports": "SUPPORT", "explanation": "Koschnitzki 2017 prints the formulation and strain list.", "snippet": "½ SME+S0 medium for all Ignicoccus representatives (Paper et al., 2007) Substance Amount Concentration SME 500 ml ½ x KH2PO4 0.5 g 3.7 mM (NH4)2SO4 0.25 g 1.9 mM NaHCO3 0.16 g 1.9 mM Resazurin (0.1 %) 1 ml 0.0001 % Na2S x 7-9 H2O 0.5 g 2.1 mM ddH2O ad 1000 ml"}] |
| variants[1].modifications / half_sme_ignicoccus_plus_0_1pct_yeast_extract | ["Add yeast extract to 0.1% (w/v)"] | candidate_needs_source_verification; VARIANT_TEXT_REQUIRES_SOURCE_REVIEW | unsupported; retrieval_failed; exact quote and concentration not verified | unknown | [{"reference": "doi:10.1128/JB.06130-11", "supports": "SUPPORT", "explanation": "Mayer et al. 2012 describes the yeast-extract supplementation explicitly.", "snippet": "Comparison of autotrophic growth with mixotrophic growth where 0.1% yeast extract was added to the normal culture medium of I. hospitalis DSM 18386."}] |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://togomedium.org/medium/M2599
- https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium897.pdf

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
