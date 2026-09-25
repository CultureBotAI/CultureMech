# YAML Record Review: bifidobacterium_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/bifidobacterium_medium__6a8d2306.yaml
- Started UTC: 2026-09-21T21:53:00Z
- Finished UTC: 2026-09-21T21:54:42Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/bifidobacterium_medium__6a8d2306.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:007834` |
| Name | `bifidobacterium_medium` |
| Original name | `Bifidobacterium Medium` |
| Category | `bacterial` |
| Media term | `TOGO:M12` / `Bifidobacterium Medium` |
| Source lineage | TOGO M12 from JCM medium 19 |
| Merge fingerprint | `6a8d23064f5544eae64dbb7764201bba9af0cee73941b78fc5ff0c8f8d548164` |
| Merged from | `TOGO_M12_Bifidobacterium_Medium` |
| Generated status | Generated from `data/normalized_yaml/bacterial/TOGO_M12_Bifidobacterium_Medium.yaml`; future fixes belong in that normalized owner or the TOGO importer and must then regenerate `data/merge_yaml/merged/`. |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/bifidobacterium_medium__6a8d2306.yaml` | Passed. |
| Strict closed schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/bifidobacterium_medium__6a8d2306.yaml --out /private/tmp/bifidobacterium_medium__6a8d2306.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/bifidobacterium_medium__6a8d2306.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed structurally, but the file has no reference checks to perform: 1 file validated, 0 total checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/bifidobacterium_medium__6a8d2306.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed with only the known `eutils` / `pkg_resources` deprecation warning. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for standalone `history/` files, not a focused one-record check for embedded `MediaRecipe.curation_history` lists. |

The direct `just` targets were not rerun for this record because the project environment currently fails before target-specific validation while building `llvmlite==0.46.0` under Python 3.13; the commands above run the same validators in the cached Python 3.11 no-project environment used for this review batch.

## Identity and Grounding

- The record's ID and generated lineage agree: `CultureMech:007834` is registered to `data/normalized_yaml/bacterial/TOGO_M12_Bifidobacterium_Medium.yaml`, and the generated merge carries only that source owner on fingerprint `6a8d23064f5544eae64dbb7764201bba9af0cee73941b78fc5ff0c8f8d548164`.
- The live TOGO M12 API identifies the recipe as `Bifidobacterium Medium`, with `original_media_id` `JCM_M19`, source URL `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=19`, and pH 6.8. Those values match the local source notes.
- The source ingredient order and core ingredients match TOGO M12: 1 L distilled water, 3 g K2HPO4, 1 ml Tween 80, 10 g glucose, 5 g yeast extract (BD-Difco), 5 g beef extract (BD-Difco), 10 g casein peptone tryptic digest, 1% sodium ascorbate solution, and 0.05% L-cysteine-HCl solution.
- An exact ignored-file-inclusive search over `data/normalized_yaml`, `data/merge_yaml`, `data/culturemech_id_registry.tsv`, `data/culturemech_recipe_catalog.tsv`, `reports`, `scripts`, and `history` for `CultureMech:007834`, `TOGO_M12_Bifidobacterium_Medium`, the exact merge fingerprint, exact `TOGO:M12`, and `JCM_M19` found the normalized owner, generated merge, expected indexes, and archived validation/report rows.

## Evidence

### Source Claims That Are Supported

| Claim in record | Source check |
|---|---|
| TOGO M12 is `Bifidobacterium Medium` sourced from JCM M19. | Supported by the live TOGO M12 API metadata and by the record's `TOGO:M12` media term. |
| K2HPO4, glucose, yeast extract, beef extract, and casein peptone amounts are 3 g, 10 g, 5 g, 5 g, and 10 g per 1 L recipe. | Supported by the live TOGO M12 component list. |
| pH is 6.8. | Supported by TOGO M12 metadata and the TOGO comment to adjust pH to 6.8. |

### Unsupported or Misplaced Claims

| Record claim | Source evidence | Assessment |
|---|---|---|
| Distilled water is `1 G_PER_L`. | TOGO M12 reports `volume: 1`, `unit: L`. | Unsupported unit conversion; the source is a solvent volume, not 1 g/L water. |
| Tween 80 is `1 G_PER_L`. | TOGO M12 reports `volume: 1`, `unit: ml`. | Unsupported unit conversion; no density or mass conversion is stated. |
| Sodium ascorbate has `VARIABLE` concentration. | TOGO M12 reports `conc_value: 1`, `conc_unit: %` and explains that sodium ascorbate is added aseptically after sterilization to a final concentration of 1.0%. | Unsupported defaulting; the source value is explicit. |
| L-cysteine-HCl has `VARIABLE` concentration. | TOGO M12 reports `conc_value: 0.05`, `conc_unit: %` and explains that L-cysteine-HCl is added aseptically after sterilization to a final concentration of 0.05%. | Unsupported defaulting; the source value is explicit. |

## Completeness

