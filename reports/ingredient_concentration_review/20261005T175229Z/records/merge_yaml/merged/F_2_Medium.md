# Ingredient Concentration Review

- Record: data/merge_yaml/merged/F_2_Medium.yaml
- ID: CultureMech:000170
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 57a22b9709df05527b3ed71f0ef619c4cd3377e82c0999a45f8dc515aadbe678
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/10
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/algae/F_2_Medium.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / 1 | {"value": "variable", "unit": "G_PER_L"} | missing_attached_evidence; RANGE_OR_NONNUMERIC_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / 2 | {"value": "variable", "unit": "G_PER_L"} | missing_attached_evidence; RANGE_OR_NONNUMERIC_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / 3 | {"value": "variable", "unit": "G_PER_L"} | missing_attached_evidence; RANGE_OR_NONNUMERIC_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / 4 | {"value": "variable", "unit": "G_PER_L"} | missing_attached_evidence; RANGE_OR_NONNUMERIC_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / 5 | {"value": "variable", "unit": "G_PER_L"} | missing_attached_evidence; RANGE_OR_NONNUMERIC_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / 6 | {"value": "variable", "unit": "G_PER_L"} | missing_attached_evidence; RANGE_OR_NONNUMERIC_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[6].concentration / 7 | {"value": "variable", "unit": "G_PER_L"} | missing_attached_evidence; RANGE_OR_NONNUMERIC_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| variants[0].modifications / n_replete_second_stage_tetraselmis_marina | ["Grow cells in F/2 medium for seven days as the first stage.", "Shift to a nitrogen-replete second stage with 4.41 mM NaNO3 for three days."] | incomplete_or_nonqualifying_attached_evidence; VARIANT_TEXT_REQUIRES_SOURCE_REVIEW | unsupported; not_performed | unknown | [{"reference": "PMID:28456040", "supports": "SUPPORT", "snippet": "After second stage of cultivation of T. marina for further 3-days under N-replete condition (4.41mM NaNO3) increased biomass concentration of 1900mg/L and lipid content of 50% were observed", "explanation": "Literature evidence describes a nitrogen-replete second-stage variant after initial F/2 cultivation."}] |
| variants[1].modifications / f_2asw_diatom_culture | ["Use artificial seawater supplemented with half-strength Guillard f solution.", "Maintain cultures at 20 deg C under continuous illumination at 30-75 umol photons m-2 s-1.", "Aerate cultures with ambient air or 1% CO2 depending on the experiment."] | incomplete_or_nonqualifying_attached_evidence; VARIANT_TEXT_REQUIRES_SOURCE_REVIEW | unsupported; not_performed | unknown | [{"reference": "DOI:10.1104/pp.18.00453", "supports": "SUPPORT", "explanation": "Matsui et al. define F/2ASW as artificial seawater plus half-strength Guillard f solution and report use with Phaeodactylum tricornutum UTEX 642 and Thalassiosira pseudonana CCMP1335."}] |
| variants[2].modifications / modified_f_2asw_sodium_response | ["Supplement F/2ASW with 10 nM sodium selenite and 0.1 mM sodium metasilicate.", "Adjust sodium concentration by altering NaCl addition to the basal medium.", "Vary CO2 availability to distinguish sodium-dependent growth effects."] | incomplete_or_nonqualifying_attached_evidence; VARIANT_TEXT_REQUIRES_SOURCE_REVIEW | unsupported; not_performed | unknown | [{"reference": "DOI:10.1007/s10126-021-10037-4", "supports": "SUPPORT", "explanation": "Tsuji et al. report Chaetoceros gracilis UTEX LB2658 growth experiments using a modified F/2ASW formulation."}] |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- DOI:10.1007/s10126-021-10037-4
- DOI:10.1104/pp.18.00453
- https://utex.org/products/f-2-medium

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
