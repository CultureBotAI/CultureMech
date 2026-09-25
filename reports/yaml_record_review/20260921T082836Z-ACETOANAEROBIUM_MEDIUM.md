# YAML Record Review: ACETOANAEROBIUM MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/ACETOANAEROBIUM_MEDIUM.yaml
- Started UTC: 2026-09-21T08:26:20Z
- Finished UTC: 2026-09-21T08:28:36Z
- Verdict: pass

## Target

- Reviewed generated record `data/merge_yaml/merged/ACETOANAEROBIUM_MEDIUM.yaml`.
- Stable identifier: `CultureMech:001496`.
- Source identity asserted by the canonical record: DSMZ Medium 38 / MediaDive `mediadive.medium:38`.
- The generated record was merged from two source owners, `acetoanaerobium_medium` and `clostridium_sticklandii_medium`, on fingerprint `880b4702c1fc0acfee955623e14eef7e6dfb16d0df5345c766883e9bca727934`.
- Current authoritative owners: `data/normalized_yaml/bacterial/acetoanaerobium_medium.yaml` and `data/normalized_yaml/bacterial/clostridium_sticklandii_medium.yaml`.

## Validation

- PASS: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ACETOANAEROBIUM_MEDIUM.yaml`
- PASS: `scripts/validate_strict.py data/merge_yaml/merged/ACETOANAEROBIUM_MEDIUM.yaml`
- PASS: `linkml-reference-validator validate data data/merge_yaml/merged/ACETOANAEROBIUM_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- PASS: `linkml-term-validator validate-data data/merge_yaml/merged/ACETOANAEROBIUM_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
- Not checked: embedded `MediaRecipe.curation_history` entries; the documented history validator targets standalone files under `history/`.

## Identity and Grounding

- DSMZ Medium 38 resolves and identifies the source as `38: ACETOANAEROBIUM MEDIUM`.
- The KOMODO child source is coherent: it cites KOMODO ModelSEED `38`, declares `DSMZ Medium: 38 (mediadive.medium:38)`, says `Aerobic: No`, and has the same ingredient/concentration signature as the direct DSMZ owner.
- A gitignore-independent exact search for `mediadive.medium:38`, `komodo.medium:38`, `DSMZ_Medium38.pdf`, `DSMZ_38_ACETOANAEROBIUM_MEDIUM`, `acetoanaerobium_medium`, and `clostridium_sticklandii_medium` found the expected direct DSMZ owner, KOMODO duplicate owner, generated merge, current source indexes, and historical validation reports.

## Evidence

- DSMZ Medium 38 lists 20 g tryptone, 10 g yeast extract, 1.04 g K2HPO4, 0.68 g KH2PO4, 0.50 ml sodium resazurin 0.1% w/v, 0.15 g Na2S.9H2O, and 1000 ml distilled water.
- The generated target represents the source solutes at the correct final concentrations, including `0.0005 G_PER_L` sodium resazurin calculated from 0.50 ml of a 0.1% w/v stock.
- DSMZ instructs adjusting to pH 7.0, boiling, cooling under 100% N2, dispensing under the same gas atmosphere, autoclaving, and adding sulfide from a sterile anoxic N2 stock after sterilization.
- The generated target preserves the pH and anaerobic preparation text from the direct DSMZ owner.

## Completeness

- The generated target omits the explicit distilled-water source row, matching the usual direct MediaDive/DSMZ solvent omission pattern.
- The generated target preserves the DSMZ/KOMODO duplicate relationship as a `SOURCE_DUPLICATE` variant child.
- The DSMZ URL is present in `notes`, but there is no structured `references` entry.

## Findings

- MINOR: distilled water is omitted as an explicit ingredient row.
- MINOR: source provenance is note-only; the linked DSMZ URL should be promoted to a structured reference or source slot.
- MINOR: `data/normalized_yaml/bacterial/clostridium_sticklandii_medium.yaml` retains malformed curation history timestamp `2026-01-27T01:15:02.fZ`.

## Recommended Edits

- Add a structured source or reference for DSMZ Medium 38.
- If direct DSMZ imports standardize solvent rows in the future, add distilled water 1000 ml to this recipe at the same time.
- Correct the malformed timestamp in `data/normalized_yaml/bacterial/clostridium_sticklandii_medium.yaml`.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after any provenance or timestamp edit.
- Re-fetch `DSMZ_Medium38.pdf` and confirm the six retained solutes, pH 7.0, and anaerobic sulfide-addition instructions remain unchanged.
- Re-run an exact ignored-file-inclusive search for `mediadive.medium:38`, `komodo.medium:38`, `acetoanaerobium_medium`, and `clostridium_sticklandii_medium` to confirm the DSMZ/KOMODO pair remains uniquely represented.

## Additional Notes

- No blocker or major finding was identified.
