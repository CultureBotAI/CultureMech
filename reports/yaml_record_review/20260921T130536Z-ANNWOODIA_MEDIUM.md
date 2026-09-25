# YAML Record Review: ANNWOODIA MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ANNWOODIA_MEDIUM.yaml
- Started UTC: 2026-09-21T13:04:47Z
- Finished UTC: 2026-09-21T13:05:36Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Path | `data/merge_yaml/merged/ANNWOODIA_MEDIUM.yaml` |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:001495` |
| Name | `annwoodia_medium` |
| Source accession | `mediadive.medium:389` |
| Source label | `ANNWOODIA MEDIUM` |
| Generated status | Generated merge from `annwoodia_medium` and `thiobacillus_aquaesulis_medium` |

The reviewed file is a generated duplicate merge of the maintained DSMZ /
MediaDive input `data/normalized_yaml/bacterial/annwoodia_medium.yaml` and the
KOMODO source duplicate
`data/normalized_yaml/bacterial/thiobacillus_aquaesulis_medium.yaml`.

The exact, gitignore-independent identity search used `rg --no-ignore --hidden`
across `data/normalized_yaml`, `data/merge_yaml/merged`, `scripts`, `tests`,
and `history` for `ANNWOODIA_MEDIUM`, `ANNWOODIA MEDIUM`, `annwoodia_medium`,
`thiobacillus_aquaesulis_medium`, `CultureMech:001495`,
`CultureMech:005166`, `mediadive.medium:389`, `komodo.medium:389`, and
`DSMZ_Medium389`. It found the two maintained inputs, this generated merge, and
generated indexes.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ANNWOODIA_MEDIUM.yaml` | Passed with no issues reported |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ANNWOODIA_MEDIUM.yaml --out /private/tmp/ANNWOODIA_MEDIUM.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ANNWOODIA_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were available |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ANNWOODIA_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` recipe validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` inside one generated merge |

The documented `just` wrappers still fail before focused validation in this
checkout because project `uv` resolves with Python 3.13 and attempts to build
`llvmlite==0.46.0`, whose setuptools build aborts with `TypeError:
Popen.__init__() got an unexpected keyword argument 'dry_run'`. The no-project
Python 3.11 commands above validate the generated record without building the
project.

## Identity and Grounding

The record correctly identifies DSMZ Medium 389 / MediaDive `389`; the rendered
DSMZ PDF is headed `389: ANNWOODIA MEDIUM`. The KOMODO
`THIOBACILLUS AQUAESULIS MEDIUM` input has already been marked as a
`SOURCE_DUPLICATE` of this DSMZ record, and the merge preserves that
relationship.

The generated merge is stale relative to the maintained inputs. It was generated
on 2026-08-06, but both normalized inputs moved Zn, Mn, and Fe into a Trace
element solution on 2026-08-07 or 2026-08-15. The generated record still exposes
those three trace components as direct final-medium rows.

Even after that partial normalized repair, the maintained inputs still flatten
DSMZ Solution A, Solution B, and Solution D into direct ingredients, and still
leave the EDTA, Ca, Co, Mo, Cu, and NaOH rows from the trace stock as direct
ingredients.

## Evidence

DSMZ Medium 389 is prepared by combining 100 ml Solution A, 870 ml Solution B,
10 ml Solution C, and 20 ml Solution D. Solutions A, B, and C are autoclaved,
Solution D is filter-sterilized, and the sterile solutions are combined after
cooling.

DSMZ lists 7.90 g disodium phosphate dihydrate, 1.50 g potassium phosphate, and
100 ml water in Solution A. It lists 0.40 g ammonium chloride, 0.10 g magnesium
sulfate heptahydrate, 15.00 g agar, and 870 ml water in Solution B. It lists
5.00 g sodium thiosulfate pentahydrate and 20 ml water in Solution D.

DSMZ lists Solution C as 10 ml of Trace element solution from Medium 333. That
Trace element stock contains disodium EDTA, zinc sulfate heptahydrate, calcium
chloride dihydrate, manganese chloride tetrahydrate, cobalt chloride
hexahydrate, ammonium molybdate tetrahydrate, ferrous sulfate heptahydrate,
copper sulfate pentahydrate, sodium hydroxide, and 1000 ml water.

