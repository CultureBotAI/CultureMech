# YAML Record Review: lb_broth_miller

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/lb_broth_miller.yaml
- Started UTC: 2026-09-23T18:45:49Z
- Finished UTC: 2026-09-23T18:47:13Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:009027` for `lb_broth_miller` in `data/merge_yaml/merged/lb_broth_miller.yaml`.

- Primary source identity: TogoMedium `TOGO:M2448`, `LB Broth, Miller`, sourced from ATCC Medium 1065.
- Merged sources: `TOGO_M2199_LB_Agar_Broth_Miller`, `lb_agar_miller`, and `lb_broth_miller`.
- Generated lineage: `merge_fingerprint: 458b8df63152ec78dc712ec4dab5e7f947d80209d5ac468f990874d0aa380b79`.
- Maintained owners for fixes: `data/normalized_yaml/bacterial/TOGO_M2199_LB_Agar_Broth_Miller.yaml`, `data/normalized_yaml/bacterial/lb_agar_miller.yaml`, and `data/normalized_yaml/bacterial/lb_broth_miller.yaml`.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation, target class `MediaRecipe`, against `src/culturemech/schema/culturemech.yaml` | Passed with "No issues found". |
| `scripts/validate_strict.py data/merge_yaml/merged/lb_broth_miller.yaml --workers 1 --quiet` | Passed with 0 error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/lb_broth_miller.yaml` | Passed with 0 reference checks. |
| `linkml-term-validator validate-data data/merge_yaml/merged/lb_broth_miller.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the repository exposes `just validate-history` for standalone files under `history/`, not for embedded `MediaRecipe.curation_history` blocks inside one generated YAML file. |

## Identity and Grounding

The primary TOGO identity is correct: TogoMedium `M2448` is the ATCC Medium 1065 `LB Broth, Miller` commercial-powder recipe with 25 g `LB Broth (BD 244620)` in 1000 ml DI water and autoclaving at 121 C. TogoMedium `M2199` is a broader `LB Agar/Broth, Miller` view from the same ATCC PDF, and TogoMedium `M2446` is the commercial `LB Agar, Miller` view with 40 g `LB Agar (BD 244520)` in 1000 ml DI water.

Those identities are related, but the generated merge over-collapses them. It uses the broth record as canonical, adds the agar record as a synonym, and duplicates the scratch tryptone/yeast-extract/sodium-chloride rows from the unrepaired `TOGO_M2199_LB_Agar_Broth_Miller` owner. It also maps the result to `mediadive.medium:74`, which is DSMZ `THERMUS THERMOPHILUS MEDIUM`, not ATCC LB Miller.

## Evidence

ATCC Medium 1065 separates 40 g/L commercial LB Agar powder from 25 g/L commercial LB Broth powder and separately gives a scratch LB Miller formula of 10 g tryptone, 5 g yeast extract, 10 g sodium chloride, and 15 g agar, with agar omitted for broth. TogoMedium M2448 captures the 25 g/L broth-powder path, M2446 captures the 40 g/L agar-powder path, and M2199 captures the broth-powder path plus the scratch broth expansion.

The generated YAML does not preserve those boundaries:

- DI water is stored as `1000 G_PER_L` instead of 1000 ml or 1 L.
- The canonical M2448 25 g/L `LB Broth (BD 244620)` row is absent.
- Tryptone, yeast extract, and sodium chloride each appear twice because the manual product-constituent expansion and the Togo scratch expansion were merged as separate ingredients.
- The generated record has no preparation step for ATCC autoclaving at 121 C.
- The generated record has no ATCC or TOGO `references`, so source URLs remain only in `notes`.

## Completeness

The record is not complete enough because it is not a clean broth recipe, a clean agar recipe, or a clean scratch formulation. A curator should decide whether commercial `LB Broth, Miller`, commercial `LB Agar, Miller`, and scratch `LB Agar/Broth, Miller` are variants of one record or separate parent/variant records, then encode the powder rows and scratch constituents without duplicating them.

No consequential source was found for incubation temperature, atmosphere, storage, or strain-specific growth. The ATCC source only supplies formulation and autoclave conditions for this medium family.

An ignored-inclusive, hidden-file-inclusive search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:009027`, `TOGO:M2448`, `TOGO:M2199`, `TOGO:M2446`, `mediadive.medium:74`, all three source slugs, and the merge fingerprint found the three maintained normalized owners, this generated merge, many stale medium-74 fallback matches, and archived validation rows for the M2199 owner. The same bounded search found the repaired `TOGO_M2447_LB_Agar_Miller.yaml` source for a sibling ATCC LB Miller import; it was not part of this generated target.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The merged ingredient list contains duplicate scratch constituents and omits the canonical commercial broth powder row. | ATCC and TogoMedium M2448 list 25 g/L `LB Broth (BD 244620)` plus DI water for this source; the generated YAML has duplicate tryptone, yeast extract, and sodium chloride rows instead. | Repair `data/normalized_yaml/bacterial/TOGO_M2199_LB_Agar_Broth_Miller.yaml`, `data/normalized_yaml/bacterial/lb_agar_miller.yaml`, and `data/normalized_yaml/bacterial/lb_broth_miller.yaml`, then regenerate the merge. |
| Major | DI water has the wrong unit. | All three inspected TOGO views list DI water as 1000 ml; every normalized owner currently stores `DI Water` as `1000 G_PER_L`. | All three normalized owners in this merge. |
| Major | Agar and broth formulations have been over-collapsed. | TogoMedium M2446 is a 40 g/L commercial agar-powder recipe, M2448 is a 25 g/L commercial broth-powder recipe, and M2199 is a combined agar/broth source; the generated liquid broth record carries `lb_agar_miller` as a synonym and loses the explicit agar/broth boundary. | All three normalized owners in this merge plus the merge grouping rule if it continues to collapse these source IDs. |
| Major | `kg_microbe_match: mediadive.medium:74` points to the wrong medium. | MediaDive medium 74 is DSMZ `THERMUS THERMOPHILUS MEDIUM`, a 4 g/L yeast extract, 8 g/L proteose peptone, and 2 g/L NaCl recipe. | Remove or recompute the stale match in all normalized owners that carry it before regeneration. |
| Minor | Material source URLs are present only in free text. | The generated record cites TOGO and ATCC only in `notes`, has no `references`, and therefore ran 0 reference-validator checks. | Add `references` to all three normalized owners. |

