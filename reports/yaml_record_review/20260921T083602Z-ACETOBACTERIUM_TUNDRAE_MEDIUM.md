# YAML Record Review: ACETOBACTERIUM TUNDRAE MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/ACETOBACTERIUM_TUNDRAE_MEDIUM.yaml
- Started UTC: 2026-09-21T08:34:40Z
- Finished UTC: 2026-09-21T08:36:02Z
- Verdict: needs curation

## Target

- Reviewed generated record `data/merge_yaml/merged/ACETOBACTERIUM_TUNDRAE_MEDIUM.yaml`.
- Stable identifier: `CultureMech:006769`.
- Source identity asserted by the canonical record: KOMODO ModelSEED `900`, copied from DSMZ Medium 900 / MediaDive `mediadive.medium:900`.
- The stale generated record was merged from two source owners, `KOMODO_900_ACETOBACTERIUM_TUNDRAE_MEDIUM` and `acetobacterium_tundrae_medium`, on fingerprint `101d1995fba4f59e03cae4b247e27b3671efdbf2d9bd45293ddd2dce8c0fea8a`.
- Current authoritative owners: `data/normalized_yaml/bacterial/KOMODO_900_ACETOBACTERIUM_TUNDRAE_MEDIUM.yaml` and `data/normalized_yaml/bacterial/acetobacterium_tundrae_medium.yaml`.

## Validation

