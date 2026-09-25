# YAML Record Review: Anaerolinea Medium-B

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/anaerolinea_medium_b.yaml
- Started UTC: 2026-09-21T12:39:44Z
- Finished UTC: 2026-09-21T12:42:20Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Path | `data/merge_yaml/merged/anaerolinea_medium_b.yaml` |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:009821` |
| Name | `anaerolinea_medium_b` |
| Source accession | `TOGO:M435` |
| Source label | `Anaerolinea Medium-B` |
| Generated status | Generated merge from `TOGO_M435_Anaerolinea_Medium-B` |

The reviewed file is the generated merge for the TOGO import of JCM Medium 435. Its maintained owner is `data/normalized_yaml/bacterial/TOGO_M435_Anaerolinea_Medium-B.yaml`; the generated record adds only merge metadata to that normalized input.

The exact, gitignore-independent identity search used `rg --no-ignore --hidden` across `data/normalized_yaml`, `data/merge_yaml/merged`, `scripts`, `tests`, and `history` for `TOGO_M435_Anaerolinea_Medium-B`, `Anaerolinea Medium-B`, `anaerolinea_medium_b`, `CultureMech:009821`, `TOGO:M435`, and `M435`. It found the maintained TOGO input, the reviewed generated merge, generated TOGO and recipe indexes, generated merge-index references, and an adjacent MediaDive/JCM `data/normalized_yaml/bacterial/anaerolinea_medium_b.yaml` record with stable ID `CultureMech:002786` and source accession `mediadive.medium:J435`.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/anaerolinea_medium_b.yaml` | Passed with no issues reported |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/anaerolinea_medium_b.yaml --out /private/tmp/anaerolinea_medium_b.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/anaerolinea_medium_b.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were available |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/anaerolinea_medium_b.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` recipe validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` inside one generated merge |

The documented `just` wrappers still fail before focused validation in this checkout because project `uv` resolves with Python 3.13 and attempts to build `llvmlite==0.46.0`, whose setuptools build aborts with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The no-project Python 3.11 commands above validate the generated record without building the project.

## Identity and Grounding

The CultureMech record correctly identifies the TOGO M435 import of JCM Medium 435 by stable ID, source accession, label, category, and liquid complex-medium classification.

The source identity is version-conflicted. The TOGO API for M435 reports `original_media_id: JCM_M435` and preserves an older structured formulation with M435-local Solution A, M435-local Solution B, 3% L-cysteine and sodium sulfide stock additions, three cross-referenced M278 trace stocks, and comments for strains JCM 10971 and JCM 12579. The direct JCM `GRMD=435` page fetched during review exposes only recipe 435, `ANAEROLINEA MEDIUM-B`, as a Medium 284-derived recipe for JCM 12579: use Solution A of Medium No. 284 supplemented with final 1.0 ml Trace vitamins solution and 1.0 g yeast extract in 1.0 L distilled water, then add 0.01 volume each of 3% L-cysteine and sodium sulfide solutions before inoculation.

The generated record therefore matches the TOGO API's label and source accession, but not the current JCM formula served from the record's own `Original URL`.

## Evidence

The generated record has no structured `references` or `source_data` block. I inspected the TOGO M435 API payload and the direct JCM `GRMD=435` page.

The old TOGO payload supports these imported facts:

- the label `Anaerolinea Medium-B`;
- `JCM_M435` as the original medium ID and the JCM `GRMD=435` URL as the original URL;
- a main M435 assembly from 900 ml Solution A, 100 ml Solution B, 10 ml of 3% `L--cysteine HCl H2O`, 10 ml of 3% `Na2S x 9H2O`, and an N2 headspace;
- Solution A containing 900 ml distilled water, the calcium, phosphate, ammonium, magnesium, bicarbonate, 1 mg resazurin, 1 g yeast extract, 1 ml Trace vitamins solution from M278, 1 ml Trace element solution from M278, 1 ml Se/W solution from M278, and an N2-CO2 gas phase;
- Solution B containing 100 ml distilled water, 2.2 g sodium pyruvate, and an N2 gas phase;
- preparation comments for Solution A pH 6.5, Solution B pH 7.0 plus filter sterilization, Solution A/Solution B assembly, anaerobic post-sterilization reductant additions, a 10% inoculum note for JCM 10971, and an alternate Medium 284-derived JCM 12579 recipe.

The current JCM page supports only the JCM 12579 Medium 284-derived recipe and a 2% inoculum note for JCM 12579. The TOGO payload still carries enough structured text to prove the importer lost or distorted several claims before this generated merge was built.

## Completeness

The root `TOGO:M435` identity is present, and the simple M435-local salts are mostly present with exact chemical grounding.

The consequential gaps are:

