# YAML Record Review: psychrilyobacter_sp_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/psychrilyobacter_sp_medium.yaml
- Started UTC: 2026-09-24T22:03:51Z
- Finished UTC: 2026-09-24T22:04:22Z
- Verdict: needs curation

## Target

- Reviewed generated `MediaRecipe`: `data/merge_yaml/merged/psychrilyobacter_sp_medium.yaml`
- Stable ID: `CultureMech:001517`
- Label: `psychrilyobacter_sp_medium`
- Original label: `PSYCHRILYOBACTER SP. MEDIUM`
- Category: `bacterial`
- Source grounding: DSMZ Medium 408, `mediadive.medium:408`
- Merge provenance: generated from `data/normalized_yaml/bacterial/psychrilyobacter_sp_medium.yaml` and `data/normalized_yaml/bacterial/py_glutamate_medium.yaml`
- Maintained owner paths for future fixes:
  - `data/normalized_yaml/bacterial/psychrilyobacter_sp_medium.yaml`
  - `data/normalized_yaml/bacterial/py_glutamate_medium.yaml`
  - the MediaDive and KOMODO import or DSMZ-enrichment paths if regenerated normalized records would overwrite direct edits

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/psychrilyobacter_sp_medium.yaml` | Passed; exited 0 with `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/psychrilyobacter_sp_medium.yaml --out /private/tmp/psychrilyobacter_sp_medium.strict.tsv --workers 1 --quiet` | Passed; the TSV at `/private/tmp/psychrilyobacter_sp_medium.strict.tsv` had 1 header row and 0 error rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/psychrilyobacter_sp_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 checks. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/psychrilyobacter_sp_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the usual `eutils` `pkg_resources` warning. |
| Embedded history | Not run | Not checked: the repository exposes `just validate-history` for standalone `history/` files, not for `MediaRecipe.curation_history` embedded in merged YAML. |

## Identity and Grounding

- The canonical record identity matches the cited DSMZ source. The DSMZ PDF at the record's `DSMZ_Medium408.pdf` URL is titled `408: PSYCHRILYOBACTER SP. MEDIUM`, and the record's `media_term` is `mediadive.medium:408` with the same source label.
- The KOMODO child is not an independent formula. `data/normalized_yaml/bacterial/py_glutamate_medium.yaml` is `komodo.medium:408`, cites `DSMZ Medium: 408`, and has DSMZ resolver history saying its ingredients were copied from DSMZ Medium 408.
- An ignored-file-inclusive search over `data/**/*.yaml` for `mediadive.medium:408`, `DSMZ_Medium408`, `DSMZ, ID: 408`, `komodo.medium:408`, `psychrilyobacter_sp_medium`, and `py_glutamate_medium` found only the generated merge, the direct DSMZ normalized record, and the KOMODO normalized duplicate.

## Evidence

- Supported directly by DSMZ Medium 408:
  - Main-medium additions of 10 g peptone, 3 g yeast extract, 10 g casamino acids, 20 g L-glutamic acid, 2 g NH4Cl, 2 g K2HPO4 x 3 H2O, 25 g NaCl, 0.50 ml sodium resazurin at 0.1% w/v, 0.50 g L-cysteine HCl x H2O, and 1000 ml distilled water.
  - A 10.00 ml addition of Modified Wolin's mineral solution per liter of main medium.
  - Boiling and cooling under 100% N2, adding cysteine before final pH adjustment to pH 7.0, dispensing under 100% N2 into anoxic Hungate-type tubes or serum vials, and autoclaving.
  - Modified Wolin's mineral solution from medium 141 with its own 1000 ml distilled water, nitrilotriacetic acid adjusted first to pH 6.5 with KOH, minerals added after that, and final stock pH adjusted to 7.0 with KOH.
- Unsupported by DSMZ Medium 408:
  - `NaCl` as `26.0 G_PER_L` in the final medium. DSMZ has 25 g/L NaCl in the main medium and 1 g/L NaCl inside a 10 ml/L Modified Wolin's mineral stock, so the stock contributes only 0.01 g/L NaCl to the final medium.
  - Full-strength Modified Wolin's mineral solution components as direct final-medium `G_PER_L` ingredients. For example, DSMZ specifies 1.50 g nitrilotriacetic acid and 3.00 g MgSO4 x 7 H2O in 1000 ml of stock, then only 10 ml of that stock per liter of final medium.
  - Missing explicit `Distilled water` ingredients for both the main 1000 ml medium and the 1000 ml Modified Wolin's mineral solution stock.

## Completeness

- Empty optional organism, growth, and literature slots are not defects for this imported medium recipe.
- The generated merge is complete enough to recover the DSMZ source accession and duplicate KOMODO accession, but it is not complete enough to make the source protocol reproducible because it collapses a 10 ml/L nested stock solution into final-medium ingredients.
- The ignored-file-inclusive `rg --no-ignore --hidden` searches described above covered YAML records under `data/`; they found no additional DSMZ 408 or KOMODO 408 owners beyond the direct normalized records and this generated merge.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Modified Wolin's mineral solution is flattened at stock strength instead of represented as a 10 ml/L stock addition. | DSMZ Medium 408 adds `Modified Wolin's mineral solution` at 10.00 ml per 1000 ml final medium, then separately defines the stock in 1000 ml water. The generated final medium lists stock components directly as `G_PER_L`, which inflates each stock-only component 100-fold. | `data/normalized_yaml/bacterial/psychrilyobacter_sp_medium.yaml`, `data/normalized_yaml/bacterial/py_glutamate_medium.yaml`, or their import/enrichment path |
| Major | Main and stock `NaCl` were summed as duplicate final-medium ingredients. | DSMZ has 25.00 g NaCl in the main recipe and 1.00 g NaCl in 1000 ml of Modified Wolin's mineral stock. At a 10 ml/L stock dose, the final stock-derived NaCl is 0.01 g/L, not 1 g/L, and it should remain inside the stock boundary. | `data/normalized_yaml/bacterial/psychrilyobacter_sp_medium.yaml`, `data/normalized_yaml/bacterial/py_glutamate_medium.yaml`, or their import/enrichment path |
| Minor | The 0.50 ml sodium resazurin stock addition has been converted to an equivalent final `0.0005 G_PER_L` amount and the source's 0.1% w/v stock form is lost. | A 0.50 ml/L addition of 0.1% w/v resazurin is dimensionally equivalent to 0.0005 g/L, but DSMZ supplies it as a solution addition. | `data/normalized_yaml/bacterial/psychrilyobacter_sp_medium.yaml`, `data/normalized_yaml/bacterial/py_glutamate_medium.yaml`, or their import/enrichment path |

