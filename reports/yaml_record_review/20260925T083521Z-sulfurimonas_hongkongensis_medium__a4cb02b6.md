# YAML Record Review: SULFURIMONAS HONGKONGENSIS MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/sulfurimonas_hongkongensis_medium__a4cb02b6.yaml
- Started UTC: 2026-09-25T08:31:00Z
- Finished UTC: 2026-09-25T08:35:21Z
- Verdict: needs curation

## Target

- Reviewed generated record `CultureMech:000577` in `data/merge_yaml/merged/sulfurimonas_hongkongensis_medium__a4cb02b6.yaml`.
- Canonical source: `data/normalized_yaml/bacterial/sulfurimonas_hongkongensis_medium.yaml`.
- Parent source: `data/normalized_yaml/bacterial/KOMODO_113_THIOBACILLUS_DENITRIFICANS_MEDIUM.yaml`.
- Media term: `mediadive.medium:113a`, `DSMZ Medium 113a`, `SULFURIMONAS HONGKONGENSIS MEDIUM`.
- Merge fingerprint: `a4cb02b6ff81dfa0741038341358ff191c94305d1c30ff5069fbf82b05a0f19d`.

## Validation

- LinkML schema validation passed; `linkml-validate` exited 0 with no diagnostics.
- Strict validation passed with 0 error rows.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` was not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

- The generated canonical identity matches DSMZ/MediaDive medium `113a`, `SULFURIMONAS HONGKONGENSIS MEDIUM`, with pH 7.0-7.2.
- The exact `CultureMech:000577`, `mediadive.medium:113a`, and merge fingerprint strings are present in the generated merge and normalized indexes at the expected locations.
- An exact ignored-file-inclusive search for `source_id: komodo.medium:113` and `id: komodo.medium:113` found the generated synonym and the KOMODO source record only in the scoped target files; an earlier broader `komodo.medium:113` search was discarded because it also matched IDs such as `komodo.medium:1130`.
- The parent `komodo.medium:113` source is not cleanly grounded: its metadata names `THIOBACILLUS DENITRIFICANS MEDIUM` and says `DSMZ Medium: 113`, but its ingredient signature matches DSMZ 113a rather than DSMZ 113.

## Evidence

- MediaDive `113a` and the DSMZ `DSMZ_Medium113a.pdf` recipe agree that the final recipe uses 942 ml Solution A, 40 ml Solution B, 20 ml Solution C, 1 ml Solution D, and 1 ml Solution E for a 1004 ml final volume.
- DSMZ 113a Solution A contains 25 g NaCl, 2 g KH2PO4, 2 g KNO3, 1 g NH4Cl, 0.8 g MgSO4 x 7 H2O, 2 ml Trace element solution SL-4, and 940 ml water.
- DSMZ 113a Solution B contains 5 g Na2S2O3 x 5 H2O in 40 ml water, Solution C contains 1 g Na2CO3 in 20 ml water, Solution D contains 20 mg FeSO4 x 7 H2O in 10 ml 0.1 N H2SO4, and Solution E adds 1 ml Wolin's vitamin solution (10x).
- MediaDive `113` and `DSMZ_Medium113.pdf` show that DSMZ Medium 113 is a distinct recipe: it omits NaCl, has only 20 ml Solution B in a 1003 ml final volume, and has no Solution E.
- The generated record stores several stock strengths as if they were final medium concentrations: 26.5393 g/L NaCl from Solution A, 125 g/L Na2S2O3 x 5 H2O from Solution B, 50 g/L Na2CO3 from Solution C, full-strength SL-4 trace components, and full-strength Wolin vitamin components.

## Completeness

- The generated record captures the DSMZ 113a name, pH range, defined/liquid classification, major stock components, trace stock components, vitamin stock components, and source preparation text.
- Explicit water rows are absent from the generated record, but they mainly define stock volumes and are not scored as missing standalone medium ingredients here.
- The normalized model cannot reconstruct the final working concentrations or stock hierarchy because Solution A, B, C, D, E, Trace element solution SL-4, and Wolin's vitamin solution were flattened.

## Findings

- The recipe is flattened at stock concentration rather than represented at final-medium concentration. DSMZ 113a calls for 942 ml Solution A, 40 ml Solution B, 20 ml Solution C, 1 ml Solution D, and 1 ml Solution E per 1004 ml final volume; the generated YAML instead emits each stock recipe's g/L values directly.
- The generated `FeSO4 x 7 H2O` value is chemically invalid. It sums the 2 g/L FeSO4 in Solution D with the 0.2 g/L FeSO4 in Trace element solution SL-4 into one 2.2 g/L ingredient, even though those values belong to different stock solutions that are added at different rates.
- `H2SO4` is unit-corrupted: the source has 10 ml of 0.1 N H2SO4 in Solution D, while the generated YAML records `10` `G_PER_L`.
- The `komodo.medium:113` source needs regrounding before it can be safely merged. It claims to be DSMZ Medium 113, but DSMZ 113 lacks 113a's NaCl and Solution E and uses a different Solution B dilution.

## Recommended Edits

- Fix `data/normalized_yaml/bacterial/sulfurimonas_hongkongensis_medium.yaml` or the MediaDive import path so DSMZ 113a retains the five final additions and nested stock recipes instead of emitting stock strengths as flat final `G_PER_L` ingredients.
- Fix the duplicate `FeSO4 x 7 H2O` cleanup so equal names in separate stocks are not summed unless they resolve into the same final solution context.
- Preserve volumetric acid entries such as 10 ml of 0.1 N H2SO4 without converting the amount to `10` `G_PER_L`.
- Reconcile `data/normalized_yaml/bacterial/KOMODO_113_THIOBACILLUS_DENITRIFICANS_MEDIUM.yaml` against KOMODO/DSMZ. If it is intended to track DSMZ 113, regenerate it from the DSMZ 113 composition and remove the DSMZ 113a duplicate edge; if it intentionally copied DSMZ 113a, correct its upstream DSMZ mapping before generating merge YAML.
- Regenerate `data/merge_yaml/merged/sulfurimonas_hongkongensis_medium__a4cb02b6.yaml`; do not hand-edit this generated file.

## Follow-up Checks

- Revalidate the normalized DSMZ 113a and KOMODO 113 sources after import or merge fixes.
- Regenerate merged YAML and verify this record no longer collapses SL-4, Wolin's vitamin solution, Solution D FeSO4, or H2SO4 into flat final ingredients.
- Confirm whether `komodo.medium:113` should remain linked to `mediadive.medium:113` or should point to `mediadive.medium:113a`.

## Additional Notes

- Empty optional fields were not treated as defects.
- DSMZ and MediaDive source agreement was checked for both medium `113a` and medium `113`.
