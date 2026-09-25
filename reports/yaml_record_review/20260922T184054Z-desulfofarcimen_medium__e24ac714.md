# YAML Record Review: DESULFOFARCIMEN MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/desulfofarcimen_medium__e24ac714.yaml
- Started UTC: 2026-09-22T18:33:20Z
- Finished UTC: 2026-09-22T18:41:20Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:000709 |
| Name | desulfofarcimen_medium |
| Original name | DESULFOFARCIMEN MEDIUM |
| Media term | mediadive.medium:124, DSMZ Medium 124 |
| Source | DSMZ via MediaDive |
| Category | bacterial |
| Generated status | Generated canonical merge in `data/merge_yaml/merged/`; do not edit directly |
| Maintained parent | `data/normalized_yaml/bacterial/desulfofarcimen_medium.yaml` |
| Duplicate normalized children | `data/normalized_yaml/bacterial/desulfotomaculum_acetoxidans_medium.yaml`; `data/normalized_yaml/bacterial/desulfotomaculum_groll_medium.yaml` |
| Merge fingerprint | e24ac7142500144900aeeb820ec1f8be1efa81ded6cd32f48483a8bc94e6e1eb |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/desulfofarcimen_medium__e24ac714.yaml` | Passed: `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/desulfofarcimen_medium__e24ac714.yaml --out /private/tmp/desulfofarcimen_medium__e24ac714.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, and only the TSV header was emitted. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/desulfofarcimen_medium__e24ac714.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 reference checks. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/desulfofarcimen_medium__e24ac714.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. The run printed the known `eutils`/`pkg_resources` deprecation warning first. |
| Embedded curation history | `just validate-history` equivalent | Not checked: the documented history validator validates standalone `history/*.yaml` records, not `MediaRecipe.curation_history` embedded in merged YAML. |

## Identity and Grounding

The record identity is internally coherent. `CultureMech:000709`, `desulfofarcimen_medium`, `DESULFOFARCIMEN MEDIUM`, and `mediadive.medium:124` all identify DSMZ Medium 124. MediaDive REST for medium 124 and the DSMZ Medium 124 PDF agree on the label, DSMZ source URL, pH 7.0-7.2, 1003 ml final volume, and the complex/undefined formulation.

The generated canonical record is a three-source merge of the DSMZ/MediaDive parent with two KOMODO rows, `komodo.medium:124` and `komodo.medium:124a`, both marked as `SOURCE_DUPLICATE` normalized children. Those relationships are plausible because the two KOMODO children carry the same DSMZ Medium 124 ingredient signature after enrichment, but they also carry the same imported stock-flattening defect as the canonical parent.

Most main-solution ingredient amounts in the generated record are MediaDive's per-liter values for DSMZ's 1003 ml final recipe: 1.17 g NaCl becomes 1.1665 g/l, 0.40 g MgCl2 x 6 H2O becomes 0.398804 g/l, and 0.40 g Na2S x 9 H2O becomes 0.398804 g/l. Sodium resazurin is likewise consistent with 0.50 ml of a 0.1% w/v stock in the 1003 ml final volume.

## Evidence

DSMZ Medium 124 states that the final medium is built from direct salts, yeast extract, sodium resazurin, bicarbonate, acetate, butyrate, sulfide, and distilled water plus three stock additions: 1.00 ml Trace element solution SL-10, 1.00 ml Selenite-tungstate solution, and 1.00 ml Wolin's vitamin solution (10x). MediaDive REST preserves the same structure by placing those three additions as `solution` rows in `Main sol. 124`.

The generated record does not preserve those stock additions. It has no `solutions` block and instead puts all SL-10 stock components (`HCl`, `FeCl2 x 4 H2O`, `ZnCl2`, `MnCl2 x 4 H2O`, `H3BO3`, `CoCl2 x 6 H2O`, `CuCl2 x 2 H2O`, `NiCl2 x 6 H2O`, `Na2MoO4 x 2 H2O`), all selenite-tungstate stock components (`NaOH`, `Na2SeO3 x 5 H2O`, `Na2WO4 x 2 H2O`), and all Wolin vitamin stock components (`Biotin`, `Folic acid`, `Pyridoxine hydrochloride`, `Thiamine HCl`, `Riboflavin`, `Nicotinic acid`, `Calcium D-(+)-pantothenate`, `Vitamin B12`, `p-Aminobenzoic acid`, `(DL)-alpha-Lipoic acid`) as top-level final-medium ingredients at the stock solution g/l concentrations.

