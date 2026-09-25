# YAML Record Review: ANAEROFILUM medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml
- Started UTC: 2026-09-21T12:36:40Z
- Finished UTC: 2026-09-21T12:37:15Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Path | `data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml` |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:006361` |
| Name | `anaerofilum_medium` |
| Source accession | `komodo.medium:719` |
| Source label | `ANAEROFILUM medium` |
| Generated status | Generated merge from `KOMODO_719_ANAEROFILUM_medium` and `anaerofilum_medium` |

The reviewed file is a generated merge rooted on the KOMODO Medium 719 duplicate. The maintained DSMZ/MediaDive parent is `data/normalized_yaml/bacterial/anaerofilum_medium.yaml`, and the maintained KOMODO child is `data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml`.

The exhaustive identity search used `rg --no-ignore --hidden` across `data/normalized_yaml`, `data/merge_yaml/merged`, `scripts`, `tests`, and `history` for the exact record labels, source accessions, file stem, and both CultureMech IDs. It found the generated merge, the two maintained normalized records, and generated index projections.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml` | Passed with no issues reported |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml --out /private/tmp/ANAEROFILUM_MEDIUM.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were available |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` recipe validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` inside one generated merge |

The documented `just` wrappers still fail before focused validation in this checkout because project `uv` resolves with Python 3.13 and attempts to build `llvmlite==0.46.0`, whose setuptools build aborts with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The no-project Python 3.11 commands above validate the generated record without building the project.

## Identity and Grounding

The generated root is a KOMODO duplicate of DSMZ Medium 719. `data/normalized_yaml/bacterial/anaerofilum_medium.yaml` keeps `CultureMech:006361` as a `SOURCE_DUPLICATE` child, and the generated merge preserves the duplicate relationship.

The generated KOMODO root omits the DSMZ pH 6.8-7.0 range even though its DSMZ parent carries that `ph_range`. Future regeneration should preserve the DSMZ condition on the exact duplicate projection.

Ingredient grounding is partly wrong or over-specific:

- `NiCl2 x 6 H2O` is grounded to anhydrous `CHEBI:34887` nickel dichloride.
- The DSMZ fatty-acid stock row `DL-2-Methylbutyric acid` is absent.
- The FeSO4 stock solvent is represented as 1000 g/L `H2SO4`, but DSMZ specifies 1000 ml of 0.1 N sulfuric acid, not neat sulfuric acid.

## Evidence

The generated record has no structured `references` or `source_data` object. It relies on its `notes`, source accession, curation history, and generated merge metadata for provenance, plus an unrelated LB Medium supplier note that is not evidence for DSMZ Medium 719.

I inspected `DSMZ_Medium719.pdf`. It supports:

- the direct KH2PO4, MgSO4 x 7 H2O, NaCl, NH4Cl, CaCl2 x 2 H2O, Yeast extract, Na-acetate, Na-formate, Sodium resazurin, NaHCO3, D-Glucose, L-Cysteine HCl x H2O, and Na2S x 9 H2O rows;
- a 2.00 ml/L FeSO4 x 7 H2O solution, not direct FeSO4 and H2SO4 rows;
- a 1.00 ml/L Trace element solution SL-10, not direct HCl through Na2MoO4 stock-component rows;
- a 20.00 ml/L Fatty acid mixture, not direct Isobutyric acid, Valeric acid, and Isovaleric acid rows at stock recipe volumes;
- the missing DL-2-Methylbutyric acid and distilled-water components inside the fatty-acid stock;
- base pH 6.8-7.0 and the four stored preparation steps.

The Tryptone 10.0 g/L, second Yeast extract 5.0 g/L, and Sodium chloride 10.0 g/L rows are not in DSMZ Medium 719. They are accompanied by LB Miller supplier notes and should not be attached to ANAEROFILUM MEDIUM.

## Completeness

The root label and duplicate relationship are coherent, and the generated record does keep the DSMZ preparation text from the maintained parent.

Consequential missing or malformed slots remain:

