# YAML Record Review: am5_medium_elusimicrobium_medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/am5_medium_elusimicrobium_medium.yaml`
- Started UTC: 2026-09-21T11:18:16Z
- Finished UTC: 2026-09-21T11:18:58Z
- Verdict: needs curation

## Target

| Field | Observed value |
| --- | --- |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:001186` |
| Name | `am5_medium_elusimicrobium_medium` |
| Original name | `AM5 MEDIUM (ELUSIMICROBIUM MEDIUM)` |
| Source identity | DSMZ Medium 1705, `mediadive.medium:1705` |
| Generated status | Generated one-source merge |
| Generated path | `data/merge_yaml/merged/am5_medium_elusimicrobium_medium.yaml` |
| Maintained input | `data/normalized_yaml/bacterial/am5_medium_elusimicrobium_medium.yaml` |

The generated file is a one-source merge and matches the normalized owner. The concentration errors are already present in the maintained normalized record.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/am5_medium_elusimicrobium_medium.yaml` | Passed; no issues found. |
| Strict | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/am5_medium_elusimicrobium_medium.yaml --out /private/tmp/am5_medium_elusimicrobium_medium.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned and 0 `ERROR` rows emitted. |
| Reference | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/am5_medium_elusimicrobium_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed. |
| Term | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/am5_medium_elusimicrobium_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Documented focused validator | Not checked: no focused embedded `MediaRecipe.curation_history` validator is documented for one merged record; `just validate-history` targets standalone files under `history/`. |

The documented `just validate-schema`, `just validate-strict`, and `just validate-terms` entrypoints are unavailable in this checkout because project `uv` attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools before target-specific validation. The no-project commands above exercise the same schema and validation code with Python 3.11.

## Identity and Grounding

The record's stable ID, name, and source accession agree with DSMZ Medium 1705:

- `id: CultureMech:001186`
- `name: am5_medium_elusimicrobium_medium`
- `media_term.term.id: mediadive.medium:1705`
- `notes: Source: DSMZ | Link: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1705.pdf`

The ingredient model does not agree with the source. DSMZ 1705 defines a basal medium plus many named stock solutions added at fixed volumes. The CultureMech record flattens stock ingredients into top-level final-medium ingredients and sums several stock solvent or buffer rows with true final-medium rows:

- `NaHCO3` is `202.52021 G_PER_L` with duplicate parts `2.52021, 100.0, 100.0`.
- `NaOH` is `300.5 G_PER_L` with duplicate parts `0.5, 100.0, 100.0, 100.0`.
- The trace-element stock's `FeCl2 x 4 H2O` is present as `2 G_PER_L` even though only 1 ml/L of that stock is added.

Most exact chemical forms are grounded, but `NiCl2 x 6 H2O` is grounded to anhydrous `CHEBI:34887`, and several aromatic fatty-acid rows still carry legacy `mediaingredientmech_term` IDs instead of `mediaingredientmech_chebi_term`.

## Evidence

Inspected source documents:

- DSMZ Medium 1705 PDF, fetched from `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1705.pdf` and converted to text with `mutool draw -F txt`

Supported claims:

- DSMZ supports the AM5 / Elusimicrobium identity, the pH 7.1-7.2 final adjustment, the N2/CO2 4:1 gas stream, butyl-stopper sealing, and filtration if insoluble residues remain.
- DSMZ supports the basal salts: 1 g NaCl, 0.5 g KCl, 0.4 g MgCl2 x 6 H2O, 0.1 g CaCl2 x 2 H2O, 0.3 g NH4Cl, 0.2 g KH2PO4, and 0.4 mg resazurin in 900 ml distilled water.
- DSMZ supports adding 30 ml 1 M NaHCO3, 10 ml 500 mM D-glucose, 10 ml 100 mM cysteine, 10 ml 10% yeast extract, 2 ml 10% casamino acids, 4 ml 250 mM dithiothreitol, and 1 ml/L each of the trace-element, selenite-tungstate, vitamin, fatty-acid, menadione, and lipoic-acid stock solutions.

Unsupported or mismatched claims:

