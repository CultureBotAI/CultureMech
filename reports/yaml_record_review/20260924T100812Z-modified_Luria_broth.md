# YAML Record Review: Modified Luria Broth

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_Luria_broth.yaml
- Started UTC: 2026-09-24T10:08:12Z
- Finished UTC: 2026-09-24T10:08:12Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Record | `data/merge_yaml/merged/modified_Luria_broth.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:009490` |
| Name | `modified_luria_broth` |
| Original name | `modified Luria broth` |
| Category | `bacterial` |
| Medium source | TOGO `M2966` |
| Maintained owner | `data/normalized_yaml/bacterial/modified_luria_broth.yaml` |
| Generated status | Stale generated merge output from one normalized TOGO record |

## Validation

| Check | Result |
| --- | --- |
| Open LinkML schema validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_Luria_broth.yaml` | Passed; exited 0 with "No issues found". |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/modified_Luria_broth.yaml --out /private/tmp/modified_Luria_broth.strict.tsv --workers 1 --quiet` | Passed; 0 strict errors were reported and `/private/tmp/modified_Luria_broth.strict.tsv` contained only the header line. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/modified_Luria_broth.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the focused run completed with 0 reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/modified_Luria_broth.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not inline `MediaRecipe.curation_history` entries in a merged YAML record. |

## Identity and Grounding

The generated record identity is coherent: `CultureMech:009490` and `TOGO:M2966` both identify the modified Luria broth formula imported by TOGO.

An exact `find data/normalized_yaml -name 'modified_luria_broth.yaml'` search, which does not honor gitignore exclusions, found `data/normalized_yaml/bacterial/modified_luria_broth.yaml` as the generated record's maintained owner.

The generated merge output is stale relative to a 2026-09-12 repair in that normalized owner. The maintained record now corrects the 1 L water row from `G_PER_L` to liters; grounds yeast extract, tryptone, and HEPES; cites the Mobley et al. DOI `10.1128/iai.58.5.1281-1289.1990`; and adds preparation steps for the pH 7.2 HEPES and 300 mosmol dilution context.

Crossref resolves DOI `10.1128/iai.58.5.1281-1289.1990` to Mobley et al. 1990, "Pyelonephritogenic Escherichia coli and killing of cultured human renal proximal tubular epithelial cells: role of hemolysin in some strains," in Infection and Immunity.

## Evidence

TOGO `M2966` supports the imported formula and includes a Mobley et al. passage with both formulation and growth context:

| Source claim | Record representation | Review |
| --- | --- | --- |
| The modified Luria broth formula is per liter: 10 g tryptone from Difco, 5 g yeast extract, 8.5 g NaCl, and 100 mM HEPES at pH 7.2. | The generated record contains 10 `G_PER_L` tryptone, 5 `G_PER_L` yeast extract, 8.5 `G_PER_L` NaCl, and 100 `MILLIMOLAR` for the source HEPES label. | Supported at the amount level, but generated HEPES remains an unguided long label and pH 7.2 is only embedded in that label. |
| The formula is made with 1 L distilled water. | Distilled water is stored as `1 G_PER_L`. | Unsupported final-volume import. |
| The solution was adjusted to 300 mosmol. | No osmolality or dilution step is represented in generated output. | Incomplete. |
| E. coli strains were grown at 37 C with aeration at 200 rpm in this modified Luria broth. | No target organism or incubation condition is represented. | Incomplete. |

## Completeness

All five TOGO ingredient rows are present in generated output with the right non-water numeric amounts, but the generated record is stale for source detail added to the normalized owner on 2026-09-12.

The record is incomplete as a representation of TOGO `M2966` because it drops the 300 mosmol osmolality adjustment and the extracted Escherichia coli 37 C aerated-growth context.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | The generated record is stale relative to the 2026-09-12 normalized repair. | The generated merge still stores `Distilled water` as `1 G_PER_L` and leaves yeast extract, HEPES, and tryptone ungrounded; the normalized owner has already corrected those values. | Regenerate from `data/normalized_yaml/bacterial/modified_luria_broth.yaml`. |
| major | Osmolality adjustment is absent. | The TOGO M2966 passage says the solution was adjusted to 300 mosmol by dilution; generated output has no osmolality condition or preparation step. | Already repaired in `data/normalized_yaml/bacterial/modified_luria_broth.yaml`; regenerate merge output. |
| major | E. coli growth context from the TOGO extract is absent. | TOGO M2966 states that E. coli cultures were grown at 37 C with aeration at 200 rpm in fresh modified Luria broth; the record has no target organism, temperature, aeration, or growth-evidence entry. | `data/normalized_yaml/bacterial/modified_luria_broth.yaml`; growth-evidence curation. |
| minor | HEPES pH 7.2 is only carried in the raw ingredient label in generated output. | The imported preferred term contains `[HEPES; pH 7.2]`, but generated output has no preparation note explaining that the 100 mM HEPES was at pH 7.2. | Already partly repaired in `data/normalized_yaml/bacterial/modified_luria_broth.yaml`; regenerate merge output. |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/modified_Luria_broth.yaml` so the 2026-09-12 repairs in `data/normalized_yaml/bacterial/modified_luria_broth.yaml` propagate to generated output.
2. Add a bounded target-organism or growth-evidence entry to `data/normalized_yaml/bacterial/modified_luria_broth.yaml` for the E. coli culture conditions in TOGO `M2966`, scoped to the source excerpt.
3. After regeneration, verify that water is represented as 1 L, HEPES is grounded to `CHEBI:42334`, tryptone and yeast extract are grounded, and the HEPES pH 7.2 plus 300 mosmol context remains represented.

## Follow-up Checks

1. Re-run focused open-schema, strict, reference, and term validators on `data/normalized_yaml/bacterial/modified_luria_broth.yaml` and the regenerated merge output.
2. Manually compare the regenerated record against TOGO `M2966`, checking the 10 g/L tryptone, 5 g/L yeast extract, 8.5 g/L NaCl, 100 mM HEPES, pH 7.2, 1 L water row, and 300 mosmol dilution.
3. Verify that any target-organism or growth-condition entry is limited to E. coli growth in the Mobley et al. modified-Luria-broth assay context.

## Additional Notes

The Mobley DOI cited by the normalized repair resolved through Crossref. The publisher PDF at the Crossref URL returned HTTP 403 during this review, so the paper text was not inspected directly; formulation, osmolality, and growth-context findings above are based on the TOGO M2966 extracted passage.

The repository-level `just` validators were not used for this focused record review because the project currently attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The focused validators above were run with Python 3.11 and the offline uv cache.
