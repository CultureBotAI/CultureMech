# YAML Record Review: ACIDAMINOBACTER MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/ACIDAMINOBACTER_MEDIUM.yaml
- Started UTC: 2026-09-21T08:47:56Z
- Finished UTC: 2026-09-21T08:49:12Z
- Verdict: needs curation

## Target

- Reviewed generated record `data/merge_yaml/merged/ACIDAMINOBACTER_MEDIUM.yaml`.
- Stable identifier: `CultureMech:004754`.
- Source identity asserted by the canonical record: KOMODO ModelSEED `292`, copied from DSMZ Medium 292 / MediaDive `mediadive.medium:292`.
- The generated record was merged from `KOMODO_292_ACIDAMINOBACTER_medium` and `acidaminobacter_medium` on fingerprint `79c4f71d22828ed862c75490da8bfc03b2b28cc801a476a228f8c8210ca081f1`.
- Current authoritative source owners: `data/normalized_yaml/bacterial/KOMODO_292_ACIDAMINOBACTER_medium.yaml` and `data/normalized_yaml/bacterial/acidaminobacter_medium.yaml`.

## Validation

- PASS: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ACIDAMINOBACTER_MEDIUM.yaml`
- PASS: `scripts/validate_strict.py data/merge_yaml/merged/ACIDAMINOBACTER_MEDIUM.yaml`
- PASS: `linkml-reference-validator validate data data/merge_yaml/merged/ACIDAMINOBACTER_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- PASS: `linkml-term-validator validate-data data/merge_yaml/merged/ACIDAMINOBACTER_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
- Not checked: embedded `MediaRecipe.curation_history` entries; the documented history validator targets standalone files under `history/`.

## Identity and Grounding

- DSMZ Medium 292 resolves and identifies the source as `292: ACIDAMINOBACTER MEDIUM`.
- The KOMODO/DSMZ duplicate relationship is coherent: the KOMODO owner says it copied DSMZ Medium 292, and the direct DSMZ owner carries `mediadive.medium:292`.
- A bounded gitignore-independent exact search for `komodo.medium:292`, `mediadive.medium:292`, `DSMZ_Medium292.pdf`, `ACIDAMINOBACTER_MEDIUM`, and `acidaminobacter_medium` found the expected KOMODO owner, expected direct DSMZ owner, expected source-index rows, and the generated source-duplicate merge.
- The source is anaerobic: DSMZ instructs sparging with 100% N2, dispensing under the same gas into anoxic Hungate-type tubes or serum vials, and adding sterile anoxic stocks. The KOMODO duplicate nevertheless says `Aerobic: Yes`.

## Evidence

- DSMZ Medium 292 directly lists 1.50 g glycine, 3.00 g Na2SO4, 0.20 g KH2PO4, 0.40 g MgCl2.6H2O, 1.20 g NaCl, 0.15 g CaCl2.2H2O, 0.40 g KCl, 0.20 g yeast extract, 0.50 ml sodium resazurin 0.1% w/v, 2.00 g NaHCO3, 0.30 g Na2S.9H2O, and 1000.00 ml distilled water.
- The generated record correctly rescales direct main-medium additions to the assembled volume: for example glycine is `1.49551 G_PER_L`, Na2SO4 is `2.99103 G_PER_L`, and NaHCO3 is `1.99402 G_PER_L`.
- DSMZ adds Trace element solution SL-10 at `1.00 ml/L`; the generated record instead flattens HCl, FeCl2.4H2O, ZnCl2, MnCl2.4H2O, H3BO3, CoCl2.6H2O, CuCl2.2H2O, NiCl2.6H2O, and Na2MoO4.2H2O at stock strength.
- DSMZ adds Selenite-tungstate solution at `1.00 ml/L`; the generated record instead flattens NaOH, Na2SeO3.5H2O, and Na2WO4.2H2O at stock strength.
- DSMZ adds Wolin's vitamin solution `(10x)` at `1.00 ml/L`; the generated record instead flattens biotin, folic acid, pyridoxine hydrochloride, thiamine HCl, riboflavin, nicotinic acid, calcium pantothenate, vitamin B12, p-aminobenzoic acid, and alpha-lipoic acid at 10x stock strength.
- The direct DSMZ owner preserves anoxic preparation and stock-addition text; the canonical generated record is KOMODO-derived and drops preparation steps.

## Completeness

- The generated record is incomplete because SL-10, selenite-tungstate solution, and Wolin's 10x vitamin solution are represented only as flattened top-level ingredients.
- DSMZ distilled-water rows are absent from the main medium and all three stock recipes.
- The generated canonical record lacks the direct DSMZ anaerobic preparation instructions.

## Findings

- BLOCKER: the generated record flattens the 1 ml/L SL-10 trace-element stock at stock strength.
- BLOCKER: the generated record flattens the 1 ml/L selenite-tungstate stock at stock strength.
- BLOCKER: the generated record flattens the 1 ml/L Wolin's vitamin solution `(10x)` at stock strength.
- MAJOR: the generated record uses the KOMODO owner as canonical and drops the direct DSMZ anaerobic preparation steps.
- MAJOR: the canonical KOMODO owner says `Aerobic: Yes`, contradicting the DSMZ anaerobic recipe it copied.
- MAJOR: `data/normalized_yaml/bacterial/KOMODO_292_ACIDAMINOBACTER_medium.yaml` retains malformed curation history timestamp `2026-01-27T01:15:02.fZ`.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/acidaminobacter_medium.yaml` and `data/normalized_yaml/bacterial/KOMODO_292_ACIDAMINOBACTER_medium.yaml` to encode the 1 ml/L SL-10 stock, 1 ml/L selenite-tungstate stock, and 1 ml/L Wolin 10x vitamin stock instead of flattening their components into the final medium.
- Preserve the DSMZ N2 sparging, anoxic dispensing, sterile-stock addition, and stock-preparation instructions in the canonical generated record.
- Remove or correct the KOMODO `Aerobic: Yes` assertion and malformed timestamp.
- Regenerate `data/merge_yaml/merged/ACIDAMINOBACTER_MEDIUM.yaml` after normalized repair.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after normalized repair and merge regeneration.
- Re-fetch `DSMZ_Medium292.pdf` and verify that every SL-10, selenite-tungstate, and Wolin 10x vitamin component is either inside its correct stock recipe or diluted by the 1 ml/L addition volume.
- Re-run ignored-file-inclusive exact searches for `komodo.medium:292`, `mediadive.medium:292`, and `ACIDAMINOBACTER_MEDIUM` to confirm only the expected KOMODO/DSMZ source-duplicate pair remains active.

## Additional Notes

- Optional empty fields were not treated as defects.
