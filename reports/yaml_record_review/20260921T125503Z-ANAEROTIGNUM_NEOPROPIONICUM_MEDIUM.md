# YAML Record Review: ANAEROTIGNUM NEOPROPIONICUM MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml
- Started UTC: 2026-09-21T12:53:03Z
- Finished UTC: 2026-09-21T12:55:03Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Path | `data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml` |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:001418` |
| Name | `anaerotignum_neopropionicum_medium` |
| Source accession | `mediadive.medium:318b` |
| Source label | `ANAEROTIGNUM NEOPROPIONICUM MEDIUM` |
| Generated status | Generated merge from `anaerotignum_neopropionicum_medium` |

The reviewed file is the generated merge for DSMZ / MediaDive Medium 318b. Its maintained owner is `data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml`; the generated record adds only merge metadata to that normalized input.

The exact, gitignore-independent identity search used `rg --no-ignore --hidden` across `data/normalized_yaml`, `data/merge_yaml/merged`, `scripts`, `tests`, and `history` for `ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM`, `ANAEROTIGNUM NEOPROPIONICUM MEDIUM`, `anaerotignum_neopropionicum_medium`, `CultureMech:001418`, `mediadive.medium:318b`, `DSMZ_Medium318b`, and `Medium318b`. It found only the maintained input, the reviewed generated merge, and generated MediaDive, bacterial, and recipe indexes for this exact record.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml` | Passed with no issues reported |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml --out /private/tmp/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were available |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` recipe validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` inside one generated merge |

The documented `just` wrappers still fail before focused validation in this checkout because project `uv` resolves with Python 3.13 and attempts to build `llvmlite==0.46.0`, whose setuptools build aborts with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The no-project Python 3.11 commands above validate the generated record without building the project.

## Identity and Grounding

The record correctly identifies DSMZ / MediaDive Medium 318b by stable ID, accession, source label, category, and liquid complex-medium classification. The rendered DSMZ PDF is headed `318b: ANAEROTIGNUM NEOPROPIONICUM MEDIUM`, and the generated record keeps the main and trace-stock preparation text.

The ingredient list conflates three source scopes: base medium rows, Trace element solution rows, and Wolin's vitamin solution rows. `NaCl` and `CaCl2 x 2 H2O` are especially affected because the base medium and trace stock both contain them; the generated record merged each pair into one direct ingredient.

`Ethanol` is represented as a direct `1.3 G_PER_L` mass even though the source adds 1.30 ml after sterilization.

The `NiCl2 x 6 H2O` ingredient is grounded to anhydrous `CHEBI:34887` nickel dichloride instead of exact nickel chloride hexahydrate.

## Evidence

The generated record has no structured `references` or `source_data` block. I rendered `DSMZ_Medium318b.pdf` directly with `mutool`.

DSMZ Medium 318b supports the base formula, 10 ml Trace element solution, 1 ml Wolin's vitamin solution, 0.5 ml 0.1% sodium resazurin, 1.30 ml ethanol, final pH range 7.0-7.2, anaerobic base preparation under 80% N2 / 20% CO2, post-sterilization addition of ethanol, cysteine, sulfide, and vitamins, Trace element solution from Medium 318, and Wolin's vitamin solution from Medium 120.

The stock composition is source-backed only inside its stock boundary:

- Trace element solution has NTA, FeCl2, MnCl2, CoCl2, CaCl2, ZnCl2, CuCl2, H3BO3, Na2MoO4, NiCl2, NaCl, Na2SeO3, and Na2WO4 in 1000 ml water.
- Wolin's vitamin solution has Biotin, Folic acid, Pyridoxine hydrochloride, Thiamine HCl, Riboflavin, Nicotinic acid, Calcium D-(+)-pantothenate, Vitamin B12, p-Aminobenzoic acid, and alpha-Lipoic acid in 1000 ml water.

Those rows are not direct final-medium `G_PER_L` additions.

## Completeness

The preparation text, final pH range, and base direct chemical rows are mostly present.

The consequential gaps are:

- no structured Trace element solution;
- no structured Wolin's vitamin solution;
- no 10 ml and 1 ml final-medium stock additions for those solutions;
- no 1.30 ml ethanol addition;
- no base-water, trace-stock water, or vitamin-stock water rows;
- no source boundary separating base NaCl and CaCl2 from trace-stock NaCl and CaCl2.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Trace element solution is flattened and merged into base rows. | DSMZ adds 10 ml Trace element solution and defines it as a 1000 ml stock. The generated record emits every trace component as a direct ingredient and merges trace-stock `NaCl` and `CaCl2 x 2 H2O` into base direct rows. | `data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml` |
| Major | Wolin's vitamin solution is flattened. | DSMZ adds 1 ml of a 10x stock from Medium 120. The generated record emits each vitamin at its stock concentration as a direct final-medium ingredient. | Same normalized owner |
| Major | Ethanol is stored with the wrong unit and addition timing. | DSMZ lists 1.30 ml ethanol and says it is added after sterilization; the generated record stores `1.3 G_PER_L` as a direct ingredient. | Same normalized owner or MediaDive/DSMZ importer |
| Minor | Three water rows are absent. | DSMZ lists 1000 ml distilled water in the base medium, the trace element stock, and the Wolin vitamin stock. None are present in the generated record. | Same normalized owner after stock repair |
| Minor | Nickel chloride hexahydrate is grounded to anhydrous nickel dichloride. | The source ingredient is `NiCl2 x 6 H2O`; the generated row stores `CHEBI:34887` with label `nickel dichloride`. | Same normalized owner or ingredient grounding enrichment |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml`, replace flattened trace-element and vitamin rows with structured stock-solution additions at 10 ml and 1 ml.
2. Split the merged direct `NaCl` and `CaCl2 x 2 H2O` rows back into base-medium rows and trace-stock rows.
3. Represent ethanol as a 1.30 ml post-sterilization addition, not a `G_PER_L` direct ingredient.
4. Preserve base, trace-stock, and vitamin-stock distilled water rows.
5. Clear `CHEBI:34887` from `NiCl2 x 6 H2O` unless an exact nickel chloride hexahydrate grounding is available in the packaged ingredient index.

## Follow-up Checks

1. Run `just validate-schema`, `just validate-strict`, `just validate-terms`, and `just validate-references` on `data/normalized_yaml/bacterial/anaerotignum_neopropionicum_medium.yaml`.
2. Regenerate `data/merge_yaml/merged/ANAEROTIGNUM_NEOPROPIONICUM_MEDIUM.yaml`.
3. Re-open the regenerated merge and verify that trace metals and vitamins no longer appear as direct final-medium ingredients.

## Additional Notes

The exact identity search included ignored files and found no generated or maintained duplicates for this DSMZ Medium 318b record.
