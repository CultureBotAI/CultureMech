# YAML Record Review: ANAEROMYXOBACTER-MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/anaeromyxobacter_medium.yaml
- Started UTC: 2026-09-21T12:48:31Z
- Finished UTC: 2026-09-21T12:50:29Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Path | `data/merge_yaml/merged/anaeromyxobacter_medium.yaml` |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:003948` |
| Name | `anaeromyxobacter_medium` |
| Source accession | `komodo.medium:1200` |
| Source label | `ANAEROMYXOBACTER-MEDIUM` |
| Generated status | Generated merge from `KOMODO_1200_ANAEROMYXOBACTER-MEDIUM` and `anaeromyxobacter_medium` |

The reviewed file is the generated canonical merge for KOMODO Medium 1200 and DSMZ / MediaDive Medium 1200. Its maintained owners are `data/normalized_yaml/bacterial/KOMODO_1200_ANAEROMYXOBACTER-MEDIUM.yaml` and `data/normalized_yaml/bacterial/anaeromyxobacter_medium.yaml`.

The exact, gitignore-independent identity search used `rg --no-ignore --hidden` across `data/normalized_yaml`, `data/merge_yaml/merged`, `scripts`, `tests`, and `history` for `KOMODO_1200_ANAEROMYXOBACTER-MEDIUM`, `ANAEROMYXOBACTER-MEDIUM`, `anaeromyxobacter_medium`, `CultureMech:003948`, `CultureMech:000650`, `komodo.medium:1200`, `mediadive.medium:1200`, `DSMZ_Medium1200`, and `Medium1200`. It found the two maintained source-duplicate records, their generated canonical merge, and generated KOMODO, MediaDive, bacterial, and recipe indexes.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/anaeromyxobacter_medium.yaml` | Passed with no issues reported |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/anaeromyxobacter_medium.yaml --out /private/tmp/anaeromyxobacter_medium.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/anaeromyxobacter_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were available |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/anaeromyxobacter_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` recipe validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` inside one generated merge |

The documented `just` wrappers still fail before focused validation in this checkout because project `uv` resolves with Python 3.13 and attempts to build `llvmlite==0.46.0`, whose setuptools build aborts with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The no-project Python 3.11 commands above validate the generated record without building the project.

## Identity and Grounding

The generated merge correctly identifies KOMODO Medium 1200 as a source duplicate of DSMZ / MediaDive Medium 1200. The direct DSMZ PDF is headed `1200. ANAEROMYXOBACTER-MEDIUM`, matching both maintained records.

The generated merge is incomplete relative to the DSMZ parent record because it drops `anaeromyxobacter_medium.yaml`'s only `preparation_steps` entry. The resulting generated file is a KOMODO-rooted record with a DSMZ duplicate link, but without the DSMZ procedure that explains the six solution additions and pH 7.2 adjustment.

The generated chemistry also conflates stock-solution composition with final medium composition. DSMZ Medium 1200 is organized as Solution A, B, C, D, E, F, Trace element solution SL-10 B, and Selenite and tungstate solution; the generated record stores their ingredients in one flat direct list.

