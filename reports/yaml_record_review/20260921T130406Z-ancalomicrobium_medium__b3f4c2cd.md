# YAML Record Review: ANCALOMICROBIUM MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ancalomicrobium_medium__b3f4c2cd.yaml
- Started UTC: 2026-09-21T13:03:28Z
- Finished UTC: 2026-09-21T13:04:06Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Path | `data/merge_yaml/merged/ancalomicrobium_medium__b3f4c2cd.yaml` |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:006091` |
| Name | `ancalomicrobium_medium` |
| Source accession | `komodo.medium:603` |
| Source label | `ANCALOMICROBIUM MEDIUM` |
| Generated status | Generated merge from `KOMODO_603_ANCALOMICROBIUM_MEDIUM` and `ancalomicrobium_medium` |

The reviewed file is a generated duplicate merge of two maintained inputs:
`data/normalized_yaml/bacterial/KOMODO_603_ANCALOMICROBIUM_MEDIUM.yaml` and
`data/normalized_yaml/bacterial/ancalomicrobium_medium.yaml`. The KOMODO record
states that DSMZ Medium 603 was copied into it, and the MediaDive parent is the
source-owned DSMZ Medium 603 input.

The exact, gitignore-independent identity search used `rg --no-ignore --hidden`
across `data/normalized_yaml`, `data/merge_yaml/merged`, `scripts`, `tests`,
and `history` for `ancalomicrobium_medium__b3f4c2cd`,
`KOMODO_603_ANCALOMICROBIUM_MEDIUM`, `komodo.medium:603`,
`CultureMech:006091`, `CultureMech:001731`, `mediadive.medium:603`, `DSMZ
Medium 603`, `DSMZ_Medium603`, and `Medium603`. It found the two maintained
inputs, this generated merge, and generated indexes.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ancalomicrobium_medium__b3f4c2cd.yaml` | Passed with no issues reported |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ancalomicrobium_medium__b3f4c2cd.yaml --out /private/tmp/ancalomicrobium_medium__b3f4c2cd.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ancalomicrobium_medium__b3f4c2cd.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were available |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ancalomicrobium_medium__b3f4c2cd.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` recipe validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` inside one generated merge |

The documented `just` wrappers still fail before focused validation in this
checkout because project `uv` resolves with Python 3.13 and attempts to build
`llvmlite==0.46.0`, whose setuptools build aborts with `TypeError:
Popen.__init__() got an unexpected keyword argument 'dry_run'`. The no-project
Python 3.11 commands above validate the generated record without building the
project. The optional `pdfinfo` binary was unavailable, but `mutool draw -F txt`
rendered the fetched DSMZ PDF text successfully.

## Identity and Grounding

The record correctly identifies KOMODO Medium 603 as a source duplicate of DSMZ
Medium 603 / MediaDive `603`, and its copied source recipe is headed
`603. ANCALOMICROBIUM MEDIUM` in the rendered DSMZ PDF.

The source is a base medium with a 10 ml Vitamin solution stock, a 20 ml
Hutner's basal salts stock, and a nested 50 ml Metals "44" addition inside
Hutner's salts. The generated record flattens all three stock levels into
direct final-medium rows.

The generated `SOLID_AGAR` state and direct 15 g/L agar row overstate the base
recipe. DSMZ says the medium may be solidified by adding 15 g/L agar; agar is
optional, not part of every ANCALOMICROBIUM MEDIUM preparation.

## Evidence

DSMZ Medium 603 supports `(NH4)2SO4`, glucose, `Na2HPO4`, 980 ml distilled
water, final pH 7, 10 ml Vitamin solution, and 20 ml Hutner's basal salts in the
main recipe. It then instructs the curator to make up the medium without
Vitamin solution, autoclave, and add the filter-sterilized Vitamin solution to
cooled medium.

DSMZ supports the seven vitamin rows as components of the Vitamin solution
stock only. It supports nitrilotriacetic acid, magnesium sulfate heptahydrate,
calcium chloride dihydrate, ammonium molybdate, ferrous sulfate heptahydrate,
50 ml Metals "44", and water as Hutner's salts stock components only.

DSMZ lists disodium EDTA, zinc sulfate heptahydrate, a second ferrous sulfate
heptahydrate row, manganese sulfate monohydrate, copper sulfate pentahydrate,
cobalt nitrate hexahydrate, sodium borate decahydrate, and water under Metals
"44" only. The generated `FeSO4 x 7 H2O` row merges the Hutner 99 mg/L and
Metals "44" 500 mg/L stock rows into `0.599 G_PER_L`, without preserving either
solution boundary or dilution.

