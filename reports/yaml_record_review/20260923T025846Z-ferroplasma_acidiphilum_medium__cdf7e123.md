# YAML Record Review: ferroplasma_acidiphilum_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/ferroplasma_acidiphilum_medium__cdf7e123.yaml
- Started UTC: 2026-09-23T02:57:41Z
- Finished UTC: 2026-09-23T02:58:46Z
- Verdict: needs curation

## Target

CultureMech:009328 is the generated merged record for TOGO Medium M277, `Ferroplasma Acidiphilum Medium`, whose original source is JCM Medium 283.

JCM 283 lists MgSO4 x 7 H2O 0.4 g, ammonium sulfate 0.2 g, KCl 0.1 g, K2HPO4 0.1 g, FeSO4 x 7 H2O 25.0 g, yeast extract 0.16 g, and 1.0 L distilled water. The recipe adjusts pH to 1.6-1.8 with H2SO4, filter-sterilizes the base, and adds yeast extract later as an autoclaved 10% solution.

## Validation

- LinkML open-schema validation: pass; `linkml-validate` reported `No issues found`.
- Strict schema validation: pass; `scripts/validate_strict.py` reported 0 files with errors and 0 total error rows.
- Reference validation: pass; the reference validator scanned the file and reported 0 checks.
- Term validation: pass; `linkml-term-validator` exited 0 and reported `Validation passed`.
- Embedded `curation_history`: Not checked: `just validate-history` validates standalone files under `history/`, not embedded history entries in generated MediaRecipe YAML.

## Identity and Grounding

The CultureMech identifier, normalized name, `TOGO:M277` medium term, original JCM 283 URL, and archaeal/liquid typing identify the intended recipe.

The generated ingredient amounts match the Togo M277 payload and the JCM 283 source table. `Yeast extract (BD-Difco)` is an undefined component, so the lack of a single-compound CHEBI grounding is appropriate.

Two chemically specific hydrated salts, `MgSO4 x 7 H2O` and `FeSO4 x 7 H2O`, have primary CHEBI terms but no `mediaingredientmech_chebi_term` links.

## Evidence

Togo M277 carries pH `1.6-1.8` in its metadata and JCM 283 carries the same pH target in its preparation sentence. The generated CultureMech record has no `ph_value` or `ph_range`.

The Togo and JCM source instructions say to mix all ingredients except yeast extract, adjust with H2SO4, filter-sterilize, and add yeast extract before use as an autoclaved 10% solution. The generated record has no `preparation_steps`; it only retains H2SO4 as a variable-concentration ingredient.

The generated ingredient list retains the seven tabular JCM components plus H2SO4 for adjustment. The `Distilled water` entry keeps the source `1 L` quantity as `1 G_PER_L`, which is a unit artifact from the Togo importer rather than a useful concentration.

## Completeness

The generated record is composition-complete for the JCM 283 ingredient table, with H2SO4 added as the pH-adjustment solution.

The record is not recipe-complete because pH 1.6-1.8 and the filter-sterilization / delayed yeast-extract addition are absent.

## Findings

1. The source pH range 1.6-1.8 was not migrated into `ph_range`.
2. The source preparation instruction is missing, so the record no longer states when to add yeast extract or how to sterilize the base.
3. `MgSO4 x 7 H2O` and `FeSO4 x 7 H2O` are missing MediaIngredientMech CHEBI links even though their primary CHEBI terms are present.
4. `Distilled water` is represented as `1 G_PER_L`, reflecting a source volume rather than a meaningful gram-per-liter concentration.

## Recommended Edits

1. Restore the Togo/JCM pH range as `min: 1.6`, `max: 1.8`.
2. Add a preparation step that preserves the source instruction to omit yeast extract before pH adjustment and filter sterilization, then add yeast extract as an autoclaved 10% solution before use.
3. Add MediaIngredientMech CHEBI links for magnesium sulfate heptahydrate and iron(2+) sulfate heptahydrate if corresponding ingredient records exist.
4. Reconsider whether the water row should be retained, removed, or represented as a volume instead of `1 G_PER_L`.

## Follow-up Checks

- Re-run open-schema, strict-schema, reference, and term validation after adding pH and preparation metadata.
- Confirm the post-fix record still points to `TOGO:M277` and the JCM 283 URL.
- Confirm the six non-water masses still match JCM 283.

## Additional Notes

None found.
