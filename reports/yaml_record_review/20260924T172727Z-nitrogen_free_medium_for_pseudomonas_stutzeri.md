# YAML Record Review: NITROGEN-FREE MEDIUM FOR PSEUDOMONAS STUTZERI
- Repository: CultureMech
- Record: data/merge_yaml/merged/nitrogen_free_medium_for_pseudomonas_stutzeri.yaml
- Started UTC: 2026-09-24T17:25:46Z
- Finished UTC: 2026-09-24T17:27:27Z
- Verdict: pass with minor issues

## Target
Reviewed `CultureMech:005466`, `nitrogen_free_medium_for_pseudomonas_stutzeri`, generated from `data/normalized_yaml/bacterial/KOMODO_460_NITROGEN-FREE_medium_FOR_PSEUDOMONAS_STUTZERI.yaml` and merged with the direct MediaDive/DSMZ owner plus `medium_460_modified_for_dsm_4166`.

The merged record represents DSMZ/MediaDive medium 460, "NITROGEN-FREE MEDIUM FOR PSEUDOMONAS STUTZERI".

## Validation
- Open LinkML validation passed with `No issues found`.
- Strict validation passed; the strict TSV had only the header row.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` was not checked: the available `just validate-history` target validates standalone files under `history/`, not inline `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding
The merge is properly grounded. The active generated record merged the KOMODO 460 owner, KOMODO 460_4166 owner, and direct MediaDive 460 owner into one recipe. Both KOMODO owners state DSMZ Medium 460 / `mediadive.medium:460` provenance, and the direct MediaDive owner carries the DSMZ Medium 460 title.

An exact hidden/no-ignore search of `data/normalized_yaml` and `data/merge_yaml` for the KOMODO and MediaDive source IDs, DSMZ 460 labels, and normalized owner names found only the expected three normalized owners and this one active generated YAML.

## Evidence
MediaDive REST medium 460 and the DSMZ Medium 460 PDF list K2HPO4 0.5 g/L, MgSO4 x 7 H2O 0.2 g/L, NaCl 0.1 g/L, yeast extract 0.2 g/L, FeCl3 x 6 H2O 15 mg/L, DL-Na-malate 6.6 g/L, and 1000 ml distilled water, adjusted to pH 7.0.

The generated YAML preserves all six non-water solutes and their concentrations. Ferric chloride hexahydrate is correctly normalized from 15 mg/L to 0.015 G_PER_L.

The pH value is preserved as `ph_value: 7.0`. The only dropped direct-source detail is the explicit MediaDive preparation step `Adjust pH to 7.0`, which is chemically redundant with `ph_value` but should be restored for source completeness.

## Completeness
The medium is complete enough for use: formula, pH, physical state, source-duplicate merge, and source provenance all match DSMZ/MediaDive 460. Distilled water is omitted from the importer output, which is consistent with other MediaDive-derived records.

## Findings
- The explicit DSMZ/MediaDive preparation instruction to adjust pH to 7.0 is absent from the generated merged record even though it exists on the direct MediaDive normalized owner.

## Recommended Edits
- Teach merge generation to preserve equivalent `preparation_steps` from the direct MediaDive owner when a KOMODO-derived owner wins the canonical merge.
- Regenerate the merged record so the pH-adjustment step is restored alongside `ph_value: 7.0`.

## Follow-up Checks
- Re-run open, strict, reference, and term validation after regenerating the merged artifact.
- Re-check that the regenerated formula still merges only the three DSMZ 460-backed normalized owners found here.

## Additional Notes
None.
