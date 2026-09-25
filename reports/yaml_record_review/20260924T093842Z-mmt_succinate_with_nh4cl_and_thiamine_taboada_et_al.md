# YAML Record Review: mmt_succinate_with_nh4cl_and_thiamine_taboada_et_al

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mmt_succinate_with_nh4cl_and_thiamine_taboada_et_al.yaml
- Started UTC: 2026-09-24T09:37:30Z
- Finished UTC: 2026-09-24T09:38:43Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:007061 |
| Label | mmt_succinate_with_nh4cl_and_thiamine_taboada_et_al |
| Original label | MMT-Succinate with NH4Cl and thiamine; Taboada et al |
| Source term | MEDIADB:170, MMT-Succinate with NH4Cl and thiamine; Taboada et al |
| Maintained owner | data/normalized_yaml/bacterial/mmt_succinate_with_nh4cl_and_thiamine_taboada_et_al.yaml |
| Reviewed artifact | data/merge_yaml/merged/mmt_succinate_with_nh4cl_and_thiamine_taboada_et_al.yaml |
| Generated? | Yes. The `merge_recipes.py` history event reports a merge from `mmt_succinate_with_nh4cl_and_thiamine_taboada_et_al.yaml`; future edits should land in the normalized MediaDB record or the MediaDB importer and then regenerate this merged artifact. |

