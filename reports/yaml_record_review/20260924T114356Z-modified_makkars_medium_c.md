# YAML Record Review: Modified Makkar's Medium C

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_makkars_medium_c.yaml
- Started UTC: 2026-09-24T11:43:56Z
- Finished UTC: 2026-09-24T11:43:56Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/modified_makkars_medium_c.yaml`.

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| CultureMech ID | `CultureMech:007832` |
| Name | `modified_makkars_medium_c` |
| Source identity | `TOGO:M1299`, originally JCM `JCM_M1212` |
| Category | `bacterial` |
| Maintained owner | `data/normalized_yaml/bacterial/TOGO_M1299_Modified_Makkar_s_Medium_C.yaml` |
| Generated artifact | yes; generated under `data/merge_yaml/merged/` from one TOGO-normalized source |

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_makkars_medium_c.yaml` reported `No issues found`. |
| Strict CultureMech validation | Passed; `scripts/validate_strict.py data/merge_yaml/merged/modified_makkars_medium_c.yaml --out /private/tmp/modified_makkars_medium_c.strict.tsv --workers 1 --quiet` reported 0 errors and wrote only the TSV header line. |
| Reference validation | Passed; `linkml-reference-validator validate data data/merge_yaml/merged/modified_makkars_medium_c.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` checked one file, ran 0 reference checks, and reported no errors. |
| Term validation | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/modified_makkars_medium_c.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0 after a harmless `pkg_resources` deprecation warning. |
| Embedded history validation | Not checked: the available `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

## Identity and Grounding

The record denotes TOGO M1299, "Modified Makkar's Medium C", which TOGO marks as an archived JCM `JCM_M1212` record. Its source identity and title are coherent, but the generated formula no longer represents the nested TOGO/JCM recipe.

An exact gitignore-independent search under `data/normalized_yaml/` found a second maintained record with the same slug and same underlying JCM identity: `data/normalized_yaml/bacterial/modified_makkars_medium_c.yaml` is MediaDive/JCM `mediadive.medium:J1212` with CultureMech ID `CultureMech:002381`. The generated merge kept only the TOGO source, so the two JCM 1212 imports remain unmerged with different CultureMech IDs and conflicting formula shapes.

## Evidence

TOGO M1299 and MediaDive J1212 agree on the medium identity and nested structure. The provider recipe contains a main solution with 650 ml distilled water, 2.5 g yeast extract, 10 g Casitone, 6 g NaHCO3, 1 g L-cysteine HCl x H2O, 1 mg resazurin, 150 ml Solution I, 150 ml Solution II, 50 ml clarified rumen fluid, CO2, and N2. After autoclaving, 20 ml of 0.2 M cellobiose solution is added aseptically and anaerobically per liter.

The inspected stock recipes are:

| Stock | Source contents |
|---|---|
| Solution I | 3 g K2HPO4 in 1 L distilled water |
| Solution II | 3 g KH2PO4, 6 g `(NH4)2SO4`, 6 g NaCl, 0.6 g MgSO4 x 7 H2O, 0.6 g CaCl2 x 2 H2O in 1 L distilled water |

The generated record conflicts with that evidence in several material ways:

| Source claim | Generated YAML |
|---|---|
| Resazurin is `1 mg` in the main recipe | `Resazurin` is `1` `G_PER_L` |
| Solution I is a 150 ml stock addition whose recipe is 3 g K2HPO4 in 1 L water | `Solution I (see below)` has empty `composition: []`, `name: Unknown solution`, and `150` `G_PER_L` |
| Solution II is a 150 ml stock addition with five salts in 1 L water | `Solution II (see below)` has empty `composition: []`, `name: Unknown solution`, and `150` `G_PER_L` |
| Clarified rumen fluid is a 50 ml addition cross-referenced to Medium M258 | `Rumen fluid, clarified (see Medium [M258])` is an empty solution with `50` `G_PER_L` |
| Cellobiose is 20 ml of a 0.2 M stock | `0.2 M Cellobiose solution` is an empty solution with `20` `G_PER_L` |
| Main, Solution I, and Solution II each have separate water rows | all three water rows were merged into one `Distilled water` ingredient at `652.0` `G_PER_L` |

The direct JCM CGI URL still named by TOGO and MediaDive was inspected but now returns `Nothing found` for medium number 1212.

## Completeness

The generated record is not complete enough to reconstruct the source. It stores four empty stock solutions, drops the Solution I and Solution II component boundaries, loses the 0.2 M concentration of the cellobiose stock, and converts several volume additions into mass-per-volume concentrations.

No target organism claims were expected from the inspected TOGO or MediaDive recipe payloads.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| blocker | The TOGO-derived record collapses nested stock solutions and water rows into a formula that cannot reproduce the source protocol. | TOGO and MediaDive keep Solution I, Solution II, clarified rumen fluid, and 0.2 M cellobiose as additions to the main medium; the generated YAML has empty `solutions`, stock salts as top-level ingredients, and one 652.0 `G_PER_L` distilled-water row made from unrelated 650 ml, 1 L, and 1 L water rows. | Fix `data/normalized_yaml/bacterial/TOGO_M1299_Modified_Makkar_s_Medium_C.yaml` and the TOGO solution migration/import logic, then regenerate `data/merge_yaml/merged/`. |
| blocker | Resazurin is off by a factor of at least 1000. | TOGO and MediaDive both encode 1 mg resazurin in the main solution; the generated YAML encodes 1 `G_PER_L`. | Correct the TOGO import unit handling in `data/normalized_yaml/bacterial/TOGO_M1299_Modified_Makkar_s_Medium_C.yaml` and the importer path that maps milligram quantities. |
| major | The same JCM M1212 medium is maintained twice with different CultureMech IDs. | The TOGO source is `TOGO:M1299` with original JCM `JCM_M1212`; `data/normalized_yaml/bacterial/modified_makkars_medium_c.yaml` is a MediaDive/JCM import of `mediadive.medium:J1212` with `CultureMech:002381`. | Reconcile `data/normalized_yaml/bacterial/TOGO_M1299_Modified_Makkar_s_Medium_C.yaml` with `data/normalized_yaml/bacterial/modified_makkars_medium_c.yaml` after the nested recipe is represented correctly. |

## Recommended Edits

1. Rebuild the TOGO-normalized record so Solution I and Solution II remain structured stocks with their own compositions instead of empty `Unknown solution` rows.
2. Preserve volume additions as volume additions: 150 ml Solution I, 150 ml Solution II, 50 ml clarified rumen fluid, and 20 ml of 0.2 M cellobiose solution.
3. Correct the resazurin source amount from `1 G_PER_L` to the source-supported 1 mg quantity, converted only with an explicit final-volume model.
4. Keep main-water, Solution I water, and Solution II water scoped to their respective solution recipes; do not merge them into a single top-level concentration.
5. Reconcile the TOGO and MediaDive J1212 imports so `modified_makkars_medium_c` has one CultureMech identity with explicit cross-references to both source accessions.

## Follow-up Checks

- Rerun focused LinkML, strict, reference, and term validation on `data/merge_yaml/merged/modified_makkars_medium_c.yaml`.
- Re-open the TOGO M1299 API payload and the MediaDive J1212 REST payload and confirm every main-medium addition and stock row remains present at the right preparation boundary.
- Confirm no generated `Modified Makkar's Medium C` row contains `Unknown solution`, an empty stock `composition`, a 652.0 `G_PER_L` distilled-water row, or a 1 `G_PER_L` resazurin row.
- Run an exact gitignore-independent search for `JCM_M1212`, `J1212`, `TOGO:M1299`, and `mediadive.medium:J1212` under `data/normalized_yaml/` to confirm the duplicate source identities have been reconciled.

## Additional Notes

- `just` validators were not used because project dependency resolution attempts to build `llvmlite==0.46.0` under Python 3.13; the focused validators were run with `/usr/local/bin/python3.11` and the offline review cache instead.
- Direct JCM lookup for `GRMD=1212` is no longer sufficient for this review because JCM returned `Nothing found`; the TOGO API and MediaDive REST copy still preserved the old JCM formula.
