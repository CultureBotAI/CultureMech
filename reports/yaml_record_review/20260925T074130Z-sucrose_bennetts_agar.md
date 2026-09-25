# YAML Record Review: SUCROSE-BENNETT'S AGAR
- Repository: CultureMech
- Record: data/merge_yaml/merged/sucrose_bennetts_agar.yaml
- Started UTC: 2026-09-25T07:41:30Z
- Finished UTC: 2026-09-25T07:41:30Z
- Verdict: pass with minor issues

## Target
Reviewed generated record `CultureMech:002232` / `sucrose_bennetts_agar` from `data/merge_yaml/merged/sucrose_bennetts_agar.yaml`.

The generated record is the canonical record for JCM J104 plus a DSMZ 1762 concentration variant.

## Validation
- Schema validation: Passed with `No issues found`.
- Strict validation: Passed for 1 file with 0 total error rows.
- Reference validation: Passed for 1 file with 0 link checks and all validations passing.
- Term validation: Passed.
- Embedded curation history validation: Not checked; the standalone history validator does not target `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding
The generated formula correctly represents JCM medium 104 as `mediadive.medium:J104`.

The direct child relationship to `CultureMech:001230` / DSMZ medium 1762 is valid as a concentration variant: DSMZ keeps yeast extract, beef extract, N-Z amine, and sucrose at the same 1, 1, 2, and 10 g/L concentrations but increases agar from 15 g/L to 20 g/L and uses pH 7.2 instead of the JCM pH 7.3.

An exact search found the JCM J104 and DSMZ 1762 normalized records, the generated JCM/DSMZ variant merge, and the expected indexes. A broader search for `J104` and an unanchored slug also matched unrelated `J1040`-to-`J1049` records and separate TOGO Sucrose-Bennett imports; that broad output was discarded.

## Evidence
The JCM 104 page and MediaDive J104 payload agree on the canonical recipe: yeast extract 1 g/L, beef extract 1 g/L, N-Z amine type A 2 g/L, sucrose 10 g/L, agar 15 g/L, distilled water to 1 L, and pH 7.3.

The MediaDive 1762 payload for DSMZ Sucrose-Bennett's Agar has the same yeast extract, beef extract, N-Z amine, and sucrose quantities, but agar at 20 g/L and pH 7.2.

MediaDive medium 187 is `MEDIUM FOR OSMOPHILIC FUNGI (M 40 Y)`, with 400 g/L sucrose, 20 g/L malt extract, 5 g/L yeast extract, 20 g/L agar, and pH 5.4. It is not an appropriate match for Sucrose-Bennett's Agar.

Two separate TOGO Sucrose-Bennett generated records are present for JCM and NBRC sources. They have separate fingerprints because their imported water rows and ingredient labels differ from the MediaDive records.

## Completeness
The generated ingredient values, pH, source identity, and DSMZ variant relationship all match the reviewed MediaDive/JCM evidence.

The generated record is stale relative to the September normalized records: the current JCM parent has an exact Yeast extract grounding, and the current DSMZ child has exact Beef extract and Yeast extract groundings that were added after the August merge.

The `kg_microbe_match: mediadive.medium:187` value is a stale false match to an unrelated high-sucrose fungal medium and should be removed.

## Findings
- Formula review passes for the JCM J104 canonical record.
- The DSMZ 1762 child is correctly modeled as a single-axis agar concentration variant.
- The kg-microbe match to MediaDive 187 is false.
- The generated merge predates later exact complex-extract groundings in both normalized parents.

## Recommended Edits
- Remove `kg_microbe_match: mediadive.medium:187` from the normalized JCM and DSMZ Sucrose-Bennett records if no exact kg-microbe match exists, then regenerate `data/merge_yaml/merged/sucrose_bennetts_agar.yaml`.
- Regenerate from the current normalized YAML so the Yeast extract and Beef extract groundings propagate.
- Keep the DSMZ 1762 relationship as a `CONCENTRATION_VARIANT` rather than merging its 20 g/L agar value into the JCM 15 g/L canonical formula.
- Deduplicate the TOGO JCM and NBRC Sucrose-Bennett records separately only after their water-row unit artifacts and label differences are normalized.

## Follow-up Checks
- Confirm the regenerated JCM canonical still has agar 15 g/L and pH 7.3.
- Confirm the DSMZ child still has agar 20 g/L and pH 7.2.
- Confirm MediaDive 187 no longer appears as a kg-microbe match.
- Re-run schema, strict, reference, and term validators on the regenerated merged YAML.

## Additional Notes
The final exact local search for `mediadive.medium:J104`, `mediadive.medium:1762`, `CultureMech:002232`, `CultureMech:001230`, and `JCM_J104_SUCROSE-BENNETT_S_AGAR` included ignored and hidden files under `data/normalized_yaml` and `data/merge_yaml/merged`.
