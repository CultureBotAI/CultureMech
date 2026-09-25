# YAML Record Review: modified_mmjs_medium_b

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_mmjs_medium_b.yaml
- Started UTC: 2026-09-24T12:25:21Z
- Finished UTC: 2026-09-24T12:25:21Z
- Verdict: needs curation

## Target

- Reviewed merged record `CultureMech:009994`, `modified_mmjs_medium_b`, generated from `data/normalized_yaml/bacterial/TOGO_M597_Modified_MMJS_Medium_B.yaml`.
- The record represents TOGO `M597`, which points back to JCM `JCM_M592` / `GRMD=592`, named `MODIFIED MMJS MEDIUM (B)`.
- The generated TOGO record was compared with TOGO `M597`, JCM `GRMD=592`, and the parallel MediaDive `J592` parse of the same JCM source.

## Validation

- LinkML open-schema validation: passed; `linkml-validate` exited 0 with `No issues found`.
- Strict validation: passed; `scripts/validate_strict.py` reported 1 file scanned, 0 files with errors, and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` checked 1 file and reported 0 reference checks and no failures.
- Term validation: passed; `linkml-term-validator` exited 0 and printed `Validation passed`.
- Embedded `curation_history` entries were not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- TOGO `M597`, MediaDive `J592`, and JCM `GRMD=592` all identify the same Modified MMJS Medium (B) recipe.
- A gitignore-independent duplicate check for the exact normalized name and JCM/TOGO/MediaDive identifiers found a parallel MediaDive maintained record, `data/normalized_yaml/bacterial/modified_mmjs_medium_b.yaml`, and a separate generated record, `data/merge_yaml/merged/modified_mmjs_medium_b__2b3d6f4c.yaml`, for the same JCM 592 source.
- No inspected source payload identified a target organism for this medium.

## Evidence

- JCM lists Solution A with 1 L distilled water; gram-scale salts including NaCl, MgSO4 x 7 H2O, MgCl2 x 6 H2O, FeSO4 x 7 H2O, Na2S2O3 x 5 H2O, and ferric citrate; 1 mg NiCl2 x 6 H2O, 1 mg Na2SeO3 x 5 H2O, and 1 mg H2WO4; and 5 ml Trace mineral solution.
- JCM instructs adjusting Solution A to pH 6.8 with NaOH, autoclaving under N2-CO2, then adding 1 ml Trace vitamins and 20 ml 5% NaHCO3 solution per liter before replacing the gas phase with N2-CO2-O2.
- TOGO `M597` preserves the source `mg`, `g`, `L`, and `ml` units in its component payload.
- The generated TOGO record stores multiple source amounts as `G_PER_L` regardless of their source unit: 1 L water becomes `1` `G_PER_L`, 1 mg NiCl2 x 6 H2O becomes `1` `G_PER_L`, 1 mg Na2SeO3 x 5 H2O becomes `1` `G_PER_L`, and 1 mg H2WO4 becomes `1` `G_PER_L`.
- The generated `solutions` rows also assign `G_PER_L` to milliliter additions, with the 5 ml Trace mineral solution, 1 ml Trace vitamins, and 20 ml 5% NaHCO3 solution stored as `5`, `1`, and `20` `G_PER_L`.

## Completeness

- Main Solution A salts are present, but their generated magnitudes are unreliable wherever the source unit was not grams.
- NaOH is present only as a variable top-level ingredient, which is reasonable for the pH adjustment instruction.
- The 5 ml Trace mineral solution, 1 ml Trace vitamins, and 20 ml 5% NaHCO3 solution additions are present as empty solution stubs but carry the wrong concentration unit.
- The current JCM page lists `Ferric citrate`; the generated TOGO record, TOGO API payload, and MediaDive payload all carry `Ferrous citrate`, so this 0.01 g row needs source reconciliation.

## Findings

- Blocker: TOGO unit conversion is not preserving source units. The source 1 mg NiCl2 x 6 H2O, 1 mg Na2SeO3 x 5 H2O, and 1 mg H2WO4 rows are each encoded as `1` `G_PER_L`, inflating those rows by roughly three orders of magnitude.
- Blocker: milliliter stock additions are encoded as grams per liter in `solutions`. The 5 ml Trace mineral solution, 1 ml Trace vitamins, and 20 ml 5% NaHCO3 solution rows are structured as empty solutions with `G_PER_L` concentrations instead of volume additions.
- Major: the 1 L distilled-water row is encoded as `1` `G_PER_L`, so the solvent amount is not represented with a volume unit.
- Major: JCM currently lists `Ferric citrate`, while the parsed TOGO and MediaDive payloads and generated YAML say `Ferrous citrate`; the source ingredient identity needs to be resolved before grounding or finalizing this row.
- Major: the same JCM 592 medium is maintained twice and generated twice, once through TOGO `M597` and once through MediaDive `J592`.

## Recommended Edits

- Fix TOGO unit normalization so source `mg`, `g`, `L`, and `ml` values are converted intentionally rather than copied numerically into `G_PER_L`.
- Represent the Trace mineral solution, Trace vitamins, and 5% NaHCO3 solution rows as milliliter additions under `solutions`, preserving their JCM cross-references where available.
- Reconcile the ferric-citrate versus ferrous-citrate source discrepancy against JCM `GRMD=592` before changing the ingredient label or grounding.
- Merge or explicitly cross-link the TOGO `M597` and MediaDive `J592` maintained records before regeneration so JCM `GRMD=592` has one CultureMech identity.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validation after TOGO unit handling and source identity are corrected.
- Compare the regenerated TOGO and MediaDive branches for JCM 592 row by row, especially the 1 mg trace salts, the 20 ml sodium bicarbonate solution, and the citrate row.
- Confirm that generated YAML no longer contains both `modified_mmjs_medium_b.yaml` and `modified_mmjs_medium_b__2b3d6f4c.yaml` as separate records for the same JCM recipe.

## Additional Notes

None found.
