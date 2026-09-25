# YAML Record Review: bm_in_arabinose_hodgson_et_al

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/bm_in_arabinose_hodgson_et_al.yaml`
- Started UTC: 2026-09-21T22:46:31Z
- Finished UTC: 2026-09-21T22:50:09Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `MediaRecipe` |
| Generated record ID | `CultureMech:007173` |
| Generated label | `bm_in_arabinose_hodgson_et_al` |
| Original name | `Bm in arabinose; hodgson et al` |
| Source term | `MEDIADB:273` / `Bm in arabinose; hodgson et al` |
| Maintained owner | `data/normalized_yaml/bacterial/bm_in_arabinose_hodgson_et_al.yaml` |
| Generated status | Derived from one active normalized MediaDB input by `merge_recipes.py`; future fixes belong in normalized YAML or the MediaDB importer, followed by merge regeneration |

The ignored-file-inclusive exact search for `CultureMech:007173`,
`MEDIADB:273`, `Medium ID: 273`, and `bm_in_arabinose_hodgson_et_al`
under `data`, `src`, and `scripts` found one active normalized owner plus
generated index, generated merge, registry, and import-tracking copies. It
found no raw MediaDB capture for medium 273 under those paths.

`find reports/yaml_record_review -name
'*bm_in_arabinose_hodgson_et_al.md'` returned no path before this report was
created.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Documented `just` schema entrypoint | `just validate-schema data/merge_yaml/merged/bm_in_arabinose_hodgson_et_al.yaml` | Failed before target-specific validation while the project `uv` environment tried to build `llvmlite==0.46.0` under Python 3.13; `setuptools` aborted with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'` |
| Open-schema LinkML | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/bm_in_arabinose_hodgson_et_al.yaml` | Passed with no diagnostics |
| Strict closed-schema validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/bm_in_arabinose_hodgson_et_al.yaml --out /private/tmp/bm_in_arabinose_hodgson_et_al.strict.tsv --workers 1 --quiet` | Passed, 1 file scanned, 0 error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/bm_in_arabinose_hodgson_et_al.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed, 0 checks, all validations passed |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/bm_in_arabinose_hodgson_et_al.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils`/`pkg_resources` warning |
| Embedded curation history | Not checked | No focused embedded `MediaRecipe.curation_history` validator is documented for one merged record; `just validate-history` targets standalone files under `history/` |

## Identity and Grounding

- The MediaDB media index lists medium 273 as `Bm in arabinose; hodgson et al`;
  the medium 273 page and tab-delimited export agree on that identity and on
  the nine-compound arabinose Bm formulation.
- `MEDIADB:273` links this medium to source 90, `Hodgson et al, 1982`, and
  not to the `Mazumdar et al. (2014) PLOS One` reference recorded in the
  MediaDB import curation history.
- Ingredient amounts in the YAML match the MediaDB 273 tab-delimited export:
  L-arabinose 10.0 mM, ethylene glycol 80.5542 mM, calcium chloride anhydrous
  0.00901024 mM, potassium dibasic phosphate 0.015 mM, magnesium sulfate
  2.43437 mM, ferrous sulfate 0.00359648 mM, zinc sulfate 0.0034779 mM,
  manganese chloride 0.0044829 mM, and ammonium nitrate 24.9838 mM.
- The generated merge is stale relative to the active normalized owner:
  `data/normalized_yaml/bacterial/bm_in_arabinose_hodgson_et_al.yaml` carries
  the August 20 MIM grounding for L-arabinose to `CHEBI:30849`, while the
  generated merge still leaves L-arabinose without a `term`.

## Evidence

Inspected sources:

| Source | Scope checked |
| --- | --- |
| `/private/tmp/mediadb-273.html` | MediaDB medium 273 identity, ingredient list, source link, organism links, and growth-data links |
| `/private/tmp/mediadb-273.tsv` | MediaDB medium 273 tab-delimited compound amounts and source-side chemical cross-references |
| `/private/tmp/mediadb-source-90.html` | MediaDB source 90 bibliographic metadata and all Hodgson et al. growth-data links |
| `/private/tmp/mediadb-growth-566.html` | J802 growth row on MediaDB medium 273 |
| `/private/tmp/mediadb-growth-573.html` | J845 growth row on MediaDB medium 273 |
| `/private/tmp/mediadb-growth-580.html` | J846 growth row on MediaDB medium 273 |
| `/private/tmp/mediadb-growth-587.html` | J847 growth row on MediaDB medium 273 |
| `data/normalized_yaml/bacterial/bm_in_arabinose_hodgson_et_al.yaml` | Maintained owner state after the August 20 L-arabinose grounding |

Supported:

- MediaDB 273 supports the generated record's stable external identity,
  original name, defined/liquid classification, nine ingredient labels, and
  nine mM ingredient amounts.
- MediaDB source 90 resolves the medium source to Hodgson et al., Journal of
  General Microbiology, 1982, with the title `Glucose repression of carbon
  source uptake and metabolism in streptomyces coelicolor a3(2) and its
  perturbation in mutants resistant to 2-deoxyglucose`.
- The four MediaDB growth rows support source-scoped growth rates for
  `Streptomyces coelicolor` J802, J845, J846, and J847 on medium 273 with no
  MediaDB pH or temperature value.

Unsupported or over-scoped:

- The `mediadb-import` curation-history entry names medium 273 but records
  `Mazumdar et al. (2014) PLOS One`; the inspected MediaDB page for medium 273
  and the linked source 90 page attribute this recipe to Hodgson et al. 1982.
- The generated record says to dissolve all ingredients, adjust pH if specified
  in the original formulation, and filter-sterilize at 0.22 um to preserve
  heat-sensitive components; neither the inspected MediaDB medium page nor its
  tab-delimited export provides those preparation instructions.
- The generic application labels for cultivation of genome-sequenced organisms,
  metabolic modeling, and systems biology research are database-level
  import defaults; the inspected medium 273 page did not assert those three
  applications specifically for Bm in arabinose.

## Completeness

- Consequentially incomplete in the generated layer: it predates the August 20
  normalized L-arabinose grounding and still publishes an ungrounded direct
  ingredient.
- Consequentially incomplete in the maintained MediaDB owner: MediaDB links
  medium 273 to four growth rows, but the normalized and generated records
  have no `target_organisms` or `growth_metrics` entries for J802, J845, J846,
  or J847.
- Empty pH, temperature, salinity, atmosphere, and storage fields are not
  defects here: MediaDB 273 and its four inspected growth rows do not provide
  those values.
- Bounded search: ignored files were included in the exact search described
  under `Target`, and no second active normalized owner or raw MediaDB medium
  273 capture was found under `data`, `src`, or `scripts`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | The generated merge is stale and lacks the active normalized owner's August 20 grounding of L-arabinose to `CHEBI:30849`. | Diff between `data/merge_yaml/merged/bm_in_arabinose_hodgson_et_al.yaml` and `data/normalized_yaml/bacterial/bm_in_arabinose_hodgson_et_al.yaml`. | No normalized edit is needed for this defect; regenerate `data/merge_yaml/merged/bm_in_arabinose_hodgson_et_al.yaml` from the repaired normalized owner. |
| major | The MediaDB import provenance cites Mazumdar et al. 2014, but MediaDB 273 and source 90 identify Hodgson et al. 1982 as the source for this formulation. | `/private/tmp/mediadb-273.html`; `/private/tmp/mediadb-source-90.html`. | `data/normalized_yaml/bacterial/bm_in_arabinose_hodgson_et_al.yaml` or the MediaDB import metadata that produced its first `curation_history` entry. |
| major | The preparation steps are generic and unsupported by the inspected MediaDB source for medium 273. | `/private/tmp/mediadb-273.html` lists ingredients, organisms, source, and growth rows but no dissolution, pH-adjustment, or filter-sterilization procedure; `/private/tmp/mediadb-273.tsv` lists only compounds and amounts. | `data/normalized_yaml/bacterial/bm_in_arabinose_hodgson_et_al.yaml` or the MediaDB importer if it injected those default steps. |
| major | The record omits the four source-linked growth observations available from MediaDB for this exact medium. | Growth-data pages 566, 573, 580, and 587 on MediaDB medium 273, all linked from the medium 273 page. | `data/normalized_yaml/bacterial/bm_in_arabinose_hodgson_et_al.yaml` or a maintained MediaDB growth-data import overlay. |
| minor | The `applications` entries are generic database-scope claims, not medium-specific claims on the inspected MediaDB 273 page. | `/private/tmp/mediadb-273.html`; `/private/tmp/mediadb-273.tsv`. | `data/normalized_yaml/bacterial/bm_in_arabinose_hodgson_et_al.yaml` or the MediaDB importer if it added default application labels. |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/bm_in_arabinose_hodgson_et_al.yaml` so
   the generated record inherits the existing L-arabinose `CHEBI:30849`
   grounding from
   `data/normalized_yaml/bacterial/bm_in_arabinose_hodgson_et_al.yaml`.
