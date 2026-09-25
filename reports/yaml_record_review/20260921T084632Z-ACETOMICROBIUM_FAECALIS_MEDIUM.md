# YAML Record Review: ACETOMICROBIUM FAECALIS MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/ACETOMICROBIUM_FAECALIS_MEDIUM.yaml
- Started UTC: 2026-09-21T08:44:43Z
- Finished UTC: 2026-09-21T08:46:32Z
- Verdict: needs curation

## Target

- Reviewed generated record `data/merge_yaml/merged/ACETOMICROBIUM_FAECALIS_MEDIUM.yaml`.
- Stable identifier: `CultureMech:005236`.
- Source identity asserted by the canonical record: KOMODO ModelSEED `412`, copied from DSMZ Medium 412 / MediaDive `mediadive.medium:412`.
- The generated record was merged from `KOMODO_412_ACETOMICROBIUM_FAECALIS_medium`, `acetomicrobium_faecalis_medium`, `medium_412_modified_for_dsm_18806`, and `medium_412_modified_for_dsm_23131` on fingerprint `b4bb5ec6456b2d374799593c9f0ed38351068a016b4ad0a6e824eca37ae8cb44`.
- Current authoritative source owners: `data/normalized_yaml/bacterial/KOMODO_412_ACETOMICROBIUM_FAECALIS_medium.yaml`, `data/normalized_yaml/bacterial/acetomicrobium_faecalis_medium.yaml`, `data/normalized_yaml/bacterial/medium_412_modified_for_dsm_18806.yaml`, and `data/normalized_yaml/bacterial/medium_412_modified_for_dsm_23131.yaml`.

## Validation

