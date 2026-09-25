# YAML Record Review: ACETOBACTEROIDES GLYCINOPHILUS MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/ACETOBACTEROIDES_GLYCINOPHILUS_MEDIUM.yaml
- Started UTC: 2026-09-21T08:36:03Z
- Finished UTC: 2026-09-21T08:38:22Z
- Verdict: needs curation

## Target

- Reviewed generated record `data/merge_yaml/merged/ACETOBACTEROIDES_GLYCINOPHILUS_MEDIUM.yaml`.
- Stable identifier: `CultureMech:005025`.
- Source identity asserted by the canonical record: KOMODO ModelSEED `331`, copied from DSMZ Medium 331 / MediaDive `mediadive.medium:331`.
- The generated record is merged from only `KOMODO_331_ACETOBACTEROIDES_GLYCINOPHILUS_medium` on fingerprint `2ae9549b82511687b25cf895ad0d6d6b3875b882338627469f9f5abdf54e2bbf`.
- Current authoritative source owners: `data/normalized_yaml/bacterial/KOMODO_331_ACETOBACTEROIDES_GLYCINOPHILUS_medium.yaml` and `data/normalized_yaml/bacterial/acetobacteroides_glycinophilus_medium.yaml`.

## Validation

- PASS: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ACETOBACTEROIDES_GLYCINOPHILUS_MEDIUM.yaml`
- PASS: `scripts/validate_strict.py data/merge_yaml/merged/ACETOBACTEROIDES_GLYCINOPHILUS_MEDIUM.yaml`
- PASS: `linkml-reference-validator validate data data/merge_yaml/merged/ACETOBACTEROIDES_GLYCINOPHILUS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- PASS: `linkml-term-validator validate-data data/merge_yaml/merged/ACETOBACTEROIDES_GLYCINOPHILUS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
- Not checked: embedded `MediaRecipe.curation_history` entries; the documented history validator targets standalone files under `history/`.

## Identity and Grounding

- DSMZ Medium 331 resolves and identifies the source as `331: ACETOBACTEROIDES GLYCINOPHILUS MEDIUM`.
- The KOMODO/DSMZ duplicate relationship is coherent: the KOMODO owner says it copied DSMZ Medium 331, and the direct DSMZ owner carries `mediadive.medium:331`.
- A bounded gitignore-independent exact search for `komodo.medium:331`, `mediadive.medium:331`, `ACETOBACTEROIDES_GLYCINOPHILUS_MEDIUM`, `acetobacteroides_glycinophilus_medium`, and `KOMODO_331_ACETOBACTEROIDES_GLYCINOPHILUS_medium` found the expected normalized owners, the expected source-index rows, the current KOMODO generated record, and the split direct-DSMZ generated record `data/merge_yaml/merged/acetobacteroides_glycinophilus_medium__7fb06851.yaml`.
- The source is anaerobic: DSMZ instructs preparing the medium anaerobically under 100% nitrogen and sterilizing several concentrated solutions under nitrogen, but the KOMODO duplicate says `Aerobic: Yes`.

## Evidence

- DSMZ Medium 331 directly lists 0.13 g CaCl2.2H2O, 1.00 g NH4Cl, 0.20 g MgCl2.6H2O, 1.00 mg resazurin, 0.50 g yeast extract, 1.50 g glycine, 3.00 g KH2PO4, 5.80 g Na2HPO4, 0.50 g NaHCO3, and 0.50 g Na2S.9H2O with 1000.00 ml distilled water.
- DSMZ adds Trace elements from DSMZ Medium 144 at `10.00 ml/L`; the generated record instead flattens the trace stock's NTA, FeCl2.4H2O, MnCl2.4H2O, CoCl2.6H2O, ZnCl2, CuCl2, H3BO3, Na2MoO4.2H2O, NiCl2.6H2O, NaCl, and Na2SeO3.5H2O at stock strength.
- DSMZ adds Vitamin solution from DSMZ Medium 141 at `5.00 ml/L`; the generated record instead flattens biotin, folic acid, pyridoxine hydrochloride, thiamine HCl, riboflavin, nicotinic acid, calcium pantothenate, vitamin B12, p-aminobenzoic acid, and alpha-lipoic acid at stock strength.
- The generated CaCl2.2H2O row is inflated to `0.23 G_PER_L` because cleanup merged the main-medium 0.13 g/L row with the trace-stock 0.10 g/L row rather than preserving the 10 ml/L stock addition.
- Both normalized owners have the same stock-flattened ingredient list and the same inflated CaCl2.2H2O sum, so the generated KOMODO record carries forward an upstream normalized defect.
- The direct DSMZ owner preserves source preparation text for pH adjustment, anaerobic 100% nitrogen handling, separate concentrated solutions, and Medium 144 trace-stock assembly; the canonical generated record is KOMODO-only and drops those preparation steps.

## Completeness

- The direct DSMZ duplicate generated as `data/merge_yaml/merged/acetobacteroides_glycinophilus_medium__7fb06851.yaml` remains split from the KOMODO-derived generated record.
- Trace elements and vitamin solution are represented only as top-level ingredients, not as DSMZ Medium 144 and DSMZ Medium 141 stock-solution additions.
- DSMZ distilled water is absent.
- The direct DSMZ preparation instructions are absent from the canonical KOMODO generated record.

## Findings

- BLOCKER: the record flattens the 10 ml/L DSMZ Medium 144 trace-element stock at stock strength.
- BLOCKER: the record flattens the 5 ml/L DSMZ Medium 141 vitamin stock at stock strength.
- MAJOR: CaCl2.2H2O was summed as `0.13 + 0.10 = 0.23 G_PER_L`, but the 0.10 g/L component belongs inside the 10 ml/L trace stock and is only a trace-level final addition.
- MAJOR: direct DSMZ Medium 331 and KOMODO Medium 331 are source duplicates but generate two separate `data/merge_yaml/merged` records.
- MAJOR: the generated record uses the KOMODO owner as canonical and drops the direct DSMZ anaerobic preparation steps.
- MAJOR: the canonical KOMODO owner says `Aerobic: Yes`, contradicting the DSMZ anaerobic recipe it copied.
- MAJOR: `data/normalized_yaml/bacterial/KOMODO_331_ACETOBACTEROIDES_GLYCINOPHILUS_medium.yaml` retains malformed curation history timestamp `2026-01-27T01:15:02.fZ`.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/acetobacteroides_glycinophilus_medium.yaml` to encode the 10 ml/L DSMZ Medium 144 trace-element stock and 5 ml/L DSMZ Medium 141 vitamin stock instead of flattening those stock recipes.
- Apply the same stock nesting repair to `data/normalized_yaml/bacterial/KOMODO_331_ACETOBACTEROIDES_GLYCINOPHILUS_medium.yaml`.
- Preserve the DSMZ pH adjustment, anaerobic handling, concentrated-stock sterilization, and trace-element-stock assembly preparation text in the canonical generated record.
- Remove or correct the KOMODO `Aerobic: Yes` note and malformed timestamp.
- Regenerate merged records so DSMZ Medium 331 and KOMODO Medium 331 collapse into one source-duplicate merge.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after normalized repair and merge regeneration.
- Re-fetch `DSMZ_Medium331.pdf` and verify that every Medium 144 and Medium 141 stock ingredient is nested in its stock recipe or diluted by the correct addition volume.
- Re-run ignored-file-inclusive exact searches for `komodo.medium:331`, `mediadive.medium:331`, and `ACETOBACTEROIDES_GLYCINOPHILUS_MEDIUM` to confirm only the expected KOMODO/DSMZ source-duplicate pair remains active.

## Additional Notes

- Optional empty fields were not treated as defects.
