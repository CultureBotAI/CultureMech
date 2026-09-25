# YAML Record Review: Acetobacterium Submarinus Medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/ACETOBACTERIUM_SUBMARINUS_MEDIUM.yaml
- Started UTC: 2026-09-21T08:33:05Z
- Finished UTC: 2026-09-21T08:34:39Z
- Verdict: needs curation

## Target

- Reviewed generated record `data/merge_yaml/merged/ACETOBACTERIUM_SUBMARINUS_MEDIUM.yaml`.
- Stable identifier: `CultureMech:009785`.
- Source identity asserted by the canonical record: TOGO Medium `M401`, copied from JCM Medium 403.
- The generated record was merged from one source owner, `TOGO_M401_Acetobacterium_Submarinus_Medium`, on fingerprint `56917c62032115e668b406df8d7ae3bbdcc91e690a954dc0b00ae934cfdf0f3f`.
- Current authoritative owner: `data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml`.

## Validation

- PASS: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ACETOBACTERIUM_SUBMARINUS_MEDIUM.yaml`
- PASS: `scripts/validate_strict.py data/merge_yaml/merged/ACETOBACTERIUM_SUBMARINUS_MEDIUM.yaml`
- PASS: `linkml-reference-validator validate data data/merge_yaml/merged/ACETOBACTERIUM_SUBMARINUS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- PASS: `linkml-term-validator validate-data data/merge_yaml/merged/ACETOBACTERIUM_SUBMARINUS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
- Not checked: embedded `MediaRecipe.curation_history` entries; the documented history validator targets standalone files under `history/`.

## Identity and Grounding

- JCM GRMD `403` resolves and identifies the source as `403 ACETOBACTERIUM SUBMARINUS MEDIUM`.
- TOGO Medium `M401` is a copy of the same JCM source: its metadata names original media `JCM_M403`, links to the same `GRMD=403` page, and carries the same JCM preparation comment.
- A gitignore-independent exact search for `TOGO:M401`, `mediadive.medium:J403`, `GRMD=403`, `JCM_J403_ACETOBACTERIUM_SUBMARINUS_MEDIUM`, and `JCM_M403` found the expected direct JCM owner, expected TOGO owner, their two generated merges, expected index rows, historical reports, and additional repaired records that cite JCM 403 as supporting cross-media evidence.

## Evidence

- JCM Medium 403 is built from 1 L distilled water, 30 g sea salts, 0.1 g yeast extract, 1 ml trace element solution from JCM 301, 1 ml vitamin solution, 1 ml thiamine solution, 1 ml vitamin B12 solution, 30 mg Na2WO4.2H2O, 0.5 mg Na2SeO4, direct acetate, methylamine, formate, methanol, KH2PO4, NH4Cl, resazurin, NaHCO3, and Na2S.9H2O.
- The generated TOGO record imports milligram source rows as grams: 30 mg Na2WO4.2H2O is `30 G_PER_L`, 0.5 mg Na2SeO4 is `0.5 G_PER_L`, and 0.5 mg resazurin is `0.5 G_PER_L`.
- The generated TOGO record imports the vitamin, thiamine, and vitamin B12 stock compositions at stock strength: for example 4 mg p-aminobenzoic acid in 100 ml stock becomes `4 G_PER_L`, 10 mg pyridoxine in 100 ml stock becomes `10 G_PER_L`, and 5 mg vitamin B12 in 100 ml stock becomes `5 G_PER_L`.
- The generated TOGO record stores all four 1 ml stock additions as solution rows with `1 G_PER_L`, so Trace element solution, Vitamin solution, Thiamine solution, and Vitamin B12 solution are not represented as volumes or as correctly diluted final concentrations.
- The generated TOGO record sums the 1 L main-medium water with 100 ml from the vitamin B12 stock as `101 G_PER_L`, losing both solvent context and volume units.
- The direct JCM / MediaDive owner imports the main rows more plausibly but still expands trace elements from JCM 301 and the vitamin stocks at stock strength, and it is not reconciled with the TOGO M401 copy.

## Completeness

- The generated target preserves JCM's anaerobic preparation text, including H2-CO2 pressurization, separate sterilization of 5% Na2S.9H2O, filtration of 8% NaHCO3, and final pH 7.0 adjustment.
- The generated merge is incomplete because the direct JCM `mediadive.medium:J403` source duplicate is not reconciled with TOGO `M401`.
- The trace element solution composition is not inlined in the TOGO target; it is preserved only as a cross-reference to TOGO `M296`.
- The stock hierarchy is absent, so reviewers cannot distinguish the final medium from Vitamin solution, Thiamine solution, Vitamin B12 solution, or Trace element solution.

## Findings

- BLOCKER: milligram rows from JCM 403 are imported as grams per liter in the generated TOGO record, creating 1000x errors for tungstate, selenate, resazurin, and vitamin rows.
- BLOCKER: Vitamin solution, Thiamine solution, and Vitamin B12 solution are flattened at stock strength instead of being represented as 1 ml/L stock additions or correctly diluted final concentrations.
- BLOCKER: all four 1 ml stock-addition volumes are represented as `1 G_PER_L` solution concentrations.
- BLOCKER: water from distinct final-medium and stock contexts is merged into a nonsensical `101 G_PER_L` ingredient.
- MAJOR: the direct JCM and TOGO duplicate records are not merged, leaving `data/merge_yaml/merged/ACETOBACTERIUM_SUBMARINUS_MEDIUM.yaml` and `data/merge_yaml/merged/acetobacterium_submarinus_medium__9fed26ec.yaml` as duplicate generated records for JCM GRMD 403.

## Recommended Edits

- Re-curate `data/normalized_yaml/bacterial/TOGO_M401_Acetobacterium_Submarinus_Medium.yaml` from JCM Medium 403 with Trace element solution, Vitamin solution, Thiamine solution, and Vitamin B12 solution represented as named stocks or correctly diluted final components.
- Apply the same stock-dilution semantics to `data/normalized_yaml/bacterial/acetobacterium_submarinus_medium.yaml`.
- Preserve milligram units for JCM's tungstate, selenate, resazurin, and vitamin rows when calculating final per-liter concentrations.
- Keep stock solvent water inside its stock context; do not merge it with the final-medium 1 L distilled water row.
- Regenerate `data/merge_yaml/merged/ACETOBACTERIUM_SUBMARINUS_MEDIUM.yaml` after normalized repair and duplicate reconciliation.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after normalized repair and merge regeneration.
- Re-fetch JCM GRMD `403` and TOGO `M401`, verify the JCM and TOGO source formulas agree, and confirm every 1 ml stock addition is either represented as a stock volume or diluted into the final medium by that volume.
- Re-run an exact ignored-file-inclusive search for `TOGO:M401`, `mediadive.medium:J403`, `JCM_M403`, and `GRMD=403` to confirm the direct JCM and TOGO copies merge into one generated record.

## Additional Notes

- The `high_metal: true` flag is justified for the current target but cannot by itself distinguish the real tungstate/selenate source amounts from the TOGO milligram-to-gram unit slips.
