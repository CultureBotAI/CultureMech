# YAML Record Review: Briggs Liver Broth (pH 5.0)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/briggs_liver_broth_ph_5_0.yaml
- Started UTC: 2026-09-22T00:26:15Z
- Finished UTC: 2026-09-22T00:27:54Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated record | `data/merge_yaml/merged/briggs_liver_broth_ph_5_0.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/TOGO_M115_Briggs_Liver_Broth_pH_5.0.yaml` |
| Related live duplicate | `data/normalized_yaml/bacterial/briggs_liver_broth_ph_5_0.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:007683` |
| Name | `briggs_liver_broth_ph_5_0` |
| Source grounding | `TOGO:M115` / JCM `JCM_M123` |
| Merge fingerprint | `d6e04ccb5eb540feef7425d649835602cb4f5ea1206b0d6a52c9b998c2f3653c` |

This is a generated one-source merge of the TOGO import for JCM Medium 123.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/briggs_liver_broth_ph_5_0.yaml` | Pass; `No issues found` |
| Strict | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/briggs_liver_broth_ph_5_0.yaml --out /private/tmp/briggs_liver_broth_ph_5_0.strict.tsv --workers 1 --quiet` | Pass |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/briggs_liver_broth_ph_5_0.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass; 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/briggs_liver_broth_ph_5_0.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass |
| Embedded history | `just validate-history` | Not checked: the documented history validator validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries |
| Full project schema | `just validate-schema` | Not rerun: project `uv` attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'` |
| Full project strict | `just validate-strict` | Not rerun: same project dependency build failure |
| Full project terms | `just validate-terms` | Not rerun: same project dependency build failure |

## Identity and Grounding

`CultureMech:007683` is grounded to TOGO M115, which names JCM `JCM_M123` as the original source and links to JCM `GRMD=123`. TOGO and JCM agree that the source recipe is Briggs Liver Broth at pH 5.0.

A gitignore-independent exact-boundary search covering `data`, `reports`, and the repository root found one TOGO owner, one generated TOGO merge, expected indexes and archives, and an adjacent MediaDive/JCM owner at `data/normalized_yaml/bacterial/briggs_liver_broth_ph_5_0.yaml` that cites the same JCM `GRMD=123` page. That second live owner generates `data/merge_yaml/merged/briggs_liver_broth_ph_5_0__4e6d8e6a.yaml` and is not yet linked to this TOGO copy as a source duplicate.

## Evidence

Supported:

- TOGO M115 and JCM Medium 123 support the source identity, label, JCM URL, and final pH 5.0.
- NaCl, Tween 80, glucose, soluble starch, yeast extract, L-cysteine hydrochloride monohydrate, and Neopeptone have source-supported masses per liter.
- The direct 400 ml Tomato juice solution and 75 ml Liver extract main-medium additions are supported as volumes of prepared stock solutions.
- The final medium is liquid; no agar or gelling agent is present.

Unsupported or over-scoped:

- The generated record omits `ph_value: 5.0`, even though TOGO M115 exposes pH 5.0 and JCM says to adjust the final medium to pH 5.0.
- `Distilled water` is stored as a single direct `725 G_PER_L` ingredient with a duplicate-merge note. JCM and TOGO instead have 525 ml distilled water in the final medium plus 200 ml water inside the Tomato juice solution.
- The Tomato juice solution is split inconsistently: the generated record has an empty `solutions` row for 400 ml/L Tomato juice solution, while also hoisting its 200 ml tomato juice, 200 ml water, and 10% NaOH subcomponents into final-medium ingredients.
- `NaOH` is present as a variable direct ingredient, but JCM uses 10% NaOH only to adjust the pH of the tomato juice stock before filtration.
- The Liver extract cross-reference is left as an empty solution named `Unknown solution`, and the JCM link target is effectively lost.
- The JCM default autoclave instruction and the tomato-juice filtration instruction are not represented as preparation steps.

## Completeness

Consequential gaps:

- The nested solution structure is not usable: both generated solution entries have empty `composition` arrays and default names.
- The maintained TOGO owner and the maintained MediaDive/JCM owner for `GRMD=123` need source-duplicate reconciliation.
- The JCM URL is only in `notes`; there is no structured `references` entry.

Empty optional slots that are acceptable as empty:

- TOGO M115 and the JCM 123 page do not name organisms, strain IDs, or incubation conditions. Those fields should remain empty unless another inspected JCM or strain page supports them.

