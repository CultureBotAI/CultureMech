# YAML Record Review: bifidobacterium_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/bifidobacterium_medium__4fefb4ac.yaml
- Started UTC: 2026-09-21T21:49:40Z
- Finished UTC: 2026-09-21T21:52:48Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/bifidobacterium_medium__4fefb4ac.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:006069` |
| Name | `bifidobacterium_medium` |
| Original name | `BIFIDOBACTERIUM medium` |
| Category | `bacterial` |
| Media term | `komodo.medium:58` / `BIFIDOBACTERIUM medium` |
| Source lineage | KOMODO ModelSEED ID 58 enriched from DSMZ/MediaDive medium 58 |
| Merge fingerprint | `4fefb4ac4f56b96641edf9512640588acbfcf55689bfd6423385b9dbee27c240` |
| Merged from | `KOMODO_58_BIFIDOBACTERIUM_medium` |
| Generated status | Generated from `data/normalized_yaml/bacterial/KOMODO_58_BIFIDOBACTERIUM_medium.yaml`; future fixes belong in that normalized owner or the KOMODO/DSMZ enrichment importer and must then regenerate `data/merge_yaml/merged/`. |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/bifidobacterium_medium__4fefb4ac.yaml` | Passed. |
| Strict closed schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/bifidobacterium_medium__4fefb4ac.yaml --out /private/tmp/bifidobacterium_medium__4fefb4ac.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/bifidobacterium_medium__4fefb4ac.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed structurally, but the file has no reference checks to perform: 1 file validated, 0 total checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/bifidobacterium_medium__4fefb4ac.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed with only the known `eutils` / `pkg_resources` deprecation warning. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for standalone `history/` files, not a focused one-record check for embedded `MediaRecipe.curation_history` lists. |

The direct `just` targets were not rerun for this record because the project environment currently fails before target-specific validation while building `llvmlite==0.46.0` under Python 3.13; the commands above run the same validators in the cached Python 3.11 no-project environment used for this review batch.

## Identity and Grounding

- The record's local identity is internally consistent: `CultureMech:006069` is registered to `data/normalized_yaml/bacterial/KOMODO_58_BIFIDOBACTERIUM_medium.yaml`; both the normalized owner and generated merge identify KOMODO source ID 58 and DSMZ/MediaDive medium 58.
- The inspected MediaDive page identifies medium 58 as `BIFIDOBACTERIUM MEDIUM`, source `DSMZ`, taxonomic range `Bacteria`, type `Complex medium`, final pH 6.8, and a schema.org URI of `https://identifiers.org/mediadive.medium:58`. Those claims match the reviewed record's source and pH at the medium level.
- Ingredient groundings use plausible CHEBI terms for ordinary salts, glucose, Tween 80, resazurin, cysteine hydrochloride hydrate, and sodium hydroxide. No wrong hydrate or salt identity surfaced during this review; the substantive chemical errors are amounts and nesting, not the CHEBI IDs themselves.
- An exact ignored-file-inclusive search over `data/normalized_yaml`, `data/merge_yaml`, `data/culturemech_id_registry.tsv`, `data/culturemech_recipe_catalog.tsv`, `reports`, `scripts`, and `history` for `CultureMech:006069`, the exact merge fingerprint, and `KOMODO_58_BIFIDOBACTERIUM_medium` found the normalized owner, generated merge, expected indexes, and archived validation/report rows.

## Evidence

### Source Claims That Are Supported

| Claim in record | Source check |
|---|---|
| KOMODO ID 58 is linked to DSMZ/MediaDive medium 58. | Supported by the normalized record notes and curation history, which state `Source: KOMODO, ID: 58` and `Copied ingredients from DSMZ Medium 58`; the live MediaDive page resolves medium 58 to `BIFIDOBACTERIUM MEDIUM`. |
| Final pH is 6.8. | Supported by MediaDive medium 58 metadata and by the MediaDive preparation step, which says to adjust pH to 6.8 using 8 N NaOH. |
| The major main-solution ingredients are 10 g/L casein peptone, 5 g/L yeast extract, 5 g/L meat extract, 5 g/L Bacto Soytone, 10 g/L glucose, 2 g/L K2HPO4, 0.2 g/L MgSO4 x 7 H2O, 0.05 g/L MnSO4 x H2O, 0.5 g/L L-Cysteine HCl x H2O. | Supported by the inspected MediaDive main-solution table, except the record has collapsed later stock-solution rows into the K2HPO4 and MgSO4 x 7 H2O final amounts. |

### Unsupported or Misplaced Claims

