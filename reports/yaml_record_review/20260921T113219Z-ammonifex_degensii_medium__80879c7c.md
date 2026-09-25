# YAML Record Review: ammonifex_degensii_medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/ammonifex_degensii_medium__80879c7c.yaml`
- Started UTC: 2026-09-21T11:31:30Z
- Finished UTC: 2026-09-21T11:32:19Z
- Verdict: needs curation

## Target

| Field | Observed value |
| --- | --- |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:001854` |
| Name | `ammonifex_degensii_medium` |
| Original name | `AMMONIFEX DEGENSII MEDIUM` |
| Source identity | DSMZ Medium 716, `mediadive.medium:716` |
| Generated status | Generated two-source merge |
| Generated path | `data/merge_yaml/merged/ammonifex_degensii_medium__80879c7c.yaml` |
| Maintained input | `data/normalized_yaml/bacterial/ammonifex_degensii_medium.yaml` plus `data/normalized_yaml/bacterial/ammonifex_medium.yaml` |

The generated record merges the DSMZ `ammonifex_degensii_medium` owner with the KOMODO `ammonifex_medium` wrapper on `merge_fingerprint: 80879c7cec9ba15e6ed8524f1f57a18798ebdc6241edb81200ae1a97b658876e`.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ammonifex_degensii_medium__80879c7c.yaml` | Passed; no issues found. |
| Strict | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ammonifex_degensii_medium__80879c7c.yaml --out /private/tmp/ammonifex_degensii_medium__80879c7c.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned and 0 `ERROR` rows emitted. |
| Reference | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ammonifex_degensii_medium__80879c7c.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ammonifex_degensii_medium__80879c7c.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Documented focused validator | Not checked: no focused embedded `MediaRecipe.curation_history` validator is documented for one merged record; `just validate-history` targets standalone files under `history/`. |

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints are unavailable in this checkout because project `uv` attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools before target-specific validation. The no-project commands above exercise the same schema and validation code with Python 3.11.

## Identity and Grounding

The DSMZ/KOMODO identity is consistent:

- `id: CultureMech:001854`
- `name: ammonifex_degensii_medium`
- `media_term.preferred_term: DSMZ Medium 716`
- `media_term.term.id: mediadive.medium:716`
- source URL in `notes`: `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium716.pdf`

The formula is not consistent with DSMZ Medium 716. A prior `data-quality-cleanup-v1.0` event merged five repeated ingredient names inside the authoritative DSMZ owner even though each pair represented a different formulation context: one basal-medium ingredient plus one component inside Modified Wolin's mineral solution. The maintained KOMODO wrapper has the same collapsed amounts because it copied the DSMZ composition and then underwent the same duplicate merge.

Grounding mismatches:

- `NiCl2 x 6 H2O` is grounded to anhydrous `CHEBI:34887` / nickel dichloride. The local ChEBI snapshot has exact nickel chloride hexahydrate as `CHEBI:53542`, and the MediaIngredientMech label index has rows for the exact hydrate spelling.
- `KNO3` has exact primary `CHEBI:63043` / potassium nitrate but still uses legacy `mediaingredientmech_term: MediaIngredientMech:000170` instead of `mediaingredientmech_chebi_term`.

## Evidence

Inspected source document:

- DSMZ Medium 716 PDF from `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium716.pdf`

Supported by DSMZ Medium 716:

- The AMMONIFEX DEGENSII MEDIUM identity, pH 7.2, defined liquid classification, and 80% H2 / 20% CO2 gas phase.
- The basal recipe has K2HPO4 x 3 H2O 0.30 g, KH2PO4 0.22 g, (NH4)2SO4 0.22 g, NaCl 1.00 g, MgSO4 x 7 H2O 0.09 g, CaCl2 x 2 H2O 0.06 g, 2 ml FeSO4 x 7 H2O in 0.1% w/v acidic solution, 0.20 ml 0.1% w/v NiCl2 x 6 H2O solution, 1 ml Modified Wolin's mineral solution, 0.50 ml sodium resazurin, KNO3 1.00 g, Na2CO3 1.50 g, DL-dithiothreitol 0.30 g, and 1000 ml distilled water.
- Modified Wolin's mineral solution is a separately prepared stock from DSMZ Medium 141 and contains 1.50 g nitrilotriacetic acid, 3.00 g MgSO4 x 7 H2O, 0.50 g MnSO4 x H2O, 1.00 g NaCl, 0.10 g FeSO4 x 7 H2O, 0.18 g CoSO4 x 7 H2O, 0.10 g CaCl2 x 2 H2O, 0.18 g ZnSO4 x 7 H2O, 0.01 g CuSO4 x 5 H2O, 0.02 g AlK(SO4)2 x 12 H2O, 0.01 g H3BO3, 0.01 g Na2MoO4 x 2 H2O, 0.03 g NiCl2 x 6 H2O, 0.30 mg Na2SeO3 x 5 H2O, 0.40 mg Na2WO4 x 2 H2O, and 1000 ml distilled water.
- The preparation steps through autoclaving, stock addition, dithiothreitol filtration, pH adjustment, and later 0.5 bar 80% H2 / 20% CO2 pressurization are preserved closely.

Unsupported or mismatched claims:

