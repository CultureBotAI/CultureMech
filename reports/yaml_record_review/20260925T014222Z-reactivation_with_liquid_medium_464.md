# YAML Record Review: reactivation_with_liquid_medium_464

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/reactivation_with_liquid_medium_464.yaml
- Started UTC: 2026-09-25T01:42:11Z
- Finished UTC: 2026-09-25T01:42:22Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/reactivation_with_liquid_medium_464.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:005520` |
| Label | `reactivation_with_liquid_medium_464` |
| Original label | `REACTIVATION WITH LIQUID medium 464` |
| Category | `bacterial` |
| Source | `komodo.medium:464a`, a KOMODO duplicate of `mediadive.medium:464a` |
| Generated status | Generated canonical merge under `data/merge_yaml/merged`; do not edit directly |
| Intended 464a owners | `data/normalized_yaml/bacterial/reactivation_with_liquid_medium_464.yaml`, `data/normalized_yaml/bacterial/KOMODO_464a_REACTIVATION_WITH_LIQUID_medium_464.yaml`, `data/normalized_yaml/bacterial/reactivation_with_liquid_medium_464_plate_count_agar.yaml` |
| Incorrectly merged 464 owners | DSMZ 464 / Plate Count Agar owners and KOMODO DSM-strain copies listed in `merged_from` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/reactivation_with_liquid_medium_464.yaml` | Passed; the validator reported `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/reactivation_with_liquid_medium_464.yaml --out /private/tmp/reactivation_with_liquid_medium_464.strict.tsv --workers 1 --quiet` | Passed with 0 errors; the TSV had its header only. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/reactivation_with_liquid_medium_464.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were present. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/reactivation_with_liquid_medium_464.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the validator emitted the known `eutils` `pkg_resources` deprecation warning. |
| Embedded history | `just validate-history` | Not checked: this repository command validates standalone `history/` records, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

## Identity and Grounding

The generated record identifies KOMODO 464a / DSMZ Medium 464a, `REACTIVATION WITH LIQUID medium 464`, but the merge group also includes DSMZ Medium 464 `PLATE COUNT AGAR`, its KOMODO source duplicate, and ten KOMODO DSM-strain copies of DSMZ 464. The DSMZ 464a PDF and MediaDive 464a API make 464a a reactivation protocol: grow lyophilized cells from the ampoule in liquid medium 464 before subsequent subculture in liquid or agar medium. DSMZ 464 is only the underlying Plate Count Agar formula with pH 7.0.

An exact gitignore-independent search over `data/normalized_yaml`, `data/merge_yaml`, `reports/media_content_review_manifest.tsv`, and `reports/yaml_record_review` for exact 464/464a slugs, source IDs, and CultureMech IDs found the direct MediaDive 464a and 464 owners, KOMODO 464a and 464 owners, the ten KOMODO DSM-strain copies of 464 that point to `KOMODO_464_PLATE_COUNT_AGAR.yaml`, the TOGO M2310 normalized source duplicate of 464a, and this generated output. It did not find a generated output that correctly groups all three 464a owners without ordinary DSMZ 464.

The generated target also uses the KOMODO 464a owner as canonical and therefore drops the reactivation preparation instruction carried by the direct MediaDive 464a owner. It is stale relative to the September 2026 TOGO M2310 repair, which linked `reactivation_with_liquid_medium_464_plate_count_agar.yaml` as a 464a source duplicate with an explicit 1 L distilled-water row.

## Evidence

The inspected DSMZ/MediaDive 464a source supports a two-level recipe:

| Source identity | Supported claim |
|---|---|
| DSMZ 464, `PLATE COUNT AGAR` | 5 g Tryptone, 2.5 g Yeast extract, 1 g Dextrose, 15 g Agar if required, 1000 ml Distilled water, pH 7.0. |
| DSMZ 464a, `REACTIVATION WITH LIQUID MEDIUM 464` | Rehydrate and grow lyophilized cells from the ampoule in liquid medium 464, then subculture in liquid medium or agar medium. |
| KOMODO 464a | A duplicate formula of DSMZ 464a that states DSMZ Medium 464a provenance but does not carry DSMZ/MediaDive preparation steps. |
| TOGO M2310 | A TOGO import of DSMZ 464a repaired locally on September 12, 2026 as a 464a source duplicate. |

The flattened ingredient list in the generated output is compatible with both DSMZ 464 and 464a because 464a references solution 464. The source accessions are still not synonymous: 464a is the reactivation protocol, and 464 is the ordinary Plate Count Agar medium.

## Completeness

The generated target has no `preparation_steps`, so it cannot represent the 464a source-defining lyophilized-cell reactivation instruction. It also omits the source-supported 1000 ml distilled water retained in the repaired TOGO M2310 owner.

The target has no `target_organisms`, `growth_metrics`, strain-specific incubation conditions, literature evidence, or growth references. That is acceptable for this source-only DSMZ recipe: the inspected source is a formulation/reactivation sheet, not a growth experiment.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | The generated 464a target falsely merges the reactivation protocol with ordinary DSMZ 464 Plate Count Agar and DSMZ 464 strain copies. | The generated `merged_from` list includes `plate_count_agar`, KOMODO 464, and ten KOMODO `medium_464_modified_for_dsm_*` records. DSMZ 464a includes a reactivation instruction that distinguishes it from the DSMZ 464 Plate Count Agar source. | Merge equivalence rules for MediaRecipe generation |
| Major | The generated target drops the 464a reactivation preparation step. | `data/normalized_yaml/bacterial/reactivation_with_liquid_medium_464.yaml` carries the source-supported instruction to rehydrate lyophilized cells in liquid medium 464; the KOMODO 464a owner and generated record have no `preparation_steps`. | Source-duplicate merge projection |
| Major | The generated 464a record is stale relative to the maintained 464a parent. | The maintained 464a parent now links the repaired TOGO M2310 source duplicate; the generated August 2026 output instead merged DSMZ 464 records and leaves TOGO M2310 split in a separate generated file. | Merge generation for `data/merge_yaml/merged/reactivation_with_liquid_medium_464.yaml` |

## Recommended Edits

1. Change merge equivalence so DSMZ/MediaDive 464a remains separate from DSMZ/MediaDive 464 and its KOMODO strain-specific copies.
2. Regenerate the 464a merge so `reactivation_with_liquid_medium_464`, `KOMODO_464a_REACTIVATION_WITH_LIQUID_medium_464`, and `reactivation_with_liquid_medium_464_plate_count_agar` merge together as source duplicates.
3. Update source-duplicate merge projection so a KOMODO 464a canonical record can inherit non-conflicting `preparation_steps`, references, and retained source rows from the direct MediaDive or TOGO 464a owners.

## Follow-up Checks

1. Run the repository merge verifier after changing the 464/464a equivalence behavior.
2. Run strict, term, and reference validation on the regenerated 464 and 464a generated outputs.
3. Manually recheck MediaDive 464, MediaDive 464a, and TOGO M2310 to confirm that Plate Count Agar no longer becomes a synonym of the 464a reactivation protocol.

## Additional Notes

The first local filename probe used the broad `*464*` pattern and was discarded because it found unrelated records whose identifiers merely contain `464`. The report evidence uses the exact 464/464a source-ID and slug search described above.
