# YAML Record Review: BRIGGS LIVER BROTH (pH 5.0)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/briggs_liver_broth_ph_5_0__4e6d8e6a.yaml
- Started UTC: 2026-09-22T00:28:48Z
- Finished UTC: 2026-09-22T00:29:27Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated record | `data/merge_yaml/merged/briggs_liver_broth_ph_5_0__4e6d8e6a.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/briggs_liver_broth_ph_5_0.yaml` |
| Related live duplicate | `data/normalized_yaml/bacterial/TOGO_M115_Briggs_Liver_Broth_pH_5.0.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:002406` |
| Name | `briggs_liver_broth_ph_5_0` |
| Source grounding | `mediadive.medium:J123` |
| Merge fingerprint | `4e6d8e6aba84636a4ed51eac1f27036f33781635b25ba2844f9bce80a34e6f12` |

This is a generated one-source merge of a JCM Medium 123 import.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/briggs_liver_broth_ph_5_0__4e6d8e6a.yaml` | Pass; `No issues found` |
| Strict | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/briggs_liver_broth_ph_5_0__4e6d8e6a.yaml --out /private/tmp/briggs_liver_broth_ph_5_0__4e6d8e6a.strict.tsv --workers 1 --quiet` | Pass |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/briggs_liver_broth_ph_5_0__4e6d8e6a.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass; 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/briggs_liver_broth_ph_5_0__4e6d8e6a.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass |
| Embedded history | `just validate-history` | Not checked: the documented history validator validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries |
| Full project schema | `just validate-schema` | Not rerun: project `uv` attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'` |
| Full project strict | `just validate-strict` | Not rerun: same project dependency build failure |
| Full project terms | `just validate-terms` | Not rerun: same project dependency build failure |

## Identity and Grounding

The record is intended to represent JCM Medium 123, Briggs Liver Broth at pH 5.0. The JCM `GRMD=123` page supports that identity, and the maintained owner plus generated file both cite the matching JCM URL.

A gitignore-independent exact-boundary search covering `data`, `reports`, and the repository root found the reviewed MediaDive/JCM owner, its generated hash-suffixed merge, expected indexes and archives, and the separate TOGO M115 owner for the same JCM page. The two JCM 123 copies are not linked as source duplicates.

## Evidence

Supported:

- The JCM page supports the recipe label, source URL, liquid state, final pH 5.0 adjustment, tomato-solution pH 7.0 adjustment, and tomato-solution filtration.
- Neopeptone, yeast extract, glucose, starch, NaCl, Tween 80, and L-cysteine hydrochloride monohydrate have source-supported masses.
- The source supports 400 ml Tomato juice solution and 75 ml Liver extract as final-medium stock-solution volumes.

Unsupported or over-scoped:

- `ph_value: 7.0` is wrong for the final Briggs Liver Broth. The source recipe is pH 5.0; only the tomato juice stock is adjusted to pH 7.0.
- The final medium omits the 525 ml distilled water from JCM 123.
- Tomato juice solution and Liver extract are modeled as direct `G_PER_L` ingredient masses. JCM gives them as 400 ml and 75 ml additions of prepared stock solutions.
- The tomato stock is not modeled as a solution with 200 ml tomato juice, 200 ml distilled water, and 10% NaOH.
- The default JCM autoclave instruction is absent.

## Completeness

Consequential gaps:

- The source's stock-solution structure is only captured in prose, not in machine-readable ingredients and solutions.
- The final pH conflicts with the recipe identity in the label.
- The JCM source URL is only in `notes`; there is no structured `references` entry.
- The exact TOGO M115 copy of the same JCM source is unlinked.

Empty optional slots that are acceptable as empty:

- JCM 123 does not name organisms, strain IDs, or incubation conditions. Those fields should remain empty until another inspected source supports them.

Bounded searches:

- A gitignore-independent exact-boundary search for `CultureMech:002406`, `mediadive.medium:J123`, `CultureMech:007683`, `TOGO:M115`, `JCM_M123`, `GRMD=123`, and `4e6d8e6aba84636a4ed51eac1f27036f33781635b25ba2844f9bce80a34e6f12` covered `data`, `reports`, and the repository root. It found the two live normalized JCM 123 owners and their two generated records.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*briggs_liver_broth_ph_5_0__4e6d8e6a.md' -print` found no prior report with this exact stem before this report was created.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | The final pH is wrong. | JCM 123 is Briggs Liver Broth pH 5.0 and says to adjust the final medium to pH 5.0; the YAML stores `ph_value: 7.0`, which belongs only to the tomato juice stock. | `data/normalized_yaml/bacterial/briggs_liver_broth_ph_5_0.yaml` |
| major | Main-medium stock volumes were imported as direct gram-per-liter ingredients. | JCM lists 400 ml Tomato juice solution and 75 ml Liver extract per liter; the YAML stores `Tomato juice` at `400 G_PER_L` and `Liver extract` at `75 G_PER_L`. | `data/normalized_yaml/bacterial/briggs_liver_broth_ph_5_0.yaml` |
| major | The record omits source-required water and stock composition. | JCM lists 525 ml distilled water in the final medium and describes preparing Tomato juice solution from equal tomato juice and water with 10% NaOH to pH 7.0; neither is represented structurally. | `data/normalized_yaml/bacterial/briggs_liver_broth_ph_5_0.yaml` |
| major | The same JCM 123 recipe exists as an unlinked TOGO owner. | The exact-boundary search found `data/normalized_yaml/bacterial/TOGO_M115_Briggs_Liver_Broth_pH_5.0.yaml`, which maps TOGO M115 to JCM_M123 and the same `GRMD=123` page. | `data/normalized_yaml/bacterial/briggs_liver_broth_ph_5_0.yaml`; `data/normalized_yaml/bacterial/TOGO_M115_Briggs_Liver_Broth_pH_5.0.yaml` |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/briggs_liver_broth_ph_5_0.yaml`, set the final `ph_value` to `5.0` and keep the tomato-stock pH 7.0 claim only in the tomato-stock preparation step.
2. Replace direct Tomato juice and Liver extract `G_PER_L` ingredients with 400 ml/L Tomato juice solution and 75 ml/L Liver extract stock references, and add the 525 ml final-medium distilled water.
3. Model Tomato juice solution composition explicitly from 200 ml Tomato juice, 200 ml distilled water, and 10% NaOH to pH 7.0.
4. Add a structured JCM `GRMD=123` reference and include the JCM default autoclave instruction where it applies.
5. Resolve the source duplicate with `data/normalized_yaml/bacterial/TOGO_M115_Briggs_Liver_Broth_pH_5.0.yaml`, then regenerate this hash-suffixed merge or retire it if the duplicate is merged away.

## Follow-up Checks

- Rerun `just validate-schema`, `just validate-strict`, `just validate-references`, and `just validate-terms` once the project Python environment can install its pinned dependencies.
- Rerun the no-project open-schema, strict, reference, and term validators on the regenerated merge.
- Re-fetch JCM `GRMD=123` and TOGO M115, then manually verify final pH, tomato-stock pH, stock volumes, and all direct gram quantities.
- Repeat a gitignore-independent exact-boundary search for `mediadive.medium:J123`, `TOGO:M115`, `JCM_M123`, and `GRMD=123` to confirm the source duplicate has been linked or intentionally retired.

## Additional Notes

None found.
