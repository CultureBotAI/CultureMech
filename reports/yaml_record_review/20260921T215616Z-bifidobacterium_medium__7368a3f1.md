# YAML Record Review: bifidobacterium_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/bifidobacterium_medium__7368a3f1.yaml
- Started UTC: 2026-09-21T21:55:00Z
- Finished UTC: 2026-09-21T21:56:16Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/bifidobacterium_medium__7368a3f1.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:001717` |
| Name | `bifidobacterium_medium` |
| Original name | `BIFIDOBACTERIUM MEDIUM` |
| Category | `bacterial` |
| Media term | `mediadive.medium:58` / `BIFIDOBACTERIUM MEDIUM` |
| Source lineage | DSMZ/MediaDive medium 58 plus 27 KOMODO `58_<DSM>` source duplicates |
| Merge fingerprint | `7368a3f1cd6e544362f37add9e3a10c2f296466dbc5597863cc79cdb15a1d5a9` |
| Merged from | `bifidobacterium_medium` and 27 `medium_58_modified_for_dsm_*` records |
| Generated status | Generated from `data/normalized_yaml/bacterial/bifidobacterium_medium.yaml` and its `SOURCE_DUPLICATE` variant owners; future fixes belong in those normalized owners or their MediaDive/KOMODO importers and must then regenerate `data/merge_yaml/merged/`. |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/bifidobacterium_medium__7368a3f1.yaml` | Passed. |
| Strict closed schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/bifidobacterium_medium__7368a3f1.yaml --out /private/tmp/bifidobacterium_medium__7368a3f1.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/bifidobacterium_medium__7368a3f1.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed structurally, but the file has no reference checks to perform: 1 file validated, 0 total checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/bifidobacterium_medium__7368a3f1.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed with only the known `eutils` / `pkg_resources` deprecation warning. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for standalone `history/` files, not a focused one-record check for embedded `MediaRecipe.curation_history` lists. |

The direct `just` targets were not rerun for this record because the project environment currently fails before target-specific validation while building `llvmlite==0.46.0` under Python 3.13; the commands above run the same validators in the cached Python 3.11 no-project environment used for this review batch.

## Identity and Grounding

- The direct owner `data/normalized_yaml/bacterial/bifidobacterium_medium.yaml` identifies DSMZ/MediaDive medium 58; the generated merge keeps that ID and folds in 27 KOMODO `58_<DSM>` normalized records that point back to DSMZ Medium 58 and are marked as `SOURCE_DUPLICATE`.
- The inspected MediaDive page identifies medium 58 as `BIFIDOBACTERIUM MEDIUM`, source `DSMZ`, taxonomic range `Bacteria`, type `Complex medium`, final pH 6.8, and a schema.org URI of `https://identifiers.org/mediadive.medium:58`. Those claims match the canonical direct owner.
- Ingredient groundings use plausible CHEBI terms for the resolved salts, glucose, Tween 80, resazurin, and cysteine hydrochloride hydrate. The reviewed defects are amount, unit, and stock-nesting defects rather than wrong CHEBI identities.
- An exact ignored-file-inclusive search over `data/normalized_yaml`, `data/merge_yaml`, `data/culturemech_id_registry.tsv`, `data/culturemech_recipe_catalog.tsv`, `reports`, `scripts`, and `history` for `CultureMech:001717`, the exact merge fingerprint, exact `mediadive.medium:58`, `medium_58_modified_for_dsm_16839`, and `bifidobacterium_medium__7368a3f1` found the expected direct owner, one inspected variant owner, generated merge, indexes, archived validation/report rows, and all of the `mediadive.medium:58` sibling owners.

## Evidence

### Source Claims That Are Supported

