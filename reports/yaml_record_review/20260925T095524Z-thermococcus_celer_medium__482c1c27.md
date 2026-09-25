# YAML Record Review: Thermococcus Celer Medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermococcus_celer_medium__482c1c27.yaml`
- Started UTC: 2026-09-25T09:53:30Z
- Finished UTC: 2026-09-25T09:55:24Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:008054`
- Merge fingerprint: `482c1c27e2bdb591a38c5c9b3f4cf310ca8a5bfd458e0235a233f17bf8d41e14`
- Merged source: `TOGO_M150_Thermococcus_Celer_Medium`
- Media term: `TOGO:M150`
- Source medium: JCM M159, "THERMOCOCCUS CELER MEDIUM"

## Validation

- LinkML schema validation: Passed with `No issues found`.
- Strict schema validation: Passed; 1 file scanned, 0 files with errors, and 0 total error rows.
- Reference validation: Passed; exited 0 after initializing `references_cache` and reported no errors.
- Term validation: Passed. The only stderr output was the expected `eutils` warning about `pkg_resources`.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` records, not the embedded `MediaRecipe.curation_history` array in this merged YAML.

## Identity and Grounding

- Identity is split across two generated records for the same JCM 159 source. The TOGO import produced this M150 record, while `data/merge_yaml/merged/THERMOCOCCUS_CELER_MEDIUM.yaml` came from direct MediaDive/JCM `J159` and expands the same JCM page to a separate fingerprint.
- `Resazurin` is mis-scaled: TOGO M150 and JCM 159 both give 1 mg per liter, while the generated TOGO branch stores 1 `G_PER_L`.
- The `Modified Brock's salt base solution` row is represented as an empty `solutions` entry with `concentration.value: 1` and `unit: G_PER_L`; the source row is a 1 L cross-reference to JCM Medium 165, surfaced by TOGO as `M156`.
- The JCM 159 preparation text mentions pH adjustment with H2SO4, N2 atmosphere handling, separate yeast-extract and Na2S x 9 H2O stock sterilization, and sulfur steaming. This generated TOGO branch keeps H2SO4 and N2 as variable ingredients but drops the preparation text itself.

## Evidence

- TOGO API `M150` and the linked JCM 159 page agree on the base recipe: 1 L `Modified Brock's salt base solution`, 40 g NaCl, 2 g yeast extract, 10 g sulfur powder, 0.5 g Na2S x 9 H2O, and 1 mg resazurin.
- MediaDive REST `J159` expands `Modified Brock's salt base solution` into its salts and trace metals, including FeCl3 x 6 H2O at 2 mg/L, and retains the anaerobic JCM preparation step.
- JCM 159 links its `Modified Brock's salt base solution` row to JCM Medium 165. JCM 165 is "SULFOLOBUS MEDIUM" and contains the same Modified Brock's salt base that TOGO exposes as M156.
- Exact ignored-file search found `TOGO_M150_Thermococcus_Celer_Medium`, the separate `JCM_J159_THERMOCOCCUS_CELER_MEDIUM`, and the direct DSMZ/KOMODO Medium 266 branches; it found no additional exact TOGO M150 branch.
- An initially broad cross-reference search over `TOGO_M156` and `TOGO_M165` was discarded because it also matched unrelated IDs such as `TOGO_M1567` and `TOGO_M1655`; exact slug and anchored-ID search was used for evidence about M156/M165.

## Completeness

- Required scalar fields, ingredient concentrations, the TOGO media term, curation history, and `merged_from` are present.
- No organisms or strain links are expected for this medium-level import.
- The cross-referenced Modified Brock's salt base composition is not materialized in this branch.
- Preparation instructions from JCM 159 are absent.

## Findings

- High - `Resazurin` is recorded at 1 g/L instead of the source value of 1 mg/L.
- High - The 1 L Modified Brock's salt base cross-reference was migrated to an empty solution with a mass concentration of 1 g/L, leaving the base salts unavailable from this generated record.
- Medium - TOGO M150 and direct MediaDive/JCM J159 are duplicates of the same JCM 159 source but remain split into different merged YAML records.
- Medium - The JCM anaerobic preparation protocol was dropped from the TOGO branch even though the imported source contains it.

## Recommended Edits

- Fix `data/normalized_yaml/archaea/TOGO_M150_Thermococcus_Celer_Medium.yaml`, not the generated merge YAML, so `Resazurin` is normalized as 0.001 g/L.
- Expand or structurally reference TOGO M156/JCM 165 for the `Modified Brock's salt base solution` row instead of storing an empty `Unknown solution` at 1 g/L.
- Merge the TOGO M150 and direct MediaDive/JCM J159 branches as one source duplicate family after the cross-reference expansion and resazurin unit are corrected.
- Preserve JCM 159's anaerobic preparation text during TOGO import or duplicate merging.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the regenerated `thermococcus_celer_medium` M150 branch.
- Re-run an exact ignored-file search for `TOGO_M150_Thermococcus_Celer_Medium`, `JCM_J159_THERMOCOCCUS_CELER_MEDIUM`, `GRMD=159`, and `mediadive.medium:J159` after duplicate merging to confirm the JCM 159 split is gone.
- Compare the regenerated record against MediaDive REST `J159` to confirm the Modified Brock's salt base concentrations survive the import path.

## Additional Notes

None found.
