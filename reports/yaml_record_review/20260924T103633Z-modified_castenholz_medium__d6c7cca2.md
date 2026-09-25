# YAML Record Review: modified_castenholz_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_castenholz_medium__d6c7cca2.yaml
- Started UTC: 2026-09-24T10:35:45Z
- Finished UTC: 2026-09-24T10:36:33Z
- Verdict: needs curation

## Target

Generated record `CultureMech:000937` for DSMZ/MediaDive medium `1470`, `MODIFIED CASTENHOLZ MEDIUM`.

The generated record merges `modified_castenholz_medium` from `data/normalized_yaml/bacterial/modified_castenholz_medium.yaml`. This is the DSMZ 1470 owner and is distinct from the KOMODO 86a owner that shares the same normalized recipe name. The generated YAML was compared with the maintained owner, MediaDive medium `1470`, and the DSMZ Medium 1470 PDF.

## Validation

- Open LinkML validation: passed with no issues found.
- Strict validation: passed; `/private/tmp/modified_castenholz_medium__d6c7cca2.strict.tsv` contained only the header row.
- Reference validation: passed with 0 reference checks.
- Term validation: passed.
- Embedded `curation_history`: Not checked: the available history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The medium identity, pH 8.2, DSMZ 1470 link, main carbon and nitrogen rows, and most small-ion CHEBI groundings match the DSMZ and MediaDive source.

`KNO3` and `NaNO3` still carry legacy `mediaingredientmech_term` links even though both rows have primary CHEBI terms. The `Tryptone (Oxoid)`, `Peptone (BD)`, and `FeCl3 x 6 H2O (1% w/v)` qualifiers are also not retained.

## Evidence

DSMZ 1470 and MediaDive `1470` list a main recipe with 5 g tryptone, 5 g peptone, 2 g sucrose, 2.8 ml `FeCl3 x 6 H2O` at 1% w/v, 1 ml `Nitsch Element Solution`, and 1000 ml distilled water, followed by pH adjustment to 8.2 with NaOH.

The same sources define `Nitsch Element Solution` as a separate 1000 ml stock with 5 ml `H2SO4`, milligram or microgram trace sulfate/chloride/molybdate rows, and 1000 ml distilled water. The generated record omits the 1 ml Nitsch addition and instead promotes `H2SO4`, `MnSO4 x H2O`, `ZnSO4 x 7 H2O`, `H3BO3`, `CuSO4 x 5 H2O`, `Na2MoO4 x 2 H2O`, and `CoCl2 x 6 H2O` to ordinary final-medium ingredients.

The `H2SO4` row is additionally unit-corrupted: the source row is 5 ml in a 1000 ml stock that is dosed at 1 ml per liter, while the generated record represents it as 5 g/L in the final medium.

## Completeness

The record preserves the DSMZ 1470 identity, pH, main salt rows, organic rows, sucrose, and NaOH pH-adjustment step.

It is incomplete for nested-stock structure and explicit water. The main 1000 ml distilled-water row and the Nitsch 1000 ml distilled-water row are absent, the 1 ml Nitsch addition is absent, and all Nitsch rows have lost their stock context.

## Findings

- High: `Nitsch Element Solution` is flattened into final-medium ingredients instead of being represented as a 1 ml stock addition.
- High: The stock `H2SO4` row is converted from 5 ml in Nitsch stock to 5 g/L in the final medium.
- Medium: Both source distilled-water rows are missing.
- Low: `KNO3` and `NaNO3` retain deprecated `mediaingredientmech_term` cross-links instead of id-safe `mediaingredientmech_chebi_term` links.

## Recommended Edits

- Recurate `data/normalized_yaml/bacterial/modified_castenholz_medium.yaml` or the MediaDive import path so `Nitsch Element Solution` remains a separate stock recipe and the main DSMZ 1470 formula keeps a structured 1 ml Nitsch addition.
- Preserve 1000 ml distilled water in both the main solution and the Nitsch stock.
- Correct `H2SO4` to the source 5 ml stock row, not 5 g/L final concentration.
- Preserve the source attributes for Oxoid tryptone, BD peptone, and the 1% w/v ferric chloride hexahydrate addition.
- Refresh `KNO3` and `NaNO3` so their MediaIngredientMech mappings use CHEBI-keyed links consistently.
- Regenerate `data/merge_yaml/merged/modified_castenholz_medium__d6c7cca2.yaml` from the repaired owner or importer.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated YAML.
- Compare the regenerated record against DSMZ 1470 and MediaDive `1470` to confirm the main 1 ml Nitsch addition and the Nitsch stock rows stay separate.
- Check that no final-medium top-level row remains for `H2SO4` from the Nitsch stock.

## Additional Notes

None found.