No blocker findings were found.

## Recommended Edits

1. Re-curate `TOGO_M2199_LB_Agar_Broth_Miller.yaml`, `lb_agar_miller.yaml`, and `lb_broth_miller.yaml` against ATCC Medium 1065 and their specific TOGO API payloads.
2. Restore the source commercial powder rows for M2446 and M2448, or explicitly model their relationship to the scratch LB Miller formulation without duplicating tryptone, yeast extract, and sodium chloride.
3. Change DI water from `1000 G_PER_L` to a volume-preserving 1000 ml or 1 L amount in all three owners.
4. Add the ATCC autoclave step and source references.
5. Remove or recompute the false `kg_microbe_match: mediadive.medium:74`.
6. Revisit the merge grouping so agar and broth views remain distinguishable after regeneration.

## Follow-up Checks

- Re-run strict, schema, term, and reference validation on the three normalized owners.
- Re-run the merge pipeline and verify that the generated `CultureMech:009027` record has no duplicate tryptone, yeast extract, or sodium chloride rows and no DSMZ medium 74 match.
- Re-run strict, schema, term, and reference validation on the regenerated `data/merge_yaml/merged/lb_broth_miller.yaml`.
- Manually compare the regenerated records against ATCC Medium 1065 and TogoMedium M2446, M2448, and M2199 to confirm that commercial agar powder, commercial broth powder, and scratch LB Miller formulae are not flattened into one unsupported mixture.

## Additional Notes

The ignored-inclusive search found many `mediadive.medium:74` fallback-style rows elsewhere in the corpus; this report only reviewed the one in `lb_broth_miller.yaml`.

This review did not create or mutate GitHub issues, pull requests, comments, labels, settings, source YAML, generated YAML, or rendered pages.
