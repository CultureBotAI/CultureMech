# YAML Record Review: Hyphomicrobium Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/hyphomicrobium_medium__c8032f6a.yaml
- Started UTC: 2026-09-23T14:08:20Z
- Finished UTC: 2026-09-23T14:10:22Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| ID | CultureMech:001109 |
| Name | hyphomicrobium_medium |
| Original name | HYPHOMICROBIUM MEDIUM |
| Class | MediaRecipe |
| Category | bacterial |
| Medium type | COMPLEX |
| Composition type | SEMI_DEFINED |
| Physical state | LIQUID |
| pH | 7.2 |
| Source identity | MediaDive/DSMZ Medium 162, HYPHOMICROBIUM MEDIUM |
| Generated path reviewed | data/merge_yaml/merged/hyphomicrobium_medium__c8032f6a.yaml |
| Maintained owner | data/normalized_yaml/bacterial/DSMZ_162_HYPHOMICROBIUM_MEDIUM.yaml |

The reviewed file is generated from the maintained MediaDive/DSMZ import above.
Future fixes should update `data/normalized_yaml/bacterial/DSMZ_162_HYPHOMICROBIUM_MEDIUM.yaml`
or the MediaDive volume import, then regenerate `data/merge_yaml/merged/`.

## Validation

| Check | Result |
|---|---|
| Open LinkML validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/hyphomicrobium_medium__c8032f6a.yaml` | Passed; no issues found. |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/hyphomicrobium_medium__c8032f6a.yaml --out /private/tmp/hyphomicrobium_medium__c8032f6a.strict.tsv --workers 1 --quiet` | Passed; zero ERROR rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/hyphomicrobium_medium__c8032f6a.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with zero reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/hyphomicrobium_medium__c8032f6a.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` entry point validates standalone YAML under `history/`, not embedded MediaRecipe history arrays. |

The focused validators used Python 3.11 and the offline uv cache because the
project-level uv environment currently fails before validation while trying to
build `llvmlite==0.46.0` with Python 3.13.

## Identity and Grounding

- The record identity is coherent: `CultureMech:001109` is the MediaDive import
  of DSMZ Medium 162, and the inspected DSMZ PDF and MediaDive REST record both
  identify HYPHOMICROBIUM MEDIUM.
- A gitignore-independent exact search for `CultureMech:001109` over the
  maintained DSMZ 162 file, generated merged file, ID registry, MediaDive
  indexes, and review manifest found only this maintained DSMZ 162 record and
  its generated index rows.
- A gitignore-independent anchored search for primary
  `id: mediadive.medium:162` rows over bacterial normalized and generated
  records found only this MediaDive DSMZ 162 record.
- A gitignore-independent exact search for the text `DSMZ Medium: 162
  (mediadive.medium:162)` over bacterial normalized and generated records found
  a separate KOMODO 162 record for the same source, which should be reconciled
  later.
- All visible chemically defined ingredient rows are grounded exactly enough;
  yeast extract remains an explicit unresolved complex ingredient, which is
  acceptable for this medium.

## Evidence

- The generated KH2PO4, Na2HPO4, ammonium sulfate, MgSO4 x 7H2O, CaCl2 x
  2H2O, FeSO4 x 7H2O, MnSO4 x H2O, Na2MoO4 x 2H2O, methylamine hydrochloride,
  and yeast extract amounts match the DSMZ 162 PDF and the MediaDive 162 REST
  payload.
- MediaDive correctly converted the source milligram rows to gram-per-liter
  values: 6 mg CaCl2 x 2H2O to 0.006 g/L, 3 mg FeSO4 x 7H2O to 0.003 g/L,
  1 mg MnSO4 x H2O to 0.001 g/L, and 1.5 mg Na2MoO4 x 2H2O to 0.0015 g/L.
- The pH and autoclave text matches the DSMZ instruction to adjust to pH 7.4,
  autoclave 20 min at 121 C, and retain final pH 7.2.
- DSMZ and MediaDive list 1000 ml distilled water; no water row appears in the
  YAML.

## Completeness

- The recipe needs its 1000 ml distilled-water row restored.
- The chemical rows, pH, physical state, and preparation are complete enough for
  a MediaDive import.
- The KOMODO 162 duplicate should be reviewed separately and later reconciled.
- Empty optional fields for target organisms, synonyms, variants, direct
  publication references, discussions, and quality flags are acceptable for
  this provider import.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The source water volume is omitted. | DSMZ 162 lists 1000 ml distilled water, and MediaDive preserves it as a 1000 ml row; the YAML has no water ingredient. | `data/normalized_yaml/bacterial/DSMZ_162_HYPHOMICROBIUM_MEDIUM.yaml`; MediaDive volume import. |
| Major | DSMZ 162 exists as an unresolved parallel KOMODO import. | `KOMODO_162_HYPHOMICROBIUM_medium.yaml` and generated `hyphomicrobium_medium__e4717447.yaml` cite the same DSMZ Medium 162 source metadata. | Normalized duplicate-resolution inputs for the MediaDive and KOMODO records. |

## Recommended Edits

1. Restore the 1000 ml distilled-water row to the DSMZ 162 MediaDive record.
2. Reconcile this MediaDive 162 record with the KOMODO 162 import so the same
   DSMZ source is not represented as unrelated stable IDs.
3. Regenerate `data/merge_yaml/merged/` from the corrected normalized record.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation for the regenerated
  DSMZ 162 merged record.
- Manually verify all eleven DSMZ 162 rows, including distilled water, against
  the DSMZ PDF and MediaDive REST payload.
- Confirm the KOMODO 162 duplicate is merged or explicitly linked.

## Additional Notes

- Unlike the DSMZ 1355 and JCM 884 Hyphomicrobium media, DSMZ 162 has no nested
  trace-element stock and the generated ingredient amounts do not show
  stock-boundary or milligram-conversion defects.
