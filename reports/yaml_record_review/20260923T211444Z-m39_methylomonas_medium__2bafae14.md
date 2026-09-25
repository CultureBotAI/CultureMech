# YAML Record Review: M39 Methylomonas Medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/m39_methylomonas_medium__2bafae14.yaml`
- Started UTC: 2026-09-23T21:13:03Z
- Finished UTC: 2026-09-23T21:14:44Z
- Verdict: needs curation

## Target

- Generated record: `data/merge_yaml/merged/m39_methylomonas_medium__2bafae14.yaml`
- Maintained owner: `data/normalized_yaml/bacterial/TOGO_M1254_M39_Methylomonas_Medium.yaml`
- CultureMech ID: `CultureMech:007785`
- Media term: `TOGO:M1254`
- Merge fingerprint: `2bafae145c91370fd902dbb61b1fa1eac0b63ef4f78ba814df77040900dcb87f`
- Merge sources: `TOGO_M1254_M39_Methylomonas_Medium`
- Ignored-inclusive exact searches over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` found the maintained TOGO M1254 owner, sibling TOGO M1253 and M431 stock owners, the generated M39 outputs, generated indexes, and archived validation rows.

## Validation

- Open LinkML validation against `MediaRecipe`: passed.
- Strict validation with `scripts/validate_strict.py`: passed with 0 error rows in `/private/tmp/m39_methylomonas_medium__2bafae14.strict.tsv`.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded `curation_history` entries were not checked as standalone history records.

## Identity and Grounding

The record represents TOGO Medium `M1254`, the solid JCM 1171 `M39 Methylomonas Medium` split that includes 15 g/L agarose. The base identity is correct and distinct from the non-agarose TOGO `M1253` sibling, which supplies the trace-element and vitamins stocks referenced by M1254.

The methane ingredient is grounded in the maintained owner but not in the generated merge because `apply_mim_groundings.py` ran after generation. H2SO4, water, sodium nitrate, potassium sulfate, and agarose have appropriate groundings.

## Evidence

- JCM 1171 and TOGO M1254 list the base as 0.099 g MgSO4 x 7H2O, 0.147 g CaCl2 x 2H2O, 0.349 g K2SO4, 0.17 g NaNO3, and 1 L distilled water, with 15.0 g/L agarose for solid medium.
- JCM 1171 says to autoclave the base and, after cooling to 60 C, add 1 ml 1.0 M KH2PO4 solution, 1 ml filter-sterilized selenite-tungstate solution from Medium 431, 1 ml filter-sterilized trace element solution from M1253, 0.1 ml filter-sterilized vitamins solution from M1253, 0.1 ml filter-sterilized 0.2 M CeCl3 solution, and 3 ml filter-sterilized 1.0 M NaHCO3 solution.
- TOGO M1253 defines the trace-element and vitamin stocks used by M1254, and TOGO M431 defines the selenite-tungstate stock.
- JCM 1171 says to adjust pH to 6.5-7.0 with 0.2 N H2SO4 and cultivate in air containing 10% v/v methane in gas-tight flasks or jars with at least 80% gas phase by volume.

## Completeness

The base ingredient rows are present, but distilled water is quantitatively wrong and every post-autoclave solution addition is flattened into an empty placeholder. The maintained owner and generated record also omit structured preparation steps, pH 6.5-7.0, 60 C cooling, the filter-sterilization boundary for starred additions, and structured references.

The ignored-inclusive exact search did not find a later repaired M1254 owner; it found only the current maintained TOGO M1254 YAML and generated products.

## Findings

1. **Blocker - all post-autoclave solution additions are stored as gram-per-liter placeholders.** JCM 1171 adds six stock solutions in milliliter amounts after autoclaving and cooling: 3 ml NaHCO3, 1 ml KH2PO4, 0.1 ml CeCl3, 1 ml selenite-tungstate, 1 ml trace elements, and 0.1 ml vitamins. The YAML stores those six additions as empty `Unknown solution` objects at `G_PER_L` values.

2. **Major - the trace, vitamin, and selenite-tungstate stock compositions are unresolved.** M1254 references TOGO M1253 and M431 for those stocks. The YAML keeps only prose cross-references, so the M1253 trace-element/vitamin recipes and the M431 selenite-tungstate recipe are not represented.

3. **Major - the base water is off by a 1000-fold liter conversion.** JCM 1171 and TOGO M1254 list 1 L distilled water; the YAML stores `Distilled water` as `1 G_PER_L` instead of a liter-scale amount.

4. **Major - preparation and atmosphere semantics are missing.** The source pH range, autoclaving, 60 C cooling point, filter-sterilized starred additions, 0.2 N H2SO4 pH adjustment, 10% methane atmosphere, and at least 80% gas-phase instruction are absent or defaulted to `VARIABLE`.

5. **Minor - the generated record is stale relative to maintained methane grounding.** `data/normalized_yaml/bacterial/TOGO_M1254_M39_Methylomonas_Medium.yaml` now has a `CHEBI:16183` methane term, but the generated merge predates that August 2026 grounding.

## Recommended Edits

- In `data/normalized_yaml/bacterial/TOGO_M1254_M39_Methylomonas_Medium.yaml`, convert the six post-autoclave additions to `ML_PER_L` solution additions and preserve which starred additions are filter-sterilized.
- Expand or structurally link the M1253 trace-element and vitamin stocks and the M431 selenite-tungstate stock instead of leaving them as empty cross-reference placeholders.
- Correct the base distilled-water amount from `1 G_PER_L` to the source 1 L volume.
- Add preparation steps for autoclaving, cooling to 60 C, adding stock solutions, adjusting pH to 6.5-7.0 with 0.2 N H2SO4, and cultivating with 10% v/v methane in air.
- Add structured references for TOGO M1254, JCM 1171, TOGO M1253, and TOGO M431.
- Regenerate merged YAML and rerun open schema, strict, reference, and term validation.

## Follow-up Checks

- Reinspect JCM 1171, TOGO M1254, TOGO M1253, and TOGO M431 after curation to confirm all base, stock, pH, methane, and sterilization details are preserved with the right units.
- Re-run an ignored-inclusive exact search for `CultureMech:007785`, `TOGO:M1254`, `TOGO:M1253`, `TOGO:M431`, and `2bafae145c91370fd902dbb61b1fa1eac0b63ef4f78ba814df77040900dcb87f` after regeneration to confirm the generated M39 record reflects the maintained owner.
- Rerun open schema, strict, term, and reference validation on the regenerated `m39_methylomonas_medium__2bafae14.yaml`.

## Additional Notes

The source uses a greater-than-or-equal gas-phase symbol in prose; this ASCII report describes it as "at least 80%" to avoid carrying that symbol into the report artifact.
