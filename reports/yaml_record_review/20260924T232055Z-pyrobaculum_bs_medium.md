# YAML Record Review: Pyrobaculum (BS) Medium
- Repository: CultureMech
- Record: `data/merge_yaml/merged/pyrobaculum_bs_medium.yaml`
- Started UTC: 2026-09-24T23:20:55Z
- Finished UTC: 2026-09-24T23:22:05Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated file | `data/merge_yaml/merged/pyrobaculum_bs_medium.yaml` |
| Maintained owner | `data/normalized_yaml/archaea/TOGO_M2219_Pyrobaculum_BS_Medium.yaml` |
| Source identity | `TOGO:M2219`, original DSMZ medium 611 |
| Source URL | `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium611.pdf` |
| Merge fingerprint | `572d2b24a413eb6d4d11d4cdbc1d4adbebd9fe9733c7eb26c228cff9957b96bd` |

The reviewed file is a generated merge from a single TOGO wrapper. Future data edits belong in the maintained normalized owner, followed by regeneration of `data/merge_yaml/merged/` and downstream artifacts.

## Validation

| Validator | Result |
| --- | --- |
| Open LinkML schema | Passed; no schema issues found. |
| Strict validator | Passed with 0 ERROR rows; TSV had the header only. |
| Reference validator | Passed; 1 file, 0 checks. |
| Term validator | Passed; emitted only the expected `eutils` `pkg_resources` warning. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

The record is a TOGO M2219 wrapper around DSMZ medium 611, `PYROBACULUM (BS) MEDIUM`. The live TOGO API, MediaDive 611 REST record, and DSMZ 611 PDF all identify the same medium with a final pH range of 7.0 to 7.2.

An ignored-file-inclusive owner search across `data/normalized_yaml` and `data/merge_yaml/merged` for `CultureMech:008808`, `TOGO:M2219$`, `togomedium.org/medium/M2219$`, `DSMZ_Medium611`, `Medium611`, `medium/611`, `mediadive.medium:611`, the full merge fingerprint, and `TOGO_M2219_Pyrobaculum_BS_Medium` found the TOGO owner and also found `data/normalized_yaml/archaea/pyrobaculum_bs_medium.yaml`, a direct DSMZ/MediaDive owner for the same DSMZ 611 source. That direct owner generates `data/merge_yaml/merged/pyrobaculum_bs_medium__76137706.yaml`, so the exact same source is stranded in two generated artifacts.

## Evidence

DSMZ 611 and MediaDive 611 define a 1012 ml final recipe with 125 ml Synthetic seawater mix, 10 ml Modified Wolin's mineral solution, 2 ml 0.01% w/v Fe(NH4)2(SO4)2 x 6 H2O solution, 0.25 g NH4Cl, 0.07 g KH2PO4, 1 g KNO3, 0.5 g yeast extract, 2 g NaHCO3, and 875 ml water. The YAML instead stores `Synthetic seawater mix` as `125` `G_PER_L` and stores the Fe solution as an empty `solutions` entry with `2` `G_PER_L`.

The DSMZ recipe defines Synthetic seawater mix as a per-liter stock. The YAML leaves no populated seawater solution and promotes that stock's contents to final ingredients. In that promotion, stock-local KBr 80 mg, SrCl2 x 6 H2O 72 mg, H3BO3 52 mg, Na2HPO4 8.1 mg, NaF 2.4 mg, Na-silicate 0.4 mg, and KI 50 ug became 80, 72, 52, 8.1, 2.4, 0.4, and 50 `G_PER_L`.

The DSMZ recipe also defines Modified Wolin's mineral solution from medium 141 as a separate per-liter stock used at 10 ml/L. The YAML stores an empty `Trace element solution` shell and promotes its contents to final ingredients. In that promotion, stock-local Na2SeO3 x 5 H2O 0.30 mg and Na2WO4 x 2 H2O 0.40 mg became `0.3` and `0.4` `G_PER_L`.

The 875 ml final water, 1000 ml seawater-stock water, and 1000 ml trace-stock water were merged into one top-level `Distilled water` amount of `2875.0` `G_PER_L`. Same-named salts from unrelated stocks were also summed, including NaCl, MgSO4 x 7 H2O, CaCl2 x 2 H2O, and H3BO3.

Current DSMZ 611 and MediaDive 611 no longer list the 0.5 ml Na-resazurin solution row that is present in TOGO M2219, and TOGO M2219 lacks DSMZ's post-inoculation instruction to add sterile 80% H2 / 20% CO2 gas to 2 bar overpressure. The generated YAML has no `preparation_steps` and no `ph_range`.

## Completeness

