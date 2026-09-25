# YAML Record Review: reactivation_with_liquid_medium_1

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/reactivation_with_liquid_medium_1__7d42c4b3.yaml
- Started UTC: 2026-09-25T01:38:13Z
- Finished UTC: 2026-09-25T01:38:45Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/reactivation_with_liquid_medium_1__7d42c4b3.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:001298` |
| Label | `reactivation_with_liquid_medium_1` |
| Original label | `REACTIVATION WITH LIQUID MEDIUM 1` |
| Category | `bacterial` |
| Source | `mediadive.medium:1a` |
| Generated status | Generated canonical merge under `data/merge_yaml/merged`; do not edit directly |
| Maintained owners | `data/normalized_yaml/bacterial/reactivation_with_liquid_medium_1.yaml`, `data/normalized_yaml/bacterial/nutrient_agar.yaml` |
| Merged from | `nutrient_agar`, `reactivation_with_liquid_medium_1` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/reactivation_with_liquid_medium_1__7d42c4b3.yaml` | Passed; exited 0 with no diagnostics. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/reactivation_with_liquid_medium_1__7d42c4b3.yaml --out /private/tmp/reactivation_with_liquid_medium_1__7d42c4b3.strict.tsv --workers 1 --quiet` | Passed with 0 errors; the TSV had its header only. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/reactivation_with_liquid_medium_1__7d42c4b3.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were present. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/reactivation_with_liquid_medium_1__7d42c4b3.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the validator emitted the known `eutils` `pkg_resources` deprecation warning. |
| Embedded history | `just validate-history` | Not checked: this repository command validates standalone `history/` records, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

## Identity and Grounding

The generated record identifies DSMZ/MediaDive medium 1a, a reactivation protocol that tells the curator to grow lyophilized cells from an ampoule in 5 ml liquid broth 1 before subculturing in liquid medium or on agar plates. DSMZ/MediaDive medium 1 is ordinary NUTRIENT AGAR with the same basal peptone, meat-extract, agar, and pH formula but without the 1a reactivation instruction.

A narrowed gitignore-independent search over `data/normalized_yaml/bacterial/reactivation_with_liquid_medium_1.yaml`, `data/normalized_yaml/bacterial/nutrient_agar.yaml`, `data/merge_yaml/merged/reactivation_with_liquid_medium_1__7d42c4b3.yaml`, and `reports/media_content_review_manifest.tsv` for exact source IDs, CultureMech IDs, and DSMZ PDF names found the two normalized owners, two manifest rows, and this generated output.

The generated target carries `kg_microbe_match: mediadive.medium:12`. MediaDive medium 12 is `SOIL EXTRACT MEDIUM`, a garden-soil/tap-water/agar recipe at pH 6.8-7.0, so that external match is unrelated to either DSMZ 1a or DSMZ 1.

## Evidence

The inspected DSMZ 1a PDF and MediaDive 1a API record support the generated 1a formula:

| Claim in generated record | Source support |
|---|---|
| `5` `G_PER_L` Peptone | Supported by DSMZ/MediaDive 1a. |
| `3` `G_PER_L` Meat extract | Supported by DSMZ/MediaDive 1a. |
| `15` `G_PER_L` Agar for solid medium | Supported by DSMZ/MediaDive 1a. |
| pH 7.0 and 10 mg MnSO4 x H2O Bacillus sporulation note | Supported by DSMZ/MediaDive 1a. |
| Rehydration and 5 ml liquid broth 1 instruction | Supported by DSMZ/MediaDive 1a only; not present in DSMZ/MediaDive 1. |

DSMZ/MediaDive 1 supports the same ingredient and pH formula but is labeled `NUTRIENT AGAR`; it does not support treating `nutrient_agar` as a synonym for the 1a reactivation protocol.

## Completeness

The generated target is stale relative to `data/normalized_yaml/bacterial/reactivation_with_liquid_medium_1.yaml`: the normalized owner now links TOGO M2358 as a source duplicate and TOGO M2359 as a 10 mg/L MnSO4 x H2O supplemented variant, and it grounds Peptone through the local exact ingredient index. Those September 2026 curation events are absent from the August 2026 generated merge.

The target has no `target_organisms`, `growth_metrics`, strain-specific incubation conditions, literature evidence, or growth references. That is acceptable for this source-only DSMZ recipe: the inspected source is a formulation/reactivation sheet, not a growth experiment.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated record falsely merges DSMZ Medium 1a with DSMZ Medium 1. | Medium 1a is a reactivation protocol with an ampoule rehydration instruction; Medium 1 is ordinary Nutrient Agar. The generated output merges `nutrient_agar` into the 1a record as a synonym because the basal formula fingerprint is identical. | Merge equivalence rules for MediaRecipe generation |
| Major | `kg_microbe_match` points to an unrelated MediaDive medium. | The generated output and both normalized owners carry `kg_microbe_match: mediadive.medium:12`; inspected MediaDive 12 is Soil Extract Medium, not DSMZ 1a or DSMZ 1. | `data/normalized_yaml/bacterial/reactivation_with_liquid_medium_1.yaml`; `data/normalized_yaml/bacterial/nutrient_agar.yaml`; external-match generation |
| Minor | The generated 1a output lags its maintained owner. | The maintained DSMZ 1a owner carries September 2026 TOGO variant/source-duplicate links and a Peptone grounding, but this generated output was last merged in August 2026. | Merge generation for `data/merge_yaml/merged/reactivation_with_liquid_medium_1__7d42c4b3.yaml` |

## Recommended Edits

1. Change merge equivalence so DSMZ 1 and DSMZ 1a remain separate generated records or are related explicitly without making Nutrient Agar a synonym of the 1a reactivation protocol.
2. Remove or recompute the false `kg_microbe_match: mediadive.medium:12` on both maintained owners.
3. Regenerate `data/merge_yaml/merged/reactivation_with_liquid_medium_1__7d42c4b3.yaml` from the repaired normalized owners so the September 2026 TOGO relationships and Peptone grounding propagate.

## Follow-up Checks

1. Run strict, term, and reference validation on `data/normalized_yaml/bacterial/reactivation_with_liquid_medium_1.yaml` and `data/normalized_yaml/bacterial/nutrient_agar.yaml` after the match repair.
2. Run the repository merge verifier and inspect generated outputs for DSMZ 1 and 1a to confirm the 1a reactivation instruction no longer collapses into Nutrient Agar.
3. Manually recheck MediaDive 1a, MediaDive 1, and MediaDive 12 after regeneration to confirm the medium identities are no longer conflated.

## Additional Notes

An earlier search for `kg_microbe_match: mediadive.medium:12` was discarded because that stale match is systemic and returned many unrelated records. The evidence above uses the narrowed search over the two maintained owners and the reviewed generated output.
