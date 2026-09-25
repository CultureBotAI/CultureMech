# YAML Record Review: Complete Chemically-defined Medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/complete_chemically_defined_medium.yaml`
- Started UTC: 2026-09-22T11:18:00Z
- Finished UTC: 2026-09-22T11:21:23Z
- Verdict: pass with minor issues

## Target

- Generated record: `CultureMech:007222`
- Normalized source: `data/normalized_yaml/bacterial/complete_chemically_defined_medium.yaml`
- Source identity: MediaDB Medium 322, `Complete Chemically-defined Medium`
- Current generated merge: one source recipe, `complete_chemically_defined_medium`

## Validation

- Open schema validation: pass.
- Strict validation: pass.
- Reference validation: pass with 0 checks.
- Term validation: pass.
- Embedded `curation_history`: not checked by the standalone history validator.

## Identity and Grounding

- MediaDB Medium 322 is a complete, nonminimal chemically defined liquid medium.
- The MediaDB HTML and tab-delimited endpoints both list 51 compounds in millimolar units.
- The generated record contains 51 ingredients and preserves the source concentrations.
- A gitignore-independent search over `data` found no same-name or same-identifier duplicate YAML records.

## Evidence

- MediaDB HTML checked: `https://mediadb.systemsbiology.net/defined_media/media/322/`.
- MediaDB tab-delimited export checked: `https://mediadb.systemsbiology.net/defined_media/media_text/322/`.
- MediaDB source page checked: `https://mediadb.systemsbiology.net/defined_media/sources/133/`.
- Local normalized owner checked: `data/normalized_yaml/bacterial/complete_chemically_defined_medium.yaml`.

## Completeness

- The bacterial category, defined medium type, defined composition type, and liquid physical state are appropriate.
- All 51 MediaDB compounds are represented with the MediaDB millimolar values.
- The preparation steps are generic import scaffolding rather than source-specific instructions, but they do not contradict the source.

## Findings

1. The generated record is stale relative to the normalized owner: the owner has an August 20, 2026 `apply_mim_groundings.py` event that grounded five ingredients from MIM exact matches, but the August 6 generated record still lacks those terms on `Adenine`, `Aspartate`, `Lysine`, `Ascorbate`, and `Threonine`.
2. The generated and normalized notes cite the MediaDB database URL but do not capture the underlying recipe citation, Letort C et al. 2001 in Journal of Applied Microbiology, exposed by MediaDB source 133.

## Recommended Edits

1. Regenerate this record from `data/normalized_yaml/bacterial/complete_chemically_defined_medium.yaml` so the five August 2026 MIM groundings appear in generated output.
2. Add the exact MediaDB source 133 / PMID 11851809 citation to the normalized record's evidence metadata.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Diff the regenerated ingredient names and millimolar concentrations against MediaDB `media_text/322`.
- Confirm the five post-August 6 ontology terms are present on the regenerated ingredients.

## Additional Notes

- No ingredient-count, concentration, duplicate, or physical-state defect was found.
- The remaining issues are provenance and stale generated ontology mappings.
