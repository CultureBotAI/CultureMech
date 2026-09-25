# YAML Record Review: Autotrophic_Nitrobacter_Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml
- Started UTC: 2026-09-21T16:50:20Z
- Finished UTC: 2026-09-21T16:52:44Z
- Verdict: needs curation

## Target

| Field | Observed |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:008936 |
| name | autotrophic_nitrobacter_medium |
| original_name | Autotrophic Nitrobacter Medium |
| category | bacterial |
| media_term | TOGO:M2351, Autotrophic Nitrobacter Medium |
| generated status | Generated merge artifact in data/merge_yaml/merged |
| maintained owner | data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml |

The target is the generated merge for one TOGO source record,
`TOGO_M2351_Autotrophic_Nitrobacter_Medium`, with merge fingerprint
`86af46dcac6fa36f1e01346a224fbd16fbb82c113dc816a455fd546cd35581c3`.

## Validation

| Check | Result |
|---|---|
| Open schema | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml` completed with no errors. |
| Strict validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml --out /private/tmp/Autotrophic_Nitrobacter_Medium.strict.tsv --workers 1 --quiet` completed with no errors. |
| Reference validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` completed with 0 checks. |
| Term validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` completed with no errors, aside from a non-fatal `eutils`/`pkg_resources` deprecation warning. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for standalone `history/` files, not a focused embedded `MediaRecipe.curation_history` validator for one merge record. |
| Direct `just` validators | Not checked: the project-level `uv` environment currently fails before target-specific validation while building `llvmlite==0.46.0` under Python 3.13, with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The no-project LinkML validator workaround above exercised the target schema, strict, reference, and term checks. |

## Identity and Grounding

- The generated TOGO identity is supported: TOGO API data for `M2351` names `Autotrophic Nitrobacter Medium` and cites `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium756c.pdf`, matching the target's `media_term` and notes.
- DSMZ 756c is an autotrophic variant of DSMZ Medium 756. The DSMZ 756c PDF says to use medium 756 with 2 g/L NaNO2 and to omit yeast extract, peptone, and Na-pyruvate.
- The adjacent `data/normalized_yaml/bacterial/autotrophic_nitrobacter_medium.yaml` record is another DSMZ/MediaDive/KOMODO 756c representation with ID `CultureMech:001891`; it is not the TOGO M2351 owner for this generated target.
- The record denotes the intended DSMZ 756c medium, but the stock identities, concentration context, preparation conditions, and medium classification are not grounded correctly.

## Evidence

Supported by inspected source text:

- DSMZ 756c inherits DSMZ Medium 756 but raises NaNO2 to 2 g/L and removes yeast extract, peptone, and Na-pyruvate.
- DSMZ Medium 756 uses 899 ml distilled water, 1 ml trace element solution, and 100 ml stock solution in the final liter.
- The DSMZ trace element solution is a per-liter stock containing 33.80 mg MnSO4 x H2O, 49.40 mg H3BO3, 43.10 mg ZnSO4 x 7 H2O, 37.10 mg (NH4)6Mo7O24, 97.30 mg FeSO4 x 7 H2O, 25.00 mg CuSO4 x 5 H2O, and 1000 ml distilled water.
- The DSMZ stock solution is a per-liter stock containing 0.07 g CaCO3, 5.00 g NaCl, 0.50 g MgSO4 x 7 H2O, 1.50 g KH2PO4, and 1000 ml distilled water.
- DSMZ 756c adjusts pH to 8.6 with NaOH or KOH, autoclaves, and leaves the medium for 2-3 days so pH self-adjusts to 7.4-7.6.

Unsupported or over-scoped claims:

- The generated record points the two final-stock additions at `mediadive.solution:6187` and `mediadive.solution:6127`. Those records are an EDTA/chloride trace stock and a nitrate/phosphate stock; they do not match DSMZ 756's local embedded stock recipes.
- Trace-element-stock salts are top-level final-medium ingredients at 25-97.3 g/L, but DSMZ 756 lists those same quantities as milligrams inside a 1000 ml trace stock that is added at 1 ml/L.
- Stock-solution salts are top-level ingredients at their full stock strengths, but DSMZ 756 adds that stock at 100 ml/L.
- `Distilled water` is `2899.0 G_PER_L`, apparently summing 899 ml final-medium water, 1000 ml trace-stock water, and 1000 ml stock-solution water across three preparation contexts.
- The record has no `ph_value`, pH range, or preparation steps for the DSMZ 756c pH adjustment, autoclaving, and 2-3 day post-autoclave stand.
- The record classifies the medium as `COMPLEX` and `UNDEFINED`, but DSMZ 756c explicitly omits the yeast extract, peptone, and Na-pyruvate from the heterotrophic parent. The remaining medium is chemically defined.
- `MgSO4 x 7 H2O` has the correct primary `CHEBI:31795` heptahydrate term, but its `mediaingredientmech_chebi_term` still points at generic `CHEBI:32599` magnesium sulfate.

## Completeness

