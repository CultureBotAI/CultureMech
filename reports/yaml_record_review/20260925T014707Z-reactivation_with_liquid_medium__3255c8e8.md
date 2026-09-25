# YAML Record Review: reactivation_with_liquid_medium__3255c8e8

- Repository: CultureMech
- Record: `data/merge_yaml/merged/reactivation_with_liquid_medium__3255c8e8.yaml`
- Started UTC: 2026-09-25T01:46:56Z
- Finished UTC: 2026-09-25T01:47:07Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:001667` for DSMZ Medium 535b / `mediadive.medium:535b`, generated from `data/normalized_yaml/bacterial/reactivation_with_liquid_medium.yaml`.

## Validation

- Open schema validation: passed; `linkml-validate` exited 0 with no diagnostics.
- Strict validation: passed; `scripts/validate_strict.py` reported 0 errors and wrote only the TSV header.
- Reference validation: passed; 0 checks.
- Term validation: passed with the known `eutils` / `pkg_resources` deprecation warning.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

MediaDive 535b and the DSMZ `DSMZ_Medium535b.pdf` source both describe "535b. REACTIVATION WITH LIQUID MEDIUM". Exact ignored-inclusive source searches found `mediadive.medium:535b` in this direct DSMZ owner, its generated target, the source indexes, the manifest row, and a KOMODO 535b owner note. Exact ignored-inclusive DSMZ-PDF searches also found `TOGO:M2357` / `data/normalized_yaml/bacterial/TOGO_M2357_Reactivation_With_Liquid_Medium.yaml`, which imports the same `DSMZ_Medium535b.pdf` as a separate owner and generated target.

## Evidence

The primary DSMZ source says to rehydrate lyophilized cells in 5 ml liquid broth 545 and then subculture in liquid medium 545 or on agar plates. MediaDive 535b models the same reactivation instruction as a wrapper with alternatives to DSMZ 535 / Trypticase Soya Agar and DSMZ 545 / Tryptone Soya Broth.

The DSMZ source lists the 545 broth ingredients as peptone from casein 17 g/L, peptone from soymeal 3 g/L, D(+)-glucose 2.5 g/L, NaCl 5 g/L, K2HPO4 2.5 g/L, optional agar 15 g/L if agar is required, distilled water 1000 ml, and pH 7.3. MediaDive also carries the DSMZ 535 agar alternative as a commercial Trypticase Soy Broth 30 g/L plus agar 20 g/L recipe.

## Completeness

The record carries DSMZ 535b, the imported pH, and the MediaDive reactivation instruction, but its ingredient set is not a faithful representation of either DSMZ alternative because direct MediaDive solution rows and later product-level TSB/TSA enrichment rows are both present.

## Findings

- The generated target has a duplicated, over-expanded ingredient list. Lines 30-78 keep MediaDive's expanded DSMZ 545 ingredients, while lines 79-193 add a second researched commercial TSB/TSA decomposition for the same casein, soy, glucose, sodium chloride, dipotassium phosphate, and agar recipe. The researched rows were sourced from the Tryptic Soy Broth / Tryptic Soy Agar product enrichment block in `notes`, but DSMZ 535b already supplied the relevant constituent amounts through MediaDive.
- The first `Agar` row is mathematically wrong: line 73 reports 35.0 g/L with `Merged 2 duplicates: 15.0, 20.0`. The source has 15 g/L agar for DSMZ 545 only if required and 20 g/L agar for the separate DSMZ 535 agar alternative; those amounts are not duplicate observations for one formulation and should not be summed.
- The generated record has no source-duplicate relationship to `TOGO:M2357`, even though `data/normalized_yaml/bacterial/TOGO_M2357_Reactivation_With_Liquid_Medium.yaml` cites the same `DSMZ_Medium535b.pdf`. Those records remain emitted as separate generated targets.

## Recommended Edits

- Fix `data/normalized_yaml/bacterial/reactivation_with_liquid_medium.yaml` so DSMZ 535b is either represented as the reactivation protocol that chooses a liquid 545 or agar 535 subculture medium, or split/linked to the existing DSMZ 535 and 545 recipes rather than flattening both alternatives into one ingredient list.
- Remove the commercial TSB/TSA researched constituent rows from this DSMZ owner or make the enrichment logic skip product decomposition when MediaDive already provides the DSMZ 545 constituents.
- Prevent duplicate cleanup from summing alternative agar amounts; the 15 g/L and 20 g/L agar rows come from different DSMZ alternatives.
- Merge or source-link the `TOGO:M2357` owner with the corrected DSMZ 535b owner and regenerate `data/merge_yaml/merged`.

## Follow-up Checks

- Regenerate merged YAML and verify this target no longer contains duplicate casein/soy/glucose/NaCl/K2HPO4/agar rows or a 35 g/L agar sum.
- Verify the DSMZ 535b record and the TOGO M2357 record converge to one generated target or carry an explicit duplicate-source relationship.
- Re-run open schema, strict, reference, and term validation for the regenerated target.

## Additional Notes

The normalized owner and generated target are identical for the inspected fields, so the correction belongs in normalized YAML and/or the merge and product-enrichment logic, not in `data/merge_yaml/merged` by hand.
