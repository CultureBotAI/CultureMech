# YAML Record Review: Inorganic Salts-Starch Agar (ISP-4) With 0.05% Yeast Extract

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/inorganic_salts_starch_agar_isp_4_with_0_05_yeast_extract.yaml
- Started UTC: 2026-09-23T15:10:00Z
- Finished UTC: 2026-09-23T15:13:54Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| ID | CultureMech:008702 |
| Name | inorganic_salts_starch_agar_isp_4_with_0_05_yeast_extract |
| Original name | Inorganic Salts-Starch Agar (ISP-4) With 0.05% Yeast Extract |
| Class | MediaRecipe |
| Category | bacterial |
| Medium type | COMPLEX |
| Composition type | UNDEFINED |
| Physical state | SOLID_AGAR |
| pH | Not represented |
| Source identity | TOGO Medium M210, derived from JCM Medium 217 |
| Generated path reviewed | data/merge_yaml/merged/inorganic_salts_starch_agar_isp_4_with_0_05_yeast_extract.yaml |
| Maintained owner | data/normalized_yaml/bacterial/inorganic_salts_starch_agar_isp_4_with_0_05_yeast_extract.yaml |

The reviewed file is generated from the maintained TOGO/JCM owner above. Future
fixes should regenerate `data/merge_yaml/merged/` from that already repaired
normalized record.

## Validation

| Check | Result |
|---|---|
| Open LinkML validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/inorganic_salts_starch_agar_isp_4_with_0_05_yeast_extract.yaml` | Passed; no issues found. |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/inorganic_salts_starch_agar_isp_4_with_0_05_yeast_extract.yaml --out /private/tmp/inorganic_salts_starch_agar_isp_4_with_0_05_yeast_extract.strict.tsv --workers 1 --quiet` | Passed; zero ERROR rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/inorganic_salts_starch_agar_isp_4_with_0_05_yeast_extract.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; zero reference checks were applicable. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/inorganic_salts_starch_agar_isp_4_with_0_05_yeast_extract.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` entry point validates standalone YAML under `history/`, not embedded MediaRecipe history arrays. |

The focused validators used Python 3.11 and the offline uv cache because the
project-level uv environment currently fails before validation while trying to
build `llvmlite==0.46.0` with Python 3.13.

## Identity and Grounding

- The stable ID, slug, `TOGO:M210` media term, and source URL identify TOGO's
  JCM Medium 217 import.
- A gitignore-independent exact search for `CultureMech:008702` over bacterial
  normalized records, normalized indexes, and merged records found this owner,
  this generated copy, index entries, and the repaired parent ISP-4 backlink.
- A gitignore-independent exact anchored search for `TOGO:M210` over bacterial
  normalized records, normalized indexes, and merged records found only this
  owner, this generated copy, and generated index entries.
- JCM Medium 217 and TOGO M210 agree that this is JCM Medium 58 ISP-4
  supplemented with 0.5 g yeast extract per liter.

## Evidence

- JCM 217 lists exactly 1 L Inorganic salts-starch agar (ISP-4), by reference
  to JCM Medium 58, plus 0.5 g yeast extract.
- The generated record only carries 0.5 g/L Yeast extract and an empty
  `Unknown solution` for the referenced M50 / JCM 58 parent medium.
- The Sep 6 maintained owner expands the full JCM 58 parent recipe, keeps the
  M50 trace-salt stock nested at 1 ml/L, restores 1 L distilled water and pH
  7.0-7.4, and records the extra 0.5 g/L yeast extract from JCM Medium 217.
- The maintained owner also now records `parent_media`, `variant_relationship`,
  and `variant_modifications` to mark this as a supplemented variant of the
  TOGO M50/JCM 58 ISP-4 parent.

## Completeness

- The maintained normalized owner is source-faithful for JCM Medium 217 and
  links it to its ISP-4 parent.
- The generated copy is stale and incomplete: it lacks the parent formula,
  trace-salt stock, water row, pH range, preparation metadata, references,
  parent-media relationship, and data-quality flags.
- Empty optional fields for synonyms, direct publication references, organism
  targets, discussions, and quality flags are acceptable after the generated
  file is refreshed from the repaired owner.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated file is stale relative to the repaired M210 owner. | The reviewed merged file was generated on Aug 6, while the maintained owner was rebuilt on Sep 6 with the full JCM 58 parent recipe plus JCM 217 yeast extract. | Regenerate from `data/normalized_yaml/bacterial/inorganic_salts_starch_agar_isp_4_with_0_05_yeast_extract.yaml`. |
| Major | The ISP-4 parent medium is represented only as an empty solution. | JCM 217 uses 1 L JCM Medium 58 ISP-4; the generated YAML has a 1 g/L `Unknown solution` for M50 and no parent ingredients. | Already fixed in the maintained owner; regenerate. |
| Major | Parent-medium solution structure and pH are missing. | The generated YAML lacks the M50 trace-salt stock, 1 L distilled water, autoclaving metadata, and pH 7.0-7.4 that were restored in the owner. | Already fixed in the maintained owner; regenerate. |
| Minor | The supplemented-variant relationship is missing. | The maintained owner links to TOGO M50 with `variant_relationship: SUPPLEMENTED_VARIANT`; the generated file predates that link. | Already fixed in the maintained owner; regenerate. |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/inorganic_salts_starch_agar_isp_4_with_0_05_yeast_extract.yaml`
   from its maintained owner.
2. Confirm the regenerated file contains the full ISP-4 base recipe, nested
   trace-salt solution, 0.5 g/L yeast extract, pH 7.0-7.4, and M50 parent link.
3. Confirm the generated output retains JCM 217 and JCM 58 references,
   data-quality flags, and the Sep 6 curation event.

## Follow-up Checks

1. Rerun open LinkML, strict, reference, and term validation after regenerating
   the merged YAML.
2. Diff regenerated `data/merge_yaml/merged/inorganic_salts_starch_agar_isp_4_with_0_05_yeast_extract.yaml`
   against the maintained owner to confirm the only expected difference is
   appended merge provenance.
3. Re-run variant-link validation so this supplemented variant still points to
   the refreshed TOGO M50 parent.

## Additional Notes

- This record has no target-organism or literature evidence entries, so no
  organism-grounding, snippet, or DOI checks were applicable.
