# YAML Record Review: BACTEROIDES CELLULOSOLVENS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml
- Started UTC: 2026-09-21T18:18:21Z
- Finished UTC: 2026-09-21T18:18:21Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:005002 |
| Name | bacteroides_cellulosolvens_medium |
| Original name | BACTEROIDES CELLULOSOLVENS MEDIUM |
| Maintained canonical input | data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml |
| Merge participants | data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml; data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml; data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml |
| Primary checked source | DSMZ Medium 315 PDF |
| Generated status | Generated merge under data/merge_yaml/merged; future fixes belong in normalized inputs or the source/import and merge rules that produced them |

The generated merge is the KOMODO Medium 315 record for DSMZ Medium 315, merged with a DSMZ duplicate and a KOMODO variant named `315_replace_Cellobiose_with_Cellulose`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml` | Passed: `No issues found` |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml --out /private/tmp/BACTEROIDES_CELLULOSOLVENS_MEDIUM.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 ERROR rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 1 file validated, 0 checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not checked | No focused embedded `MediaRecipe.curation_history` validator is documented; `just validate-history` targets standalone `history/` files. |

The repository `just validate-schema`, `just validate-strict`, `just validate-terms`, and `just validate-references` wrappers were not used for this target because the project environment currently fails while syncing the Python 3.13 dependency set. The equivalent no-project validators above ran against the checked-in schema and target file.

## Identity and Grounding

The canonical KOMODO 315 and DSMZ 315 records identify the same DSMZ source medium. The DSMZ PDF for Medium 315 is labeled `BACTEROIDES CELLULOSOLVENS MEDIUM`, lists the same direct salts, pH 7.0, 5 g/L cellobiose, and 1 L of distilled water, and supplies trace-element and vitamin stock recipes that the maintained inputs attempted to inline.

The generated record does not currently identify the source formulation exactly:

- The DSMZ record adds 10 ml/L trace-element solution and 10 ml/L vitamin solution. Their internal ingredients are stock-solution ingredients, not direct final-medium ingredients.
- The `bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml` input has a source ID and name that promise a cellobiose-to-cellulose replacement, but its composition still contains 5 g/L `Cellobiose` and no cellulose.
- The generated synonym for `bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose` therefore describes an unsupported cellulose variant, while the merge records the variant as an exact source duplicate of the canonical record.
- `NiCl2 x 6 H2O` is grounded to `CHEBI:34887` / nickel dichloride. DSMZ specifies the hexahydrate, so an anhydrous salt term is a broader near match rather than an exact supplied chemical form.

## Evidence

The following main-medium rows are supported by DSMZ 315 as direct ingredients in the one-liter medium: 0.68 g NH4Cl, 0.30 g K2HPO4, 0.18 g KH2PO4, 0.15 g `(NH4)2SO4`, 0.12 g `MgSO4 x 7 H2O`, 0.06 g `CaCl2 x 2 H2O`, 0.02 g `FeSO4 x 7 H2O`, 5 g cellobiose for the canonical variant, 1 mg resazurin, 2 g NaHCO3, 0.25 g `Cysteine-HCl x H2O`, and 0.25 g `Na2S x 9 H2O`.

The generated trace-element and vitamin rows are not supported as final-medium gram-per-liter rows. DSMZ lists them under separate `Trace element solution` and `Vitamin solution` recipes, then adds 10 ml of each stock to the main medium. Copying the stock values to top-level `G_PER_L` rows inflates each stock component by 100-fold if interpreted as a final concentration.

The `MgSO4 x 7 H2O`, `CaCl2 x 2 H2O`, and `FeSO4 x 7 H2O` rows further sum chemically identical labels across the main recipe and the trace-element stock. Their current values, 3.12, 0.16, and `0.12000000000000001` g/L, are the arithmetic sums of DSMZ's main-medium grams and stock-recipe grams before the 10 ml/L stock dilution is applied.

The generated file contains no independent citation or evidence object for a cellulose variant. Its only evidence for the variant is local provenance showing that the DSMZ resolver copied DSMZ Medium 315 into a KOMODO source record named `315_replace_Cellobiose_with_Cellulose`.

## Completeness

- DSMZ Medium 315 includes 1000 ml distilled water in the main medium; the generated record omits water entirely.
- DSMZ also includes 1000 ml distilled water in both the trace-element and vitamin stock recipes; those solution boundaries and stock water rows are absent because the record flattened both stocks into the parent ingredient list.
- The generated record lost all three DSMZ preparation statements preserved by `data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml`: adjust pH 7.0 and use an 80% N2 / 20% CO2 gas atmosphere, filter-sterilize cellobiose separately, and prepare the trace-element solution by dissolving nitrilotriacetic acid before pH adjustment and mineral addition.
- The generated `notes` field still says `Aerobic: Yes`, but DSMZ Medium 315 specifies an N2/CO2 gas atmosphere for this formulation.
- Empty organism, strain, growth-outcome, and publication-evidence fields are not automatically defects in this source-derived recipe because DSMZ 315 itself is a medium protocol, not a growth paper.

A gitignore-independent search of `reports/yaml_record_review` for `BACTEROIDES_CELLULOSOLVENS_MEDIUM|bacteroides_cellulosolvens_medium` found no existing report for this target before this report was written.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | Trace-element and vitamin stock recipes are flattened into the parent final medium at stock strength. | DSMZ adds 10 ml trace-element solution and 10 ml vitamin solution to the medium, then separately defines each stock per 1000 ml. The generated top-level rows include stock grams-per-liter values such as 1.5 g/L nitrilotriacetic acid and 0.002 g/L biotin as if they were final-medium values. | The DSMZ/KOMODO import and normalization path that builds `data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml`, `data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml`, and `data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml` |
| Major | Duplicate merging summed main-medium salts with stock-solution salts. | DSMZ has main-medium `MgSO4 x 7 H2O` 0.12 g and trace-stock `MgSO4 x 7 H2O` 3 g; the record reports 3.12 g/L. The same stock-boundary loss produced 0.16 g/L calcium chloride dihydrate and `0.12000000000000001` g/L ferrous sulfate heptahydrate. | Normalized records plus the duplicate-ingredient cleanup that collapsed rows with the same label before solution structure was preserved |
| Major | The cellulose variant has the wrong ingredient and is falsely merged away. | `data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml` is named and sourced as a replacement of cellobiose with cellulose, but it still contains the 5 g/L Cellobiose row copied from DSMZ 315. The generated canonical file lists that variant as a `SOURCE_DUPLICATE`. | KOMODO variant importer or DSMZ resolver rules for generated replacement variants |
| Major | Preparation and anaerobic gas conditions are lost in the generated record. | DSMZ 315 states pH 7.0, an N2/CO2 gas atmosphere, separate filter sterilization of cellobiose, and a trace-solution pH/mineral order. Only the DSMZ normalized duplicate has these `preparation_steps`; the generated KOMODO canonical has none. | Merge canonicalization should preserve preparation steps from exact DSMZ duplicates, or the KOMODO normalized source should be enriched with the DSMZ steps it cites |
| Major | Distilled water is missing from the main and stock recipes. | DSMZ lists distilled water at 1000 ml for the main medium and for both stocks, but the generated ingredient list has no water row and no stock subrecipes where stock water could live. | DSMZ/KOMODO import and stock-solution representation |
| Major | `NiCl2 x 6 H2O` is over-broadly grounded. | The source and row name specify nickel chloride hexahydrate, but the CHEBI link is anhydrous `CHEBI:34887` / nickel dichloride. Hydration is identity-significant for supplied media ingredients. | Ingredient grounding for the normalized source records, using the packaged MIM/CHEBI label index |
| Minor | The `FeSO4 x 7 H2O` summed value leaked floating-point presentation. | The generated value is `0.12000000000000001` rather than a source amount or a clean decimal. | Duplicate merge or YAML emission for normalized and generated ingredient concentrations |

## Recommended Edits

1. In the maintained normalized inputs or their DSMZ/KOMODO importers, model `Trace element solution` and `Vitamin solution` as stock solution references added at 10 ml/L, with their DSMZ-listed ingredient rows nested under the stock recipes rather than copied as parent ingredients.
2. Remove the pre-dilution sums for `MgSO4 x 7 H2O`, `CaCl2 x 2 H2O`, and `FeSO4 x 7 H2O`; keep the main-medium grams separate from the trace-stock grams, or compute final flattened stock contributions only after the 10 ml/L dilution is explicit.
3. Fix `data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium_replace_cellobiose_with_cellulose.yaml` so the source-specific replacement actually uses 5 g/L cellulose, not 5 g/L cellobiose, or suppress the local variant if the KOMODO source cannot support it.
4. Preserve the DSMZ preparation details in whichever normalized record is selected as the merge canonical: final pH 7.0, N2/CO2 atmosphere, separate filter sterilization of cellobiose, and the trace-element stock preparation order and pH adjustments.
5. Add distilled water to the main medium and to both stock recipes in the maintained representation.
6. Resolve `NiCl2 x 6 H2O` to an exact hexahydrate term when one exists in the packaged ingredient index, or leave it explicitly ungrounded with a quality flag instead of using anhydrous nickel dichloride.
7. Regenerate `data/merge_yaml/merged/BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml` and generated pages; do not patch the generated merge directly.

## Follow-up Checks

- Rerun the open-schema, strict, reference, and term validators on each edited normalized input and on the regenerated `data/merge_yaml/merged/BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml`.
- Rerun `just verify-merges` and `just audit-merge-freshness` after regeneration to prove the canonical merge reflects the normalized owners.
- Inspect the regenerated record for stock solution references before checking ingredient arithmetic; the absence of `[Merged 2 duplicates: 0.12, 3.0]`, `[Merged 2 duplicates: 0.06, 0.1]`, and `[Merged 2 duplicates: 0.02, 0.1]` should be required but is not sufficient on its own.
- Manually compare the regenerated cellulose variant against DSMZ 315 and the KOMODO variant identity to confirm only the carbon source differs.
- Re-run the `NiCl2 x 6 H2O` label through the packaged MediaIngredientMech label index rather than a fresh fuzzy resolver, then run term validation to verify the final CURIE and label.

## Additional Notes

- This review intentionally reports defects in `data/merge_yaml/merged/BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml` against their maintained normalized owners. The generated merge and rendered pages should be regenerated only after the normalized source recipes or import rules are corrected.
- A gitignore-independent `find` over `data/normalized_yaml` located the three normalized merge participants under `data/normalized_yaml/bacterial/`.
- The KOMODO canonical and the KOMODO cellulose-replacement input both lack DSMZ preparation steps before merge; the DSMZ duplicate has those steps, so this is a merge-preservation problem as well as a source-enrichment gap.
