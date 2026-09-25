# YAML Record Review: Artificial Soil Agar

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/ARTIFICIAL_SOIL_AGAR.yaml`
- Started UTC: 2026-09-21T15:30:50Z
- Finished UTC: 2026-09-21T15:30:58Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:008896` |
| Name | `artificial_soil_agar` |
| Original name | Artificial Soil Agar |
| Category | `bacterial` |
| Source identity | `TOGO:M230`, JCM `JCM_M238` |
| Generated status | Generated single-source merge of `data/normalized_yaml/bacterial/TOGO_M230_Artificial_Soil_Agar.yaml` |

This generated record is the TOGO-derived Artificial Soil Agar import. The
MediaDive/JCM `J238` sibling,
`data/normalized_yaml/bacterial/artificial_soil_agar.yaml`, is a separate record
and should not receive fixes for this `TOGO:M230` merge.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ARTIFICIAL_SOIL_AGAR.yaml` | Passed; no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ARTIFICIAL_SOIL_AGAR.yaml --out /private/tmp/ARTIFICIAL_SOIL_AGAR.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ARTIFICIAL_SOIL_AGAR.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ARTIFICIAL_SOIL_AGAR.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: no focused embedded `MediaRecipe.curation_history` validator is documented for one generated merge record; `just validate-history` targets standalone records under `history/`. |

The documented `just` validator entrypoints were not used because project `uv`
fails while building `llvmlite==0.46.0` under Python 3.13 before the requested
target-specific check runs. The no-project commands above ran the focused
validators successfully.

## Identity and Grounding

The CultureMech ID, TOGO ID, JCM original ID, category, and label all identify
the TOGO Artificial Soil Agar import. TOGO `M230` resolves to JCM `M238` and pH
6.6-6.8. The live JCM `GRMD=238` page returned "Nothing found", so source-level
formulation verification used TOGO's structured payload.

Most simple salts are grounded to the exact hydrate or salt represented in the
TOGO source. `Soil extract (see below)`, `tap water`, and `leafy soil` should
not remain variable direct medium ingredients: the source presents a 50 ml soil
extract addition and a separate preparation note for equal volumes of leafy soil
and tap water.

## Evidence

TOGO `M230` reports a main recipe with 950 ml distilled water, 0.7 g MgSO4.7H2O,
0.1 g yeast extract, 5 mg K2HPO4, 0.2 g NaHCO3, 1 mg FeCl3.6H2O, 1.01 g
CaSO4.2H2O, 0.49 g Ca(NO3)2.4H2O, 25 mg K2SO4, 10 mg glucose, 15 g agar, and
50 ml soil extract. It also reports pH 6.6-6.8 and says the soil extract is
made by boiling equal volumes of leafy soil and tap water for 2 hours, then
clearing by centrifugation.

The generated record changes several of those claims:

| Current row | Source row |
|---|---|
| `K2HPO4`, `5 G_PER_L` | 5 mg |
| `FeCl3.6H2O`, `1 G_PER_L` | 1 mg |
| `K2SO4`, `25 G_PER_L` | 25 mg |
| `Glucose`, `10 G_PER_L` | 10 mg |
| `Soil extract (see below)`, `50 G_PER_L` | 50 ml |
| `tap water`, variable direct ingredient | stock/extract preparation material |
| `leafy soil`, variable direct ingredient | stock/extract preparation material |

## Completeness

The record is missing:

- pH 6.6-6.8;
- the 50 ml soil-extract addition as a volume;
- the soil-extract preparation boundary;
- the boil-for-2-hours extraction step; and
- clearing the extract by centrifugation.

Optional target-organism and growth-evidence slots are empty. I did not flag
that as a defect because the inspected TOGO payload only establishes the recipe
and preparation.

Before reporting raw-source absence, I searched for `CultureMech:008896`,
`M230`, `JCM_M238`, and `Artificial Soil Agar` with `rg --no-ignore --hidden`
across `data`, `scripts`, `history`, `src`, `reports`, and `references_cache`.
The exact `M230` query also matched other TOGO IDs containing the same digits,
but the gitignore-independent search found no maintained raw YAML or
source-specific import transform for the M230 Artificial Soil Agar record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Four milligram-scale rows are imported as gram-scale concentrations. | TOGO lists 5 mg K2HPO4, 1 mg FeCl3.6H2O, 25 mg K2SO4, and 10 mg glucose; the generated record stores 5, 1, 25, and 10 `G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M230_Artificial_Soil_Agar.yaml` |
| major | The 50 ml soil-extract addition is encoded as `50 G_PER_L`. | TOGO lists `Soil extract (see below)` as 50 ml in the final recipe. | `data/normalized_yaml/bacterial/TOGO_M230_Artificial_Soil_Agar.yaml` |
| major | Soil-extract preparation materials are direct final-medium ingredients. | TOGO separates a `Soil extract` section with tap water and leafy soil and describes how to boil and centrifuge the extract; the generated record lists `tap water` and `leafy soil` directly with variable concentrations. | `data/normalized_yaml/bacterial/TOGO_M230_Artificial_Soil_Agar.yaml` |
| major | Source pH and soil-extract preparation text are missing. | TOGO records pH 6.6-6.8 and gives the soil-extract boiling and centrifugation procedure. | `data/normalized_yaml/bacterial/TOGO_M230_Artificial_Soil_Agar.yaml` |

## Recommended Edits

1. Correct the four milligram rows to 5 mg K2HPO4, 1 mg FeCl3.6H2O, 25 mg K2SO4, and 10 mg glucose or to their exact final concentrations.
2. Represent `Soil extract (see below)` as a 50 ml addition, with `tap water` and `leafy soil` scoped to soil-extract preparation rather than the final medium.
3. Add the pH 6.6-6.8 range and the soil-extract boil/centrifuge preparation step.
4. Regenerate `data/merge_yaml/merged/ARTIFICIAL_SOIL_AGAR.yaml`.

## Follow-up Checks

- Run `just validate-schema data/normalized_yaml/bacterial/TOGO_M230_Artificial_Soil_Agar.yaml`.
- Run `just validate-strict data/normalized_yaml/bacterial/TOGO_M230_Artificial_Soil_Agar.yaml`.
- Run `just validate-terms data/normalized_yaml/bacterial/TOGO_M230_Artificial_Soil_Agar.yaml`.
- Run `just validate-references data/normalized_yaml/bacterial/TOGO_M230_Artificial_Soil_Agar.yaml`.
- Run `just verify-merges` after regeneration.
- Manually compare the regenerated record with TOGO M230 to confirm milligram units, the 50 ml soil-extract addition, pH, and extract preparation were retained.

## Additional Notes

- The cited JCM `GRMD=238` URL returned a "Nothing found" page during review;
  TOGO's structured M230 payload was available.
