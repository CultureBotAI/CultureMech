# YAML Record Review: desulfotomaculum_pbe_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/desulfotomaculum_pbe_medium__4b51f416.yaml
- Started UTC: 2026-09-22T20:16:31Z
- Finished UTC: 2026-09-22T20:18:42Z
- Verdict: needs curation

## Target

Generated MediaRecipe `CultureMech:002894`, `desulfotomaculum_pbe_medium`, from JCM medium J547 through MediaDive.

The generated record has `media_term.id` `mediadive.medium:J547` and links to the JCM 547 recipe.

## Validation

- LinkML open validation: passed.
- Strict validation: passed with 0 errors.
- LinkML reference validation: passed with 0 checks.
- LinkML term validation: passed.
- Embedded history validation: Not checked: the repository history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged records.

## Identity and Grounding

The lead MediaDive identity is JCM 547, `DESULFOTOMACULUM PBE MEDIUM`.

The same JCM 547 source is represented by TOGO M549. The current normalized MediaDive and TOGO records both contain September 2026 repair curation that resolves TOGO M549 as a source duplicate of MediaDive J547, but this generated record predates that repair and emits only the old MediaDive import.

## Evidence

The JCM 547 page describes `Solution A` with peptone, beef extract, MgSO4 x 7H2O, Na2SO4, CaCl2, and 900 ml distilled water, then instructs autoclaving Solution A under N2.

JCM then adds four solutions to complete the medium: 10 ml of 5% K2HPO4 solution, 70 ml of 5% sodium lactate, 10 ml of 4% Fe(NH4)2(SO4)2 x 6H2O solution, and 10 ml of 1% sodium ascorbate solution.

The generated YAML drops the 900 ml water row and emits `K2HPO4`, `Sodium lactate`, `Fe(NH4)2(SO4)2 x 6 H2O`, and `Sodium ascorbate` as top-level `G_PER_L` rows with concentrations `10`, `70`, `10`, and `10`. Those numbers are milliliter stock additions, not final solute masses.

## Completeness

The generated record preserves the JCM 547 identity and the two source preparation sentences.

It does not preserve the actual medium structure. `Solution A` water is absent, the four completion stocks are flattened, and the generated record has no `solutions` block for the K2HPO4, lactate, iron ammonium sulfate, or sodium ascorbate additions.

## Findings

1. **Four solution additions were copied as gram-per-liter final rows.**

   JCM 547 adds 10 ml 5% K2HPO4, 70 ml 5% sodium lactate, 10 ml 4% Fe(NH4)2(SO4)2 x 6H2O, and 10 ml 1% sodium ascorbate. The generated target stores those addition volumes as `10`, `70`, `10`, and `10` `G_PER_L`, which materially overstates the final formula.

2. **Solution A is not modeled.**

   The source explicitly names Solution A, but the generated record has no Solution A container and omits its 900 ml distilled-water row.

3. **The generated output is stale relative to repaired normalized YAML.**

   `data/normalized_yaml/bacterial/desulfotomaculum_pbe_medium.yaml` already models the 5% K2HPO4, 5% sodium lactate, 4% iron ammonium sulfate, and 1% sodium ascorbate additions as structured solutions. It also links TOGO M549 as a source duplicate and notes that no final pH is reported. None of that September 2026 repair is present in this generated YAML.

4. **Medium type and composition type are stale.**

   The generated record still declares `medium_type: DEFINED` and `composition_type: DEFINED` even though the repaired normalized source treats the peptone/beef-extract medium as complex and undefined.

## Recommended Edits

Regenerate merged YAML from the current normalized MediaDive J547 and TOGO M549 sources. The upstream normalized files already contain the structured stock additions and source-duplicate relationship needed for this record.

Confirm that the regenerated output keeps K2HPO4, sodium lactate, iron ammonium sulfate, and sodium ascorbate under `solutions` with `ML_PER_L` addition volumes and `PERCENT_W_V` stock compositions.

Restore the 900 ml Solution A water row and retain the repaired complex/undefined medium classification.

## Follow-up Checks

Compare the regenerated record against JCM 547, MediaDive J547, and TOGO M549 and verify that the MediaDive and TOGO paths collapse into one canonical record.

Check that no `10` or `70` `G_PER_L` rows remain for the four completion stocks.

Run the focused LinkML open, strict, reference, and term validators on the regenerated record.

## Additional Notes

No source YAML was edited during this review. Exact local searches for the PBE medium included ignored files.
