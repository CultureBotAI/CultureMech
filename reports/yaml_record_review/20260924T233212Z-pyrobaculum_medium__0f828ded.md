# YAML Record Review: Pyrobaculum Medium
- Repository: CultureMech
- Record: `data/merge_yaml/merged/pyrobaculum_medium__0f828ded.yaml`
- Started UTC: 2026-09-24T23:32:12Z
- Finished UTC: 2026-09-24T23:33:34Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated file | `data/merge_yaml/merged/pyrobaculum_medium__0f828ded.yaml` |
| Maintained owner | `data/normalized_yaml/archaea/TOGO_M2470_Pyrobaculum_Medium.yaml` |
| Source identity | `TOGO:M2470`, original DSMZ medium 390 |
| Source URL | `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium390.pdf` |
| Merge fingerprint | `0f828ded0289f72c0deef25a863d6340461b19322faa325af7e2376ece484056` |

The reviewed file is a generated merge from a single TOGO owner. Future data edits belong in the maintained normalized owner, followed by regeneration of `data/merge_yaml/merged/` and downstream artifacts.

## Validation

| Validator | Result |
| --- | --- |
| Open LinkML schema | Passed; no schema issues found. |
| Strict validator | Passed with 0 ERROR rows; TSV had the header only. |
| Reference validator | Passed; 1 file, 0 checks. |
| Term validator | Passed; emitted only the expected `eutils` `pkg_resources` warning. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

The record is a TOGO M2470 wrapper around DSMZ medium 390. Live TOGO M2470 still resolves to the DSMZ 390 PDF, but its table differs from the current DSMZ 390 PDF and MediaDive 390 record: current DSMZ 390 uses 0.5 g Trypticase peptone, 0.2 g yeast extract, and 2 g Na2S2O3 x 5 H2O in the main recipe, while TOGO M2470 has 1 g yeast extract, 1 g Na2SeO3 x 5 H2O, and no Trypticase peptone or thiosulfate row.

An ignored-file-inclusive owner search across `data/normalized_yaml` and `data/merge_yaml/merged` for `CultureMech:009046`, `TOGO:M2470$`, `togomedium.org/medium/M2470$`, `DSMZ_Medium390`, `mediadive.medium:390`, the full merge fingerprint, and `TOGO_M2470_Pyrobaculum_Medium` found this TOGO owner plus direct DSMZ 390 and KOMODO 390-derived owners. Some DSMZ 390 owners are strain-specific variants, so same-source deduplication must respect the DSMZ variant text rather than collapsing every `DSMZ_Medium390` record blindly.

## Evidence

The generated artifact is stale relative to the maintained owner: the generated `Distilled water` row is `2000.0` `G_PER_L` from a summed duplicate, while the maintained TOGO M2470 owner already collapsed the identical 1000 ml main-solution water and 1000 ml trace-solution water rows back to one `1000.0` `G_PER_L` row.

