# YAML Record Review: Alicyclobacillus Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ALICYCLOBACILLUS_MEDIUM.yaml
- Started UTC: 2026-09-21T10:18:41Z
- Finished UTC: 2026-09-21T10:21:35Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/ALICYCLOBACILLUS_MEDIUM.yaml`.

- Class: `MediaRecipe`
- ID: `CultureMech:005217`
- Label: `alicyclobacillus_medium`
- Original name: `ALICYCLOBACILLUS medium`
- Category: `bacterial`
- Media term: `komodo.medium:402`
- Generated status: generated merge of 22 source records: `KOMODO_402_ALICYCLOBACILLUS_medium.yaml`, `alicyclobacillus_medium.yaml`, `for_strains_of_a_cycloheptanicus.yaml`, and 19 KOMODO `medium_402_modified_for_dsm_*` records.

## Validation

All narrow record-level validators passed for the generated YAML shape:

- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ALICYCLOBACILLUS_MEDIUM.yaml`
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ALICYCLOBACILLUS_MEDIUM.yaml --out /private/tmp/ALICYCLOBACILLUS_MEDIUM.strict.tsv --workers 1 --quiet`
  - Summary: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ALICYCLOBACILLUS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Summary: 1 file validated, 0 total checks, all validations passed.
- PASS: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ALICYCLOBACILLUS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Summary: term validation passed; the command also printed the expected `eutils` / `pkg_resources` deprecation warning.
- Not checked: embedded `MediaRecipe.curation_history` semantics. The repository documents `just validate-history` for standalone records under `history/`, not as a focused one-file validator for generated embedded history.

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints still fail before target-specific validation because this project resolves `llvmlite==0.46.0` under Python 3.13 and crashes in `setuptools` with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`; the no-project Python 3.11 invocations above exercise the same validators against the target file.

## Identity and Grounding

The target's canonical source is KOMODO Medium 402, which locally maps to DSMZ Medium 402. The fetched DSMZ `DSMZ_Medium402.pdf` confirms the `ALICYCLOBACILLUS MEDIUM` formulation, pH 4.0, Solution A base, a 1 ml addition of Trace element solution SL-6 from DSMZ Medium 27, and separate liquid-versus-solid assembly instructions.

The target is not a faithful solid final medium. DSMZ 402's solid form uses double-strength Solution A made with 500 ml water, 1 ml SL-6, and Solution C containing 15 g agar in 500 ml water. The target instead records the SL-6 stock's internal trace salts at top level and keeps agar as `30 G_PER_L`, the concentration inside the 500 ml Solution C stock, not the final concentration after Solution C is combined with Solution A.

The direct DSMZ parent `data/normalized_yaml/bacterial/alicyclobacillus_medium.yaml` has the same flattened top-level chemistry but does retain the pH and a preparation step that distinguishes the liquid 1000 ml Solution A branch from the solid 500 ml Solution A plus 500 ml Solution C branch. Those preparation steps were lost when the KOMODO import became the canonical generated record.

## Evidence

Supported:

- CaCl2 x 2 H2O 0.25 g, MgSO4 x 7 H2O 0.5 g, ammonium sulfate 0.2 g, yeast extract 2 g, glucose 5 g, and KH2PO4 3 g in Solution A are supported by DSMZ Medium 402.
- pH 4.0 is supported by DSMZ Medium 402.
- The target's seven trace salts match the SL-6 stock recipe shown in DSMZ Medium 27 and in local stock `data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml`.
- CaCl2 x 2 H2O, MgSO4 x 7 H2O, ammonium sulfate, glucose, KH2PO4, agar, ZnSO4 x 7 H2O, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, and Na2MoO4 x 2 H2O have ingredient identities that match their source labels.

Unsupported or over-scoped:

- SL-6 is a 1 ml stock addition in DSMZ 402. The generated target promotes the SL-6 internal salts to final-medium top-level ingredients at stock concentration, about 1000 times too concentrated for the liquid 1 L branch.
- Agar is 15 g in 500 ml Solution C. The generated target stores `30 G_PER_L`, which is only the Solution C stock concentration; the solid final medium is made by combining Solution C with 500 ml Solution A.
- The generated merge dropped the direct DSMZ parent preparation text that explains separate sterilization and liquid-versus-solid assembly.
- The 5 g/L yeast-extract instruction for strains of `A. cycloheptanicus` is preserved only as `for_strains_of_a_cycloheptanicus` in the synonym list; the generated record does not represent it as a scoped strain-specific variant.
- NiCl2 x 6 H2O is linked to `CHEBI:34887` with canonical label `nickel dichloride`; that grounding loses the hexahydrate specified by DSMZ Medium 27.
- No structured DSMZ, KOMODO, or TOGO references are present, so `linkml-reference-validator` performed zero checks.

