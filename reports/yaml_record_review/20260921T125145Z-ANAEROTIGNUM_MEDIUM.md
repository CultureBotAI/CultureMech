# YAML Record Review: Anaerotignum Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ANAEROTIGNUM_MEDIUM.yaml
- Started UTC: 2026-09-21T12:50:29Z
- Finished UTC: 2026-09-21T12:51:45Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Path | `data/merge_yaml/merged/ANAEROTIGNUM_MEDIUM.yaml` |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:009303` |
| Name | `anaerotignum_medium` |
| Source accession | `TOGO:M2752` |
| Source label | `Anaerotignum Medium` |
| Generated status | Generated merge from `TOGO_M2752_Anaerotignum_Medium` |

The reviewed file is the generated merge for TOGO Medium M2752, a TOGO import sourced from `DSMZ_Medium156.pdf`. Its maintained owner is `data/normalized_yaml/bacterial/TOGO_M2752_Anaerotignum_Medium.yaml`; the generated record adds only merge metadata to that normalized input.

The exact, gitignore-independent identity search used `rg --no-ignore --hidden` across `data/normalized_yaml`, `data/merge_yaml/merged`, `scripts`, `tests`, and `history` for `TOGO_M2752_Anaerotignum_Medium`, `ANAEROTIGNUM_MEDIUM`, `Anaerotignum Medium`, `anaerotignum_medium`, `CultureMech:009303`, `TOGO:M2752`, `M2752`, `DSMZ_Medium156`, and `Medium156`. It found the maintained TOGO M2752 input, the reviewed generated merge, generated TOGO and recipe indexes, adjacent DSMZ / MediaDive Medium 156 records and variants, and unrelated medium numbers containing the `156` substring.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ANAEROTIGNUM_MEDIUM.yaml` | Passed with no issues reported |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ANAEROTIGNUM_MEDIUM.yaml --out /private/tmp/ANAEROTIGNUM_MEDIUM.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ANAEROTIGNUM_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were available |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ANAEROTIGNUM_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` recipe validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` inside one generated merge |

The documented `just` wrappers still fail before focused validation in this checkout because project `uv` resolves with Python 3.13 and attempts to build `llvmlite==0.46.0`, whose setuptools build aborts with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The no-project Python 3.11 commands above validate the generated record without building the project.

## Identity and Grounding

The record correctly identifies TOGO Medium M2752 by stable ID, source accession, label, category, and liquid complex-medium classification. The source note points to DSMZ Medium 156, and the rendered PDF is headed `156: ANAEROTIGNUM MEDIUM`.

The main formulation is source-backed, but three volume additions are misrepresented as `G_PER_L` solution rows. DSMZ lists 5.00 ml potassium phosphate buffer, 2.50 ml saturated aqueous calcium sulfate, and 0.50 ml sodium resazurin solution; the generated record stores them as gram-per-liter amounts, and the first remains in the direct ingredient list.

The `MgSO4 x 7 H2O` primary `term` was repaired to exact heptahydrate, but its `mediaingredientmech_chebi_term` still points to generic magnesium sulfate.

## Evidence

The generated record has no structured `references` or `source_data` block. I inspected the TOGO M2752 API payload and rendered `DSMZ_Medium156.pdf` directly with `mutool`.

Both sources support the direct base rows, the 1000 ml distilled water row, the 0.5 ml 0.1% sodium resazurin solution, 5.0 ml 1 M pH 7.1 potassium phosphate buffer, 2.5 ml saturated aqueous calcium sulfate, and final pH range 7.0-7.2.

TOGO imported DSMZ's comments for all preparation details:

- dissolve ingredients except bicarbonate and cysteine;
- adjust pH to 7.0;
- sparge with 100% N2 for 30-45 minutes;
- add and dissolve bicarbonate and cysteine;
- dispense under 100% N2 into anoxic Hungate-type tubes or serum vials;
- autoclave;
- adjust complete medium to pH 7.0-7.2 if necessary.

None of those comments are present as `preparation_steps`.

## Completeness

The core base composition is present, and optional strain-variant relationships are not expected for the standalone TOGO M2752 projection.

