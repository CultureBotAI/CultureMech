# YAML Record Review: ACETOHALOBIUM MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/ACETOHALOBIUM_MEDIUM.yaml
- Started UTC: 2026-09-21T08:41:32Z
- Finished UTC: 2026-09-21T08:43:16Z
- Verdict: needs curation

## Target

- Reviewed generated record `data/merge_yaml/merged/ACETOHALOBIUM_MEDIUM.yaml`.
- Stable identifier: `CultureMech:005623`.
- Source identity asserted by the canonical record: KOMODO ModelSEED `494`, copied from DSMZ Medium 494 / MediaDive `mediadive.medium:494`.
- The generated record was merged from `KOMODO_494_ACETOHALOBIUM_medium`, `acetohalobium_medium`, and `acetohalobium_medium_replace_trimethylamine_x_hcl_with_glycinebetaine` on fingerprint `1401b145bd3127b1659b68b13c46c8ec44493249b96bb9dae924884169c19559`.
- Current authoritative source owners for that merge: `data/normalized_yaml/bacterial/KOMODO_494_ACETOHALOBIUM_medium.yaml`, `data/normalized_yaml/bacterial/acetohalobium_medium.yaml`, and `data/normalized_yaml/bacterial/acetohalobium_medium_replace_trimethylamine_x_hcl_with_glycinebetaine.yaml`.

## Validation

