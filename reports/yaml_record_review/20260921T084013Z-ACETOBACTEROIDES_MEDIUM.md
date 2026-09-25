# YAML Record Review: ACETOBACTEROIDES MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/ACETOBACTEROIDES_MEDIUM.yaml
- Started UTC: 2026-09-21T08:38:23Z
- Finished UTC: 2026-09-21T08:40:13Z
- Verdict: needs curation

## Target

- Reviewed generated record `data/merge_yaml/merged/ACETOBACTEROIDES_MEDIUM.yaml`.
- Stable identifier: `CultureMech:001130`.
- Source identity asserted by the record: DSMZ Medium 1647 / MediaDive `mediadive.medium:1647`.
- The generated record is merged from only `acetobacteroides_medium` on fingerprint `b1a42f76e65b9365eb88eee37fc3c241310fdd6d04e86a88e79dbe62fd072f9e`.
- Current authoritative source owner: `data/normalized_yaml/bacterial/acetobacteroides_medium.yaml`.

## Validation

- PASS: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ACETOBACTEROIDES_MEDIUM.yaml`
- PASS: `scripts/validate_strict.py data/merge_yaml/merged/ACETOBACTEROIDES_MEDIUM.yaml`
- PASS: `linkml-reference-validator validate data data/merge_yaml/merged/ACETOBACTEROIDES_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- PASS: `linkml-term-validator validate-data data/merge_yaml/merged/ACETOBACTEROIDES_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
- Not checked: embedded `MediaRecipe.curation_history` entries; the documented history validator targets standalone files under `history/`.

## Identity and Grounding

- DSMZ Medium 1647 resolves and identifies the source as `1647: ACETOBACTEROIDES MEDIUM`.
- A bounded gitignore-independent exact search for `mediadive.medium:1647`, `DSMZ_Medium1647.pdf`, `ACETOBACTEROIDES_MEDIUM`, and `acetobacteroides_medium` found the expected direct DSMZ normalized owner, source-index rows, and generated merge.
- No KOMODO or JCM duplicate was visible in the reviewed active `data/normalized_yaml` and `data/merge_yaml/merged` paths.

## Evidence

- DSMZ Medium 1647 directly lists 0.20 g yeast extract, 0.18 g glucose, 0.14 g KH2PO4, 0.20 g MgCl2.6H2O, 0.15 g CaCl2.2H2O, 0.54 ml NH4Cl, 0.30 g cysteine-HCl.H2O, 2.50 g NaHCO3, 0.30 g Na2S.9H2O, and 1.00 mg resazurin with 1000.00 ml distilled water.
- DSMZ adds its modified Trace element solution at `1.00 ml/L`; the generated record instead flattens the stock's NTA, FeCl2.4H2O, MnCl2.4H2O, CoCl2.6H2O, CaCl2.2H2O, ZnCl2, CuCl2, H3BO3, Na2MoO4.2H2O, and NiCl2.6H2O at stock strength.
- DSMZ adds Se/W solution at `1.00 ml/L`; the generated record instead represents the stock's 4 mg/L Na2SeO3 and 4 mg/L Na2WO4 rows as final `0.004 G_PER_L` additions.
- DSMZ adds Vitamin solution at `1.00 ml/L`; the generated record instead flattens biotin, folic acid, pyridoxine-HCl, thiamine-HCl.2H2O, riboflavin, nicotinic acid, D-Ca-pantothenate, vitamin B12, p-aminobenzoic acid, and lipoic acid at stock strength.
- The generated CaCl2.2H2O row is inflated to `0.25 G_PER_L` because cleanup merged the main-medium 0.15 g/L row with the trace-stock 0.10 g/L row rather than preserving the 1 ml/L trace-stock context.
- The preparation text correctly states that the vitamin solution, trace element solution, Se/W solution, cysteine, glucose, Na2S, and NaHCO3 are added after autoclaving, but the generated ingredient list does not preserve the three solution contexts named by that step.

## Completeness

- The record is incomplete as a recipe hierarchy because it lacks nested recipes for the modified trace-element solution, Se/W solution, and vitamin solution.
- DSMZ distilled-water rows are absent from the main medium and all three stock solutions.
- The preparation steps for DSMZ Medium 141 and DSMZ Medium 318 are referenced only as free text; their chemistry has been flattened into the final ingredient list.

## Findings

- BLOCKER: the record flattens the 1 ml/L modified trace-element stock at stock strength.
- BLOCKER: the record flattens the 1 ml/L vitamin stock at stock strength.
- BLOCKER: the record flattens the 1 ml/L Se/W stock at stock strength, causing Na2SeO3 and Na2WO4 to be represented as `0.004 G_PER_L` final concentrations.
- MAJOR: CaCl2.2H2O was summed as `0.15 + 0.10 = 0.25 G_PER_L`, but the 0.10 g/L component belongs inside the 1 ml/L trace stock.
- MINOR: distilled water is absent from the main recipe and the embedded stock recipes.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/acetobacteroides_medium.yaml` to encode the 1 ml/L modified trace-element stock, 1 ml/L Se/W stock, and 1 ml/L vitamin stock instead of flattening their components into the final medium.
- Keep the direct main-medium CaCl2.2H2O row separate from the trace-stock CaCl2.2H2O row.
- Preserve the DSMZ Medium 141 and DSMZ Medium 318 preparation references on the corresponding stock recipes rather than attaching all stock-preparation text to the final recipe.
- Add distilled water rows for the main medium and each stock if water representation is in scope for the stock-nesting repair.
- Regenerate `data/merge_yaml/merged/ACETOBACTEROIDES_MEDIUM.yaml` after normalized repair.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after normalized repair and merge regeneration.
- Re-fetch `DSMZ_Medium1647.pdf` and verify that all modified-trace, Se/W, and vitamin stock ingredients are either nested in their stock recipes or diluted by the correct 1 ml/L addition volume.
- Re-run ignored-file-inclusive exact searches for `mediadive.medium:1647`, `DSMZ_Medium1647.pdf`, and `ACETOBACTEROIDES_MEDIUM` to confirm the repaired DSMZ owner is still a singleton.

## Additional Notes

- Optional empty fields were not treated as defects.
