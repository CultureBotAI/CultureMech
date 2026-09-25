# YAML Record Review: bacteriovorax_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BACTERIOVORAX_MEDIUM.yaml
- Started UTC: 2026-09-21T18:12:30Z
- Finished UTC: 2026-09-21T18:13:40Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| Generated record | `data/merge_yaml/merged/BACTERIOVORAX_MEDIUM.yaml` |
| Generated ID | `CultureMech:002000` |
| Label | `bacteriovorax_medium` |
| Source selected by merge | DSMZ Medium 844, `mediadive.medium:844` |
| Duplicate parent | `data/normalized_yaml/bacterial/ppye_medium.yaml` / KOMODO Medium 844, `komodo.medium:844` |
| Canonical normalized owner | `data/normalized_yaml/bacterial/DSMZ_844_BACTERIOVORAX_MEDIUM.yaml` |
| Merge fingerprint | `ad9b0a77f7bd2047181360e6cb446b5dc8904a18c955db3b66e2e8f23fad1d0c` |

The target is a generated duplicate merge of the DSMZ Medium 844 normalized record and the KOMODO `PPYE medium` copy. Future fixes belong in those normalized source records or import/enrichment rules, followed by merge regeneration.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BACTERIOVORAX_MEDIUM.yaml` | Passed: no issues found |
| Strict closed schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/BACTERIOVORAX_MEDIUM.yaml --out /private/tmp/BACTERIOVORAX_MEDIUM.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/BACTERIOVORAX_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 0 checks, all validations passed |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/BACTERIOVORAX_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not checked | No focused embedded `MediaRecipe.curation_history` validator is documented for one merged record; `just validate-history` targets standalone `history/` files |

## Identity and Grounding

The DSMZ Medium 844 identity and PPYE synonym are supported: DSMZ names this recipe `BACTERIOVORAX MEDIUM`, KOMODO imports DSMZ Medium 844 as `PPYE medium`, and the two normalized parents share the same ingredient signature. The generated merge chose the DSMZ identity, so the label is more specific than the KOMODO synonym.

`MgCl2 x 6 H2O`, `CaCl2 x 2 H2O`, and optional agar are correctly grounded. `Proteose peptone no. 3` and `Yeast extract` are still ungrounded in both normalized parents and the generated merge even though ignored-file-inclusive searches of the packaged MIM label index found exact or near-exact source-label mappings for `Proteose peptone no. 3` and `Yeast extract (BD Bacto)`.

## Evidence

DSMZ Medium 844 supports 1.00 g Proteose peptone no. 3, 0.30 g yeast extract, 0.60 g `MgCl2 x 6 H2O`, 0.30 g `CaCl2 x 2 H2O`, optional 12.00 g agar, and 1000.00 ml distilled water. The source specifically says to dissolve all ingredients except magnesium chloride and calcium chloride, then add those two salts after autoclaving from sterile 5% w/v stocks. The generated record keeps the post-autoclave stock-addition instruction as prose and records the final MgCl2 and CaCl2 g/L amounts.

The only source component absent from the ingredient list is distilled water. The two complex organics lack term links despite local MIM mappings.

## Completeness

Consequential gaps:

- Missing `Distilled water 1000.00 ml`.
- Missing exact local term links for `Proteose peptone no. 3` and `Yeast extract`.

Optional organism and growth-evidence fields are not defects for this DSMZ source recipe. The optional agar row is present with 12 g/L and a note marking it optional; the physical state is `SOLID_AGAR`, which is acceptable for the represented agar-plate form.

An ignored-file-inclusive prior-report search covered `reports/yaml_record_review` for `BACTERIOVORAX_MEDIUM`, `bacteriovorax_medium`, `DSMZ_844_BACTERIOVORAX_MEDIUM`, `ppye_medium`, `CultureMech:002000`, and `CultureMech:006649`; it found no prior report for this generated record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The medium omits distilled water. | DSMZ Medium 844 lists 1000.00 ml distilled water. Neither normalized parent nor the generated merge has a water row. | `data/normalized_yaml/bacterial/DSMZ_844_BACTERIOVORAX_MEDIUM.yaml`; `data/normalized_yaml/bacterial/ppye_medium.yaml` |
| Major | Two exact complex ingredients are left ungrounded. | The generated `Proteose peptone no. 3` and `Yeast extract` rows have only `preferred_term` and concentration. The local MIM index maps `Proteose peptone no. 3` to `MICRO:0000180` and maps `Yeast extract (BD Bacto)` to `FOODON:03315426`. | `data/normalized_yaml/bacterial/DSMZ_844_BACTERIOVORAX_MEDIUM.yaml`; `data/normalized_yaml/bacterial/ppye_medium.yaml`; exact-term repair coverage |

## Recommended Edits

1. Add `Distilled water` as 1000.00 ml/L to the DSMZ and KOMODO normalized parents.
2. Ground `Proteose peptone no. 3` to `MICRO:0000180` and `Yeast extract` to `FOODON:03315426` in both normalized parents.
3. Optionally retain the DSMZ brand/source strings, `BD Bacto` for peptone and yeast extract and `Bacto` for agar, in ingredient notes if the source transform can capture them without conflating brand with ingredient identity.
4. Regenerate `data/merge_yaml/merged/BACTERIOVORAX_MEDIUM.yaml`.

## Follow-up Checks

- Run `just validate data/normalized_yaml/bacterial/DSMZ_844_BACTERIOVORAX_MEDIUM.yaml`.
- Run `just validate data/normalized_yaml/bacterial/ppye_medium.yaml`.
- Run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Re-run the no-project open-schema, strict, reference, and term validators against `data/merge_yaml/merged/BACTERIOVORAX_MEDIUM.yaml`.
- Manually compare the regenerated record with DSMZ Medium 844 to confirm the water row, post-autoclave MgCl2/CaCl2 instruction, and optional 12 g/L agar are present.

## Additional Notes

No additional issues.
