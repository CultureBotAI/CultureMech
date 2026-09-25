# YAML Record Review: bm_in_galactose_hodgson_et_al

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/bm_in_galactose_hodgson_et_al.yaml`
- Started UTC: 2026-09-21T22:54:44Z
- Finished UTC: 2026-09-21T22:55:32Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `MediaRecipe` |
| Generated record ID | `CultureMech:007175` |
| Generated label | `bm_in_galactose_hodgson_et_al` |
| Original name | `Bm in galactose; hodgson et al` |
| Source term | `MEDIADB:275` / `Bm in galactose; hodgson et al` |
| Maintained owner | `data/normalized_yaml/bacterial/bm_in_galactose_hodgson_et_al.yaml` |
| Generated status | Derived from one active normalized MediaDB input by `merge_recipes.py`; future fixes belong in normalized YAML or the MediaDB importer, followed by merge regeneration |

The ignored-file-inclusive exact search for `CultureMech:007175`,
`MEDIADB:275`, `Medium ID: 275`, and `bm_in_galactose_hodgson_et_al`
under `data`, `src`, and `scripts` found one active normalized owner plus
generated index, generated merge, registry, and import-tracking copies. It
found no raw MediaDB capture for medium 275 under those paths.

`find reports/yaml_record_review -name '*bm_in_galactose_hodgson_et_al.md'`
returned no path before this report was created.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open-schema LinkML | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/bm_in_galactose_hodgson_et_al.yaml` | Passed with no diagnostics |
| Strict closed-schema validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/bm_in_galactose_hodgson_et_al.yaml --out /private/tmp/bm_in_galactose_hodgson_et_al.strict.tsv --workers 1 --quiet` | Passed, 1 file scanned, 0 error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/bm_in_galactose_hodgson_et_al.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed, 0 checks, all validations passed |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/bm_in_galactose_hodgson_et_al.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils`/`pkg_resources` warning |
| Embedded curation history | Not checked | No focused embedded `MediaRecipe.curation_history` validator is documented for one merged record; `just validate-history` targets standalone files under `history/` |

The documented `just validate-schema` entrypoint was checked during this
MediaDB review batch and failed before target-specific validation while the
project `uv` environment tried to build `llvmlite==0.46.0` under Python 3.13.
The no-project Python 3.11 commands above exercise the same target validators.

## Identity and Grounding

- The MediaDB media index and medium 275 page identify this source accession as
  `Bm in galactose; hodgson et al`.
- `MEDIADB:275` links this medium to source 90, `Hodgson et al, 1982`, and
  not to the `Mazumdar et al. (2014) PLOS One` reference recorded in the
  MediaDB import curation history.
- Ingredient amounts in the YAML match the MediaDB 275 tab-delimited export:
  D-galactose 10.0 mM, ethylene glycol 80.5542 mM, calcium chloride anhydrous
  0.00901024 mM, potassium dibasic phosphate 0.015 mM, magnesium sulfate
  2.43437 mM, ferrous sulfate 0.00359648 mM, zinc sulfate 0.0034779 mM,
  manganese chloride 0.0044829 mM, and ammonium nitrate 24.9838 mM.
- The generated merge matches the active normalized owner for ingredient
  identities and concentrations; the defects below are source-owned MediaDB
  import defects, not merge staleness.

## Evidence

Inspected sources:

| Source | Scope checked |
| --- | --- |
| `/private/tmp/mediadb-275.html` | MediaDB medium 275 identity, ingredient list, source link, organism links, and growth-data links |
| `/private/tmp/mediadb-275.tsv` | MediaDB medium 275 tab-delimited compound amounts and source-side chemical cross-references |
| `/private/tmp/mediadb-source-90.html` | MediaDB source 90 bibliographic metadata and all Hodgson et al. growth-data links |
| `/private/tmp/mediadb-growth-568.html` | J802 growth row on MediaDB medium 275 |
| `/private/tmp/mediadb-growth-575.html` | J845 growth row on MediaDB medium 275 |
| `/private/tmp/mediadb-growth-582.html` | J846 growth row on MediaDB medium 275 |
| `/private/tmp/mediadb-growth-589.html` | J847 growth row on MediaDB medium 275 |
| `data/normalized_yaml/bacterial/bm_in_galactose_hodgson_et_al.yaml` | Maintained MediaDB owner for medium 275 |

Supported:

- MediaDB 275 supports the generated record's stable external identity,
  original name, defined/liquid classification, nine ingredient labels, and
  nine mM ingredient amounts.
- MediaDB source 90 resolves the medium source to Hodgson et al., Journal of
  General Microbiology, 1982, with the title `Glucose repression of carbon
  source uptake and metabolism in streptomyces coelicolor a3(2) and its
  perturbation in mutants resistant to 2-deoxyglucose`.
- The four MediaDB growth rows support source-scoped growth rates for
  `Streptomyces coelicolor` J802, J845, J846, and J847 on medium 275 with no
  MediaDB pH or temperature value.

