# YAML Record Review: ARTIFICIAL BRACKISH WATER MEDIUM 2

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/artificial_brackish_water_medium_2.yaml`
- Started UTC: 2026-09-21T14:58:23Z
- Finished UTC: 2026-09-21T14:58:39Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:015853` |
| Label | `artificial_brackish_water_medium_2` |
| Source identity | JCM Medium 1399 |
| Generated status | Generated merge under `data/merge_yaml/merged/`; do not edit in place |
| Maintained owner | `data/normalized_yaml/bacterial/JCM_J1399_ARTIFICIAL_BRACKISH_WATER_MEDIUM_2.yaml` |
| Merge provenance | Single-source merge from `JCM_J1399_ARTIFICIAL_BRACKISH_WATER_MEDIUM_2` |

This review covers exactly `data/merge_yaml/merged/artificial_brackish_water_medium_2.yaml`. `find reports/yaml_record_review -name '*artificial_brackish_water_medium_2.md' -print` searched the ignored `reports/yaml_record_review/` tree and found no prior report named for this target.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/artificial_brackish_water_medium_2.yaml` | Passed: `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/artificial_brackish_water_medium_2.yaml --out /private/tmp/artificial_brackish_water_medium_2.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/artificial_brackish_water_medium_2.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/artificial_brackish_water_medium_2.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. The only emitted message was the known `eutils` `pkg_resources` deprecation warning. |
| Embedded curation history | `just validate-history` | Not checked: the repository exposes this validator for standalone `history/*.yaml` records, not for embedded `MediaRecipe.curation_history` blocks in one merged recipe. |

The project `just` wrappers were not rerun in this pass because this checkout currently resolves through Python 3.13 and attempts to build `llvmlite==0.46.0`, which fails before any target-specific YAML validation. The no-project commands above exercise the narrow validators against this one generated record.

## Identity and Grounding

The record identity is sound. JCM Medium 1399 is titled `ARTIFICIAL BRACKISH WATER MEDIUM 2`, and the generated record's `jcm.grmd:1399` term, label, source link, category, physical state, and single-source `merged_from` all point at that one medium.

The direct base ingredients are grounded and quantified correctly. JCM 1399 lists NaCl 13.2 g, KH2PO4 0.2 g, NH4Cl 0.25 g, KCl 0.5 g, Na2SO4 4.0 g, Resazurin 1.0 mg, and Distilled water 940.0 ml, matching the generated YAML's values and units.

## Evidence

JCM 1399 supports the generated post-autoclave stock amounts: Trace element solution from JCM 439 at 1.0 ml/L, Selenite-tungstate solution from JCM 431 at 1.0 ml/L, 8% NaHCO3 at 30.0 ml/L, 1 M MgCl2 x 6H2O at 17.0 ml/L, 1 M CaCl2 x 2H2O at 1.0 ml/L, three JCM 403 vitamin-family stocks at 1.0 ml/L each, 1 M sodium formate at 5.0 ml/L, 1 M sodium acetate at 2.0 ml/L, and pre-use 5% Na2S x 9H2O at 6.0 ml/L.

The generated record is stale relative to its maintained owner. Its JCM 1399 stock additions still appear as direct `ingredients` with no `source` or `notes`, and its two preparation steps collapse the source protocol. The maintained owner now has named `solutions`, aeration and culture-vessel context, five preparation steps, a September 11 repair event, data-quality flags, and formal JCM references.

JCM 439, 431, and 403 supply stock compositions for Trace element, Selenite-tungstate, Vitamin, Thiamine, and Vitamin B12 solutions. The maintained owner cites those sources but still leaves those solution `composition` arrays absent.

## Completeness

Consequential gaps:

- The generated output lacks the maintained owner's `aeration`, `culture_vessel`, `incubation_atmosphere`, formal `references`, data-quality flags, source notes, and repaired preparation sequence.
- The maintained owner still has no nested composition for the JCM 439 trace-element stock, JCM 431 selenite-tungstate stock, the three JCM 403 vitamin-family stocks, 1 M MgCl2 x 6H2O, 1 M CaCl2 x 2H2O, 1 M sodium formate, or 1 M sodium acetate.

Optional `target_organisms` are absent. That is acceptable because this JCM recipe does not itself provide a curated organism-growth assertion.

## Findings

| Severity | Finding | Evidence | Maintained owner for a fix |
|---|---|---|---|
| Major | The generated merge is stale relative to the repaired normalized JCM 1399 owner. | The generated record's last curation event is the 2026-08-06 merge, while the maintained owner has a 2026-09-11 `RESOLVED_JCM_1399_BRACKISH_SCORE15` event with repaired `solutions`, `preparation_steps`, `aeration`, `culture_vessel`, `incubation_atmosphere`, and `references`. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/bacterial/JCM_J1399_ARTIFICIAL_BRACKISH_WATER_MEDIUM_2.yaml`. |
| Major | Referenced stock compositions are still incomplete in the maintained owner. | JCM 1399 references JCM 439, JCM 431, and JCM 403 stock recipes; the maintained owner carries the referenced stock names and ml/L amounts but omits their internal compositions. | Add nested compositions from JCM Media 439, 431, and 403 to the corresponding `solutions` entries. |
| Minor | Four simple stocks are represented only by stock names and molarity or percent in text. | JCM 1399 names 1 M MgCl2 x 6H2O, 1 M CaCl2 x 2H2O, 1 M Sodium formate, and 1 M Sodium acetate solutions; the maintained owner records only the final ml/L amounts. | Add one-solute `composition` entries for those four stock solutions so their stock strength is structured. |

## Recommended Edits

1. Curate nested compositions for the JCM 439 Trace element, JCM 431 Selenite-tungstate, and JCM 403 Vitamin/Thiamine/Vitamin B12 solutions in `data/normalized_yaml/bacterial/JCM_J1399_ARTIFICIAL_BRACKISH_WATER_MEDIUM_2.yaml`.
2. Add one-solute compositions for the 1 M MgCl2 x 6H2O, 1 M CaCl2 x 2H2O, 1 M Sodium formate, and 1 M Sodium acetate stocks.
3. Regenerate `data/merge_yaml/merged/artificial_brackish_water_medium_2.yaml` from the repaired normalized owner.

## Follow-up Checks

- Run `just validate data/normalized_yaml/bacterial/JCM_J1399_ARTIFICIAL_BRACKISH_WATER_MEDIUM_2.yaml`.
- Run `just validate-references data/normalized_yaml/bacterial/JCM_J1399_ARTIFICIAL_BRACKISH_WATER_MEDIUM_2.yaml`.
- Run the same open-schema, strict, reference, and term validators against the regenerated merged record.
- Manually compare the regenerated stock solutions against JCM Media 1399, 439, 431, and 403.

## Additional Notes

- The single-source merge itself is sound; no cross-source identity conflation was found.
- The JCM GRMD import spelling is corrected here relative to the previous `Artficial` records: JCM 1399 uses `ARTIFICIAL`, and the record preserves that spelling.
