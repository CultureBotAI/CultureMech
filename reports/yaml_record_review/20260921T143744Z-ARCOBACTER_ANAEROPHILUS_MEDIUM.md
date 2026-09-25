# YAML Record Review: ARCOBACTER ANAEROPHILUS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml
- Started UTC: 2026-09-21T14:33:30Z
- Finished UTC: 2026-09-21T14:37:43Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:000992` |
| Generated record | `data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml` |
| Merge input | `arcobacter_anaerophilus_medium` |
| Name | `arcobacter_anaerophilus_medium` |
| Original/source label | `ARCOBACTER ANAEROPHILUS MEDIUM` |
| Source grounding | DSMZ / MediaDive medium `1521`, `mediadive.medium:1521` |

The generated merge has one normalized source recipe and adds only
`curation_history`, `merge_fingerprint`, and `merged_from` merge metadata after
the maintained content. `data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml`
is therefore the path that owns any future curation.

## Validation

| Check | Result |
|---|---|
| Open-schema LinkML validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml` returned `No issues found`. |
| Strict validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml --out /private/tmp/arcobacter_anaerophilus_medium.strict.tsv --workers 1 --quiet` scanned one file and reported `total ERROR rows: 0`. |
| Reference validation | Pass with no reference checks. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` reported one file validated, zero checks, and all validations passed. |
| Term validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` reported `Validation passed` after the known `eutils/pkg_resources` warning. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for standalone `history/*.yaml` records, not a focused validator for `MediaRecipe.curation_history` arrays embedded in one generated merge. |
| DSMZ source retrieval | Pass. The cited DSMZ Medium 1521 PDF was fetched and extracted locally for source comparison. |

The documented `just validate-schema`, `just validate-strict`,
`just validate-references`, and `just validate-terms` entrypoints were not used
directly because this checkout's project environment currently fails before
dispatching validators when `uv` tries to build `llvmlite==0.46.0` under Python
3.13. The commands above run the same focused LinkML/script validators through
an isolated Python 3.11 no-project environment.

## Identity and Grounding

The record identity is sound. The generated YAML declares
`CultureMech:000992`, `mediadive.medium:1521`, and label
`ARCOBACTER ANAEROPHILUS MEDIUM`; DSMZ Medium 1521 has the same title in the
cited PDF. An ignored-inclusive exact search over the normalized indexes,
registry, catalog, and import-tracking reports found the same stable ID at
`data/culturemech_id_registry.tsv`, the active recipe catalog row, the
MediaDive and category indexes, and the normalized owner path.

The base liter-scale salts and organics are transcribed from DSMZ with the
same gram amounts for `KH2PO4`, `NaCl`, `CaCl2 x 2 H2O`, `MgSO4 x 7 H2O`,
`NH4Cl`, `Sodium citrate`, `Yeast extract`, `Ammonium acetate`, `Lactate`,
`Pyruvate`, and `Resazurin`. The CHEBI-backed terms that are present validate
under the term validator. `Yeast extract` remains an explicit undefined complex
ingredient, which is acceptable for this `composition_type: UNDEFINED` medium.

The terminal additions are not grounded to the right formulation entities:
DSMZ lists `SL10` as `1.0 ml` in a 1 liter recipe, and lists `NaHCO3 (10%)`,
`Na2S x 9 H2O (1 M)`, and `Vitamin B12` as separate sterile solution additions
after autoclaving. The YAML instead stores those three post-autoclave solutions
as direct `G_PER_L` reagent rows and stores `SL10` as `1 G_PER_L`. That makes
stock volumes, stock concentrations, and final direct masses indistinguishable.

## Evidence

Supported by the inspected DSMZ PDF:

- DSMZ Medium 1521 is `ARCOBACTER ANAEROPHILUS MEDIUM`.
- The recipe's first ten gram-scale reagents match the record's values:
  `0.50 g` `KH2PO4`, `20.00 g` `NaCl`, `0.25 g` `CaCl2 x 2 H2O`,
  `1.00 g` `MgSO4 x 7 H2O`, `0.50 g` `NH4Cl`, `0.3 g`
  `Sodium citrate`, `0.50 g` `Yeast extract`, `1.00 g`
  `Ammonium acetate`, `1.00 g` `Lactate`, and `1.00 g` `Pyruvate`.
- `1.00 mg` resazurin in the liter-scale DSMZ recipe supports the record's
  `0.001 G_PER_L` value.
- The source directs the curator to add distilled water to 1 liter, boil,
  cool under `N2`, distribute under `N2`, autoclave, and then add sterilized
  post-autoclave solutions.

Unsupported or mis-scoped in the YAML:

- `SL10` is printed as a `1.0 ml` addition, not as `1 G_PER_L`.
- `NaHCO3 (10%)` is printed as `150 ul/10 ml`; the record drops both the
  `10%` stock concentration and the `150 ul/10 ml` aliquot and replaces them
  with `1 G_PER_L`.
- `Na2S x 9 H2O (1 M)` is printed as `10 ul/10 ml`; the record drops the
  `1 M` stock concentration and aliquot and replaces them with
  `2.40182 G_PER_L`.
- `Vitamin B12` is printed as `10 ul/10 ml`; the record drops the aliquot and
  replaces it with `10 G_PER_L`.
- The sole preparation step ends at the colon after "the following sterilized
  solutions are added:" and omits the three listed solutions.

## Completeness

The record has enough provenance to recover its source PDF, but it is not
complete enough to reproduce the DSMZ formulation:

- The post-autoclave solution boundary is missing. A user following the YAML
  would weigh `NaHCO3`, sodium sulfide nonahydrate, and vitamin B12 as ordinary
  liter-scale ingredients instead of adding sterilized aliquots after
  autoclaving.
- The record has no represented stock entity for `SL10`; an ignored-inclusive
  exact search found this exact row in `data/import_tracking/reports/ungrounded_ingredients.tsv`
  as unresolved for `CultureMech:000992`.
- The record has no represented stock concentration for the vitamin B12
  aliquot, so the source supports the volume addition but not a final mass for
  cobalamin.
- Optional organism and growth-evidence fields are empty; this review did not
  find a source-local strain or growth outcome claim in the DSMZ Medium 1521
  PDF, so their absence is not a defect.

The ignored `reports/yaml_record_review/` directory was searched with `find`
before writing this report; no prior `*ARCOBACTER_ANAEROPHILUS_MEDIUM.md`
report was present.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Four solution additions are flattened into unsupported direct `G_PER_L` ingredients. | DSMZ lists `SL10` as `1.0 ml`; lists `NaHCO3 (10%)` as `150 ul/10 ml`; lists `Na2S x 9 H2O (1 M)` as `10 ul/10 ml`; and lists `Vitamin B12` as `10 ul/10 ml`. The YAML stores these as `1`, `1`, `2.40182`, and `10 G_PER_L`, respectively. | `data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml` |
| Major | The preparation step is truncated exactly where DSMZ begins naming post-autoclave additions. | The YAML description ends with "After autoclaving the following sterilized solutions are added:" and then stops; DSMZ immediately lists the `NaHCO3`, `Na2S x 9 H2O`, and `Vitamin B12` solution additions. | `data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml` |

No blockers: the YAML is valid and denotes the intended DSMZ medium.

No minor findings beyond the material formulation and preparation defects
above.

## Recommended Edits

1. In `data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml`,
   replace the direct `SL10` `G_PER_L` row with a volume-based stock addition
   of `1.0 ML_PER_L`, or with the repository's preferred `solutions` form if
   the exact DSMZ SL10 stock record is selected.
2. In the same normalized file, preserve the three post-autoclave additions as
   sterile solution additions rather than unqualified direct gram quantities:
   `NaHCO3 (10%)` at `150 ul/10 ml` (`15 ML_PER_L`), `Na2S x 9 H2O (1 M)` at
   `10 ul/10 ml` (`1 ML_PER_L`), and `Vitamin B12` at `10 ul/10 ml`
   (`1 ML_PER_L`).
3. Extend `preparation_steps` so the autoclave step includes DSMZ's full
   post-autoclave instruction and lists the three added sterilized solutions
   with their source-stated aliquots.
4. Add a curation event that states this was a DSMZ Medium 1521 stock-addition
   repair, then regenerate `data/merge_yaml/merged/` so
   `ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml` reflects the normalized correction.

## Follow-up Checks

- Re-run the focused schema, strict, term, and reference validators on
  `data/normalized_yaml/bacterial/arcobacter_anaerophilus_medium.yaml` and on
  the regenerated
  `data/merge_yaml/merged/ARCOBACTER_ANAEROPHILUS_MEDIUM.yaml`.
- Run `just verify-merges` after regenerating the merged corpus to prove that
  this generated record matches its normalized owner.
- Re-run the concentration-plausibility and ungrounded-ingredient reports or
  an exact ignored-inclusive `rg` over `data/import_tracking/reports/` to
  confirm that `CultureMech:000992` no longer appears for `Vitamin B12`
  `10 G_PER_L` or unresolved `SL10`.
- Manually verify that the selected SL10 stock identity is the DSMZ stock meant
  by Medium 1521 before linking the `SL10` addition to a `CultureMechTerm`.

## Additional Notes

The generated record is number 516 of 6286 in the case-folded
`data/merge_yaml/merged/*.yaml` review order used by this bulk pass.

`ML_PER_L` already exists in `ConcentrationUnitEnum` for solution/component
additions, so this record's source-stated stock volumes can be represented
without inventing a new unit.
