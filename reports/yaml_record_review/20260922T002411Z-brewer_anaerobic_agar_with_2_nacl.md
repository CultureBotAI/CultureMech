# YAML Record Review: Brewer Anaerobic Agar With 2% NaCl

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/brewer_anaerobic_agar_with_2_nacl.yaml
- Started UTC: 2026-09-22T00:24:11Z
- Finished UTC: 2026-09-22T00:25:31Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated record | `data/merge_yaml/merged/brewer_anaerobic_agar_with_2_nacl.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/brewer_anaerobic_agar_with_2_nacl.yaml` |
| Related live duplicate | `data/normalized_yaml/specialized/brewer_anaerobic_agar_with_2_nacl.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:010090` |
| Name | `brewer_anaerobic_agar_with_2_nacl` |
| Source grounding | `TOGO:M685` / JCM `JCM_M667` |
| Merge fingerprint | `cd2c24232935eac0eba9984791ccaeb4ef9aa523b270488cbb961d98203468c2` |

This is a generated one-source merge of a bacterial TOGO import. The same JCM 667 source also exists as a separate specialized normalized record.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/brewer_anaerobic_agar_with_2_nacl.yaml` | Pass; `No issues found` |
| Strict | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/brewer_anaerobic_agar_with_2_nacl.yaml --out /private/tmp/brewer_anaerobic_agar_with_2_nacl.strict.tsv --workers 1 --quiet` | Pass |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/brewer_anaerobic_agar_with_2_nacl.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass; 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/brewer_anaerobic_agar_with_2_nacl.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass |
| Embedded history | `just validate-history` | Not checked: the documented history validator validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries |
| Full project schema | `just validate-schema` | Not rerun: project `uv` attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'` |
| Full project strict | `just validate-strict` | Not rerun: same project dependency build failure |
| Full project terms | `just validate-terms` | Not rerun: same project dependency build failure |

## Identity and Grounding

`CultureMech:010090` is grounded to TOGO M685, whose API names JCM `JCM_M667` as the original source and links to JCM `GRMD=667`. The TOGO and JCM labels both match Brewer Anaerobic Agar With 2% NaCl, and the three top-level components agree: Brewer anaerobic agar (BD-Difco), NaCl, and distilled water.

A gitignore-independent exact search covering `data`, `reports`, and the repository root found the maintained bacterial owner, the generated merge, expected indexes and archive references, media-variant proposal reports, and a live `data/normalized_yaml/specialized/brewer_anaerobic_agar_with_2_nacl.yaml` record for the same JCM 667 recipe. That specialized record should be reconciled instead of remaining a separate generated-target omission.

## Evidence

Supported:

- TOGO M685 and JCM Medium 667 support the label and JCM source identity.
- The generated solid agar state is supported by the JCM recipe's use of Brewer anaerobic agar.
- `NaCl` at `20 G_PER_L` matches JCM's 20.0 g per 1.0 L and is correctly grounded to sodium chloride.
- `Brewer anaerobic agar (BD-Difco)` at `58 G_PER_L` matches JCM's 58.0 g per 1.0 L.
- The JCM source page supports autoclaving at 121 C for 15 min unless otherwise stated.

Unsupported or over-scoped:

- `Distilled water` is imported with value `1` and unit `G_PER_L`. TOGO stores 1 L, JCM stores 1.0 L, and the specialized owner already models it as `1000 ML_PER_L`; the generated unit is wrong.
- The generated record stores the JCM URL only inside `notes`. The same recipe's specialized owner has a structured `references` entry and the repair history that names the source URL.
- The generated record does not carry the JCM autoclave instruction.

## Completeness

Consequential gaps:

- The bacterial owner needs the September 2026 JCM simple-recipe repair that has already been applied to the specialized owner: corrected water volume, structured JCM reference, preparation steps, sterilization, and quality flags.
- The bacterial and specialized copies should be linked or merged as exact source duplicates for JCM Medium 667.
- Brewer anaerobic agar is necessarily a complex commercial base and is acceptable as an unmapped ingredient, but the record should keep a quality flag for that unmapped ingredient after repair.

