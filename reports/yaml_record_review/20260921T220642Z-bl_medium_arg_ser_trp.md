# YAML Record Review: bl_medium_arg_ser_trp

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/bl_medium_arg_ser_trp.yaml
- Started UTC: 2026-09-21T22:05:16Z
- Finished UTC: 2026-09-21T22:06:42Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/bl_medium_arg_ser_trp.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:007306` |
| Name | `bl_medium_arg_ser_trp` |
| Original name | `BL Medium + Arg + Ser + Trp` |
| Category | `bacterial` |
| Source term | `MEDIADB:405` / `BL Medium + Arg + Ser + Trp` |
| Merge fingerprint | `26525477a029ea24af66b7e16df96d679f0cab061a957aeb763f5eed49624ee3` |
| Merged from | `bl_medium_arg_ser_trp` |
| Maintained owner | `data/normalized_yaml/bacterial/bl_medium_arg_ser_trp.yaml` |
| Generated status | Derived one-source merge product; future fixes belong in `data/normalized_yaml/bacterial/bl_medium_arg_ser_trp.yaml`, the MediaDB importer, or maintained MediaDB enrichment, then regenerated `data/merge_yaml/merged/` and pages. |

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/bl_medium_arg_ser_trp.yaml` | Passed, `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/bl_medium_arg_ser_trp.yaml --out /private/tmp/bl_medium_arg_ser_trp.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/bl_medium_arg_ser_trp.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 reference checks. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/bl_medium_arg_ser_trp.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: no focused embedded `MediaRecipe.curation_history` validator is documented for one generated merge record; `just validate-history` targets standalone files under `history/`. |

Direct `just validate-schema`, `just validate-strict`, `just validate-references`, and `just validate-terms` were not rerun because this checkout still fails before target-specific validation while the project `uv` environment tries to build `llvmlite==0.46.0` under Python 3.13. The no-project Python 3.11 commands above are the same validators with cached dependencies and the target file supplied directly.

## Identity and Grounding

- `CultureMech:007306`, `name: bl_medium_arg_ser_trp`, `original_name: BL Medium + Arg + Ser + Trp`, `media_term.term.id: MEDIADB:405`, `category: bacterial`, `medium_type: DEFINED`, `composition_type: DEFINED`, and `physical_state: LIQUID` all match the generated record's MediaDB source identity.
- Live MediaDB lists medium 405 as `Bl medium + arg + ser + trp`, with a tab-delimited export at `/defined_media/media_text/405/`. That export has the same 35 compound names and 35 millimolar quantities as the generated YAML.
- The generated merge is byte-for-byte equivalent to the normalized owner except for the generated `MERGED_RECIPES` curation event, `merge_fingerprint`, and `merged_from` trailer.
- Exact ignored-file-inclusive searches over `data/normalized_yaml`, `data/merge_yaml/merged`, `data/culturemech_id_registry.tsv`, `data/culturemech_recipe_catalog.tsv`, `scripts`, `tests`, `reports/yaml_record_review`, and `history` for `CultureMech:007306`, `MEDIADB:405`, the exact merge fingerprint, `BL Medium + Arg + Ser + Trp`, and `bl_medium_arg_ser_trp.yaml` found the normalized owner, generated merge, and expected index rows.
- An exact ignored-file-inclusive search over `data/raw` and `data/import_tracking` for `MEDIADB:405`, `Medium ID: 405`, and `bl_medium_arg_ser_trp` found only `data/import_tracking/reports/deep_research_priority.json`; no cached raw MediaDB 405 source capture is present.

## Evidence

### Source Claims That Are Supported

| Claim | Support |
|---|---|
| MediaDB 405 is `Bl medium + arg + ser + trp`. | The live MediaDB `/defined_media/media/405/` page has title and heading `Media: Bl medium + arg + ser + trp`. |
| The record has 35 defined millimolar ingredients. | The live MediaDB page and tab-delimited `media_text/405` export list 35 compounds. A parsed comparison found 35 TSV rows, 35 YAML rows, no missing names, no extra names, and no value mismatches. |
| This variant adds L-serine and L-tryptophan to the L-arginine BL Medium variant. | MediaDB 405 includes `L-Arginine` at 1.1 mM, `L-Serine` at 2.9 mM, and `L-Tryptophan` at 0.5 mM; Medium 402 has the same base with L-arginine but not serine or tryptophan. |
| MediaDB links a medium-specific primary source and growth row. | MediaDB Medium 405 links Source 128, `Jensen et al, 1993`, and Growth Data 785, `Lactococcus lactis MG1363 on Bl medium + arg + ser + trp`. Growth Data 785 reports growth rate 0.36, pH 7.2, and temperature 30.0 for MG1363 on this medium. |

### Unsupported or Misplaced Claims in the Generated Record

| Generated claim | Problem |
|---|---|
| Preparation step: `Dissolve all ingredients in distilled water to specified concentrations`. | The inspected MediaDB 405 page and TSV export give millimolar compounds but do not state the solvent or a dissolve protocol. |
| Preparation step: `Adjust pH if specified in original formulation`. | MediaDB Growth Data 785 gives pH 7.2 for the linked MG1363 growth condition, but the Medium 405 formulation page does not say to adjust the recipe to a pH value. The conditional wording is generic importer text. |
| Preparation step: `Sterilize by filtration (0.22 um) to preserve heat-sensitive components`. | MediaDB 405 does not publish a 0.22 um filtration instruction. |
| Curation history `Reference: Mazumdar et al. (2014) PLOS One`. | That is the MediaDB database paper, not the medium-specific primary source. MediaDB 405 points to `Jensen et al, 1993`; the source page identifies Applied and Environmental Microbiology and the title `Minimal Requirements for Exponential Growth ofLactococcus lactis`. |

The old ASM URL linked from MediaDB Source 128 returned a Cloudflare JavaScript challenge when checked during the adjacent Medium 402 review, so the original Jensen article body was not inspected from that publisher URL. This review relies on live MediaDB pages for the Medium 405 formula and Growth Data 785 metadata, and on the already-inspected MediaDB Source 128 page for the Jensen source metadata.

## Completeness

- **Ingredients:** complete relative to the MediaDB 405 export: all 35 ingredient names and millimolar amounts match exactly.
- **Grounding:** some exact chemical forms are represented with broader salts or acids, but they are inherited from MediaDB/MediaDB enrichment and are not unique to this record. Examples include `Molybdic acid ammonium salt tetrahydrate` grounded to anhydrous `ammonium molybdate`, `Calcium chloride anhydrous` grounded to `calcium dichloride`, and `Thiamine HCl` grounded to `thiamine hydrochloride`.
- **Source provenance:** incomplete. The source-specific MediaDB URL, Source 128 URL, Growth Data 785 URL, and Jensen source metadata are absent from `references` and from curation events; the record only preserves a generic MediaDB homepage note and a generic Mazumdar 2014 import-history note.
- **Growth context:** incomplete. MediaDB Growth Data 785 supports a scoped `Lactococcus lactis MG1363` growth context on MediaDB 405 with a 0.36 growth rate, pH 7.2, and temperature 30.0 C; the record has no `target_organisms`, `growth_metrics`, pH, or temperature context.
- **Preparation:** unsupported. All three `preparation_steps` appear to be generic MediaDB importer defaults rather than Medium 405 source claims.
- **Optional fields:** atmosphere, salinity, storage, and discussion are acceptable to leave empty because the inspected MediaDB 405, Source 128, and Growth Data 785 pages did not provide those details.
- **Raw cache:** no cached MediaDB 405 raw page was found under `data/raw`; the exact ignored-file-inclusive raw/import-tracking search only found `data/import_tracking/reports/deep_research_priority.json` metadata for this recipe.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Unsupported generic preparation steps are asserted as if they came from MediaDB Medium 405. | The live MediaDB 405 page and tab-delimited export list compounds and amounts, linked organisms, a linked source, and a linked growth-data record. They do not state a distilled-water dissolve step, a recipe pH adjustment, or 0.22 um filter sterilization. | `data/normalized_yaml/bacterial/bl_medium_arg_ser_trp.yaml`; broad repeats may require the MediaDB importer or a post-import cleanup rule. |
| Major | MediaDB's own primary source and growth-data context are not represented. | Medium 405 links Source 128 and Growth Data 785. Growth Data 785 reports `Lactococcus lactis MG1363 on Bl medium + arg + ser + trp`, growth rate 0.36, pH 7.2, and temperature 30.0; the YAML has no `references`, no `target_organisms`, no `growth_metrics`, no pH or temperature condition, and only names the generic Mazumdar 2014 MediaDB paper. | `data/normalized_yaml/bacterial/bl_medium_arg_ser_trp.yaml`; broad repeats may require MediaDB importer/enrichment changes. |

## Recommended Edits

1. Remove the three unsupported generic preparation steps from `data/normalized_yaml/bacterial/bl_medium_arg_ser_trp.yaml` unless a checked Jensen source or MediaDB page supports them.
2. Add structured `references` for MediaDB Medium 405, MediaDB Source 128, and MediaDB Growth Data 785; if Jensen 1993 can be inspected through a non-blocked authoritative copy, add its PMID or DOI instead of only the MediaDB source page.
3. Add a scoped growth assertion for `Lactococcus lactis MG1363` on `BL Medium + Arg + Ser + Trp`, preserving MediaDB Growth Data 785's growth rate 0.36, pH 7.2, and 30.0 C context and not generalizing it to the sibling BL Medium Arg, Asp, or low-MOPS records.
4. Review the exact salt/hydrate groundings for the MediaDB inorganic rows against the intended MediaDB compound identities before adding more source-specific evidence.

## Follow-up Checks

- Re-fetch MediaDB `/defined_media/media/405/`, `/defined_media/media_text/405/`, `/defined_media/sources/128/`, and `/defined_media/growthdata/785/` and manually compare the normalized ingredients, source, organism, pH, temperature, and growth rate.
- Run focused schema, strict, term, and reference validators on `data/normalized_yaml/bacterial/bl_medium_arg_ser_trp.yaml`.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating `data/merge_yaml/merged/`.
- After adding external article evidence, run the reference validator on any exact snippets before retaining them.

## Additional Notes

- The exact `find` for `*-bl_medium_arg_ser_trp.md` under ignored `reports/yaml_record_review/` found no existing report before this file was written.
- `data/merge_yaml/merged/bl_medium_arg.yaml`, `data/merge_yaml/merged/bl_medium_asp.yaml`, and `data/merge_yaml/merged/bl_medium_low_mops.yaml` are adjacent MediaDB/Jensen BL Medium variants and should be reviewed separately.