| Claim in record | Source check |
|---|---|
| DSMZ/MediaDive medium 58 is `BIFIDOBACTERIUM MEDIUM` with final pH 6.8. | Supported by the inspected live MediaDive medium 58 page. |
| The main solution includes 10 g/L casein peptone, 5 g/L yeast extract, 5 g/L meat extract, 5 g/L Bacto Soytone, 10 g/L glucose, 2 g/L K2HPO4, 0.2 g/L MgSO4 x 7 H2O, 0.05 g/L MnSO4 x H2O, and 0.5 g/L L-Cysteine HCl x H2O. | Supported by MediaDive's main-solution table, except the record has collapsed later stock-solution rows into the K2HPO4 and MgSO4 x 7 H2O final amounts. |
| The preparation boils and cools the medium under CO2, adjusts pH to 6.8 with 8 N NaOH, distributes under N2, and autoclaves. | Supported by the MediaDive medium 58 preparation text and preserved in the record as one `AUTOCLAVE` step. |

### Unsupported or Misplaced Claims

| Record claim | Source evidence | Assessment |
|---|---|---|
| `K2HPO4` is 3 g/L, `MgSO4 x 7 H2O` is 0.7 g/L, and `NaCl` is 7 g/L after duplicate merging. | MediaDive medium 58 has 2, 0.2, and 5 g/L direct main-solution rows, plus 40 ml/L of a salt stock that contains 1, 0.5, and 2 g/L respectively. MediaDive's molecular-composition export gives the salt-stock contributions as 0.04, 0.02, and 0.08 g/L. | Unsupported; the source stock concentrations were added as if they were direct final concentrations. |
| `CaCl2 x 2 H2O`, `KH2PO4`, and `NaHCO3` are direct final ingredients at 0.25, 1, and 10 g/L. | These appear only inside a `Salt solution` that is added at 40 ml/L. The final molecular-composition export reports 0.01, 0.04, and 0.4 g/L. | Unsupported stock/final collapse. |
| `Tween 80` and `Resazurin` are 1 and 4 g/L. | MediaDive lists Tween 80 as 1 ml/L and Resazurin as 4 ml/L of a 25 mg/100 ml stock. | Unsupported unit conversion; the source reports volume additions, not gram additions. |

## Completeness

