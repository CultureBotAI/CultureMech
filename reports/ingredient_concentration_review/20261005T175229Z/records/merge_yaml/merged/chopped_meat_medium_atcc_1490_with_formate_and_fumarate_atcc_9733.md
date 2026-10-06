# Ingredient Concentration Review

- Record: data/merge_yaml/merged/chopped_meat_medium_atcc_1490_with_formate_and_fumarate_atcc_9733.yaml
- ID: CultureMech:009185
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: c222e5aa8e26853a4391a18b57c76ce51e9ec98cf9c8bb8e40a76b851bfee899
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/25
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/chopped_meat_medium_atcc_1490_with_formate_and_fumarate_atcc_9733.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / ATCC Medium 1490 | {"value": "952.4", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Carbon dioxide gas | {"value": "variable", "unit": "VARIABLE"} | missing_attached_evidence; VARIABLE_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Nitrogen gas | {"value": "variable", "unit": "VARIABLE"} | missing_attached_evidence; VARIABLE_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Hydrogen gas | {"value": "variable", "unit": "VARIABLE"} | missing_attached_evidence; VARIABLE_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / Distilled water | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / N NaOH | {"value": "26.0", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[6].concentration / Ground beef (fat-free) | {"value": "500", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[7].concentration / 0.025% Resazurin | {"value": "4", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[8].concentration / Yeast extract | {"value": "5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[9].concentration / K2HPO4 | {"value": "5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[10].concentration / Agar | {"value": "20", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[11].concentration / Trypticase Peptone (BD 211921) | {"value": "30", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[12].concentration / L-Cysteine . HCl | {"value": "0.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[13].concentration / 95% Ethanol | {"value": "30", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[14].concentration / Vitamin K1 | {"value": "0.15", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[15].concentration / Distilled water to | {"value": "100", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[16].concentration / Hemin | {"value": "50", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[17].concentration / DI Water | {"value": "100", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[18].concentration / Fumaric Acid | {"value": "6", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[19].concentration / Sodium Formate | {"value": "6", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[0].concentration / Formate and Fumarate Solution | {"value": "47.6", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[1].concentration / Hemin Solution | {"value": "10", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[2].concentration / Vitamin K1 Solution | {"value": "0.2", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| variants[0].modifications / atcc_1490_base_no_formate_fumarate | ["Formate and fumarate omitted relative to the parent (ATCC 1490 + formate + fumarate).", "Base ATCC 1490 Modified Chopped Meat medium; anaerobic, 37C, 24-48 h."] | candidate_needs_source_verification; VARIANT_TEXT_REQUIRES_SOURCE_REVIEW | unsupported; retrieval_failed; exact quote and concentration not verified | unknown | [{"reference": "doi:10.1186/1471-2334-11-200", "supports": "SUPPORT", "explanation": "O'Hanlon et al. 2011 distinguishes the plain ATCC 1490 base from the formate+fumarate parent formulation.", "snippet": "Fusobacterium nucleatum ATCC 25586 and Porphyromonas levii ATCC 29147 were all grown in ATCC medium 1490 (Modified chopped meat medium)."}] |
| variants[1].modifications / atcc_1490_carbonate_co2_buffered | ["Carbonate/CO2 buffering added to ATCC 1490 base (exact carbonate species/concentration and gas composition not printed).", "For MIC assays, medium clarified through a 0.8 um filter (assay-use processing).", "Anaerobic glove bag; serum bottle technique; 38C."] | candidate_needs_source_verification; VARIANT_TEXT_REQUIRES_SOURCE_REVIEW | unsupported; retrieval_failed; exact quote and concentration not verified | unknown | [{"reference": "doi:10.1002/ptr.765", "supports": "SUPPORT", "explanation": "Johnston et al. 2001; ATCC 1490-derived variant with carbonate/CO2 buffering; no formate/fumarate, so distinct from the parent.", "snippet": "Fusobacterium necrophorum (ATCC 27852) was grown in a modified chopped meat medium (ATCC 1490) buffered with carbonate/CO2. For MIC assays, this medium was clarified through a 0.8 um filter."}] |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://togomedium.org/medium/M2618
- https://www.atcc.org/~/media/78329ED2D2314D3BB1BC2F3BEAA2ECFB.ashx

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
