# YAML Record Review: rcm_medium_with_sea_salts

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/rcm_medium_with_sea_salts.yaml
- Started UTC: 2026-09-25T01:27:46Z
- Finished UTC: 2026-09-25T01:27:56Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/rcm_medium_with_sea_salts.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:001767` |
| Label | `rcm_medium_with_sea_salts` |
| Original label | `RCM MEDIUM (with Sea Salts)` |
| Category | `bacterial` |
| Source | `mediadive.medium:634b` |
| Source document | `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium634b.pdf` |
| Generated status | Generated canonical merge under `data/merge_yaml/merged`; do not edit directly |
| Maintained owner | `data/normalized_yaml/bacterial/rcm_medium_with_sea_salts.yaml` |
| Merged from | `rcm_medium_with_sea_salts` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/rcm_medium_with_sea_salts.yaml` | Passed; the validator reported `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/rcm_medium_with_sea_salts.yaml --out /private/tmp/rcm_medium_with_sea_salts.strict.tsv --workers 1 --quiet` | Passed with 0 errors; the TSV had its header only. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/rcm_medium_with_sea_salts.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were present. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/rcm_medium_with_sea_salts.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the validator emitted the known `eutils` `pkg_resources` deprecation warning. |
| Embedded history | `just validate-history` | Not checked: this repository command validates standalone `history/` records, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

## Identity and Grounding

The generated record identifies DSMZ Medium 634b / MediaDive `mediadive.medium:634b`, and its ID, label, original label, `media_term`, source URL, and `merged_from` all agree with that target.

A fresh DSMZ 634b PDF fetch from the record's source URL rendered as `634b: RCM MEDIUM (with Sea Salts)` with final pH 6.8, final volume 1000 ml, 38 g dehydrated RCM medium, 30 g SIGMA Sea Salts, 0.50 ml of 0.1% w/v sodium resazurin, 1000 ml distilled water, 100% N2 sparging, anoxic Hungate tubes or serum vials, 15 min autoclaving at 121 C, and final adjustment to pH 6.8. The generated record's formula and preparation step preserve those target-defining claims.

An exact gitignore-independent search over `data/normalized_yaml`, `data/merge_yaml`, `reports/yaml_record_review`, and `reports/media_content_review_manifest.tsv` for `rcm_medium_with_sea_salts`, `mediadive.medium:634b`, `DSMZ_Medium634b`, `CultureMech:001767`, `rcm_medium_halophilic_clostridia`, `komodo.medium:634b`, and `CultureMech:006150` found the maintained MediaDive 634b owner, this generated output, index/manifest entries, the previous 634c review report that cited the stale KOMODO 634b owner, and `data/normalized_yaml/bacterial/rcm_medium_halophilic_clostridia.yaml`. The stale KOMODO owner also denotes DSMZ 634b but was not merged with this target because its copied formula is currently the DSMZ 634c formula.

The Sodium resazurin ingredient is grounded to `CHEBI:8806` Resazurin, which is the corpus-consensus grounding for this indicator. The Sea salts row is intentionally ungrounded; the maintained owner marks the dehydrated RCM medium and Sea salts rows as reviewed opaque ingredients.

## Evidence

The inspected DSMZ 634b PDF supports the medium identity, pH, ingredient set, and preparation text:

| Claim in generated record | Source support |
|---|---|
| `38` `G_PER_L` dehydrated RCM medium | Supported by the DSMZ 634b 1000 ml formula. |
| `30` `G_PER_L` Sea salts | Supported by the DSMZ 634b 1000 ml formula, which names SIGMA Sea Salts. |
| `0.0005` `G_PER_L` Sodium resazurin | Supported by 0.5 ml/L of a 0.1% w/v sodium resazurin stock, which equals 0.5 mg/L or 0.0005 g/L. |
| `ph_value: 6.8` | Supported by the final pH line and the final pH adjustment in the preparation text. |
| Boil/cool under 100% N2, dispense anoxically, autoclave 15 min at 121 C | Supported by the DSMZ preparation paragraph. |

No unsupported medium-formula claim was found in the generated MediaDive 634b target itself.

## Completeness

The target has no `target_organisms`, `growth_metrics`, strain-specific incubation conditions, literature evidence, or growth references. That is acceptable for this source-only DSMZ recipe: the inspected source is a formulation sheet, not a growth experiment.

The DSMZ formula's 1000 ml distilled water is represented in the preparation text as the solvent boundary and is not retained as a final `ingredients` row. That does not change the reconstructable final formula.

The exact gitignore-independent search described above did not find another MediaDive 634b owner in the checked normalized or merge outputs. It did find one KOMODO 634b sibling that should eventually become source-equivalent with this record after its stale 634c formula is repaired.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The corpus still has a stale KOMODO 634b owner outside this 634b merge group. | `data/normalized_yaml/bacterial/rcm_medium_halophilic_clostridia.yaml` names `komodo.medium:634b` and DSMZ Medium 634b, but its ingredient list omits the required 30 g/L Sea salts and contains 1 g/L sodium carbonate copied from DSMZ 634c. | `data/normalized_yaml/bacterial/rcm_medium_halophilic_clostridia.yaml`; DSMZ/KOMODO resolver; merge equivalence rules |
| Minor | The generated 634b record lags its maintained owner. | `data/normalized_yaml/bacterial/rcm_medium_with_sea_salts.yaml` now carries an `ingredients_curated` / `has_unmapped_ingredients` review event from 2026-09-13, while this generated output was last merged on 2026-08-06 and lacks those maintained flags and curation history. | Merge generation for `data/merge_yaml/merged/rcm_medium_with_sea_salts.yaml` |

## Recommended Edits

1. Rebuild `data/normalized_yaml/bacterial/rcm_medium_halophilic_clostridia.yaml` from the real DSMZ 634b / KOMODO 634b formula: add 30 g/L SIGMA Sea Salts, remove the copied 1 g/L sodium carbonate, and preserve DSMZ 634b pH 6.8 and 100% N2 preparation semantics.
2. Recompute MediaRecipe merge equivalence so the repaired KOMODO 634b owner either merges into `rcm_medium_with_sea_salts` as a source duplicate or is explicitly related without carrying a false 634c formula.
3. Regenerate `data/merge_yaml/merged/rcm_medium_with_sea_salts.yaml` from `data/normalized_yaml/bacterial/rcm_medium_with_sea_salts.yaml` so the 2026-09-13 opaque-ingredient review flags and curation history propagate to the canonical merge layer.

## Follow-up Checks

1. Run strict, term, and reference validation on `data/normalized_yaml/bacterial/rcm_medium_halophilic_clostridia.yaml` after rebuilding the KOMODO 634b owner.
2. Run the repository merge verifier after regenerating `data/merge_yaml/merged` to confirm DSMZ 634b no longer splits from or falsely merges with DSMZ 634c.
3. Reopen the regenerated `rcm_medium_with_sea_salts.yaml` and the 634c output to confirm `merged_from` no longer misplaces the KOMODO 634b owner.

## Additional Notes

The direct MediaDive 634b formula is source-faithful; the major finding is a sibling-owner defect, not a transcription defect in `data/normalized_yaml/bacterial/rcm_medium_with_sea_salts.yaml`.