- Source provenance points a reader to TOGO M2351 and the DSMZ 756c PDF. A complete repair also needs the inherited DSMZ Medium 756 PDF because DSMZ 756c is expressed as a delta from medium 756.
- The existing `mediadive_1545_Trace_element_solution.yaml` and `mediadive_1544_Stock_solution.yaml` records contain the local DSMZ 756 stock members. They are closer than the linked `mediadive.solution:6187` and `mediadive.solution:6127` records, but still need review because their water rows are represented as `1000 PERCENT_V_V`.
- Empty organism/growth slots are acceptable for this source recipe. The inspected DSMZ and TOGO sources establish the formulation, not growth of a specific strain.
- Gitignore-independent search covered `data/normalized_yaml`, `data/merge_yaml`, `reports/yaml_record_review`, `history`, and `.claude` for `Autotrophic Nitrobacter Medium`, `autotrophic_nitrobacter_medium`, `CultureMech:008936`, `TOGO:M2351`, `M2351`, and `DSMZ_Medium756c`. It found adjacent DSMZ/MediaDive/KOMODO records for the 756-family media and no prior Markdown report for this exact generated record.
- Exact gitignore-independent search for `mediadive.solution:6187` and `mediadive.solution:6127` found many unrelated uses of the generic global solutions, including this record; exact search for `mediadive.solution:1544` and `mediadive.solution:1545` found only index entries and the two local solution records.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | The two solution references point to the wrong stock recipes. | DSMZ 756 uses local sulfate/carbonate/nitrite-family stock recipes; `mediadive.solution:6187` is an EDTA/chloride trace solution and `mediadive.solution:6127` is a nitrate/phosphate stock. | `data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml` plus stock-solution generation/linking rules. |
| Major | The trace-element stock is flattened into the final medium and inflated from mg to g. | DSMZ 756 lists 25-97.3 mg quantities per liter of trace stock and adds that stock at 1 ml/L; the generated top-level rows record 25-97.3 g/L final-medium concentrations. | TOGO stock-solution importer / `solution-migrator-v1.0`. |
| Major | The 100 ml/L stock solution is flattened at full stock strength. | DSMZ 756 adds 100 ml/L of a stock containing 0.07 g CaCO3, 5 g NaCl, 0.5 g MgSO4 x 7 H2O, and 1.5 g KH2PO4 per liter; the generated top-level rows keep those undiluted per-liter stock amounts. | TOGO stock-solution importer / `solution-migrator-v1.0`. |
| Major | Distilled-water quantities from three contexts are merged into one impossible mass concentration. | DSMZ 756 has 899 ml water in the final medium plus 1000 ml in each stock recipe; the generated record has `2899.0 G_PER_L`. | TOGO solution-boundary migration and duplicate-water merge cleanup. |
| Major | The DSMZ 756c pH and standing instructions are missing. | DSMZ 756c says to adjust pH to 8.6 with NaOH or KOH, autoclave, and leave the medium for 2-3 days so pH can settle to 7.4-7.6. The generated record has no pH or preparation steps. | `data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml`. |
| Major | Medium classification still describes a complex, undefined recipe even though DSMZ 756c removes the undefined parent ingredients. | The source variant omits yeast extract, peptone, and Na-pyruvate from DSMZ 756; the remaining NaNO2, mineral stocks, CaCO3, NaCl, MgSO4 x 7 H2O, and KH2PO4 are defined chemicals. | `data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml` or the TOGO import classification rule. |
| Minor | `high_metal: true` is likely an artifact of the inflated trace stock. | The apparent high metal burden is created by gram-level top-level trace rows that should remain mg/L stock components or microgram/L final-medium contributions. | Recompute quality flags after fixing stock nesting. |
| Minor | The MgSO4 x 7 H2O MediaIngredientMech CHEBI link is stale. | The primary term is the correct heptahydrate, `CHEBI:31795`, but `mediaingredientmech_chebi_term` still points to generic magnesium sulfate, `CHEBI:32599`. | CHEBI/MIM enrichment for `data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml`. |

## Recommended Edits

1. Remove the `mediadive.solution:6187` and `mediadive.solution:6127` links from the TOGO M2351 record; they are unrelated stock recipes.
2. Reference or inline the DSMZ 756 local stock recipes at their final-medium volumes: 1 ml/L for `mediadive.solution:1545` and 100 ml/L for `mediadive.solution:1544`, after repairing any water-unit defects in those `SolutionRecipe` owners.
3. Move H3BO3, FeSO4 x 7 H2O, ZnSO4 x 7 H2O, CuSO4 x 5 H2O, MnSO4 x H2O, (NH4)6Mo7O24, CaCO3, NaCl, MgSO4 x 7 H2O, and KH2PO4 out of final top-level ingredients.
4. Preserve the final DSMZ 756c formulation exactly: NaNO2 2 g/L, 899 ml distilled water, 1 ml trace element solution, 100 ml stock solution, and no yeast extract, peptone, or Na-pyruvate.
5. Add the DSMZ 756c pH and preparation sequence: adjust to pH 8.6 with NaOH or KOH, autoclave, and leave the medium for 2-3 days to reach pH 7.4-7.6.
6. Reclassify the medium as chemically defined and recompute `high_metal` or other derived flags after the stock nesting is fixed.

## Follow-up Checks

- `just validate-strict data/normalized_yaml/bacterial/TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml` after the maintained TOGO record is repaired.
- `just validate-terms` on any corrected DSMZ-756-local `SolutionRecipe` records.
- `just verify-merges` after regenerating `data/merge_yaml/merged/Autotrophic_Nitrobacter_Medium.yaml`.
- Manual comparison with DSMZ 756 and DSMZ 756c to verify the generated medium has 1 ml/L trace-element stock, 100 ml/L stock solution, 899 ml water, 2 g/L NaNO2, no heterotrophic supplements, and the pH 8.6 to 7.4-7.6 preparation context.

## Additional Notes

- This defect pattern matches the sibling TOGO M2350 10% Mixotrophic Nitrobacter import reviewed in `reports/yaml_record_review/20260921T042843Z-10_mixotrophic_nitrobacter_medium.md`.
- `linkml-reference-validator` performed zero checks because this generated record has no `references` block.
