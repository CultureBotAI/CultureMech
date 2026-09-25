# YAML Record Review: clostridiisalibacter_paucivorans_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/clostridiisalibacter_paucivorans_medium__ca7bf319.yaml
- Started UTC: 2026-09-22T09:00:00Z
- Finished UTC: 2026-09-22T09:02:11Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/clostridiisalibacter_paucivorans_medium__ca7bf319.yaml`, a generated `MediaRecipe` for `CultureMech:002921` / `clostridiisalibacter_paucivorans_medium`.

The record is generated from the single maintained source `data/normalized_yaml/bacterial/clostridiisalibacter_paucivorans_medium.yaml` with merge fingerprint `ca7bf3195f763b3f08d9c144f02d9f519cc081a03415d558dc8504580ad7c244`.

The source identity is JCM Medium 573 via `mediadive.medium:J573`, labelled `CLOSTRIDIISALIBACTER PAUCIVORANS MEDIUM`.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/clostridiisalibacter_paucivorans_medium__ca7bf319.yaml` | Pass |
| `python scripts/validate_strict.py data/merge_yaml/merged/clostridiisalibacter_paucivorans_medium__ca7bf319.yaml --out /private/tmp/clostridiisalibacter_paucivorans_medium__ca7bf319.strict.tsv --workers 1 --quiet` | Pass; TSV contained only the header row |
| `linkml-reference-validator validate data data/merge_yaml/merged/clostridiisalibacter_paucivorans_medium__ca7bf319.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass; 0 reference checks |
| `linkml-term-validator validate-data data/merge_yaml/merged/clostridiisalibacter_paucivorans_medium__ca7bf319.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass; emitted only the expected NCBI E-utilities deprecation warning |
| Embedded curation-history validation | Not checked: the documented `just validate-history` target validates standalone `history/` records, not embedded `MediaRecipe.curation_history` nodes in generated YAML |

`just` wrapper validators were not used because the project environment attempts to build `llvmlite==0.46.0` under Python 3.13 and fails inside setuptools. The equivalent focused LinkML, strict, reference, and term validators were run under `/usr/local/bin/python3.11` with offline cached packages.

## Identity and Grounding

The reviewed record points to the right JCM page: `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=573` returns Medium 573, `CLOSTRIDIISALIBACTER PAUCIVORANS MEDIUM`.

The ingredient and solution identities are not represented at the right preparation level:

- The JCM page has a 900 ml base recipe with 10 ml of `Trace minerals (see Medium No. 151)`.
- It then completes each 4.5 ml base aliquot with 0.1 ml of 15% MgCl2 x 6H2O, 0.3 ml of 5% NaHCO3, and 0.1 ml of 2% Na2S x 9H2O.
- JCM Medium 151 defines the trace-minerals stock as its own one-liter recipe.

The YAML flattens those boundaries: salts from JCM 151 and the three final stock additions are stored as top-level gram-per-liter ingredients in the J573 parent.

The exact hydrate groundings for MgCl2 x 6 H2O, MgSO4 x 7 H2O, FeSO4 x 7 H2O, CoSO4 x 7 H2O, CaCl2 x 2 H2O, ZnSO4 x 7 H2O, CuSO4 x 5 H2O, and Na2MoO4 x 2 H2O match their JCM labels. The generic `manganese(II) sulfate` grounding for `MnSO4 x n H2O` is appropriately not over-specified because JCM 151 gives a variable hydrate.

An ignored-inclusive search of `data/normalized_yaml`, `data/merge_yaml/merged`, `data/import_tracking`, and `reports` for `CultureMech:002921`, `mediadive.medium:J573`, `J573`, `GRMD=573`, the merge fingerprint, `clostridiisalibacter_paucivorans_medium.yaml`, and the exact uppercase label found the reviewed JCM owner, a malformed `Main sol. J573` solution record, and a separate TOGO M577 normalized/merged record that also names JCM `GRMD=573`.

## Evidence

The inspected JCM 573 HTML supports the pH 7.0 base-medium instruction, the N2-CO2 4:1 gas mixture, butyl-stoppered autoclaving, NaHCO3 filter sterilization/storage under N2-CO2, and anaerobic storage of the other solutions under N2.

The JCM 573 and JCM 151 pages also show that the current concentration arithmetic is wrong:

- `KH2PO4`, `K2HPO4`, `NH4Cl`, and NaCl values such as `0.329308`, `1.09769`, and `43.9078` are the source masses divided by an inferred 0.911 L intermediate volume. They are not the final per-liter values after using 4.5 ml of base in a 5.0 ml completed tube.
- The top-level NaCl value merges 43.9078 from the 900 ml base with 1.0 from the one-liter trace-minerals stock, even though only 10 ml of the trace stock is added.
- The trace minerals from JCM 151 are present at full one-liter stock strengths, not at the 10 ml aliquot strength used by JCM 573.
- MgCl2 x 6H2O, NaHCO3, and Na2S x 9H2O are stored as 0.1, 0.3, and 0.1 `G_PER_L`, but those source numbers are milliliters of percent stock solutions added per 4.5 ml of base medium.

The maintained `data/normalized_yaml/bacterial/mediadive_4401_Main_sol_J573.yaml` object preserves the intermediate 0.911 L volume and the three percent stock additions as `PERCENT_V_V`, but it is also malformed as a solution: it lives under `data/normalized_yaml/bacterial/`, has a placeholder `See source for composition` ingredient, and carries an `incomplete_composition` flag.

