# Ingredient Concentration Review

- Record: data/normalized_yaml/bacterial/TOGO_M1308_Methylotroph_Medium.yaml
- ID: CultureMech:007843
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 1b4b4e0a968f02e33cb6eb0cdab058ee3c2820033861e9caf24cd99191523ab0
- Layer: normalized
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 7/40
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/TOGO_M1308_Methylotroph_Medium.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Distilled water | {"value": "970", "unit": "G_PER_L"} | incomplete_or_nonqualifying_attached_evidence;  | correct; inspected_conflicting_unit | {"value": "0.97", "unit": "L"} | [{"reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1219", "snippet": "970.0", "locator": "Main table, Distilled water row, amount cell; adjacent unit cell is ml", "calculation": "970 ml / 1000 = 0.97 L of preparation water. This is not 970 g/L of solute.", "explanation": "The original source linked by this TOGO record specifies preparation volume, not mass concentration. Replace only after apply authorization; preserve downstream addition volumes separately."}] |
| ingredients[1].concentration / CaCl2・2H2O | {"value": "0.07", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / KH2PO4 | {"value": "0.27", "unit": "G_PER_L"} | incomplete_or_nonqualifying_attached_evidence;  | unsupported; inspected_basis_unresolved | unknown | [{"reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1219", "snippet": "0.27", "locator": "Main table, KH2PO4 row, amount cell; adjacent unit is g", "calculation": "Batch mass is explicit; final volume after the post-autoclave additions is not specified as exactly 1 L.", "explanation": "Do not automatically equate the reported grams per preparation with a precise final G_PER_L value. Source supports batch quantity; denominator convention remains unresolved."}] |
| ingredients[3].concentration / MgCl2・6H2O | {"value": "0.2", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / NaNO3 | {"value": "0.42", "unit": "G_PER_L"} | incomplete_or_nonqualifying_attached_evidence;  | unsupported; inspected_basis_unresolved | unknown | [{"reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1219", "snippet": "0.42", "locator": "Main table, NaNO3 row, amount cell; adjacent unit is g", "calculation": "Batch mass is explicit; final volume after the post-autoclave additions is not specified as exactly 1 L.", "explanation": "Reported batch amount is supported but a precise final G_PER_L denominator remains unresolved."}] |
| ingredients[5].concentration / Na2SO4 | {"value": "0.014", "unit": "G_PER_L"} | incomplete_or_nonqualifying_attached_evidence;  | unsupported; inspected_basis_unresolved | unknown | [{"reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1219", "snippet": "0.014", "locator": "Main table, Na2SO4 row, amount cell; adjacent unit is g", "calculation": "Batch mass is explicit; final volume after the post-autoclave additions is not specified as exactly 1 L.", "explanation": "Reported batch amount is supported but a precise final G_PER_L denominator remains unresolved."}] |
| ingredients[6].concentration / HEPES | {"value": "4.77", "unit": "G_PER_L"} | incomplete_or_nonqualifying_attached_evidence;  | unsupported; inspected_basis_unresolved | unknown | [{"reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1219", "snippet": "4.77", "locator": "Main table, HEPES row, amount cell; adjacent unit is g", "calculation": "Batch mass is explicit; final volume after the post-autoclave additions is not specified as exactly 1 L.", "explanation": "Reported batch amount is supported but a precise final G_PER_L denominator remains unresolved."}] |
| ingredients[7].concentration / KOH | {"value": "variable", "unit": "VARIABLE"} | incomplete_or_nonqualifying_attached_evidence; VARIABLE_REQUIRES_SOURCE | not_quantified; inspected_explicit_titration | unknown | [{"reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1219", "snippet": "Mix components and adjust pH to 7.0 with 6 N KOH.", "locator": "Instruction following the main composition table", "calculation": "The 6 N figure describes titrant strength, not a fixed final-medium KOH concentration.", "explanation": "Variable dose is legitimate for pH adjustment. Add supporting provenance, not an invented concentration."}] |
| ingredients[8].concentration / Methanol | {"value": "0.81", "unit": "G_PER_L"} | incomplete_or_nonqualifying_attached_evidence;  | correct; inspected_conflicting_unit | unknown | [{"reference": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1219", "snippet": "0.81", "locator": "Post-autoclave addition table, Methanol row, amount cell; adjacent unit cell is ml", "calculation": "The source gives 0.81 ml per prepared batch. Mass concentration requires verified density and final volume, neither supplied here. Do not blindly replace G_PER_L by ML_PER_L with the same number.", "explanation": "The record stores a volume as a mass concentration. Preserve the source batch dose in a suitable structure; a corrected final concentration remains unresolved."}] |
| solutions[0].concentration / Trace element solution (see Medium [M278]) | {"value": "10", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[0].composition[0].concentration / Nitrilotriacetic acid | {"value": "12.8", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[0].composition[1].concentration / FeCl3 x 6 H2O | {"value": "1.35", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[0].composition[2].concentration / MnCl2 x 4 H2O | {"value": "0.1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[0].composition[3].concentration / CoCl2 x 6 H2O | {"value": "0.024", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[0].composition[4].concentration / CaCl2 x 2 H2O | {"value": "0.1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[0].composition[5].concentration / ZnCl2 | {"value": "0.1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[0].composition[6].concentration / CuCl2 x 2 H2O | {"value": "0.025", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[0].composition[7].concentration / H3BO3 | {"value": "0.01", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[0].composition[8].concentration / Na2MoO4 x 2 H2O | {"value": "0.024", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[0].composition[9].concentration / NiCl2 x 6 H2O | {"value": "0.12", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[1].concentration / Se/W solution (see Medium [M278]) | {"value": "10", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[1].composition[0].concentration / Na2SeO3 x 5 H2O | {"value": "4", "unit": "MG_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[1].composition[1].concentration / Na2WO4 x 2 H2O | {"value": "4", "unit": "MG_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[2].concentration / Trace vitamins (see Medium [M190]) | {"value": "10", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[2].composition[0].concentration / Biotin | {"value": "2", "unit": "MG_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[2].composition[1].concentration / Folic acid | {"value": "2", "unit": "MG_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[2].composition[2].concentration / Pyridoxine hydrochloride | {"value": "10", "unit": "MG_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[2].composition[3].concentration / Thiamine HCl | {"value": "5", "unit": "MG_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[2].composition[4].concentration / Riboflavin | {"value": "5", "unit": "MG_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[2].composition[5].concentration / Nicotinic acid | {"value": "5", "unit": "MG_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[2].composition[6].concentration / Calcium pantothenate | {"value": "5", "unit": "MG_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[2].composition[7].concentration / Vitamin B12 | {"value": "0.1", "unit": "MG_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[2].composition[8].concentration / p-Aminobenzoic acid | {"value": "5", "unit": "MG_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[2].composition[9].concentration / Lipoic acid | {"value": "5", "unit": "MG_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[3].concentration / 10 mM CuCl2 solution | {"value": "2", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[3].composition[0].concentration / CuCl2 | {"value": "10", "unit": "MILLIMOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[4].concentration / 10 mM CeCl3 solution | {"value": "2", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[4].composition[0].concentration / CeCl3 | {"value": "10", "unit": "MILLIMOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| variants[0].modifications / solid_methylotroph_medium | ["Add agar at 15.0 g/L before autoclaving."] | incomplete_or_nonqualifying_attached_evidence; VARIANT_TEXT_REQUIRES_SOURCE_REVIEW | unsupported; not_performed | unknown | [{"reference": "DSMZ:J1219", "supports": "SUPPORT", "explanation": "MediaDive/JCM medium J1219 states that agar is added for solid medium preparation."}] |
| variants[1].modifications / ca_free_lanthanide_test_basal_medium | ["Omit CaCl2 from the trace element solution.", "Supplement cultures with methane or methanol and defined CaCl2 or rare-earth element chlorides after autoclaving.", "Use methanol cultures to quantify lanthanide-dependent growth of strain Ce-a6."] | incomplete_or_nonqualifying_attached_evidence; VARIANT_TEXT_REQUIRES_SOURCE_REVIEW | unsupported; not_performed | unknown | [{"reference": "doi:10.1264/jsme2.ME19128", "supports": "SUPPORT", "explanation": "Kato et al. describe a Ca-free inorganic basal medium closely related to J1219 and the carbon-source/lanthanide supplements used for growth tests."}] |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- PMID:11315676
- doi:10.1264/jsme2.ME19128
- https://togomedium.org/medium/M1308
- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1219

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
