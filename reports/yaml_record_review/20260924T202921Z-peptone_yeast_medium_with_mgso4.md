# YAML Record Review: peptone_yeast_medium_with_mgso4

- Repository: CultureMech
- Record: data/merge_yaml/merged/peptone_yeast_medium_with_mgso4.yaml
- Started UTC: 2026-09-24T20:29:21Z
- Finished UTC: 2026-09-24T20:29:21Z
- Verdict: pass with minor issues

## Target

Generated cross-category MediaRecipe `CultureMech:006497`, `peptone_yeast_medium_with_mgso4`, merged from `data/normalized_yaml/bacterial/peptone_yeast_medium_with_mgso4.yaml` and `data/normalized_yaml/fungal/peptone_yeast_medium_with_mgso4.yaml`.

The record represents KOMODO medium 790 as a source duplicate of DSMZ / MediaDive medium 790, PEPTONE-YEAST MEDIUM with MgSO4. The generated recipe has 10 g/L peptone, 1 g/L dehydrated yeast extract, 2 g/L MgSO4 x 7 H2O, and 2 g/L ammonium sulfate, with pH 7.0.

## Validation

- Open LinkML validation: Passed with no issues.
- Strict validator: Passed; `/private/tmp/peptone_yeast_medium_with_mgso4.strict.tsv` was header-only, so there were 0 strict errors.
- Reference validation: Passed; 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not embedded `MediaRecipe.curation_history`.

## Identity and Grounding

The source-duplicate merge is sound. The bacterial owner explicitly cites KOMODO 790 and DSMZ / `mediadive.medium:790`, while the fungal owner is a direct MediaDive/DSMZ 790 import with the same physical state, pH, ingredients, and concentrations.

The duplicate search found specialized PYE no-calcium records with `kg_microbe_match: mediadive.medium:790`, but a local repair script explicitly marks that NBRC 219 match as false. Those are KG cross-references, not duplicate MediaRecipe owners for DSMZ medium 790.

## Evidence

MediaDive medium 790 supports the DSMZ source identity, pH 7.0, 10 g peptone, 1 g dehydrated yeast extract, 2 g MgSO4 x 7 H2O, 2 g ammonium sulfate, and 1000 ml distilled water in a 1 L recipe.

The linked DSMZ medium 790 PDF agrees on the four non-water components, the 1000 ml distilled water row, and pH adjustment to 7.0.

The ingredient grounding is appropriate: magnesium sulfate heptahydrate and ammonium sulfate have specific CHEBI terms, while peptone and dehydrated yeast extract remain ungrounded as complex undefined ingredients.

## Completeness

The merge preserves both category owners, the non-water ingredients, pH 7.0, and the expected source-duplicate relationship.

Both maintained inputs omit the 1000 ml distilled water row, and the generated merge uses the bacterial KOMODO owner as canonical, so it drops the fungal DSMZ owner's `Adjust pH to 7.0` preparation step even though the scalar `ph_value` is present.

## Findings

1. Minor issue: both maintained owners and the generated record omit the 1000 ml `Distilled water` row from DSMZ / MediaDive medium 790.
2. Minor issue: the generated merge drops the direct DSMZ owner's `Adjust pH to 7.0` preparation step; `ph_value: 7.0` is still preserved.

## Recommended Edits

1. Add the 1000 ml distilled water row to both maintained owners.
2. Preserve the DSMZ pH-adjustment preparation step when regenerating the KOMODO / DSMZ source-duplicate merge.

## Follow-up Checks

1. Re-run open, strict, reference, and term validation on the repaired maintained owners and regenerated merged record.
2. Repeat an exact ignored-inclusive search for `komodo.medium:790`, `mediadive.medium:790`, `DSMZ_Medium790`, and the two CultureMech IDs to confirm DSMZ medium 790 is represented only by the intended merged record and false KG cross-references.

## Additional Notes

The exact ignored-inclusive duplicate searches covered `data`, `src`, and `scripts` for `komodo.medium:790`, `mediadive.medium:790`, `DSMZ Medium: 790`, `DSMZ_Medium790`, `CultureMech:006497`, and `CultureMech:010477`.
