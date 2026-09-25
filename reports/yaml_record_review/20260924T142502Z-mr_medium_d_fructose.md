# YAML Record Review: mr_medium_d_fructose

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mr_medium_d_fructose.yaml
- Started UTC: 2026-09-24T14:24:06Z
- Finished UTC: 2026-09-24T14:25:02Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/mr_medium_d_fructose.yaml`.

- Class: `MediaRecipe`
- ID: `CultureMech:007220`
- Label: `mr_medium_d_fructose`
- Original label: `MR Medium + D-fructose`
- Category: `bacterial`
- Media source: MediaDB Medium `320`
- Generated status: generated merge output from one normalized source on fingerprint `9965f82221dd53cdbeb29bd2f04b2c32385428d5f348f9249a2b82098d04c031`
- Maintained owner: `data/normalized_yaml/bacterial/mr_medium_d_fructose.yaml`

The generated record matches its maintained normalized owner except for generated merge metadata.

## Validation

Validation was run on the generated merged YAML.

- Open LinkML schema validation:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mr_medium_d_fructose.yaml`
  - Result: passed with `No issues found`.
- Strict validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/mr_medium_d_fructose.yaml --out /private/tmp/mr_medium_d_fructose.strict.tsv --workers 1 --quiet`
  - Result: passed; exited 0 after its startup line and wrote a TSV with only its header row.
- Reference validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/mr_medium_d_fructose.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Result: passed; 0 reference checks were evaluated.
- Term validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/mr_medium_d_fructose.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Result: passed after the known `eutils` / `pkg_resources` warning.
- Embedded merge history:
  - Result: not checked. The repository history validator targets standalone `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

The record correctly denotes MediaDB Medium `320`, `Mr medium + d-fructose`.

An exact gitignore-independent search of `data/normalized_yaml` and `data/merge_yaml/merged` for `CultureMech:007220`, `MEDIADB:320`, bounded `Medium ID: 320`, the slug, and exact MediaDB URL fragments for medium `320` found only `data/normalized_yaml/bacterial/mr_medium_d_fructose.yaml` and this generated output. Ignored files were included.

The MediaDB medium page links Medium 320 to source `140`, Park JM et al. 2011, and to growth-data records 649, 650, and 651 for `Cupriavidus necator H16 on Mr medium + d-fructose`.

## Evidence

The MediaDB tab-delimited export for medium 320 lists the same 12 compounds and millimolar amounts that the record imports:

| Compound | MediaDB amount | CultureMech amount | Status |
| --- | ---: | ---: | --- |
| `D-Fructose` | 111.0 mM | 111.0 mM | supported |
| `Citrate` | 4.164 mM | 4.164 mM | supported |
| `Calcium chloride anhydrous` | 0.09011 mM | 0.09011 mM | supported |
| `Potassium dihydrogen phosphate` | 49.01 mM | 49.01 mM | supported |
| `Magnesium sulfate` | 4.587 mM | 4.587 mM | supported |
| `Manganese sulfate` | 0.01121 mM | 0.01121 mM | supported |
| `Ferrous sulfate` | 0.1798 mM | 0.1798 mM | supported |
| `Zinc sulfate` | 0.03825 mM | 0.03825 mM | supported |
| `Cupric sulfate` | 0.02002 mM | 0.02002 mM | supported |
| `Sodium borate` | 0.0002622 mM | 0.0002622 mM | supported |
| `Molybdic acid ammonium salt tetrahydrate` | 0.0004045 mM | 0.0004045 mM | supported |
| `Ammonium phosphate` | 30.29 mM | 30.29 mM | supported |

Unsupported or mismatched:

