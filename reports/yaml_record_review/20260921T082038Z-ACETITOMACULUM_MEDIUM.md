# YAML Record Review: ACETITOMACULUM medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml
- Started UTC: 2026-09-21T08:19:11Z
- Finished UTC: 2026-09-21T08:20:38Z
- Verdict: needs curation

## Target

- Reviewed generated record `data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml`.
- Stable identifier: `CultureMech:005968`.
- Source identity asserted by the canonical record: KOMODO ModelSEED `540`, copied from DSMZ Medium 540 / MediaDive `mediadive.medium:540`.
- The generated record was merged from two source owners, `KOMODO_540_ACETITOMACULUM_medium` and `acetitomaculum_medium`, on fingerprint `7217671110030d498118c836450613fcc9f3fccc5b4a27bf59e138d4ad0f416c`.
- Current authoritative owners: `data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml` and `data/normalized_yaml/bacterial/acetitomaculum_medium.yaml`.

## Validation

- PASS: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml`
- PASS: `scripts/validate_strict.py data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml`
- PASS: `linkml-reference-validator validate data data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- PASS: `linkml-term-validator validate-data data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
- Not checked: embedded `MediaRecipe.curation_history` entries; the documented history validator targets standalone files under `history/`.

## Identity and Grounding

- The KOMODO/DSMZ duplicate relationship is coherent: the KOMODO owner explicitly says it copied DSMZ Medium 540, and both normalized owners have the same ingredient/concentration signature.
- The DSMZ Medium 540 PDF resolves and identifies the source as `540: ACETITOMACULUM MEDIUM`.
- A gitignore-independent exact search for `komodo.medium:540`, `mediadive.medium:540`, `DSMZ Medium 540`, `DSMZ_Medium540`, and `KOMODO_540_ACETITOMACULUM_medium` found the expected KOMODO owner, expected DSMZ owner, their generated merge, and source-index rows.
- Many ChEBI groundings are plausible label matches, including KH2PO4, Na2SO4, NH4Cl, KCl, MgCl2.6H2O, CaCl2.2H2O, NaHCO3, D-glucose, L-cysteine.HCl.H2O, and Na2S.9H2O.
- The source is anaerobic: DSMZ instructs sparging with 80% N2 / 20% CO2, dispensing under that gas, and preparing reducing-agent stocks under 100% N2. The KOMODO notes nevertheless say `Aerobic: Yes`.

## Evidence

- DSMZ lists the base medium plus several liquid additions: 10 ml Modified Wolin's mineral solution, 1 ml 0.1% NiCl2.6H2O, 0.10 ml 0.1% Na2WO4.2H2O, four 0.50 ml vitamin-like 0.01% stocks, 1 ml Wolin's vitamin solution (10x), and the reducing agents.
- The target imports Modified Wolin's mineral solution components at their full stock concentrations rather than after the 10 ml/L dilution.
- The target imports Wolin's vitamin solution (10x) components at their full stock concentrations rather than after the 1 ml/L dilution.
- Duplicate cleanup merged chemically identical rows across the final medium and stock recipes: NaCl is `6.89655 + 1.0`, CaCl2.2H2O is `0.147783 + 0.1`, NiCl2.6H2O is `0.000985222 + 0.03`, and Na2WO4.2H2O is `0.0000985222 + 0.0004`.
- The generated merge uses the KOMODO owner as canonical; this drops the direct DSMZ owner's structured anaerobic preparation steps.

## Completeness

- The generated record is complete relative to the current KOMODO owner but incomplete relative to the direct DSMZ owner because DSMZ preparation steps are missing from the merge.
- Distilled water rows from the main recipe, the Modified Wolin mineral stock, and the Wolin vitamin stock are absent.
- The stock-solution additions are not structurally complete: the record does not say which rows came from Modified Wolin's mineral solution or Wolin's vitamin solution.

## Findings

- BLOCKER: reusable stock-solution components are modeled as top-level final-medium ingredients at stock strength. Modified Wolin minerals should be diluted from a 10 ml/L addition, and Wolin vitamins should be diluted from a 1 ml/L addition.
- BLOCKER: duplicate cleanup summed final-medium salts with stock-solution salts, corrupting final NaCl, CaCl2.2H2O, NiCl2.6H2O, and Na2WO4.2H2O concentrations.
- MAJOR: DSMZ preparation steps are lost from `data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml` even though the direct DSMZ owner contains the anoxic sparging, dispensing, filtration, and pH instructions.
- MAJOR: the canonical KOMODO record says `Aerobic: Yes`, contradicting DSMZ's explicitly anoxic preparation.
- MAJOR: `data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml` retains malformed curation history timestamp `2026-01-27T01:15:03.fZ`.
- MINOR: no distilled-water row is retained for the main medium or either stock solution.

## Recommended Edits

- Re-curate `data/normalized_yaml/bacterial/acetitomaculum_medium.yaml` and `data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml` from DSMZ Medium 540 with Modified Wolin's mineral solution and Wolin's vitamin solution represented as stocks or correctly diluted final components.
- Undo the cross-context duplicate sums for NaCl, CaCl2.2H2O, NiCl2.6H2O, and Na2WO4.2H2O.
- Carry the direct DSMZ anaerobic preparation steps into the canonical generated record.
- Remove or correct the KOMODO `Aerobic: Yes` assertion.
- Correct the KOMODO import timestamp to a parseable ISO 8601 timestamp.
- Regenerate `data/merge_yaml/merged/ACETITOMACULUM_MEDIUM.yaml` after normalized repair.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after normalized repair and merge regeneration.
- Re-fetch `DSMZ_Medium540.pdf` and verify that no stock-solution component appears at full stock strength in the final medium.
- Re-run an exact ignored-file-inclusive search for `komodo.medium:540`, `mediadive.medium:540`, and `DSMZ_Medium540` to confirm only the expected KOMODO/DSMZ source-duplicate pair remains.

## Additional Notes

- MediaDive appears to have divided the main-medium masses by the final volume after additions, which explains non-round values such as `0.197044` for KH2PO4. That normalization is defensible only if the nested stock additions are also diluted, which they currently are not.
