# YAML Record Review: Ignicoccus Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ignicoccus_medium__66dc867c.yaml
- Started UTC: 2026-09-23T14:27:01Z
- Finished UTC: 2026-09-23T14:27:54Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| ID | CultureMech:009181 |
| Name | ignicoccus_medium |
| Original name | Ignicoccus Medium |
| Class | MediaRecipe |
| Category | archaea |
| Medium type | COMPLEX |
| Composition type | UNDEFINED |
| Physical state | LIQUID |
| pH | Not represented |
| Source identity | TOGO Medium M2614, derived from DSMZ Medium 897 |
| Generated path reviewed | data/merge_yaml/merged/ignicoccus_medium__66dc867c.yaml |
| Maintained owner | data/normalized_yaml/archaea/TOGO_M2614_Ignicoccus_Medium.yaml |

The reviewed file is generated from the maintained TOGO M2614 import above.
Future fixes should update that normalized record, the TOGO import rules that
own row units and solution migration, and duplicate-resolution inputs before
regenerating `data/merge_yaml/merged/`.

## Validation

| Check | Result |
|---|---|
| Open LinkML validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ignicoccus_medium__66dc867c.yaml` | Passed; no issues found. |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/ignicoccus_medium__66dc867c.yaml --out /private/tmp/ignicoccus_medium__66dc867c.strict.tsv --workers 1 --quiet` | Passed; zero ERROR rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/ignicoccus_medium__66dc867c.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with zero reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/ignicoccus_medium__66dc867c.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` entry point validates standalone YAML under `history/`, not embedded MediaRecipe history arrays. |

The focused validators used Python 3.11 and the offline uv cache because the
project-level uv environment currently fails before validation while trying to
build `llvmlite==0.46.0` with Python 3.13.

## Identity and Grounding

- The stable ID and `TOGO:M2614` media term uniquely identify the TOGO
  Ignicoccus Medium record derived from DSMZ Medium 897.
- A gitignore-independent exact search for `CultureMech:009181` over this
  maintained YAML, this generated YAML, the ID registry, TOGO and archaea
  indexes, and the media content-review manifest found this TOGO import and
  its generated index or manifest entries.
- A gitignore-independent exact search for `TOGO:M2614` over maintained
  archaeal records, generated merged records, and normalized indexes found only
  this TOGO M2614 import.
- The recipe identity is the DSMZ 897 base Ignicoccus formulation and overlaps
  the MediaDive DSMZ 897 and KOMODO 897 records, so duplicate resolution should
  preserve one base record plus the DSM 18386 no-meat-extract variant.

## Evidence

- The TOGO payload and DSMZ 897 agree on the round source amounts for the main
  salts, sulfur, meat extract, and Na2S x 9 H2O, and those rows are present.
- The DSMZ and TOGO pH range, 5.0-5.5 with 2 N H2SO4, appears only in the
  preparation text; no `ph_range` or `ph_value` was imported.
- The TOGO payload carries `H3BO3` as 15 mg; the YAML records `15 G_PER_L`.
- DSMZ and TOGO carry 0.5 ml sodium resazurin at 0.1% w/v; the YAML records it
  as 0.5 g/L.
- DSMZ lists SrCl2 x 6 H2O, while TOGO M2614 has `SrCl3 x 6 H2O solution`.
  The generated YAML moved that typo into an empty `Unknown solution` with no
  composition and `7 G_PER_L` instead of the source 7 ml stock addition.
- The 0.5 ml KI solution at 0.01% w/v was also migrated into an empty `Unknown
  solution` with `0.5 G_PER_L`.
- Distilled water is represented as 1000 g/L instead of the source 1000 ml row.
- H2SO4, N2, CO2, and H2 appear as variable-concentration ingredients even
  though the DSMZ source scopes them to pH adjustment, anoxic sparging, sterile
  stock preparation, and post-inoculation pressurization.

## Completeness

- The base DSMZ 897 recipe needs the same duplicate reconciliation as the
  MediaDive and KOMODO 897 records.
- The pH range and DSMZ 18386 no-meat-extract variant are missing.
- The Sr/KI/resazurin stock additions need quantities, units, and formulas
  restored from DSMZ rather than kept as empty solution placeholders.
- Preparation gases and H2SO4 should be scoped to preparation, not to the final
  ingredient list.
- Empty optional fields for target organisms, synonyms, direct publication
  references, and quality flags are acceptable for this provider import once
  the explicit DSMZ variant is represented elsewhere.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Source `mg` and `ml` rows were imported as `G_PER_L`. | `H3BO3` is 15 mg in TOGO/DSMZ but 15 g/L in YAML; 0.5 ml of 0.1% sodium resazurin became 0.5 g/L; 1000 ml water became 1000 g/L. | `data/normalized_yaml/archaea/TOGO_M2614_Ignicoccus_Medium.yaml`; TOGO unit import. |
| Major | Sr and KI stocks were migrated to empty, wrongly quantified solutions. | DSMZ lists 7 ml SrCl2 x 6 H2O stock and 0.5 ml KI stock; the YAML has empty `Unknown solution` records with `G_PER_L` quantities. | `data/normalized_yaml/archaea/TOGO_M2614_Ignicoccus_Medium.yaml`; `solution-migrator-v1.0`. |
| Major | TOGO's `SrCl3 x 6 H2O` typo is unresolved against DSMZ. | The authoritative DSMZ 897 PDF says `SrCl2 x 6 H2O`; TOGO M2614 and the YAML say `SrCl3 x 6 H2O solution`. | TOGO import cleanup for `data/normalized_yaml/archaea/TOGO_M2614_Ignicoccus_Medium.yaml`. |
| Major | Preparation-only acid and gases are final-medium ingredients. | H2SO4, N2, CO2, and H2 occur in DSMZ preparation instructions, but the YAML records them as variable-concentration ingredient rows. | `data/normalized_yaml/archaea/TOGO_M2614_Ignicoccus_Medium.yaml`; TOGO comment parsing. |
| Major | The DSMZ pH range is missing. | DSMZ and TOGO state pH 5.0-5.5 in the H2SO4 adjustment instruction, and the YAML has neither `ph_range` nor `ph_value`. | `data/normalized_yaml/archaea/TOGO_M2614_Ignicoccus_Medium.yaml`; TOGO pH extraction. |
| Major | The DSMZ 897 base formula is duplicated across providers. | This TOGO M2614 record overlaps the MediaDive DSMZ 897 and KOMODO 897 Ignicoccus Medium records. | Duplicate-resolution inputs for TOGO, MediaDive, and KOMODO imports. |

## Recommended Edits

1. Correct H3BO3, sodium resazurin, and distilled-water units from the original
   TOGO/DSMZ row units.
2. Replace the empty Sr and KI `Unknown solution` records with source-faithful
   stock additions, correcting TOGO's SrCl3 typo to DSMZ `SrCl2 x 6 H2O`.
3. Move 2 N H2SO4, N2, CO2, and H2 out of final ingredients and retain them
   only in preparation or atmosphere fields.
4. Restore `ph_range: 5.0-5.5` from the pH-adjustment instruction.
5. Reconcile this base record with the MediaDive and KOMODO DSMZ 897 copies
   and keep the DSM 18386 no-meat-extract variant as a separate linked
   formulation.
6. Regenerate `data/merge_yaml/merged/` from the corrected normalized records.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation for the regenerated
  TOGO M2614 merged record.
- Manually compare the regenerated record against TOGO M2614 and the DSMZ 897
  PDF, paying particular attention to `mg`, `ml`, and variable gas rows.
- Verify that the generated base Ignicoccus recipe is merged or linked with
  the MediaDive and KOMODO DSMZ 897 imports.

## Additional Notes

- The TOGO source points to the same DSMZ 897 PDF as MediaDive, so DSMZ should
  be used to resolve the SrCl3/SrCl2 conflict and the missing DSM 18386
  variant note.