The generated record emits Solution A, Solution B, Solution D, and most of the
Trace element stock at local solution concentrations rather than as additions.
For example, the source has 5 g sodium thiosulfate pentahydrate in 20 ml
Solution D, but the generated record stores `250 G_PER_L` as a direct ingredient
instead of a 20 ml Solution D addition.

## Completeness

The source identity, pH values, main autoclave/filter-sterilization text, and
solid state are present.

The consequential gaps are:

- no structured Solution A, B, C, or D additions;
- only a partial Trace element solution in the maintained normalized records;
- a stale generated merge that missed the August trace-solution nesting;
- no source water rows;
- stock-local pH adjustments stored at the medium root.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The generated merge is stale relative to both maintained inputs. | The merge was generated on 2026-08-06; later `NESTED_FLATTENED_COCKTAIL` events moved Zn, Mn, and Fe into `solutions` in both normalized inputs. The generated merge still stores those rows directly. | Regenerate `data/merge_yaml/merged/ANNWOODIA_MEDIUM.yaml` after finishing the normalized repairs |
| Major | Solutions A, B, and D are flattened into direct final-medium ingredients. | DSMZ combines 100 ml Solution A, 870 ml Solution B, and 20 ml Solution D. The maintained inputs and generated merge emit their components as direct rows at stock-local g/L values. | `data/normalized_yaml/bacterial/annwoodia_medium.yaml`; mirror in `data/normalized_yaml/bacterial/thiobacillus_aquaesulis_medium.yaml` |
| Major | The Trace element solution from DSMZ Medium 333 is only partially nested. | DSMZ adds 10 ml Trace element solution. The normalized inputs nest Zn, Mn, and Fe, but EDTA, calcium, cobalt, molybdate, copper, and NaOH remain as direct ingredients. | Same two maintained inputs |
| Minor | Stock-local pH steps are scoped to the medium root. | DSMZ's pH 7.6 adjustment belongs to Solution A and its EDTA/pH 6.0 step belongs to the Trace element stock, but both are root `preparation_steps`. | Same two maintained inputs |
| Minor | Ammonium molybdate tetrahydrate is grounded to generic ammonium molybdate. | The source ingredient is `(NH4)6Mo7O24 x 4 H2O`; the generated row stores `CHEBI:91249` with label `ammonium molybdate`. | Same two maintained inputs or ingredient grounding enrichment |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/annwoodia_medium.yaml`, split the medium
   into Solution A, Solution B, 10 ml Trace element solution, and Solution D
   instead of emitting Solution A/B/D components directly.
2. Finish the Trace element solution by moving EDTA, calcium chloride, cobalt
   chloride, ammonium molybdate, copper sulfate, and NaOH into the existing
   nested stock and restoring its 1000 ml water row.
3. Mirror the same repair in
   `data/normalized_yaml/bacterial/thiobacillus_aquaesulis_medium.yaml`, or
   regenerate the KOMODO source duplicate from the repaired DSMZ parent.
4. Re-scope the pH 7.6 step to Solution A and the EDTA/pH 6.0 step to the Trace
   element solution.
5. Clear the generic ammonium molybdate term unless an exact tetrahydrate
   grounding is available in the packaged MediaIngredientMech index.
6. Regenerate the merge so `ANNWOODIA_MEDIUM.yaml` picks up the completed nested
   solution structure.

## Follow-up Checks

1. Run `just validate-schema`, `just validate-strict`, `just validate-terms`,
   and `just validate-references` on both normalized owner records.
2. Regenerate `data/merge_yaml/merged/ANNWOODIA_MEDIUM.yaml`.
3. Re-open the regenerated merge and verify that only Solution A, Solution B,
   Solution C, and Solution D appear at the final-medium level.

## Additional Notes

The exact identity search included ignored files and found no additional
maintained inputs merged into this generated Annwoodia record.
