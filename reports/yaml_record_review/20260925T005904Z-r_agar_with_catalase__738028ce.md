# YAML Record Review: R AGAR WITH CATALASE

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/r_agar_with_catalase__738028ce.yaml
- Started UTC: 2026-09-25T00:57:26Z
- Finished UTC: 2026-09-25T00:59:04Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Path | `data/merge_yaml/merged/r_agar_with_catalase__738028ce.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:002351` |
| Label | `R AGAR WITH CATALASE` |
| Category | `bacterial` |
| Source identity | `mediadive.medium:J117` |
| Generated status | Generated singleton with `merge_fingerprint: 738028ce8099e07f86f5615aae17c4edc8d3a780848bbb4d957dbc2370026fe2`; owned upstream by `data/normalized_yaml/bacterial/r_agar_with_catalase.yaml`. |

## Validation

| Check | Result |
| --- | --- |
| Open LinkML schema | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/r_agar_with_catalase__738028ce.yaml` exited 0 with no diagnostics. |
| Strict validator | Passed; `scripts/validate_strict.py data/merge_yaml/merged/r_agar_with_catalase__738028ce.yaml --out /private/tmp/r_agar_with_catalase_738028ce.strict.tsv --workers 1 --quiet` reported 0 files with errors and the strict TSV had only its header row. |
| Reference validator | Passed trivially; `linkml-reference-validator validate data data/merge_yaml/merged/r_agar_with_catalase__738028ce.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` validated 1 file, ran 0 checks, and reported all validations passed. |
| Term validator | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/r_agar_with_catalase__738028ce.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0 and reported validation passed. |
| Embedded curation history | Not checked: `just validate-history` validates the standalone `history/` tree, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

## Identity and Grounding

- The ID, label, category, and `mediadive.medium:J117` CURIE identify the direct MediaDive mirror of JCM Medium 117, `R AGAR WITH CATALASE`.
- The live JCM GRMD 117 endpoint now returns `Nothing found`, but the live MediaDive J117 mirror still resolves to source `JCM` and the same GRMD 117 URL.
- TOGO M109 records `original_media_id: JCM_M117` and the same GRMD 117 source URL, so it is source-equivalent evidence for the retired JCM page.
- Live MediaDive J117 and TOGO M109 both support R Agar at 1000 ml/L plus 60 mg/L catalase and separate filter sterilization of the catalase.
- The catalase concentration is correct in the reviewed generated copy, but the R Agar base is encoded as a 1000 g/L ingredient and is wrongly mapped to `CHEBI:2509` `agar`.

## Evidence

- Supported:
  - MediaDive J117 supports the `mediadive.medium:J117` identity, the `R AGAR WITH CATALASE` label, the JCM source, the complex solid-agar medium type, 60 mg/L catalase, and the filtration note.
  - TOGO M109 independently supports the same original JCM 117 source identity and the same catalase and R Agar amounts.
- Unsupported or over-scoped:
  - `R agar` is a referenced base medium, not a chemical ingredient at 1000 g/L.
  - The `R agar` row should not carry `mediaingredientmech_chebi_term: CHEBI:2509`, because the source row points to a complete R Agar recipe, not to agar alone.
  - The generated record omits the explicit `solutions` representation that the maintained owner now uses for 1000 ml/L R Agar.
  - The generated JCM artifact omits the TOGO M109 and M19 repair evidence that currently backs the retired JCM 117 page.

## Completeness

- The maintained direct owner has a September 2026 `RESOLVED_JCM_117_863_SCORE20` repair, `ph_value: 7.2`, `solutions`, three preparation steps, `parent_media`, `variant_relationship`, `variant_modifications`, `data_quality_flags`, and references; none of that appears in the generated August copy.
- The exact gitignore-independent search over `data/normalized_yaml`, `data/merge_yaml`, and `reports` for `mediadive.medium:J117`, `TOGO:M109`, `GRMD=117`, `CultureMech:002351`, and `r_agar_with_catalase` found the direct JCM owner, the TOGO M109 owner, their two stale generated outputs, reciprocal R Agar parent links, indexes, and historical validation rows.
- Empty optional target-organism fields are not defects for this record.

## Findings

| Severity | Finding | Evidence | Owner |
| --- | --- | --- | --- |
| Major | The generated direct JCM artifact models a base recipe as an agar chemical ingredient. | MediaDive J117 and TOGO M109 both represent R Agar as a 1000 ml/L base medium; the reviewed generated record uses `R agar` at `1000 G_PER_L` and attaches `CHEBI:2509` for agar. | Regenerate `data/merge_yaml/merged/r_agar_with_catalase__738028ce.yaml` from `data/normalized_yaml/bacterial/r_agar_with_catalase.yaml`. |
| Major | The generated record is stale relative to its maintained owner. | The generated record ends with an August 2026 `MERGED_RECIPES` event; the normalized owner carries a September 2026 repair with corrected solutions, preparation steps, parent-media links, quality flags, and references. | `data/normalized_yaml/bacterial/r_agar_with_catalase.yaml` already owns the corrected direct-JCM content; the merge layer must be rerun. |
| Major | The source-equivalent TOGO M109 and direct MediaDive J117 generated records remain split. | MediaDive J117 points to JCM GRMD 117, and TOGO M109 records `original_media_id: JCM_M117` with the same JCM GRMD 117 URL. The exact search found separate generated files at `r_agar_with_catalase__738028ce.yaml` and `R_AGAR_WITH_CATALASE.yaml`. | Add or repair source-equivalence handling between `data/normalized_yaml/bacterial/r_agar_with_catalase.yaml` and `data/normalized_yaml/bacterial/TOGO_M109_R_Agar_With_Catalase.yaml`, then regenerate. |

## Recommended Edits

1. Regenerate the direct JCM generated artifact from `data/normalized_yaml/bacterial/r_agar_with_catalase.yaml` so `R agar` is a 1000 ml/L solution linked to `CultureMech:002627`, not a 1000 g/L `CHEBI:2509` ingredient.
2. Preserve the 0.06 g/L catalase amount, the catalase filtration step, the 7.2 pH inherited from the R Agar base, and the variant relationship already present in the maintained owner.
3. Reconcile the TOGO M109 and MediaDive J117 generated outputs so the same original JCM 117 recipe is not emitted under two separate generated identities.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validators against the regenerated `data/merge_yaml/merged/r_agar_with_catalase__738028ce.yaml`.
- Re-run a gitignore-independent exact search for `TOGO:M109`, `mediadive.medium:J117`, and `GRMD=117` to confirm the source-equivalent records are auditable after regeneration.
- Re-fetch MediaDive J117 and TOGO M109 to confirm the 60 mg/L catalase amount and filtration instruction. The live JCM GRMD 117 endpoint can be checked, but it currently returns `Nothing found`.

## Additional Notes

- The reviewed generated artifact still has the right catalase value after converting 60 mg/L to 0.06 g/L. Its main defect is the old solution-migration representation for the R Agar base.
- The TOGO M109 generated artifact is also stale: it still encodes catalase as `60 G_PER_L` and the R Agar reference as `1 G_PER_L`.