- DSMZ never lists top-level 202.52021 g/L NaHCO3 or 300.5 g/L NaOH concentrations; those are sums of independent final amounts and stock make-up reagents.
- DSMZ does not list LB Medium or its tryptone, yeast-extract, and sodium-chloride subcomposition as part of AM5.
- DSMZ includes alpha-Methylbutyric acid in the branched-chain fatty acids solution, but the CultureMech record omits it.
- DSMZ's trace-element and vitamin stock ingredients are all downstream of 1 ml/L stock additions; the CultureMech record treats most of the stock-strength mg/L rows as final-medium g/L rows.
- The `preparation_steps` text ends the anaerobic addition instruction with a colon and never enumerates the stock solutions to add.

## Completeness

Consequential gaps:

- Named DSMZ stock solutions are absent as `solutions`.
- NaHCO3, NaOH, trace salts, vitamins, fatty acids, menadione, and lipoic acid need stock-aware final concentration modeling.
- The unrelated LB Medium supplier enrichment injected tryptone, a duplicate yeast-extract row, and a duplicate sodium-chloride row.
- Alpha-Methylbutyric acid is missing from the branched-chain fatty acids solution.
- The anaerobic addition list and stock-solution recipes are missing from the preparation model.
- Target organisms are absent; no focused growth-evidence search was performed during this review.

Empty optional slots correctly left empty:

- No target organism was asserted, so there is no unsupported growth claim.
- No storage condition was asserted by DSMZ.

Bounded absence checks:

- A gitignore-independent `find reports/yaml_record_review -maxdepth 1 -type f -name '*am5_medium_elusimicrobium_medium.md'` search found no pre-existing report for this generated record before this report was written.
- A gitignore-independent `rg --no-ignore --hidden` search over `data`, `src`, `scripts`, `history`, and `reports/yaml_record_review` for `am5_medium_elusimicrobium_medium`, `AM5 MEDIUM`, `ELUSIMICROBIUM`, `Elusimicrobium`, and `Elusimicrobia` found the DSMZ 1705 owner plus related modified AM5 and Elusimicrobium minutum records.
- A gitignore-independent exact search for `alpha-Methylbutyric`, `Methylbutyric`, `methylbutyric`, and `Alpha` inside this generated AM5 record and its normalized owner found no row for DSMZ's alpha-Methylbutyric acid.

## Findings

### Blocker

1. **DSMZ stock solutions were flattened into the final medium and duplicate-merged, making the composition chemically impossible.**

   Evidence: DSMZ lists 30 ml of 1 M NaHCO3 solution per liter, a 1 ml/L selenite-tungstate solution containing 0.5 g NaOH in 1000 ml, 1 ml/L folic acid and menadione solutions made in 10 mM NaHCO3, a 1 ml/L aromatic fatty acids solution made up to 100 ml with 20 mM NaOH, a 1 ml/L lipoic-acid solution made up to 100 ml with 1 mM NaOH, and a 1 ml/L branched-chain fatty acids solution made up to 100 ml with 0.1 N NaOH. The CultureMech record instead reports `NaHCO3` at 202.52021 g/L and `NaOH` at 300.5 g/L, with notes showing duplicate parts of `100.0`.

   Owner: re-curate `data/normalized_yaml/bacterial/am5_medium_elusimicrobium_medium.yaml` with explicit stock `solutions`, remove summed stock-solvent rows from the final ingredient list, and regenerate `data/merge_yaml/merged/`.

### Major

1. **Trace, vitamin, fatty-acid, menadione, and lipoic-acid stock components are at the wrong dilution layer.**

   Evidence: DSMZ adds the trace-element, selenite-tungstate, 7-vitamin, folic-acid, riboflavin, branched-chain fatty-acid, aromatic fatty-acid, menadione, and lipoic-acid solutions at 1 ml/L. The generated record lists stock components such as `FeCl2 x 4 H2O: 2 G_PER_L`, `Na2-EDTA: 5.2 G_PER_L`, `Vitamin B12: 0.0027972 G_PER_L`, and `Menadione: 0.027972 G_PER_L` as direct final-medium concentrations.

   Owner: model each named DSMZ solution under `solutions` with its stock recipe and a 1 ml/L addition.

