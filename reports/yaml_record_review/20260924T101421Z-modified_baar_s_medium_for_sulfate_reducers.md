# YAML Record Review: Modified Baar's Medium For Sulfate Reducers

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_baar_s_medium_for_sulfate_reducers.yaml
- Started UTC: 2026-09-24T10:14:21Z
- Finished UTC: 2026-09-24T10:14:21Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Record | `data/merge_yaml/merged/modified_baar_s_medium_for_sulfate_reducers.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:009183` |
| Name | `modified_baar_s_medium_for_sulfate_reducers` |
| Original name | `Modified Baar's Medium For Sulfate Reducers` |
| Category | `bacterial` |
| Medium source | TOGO `M2616`; original source ATCC medium 1249 PDF |
| Maintained owner | `data/normalized_yaml/bacterial/modified_baar_s_medium_for_sulfate_reducers.yaml` |
| Generated status | Generated merge output from one normalized TOGO record |

## Validation

| Check | Result |
| --- | --- |
| Open LinkML schema validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_baar_s_medium_for_sulfate_reducers.yaml` | Passed; exited 0 with "No issues found". |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/modified_baar_s_medium_for_sulfate_reducers.yaml --out /private/tmp/modified_baar_s_medium_for_sulfate_reducers.strict.tsv --workers 1 --quiet` | Passed; 0 strict errors were reported and `/private/tmp/modified_baar_s_medium_for_sulfate_reducers.strict.tsv` contained only the header line. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/modified_baar_s_medium_for_sulfate_reducers.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the focused run completed with 0 reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/modified_baar_s_medium_for_sulfate_reducers.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not inline `MediaRecipe.curation_history` entries in a merged YAML record. |

## Identity and Grounding

The record identity is coherent: `CultureMech:009183`, `TOGO:M2616`, and the ATCC 1249 PDF all identify Modified Baar's Medium For Sulfate Reducers.

An exact `find data/normalized_yaml -name 'modified_baar_s_medium_for_sulfate_reducers.yaml'` search, which does not honor gitignore exclusions, found `data/normalized_yaml/bacterial/modified_baar_s_medium_for_sulfate_reducers.yaml` as the generated record's maintained owner.

The resolved chemical groundings preserve the source identities for NH4Cl, CaSO4 x 2H2O, MgSO4, sodium citrate, K2HPO4, and sodium lactate.

## Evidence

TOGO `M2616` and the ATCC 1249 PDF support a three-component protocol: Component I is 400 ml; Component II is 200 ml; Component III is 400 ml; each component is adjusted to pH 7.5 and autoclaved at 121 C; the three components are mixed aseptically and tubed under 97% N2 and 3% H2 while warm; and an optional filter-sterilized 5% ferrous ammonium sulfate solution is added at 0.1 ml to 5 ml of medium only when specified.

| Source claim | Record representation | Review |
| --- | --- | --- |
| The final medium is assembled from Component I, Component II, and Component III at 400, 200, and 400 ml. | `Component I`, `Component II`, and `Component III` are top-level ingredients at 400, 200, and 400 `G_PER_L`. | Unsupported unit and lost component boundary. |
| Component I contains 400 ml DI water; Component II contains 200 ml DI water; Component III contains 400 ml DI water. | The three DI Water rows are duplicate-merged into `1000.0 G_PER_L`. | Unsupported volume-to-mass import and component collapse. |
| Tube under a 97% N2 / 3% H2 gas phase. | N2 and H2 are variable ingredients with no 97:3 ratio. | Incomplete gas composition. |
| Each component is adjusted to pH 7.5 and autoclaved at 121 C, then mixed aseptically while warm. | No pH or preparation steps are represented. | Incomplete. |
| 5% Ferrous Ammonium Sulfate is filter sterilized and optionally added at 0.1 ml per 5 ml medium when specified. | No optional ferrous ammonium sulfate solution or filtration step is represented. | Incomplete. |

## Completeness

