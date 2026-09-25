# YAML Record Review: ARHODOMONAS MEDIUM RS91

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ARHODOMONAS_MEDIUM_RS91.yaml
- Started UTC: 2026-09-21T14:37:50Z
- Finished UTC: 2026-09-21T14:39:41Z
- Verdict: pass with minor issues

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:000950` |
| Generated record | `data/merge_yaml/merged/ARHODOMONAS_MEDIUM_RS91.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/arhodomonas_medium_rs91.yaml` |
| Merge input | `arhodomonas_medium_rs91` |
| Name | `arhodomonas_medium_rs91` |
| Original/source label | `ARHODOMONAS MEDIUM RS91` |
| Source grounding | DSMZ / MediaDive medium `1482`, `mediadive.medium:1482` |

The generated record merges one normalized source recipe, so
`data/normalized_yaml/bacterial/arhodomonas_medium_rs91.yaml` owns any future
scientific edit. `find` over the ignored report directory found no existing
`*ARHODOMONAS_MEDIUM_RS91.md` report before this one was written.

## Validation

| Check | Result |
|---|---|
| Open-schema LinkML validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ARHODOMONAS_MEDIUM_RS91.yaml` returned `No issues found`. |
| Strict validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ARHODOMONAS_MEDIUM_RS91.yaml --out /private/tmp/arhodomonas_medium_rs91.strict.tsv --workers 1 --quiet` scanned one file and reported `total ERROR rows: 0`. |
| Reference validation | Pass with no reference checks. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ARHODOMONAS_MEDIUM_RS91.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` reported one file validated, zero checks, and all validations passed. |
| Term validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ARHODOMONAS_MEDIUM_RS91.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` reported `Validation passed` after the known `eutils/pkg_resources` warning. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for standalone `history/*.yaml` records, not a focused validator for `MediaRecipe.curation_history` arrays embedded in one generated merge. |
| DSMZ source retrieval | Pass. The cited DSMZ Medium 1482 PDF was fetched and extracted locally for source comparison. |

The documented `just` entrypoints are currently blocked by the project
environment's Python 3.13 / `llvmlite==0.46.0` build failure, so the review used
the same focused validators through the Python 3.11 no-project workaround.

## Identity and Grounding

The record identity is correct. The generated YAML declares
`CultureMech:000950`, `mediadive.medium:1482`, and `ARHODOMONAS MEDIUM RS91`;
the inspected DSMZ PDF is titled `1482. ARHODOMONAS MEDIUM RS91`. An
ignored-inclusive exact search found the same stable ID and MediaDive source in
the ID registry, active recipe catalog, global normalized index, MediaDive
index, and bacterial index.

The CHEBI-backed salt and agar groundings align with the source's supplied
forms, including the hydrates for `MgCl2 x 6 H2O`, `CaCl2 x 2 H2O`, and
`MgSO4 x 7 H2O`. The `(NH4)2HPO4` primary term also validates as
`CHEBI:63051` / diammonium hydrogen phosphate and the packaged MIM label index
maps `(NH4)2HPO4` to the same CHEBI identifier.

## Evidence

Supported by the inspected DSMZ PDF:

- DSMZ Medium 1482 is `ARHODOMONAS MEDIUM RS91`.
- The source and YAML agree on all gram-scale amounts for `NaCl`,
  `MgCl2 x 6 H2O`, `KCl`, `CaCl2 x 2 H2O`, `MgSO4 x 7 H2O`, `(NH4)2HPO4`,
  `Na pyruvate`, `Na acetate`, `Casein hydrolysate`, `Yeast extract`,
  `Tryptone`, and `Agar`.
- The source lists `20.0 g` agar, supporting `physical_state: SOLID_AGAR`.
- The source states `Adjust to pH 6.5-7.5`, supporting both `ph_range` and the
  single preparation step.

The record drops three source qualifiers on complex ingredients:

- `Casein hydrolysate` omits DSMZ's `Oxoid LP0041`.
- `Yeast extract` omits DSMZ's `BD212750`.
- `Tryptone` omits DSMZ's `BD211921`.

## Completeness

The medium is complete enough to recover and prepare the formulation because
every non-water amount, the agar, and the pH range are present.

Minor completeness gaps:

- DSMZ prints `Distilled water 1000.0 ml`; the YAML omits an explicit water or
  final-volume row.
- The supplier/catalog details for three undefined complex ingredients are not
  preserved in notes or evidence.
- `(NH4)2HPO4` still carries a legacy `mediaingredientmech_term` with
  `MediaIngredientMech:000385` instead of the CHEBI-keyed
  `mediaingredientmech_chebi_term` used by neighboring grounded ingredients.

Optional organism and growth-evidence fields are empty. That is not a defect
for this source-only import because the DSMZ medium recipe does not assert a
specific strain outcome.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Minor | Three complex ingredient rows lose source-stated catalog qualifiers. | DSMZ specifies `Casein hydrolysate (Oxoid LP0041)`, `Yeast extract (BD212750)`, and `Tryptone (BD211921)`; the YAML retains only the generic labels and the correct gram amounts. | `data/normalized_yaml/bacterial/arhodomonas_medium_rs91.yaml` |
| Minor | The explicit water line is absent. | DSMZ lists `Distilled water 1000.0 ml` after agar; the YAML starts with the salts and does not record water or a final-volume marker. | `data/normalized_yaml/bacterial/arhodomonas_medium_rs91.yaml` |
| Minor | One ingredient retained a legacy MediaIngredientMech link shape. | `(NH4)2HPO4` has the correct primary `CHEBI:63051` term, but its secondary MIM linkage still uses `mediaingredientmech_term: MediaIngredientMech:000385` even though the packaged label index maps the label to CHEBI and this record otherwise uses `mediaingredientmech_chebi_term`. | `data/normalized_yaml/bacterial/arhodomonas_medium_rs91.yaml` |

No blockers or major findings.

## Recommended Edits

1. In `data/normalized_yaml/bacterial/arhodomonas_medium_rs91.yaml`, add
   notes or source-label detail to preserve `Oxoid LP0041`, `BD212750`, and
   `BD211921` for the three complex nutrient rows.
2. Add a `Distilled water` 1000 ml/L final-volume component if the curation
   style for DSMZ water rows is to retain explicit solvent rows.
3. Replace the stale `(NH4)2HPO4` `mediaingredientmech_term` block with
   `mediaingredientmech_chebi_term` keyed to `CHEBI:63051`, matching the
   primary ingredient term and the packaged MIM label-index mapping.
4. Regenerate `data/merge_yaml/merged/` after any normalized edit so this
   generated record reflects the maintained owner.

## Follow-up Checks

- Re-run the focused schema, strict, term, and reference validators on the
  normalized owner and regenerated merge record.
- Run `just verify-merges` after regeneration.
- Re-read the regenerated YAML around the `(NH4)2HPO4`, `Casein hydrolysate`,
  `Yeast extract`, and `Tryptone` rows to ensure only the intended source
  details and MIM block changed.

## Additional Notes

The generated record is number 517 of 6286 in the case-folded
`data/merge_yaml/merged/*.yaml` review order used by this bulk pass.

An exact ignored-inclusive search of `data/import_tracking/reports/concentration_plausibility.tsv`,
`data/import_tracking/reports/ungrounded_ingredients.tsv`, and
`data/import_tracking/reports/composition_type_conflicts.tsv` found no existing
target-specific backlog row for `CultureMech:000950`.
