# YAML Record Review: modified_methanocaldococcus_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_methanocaldococcus_medium__db540ec9.yaml
- Started UTC: 2026-09-24T12:16:49Z
- Finished UTC: 2026-09-24T12:16:49Z
- Verdict: needs curation

## Target

- Reviewed merged record `CultureMech:002834`, `modified_methanocaldococcus_medium`, generated from `data/normalized_yaml/archaea/modified_methanocaldococcus_medium.yaml`.
- The record represents JCM Medium J484 / MediaDive `mediadive.medium:J484`, named `MODIFIED METHANOCALDOCOCCUS MEDIUM`.
- The reviewed generated record is byte-equivalent in content to its normalized owner for the inspected fields; any correction should be made in the maintained normalized record or in the MediaDive import and merge logic, not directly in `data/merge_yaml/merged`.

## Validation

- LinkML open-schema validation: passed; `linkml-validate` exited 0 with `No issues found`.
- Strict validation: passed; `scripts/validate_strict.py` exited 0 and wrote only the TSV header, for 0 strict errors.
- Reference validation: passed; `linkml-reference-validator` checked 1 file and reported 0 reference checks and no failures.
- Term validation: passed; `linkml-term-validator` exited 0 and printed `Validation passed`.
- Embedded `curation_history` entries were not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The MediaDive source points to the JCM page with `GRMD=484` and a JCM label of `MODIFIED METHANOCALDOCOCCUS MEDIUM`, which matches the generated record's label and notes.
- The identity is duplicated: `data/normalized_yaml/archaea/TOGO_M485_Modified_Methanocaldococcus_Medium.yaml` also represents the same JCM 484 medium through TOGO `M485` / `JCM_M484`, has the same normalized `name`, and carries a second CultureMech identifier.
- No source-inspected JCM, MediaDive, or TOGO payload identified a target organism for this medium; the generated record correspondingly has no target organism assertion.

## Evidence

- MediaDive `J484` exposes a main solution containing the core salts, 5 ml Iron stock solution, 10 ml Trace minerals solution, 10 ml Trace vitamins, sodium thiosulfate pentahydrate, yeast extract, 2-mercaptoethanol, resazurin, and 1000 ml water.
- JCM `GRMD=484` preserves the same medium structure: the main recipe links Iron stock solution to Medium No. 228, includes a local Trace minerals stock, links Trace vitamins to Medium No. 197, and then lists the same late additions and preparation text.
- MediaDive solution `4242` is the Trace minerals solution stock with its own 1000 ml distilled water context. It is an embedded stock added at 10 ml per main solution, not a set of top-level 1 L additions.
- MediaDive solution `3861` is the Trace vitamins stock, again prepared as a 1000 ml stock and used as 10 ml per main solution.
- MediaDive solution `3904` for Iron stock solution has no parsed `recipe` array but its preparation step states that 0.2 g Fe(NH4)2(SO4)2 x 6 H2O is dissolved in 5 ml distilled water with 2 drops concentrated HCl and brought to 100 ml.
- The generated record lists the Trace minerals and Trace vitamins compounds as if their stock concentrations were main-medium concentrations, while no structured 5 ml Iron stock solution addition is present.

## Completeness

- Main salts, sodium thiosulfate pentahydrate, yeast extract, 2-mercaptoethanol, and resazurin are present.
- The 10 ml Trace minerals and 10 ml Trace vitamins additions are not preserved as solution additions; their components are flattened into the top-level ingredient list at stock concentration.
- The 5 ml Iron stock solution addition is missing as a structured addition, and the source Fe(NH4)2(SO4)2 x 6 H2O and acidified-water preparation are present only as free-text preparation context.
- The 1000 ml water entries for the main solution, Trace minerals solution, and Trace vitamins stock are absent.
- No target organism was available from the inspected source data.

## Findings

- Blocker: the MediaDive import flattened nested stock recipes into top-level ingredients without scaling them by the parent stock volume. For example, the generated record carries Trace minerals stock entries such as 1.5 g/L Nitrilotriacetic acid and 0.5 g/L MnSO4 x n H2O as top-level medium concentrations even though only 10 ml of that stock are added to the main solution.
- Blocker: duplicate compounds from the main medium and the Trace minerals stock were summed across recipe scopes. The generated record reports `CaCl2 x 2 H2O` as `0.23658500000000002` g/L from `0.136585 + 0.1`, `MgSO4 x 7 H2O` as `6.31707` g/L from `3.31707 + 3.0`, and `NaCl` as `30.2683` g/L from `29.2683 + 1.0`; those second values belong to the stock solution, not the main medium.
- Major: the 5 ml Iron stock solution main-medium ingredient was dropped as a structured addition, so the generated YAML cannot reconstruct the JCM/MediaDive formula from structured fields.
- Major: source water rows are omitted for the main solution and both preserved stocks, which makes the nested 1 L contexts less auditable.
- Major: JCM 484 is maintained twice under separate CultureMech IDs, once through MediaDive `J484` and once through TOGO `M485` / `JCM_M484`.

## Recommended Edits

- Teach the MediaDive import path to preserve nested solution boundaries instead of concatenating stock-solution recipes into the main ingredient array.
- Scale stock-solution components only if CultureMech intentionally wants final effective concentrations; otherwise retain a 10 ml Trace minerals solution addition and a 10 ml Trace vitamins addition with their stock recipes nested or linked.
- Preserve the 5 ml Iron stock solution as a first-class addition and attach the available acidified ferrous ammonium sulfate preparation from MediaDive solution `3904` in structured or note form.
- Keep duplicate consolidation scoped to a single recipe context so main-medium salts are not summed with stock-solution components.
- Add explicit distilled-water entries for the main solution and each stock solution if water rows are in scope for structured curation.
- Deduplicate the MediaDive `J484` and TOGO `M485` normalized records so the same JCM medium has one CultureMech record or an explicit cross-source equivalence.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validation after the MediaDive nested-solution handling is corrected.
- Compare the corrected record against both JCM `GRMD=484` and MediaDive `J484`, including Iron stock solution, Trace minerals solution, and Trace vitamins membership.
- Confirm that the TOGO `M485` import either merges into the same maintained record or is excluded as a duplicate before regeneration.

## Additional Notes

None found.
