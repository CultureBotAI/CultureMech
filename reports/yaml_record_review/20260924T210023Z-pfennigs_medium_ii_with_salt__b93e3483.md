# YAML Record Review: pfennigs_medium_ii_with_salt

- Repository: CultureMech
- Record: data/merge_yaml/merged/pfennigs_medium_ii_with_salt__b93e3483.yaml
- Started UTC: 2026-09-24T21:00:23Z
- Finished UTC: 2026-09-24T21:00:23Z
- Verdict: needs curation

## Target

- MediaRecipe ID: CultureMech:009053
- Name: pfennigs_medium_ii_with_salt
- Source import: TOGO_M2477_Pfennig_s_Medium_II_With_Salt
- Primary external ID: TOGO:M2477
- Source URL: DSMZ_Medium40.pdf

This generated record represents TOGO M2477, which points at DSMZ Medium 40, PFENNIG'S MEDIUM II WITH SALT.

## Validation

- Open LinkML validation: passed with no reported issues.
- Strict validation: passed for 1 file with 0 error rows; `/private/tmp/pfennigs_medium_ii_with_salt__b93e3483.strict.tsv` is header-only.
- Reference validation: passed for 1 file with 0 reference checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

The record identity is pointed at the right source family: TOGO M2477 resolves to DSMZ Medium 40, and DSMZ Medium 40 is the Pfennig's Medium II with Salt variant. The medium itself is not truly a full independent recipe in the DSMZ source; it is Medium 29 with 1% sodium chloride added. This record therefore needs to merge with the other DSMZ Medium 40 records and retain a parent or nested Medium 29 structure instead of exposing every inherited stock ingredient as a final top-level ingredient.

Top-level sodium chloride is present at 1 PERCENT_W_V, which is the distinguishing salt addition from DSMZ 40. However, the inherited Medium 29 stock components are flattened into the final medium, and several rows are assigned gram-per-liter final-medium quantities even when they came from milliliter aliquots or milligram-per-liter trace stock concentrations.

Two grounding cleanups are also needed:

- `Pyruvic acid sodium salt` still has a legacy `mediaingredientmech_term`.
- `MgSO4 x 7 H2O` has the heptahydrate as its primary ChEBI term but retains a stale `mediaingredientmech_chebi_term` for generic magnesium sulfate.

## Evidence

- The DSMZ Medium 40 PDF says this medium is produced by adding 1% NaCl to DSMZ Medium 29.
- TOGO M2477 was fetched and confirmed to be another import of the same DSMZ Medium 40 source.
- Exact ignored-file searches found this generated file alongside the TOGO M2258 and direct/KOMODO DSMZ 40 siblings, so this record should not remain split after source normalization.
- The generated YAML itself contains Solution A-F and Trace element solution SL-10 B remnants as top-level ingredient rows and as solution stubs.

## Completeness

The curated representation is incomplete because the parent DSMZ Medium 29 context has been flattened away. The generated record includes a correct top-level 1% NaCl addition, but it also includes Medium 29 solution internals as if they were final concentrations in Medium 40.

Key omissions or distortions:

- The real Medium 40 instruction, Medium 29 plus 1% NaCl, is not preserved as the central relationship.
- Solution A, B, C, D, E, F, and SL-10 B stock aliquots are represented as final `G_PER_L` ingredient rows.
- Source water rows are summed into `Distilled water` 2270.0 G_PER_L, which is not a final-medium water amount.
- SL-10 B trace stock rows such as Na2MoO4, H3BO3, FeSO4, MnCl2, CoCl2, NiCl2, CuCl2, and ZnCl2 have milligram stock values stored as grams per liter.
- Na2S x 9 H2O stock and feed rows are collapsed together at the top level, losing their solution context and addition volumes.
- N2, CO2, and gas-sparging rows are represented as variable final ingredients instead of preparation conditions.
- The pH range from Medium 29, pH 6.8-7.1, is not present.

## Findings

1. The DSMZ parent relation is structurally wrong. DSMZ Medium 40 is Medium 29 plus 1% NaCl, but this generated record expands the Medium 29 component stocks directly into Medium 40.
2. Solution aliquots were parsed with the wrong dimensionality. `Sol. 1` at 50 G_PER_L, Solution A-F rows, and SL-10 B at 1 G_PER_L are solution volumes or stock references, not final grams per liter.
3. Several inherited stock concentrations are off by three orders of magnitude or lack final-medium context because milligram stock rows were imported as grams per liter.
4. Water is duplicated and summed across nested stocks, yielding `Distilled water` 2270.0 G_PER_L.
5. Gas handling was imported as chemical ingredients, even though the N2/CO2 entries describe the anaerobic preparation atmosphere for the parent medium.
6. Required source structure is split across sibling DSMZ 40 generated records instead of one curated normalized record.
7. Legacy and stale MediaIngredientMech links remain for pyruvate and magnesium sulfate heptahydrate rows.

## Recommended Edits

- Normalize DSMZ Medium 40 as a salt variant of DSMZ Medium 29 with a single top-level 1% NaCl addition.
- Preserve Medium 29 as a parent or nested recipe rather than flattening inherited Solution A-F and SL-10 B internals into the final medium.
- Convert solution additions with volume-aware handling; keep stock concentrations inside their source stock solution contexts.
- Do not sum water rows from nested stocks into the final liter of Medium 40.
- Model N2/CO2 sparging, Na2S feed handling, and pH 6.8-7.1 as source preparation metadata where the schema supports it.
- Replace the legacy `mediaingredientmech_term` on `Pyruvic acid sodium salt` with the curated ingredient grounding.
- Drop the stale generic magnesium sulfate MIM link from the `MgSO4 x 7 H2O` row.
- Merge the TOGO M2477, TOGO M2258, direct DSMZ 40, and KOMODO DSMZ 40 variants after the source-specific normalized records agree.

## Follow-up Checks

- Regenerate merged YAML and verify that DSMZ 40 has exactly one curated representation per intended source identity.
- Re-run open schema, strict, term, and reference validation after regeneration.
- Run exact ignored-file searches for `TOGO:M2477`, `TOGO:M2258`, and `DSMZ_Medium40` to confirm that stale duplicate generated records were not left behind.
- Spot-check the rendered DSMZ 40 page to ensure it shows the 1% NaCl addition without exposing inherited SL-10 B milligram stock rows as final grams per liter.

## Additional Notes

None found.