| Record claim | Source evidence | Assessment |
|---|---|---|
| `K2HPO4` is 3 g/L with merged duplicate values `2.0, 1.0`. | MediaDive main solution has 2 g/L K2HPO4 and 40 ml/L of a salt stock that contains 1 g/L K2HPO4; MediaDive's own molecular-composition export gives 0.04 g/L K2HPO4 contribution from that stock. | Unsupported; the 1 g/L stock concentration was added directly instead of diluted 25-fold. |
| `MgSO4 x 7 H2O` is 0.7 g/L with merged duplicate values `0.2, 0.5`. | MediaDive main solution has 0.2 g/L MgSO4 x 7 H2O and 40 ml/L of a salt stock that contains 0.5 g/L MgSO4 x 7 H2O; the molecular-composition export gives 0.02 g/L from the stock. | Unsupported; the 0.5 g/L stock concentration was added directly instead of diluted 25-fold. |
| `NaCl` is 7 g/L with merged duplicate values `5.0, 2.0`. | MediaDive main solution has 5 g/L NaCl and 40 ml/L of a salt stock that contains 2 g/L NaCl; the molecular-composition export gives 0.08 g/L from the stock. | Unsupported; the 2 g/L stock concentration was added directly instead of diluted 25-fold. |
| `CaCl2 x 2 H2O`, `KH2PO4`, and `NaHCO3` are final direct ingredients at 0.25, 1, and 10 g/L. | These appear only in the 1000 ml salt-solution recipe that is added to the main solution at 40 ml/L. MediaDive's final molecular-composition export gives 0.01, 0.04, and 0.4 g/L respectively. | Unsupported stock/final collapse. |
| `Tween 80` and `Resazurin` are 1 and 4 g/L. | The source main solution adds Tween 80 as 1 ml/L and Resazurin as 4 ml/L of a 25 mg/100 ml stock. | Unsupported unit conversion; the source reports volume additions, not gram additions, and resazurin is a stock solution rather than 4 g/L final mass. |
| `NaOH` is an ingredient with a variable concentration. | MediaDive mentions NaOH only in the preparation instruction for pH adjustment: use 8 N NaOH to adjust to pH 6.8. | Overstructured; this belongs in a pH-adjustment preparation step or condition, not as a medium ingredient. |

## Completeness

