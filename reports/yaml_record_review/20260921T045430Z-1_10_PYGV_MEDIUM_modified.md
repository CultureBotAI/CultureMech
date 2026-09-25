# YAML Record Review: 1_10_pygv_medium_modified

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/1_10_PYGV_MEDIUM_modified.yaml`
- Started UTC: 20260921T045319Z
- Finished UTC: 20260921T045430Z
- Verdict: needs curation

## Target

| Field | Observed value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:000859` |
| Label | `1_10_pygv_medium_modified` |
| Original label | `1/10 PYGV MEDIUM modified` |
| Category | `bacterial` |
| Generated or maintained | Generated merge artifact under `data/merge_yaml/merged/`; future edits belong in `data/normalized_yaml/bacterial/1_10_pygv_medium_modified.yaml`, `data/normalized_yaml/bacterial/KOMODO_1398_1_10_PYGV_medium_modified.yaml`, their import/cocktail normalization, or merge regeneration |
| Merge owner | `merged_from: [1_10_pygv_medium_modified, KOMODO_1398_1_10_PYGV_medium_modified]` |
| Maintained owners | `data/normalized_yaml/bacterial/1_10_pygv_medium_modified.yaml`; `data/normalized_yaml/bacterial/KOMODO_1398_1_10_PYGV_medium_modified.yaml` |

This generated record is the Aug 6 merge of the direct DSMZ Medium 1398 import and a KOMODO record that states it copied DSMZ Medium 1398.

## Validation

