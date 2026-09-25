# YAML Record Review: SULFUROSPIRILLUM BARNESII MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/sulfurospirillum_barnesii_medium__fb8c612b.yaml
- Started UTC: 2026-09-25T08:42:50Z
- Finished UTC: 2026-09-25T08:44:22Z
- Verdict: needs curation

## Target

- Reviewed generated record `CultureMech:001905` in `data/merge_yaml/merged/sulfurospirillum_barnesii_medium__fb8c612b.yaml`.
- Canonical source: `data/normalized_yaml/bacterial/sulfurospirillum_barnesii_medium.yaml`.
- Parent source: `data/normalized_yaml/bacterial/sulfurospirillum_ii_medium.yaml`.
- Media term: `mediadive.medium:771`, `DSMZ Medium 771`, `SULFUROSPIRILLUM BARNESII MEDIUM`.
- Parent media term: `komodo.medium:771`, `KOMODO Medium 771`, `SULFUROSPIRILLUM II medium`.
- Merge fingerprint: `fb8c612baeebd3543e0e2fc01e66aa5298069b23fda3e56f0c22ab9865eec175`.

## Validation

- LinkML schema validation passed: `No issues found`.
- Strict validation passed with 0 error rows.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` was not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

- The canonical identity matches MediaDive/DSMZ medium `771`, `SULFUROSPIRILLUM BARNESII MEDIUM`, with pH 7.2-7.4.
- Exact ignored-file-inclusive searches found `CultureMech:001905`, `CultureMech:006428`, `mediadive.medium:771`, `komodo.medium:771`, `source_id: komodo.medium:771`, and the `fb8c612baeebd3543e0e2fc01e66aa5298069b23fda3e56f0c22ab9865eec175` fingerprint in the generated and normalized target files at expected locations.
- The KOMODO parent explicitly records `DSMZ Medium: 771 (mediadive.medium:771)` and has the same flattened DSMZ-derived composition, so the source-duplicate edge is plausible.
- DSMZ `DSMZ_Medium771.pdf` agrees with MediaDive 771 on the base recipe and the three 1 ml stock additions.

## Evidence

- DSMZ/MediaDive 771 add 1 ml Trace element solution SL-10, 1 ml Selenite-tungstate solution, and 1 ml Wolin's vitamin solution (10x) to the main 1003 ml recipe.
- Trace element solution SL-10 is a 1 L stock containing 10 ml 25% HCl, 1.5 g FeCl2 x 4 H2O, and several milligram-scale salts.
- Selenite-tungstate solution is a 1 L stock containing 0.5 g NaOH, 3 mg Na2SeO3 x 5 H2O, and 4 mg Na2WO4 x 2 H2O.
- Wolin's vitamin solution (10x) is a 1 L stock and is added to the final medium at 1 ml.
- DSMZ instructs carbonate, lactate, nitrate, vitamins, cysteine, and sulfide to be omitted before autoclaving and added later from sterile anoxic stocks.

## Completeness

- The generated record preserves the DSMZ identity, pH range, complex/liquid classification, base salts, yeast extract, late-added carbon/nitrogen/reducing compounds, stock-solution components, and source preparation text.
- The generated record does not preserve Trace element solution SL-10, Selenite-tungstate solution, or Wolin's vitamin solution (10x) as 1 ml additions.
- The KOMODO parent has no preparation steps, but that is not a generated-record loss because the MediaDive canonical source carries the DSMZ preparation text.

## Findings

- Trace element solution SL-10 was flattened at stock strength. The generated HCl, FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, and Na2MoO4 x 2 H2O rows should remain in a 1 L stock recipe that is added at 1 ml per 1003 ml.
- Selenite-tungstate solution was flattened at stock strength. The generated NaOH, Na2SeO3 x 5 H2O, and Na2WO4 x 2 H2O rows are stock components, not final-medium concentrations.
- Wolin's vitamin solution (10x) was flattened at stock strength even though DSMZ adds only 1 ml stock to the final recipe.
- The generated HCl row records the 25% HCl stock as `2.5` `G_PER_L`, which loses the source's 10 ml 25% HCl context inside SL-10.

## Recommended Edits

- Fix `data/normalized_yaml/bacterial/sulfurospirillum_barnesii_medium.yaml` or the MediaDive import path so SL-10, Selenite-tungstate solution, and Wolin's vitamin solution remain nested stock recipes with 1 ml addition rates.
- Preserve the 25% HCl volume inside SL-10 rather than flattening it to an HCl final concentration.
- Keep the sterile anoxic post-autoclave additions linked to carbonate, lactate, nitrate, vitamins, cysteine, and sulfide.
- Regenerate `data/merge_yaml/merged/sulfurospirillum_barnesii_medium__fb8c612b.yaml`; do not hand-edit this generated file.

## Follow-up Checks

- Revalidate the normalized DSMZ 771 and KOMODO 771 sources after stock-solution fixes.
- Regenerate merged YAML and verify that the KOMODO duplicate still merges by source identity without flattening SL-10, selenite-tungstate, or Wolin vitamins.
- Verify that HCl stays in the Trace element solution SL-10 context as 10 ml of 25% HCl.

## Additional Notes

- Empty optional fields were not treated as defects.
- The DSMZ PDF was checked directly after comparing MediaDive 771 and the KOMODO duplicate source.
