# YAML Record Review: halomonas_beimenensis_medium__32b4910e

- Repository: CultureMech
- Record: `data/merge_yaml/merged/halomonas_beimenensis_medium__32b4910e.yaml`
- Started UTC: 2026-09-23T10:29:40Z
- Finished UTC: 2026-09-23T10:30:31Z
- Verdict: needs curation

## Target

Generated merged YAML for the direct MediaDive/JCM import of JCM medium 771, `HALOMONAS BEIMENENSIS MEDIUM`.

## Validation

- LinkML validation: passed for target class `MediaRecipe`.
- Strict validation: passed; `/private/tmp/halomonas_beimenensis_medium__32b4910e.strict.tsv` contained only the header row.
- Reference validation: passed with 0 checked references.
- Term validation: passed.
- Embedded history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The record identity matches MediaDive `mediadive.medium:J771` and JCM medium 771.
- An ignored-file-inclusive exact search for the JCM 771 source found the direct JCM import, the related TOGO `M799` and `M800` parses, and one unrelated KG-Microbe match pointer.
- `Casamino acids` is correctly ungrounded as a mixture, and the simple salt groundings are appropriate.
- `Trisodium citrate` is grounded to generic sodium citrate; this should be checked during curation.

## Evidence

- The JCM page and the MediaDive J771 REST payload list 5 g Casamino acids with `BD-Difco`, 5 g Yeast extract with `BD-Difco`, 1 g Na glutamate, 3 g Trisodium citrate, 5 g MgSO4 x 7 H2O, 2 g KCl, and 50 g NaCl.
- JCM instructs preparation in distilled water to a 1.0 L final volume and states that 18.0 g/L agar is added for solid medium.
- TOGO `M799` parses the liquid base and TOGO `M800` parses the 18 g/L agar solid variant.

## Completeness

- Missing ingredient: distilled water is explicit in the source preparation instruction but absent from the direct generated record.
- Missing qualifiers: the `BD-Difco` attributes on Casamino acids and Yeast extract were dropped.
- The solid-medium agar instruction is stored as a plain `MIX` step on a `LIQUID` recipe instead of a variant relationship to the solid agar form.
- Missing default JCM autoclaving.

## Findings

1. The direct liquid record omits distilled water and the final 1.0 L volume as structured data.
2. `BD-Difco` was lost from both Casamino acids and Yeast extract.
3. The 18.0 g/L agar sentence is unconditional in `preparation_steps` even though it only applies to the solid form of the medium.
4. The direct JCM recipe is split from its TOGO liquid and solid parses.

## Recommended Edits

- Add the 1.0 L distilled-water final-volume ingredient or equivalent curated solvent structure.
- Restore `BD-Difco` on Casamino acids and Yeast extract.
- Keep this record as the liquid JCM 771 base and link the agar form as the 18 g/L solid variant.
- Add JCM default autoclaving semantics.
- Check whether trisodium citrate can be grounded more specifically than generic sodium citrate.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation after curation.
- Verify that the liquid base has no required agar row and that the solid variant keeps 18.0 g/L agar.
- Re-run an ignored-file-inclusive exact search for `mediadive.medium:J771`, `TOGO:M799`, and `TOGO:M800` after regeneration.

## Additional Notes

- Empty optional fields were not treated as defects.
- Exact local searches used `rg --no-ignore --hidden`, so ignored files were included.
