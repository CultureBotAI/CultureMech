# YAML Record Review: thermoflexus_hungenholtzii_medium__598b509d

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermoflexus_hungenholtzii_medium__598b509d.yaml
- Started UTC: 2026-09-25T12:00:21Z
- Finished UTC: 2026-09-25T12:00:21Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:003325`, `thermoflexus_hungenholtzii_medium`, generated from JCM Medium J976 / MediaDive `mediadive.medium:J976`.

## Validation

- LinkML schema: Passed with `linkml-validate`; no issues found.
- Strict validation: Passed with 0 ERROR rows; `/private/tmp/thermoflexus_hungenholtzii_medium__598b509d.strict.tsv` contained only the header.
- Reference validation: Passed; the validator ran 0 checks for this record.
- Term validation: Passed.
- Embedded curation history: Not checked; the available history validator covers standalone `history/` records, not embedded `MediaRecipe.curation_history`.

## Identity and Grounding

The recipe is grounded to the correct source medium, JCM J976, "THERMOFLEXUS HUNGENHOLTZII MEDIUM". JCM J976 defines a main salts mixture, adds 5 ml of a separate Mineral solution, and then adds 10 ml of trace vitamins from JCM J197 plus 10 ml of a 10% peptone solution per liter after autoclaving.

## Evidence

- JCM J976: NaCl, KCl, Na2SO4, MgSO4 x 7 H2O, CaCl2 x 2 H2O, NH4Cl, NaH2PO4, 5 ml Mineral solution, and 1 L distilled water are mixed, adjusted to pH 6.75 with NaOH, dispensed under N2, sealed, and autoclaved.
- JCM J976: after cooling, 10 ml trace vitamins and 10 ml 10% w/v peptone solution are added per liter, and filter-sterilized O2 gas or air is added before inoculation at 1% O2 in the gas phase.
- JCM J976: the Mineral solution is a 1 L stock that contains EDTA, FeSO4 x 7 H2O, MnCl2 x 4 H2O, ZnSO4 x 7 H2O, CoCl2 x 6 H2O, CuCl2 x 2 H2O, Na2MoO4 x 2 H2O, H3BO3, and water, and is adjusted to pH 6.0 with KOH.

## Completeness

The record preserves the main scalar salts and copies the Mineral solution and J197 trace vitamins ingredients, but it flattens both stocks into top-level ingredients at their 1 L stock strengths. The 1 L distilled-water row is absent, the 5 ml and 10 ml stock addition semantics are not represented, and the 10 ml 10% peptone addition is recorded as `Peptone` 10 G_PER_L rather than as a stock addition.

## Findings

- The Mineral solution rows are 200-fold too high if read as final medium concentrations because J976 adds 5 ml of that stock per liter.
- The J197 trace-vitamin rows are 100-fold too high if read as final medium concentrations because J976 adds 10 ml of that stock per liter.
- The source adds 10 ml of 10% w/v peptone solution; the generated `Peptone` 10 G_PER_L row appears to copy the 10 ml addition volume into a mass concentration.
- `ph_value: 6.0` is suspect: the direct JCM target page adjusts the main mixture to pH 6.75, while the pH 6.0 instruction belongs to the Mineral solution stock.
- The Mineral solution KOH adjustment and stopper-pretreatment comment are emitted as top-level preparation steps rather than as stock-scoped or comment-scoped instructions.

## Recommended Edits

- Model the Mineral solution as a separate stock and record its 5 ml/L addition to the main J976 formulation.
- Model J197 trace vitamins as a separate stock and record its 10 ml/L post-autoclave addition.
- Replace the 10 G_PER_L peptone row with a 10 ml/L addition of 10% w/v peptone solution, or derive a final concentration only after preserving that source stock.
- Add the distilled-water row and scope the Mineral solution pH adjustment to the Mineral solution.
- Revisit the recipe `ph_value` after deciding whether the record should carry MediaDive's parsed pH 6.0 or the main-solution pH 6.75 from the target JCM page.

## Follow-up Checks

- Verify the J197 trace-vitamin stock remains shared with other JCM records after refactoring, because the same stock appears in many generated imports.
- Check whether the schema has a native way to represent the 1% O2 gas phase before converting that instruction into structured fields.

## Additional Notes

No target-organism evidence was reviewed. The exact local source search included ignored and hidden files and found only the expected J976 normalized recipe for this record; linked JCM pages J976 and J197 were fetched directly.
