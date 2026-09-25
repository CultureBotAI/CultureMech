# YAML Record Review: Pyrobaculum Calidifontis Medium
- Repository: CultureMech
- Record: `data/merge_yaml/merged/pyrobaculum_calidifontis_medium__ac1a598f.yaml`
- Started UTC: 2026-09-24T23:28:25Z
- Finished UTC: 2026-09-24T23:29:25Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated file | `data/merge_yaml/merged/pyrobaculum_calidifontis_medium__ac1a598f.yaml` |
| Maintained owner | `data/normalized_yaml/archaea/TOGO_M333_Pyrobaculum_Calidifontis_Medium.yaml` |
| Source identity | `TOGO:M333`, original source `JCM_M338` |
| Source URL | `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=338` |
| Merge fingerprint | `ac1a598f5be2d841887a27803fa1799231ab118ec60710e8c9225e0b1fd95448` |

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

The record is a TOGO M333 wrapper around JCM medium 338. Live TOGO M333 and the live JCM `GRMD=338` page agree on `Pyrobaculum Calidifontis Medium`, pH 7.0, 10 g Tryptone, 1 g yeast extract, 3 g Na2S2O3 x 5 H2O, and 1 L distilled water.

An ignored-file-inclusive owner search across `data/normalized_yaml` and `data/merge_yaml/merged` for `CultureMech:009711`, `TOGO:M333$`, `togomedium.org/medium/M333$`, `JCM_M338`, `GRMD=338`, the full merge fingerprint, and `TOGO_M333_Pyrobaculum_Calidifontis_Medium` found this TOGO owner plus `data/normalized_yaml/archaea/JCM_J338_PYROBACULUM_CALIDIFONTIS_MEDIUM.yaml`, a direct JCM 338 owner. The same JCM source is therefore split into two generated records.

## Evidence

The JCM 338 source and TOGO M333 both list distilled water at 1 L. The generated YAML stores that row as `1` `G_PER_L`, so the final water amount is 1000-fold too low relative to the source volume.

The source also instructs curators to adjust the pH to 7.0 with NaOH. The generated YAML has a variable NaOH ingredient inferred from that comment but no `preparation_steps`, so the actual pH-adjustment instruction is missing.

The direct JCM owner already grounds Tryptone to `MICRO:0000182` and Yeast extract to `FOODON:03315426`. The TOGO M333 owner still lacks terms for both undefined components.

## Completeness

The Tryptone, yeast extract, thiosulfate, pH, and JCM identity are present, but the water row is materially wrong and the pH-adjustment instruction is absent. Repairing the water conversion should make this TOGO owner fingerprint with the direct JCM owner or otherwise become an intentional redundant wrapper.

## Findings

| Severity | Finding | Evidence | Recommended owner |
| --- | --- | --- | --- |
| Blocker | The 1 L water row is represented as `1 G_PER_L`. | TOGO M333 and JCM 338 list 1 L Distilled water; the generated YAML stores Distilled water with `value: '1'` and `unit: G_PER_L`. | `data/normalized_yaml/archaea/TOGO_M333_Pyrobaculum_Calidifontis_Medium.yaml` |
| Major | The JCM pH-adjustment instruction is absent. | TOGO M333 and JCM 338 both say to adjust to pH 7.0 with NaOH; the YAML has no `preparation_steps`. | `data/normalized_yaml/archaea/TOGO_M333_Pyrobaculum_Calidifontis_Medium.yaml` |
| Major | The same JCM 338 source is split across two generated records. | Ignored-file-inclusive search found `data/normalized_yaml/archaea/JCM_J338_PYROBACULUM_CALIDIFONTIS_MEDIUM.yaml` and generated `PYROBACULUM_CALIDIFONTIS_MEDIUM.yaml`, both pointing to `GRMD=338`. | Merge identity/fingerprint logic plus both normalized owners |
| Minor | Tryptone and Yeast extract are ungrounded. | The TOGO owner has no ontology terms for either undefined component, while the direct JCM owner already grounds them to `MICRO:0000182` and `FOODON:03315426`. | `data/normalized_yaml/archaea/TOGO_M333_Pyrobaculum_Calidifontis_Medium.yaml` |

## Recommended Edits

1. Convert the 1 L distilled water source row to the repository's 1000 ml/L or 1000 g/L water representation.
2. Add the JCM 338 pH 7.0 adjustment with NaOH as a preparation step.
3. Ground Tryptone and Yeast extract using the same exact mappings already applied to the direct JCM owner.
4. Reconcile the TOGO M333 wrapper with the direct JCM 338 owner so the exact JCM source merges or one wrapper is intentionally suppressed.
5. Regenerate `data/merge_yaml/merged/` after the maintained YAML and merge identity are repaired.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation on the regenerated record.
- Re-open TOGO M333 and JCM 338 to confirm water is no longer represented as `1 G_PER_L`.
- Re-run an ignored-file-inclusive search for `TOGO:M333`, `JCM_M338`, and `GRMD=338` to confirm exact JCM 338 duplicate handling.

## Additional Notes

The JCM source has the same three non-water ingredients and pH as DSMZ 1090, but this report treated only JCM 338 and its TOGO M333 wrapper as exact same-source duplicates.