- **Salt solution:** missing. MediaDive medium 58 has a named `Salt solution` added at 40 ml/L; the reviewed record has `solutions: 0` and flattened the stock ingredients into the final ingredient list.
- **Distilled water:** missing. MediaDive's main solution contains 950 ml distilled water and its salt solution contains 1000 ml distilled water; the reviewed record omits the solvent entirely.
- **Preparation:** missing. The source says to add cysteine after the medium is boiled and cooled under CO2, adjust pH to 6.8 with 8 N NaOH, distribute under N2, and autoclave. The normalized KOMODO owner and reviewed merge have no `preparation_steps`.
- **Direct references:** missing. The only recoverable source assertions are free text in `notes` and `curation_history`; `references` is empty.
- **Growth claims:** no specific `target_organisms` or growth evidence are asserted in this record, so those optional slots are correctly empty for the inspected source recipe.
- **Report absence:** a `find` search over `reports/yaml_record_review` found no prior `*-bifidobacterium_medium__4fefb4ac.md` report before this file was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Stock-solution salts were flattened and given 25x source-stock concentrations, then three main-solution rows were summed with stock rows as duplicates. | MediaDive medium 58 uses `40.00 ml` of `Salt solution`; that stock contains CaCl2 x 2 H2O 0.25 g/L, MgSO4 x 7 H2O 0.50 g/L, K2HPO4 1.00 g/L, KH2PO4 1.00 g/L, NaHCO3 10.00 g/L, NaCl 2.00 g/L, and distilled water to 1000 ml. The downloaded MediaDive molecular-composition export gives their final contributions as 0.01, 0.02, 0.04, 0.04, 0.4, and 0.08 g/L, but the reviewed YAML records 0.25, 0.7, 3.0, 1, 10, and 7 g/L after adding stock values to main rows. | `data/normalized_yaml/bacterial/KOMODO_58_BIFIDOBACTERIUM_medium.yaml`; the same importer/cleanup defect also affects `data/normalized_yaml/bacterial/bifidobacterium_medium.yaml` and the MediaDive-58 duplicate cluster. |
| Major | Volume and stock additions were converted into unsupported `G_PER_L` ingredient rows. | MediaDive lists Tween 80 as `1.00 ml` and Resazurin as `4.00 ml` of a `25 mg/100ml` stock. The record stores Tween 80 as `1 G_PER_L` and Resazurin as `4 G_PER_L`, which is dimensionally unsupported and especially wrong for resazurin. | `data/normalized_yaml/bacterial/KOMODO_58_BIFIDOBACTERIUM_medium.yaml`; fix the DSMZ/KOMODO import path so volume additions and stock solutions are not coerced to grams per liter. |
| Major | The preparation protocol was dropped, and NaOH was turned into a variable-concentration ingredient. | The inspected source preparation says to add cysteine after boiling/cooling under CO2, adjust to pH 6.8 with 8 N NaOH, distribute under N2, and autoclave. The reviewed record has no preparation steps and only captures `NaOH` as a `VARIABLE` ingredient extracted from a `pH buffer: NaOH` note. | `data/normalized_yaml/bacterial/KOMODO_58_BIFIDOBACTERIUM_medium.yaml`. |
| Major | The active KOMODO base record remains a duplicate of the direct DSMZ/MediaDive medium 58 record instead of being merged with it. | An exact ignored-file-inclusive search for `mediadive.medium:58`, `DSMZ Medium: 58`, `Source: KOMODO, ID: 58`, and `Copied ingredients from DSMZ Medium 58` found the reviewed generated record and owner, plus the active direct MediaDive owner `data/normalized_yaml/bacterial/bifidobacterium_medium.yaml` and its generated merge `data/merge_yaml/merged/bifidobacterium_medium__7368a3f1.yaml`. | Normalized duplicate metadata and merge inputs for `data/normalized_yaml/bacterial/KOMODO_58_BIFIDOBACTERIUM_medium.yaml` and `data/normalized_yaml/bacterial/bifidobacterium_medium.yaml`. |
| Minor | Source provenance is recoverable only from free-text import notes. | The record has no `sources`, `source_data`, or `references`; it relies on notes naming KOMODO ID 58 and DSMZ Medium 58. | `data/normalized_yaml/bacterial/KOMODO_58_BIFIDOBACTERIUM_medium.yaml`. |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/KOMODO_58_BIFIDOBACTERIUM_medium.yaml`, replace the flattened salt rows with a structured `Salt solution` added at 40 ml/L. The stock should preserve CaCl2 x 2 H2O 0.25 g/L, MgSO4 x 7 H2O 0.50 g/L, K2HPO4 1.00 g/L, KH2PO4 1.00 g/L, NaHCO3 10.00 g/L, NaCl 2.00 g/L, and 1000 ml distilled water, or the final record should use the MediaDive final molecular-composition values without pretending the stock recipe amounts are direct final additions.
2. Preserve source units for 1 ml/L Tween 80 and 4 ml/L resazurin stock addition; if the schema needs stock recipes for resazurin, represent `25 mg/100ml` as a stock concentration instead of the current `4 G_PER_L` final row.
3. Add the missing 950 ml main-solution distilled water and the source preparation step for cysteine, CO2 cooling, pH adjustment with 8 N NaOH, N2 distribution, and autoclaving. Remove the synthetic variable-concentration `NaOH` ingredient once the pH-adjustment step carries that information.
4. Add narrow, recoverable provenance for KOMODO ID 58 and DSMZ/MediaDive medium 58 in the normalized owner rather than relying only on `notes`.
5. Link or merge the KOMODO base record with the direct MediaDive medium 58 record and the existing MediaDive-58 duplicate cluster so equivalent source recipes no longer produce two canonical generated records.
6. Regenerate `data/merge_yaml/merged/` after the normalized/source-owned corrections; never patch `data/merge_yaml/merged/bifidobacterium_medium__4fefb4ac.yaml` directly.

## Follow-up Checks

- Run `just validate data/normalized_yaml/bacterial/KOMODO_58_BIFIDOBACTERIUM_medium.yaml` after curating the normalized owner.
- Run `just verify-merges` and `just audit-merge-freshness` after the duplicate metadata and merge inputs are corrected.
- Re-run focused schema, strict, term, and reference validators on the regenerated `data/merge_yaml/merged/bifidobacterium_medium__4fefb4ac.yaml` or its replacement merge fingerprint.
- Manually compare the regenerated recipe against MediaDive's medium 58 main solution, `Salt solution`, molecular-composition export, and preparation protocol to confirm stock/final arithmetic is dimensionally consistent.
- Search with `rg --no-ignore --hidden` for `mediadive.medium:58` and `komodo.medium:58` after regeneration to confirm the direct DSMZ and KOMODO base records no longer remain in separate generated canonical records when their ingredient/preparation signatures match.

## Additional Notes

- MediaDive's live HTML for medium 58, its JSON molecular-composition export, and its CSV molecular-composition export were downloaded and inspected during this review. The export is useful for final concentrations but intentionally omits source volume rows, so the HTML main-solution and `Salt solution` tables were also checked.
- `bifidobacterium_medium__4fefb4ac` is a single-source generated merge of the KOMODO base owner. The direct DSMZ/MediaDive owner and 27 strain-modified KOMODO source records are represented separately by `bifidobacterium_medium__7368a3f1`; the bad salt flattening predates that merge too.
