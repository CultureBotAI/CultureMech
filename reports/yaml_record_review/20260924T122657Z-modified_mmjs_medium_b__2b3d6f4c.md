# YAML Record Review: modified_mmjs_medium_b

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_mmjs_medium_b__2b3d6f4c.yaml
- Started UTC: 2026-09-24T12:26:57Z
- Finished UTC: 2026-09-24T12:26:57Z
- Verdict: needs curation

## Target

- Reviewed merged record `CultureMech:002940`, `modified_mmjs_medium_b`, generated from the MediaDive records `data/normalized_yaml/bacterial/modified_mmjs_medium_b.yaml` and `data/normalized_yaml/bacterial/mmmjs_pt.yaml`.
- The primary generated record represents JCM Medium J592 / MediaDive `mediadive.medium:J592`, named `MODIFIED MMJS MEDIUM (B)`.
- The merge also folded in `mmmjs_pt`, MediaDive `mediadive.medium:J603`, as a source duplicate.

## Validation

- LinkML open-schema validation: passed; `linkml-validate` exited 0 with `No issues found`.
- Strict validation: passed; `scripts/validate_strict.py` reported 1 file scanned, 0 files with errors, and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` checked 1 file and reported 0 reference checks and no failures.
- Term validation: passed; `linkml-term-validator` exited 0 and printed `Validation passed`.
- Embedded `curation_history` entries were not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- MediaDive `J592`, JCM `GRMD=592`, and TOGO `M597` identify the same Modified MMJS Medium (B) source recipe.
- A gitignore-independent duplicate check for the exact JCM/TOGO/MediaDive identifiers found `data/normalized_yaml/bacterial/TOGO_M597_Modified_MMJS_Medium_B.yaml` and the generated TOGO record `data/merge_yaml/merged/modified_mmjs_medium_b.yaml` as a second CultureMech representation of JCM 592.
- MediaDive `J603` / JCM `GRMD=603` is not a pure duplicate: JCM 603 starts with Medium No. 592 but adds 2.0 g/L yeast extract and changes the final N2-CO2-O2 gas mixture to 77:20:3 at 200 kPa.
- No inspected source payload identified a target organism for JCM 592 or JCM 603.

## Evidence

- JCM 592 lists Solution A with 1 L distilled water; the gram-scale salts; 1 mg NiCl2 x 6 H2O, 1 mg Na2SeO3 x 5 H2O, and 1 mg H2WO4; 0.01 g ferric citrate; 5 ml Trace mineral solution; then 1 ml Trace vitamins and 20 ml 5% NaHCO3 solution after autoclaving.
- MediaDive `J592` converts the Solution A mg rows into small gram-per-liter values such as `0.000974659` g/L for the nickel chloride, selenite, and tungstic-acid rows, which the generated record preserves.
- MediaDive `J592` carries the 5 ml Trace mineral solution as solution `4286` with a step saying to use the Trace mineral solution of Medium No. 413 with 0.01 g/L final Na2MoO4 x 2H2O.
- MediaDive `J592` carries the 1 ml Trace vitamins addition as solution `3861`, a 1000 ml stock recipe.
- JCM and MediaDive `J603` state only that mMMJS/PT uses Medium No. 592 supplemented with 2.0 g/L yeast extract and a changed final gas phase, but the generated merge has no yeast extract row.

## Completeness

- Main gram-scale and milligram-scale Solution A salts are present with MediaDive-computed gram-per-liter values.
- The 5 ml Trace mineral solution is missing as a structured solution addition; only the Medium No. 413 instruction remains in a preparation step, without the 5 ml amount.
- The 1 ml Trace vitamins addition is not preserved as a first-class addition; its stock components are flattened into the main ingredient list at stock strength.
- The 20 ml 5% NaHCO3 solution is represented as a `20` `G_PER_L` NaHCO3 row, not as a milliliter stock addition.
- The 1 L Solution A water row and the 1000 ml Trace vitamins water row are absent.
- The JCM 603 yeast extract supplement is absent despite `mmmjs_pt` being merged into this generated record.

## Findings

- Blocker: JCM 603 mMMJS/PT was collapsed into JCM 592 as a `SOURCE_DUPLICATE`, but JCM 603 adds 2.0 g/L yeast extract and uses a final N2-CO2-O2 gas mixture of 77:20:3. The generated merged record loses that variant-specific yeast extract and preserves only JCM 592 ingredients.
- Blocker: the 1 ml Trace vitamins stock from JCM 592 is flattened into top-level ingredients at 1 L stock strength. The generated vitamin rows are stock concentrations, not direct main-medium additions.
- Major: the 5 ml Trace mineral solution of JCM 592 is missing as a structured addition, so the generated YAML does not preserve the source amount even though the Medium No. 413 adjustment survives as a free-text step.
- Major: the 20 ml 5% NaHCO3 solution is stored as `20` `G_PER_L`, losing both the stock strength and the milliliter addition amount.
- Major: the current JCM 592 page lists `Ferric citrate`, while MediaDive and the generated record carry `Ferrous citrate`; the parsed source should be reconciled against the current JCM label.
- Major: the same JCM 592 medium is generated twice, once through MediaDive `J592` and once through TOGO `M597`.

## Recommended Edits

- Split `mmmjs_pt` / JCM 603 back out from the JCM 592 source duplicate and represent it as a variant that supplements Medium No. 592 with 2.0 g/L yeast extract and the 77:20:3 final gas mixture.
- Preserve the 5 ml Trace mineral solution and 1 ml Trace vitamins rows from JCM 592 as structured solution additions or nested stock recipes.
- Preserve the 20 ml 5% NaHCO3 solution as a volume stock addition, not a `20` `G_PER_L` compound row.
- Reconcile the ferric-citrate versus ferrous-citrate source discrepancy against JCM `GRMD=592`.
- Merge or explicitly cross-link MediaDive `J592` and TOGO `M597` so JCM `GRMD=592` has a single CultureMech identity after regeneration.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validation after correcting the false duplicate merge and nested-solution handling.
- Confirm that regenerated JCM 592 contains a structured 5 ml Trace mineral solution, a structured 1 ml Trace vitamins addition, and a structured 20 ml 5% NaHCO3 solution.
- Confirm that regenerated JCM 603 still contains the Medium No. 592 dependency plus 2.0 g/L yeast extract and is not merged away as an identical source.
- Confirm that generated YAML no longer contains separate MediaDive and TOGO records for JCM 592.

## Additional Notes

None found.