2. **Unrelated LB Medium composition was injected into AM5.**

   Evidence: the CultureMech notes add an LB Medium supplier/product paragraph, and the ingredient list contains `Tryptone: 10.0 G_PER_L`, `Yeast extract: 5.0 G_PER_L`, and `Sodium chloride: 10.0 G_PER_L` with LB supplier metadata. DSMZ 1705 does not list LB Medium; it only adds 10 ml of 10% yeast extract as an AM5 stock and already has 1 g NaCl in the basal recipe.

   Owner: remove LB product decomposition from this normalized record and restrict commercial-product expansion so an unrelated LB formulation cannot be added to DSMZ AM5.

3. **DSMZ alpha-Methylbutyric acid is missing.**

   Evidence: DSMZ's branched-chain fatty acids solution lists valeric acid, isovaleric acid, alpha-Methylbutyric acid, and isobutyric acid. The CultureMech record has valeric, isovaleric, and isobutyric acid only; an ignored-inclusive exact search found no alpha-Methylbutyric acid row in the normalized or generated AM5 YAML.

   Owner: add alpha-Methylbutyric acid to the branched-chain fatty acids solution in the normalized AM5 owner.

4. **The preparation text truncates the anaerobic stock-addition list.**

   Evidence: step 1 says to add anaerobically "the following solutions:" and then stops. DSMZ lists NaHCO3, D-glucose, cysteine, yeast-extract, casamino-acid, dithiothreitol, trace-element, selenite-tungstate, 7-vitamin, folic-acid, riboflavin, branched-chain fatty-acid, aromatic fatty-acid, menadione, and lipoic-acid additions before the pH adjustment.

   Owner: encode those stock additions either as complete `solutions` or as preparation substeps in the maintained AM5 owner.

5. **Several exact ingredient groundings are stale or incomplete.**

   Evidence: `NiCl2 x 6 H2O` points to anhydrous nickel dichloride, and phenyl acetic acid, phenyl propionic acid, 4-hydroxyphenyl acetic acid, and 3-indolyl acetic acid still use legacy `mediaingredientmech_term` IDs.

   Owner: rerun exact-form ingredient enrichment after stock solution curation, preserving hydrated salt specificity.

### Minor

None found.

## Recommended Edits

1. Rebuild `data/normalized_yaml/bacterial/am5_medium_elusimicrobium_medium.yaml` from DSMZ Medium 1705 with the basal medium plus explicit stock `solutions`.
2. Remove summed `NaHCO3` and `NaOH` stock-solvent rows from the top-level ingredient list.
3. Move all trace-element, selenite-tungstate, vitamin, branched-chain fatty-acid, aromatic fatty-acid, menadione, and lipoic-acid rows into named stock solutions added at 1 ml/L.
4. Delete the unrelated LB Medium commercial decomposition and keep only DSMZ's 10 ml 10% yeast-extract stock addition.
5. Add the missing alpha-Methylbutyric acid to the branched-chain fatty acids solution.
6. Complete preparation steps so all anaerobic stock additions, pH adjustment, N2/CO2 atmosphere, butyl-stopper sealing, and optional filtration are represented.
7. Correct nickel chloride hexahydrate and legacy aromatic-acid MediaIngredientMech groundings.
8. Regenerate generated merge records and rendered products.

## Follow-up Checks

- Rerun schema, strict, reference, and term validators on the corrected normalized AM5 record and regenerated output.
- Rerun concentration plausibility and confirm the `TRACE_SALT_AS_STOCK` FeCl2 row and the NaHCO3/NaOH merged-duplicate rows for AM5 disappear.
- Manually diff the regenerated stock solution list against DSMZ Medium 1705.
- Inspect the rendered AM5 page and confirm that stock solutions are nested, not displayed as full-strength final-medium ingredients.

## Additional Notes

- This review is read-only. It intentionally leaves `data/merge_yaml/merged/am5_medium_elusimicrobium_medium.yaml`, its normalized owner, and generated pages unchanged.
- Generated files under `data/merge_yaml/merged/` are derived artifacts. Corrections belong in `data/normalized_yaml/bacterial/am5_medium_elusimicrobium_medium.yaml` and the importer/enrichment logic that flattened DSMZ stock recipes and injected the unrelated LB composition.
