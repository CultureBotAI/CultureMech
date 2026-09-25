# YAML Record Review: Thermococcus Medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermococcus_medium__670c562c.yaml`
- Started UTC: 2026-09-25T09:56:00Z
- Finished UTC: 2026-09-25T09:58:44Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:009300`
- Merge fingerprint: `670c562c08fc488df1c4fe6acf6a8fc0e0993cc34ac11c08c0882663a2c8d373`
- Merged source: `TOGO_M274_Thermococcus_Medium`
- Media term: `TOGO:M274`
- Source medium: JCM M280-2, the maltodextrin/no-sulfur branch of "THERMOCOCCUS MEDIUM"

## Validation

- LinkML schema validation: Passed; exited 0 with no diagnostics.
- Strict schema validation: Passed; 1 file scanned, 0 files with errors, and 0 total error rows.
- Reference validation: Passed; 0 reference checks and no errors.
- Term validation: Passed. The only stderr output was the expected `eutils` warning about `pkg_resources`.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` records, not the embedded `MediaRecipe.curation_history` array in this merged YAML.

## Identity and Grounding

- TOGO M274 is the JCM M280 variant described in the source comment as most Thermococcus strains growing with 5.0 g/L maltodextrin and omitted sulfur; the generated branch correctly includes maltodextrin and omits elemental sulfur.
- The imported `Resazurin` amount is 1000x too high: TOGO M274 and JCM 280 both specify 1 mg, while this branch stores 1 `G_PER_L`.
- The imported `NaBr` amount is 1000x too high: TOGO M274 and JCM 280 both specify 10 mg, while this branch stores 10 `G_PER_L`.
- TOGO M274 inherits the same upstream FeSO4 x 7 H2O mismatch as MediaDive J280: JCM 280 lists 2.5 mg, but the structured TOGO and MediaDive rows use 0.025 g before CultureMech import.

## Evidence

- TOGO API `M274` reports `original_media_id: JCM_M280-2`, the JCM 280 source URL, 5 g/L maltodextrin, 1 mg resazurin, 10 mg NaBr, 10 ml Trace minerals `M142`, and 10 ml Trace vitamins `M190`.
- The JCM 280 HTML source links Trace minerals to JCM Medium 151, Trace vitamins to JCM Medium 197, and lists 2.5 mg FeSO4 x 7 H2O, 10 mg NaBr, 1 mg resazurin, and 1 L distilled water.
- MediaDive REST `J280` expands the Trace minerals and Trace vitamins stocks, but the TOGO branch leaves both as empty `Unknown solution` records at 10 g/L.
- Exact ignored-file search found the paired TOGO M273/M274 branches and the separate direct `JCM_J280_THERMOCOCCUS_MEDIUM` record merged under `thermococcus_medium_ph_6_0.yaml`; no additional exact TOGO M274 branch was found.

## Completeness

- Required scalar fields, ingredient concentrations, the TOGO media term, curation history, and `merged_from` are present.
- The maltodextrin/no-sulfur variant membership is represented.
- No organisms or strain links are expected for this medium-level import.
- The trace mineral and vitamin compositions are absent because the 10 ml stock rows were not expanded.
- The anaerobic JCM 280 preparation instructions are absent.

## Findings

- High - `Resazurin` and `NaBr` were imported as g/L values even though the source uses mg amounts.
- High - `Trace minerals` and `Trace vitamins` were migrated to empty 10 g/L solutions instead of preserving 10 ml stock additions and expanding TOGO M142/M190 or JCM 151/197.
- High - `Distilled water` is stored as 1 g/L even though the source row is a 1 L solvent volume.
- Medium - FeSO4 x 7 H2O follows a structured TOGO/MediaDive amount of 0.025 g, but the original JCM 280 source says 2.5 mg.
- Medium - JCM 280's anaerobic N2 preparation protocol was dropped from this TOGO-derived branch.
- Medium - The branch has no pH value even though JCM 280 gives pH 7.0-7.2 for the base medium that the M274 variant modifies.

## Recommended Edits

- Fix `data/normalized_yaml/archaea/TOGO_M274_Thermococcus_Medium.yaml`, not the generated merge YAML, so mg rows are normalized as mg-derived g/L concentrations and water remains a volume/solvent row rather than 1 g/L.
- Expand or structurally reference Trace minerals `M142` and Trace vitamins `M190` instead of emitting empty `Unknown solution` records.
- Carry the JCM 280 anaerobic preparation text into the TOGO M274 branch.
- Re-check FeSO4 x 7 H2O against the original JCM HTML before deciding whether to override TOGO/MediaDive's structured 0.025 g value.
- Preserve the JCM pH range for the maltodextrin/no-sulfur variant unless a stronger source says the variant changes pH.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the regenerated M274 branch.
- Re-run exact ignored-file search for `TOGO_M274_Thermococcus_Medium`, `JCM_M280-2`, `TOGO:M274`, and `GRMD=280` after regeneration.
- Compare the regenerated trace stocks against MediaDive REST `J280` and the JCM 151/197 cross-references before merging the JCM 280 family.

## Additional Notes

None found.
