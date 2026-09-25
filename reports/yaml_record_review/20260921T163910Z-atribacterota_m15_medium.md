# YAML Record Review: atribacterota_m15_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/atribacterota_m15_medium.yaml
- Started UTC: 2026-09-21T16:37:36Z
- Finished UTC: 2026-09-21T16:39:10Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/atribacterota_m15_medium.yaml`, a generated
`MediaRecipe` with stable ID `CultureMech:015850`, normalized name
`atribacterota_m15_medium`, original name `ATRIBACTEROTA M15 MEDIUM`, category
`bacterial`, `medium_type: COMPLEX`, `composition_type: UNDEFINED`,
`physical_state: LIQUID`, `ph_value: 7.5`, media term `jcm.grmd:1392`, and
merge fingerprint
`01d96e444ccb68e4d9d3dddc81509b94ff6f55a6c4bfe454e07f688ff7d0f19c`.

The generated merge was produced from
`data/normalized_yaml/bacterial/JCM_J1392_ATRIBACTEROTA_M15_MEDIUM.yaml`. That
normalized owner is the authoritative record; the generated merge should be
regenerated from it, not edited in place.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/atribacterota_m15_medium.yaml` | Pass, `No issues found`. |
| Strict schema layer | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/atribacterota_m15_medium.yaml --out /private/tmp/atribacterota_m15_medium.strict.tsv --workers 1 --quiet` | Pass: 1 file scanned, 0 files with errors, 0 error rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/atribacterota_m15_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass: 1 file validated, 0 reference checks emitted. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/atribacterota_m15_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass; the validator also emitted only the known `eutils`/`pkg_resources` deprecation warning. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for standalone `history/` files, not a focused validator for `MediaRecipe.curation_history` in one generated merge record. |

The direct `just validate-schema`, `just validate-strict`, `just
validate-references`, and `just validate-terms` entrypoints were not used for
this target because this checkout currently reaches a project `uv` build of
`llvmlite==0.46.0` under Python 3.13 before target-specific validation and
crashes in setuptools with `TypeError: Popen.__init__() got an unexpected
keyword argument 'dry_run'`.

## Identity and Grounding

The target identity is correct. The live JCM GRMD 1392 page resolves as
`ATRIBACTEROTA M15 MEDIUM`, and the generated target, its normalized owner,
and the JCM page all agree on GRMD 1392, name, pH 7.5, liquid state, base
salts, stock additions, and preparation text.

A corrected gitignore-independent search covered `data`, `reports`, `history`,
and `.claude` for `CultureMech:015850`, `jcm.grmd:1392`, `GRMD=1392`,
`JCM_J1392_ATRIBACTEROTA_M15_MEDIUM`, and `ATRIBACTEROTA M15 MEDIUM`. It found
the generated target, the maintained JCM owner, indexes, import-tracking rows,
and no same-source duplicate normalized owner. The initial broader search also
included generic `M15` and was interrupted because it matched unrelated
records; it was not used for this judgement. An exhaustive `find` confirmed
the maintained owner at
`data/normalized_yaml/bacterial/JCM_J1392_ATRIBACTEROTA_M15_MEDIUM.yaml`.

## Evidence

The live JCM page supports the seven direct ingredients in the maintained
owner: NaCl 20.0 g/L, MgCl2 hexahydrate 3.0 g/L, CaCl2 dihydrate 0.15 g/L,
NH4Cl 0.25 g/L, KH2PO4 0.2 g/L, Resazurin 1.0 mg/L, and distilled water
950.0 ml/L.

JCM GRMD 1392 then adds these solutions after cooling: 1.0 ml/L of Selenite-
tungstate solution from JCM 431, 50.0 ml/L of 8% NaHCO3 solution, 1.0 ml/L
each of Vitamin solution, Thiamine solution, and Vitamin B12 solution from JCM
403, followed by 20.0 ml/L of 10% Yeast extract solution and 10.0 ml/L of 5%
Na2S x 9H2O solution. It also calls for 1.0 ml/L of Trace element solution
from JCM 439 in the initial mixture.

The normalized owner now preserves that stock structure: it has seven direct
`ingredients`, eight `solutions`, nested compositions for the explicit NaHCO3,
yeast-extract, and sulfide stocks, opaque rows for the JCM 439/431/403
cross-referenced stocks, four `references`, and a
`repair_jcm_score10_stock_solutions.py` curation event dated
2026-09-13. The generated target is stale relative to that owner: it was
merged on 2026-08-06, lacks the 2026-09-13 repair event and `references`, and
still has the eight stock additions flattened into `ingredients`.

The generated preparation text is source-supported. The source directs
mixing and pH adjustment to 7.5, boiling and cooling under an N2-CO2 4:1 gas
stream, autoclaving under the same gas, filter-sterile additions after
cooling, anaerobic Balch-tube distribution under the same gas, and pH
readjustment to 7.5-8.0 if needed.

## Completeness

The missing target organism and growth-evidence fields are not findings in
this imported JCM recipe: the inspected JCM recipe does not assert a strain
growth outcome.

The generated target is materially incomplete as a projection of its maintained
source because it drops the maintained stock-solution hierarchy and reference
list. Before writing this report,
`find reports/yaml_record_review -maxdepth 1 -name '*atribacterota_m15_medium.md' -print`
covered ignored and unignored files in the review-report directory and found no
prior exact report for this generated stem.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated merge is stale and no longer preserves the maintained record's repaired stock-solution hierarchy. | `data/normalized_yaml/bacterial/JCM_J1392_ATRIBACTEROTA_M15_MEDIUM.yaml` moved the JCM 1392 stocks into eight `solutions` on 2026-09-13; `data/merge_yaml/merged/atribacterota_m15_medium.yaml` was last merged on 2026-08-06 and still contains all eight stock additions as flat `ingredients`. | Regenerate `data/merge_yaml/merged/` from the current normalized source; do not patch the generated file by hand. |

No blockers or minor findings were found beyond this stale-generated-output
major finding.

## Recommended Edits

1. Regenerate the merge layer so `data/merge_yaml/merged/atribacterota_m15_medium.yaml`
   is rebuilt from the current `data/normalized_yaml/bacterial/JCM_J1392_ATRIBACTEROTA_M15_MEDIUM.yaml`.
2. Confirm the regenerated target retains seven direct ingredients, eight
   solution additions, nested NaHCO3, yeast extract, and Na2S x 9H2O stock
   compositions, opaque JCM 439/431/403 cross-references, and all four JCM
   references from the normalized owner.
3. Regenerate any page/browser products derived from `data/merge_yaml/merged/`
   after the merge output is refreshed.

## Follow-up Checks

- Re-run open-schema LinkML, `scripts/validate_strict.py`, the reference
  validator, and the term validator against the regenerated
  `data/merge_yaml/merged/atribacterota_m15_medium.yaml`.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating
  generated merges to prove the stale August 2026 projection has been replaced.
- Manually compare the regenerated merge against JCM GRMD 1392 to confirm the
  solution-addition boundaries still match the live source page.

## Additional Notes

This generated record is a good example of a source layer that has already
been curated while the derived merge layer remains out of date. The normalized
owner matches the inspected JCM source closely; the review finding is limited
to the stale generated target requested by the bulk review order.
