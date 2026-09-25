# YAML Record Review: Brucella albimi Broth

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/Brucella_albimi_Broth.yaml
- Started UTC: 2026-09-22T00:35:47Z
- Finished UTC: 2026-09-22T00:37:00Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated record | `data/merge_yaml/merged/Brucella_albimi_Broth.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/brucella_albimi_broth.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:008874` |
| Name | `brucella_albimi_broth` |
| Source grounding | `TOGO:M2288` |
| Merge fingerprint | `2c948f0268431a4afa28b5291a7d039376fb8a0124ec7065fb1e7ef4eae485d5` |

This is a generated one-source merge of a TOGO M2288 import.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/Brucella_albimi_Broth.yaml` | Pass |
| Strict | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/Brucella_albimi_Broth.yaml --out /private/tmp/Brucella_albimi_Broth.strict.tsv --workers 1 --quiet` | Pass |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/Brucella_albimi_Broth.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass; 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/Brucella_albimi_Broth.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass |
| Embedded history | `just validate-history` | Not checked: the documented history validator validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries |
| Full project schema | `just validate-schema` | Not rerun: project `uv` attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'` |
| Full project strict | `just validate-strict` | Not rerun: same project dependency build failure |
| Full project terms | `just validate-terms` | Not rerun: same project dependency build failure |

## Identity and Grounding

`CultureMech:008874` is grounded to TOGO M2288, Brucella albimi Broth, and TOGO links the matching ATCC medium PDF. The source recipe is 28 g Brucella Broth (BD 211088) in 1000 ml DI water, autoclaved at 121 C.

A gitignore-independent exact search covering `data`, `reports`, and the repository root found the single live normalized owner, the generated merge, and expected index/archive/import-report references for `CultureMech:008874`, `TOGO:M2288`, the record slug, the ATCC URL hash, and the merge fingerprint.

## Evidence

Supported:

- The medium identity, liquid physical state, `Brucella Broth (BD 211088)` amount, DI water volume, ATCC URL, and 121 C autoclave instruction are supported by both TOGO M2288 and the ATCC PDF.
- Preserving Brucella Broth as a complex commercial base is appropriate; the same ATCC page gives an optional scratch formulation but does not require decomposing the BD 211088 product row.

Unsupported or over-scoped:

- The generated merge is stale relative to its maintained owner. The owner already has DI water as `1.0 L`, ingredient source notes, the TOGO and ATCC structured references, `preparation_steps`, `sterilization`, and quality flags from the 2026-09-07 `RESOLVED_TOGO_LITERAL_PRODUCT_SCORE40_GRAPH` repair; the generated merge still has `1000 G_PER_L` DI water and none of those structured repairs.
- The pH 6.8-7.2 exposed by TOGO and ATCC is absent from both the generated merge and the repaired owner.

## Completeness

Consequential gaps:

- The generated artifact should be regenerated from `data/normalized_yaml/bacterial/brucella_albimi_broth.yaml` so it picks up the water-unit, reference, and autoclave repair.
- The maintained owner should still add the source pH range before regeneration.

Empty optional slots that are acceptable as empty:

- TOGO M2288 and the ATCC page do not expose strain IDs, incubation temperature, or atmosphere. Those fields should stay empty.

Bounded searches:

- A gitignore-independent exact search for `CultureMech:008874`, `TOGO:M2288`, `brucella_albimi_broth`, the ATCC URL hash, and `2c948f0268431a4afa28b5291a7d039376fb8a0124ec7065fb1e7ef4eae485d5` covered `data`, `reports`, and the repository root. It found no duplicate live YAML owner.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*Brucella_albimi_Broth.md' -print` found no prior report with this stem before this report was created.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | The generated record is stale and still contains the pre-repair water-unit bug. | The generated merge stores DI water as `1000 G_PER_L`; the maintained owner repaired that to `1.0 L` on 2026-09-07 and added source notes, structured references, and autoclave fields. | Regenerate from `data/normalized_yaml/bacterial/brucella_albimi_broth.yaml` |
| minor | The source pH range is still missing from the maintained owner. | TOGO M2288 exposes pH 6.8 - 7.2 and the ATCC PDF reports pH 7.0 +/- 0.2. | `data/normalized_yaml/bacterial/brucella_albimi_broth.yaml` |

## Recommended Edits

1. Add `ph_value: 7.0` with a pH-range note to `data/normalized_yaml/bacterial/brucella_albimi_broth.yaml`.
2. Regenerate `data/merge_yaml/merged/Brucella_albimi_Broth.yaml` from the repaired normalized owner so the merge no longer contains `1000 G_PER_L` water and stale unstructured provenance.

## Follow-up Checks

- Rerun `just validate-schema`, `just validate-strict`, `just validate-references`, and `just validate-terms` once the project Python environment can install its pinned dependencies.
- Rerun the no-project open-schema, strict, reference, and term validators on the regenerated merge.
- Re-fetch TOGO M2288 and the ATCC PDF and manually verify the 28 g commercial broth amount, 1000 ml DI water amount, pH range, and 121 C autoclave step.
- Repeat a gitignore-independent exact search for `TOGO:M2288` and `CultureMech:008874` to confirm no duplicate owner appears after repair.

## Additional Notes

None found.
