# YAML Record Review: ANAEROBACULUM MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/anaerobaculum_medium__7e498ca6.yaml
- Started UTC: 2026-09-21T11:54:46Z
- Finished UTC: 2026-09-21T11:56:19Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:000474 |
| Source | mediadive.medium:104a |
| Generated path | data/merge_yaml/merged/anaerobaculum_medium__7e498ca6.yaml |
| Maintained owner | data/normalized_yaml/bacterial/anaerobaculum_medium.yaml |
| Current parent | data/normalized_yaml/bacterial/KOMODO_104b_PYX-MEDIUM.yaml |
| Merge fingerprint | 7e498ca67c37850b59b33b2bc679fffb2d43f304206aef374fcb1f6ff36a6247 |
| Merged source count | 57 |

`data/merge_yaml/merged/anaerobaculum_medium__7e498ca6.yaml` is a generated duplicate merge rooted in the DSMZ/MediaDive 104a normalized owner. It was generated on August 6 and is stale relative to September 13 relationship repairs on the PYX-MEDIUM family.

## Validation

| Check | Result |
| --- | --- |
| Open schema | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/anaerobaculum_medium__7e498ca6.yaml` under the cached Python 3.11 no-project environment. |
| Strict schema | Passed with `scripts/validate_strict.py data/merge_yaml/merged/anaerobaculum_medium__7e498ca6.yaml --workers 1 --quiet`; the TSV contained 0 ERROR rows. |
| Reference validator | Passed with `linkml-reference-validator validate data ...`; no reference checks were emitted for this file. |
| Term validator | Passed with `linkml-term-validator validate-data ... --labels -c conf/oak_config.yaml`. |
| Embedded curation history | Not checked: this repository exposes `just validate-history` for standalone records under `history/`; no documented focused validator targets embedded `MediaRecipe.curation_history` inside one merge record. |

The project-level `just validate-schema`, `just validate-strict`, and `just validate-terms` routes were not usable for this target because project installation currently attempts to build `llvmlite==0.46.0` on Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The equivalent LinkML validators passed through an offline `uv run --no-project` invocation against `/usr/local/bin/python3.11`.

## Identity and Grounding

- The stable CultureMech ID, `mediadive.medium:104a`, and merge fingerprint identify the DSMZ Medium 104a, ANAEROBACULUM MEDIUM, generated merge.
- A gitignore-independent search across `data`, `src`, `scripts`, `history`, `conf`, `reports`, `.claude`, `justfile`, and `CLAUDE.md` found the current DSMZ owner, its PYX-MEDIUM parent, and September 13 repair events on the parent and several variant children; older `DSMZ_104a_ANAEROBACULUM_MEDIUM.yaml` names appear only in archived validation reports.
- The inspected DSMZ 104a PDF supports the recipe identity, pH 7.0, liquid state, major organic ingredients, the post-autoclave glucose and thiosulfate additions, and the anaerobic preparation under 100% N2.
- The generated record still says 57 normalized recipes were merged as duplicates. Current normalized PYX records have already split some of those old duplicate children into `PH_VARIANT` or `STRAIN_SPECIFIC_VARIANT` on September 13, so this generated merge overstates duplicate equivalence.

## Evidence

- DSMZ 104a lists Trypticase peptone 5.00 g, meat peptone 5.00 g, yeast extract 10.00 g, NaCl 8.00 g, 40.00 ml salt solution from medium 104, 0.50 ml of 0.1% w/v sodium resazurin, 0.50 g cysteine hydrate, 1.00 g D-glucose, 2.50 g sodium thiosulfate pentahydrate, and distilled water 960.00 ml.
- The generated record preserves the organic additions and sodium resazurin final mass, but it flattens the nested medium 104 salt solution as if its stock recipe were direct final-medium grams per liter.
- The `NaCl` row records `10.0 G_PER_L` with a note that `8.0` and `2.0` were merged; DSMZ 104a instead has 8.00 g directly in the base and 2.00 g inside the one-liter salt stock of which only 40 ml is added.
- Current `data/normalized_yaml/bacterial/KOMODO_104b_PYX-MEDIUM.yaml` contains September 13 curation events that reclassified pH and strain-specific PYX children, but the generated merge still includes those source IDs in `merged_from` and `synonyms` under a single source-duplicate recipe.

## Completeness

- Consequentially incorrect: the medium 104 salt stock boundary is lost, and stock-strength salt rows have been copied into the final recipe.
- Consequentially incorrect: base NaCl and stock NaCl were added into one final `NaCl` row.
- Consequentially incomplete: the generated merge is stale relative to the repaired PYX variant relationships.
- Empty target-organism, temperature, storage, and salinity slots are acceptable here; the inspected DSMZ Medium 104a PDF did not provide those claims.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Blocker | The generated 57-way duplicate merge is stale and overbroad. | September 13 repairs in `KOMODO_104b_PYX-MEDIUM.yaml` changed several old duplicate children to pH or strain-specific variants; the August generated merge still includes them all in one merged `SOURCE_DUPLICATE` output. | Regenerate `data/merge_yaml/merged` from the current normalized owners with `just merge-recipes`; if pH and strain variants still collapse, fix `src/culturemech/merge/merge_recipes.py`. |
| Major | The medium 104 salt solution was flattened at stock strength. | DSMZ 104a adds 40 ml of Salt solution from medium 104, but the record includes CaCl2.2H2O, MgSO4.7H2O, K2HPO4, KH2PO4, NaHCO3, and the stock NaCl at their one-liter stock masses as direct final-medium `G_PER_L` rows. | Model the Medium 104 salt solution as a referenced stock or convert each salt to the 40 ml per liter final contribution in `data/normalized_yaml/bacterial/anaerobaculum_medium.yaml`. |
| Major | Base NaCl and stock NaCl were summed into one final row. | DSMZ 104a has 8.00 g NaCl directly in the base and 2.00 g NaCl inside the salt stock; the record's `NaCl` row stores `10.0 G_PER_L` with `Merged 2 duplicates: 8.0, 2.0`. | Restore separate source semantics or recalculate the salt-stock contribution before any final-concentration summation. |
| Minor | The sole preparation step is overpacked. | DSMZ 104a has a multi-stage anaerobic workflow with boiling, N2 cooling, cysteine addition, pH adjustment, dispensing, autoclaving, and post-autoclave glucose/thiosulfate stock additions; the record preserves the prose but collapses all stages into one `AUTOCLAVE` step. | Split the DSMZ preparation text into ordered preparation steps in the normalized owner. |

## Recommended Edits

1. Regenerate merge YAML so the September 13 PYX relationship repairs are reflected in generated `merged_from`, `synonyms`, and variant metadata.
2. Correct `data/normalized_yaml/bacterial/anaerobaculum_medium.yaml` so the 40 ml Medium 104 salt solution is represented as a stock-solution addition or as final amounts calculated from the stock dilution.
3. Undo the `NaCl` duplicate summation and preserve the distinction between 8.00 g base NaCl and 2.00 g per liter inside the Medium 104 salt stock.
4. Split the long DSMZ preparation prose into ordered, scoped steps.

## Follow-up Checks

1. Run focused open-schema, strict, term, and reference validation on `data/normalized_yaml/bacterial/anaerobaculum_medium.yaml` and the regenerated `data/merge_yaml/merged/anaerobaculum_medium__7e498ca6.yaml`.
2. Run `just verify-merges` and `just audit-merge-freshness --fail-on-drift` after regeneration.
3. Re-fetch or re-open `DSMZ_Medium104a.pdf` and verify that Medium 104 salt solution remains nested or is diluted exactly by 40 ml per liter.
4. Inspect the regenerated merge to confirm that PYX pH and strain-specific variants no longer appear as source duplicates in the 104a merge.

## Additional Notes

- The bounded identity search used `rg --no-ignore --hidden`; ignored paths were included for the searched roots.
- The DSMZ source PDF was fetched directly from `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium104a.pdf` during this review.
