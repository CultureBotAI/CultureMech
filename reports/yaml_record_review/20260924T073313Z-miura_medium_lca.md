# YAML Record Review: miura_medium_lca

- Repository: CultureMech
- Record: data/merge_yaml/merged/miura_medium_lca.yaml
- Started UTC: 2026-09-24T07:33:13Z
- Finished UTC: 2026-09-24T07:33:43Z
- Verdict: pass with minor issues

## Target

- Generated record: `CultureMech:009716`
- Generated name: `miura_medium_lca`
- Generated source file: `data/merge_yaml/merged/miura_medium_lca.yaml`
- Normalized owner: `data/normalized_yaml/bacterial/TOGO_M338_Miura_Medium_LCA.yaml`
- Upstream source: TOGO Medium `M338`, `Miura Medium (LCA)`

## Validation

- Open LinkML validation passed: `No issues found`.
- Strict validation passed with 0 ERROR rows in `/private/tmp/miura_medium_lca.strict.tsv`.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` was not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The generated record identity is aligned with TOGO `M338`.
- The `media_term` points to `TOGO:M338` with label `Miura Medium (LCA)`.
- The TOGO metadata preserves original media ID `JCM_M343` and the JCM detail URL for `GRMD=343`.
- Seven of eight source ingredients have primary CHEBI or agar grounding.
- `Yeast extract (BD-Difco)` remains ungrounded, which is acceptable for an undefined branded yeast-extract ingredient.

## Evidence

- TOGO `M338` lists eight components in `main solution 1`: 1 L distilled water, 0.2 g `MgSO4 x 7H2O`, 1 g `KH2PO4`, 0.2 g KCl, 2 g `NaNO3`, 1 g glucose, 15 g agar, and 0.2 g `Yeast extract (BD-Difco)`.
- The generated record preserves all eight components with matching amounts per liter.
- MediaDive/JCM medium `J343` is the same JCM formula mirrored by TOGO `M338`, but remains as a separate generated record, `miura_medium_lca__40e6b647.yaml`.
- TOGO `M338` carries the comment `pH unadjusted`.
- The old JCM `GRMD=343` URL returned an empty body during review, so the current formula was checked against TOGO rather than the JCM page.

## Completeness

- The formula and solid-agar state are complete against TOGO `M338`.
- The `pH unadjusted` source comment is missing from the generated record.
- The exact normalized owner lookup had to use the stable ID because `data/normalized_yaml/bacterial/miura_medium_lca.yaml` is occupied by the separate JCM `J343` import.

## Findings

- Low: The source comment `pH unadjusted` is not represented.
- Low: `Yeast extract (BD-Difco)` is intentionally undefined but ungrounded; a FoodOn or product-level term could improve searchability if a defensible branded-term mapping exists.
- Medium: TOGO `M338` and MediaDive/JCM `J343` describe the same JCM Miura Medium (LCA) formula but survive as two CultureMech records.

## Recommended Edits

- Add the `pH unadjusted` source comment to `preparation_notes` or an equivalent source-context field.
- Add a conservative yeast-extract or product-level grounding only if it does not erase the BD-Difco qualifier.
- De-duplicate TOGO `M338` and JCM `J343`, preserving both source cross-references on one curated record.

## Follow-up Checks

- Re-fetch TOGO `M338` and verify all eight component rows still match after any edit.
- Re-fetch MediaDive/JCM `J343` and confirm de-duplication retains its JCM source identity.
- Retry the JCM `GRMD=343` URL in case its empty response was transient.
- Re-run open LinkML, strict, reference, and term validation after regenerating the merged record.
- The normalized-owner lookup used `rg --no-ignore --hidden`; repeat ignored-file-inclusive checks for exact owner and duplicate source paths after the edit.

## Additional Notes

- None found.
