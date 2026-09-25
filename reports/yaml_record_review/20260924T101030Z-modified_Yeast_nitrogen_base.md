# YAML Record Review: Modified Yeast Nitrogen Base

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_Yeast_nitrogen_base.yaml
- Started UTC: 2026-09-24T10:10:30Z
- Finished UTC: 2026-09-24T10:10:30Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Record | `data/merge_yaml/merged/modified_Yeast_nitrogen_base.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:010461` |
| Name | `modified_yeast_nitrogen_base` |
| Original name | `modified Yeast nitrogen base` |
| Category | `fungal` |
| Medium source | MediaDive / DSMZ `mediadive.medium:1837` |
| Maintained owner | `data/normalized_yaml/fungal/modified_yeast_nitrogen_base.yaml` |
| Generated status | Generated merge output from one normalized MediaDive record |

## Validation

| Check | Result |
| --- | --- |
| Open LinkML schema validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_Yeast_nitrogen_base.yaml` | Passed; exited 0 with "No issues found". |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/modified_Yeast_nitrogen_base.yaml --out /private/tmp/modified_Yeast_nitrogen_base.strict.tsv --workers 1 --quiet` | Passed; 0 strict errors were reported and `/private/tmp/modified_Yeast_nitrogen_base.strict.tsv` contained only the header line. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/modified_Yeast_nitrogen_base.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the focused run completed with 0 reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/modified_Yeast_nitrogen_base.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not inline `MediaRecipe.curation_history` entries in a merged YAML record. |

## Identity and Grounding

The record identity is coherent: `CultureMech:010461` and MediaDive / DSMZ `1837` both identify modified Yeast nitrogen base.

An exact `find data/normalized_yaml -name 'modified_yeast_nitrogen_base.yaml'` search, which does not honor gitignore exclusions, found `data/normalized_yaml/fungal/modified_yeast_nitrogen_base.yaml` as the generated record's maintained owner.

The resolved glucose, MgSO4 x 7 H2O, and Gellan Gum ingredient groundings preserve the source identities. `Yeast Nitrogen Base` and `MES Hydrat` are exact MediaDive labels but remain ungrounded; that is preferable to assigning a plausible but unchecked broader term.

## Evidence

MediaDive 1837 supports the imported single-solution formula:

| Source claim | Record representation | Review |
| --- | --- | --- |
| The recipe is `Main sol. 1837`, 1000 ml, for modified Yeast nitrogen base. | The record is a `MediaRecipe` for `mediadive.medium:1837`. | Supported. |
| The formula contains 6.7 g Yeast Nitrogen Base, 2 g glucose, 3.9 g MES Hydrat, 1 g MgSO4 x 7 H2O, and 8 g Gellan Gum. | The record contains those five ingredients with matching `G_PER_L` amounts. | Supported. |
| MgSO4 x 7 H2O and Gellan Gum are autoclaved separately in 500 ml; the liquid medium omits MgSO4 x 7 H2O and Gellan Gum. | The record has the same preparation text. | Supported, aside from preserving MediaDive's original `und` typo. |
| The final recipe includes 8 g/L Gellan Gum. | The record is classified as `LIQUID`. | Internally inconsistent physical-state classification. |

## Completeness

The generated record includes every compound row exposed by the MediaDive 1837 REST record, and the source exposes no pH, target organism, strain-specific growth table, or additional comment to capture.

The remaining gap is the final-medium state: MediaDive includes Gellan Gum as a required 8 g/L component, so the `LIQUID` physical state appears to be an import default for a medium that is solidified by gellan gum.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | The record classifies a gellan-gum medium as `LIQUID`. | MediaDive 1837 contains a required `Gellan Gum` row at 8 g/L and says to autoclave MgSO4 x 7 H2O and Gellan Gum separately in 500 ml; the YAML keeps that row but sets `physical_state: LIQUID`. | `data/normalized_yaml/fungal/modified_yeast_nitrogen_base.yaml`; MediaDive physical-state curation. |

## Recommended Edits

1. Re-curate `data/normalized_yaml/fungal/modified_yeast_nitrogen_base.yaml` so the physical state no longer asserts `LIQUID` for a recipe containing 8 g/L Gellan Gum.
2. Regenerate `data/merge_yaml/merged/modified_Yeast_nitrogen_base.yaml` after the normalized source is corrected.

## Follow-up Checks

1. Re-run focused open-schema, strict, reference, and term validators on `data/normalized_yaml/fungal/modified_yeast_nitrogen_base.yaml` and the regenerated merge output.
2. Manually compare the regenerated record against MediaDive `1837`, checking all five ingredient amounts and the separate-autoclave preparation text.
3. Verify that `MES Hydrat` remains exact and unresolved unless a curator confirms the precise chemical hydrate form.

## Additional Notes

The repository-level `just` validators were not used for this focused record review because the project currently attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The focused validators above were run with Python 3.11 and the offline uv cache.
