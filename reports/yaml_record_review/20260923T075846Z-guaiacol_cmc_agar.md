# YAML Record Review: Guaiacol-CMC Agar

- Repository: CultureMech
- Record: `data/merge_yaml/merged/guaiacol_cmc_agar.yaml`
- Started UTC: 2026-09-23T07:57:30Z
- Finished UTC: 2026-09-23T07:58:46Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:008241`, `guaiacol_cmc_agar`, imported from Togo Medium `M1682` / `NBRC_M887`.

## Validation

- LinkML validation: passed.
- Strict validation: passed with 0 ERROR rows in `/private/tmp/guaiacol_cmc_agar.strict.tsv`.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded history validation: Not checked: the available `just validate-history` target validates standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The record identity is internally consistent: the normalized parent and generated record both carry Togo Medium `M1682`, `original_name: Guaiacol-CMC Agar`, and the NBRC `NBRC_M887` provenance in `notes`.

The generated record is stale relative to `data/normalized_yaml/bacterial/guaiacol_cmc_agar.yaml`: the normalized parent picked up a `CHEBI:28591` guaiacol grounding on 2026-08-20, but the generated record still leaves Guaiacol ungrounded.

## Evidence

The Togo API payload for `M1682` has a single main solution with 1 L distilled water, 0.1 g CM-Cellulose, 0.2 g Ammonium tartrate, 15 g Agar, 11.7 g Difco Yeast Carbon Base, and 0.1 g Guaiacol. Those ingredient names and nominal numeric values match the generated rows, apart from water unit conversion.

Togo also preserves `ph: "4.5"` in the medium metadata and repeats `pH 4.5` in comments. The generated record has no pH field or note carrying that target pH.

## Completeness

The six source ingredients are present, and the solid agar physical state is appropriate. Recipe completeness is still limited because the generated output drops the final pH and renders 1 L water as 1 g/L rather than as the solvent volume for the 1 L recipe.

## Findings

- The Togo source pH is missing. `M1682` reports pH 4.5 in both the `meta.ph` field and comments, but `guaiacol_cmc_agar.yaml` has no `pH` value or preparation note for the target pH.
- Distilled water is misunitized. Togo reports `Distilled water` as `1 L`; the generated row stores `value: '1'` with `unit: G_PER_L`, making a one-liter solvent addition read as a 1 g/L mass concentration.
- The generated record is stale relative to its parent. The source parent now grounds Guaiacol to `CHEBI:28591`, while the generated record omits that `term`.
- CM-Cellulose and Ammonium tartrate remain ungrounded simple components. These are not validation failures, but they should be checked against available ChEBI or MIM mappings during recuration.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/guaiacol_cmc_agar.yaml` from `data/normalized_yaml/bacterial/guaiacol_cmc_agar.yaml` so the existing Guaiacol grounding is preserved.
- Preserve the Togo `pH 4.5` value in the recipe during import or attach it as a preparation note if the schema does not support an explicit generated pH field.
- Correct water handling for Togo liter inputs so recipe water volumes are not emitted as `G_PER_L`.
- Attempt ontology grounding for CM-Cellulose and Ammonium tartrate.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validators after regenerating the record.
- Recompare regenerated ingredient rows against Togo `M1682` and verify that pH 4.5 is still visible in the CultureMech record.

## Additional Notes

No ignored files were needed to establish identity or deduplication for this record; exact scoped search of `data/normalized_yaml` and `data/merge_yaml/merged` was sufficient for the expected parent/generated pair.
