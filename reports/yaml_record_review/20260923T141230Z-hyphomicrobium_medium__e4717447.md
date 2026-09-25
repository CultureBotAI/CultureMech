# YAML Record Review: Hyphomicrobium Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/hyphomicrobium_medium__e4717447.yaml
- Started UTC: 2026-09-23T14:11:05Z
- Finished UTC: 2026-09-23T14:12:30Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| ID | CultureMech:004187 |
| Name | hyphomicrobium_medium |
| Original name | HYPHOMICROBIUM medium |
| Class | MediaRecipe |
| Category | bacterial |
| Medium type | COMPLEX |
| Composition type | SEMI_DEFINED |
| Physical state | LIQUID |
| pH | 7.2 |
| Source identity | KOMODO Medium 162, resolved to DSMZ Medium 162 |
| Generated path reviewed | data/merge_yaml/merged/hyphomicrobium_medium__e4717447.yaml |
| Maintained owner | data/normalized_yaml/bacterial/KOMODO_162_HYPHOMICROBIUM_medium.yaml |

The reviewed file is generated from the maintained KOMODO 162 record above,
which was enriched from DSMZ Medium 162. Future fixes should update the
normalized KOMODO record or duplicate-resolution inputs and regenerate
`data/merge_yaml/merged/`.

## Validation

| Check | Result |
|---|---|
| Open LinkML validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/hyphomicrobium_medium__e4717447.yaml` | Passed; no issues found. |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/hyphomicrobium_medium__e4717447.yaml --out /private/tmp/hyphomicrobium_medium__e4717447.strict.tsv --workers 1 --quiet` | Passed; zero ERROR rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/hyphomicrobium_medium__e4717447.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with zero reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/hyphomicrobium_medium__e4717447.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` entry point validates standalone YAML under `history/`, not embedded MediaRecipe history arrays. |

The focused validators used Python 3.11 and the offline uv cache because the
project-level uv environment currently fails before validation while trying to
build `llvmlite==0.46.0` with Python 3.13.

## Identity and Grounding

- The record identity is coherent for a KOMODO provider copy: `CultureMech:004187`
  is KOMODO Medium 162, and its metadata links that KOMODO entry to DSMZ
  Medium 162.
- A gitignore-independent exact search for `CultureMech:004187` over the
  maintained KOMODO file, generated KOMODO file, ID registry, bacterial index,
  and review manifest found only this KOMODO 162 record.
- A gitignore-independent exact search for `KOMODO_162_HYPHOMICROBIUM_medium`
  over normalized records, generated records, the ID registry, and the review
  manifest found only this maintained KOMODO 162 record and its generated
  merged copy.
- The ten DSMZ 162 formula compounds match the inspected DSMZ PDF and the
  MediaDive DSMZ 162 parse.
- Yeast extract remains an explicit unresolved complex ingredient, which is
  acceptable for this medium.

## Evidence

- KH2PO4, Na2HPO4, ammonium sulfate, MgSO4 x 7H2O, CaCl2 x 2H2O, FeSO4 x
  7H2O, MnSO4 x H2O, Na2MoO4 x 2H2O, methylamine hydrochloride, and yeast
  extract match DSMZ 162.
- DSMZ and MediaDive list 1000 ml distilled water; no water row appears in the
  YAML.
- DSMZ instructs curators to adjust pH to 7.4 with NaOH, autoclave for 20 min
  at 121 C, and use final pH 7.2. The KOMODO record has pH 7.2 and imports NaOH
  as a variable-concentration ingredient, but it has no preparation step.
- The same DSMZ 162 formula is represented in the MediaDive-owned
  `DSMZ_162_HYPHOMICROBIUM_MEDIUM.yaml` record under a different stable ID.
- The first `curation_history` timestamp is `2026-01-27T01:15:02.fZ`, which is
  not a valid ISO timestamp.

## Completeness

- The recipe needs its 1000 ml distilled-water row restored.
- The pH-adjustment and autoclave procedure should be represented as
  preparation, not as a synthetic NaOH ingredient.
- The KOMODO and MediaDive DSMZ 162 copies need duplicate resolution.
- Empty optional fields for target organisms, synonyms, variants, direct
  publication references, discussions, and quality flags are acceptable for
  this provider import.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The source water volume is omitted. | DSMZ 162 lists 1000 ml distilled water, and the KOMODO YAML has no water ingredient. | `data/normalized_yaml/bacterial/KOMODO_162_HYPHOMICROBIUM_medium.yaml`; DSMZ resolver / KOMODO import. |
| Major | NaOH was imported as a final-medium ingredient and the real preparation is missing. | NaOH appears only in DSMZ's pH-adjustment instruction; the YAML has a variable NaOH ingredient and no autoclave/pH preparation step. | `data/normalized_yaml/bacterial/KOMODO_162_HYPHOMICROBIUM_medium.yaml`; pH-buffer migration. |
| Major | DSMZ 162 exists as unresolved parallel MediaDive and KOMODO imports. | `DSMZ_162_HYPHOMICROBIUM_MEDIUM.yaml` and `KOMODO_162_HYPHOMICROBIUM_medium.yaml` represent the same DSMZ formula with different stable IDs. | Normalized duplicate-resolution inputs for the MediaDive and KOMODO records. |
| Minor | The initial KOMODO import history timestamp is malformed. | `curation_history[0].timestamp` is `2026-01-27T01:15:02.fZ`. | `data/normalized_yaml/bacterial/KOMODO_162_HYPHOMICROBIUM_medium.yaml`; history cleanup. |

## Recommended Edits

1. Restore the 1000 ml distilled-water row.
2. Move NaOH out of final ingredients and encode the DSMZ pH-adjustment plus
   20 min, 121 C autoclave instruction as preparation.
3. Reconcile this KOMODO record with the MediaDive DSMZ 162 import.
4. Repair the malformed KOMODO import timestamp.
5. Regenerate `data/merge_yaml/merged/` from the corrected normalized record.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation for the regenerated
  KOMODO 162 merged record.
- Manually compare the regenerated KOMODO copy against the DSMZ 162 PDF.
- Verify the KOMODO and MediaDive DSMZ 162 records are merged or explicitly
  linked.

## Additional Notes

- The visible DSMZ-derived chemical concentrations are already correct; the
  defects are water omission, pH-buffer leakage into ingredients, missing
  preparation, and duplicate provider identity.