## Completeness

The record captures JCM 573's label, source URL, pH target, gas mixture, and general autoclave/filter-sterilize preparation text, so the identity is recoverable.

The recipe is not complete enough to follow safely. It omits the explicit 900 ml distilled-water base row, erases the trace-minerals stock boundary, erases the 4.5 ml plus 0.5 ml completion arithmetic, and represents percent stock additions as final gram-per-liter salts.

The exact ignored-inclusive search also found `data/normalized_yaml/bacterial/TOGO_M577_Clostridiisalibacter_Paucivorans_Medium.yaml` and `data/merge_yaml/merged/CLOSTRIDIISALIBACTER_PAUCIVORANS_MEDIUM.yaml`, a second CultureMech record for the same JCM 573 recipe through TOGO. That duplicate has different broken solution structure and is not merged with this direct JCM record.

Empty target-organism, storage, salinity, and light fields are acceptable for the inspected JCM page; the public JCM recipe itself does not identify a strain, storage condition, salinity, or light condition.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | Main-medium concentration arithmetic is wrong: source masses were divided by an inferred 0.911 L intermediate volume, producing values like `NaCl` 43.9078 `G_PER_L`, instead of preserving the 900 ml base plus 10 ml trace stock plus 0.5 ml final stock additions. | `data/normalized_yaml/bacterial/clostridiisalibacter_paucivorans_medium.yaml`; likely the MediaDive JCM importer |
| Major | The `Trace minerals (see Medium No. 151)` 10 ml stock is flattened into the J573 parent at full one-liter stock concentrations. This also caused the parent `NaCl` value to be merged with the trace stock's `NaCl` row as `44.9078` `G_PER_L`. | `data/normalized_yaml/bacterial/clostridiisalibacter_paucivorans_medium.yaml` and stock import logic for JCM 151 |
| Major | The 15% MgCl2 x 6H2O, 5% NaHCO3, and 2% Na2S x 9H2O additions were imported as 0.1, 0.3, and 0.1 `G_PER_L`; JCM gives those numbers as milliliters of stock solution per 4.5 ml of base medium. | `data/normalized_yaml/bacterial/clostridiisalibacter_paucivorans_medium.yaml` and `data/normalized_yaml/bacterial/mediadive_4401_Main_sol_J573.yaml` |
| Major | Duplicate source identity remains unresolved: the TOGO M577 record points to the same JCM `GRMD=573` URL but survives as `CultureMech:009973` instead of merging with direct JCM `CultureMech:002921`. | MediaDive/TOGO deduplication or merge logic; direct owners are `data/normalized_yaml/bacterial/clostridiisalibacter_paucivorans_medium.yaml` and `data/normalized_yaml/bacterial/TOGO_M577_Clostridiisalibacter_Paucivorans_Medium.yaml` |
| Minor | The `Main sol. J573` auxiliary solution record is indexed as a solution but is stored under `data/normalized_yaml/bacterial/`, retains placeholder `ingredients`, and is flagged `incomplete_composition`. | `data/normalized_yaml/bacterial/mediadive_4401_Main_sol_J573.yaml` |

No blocker findings were found. The JCM 573 identity is correct and the ingredient labels generally preserve exact salt hydrates where JCM specifies them.

## Recommended Edits

1. Rework the JCM/MediaDive import for J573 so the parent record preserves the 900 ml base recipe, the 10 ml JCM 151 trace-mineral stock reference, and the three completion stock additions as stock solutions with milliliter aliquots.
2. Model JCM Medium 151 trace minerals as a reusable one-liter stock and dilute it into JCM 573 instead of flattening its ingredients into the parent medium.
3. Correct the three final stock additions so 0.1 ml 15% MgCl2 x 6H2O, 0.3 ml 5% NaHCO3, and 0.1 ml 2% Na2S x 9H2O are represented as solution additions, not as 0.1/0.3/0.1 `G_PER_L` final salts.
4. Merge or otherwise deduplicate TOGO M577 and MediaDive J573 so only one CultureMech identity represents the JCM `GRMD=573` page.
5. Move or regenerate `Main sol. J573` into the correct solution layer if it remains useful after the J573 import is corrected.

## Follow-up Checks

- Rerun the focused schema, strict, term, and reference validators on the maintained J573 owner and any regenerated stock-solution records.
- Regenerate merged YAML and verify that no generated record for JCM 573 carries the obsolete `ca7bf3195f763b3f08d9c144f02d9f519cc081a03415d558dc8504580ad7c244` fingerprint.
- Re-run the MediaDive/TOGO duplicate report or inspect an ignored-inclusive exact search for `GRMD=573`, `mediadive.medium:J573`, and `TOGO:M577` to confirm that the direct JCM and TOGO imports no longer publish as separate recipes.
- Manually compare the regenerated parent, the JCM 151 trace-mineral stock, and the three completion stocks against the JCM 573 and 151 HTML pages.

## Additional Notes

The exact duplicate/source search was gitignore-independent and covered `data/normalized_yaml`, `data/merge_yaml/merged`, `data/import_tracking`, and `reports`. Its non-owner hits included `data/import_tracking/reports/merged_duplicates.tsv`, which already flags the merged `NaCl` row as needing the source recipe.