## Recommended Edits

1. Rework the maintained DSMZ 408 and KOMODO 408 normalized records so the main recipe carries 25 g/L NaCl and a 10 ml/L reference to a child `Modified Wolin's mineral solution (from medium 141)` record, rather than full-strength stock ingredients.
2. Move nitrilotriacetic acid, MgSO4 x 7 H2O, MnSO4 x H2O, NaCl, FeSO4 x 7 H2O, CoSO4 x 7 H2O, CaCl2 x 2 H2O, ZnSO4 x 7 H2O, CuSO4 x 5 H2O, AlK(SO4)2 x 12 H2O, H3BO3, Na2MoO4 x 2 H2O, NiCl2 x 6 H2O, Na2SeO3 x 5 H2O, and Na2WO4 x 2 H2O into that stock solution at the concentrations DSMZ gives per 1000 ml stock.
3. Preserve the two distinct distilled-water volumes and attach the "First dissolve nitrilotriacetic acid..." pH procedure to the Modified Wolin stock rather than to the final Psychrilyobacter medium.
4. Consider preserving sodium resazurin as a 0.50 ml/L addition of 0.1% w/v solution if the representation supports solution additions for this imported class; otherwise leave the mathematically equivalent 0.0005 g/L final amount with a source-form note.
5. Regenerate `data/merge_yaml/merged/psychrilyobacter_sp_medium.yaml` after the maintained normalized records are repaired.

## Follow-up Checks

- Re-run the schema, strict, reference, and term validators against the regenerated merged record.
- Manually compare the regenerated ingredient list with DSMZ Medium 408 and confirm that the final medium has 25 g/L direct NaCl plus a 10 ml/L Modified Wolin stock reference, not a merged 26 g/L NaCl ingredient.
- Confirm that `data/merge_yaml/merged/psychrilyobacter_sp_medium.yaml` still merges the DSMZ and KOMODO source duplicates after the stock representation changes.

## Additional Notes

- `https://mediadive.dsmz.de/rest/medium/408` returned an empty response during this review, so the source comparison used the DSMZ PDF linked from the record itself.