- PASS: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ACETOBACTERIUM_TUNDRAE_MEDIUM.yaml`
- PASS: `scripts/validate_strict.py data/merge_yaml/merged/ACETOBACTERIUM_TUNDRAE_MEDIUM.yaml`
- PASS: `linkml-reference-validator validate data data/merge_yaml/merged/ACETOBACTERIUM_TUNDRAE_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- PASS: `linkml-term-validator validate-data data/merge_yaml/merged/ACETOBACTERIUM_TUNDRAE_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
- Not checked: embedded `MediaRecipe.curation_history` entries; the documented history validator targets standalone files under `history/`.

## Identity and Grounding

- DSMZ Medium 900 resolves and identifies the source as `900: ACETOBACTERIUM TUNDRAE MEDIUM`.
- The KOMODO/DSMZ duplicate relationship is coherent: the KOMODO owner says it copied DSMZ Medium 900, and both normalized owners share the same ingredient/concentration signature.
- A gitignore-independent exact search for `komodo.medium:900`, `mediadive.medium:900`, `DSMZ_Medium900.pdf`, `KOMODO_900_ACETOBACTERIUM_TUNDRAE_MEDIUM`, and `DSMZ_900_ACETOBACTERIUM_TUNDRAE_MEDIUM` found the expected KOMODO owner, expected direct DSMZ owner, current generated merge, expected source-index rows, historical validation reports, and the earlier DSMZ/KOMODO source-duplicate review.
- The source is anaerobic: DSMZ instructs sparging with 80% N2 / 20% CO2, dispensing under the same gas, autoclaving anoxic tubes or vials, and adding anoxic sterile stocks. The KOMODO duplicate nevertheless says `Aerobic: Yes`.

## Evidence

- DSMZ Medium 900 is built from 1000 ml distilled water, 1 ml Trace element solution SL-10, 1 ml Seven vitamins solution, direct KCl, MgCl2.6H2O, CaCl2.2H2O, NH4Cl, KH2PO4, yeast extract, 0.50 ml sodium resazurin 0.1% w/v, 1.50 g Na2CO3, 5.00 g D-fructose, 0.30 g cysteine, and 0.30 g Na2S.9H2O.
- The generated record correctly rescales the direct main-medium rows to the approximately 1002 ml assembled volume: for example KCl is `0.329341 G_PER_L`, MgCl2.6H2O is `0.518962 G_PER_L`, yeast extract is `0.998004 G_PER_L`, and sodium carbonate is `1.49701 G_PER_L`.
- The generated record is stale relative to the 2026-08-07 normalized repair: FeCl2.4H2O, vitamin B12, nicotinic acid, pyridoxine, and thiamine have been moved into 1 ml/L stock solutions in current `data/normalized_yaml`, but the generated merge still has them as top-level final ingredients.
- The current normalized owners still leave most Trace element solution SL-10 components at stock strength as top-level final ingredients: HCl is `2.5 G_PER_L`, ZnCl2 is `0.07 G_PER_L`, MnCl2.4H2O is `0.1 G_PER_L`, H3BO3 is `0.006 G_PER_L`, CoCl2.6H2O is `0.19 G_PER_L`, CuCl2.2H2O is `0.002 G_PER_L`, NiCl2.6H2O is `0.024 G_PER_L`, and Na2MoO4.2H2O is `0.036 G_PER_L`.
- The current normalized owners also leave p-aminobenzoic acid, D-biotin, and calcium pantothenate at Seven-vitamins stock strength even though only 1 ml/L is added to the final medium.

## Completeness

- The generated record is incomplete relative to the direct DSMZ owner because it uses the KOMODO owner as canonical and drops the DSMZ anaerobic preparation steps.
- The generated record is stale relative to current normalized stock nesting.
- Distilled water rows are absent from the main medium and both stock recipes.
- The stock hierarchy is incomplete even in current normalized owners, so reviewers cannot see all SL-10 and Seven-vitamins components inside their correct stock contexts.

## Findings

- BLOCKER: the generated record flattens Trace element solution SL-10 components at stock strength instead of preserving a 1 ml/L stock addition.
- BLOCKER: the generated record flattens Seven vitamins solution components at stock strength instead of preserving a 1 ml/L stock addition.
- MAJOR: the generated merge is stale and has not picked up the 2026-08-07 partial stock nesting in both normalized owners.
- MAJOR: the current normalized owners only partially nested SL-10 and Seven vitamins, leaving most stock components as top-level final ingredients.
- MAJOR: the generated merge uses the KOMODO owner as canonical and drops the DSMZ anaerobic preparation steps.
- MAJOR: the canonical KOMODO owner says `Aerobic: Yes`, contradicting the DSMZ anaerobic recipe it copied.
- MAJOR: `data/normalized_yaml/bacterial/KOMODO_900_ACETOBACTERIUM_TUNDRAE_MEDIUM.yaml` retains malformed curation history timestamp `2026-01-27T01:15:03.fZ`.

## Recommended Edits

- Finish stock nesting in `data/normalized_yaml/bacterial/acetobacterium_tundrae_medium.yaml` so every Trace element solution SL-10 component and every Seven vitamins component is inside the proper 1 ml/L stock solution.
- Apply the same repair to `data/normalized_yaml/bacterial/KOMODO_900_ACETOBACTERIUM_TUNDRAE_MEDIUM.yaml`.
- Preserve the direct DSMZ anaerobic preparation text in the canonical generated record.
- Remove or correct the KOMODO `Aerobic: Yes` assertion and malformed timestamp.
- Regenerate `data/merge_yaml/merged/ACETOBACTERIUM_TUNDRAE_MEDIUM.yaml` after normalized repair.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after normalized repair and merge regeneration.
- Re-fetch `DSMZ_Medium900.pdf` and verify that all SL-10 and Seven-vitamins components are either inside their stock recipes or diluted into the final medium by the 1 ml/L addition volume.
- Re-run an exact ignored-file-inclusive search for `komodo.medium:900`, `mediadive.medium:900`, and `KOMODO_900_ACETOBACTERIUM_TUNDRAE_MEDIUM` to confirm only the expected KOMODO/DSMZ source-duplicate pair remains.

## Additional Notes

- DSMZ's For DSM 8238 note is about a lactate/pH 7.5 variant of Medium 900 and is not part of this base Acetobacterium tundrae recipe.
