# YAML Record Review: basal_salts_medium_bsm_modified_from_that_of_hareland_et_al_j_bacteriol_121_272_285_1975_by_removal_of_the_nitriloacetic_acid

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/basal_salts_medium_bsm_modified_from_that_of_hareland_et_al_j_bacteriol_121_272_285_1975_by_removal_of_the_nitriloacetic_acid.yaml
- Started UTC: 2026-09-21T18:45:02Z
- Finished UTC: 2026-09-21T18:47:10Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path reviewed | `data/merge_yaml/merged/basal_salts_medium_bsm_modified_from_that_of_hareland_et_al_j_bacteriol_121_272_285_1975_by_removal_of_the_nitriloacetic_acid.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/basal_salts_medium_bsm_modified_from_that_of_hareland_et_al_j_bacteriol_121_272_285_1975_by_removal_of_the_nitriloacetic_acid.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:008825` |
| Name | `basal_salts_medium_bsm_modified_from_that_of_hareland_et_al_j_bacteriol_121_272_285_1975_by_removal_of_the_nitriloacetic_acid` |
| Original name | `Basal salts medium (BSM) modified from that of Hareland et al. ( J Bacteriol 121:272-285(1975)) by removal of the nitriloacetic acid` |
| Source | TOGO Medium `M2237` |
| Merge status | Generated one-source merge from the same slug |

## Validation

| Check | Result |
|---|---|
| Open schema | Passed with the no-project LinkML invocation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe`, and the generated M2237 merge. |
| Strict schema | Passed with the no-project invocation of `scripts/validate_strict.py`: 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validator | Passed with 0 reference checks because this TOGO import has no populated `references` list or evidence objects. |
| Term validator | Passed with `linkml-term-validator validate-data` against the generated M2237 merge. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for the standalone `history/` tree, not a focused one-record `MediaRecipe.curation_history` check. |
| Project `just` wrappers | Not rerun here: direct `just validate-schema`, `just validate-strict`, and `just validate-terms` fail before target-specific validation in this checkout while the project `uv` environment attempts to build `llvmlite==0.46.0` under Python 3.13. The equivalent no-project Python 3.11 validators above exercised the target record. |

## Identity and Grounding

- The record identity is coherent: `CultureMech:008825` is registered to the normalized bacterial M2237 owner, and the generated merge is a one-source derivative with fingerprint `58af19d8d8407cb987b003ca0297739f8eb37dc5b9412adcc542f888e4aeefb9`.
- Exact gitignore-independent searches for `CultureMech:008825`, `M2237`, and the long normalized slug covered `data`, `src`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md`. They found only the normalized owner, generated merge, generated indexes, registry rows, and import/report metadata for this record.
- `Distilled water`, magnesium sulfate heptahydrate, ammonium chloride, ferrous sulfate heptahydrate, zinc sulfate heptahydrate, manganese sulfate monohydrate, and glucose have exact or acceptably normalized CHEBI groundings.
- Yeast extract and CAS amino acids are undefined mixtures and are correctly left without single small-molecule CHEBI terms.
- The exact source chemicals `Cobalt sulfate heptahydrate`, `di-Potassium hydrogen orthophosphate trihydrate`, and `Sodium dihydrogen orthophosphate monohydrate` remain ungrounded.

## Evidence

- The inspected TOGO M2237 API response supports the record name, the `TOGO:M2237` accession, and all 12 imported component rows.
- TOGO M2237 lists 1 L water plus gram amounts for every solute. The generated record preserves the TOGO numeric values as grams per liter, so the solute quantities match the one-liter source formulation.
- TOGO M2237 lists `Distilled water` as `1 L`; the generated record instead stores `1 G_PER_L`.
- The source has a free-text growth/incubation comment, `Cultures were grown at 30 C with shaking at 150 rev min-1 for 18 h`, that is absent from the generated record.
- The record has no direct primary citation for Hareland et al. 1975, no DOI, no PMID, no named target organism, and no strain-level growth evidence.

## Completeness

