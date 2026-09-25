# YAML Record Review: Thermococcus Medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermococcus_medium__89e8f0c8.yaml`
- Started UTC: 2026-09-25T09:56:00Z
- Finished UTC: 2026-09-25T09:58:45Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:009290`
- Merge fingerprint: `89e8f0c8097f73aa709435e3ac50d263346f883808d009dcd18e8e5d9d2117ce`
- Merged source: `TOGO_M273_Thermococcus_Medium`
- Media term: `TOGO:M273`
- Source medium: JCM M280, base "THERMOCOCCUS MEDIUM"

## Validation

- LinkML schema validation: Passed; exited 0 with no diagnostics.
- Strict schema validation: Passed; 1 file scanned, 0 files with errors, and 0 total error rows.
- Reference validation: Passed; 0 reference checks and no errors.
- Term validation: Passed. The only stderr output was the expected `eutils` warning about `pkg_resources`.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` records, not the embedded `MediaRecipe.curation_history` array in this merged YAML.

## Identity and Grounding

- TOGO M273 is the base JCM 280 Thermococcus Medium branch with sulfur and without maltodextrin.
- The imported `Resazurin` amount is 1000x too high: TOGO M273 and JCM 280 both specify 1 mg, while this branch stores 1 `G_PER_L`.
- The imported `NaBr` amount is 1000x too high: TOGO M273 and JCM 280 both specify 10 mg, while this branch stores 10 `G_PER_L`.
- TOGO M273 inherits the same upstream FeSO4 x 7 H2O mismatch as MediaDive J280: JCM 280 lists 2.5 mg, but the structured TOGO and MediaDive rows use 0.025 g before CultureMech import.

## Evidence

- TOGO API `M273` reports `original_media_id: JCM_M280`, pH 7.0-7.2, 10 g sulfur powder, 1 mg resazurin, 10 mg NaBr, 10 ml Trace minerals `M142`, and 10 ml Trace vitamins `M190`.
- The JCM 280 HTML source links Trace minerals to JCM Medium 151, Trace vitamins to JCM Medium 197, and lists the same base medium without maltodextrin.
- MediaDive REST `J280` expands the Trace minerals and Trace vitamins stocks, but the TOGO branch leaves both as empty `Unknown solution` records at 10 g/L.
- Exact ignored-file search found the paired TOGO M273/M274 branches and the separate direct `JCM_J280_THERMOCOCCUS_MEDIUM` record merged under `thermococcus_medium_ph_6_0.yaml`; no additional exact TOGO M273 branch was found.

## Completeness

- Required scalar fields, ingredient concentrations, the TOGO media term, curation history, and `merged_from` are present.
- No organisms or strain links are expected for this medium-level import.
- The trace mineral and vitamin compositions are absent because the 10 ml stock rows were not expanded.
- The anaerobic JCM 280 preparation instructions are absent.

## Findings

- High - `Resazurin` and `NaBr` were imported as g/L values even though the source uses mg amounts.
- High - `Trace minerals` and `Trace vitamins` were migrated to empty 10 g/L solutions instead of preserving 10 ml stock additions and expanding TOGO M142/M190 or JCM 151/197.
- High - `Distilled water` is stored as 1 g/L even though the source row is a 1 L solvent volume.
- Medium - FeSO4 x 7 H2O follows a structured TOGO/MediaDive amount of 0.025 g, but the original JCM 280 source says 2.5 mg.
- Medium - JCM 280's anaerobic N2 preparation protocol was dropped from this TOGO-derived branch.
- Medium - The direct MediaDive/JCM J280 branch is not merged with this TOGO M273 record; it is currently grouped with a `thermococcus_medium_ph_6_0` record instead.

## Recommended Edits

- Fix `data/normalized_yaml/archaea/TOGO_M273_Thermococcus_Medium.yaml`, not the generated merge YAML, so mg rows are normalized as mg-derived g/L concentrations and water remains a volume/solvent row rather than 1 g/L.
- Expand or structurally reference Trace minerals `M142` and Trace vitamins `M190` instead of emitting empty `Unknown solution` records.
- Carry the JCM 280 anaerobic preparation text into the TOGO M273 branch.
- Re-check FeSO4 x 7 H2O against the original JCM HTML before deciding whether to override TOGO/MediaDive's structured 0.025 g value.
- Reconcile TOGO M273, TOGO M274, and direct MediaDive/JCM J280 source lineage so the base medium, the maltodextrin/no-sulfur variant, and the direct import are not split by incidental naming.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the regenerated M273 branch.
- Re-run exact ignored-file search for `TOGO_M273_Thermococcus_Medium`, `JCM_M280`, `mediadive.medium:J280`, `TOGO:M273`, and `GRMD=280` after duplicate reconciliation.
- Compare the regenerated trace stocks against MediaDive REST `J280` and the JCM 151/197 cross-references before merging the JCM 280 family.

## Additional Notes

None found.