The `Na2S x H2O` ingredient is grounded to anhydrous sodium sulfide, and `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride.

## Evidence

The generated record has no structured `references` or `source_data` block. I rendered `DSMZ_Medium1200.pdf` directly with `mutool`.

DSMZ Medium 1200 supports the source identity, final pH 7.2, separate preparation of Solutions A, B, and D under 80% N2 plus 20% CO2, autoclaving for those three solutions, filter sterilization and N2 outgassing for Solutions C, E, and F, the Solution B pH-adjustment addition, and the final additions of Solutions C, D, E, and F to each 10 ml of Solution A.

The source amounts that are inflated in the generated record are stock concentrations, not final-medium g/L values:

- Solution B is 2.5 g `NaHCO3` in 50 ml water, added at about 1 ml per 10 ml Solution A.
- Solution C is 385 mg DL-Dithiothreitol in 50 ml water, added at 0.2 ml per 10 ml Solution A.
- Solution D contains 37.5 mg L-Cysteine and 40 mg `Na2S x H2O` in 50 ml water, added at 0.2 ml per 10 ml Solution A.
- Solution E contains 4.0 g disodium fumarate in 50 ml water, added at 0.05 ml per 10 ml Solution A.
- Solution F is a 1000 ml vitamin stock, added at 0.2 ml per 10 ml Solution A.
- Trace element solution SL-10 B and Selenite and tungstate solution are source stock solutions, not final direct rows.

## Completeness

The duplicate relationship between KOMODO 1200 and DSMZ Medium 1200 is present, and the DSMZ `ph_value: 7.2` is present.

The consequential gaps are:

- no generated preparation step;
- no structured Solution A, B, C, D, E, or F;
- no structured Trace element solution SL-10 B;
- no structured Selenite and tungstate solution;
- no final volume additions for Solutions B through F;
- no water rows for any solution;
- no stock context for HCl, NaOH, trace metals, selenite/tungstate, or vitamin rows.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The generated merge drops the DSMZ preparation step. | `anaeromyxobacter_medium.yaml` includes the DSMZ step for anaerobic/autoclaved Solution A, B, and D preparation, filter-sterilized Solution C/E/F preparation, and final addition ratios; the generated source-duplicate merge omits `preparation_steps`. | Merge regeneration/rules plus `data/normalized_yaml/bacterial/KOMODO_1200_ANAEROMYXOBACTER-MEDIUM.yaml` if the KOMODO child must carry inherited prep explicitly |
| Major | Solution B, C, D, E, and F stock contents are flattened into direct ingredients. | DSMZ adds small volumes of Solutions B-F per 10 ml Solution A. The generated record stores stock concentrations such as `NaHCO3` at `50 G_PER_L`, DL-Dithiothreitol at `7.7 G_PER_L`, and disodium fumarate at `80 G_PER_L` as direct ingredients. | Both maintained normalized inputs or the DSMZ/MediaDive resolver that copied Medium 1200 |
| Major | Trace element solution SL-10 B is flattened. | DSMZ defines SL-10 B as a 1000 ml stock with HCl, ferrous sulfate, zinc, manganese, borate, cobalt, copper, nickel, and molybdate salts. Those rows appear as final direct ingredients in the generated medium. | Both maintained normalized inputs or the stock-solution resolver |
| Major | Selenite and tungstate solution is flattened. | DSMZ defines a 1000 ml stock containing 0.5 g NaOH, 3.0 mg sodium selenite pentahydrate, and 4.0 mg sodium tungstate dihydrate; all three appear as direct ingredients. | Same maintained owner set |
| Major | Vitamin stock components are flattened. | DSMZ adds 0.2 ml Solution F per 10 ml Solution A; the generated medium emits each vitamin as a direct g/L ingredient. | Same maintained owner set |
| Minor | Hydrated sulfide and nickel salts are grounded imprecisely. | The source names `Na2S x H2O` and `NiCl2 x 6 H2O`; the generated record stores anhydrous sodium sulfide and anhydrous nickel dichloride. | Same maintained owner set or ingredient grounding enrichment |

## Recommended Edits

1. Preserve DSMZ Solutions A-F, Trace element solution SL-10 B, and Selenite and tungstate solution as structured solution records in `data/normalized_yaml/bacterial/anaeromyxobacter_medium.yaml`; propagate the same structure into the KOMODO duplicate or ensure the merge inherits it.
2. Replace flattened stock concentrations with source volume additions: about 1 ml B, 0.2 ml C, 0.2 ml D, 0.2 ml F, and 0.05 ml E per 10 ml A.
3. Regenerate `data/merge_yaml/merged/anaeromyxobacter_medium.yaml` and verify the DSMZ preparation step is retained in the KOMODO-rooted canonical merge.
4. Preserve all DSMZ water rows inside their owning solution records.
5. Clear anhydrous groundings from `Na2S x H2O` and `NiCl2 x 6 H2O` unless exact hydrate groundings are available in the packaged ingredient index.

## Follow-up Checks

1. Run `just validate-schema`, `just validate-strict`, `just validate-terms`, and `just validate-references` on both maintained normalized records.
2. Run `just verify-merges` after regeneration and confirm the source-duplicate merge still links `CultureMech:003948` and `CultureMech:000650`.
3. Re-open the regenerated merge and verify that high-concentration stock-only rows such as `NaHCO3 50 G_PER_L` and `Disodium fumarate 80 G_PER_L` are gone from direct ingredients.

## Additional Notes

No missing same-source normalized record was found: the exhaustive exact search found one KOMODO 1200 child and one DSMZ / MediaDive 1200 parent for ANAEROMYXOBACTER-MEDIUM.