- Consequential gaps:
  - The solvent amount is dimensionally wrong and needs a volume/final-volume representation.
  - The 30 C, 150 rev/min, 18 h incubation detail needs to be retained if this record is meant to capture the TOGO source fully.
  - Three exact inorganic salts need ontology review and, where resolvable, exact CHEBI or MediaIngredientMech links.
- Correctly empty optional slots:
  - `solutions` is absent because TOGO M2237 lists all components directly.
  - `target_organisms`, `references`, and growth-evidence fields are empty because the inspected TOGO payload does not name a strain, organism, DOI, PMID, or explicit growth outcome.
  - CAS amino acids and Yeast extract are correctly ungrounded as mixture/undefined components.
- Bounded negative searches:
  - An exact gitignore-independent search for `Cultures were grown at 30` across `data`, `src`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found no local copy of the TOGO incubation sentence.
  - Exact gitignore-independent searches for `GMO_001125` and `M2237` found no maintained raw TOGO payload under the searched paths.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The one-liter water row is dimensionally wrong. | TOGO M2237 lists `Distilled water`, `volume: 1`, `unit: L`; the record stores `value: '1'`, `unit: G_PER_L`. | `data/normalized_yaml/bacterial/basal_salts_medium_bsm_modified_from_that_of_hareland_et_al_j_bacteriol_121_272_285_1975_by_removal_of_the_nitriloacetic_acid.yaml`; broad repeats should be fixed in TOGO import volume handling. |
| Major | Source incubation conditions were dropped. | The inspected TOGO comment states that cultures were grown at 30 C with shaking at 150 rev/min for 18 h, but the YAML has no temperature, agitation, duration, or note retaining this source context. | `data/normalized_yaml/bacterial/basal_salts_medium_bsm_modified_from_that_of_hareland_et_al_j_bacteriol_121_272_285_1975_by_removal_of_the_nitriloacetic_acid.yaml`. |
| Minor | Three exact salts are ungrounded. | Local exact searches and `data/import_tracking/reports/ungrounded_ingredients.tsv` show no term on cobalt sulfate heptahydrate, dipotassium hydrogen orthophosphate trihydrate, or sodium dihydrogen orthophosphate monohydrate. | `data/normalized_yaml/bacterial/basal_salts_medium_bsm_modified_from_that_of_hareland_et_al_j_bacteriol_121_272_285_1975_by_removal_of_the_nitriloacetic_acid.yaml`. |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/basal_salts_medium_bsm_modified_from_that_of_hareland_et_al_j_bacteriol_121_272_285_1975_by_removal_of_the_nitriloacetic_acid.yaml`, represent the solvent as `1 L` or a schema-supported one-liter final-volume row instead of `1 G_PER_L`.
2. Preserve the TOGO incubation comment as structured temperature, shaking, and duration fields where the schema supports them, or as a source-scoped preparation/incubation note.
3. Resolve exact CHEBI terms for cobalt sulfate heptahydrate, dipotassium hydrogen orthophosphate trihydrate, and sodium dihydrogen orthophosphate monohydrate; leave any unresolved salt explicit rather than grounding it to a generic parent.
4. Regenerate `data/merge_yaml/merged/basal_salts_medium_bsm_modified_from_that_of_hareland_et_al_j_bacteriol_121_272_285_1975_by_removal_of_the_nitriloacetic_acid.yaml` from the normalized owner.

## Follow-up Checks

- Rerun open-schema LinkML validation, `scripts/validate_strict.py`, `linkml-term-validator`, and the reference validator on the normalized owner after edits.
- Regenerate the generated merge and run `just verify-merges` plus `just audit-merge-freshness`.
- Re-fetch TOGO M2237 and manually compare every component amount and the incubation comment against the normalized record.
- Search `data/import_tracking/reports/ungrounded_ingredients.tsv` for `CultureMech:008825` after any grounding changes and confirm only Yeast extract and CAS amino acids remain ungrounded.

## Additional Notes

- The generated merge only adds the `merge_recipes.py` curation event, `merge_fingerprint`, and `merged_from`; scientific rows are inherited from the normalized owner.
- The exact gitignore-independent searches included ignored files where present.
