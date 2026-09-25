# YAML Record Review: BCYE_alpha_agar

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BCYE_alpha_agar.yaml
- Started UTC: 2026-09-21T19:27:07Z
- Finished UTC: 2026-09-21T19:29:03Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path reviewed | `data/merge_yaml/merged/BCYE_alpha_agar.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/bcye_alpha_agar.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:001712` |
| Name | `bcye_alpha_agar` |
| Original name | `BCYE alpha agar` |
| Source | MediaDive / DSMZ Medium `585a` |
| Merge status | Generated one-source merge from `bcye_alpha_agar` |

## Validation

| Check | Result |
|---|---|
| Open schema | Passed with the no-project LinkML invocation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe`, and the generated DSMZ 585a merge. |
| Strict schema | Passed with the no-project invocation of `scripts/validate_strict.py`: 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validator | Passed with 0 reference checks because this MediaDive import has no populated `references` list or evidence objects. |
| Term validator | Passed with `linkml-term-validator validate-data` against the generated DSMZ 585a merge. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for the standalone `history/` tree, not a focused one-record `MediaRecipe.curation_history` check. |
| Project `just` wrappers | Not rerun here: direct `just validate-schema`, `just validate-strict`, and `just validate-terms` fail before target-specific validation in this checkout while the project `uv` environment attempts to build `llvmlite==0.46.0` under Python 3.13. The equivalent no-project Python 3.11 validators above exercised the target record. |

## Identity and Grounding

- `data/merge_yaml/merged/BCYE_alpha_agar.yaml` denotes DSMZ Medium 585a, `BCYE alpha agar`, and is a one-source generated merge from `data/normalized_yaml/bacterial/bcye_alpha_agar.yaml`.
- The generated merge and normalized owner match for the scientific fields, so future fixes belong in the normalized owner followed by merge regeneration.
- The inspected MediaDive 585a page, PDF, and JSON all identify 585a as a BCYE alpha formulation with final pH 6.9, final volume 1000 ml, solution A through D components, and 1 g/L sodium alpha-ketoglutarate added to solution A.
- The source supports the medium identity but not the YAML's stock `g_l` values, its `OXOID Legionella CYE-Agar base` row at `1000 G_PER_L`, its missing distilled-water rows, or its anion grounding for `Na2 alpha-ketoglutarate`.
- Exact gitignore-independent searches for `CultureMech:001712`, exact `mediadive.medium:585a`, `DSMZ Medium 585a`, and `bcye_alpha_agar` covered `data`, `src`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md`. They found the normalized owner, generated merge, indexes, and import-priority reports, but no local raw MediaDive 585a source capture under `data`.

## Evidence

- MediaDive 585a lists the main `CYE-ACES alpha AGAR` recipe as 490 ml solution A, 490 ml solution B, 10 ml solution C, and 10 ml solution D.
- In solution A, MediaDive 585a lists 10 g ACES, 10 g yeast extract, 2 g activated charcoal, 1 g Na2 alpha-ketoglutarate, and 490 ml distilled water.
- The MediaDive 585a final-composition JSON reports final concentrations of 10 g/L ACES, 10 g/L yeast extract, 2 g/L activated charcoal, 1 g/L Na2 alpha-ketoglutarate, 15 g/L agar, 0.4 g/L L-cysteine HCl x H2O, and 0.25 g/L Fe4(PO4)2.
- The YAML instead records solution-stock concentrations: 20.4082 g/L ACES and yeast extract, 4.08163 g/L activated charcoal, 2.04082 g/L Na2 alpha-ketoglutarate, 30.6122 g/L agar, 40 g/L L-cysteine HCl x H2O, and 25 g/L Fe4(PO4)2.
- MediaDive lists an `OXOID Legionella CYE-Agar base` solution at 1000 ml with Legionella BCYE supplement; the YAML imports that as an ingredient at 1000 g/L.

## Completeness