Live TOGO M2470 represents Allen's trace element solution as a 10 ml addition plus a separate one-liter stock. The YAML leaves `Allen's trace element solution` as an empty `solutions` entry with `10` `G_PER_L` and promotes all trace salts to top-level ingredients. In that promotion, source rows such as 180 mg MnCl2 x 4 H2O, 450 mg Na2B4O7 x 10 H2O, 22 mg ZnSO4 x 7 H2O, 5 mg CuCl2 x 2 H2O, 3 mg Na2MoO4 x 2 H2O, and 1 mg CoSO4 x 7 H2O became 180, 450, 22, 5, 3, and 1 `G_PER_L`.

Live TOGO M2470 carries final-medium N2 handling, a pH 7.0 final adjustment, the Allen's trace stock pH adjustment to pH 2 with 1 N HCl, and a longer anoxic preparation paragraph from DSMZ 390. The generated YAML has no `preparation_steps`.

The current DSMZ 390 PDF and MediaDive 390 no longer agree with the TOGO main-solution ingredient set. The current DSMZ source still uses Allen's trace element solution, but the main recipe now has 0.5 g Trypticase peptone, 0.2 g yeast extract, 2 g Na2S2O3 x 5 H2O, and pH 6.0 for the default DSMZ 390 recipe.

## Completeness

The generated file is not complete enough for use. At minimum it needs regeneration to pick up the existing water de-duplication repair, nested representation of Allen's trace element solution, corrected milligram conversions inside that stock, the TOGO preparation text, and a source-age decision about whether M2470 should keep the live TOGO recipe or be refreshed to the current DSMZ 390 formulation.

## Findings

| Severity | Finding | Evidence | Recommended owner |
| --- | --- | --- | --- |
| Blocker | Allen's trace element solution is empty and flattened. | TOGO M2470 adds 10 ml Allen's trace element solution to the main recipe; the generated YAML has an empty solution shell and top-level rows for the stock-local trace salts. | `data/normalized_yaml/archaea/TOGO_M2470_Pyrobaculum_Medium.yaml` |
| Blocker | Stock-local milligram rows are inflated to grams per liter. | MnCl2 x 4 H2O 180 mg, Na2B4O7 x 10 H2O 450 mg, ZnSO4 x 7 H2O 22 mg, CuCl2 x 2 H2O 5 mg, Na2MoO4 x 2 H2O 3 mg, VOSO4 x 2 H2O 3 mg, and CoSO4 x 7 H2O 1 mg are stored as `G_PER_L` values. | `data/normalized_yaml/archaea/TOGO_M2470_Pyrobaculum_Medium.yaml` |
| Major | The generated artifact is stale relative to the maintained owner. | The reviewed generated file has water at `2000.0` `G_PER_L`, but the maintained TOGO M2470 owner already has the duplicate water row collapsed to `1000.0` `G_PER_L`. | Regenerate `data/merge_yaml/merged/` |
| Major | The source preparation text is absent. | TOGO M2470 carries final pH, N2 sparging, anoxic stock addition, sulfide addition, and Allen's trace pH-adjustment comments; the YAML has no `preparation_steps`. | `data/normalized_yaml/archaea/TOGO_M2470_Pyrobaculum_Medium.yaml` |
| Major | The TOGO wrapper is stale relative to current DSMZ 390. | Current DSMZ 390 / MediaDive 390 list Trypticase peptone, 0.2 g yeast extract, 2 g Na2S2O3 x 5 H2O, and no 1 g Na2SeO3 x 5 H2O main row; live TOGO M2470 still has the older table. | TOGO import source policy plus `data/normalized_yaml/archaea/TOGO_M2470_Pyrobaculum_Medium.yaml` |
| Minor | Several existing groundings need refresh. | The owner still has a stale MgSO4 x 7 H2O `mediaingredientmech_chebi_term` of `CHEBI:32599`, a legacy `MediaIngredientMech:000279` VOSO4 link, and no term for Yeast extract. | `data/normalized_yaml/archaea/TOGO_M2470_Pyrobaculum_Medium.yaml` |

## Recommended Edits

1. Decide whether TOGO M2470 should preserve the live TOGO table as a historical DSMZ 390 recipe or be refreshed to current DSMZ 390.
2. Rebuild Allen's trace element solution as a populated nested stock used at 10 ml/L.
3. Convert Allen's trace milligram rows in their stock context instead of promoting them to final-medium gram-per-liter rows.
4. Attach the main anoxic preparation and Allen's trace pH adjustment to the appropriate recipe or stock.
5. Refresh Yeast extract, MgSO4 x 7 H2O, and VOSO4 grounding.
6. Reconcile the TOGO M2470 wrapper with exact current or historical DSMZ 390 duplicates while preserving DSMZ 390 strain variants.
7. Regenerate `data/merge_yaml/merged/` after the maintained YAML and merge identity are repaired.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation on the regenerated record.
- Re-open TOGO M2470, MediaDive 390, and the DSMZ 390 PDF to confirm the source-age decision is deliberate.
- Re-run an ignored-file-inclusive search for `TOGO:M2470`, `DSMZ_Medium390`, and `mediadive.medium:390` to confirm duplicate handling with strain variants preserved.
- Confirm Allen's trace element solution exists once and its milligram salts are not top-level `G_PER_L` ingredients.

## Additional Notes

None found.