- **Salt solution:** missing. MediaDive medium 58 uses a named `Salt solution` at 40 ml/L; the reviewed record has no `solutions` and flattens the stock ingredients into the final ingredient list.
- **Distilled water:** missing. MediaDive's main solution contains 950 ml distilled water and its salt solution contains 1000 ml distilled water; the reviewed record omits the solvent entirely.
- **Resazurin stock:** missing. The source adds 4 ml of 25 mg/100 ml resazurin, but the record only has a direct `4 G_PER_L` Resazurin row.
- **Direct references:** missing. Source recovery depends on free-text import notes; `references` is empty even though all 28 merged owners came from DSMZ/MediaDive or KOMODO records pointing to DSMZ Medium 58.
- **Growth claims:** no specific `target_organisms` or growth evidence are asserted in this record, so those optional slots are correctly empty for the inspected source recipe.
- **Report absence:** a `find` search over `reports/yaml_record_review` found no prior `*-bifidobacterium_medium__7368a3f1.md` report before this file was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Salt-solution contents were flattened and recorded at source-stock concentrations instead of final 40 ml/L contributions. | MediaDive medium 58 uses `40.00 ml` of `Salt solution`; that stock contains CaCl2 x 2 H2O 0.25 g/L, MgSO4 x 7 H2O 0.50 g/L, K2HPO4 1.00 g/L, KH2PO4 1.00 g/L, NaHCO3 10.00 g/L, NaCl 2.00 g/L, and distilled water to 1000 ml. The record stores those stock rows as final rows, and three rows were then summed with main-medium duplicates. | `data/normalized_yaml/bacterial/bifidobacterium_medium.yaml` and the 27 `medium_58_modified_for_dsm_*` owners; if the flattening was importer-owned, repair the MediaDive/KOMODO import path too. |
| Major | Volume and stock additions were converted into unsupported `G_PER_L` ingredient rows, while water was dropped. | MediaDive lists Tween 80 as `1.00 ml`, Resazurin as `4.00 ml` of a `25 mg/100ml` stock, and 950 ml distilled water in the main solution. The record stores Tween 80 as `1 G_PER_L`, Resazurin as `4 G_PER_L`, and has no main-solution water. | Same normalized owners as above. |
| Major | The cluster remains an active duplicate of the KOMODO base medium 58 record. | The reviewed merge groups the direct MediaDive owner and 27 KOMODO strain-specific owners, but an exact ignored-file-inclusive search also found `data/normalized_yaml/bacterial/KOMODO_58_BIFIDOBACTERIUM_medium.yaml` and generated merge `data/merge_yaml/merged/bifidobacterium_medium__4fefb4ac.yaml`, which independently point to DSMZ/MediaDive medium 58 with the same collapsed formula. | Duplicate metadata spanning this record's normalized owners and `data/normalized_yaml/bacterial/KOMODO_58_BIFIDOBACTERIUM_medium.yaml`. |
| Minor | Source provenance is recoverable only from free-text import notes. | The record has no `references`, `sources`, or `source_data`; the direct owner carries a free-text DSMZ link and the KOMODO variant owners carry `DSMZ Medium: 58 (mediadive.medium:58)` in `notes`. | Direct and KOMODO normalized owners in this merge. |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/bifidobacterium_medium.yaml` and the 27 `medium_58_modified_for_dsm_*` owners, replace flattened salt rows with a structured `Salt solution` added at 40 ml/L, or use MediaDive's final molecular-composition values without preserving the stock as direct final additions.
2. Preserve source units and stock semantics for 1 ml/L Tween 80, 4 ml/L of 25 mg/100 ml resazurin, and 950 ml main-solution distilled water.
3. Keep the MediaDive preparation step and ensure any structured salt/resazurin stocks do not erase the pH, CO2, N2, cysteine-addition, and autoclave instructions.
4. Add structured source provenance for DSMZ/MediaDive medium 58 and KOMODO `58_<DSM>` source IDs where the schema supports it.
5. Link or merge this 28-record cluster with `data/normalized_yaml/bacterial/KOMODO_58_BIFIDOBACTERIUM_medium.yaml` after the shared formula is source-accurate.
6. Regenerate `data/merge_yaml/merged/` after the normalized/source-owned corrections; never patch `data/merge_yaml/merged/bifidobacterium_medium__7368a3f1.yaml` directly.

## Follow-up Checks

- Run `just validate data/normalized_yaml/bacterial/bifidobacterium_medium.yaml` and a representative `medium_58_modified_for_dsm_*` owner after curation.
- Run `just verify-merges` and `just audit-merge-freshness` after the duplicate metadata and merge inputs are corrected.
- Re-run focused schema, strict, term, and reference validators on the regenerated `data/merge_yaml/merged/bifidobacterium_medium__7368a3f1.yaml` or its replacement merge fingerprint.
- Manually compare the regenerated recipe against MediaDive's medium 58 main solution, `Salt solution`, molecular-composition export, and preparation protocol to confirm the 40 ml/L stock dilution is represented correctly.
- Search with `rg --no-ignore --hidden` for exact `mediadive.medium:58` and `komodo.medium:58` after regeneration to confirm the direct DSMZ cluster and KOMODO base record no longer remain in separate generated canonical records when their ingredient/preparation signatures match.

## Additional Notes

- MediaDive's live HTML for medium 58, its JSON molecular-composition export, and its CSV molecular-composition export were downloaded and inspected during the immediately preceding review of `bifidobacterium_medium__4fefb4ac`. Those same source artifacts support this direct DSMZ/MediaDive 58 cluster.
- The inspected `medium_58_modified_for_dsm_16839` owner has the same erroneous flattened amounts as `bifidobacterium_medium.yaml` and explicitly points back to `bifidobacterium_medium` as `SOURCE_DUPLICATE`, supporting the generated merge relationship but not the ingredient amounts.