Unsupported or over-scoped:

- The `mediadb-import` curation-history entry names medium 275 but records
  `Mazumdar et al. (2014) PLOS One`; the inspected MediaDB page for medium 275
  and the linked source 90 page attribute this recipe to Hodgson et al. 1982.
- The generated record says to dissolve all ingredients, adjust pH if specified
  in the original formulation, and filter-sterilize at 0.22 um to preserve
  heat-sensitive components; neither the inspected MediaDB medium page nor its
  tab-delimited export provides those preparation instructions.
- The generic application labels for cultivation of genome-sequenced organisms,
  metabolic modeling, and systems biology research are database-level
  import defaults; the inspected medium 275 page did not assert those three
  applications specifically for Bm in galactose.

## Completeness

- Consequentially incomplete in the maintained MediaDB owner: MediaDB links
  medium 275 to four growth rows, but the normalized and generated records
  have no `target_organisms` or `growth_metrics` entries for J802, J845, J846,
  or J847.
- Complete enough for direct ingredients: the generated record carries all
  nine compounds and all nine amounts from the MediaDB 275 tab-delimited
  export.
- Empty pH, temperature, salinity, atmosphere, and storage fields are not
  defects here: MediaDB 275 and its four inspected growth rows do not provide
  those values.
- Bounded search: ignored files were included in the exact search described
  under `Target`, and no second active normalized owner or raw MediaDB medium
  275 capture was found under `data`, `src`, or `scripts`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | The MediaDB import provenance cites Mazumdar et al. 2014, but MediaDB 275 and source 90 identify Hodgson et al. 1982 as the source for this formulation. | `/private/tmp/mediadb-275.html`; `/private/tmp/mediadb-source-90.html`. | `data/normalized_yaml/bacterial/bm_in_galactose_hodgson_et_al.yaml` or the MediaDB import metadata that produced its first `curation_history` entry. |
| major | The preparation steps are generic and unsupported by the inspected MediaDB source for medium 275. | `/private/tmp/mediadb-275.html` lists ingredients, organisms, source, and growth rows but no dissolution, pH-adjustment, or filter-sterilization procedure; `/private/tmp/mediadb-275.tsv` lists only compounds and amounts. | `data/normalized_yaml/bacterial/bm_in_galactose_hodgson_et_al.yaml` or the MediaDB importer if it injected those default steps. |
| major | The record omits the four source-linked growth observations available from MediaDB for this exact medium. | Growth-data pages 568, 575, 582, and 589 on MediaDB medium 275, all linked from the medium 275 page. | `data/normalized_yaml/bacterial/bm_in_galactose_hodgson_et_al.yaml` or a maintained MediaDB growth-data import overlay. |
| minor | The `applications` entries are generic database-scope claims, not medium-specific claims on the inspected MediaDB 275 page. | `/private/tmp/mediadb-275.html`; `/private/tmp/mediadb-275.tsv`. | `data/normalized_yaml/bacterial/bm_in_galactose_hodgson_et_al.yaml` or the MediaDB importer if it added default application labels. |

## Recommended Edits

1. Correct the maintained MediaDB provenance for medium 275 so the first import
   event and any source metadata point to Hodgson et al. 1982 rather than
   Mazumdar et al. 2014.
2. Remove or replace the unsupported generic `DISSOLVE`, `ADJUST_PH`, and
   `FILTER_STERILIZE` preparation steps in the normalized owner. Preserve only
   procedure text supported by MediaDB 275, Hodgson et al. 1982, or another
   inspected primary source.
3. Curate the four MediaDB growth rows for `Streptomyces coelicolor` J802,
   J845, J846, and J847 on medium 275 as source-scoped growth evidence, or add
   a quality flag explaining why MediaDB growth-data rows are intentionally out
   of scope for this importer.
4. Drop, narrow, or explicitly justify the generic `applications` labels if
   they remain MediaDB-wide import defaults rather than medium-specific
   assertions.
5. Regenerate `data/merge_yaml/merged/bm_in_galactose_hodgson_et_al.yaml`
   after the normalized owner is curated.
6. Do not patch `data/merge_yaml/merged/bm_in_galactose_hodgson_et_al.yaml`
   directly; it is a derived record.

## Follow-up Checks

- Run the focused schema, strict, term, and reference validators on
  `data/normalized_yaml/bacterial/bm_in_galactose_hodgson_et_al.yaml`.
- Run the same validators on
  `data/merge_yaml/merged/bm_in_galactose_hodgson_et_al.yaml` after merge
  regeneration.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating
  merge outputs.
- Re-fetch MediaDB medium 275, `/defined_media/media_text/275/`, source 90,
  and growth rows 568, 575, 582, and 589, then manually verify the regenerated
  record's ingredient, source-provenance, and growth-evidence claims against
  those inspected pages.

## Additional Notes

- This review intentionally wrote only this Markdown report. The generated
  merge record and normalized owner YAML were left unchanged.
