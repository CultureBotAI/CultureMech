# YAML Record Review: Basal_salts_solution_supplemented_with_tetrathionate

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/Basal_salts_solution_supplemented_with_tetrathionate.yaml
- Started UTC: 2026-09-21T18:47:10Z
- Finished UTC: 2026-09-21T18:48:32Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path reviewed | `data/merge_yaml/merged/Basal_salts_solution_supplemented_with_tetrathionate.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/basal_salts_solution_supplemented_with_tetrathionate.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:009680` |
| Name | `basal_salts_solution_supplemented_with_tetrathionate` |
| Original name | `Basal salts solution supplemented with tetrathionate` |
| Source | TOGO Medium `M3248` |
| Merge status | Generated one-source merge from `basal_salts_solution_supplemented_with_tetrathionate` |

## Validation

| Check | Result |
|---|---|
| Open schema | Passed with the no-project LinkML invocation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe`, and the generated M3248 merge. |
| Strict schema | Passed with the no-project invocation of `scripts/validate_strict.py`: 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validator | Passed with 0 reference checks because this TOGO import has no populated `references` list or evidence objects. |
| Term validator | Passed with `linkml-term-validator validate-data` against the generated M3248 merge. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for the standalone `history/` tree, not a focused one-record `MediaRecipe.curation_history` check. |
| Project `just` wrappers | Not rerun here: direct `just validate-schema`, `just validate-strict`, and `just validate-terms` fail before target-specific validation in this checkout while the project `uv` environment attempts to build `llvmlite==0.46.0` under Python 3.13. The equivalent no-project Python 3.11 validators above exercised the target record. |

## Identity and Grounding

- The generated record denotes TOGO `M3248`, `Basal salts solution supplemented with tetrathionate`, and has the permanent ID `CultureMech:009680`.
- Exact gitignore-independent searches for `CultureMech:009680`, `M3248`, and `Basal_salts_solution_supplemented_with_tetrathionate` covered `data`, `src`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md`. They found the normalized owner, generated merge, generated indexes, registry rows, and one metal-analysis entry; they found no maintained raw TOGO payload.
- The generated merge is stale relative to `data/normalized_yaml/bacterial/basal_salts_solution_supplemented_with_tetrathionate.yaml`: the normalized owner contains an August 20, 2026 MIM grounding event and a `CHEBI:15226` term on the tetrathionate row that are absent from the generated merge.
- The newer normalized `CHEBI:15226` term still requires exact review. TOGO's component label is `Potassium tetrathionate`, the free text specifies `20 mM K2S4O6`, and the packaged MIM label index maps `Potassium tetrathionate` to `CHEBI:86466`; tetrathionate(2-) is the ion, not the added salt.

## Evidence

- The inspected TOGO M3248 API response supports the record name, `TOGO:M3248`, the five basal salt quantities, 1 L deionized water, 20 mM tetrathionate as `K2S4O6`, HCl adjustment to pH 4.0, and filter sterilization for tetrathionate experiments.
- The imported basal salt quantities agree with the TOGO source: `0.6 g/L NH4Cl`, `0.2 g/L MgCl2.6H2O`, `0.1 g/L K2HPO4`, `0.10 g/L KCl`, and `0.01 g/L Ca(NO3)2`.
- The water row is dimensionally wrong: TOGO lists `Deionized water` as `1 L`, but the record stores `1 G_PER_L`.
- The source states that the pH was adjusted to 4 with trace-metal grade HCl, while the record has a default `variable` HCl row with role `Solvating media` and no pH.
- The source separates sterilization by electron donor: elemental-sulfur experiments were autoclaved and tetrathionate experiments were filter-sterilized to prevent oxidation. The tetrathionate record does not preserve the filter-sterilization requirement.

## Completeness

- Consequential gaps:
  - The generated merge should be regenerated from the Aug 20 normalized owner before review findings are rechecked.
  - The solvent needs a volume/final-volume representation instead of `1 G_PER_L`.
  - Tetrathionate should be represented as 20 mM potassium tetrathionate, not an ungrounded generic source string or the bare tetrathionate ion.
  - pH 4, trace-metal grade HCl adjustment, and tetrathionate filter sterilization are missing.
  - This all-defined medium is still classified as `COMPLEX`/`UNDEFINED`.