The consequential gaps are:

- no `preparation_steps`;
- no source-scoped pH 7.0 pre-sparging condition;
- no final pH 7.0-7.2 condition;
- no 100% N2 sparging or dispensing atmosphere;
- no anaerobic Hungate-tube or serum-vial vessel context;
- no true volume representation for the phosphate buffer, calcium sulfate, or sodium resazurin additions;
- no stable `SolutionRecipe` entries for sodium resazurin or saturated calcium sulfate.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | DSMZ and TOGO volume additions were stored as gram-per-liter values. | The source adds 5.00 ml potassium phosphate buffer, 2.50 ml saturated calcium sulfate solution, and 0.50 ml sodium resazurin solution. The generated record stores the first as a `5 G_PER_L` direct ingredient and the latter two as `2.5 G_PER_L` and `0.5 G_PER_L` solution entries. | `data/normalized_yaml/bacterial/TOGO_M2752_Anaerotignum_Medium.yaml` or the TOGO unit/solution importer |
| Major | `FeSO4 x 7 H2O` is inflated 1000-fold. | DSMZ Medium 156 and TOGO M2752 list 18.00 mg ferrous sulfate heptahydrate; the generated record stores `18 G_PER_L`. | Same normalized TOGO M2752 owner or TOGO unit importer |
| Major | Preparation and pH text was dropped. | TOGO carries DSMZ's pH 7.0, 30-45 minute 100% N2 sparge, bicarbonate/cysteine timing, anoxic dispensing, autoclaving, and final pH 7.0-7.2 comments; the generated record has no `preparation_steps` and no `ph_value`. | Same normalized TOGO M2752 owner or TOGO comment importer |
| Minor | The sodium resazurin and calcium sulfate solution rows still have default names and empty composition. | `solution-migrator-v1.0` created two solution entries, but `schema-defaulter-v1.0` later named both `Unknown solution`; both have `composition: []`. | Same normalized TOGO M2752 owner after source solution representation is fixed |
| Minor | The MediaIngredientMech CHEBI link for magnesium sulfate heptahydrate is stale. | The primary row term is exact `CHEBI:31795` magnesium sulfate heptahydrate, but `mediaingredientmech_chebi_term` remains generic `CHEBI:32599` magnesium sulfate. | Same normalized TOGO M2752 owner or the MgSO4 heptahydrate link fixer |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/TOGO_M2752_Anaerotignum_Medium.yaml` or the TOGO importer, preserve the phosphate buffer, sodium resazurin solution, and saturated calcium sulfate solution as milliliter additions.
2. Correct `FeSO4 x 7 H2O` from 18 g/L to the 18 mg amount stated by DSMZ.
3. Import the DSMZ preparation comments as ordered steps with pH 7.0, 100% N2 sparging, bicarbonate/cysteine addition timing, anoxic dispensing, autoclaving, and conditional final pH 7.0-7.2.
4. Replace default `Unknown solution` names with source labels and either link sodium resazurin and saturated calcium sulfate to true solution records or leave them as explicitly unresolved source solution additions.
5. Refresh `mediaingredientmech_chebi_term` for `MgSO4 x 7 H2O` so it no longer contradicts the repaired primary term.

## Follow-up Checks

1. Run `just validate-schema`, `just validate-strict`, `just validate-terms`, and `just validate-references` on `data/normalized_yaml/bacterial/TOGO_M2752_Anaerotignum_Medium.yaml`.
2. If importer code changes, add or update focused tests for DSMZ mg rows, milliliter solution additions, and TOGO comment import on M2752.
3. Regenerate `data/merge_yaml/merged/ANAEROTIGNUM_MEDIUM.yaml` and verify `FeSO4 x 7 H2O` is no longer `18 G_PER_L`.

## Additional Notes

The adjacent DSMZ / MediaDive Medium 156 merge for `anaerotignum_medium` is reviewed separately because it has a different stable ID, source accession, and variant topology. The TOGO public `/medium/M2752` route is not enough for source review, so the TOGO-side comparison used `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2752`.
