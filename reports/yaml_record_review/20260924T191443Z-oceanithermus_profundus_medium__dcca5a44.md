# YAML Record Review: oceanithermus_profundus_medium__dcca5a44

- Repository: CultureMech
- Record: data/merge_yaml/merged/oceanithermus_profundus_medium__dcca5a44.yaml
- Started UTC: 2026-09-24T19:14:43Z
- Finished UTC: 2026-09-24T19:15:50Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/oceanithermus_profundus_medium__dcca5a44.yaml`, a generated bacterial `MediaRecipe` with id `CultureMech:008869` and source term `TOGO:M2283`.

The generated record has one source owner, `data/normalized_yaml/bacterial/TOGO_M2283_Oceanithermus_Profundus_Medium.yaml`, for DSMZ Medium 975.

## Validation

- LinkML open-schema validation: passed; no issues found.
- Strict validation: passed; `/private/tmp/oceanithermus_profundus_medium__dcca5a44.strict.tsv` contained only the header row.
- Reference validation: passed; the validator reported 0 configured checks for this record.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

TOGO M2283 is a TOGO import of DSMZ Medium 975. The exact ignored-inclusive search shows the direct DSMZ 975 record, `mediadive.medium:975`, is already present and merged with KOMODO Medium 975 in `data/merge_yaml/merged/OCEANITHERMUS_PROFUNDUS_MEDIUM.yaml`.

TOGO M2283 should be repaired and then linked into that same DSMZ 975 source-duplicate group, not emitted as an independent Oceanithermus Profundus Medium.

## Evidence

Checked the generated TOGO M2283 record, the normalized TOGO M2283 owner, an ignored-inclusive exact repository search for TOGO M2283 and DSMZ Medium 975 identifiers, the fetched TOGO M2283 REST payload, the DSMZ MediaDive REST payload for medium 975, and text extracted from the official DSMZ Medium 975 PDF.

DSMZ Medium 975 has three recipe scopes:

- Main medium: salts, HEPES, yeast extract, tryptone, sucrose, 1 ml vitamin solution, 1 ml trace elements, and 1000 ml distilled water.
- Wolin's vitamin solution: mg quantities of vitamins made up to 1000 ml.
- Modified Wolin's mineral solution: salts made up to 1000 ml, including Na2SeO3 x 5 H2O and Na2WO4 x 2 H2O as milligram additions.

The DSMZ and MediaDive sources also include a multi-step anaerobic preparation that omits several ingredients before autoclaving and adds sterile stock solutions after cooling.

## Completeness

The generated YAML does not preserve the three source scopes:

- Main-medium water, vitamin-stock water, and trace-stock water are collapsed into one generated `3000.0 G_PER_L` ingredient. The normalized owner has reduced this to `1000.0 G_PER_L`, but the unit is still wrong and stock waters still are not nested.
- Main-medium NaCl at 30 G_PER_L is summed with mineral-stock NaCl at 1 G_PER_L and emitted as 31 G_PER_L.
- Main-medium CaCl2 x 2 H2O at 0.33 G_PER_L is summed with mineral-stock CaCl2 x 2 H2O at 0.1 G_PER_L and emitted as `0.43000000000000005` G_PER_L.
- Vitamin and mineral-stock rows are flattened as final G_PER_L ingredients.
- `Vitamin solution` and `Trace elements` are represented as 1 G_PER_L solution placeholders instead of 1 ML_PER_L stock additions with nested composition.
- Na2SeO3 x 5 H2O and Na2WO4 x 2 H2O are imported as 0.3 and 0.4 G_PER_L, but the DSMZ mineral stock lists them as 0.3 and 0.4 mg per 1000 ml stock.
- No preparation steps capture anaerobic setup, pH 7.0-7.5, autoclaving, or sterile post-autoclave stock additions.

## Findings

- BLOCKER: The TOGO M2283 owner flattens Wolin's vitamin solution and Modified Wolin's mineral solution into final-medium rows, causing stock concentrations to be interpreted as final concentrations.
- BLOCKER: TOGO M2283 and direct DSMZ 975 are the same source recipe but are split into different generated canonical records.
- BLOCKER: NaCl and CaCl2 x 2 H2O are summed across the main medium and mineral stock; the generated values 31 and 0.43000000000000005 G_PER_L are not source rows.
- MAJOR: The two imported stock rows use 1 G_PER_L placeholders even though the DSMZ source adds 1 ml of each stock per final liter.
- MAJOR: Distilled water is represented as G_PER_L and is collapsed across the main medium and two stock solutions.
- MAJOR: Na2SeO3 x 5 H2O and Na2WO4 x 2 H2O are milligram-scale mineral-stock components but are emitted as G_PER_L ingredients.
- MAJOR: The MgSO4 x 7 H2O primary term is CHEBI:31795 while its `mediaingredientmech_chebi_term` mirror still points to generic magnesium sulfate.
- MINOR: KNO3 still has a legacy `mediaingredientmech_term`.

## Recommended Edits

- Split the TOGO M2283 normalized representation into a main final medium plus nested `Wolin's vitamin solution` and `Modified Wolin's mineral solution` stocks.
- Encode final distilled water as 1000 ML_PER_L in the main medium and keep stock waters inside their corresponding solutions.
- Keep 30 G_PER_L NaCl and 0.33 G_PER_L CaCl2 x 2 H2O in the final medium; keep 1 G_PER_L NaCl and 0.1 G_PER_L CaCl2 x 2 H2O only in the mineral stock.
- Convert `Vitamin solution` and `Trace elements` to 1 ML_PER_L stock additions and keep their components in stock concentration units, including 0.3 MG_PER_L Na2SeO3 x 5 H2O and 0.4 MG_PER_L Na2WO4 x 2 H2O for the mineral stock.
- Add the DSMZ anaerobic preparation and post-autoclave stock-addition instructions as `preparation_steps`.
- Link TOGO M2283 to the direct DSMZ 975 owner as `SOURCE_DUPLICATE`, then regenerate merged YAML so DSMZ 975/TOGO M2283/KOMODO 975 emit as one generated record.

## Follow-up Checks

- Run an ignored-inclusive exact search for `TOGO:M2283`, `mediadive.medium:975`, `DSMZ_Medium975`, and `TOGO_M2283_Oceanithermus_Profundus_Medium` after repair to confirm the DSMZ source group has one generated owner.
- Rebuild merged YAML and verify the DSMZ 975 group remains distinct from the NBRC 404 and other TOGO Oceanithermus profundus media.
- Re-run open-schema, strict, reference, and term validation after the normalized owner is repaired and generated YAML is rebuilt.

## Additional Notes

None found.