- MediaDB source `140` is Park JM et al. 2011, PMID 21711532; the `mediadb-import` history instead says `Reference: Mazumdar et al. (2014) PLOS One`.
- MediaDB exposes the medium composition, source, organism, and pH/temperature growth records, but it does not state the generic dissolve, pH-adjustment, or 0.22 um filtration steps in this record.
- The MediaDB export maps `Magnesium sulfate` to `CHEBI:31795`, while CultureMech maps that row to generic `CHEBI:32599`.
- The `Manganese sulfate` row is mapped to manganese(II) sulfate monohydrate even though MediaDB exported no CHEBI for that compound and the source label does not say `monohydrate`.

## Completeness

The record lacks exact MediaDB provenance:

- Medium page: `/defined_media/media/320/`
- Tab-delimited formula: `/defined_media/media_text/320/`
- Source page: `/defined_media/sources/140/`
- Growth data pages: `/defined_media/growthdata/649/`, `/defined_media/growthdata/650/`, `/defined_media/growthdata/651/`

The compound list itself is complete for the MediaDB 320 formula.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The import history cites the wrong paper. | MediaDB Medium 320 links to source 140, Park JM et al. 2011, PMID 21711532; the record says `Mazumdar et al. (2014) PLOS One`. | `data/normalized_yaml/bacterial/mr_medium_d_fructose.yaml` |
| Major | Generic preparation steps are unsupported by the inspected source. | MediaDB 320 provides no instruction to dissolve all ingredients, adjust pH if specified, or filter-sterilize at 0.22 um. | `data/normalized_yaml/bacterial/mr_medium_d_fructose.yaml`; MediaDB import defaults |
| Minor | Exact MediaDB medium, source, and growth-data provenance is lost. | The record keeps only a generic MediaDB home URL even though Medium 320 links to source 140 and growth records 649, 650, and 651. | `data/normalized_yaml/bacterial/mr_medium_d_fructose.yaml` |
| Minor | MediaDB and CultureMech disagree on selected ontology mappings. | MediaDB exports `CHEBI:31795` for `Magnesium sulfate`, but CultureMech stores `CHEBI:32599`; `Manganese sulfate` is over-specified to a monohydrate term without a MediaDB CHEBI. | `data/normalized_yaml/bacterial/mr_medium_d_fructose.yaml` |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/mr_medium_d_fructose.yaml`, replace the `Mazumdar et al. (2014) PLOS One` import-history text with MediaDB source 140, Park JM et al. 2011, PMID 21711532.
2. Remove the three generic preparation steps unless a primary source is inspected and shown to support them.
3. Add exact MediaDB provenance for medium 320, media-text 320, source 140, and growth-data records 649, 650, and 651.
4. Reconcile ingredient groundings against the MediaDB CHEBI export, especially magnesium sulfate and manganese sulfate.
5. Regenerate `data/merge_yaml/merged/mr_medium_d_fructose.yaml` from the maintained normalized record.

## Follow-up Checks

- Re-run open schema validation on the regenerated merged YAML.
- Re-run `scripts/validate_strict.py` and verify that the TSV remains header-only.
- Re-run `linkml-reference-validator` and `linkml-term-validator` to confirm any new MediaDB URLs and corrected CHEBI mappings resolve.
- Re-fetch MediaDB medium 320, `media_text/320`, source 140, and growth records 649, 650, and 651 to verify source and growth provenance.
- Repeat the exact ignored-inclusive search for `MEDIADB:320` and the MediaDB medium/source/growth URLs to verify no duplicate MediaDB 320 recipe was introduced.

## Additional Notes

- Fetching `/defined_media/growthdata/320/` is not a valid lookup for Medium 320. MediaDB growth-data record 320 is an unrelated `Escherichia coli MC4100 on Nmm with glucose` page; the correct growth-data records for this medium are 649, 650, and 651.
- `Sodium borate`, `Molybdic acid ammonium salt tetrahydrate`, `Calcium chloride anhydrous`, `Cupric sulfate`, `Ferrous sulfate`, `Citrate`, `Potassium dihydrogen phosphate`, and `Ammonium phosphate` lack `mediaingredientmech_chebi_term` mirrors.
