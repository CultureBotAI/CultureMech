# YAML Record Review: freshwater_medium_with_toluene

- Repository: CultureMech
- Record: data/merge_yaml/merged/freshwater_medium_with_toluene__185c443d.yaml
- Started UTC: 2026-09-23T04:42:13Z
- Finished UTC: 2026-09-23T04:43:28Z
- Verdict: needs curation

## Target

- Reviewed generated MediaRecipe `CultureMech:003090` / `freshwater_medium_with_toluene`, the direct MediaDive/JCM Medium J747 import.
- Compared it with maintained source `data/normalized_yaml/bacterial/freshwater_medium_with_toluene.yaml`.
- Cross-checked the MediaDive REST payload for JCM J747 and the live JCM GRMD=747 page.

## Validation

- LinkML open-schema validation: pass.
- Strict CultureMech validation: pass with 0 error rows.
- LinkML reference validation: pass; 0 external reference checks.
- LinkML term validation: pass.
- Embedded curation history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding

- `mediadive.medium:J747` correctly identifies JCM Medium 747, FRESHWATER MEDIUM WITH TOLUENE.
- Exact ignored-inclusive lookup for `mediadive.medium:J747`, `CultureMech:003090`, and `freshwater_medium_with_toluene__185c443d` covered normalized and generated YAML; it found this single maintained JCM J747 owner, index entries for the owner, and the suffixed generated file.
- The generated record's base medium identity is correct, but its quantities are dominated by a J747 parse error that treated the 36 ml of post-autoclave additions as the main-solution volume.
- The dangling solution `Trace element solution (see Medium No. 187` is empty and missing the closing parenthesis/source linkage needed to represent the 1 ml Medium 187 trace element addition.

## Evidence

- JCM 747 defines a base with 3.0 g Iron(III) citrate, 1.0 g NaCl, 0.5 g KCl, 0.4 g MgCl2 x 6 H2O, 0.25 g NH4Cl, 0.2 g KH2PO4, 0.1 g CaCl2 x 2 H2O, 1.42 mg Na2SO4, and 1.36 g Sodium acetate x 3 H2O brought to 970 ml before post-autoclave additions.
- MediaDive's J747 payload instead reports Solution A as 36 ml, the sum of the 30 ml NaHCO3 stock plus six 1 ml stock additions. The generated NaCl row is consequently 1 g / 0.036 L = 27.7778 g/L, and the same denominator inflates the other base minerals.
- Live JCM has 3.0 g Iron(III) citrate in the 970 ml base, but MediaDive reports 12 g in the erroneous 36 ml Solution A and the generated file carries that as 333.333 g/L.
- The generated NaHCO3, FeCl2, and Toluene rows convert source additions of 30 ml 8.5% NaHCO3 solution, 0.5 ml 100 mM FeCl2 solution per 50 ml, and 5 ul Toluene per 50 ml into 30, 0.5, and 5 g/L top-level ingredient rows.
- The Medium 187 FeCl2 solution, Medium 403 Vitamin solution, Medium 403 Thiamine solution, Medium 403 Vitamin B12 solution, and Medium 431 Selenite-tungstate solution are flattened into top-level stock-strength ingredients instead of modeled as 1 ml stock additions.
- The generated `Sodium phosphate buffer` row is 200 g/L because two 100 ml buffer solvent rows from separate vitamin and thiamine stocks were merged by summation; the maintained normalized YAML now collapses that stale merge artifact to 100 g/L, but both values are products of stock flattening.

## Completeness

- Solution A, the 8.5% NaHCO3 solution, the Medium 187 FeCl2 solution, the Medium 187 trace element solution, the three Medium 403 vitamin stocks, and the Medium 431 Selenite-tungstate solution are not structurally represented.
- The two post-distribution anaerobic additions of 0.5 ml 100 mM FeCl2 solution and 5 ul Toluene per 50 ml are not represented with their per-vessel basis.
- Filter-sterilized stock additions after autoclaving are not tied to the corresponding solution rows.
- Trace element solution composition is entirely absent.

## Findings

- Major: JCM 747 base salts are inflated because MediaDive parsed the 36 ml of post-autoclave additions as the Solution A volume instead of preserving the 970 ml base context.
- Major: Iron(III) citrate is both misparsed by MediaDive as 12 g instead of the JCM source 3.0 g and normalized over the erroneous 36 ml volume.
- Major: milliliter stock additions and the microliter toluene addition were imported as gram-per-liter final ingredient concentrations.
- Major: referenced Medium 187, Medium 403, and Medium 431 stocks are flattened into top-level stock-strength ingredients or, for Trace element solution, reduced to an empty malformed solution stub.
- Major: the generated `Sodium phosphate buffer` row still contains a stale summed duplicate value that no longer matches maintained normalized YAML.

## Recommended Edits

- Rebuild the maintained JCM 747 record directly from JCM GRMD=747, using a 970 ml base before the filter-sterilized stock additions.
- Restore Iron(III) citrate to the live JCM 3.0 g source amount before any final-volume normalization.
- Represent 30 ml 8.5% NaHCO3, 1 ml FeCl2 solution, 1 ml Trace element solution, 1 ml Vitamin solution, 1 ml Thiamine solution, 1 ml Vitamin B12 solution, and 1 ml Selenite-tungstate solution as filter-sterilized post-autoclave additions.
- Represent the 0.5 ml 100 mM FeCl2 and 5 ul Toluene additions on the source per-50-ml vessel basis or convert them explicitly with unit-aware logic.
- Move all Medium 187, Medium 403, and Medium 431 stock contents into proper nested stock recipes and remove the flattened stock-strength top-level rows.
- Regenerate `data/merge_yaml/merged/freshwater_medium_with_toluene__185c443d.yaml` after normalized/import curation so the merged output picks up the normalized duplicate-buffer repair.

## Follow-up Checks

- After repair, rerun open-schema, strict, reference, and term validation on the generated JCM J747 YAML.
- Confirm the base mineral rows are no longer divided by 0.036 L.
- Confirm stock-only vitamin, thiamine, B12, selenite-tungstate, and FeCl2-solution ingredients do not appear as top-level final-medium rows.
- Confirm the Medium 187 trace element solution is populated and keeps its source reference.
- Confirm the generated file contains no 200 g/L Sodium phosphate buffer row.

## Additional Notes

- The generated file is derived data and is stale relative to the September duplicate-buffer repair in normalized YAML. The same major JCM J747 MediaDive parse and stock-flattening errors remain in the maintained normalized record.
