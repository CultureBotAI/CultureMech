# YAML Record Review: ACETOBACTERIUM MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/ACETOBACTERIUM_MEDIUM.yaml
- Started UTC: 2026-09-21T08:31:24Z
- Finished UTC: 2026-09-21T08:33:04Z
- Verdict: needs curation

## Target

- Reviewed generated record `data/merge_yaml/merged/ACETOBACTERIUM_MEDIUM.yaml`.
- Stable identifier: `CultureMech:003084`.
- Source identity asserted by the canonical record: JCM Medium J741 / MediaDive `mediadive.medium:J741`.
- The generated record was merged from one source owner, `JCM_J741_ACETOBACTERIUM_MEDIUM`, on fingerprint `50ec0c4aef854b406856b23792c9721941c2859c62ca6d4d42990263f05eaebd`.
- Current authoritative owner: `data/normalized_yaml/bacterial/JCM_J741_ACETOBACTERIUM_MEDIUM.yaml`.

## Validation

- PASS: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ACETOBACTERIUM_MEDIUM.yaml`
- PASS: `scripts/validate_strict.py data/merge_yaml/merged/ACETOBACTERIUM_MEDIUM.yaml`
- PASS: `linkml-reference-validator validate data data/merge_yaml/merged/ACETOBACTERIUM_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- PASS: `linkml-term-validator validate-data data/merge_yaml/merged/ACETOBACTERIUM_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
- Not checked: embedded `MediaRecipe.curation_history` entries; the documented history validator targets standalone files under `history/`.

## Identity and Grounding

- JCM GRMD `741` resolves and identifies the source as `741 ACETOBACTERIUM MEDIUM`.
- TOGO Medium `M766` is a copy of the same JCM source: its metadata names original media `JCM_M741`, links to the same `GRMD=741` page, and carries the same JCM preparation comments.
- A gitignore-independent exact search for `mediadive.medium:J741`, `GRMD=741`, `JCM_J741_ACETOBACTERIUM_MEDIUM`, and `JCM_M741` found the expected direct JCM owner, expected TOGO owner, their two generated merges, expected index rows, the generated JCM merge, and historical reports.
- Multiple other records share the generic `acetobacterium_medium` name or derive from DSMZ Medium 135 and DSMZ Medium 135a, but those records carry different source IDs and should not be merged with JCM 741 by name alone.

## Evidence

- JCM Medium 741 is built from 1 L distilled water, 20 ml Trace element solution, 20 ml Trace vitamins from JCM 197, direct salts, 2 g yeast extract, 10 g fructose, 1 mg resazurin, 10 g NaHCO3, 0.5 g cysteine, and 0.5 g Na2S.9H2O.
- The generated direct JCM record correctly rescales the direct main-medium rows to the documented 1040 ml working volume: for example NH4Cl is `0.961538 G_PER_L`, fructose and NaHCO3 are both `9.61539 G_PER_L`, and resazurin is `0.000961538 G_PER_L`.
- The generated direct JCM record flattens Trace element solution components at stock strength instead of diluting them from the 20 ml/L addition. Nitrilotriacetic acid is `1.5 G_PER_L`, MnSO4.xH2O is `0.5 G_PER_L`, NaCl is `1 G_PER_L`, FeSO4.7H2O is `0.1 G_PER_L`, NiCl2.6H2O is `0.025 G_PER_L`, and the trace selenium salt is likewise imported as a stock row.
- The direct MgSO4.7H2O row and the Trace element solution MgSO4.7H2O row were duplicate-merged as `3.0961538 G_PER_L`; the correct representation would either keep the two contexts separate or add a roughly `0.0577 G_PER_L` stock contribution to the direct `0.0961538 G_PER_L`.
- Trace vitamins from JCM 197 are flattened at stock strength even though JCM 741 adds 20 ml/L of the vitamin stock.
- The source says to adjust the finished medium to pH 8.2 with a sterile anaerobic 5% Na2CO3 stock, while the generated record instead has scalar `ph_value: 7.0` from the trace element solution pH and has no Na2CO3 ingredient or stock addition.

## Completeness

- The generated merge is incomplete because the TOGO `M766` source duplicate is not reconciled with the direct JCM owner.
- The generated target retains JCM's anaerobic main preparation text and trace element preparation text, but the trace element pH step is incorrectly promoted to the recipe-level pH.
- Distilled water rows are absent from the main medium and trace element stock in the direct JCM owner.
- The stock hierarchy is absent, so reviewers cannot tell which rows belong to the final medium, Trace element solution, or Trace vitamins.

## Findings

- BLOCKER: Trace element solution is flattened at stock strength instead of being represented as a 20 ml/L stock addition or correctly diluted final concentrations.
- BLOCKER: duplicate cleanup summed MgSO4.7H2O from the direct medium and Trace element solution, producing `3.0961538 G_PER_L`.
- BLOCKER: Trace vitamins are flattened at stock strength even though JCM adds 20 ml/L of the JCM 197 vitamin stock.
- BLOCKER: the recipe-level pH is imported from the trace element stock's pH 7.0; the final medium is adjusted before use to pH 8.2 with 5% Na2CO3.
- MAJOR: the sterile 5% Na2CO3 stock addition is described in prose but absent from the ingredient or solution structure.
- MAJOR: the direct JCM and TOGO duplicate records are not merged, leaving `data/merge_yaml/merged/ACETOBACTERIUM_MEDIUM.yaml` and `data/merge_yaml/merged/acetobacterium_medium__0a1ffb5c.yaml` as duplicate generated records for JCM GRMD 741.

## Recommended Edits

- Re-curate `data/normalized_yaml/bacterial/JCM_J741_ACETOBACTERIUM_MEDIUM.yaml` from JCM Medium 741 with Trace element solution and Trace vitamins represented as named stocks or correctly diluted final components.
- Remove the duplicate-merged MgSO4.7H2O artifact and keep direct-medium MgSO4.7H2O distinct from Trace element solution MgSO4.7H2O unless both are explicitly diluted to final mass.
- Move the pH 7.0 KOH adjustment into the Trace element solution context and represent the final pH 8.2 Na2CO3 adjustment as a sterile 5% stock addition.
- Mark `data/normalized_yaml/bacterial/TOGO_M766_Acetobacterium_Medium.yaml` as a duplicate of the direct JCM owner after the same stock-addition semantics are preserved.
- Regenerate `data/merge_yaml/merged/ACETOBACTERIUM_MEDIUM.yaml` after normalized repair.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after normalized repair and merge regeneration.
- Re-fetch JCM GRMD `741` and TOGO `M766`, verify the JCM and TOGO source formulas agree, and confirm every 20 ml stock addition is either represented as a stock volume or diluted into the final medium by that volume.
- Re-run an exact ignored-file-inclusive search for `mediadive.medium:J741`, `TOGO:M766`, `JCM_M741`, and `GRMD=741` to confirm the direct JCM and TOGO copies merge into one generated record while the DSMZ 135 and 135a Acetobacterium recipes remain separate.

## Additional Notes

- `data/normalized_yaml/bacterial/TOGO_M766_Acetobacterium_Medium.yaml` also preserves the incorrect source-level `ph: 7.0`, so duplicate reconciliation needs an explicit source review rather than a blind owner merge.
