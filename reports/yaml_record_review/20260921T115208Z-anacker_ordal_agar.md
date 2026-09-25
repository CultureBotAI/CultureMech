# YAML Record Review: ANACKER-ORDAL AGAR

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/anacker_ordal_agar.yaml
- Started UTC: 2026-09-21T11:50:48Z
- Finished UTC: 2026-09-21T11:52:08Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:003553 |
| Source | komodo.medium:1039 |
| DSMZ source | mediadive.medium:1039 |
| Generated path | data/merge_yaml/merged/anacker_ordal_agar.yaml |
| Maintained owner | data/normalized_yaml/bacterial/KOMODO_1039_ANACKER-ORDAL_AGAR.yaml |
| Merge fingerprint | de9cb528e52a2b56a47d0208195782affa0381c95d7aa080c401e5abe9149e3d |
| Merge source | KOMODO_1039_ANACKER-ORDAL_AGAR.yaml |

`data/merge_yaml/merged/anacker_ordal_agar.yaml` is a generated singleton merge from the KOMODO 1039 normalized owner. KOMODO 1039 cites DSMZ Medium 1039, but this record has not been linked as a source duplicate of `data/normalized_yaml/bacterial/anacker_ordal_agar.yaml`.

## Validation

| Check | Result |
| --- | --- |
| Open schema | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/anacker_ordal_agar.yaml` under the cached Python 3.11 no-project environment. |
| Strict schema | Passed with `scripts/validate_strict.py data/merge_yaml/merged/anacker_ordal_agar.yaml --workers 1 --quiet`; the TSV contained 0 ERROR rows. |
| Reference validator | Passed with `linkml-reference-validator validate data ...`; no reference checks were emitted for this file. |
| Term validator | Passed with `linkml-term-validator validate-data ... --labels -c conf/oak_config.yaml`. |
| Embedded curation history | Not checked: this repository exposes `just validate-history` for standalone records under `history/`; no documented focused validator targets embedded `MediaRecipe.curation_history` inside one merge record. |

The project-level `just validate-schema`, `just validate-strict`, and `just validate-terms` routes were not usable for this target because project installation currently attempts to build `llvmlite==0.46.0` on Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The equivalent LinkML validators passed through an offline `uv run --no-project` invocation against `/usr/local/bin/python3.11`.

## Identity and Grounding

- The stable CultureMech ID, `komodo.medium:1039`, and merge fingerprint identify the KOMODO copy of DSMZ Medium 1039, ANACKER-ORDAL AGAR.
- A gitignore-independent search across `data`, `src`, `scripts`, `history`, `conf`, `reports`, `.claude`, `justfile`, and `CLAUDE.md` found the current KOMODO owner and a separate DSMZ/MediaDive owner at `data/normalized_yaml/bacterial/anacker_ordal_agar.yaml`; older `DSMZ_1039_ANACKER-ORDAL_AGAR.yaml` names appear only in archived validation reports.
- The inspected DSMZ Medium 1039 PDF supports the medium identity, pH 7.2, solid agar state, and six material rows: Tryptone peptone 0.5 g, Yeast extract 0.5 g, Na-acetate 0.2 g, Meat extract 0.2 g, Agar 11.0 g, and Tap water 1000.0 ml.
- The exact simple ingredient groundings for sodium acetate and agar are supported.
- The undefined complex rows, `Tryptone peptone` and `Meat extract`, are explicit and ungrounded, which is preferable to a forced narrow chemical identity.

## Evidence

- The KOMODO owner and generated merge carry the DSMZ 1039 pH and all six DSMZ rows at the same numeric values.
- `Tap water` is a final volume of 1000.0 ml in DSMZ 1039; the record imports it as `1000 G_PER_L`, which presents the solvent volume as a solute concentration.
- `KOH` appears only in the DSMZ instruction to adjust to pH 7.2 prior to autoclaving with KOH. The generated record turns it into an ingredient with `value: variable`, `unit: VARIABLE`.
- The DSMZ instruction to use indicator paper, not a pH electrode, is present in the separate DSMZ/MediaDive normalized owner but absent from this KOMODO owner and generated record.

## Completeness

- Consequentially incomplete: preparation details from DSMZ 1039 were not carried into the KOMODO 1039 owner or this generated record.
- Consequentially incorrect: tap water and KOH are modeled as ingredient concentrations even though DSMZ uses them as final volume and pH-adjustment context.
- Consequentially incomplete: the KOMODO 1039 owner explicitly cites DSMZ 1039 but is not linked to the existing `CultureMech:000462` DSMZ normalized owner as a source duplicate.
- Empty target-organism, temperature, storage, and salinity slots are acceptable here; the inspected DSMZ Medium 1039 PDF did not provide those claims.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | `Tap water` is represented as `1000 G_PER_L`. | DSMZ 1039 lists Tap water as `1000.0 ml`, the recipe final volume; the normalized owner and generated merge store `value: '1000'`, `unit: G_PER_L`. | Fix the DSMZ-to-KOMODO enrichment/importer path and `data/normalized_yaml/bacterial/KOMODO_1039_ANACKER-ORDAL_AGAR.yaml` so final-volume water is not represented as a gram-per-liter solute. |
| Major | KOH is modeled as a variable-concentration ingredient. | DSMZ 1039 names KOH only in the preparation sentence `Adjust to pH 7.2 prior to autoclaving with KOH`; it is not a weighed or variable recipe component. | Move KOH into the pH-adjustment preparation step and remove it from the normalized owner's `ingredients`. |
| Major | The DSMZ preparation warning was not copied into the KOMODO-side record. | `data/normalized_yaml/bacterial/anacker_ordal_agar.yaml` and the DSMZ PDF include the indicator-paper warning; `KOMODO_1039_ANACKER-ORDAL_AGAR.yaml` and the generated merge do not. | Copy or merge the DSMZ-supported preparation steps into the KOMODO owner or teach the merge layer to retain non-conflicting parent steps from the DSMZ duplicate. |
| Major | KOMODO Medium 1039 remains a singleton instead of a source duplicate of DSMZ Medium 1039. | The local DSMZ owner has the same identity, pH, physical state, and true ingredient signature once the spurious KOH row is removed. | Add reciprocal `SOURCE_DUPLICATE` metadata between `KOMODO_1039_ANACKER-ORDAL_AGAR.yaml` and `anacker_ordal_agar.yaml`, then regenerate merge YAML. |

## Recommended Edits

1. Remove `Tap water` as a `G_PER_L` ingredient from the KOMODO 1039 normalized owner unless the schema gains a final-volume field for the 1000 ml volume.
2. Remove KOH from `ingredients`; represent it only in the pH 7.2 preparation instruction.
3. Add the DSMZ 1039 preparation details to the KOMODO record: adjust before autoclaving with KOH, and use indicator paper rather than a pH electrode.
4. Mark the KOMODO 1039 and DSMZ/MediaDive 1039 owners as reciprocal `SOURCE_DUPLICATE` records once the ingredient signatures align.
5. Regenerate `data/merge_yaml/merged` with `just merge-recipes` after the normalized owners or merge rules are corrected.

## Follow-up Checks

1. Run focused open-schema, strict, term, and reference validation on `data/normalized_yaml/bacterial/KOMODO_1039_ANACKER-ORDAL_AGAR.yaml`, `data/normalized_yaml/bacterial/anacker_ordal_agar.yaml`, and the regenerated merged ANACKER-ORDAL AGAR record.
2. Run `just verify-merges` and `just audit-merge-freshness --fail-on-drift` after regeneration; the KOMODO and DSMZ 1039 records should no longer produce separate generated merge files if they are source duplicates.
3. Re-fetch or re-open `DSMZ_Medium1039.pdf` and check that the generated recipe still matches all five weighed solutes plus agar, pH 7.2, the 1000 ml water final volume semantics, and the indicator-paper warning.
4. Re-run the concentration plausibility report and confirm the existing `WATER_AS_VOLUME` finding for `CultureMech:003553` is gone.

## Additional Notes

- The bounded identity search used `rg --no-ignore --hidden`; ignored paths were included for the searched roots.
- `data/merge_yaml/merged/anacker_ordal_agar__824a105c.yaml` is the separate current merge for the DSMZ/MediaDive owner and should collapse with this KOMODO record after source-duplicate repair.
- The DSMZ source PDF was fetched directly from `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1039.pdf` during this review.
