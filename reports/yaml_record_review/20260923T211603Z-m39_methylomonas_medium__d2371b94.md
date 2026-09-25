# YAML Record Review: M39 METHYLOMONAS MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/m39_methylomonas_medium__d2371b94.yaml`
- Started UTC: 2026-09-23T21:14:44Z
- Finished UTC: 2026-09-23T21:16:03Z
- Verdict: needs curation

## Target

- Generated record: `data/merge_yaml/merged/m39_methylomonas_medium__d2371b94.yaml`
- Maintained owner: `data/normalized_yaml/bacterial/m39_methylomonas_medium.yaml`
- CultureMech ID: `CultureMech:002344`
- Media term: `mediadive.medium:J1171`
- Merge fingerprint: `d2371b943ea50b9c7081b196404af8878c848a457e3aa87a85298dbdf79cca2b`
- Merge sources: `m39_methylomonas_medium`
- Ignored-inclusive exact searches over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` found the direct MediaDive/JCM J1171 owner, the TOGO M1253 and M1254 siblings, generated M39 outputs, generated indexes, and archived validation rows that referenced the owner's former filename.

## Validation

- Open LinkML validation against `MediaRecipe`: passed.
- Strict validation with `scripts/validate_strict.py`: passed with 0 error rows in `/private/tmp/m39_methylomonas_medium__d2371b94.strict.tsv`.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded `curation_history` entries were not checked as standalone history records.

## Identity and Grounding

The record represents the direct MediaDive serialization of JCM Medium 1171, `M39 METHYLOMONAS MEDIUM`. It should be the liquid JCM M39 recipe, distinct from the TOGO M1254 solid-agar split reviewed under `m39_methylomonas_medium__2bafae14.yaml`.

Chemical grounding is mostly correct. The NaNO3 row still uses legacy `mediaingredientmech_term: MediaIngredientMech:000171` despite having a primary `CHEBI:63005` term.

## Evidence

- JCM 1171 supports the base of 0.099 g MgSO4 x 7H2O, 0.147 g CaCl2 x 2H2O, 0.349 g K2SO4, 0.17 g NaNO3, and 1 L distilled water.
- JCM 1171 says to autoclave the base and, after cooling to 60 C, add 1 ml 1.0 M KH2PO4 solution, 1 ml filter-sterilized selenite-tungstate solution, 1 ml filter-sterilized trace element solution, 0.1 ml filter-sterilized vitamins solution, 0.1 ml filter-sterilized 0.2 M CeCl3 solution, and 3 ml filter-sterilized 1.0 M NaHCO3 solution.
- JCM 1171 defines trace-element and vitamins stocks in the same page; the trace stock includes 1 L SL-6 trace element solution, and the vitamins stock is a separate 1 L stock.
- MediaDive `J1171` expands those nested stocks, but it also serializes `Main sol. J1171` with volume 3006 ml, showing that stock solvent volumes were incorrectly folded into the final-medium volume.
- MediaDive `J1171` separately preserves the Selenite-tungstate and SL-6 stock definitions as stock solutions.

## Completeness

The generated record is complete for many names after MediaDive expansion, but it is not complete enough to make the source recipe. It has no main distilled-water ingredient, no structured final additions for KH2PO4/CeCl3/NaHCO3, no selenite-tungstate or SL-6 stock boundaries, no vitamins stock boundary, no methane gas component, and no 0.2 N H2SO4 addition.

The source 1 L SL-6 and 1 L vitamin stock solvents must not be counted as 2 L of extra final M39 medium. MediaDive's 3006 ml normalization should be treated as an import artifact.

## Findings

1. **Blocker - stock solvent volumes were counted as final-medium volume.** JCM 1171 starts with 1 L base water and then adds only 1 ml trace-element stock and 0.1 ml vitamins stock, but MediaDive `J1171` normalized the formula to 3006 ml by including the 1 L SL-6 and 1 L vitamin stock waters. The YAML inherits concentrations such as `0.0329341 G_PER_L` MgSO4 x 7H2O from that false 3006 ml denominator.

2. **Blocker - trace, vitamin, selenite-tungstate, and SL-6 stock ingredients are flattened into the final medium.** The YAML stores stock rows such as Na2-EDTA, FeCl2 x 4 H2O, vitamins, Na2SeO3 x 5 H2O, Na2WO4 x 2 H2O, and SL-6 metal salts as final ingredients instead of keeping them in their source stock solutions with 1 ml or 0.1 ml additions to the base.

3. **Major - base water and several post-autoclave solution additions are missing or mis-modeled.** The JCM 1171 1 L distilled water row is absent, the 1 ml KH2PO4, 0.1 ml CeCl3, and 3 ml NaHCO3 additions are stored as grams per liter, and the source methane and H2SO4 rows are missing from the ingredient or solution lists.

4. **Major - preparation-step scope is wrong.** `Adjust pH to 3.6` is the SL-6 trace-element stock step, not a final M39 step, while the final pH 6.5-7.0 adjustment with 0.2 N H2SO4, 10% methane cultivation atmosphere, and at least 80% gas phase are flattened into a partially escaped prose step.

5. **Minor - one MediaIngredientMech link was not migrated to CHEBI keying.** The NaNO3 row has `CHEBI:63005` as its primary term but still carries `mediaingredientmech_term: MediaIngredientMech:000171`.

## Recommended Edits

- In `data/normalized_yaml/bacterial/m39_methylomonas_medium.yaml`, discard MediaDive's 3006 ml denominator and remodel JCM 1171 from the JCM table: 1 L base water plus the specified milliliter post-autoclave additions.
- Move the vitamins, trace-element, selenite-tungstate, and SL-6 rows into source-backed stock solutions with their own stock solvents and preparation steps.
- Restore the source 1 L distilled-water base, the 1 ml KH2PO4 stock, 0.1 ml CeCl3 stock, 3 ml NaHCO3 stock, 0.2 N H2SO4 pH adjustment, and 10% methane atmosphere.
- Scope the SL-6 `Adjust pH to 3.6` step to the SL-6 stock rather than the final M39 medium.
- Replace the NaNO3 legacy MediaIngredientMech link with a CHEBI-keyed link.
- Add structured references for MediaDive J1171 and JCM 1171.
- Regenerate merged YAML and rerun open schema, strict, reference, and term validation.

## Follow-up Checks

- Reinspect JCM 1171 and MediaDive J1171 after curation to confirm the regenerated record no longer uses the 3006 ml MediaDive volume artifact.
- Re-run an ignored-inclusive exact search for `CultureMech:002344`, `mediadive.medium:J1171`, and `d2371b943ea50b9c7081b196404af8878c848a457e3aa87a85298dbdf79cca2b` after regeneration to verify the direct MediaDive/JCM record remains separate from the TOGO M1253 and M1254 siblings.
- Rerun open schema, strict, term, and reference validation on the regenerated `m39_methylomonas_medium__d2371b94.yaml`.

## Additional Notes

The direct MediaDive import has `physical_state: LIQUID`; that is acceptable for the non-agarose JCM 1171 recipe. The solid agarose variant is tracked separately by TOGO M1254.
