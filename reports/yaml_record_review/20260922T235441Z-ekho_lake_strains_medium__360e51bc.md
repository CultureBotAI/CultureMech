# YAML Record Review: EKHO LAKE STRAINS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ekho_lake_strains_medium__360e51bc.yaml
- Started UTC: 2026-09-22T23:48:00Z
- Finished UTC: 2026-09-22T23:54:41Z
- Verdict: needs curation

## Target

- Reviewed record: `data/merge_yaml/merged/ekho_lake_strains_medium__360e51bc.yaml`
- Class: `MediaRecipe`
- ID: `CultureMech:001753`
- Name: `ekho_lake_strains_medium`
- Original label: `EKHO LAKE STRAINS MEDIUM`
- Category: `bacterial`
- Medium term: `mediadive.medium:621a` / `DSMZ Medium 621a`
- Generated status: generated merge record with fingerprint `360e51bcbdf74f928274c4a0ce3147ce627f3da9e5eb970ec2d6dd41866be836`
- Maintained owner for future edits: `data/normalized_yaml/bacterial/ekho_lake_strains_medium.yaml`

The merge record adds only the `merge_recipes.py` history entry, `merge_fingerprint`, and `merged_from` metadata on top of the maintained normalized record.

## Validation

Focused validation was clean.

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ekho_lake_strains_medium__360e51bc.yaml` | Passed; `No issues found`. |
| Strict schema wrapper | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ekho_lake_strains_medium__360e51bc.yaml --out /private/tmp/ekho_lake_strains_medium__360e51bc.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ekho_lake_strains_medium__360e51bc.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 reference checks, all validations passed. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ekho_lake_strains_medium__360e51bc.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; the run emitted the expected `eutils` / `pkg_resources` deprecation warning. |
| Embedded history | `just validate-history` | Not checked: the documented history validator validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

The record denotes DSMZ Medium 621a, `EKHO LAKE STRAINS MEDIUM`. The DSMZ 621a PDF, MediaDive `621a` REST response, KOMODO `621a`, and TOGO M1572 all point at the same DSMZ medium.

The high-level fields are source-aligned: DSMZ 621a is a solid agar recipe with pH 7.2-7.4, and the reviewed record preserves that `ph_range`.

Most CHEBI terms are chemically aligned for the ingredient names present. The major issue is not ontology identity; it is that ingredients from Artificial sea water, Mineral salt solution, Vitamin solution, and Metall salt sol. 44 have been moved into the final medium at stock concentrations.

## Evidence

DSMZ 621a is an overlay on DSMZ 621: prepare DSMZ 621 but use Artificial sea water instead of the 965 ml distilled-water line. DSMZ/MediaDive model the final 621a main medium as 20 ml Mineral salt solution, 0.25 g Bacto peptone, 0.25 g Bacto yeast extract, 15 g Bacto agar, 965 ml Artificial sea water, 10 ml sterile-filtered 2.5 percent glucose solution, and 5 ml Vitamin solution at double concentration.

The inspected nested stocks are:

- Artificial sea water is a 1 L stock containing NaCl, Na2SO4, MgCl2 x 6 H2O, CaCl2, NaHCO3, KCl, KBr, H3BO3, SrCl2, and NaF.
- Mineral salt solution is a 1 L stock containing NTA, MgSO4 x 7 H2O, CaCl2 x 2 H2O, Na2MoO4 x 2 H2O, FeSO4 x 7 H2O, 50 ml Metall salt sol. 44, and water.
- Vitamin solution is a double-concentration 1 L stock added at 5 ml/L and containing nine vitamin rows.
- Metall salt sol. 44 is defined by DSMZ 590 as a 1 L stock with Na-EDTA, ZnSO4 x 7 H2O, FeSO4 x 7 H2O, MnSO4 x H2O, CuSO4 x 5 H2O, Co(NO3)2 x 6 H2O, Na2B4O7 x 10 H2O, and water.

The reviewed record flattens the sea-water salts, Mineral salt solution components, and double-strength vitamin stock rows into top-level ingredients. The YAML keeps a `solutions` entry for `Metall salt sol. 44`, but the entry is empty and has `50 G_PER_L` rather than representing 50 ml of Metall salt sol. 44 inside the Mineral salt solution stock.

## Completeness

The main Bacto peptone, Bacto yeast extract, Bacto agar, and final glucose amounts are recoverable, although the Bacto and sterile-filtered 2.5 percent glucose source qualifiers are not structured.

The record is materially incomplete for stock structure. A user following the current ingredient table would add 100 percent artificial sea water salts instead of 965 ml/L Artificial sea water, add Mineral salt solution salts at stock strength instead of a 20 ml/L stock addition, add double-strength vitamins at stock strength instead of a 5 ml/L post-autoclave addition, and never learn the composition of Metall salt sol. 44.

Exact local discovery used `find`, which includes ignored files, and found the expected sibling source records `data/normalized_yaml/bacterial/KOMODO_621a_EKHO_LAKE_STRAINS_medium.yaml` and `data/normalized_yaml/bacterial/TOGO_M1572_Ekho_Lake_Strains_Medium.yaml`. Neither sibling changes the DSMZ 621a identity or resolves the missing stock boundaries in this direct DSMZ import.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| major | Artificial sea water is flattened into final ingredients. | DSMZ 621a substitutes 965 ml Artificial sea water for the distilled water in DSMZ 621; the reviewed record lists the ASW salts as ordinary final `G_PER_L` rows and loses the 965 ml stock boundary. | `data/normalized_yaml/bacterial/ekho_lake_strains_medium.yaml` |
| major | Mineral salt solution is flattened at stock strength. | DSMZ 621/MediaDive add 20 ml Mineral salt solution per liter; the reviewed record lists NTA, MgSO4 x 7 H2O, CaCl2 x 2 H2O, Na2MoO4 x 2 H2O, and FeSO4 x 7 H2O at the stock's g/L values. | `data/normalized_yaml/bacterial/ekho_lake_strains_medium.yaml` |
| major | Vitamin solution is flattened at stock strength. | DSMZ 621/621a add 5 ml double-concentration Vitamin solution after cooling; the reviewed record lists each vitamin at the 1 L stock concentration rather than under a 5 ml/L stock addition. | `data/normalized_yaml/bacterial/ekho_lake_strains_medium.yaml` |
| major | `Metall salt sol. 44` is an empty gram-per-liter solution. | DSMZ 621 adds 50 ml Metall salt sol. 44 to the Mineral salt solution stock and DSMZ 590 defines its composition; the reviewed record has an empty `solutions` entry with `value: '50'`, `unit: G_PER_L`. | `data/normalized_yaml/bacterial/ekho_lake_strains_medium.yaml` |
| minor | Source-specific ingredient qualifiers were dropped. | DSMZ calls the main complex ingredients Bacto peptone, Bacto yeast extract, and Bacto agar, and adds glucose as 10 ml of a sterile-filtered 2.5 percent solution; the reviewed record stores only generic peptone, yeast extract, agar, and final glucose. | `data/normalized_yaml/bacterial/ekho_lake_strains_medium.yaml` |

## Recommended Edits

1. Rebuild `data/normalized_yaml/bacterial/ekho_lake_strains_medium.yaml` around solution additions: 20 ml Mineral salt solution, 965 ml Artificial sea water, 10 ml sterile-filtered glucose solution, and 5 ml double-concentration Vitamin solution.
2. Move Artificial sea water, Mineral salt solution, Vitamin solution, and Metall salt sol. 44 component lists into their own nested solution records.
3. Populate Metall salt sol. 44 from DSMZ Medium 590 / MediaDive medium 590 instead of leaving it as an empty solution.
4. Preserve Bacto and sterile-filtered glucose qualifiers in structured notes or source fields.
5. Regenerate merged YAML and downstream pages.

## Follow-up Checks

1. Rerun LinkML schema, strict schema, reference, and term validation on the regenerated `data/merge_yaml/merged/ekho_lake_strains_medium__360e51bc.yaml`.
2. Reopen DSMZ Medium 621a, DSMZ Medium 621, DSMZ Medium 590, and MediaDive 621a and manually verify every solution volume and stock composition.
3. Inspect the generated page to confirm the final medium shows stock additions first and stock-strength ASW, mineral, vitamin, and Metals 44 components only within their solution sections.

## Additional Notes

- The DSMZ PDF spells Artificial Sea Water as `Artifical` in several places; this review uses the MediaDive spelling when naming the stock and does not treat that typo as a record defect.
