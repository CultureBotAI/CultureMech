# YAML Record Review: bl_medium_low_mops

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/bl_medium_low_mops.yaml
- Started UTC: 2026-09-21T22:09:05Z
- Finished UTC: 2026-09-21T22:10:17Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/bl_medium_low_mops.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:007305` |
| Name | `bl_medium_low_mops` |
| Original name | `BL Medium, Low MOPS` |
| Category | `bacterial` |
| Source term | `MEDIADB:404` / `BL Medium, Low MOPS` |
| Merge fingerprint | `df5e4da121c229a7832b37b38ca0ecda6e5c381eb3baa28fe8bab05615eb64b5` |
| Merged from | `bl_medium`, `bl_medium_low_mops` |
| Maintained owner | `data/normalized_yaml/bacterial/bl_medium_low_mops.yaml` |
| Parent owner | `data/normalized_yaml/bacterial/bl_medium.yaml` |
| Generated status | Derived merge product; future fixes belong in `data/normalized_yaml/bacterial/bl_medium_low_mops.yaml`, the MediaDB importer, or merge logic, then regenerated `data/merge_yaml/merged/` and pages. |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/bl_medium_low_mops.yaml` | Passed, `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/bl_medium_low_mops.yaml --out /private/tmp/bl_medium_low_mops.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/bl_medium_low_mops.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with exit 0 and no reference diagnostics. The record has no structured `references` to check. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/bl_medium_low_mops.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after a non-fatal `eutils` `pkg_resources` warning. |
| Embedded curation history | Not checked: no focused embedded `MediaRecipe.curation_history` validator is documented for one generated merge record; `just validate-history` targets standalone files under `history/`. |

Direct `just validate-schema`, `just validate-strict`, `just validate-references`, and `just validate-terms` were not rerun because this checkout still fails before target-specific validation while the project `uv` environment tries to build `llvmlite==0.46.0` under Python 3.13. The no-project Python 3.11 commands above are the same validators with cached dependencies and the target file supplied directly.

## Identity and Grounding

- `CultureMech:007305`, `name: bl_medium_low_mops`, `original_name: BL Medium, Low MOPS`, `media_term.term.id: MEDIADB:404`, `category: bacterial`, `medium_type: DEFINED`, `composition_type: DEFINED`, and `physical_state: LIQUID` all identify the intended low-MOPS MediaDB record.
- Live MediaDB lists medium 404 as `Bl medium, low mops`, with a tab-delimited export at `/defined_media/media_text/404/`. That export has the same 32 compound names as the generated YAML.
- The generated merge uses the wrong MOPS concentration. MediaDB 404 and the normalized owner both list `MOPS` at 40.0 mM; the generated merge lists 190.0 mM, which is the parent MediaDB 401 BL Medium value.
- The normalized BL Medium and BL Medium, Low MOPS owners already model the relationship correctly: `data/normalized_yaml/bacterial/bl_medium.yaml` keeps MediaDB 401 with 190 mM MOPS and a `variant_children` link to `data/normalized_yaml/bacterial/bl_medium_low_mops.yaml`; `data/normalized_yaml/bacterial/bl_medium_low_mops.yaml` keeps MediaDB 404 with 40 mM MOPS and `parent_media`/`variant_relationship: CONCENTRATION_VARIANT`.
- Exact ignored-file-inclusive searches over `data/normalized_yaml`, `data/merge_yaml/merged`, `data/culturemech_id_registry.tsv`, `data/culturemech_recipe_catalog.tsv`, `scripts`, `tests`, `reports/yaml_record_review`, and `history` for `CultureMech:007305`, `MEDIADB:404`, the exact merge fingerprint, `BL Medium, Low MOPS`, and `bl_medium_low_mops.yaml` found the normalized owner, the generated merge, the parent `bl_medium` owner, and expected index rows.
- An exact ignored-file-inclusive search over `data/raw` and `data/import_tracking` for `MEDIADB:404`, `Medium ID: 404`, and `bl_medium_low_mops` found only `data/import_tracking/reports/deep_research_priority.json`; no cached raw MediaDB 404 source capture is present.

## Evidence

### Source Claims That Are Supported

| Claim | Support |
|---|---|
| MediaDB 404 is `Bl medium, low mops`. | The live MediaDB `/defined_media/media/404/` page has title and heading `Media: Bl medium, low mops`. |
| The record should have 32 defined millimolar ingredients. | The live MediaDB page and tab-delimited `media_text/404` export list 32 compounds. A parsed comparison found 32 TSV rows, 32 YAML rows, no missing names, and no extra names. |
| The low-MOPS variant has 40.0 mM MOPS. | MediaDB 404 lists `MOPS` at 40.0 mM; the normalized low-MOPS owner has the same value and explicitly says MOPS decreased from 190 mM to 40 mM. |
| The parent BL Medium has 190.0 mM MOPS. | `data/normalized_yaml/bacterial/bl_medium.yaml` is `MEDIADB:401` and lists `MOPS` at 190.0 mM. |
| MediaDB links a medium-specific primary source and growth row. | MediaDB Medium 404 links Source 128, `Jensen et al, 1993`, and Growth Data 784, `Lactococcus lactis MG1363 on Bl medium, low mops`. Growth Data 784 reports growth rate 0.29, pH 7.2, and temperature 30.0 for MG1363 on this medium. |

### Unsupported or Misplaced Claims in the Generated Record

| Generated claim | Problem |
|---|---|
| `MOPS` at `190.0 MILLIMOLAR` in a `MEDIADB:404` low-MOPS recipe. | MediaDB 404 states 40.0 mM; 190.0 mM is the parent MediaDB 401 concentration. This is the only ingredient mismatch against the MediaDB 404 TSV export, but it is the defining difference between the parent and child. |
| `merged_from: [bl_medium, bl_medium_low_mops]` with `media_term.term.id: MEDIADB:404`. | Parent Medium 401 and child Medium 404 are concentration variants, not duplicates. Collapsing them caused a generated record with the child ID and source term but the parent composition. |
| Preparation step: `Dissolve all ingredients in distilled water to specified concentrations`. | The inspected MediaDB 404 page and TSV export give millimolar compounds but do not state the solvent or a dissolve protocol. |
| Preparation step: `Adjust pH if specified in original formulation`. | MediaDB Growth Data 784 gives pH 7.2 for the linked MG1363 growth condition, but the Medium 404 formulation page does not say to adjust the recipe to a pH value. The conditional wording is generic importer text. |
| Preparation step: `Sterilize by filtration (0.22 um) to preserve heat-sensitive components`. | MediaDB 404 does not publish a 0.22 um filtration instruction. |
| Curation history `Reference: Mazumdar et al. (2014) PLOS One`. | That is the MediaDB database paper, not the medium-specific primary source. MediaDB 404 points to `Jensen et al, 1993`; the source page identifies Applied and Environmental Microbiology and the title `Minimal Requirements for Exponential Growth ofLactococcus lactis`. |

The old ASM URL linked from MediaDB Source 128 returned a Cloudflare JavaScript challenge when checked during the adjacent Medium 402 review, so the original Jensen article body was not inspected from that publisher URL. This review relies on live MediaDB pages for the Medium 404 formula and Growth Data 784 metadata, and on the already-inspected MediaDB Source 128 page for the Jensen source metadata.

## Completeness

- **Ingredients:** one critical mismatch. All ingredient names match MediaDB 404, but `MOPS` is 190.0 mM instead of 40.0 mM.
- **Variant classification:** internally contradictory. The generated record preserves the normalized statement that MOPS should be decreased to 40 mM, but the ingredient row uses the 190 mM parent concentration.
- **Source provenance:** incomplete. The source-specific MediaDB URL, Source 128 URL, Growth Data 784 URL, and Jensen source metadata are absent from `references` and from curation events; the record only preserves a generic MediaDB homepage note and a generic Mazumdar 2014 import-history note.
- **Growth context:** incomplete. MediaDB Growth Data 784 supports a scoped `Lactococcus lactis MG1363` growth context on MediaDB 404 with a 0.29 growth rate, pH 7.2, and temperature 30.0 C; the record has no `target_organisms`, `growth_metrics`, pH, or temperature context.
- **Preparation:** unsupported. All three `preparation_steps` appear to be generic MediaDB importer defaults rather than Medium 404 source claims.
- **Optional fields:** atmosphere, salinity, storage, and discussion are acceptable to leave empty because the inspected MediaDB 404, Source 128, and Growth Data 784 pages did not provide those details.
- **Raw cache:** no cached MediaDB 404 raw page was found under `data/raw`; the exact ignored-file-inclusive raw/import-tracking search only found `data/import_tracking/reports/deep_research_priority.json` metadata for this recipe.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | The generated merge conflates MediaDB 401 and MediaDB 404 and gives the low-MOPS record the parent MOPS concentration. | Live MediaDB 404 and `data/normalized_yaml/bacterial/bl_medium_low_mops.yaml` both list MOPS at 40.0 mM. The generated `MEDIADB:404` record lists MOPS at 190.0 mM and says it was merged from both `bl_medium` and `bl_medium_low_mops`. | Merge rules or merge clustering for the MediaDB BL Medium pair; normalized owners already hold separate parent/child records. |
| Major | Unsupported generic preparation steps are asserted as if they came from MediaDB Medium 404. | The live MediaDB 404 page and tab-delimited export list compounds and amounts, linked organisms, a linked source, and a linked growth-data record. They do not state a distilled-water dissolve step, a recipe pH adjustment, or 0.22 um filter sterilization. | `data/normalized_yaml/bacterial/bl_medium_low_mops.yaml`; broad repeats may require the MediaDB importer or a post-import cleanup rule. |
| Major | MediaDB's own primary source and growth-data context are not represented. | Medium 404 links Source 128 and Growth Data 784. Growth Data 784 reports `Lactococcus lactis MG1363 on Bl medium, low mops`, growth rate 0.29, pH 7.2, and temperature 30.0; the YAML has no `references`, no `target_organisms`, no `growth_metrics`, no pH or temperature condition, and only names the generic Mazumdar 2014 MediaDB paper. | `data/normalized_yaml/bacterial/bl_medium_low_mops.yaml`; broad repeats may require MediaDB importer/enrichment changes. |

## Recommended Edits

1. Fix merge clustering so MediaDB 401 `bl_medium` and MediaDB 404 `bl_medium_low_mops` remain separate concentration variants; then regenerate `data/merge_yaml/merged/`.
2. After regeneration, confirm the generated low-MOPS record retains `MEDIADB:404`, MOPS at 40.0 mM, and the parent link to `CultureMech:007302`, with no `merged_from: bl_medium`.
3. Remove the three unsupported generic preparation steps from `data/normalized_yaml/bacterial/bl_medium_low_mops.yaml` unless a checked Jensen source or MediaDB page supports them.
4. Add structured `references` for MediaDB Medium 404, MediaDB Source 128, and MediaDB Growth Data 784; if Jensen 1993 can be inspected through a non-blocked authoritative copy, add its PMID or DOI instead of only the MediaDB source page.
5. Add a scoped growth assertion for `Lactococcus lactis MG1363` on `BL Medium, Low MOPS`, preserving MediaDB Growth Data 784's growth rate 0.29, pH 7.2, and 30.0 C context and not generalizing it to the sibling BL Medium Arg, Arg/Ser/Trp, or Asp records.

## Follow-up Checks

- Re-fetch MediaDB `/defined_media/media/404/`, `/defined_media/media_text/404/`, `/defined_media/sources/128/`, and `/defined_media/growthdata/784/` and manually compare the normalized ingredients, source, organism, pH, temperature, and growth rate.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating `data/merge_yaml/merged/`; the stale fingerprint `df5e4da121c229a7832b37b38ca0ecda6e5c381eb3baa28fe8bab05615eb64b5` should leave active output.
- Run focused schema, strict, term, and reference validators on `data/normalized_yaml/bacterial/bl_medium_low_mops.yaml`.
- After adding external article evidence, run the reference validator on any exact snippets before retaining them.

## Additional Notes

- The exact `find` for `*-bl_medium_low_mops.md` under ignored `reports/yaml_record_review/` found no existing report before this file was written.
- `data/merge_yaml/merged/bl_medium_arg.yaml`, `data/merge_yaml/merged/bl_medium_arg_ser_trp.yaml`, and `data/merge_yaml/merged/bl_medium_asp.yaml` are adjacent MediaDB/Jensen BL Medium variants and should be kept source-scoped if growth evidence is added.
