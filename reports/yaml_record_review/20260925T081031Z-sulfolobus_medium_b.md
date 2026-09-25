# YAML Record Review: Sulfolobus Medium (B)

- Repository: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech`
- Record: `data/merge_yaml/merged/sulfolobus_medium_b.yaml` (`CultureMech:002532`)
- Started UTC: `2026-09-25T08:10:31Z`
- Finished UTC: `2026-09-25T08:10:59Z`
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated YAML | `data/merge_yaml/merged/sulfolobus_medium_b.yaml` |
| Canonical normalized source | `data/normalized_yaml/archaea/sulfolobus_medium_b.yaml` |
| CultureMech ID | `CultureMech:002532` |
| Media term | `mediadive.medium:J172` |
| Original source | JCM Medium 172, Sulfolobus Medium (B) |
| Merge fingerprint | `2c3421f0008a0c9a23bb7ae7d9686652f36aced5b3cb4d3fb1c70710b3da0783` |
| Merged from | `JCM_J165_SULFOLOBUS_MEDIUM`, `sulfolobus_medium_b`, `ms_medium`, `modified_brocks_basal_salts_yeast_extract_medeium_b`, `modified_brocks_basal_salts_yeast_extract_medium`, `modified_brocks_basal_salts_yeast_extract_tryptone_medium` |

## Validation

| Check | Result |
| --- | --- |
| LinkML schema | Passed; `linkml-validate` reported `No issues found` for the generated YAML. |
| Strict validator | Passed; `scripts/validate_strict.py` reported 1 file, 0 total errors. |
| Reference validator | Passed; `linkml-reference-validator` reported 1 file, 0 checks, all passed. |
| Term validator | Passed; `linkml-term-validator` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

## Identity and Grounding

The generated record keeps the expected `CultureMech:002532` identifier, the exact `mediadive.medium:J172` source term, and the JCM 172 pH 3.5 Sulfolobus Medium (B) label. Exact gitignore-independent searches with `--no-ignore --hidden` for `CultureMech:002532`, `mediadive.medium:J172`, the merge fingerprint, and `sulfolobus_medium_b.yaml` found the J172 normalized source and this generated merge as the only direct owners of those exact identifiers.

The merge grouping is not grounded against the current normalized sources. It folds JCM 172 together with JCM 165, JCM 269, JCM 542, JCM 585, and JCM 812 recipes that have distinct pH, additive, yeast, and tryptone requirements.

The ingredient groundings in the J172 portion are mostly plausible. `VOSO4 x n H2O` uses the hydrated vanadyl sulfate class as expected for the JCM source's `VOSO4 x H2O` row.

## Evidence

JCM 172 is a wrapper over 1 L of JCM 165 Sulfolobus Medium and adjusts final pH to 3.5 with 10 N H2SO4. MediaDive models it as a 1 L main solution containing 1 L of JCM 165, where JCM 165 is 1 L of Modified Brock's salt base plus 1 g yeast extract and pH 2.0 adjustment.

The other merged sources are source variants, not duplicates. JCM 269 says to use JCM 165 with 1.0 g Na2S2O3 x 5 H2O and adjust pH to 7.0 to 7.5 with NaOH. JCM 542 contains 5 g/L yeast extract and pH 9.0. JCM 585 says to prepare JCM 542 with 0.5 g/L final yeast extract and pH 3.0. JCM 812 says to use JCM 542 with 3.0 g/L final yeast extract, 3.0 g/L tryptone, pH 7.0, and optionally 15.0 g/L agar for solid medium.

The generated canonical formula has the J172/J165 1 g/L yeast extract and pH 3.5, but its synonyms claim the J269, J542, J585, and J812 sources are duplicates. Those source-specific thiosulfate, NaOH, pH 9.0, pH 3.0, 0.5 g/L yeast, 3.0 g/L yeast, 3.0 g/L tryptone, and optional agar requirements are absent.

## Completeness

The generated record is incomplete because it cannot represent all six merged recipes and erases each non-J172 derivative. It also keeps the inherited JCM 165 pH 2.0 step as a second top-level adjustment rather than scoping it to the source medium before the final JCM 172 pH 3.5 adjustment.

`target_organisms` is absent. The reviewed JCM medium pages do not assert growth observations in these recipe records, so no growth target was inferred.

## Findings

- The six-way merge incorrectly marks JCM 165, JCM 269, JCM 542, JCM 585, and JCM 812 as duplicates of JCM 172.
- JCM 269's required `1.0 g` Na2S2O3 x 5 H2O and pH 7.0 to 7.5 NaOH adjustment are absent.
- JCM 542's 5 g/L yeast extract, pH 9.0 adjustment, autoclaving, and precipitate-removal instruction are absent from the canonical formula.
- JCM 585's 0.5 g/L final yeast extract and pH 3.0 requirement were collapsed to J172's 1 g/L yeast and pH 3.5.
- JCM 812's 3.0 g/L final yeast extract, 3.0 g/L tryptone, pH 7.0, and optional 15.0 g/L agar addition were collapsed to J172's composition.
- The generated record includes two top-level H2SO4 pH steps, pH 3.5 and pH 2.0, without preserving that pH 2.0 belongs to the referenced JCM 165 source medium.

## Recommended Edits

- Repair the referenced-JCM resolution and duplicate merge logic, then regenerate `data/merge_yaml/merged/sulfolobus_medium_b.yaml`.
- Keep JCM 172 distinct from JCM 269, JCM 542, JCM 585, and JCM 812 because their pH and additive instructions differ.
- Represent JCM 172 as a derivative of JCM 165 with final pH 3.5, or expand JCM 165 while avoiding an extra final pH 2.0 step on the completed J172 record.
- Add Na2S2O3 x 5 H2O to JCM 269, preserve JCM 542's 5 g/L yeast and pH 9.0, preserve JCM 585's 0.5 g/L final yeast and pH 3.0, and preserve JCM 812's 3 g/L yeast, 3 g/L tryptone, pH 7.0, and optional agar.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regenerating the merged YAML.
- Re-run exact gitignore-independent searches for `CultureMech:002532`, `mediadive.medium:J172`, `2c3421f0008a0c9a23bb7ae7d9686652f36aced5b3cb4d3fb1c70710b3da0783`, and the six `merged_from` basenames.
- Recompare JCM 172, JCM 269, JCM 542, JCM 585, and JCM 812 against their JCM pages after the source split.

## Additional Notes

Empty optional fields that are unrelated to derivative source identity and source-backed growth evidence were not treated as defects.

The generated YAML should not be hand-edited. The review findings target the maintained normalized JCM/MediaDive source records and merge grouping.