2. Correct the maintained MediaDB provenance for medium 273 so the first import
   event and any source metadata point to Hodgson et al. 1982 rather than
   Mazumdar et al. 2014.
3. Remove or replace the unsupported generic `DISSOLVE`, `ADJUST_PH`, and
   `FILTER_STERILIZE` preparation steps in the normalized owner. Preserve only
   procedure text supported by MediaDB 273, Hodgson et al. 1982, or another
   inspected primary source.
4. Curate the four MediaDB growth rows for `Streptomyces coelicolor` J802,
   J845, J846, and J847 on medium 273 as source-scoped growth evidence, or add
   a quality flag explaining why MediaDB growth-data rows are intentionally out
   of scope for this importer.
5. Drop, narrow, or explicitly justify the generic `applications` labels if
   they remain MediaDB-wide import defaults rather than medium-specific
   assertions.
6. Do not patch `data/merge_yaml/merged/bm_in_arabinose_hodgson_et_al.yaml`
   directly; it is a derived record.

## Follow-up Checks

- Run the focused schema, strict, term, and reference validators on
  `data/normalized_yaml/bacterial/bm_in_arabinose_hodgson_et_al.yaml`.
- Run the same validators on
  `data/merge_yaml/merged/bm_in_arabinose_hodgson_et_al.yaml` after merge
  regeneration.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating
  merge outputs.
- Re-fetch MediaDB medium 273, `/defined_media/media_text/273/`, source 90,
  and growth rows 566, 573, 580, and 587, then manually verify the regenerated
  record's ingredient, source-provenance, and growth-evidence claims against
  those inspected pages.

## Additional Notes

- This review intentionally wrote only this Markdown report. The generated
  merge record and normalized owner YAML were left unchanged.