## Completeness

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ALICYCLOBACILLUS_MEDIUM.md'` searched the ignored timestamped-report directory and found no pre-existing ALICYCLOBACILLUS MEDIUM report.
- Exact `rg --no-ignore --hidden` searches for `mediadive.medium:402`, `komodo.medium:402`, `DSMZ Medium: 402`, `KOMODO_402_ALICYCLOBACILLUS_medium`, `ALICYCLOBACILLUS medium`, and `alicyclobacillus_medium` covered `data/normalized_yaml`, `data/merge_yaml`, and `data/import_tracking` while including ignored files. They found the 22-source generated target, the direct DSMZ parent, KOMODO 402 and its strain-specific 402 derivatives, TOGO M2390/M2391 liquid/solid DSMZ copies, and two separate generated TOGO outputs.
- DSMZ Medium 402, DSMZ Medium 27, and the TOGO M2390/M2391 API records were fetched live. TOGO M2390 corresponds to the liquid branch and M2391 corresponds to the solid branch; both share the same upstream DSMZ Medium 402 PDF.
- The local SL-6 stock `data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml` was inspected. Its trace salts match DSMZ Medium 27, but its water row is malformed as `1000 PERCENT_V_V` and it is still flagged `incomplete_composition`.

## Findings

### blocker: SL-6 stock ingredients are represented as final ingredients

DSMZ 402 adds 1 ml of Trace element solution SL-6. The target flattens the ZnSO4, MnCl2, H3BO3, CoCl2, CuCl2, NiCl2, and Na2MoO4 rows from the SL-6 stock into the medium's top-level ingredient list at stock strength, not at their 1 ml/L final contribution.

### blocker: the solid-medium agar concentration is still a Solution C stock value

DSMZ 402's solid branch uses 15 g agar in 500 ml water as Solution C and then combines that with Solution A. The target records agar as `30 G_PER_L`, which is the Solution C stock concentration, not the final agar concentration.

### major: liquid and solid assembly semantics were collapsed

DSMZ 402 has one branch that combines 1000 ml Solution A with 1 ml Solution B for liquid medium and a second branch that combines 500 ml Solution A, 1 ml Solution B, and 500 ml Solution C for solid medium. The generated merge is typed only as `SOLID_AGAR`, keeps no Solution A/B/C structure, and loses the DSMZ preparation step that explained separate sterilization and assembly.

### major: the A. cycloheptanicus yeast-extract variant is treated as a synonym

The DSMZ PDF specifically says strains of `A. cycloheptanicus` use 5 g/L yeast extract instead of 2 g/L. `for_strains_of_a_cycloheptanicus` is merged into the canonical KOMODO 402 record with a `SOURCE_DUPLICATE` relationship and preserved only as a synonym, so the strain-scoped 5 g/L variant is not represented.

### minor: NiCl2 x 6 H2O is grounded to an anhydrous nickel-chloride term

The source and preferred term specify nickel chloride hexahydrate, but the target grounds the row to `CHEBI:34887` / `nickel dichloride`.

## Recommended Edits

1. Fix `data/normalized_yaml/bacterial/alicyclobacillus_medium.yaml`, `data/normalized_yaml/bacterial/KOMODO_402_ALICYCLOBACILLUS_medium.yaml`, the 20 KOMODO 402 child records, and `data/normalized_yaml/bacterial/mediadive_25_Trace_element_solution_SL-6.yaml`; do not edit `data/merge_yaml/merged/ALICYCLOBACILLUS_MEDIUM.yaml` directly.
2. Represent SL-6 as a 1 ml addition to DSMZ Medium 402, with its internal formula owned by the repaired `mediadive_25_Trace_element_solution_SL-6.yaml` stock record.
3. Split the DSMZ 402 liquid and solid assemblies into explicit variants or scoped preparation branches so 1000 ml Solution A for liquid medium is not conflated with the 500 ml Solution A plus 500 ml Solution C solid branch.
4. Store agar as 15 g/L in the final solid medium, or keep the 30 g/L value only inside Solution C with an explicit 500 ml addition.
5. Preserve the separate-sterilization and final-combination instructions from DSMZ Medium 402.
6. Split the `A. cycloheptanicus` 5 g/L yeast-extract formulation out of `synonyms` into a real strain-scoped variant.
7. Reground NiCl2 x 6 H2O to a CHEBI term that preserves the hexahydrate, or leave it ungrounded rather than pointing at an anhydrous salt.
8. Add structured DSMZ 402, DSMZ 27, KOMODO 402, and TOGO M2390/M2391 references as applicable.

## Follow-up Checks

- Rerun the four one-file validators above against regenerated `data/merge_yaml/merged/ALICYCLOBACILLUS_MEDIUM.yaml`.
- Fetch DSMZ Medium 402 and DSMZ Medium 27 again and confirm the regenerated solid branch has 15 g/L final agar, the SL-6 stock remains nested at 1 ml/L, and the pH 4.0 and separate-sterilization preparation text round-trip.
- Search with `rg --no-ignore --hidden 'mediadive.medium:402\b|komodo.medium:402\b|TOGO:M2390\b|TOGO:M2391\b|mediadive.solution:25\b|komodo.medium:402.1\b' data/normalized_yaml/bacterial data/merge_yaml/merged` and confirm the direct DSMZ, KOMODO, TOGO, and SL-6 records are no longer split into incompatible flattened outputs.
- Run the ingredient term validator against the repaired normalized records and confirm `NiCl2 x 6 H2O` no longer resolves to an anhydrous `nickel dichloride` label.

## Additional Notes

- Optional target-organism and growth-metric slots were not treated as defects because DSMZ Medium 402 is a provider recipe, not primary growth evidence for a specific strain.
