# YAML Record Review: ACETIVIBRIO MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml
- Started UTC: 2026-09-21T08:25:47Z
- Finished UTC: 2026-09-21T08:26:19Z
- Verdict: needs curation

## Target

- Reviewed generated record `data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml`.
- Stable identifier: `CultureMech:002198`.
- Source identity asserted by the canonical record: JCM Medium J1013 / MediaDive `mediadive.medium:J1013`.
- The generated record was merged from one source owner, `JCM_J1013_ACETIVIBRIO_MEDIUM`, on fingerprint `0a8a39e6e8e61f26fd910231941aef7323cdfa1f191de06c53bee10023571ddb`.
- Current authoritative owner: `data/normalized_yaml/bacterial/JCM_J1013_ACETIVIBRIO_MEDIUM.yaml`.

## Validation

- PASS: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml`
- PASS: `scripts/validate_strict.py data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml`
- PASS: `linkml-reference-validator validate data data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- PASS: `linkml-term-validator validate-data data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
- Not checked: embedded `MediaRecipe.curation_history` entries; the documented history validator targets standalone files under `history/`.

## Identity and Grounding

- JCM GRMD `1013` resolves and identifies the source as `1013 ACETIVIBRIO MEDIUM`.
- TOGO Medium `M1071` is a copy of the same JCM source: its metadata names original media `JCM_M1013`, links to the same `GRMD=1013` page, and carries the same pH range, final-medium additions, and basal-medium formula.
- A gitignore-independent exact search for `mediadive.medium:J1013`, `TOGO:M1071`, `JCM_M1013`, `GRMD=1013`, and `JCM_J1013_ACETIVIBRIO_MEDIUM` found the expected direct JCM owner, expected TOGO owner, their two generated merges, expected index rows, and historical reports.
- The same `acetivibrio_medium` file stem is also used for DSMZ Medium 122 / MediaDive `mediadive.medium:122`, but that pH 7.0-7.2 recipe has a distinct composition and should remain separate from JCM 1013.

## Evidence

- JCM Medium 1013 is assembled from 950 ml Basal medium, 1 ml Trace element solution SL-10, 1 ml Selenite-tungstate solution, 10 ml Vitamin solution, 30 ml NaHCO3 5% w/v, 10 ml sucrose 20% w/v, 50 mg yeast extract, and 0.25 g Na2S.9H2O.
- The generated direct JCM record imports NaHCO3 and sucrose as `30 G_PER_L` and `10 G_PER_L`; those are stock-addition volumes, while the intended final amounts are approximately 1.5 g/L NaHCO3 and 2.0 g/L sucrose.
- The generated direct JCM record imports `Vitamin solution` as a solution with `concentration.value: 10` and `unit: G_PER_L`, losing the fact that 10 ml of a stock solution is added to each liter of final medium.
- Trace element solution SL-10 and Selenite-tungstate solution were expanded into their components at stock strength: for example HCl is `2.5 G_PER_L`, FeCl2.4H2O is `1.5 G_PER_L`, ZnCl2 is `0.07 G_PER_L`, NaOH is `0.5 G_PER_L`, Na2SeO3.5H2O is `0.003 G_PER_L`, and Na2WO4.2H2O is `0.004 G_PER_L` instead of being diluted from 1 ml/L stock additions.
- Basal-medium salts are imported at the 950 ml basal-medium recipe strength rather than the final 950 ml/L addition strength: for example KH2PO4 is `1.47368 G_PER_L` instead of 1.4 g/L, NH4Cl is `0.526316 G_PER_L` instead of 0.5 g/L, and MgCl2.6H2O is `0.210526 G_PER_L` instead of 0.2 g/L.

## Completeness

- The generated merge is incomplete because the TOGO `M1071` source duplicate is not reconciled with the direct JCM owner.
- The generated direct JCM owner omits distilled water from the basal medium.
- The generated direct JCM record collapses a pH 7.7-7.9 source range into scalar `ph_value: 7.8`.
- The stock hierarchy is absent, so reviewers cannot tell which ingredients belong to Basal medium, Trace element solution SL-10, Selenite-tungstate solution, and Vitamin solution.

## Findings

- BLOCKER: 30 ml of 5% NaHCO3 and 10 ml of 20% sucrose are represented as `30 G_PER_L` and `10 G_PER_L` instead of approximately 1.5 g/L and 2.0 g/L final concentrations.
- BLOCKER: Trace element solution SL-10 and Selenite-tungstate solution are flattened at full stock strength even though each stock is added at only 1 ml/L.
- BLOCKER: `Vitamin solution` stores a 10 ml/L volume as `10 G_PER_L`, has no inline composition, and therefore encodes neither the JCM 197 stock identity nor final vitamin concentrations.
- MAJOR: Basal-medium components are rescaled to per-liter basal stock strength instead of being left as their source masses for the 950 ml/L basal addition or as correctly calculated final amounts.
- MAJOR: the direct JCM and TOGO duplicate records are not merged, leaving `data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml` and `data/merge_yaml/merged/acetivibrio_medium__a428d46a.yaml` as duplicate generated records for JCM GRMD 1013.
- MINOR: scalar `ph_value: 7.8` loses the source pH range `7.7 - 7.9`.

## Recommended Edits

- Re-curate `data/normalized_yaml/bacterial/JCM_J1013_ACETIVIBRIO_MEDIUM.yaml` from JCM Medium 1013 with Basal medium, Trace element solution SL-10, Selenite-tungstate solution, Vitamin solution, NaHCO3 5% w/v, and sucrose 20% w/v represented as named stocks or correctly diluted final components.
- Preserve the JCM pH 7.7-7.9 range rather than collapsing it to `ph_value: 7.8`.
- Add the basal-medium distilled water row or keep water explicitly inside a named Basal medium recipe.
- Mark `data/normalized_yaml/bacterial/TOGO_M1071_Acetivibrio_Medium.yaml` as a duplicate of the direct JCM owner after the same stock-addition semantics are preserved.
- Regenerate `data/merge_yaml/merged/ACETIVIBRIO_MEDIUM.yaml` after normalized repair.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after normalized repair and merge regeneration.
- Re-fetch JCM GRMD `1013` and TOGO `M1071`, verify the JCM and TOGO source formulas agree, and confirm every stock addition is either represented as a stock volume or diluted into the final medium by the correct volume.
- Re-run an exact ignored-file-inclusive search for `mediadive.medium:J1013`, `TOGO:M1071`, `JCM_M1013`, and `GRMD=1013` to confirm the direct JCM and TOGO copies merge into one generated record.

## Additional Notes

- The normalized direct JCM owner already retains the JCM anaerobic preparation text; ingredient hierarchy and duplicate reconciliation are the primary repairs.