- Consequential gaps:
  - Stock concentrations are used where the final medium should use final concentrations.
  - The commercial OXOID row has the wrong unit and is flattened into an ingredient.
  - Solutions A through D are not represented as solutions, and their distilled-water rows are absent.
  - The preparation steps are present as prose but are not scoped to their solution boundaries.
  - The sodium alpha-ketoglutarate row is grounded to the alpha-ketoglutarate dianion, not the sodium salt named by the source.
  - The MediaDive 585a URL is absent from structured `references`.
- Correctly empty optional slots:
  - `target_organisms` and `growth_metrics` are absent; MediaDive 585a is a formulation/protocol source and not a strain-specific growth assay.
  - The OXOID commercial shortcut should not be forced to a narrow ChEBI small-molecule term.
- Bounded negative searches:
  - Exact gitignore-independent searches found no local raw MediaDive 585a page, PDF, or JSON capture under `data/raw`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The record stores stock concentrations as final concentrations. | MediaDive's final-composition JSON reports 10, 10, 2, 1, 15, 0.4, and 0.25 g/L for the final solutes; the YAML stores each non-OXOID row at its A/B/C/D stock concentration. | `data/normalized_yaml/bacterial/bcye_alpha_agar.yaml`. |
| Major | The `OXOID Legionella CYE-Agar base` row has the wrong amount and boundary. | MediaDive represents the OXOID commercial route as a 1000 ml solution with Legionella BCYE supplement; the YAML stores it as a 1000 g/L ingredient alongside the CYE-ACES alpha alternative. | `data/normalized_yaml/bacterial/bcye_alpha_agar.yaml`. |
| Major | The solution graph is flattened away. | The source recipe is a four-solution 1000 ml recipe; the YAML has no solution nodes, no water rows, and unscoped preparation steps. | `data/normalized_yaml/bacterial/bcye_alpha_agar.yaml`. |
| Major | Sodium alpha-ketoglutarate is grounded to the wrong chemical form. | The source names `Na2 alpha-ketoglutarate`; the YAML grounds it to `CHEBI:16810`, label `2-oxoglutarate(2-)`, which is the dianion rather than the sodium salt. | `data/normalized_yaml/bacterial/bcye_alpha_agar.yaml`. |
| Minor | The ACES row still uses the legacy `mediaingredientmech_term` slot. | This row has `term: CHEBI:39061` but retains `mediaingredientmech_term: MediaIngredientMech:000555` while neighboring migrated rows use `mediaingredientmech_chebi_term`. | `data/normalized_yaml/bacterial/bcye_alpha_agar.yaml`; broad repeats may need the MIM legacy migration. |

## Recommended Edits

1. Rebuild the normalized DSMZ 585a record around `CYE-ACES alpha AGAR`: solution A with 1 g Na2 alpha-ketoglutarate, solutions B through D reused from DSMZ 585, and a final 1000 ml formulation at pH 6.9.
2. Store final concentrations from the MediaDive final-composition JSON, not the individual stock `g_l` values.
3. Represent the OXOID Legionella CYE-Agar base route as a separate 1000 ml commercial shortcut or remove it from the explicit CYE-ACES alpha ingredient list.
4. Ground `Na2 alpha-ketoglutarate` to an exact sodium salt term after verifying an ID/label match, or leave it intentionally ungrounded with a note.
5. Add a structured MediaDive 585a reference.
6. Regenerate `data/merge_yaml/merged/BCYE_alpha_agar.yaml` from the repaired normalized owner.

## Follow-up Checks

- Rerun open-schema LinkML validation, `scripts/validate_strict.py`, `linkml-term-validator`, and the reference validator on the repaired normalized owner.
- Re-fetch MediaDive 585a PDF and composition JSON and manually compare final volume, pH, all four solution rows, final-composition `g_l` values, and the OXOID shortcut.
- Run `just verify-merges` and `just audit-merge-freshness --json --list` after regenerating.
- Re-check exact `CultureMech:001712`, exact `mediadive.medium:585a`, and `bcye_alpha_agar` occurrences with a gitignore-independent search to verify only the normalized owner and fresh generated merge carry the repaired DSMZ 585a representation.

## Additional Notes

- The inspected upstream source was the live MediaDive 585a page plus its PDF and JSON downloads.
- Exact gitignore-independent searches included ignored files where present.