- Correctly empty optional slots:
  - `solutions` is absent because TOGO M3248 lists all components directly.
  - `target_organisms` and `references` are empty because the inspected TOGO payload does not name a strain, organism, DOI, or PMID.
- Bounded negative searches:
  - Exact gitignore-independent searches for `20 mM K2S4O6` and `filter sterilized for the experiments with tetrathionate` across `data`, `src`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found no local copy of those TOGO comment strings.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated merge is stale and lacks the normalized owner's Aug 20 tetrathionate grounding. | The generated merge contains no `term` for `Tetrathionate`; the normalized owner now has `CHEBI:15226` and an `apply_mim_groundings.py` curation event dated 2026-08-20. | Regenerate `data/merge_yaml/merged/Basal_salts_solution_supplemented_with_tetrathionate.yaml` from `data/normalized_yaml/bacterial/basal_salts_solution_supplemented_with_tetrathionate.yaml`. |
| Major | The tetrathionate identity is under-specified and likely overbroadened in the normalized fix. | TOGO M3248 labels the ingredient `Potassium tetrathionate` and comments `20 mM K2S4O6`; the MIM label index maps `Potassium tetrathionate` to `CHEBI:86466`, not `CHEBI:15226` tetrathionate(2-). | `data/normalized_yaml/bacterial/basal_salts_solution_supplemented_with_tetrathionate.yaml`. |
| Major | The one-liter deionized-water row is dimensionally wrong. | TOGO M3248 lists `Deionized water`, `volume: 1`, `unit: L`; the record stores `value: '1'`, `unit: G_PER_L`. | `data/normalized_yaml/bacterial/basal_salts_solution_supplemented_with_tetrathionate.yaml`; broad repeats should be fixed in TOGO import volume handling. |
| Major | The source pH and acid-adjustment semantics were dropped. | The TOGO API has `ph: 4.0` and the comment says HCl adjusts the medium to pH 4; the YAML stores HCl as default `variable`/`VARIABLE` with no pH and the imported GMO role `Solvating media`. | `data/normalized_yaml/bacterial/basal_salts_solution_supplemented_with_tetrathionate.yaml`. |
| Major | Tetrathionate-specific sterilization was dropped. | TOGO says tetrathionate experiments were filter-sterilized to prevent oxidation; the YAML has no preparation or sterilization detail. | `data/normalized_yaml/bacterial/basal_salts_solution_supplemented_with_tetrathionate.yaml`. |
| Major | The all-defined recipe is classified as complex and undefined. | Every ingredient in TOGO M3248 is a defined salt, deionized water, tetrathionate salt, or HCl solution; the YAML says `medium_type: COMPLEX` and `composition_type: UNDEFINED`. | `data/normalized_yaml/bacterial/basal_salts_solution_supplemented_with_tetrathionate.yaml`. |

## Recommended Edits

1. Re-ground `Tetrathionate` as potassium tetrathionate, preserve the `K2S4O6` form, and keep the 20 mM concentration.
2. Represent `Deionized water` as 1 L or an equivalent schema-supported final-volume row instead of `1 G_PER_L`.
3. Add pH 4 and model HCl as a pH-adjustment reagent rather than a generic variable-concentration solvent.
4. Add the tetrathionate-specific filter-sterilization instruction and keep the elemental-sulfur autoclaving note out of this tetrathionate-only recipe unless a separate sulfur variant is curated.
5. Reclassify the record to `composition_type: DEFINED` with derived `medium_type: DEFINED`.
6. Regenerate the generated M3248 merge after normalized curation.

## Follow-up Checks

- Rerun open-schema LinkML validation, `scripts/validate_strict.py`, `linkml-term-validator`, and the reference validator on the normalized owner after edits.
- Regenerate `data/merge_yaml/merged/Basal_salts_solution_supplemented_with_tetrathionate.yaml` and run `just verify-merges` plus `just audit-merge-freshness`.
- Re-fetch TOGO M3248 and manually compare the pH, HCl, water, tetrathionate, and filter-sterilization claims against the normalized record.
- Confirm the regenerated merge carries the intended tetrathionate term and no longer lags the normalized owner's August 2026 curation.

## Additional Notes

- `data/metal_ree_analysis.yaml` currently records only the magnesium and potassium rows for TOGO M3248; calcium nitrate is absent from that generated analysis even though the recipe contains `0.01 g/L Ca(NO3)2`.
- The exact gitignore-independent searches included ignored files where present.
