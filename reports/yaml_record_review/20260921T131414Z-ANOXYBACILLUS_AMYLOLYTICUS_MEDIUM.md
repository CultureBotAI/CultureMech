# YAML Record Review: ANOXYBACILLUS AMYLOLYTICUS medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ANOXYBACILLUS_AMYLOLYTICUS_MEDIUM.yaml
- Started UTC: 2026-09-21T13:13:35Z
- Finished UTC: 2026-09-21T13:14:15Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:003604` / `anoxybacillus_amylolyticus_medium` in `data/merge_yaml/merged/ANOXYBACILLUS_AMYLOLYTICUS_MEDIUM.yaml`.

- The generated record was produced by `merge_recipes.py` from `KOMODO_1046_ANOXYBACILLUS_AMYLOLYTICUS_medium.yaml` and `anoxybacillus_amylolyticus_medium.yaml`.
- The maintained owners are `data/normalized_yaml/bacterial/KOMODO_1046_ANOXYBACILLUS_AMYLOLYTICUS_medium.yaml` and `data/normalized_yaml/bacterial/anoxybacillus_amylolyticus_medium.yaml`.
- An ignored-inclusive exact search across `data`, `.claude`, and `reports` for `ANOXYBACILLUS_AMYLOLYTICUS_MEDIUM`, `Anoxybacillus Amylolyticus Medium`, `ANOXYBACILLUS AMYLOLYTICUS MEDIUM`, and `Anoxybacillus amylolyticus` found only the expected normalized inputs, this generated merge, registry/index/report rows, and unrelated `Desulfurococcus amylolyticus` records that share only the species epithet.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ANOXYBACILLUS_AMYLOLYTICUS_MEDIUM.yaml` through the Python 3.11 no-project workaround | Pass; no issues found. |
| `python scripts/validate_strict.py data/merge_yaml/merged/ANOXYBACILLUS_AMYLOLYTICUS_MEDIUM.yaml --out /private/tmp/anoxybacillus_amylolyticus.strict.tsv --workers 1 --quiet` through the Python 3.11 no-project workaround | Pass; 1 file scanned and 0 error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/ANOXYBACILLUS_AMYLOLYTICUS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` through the Python 3.11 no-project workaround | Pass; 0 reference checks were discovered. |
| `linkml-term-validator validate-data data/merge_yaml/merged/ANOXYBACILLUS_AMYLOLYTICUS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` through the Python 3.11 no-project workaround | Pass; only the known `eutils` `pkg_resources` deprecation warning was emitted. |
| Embedded `MediaRecipe.curation_history` | Not checked: the documented `just validate-history` gate targets standalone files under `history/`, not embedded history on one generated merge record. |

The documented `just validate-schema`, `just validate-strict`, `just validate-references`, and `just validate-terms` wrappers were not rerun directly because project-level `uv` attempts to build `llvmlite==0.46.0` under Python 3.13 and fails before any target-specific validation begins. The equivalent LinkML/strict/reference/term checks above were run with `uv run --no-project --python /usr/local/bin/python3.11`.

## Identity and Grounding

The record denotes DSMZ/KOMODO medium 1046, `ANOXYBACILLUS AMYLOLYTICUS MEDIUM`. The two normalized inputs correctly identify the same DSMZ medium number through `mediadive.medium:1046` and `komodo.medium:1046`, and the generated merge records their `SOURCE_DUPLICATE` relationship.

NaCl is correctly grounded to `CHEBI:26710` / `sodium chloride`. `Yeast extract` is appropriately left ungrounded because it is an undefined mixture. `Tap water` is over-grounded to `CHEBI:15377` / `water`; DSMZ specifies tap water, not chemically pure water.

## Evidence

The inspected DSMZ Medium 1046 PDF supports the scientific core of the record: it names the medium `ANOXYBACILLUS AMYLOLYTICUS MEDIUM` and lists 6.0 g yeast extract, 6.0 g NaCl, 1000.0 ml tap water, and pH adjustment to 5.6. The `medium_type: COMPLEX`, `composition_type: UNDEFINED`, `physical_state: LIQUID`, bacterial category, and source-duplicate merge of DSMZ 1046 with KOMODO 1046 are consistent with those local and external sources.

## Completeness

The generated merge lost the explicit `preparation_steps` entry from the DSMZ/MediaDive owner. The pH value remains as `ph_value: 5.6`, so the omission is not as severe as losing pH entirely, but the maintained input does carry `action: ADJUST_PH` with `description: adjust pH 5.6` and the source phrase is a preparation instruction.

No target organism is required solely from the medium name; the DSMZ PDF is only a medium formulation and does not provide an organism evidence table.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Tap water is represented with a mass unit and grounded as pure water. | DSMZ Medium 1046 says `Tap water` at 1000.0 ml. Both normalized inputs and the generated merge store `value: '1000'`, `unit: G_PER_L`, and link the row to `CHEBI:15377` / `water`, which changes both the unit and the ingredient identity. | Both normalized 1046 inputs or the DSMZ/KOMODO import normalizer. |
| minor | The merged record omits the DSMZ pH adjustment step. | `data/normalized_yaml/bacterial/anoxybacillus_amylolyticus_medium.yaml` retains `adjust pH 5.6`; the generated merge retains `ph_value: 5.6` but no `preparation_steps`. | Merge rules for source-duplicate DSMZ/KOMODO pairs. |
| minor | The KOMODO curation history contains a malformed timestamp that propagated into the merge. | The first KOMODO event is `2026-01-27T01:15:01.fZ`; a literal `f` is not a fractional-second field. Strict validation currently treats embedded timestamps leniently and does not catch it. | `data/normalized_yaml/bacterial/KOMODO_1046_ANOXYBACILLUS_AMYLOLYTICUS_medium.yaml`. |

## Recommended Edits

1. Preserve DSMZ tap water as a volume of tap water; do not ground it to pure `CHEBI:15377` unless a tap-water ingredient class intentionally maps to water while preserving the displayed source name.
2. Merge the DSMZ `ADJUST_PH` preparation step into the generated SOURCE_DUPLICATE record or make the merge prefer the DSMZ record as canonical when the KOMODO side only adds the same medium number.
3. Normalize the KOMODO import timestamp to a valid ISO 8601 value or annotate the failed fractional second parse before regenerating.
4. Regenerate `data/merge_yaml/merged/ANOXYBACILLUS_AMYLOLYTICUS_MEDIUM.yaml` from normalized data instead of hand-editing it.

## Follow-up Checks

- Rerun focused open-schema, strict, reference, and term validation on both normalized DSMZ/KOMODO 1046 inputs.
- Rerun `just verify-merges` and `just audit-merge-freshness` after any merge-rule repair.
- Inspect the regenerated merge and confirm it still merges exactly the two DSMZ/KOMODO 1046 owners while preserving the pH adjustment.

## Additional Notes

The KOMODO note `Aerobic: No` was not cross-checked against ModelSEED because the DSMZ PDF does not carry an aerobic/anaerobic flag; no finding is made for that free-text note.
