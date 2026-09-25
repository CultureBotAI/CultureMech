# YAML Record Review: fermentation_medium_pyruvate_nh4cl

- Repository: CultureMech
- Record: data/merge_yaml/merged/fermentation_medium_pyruvate_nh4cl.yaml
- Started UTC: 2026-09-23T02:44:38Z
- Finished UTC: 2026-09-23T02:45:28Z
- Verdict: pass with minor issues

## Target

CultureMech:007260 is the generated merged record for MediaDB 359, `Fermentation medium (pyruvate+nh4cl)`.

MediaDB 359 lists nine compounds: ammonium chloride 130.9 mM, biotin 0.0001228 mM, magnesium sulfate 3.246 mM, nicotinate 0.09747 mM, potassium dihydrogen phosphate 36.74 mM, pyridoxine HCl 0.001459 mM, pyruvate 111.0 mM, riboflavin 0.0003986 mM, and thiamine HCl 0.0001334 mM. It is associated with `Candida glabrata CTCC M202019` and Source 124, `Xu n et al, 2013`.

## Validation

- LinkML open-schema validation: pass; `linkml-validate` reported `No issues found`.
- Strict schema validation: pass; `scripts/validate_strict.py` exited 0 and the TSV contained only the header row.
- Reference validation: pass; the reference validator scanned the file and reported 0 checks.
- Term validation: pass; `linkml-term-validator` exited 0 and reported `Validation passed`.
- Embedded `curation_history`: Not checked: `just validate-history` validates standalone files under `history/`, not embedded history entries in generated MediaRecipe YAML.

## Identity and Grounding

The CultureMech identifier, normalized name, category, defined/liquid typing, ingredient list, concentrations, and MediaDB identifier point to the intended MediaDB 359 recipe.

The generated `original_name` and `media_term.term.label` are stale. `data/normalized_yaml/bacterial/fermentation_medium_pyruvate_nh4cl.yaml` has already restored both fields to `Fermentation Medium (Pyruvate+NH4Cl)` via the 2026-08-31 `repair_mediadb_names.py` pass, while the generated merge still stores the truncated `'''Fermentation Medium (Pyruvate+NH4Cl`.

All nine ingredients carry CHEBI term grounding in the generated record.

## Evidence

The generated ingredient list is composition-complete for MediaDB 359. Ammonium chloride, biotin, magnesium sulfate, nicotinate, potassium dihydrogen phosphate, pyridoxine HCl, pyruvate, riboflavin, and thiamine HCl all retain the same millimolar amounts shown on the source page.

MediaDB 359 exposes Source 124, `Xu n et al, 2013`; the CultureMech source record only carries the generic MediaDB homepage plus an import-history note naming `Mazumdar et al. (2014) PLOS One`.

## Completeness

The generated record has all nine MediaDB 359 ingredients, no extra ingredients, and all nine ingredient-level CHEBI terms.

External source provenance is incomplete because MediaDB Source 124 is not materialized.

## Findings

1. The generated merge was built from the pre-repair MediaDB medium labels; the normalized YAML was repaired on 2026-08-31, but the generated `original_name` and `media_term.term.label` are still truncated.
2. MediaDB Source 124 is absent, leaving only the generic MediaDB URL and an import-history note that does not match the source label shown on the MediaDB 359 page.

## Recommended Edits

1. Regenerate the merge from the repaired normalized source so the generated `original_name` and `media_term.term.label` become `Fermentation Medium (Pyruvate+NH4Cl)`.
2. Preserve or materialize MediaDB Source 124 for this imported recipe.

## Follow-up Checks

- Re-run open-schema, strict-schema, reference, and term validation after regenerating the merge.
- Confirm an ignored-inclusive exact search for `Fermentation Medium (Pyruvate+NH4Cl)` finds the repaired label in the generated merge.
- Confirm the generated merge remains at nine ingredients and that all nine MediaDB 359 amounts still match the source page.

## Additional Notes

The exact search for `Fermentation Medium (Pyruvate+NH4Cl)` included ignored files by using `rg --no-ignore --hidden` over the reviewed data and report paths.
