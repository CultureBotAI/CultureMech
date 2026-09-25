# YAML Record Review: Modified Baars Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_baars_medium.yaml
- Started UTC: 2026-09-24T10:15:33Z
- Finished UTC: 2026-09-24T10:15:33Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Record | `data/merge_yaml/merged/modified_baars_medium.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:007775` |
| Name | `modified_baars_medium` |
| Original name | `Modified Baar's Medium` |
| Category | `bacterial` |
| Medium source | TOGO `M1245`; original source JCM `JCM_M1163` |
| Maintained owner | `data/normalized_yaml/bacterial/TOGO_M1245_Modified_Baar_s_Medium.yaml` |
| Generated status | Generated merge output from one normalized TOGO record |

## Validation

| Check | Result |
| --- | --- |
| Open LinkML schema validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_baars_medium.yaml` | Passed; exited 0 with "No issues found". |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/modified_baars_medium.yaml --out /private/tmp/modified_baars_medium.strict.tsv --workers 1 --quiet` | Passed; 0 strict errors were reported and `/private/tmp/modified_baars_medium.strict.tsv` contained only the header line. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/modified_baars_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the focused run completed with 0 reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/modified_baars_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not inline `MediaRecipe.curation_history` entries in a merged YAML record. |

## Identity and Grounding

The record identity is coherent: `CultureMech:007775`, `TOGO:M1245`, and the archived JCM accession `JCM_M1163` all identify Modified Baar's Medium.

An exact `find data/normalized_yaml -name 'TOGO_M1245_Modified_Baar_s_Medium.yaml'` search, which does not honor gitignore exclusions, found `data/normalized_yaml/bacterial/TOGO_M1245_Modified_Baar_s_Medium.yaml` as the generated record's maintained owner.

Most groundings preserve source chemical forms, including MgSO4 x 7H2O and ammonium nickel sulfate hexahydrate. `Trisodium citrate x 2H2O`, however, is grounded to `CHEBI:53258` / `sodium citrate`, which does not preserve the dihydrate form named by TOGO.

## Evidence

TOGO `M1245` supports a 1 L formulation with 1 L distilled water, 2 g MgSO4 x 7H2O, 1 g yeast extract, 1 g NH4Cl, 3.5 g sodium lactate, 1 g ammonium nickel sulfate hexahydrate, 5 g trisodium citrate dihydrate, and 1 g CaSO4.

| Source claim | Record representation | Review |
| --- | --- | --- |
| The medium uses 1 L distilled water. | `Distilled water` is stored as `1 G_PER_L`. | Unsupported final-volume import. |
| The seven non-water ingredients are gram-scale direct additions. | The record stores the correct numeric gram-per-liter values for all seven. | Supported at the amount level. |
| The medium is adjusted to pH 7.2, brought to a boil, cooled, dispensed into vessels under an N2 gas stream, sealed with butyl rubber stoppers, and autoclaved. | N2 is represented as a variable ingredient, but no pH or preparation step is represented. | Incomplete. |
| JCM `GRMD=1163` is the original source URL. | The record still cites that JCM URL. | Historically plausible, but the live JCM URL now returns "Nothing found"; TOGO preserves the formula. |

## Completeness

The generated record has all visible TOGO ingredient labels and all non-water ingredient amounts. It is missing the source pH and preparation context that make the anaerobic N2 handling meaningful, and it stores final-volume water as a mass concentration.

Empty target-organism and growth-evidence fields were not treated as defects. TOGO M1245 is a medium formulation import, not a growth-evidence page.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | The 1 L water row is represented as a mass concentration. | TOGO lists 1 L distilled water; the record stores `Distilled water` as `1 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M1245_Modified_Baar_s_Medium.yaml`; TOGO unit normalization. |
| major | pH and anaerobic preparation are absent. | TOGO says to adjust pH to 7.2, boil, cool, dispense under an N2 gas stream, seal with butyl rubber stoppers, and autoclave; none of those steps are modeled. | `data/normalized_yaml/bacterial/TOGO_M1245_Modified_Baar_s_Medium.yaml`; TOGO comment import. |
| major | `Trisodium citrate x 2H2O` is grounded to an anhydrous/generic sodium citrate term. | The source label includes the dihydrate form; the record links `CHEBI:53258` / `sodium citrate`. | `data/normalized_yaml/bacterial/TOGO_M1245_Modified_Baar_s_Medium.yaml`; compound grounding. |
| minor | The original JCM URL no longer resolves to a formula. | The live `GRMD=1163` page returns `Nothing found`, although TOGO still preserves the JCM-derived formula. | `data/normalized_yaml/bacterial/TOGO_M1245_Modified_Baar_s_Medium.yaml`; source provenance. |

## Recommended Edits

1. Re-curate `data/normalized_yaml/bacterial/TOGO_M1245_Modified_Baar_s_Medium.yaml` so distilled water is represented as the 1 L final volume instead of `1 G_PER_L`.
2. Import pH 7.2 and the boil, cool, N2 gas stream, butyl-rubber-stopper sealing, and autoclave preparation sequence.
3. Re-ground `Trisodium citrate x 2H2O` to the exact dihydrate form or leave it unresolved.
4. Annotate the JCM source URL as currently unavailable if the repository has a pattern for stale source URLs.
5. Regenerate `data/merge_yaml/merged/modified_baars_medium.yaml` after the normalized source is corrected.

## Follow-up Checks

1. Re-run focused open-schema, strict, reference, and term validators on `data/normalized_yaml/bacterial/TOGO_M1245_Modified_Baar_s_Medium.yaml` and the regenerated merge output.
2. Manually compare the regenerated record against TOGO `M1245`, checking all ingredient amounts, the 1 L water row, pH 7.2, and the full anaerobic preparation instruction.
3. Confirm that the JCM `GRMD=1163` unavailability is preserved as provenance rather than treated as evidence that the JCM accession was wrong.

## Additional Notes

The direct JCM `GRMD=1163` fetch returned a page with `Nothing found`; the search covered that exact URL from the record notes. TOGO `M1245` remains the inspected source for the formula.

The repository-level `just` validators were not used for this focused record review because the project currently attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The focused validators above were run with Python 3.11 and the offline uv cache.
