# YAML Record Review: BROCKIA MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BROCKIA_MEDIUM.yaml
- Started UTC: 2026-09-22T00:30:12Z
- Finished UTC: 2026-09-22T00:31:22Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated record | `data/merge_yaml/merged/BROCKIA_MEDIUM.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/brockia_medium.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:001503` |
| Name | `brockia_medium` |
| Source grounding | `mediadive.medium:395a` |
| Merge fingerprint | `4e9a972454549b583dc5dbd4b38e9dc6870b8739b7d5cec691d375e8c61b7e29` |

This is a generated one-source merge of the MediaDive/DSMZ Medium 395a import.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BROCKIA_MEDIUM.yaml` | Pass |
| Strict | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/BROCKIA_MEDIUM.yaml --out /private/tmp/BROCKIA_MEDIUM.strict.tsv --workers 1 --quiet` | Pass |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/BROCKIA_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass; 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/BROCKIA_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass |
| Embedded history | `just validate-history` | Not checked: the documented history validator validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries |
| Full project schema | `just validate-schema` | Not rerun: project `uv` attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'` |
| Full project strict | `just validate-strict` | Not rerun: same project dependency build failure |
| Full project terms | `just validate-terms` | Not rerun: same project dependency build failure |

## Identity and Grounding

`CultureMech:001503` denotes DSMZ Medium 395a, BROCKIA MEDIUM. The DSMZ 395a PDF supports the medium label, liquid state, pH 6.5 final adjustment, anaerobic preparation under hydrogen/carbon dioxide, addition of sulfur to vessels before sterilization, and post-sterilization addition of bicarbonate, vitamins, and sulfide from sterile anoxic stocks.

A gitignore-independent exact search covering `data`, `reports`, and the repository root found only the expected normalized owner, generated merge, indexes, and archive/import reports for `CultureMech:001503`, `mediadive.medium:395a`, `DSMZ_Medium395a`, and `brockia_medium`. No second live normalized YAML owner was found.

## Evidence

Supported:

- The record has the correct DSMZ Medium 395a identity and final `ph_value: 6.5`.
- The direct basal salts, sulfur, bicarbonate, sodium sulfide, and sodium resazurin are close to DSMZ's per-liter quantities.
- The preparation prose accurately preserves the anoxic sparging, 80:20 H2/CO2 dispensing gas, intermittent boiling sterilization, bicarbonate stock gas, vitamin filtration, 100% N2 sulfide stock, and final pH adjustment.
- The trace-element and vitamin member identities are all sourced from the DSMZ 395a PDF's SL-10 and Wolin 10x recipes.

Unsupported or over-scoped:

- Trace element solution SL-10 and Wolin's vitamin solution (10x) have been flattened into final-medium ingredients at stock-recipe concentrations. DSMZ 395a adds only 1.00 ml of each stock per liter of final medium.
- The SL-10 constituents are therefore too high by about 1000x in the generated final medium. For example, 1.50 g/L FeCl2 tetrahydrate is the stock concentration; a 1 ml/L addition contributes 0.0015 g/L to the final medium before any volume correction.
- The Wolin vitamin constituents have the same scale error: 20 mg/L biotin in the stock becomes 0.00002 g/L final, not `0.02 G_PER_L`.
- HCl is part of the SL-10 stock recipe as 10 ml of 25% HCl, but the generated final medium stores `2.5 G_PER_L` HCl as though it were a direct ingredient.
- Final 1000 ml distilled water and stock-solution waters are omitted structurally.

## Completeness

Consequential gaps:

- The record has no `solutions` entries for Trace element solution SL-10 or Wolin's vitamin solution (10x), so stock-recipe quantities cannot be separated from final-medium dosages.
- The record does not explicitly model 1.00 ml/L SL-10, 0.50 ml/L 0.1% sodium resazurin, 1.00 ml/L Wolin vitamins, or the post-sterilization addition semantics for bicarbonate, vitamins, and sulfide as bounded stock additions.
- The DSMZ PDF URL is only in `notes`; there is no structured `references` entry.

Empty optional slots that are acceptable as empty:

- DSMZ 395a does not name a strain or incubation temperature on the inspected PDF pages. Those fields should remain empty unless another inspected source supports them.

Bounded searches:

- A gitignore-independent exact search for `CultureMech:001503`, `mediadive.medium:395a`, `DSMZ_Medium395a`, `brockia_medium`, and `BROCKIA MEDIUM` covered `data`, `reports`, and the repository root. It found no duplicate live normalized YAML owner.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*BROCKIA_MEDIUM.md' -print` found no prior report with this stem before this report was created.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | Stock-solution constituents were promoted to final-medium ingredients at stock concentration. | DSMZ 395a adds 1.00 ml/L Trace element solution SL-10 and 1.00 ml/L Wolin's vitamin solution (10x), while the generated YAML stores SL-10 and vitamin constituents as if the entire final liter were those stock recipes. | `data/normalized_yaml/bacterial/brockia_medium.yaml` |
| major | HCl is modeled as a direct 2.5 g/L final-medium ingredient. | DSMZ puts 10 ml 25% HCl inside 1 L of SL-10 stock and then adds 1 ml/L of that stock to the final medium. | `data/normalized_yaml/bacterial/brockia_medium.yaml` |
| minor | Source references are unstructured. | The DSMZ PDF URL appears only in `notes`, so the reference validator performs 0 checks for this sourced record. | `data/normalized_yaml/bacterial/brockia_medium.yaml` |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/brockia_medium.yaml`, restore Trace element solution SL-10 and Wolin's vitamin solution (10x) as `solutions` with their DSMZ Medium 320 and Medium 120 compositions.
2. Represent the final medium as 1.00 ml/L SL-10, 0.50 ml/L 0.1% sodium resazurin, 1.00 ml/L Wolin vitamins, and the direct gram-per-liter basal ingredients from DSMZ 395a.
3. Remove HCl and the trace/vitamin member chemicals from the top-level final-medium `ingredients`.
4. Add the DSMZ Medium 395a PDF as a structured reference.
5. Regenerate `data/merge_yaml/merged/BROCKIA_MEDIUM.yaml` after the maintained owner is repaired.

## Follow-up Checks

- Rerun `just validate-schema`, `just validate-strict`, `just validate-references`, and `just validate-terms` once the project Python environment can install its pinned dependencies.
- Rerun the no-project open-schema, strict, reference, and term validators on the regenerated merge.
- Re-fetch DSMZ Medium 395a and manually confirm direct basal quantities, stock addition volumes, SL-10 stock composition, Wolin 10x stock composition, sodium resazurin dilution, and final pH.
- Repeat the gitignore-independent exact search for `mediadive.medium:395a` and `brockia_medium` to confirm no duplicate owner appears after repair.

## Additional Notes

None found.