Repository `just` entrypoints were blocked before target-specific validation because the project `uv` environment attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`.

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/1_10_PYGV_MEDIUM_modified.yaml` | Pass |
| Closed schema / strict | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/1_10_PYGV_MEDIUM_modified.yaml --out /private/tmp/1_10_PYGV_MEDIUM_modified.strict.tsv --workers 1 --quiet` | Pass; 1 file scanned, 0 files with `ERROR`, TSV at `/private/tmp/1_10_PYGV_MEDIUM_modified.strict.tsv` |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/1_10_PYGV_MEDIUM_modified.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass; 1 file validated, 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/1_10_PYGV_MEDIUM_modified.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass |
| Embedded curation history | Not checked | No focused embedded `MediaRecipe.curation_history` validator is documented for one merge record; `just validate-history` targets standalone files under `history/` |

## Identity and Grounding

The generated record correctly denotes DSMZ Medium 1398, `1/10 PYGV MEDIUM modified`, and the KOMODO `SOURCE_DUPLICATE` relationship is source-plausible because the KOMODO record cites DSMZ Medium 1398 and matches the DSMZ-derived signature.

The formulation is not correct yet:

- DSMZ 1398's final medium adds 75 ml `S I`, 75 ml `S II`, 10 ml `100x Vitamin solution`, and 0.5 ml `0.1% Resazurin`, then makes the volume up to 1 L.
- The Aug 6 generated merge still exposes the 100x vitamin stock components as final-medium ingredients.
- The Aug 7 `apply_cocktail_nesting.py` repair moved six vitamin rows under `100x Vitamin solution` in both normalized owners, but it left `Cobalamine` as a final-medium row and did not model `S I` or `S II` as stock solutions.
- The `Trypticase` ingredient is grounded to `CHEBI:78018`, whose OBO label is `dodecylphosphocholine`, not Trypticase.

## Evidence

Supported by inspected source text:

- The DSMZ PDF supports the medium identity, pH 7.0, Trypticase, 0.5 mg/L yeast extract, 1 g/L glucose, 0.3 mg/L L-cysteine HCl, the N2/Hungate preparation, and aseptic addition of a filter-sterilized vitamin solution.
- K2HPO4 is a real component of `S I`.
- KH2PO4, ammonium sulfate, NaCl, MgSO4 x 7 H2O, and CaCl2 x 2 H2O are real components of `S II`.
- Biotin, Cobalamine, Thiamine-HCl x 2 H2O, p-Aminobenzoic acid, Pyridoxine, Riboflavin, and Folic acid are real components of the 100x Vitamin solution.

Unsupported or malformed in the generated record:

- `S I`, `S II`, `0.1% Resazurin`, and `100x Vitamin solution` are missing as final-medium additions.
- The `S I`, `S II`, and vitamin ingredients are modeled as final-medium grams per liter instead of stock-solution composition.
- `Trypticase` has the wrong CHEBI grounding.
- `pH 7.0` is typed as a generic `MIX` preparation step.
- The DSMZ PDF URL is present only in free-text `notes`; there is no structured `references` block for `linkml-reference-validator` to resolve.

## Completeness

- The generated record is stale relative to both normalized owners: it does not include their Aug 7 `100x Vitamin solution` nesting.
- The normalized owners still lack `S I` and `S II` stock representations, keep `Cobalamine` outside the vitamin stock, and omit the make-up water row.
- Empty growth-evidence slots are acceptable for this imported provider recipe because the DSMZ PDF does not state an organism-specific growth observation.
- A gitignore-independent `rg --no-ignore --hidden` search over `data/normalized_yaml` and `data/merge_yaml/merged` for `CultureMech:000859`, `KOMODO_1398_1_10_PYGV_medium_modified`, `mediadive.medium:1398`, `komodo.medium:1398`, and `DSMZ_Medium1398` found only the expected direct DSMZ owner, KOMODO owner, their generated merge, and ID/catalog entries.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | `S I`, `S II`, and the 100x Vitamin solution are flattened into final-medium ingredients. | DSMZ 1398 adds 75 ml `S I`, 75 ml `S II`, and 10 ml `100x Vitamin solution`; the generated record lists each stock's internal components as top-level `G_PER_L` ingredients. | `data/normalized_yaml/bacterial/1_10_pygv_medium_modified.yaml`, `data/normalized_yaml/bacterial/KOMODO_1398_1_10_PYGV_medium_modified.yaml`, and the MediaDive/KOMODO stock-solution importer. |
| Blocker | The generated merge is stale relative to the Aug 7 normalized vitamin-stock repair. | Both normalized owners now have a `100x Vitamin solution` solution entry, but the Aug 6 generated artifact still lists Biotin, Thiamine-HCl x 2 H2O, p-Aminobenzoic acid, Pyridoxine, Riboflavin, and Folic acid as top-level final ingredients. | Regenerate `data/merge_yaml/merged/` after finishing the remaining normalized fixes. |
| Major | `Cobalamine` was omitted from the `100x Vitamin solution` nesting repair. | DSMZ puts Cobalamine in the 100x Vitamin solution; both normalized owners still keep `Cobalamine` as a top-level ingredient after the Aug 7 cocktail nesting pass moved the other six vitamin components. | Both normalized owners or `apply_cocktail_nesting.py` input matching. |
| Major | Trypticase is grounded to the wrong chemical concept. | The generated record maps `Trypticase` to `CHEBI:78018` / `dodecylphosphocholine`, which is not the casein digest ingredient named by DSMZ. | Both normalized owners or the ingredient grounding table. |
| Major | The final stock-addition volumes are missing. | The record has no final-medium rows for 75 ml `S I`, 75 ml `S II`, 10 ml `100x Vitamin solution`, or 0.5 ml `0.1% Resazurin`. | Both normalized owners. |
| Minor | The pH preparation action is mis-typed as `MIX`. | DSMZ states pH 7.0; the generated record stores a preparation step with `action: MIX` and `description: pH 7.0`. | `data/normalized_yaml/bacterial/1_10_pygv_medium_modified.yaml` or the MediaDive preparation-step importer. |
| Minor | Structured references are absent. | The DSMZ PDF URL is present only in `notes`; the generated file has no `references` block, so `linkml-reference-validator` performed zero checks. | Both normalized owners or their DSMZ/KOMODO import mapping. |

## Recommended Edits

1. Model `S I` and `S II` as stock solutions and replace their flattened top-level salts with 75 ml/L `S I` and 75 ml/L `S II` final additions.
2. Move `Cobalamine` under `100x Vitamin solution` and keep that stock added to the final medium at 10 ml/L.
3. Represent `0.1% Resazurin` as a 0.5 ml/L stock addition, or explicitly document the concentration conversion if preserving the final 0.0005 g/L amount.
4. Remove the stray `SII` top-level preparation step after `S II` is represented structurally.
5. Correct `Trypticase` grounding so it no longer points at `dodecylphosphocholine`.
6. Recode the pH 7.0 preparation step from `MIX` to a pH-specific action and add structured DSMZ references.
7. Regenerate `data/merge_yaml/merged/` and confirm the DSMZ and KOMODO records still coalesce as source duplicates.

## Follow-up Checks

- `just validate-strict data/normalized_yaml/bacterial/1_10_pygv_medium_modified.yaml data/normalized_yaml/bacterial/KOMODO_1398_1_10_PYGV_medium_modified.yaml` after normalized edits.
- `just validate-terms data/normalized_yaml/bacterial/1_10_pygv_medium_modified.yaml` after correcting `Trypticase`.
- `just validate-references data/normalized_yaml/bacterial/1_10_pygv_medium_modified.yaml` after adding a structured DSMZ reference.
- `just verify-merges` to prove the DSMZ and KOMODO generated outputs still coalesce after regeneration.
- `just validate-strict` and `just validate-terms` on the regenerated `1_10_PYGV_MEDIUM_modified.yaml` merge artifact.
- Manual comparison to DSMZ Medium 1398 for final volumes, `S I`, `S II`, 100x Vitamin solution, resazurin, make-up water, N2/Hungate preparation, and pH 7.0.

## Additional Notes

- `linkml-reference-validator` performed zero checks because the generated record has no `references` block.