- **Preparation:** missing. TOGO M12 has two comments: adjust pH to 6.8, and after sterilization aseptically add sodium ascorbate and L-cysteine-HCl to final concentrations of 1.0% and 0.05%; it also says medium not freshly prepared should be heated in a steamer for 10 min before adding the reducing substances. The reviewed record has no `preparation_steps`.
- **Ingredient source units:** incomplete. Water, Tween 80, sodium ascorbate, and L-cysteine-HCl all need source-preserving volume or percent modeling rather than the current gram-per-liter or variable placeholders.
- **Direct references:** missing. The record has no `references`; source recovery depends on free-text `notes`.
- **JCM live source:** the exact JCM `GRMD=19` URL named in the record now returns a small `Nothing found` page, so TOGO's M12 API is currently the recoverable authoritative source for the imported TOGO payload.
- **Growth claims:** no specific `target_organisms` or growth evidence are asserted in this record, so those optional slots are correctly empty for the inspected source recipe.
- **Report absence:** a `find` search over `reports/yaml_record_review` found no prior `*-bifidobacterium_medium__6a8d2306.md` report before this file was written.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Three non-mass additions were coerced into unsupported mass concentrations. | TOGO M12 reports 1 L distilled water and 1 ml Tween 80, while the reviewed YAML stores both as `G_PER_L`. TOGO also reports percent final concentrations for the two reducing solutions, but the reviewed YAML stores sodium ascorbate and L-cysteine-HCl as `VARIABLE`. | `data/normalized_yaml/bacterial/TOGO_M12_Bifidobacterium_Medium.yaml`; if the coercion is importer-owned, fix the TOGO importer too. |
| Major | The post-sterilization and pH instructions were dropped. | TOGO M12 explicitly says to adjust pH to 6.8 and to add sodium ascorbate and L-cysteine-HCl aseptically after sterilization; the generated record has no `preparation_steps`, so following it would add the reducing agents before sterilization or omit them entirely. | `data/normalized_yaml/bacterial/TOGO_M12_Bifidobacterium_Medium.yaml`. |
| Major | The TOGO M12 record is an active duplicate of the direct JCM/MediaDive J19 record. | TOGO M12 declares `original_media_id: JCM_M19`. A no-ignore exact search for `CultureMech:002562`, `JCM_J19_BIFIDOBACTERIUM_MEDIUM`, and `mediadive.medium:J19` found active owner `data/normalized_yaml/bacterial/JCM_J19_BIFIDOBACTERIUM_MEDIUM.yaml` and generated merge `data/merge_yaml/merged/BIFIDOBACTERIUM_MEDIUM.yaml`, whose source is the same JCM medium 19 recipe. | Duplicate metadata spanning `data/normalized_yaml/bacterial/TOGO_M12_Bifidobacterium_Medium.yaml` and `data/normalized_yaml/bacterial/JCM_J19_BIFIDOBACTERIUM_MEDIUM.yaml`. |
| Minor | L-cysteine-HCl remains ungrounded even though TOGO supplies GMO identity for the ingredient. | TOGO M12 supplies GMO ID `GMO_002094` with label `L-Cysteine hydrochloride solution`; the YAML preserves the label but has no `term` or MediaIngredientMech/CHEBI grounding for this reducing solution. | `data/normalized_yaml/bacterial/TOGO_M12_Bifidobacterium_Medium.yaml`. |
| Minor | Source provenance is recoverable only from free-text import notes. | The record has no `references`, `sources`, or `source_data`; it stores the TOGO and original JCM URLs only in `notes`. | `data/normalized_yaml/bacterial/TOGO_M12_Bifidobacterium_Medium.yaml`. |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/TOGO_M12_Bifidobacterium_Medium.yaml`, preserve TOGO's explicit non-mass units: 1 L distilled water, 1 ml Tween 80, sodium ascorbate at 1.0%, and L-cysteine-HCl at 0.05%.
2. Add source-supported preparation steps for pH adjustment, sterilization, post-sterilization aseptic addition of sodium ascorbate and L-cysteine-HCl, and steaming non-fresh medium for 10 min before adding the reducing substances.
3. Ground or explicitly leave unresolved the L-cysteine-HCl solution after checking the packaged MediaIngredientMech label index; do not force the anhydrous amino acid if the source denotes a hydrochloride solution.
4. Add narrow source provenance for TOGO M12 and its JCM M19 origin in structured source/reference fields if the schema supports them.
5. Link or merge this TOGO M12 record with the direct JCM J19 owner after both normalized records have the same source-accurate formula and preparation semantics.
6. Regenerate `data/merge_yaml/merged/` after the normalized/source-owned corrections; never patch `data/merge_yaml/merged/bifidobacterium_medium__6a8d2306.yaml` directly.

## Follow-up Checks

- Run `just validate data/normalized_yaml/bacterial/TOGO_M12_Bifidobacterium_Medium.yaml` after curating the normalized owner.
- Run `just verify-merges` and `just audit-merge-freshness` after the duplicate metadata and merge inputs are corrected.
- Re-run focused schema, strict, term, and reference validators on the regenerated `data/merge_yaml/merged/bifidobacterium_medium__6a8d2306.yaml` or its replacement merge fingerprint.
- Manually compare the regenerated record against the TOGO M12 API to ensure gram, liter, milliliter, and percent additions were not coerced to incorrect mass concentrations.
- Search with `rg --no-ignore --hidden` for exact `TOGO:M12`, `JCM_M19`, and `mediadive.medium:J19` after regeneration to confirm the TOGO and JCM views of medium 19 no longer remain as unlinked duplicate canonical records.

## Additional Notes

- TOGO M12's original JCM `GRMD=19` URL was checked live and returned `Nothing found`; this report therefore uses the live TOGO API payload as the source text for this TOGO import.
- The direct JCM/MediaDive J19 owner was also reviewed in `reports/yaml_record_review/20260921T214717Z-BIFIDOBACTERIUM_MEDIUM.md`; the duplicate should be resolved after the shared JCM M19 recipe is source-accurate in both inputs.
