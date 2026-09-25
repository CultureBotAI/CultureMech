# YAML Record Review: Anaerolinea Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/anaerolinea_medium__d79e886b.yaml
- Started UTC: 2026-09-21T12:46:50Z
- Finished UTC: 2026-09-21T12:48:31Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Path | `data/merge_yaml/merged/anaerolinea_medium__d79e886b.yaml` |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:009042` |
| Name | `anaerolinea_medium` |
| Source accession | `TOGO:M2464` |
| Source label | `Anaerolinea Medium` |
| Generated status | Generated merge from `TOGO_M2464_Anaerolinea_Medium` |

The reviewed file is the generated merge for TOGO Medium M2464, a TOGO import sourced from `DSMZ_Medium1004.pdf`. Its maintained owner is `data/normalized_yaml/bacterial/TOGO_M2464_Anaerolinea_Medium.yaml`.

The exact, gitignore-independent identity search used `rg --no-ignore --hidden` across `data/normalized_yaml`, `data/merge_yaml/merged`, `scripts`, `tests`, and `history` for `TOGO_M2464_Anaerolinea_Medium`, `anaerolinea_medium__d79e886b`, `CultureMech:009042`, `TOGO:M2464`, `M2464`, `DSMZ_Medium1004`, and `Medium1004`. It found the maintained TOGO M2464 input, the reviewed generated merge, generated TOGO and recipe indexes, the DSMZ-owned `anaerolinea_medium.yaml`, and the sibling TOGO M2232 generated merge and normalized record.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/anaerolinea_medium__d79e886b.yaml` | Passed with no issues reported |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/anaerolinea_medium__d79e886b.yaml --out /private/tmp/anaerolinea_medium__d79e886b.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/anaerolinea_medium__d79e886b.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were available |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/anaerolinea_medium__d79e886b.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` recipe validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` inside one generated merge |

The documented `just` wrappers still fail before focused validation in this checkout because project `uv` resolves with Python 3.13 and attempts to build `llvmlite==0.46.0`, whose setuptools build aborts with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The no-project Python 3.11 commands above validate the generated record without building the project.

## Identity and Grounding

The record correctly identifies TOGO Medium M2464 by stable ID, source accession, label, category, and liquid complex-medium classification. Its source note points to DSMZ Medium 1004, whose PDF is headed `1004: ANAEROLINEA MEDIUM`.

The generated merge is stale relative to the maintained TOGO input. `data/normalized_yaml/bacterial/TOGO_M2464_Anaerolinea_Medium.yaml` has a 2026-09-02 `REPAIRED_SUMMED_DUPLICATE_MERGE` event and a corrected `Distilled water` value of `1000.0`; the generated merge still stores `4000.0 G_PER_L`.

TOGO M2464 is lossy relative to DSMZ Medium 1004 in the same places as TOGO M2232: the API changes the bicarbonate pH instruction to pH 7.0 instead of DSMZ's pH 6.4-6.8, and it omits all DSMZ strain-specific modifications for DSM 16554/16555/17877, DSM 16556, DSM 22659, DSM 23815, and DSM 103421.

The `NiCl2 x 6 H2O` ingredient is grounded to anhydrous `CHEBI:34887` nickel dichloride instead of exact nickel chloride hexahydrate.

## Evidence

The generated record has no structured `references` or `source_data` block. I inspected the TOGO M2464 API payload and rendered `DSMZ_Medium1004.pdf` directly with `mutool`.

Both source paths support the base ANAEROLINEA MEDIUM identity, final volume 1003 ml, final pH 7.0, the direct DSMZ base ingredient rows, and 1 ml Trace element solution SL-11, 1 ml Selenite-tungstate solution, 0.5 ml sodium resazurin solution, and 10 ml Wolin vitamin solution stock additions.

The rendered DSMZ PDF additionally supports the preparation and variant details that the TOGO projection did not preserve: 30-45 minutes of sparging with 80% N2 / 20% CO2, pH 6.4-6.8 after bicarbonate, Hungate or serum-vial dispensing under 80% N2 / 20% CO2, post-autoclave filtered/anoxic additions, conditional final pH adjustment to 7.0, the full SL-11, Selenite-tungstate, and Wolin-vitamin stock recipes, and the five DSM strain-specific formula changes.

## Completeness

The generated record preserves the base DSMZ direct ingredient identities but loses the protocol and stock-solution structure needed to follow the recipe.

The consequential gaps are:

