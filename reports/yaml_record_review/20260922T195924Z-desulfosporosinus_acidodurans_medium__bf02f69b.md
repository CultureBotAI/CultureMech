# YAML Record Review: desulfosporosinus_acidodurans_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/desulfosporosinus_acidodurans_medium__bf02f69b.yaml
- Started UTC: 2026-09-22T19:55:32Z
- Finished UTC: 2026-09-22T19:59:24Z
- Verdict: needs curation

## Target

Generated MediaRecipe `CultureMech:003347`, `desulfosporosinus_acidodurans_medium`, from MediaDive/JCM medium J998.

The generated record is a merged derivative of `data/normalized_yaml/bacterial/desulfosporosinus_acidodurans_medium.yaml`; it carries `media_term.id` `mediadive.medium:J998` and a source link to the JCM 998 recipe.

## Validation

- LinkML open validation: passed.
- Strict validation: passed with 0 errors.
- LinkML reference validation: passed with 0 checks.
- LinkML term validation: passed.
- Embedded history validation: Not checked: the repository history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged records.

## Identity and Grounding

The record is grounded to JCM 998 through MediaDive. Its top-level salts, yeast extract, and resazurin correspond to the JCM formula after MediaDive normalizes the 1 L base solution plus three 10 ml post-autoclave additions and two 1 ml stock additions to a 1032 ml final volume.

The same JCM 998 source family is split across generated records:

- `DESULFOSPOROSINUS_ACIDODURANS_MEDIUM.yaml`, derived from TOGO M1053 / JCM_M998, represents the base JCM 998 formula.
- `desulfosporosinus_acidodurans_medium__6b582775.yaml`, derived from TOGO M1054 / JCM_M998-2, represents the 10 g/L iron-powder variant.
- this MediaDive J998 record blends the base medium with the JCM strain note for the iron-powder variant: it preserves the pH 2.5 / iron-powder comment but omits the 10 g/L iron powder ingredient.

That split should be resolved before this generated record is treated as canonical. Otherwise CultureMech exposes duplicate base-medium identities and one partially represented variant for the same JCM recipe family.

## Evidence

The JCM 998 page and the MediaDive J998 REST payload both show a base formula containing sulfate/phosphate salts, yeast extract, resazurin, 1 ml FeCl2 solution, and 1 ml trace element solution in 1 L water. They then add 10 ml of 5% glycerin, 10 ml trace vitamins, and 10 ml of 5% L-cysteine hydrochloride after autoclaving.

MediaDive resolves the referenced FeCl2, trace element, and trace vitamins stocks as separate solution records. The generated merged YAML has no `solutions` block, and instead lifts those nested stock constituents to top-level `ingredients`.

The JCM page also instructs adding 10.0 g iron powder per liter for strains JCM 32882 and JCM 32883. The generated record retains this instruction only as a preparation comment and has no iron powder ingredient.

## Completeness

Substantial source semantics are missing or misplaced.

The generated record preserves the main-solution salts and the human-readable preparation text, but it does not preserve the stock-solution topology. The FeCl2, trace element, and trace vitamin formulas are flattened into top-level formula rows, so the 1 ml and 10 ml stock additions cannot be distinguished from grams per liter in the final medium.

The two 10 ml additions of 5% glycerin and 5% L-cysteine hydrochloride monohydrate are also modeled as `10` `G_PER_L` top-level rows. Those values are source addition volumes, not final solute concentrations.

## Findings

1. **Nested stocks are flattened into the final medium.**

   The generated record has top-level rows for FeCl2 stock acid/base constituents, trace element stock constituents, and ten trace vitamin compounds. These belong in nested stock solutions that are added at 1 ml or 10 ml to the JCM 998 main medium. As generated, a consumer would read the stock concentrations as final grams per liter.

2. **Post-autoclave 10 ml additions became 10 g/L ingredient quantities.**

   `Glycerin` and `L-Cysteine HCl x H2O` each have `amount: 10` and `unit: G_PER_L`, matching the source milliliter addition volumes. The source additions are 10 ml of 5% stock solutions, so both ingredient amounts are materially overstated.

3. **The iron-powder variant is incomplete.**

   The record includes the JCM comment for strains JCM 32882 and JCM 32883 but lacks the required 10.0 g/L iron powder row. If this MediaDive import is meant to represent the base JCM 998 medium, the strain-specific pH 2.5 / iron-powder comment does not belong at top level. If it is meant to represent the variant, iron powder must be modeled explicitly.

4. **JCM 998 identities are duplicated across import providers.**

   TOGO M1053 and MediaDive J998 both describe the base JCM 998 recipe, while TOGO M1054 describes the JCM M998-2 iron-powder variant. The generated records are not cross-linked, so exact and near-exact duplicates are visible under different CultureMech IDs.

## Recommended Edits

Rebuild the normalized J998 import so referenced FeCl2, trace element, and trace vitamins formulas are nested under `solutions` with explicit 1 ml or 10 ml additions from the main recipe.

Represent the two 10 ml 5% additions as solution additions, or convert their final concentrations from the underlying 5% stock concentration and addition volume.

Separate the base JCM 998 medium from the iron-powder variant. Add 10.0 g/L iron powder to the variant record and associate the pH 2.5 instruction with that variant, not unqualified base JCM 998.

Add cross-provider equivalence links between MediaDive J998, TOGO M1053, TOGO M1054, and the JCM recipe identifiers so the merge can collapse exact duplicates while keeping the iron-powder variant distinct.

## Follow-up Checks

After curation, compare the regenerated merged YAML against both the JCM 998 page and the MediaDive J998 REST payload and confirm that no stock ingredient is present in the final formula unless the source itself supplies a final-medium concentration.

Regenerate the duplicate M1053, M1054, and J998 outputs together and verify that the base and variant are each represented once.

Run the focused LinkML open, strict, reference, and term validators on the regenerated record.

## Additional Notes

No source YAML was edited during this review. The defects above are importer or merge artifacts in generated output, not validation failures in the current schema.