Bounded searches:

- A gitignore-independent exact-boundary search for `CultureMech:007683`, `TOGO:M115`, `TOGO_M115_Briggs_Liver_Broth_pH_5.0`, `JCM_M123`, `GRMD=123`, and `d6e04ccb5eb540feef7425d649835602cb4f5ea1206b0d6a52c9b998c2f3653c` covered `data`, `reports`, and the repository root. It found no second live owner of `CultureMech:007683`, but did find the separate JCM `GRMD=123` owner at `data/normalized_yaml/bacterial/briggs_liver_broth_ph_5_0.yaml`.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*briggs_liver_broth_ph_5_0.md' -print` found no prior report with this exact stem before this report was created; the hash-suffixed Briggs record is a separate next target.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | The nested tomato and liver stock-solution structure was flattened into an incorrect final-medium ingredient list. | JCM 123 lists 400 ml Tomato juice solution and 75 ml Liver extract as main components, then separately defines the tomato solution from tomato juice, equal water, and 10% NaOH; the generated record hoists the tomato-stock water, tomato juice, and NaOH into top-level ingredients and leaves both solution compositions empty. | `data/normalized_yaml/bacterial/TOGO_M115_Briggs_Liver_Broth_pH_5.0.yaml` |
| major | The generated record is missing the final pH 5.0 claim. | The recipe label, TOGO `meta.ph`, and JCM preparation text all say the final Briggs Liver Broth is pH 5.0. | `data/normalized_yaml/bacterial/TOGO_M115_Briggs_Liver_Broth_pH_5.0.yaml` |
| major | The same JCM 123 recipe exists as an unlinked adjacent live owner. | The exact search found `data/normalized_yaml/bacterial/briggs_liver_broth_ph_5_0.yaml`, which cites the same JCM `GRMD=123` page and generates the adjacent hash-suffixed Briggs liver broth record. | `data/normalized_yaml/bacterial/TOGO_M115_Briggs_Liver_Broth_pH_5.0.yaml`; `data/normalized_yaml/bacterial/briggs_liver_broth_ph_5_0.yaml` |
| minor | Structured source and preparation fields are incomplete. | The JCM URL appears only in `notes`, and the source-supported final-pH, tomato-filtration, and default autoclave steps are absent from `preparation_steps`. | `data/normalized_yaml/bacterial/TOGO_M115_Briggs_Liver_Broth_pH_5.0.yaml` |

## Recommended Edits

1. Rebuild `solutions` in `data/normalized_yaml/bacterial/TOGO_M115_Briggs_Liver_Broth_pH_5.0.yaml` so the final medium references 400 ml/L Tomato juice solution and 75 ml/L Liver extract while keeping the tomato stock's 200 ml water, 200 ml tomato juice, and 10% NaOH inside the stock definition.
2. Add `ph_value: 5.0`, a structured JCM `GRMD=123` reference, and preparation steps for final pH adjustment, tomato-stock pH adjustment and filtration, and the JCM default autoclave rule where it applies.
3. Preserve the Liver extract cross-reference to the JCM medium 13 link rather than leaving it as an `Unknown solution` with no composition or source URL.
4. Resolve the source duplicate between the TOGO M115 owner and `data/normalized_yaml/bacterial/briggs_liver_broth_ph_5_0.yaml` so one regenerated record represents JCM 123.
5. Regenerate `data/merge_yaml/merged/briggs_liver_broth_ph_5_0.yaml` after the maintained owner is repaired.

## Follow-up Checks

- Rerun `just validate-schema`, `just validate-strict`, `just validate-references`, and `just validate-terms` once the project Python environment can install its pinned dependencies.
- Rerun the no-project open-schema, strict, reference, and term validators on the regenerated merge.
- Re-fetch TOGO M115 and JCM `GRMD=123`, then manually verify final pH, the 525 ml final-medium water, the 400 ml Tomato juice solution, the 75 ml Liver extract link, all gram quantities, and the tomato-stock 10% NaOH pH-adjustment step.
- Repeat a gitignore-independent exact-boundary search for `TOGO:M115`, `JCM_M123`, and `GRMD=123` to confirm no unlinked JCM 123 duplicate remains.

## Additional Notes

The first broad source search was intentionally re-run with digit-aware boundaries because `TOGO:M115` and `GRMD=123` are prefixes of many unrelated source accessions.
