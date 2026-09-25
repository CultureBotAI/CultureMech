# YAML Record Review: mmsuc_jasiecki_et_al

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mmsuc_jasiecki_et_al.yaml
- Started UTC: 2026-09-24T09:35:20Z
- Finished UTC: 2026-09-24T09:37:17Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:007030 |
| Label | mmsuc_jasiecki_et_al |
| Original label | Mmsuc; jasiecki et al |
| Source term | MEDIADB:140, Mmsuc; jasiecki et al |
| Maintained owner | data/normalized_yaml/bacterial/mmsuc_jasiecki_et_al.yaml |
| Reviewed artifact | data/merge_yaml/merged/mmsuc_jasiecki_et_al.yaml |
| Generated? | Yes. The `merge_recipes.py` history event reports a merge from `mmsuc_jasiecki_et_al.yaml`; future edits should land in the normalized MediaDB record or the MediaDB importer and then regenerate this merged artifact. |

I searched for `CultureMech:007030`, `mmsuc_jasiecki_et_al`, `Mmsuc; jasiecki et al`, `MEDIADB:140`, and `Medium ID: 140` with `rg --no-ignore --hidden` across this record, its normalized owner, the ID registry, the recipe catalog, archived validation reports, import reports, and the review manifest. The search included ignored files and found one maintained normalized owner for the ID.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open LinkML schema validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mmsuc_jasiecki_et_al.yaml` | Passed with `No issues found`. |
| Strict validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/mmsuc_jasiecki_et_al.yaml --out /private/tmp/mmsuc_jasiecki_et_al.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. `/private/tmp/mmsuc_jasiecki_et_al.strict.tsv` has 1 line, so only the TSV header was emitted. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/mmsuc_jasiecki_et_al.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/mmsuc_jasiecki_et_al.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the expected `eutils/pkg_resources` warning. |
| Embedded history | `just validate-history` | Not checked: the repository history validator validates standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

## Identity and Grounding

The CultureMech ID, slug, `media_term`, and maintained path all identify MediaDB medium 140, `Mmsuc; jasiecki et al`. The live MediaDB medium page for `/defined_media/media/140/` reports the same medium label, 10 compounds with mM amounts, two organism rows, source 44, and two growth-data records; `/defined_media/media_text/140/` reports the same 10 tab-delimited compound rows and concentrations.

The MediaDB source page for source 44 identifies Jasiecki et al. 2003 and PMID 12612607. Crossref resolves the same article, `Growth-rate dependent RNA polyadenylation in Escherichia coli`, to DOI `10.1038/sj.embor.embor733`. I also inspected the publisher PDF and confirmed that `MMSuc` is the succinate variant of a minimal-salts medium adjusted to pH 7.2 and cultured at 37 C.

The exact phosphate form is not grounded. The Jasiecki recipe used disodium hydrogen phosphate dodecahydrate, but the record grounds `Dibasic sodium phosphate` only to anhydrous `CHEBI:34683`.

## Evidence

Supported by inspected MediaDB and article sources:

- MediaDB 140 and the primary article both denote the succinate variant of Jasiecki et al.'s minimal medium.
- The 10 MediaDB mM rows match the generated ingredient concentrations.
- The primary article supports the same minimal salts recipe: Tris, maleic acid, NaCl, KCl, NH4Cl, MgCl2 x 6 H2O, Na2SO4, Na2HPO4 x 12 H2O, thiamine, and the MMSuc carbon source, sodium succinate.
- The primary article supports pH 7.2 and 37 C as medium/growth context.
- MediaDB growthdata 278 and 282 match the primary article's Table 1 generation times for `MMSuc`: 140 minutes for `MG1655/pKB2` and 86 minutes for `VH1000::ppcnB-lacZ`, converted in MediaDB to 0.297 1/h and 0.484 1/h.

Unsupported or over-scoped:

- The record omits the source pH 7.2.
- The primary article does not support the generated 0.22 um filter-sterilization step.
- The two MediaDB growth rows are absent from `target_organisms` and any scoped growth-evidence structure.
- The MediaDB page and the primary paper support Jasiecki et al. 2003, but the embedded January import event cites `Mazumdar et al. (2014) PLOS One`.
- The generic `Cultivation of genome-sequenced organisms`, `Metabolic modeling`, and `Systems biology research` application tags are not stated on the inspected MediaDB 140, source 44, organism 57/58, growth-data 278/282, or Jasiecki PDF sources.

## Completeness

The imported compound list is present and the mM values match MediaDB and the primary article after g/L to mM conversion.

Consequential gaps:

- Both MediaDB succinate growth rows are missing: `Escherichia coli MG1655 / pKB2`, 0.297 1/h, 37 C; and `Escherichia coli VH1000 :: ppcnB-lacZ`, 0.484 1/h, 37 C.
- The record lacks pH 7.2 even though the primary recipe states it.
- The record has no structured reference for DOI `10.1038/sj.embor.embor733` or PMID 12612607.
- The record has no discussion flag to distinguish what MediaDB supplied from what the primary Jasiecki paper additionally supplies.

Empty optional fields that are not inherently defects:

- The record has no variants, parent recipe, or nested stock solutions; MediaDB 140 did not list nested stocks and the primary recipe is a single final-medium formulation.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Blocker | None found | The file is valid YAML, its ID and `MEDIADB:140` source term resolve to one MediaDB medium, and schema, strict, reference, and term validation passed. | Not applicable |
| Major | The pH 7.2 source condition is missing. | The Jasiecki PDF states the minimal medium salts and pH 7.2; the generated record has only the placeholder step `Adjust pH if specified in original formulation`. | Add source-backed pH 7.2 in `data/normalized_yaml/bacterial/mmsuc_jasiecki_et_al.yaml` and teach `src/culturemech/import/mediadb_importer.py` not to replace known pH with a generic placeholder. |
| Major | Two MediaDB growth conditions are missing. | MediaDB links growthdata 278 and 282 from medium 140; the growth pages report 0.297 1/h for `Escherichia coli MG1655 / pKB2` and 0.484 1/h for `Escherichia coli VH1000 :: ppcnB-lacZ`, both at 37 C. The generated record has no `target_organisms`. | Add MediaDB growth-data import support in `src/culturemech/import/mediadb_importer.py`, or curate `data/normalized_yaml/bacterial/mmsuc_jasiecki_et_al.yaml` if the importer will not be rerun. |
| Major | Source provenance cites the wrong paper and omits the structured Jasiecki source. | MediaDB source 44 names Jasiecki et al. 2003 and PMID 12612607, and Crossref resolves DOI `10.1038/sj.embor.embor733`; the embedded import event cites `Mazumdar et al. (2014) PLOS One` because `_create_curation_history` hard-codes that reference. | Fix `src/culturemech/import/mediadb_importer.py` and repair the existing curation event/source metadata in `data/normalized_yaml/bacterial/mmsuc_jasiecki_et_al.yaml`. |
| Major | The exact phosphate hydrate is wrong. | The primary Jasiecki recipe used `Na2HPO4 x 12 H2O`; the record stores `Dibasic sodium phosphate` with `CHEBI:34683`, an anhydrous disodium hydrogenphosphate term. | Preserve the dodecahydrate form in `data/normalized_yaml/bacterial/mmsuc_jasiecki_et_al.yaml`; if no exact CHEBI term is available, leave the text explicit rather than mapping to an adjacent anhydrous salt. |
| Major | Filter sterilization is source-unsupported. | The record uses the MediaDB importer's unconditional 0.22 um filter-sterilization default; the MediaDB page does not provide a preparation protocol and the inspected Jasiecki text does not state filter sterilization. | Remove or qualify generic MediaDB preparation defaults in `src/culturemech/import/mediadb_importer.py`; update the normalized record to keep only source-backed steps. |
| Minor | Two cross-reference notes mislabel BiGG IDs as KEGG IDs. | MediaDB's text export separates KEGG IDs from BiGG IDs, but `Thiamine` and `Maleic acid` carry notes `KEGG:thm` and `KEGG:male`; those are the BiGG values in the MediaDB row. | Repair MediaDB xref note construction in `src/culturemech/import/mediadb_importer.py` and update `data/normalized_yaml/bacterial/mmsuc_jasiecki_et_al.yaml`. |
| Minor | One deprecated MediaIngredientMech slot remains after migration. | `Thiamine` still has `mediaingredientmech_term: MediaIngredientMech:000898` even though the June 2026 history event says seven legacy MediaIngredientMech IDs were replaced with CHEBI-keyed links where id-safe. | Re-run or patch the MediaIngredientMech migration for this ingredient in `data/normalized_yaml/bacterial/mmsuc_jasiecki_et_al.yaml` if `CHEBI:18385` is an id-safe mapping. |
| Minor | Generic application tags are over-broad for this single source record. | The inspected sources do not assert the three generic MediaDB application strings for the Jasiecki succinate medium. | Replace generic MediaDB application defaults with evidence-backed applications in `src/culturemech/import/mediadb_importer.py` or remove them from the normalized record. |

## Recommended Edits

1. Add a structured reference for Jasiecki et al. 2003, PMID 12612607, DOI `10.1038/sj.embor.embor733`, and fix the hard-coded Mazumdar import note.
2. Add pH 7.2 and 37 C as source-backed recipe/growth context for the Jasiecki minimal media.
3. Import or curate MediaDB growthdata 278 and 282 as two separate E. coli strain-specific growth claims on MediaDB 140.
4. Correct the dibasic sodium phosphate ingredient to preserve the dodecahydrate form stated in the primary recipe.
5. Remove the unsupported generic filter-sterilization step and keep preparation fields limited to source-backed statements.
6. Correct the BiGG/KEGG note labeling for `thm` and `male`.
7. Finish converting the leftover thiamine `mediaingredientmech_term` if the CHEBI mapping is id-safe.
8. Remove or substantiate the generic application tags.

## Follow-up Checks

- Rerun the focused schema, strict, reference, and term validators against both `data/normalized_yaml/bacterial/mmsuc_jasiecki_et_al.yaml` and the regenerated `data/merge_yaml/merged/mmsuc_jasiecki_et_al.yaml`.
- Re-open `/defined_media/media/140/`, `/defined_media/media_text/140/`, `/defined_media/sources/44/`, `/defined_media/organisms/57/`, `/defined_media/organisms/58/`, `/defined_media/growthdata/278/`, and `/defined_media/growthdata/282/` and verify each curated MediaDB identifier.
- Compare any g/L to mM conversions against the Jasiecki PDF before changing exact chemical forms; hydrate changes alter formula weights even when the MediaDB mM row is correct.
- Rerun merge verification after regeneration and confirm only `merge_recipes.py`-owned fields changed in `data/merge_yaml/merged/mmsuc_jasiecki_et_al.yaml`.

## Additional Notes

- The Wiley full-XML endpoint for the DOI was blocked by a Cloudflare challenge, but the EMBO Press/Springer PDF endpoint returned a readable publisher PDF.
- No local raw MediaDB SQL capture was present when I searched under `data` with gitignore-independent `find` during the adjacent MediaDB review; the reviewed evidence here came from live MediaDB plus the publisher PDF.
- No GitHub issue, PR, or comment was created or edited by this read-only review.
