# YAML Record Review: marine_caulobacter_medium_spyem_containing_sea_salts_and_nh4cl

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/marine_caulobacter_medium_spyem_containing_sea_salts_and_nh4cl.yaml
- Started UTC: 2026-09-23T23:55:04Z
- Finished UTC: 2026-09-23T23:55:27Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | data/merge_yaml/merged/marine_caulobacter_medium_spyem_containing_sea_salts_and_nh4cl.yaml |
| Class | MediaRecipe |
| ID | CultureMech:008859 |
| Label | marine_caulobacter_medium_spyem_containing_sea_salts_and_nh4cl |
| Source identity | TOGO:M2273, Marine-Caulobacter medium SPYEM containing sea salts and NH4Cl |
| Generation state | Generated one-source merge under data/merge_yaml/merged; repair data/normalized_yaml/bacterial/marine_caulobacter_medium_spyem_containing_sea_salts_and_nh4cl.yaml or the merge generation step rather than this file |

The generated record denotes TOGO Medium M2273. Its stable ID, name, source accession, category, and one-source merge lineage agree, but the visible formula is stale relative to the maintained September 2026 repair of the stock additions and nested stock compositions.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/marine_caulobacter_medium_spyem_containing_sea_salts_and_nh4cl.yaml` | Passed; `No issues found` |
| Strict closed-schema gate | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/marine_caulobacter_medium_spyem_containing_sea_salts_and_nh4cl.yaml --out /private/tmp/marine_caulobacter_medium_spyem_containing_sea_salts_and_nh4cl.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/marine_caulobacter_medium_spyem_containing_sea_salts_and_nh4cl.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/marine_caulobacter_medium_spyem_containing_sea_salts_and_nh4cl.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known `eutils` `pkg_resources` deprecation warning |
| Embedded curation history | Not checked | `just validate-history` validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` entries |

## Identity and Grounding

- CultureMech:008859, `marine_caulobacter_medium_spyem_containing_sea_salts_and_nh4cl`, and TOGO M2273 agree on the intended record identity.
- TOGO M2273 exposes no separate original source URL in the inspected API payload; the record is grounded directly to TOGO.
- TOGO M2273 lists a final autoclaved base of 0.5 g NH4Cl, 30 g Sea salts from Sigma, and 1 L deionized water, followed after autoclaving and cooling by 2 ml sterile 50% glucose, 20 ml 50xPYE, and 5 ml filter-sterilized 0.2 mg/ml riboflavin.
- The generated record has the right NH4Cl and Sea salts amounts, but it flattens `Glucose (50%)`, `50xPYE`, `Riboflavin (0.2 mg/ml)`, `Yeast extract`, `Peptone`, and `Riboflavin` into top-level g/L ingredient rows.
- NH4Cl and Riboflavin are grounded to exact ChEBI terms. Sea salts from Sigma, 50xPYE, Yeast extract, and Peptone are complex or source-defined materials and remain ungrounded.

## Evidence

- The generated 0.5 g/L NH4Cl and 30 g/L Sea salts rows match the TOGO M2273 base recipe.
- TOGO M2273 lists 1 L deionized water in the base; the generated record instead has 12.0 g/L `Deionized water` with a note saying it merged three duplicate rows, reflecting the old flattening of the base 1 L, 50xPYE 1 L, and riboflavin-stock 10 ml water rows.
- TOGO M2273 lists glucose as a 2 ml addition of a 50% solution. The generated record encodes `Glucose (50%)` as 2 g/L.
- TOGO M2273 lists 50xPYE as a 20 ml addition whose stock recipe contains 100 g/L peptone and 50 g/L yeast extract. The generated record encodes 50xPYE as 20 g/L and also publishes stock-only Peptone and Yeast extract as if they were 100 g/L and 50 g/L final-medium rows.
- TOGO M2273 lists 0.2 mg/ml riboflavin as a 5 ml filter-sterilized stock addition. The generated record encodes that stock as 5 g/L and separately encodes stock-only riboflavin as 2 g/L.

## Completeness

- The generated record is materially incomplete until it is regenerated from the already repaired maintained M2273 input with the three stock additions represented as `solutions`.
- The generated record loses the source's preparation order: autoclave the base, cool it, autoclave 50xPYE, filter-sterilize riboflavin, then aseptically add 50xPYE, glucose, and riboflavin.
- TOGO M2273 does not declare a pH, incubation condition, target organism, growth metric, or primary literature source in the inspected API payload. Those absent optional slots are acceptable in this generated formulation record.
- Exact gitignore-independent searches were run for `CultureMech:008859`, `marine_caulobacter_medium_spyem_containing_sea_salts_and_nh4cl`, `TOGO:M2273`, and the merge fingerprint across the scoped bacterial normalized YAML directory, this target merged YAML, and the TOGO, bacterial, and recipe index files with `--no-ignore --hidden`; the searches found only the expected maintained input, generated target, and index entries.
- An exact `find reports/yaml_record_review -maxdepth 1 -name '*-marine_caulobacter_medium_spyem_containing_sea_salts_and_nh4cl.md' -print` search, which includes ignored files, found no pre-existing review report for this generated record before this report was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The generated final-medium formulation flattens source stock recipes into unsupported top-level g/L ingredients. | TOGO M2273 adds 2 ml 50% glucose, 20 ml 50xPYE, and 5 ml 0.2 mg/ml riboflavin after cooling; the YAML instead stores those additions as 2, 20, and 5 g/L rows and publishes stock-only Peptone, Yeast extract, and Riboflavin as final-medium rows. | data/merge_yaml generation from data/normalized_yaml/bacterial/marine_caulobacter_medium_spyem_containing_sea_salts_and_nh4cl.yaml |
| major | The generated water row is a nonsensical duplicate merge rather than the TOGO final base volume. | TOGO M2273 lists 1 L deionized water for the final-medium base; the YAML has 12.0 g/L deionized water and records an old merge of three nested water quantities. | data/merge_yaml generation from data/normalized_yaml/bacterial/marine_caulobacter_medium_spyem_containing_sea_salts_and_nh4cl.yaml |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/` from the September 2026 repaired M2273 normalized YAML so the final record carries the base ingredients plus three stock-solution additions.
2. Confirm that regenerated M2273 does not promote 50xPYE or riboflavin stock-only Peptone, Yeast extract, Riboflavin, or nested Deionized water rows into top-level final-medium ingredients.
3. Preserve the TOGO preparation boundary by keeping autoclaving and filter-sterilization steps from data/normalized_yaml/bacterial/marine_caulobacter_medium_spyem_containing_sea_salts_and_nh4cl.yaml.

## Follow-up Checks

- Diff the regenerated M2273 YAML against data/normalized_yaml/bacterial/marine_caulobacter_medium_spyem_containing_sea_salts_and_nh4cl.yaml and verify the stock additions remain 2, 20, and 5 ml/L solution rows.
- Re-run open schema, strict schema, reference, and term validation on the regenerated merged M2273 output.
- Inspect the regenerated merged YAML to ensure only NH4Cl, Sea salts, and the final-medium 1 L deionized water remain as top-level ingredients.

## Additional Notes

- TOGO M2273 is a good example of why stock and final-medium quantities cannot be reviewed by scalar concentration alone: 100 g/L peptone is source-supported inside 50xPYE, but false when published as a final-medium concentration.