- no representation of the current JCM Medium 435 formula served from the record's own JCM URL;
- no `preparation_steps` at all;
- no pH 6.5 preparation condition for Solution A;
- no pH 7.0 preparation condition for Solution B;
- no filter-sterilization instruction for Solution B;
- no anaerobic post-sterilization addition instruction for the 3% L-cysteine and sodium sulfide stocks;
- no JCM 10971 10% inoculum note from the old TOGO payload;
- no JCM 12579 2% inoculum note from the current JCM page;
- no internal composition for the M435-local Solution A and Solution B stocks;
- no resolved composition for the three M278 cross-referenced trace stocks;
- no stable identifiers for the three M278 stock-solution references;
- no non-default names for any of the six generated solution entries.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The generated TOGO M435 record is stale relative to the current original JCM page. | The generated record carries the old TOGO API's M435-local Solution A and B formulation. The direct `GRMD=435` page now lists only a Medium 284-derived ANAEROLINEA MEDIUM-B recipe for JCM 12579. | `data/normalized_yaml/bacterial/TOGO_M435_Anaerolinea_Medium-B.yaml` or the TOGO importer/cache that owns M435 source refresh |
| Major | Stock-solution volumes were converted to `G_PER_L` quantities. | The TOGO payload adds 10 ml of 3% sodium sulfide solution, 10 ml of 3% L-cysteine solution, 1 ml each of three M278 trace stocks, 900 ml Solution A, and 100 ml Solution B. The generated record stores these six solution amounts as `10`, `1`, `900`, or `100` `G_PER_L`; L-cysteine was left as a direct ingredient. | `data/normalized_yaml/bacterial/TOGO_M435_Anaerolinea_Medium-B.yaml` or the TOGO unit/solution importer |
| Major | Solution A and Solution B point at the wrong stock identities. | The old TOGO M435 payload defines M435-local Solution A and Solution B in the same source record. The generated rows instead ground them to `mediadive.solution:5342` and `mediadive.solution:5343`, with notes that refer to `mediadive_5342_Solution_A.yaml` and `mediadive_5343_Solution_B.yaml`. | Same TOGO M435 normalized record or cross-source solution-linking importer |
| Major | Preparation and condition text was dropped. | The TOGO payload gives pH adjustment, boiling, N2-CO2 cooling, bicarbonate addition, anaerobic dispensing, autoclaving, overnight standing, Solution B filter sterilization, final Solution B addition, and post-sterilization reductant addition steps. The generated record has no `preparation_steps`. | Same TOGO M435 normalized record or TOGO comment importer |
| Major | Quantities inside sub-solutions lost their original dimensions and boundaries. | TOGO lists 900 ml water in Solution A and 100 ml water in Solution B, but the generated direct water row is `1000.0 G_PER_L`; TOGO lists 1 mg resazurin in Solution A, but the generated direct row is `1 G_PER_L`. | Same TOGO M435 normalized record or TOGO unit importer |
| Minor | Gas rows are duplicated and underspecified. | The old TOGO payload distinguishes N2 in the main assembly, an N2-CO2 gas phase for Solution A, and N2 for Solution B. The generated direct ingredients contain separate `N2`, `Carbon dioxide gas`, and `Nitrogen gas` rows without their solution or atmosphere context. | Same TOGO M435 normalized record or TOGO gas importer |
| Minor | Every generated solution carries a default name. | The `solution-migrator` produced six real solution entries, but `schema-defaulter-v1.0` later filled all six as `name: Unknown solution`. | Same TOGO M435 normalized record after the solution importer preserves explicit names |

## Recommended Edits

1. Reconcile M435 against the current JCM `GRMD=435` page before correcting individual amounts; either refresh the TOGO M435 import to the current Medium 284-derived recipe or preserve the older TOGO formulation as a versioned/source-specific variant with an explicit source snapshot.
2. In `data/normalized_yaml/bacterial/TOGO_M435_Anaerolinea_Medium-B.yaml` or the TOGO importer, keep the 10 ml and 1 ml stock additions as volume additions to named solutions, not as direct `G_PER_L` ingredients.
3. Replace `mediadive.solution:5342` and `mediadive.solution:5343` on TOGO M435's Solution A and Solution B with structured M435-local solution records, if the older TOGO formulation is retained.
4. Import TOGO and JCM preparation comments into ordered `preparation_steps`, including Solution A and B pH values, Solution B filter sterilization, autoclaving, overnight standing, anaerobic gas handling, and post-sterilization L-cysteine and sodium sulfide additions.
5. Preserve water and milligram units within their source solution boundaries; in particular, prevent 900 ml plus 100 ml water from merging into direct `1000.0 G_PER_L` and prevent 1 mg resazurin from becoming `1 G_PER_L`.
6. Scope N2 and CO2 gas rows to the relevant main or sub-solution stage instead of emitting three indistinguishable direct ingredients.
7. Give each solution its source label in `name` and clear the `Unknown solution` defaults.

## Follow-up Checks

1. Run `just validate-schema`, `just validate-strict`, `just validate-terms`, and `just validate-references` on `data/normalized_yaml/bacterial/TOGO_M435_Anaerolinea_Medium-B.yaml`.
2. If the TOGO importer changes, run the focused importer tests that cover solution parsing, volume units, milligram units, and comment-to-preparation mapping.
3. Regenerate `data/merge_yaml/merged/anaerolinea_medium_b.yaml` and verify that stock additions retain `ml`, that resazurin is not inflated by 1000-fold, and that M435-local Solution A/B no longer reference MediaDive solution IDs.
4. Re-open the current JCM `GRMD=435` page and compare it with the refreshed record so the generated merge no longer contradicts its own original URL.

## Additional Notes

The adjacent MediaDive/JCM `data/normalized_yaml/bacterial/anaerolinea_medium_b.yaml` record already models the current JCM 12579 text as a Medium 284-derived formulation, although its inherited Medium 284 expansion and `SOURCE_DUPLICATE` relation need their own separate review. I used it only to disambiguate the similarly named record and did not treat it as independent evidence for the TOGO import.

The direct JCM page fetched during review is an HTML source page for medium no. 435, not a search snippet. The TOGO public `/medium/M435` route returned only an application shell, so the source-data comparison used `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M435`.
