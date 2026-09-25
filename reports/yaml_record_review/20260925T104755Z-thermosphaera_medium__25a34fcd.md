# YAML Record Review: thermosphaera_medium__25a34fcd

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermosphaera_medium__25a34fcd.yaml
- Started UTC: 2026-09-25T10:47:51Z
- Finished UTC: 2026-09-25T10:47:55Z
- Verdict: needs curation

## Target

- Generated YAML for TOGO Medium M2672, Thermosphaera Medium.
- The record was merged from `TOGO_M2672_Thermosphaera_Medium`.
- The main checked sources were TOGO M2672, DSMZ Medium 817, and MediaDive REST entry 817.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The TOGO identity points to M2672 and the original DSMZ Medium 817 PDF.
- TOGO M2672 includes pH 6.5 in `meta.ph`, but the generated record has no `ph_value`.
- The generated TOGO record is a lossy source-specific duplicate of DSMZ 817; direct DSMZ/MediaDive 817 and KOMODO copies have already been merged into `THERMOSPHAERA_MEDIUM`.

## Evidence

- DSMZ/MediaDive 817 lists 1000 ml distilled water, 17 mg KCl, 12 mg NH4Cl, 1 g yeast extract, 1 g peptone, 0.5 g Na2CO3, 0.5 g Na2S x 9 H2O, 1 ml Wolin's vitamin solution 10x, pH 6.5, and an N2/CO2 pressure step.
- TOGO M2672 lists its source URL as DSMZ Medium 817 but has a stale or divergent main recipe with NaHCO3, 10 ml Vitamin solution, explicit gas pseudo-ingredients, and a duplicated vitamin subcomponent.
- The generated record moved several stock-solution rows to `solutions` placeholders while also leaving stock vitamins as top-level gram-per-liter ingredients.

## Completeness

- The generated record lacks the pH 6.5 value present in both TOGO M2672 and DSMZ/MediaDive 817.
- The main water is summed with stock-solution water into 2000 g/L, while the direct DSMZ recipe has 1000 ml main water plus 1000 ml water only inside the vitamin stock.
- The generated record does not preserve the DSMZ carbonate/vitamin/sulfide additions as a coherent stock-solution relationship.

## Findings

- The formula has blocking stock-solution flattening errors: KCl and NH4Cl are imported as `17` and `12` g/L instead of 17 and 12 mg/L-scale additions, and the vitamin stock rows are imported as gram-per-liter top-level ingredients.
- The TOGO import keeps empty placeholder solutions for CaCl2 x 2 H2O, sodium resazurin, K2HPO4 x 3 H2O, FeCl3, and Vitamin solution instead of modeling the source addition volumes cleanly.
- The recipe is source-duplicated by `THERMOSPHAERA_MEDIUM`, which was generated from direct DSMZ/MediaDive 817 and KOMODO DSMZ 817 inputs and retains pH 6.5 and the DSMZ preparation steps.

## Recommended Edits

- Retire the stale TOGO M2672 generated record or fold it into the direct DSMZ 817 canonical record.
- If TOGO M2672 is regenerated, preserve pH 6.5, avoid summing stock water into the main medium, and represent the vitamin and salt stock additions by source volume instead of top-level stock concentrations.
- Prefer the direct DSMZ/MediaDive 817 formula for the canonical Thermosphaera medium because it matches the fetched DSMZ PDF and current MediaDive 817 REST response.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after duplicate cleanup.
- Confirm that no generated Thermosphaera record retains the TOGO vitamin-stock flattening or the 2000 g/L water artifact.

## Additional Notes

- None found.