Empty optional slots that are acceptable as empty:

- TOGO M685 and the JCM 667 page do not name organisms, strain IDs, pH, incubation temperature, or atmosphere. Those fields should stay empty until another inspected JCM or strain page supports them.

Bounded searches:

- A gitignore-independent exact search for `CultureMech:010090`, `TOGO:M685`, `M685`, `JCM_M667`, `GRMD=667`, `brewer_anaerobic_agar_with_2_nacl`, and the merge fingerprint covered `data`, `reports`, and the repository root. It found the additional specialized YAML owner and no other live normalized YAML source for JCM 667.
- The same search intentionally found unrelated `JCM_M685` records; those are JCM Medium 685 and are not duplicates of JCM Medium 667.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*brewer_anaerobic_agar_with_2_nacl.md' -print` found no prior report with this stem before this report was created.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | Distilled water has the wrong unit. | TOGO M685 reports 1 L and JCM 667 reports 1.0 L distilled water; `data/merge_yaml/merged/brewer_anaerobic_agar_with_2_nacl.yaml` records `value: '1'` with `unit: G_PER_L`. | `data/normalized_yaml/bacterial/brewer_anaerobic_agar_with_2_nacl.yaml` |
| major | The same JCM 667 recipe is curated twice in live normalized YAML. | The bacterial owner is TOGO M685 / JCM_M667 with three matching ingredients, and `data/normalized_yaml/specialized/brewer_anaerobic_agar_with_2_nacl.yaml` is the repaired JCM Medium 667 import for the same formulation. | `data/normalized_yaml/bacterial/brewer_anaerobic_agar_with_2_nacl.yaml`; `data/normalized_yaml/specialized/brewer_anaerobic_agar_with_2_nacl.yaml` |
| minor | The JCM source URL and default autoclave instruction have not been carried into the generated record structurally. | JCM's Medium 667 page gives the 121 C, 15 min autoclave default. The specialized owner has `references`, `preparation_steps`, and `sterilization`, while the bacterial TOGO owner keeps only an unstructured original URL note. | `data/normalized_yaml/bacterial/brewer_anaerobic_agar_with_2_nacl.yaml` |

## Recommended Edits

1. Apply the `RESOLVED_OFFICIAL_SIMPLE_SCORE20` JCM 667 repair to `data/normalized_yaml/bacterial/brewer_anaerobic_agar_with_2_nacl.yaml`: model 1.0 L water as volume, add the JCM URL as a structured reference, and preserve the autoclave default.
2. Mark the specialized JCM owner and the bacterial TOGO owner as source duplicates, or merge them if cross-category duplicate handling allows an exact JCM/TOGO match.
3. Keep `Brewer anaerobic agar (BD-Difco)` as an explicit complex base and leave `has_unmapped_ingredients` until that commercial product has a precise ontology or catalog grounding.
4. Regenerate `data/merge_yaml/merged/brewer_anaerobic_agar_with_2_nacl.yaml` from the repaired normalized owner.

## Follow-up Checks

- Rerun `just validate-schema`, `just validate-strict`, `just validate-references`, and `just validate-terms` once the project Python environment can install its pinned dependencies.
- Rerun the no-project open-schema, strict, reference, and term validators on the regenerated merge.
- Re-fetch TOGO M685 and JCM `GRMD=667`, then manually confirm the generated water volume, NaCl mass, Brewer agar mass, and preparation steps.
- Repeat a gitignore-independent exact search for `JCM_M667`, `GRMD=667`, and `brewer_anaerobic_agar_with_2_nacl` to verify that any remaining bacterial/specialized duplication is intentional and explicitly linked.

## Additional Notes

`reports/media_variant_parent_group_proposals.json` and `reports/media_variant_link_proposals.json` already mention the bacterial owner and the specialized owner as a proposed parent/child pair. Those proposal rows have not been applied to the normalized owners reviewed here.