- no `preparation_steps`;
- no DSMZ pH 6.4-6.8 base-medium condition;
- no 80:20 N2/CO2 sparging or 100% N2 stock-preparation context;
- no post-autoclave addition scope for yeast extract, vitamins, glucose, sulfide, and cysteine;
- no DSMZ strain-specific variants or quality flags for the five formula changes;
- no stock-solution composition for Na-resazurin, SL-11, Selenite-tungstate, or Wolin vitamin solution;
- no regenerated 1000 ml water value from the maintained 2026-09-02 repair.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The generated merge is stale relative to the maintained normalized record. | The maintained M2464 input was repaired on 2026-09-02 and stores `Distilled water` at `1000.0`; the generated merge still stores `4000.0 G_PER_L`. | Regenerate `data/merge_yaml/merged/anaerolinea_medium__d79e886b.yaml` from `data/normalized_yaml/bacterial/TOGO_M2464_Anaerolinea_Medium.yaml` |
| Major | Three DSMZ stock solutions are flattened into direct ingredients. | DSMZ adds SL-11, Selenite-tungstate solution, and Wolin's vitamin solution to the base medium as stock additions. The generated record emits their component salts and vitamins as direct final-medium rows. | `data/normalized_yaml/bacterial/TOGO_M2464_Anaerolinea_Medium.yaml` or the TOGO DSMZ importer |
| Major | Milligram stock quantities are inflated to gram-per-liter direct amounts. | DSMZ lists many stock components in mg per 1000 ml stock; generated examples include `Na2MoO4 x 2 H2O` at `36 G_PER_L`, `Na2SeO3 x 5 H2O` at `3 G_PER_L`, and `Vitamin B12` at `0.1 G_PER_L`. | Same normalized TOGO M2464 owner or unit importer |
| Major | Preparation and pH evidence is dropped or contradicted. | DSMZ gives pH 6.4-6.8 after bicarbonate and a complete anoxic/autoclave/post-autoclave workflow. The generated record has no `preparation_steps`, and TOGO M2464's extracted comment changes the bicarbonate pH to 7.0. | Same normalized TOGO M2464 owner or TOGO comment extraction |
| Major | DSMZ strain-specific variants are absent. | DSMZ Medium 1004 lists five formula-changing strain instructions, but the TOGO M2464 record has only the base recipe. | Same normalized TOGO M2464 owner or new normalized strain-variant records |
| Minor | Sodium hydroxide used for stock pH adjustment is represented as a medium ingredient. | DSMZ names NaOH in the SL-11 and Selenite-tungstate stock contexts; the generated record has a standalone variable `NaOH` ingredient. | Same normalized TOGO M2464 owner after preparation/stock repair |
| Minor | Nickel chloride hexahydrate is grounded to anhydrous nickel dichloride. | DSMZ lists `NiCl2 x 6 H2O`; the generated row stores `CHEBI:34887` with label `nickel dichloride`. | Same normalized TOGO M2464 owner or ingredient grounding enrichment |

## Recommended Edits

1. Regenerate the generated merge from `data/normalized_yaml/bacterial/TOGO_M2464_Anaerolinea_Medium.yaml` so the 2026-09-02 water repair reaches `data/merge_yaml/merged/anaerolinea_medium__d79e886b.yaml`.
2. In the normalized TOGO M2464 owner or importer, preserve DSMZ's Na-resazurin, SL-11, Selenite-tungstate, and Wolin-vitamin stock additions at their stated milliliter amounts.
3. Move stock components out of the base direct ingredient list and preserve milligram units inside the stock recipes.
4. Import DSMZ preparation steps and keep pH 6.4-6.8 distinct from conditional final pH 7.0.
5. Add explicit representation for the five DSMZ strain-specific formula changes or flags that name the missing variants.
6. Keep NaOH scoped to stock pH adjustment rather than a final-medium ingredient.
7. Clear `CHEBI:34887` from `NiCl2 x 6 H2O` unless an exact nickel chloride hexahydrate grounding is available in the packaged ingredient index.

## Follow-up Checks

1. Run `just validate-schema`, `just validate-strict`, `just validate-terms`, and `just validate-references` on `data/normalized_yaml/bacterial/TOGO_M2464_Anaerolinea_Medium.yaml`.
2. If importer code changes, add or update focused tests for TOGO M2464 stock parsing, pH comment extraction, and milligram preservation.
3. Regenerate `data/merge_yaml/merged/anaerolinea_medium__d79e886b.yaml` and verify that `Distilled water` is no longer `4000.0 G_PER_L`.
4. Re-open the regenerated merge and verify that DSMZ stock components no longer appear as direct final-medium ingredients.

## Additional Notes

M2464 is a duplicate TOGO import of the same DSMZ Medium 1004 source reviewed for TOGO M2232 and for the DSMZ/KOMODO `ANAEROLINEA_MEDIUM.yaml` family. It should be reconciled through its own maintained TOGO owner or source importer, then regenerated.

The TOGO public `/medium/M2464` route is not enough for source review, so the TOGO-side comparison used `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2464`.