The record captures the TOGO/DSMZ source identity but is incomplete as an executable recipe. It needs a final recipe with explicit additions for 125 ml/L seawater, 10 ml/L Modified Wolin's mineral solution, 2 ml/L Fe solution, 875 ml/L water, and final pH 7.0 to 7.2; it also needs populated nested stocks instead of empty solution placeholders and flattened stock members. The TOGO-only Na-resazurin row should be reconciled against the current DSMZ and MediaDive source before regeneration.

The sibling direct DSMZ owner preserves the pH range and DSMZ preparation text and converts small seawater/trace rows correctly, but it also collapses both stocks into top-level ingredients and sums unrelated stock-local salts. Both owners need coordinated repair and merge-deduplication.

## Findings

| Severity | Finding | Evidence | Recommended owner |
| --- | --- | --- | --- |
| Blocker | Stock additions are represented as grams-per-liter scalars or empty solutions. | The 125 ml Synthetic seawater mix final addition became `125` `G_PER_L`; the 2 ml Fe solution, TOGO-only 0.5 ml Na-resazurin row, and 10 ml Modified Wolin's mineral solution became empty `solutions` entries. | `data/normalized_yaml/archaea/TOGO_M2219_Pyrobaculum_BS_Medium.yaml` |
| Blocker | Two full stocks were flattened into the final ingredient list. | DSMZ 611 nests Synthetic seawater mix and Modified Wolin's mineral solution; the YAML promotes both stocks' members to top-level ingredients and merges their 1000 ml water rows into the final 875 ml water row. | `data/normalized_yaml/archaea/TOGO_M2219_Pyrobaculum_BS_Medium.yaml` |
| Blocker | Milligram and microgram stock rows are inflated to gram-per-liter rows. | Source KI is 50 ug in Synthetic seawater mix but is `50` `G_PER_L`; KBr 80 mg, SrCl2 x 6 H2O 72 mg, H3BO3 52 mg, Na2HPO4 8.1 mg, NaF 2.4 mg, and Na2SeO3 x 5 H2O 0.30 mg are also inflated. | `data/normalized_yaml/archaea/TOGO_M2219_Pyrobaculum_BS_Medium.yaml` |
| Major | Source pH and preparation steps are absent. | TOGO M2219, MediaDive 611, and DSMZ 611 all carry pH 7.0 to 7.2 and gas-handling preparation text; current DSMZ/MediaDive also include a 2 bar post-inoculation overpressure step. The YAML has no `ph_range` or `preparation_steps`. | `data/normalized_yaml/archaea/TOGO_M2219_Pyrobaculum_BS_Medium.yaml` |
| Major | The same DSMZ 611 source is split across two generated records. | Ignored-file-inclusive search found `data/normalized_yaml/archaea/pyrobaculum_bs_medium.yaml` and generated `pyrobaculum_bs_medium__76137706.yaml`, both pointing to `DSMZ_Medium611.pdf` / `mediadive.medium:611`. | Merge identity/fingerprint logic plus both normalized owners |

## Recommended Edits

1. Restore `ph_range` 7.0 to 7.2 and the DSMZ 611 final-medium and Modified Wolin's solution preparation steps.
2. Model Synthetic seawater mix as a populated nested stock used at 125 ml/L.
3. Model Modified Wolin's mineral solution as a populated nested stock used at 10 ml/L.
4. Model the 0.01% w/v Fe(NH4)2(SO4)2 x 6 H2O solution as a 2 ml/L volume addition, not a `G_PER_L` stock object.
5. Convert all milligram and microgram rows in their own stock contexts and stop summing stock-local rows into final-medium ingredients.
6. Resolve the TOGO-only Na-resazurin row and missing 2 bar overpressure instruction against the current DSMZ 611 and MediaDive 611 sources.
7. Reconcile the TOGO and direct DSMZ owners so exact DSMZ 611 duplicates merge or one wrapper is intentionally suppressed.
8. Regenerate `data/merge_yaml/merged/` after the maintained YAML and merge identity are repaired.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation on the regenerated record.
- Re-open TOGO M2219, MediaDive 611, and the DSMZ 611 PDF to confirm stock volumes, pH, and preparation steps match.
- Re-run an ignored-file-inclusive search for `TOGO:M2219`, `DSMZ_Medium611`, and `mediadive.medium:611` to confirm same-source duplicate handling.
- Confirm KI is no longer represented as `50` `G_PER_L` anywhere in the repaired generated record.

## Additional Notes

The current TOGO owner still has a stale MgSO4 x 7 H2O `mediaingredientmech_chebi_term` of `CHEBI:32599` while its primary term is correctly grounded to `CHEBI:31795`; that should be refreshed while the owner is being repaired.
