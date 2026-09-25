# YAML Record Review: ACETIVIBRIO ALKALICELLULOSI MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/ACETIVIBRIO_ALKALICELLULOSI_MEDIUM.yaml
- Started UTC: 2026-09-21T08:20:39Z
- Finished UTC: 2026-09-21T08:22:06Z
- Verdict: needs curation

## Target

- Reviewed generated record `data/merge_yaml/merged/ACETIVIBRIO_ALKALICELLULOSI_MEDIUM.yaml`.
- Stable identifier: `CultureMech:000459`.
- Source identity asserted by the canonical record: DSMZ Medium 1036 / MediaDive `mediadive.medium:1036`.
- The generated record was merged from two source owners, `acetivibrio_alkalicellulosi_medium` and `clostridium_alkalicellum_medium`, on fingerprint `2564446e099acb871489b6fc54ddf1c85811ac829cd380253583550bab4d1127`.
- Current authoritative owners: `data/normalized_yaml/bacterial/acetivibrio_alkalicellulosi_medium.yaml` and `data/normalized_yaml/bacterial/clostridium_alkalicellum_medium.yaml`.

## Validation

- PASS: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ACETIVIBRIO_ALKALICELLULOSI_MEDIUM.yaml`
- PASS: `scripts/validate_strict.py data/merge_yaml/merged/ACETIVIBRIO_ALKALICELLULOSI_MEDIUM.yaml`
- PASS: `linkml-reference-validator validate data data/merge_yaml/merged/ACETIVIBRIO_ALKALICELLULOSI_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- PASS: `linkml-term-validator validate-data data/merge_yaml/merged/ACETIVIBRIO_ALKALICELLULOSI_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
- Not checked: embedded `MediaRecipe.curation_history` entries; the documented history validator targets standalone files under `history/`.

## Identity and Grounding

- The DSMZ/KOMODO duplicate relationship is coherent: the KOMODO `CLOSTRIDIUM ALKALICELLULUM medium` owner says it copied DSMZ Medium 1036 and is ingredient-identical to the current DSMZ `ACETIVIBRIO ALKALICELLULOSI MEDIUM` owner.
- The DSMZ Medium 1036 PDF resolves and identifies the source as `1036: ACETIVIBRIO ALKALICELLULOSI MEDIUM`.
- A gitignore-independent exact search for `mediadive.medium:1036`, `DSMZ Medium 1036`, `DSMZ_Medium1036`, `acetivibrio_alkalicellulosi_medium`, and `clostridium_alkalicellum_medium` found the expected DSMZ owner, expected KOMODO source-duplicate owner, their generated merge, and source-index rows.
- The source is anaerobic: DSMZ instructs sparging with 100% N2, dispensing under N2, and preparing anoxic cellobiose and sulfide stocks. The KOMODO duplicate nevertheless says `Aerobic: Yes`.
- The ChEBI groundings for NH4Cl, KH2PO4, MgCl2.6H2O, KCl, Na2CO3, NaHCO3, NaCl, cellobiose, Na2S.9H2O, FeCl2.4H2O, and the SL-10 salts are plausible label matches.

## Evidence

- DSMZ lists a base medium with two 1 ml/L stock additions: Trace element solution SL-10 and Selenite-tungstate solution.
- The base-medium component concentrations in CultureMech are DSMZ masses normalized over the final volume after two 1 ml additions, e.g. 0.50 g NH4Cl appears as `0.499002 G_PER_L`.
- Components inside SL-10 are stock components, not direct final-medium grams per litre. The record imports 1.50 g/L FeCl2.4H2O, 70 mg/L ZnCl2, 100 mg/L MnCl2.4H2O, and the rest of SL-10 at full stock strength, even though only 1 ml of that stock is added per litre.
- Components inside Selenite-tungstate solution are likewise imported at stock strength: 0.50 g/L NaOH, 3 mg/L Na2SeO3.5H2O, and 4 mg/L Na2WO4.2H2O.
- DSMZ's 1000 ml distilled water rows for the base medium and both stock solutions are absent.

## Completeness

- The generated merge is complete relative to the direct DSMZ owner.
- The direct DSMZ owner is incomplete relative to DSMZ 1036 because the SL-10 and selenite-tungstate stocks are flattened without the required 1 ml/L dilution.
- The DSMZ anoxic preparation instructions are retained in the generated record.
- The `SOURCE_DUPLICATE` relationship correctly keeps the older KOMODO `Clostridium alkalicellum` name as a synonym of the current DSMZ `Acetivibrio alkalicellulosi` medium.

## Findings

- BLOCKER: Trace element solution SL-10 components are present at stock strength, not at the final 1 ml/L dilution used by DSMZ Medium 1036.
- BLOCKER: Selenite-tungstate solution components are present at stock strength, not at the final 1 ml/L dilution used by DSMZ Medium 1036.
- MAJOR: distilled water is omitted for the base medium and both nested stock solutions.
- MAJOR: the KOMODO `clostridium_alkalicellum_medium` owner says `Aerobic: Yes`, contradicting the DSMZ anaerobic recipe it copied.
- MAJOR: `data/normalized_yaml/bacterial/clostridium_alkalicellum_medium.yaml` retains malformed curation history timestamp `2026-01-27T01:15:01.fZ`.

## Recommended Edits

- Re-curate `data/normalized_yaml/bacterial/acetivibrio_alkalicellulosi_medium.yaml` from DSMZ Medium 1036 with Trace element solution SL-10 and Selenite-tungstate solution represented as stocks or correctly diluted final components.
- Apply the same repair to `data/normalized_yaml/bacterial/clostridium_alkalicellum_medium.yaml` or regenerate it from the repaired DSMZ parent.
- Add the DSMZ distilled-water rows for the base recipe and stock solutions.
- Remove or correct the KOMODO `Aerobic: Yes` assertion.
- Correct the KOMODO import timestamp to a parseable ISO 8601 timestamp.
- Regenerate `data/merge_yaml/merged/ACETIVIBRIO_ALKALICELLULOSI_MEDIUM.yaml` after normalized repair.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after normalized repair and merge regeneration.
- Re-fetch `DSMZ_Medium1036.pdf` and verify that every SL-10 and selenite-tungstate component is either represented inside a named stock or diluted by 0.001 in the final medium.
- Re-run an exact ignored-file-inclusive search for `mediadive.medium:1036`, `DSMZ_Medium1036`, `acetivibrio_alkalicellulosi_medium`, and `clostridium_alkalicellum_medium` to confirm that only the expected source-duplicate pair remains.

## Additional Notes

- The non-round main-medium amounts appear to be final-volume normalization after adding two 1 ml stocks; those base amounts should be left alone if the stock additions remain at 1 ml/L.