- PASS: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ACETOMICROBIUM_FAECALIS_MEDIUM.yaml`
- PASS: `scripts/validate_strict.py data/merge_yaml/merged/ACETOMICROBIUM_FAECALIS_MEDIUM.yaml`
- PASS: `linkml-reference-validator validate data data/merge_yaml/merged/ACETOMICROBIUM_FAECALIS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- PASS: `linkml-term-validator validate-data data/merge_yaml/merged/ACETOMICROBIUM_FAECALIS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
- Not checked: embedded `MediaRecipe.curation_history` entries; the documented history validator targets standalone files under `history/`.

## Identity and Grounding

- DSMZ Medium 412 resolves and identifies the source as `412: ACETOMICROBIUM FAECALIS MEDIUM`.
- The base KOMODO/DSMZ duplicate relationship is coherent: the KOMODO owner says it copied DSMZ Medium 412, and the direct DSMZ owner carries `mediadive.medium:412`.
- The DSM-specific KOMODO owners `komodo.medium:412_18806` and `komodo.medium:412_23131` currently have the same ingredient/concentration signature as base Medium 412 and are merged as aliases.
- A bounded gitignore-independent exact search for `komodo.medium:412`, `komodo.medium:412_18806`, `komodo.medium:412_23131`, `mediadive.medium:412`, `DSMZ_Medium412.pdf`, `ACETOMICROBIUM_FAECALIS_MEDIUM`, and `acetomicrobium_faecalis_medium` found the expected four normalized owners, the expected source-index rows, and the current generated merge.

## Evidence

- DSMZ Medium 412 directly lists 2.000 g Trypticase peptone, 2.000 g yeast extract, 4.000 g glucose, 0.225 g K2HPO4, 0.255 g KH2PO4, 0.255 g ammonium sulfate, 0.500 g NaCl, 0.100 g MgSO4.7H2O, 0.070 g CaCl2.2H2O, 5.000 g Na-acetate, 1.000 mg resazurin, 6.000 g NaHCO3, 0.500 g cysteine-HCl.H2O, and 1000.000 ml distilled water.
- DSMZ adds Vitamin solution from DSMZ Medium 141 at `10.000 ml/L`; the generated record instead flattens biotin, folic acid, pyridoxine hydrochloride, thiamine HCl, riboflavin, nicotinic acid, calcium pantothenate, vitamin B12, p-aminobenzoic acid, and alpha-lipoic acid at stock strength.
- DSMZ adds Trace element solution from DSMZ Medium 141 at `10.000 ml/L`; the generated record instead flattens the trace stock's NTA, MnSO4.H2O, FeSO4.7H2O, CoSO4.7H2O, ZnSO4.7H2O, CuSO4.5H2O, AlK(SO4)2.12H2O, H3BO3, Na2MoO4.2H2O, NiCl2.6H2O, Na2SeO3.5H2O, and Na2WO4.2H2O at stock strength.
- Cleanup merged main-medium rows with DSMZ Medium 141 trace-stock rows: NaCl is recorded as `1.5 G_PER_L` with `0.5 + 1.0`, MgSO4.7H2O is recorded as `3.1 G_PER_L` with `0.1 + 3.0`, and CaCl2.2H2O is recorded as `0.17 G_PER_L` with `0.07 + 0.1`.
- The direct DSMZ owner preserves the `Autoclave under 2 bar N2:CO2 (80:20)` preparation instruction; the canonical generated record is KOMODO-derived and drops preparation steps.
- The base KOMODO owner says `Aerobic: Yes`, while the two DSM-specific KOMODO owners say `Aerobic: No` for the same DSMZ Medium 412 chemistry.

## Completeness

- The generated record is incomplete because DSMZ Medium 141 vitamin and trace-element stocks are represented only as flattened top-level ingredients.
- DSMZ distilled-water rows are absent from the main recipe and both stock recipes.
- The direct DSMZ anaerobic autoclave instruction and DSMZ Medium 141 trace-solution preparation text are absent from the canonical generated record.

## Findings

- BLOCKER: the generated record flattens the 10 ml/L DSMZ Medium 141 vitamin stock at stock strength.
- BLOCKER: the generated record flattens the 10 ml/L DSMZ Medium 141 trace-element stock at stock strength.
- MAJOR: NaCl, MgSO4.7H2O, and CaCl2.2H2O were summed across direct main-medium rows and trace-stock rows rather than preserving the 10 ml/L stock addition context.
- MAJOR: the generated record uses the KOMODO owner as canonical and drops the direct DSMZ anaerobic autoclave instruction.
- MAJOR: the canonical KOMODO owner says `Aerobic: Yes`, contradicting the anaerobic DSMZ source and the two DSM-specific KOMODO aliases.
- MAJOR: `data/normalized_yaml/bacterial/KOMODO_412_ACETOMICROBIUM_FAECALIS_medium.yaml`, `data/normalized_yaml/bacterial/medium_412_modified_for_dsm_18806.yaml`, and `data/normalized_yaml/bacterial/medium_412_modified_for_dsm_23131.yaml` retain malformed curation history timestamp `2026-01-27T01:15:02.fZ`.

## Recommended Edits

- Repair all four normalized Medium 412 owners to encode the 10 ml/L DSMZ Medium 141 vitamin stock and 10 ml/L DSMZ Medium 141 trace-element stock instead of flattening those stocks into the final medium.
- Keep main-medium NaCl, MgSO4.7H2O, and CaCl2.2H2O separate from stock rows.
- Preserve the DSMZ anaerobic autoclave instruction and DSMZ Medium 141 trace-preparation text in the canonical generated record.
- Remove or correct the base KOMODO `Aerobic: Yes` assertion and malformed KOMODO timestamps.
- Verify whether `412_18806` and `412_23131` are true source aliases or strain-specific variants after normalized stock repair.
- Regenerate `data/merge_yaml/merged/ACETOMICROBIUM_FAECALIS_MEDIUM.yaml` after normalized repair.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after normalized repair and merge regeneration.
- Re-fetch `DSMZ_Medium412.pdf` and verify that every DSMZ Medium 141 vitamin and trace component is either inside its proper stock recipe or diluted by the 10 ml/L addition volume.
- Re-run ignored-file-inclusive exact searches for `komodo.medium:412`, `komodo.medium:412_18806`, `komodo.medium:412_23131`, and `mediadive.medium:412` to confirm the four source owners still merge only if their repaired formulas are identical.

## Additional Notes

- Optional empty fields were not treated as defects.
