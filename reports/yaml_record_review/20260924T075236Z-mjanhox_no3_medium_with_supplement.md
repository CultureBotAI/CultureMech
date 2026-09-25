# YAML Record Review: mjanhox_no3_medium_with_supplement

- Repository: CultureMech
- Record: data/merge_yaml/merged/mjanhox_no3_medium_with_supplement.yaml
- Started UTC: 2026-09-24T07:52:36Z
- Finished UTC: 2026-09-24T07:53:10Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:003497`
- Generated name: `mjanhox_no3_medium_with_supplement`
- Generated source file: `data/merge_yaml/merged/mjanhox_no3_medium_with_supplement.yaml`
- Normalized owner: `data/normalized_yaml/bacterial/mjanhox_no3_medium_with_supplement.yaml`
- Duplicate normalized source: `data/normalized_yaml/bacterial/KOMODO_1000_MJANHOX-NO3_MEDIUM_WITH_SUPPLEMENT.yaml`
- Upstream source: DSMZ/MediaDive medium `1000`, with KOMODO medium `1000` duplicate

## Validation

- Open LinkML validation passed: `No issues found`.
- Strict validation passed with 0 ERROR rows in `/private/tmp/mjanhox_no3_medium_with_supplement.strict.tsv`.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` was not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The generated record merges matching DSMZ/MediaDive `1000` and KOMODO `1000` sources.
- The generated `media_term` points to `komodo.medium:1000`; DSMZ medium `1000` is retained in `notes` and `parent_media`.
- `NiCl2 x 6 H2O` is grounded to generic nickel dichloride.
- Fe2(SO4)3 hydrate is grounded to generic iron(3+) sulfate.
- NaNO3 still carries legacy `mediaingredientmech_term: MediaIngredientMech:000171`.

## Evidence

- MediaDive `1000` main solution `2038` contains 1000 ml water, 3 g NaCl, 0.014 g K2HPO4, 0.014 g `CaCl2 x 2 H2O`, 0.04 g NH4Cl, 0.34 g `MgSO4 x 7 H2O`, 0.418 g `MgCl2 x 6 H2O`, 0.033 g KCl, 5 mg ferric sulfate hydrate, 5 ug `NiCl2 x 6 H2O`, 5 ug `Na2SeO3 x 5 H2O`, 0.5 g `Na2SiO3 x 9 H2O`, 1 ml Trace mineral solution `2039`, 10 mM thiosulfate, 0.2% bicarbonate, and 0.05% nitrate.
- The generated record matches MediaDive's final values for the direct final additions, including 2.48186 g/L `Na2S2O3 x 5 H2O`, 2 g/L NaHCO3, and 0.5 g/L NaNO3.
- MediaDive Trace mineral solution `2039` is a 1000 ml stock containing nitrilotriacetic acid, `MnSO4 x 2 H2O`, CoSO4, ZnSO4, CuSO4, `AlK(SO4)2 x 12 H2O`, H3BO3, `Na2MoO4 x 2 H2O`, and water.
- The main solution uses only 1 ml of Trace mineral solution `2039`.

## Completeness

- The generated record has no `solutions` array.
- The 1 ml Trace mineral solution `2039` addition was flattened into direct top-level rows at raw stock concentration.
- Water rows for the main solution and the trace-mineral stock are not represented structurally.
- The gas purging and 3 atm pressurization instructions from MediaDive are absent from structured preparation steps.

## Findings

- High: The 1 ml Trace mineral solution stock was flattened at undiluted stock concentration.
- Medium: The H2-CO2 purging and 3 atm pressure preparation step was dropped.
- Medium: Sodium nitrate still uses the deprecated `mediaingredientmech_term` slot.
- Medium: Hydration-specific ontology grounding is incomplete for nickel chloride and ferric sulfate.

## Recommended Edits

- Rebuild `data/normalized_yaml/bacterial/mjanhox_no3_medium_with_supplement.yaml` with an explicit 1 ml Trace mineral solution `2039` addition.
- Dilute the Trace mineral stock through the 1 ml addition or preserve it as a nested stock with its usage volume recorded.
- Keep thiosulfate, bicarbonate, and nitrate as final-concentration additions.
- Add preparation semantics for H2-CO2 purging and the 3 atm gas phase.
- Replace the legacy nitrate `mediaingredientmech_term` with the ingredient's CHEBI key.
- Regenerate the merged record after repairing the DSMZ/KOMODO normalized sources.

## Follow-up Checks

- Re-fetch MediaDive `1000` and verify no raw `2039` stock concentration is present as a direct final-medium concentration.
- Confirm the DSMZ and KOMODO duplicate sources still merge after the trace-mineral stock is represented consistently.
- Confirm gas-phase preparation text is no longer dropped.
- Re-run open LinkML, strict, reference, and term validation after regenerating the merged record.

## Additional Notes

- None found.