- no `ph_range` despite the DSMZ 6.8-7.0 complete-medium pH;
- no stock-solution boundary for Trace element solution SL-10;
- no stock-solution boundary for Fatty acid mixture;
- no stock-solution boundary for FeSO4 x 7 H2O solution;
- no DL-2-Methylbutyric acid in the fatty-acid stock;
- no base, SL-10, or fatty-acid-stock distilled-water rows;
- no explicit 1.00 ml/L SL-10, 20.00 ml/L fatty-acid-mixture, or 2.00 ml/L FeSO4-stock additions;
- unrelated LB Miller constituents are present as if they were direct DSMZ Medium 719 ingredients.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Three unrelated LB Miller constituents are injected into the ANAEROFILUM recipe. | DSMZ Medium 719 has no Tryptone, no extra 5 g/L Yeast extract row, and no 10 g/L Sodium chloride row. The generated YAML carries those rows with LB Miller supplier notes and repeats Yeast extract/Sodium chloride after the DSMZ rows. | `data/normalized_yaml/bacterial/anaerofilum_medium.yaml` and `data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml`, followed by merge regeneration |
| Major | Trace element solution SL-10 is flattened into final-medium ingredients at stock concentrations. | DSMZ adds 1.00 ml/L SL-10. The generated file stores HCl, FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, and Na2MoO4 x 2 H2O as direct final g/L ingredients. | Both normalized inputs and any source transform that flattened DSMZ Medium 320 stock components |
| Major | Fatty acid mixture is flattened, has the wrong unit boundary, and is incomplete. | DSMZ adds 20.00 ml/L of Fatty acid mixture and defines the stock as 23 ml Isobutyric acid, 27 ml DL-2-Methylbutyric acid, 27 ml Valeric acid, 27 ml Isovaleric acid, and 896 ml water. The generated file stores only three acids as direct G_PER_L rows and omits DL-2-Methylbutyric acid and water. | Both normalized inputs |
| Major | FeSO4 x 7 H2O solution is flattened and misrepresents its solvent. | DSMZ adds 2.00 ml/L of FeSO4 x 7 H2O solution and defines the stock as 1.00 g FeSO4 x 7 H2O in 1000 ml H2SO4 (0.1 N). The generated file stores 1 g/L FeSO4 and 1000 g/L sulfuric acid as direct ingredients. | Both normalized inputs |
| Major | The generated KOMODO-rooted exact duplicate drops the DSMZ pH range. | The maintained DSMZ parent has `ph_range` 6.8-7.0 and the DSMZ preparation text says to adjust complete medium to 6.8-7.0 before use. The generated merge has no `ph_range`. | Merge rule or canonical-root selection for exact DSMZ/KOMODO duplicates |
| Minor | Nickel chloride hexahydrate is grounded to anhydrous nickel dichloride. | The source ingredient is `NiCl2 x 6 H2O`; the generated row stores `CHEBI:34887` with label `nickel dichloride`. | Both normalized inputs, followed by merge regeneration |

## Recommended Edits

1. Remove the LB Miller Tryptone, second Yeast extract, and Sodium chloride commercial-product rows and the LB supplier note from both normalized ANAEROFILUM records.
2. Replace the flattened SL-10 rows with a 1.00 ml/L Trace element solution SL-10 addition and a stock-solution definition containing HCl (25%), FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, and 990 ml distilled water.
3. Replace the direct Isobutyric acid, Valeric acid, and Isovaleric acid rows with a 20.00 ml/L Fatty acid mixture addition and a stock solution containing Isobutyric acid, DL-2-Methylbutyric acid, Valeric acid, Isovaleric acid, and 896 ml distilled water by source volume.
4. Replace the direct FeSO4 and H2SO4 rows with a 2.00 ml/L FeSO4 x 7 H2O solution and a stock solution with 1.00 g FeSO4 x 7 H2O in 1000 ml 0.1 N H2SO4.
5. Ensure the regenerated KOMODO-rooted merge retains pH 6.8-7.0, either by changing canonical-root selection or by merging DSMZ conditions onto exact KOMODO duplicates.
6. Clear `CHEBI:34887` from `NiCl2 x 6 H2O` unless the packaged ingredient index has an exact nickel chloride hexahydrate term.

## Follow-up Checks

1. Run `just validate-schema`, `just validate-strict`, and `just validate-terms` on both edited normalized records.
2. Run `just verify-merges` and `just audit-merge-freshness` after regenerating `data/merge_yaml/merged/ANAEROFILUM_MEDIUM.yaml`.
3. Re-open the generated merge and manually verify that only the 13 DSMZ direct base ingredients remain direct, the three stock additions retain their addition volumes, no LB supplier metadata remains, and pH 6.8-7.0 is present.

## Additional Notes

Empty optional organism and growth-evidence fields are not defects here; this was a source-formulation review. The exact gitignore-independent search found no checked-in repair script for KOMODO/DSMZ Medium 719 analogous to the Medium 860 and Medium 516 topology repairs reviewed immediately before this record.
