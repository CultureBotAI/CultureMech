# YAML Record Review: Anoxic bicarbonate-buffered basal medium (BBM) with 10 mM sodium nitrate and various concentrations of sodium acetate

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/anoxic_bicarbonate_buffered_basal_medium_bbm_with_10_mm_sodium_nitrate_and_various_concentrations_of_sodium_acetate.yaml
- Started UTC: 2026-09-21T13:06:17Z
- Finished UTC: 2026-09-21T13:07:05Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Path | `data/merge_yaml/merged/anoxic_bicarbonate_buffered_basal_medium_bbm_with_10_mm_sodium_nitrate_and_various_concentrations_of_sodium_acetate.yaml` |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:008779` |
| Name | `anoxic_bicarbonate_buffered_basal_medium_bbm_with_10_mm_sodium_nitrate_and_various_concentrations_of_sodium_acetate` |
| Source accession | `TOGO:M2185` |
| Source label | `Anoxic bicarbonate-buffered basal medium (BBM) with 10 mM sodium nitrate and various concentrations of sodium acetate` |
| Generated status | Generated merge from one TOGO M2185 input |

The reviewed file is a generated merge of one maintained TOGO input:
`data/normalized_yaml/bacterial/anoxic_bicarbonate_buffered_basal_medium_bbm_with_10_mm_sodium_nitrate_and_various_concentrations_of_sodium_acetate.yaml`.

The exact, gitignore-independent identity search used `rg --no-ignore --hidden`
across `data/normalized_yaml`, `data/merge_yaml/merged`, `scripts`, `tests`,
and `history` for
`anoxic_bicarbonate_buffered_basal_medium_bbm_with_10_mm_sodium_nitrate_and_various_concentrations_of_sodium_acetate`,
`CultureMech:008779`, `TOGO:M2185`, `M2185`, and
`Anoxic bicarbonate-buffered basal medium`. It found the maintained TOGO input,
this generated merge, and generated indexes.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/anoxic_bicarbonate_buffered_basal_medium_bbm_with_10_mm_sodium_nitrate_and_various_concentrations_of_sodium_acetate.yaml` | Passed with no issues reported |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/anoxic_bicarbonate_buffered_basal_medium_bbm_with_10_mm_sodium_nitrate_and_various_concentrations_of_sodium_acetate.yaml --out /private/tmp/anoxic_bicarbonate.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/anoxic_bicarbonate_buffered_basal_medium_bbm_with_10_mm_sodium_nitrate_and_various_concentrations_of_sodium_acetate.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were available |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/anoxic_bicarbonate_buffered_basal_medium_bbm_with_10_mm_sodium_nitrate_and_various_concentrations_of_sodium_acetate.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` recipe validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` inside one generated merge |

The documented `just` wrappers still fail before focused validation in this
checkout because project `uv` resolves with Python 3.13 and attempts to build
`llvmlite==0.46.0`, whose setuptools build aborts with `TypeError:
Popen.__init__() got an unexpected keyword argument 'dry_run'`. The no-project
Python 3.11 commands above validate the generated record without building the
project.

## Identity and Grounding

The record correctly identifies TOGO Medium M2185 by stable ID, name, category,
and source accession. The TOGO API payload names the same long BBM medium and
sets pH to 6.8.

The record does not preserve the source topology. In the TOGO source, the
top-level M2185 recipe contains 6.25 mM sodium acetate, 10 mM sodium nitrate,
and 1 L Bicarbonate-buffered basal medium. The BBM subcomponent contains the
salts plus 10 ml Vitamins and 10 ml Minerals. The generated record retains
placeholder `Bicarbonate-buffered basal medium (BBM)`, `Vitamins`, and
`Minerals` rows as `G_PER_L`, while also flattening the BBM, Vitamins, and
Minerals contents into the same ingredient list.

The generated merge is stale relative to its normalized owner for the water row:
a September 2026 repair collapsed three identical 1 L water rows back to
`1.0 G_PER_L` in the maintained input, but the generated merge still stores
their sum, `3.0 G_PER_L`.

## Evidence

The TOGO M2185 payload supports only three top-level rows: sodium acetate,
sodium nitrate, and a 1 L BBM addition. It then describes BBM as a 1 L recipe
with ammonium chloride, potassium chloride, sodium bicarbonate, sodium
dihydrogen phosphate, 10 ml Vitamins, and 10 ml Minerals.