- PASS: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ACETOHALOBIUM_MEDIUM.yaml`
- PASS: `scripts/validate_strict.py data/merge_yaml/merged/ACETOHALOBIUM_MEDIUM.yaml`
- PASS: `linkml-reference-validator validate data data/merge_yaml/merged/ACETOHALOBIUM_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- PASS: `linkml-term-validator validate-data data/merge_yaml/merged/ACETOHALOBIUM_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
- Not checked: embedded `MediaRecipe.curation_history` entries; the documented history validator targets standalone files under `history/`.

## Identity and Grounding

- DSMZ Medium 494 resolves and identifies the source as `494: ACETOHALOBIUM MEDIUM`.
- The KOMODO/DSMZ duplicate relationship is coherent: the KOMODO owner says it copied DSMZ Medium 494, and the direct DSMZ owner carries `mediadive.medium:494`.
- A bounded gitignore-independent exact search for `komodo.medium:494`, `mediadive.medium:494`, `TOGO:M2719`, `TOGO:M2720`, `DSMZ_Medium494.pdf`, `ACETOHALOBIUM_MEDIUM`, and `acetohalobium_medium` found the expected KOMODO/DSMZ source owners, the trimethylamine-to-glycinebetaine KOMODO owner, a TOGO M2719 owner that cites the same DSMZ Medium 494 PDF, a TOGO M2720 owner that cites an ATCC source, the corresponding generated records, and the expected source-index rows.
- The source is anaerobic: DSMZ instructs sparging with 80% N2 / 20% CO2, dispensing under the same gas atmosphere into anoxic Hungate-type tubes or serum vials, and using sterile anoxic stocks. The KOMODO duplicate nevertheless says `Aerobic: Yes`.

## Evidence

- DSMZ Medium 494 directly lists 150.00 g NaCl, 0.33 g KCl, 0.33 g NH4Cl, 0.33 g KH2PO4, 0.33 g CaCl2.2H2O, 4.00 g MgCl2.6H2O, 0.50 ml sodium resazurin 0.1% w/v, 2.00 g Na2CO3, 0.05 g yeast extract, 2.40 g trimethylamine-HCl, 0.50 g Na2S.9H2O, and 1000.00 ml distilled water.
- DSMZ adds Modified Wolin's mineral solution at `10.00 ml/L`; the generated record instead flattens that stock's NTA, MgSO4.7H2O, MnSO4.H2O, FeSO4.7H2O, CoSO4.7H2O, ZnSO4.7H2O, CuSO4.5H2O, AlK(SO4)2.12H2O, H3BO3, Na2MoO4.2H2O, NiCl2.6H2O, Na2SeO3.5H2O, and Na2WO4.2H2O at stock strength.
- DSMZ also adds Wolin's vitamin solution `(10x)` at `1.00 ml/L`; the generated record instead flattens biotin, folic acid, pyridoxine hydrochloride, thiamine HCl, riboflavin, nicotinic acid, calcium pantothenate, vitamin B12, p-aminobenzoic acid, and alpha-lipoic acid at 10x stock strength.
- The generated NaCl and CaCl2.2H2O rows are inflated because cleanup merged the main-medium rows with the Modified Wolin stock rows: NaCl is recorded as `149.368 G_PER_L` with `148.368 + 1.0`, and CaCl2.2H2O is recorded as `0.42640900000000004 G_PER_L` with `0.326409 + 0.1`.
- The source named `acetohalobium_medium_replace_trimethylamine_x_hcl_with_glycinebetaine` still contains `Trimethylamine-HCl` at `2.37389 G_PER_L` and no glycinebetaine row, so the generated merge treats an intended substrate variant as another source duplicate of the base trimethylamine recipe.
- The direct DSMZ owner preserves anaerobic preparation text and Modified Wolin mineral preparation text; the canonical generated record is KOMODO-derived and drops that preparation text.

## Completeness

- The generated record is incomplete as a stock hierarchy because Modified Wolin's mineral solution and Wolin's vitamin solution are represented only as flattened top-level ingredients.
- DSMZ distilled-water rows are absent from the main recipe and both stock recipes.
- The canonical generated record is incomplete relative to the direct DSMZ owner because it drops anaerobic handling, sterile-stock addition, pH-adjustment, and Modified Wolin mineral preparation instructions.
- TOGO M2719 also cites DSMZ Medium 494 but remains a separate generated sibling.

## Findings

- BLOCKER: the record flattens the 10 ml/L Modified Wolin's mineral stock at stock strength.
- BLOCKER: the record flattens the 1 ml/L Wolin's vitamin solution `(10x)` at stock strength.
- MAJOR: NaCl and CaCl2.2H2O were summed across direct main-medium rows and Modified Wolin stock rows rather than preserving the 10 ml/L stock addition context.
- MAJOR: `acetohalobium_medium_replace_trimethylamine_x_hcl_with_glycinebetaine` is merged as a source duplicate even though its source ID denotes a glycinebetaine replacement variant.
- MAJOR: the generated record uses the KOMODO owner as canonical and drops the direct DSMZ anaerobic preparation steps.
- MAJOR: the canonical KOMODO owner says `Aerobic: Yes`, contradicting the DSMZ anaerobic recipe it copied.
- MAJOR: `data/normalized_yaml/bacterial/KOMODO_494_ACETOHALOBIUM_medium.yaml` and `data/normalized_yaml/bacterial/acetohalobium_medium_replace_trimethylamine_x_hcl_with_glycinebetaine.yaml` retain malformed curation history timestamp `2026-01-27T01:15:02.fZ`.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/acetohalobium_medium.yaml` and `data/normalized_yaml/bacterial/KOMODO_494_ACETOHALOBIUM_medium.yaml` to encode DSMZ's 10 ml/L Modified Wolin mineral stock and 1 ml/L Wolin 10x vitamin stock instead of flattening them into the final medium.
- Keep main-medium NaCl and CaCl2.2H2O separate from stock NaCl and CaCl2.2H2O.
- Move the DSMZ anoxic handling and sterile-stock addition text into the canonical generated record after repair.
- Repair `data/normalized_yaml/bacterial/acetohalobium_medium_replace_trimethylamine_x_hcl_with_glycinebetaine.yaml` so it actually represents a glycinebetaine replacement variant, then keep it out of the base recipe's source-duplicate merge.
- Remove or correct the KOMODO `Aerobic: Yes` assertion and malformed timestamps.
- Reconcile the TOGO M2719 DSMZ Medium 494 owner with the direct DSMZ/KOMODO source after the stock hierarchy is repaired.
- Regenerate merged records after normalized repair.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after normalized repair and merge regeneration.
- Re-fetch `DSMZ_Medium494.pdf` and verify that every Modified Wolin and Wolin 10x vitamin component is either inside the correct stock recipe or diluted by the correct addition volume.
- Re-run ignored-file-inclusive exact searches for `komodo.medium:494`, `mediadive.medium:494`, `TOGO:M2719`, and `ACETOHALOBIUM_MEDIUM` to confirm DSMZ/KOMODO/TOGO duplicates and glycinebetaine variants generate into the right families.

## Additional Notes

- Optional empty fields were not treated as defects.
