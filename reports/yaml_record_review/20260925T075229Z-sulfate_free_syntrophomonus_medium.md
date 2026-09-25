# YAML Record Review: Sulfate-Free Syntrophomonus Medium

- Repository: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech`
- Record: `data/merge_yaml/merged/sulfate_free_syntrophomonus_medium.yaml` (`CultureMech:009890`)
- Started UTC: `2026-09-25T07:52:29Z`
- Finished UTC: `2026-09-25T07:53:10Z`
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated YAML | `data/merge_yaml/merged/sulfate_free_syntrophomonus_medium.yaml` |
| Normalized source | `data/normalized_yaml/bacterial/TOGO_M500_Sulfate-Free_Syntrophomonus_Medium.yaml` |
| CultureMech ID | `CultureMech:009890` |
| Media term | `TOGO:M500` |
| Original source | JCM `JCM_M499`, Sulfate-Free Syntrophomonus Medium |
| Merge fingerprint | `918eed8275e59de39624b076da5e949a5cc06340c0e9d1d5fa4536e09d431d23` |
| Merged from | `TOGO_M500_Sulfate-Free_Syntrophomonus_Medium` |

## Validation

| Check | Result |
| --- | --- |
| LinkML schema | Passed; `linkml-validate` reported `No issues found` for the generated YAML. |
| Strict validator | Passed; `scripts/validate_strict.py` reported 1 file, 0 total errors. |
| Reference validator | Passed; `linkml-reference-validator` reported 1 file, 0 checks, all passed. |
| Term validator | Passed; `linkml-term-validator` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

## Identity and Grounding

The generated record has the expected stable identifier, TOGO M500 term, original JCM_M499 source, and single-source merge fingerprint.

Exact gitignore-independent searches with `--no-ignore --hidden` for `TOGO:M500`, `JCM_M499`, `CultureMech:009890`, and `sulfate_free_syntrophomonus_medium` found this TOGO M500 owner, an older MediaDive J499 normalized source, and a downstream `syntrophus_aciditrophicus_medium__4d89af40.yaml` record that copied from the MediaDive source. No conflicting use of `CultureMech:009890` was found.

The simple chemical groundings are mostly plausible, including exact hydrate terms for `CaCl2*2H2O` and `MgCl2*6H2O`. The generated vitamins and salts need concentration repair before any secondary grounding audit because several source-stock values are currently attached to the wrong solution scope.

## Evidence

TOGO M500 and JCM 499 agree on a four-solution assembly: 916 ml Solution A, 70 ml Solution B, 10 ml Solution C, and 10 ml Solution D are combined after each has been prepared and sterilized differently. Solution A itself contains 50 ml mineral solution, 1 ml trace element solution SL-10, 50 ml clarified rumen fluid, 1 g Trypticase peptone, 5 ml vitamin solution, 1.7 g crotonic acid, 1 mg resazurin, and 810 ml distilled water.

The source mineral solution is a separate 1 L stock with 8 g NaCl, 1 g CaCl2*2H2O, 10 g KH2PO4, 8 g NH4Cl, and 6.6 g MgCl2*6H2O. The vitamin solution is another 1 L stock with milligram quantities of biotin, p-aminobenzoic acid, thiamine HCl, pyridoxine HCl, nicotinic acid, and pantothenic acid.

JCM 499 also specifies Solution A pH adjustment to 7.2, boiling and cooling under N2/CO2 4:1, Solution B filter sterilization and gas equilibration, and autoclaving Solutions C and D under N2. None of those preparation steps are present in the generated YAML.

## Completeness

The generated record is incomplete for a solution-assembled anaerobic medium. It exposes Solution A-D and the mineral, trace, rumen-fluid, and vitamin additions as empty `solutions` entries with gram-per-liter units rather than keeping their nested compositions and volume additions.

`target_organisms` is absent. The JCM and TOGO medium pages name the Syntrophomonus medium recipe but do not assert source-backed organism growth for this record, so no growth target was inferred.

## Findings

- Six different water rows from Solution A, Solution B, Solution C, Solution D, the mineral stock, and the vitamin stock were summed into one top-level `Distilled water` row at `902 G_PER_L`; these rows have different scopes and should not be merged.
- The generated solution entries for 916 ml Solution A, 70 ml Solution B, 10 ml Solution C, 10 ml Solution D, 50 ml mineral solution, 1 ml SL-10, 50 ml clarified rumen fluid, and 5 ml vitamin solution are empty and store source volume additions as `G_PER_L`.
- Mineral-stock components are top-level ingredients at 1 L stock strength, even though only 50 ml of mineral solution is added to Solution A.
- Vitamin-stock milligram amounts are top-level `G_PER_L` rows; for example 0.25 mg biotin and 1.25 mg p-aminobenzoic acid in the 1 L stock become `0.25 G_PER_L` and `1.25 G_PER_L`.
- The 1 mg Solution A resazurin row becomes `1 G_PER_L`, a 1000x unit slip.
- The generated YAML drops all preparation steps, including pH 7.2 adjustment, N2/CO2 boiling and dispensing, Solution B filter sterilization and gas equilibration, and N2 autoclaving for Solutions C and D.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/TOGO_M500_Sulfate-Free_Syntrophomonus_Medium.yaml` or the TOGO import/solution migration path, then regenerate `data/merge_yaml/merged/sulfate_free_syntrophomonus_medium.yaml`.
- Preserve Solution A, Solution B, Solution C, Solution D, mineral solution, and vitamin solution as distinct solution scopes; do not merge their water rows or same-named salts across scopes.
- Store Solution A-D, SL-10, clarified rumen fluid, mineral solution, and vitamin solution as volume additions or structured cross-references, not as empty `G_PER_L` solution records.
- Convert source milligram values to appropriate g/L values within their own stock scopes, especially Solution A resazurin and all vitamin stock components.
- Add source-backed preparation steps for pH adjustment, anaerobic boiling/cooling under N2/CO2, distribution under the same gas mixture, Solution B filter sterilization and gas equilibration, N2 autoclaving of Solutions C and D, and final combination of Solution B-D into Solution A.
- Reconcile this TOGO M500 record with the older MediaDive J499 normalized source and the `syntrophus_aciditrophicus_medium__4d89af40.yaml` copy-forward so future duplicate resolution uses the repaired recipe.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regenerating the merged YAML.
- Re-run exact gitignore-independent searches for `TOGO:M500`, `JCM_M499`, `CultureMech:009890`, and `sulfate_free_syntrophomonus_medium` to confirm no repaired source was split or merged unexpectedly.
- Compare the regenerated TOGO M500 ingredient scopes against JCM 499 and the MediaDive J499-derived record before propagating anything into `syntrophus_aciditrophicus_medium`.

## Additional Notes

Empty optional fields that are unrelated to solution structure and source-backed growth evidence were not treated as defects.

The generated YAML should not be hand-edited. The review findings target the maintained normalized TOGO source and the stock-aware generation path.
