# YAML Record Review: Inorganic Salts-Starch Agar (ISP-4)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/inorganic_salts_starch_agar_isp_4.yaml
- Started UTC: 2026-09-23T15:06:20Z
- Finished UTC: 2026-09-23T15:09:44Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| ID | CultureMech:009900 |
| Name | inorganic_salts_starch_agar_isp_4 |
| Original name | Inorganic Salts-Starch Agar (ISP-4) |
| Class | MediaRecipe |
| Category | bacterial |
| Medium type | COMPLEX |
| Composition type | UNDEFINED |
| Physical state | SOLID_AGAR |
| pH | Not represented |
| Source identity | TOGO Medium M50, derived from JCM Medium 58 |
| Generated path reviewed | data/merge_yaml/merged/inorganic_salts_starch_agar_isp_4.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M50_Inorganic_Salts-Starch_Agar_ISP-4.yaml |

The reviewed file is generated from the maintained TOGO/JCM owner above. Future
fixes should regenerate `data/merge_yaml/merged/` from that already repaired
normalized record.

## Validation

| Check | Result |
|---|---|
| Open LinkML validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/inorganic_salts_starch_agar_isp_4.yaml` | Passed; no issues found. |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/inorganic_salts_starch_agar_isp_4.yaml --out /private/tmp/inorganic_salts_starch_agar_isp_4.strict.tsv --workers 1 --quiet` | Passed; zero ERROR rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/inorganic_salts_starch_agar_isp_4.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; zero reference checks were applicable. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/inorganic_salts_starch_agar_isp_4.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` entry point validates standalone YAML under `history/`, not embedded MediaRecipe history arrays. |

The focused validators used Python 3.11 and the offline uv cache because the
project-level uv environment currently fails before validation while trying to
build `llvmlite==0.46.0` with Python 3.13.

## Identity and Grounding

- The stable ID, slug, `TOGO:M50` media term, and source URL identify TOGO's
  JCM Medium 58 import of Inorganic Salts-Starch Agar (ISP-4).
- A gitignore-independent exact search for `CultureMech:009900` over bacterial
  normalized records, normalized indexes, and merged records found the TOGO M50
  owner, this generated copy, index entries, and curated variant back-links to
  this parent.
- A gitignore-independent exact anchored search for `TOGO:M50` over bacterial
  normalized records, normalized indexes, and merged records found only this
  owner, this generated copy, and generated index entries.
- The broad slug family also includes 5%, 10%, and 15% NaCl salinity variants
  plus a 0.05% yeast-extract supplemented variant, all of which are now linked
  to the maintained TOGO M50 owner.

## Evidence

- JCM 58 and TOGO M50 list soluble starch, K2HPO4, MgSO4 x 7 H2O, NaCl,
  ammonium sulfate, CaCO3, 1 ml trace salts solution, 20 g agar, and 1 L
  distilled water.
- The trace-salt stock is prepared from 0.1 g each FeSO4 x 7 H2O, MnCl2 x 4
  H2O, and ZnSO4 x 7 H2O in 100 ml distilled water, then added at 1 ml/L.
- The generated record still has the three trace salts as top-level 0.1 g/L
  final ingredients and also keeps an empty `Unknown solution` for the 1 ml
  trace-salt addition.
- The generated record has distilled water summed to `101.0 G_PER_L` from the
  1 L final water row and the 100 ml trace-stock water row.
- The source pH range is 7.0 to 7.4, but the generated file has no `ph_range`.
- The maintained owner already corrected the trace-salt solution, restored
  distilled water to 1 L, added pH, autoclaving, references, data-quality
  flags, and salinity or yeast-extract variant children on Sep 6 through Sep
  13.

## Completeness

- The maintained normalized owner is now source-faithful for JCM Medium 58.
- The generated copy is stale and should not be used until the September
  normalized repairs are propagated.
- Empty optional fields for synonyms, direct publication references, organism
  targets, discussions, and quality flags are acceptable after the generated
  file is refreshed from the repaired owner.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated file is stale relative to the repaired TOGO owner. | The reviewed merged file was generated on Aug 6, while the owner was repaired on Sep 6, Sep 8, and Sep 13 with source-faithful ISP-4 rows, pH, sterilization, references, and variant links. | Regenerate from `data/normalized_yaml/bacterial/TOGO_M50_Inorganic_Salts-Starch_Agar_ISP-4.yaml`. |
| Major | Trace salts are both flattened and left as an empty solution. | JCM and TOGO add 1 ml/L trace-salt stock; the generated YAML has FeSO4 x 7 H2O, MnCl2 x 4 H2O, and ZnSO4 x 7 H2O as top-level ingredients plus an empty `Unknown solution`. | Already fixed in `data/normalized_yaml/bacterial/TOGO_M50_Inorganic_Salts-Starch_Agar_ISP-4.yaml`; regenerate. |
| Major | Distilled water was summed across the final medium and stock recipe. | JCM has 1 L final water and 100 ml stock water; the generated YAML records `101.0 G_PER_L` with a duplicate-merge note. | Already fixed in `data/normalized_yaml/bacterial/TOGO_M50_Inorganic_Salts-Starch_Agar_ISP-4.yaml`; regenerate. |
| Minor | The source pH range and curated child links are missing from the generated file. | JCM reports unadjusted pH 7.0-7.4, and the repaired owner links NaCl and yeast-extract variants; the generated file predates those repairs. | Already fixed in `data/normalized_yaml/bacterial/TOGO_M50_Inorganic_Salts-Starch_Agar_ISP-4.yaml`; regenerate. |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/inorganic_salts_starch_agar_isp_4.yaml`
   from `data/normalized_yaml/bacterial/TOGO_M50_Inorganic_Salts-Starch_Agar_ISP-4.yaml`.
2. Confirm the regenerated file keeps the trace salts under `solutions` at
   1 ml/L with 1 g/L stock composition rows.
3. Confirm the regenerated file keeps Distilled water at 1 L, includes
   `ph_range: 7.0-7.4`, and carries the autoclave step, references,
   data-quality flags, and variant children.

## Follow-up Checks

1. Rerun open LinkML, strict, reference, and term validation after regenerating
   the merged YAML.
2. Diff regenerated `data/merge_yaml/merged/inorganic_salts_starch_agar_isp_4.yaml`
   against the maintained owner to confirm the only difference is appended
   merge provenance.
3. Re-run variant-link validation so the NaCl and yeast-extract child links
   still point back to the refreshed parent.

## Additional Notes

- This record has no target-organism or literature evidence entries, so no
  organism-grounding, snippet, or DOI checks were applicable.