I searched for `mmt_succinate_with_nh4cl_and_thiamine_taboada_et_al`, `Mmt succinate with nh4cl and thiamine taboada et al`, and `MEDIADB:` with `rg --no-ignore --hidden` across the target, its normalized owner, the CultureMech ID registry, and the recipe catalog. The search included ignored files and found `CultureMech:007061` owned by `data/normalized_yaml/bacterial/mmt_succinate_with_nh4cl_and_thiamine_taboada_et_al.yaml`.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open LinkML schema validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mmt_succinate_with_nh4cl_and_thiamine_taboada_et_al.yaml` | Passed with `No issues found`. |
| Strict validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/mmt_succinate_with_nh4cl_and_thiamine_taboada_et_al.yaml --out /private/tmp/mmt_succinate_with_nh4cl_and_thiamine_taboada_et_al.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. `/private/tmp/mmt_succinate_with_nh4cl_and_thiamine_taboada_et_al.strict.tsv` has 1 line, so only the TSV header was emitted. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/mmt_succinate_with_nh4cl_and_thiamine_taboada_et_al.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/mmt_succinate_with_nh4cl_and_thiamine_taboada_et_al.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the expected `eutils/pkg_resources` warning. |
| Embedded history | `just validate-history` | Not checked: the repository history validator validates standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

## Identity and Grounding

The CultureMech ID, slug, and `media_term` identify MediaDB medium 170, `Mmt-succinate with nh4cl and thiamine; taboada et al`. The live MediaDB medium page for `/defined_media/media/170/` reports the same medium, seven compounds with mM amounts, four `Rhizobium etli` organism rows, source 63, and four growth-data records; `/defined_media/media_text/170/` reports the same seven tab-delimited compound rows and concentrations.

The generated merge is stale relative to its owner. `data/normalized_yaml/bacterial/mmt_succinate_with_nh4cl_and_thiamine_taboada_et_al.yaml` was repaired on 2026-08-31 by `repair_mediadb_names.py` and now restores `Iron(III) chloride`, but this 2026-08-06 merge still contains only the parse fragment `'''Iron(III` for the 0.0184 mM ingredient.

MediaDB source 63 identifies Taboada et al. 2008 and PMID 18177306. Crossref resolves the Taboada paper to DOI `10.1111/j.1574-6968.2007.01006.x`. The record instead has only a generic MediaDB note and an import history line citing `Mazumdar et al. (2014) PLOS One`.

## Evidence

Supported by inspected MediaDB endpoints:

- MediaDB 170 is the thiamine-supplemented, NH4Cl-containing MMT succinate formulation from Taboada et al.
- The seven source compounds and mM amounts match the MediaDB tab-delimited export.
- MediaDB growthdata 342, 343, 344, and 345 each point back to MediaDB 170 and source 63.
- The four MediaDB growth rows give pH 6.8, 28 C, and `Second subculture` for strains CE3, M4, Viking 1, and CIAT613.

Unsupported or over-scoped:

- The generated `'''Iron(III` row is not a MediaDB compound label; MediaDB 170 says `Iron(III) chloride`.
- The MediaDB row carries ChEBI 30808 for iron(III) chloride, but neither the generated merge nor the already repaired normalized owner has a structured ontology term for that ingredient.
- The record omits the pH 6.8 and 28 C conditions attached to every MediaDB 170 growth row.
- The record omits all four strain-specific `Rhizobium etli` growth claims.
- The generated dissolve, conditional pH-adjustment, and 0.22 um filter-sterilization steps are generic importer defaults; MediaDB 170 does not expose a preparation protocol.
- The embedded January import event cites the wrong publication.

## Completeness

The seven-compound table is present and its mM amounts match MediaDB's text export.

Consequential gaps:

- Four growth rows are missing: CE3 at 0.251191 1/h, M4 at 0.298289 1/h, Viking 1 at 0.308756 1/h, and CIAT613 at 0.248574 1/h.
- The common pH 6.8 and 28 C context for those growth rows is absent.
- DOI `10.1111/j.1574-6968.2007.01006.x`, PMID 18177306, and MediaDB source 63 are not represented structurally.
- The repaired normalized owner still has no ChEBI term for iron(III) chloride even though the MediaDB export lists ChEBI 30808 for that row.

Empty optional fields that are not inherently defects:

- The source page groups related Taboada/Encarnacion variants, but MediaDB 170 itself did not provide a parent recipe, stock solution, or in-page variant relation that this generated record would be expected to encode.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Blocker | None found | The file is valid YAML, its ID and `MEDIADB:170` source term resolve to one MediaDB medium, and schema, strict, reference, and term validation passed. | Not applicable |
| Major | The merged artifact is stale and still exposes the old MediaDB SQL parser truncation. | The generated record's 0.0184 mM iron ingredient has `preferred_term: '''Iron(III`; MediaDB 170 and the normalized owner call that row `Iron(III) chloride`; the normalized owner already has a 2026-08-31 `REPAIRED_MEDIADB_TRUNCATED_NAME` event. | Regenerate `data/merge_yaml/merged/mmt_succinate_with_nh4cl_and_thiamine_taboada_et_al.yaml` from the repaired normalized owner; if regeneration reintroduces the fragment, fix `scripts/merge_recipes.py` or the MediaDB merge input path. |
| Major | Four MediaDB growth conditions are missing. | MediaDB links growthdata 342, 343, 344, and 345 from medium 170; the generated record has no `target_organisms` for CE3, M4, Viking 1, or CIAT613 and no growth-rate evidence. | Add MediaDB growth-data import support in `src/culturemech/import/mediadb_importer.py`, or curate the four rows in `data/normalized_yaml/bacterial/mmt_succinate_with_nh4cl_and_thiamine_taboada_et_al.yaml`. |
| Major | The shared pH and temperature context is missing. | Each inspected MediaDB 170 growth page reports pH 6.8 and temperature 28.0. The record keeps the placeholder pH-adjustment text and no 28 C condition. | Curate pH and temperature in the normalized owner, scoped to the Taboada growth evidence unless primary source inspection proves they are recipe-wide. |
| Major | Source provenance cites the wrong paper and omits the structured Taboada source. | MediaDB source 63 names Taboada et al. 2008 and PMID 18177306, and Crossref resolves DOI `10.1111/j.1574-6968.2007.01006.x`; the embedded import event cites `Mazumdar et al. (2014) PLOS One` because `_create_curation_history` hard-codes that reference. | Fix `src/culturemech/import/mediadb_importer.py` and repair the existing curation event/source metadata in the normalized owner. |
| Major | The known iron(III) chloride ontology mapping was lost. | The MediaDB 170 text export lists ChEBI 30808 for `Iron(III) chloride`; both the stale merge and the repaired normalized owner leave the ingredient ungrounded. | After regenerating the repaired name, add the exact ChEBI 30808 mapping to `data/normalized_yaml/bacterial/mmt_succinate_with_nh4cl_and_thiamine_taboada_et_al.yaml` if it resolves to iron(III) chloride in the packaged term index. |
| Major | Filter sterilization is source-unsupported. | The record uses the MediaDB importer's unconditional 0.22 um filter-sterilization default; the inspected MediaDB source exposes no preparation protocol. | Remove or qualify generic MediaDB preparation defaults in `src/culturemech/import/mediadb_importer.py`; update the normalized record to keep only source-backed steps. |
| Minor | Two cross-reference notes mislabel BiGG IDs as KEGG IDs. | MediaDB's text export separates KEGG IDs from BiGG IDs, but `Succinate` and `Thiamine` carry notes `KEGG:succ` and `KEGG:thm`; those are the BiGG values in the MediaDB rows. | Repair MediaDB xref note construction in `src/culturemech/import/mediadb_importer.py` and update the normalized record. |
| Minor | One deprecated MediaIngredientMech slot remains after migration. | `Thiamine` still has `mediaingredientmech_term: MediaIngredientMech:000898` even though the June 2026 history event says three legacy MediaIngredientMech IDs were replaced with CHEBI-keyed links where id-safe. | Re-run or patch the MediaIngredientMech migration for this ingredient in the normalized owner if `CHEBI:18385` is an id-safe mapping. |
| Minor | Generic application tags are over-broad for this single source record. | The inspected MediaDB pages do not assert `Cultivation of genome-sequenced organisms`, `Metabolic modeling`, or `Systems biology research` as applications of this Taboada medium. | Replace generic MediaDB application defaults with evidence-backed applications in `src/culturemech/import/mediadb_importer.py` or remove them from the normalized record. |

## Recommended Edits

1. Regenerate the merged YAML from the repaired normalized record so `Iron(III) chloride` replaces `'''Iron(III`.
2. Add ChEBI 30808 grounding for the iron(III) chloride ingredient after confirming the local term label exactly matches the MediaDB compound.
3. Add structured Taboada et al. 2008 source metadata with PMID 18177306 and DOI `10.1111/j.1574-6968.2007.01006.x`, and fix the hard-coded Mazumdar import note.
4. Import or curate MediaDB growthdata 342, 343, 344, and 345 as four separate `Rhizobium etli` strain-specific growth claims.
5. Scope pH 6.8, 28 C, and `Second subculture` to those four growth rows unless primary source inspection supports a broader placement.
6. Remove the unsupported generic filter-sterilization step and keep preparation fields limited to source-backed statements.
7. Correct the BiGG/KEGG note labeling for `succ` and `thm`.
8. Finish converting the leftover thiamine `mediaingredientmech_term` if the CHEBI mapping is id-safe.
9. Remove or substantiate the generic application tags.

## Follow-up Checks

- Rerun the focused schema, strict, reference, and term validators against both the normalized owner and the regenerated merged record.
- Re-open `/defined_media/media/170/`, `/defined_media/media_text/170/`, `/defined_media/sources/63/`, and `/defined_media/growthdata/342` through `/growthdata/345` and verify each curated MediaDB identifier.
- Inspect DOI `10.1111/j.1574-6968.2007.01006.x` before broadening pH or preparation claims from growth-context evidence to recipe-level assertions.
- Rerun merge verification after regeneration and confirm `'''Iron(III` no longer appears in the merged artifact.

## Additional Notes

- The OUP article PDF endpoint was blocked by a Cloudflare challenge, so I did not inspect the Taboada et al. primary paper.
- The exact search for growthdata IDs and the four MediaDB growth-rate values found no representation of those growth rows in this normalized or merged record; the search used `rg --no-ignore --hidden` and included ignored files in the scoped paths searched.
- No GitHub issue, PR, or comment was created or edited by this read-only review.
