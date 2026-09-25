# YAML Record Review: rdm_base_medium_vitamins_maltose_1_g_l_nh4cl

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/rdm_base_medium_vitamins_maltose_1_g_l_nh4cl.yaml
- Started UTC: 2026-09-25T01:32:20Z
- Finished UTC: 2026-09-25T01:32:36Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/rdm_base_medium_vitamins_maltose_1_g_l_nh4cl.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:007285` |
| Label | `rdm_base_medium_vitamins_maltose_1_g_l_nh4cl` |
| Original label | `'''RDM Base Medium + Vitamins + Maltose (1 g/L NH4Cl` |
| Category | `bacterial` |
| Source | `MEDIADB:381` |
| Generated status | Generated canonical merge under `data/merge_yaml/merged`; do not edit directly |
| Maintained owners | `data/normalized_yaml/bacterial/rdm_base_medium_vitamins_maltose_1_g_l_nh4cl.yaml`, `data/normalized_yaml/bacterial/rdm_base_medium_vitamins_maltose_0_5_g_l_nh4cl.yaml` |
| Merged from | `rdm_base_medium_vitamins_maltose_0_5_g_l_nh4cl`, `rdm_base_medium_vitamins_maltose_1_g_l_nh4cl` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/rdm_base_medium_vitamins_maltose_1_g_l_nh4cl.yaml` | Passed; exited 0 with no diagnostics. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/rdm_base_medium_vitamins_maltose_1_g_l_nh4cl.yaml --out /private/tmp/rdm_base_medium_vitamins_maltose_1_g_l_nh4cl.strict.tsv --workers 1 --quiet` | Passed with 0 errors; the TSV had its header only. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/rdm_base_medium_vitamins_maltose_1_g_l_nh4cl.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were present. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/rdm_base_medium_vitamins_maltose_1_g_l_nh4cl.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the validator emitted the known `eutils` `pkg_resources` deprecation warning. |
| Embedded history | `just validate-history` | Not checked: this repository command validates standalone `history/` records, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

## Identity and Grounding

The generated record says it is MediaDB 381 / `RDM Base Medium + Vitamins + Maltose (1 g/L NH4Cl)`, but its `ingredients` carry 9.348 mM Ammonium chloride and its `merged_from` list collapses MediaDB 381 with MediaDB 382.

The inspected MediaDB tab-delimited exports show that MediaDB 381 is the 1 g/L NH4Cl formulation with 18.7 mM Ammonium chloride, while MediaDB 382 is the 0.5 g/L NH4Cl formulation with 9.348 mM Ammonium chloride. The maintained normalized owners already preserve those concentrations and use `CONCENTRATION_VARIANT` links. The generated output incorrectly merged them and retained the child 0.5 g/L ammonium concentration in the 1 g/L record.

An exact gitignore-independent search over `data/normalized_yaml`, `data/merge_yaml`, `reports/yaml_record_review`, and `reports/media_content_review_manifest.tsv` for `rdm_base_medium_vitamins_maltose_1_g_l_nh4cl`, `MEDIADB:381`, `CultureMech:007285`, `rdm_base_medium_vitamins_maltose_0_5_g_l_nh4cl`, `MEDIADB:382`, and `CultureMech:007286` found the two normalized owners, their indexes/manifest rows, and this generated merge output. It did not find other exact normalized or generated owners for these MediaDB accessions in the searched paths.

The generated target also predates normalized curation that repaired MediaDB's parenthesis-truncated medium label. The maintained 1 g/L owner has full `original_name` and `media_term.term.label` values plus an August 31, 2026 `REPAIRED_MEDIADB_TRUNCATED_NAME` event; the generated target still starts its `original_name` with triple quotes and lacks the closing parenthesis in `NH4Cl)`.

## Evidence

The inspected MediaDB 381 page and its tab-delimited export support a 25-compound 1 g/L NH4Cl formula and specifically support Ammonium chloride at 18.7 mM. The generated 9.348 mM value is only supported by the MediaDB 382 export for the 0.5 g/L NH4Cl child.

The inspected MediaDB pages also support additional evidence that the generated record does not carry:

| Claim source | Supported claim |
|---|---|
| MediaDB 381 page | Rdm base medium + vitamins + maltose (1 g/L NH4Cl) contains 25 compounds, is linked to source 143, and has a growth data record for `Thermotoga maritima DSM 3109 on Rdm base medium + vitamins + maltose (1 g/L NH4Cl)`. |
| MediaDB source 143 page | Source 143 is Rinker KD et al. 2000, `Effect of carbon and nitrogen sources on growth dynamics and exopolysaccharide production for the hyperthermophilic archaeon Thermococcus litoralis and bacterium Thermotoga maritima.`, in `Biotechnology And Bioengineering`, with PubMed term `10898863`. |
| MediaDB growth record 746 | `Thermotoga maritima DSM 3109` grew on MediaDB 381 at 88.0 C; the growth rate and pH fields are `None`. |

No inspected MediaDB source text supported the generated preparation steps. The source pages and tab-delimited export name compound amounts and growth metadata, but do not say to adjust an unspecified pH or filter-sterilize through 0.22 um membrane.

## Completeness

The target omits the MediaDB source 143 provenance and growth record 746 even though the MediaDB 381 page links them directly. Future curation should add a bounded `target_organisms` block for `Thermotoga maritima DSM 3109` at 88.0 C, leave growth rate and pH absent unless another inspected source resolves them, and cite source 143.

The exact ignored-file-inclusive search described above found both local RDM vitamins/maltose/NH4Cl owners by exact ID/source/slug and did not find additional exact owners for MediaDB 381 or 382 in the checked normalized or merge paths.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | The generated 1 g/L NH4Cl RDM target falsely merges the 1 g/L and 0.5 g/L concentration variants and keeps the 0.5 g/L ammonium value. | MediaDB exports for 381 and 382 list Ammonium chloride at 18.7 and 9.348 mM respectively. The generated `MEDIADB:381` record lists 9.348 mM and `merged_from` includes both slugs. | Merge equivalence rules for MediaRecipe generation |
| Major | The generated target is stale relative to its maintained 1 g/L owner. | `data/normalized_yaml/bacterial/rdm_base_medium_vitamins_maltose_1_g_l_nh4cl.yaml` repaired the MediaDB label truncation and carries the August 31, 2026 repair event; the generated record still has the truncated `'''RDM Base Medium + Vitamins + Maltose (1 g/L NH4Cl` label. | Merge generation for `data/merge_yaml/merged/rdm_base_medium_vitamins_maltose_1_g_l_nh4cl.yaml` |
| Major | The MediaDB importer added unsupported generic preparation steps. | The generated and normalized RDM vitamins/maltose/NH4Cl owners say to dissolve, adjust pH if specified, and filter-sterilize at 0.22 um. The inspected MediaDB medium, source, growth, and tab-delimited pages only provide compound amounts, source/growth links, temperature, and growth metadata. | `data/normalized_yaml/bacterial/rdm_base_medium_vitamins_maltose_1_g_l_nh4cl.yaml`; `data/normalized_yaml/bacterial/rdm_base_medium_vitamins_maltose_0_5_g_l_nh4cl.yaml`; MediaDB import templates |
| Major | The 1 g/L RDM owner lacks direct MediaDB growth/source evidence. | MediaDB 381 links to source 143 and growth record 746 for `Thermotoga maritima DSM 3109`; growth record 746 reports 88.0 C. The record has no references, target organism, growth condition, or source 143 provenance. | `data/normalized_yaml/bacterial/rdm_base_medium_vitamins_maltose_1_g_l_nh4cl.yaml`; MediaDB growth importer |

## Recommended Edits

1. Change the merge fingerprint or merge-equivalence guard so ammonium chloride concentration is identity-significant; regenerate the merge layer so MediaDB 381 and 382 remain separate generated records connected as `CONCENTRATION_VARIANT`s.
2. Regenerate `data/merge_yaml/merged/rdm_base_medium_vitamins_maltose_1_g_l_nh4cl.yaml` from current normalized inputs so the 18.7 mM Ammonium chloride value, repaired label, and later curation event propagate.
3. Remove or qualify the unsupported generic RDM preparation steps in the two maintained RDM vitamins/maltose/NH4Cl owners unless a checked source is added that states a pH adjustment and 0.22 um filter sterilization protocol.
4. Add MediaDB 381 source and growth evidence to the 1 g/L normalized owner: Source 143 / Rinker 2000, growthdata 746, `Thermotoga maritima DSM 3109`, and temperature 88.0 C.

## Follow-up Checks

1. Run strict, term, and reference validation on both normalized RDM vitamins/maltose/NH4Cl owners after changing MediaDB evidence or preparation text.
2. Rerun the merge verifier and inspect regenerated outputs for MediaDB 381 and 382 to confirm that both Ammonium chloride values stay distinct.
3. Reopen the regenerated 1 g/L output and verify that it carries `MEDIADB:381`, Ammonium chloride 18.7 mM, and the full parenthesized MediaDB label.
4. Manually recheck the MediaDB 381 medium page, source 143 page, and growthdata 746 page after adding target-organism evidence.

## Additional Notes

None found.