- `NaCl: 1.997009 G_PER_L`, `MgSO4 x 7 H2O: 3.0897308 G_PER_L`, `CaCl2 x 2 H2O: 0.1598205 G_PER_L`, `FeSO4 x 7 H2O: 0.10199402 G_PER_L`, and `NiCl2 x 6 H2O: 0.030199402 G_PER_L` are sums of two different DSMZ rows and are not final medium concentrations.
- The record flattens Modified Wolin's mineral solution into root-level ingredients at stock strength instead of recording the main-recipe addition of 1 ml.
- The main-recipe FeSO4 and NiCl2 additions are stock additions, but their stock descriptions are only implicit in the merged numeric parts.
- The Modified Wolin's mineral solution preparation step is kept as a third top-level step after the main-medium steps, which no longer marks it as a separate stock-solution procedure.

## Completeness

Consequential gaps:

- The generated record lacks explicit boundaries for the Modified Wolin's mineral solution stock and for the two acidic FeSO4 / NiCl2 stock additions.
- The five `DIFFERING_PARTS` rows listed for `data/normalized_yaml/bacterial/ammonifex_degensii_medium.yaml` in `data/import_tracking/reports/merged_duplicates.tsv` are still unresolved in the authoritative normalized owner.
- No target-organism or growth-evidence claim is present; that is an empty optional field, not a defect by itself.

Bounded searches:

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ammonifex_degensii_medium__80879c7c.md'` found no prior report for this generated target.
- `rg --no-ignore --hidden` over `data`, `src`, `scripts`, `history`, and `reports/yaml_record_review` for the target label, source labels, DSMZ/KOMODO ID, and fingerprint found the generated target, maintained DSMZ/KOMODO inputs, the independent TOGO M2714 Ammonifex owner, and the unresolved concentration-merge warnings under `data/import_tracking/reports/merged_duplicates.tsv`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Basal-medium rows and Modified Wolin's mineral-solution rows with the same ingredient name were summed into one root ingredient. | `data/import_tracking/reports/merged_duplicates.tsv` reports `DIFFERING_PARTS` for NaCl, MgSO4 x 7 H2O, CaCl2 x 2 H2O, FeSO4 x 7 H2O, and NiCl2 x 6 H2O. DSMZ 716 shows these are not duplicates; one amount is in the main medium and the other is inside the 1 ml/L Wolin stock. | `data/normalized_yaml/bacterial/ammonifex_degensii_medium.yaml`, `data/normalized_yaml/bacterial/ammonifex_medium.yaml`, and the duplicate-ingredient cleanup/import path |
| Major | Stock additions are flattened without preserving solution boundaries. | DSMZ 716 names 2 ml FeSO4 solution, 0.20 ml NiCl2 solution, and 1 ml Modified Wolin's mineral solution; the record instead exposes stock-internal salts at root level. | MediaDive/KOMODO import or stock-normalization code, then `data/normalized_yaml/bacterial/ammonifex_degensii_medium.yaml` |
| Major | `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride. | DSMZ and the preferred term both specify the hexahydrate; the target uses `CHEBI:34887`, while local ChEBI contains exact `CHEBI:53542` for nickel chloride hexahydrate. | MediaIngredientMech label index or post-import ingredient grounding |
| Minor | `KNO3` still has a deprecated `MediaIngredientMech:*` link. | The primary term is exact `CHEBI:63043`, but the ingredient retains `mediaingredientmech_term: MediaIngredientMech:000170` after the MIM-to-ChEBI migration event. | `data/normalized_yaml/bacterial/ammonifex_degensii_medium.yaml` and `data/normalized_yaml/bacterial/ammonifex_medium.yaml` |

## Recommended Edits

1. Restore the DSMZ 716 source structure: keep the basal NaCl/MgSO4/CaCl2 rows, the FeSO4 and NiCl2 stock additions, and Modified Wolin's mineral solution as distinct formulation entries instead of summing repeated stock ingredients.
2. Encode Modified Wolin's mineral solution as its own solution recipe or rescale its components by the documented 1 ml/L addition and annotate every rescaled component with the dilution.
3. Remove the unresolved duplicate-sum values from both `ammonifex_degensii_medium.yaml` and the KOMODO `ammonifex_medium.yaml` wrapper, then regenerate `data/merge_yaml/merged/`.
4. Ground `NiCl2 x 6 H2O` to exact nickel chloride hexahydrate or leave the hydrate ungrounded if the packaged MIM label index still rejects the exact ChEBI term.
5. Replace `KNO3`'s legacy `mediaingredientmech_term` with a `mediaingredientmech_chebi_term` keyed to `CHEBI:63043`.

## Follow-up Checks

- Rerun `just validate data/normalized_yaml/bacterial/ammonifex_degensii_medium.yaml` and the no-project single-record schema/strict/term/reference checks after the maintained records are corrected.
- Rerun `just validate-media-variant-links`, `just verify-merges`, and `just audit-merge-freshness` after regenerating the merged outputs.
- Manually compare the regenerated Ammonifex page with DSMZ Medium 716 to confirm that the main solution, Fe/Ni stock additions, Modified Wolin's stock, dithiothreitol filtration, and 0.5 bar pressurization remain distinguishable.

## Additional Notes

- The generated `parent_media` points from the DSMZ canonical record to its exact KOMODO duplicate. That is harmless compared with the amount errors, but the merger should eventually drop exact-duplicate parent links when both endpoints have been collapsed into one generated record.
- `data/normalized_yaml/bacterial/TOGO_M2714_Ammonifex_Degensii_Medium.yaml` is an independent TOGO import of the same recipe name and should be reconciled only after the DSMZ/KOMODO owner is corrected.