The DSMZ source also states that the medium may be solidified by adding 15 g/L
agar and that DSM 3698, DSM 3699, DSM 5900, and DSM 5901 require 0.1 g/L yeast
extract. The generated record has agar as a mandatory row and lacks the
strain-specific yeast-extract variants.

## Completeness

The stable source identity, base dry rows, pH value, and KOMODO-to-DSMZ
duplicate relationship are present.

The consequential gaps are:

- no explicit 10 ml Vitamin solution addition;
- no explicit 20 ml Hutner's basal salts addition;
- no explicit 50 ml Metals "44" addition;
- no water row from the main medium or any stock solution;
- no Medium 603 preparation steps after the merge selected the KOMODO surface;
- no representation of the four DSM strain variants with 0.1 g/L yeast extract;
- no way to tell that agar is optional.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Vitamin solution, Hutner's basal salts, and Metals "44" are flattened into direct final-medium ingredients. | DSMZ adds 10 ml Vitamin solution and 20 ml Hutner's basal salts; Hutner's salts add 50 ml Metals "44". The generated record emits all stock components as direct ingredients at stock concentrations. | `data/normalized_yaml/bacterial/ancalomicrobium_medium.yaml`; mirror the same repair in `data/normalized_yaml/bacterial/KOMODO_603_ANCALOMICROBIUM_MEDIUM.yaml` or regenerate the KOMODO duplicate from the repaired DSMZ parent |
| Major | The merge dropped DSMZ preparation instructions. | The DSMZ-owned parent has preparation text for autoclaving, vitamin filtration, Hutner pH adjustment, and Metals "44" acidification; the generated duplicate merge selected the KOMODO source and has no `preparation_steps`. | Same two maintained inputs or merge duplicate selection |
| Major | Optional agar is represented as mandatory. | DSMZ says the medium may be solidified with 15 g/L agar; the generated record stores `physical_state: SOLID_AGAR` and a direct `Agar` ingredient. | Same two maintained inputs |
| Major | Four strain-specific yeast-extract variants are absent. | DSMZ says DSM 3698, DSM 3699, DSM 5900, and DSM 5901 add 0.1 g/L yeast extract. The generated record has no variant children or discussion flag for those strains. | Same two maintained inputs |
| Minor | Ammonium molybdate tetrahydrate is grounded to generic ammonium molybdate. | The source ingredient is hydrated; the generated `(NH4)6Mo7O24 x 4 H2O` row stores `CHEBI:91249` with label `ammonium molybdate`. | Same two maintained inputs or ingredient grounding enrichment |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/ancalomicrobium_medium.yaml`, restore
   Vitamin solution, Hutner's basal salts, and Metals "44" as structured nested
   stock additions instead of direct final-medium rows.
2. Keep `data/normalized_yaml/bacterial/KOMODO_603_ANCALOMICROBIUM_MEDIUM.yaml`
   aligned with the repaired DSMZ parent, because it is marked as a
   `SOURCE_DUPLICATE`.
3. Preserve the DSMZ Medium 603 preparation steps in whichever duplicate the
   merge exposes as canonical.
4. Split the optional 15 g/L agar addition from the liquid base, or mark it as
   an optional solidification variant instead of making the whole record
   `SOLID_AGAR`.
5. Add explicit DSM 3698, DSM 3699, DSM 5900, and DSM 5901 variants or a quality
   flag naming the missing 0.1 g/L yeast-extract additions.
6. Clear the generic ammonium molybdate term unless an exact hydrated grounding
   is available in the packaged ingredient index.

## Follow-up Checks

1. Run `just validate-schema`, `just validate-strict`, `just validate-terms`,
   and `just validate-references` on both maintained Ancalomicrobium DSMZ/KOMODO
   source-duplicate inputs.
2. Regenerate `data/merge_yaml/merged/ancalomicrobium_medium__b3f4c2cd.yaml`.
3. Re-open the regenerated merge and verify that stock ingredients are nested,
   DSMZ preparation survived duplicate merging, agar is not mandatory in the
   base liquid recipe, and the four DSM strain variants are represented or
   explicitly flagged.

## Additional Notes

The exact identity search included ignored files and found no additional
maintained inputs merged into this generated DSMZ/KOMODO duplicate.