The TOGO source supports the vitamin rows as components of the Vitamins stock
only and the trace metal rows as components of the Minerals stock only. The
generated record emits those stock components directly; for example, 2 mg/L
biotin in the Vitamins stock becomes `2 G_PER_L` as a direct final-medium row.

The source also carries a pH and incubation-temperature comment, `pH 6.8, at 37
C`, and a prose comment explaining the BBM liter composition and that vitamins
and minerals follow Bruce et al., 1999. Neither comment is represented in the
generated YAML.

## Completeness

The sodium acetate, sodium nitrate, BBM, Vitamins, and Minerals labels are
present, and the record keeps exact TOGO M2185 identity.

The consequential gaps are:

- no `ph_value: 6.8`;
- no 37 C condition or BBM explanatory source comment;
- no structured BBM subcomponent;
- no structured 10 ml Vitamins or Minerals additions;
- no distinct water rows for BBM, Vitamins, and Minerals;
- no source-faithful unit for the 1 L BBM, 10 ml Vitamins, or 10 ml Minerals
  rows.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | BBM, Vitamins, and Minerals are flattened into one final ingredient list. | The TOGO source has a top-level 1 L BBM addition; BBM has 10 ml Vitamins and 10 ml Minerals additions. The generated record emits their stock components as direct ingredients and keeps the three stock names as `G_PER_L` rows. | `data/normalized_yaml/bacterial/anoxic_bicarbonate_buffered_basal_medium_bbm_with_10_mm_sodium_nitrate_and_various_concentrations_of_sodium_acetate.yaml` |
| Major | The generated merge is stale relative to the normalized water repair. | The normalized owner has a 2026-09-02 `REPAIRED_SUMMED_DUPLICATE_MERGE` event and now stores `Distilled water` as `1.0 G_PER_L`; the generated merge still stores a summed `3.0 G_PER_L`. | Regenerate the generated merge after repairing the normalized owner |
| Minor | Source pH and temperature are missing. | TOGO M2185 states `pH 6.8, at 37 C`; the generated record has no `ph_value` and no preparation or incubation condition. | Same normalized owner |
| Minor | Cobalt chloride and nickel chloride hydrate labels are grounded to anhydrous salts. | The source rows are `CoCl2.6H2O` and `NiCl2.6H2O`; the generated record stores `CHEBI:35696` cobalt dichloride and `CHEBI:34887` nickel dichloride. | Same normalized owner or ingredient grounding enrichment |
| Minor | The `Thiamine` row still carries a legacy MediaIngredientMech ID. | The row has a CHEBI primary term but still stores `mediaingredientmech_term: MediaIngredientMech:000898`. | Same normalized owner or legacy MIM migration |

## Recommended Edits

1. In
   `data/normalized_yaml/bacterial/anoxic_bicarbonate_buffered_basal_medium_bbm_with_10_mm_sodium_nitrate_and_various_concentrations_of_sodium_acetate.yaml`,
   preserve the top-level M2185 recipe as sodium acetate, sodium nitrate, and a
   1 L BBM addition.
2. Move the BBM salts under a structured BBM subcomponent and move the vitamin
   and mineral rows under 10 ml Vitamins and 10 ml Minerals stock additions.
3. Restore distinct source water rows for BBM, Vitamins, and Minerals rather
   than merging them.
4. Add pH 6.8 and retain the 37 C source condition in a scoped condition or
   preparation note.
5. Clear the anhydrous cobalt and nickel chloride groundings unless exact
   hexahydrate terms are available in the packaged MediaIngredientMech index.
6. Convert the `Thiamine` row's legacy MIM link to a CHEBI-keyed
   `mediaingredientmech_chebi_term` link.
7. Regenerate
   `data/merge_yaml/merged/anoxic_bicarbonate_buffered_basal_medium_bbm_with_10_mm_sodium_nitrate_and_various_concentrations_of_sodium_acetate.yaml`.

## Follow-up Checks

1. Run `just validate-schema`, `just validate-strict`, `just validate-terms`,
   and `just validate-references` on the normalized TOGO M2185 owner.
2. Regenerate this generated merge.
3. Re-open the regenerated merge and verify that BBM, Vitamins, and Minerals
   are nested rather than duplicated as both placeholder and flattened final
   ingredients.

## Additional Notes

The exact identity search included ignored files and found no additional
maintained inputs merged into this generated TOGO M2185 record.
