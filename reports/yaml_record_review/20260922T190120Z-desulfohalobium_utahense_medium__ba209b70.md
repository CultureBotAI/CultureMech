# YAML Record Review: DESULFOHALOBIUM UTAHENSE MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/desulfohalobium_utahense_medium__ba209b70.yaml
- Started UTC: 2026-09-22T18:58:13Z
- Finished UTC: 2026-09-22T19:01:25Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:003305 |
| Name | desulfohalobium_utahense_medium |
| Original name | DESULFOHALOBIUM UTAHENSE MEDIUM |
| Media term | mediadive.medium:J957, JCM Medium J957 |
| Source | JCM Medium 957 via MediaDive |
| Category | bacterial |
| Generated status | Generated single-source merge in `data/merge_yaml/merged/`; do not edit directly |
| Maintained parent | `data/normalized_yaml/bacterial/desulfohalobium_utahense_medium.yaml` |
| Merge fingerprint | ba209b70a052554d1185e37df8f7e851e20a93585e06131bd8913ff341849045 |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/desulfohalobium_utahense_medium__ba209b70.yaml` | Passed: `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/desulfohalobium_utahense_medium__ba209b70.yaml --out /private/tmp/desulfohalobium_utahense_medium__ba209b70.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, and only the TSV header was emitted. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/desulfohalobium_utahense_medium__ba209b70.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 reference checks. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/desulfohalobium_utahense_medium__ba209b70.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. The run printed the known `eutils`/`pkg_resources` deprecation warning first. |
| Embedded curation history | `just validate-history` equivalent | Not checked: the documented history validator validates standalone `history/*.yaml` records, not `MediaRecipe.curation_history` embedded in merged YAML. |

## Identity and Grounding

The record identity is correct. The generated record points to JCM Medium 957 and the live JCM 957 page identifies the source as `DESULFOHALOBIUM UTAHENSE MEDIUM`. TOGO M1006 is a parallel parse of the same JCM source, and the exact search found it as a separate normalized/generated record, not part of the `ba209b70` merge.

The direct base-salt rows in the generated record are consistent with MediaDive's per-liter scaling of the JCM recipe. For example, 100 g NaCl from the JCM base recipe appears as 99.2064 G_PER_L after MediaDive accounts for the added post-autoclave solutions.

## Evidence

The JCM page makes the post-autoclave additions explicit: the base medium is autoclaved under an 80:20 N2-CO2 gas mixture, then 10 ml trace vitamins, 50 ml 8% NaHCO3 solution, 50 ml 5% L-sodium lactate solution, and finally 6 ml 5% Na2S x 9 H2O from an anaerobic stock are added per liter.

The generated record has no `solutions` block and models all of those post-autoclave additions as if they were final ingredient masses. `NaHCO3` is 50 G_PER_L, `L-Sodium lactate` is 50 G_PER_L, and `Na2S x 9 H2O` is 6 G_PER_L; the source values are milliliter additions of percent stocks, not gram masses.

The generated record also flattens the FeCl2 solution, the trace element solution, and the trace vitamin solution into top-level stock-strength ingredients. HCl through Na2MoO4 x 2 H2O belong to the referenced FeCl2/trace stocks, and Biotin through Lipoic acid belong to the referenced trace vitamins stock.

The two generated preparation steps are source text fragments, but they no longer point to structured solution additions: step 1 says to add following solutions after autoclaving, yet the following solutions are missing; step 2 says to add a final anaerobic stock, but the 5% Na2S x 9 H2O stock is also missing.

The generated `high_metal: true` flag is unsupported as a final-medium property because it comes from the flattened 1.5 G_PER_L FeCl2 stock ingredient.

## Completeness

The record is incomplete for every JCM stock or supplement addition. A reader cannot recover the 1 ml FeCl2 stock, 1 ml trace element stock, 10 ml trace vitamin stock, 50 ml bicarbonate stock, 50 ml lactate stock, or 6 ml sulfide stock from the generated flat ingredients.

Explicit target-organism growth evidence is correctly absent because the inspected JCM recipe page and TOGO parse do not report a growth experiment.

Gitignore-independent `rg --no-ignore --hidden` over normalized YAML, merge YAML, import-tracking reports, the ID registry, and the recipe catalog found the maintained JCM/MediaDive owner, a TOGO M1006 parse of the same JCM source, a KOMODO 1055 parse, DSM-specific KOMODO variants, and no additional source merged into fingerprint `ba209b70`. A `find` under `reports/yaml_record_review` found no pre-existing review report for `desulfohalobium_utahense_medium__ba209b70`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Percent stock additions are represented as raw G_PER_L ingredient concentrations. | JCM 957 adds 50 ml 8% NaHCO3, 50 ml 5% L-sodium lactate, and 6 ml 5% Na2S x 9 H2O as solutions; the generated YAML records 50, 50, and 6 G_PER_L top-level rows. | `data/normalized_yaml/bacterial/desulfohalobium_utahense_medium.yaml`. |
| Major | FeCl2, trace element, and trace vitamin stock recipes are flattened into final ingredients. | JCM 957 references 1 ml FeCl2 solution, 1 ml Trace element solution, and 10 ml Trace vitamins; the generated YAML has their component chemicals directly in `ingredients` and no `solutions` block. | `data/normalized_yaml/bacterial/desulfohalobium_utahense_medium.yaml`. |
| Major | Preparation steps reference missing solution structures. | The two generated steps direct the curator to add following solutions and a final anaerobic stock, but those source solution additions are absent after flattening. | `data/normalized_yaml/bacterial/desulfohalobium_utahense_medium.yaml`. |

## Recommended Edits

1. Replace `NaHCO3`, `L-Sodium lactate`, and `Na2S x 9 H2O` mass rows with 50 ml 8% bicarbonate, 50 ml 5% L-sodium lactate, and 6 ml 5% sulfide solution additions.
2. Replace the flattened FeCl2, trace-element, and trace-vitamin components with 1 ml FeCl2 solution, 1 ml Trace element solution, and 10 ml Trace vitamins additions that resolve to their JCM stock sources.
3. Keep only the true base-solution ingredients as direct final-medium ingredients and preserve MediaDive's per-liter scaling for those rows.
4. Attach the N2-CO2 autoclaving instruction to the base medium and the anaerobic sulfide instruction to the 5% sulfide addition.
5. Regenerate `data/merge_yaml/merged/desulfohalobium_utahense_medium__ba209b70.yaml`.

## Follow-up Checks

1. Re-run open-schema, strict, reference, and term validation on the repaired normalized record and regenerated merge.
2. Re-run concentration-plausibility reporting for `CultureMech:003305`; the FeCl2 x 4 H2O `TRACE_SALT_AS_STOCK` row should disappear.
3. Manually compare the regenerated record against JCM Medium 957 and TOGO M1006 for all six post-autoclave additions and the 80:20 N2-CO2 autoclaving condition.

## Additional Notes

The neighboring `DESULFOHALOBIUM_UTAHENSE_MEDIUM.yaml` generated record represents TOGO M1006. It was discovered with ignored files included and should be reviewed as a separate source import.
