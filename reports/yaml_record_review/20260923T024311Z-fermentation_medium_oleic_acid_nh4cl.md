# YAML Record Review: fermentation_medium_oleic_acid_nh4cl

- Repository: CultureMech
- Record: data/merge_yaml/merged/fermentation_medium_oleic_acid_nh4cl.yaml
- Started UTC: 2026-09-23T02:41:55Z
- Finished UTC: 2026-09-23T02:43:11Z
- Verdict: needs curation

## Target

CultureMech:007264 is the generated merged record for MediaDB 362, `Fermentation medium (oleic acid+nh4cl)`.

MediaDB 362 lists nine compounds: `(9Z)-Octadecenoic acid` 111.0 mM, ammonium chloride 130.9 mM, biotin 0.0001228 mM, magnesium sulfate 3.246 mM, nicotinate 0.09747 mM, potassium dihydrogen phosphate 36.74 mM, pyridoxine HCl 0.001459 mM, riboflavin 0.0003986 mM, and thiamine HCl 0.0001334 mM. It is associated with `Candida glabrata CTCC M202019` and Source 124, `Xu n et al, 2013`.

## Validation

- LinkML open-schema validation: pass; `linkml-validate` reported `No issues found`.
- Strict schema validation: pass; `scripts/validate_strict.py` reported 0 files with errors and 0 total error rows.
- Reference validation: pass; the reference validator scanned the file and reported 0 checks.
- Term validation: pass; `linkml-term-validator` exited 0 and reported `Validation passed`.
- Embedded `curation_history`: Not checked: `just validate-history` validates standalone files under `history/`, not embedded history entries in generated MediaRecipe YAML.

## Identity and Grounding

The CultureMech identifier, normalized name, medium category, defined/liquid typing, and MediaDB identity all point to the intended source record.

The generated YAML is stale relative to its normalized source. `data/normalized_yaml/bacterial/fermentation_medium_oleic_acid_nh4cl.yaml` has already restored the medium's own `original_name` and `media_term.term.label` and the first ingredient name via the 2026-08-31 `repair_mediadb_names.py` pass; the generated merge still has `'''Fermentation Medium (Oleic acid+NH4Cl` and `'''(9Z`.

Eight of nine generated ingredients carry a CHEBI term where the source names are chemically specific. `(9Z)-Octadecenoic acid` has no `term` or `mediaingredientmech_chebi_term` in either the normalized source or the generated merge. MediaDB compound 659 exposes `CHEBI:16196`, `KEGG:C00712`, and `SEED:cpd00536` for this compound, and an exact ignored-inclusive search found `CHEBI:16196` reused elsewhere in local YAML records, so the missing oleic-acid grounding is not a novel entity problem.

## Evidence

The generated ingredient list preserves all nine MediaDB 362 amounts, but the oleic-acid ingredient is damaged by stale MediaDB SQL parsing. MediaDB lists `(9Z)-Octadecenoic acid` at 111.0 mM; the normalized source now stores the same preferred term; the generated merge stores only `'''(9Z`, which is not a valid ingredient label.

The other eight generated amounts match MediaDB 362: ammonium chloride 130.9 mM, biotin 0.0001228 mM, magnesium sulfate 3.246 mM, nicotinate 0.09747 mM, potassium dihydrogen phosphate 36.74 mM, pyridoxine HCl 0.001459 mM, riboflavin 0.0003986 mM, and thiamine HCl 0.0001334 mM.

MediaDB 362 exposes Source 124, `Xu n et al, 2013`; the CultureMech source record only carries the generic MediaDB homepage plus an import-history note naming `Mazumdar et al. (2014) PLOS One`.

## Completeness

The generated record is composition-complete for the MediaDB 362 compound list and has no extra ingredients.

Grounding is incomplete for `(9Z)-Octadecenoic acid`, and external source provenance is incomplete because MediaDB Source 124 is not materialized.

## Findings

1. The generated merge was built from pre-repair MediaDB names. The source YAML under `data/normalized_yaml` was repaired on 2026-08-31, but `data/merge_yaml/merged/fermentation_medium_oleic_acid_nh4cl.yaml` still truncates the medium label and the first ingredient at a parenthesis.
2. `(9Z)-Octadecenoic acid` is ungrounded despite MediaDB compound 659 exposing `CHEBI:16196`, `KEGG:C00712`, and `SEED:cpd00536`; an exact ignored-inclusive search found local CHEBI:16196 reuse in other YAML records.
3. MediaDB Source 124 is absent, leaving only the generic MediaDB URL and an import-history note that does not match the source label shown on the MediaDB 362 page.

## Recommended Edits

1. Regenerate the merge from the repaired normalized source so `original_name`, `media_term.term.label`, and the first ingredient become `Fermentation Medium (Oleic acid+NH4Cl)` and `(9Z)-Octadecenoic acid`.
2. Ground `(9Z)-Octadecenoic acid` to `CHEBI:16196` and add the matching `mediaingredientmech_chebi_term` link.
3. Preserve or materialize MediaDB Source 124 for this imported recipe.

## Follow-up Checks

- Re-run open-schema, strict-schema, reference, and term validation after regenerating the merge.
- Confirm an ignored-inclusive exact search for the repaired label no longer finds `'''(9Z` in `data/merge_yaml/merged/fermentation_medium_oleic_acid_nh4cl.yaml`.
- Confirm the generated merge remains at nine ingredients and that all nine MediaDB 362 amounts still match the source page.

## Additional Notes

The exact search for `(9Z)-Octadecenoic acid`, `MEDIADB:362`, and `CHEBI:16196` included ignored files by using `rg --no-ignore --hidden` over the reviewed data and report paths.
