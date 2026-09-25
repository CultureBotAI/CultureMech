# YAML Record Review: Brucella agar plates supplemented with hemin and vitamin K1

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/Brucella_agar_plates_supplemented_with_hemin_and_vitamin_K1.yaml
- Started UTC: 2026-09-22T00:34:03Z
- Finished UTC: 2026-09-22T00:35:04Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated record | `data/merge_yaml/merged/Brucella_agar_plates_supplemented_with_hemin_and_vitamin_K1.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/brucella_agar_plates_supplemented_with_hemin_and_vitamin_k1.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:009246` |
| Name | `brucella_agar_plates_supplemented_with_hemin_and_vitamin_k1` |
| Source grounding | `TOGO:M2694` |
| Merge fingerprint | `7f2a46a0b8287892a768db81d908dfef5a7695fc8db301639b2a3042619e9d8b` |

This is a generated one-source merge of a TOGO M2694 import.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/Brucella_agar_plates_supplemented_with_hemin_and_vitamin_K1.yaml` | Pass; `No issues found` |
| Strict | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/Brucella_agar_plates_supplemented_with_hemin_and_vitamin_K1.yaml --out /private/tmp/Brucella_agar_plates_supplemented_with_hemin_and_vitamin_K1.strict.tsv --workers 1 --quiet` | Pass |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/Brucella_agar_plates_supplemented_with_hemin_and_vitamin_K1.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass; 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/Brucella_agar_plates_supplemented_with_hemin_and_vitamin_K1.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass |
| Embedded history | `just validate-history` | Not checked: the documented history validator validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries |
| Full project schema | `just validate-schema` | Not rerun: project `uv` attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'` |
| Full project strict | `just validate-strict` | Not rerun: same project dependency build failure |
| Full project terms | `just validate-terms` | Not rerun: same project dependency build failure |

## Identity and Grounding

`CultureMech:009246` is grounded to TOGO M2694, which names the recipe Brucella agar plates supplemented with hemin and vitamin K1. The TOGO payload supports the Brucella agar constituent amounts, the hemin and vitamin K1 supplement amounts, the sheep-blood percentage, solid agar state, and pH 7.2 +/- 0.2.

A gitignore-independent exact search covering `data`, `reports`, and the repository root found one live normalized owner, one generated merge, and expected index/archive/import-report references for `CultureMech:009246`, `TOGO:M2694`, the record slug, and the merge fingerprint.

## Evidence

Supported:

- TOGO M2694 supports the label and Brucella agar plate identity.
- The 2 g yeast extract, 5 g sodium chloride, 5 mg hemin, 1 g glucose, 10 mg vitamin K1, 15 g agar, 0.1 g sodium bisulfite, 10 g pancreatic digest of casein, and 10 g peptic digest of animal tissue rows are source-supported per liter.
- Sodium chloride, hemin, glucose, agar, sodium hydrogensulfite, and vitamin K1 have appropriate chemical groundings.

Unsupported or over-scoped:

- `Distilled water` is stored as `1 G_PER_L`; TOGO M2694 lists 1 L.
- The source pH 7.2 +/- 0.2 is absent.
- TOGO's sheep blood unit is `%`; the YAML stores `PERCENT_W_V`, which is not supported for a defibrinated blood volume addition without another inspected source.
- TOGO's source comment records incubation at 37 C in an anaerobic atmosphere, but the YAML has no structured temperature or atmosphere condition.
- TOGO `src_url` is empty, so the original publication behind the TOGO excerpt is not recorded or cited.

## Completeness

Consequential gaps:

- The medium cannot be reproduced literally because the 1 L water row is unit-corrupted.
- pH and anaerobic 37 C incubation context are omitted.
- The primary citation and organism or strain context behind TOGO M2694 are missing.
- Pancreatic digest of casein, peptic digest of animal tissue, Yeast Extract, and defibrinated sheep blood remain ungrounded complex components.

Empty optional slots that are acceptable as empty:

- The TOGO API does not expose strain IDs, preparation order, or sterilization conditions for this entry. Those fields should stay empty until the primary source is recovered.

Bounded searches:

- A gitignore-independent exact search for `CultureMech:009246`, `TOGO:M2694`, `brucella_agar_plates_supplemented_with_hemin_and_vitamin_k1`, and `7f2a46a0b8287892a768db81d908dfef5a7695fc8db301639b2a3042619e9d8b` covered `data`, `reports`, and the repository root. It found no duplicate live YAML owner.
- `find reports/yaml_record_review -maxdepth 1 -type f -name '*Brucella_agar_plates_supplemented_with_hemin_and_vitamin_K1.md' -print` found no prior report with this stem before this report was created.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | Distilled water has the wrong unit. | TOGO M2694 lists 1 L water, while the generated YAML stores `value: '1'`, `unit: G_PER_L`. | `data/normalized_yaml/bacterial/brucella_agar_plates_supplemented_with_hemin_and_vitamin_k1.yaml` |
| major | Source-supported pH and anaerobic incubation context are missing. | TOGO exposes pH 7.2 +/- 0.2 and comments that the Brucella agar plates were incubated at 37 C in an anaerobic atmosphere. | `data/normalized_yaml/bacterial/brucella_agar_plates_supplemented_with_hemin_and_vitamin_k1.yaml` |
| minor | The sheep-blood percentage is over-specified. | TOGO gives the unit as plain percent, but the YAML stores `PERCENT_W_V` for defibrinated sheep blood. | `data/normalized_yaml/bacterial/brucella_agar_plates_supplemented_with_hemin_and_vitamin_k1.yaml` |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/brucella_agar_plates_supplemented_with_hemin_and_vitamin_k1.yaml`, correct the 1 L distilled water row to a volume unit or remove it if water is represented as final volume elsewhere.
2. Add `ph_value: 7.2` with an appropriate +/- 0.2 note if the schema has no pH range field.
3. Capture the 37 C anaerobic incubation context from TOGO M2694 as structured conditions or a source-scoped note.
4. Search for the primary publication behind the TOGO M2694 comment, then add the citation and any organism or strain scope it supports.
5. Change defibrinated sheep blood to a generic percent unit unless an inspected source supports weight/volume.
6. Regenerate `data/merge_yaml/merged/Brucella_agar_plates_supplemented_with_hemin_and_vitamin_K1.yaml` after curation.

## Follow-up Checks

- Rerun `just validate-schema`, `just validate-strict`, `just validate-references`, and `just validate-terms` once the project Python environment can install its pinned dependencies.
- Rerun the no-project open-schema, strict, reference, and term validators on the regenerated merge.
- Re-fetch TOGO M2694 and manually compare all ingredient masses, water volume, pH, sheep-blood unit, and incubation comment.
- Repeat a gitignore-independent exact search for `TOGO:M2694` and `CultureMech:009246` to confirm no duplicate owner appears after repair.

## Additional Notes

None found.