The flattened record has the right final mass totals for the non-water Component I, II, and III solutes, but it is missing the source component structure that makes the ATCC protocol reproducible. The generated Component I/II/III placeholder ingredients, merged water row, default gas variables, and absent pH/preparation steps would not tell a curator or user how to prepare the source recipe.

Empty target-organism and growth-evidence fields were not treated as defects. ATCC 1249 is a medium formulation page, not a growth-evidence page.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | Component I, II, and III volumes are represented as gram-per-liter ingredients. | TOGO and ATCC list 400, 200, and 400 ml as component volumes to be mixed; the record stores those components as 400, 200, and 400 `G_PER_L` ingredients. | `data/normalized_yaml/bacterial/modified_baar_s_medium_for_sulfate_reducers.yaml`; TOGO component migration. |
| major | Three compartment-specific water rows were flattened into one mass concentration. | The ATCC PDF has 400 ml DI Water in Component I, 200 ml in Component II, and 400 ml in Component III; the record has one `1000.0 G_PER_L` DI Water row with a duplicate-merge note. | `data/normalized_yaml/bacterial/modified_baar_s_medium_for_sulfate_reducers.yaml`; duplicate cleanup must preserve component boundaries. |
| major | The 97% N2 / 3% H2 gas phase is lost. | The source specifies tubing under 97% N2 and 3% H2; the record has variable N2 and H2 ingredients without the ratio. | `data/normalized_yaml/bacterial/modified_baar_s_medium_for_sulfate_reducers.yaml`; gas parsing. |
| major | pH 7.5 and 121 C component autoclaving are absent. | ATCC says each component is adjusted to pH 7.5 and autoclaved at 121 C before aseptic mixing; no pH or preparation step is stored. | `data/normalized_yaml/bacterial/modified_baar_s_medium_for_sulfate_reducers.yaml`; TOGO comment import. |
| major | The optional ferrous ammonium sulfate addition is absent. | ATCC says 5% Ferrous Ammonium Sulfate should be filter sterilized and added at 0.1 ml to 5.0 ml medium prior to inoculation only when specified; the record has no optional solution or filtration note. | `data/normalized_yaml/bacterial/modified_baar_s_medium_for_sulfate_reducers.yaml`; TOGO comment import and optional solution modeling. |

## Recommended Edits

1. Re-curate `data/normalized_yaml/bacterial/modified_baar_s_medium_for_sulfate_reducers.yaml` from TOGO `M2616` and the ATCC 1249 PDF so Component I, II, and III are explicit compartments mixed at 400, 200, and 400 ml.
2. Preserve the 400/200/400 ml DI Water rows inside their source components instead of duplicate-merging them into `1000.0 G_PER_L`.
3. Represent the 97% N2 / 3% H2 tubing atmosphere and add pH 7.5 plus 121 C component autoclaving, aseptic mixing, and warm tubing preparation steps.
4. Represent the optional 5% ferrous ammonium sulfate solution as a filter-sterilized post-mix addition at 0.1 ml per 5 ml when specified, not as an always-present ingredient.
5. Regenerate `data/merge_yaml/merged/modified_baar_s_medium_for_sulfate_reducers.yaml` after the normalized source is corrected.

## Follow-up Checks

1. Re-run focused open-schema, strict, reference, and term validators on `data/normalized_yaml/bacterial/modified_baar_s_medium_for_sulfate_reducers.yaml` and the regenerated merge output.
2. Manually compare the regenerated record against the ATCC 1249 PDF, checking all three component recipes, the 97:3 N2/H2 gas phase, pH 7.5, 121 C autoclaving, and the optional ferrous ammonium sulfate addition.
3. Verify that no Component I/II/III placeholder remains as a mass ingredient.

## Additional Notes

The ATCC original was fetched as a one-page PDF and rendered to text with `mutool`; the extracted PDF text was sufficient to verify TOGO's parsed source rows.

The repository-level `just` validators were not used for this focused record review because the project currently attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The focused validators above were run with Python 3.11 and the offline uv cache.
