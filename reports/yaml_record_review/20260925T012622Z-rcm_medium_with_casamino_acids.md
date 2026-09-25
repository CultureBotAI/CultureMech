# YAML Record Review: rcm_medium_with_casamino_acids

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/rcm_medium_with_casamino_acids.yaml
- Started UTC: 2026-09-25T01:25:55Z
- Finished UTC: 2026-09-25T01:26:22Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/rcm_medium_with_casamino_acids.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:001766` |
| Label | `rcm_medium_with_casamino_acids` |
| Original label | `RCM MEDIUM (with Casamino acids)` |
| Category | `bacterial` |
| Source | `mediadive.medium:634a` |
| Source document | `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium634a.pdf` |
| Generated status | Generated canonical merge under `data/merge_yaml/merged`; do not edit directly |
| Maintained owner | `data/normalized_yaml/bacterial/rcm_medium_with_casamino_acids.yaml` |
| Merged from | `rcm_medium_with_casamino_acids` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/rcm_medium_with_casamino_acids.yaml` | Passed; exited 0 with no diagnostics. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/rcm_medium_with_casamino_acids.yaml --out /private/tmp/rcm_medium_with_casamino_acids.strict.tsv --workers 1 --quiet` | Passed with 0 errors; the TSV had its header only. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/rcm_medium_with_casamino_acids.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were present. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/rcm_medium_with_casamino_acids.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the validator emitted the known `eutils` `pkg_resources` deprecation warning. |
| Embedded history | `just validate-history` | Not checked: this repository command validates standalone `history/` records, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

## Identity and Grounding

The generated record identifies DSMZ Medium 634a / MediaDive `mediadive.medium:634a`, and its ID, label, original label, `media_term`, `kg_microbe_match`, and `merged_from` all agree with that target.

A fresh DSMZ 634a PDF fetch from the record's source URL rendered as `634a: RCM MEDIUM (with Casamino acids)` with final pH 6.8, final volume 1000 ml, 38 g dehydrated RCM medium, 15 g Casamino acids, 0.50 ml of 0.1% w/v sodium resazurin, 1000 ml distilled water, 100% N2 sparging, anoxic Hungate tubes or serum vials, 15 min autoclaving at 121 C, and final adjustment to pH 6.8. The generated record's formula and preparation step preserve those target-defining claims.

An exact gitignore-independent search over `data/normalized_yaml`, `data/merge_yaml`, `reports/yaml_record_review`, and `reports/media_content_review_manifest.tsv` for `mediadive.medium:634a`, `CultureMech:001766`, `DSMZ_Medium634a`, `rcm_medium_with_casamino_acids`, `rcm_medium_modified`, `komodo.medium:634a`, and `CultureMech:006149` found the maintained MediaDive 634a owner, this generated output, index/manifest entries, the previous 634c review report that cited the stale KOMODO 634a owner, and `data/normalized_yaml/bacterial/rcm_medium_modified.yaml`. The stale KOMODO owner also denotes DSMZ 634a but was not merged with this target because its copied formula is currently the DSMZ 634c formula.

The Sodium resazurin ingredient is grounded to `CHEBI:8806` Resazurin, which is the corpus-consensus grounding for this indicator. Casamino acids are intentionally left ungrounded in this generated output, although the maintained owner has since added `FOODON:03315719` and should be regenerated into the merge layer.

## Evidence

The inspected DSMZ 634a PDF supports the medium identity, pH, ingredient set, and preparation text:

| Claim in generated record | Source support |
|---|---|
| `38` `G_PER_L` dehydrated RCM medium | Supported by the DSMZ 634a 1000 ml formula. |
| `15` `G_PER_L` Casamino acids | Supported by the DSMZ 634a 1000 ml formula and repeated in the preparation note. |
| `0.0005` `G_PER_L` Sodium resazurin | Supported by 0.5 ml/L of a 0.1% w/v sodium resazurin stock, which equals 0.5 mg/L or 0.0005 g/L. |
| `ph_value: 6.8` | Supported by the final pH line and the final pH adjustment in the preparation text. |
| Boil/cool under 100% N2, dispense anoxically, autoclave 15 min at 121 C | Supported by the DSMZ preparation paragraph. |

No unsupported medium-formula claim was found in the generated MediaDive 634a target itself.

## Completeness

The target has no `target_organisms`, `growth_metrics`, strain-specific incubation conditions, literature evidence, or growth references. That is acceptable for this source-only DSMZ recipe: the inspected source is a formulation sheet, not a growth experiment.

The DSMZ formula's 1000 ml distilled water is represented in the preparation text as the solvent boundary and is not retained as a final `ingredients` row. That does not change the reconstructable final formula.

The exact gitignore-independent search described above did not find another MediaDive 634a owner in the checked normalized or merge outputs. It did find one KOMODO 634a sibling that should eventually become source-equivalent with this record after its stale 634c formula is repaired.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The corpus still has a stale KOMODO 634a owner outside this 634a merge group. | `data/normalized_yaml/bacterial/rcm_medium_modified.yaml` names `komodo.medium:634a` and DSMZ Medium 634a, but its ingredient list omits the required 15 g/L Casamino acids and contains 1 g/L sodium carbonate copied from DSMZ 634c. | `data/normalized_yaml/bacterial/rcm_medium_modified.yaml`; DSMZ/KOMODO resolver; merge equivalence rules |
| Minor | The generated 634a record lags its maintained owner. | `data/normalized_yaml/bacterial/rcm_medium_with_casamino_acids.yaml` now grounds Casamino acids to `FOODON:03315719` and carries the 2026-09-13 exact-term curation event, while this generated output was last merged on 2026-08-06 and lacks both the term and event. | Merge generation for `data/merge_yaml/merged/rcm_medium_with_casamino_acids.yaml` |

## Recommended Edits

1. Rebuild `data/normalized_yaml/bacterial/rcm_medium_modified.yaml` from the real DSMZ 634a / KOMODO 634a formula: add 15 g/L Casamino acids, remove the copied 1 g/L sodium carbonate, and preserve DSMZ 634a pH 6.8 and 100% N2 preparation semantics.
2. Recompute MediaRecipe merge equivalence so the repaired KOMODO 634a owner either merges into `rcm_medium_with_casamino_acids` as a source duplicate or is explicitly related without carrying a false 634c formula.
3. Regenerate `data/merge_yaml/merged/rcm_medium_with_casamino_acids.yaml` from `data/normalized_yaml/bacterial/rcm_medium_with_casamino_acids.yaml` so the current Casamino acids FOODON grounding and 2026-09-13 curation history propagate to the canonical merge layer.

## Follow-up Checks

1. Run strict, term, and reference validation on `data/normalized_yaml/bacterial/rcm_medium_modified.yaml` after rebuilding the KOMODO 634a owner.
2. Run the repository merge verifier after regenerating `data/merge_yaml/merged` to confirm DSMZ 634a no longer splits from or falsely merges with DSMZ 634c.
3. Reopen the regenerated `rcm_medium_with_casamino_acids.yaml` and the 634c output to confirm `merged_from` no longer misplaces the KOMODO 634a owner.

## Additional Notes

The direct MediaDive 634a formula is source-faithful; the major finding is a sibling-owner defect, not a transcription defect in `data/normalized_yaml/bacterial/rcm_medium_with_casamino_acids.yaml`.