The generated main preparation step is supported by DSMZ and MediaDive. The second generated step is supported only as the preparation instruction for Trace element solution SL-10; it should be attached to that stock solution and not to the final Desulfofarcimen medium.

## Completeness

The record is missing a structured representation of the three named stock additions and their separate compositions. Without those solution boundaries, a downstream reader cannot distinguish a 1 ml final-medium stock addition from the stock recipe itself.

The generated record correctly omits explicit growth evidence: DSMZ Medium 124 is a recipe source and does not assert a target organism growth experiment in the inspected PDF or MediaDive REST payload.

Gitignore-independent searches with `rg --no-ignore --hidden` and `find` covered `data`, `.claude`, `src`, `scripts`, and `reports/yaml_record_review`. They found the DSMZ parent, two KOMODO duplicate children, separate TOGO M2526/M2533 normalized records, and no pre-existing review report for `desulfofarcimen_medium__e24ac714`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The DSMZ stock additions are flattened into final-medium ingredient rows, and the record has no `solutions` block for Trace element solution SL-10, Selenite-tungstate solution, or Wolin's vitamin solution (10x). | DSMZ and MediaDive both add those stocks to the final medium as 1 ml solution rows; the generated YAML instead represents the stock formulas as top-level ingredient concentrations. | `data/normalized_yaml/bacterial/desulfofarcimen_medium.yaml`; also repair or regenerate duplicate children `data/normalized_yaml/bacterial/desulfotomaculum_acetoxidans_medium.yaml` and `data/normalized_yaml/bacterial/desulfotomaculum_groll_medium.yaml` before regenerating the merged record. |
| Major | The SL-10 preparation instruction is attached to the final MediaRecipe even though it prepares only the missing SL-10 stock. | DSMZ places the FeCl2/HCl dissolution instruction under Trace element solution SL-10; the generated YAML has it as `preparation_steps[1]` in `DESULFOFARCIMEN MEDIUM`. | `data/normalized_yaml/bacterial/desulfofarcimen_medium.yaml`; the same stock-boundary fix should keep the step on the modeled SL-10 solution. |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/desulfofarcimen_medium.yaml`, replace the flattened SL-10, selenite-tungstate, and Wolin vitamin ingredients with three solution additions at 1 ml per DSMZ 124 final recipe.
2. Represent the SL-10, selenite-tungstate, and Wolin vitamin formulas as separate stock solutions, including their source volumes and water quantities, or link the final recipe to maintained solution records that carry those formulas.
3. Move the SL-10-specific HCl/FeCl2 preparation instruction off the final MediaRecipe and onto the SL-10 SolutionRecipe.
4. Apply the equivalent stock-boundary repair to `data/normalized_yaml/bacterial/desulfotomaculum_acetoxidans_medium.yaml` and `data/normalized_yaml/bacterial/desulfotomaculum_groll_medium.yaml`, or replace those duplicate formulations with clean source-duplicate links to the DSMZ parent.
5. Regenerate `data/merge_yaml/merged/desulfofarcimen_medium__e24ac714.yaml` and inspect the generated record for three named solution additions and no top-level SL-10/selenite/vitamin stock rows.

## Follow-up Checks

1. Re-run open-schema, strict, reference, and term validation on the repaired normalized records and on the regenerated merged canonical record.
2. Run the repository merge verification and freshness checks documented for generated merge outputs.
3. Manually compare the regenerated record against DSMZ Medium 124 and MediaDive medium 124 to verify the 1003 ml final formula, pH 7.0-7.2, post-autoclave additions, and three stock additions are all scoped correctly.

## Additional Notes

The DSMZ PDF also lists three medium 124 strain-specific substrate replacements for DSM 2925, DSM 7213, and DSM 100382. The TOGO M2533 record for the DSM 7213 benzoate variant is present separately under `data/normalized_yaml/bacterial/desulfofarcimen_medium_for_dsm_7213.yaml`; this review did not audit parent/child variant links for those substrate variants because the requested target was the generated DSMZ base-medium record.
