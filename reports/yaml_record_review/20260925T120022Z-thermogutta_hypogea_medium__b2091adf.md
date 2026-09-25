# YAML Record Review: thermogutta_hypogea_medium__b2091adf

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermogutta_hypogea_medium__b2091adf.yaml
- Started UTC: 2026-09-25T12:00:22Z
- Finished UTC: 2026-09-25T12:00:22Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:002215`, `thermogutta_hypogea_medium`, generated from JCM Medium J1031 / MediaDive `mediadive.medium:J1031`.

## Validation

- LinkML schema: Passed with `linkml-validate`; no issues found.
- Strict validation: Passed with 0 ERROR rows; `/private/tmp/thermogutta_hypogea_medium__b2091adf.strict.tsv` contained only the header.
- Reference validation: Passed; the validator ran 0 checks for this record.
- Term validation: Passed.
- Embedded curation history: Not checked; the available history validator covers standalone `history/` records, not embedded `MediaRecipe.curation_history`.

## Identity and Grounding

The generated record is grounded to the correct source medium, JCM J1031, "THERMOGUTTA HYPOGEA MEDIUM". The JCM page for J1031 links its Trace elements solution to Medium No. 1030 and its Trace vitamins to Medium No. 197; the MediaDive J1031 payload expands both stocks.

## Evidence

- JCM J1031: the main mixture contains NH4Cl, KCl, MgCl2 x 6 H2O, KH2PO4, CaCl2 x 2 H2O, 10 ml Trace elements solution from J1030, and 1 L distilled water.
- JCM J1031: while gassing with N2, 10 ml Trace vitamins from J197 and 2 g NaHCO3 are added, then the pH is checked at 7.6-8.0 and adjusted if needed before autoclaving under N2.
- JCM J1031: 20 ml 10% w/v glucose solution, 10 ml 1% yeast extract solution, and 10 ml 1 M KNO3 solution are aseptically and anaerobically added after autoclaving.

## Completeness

The record keeps the main salts and expands the J1030 trace-elements stock and J197 trace-vitamin stock, but it lists those stock ingredients at full stock concentration as if they were direct medium ingredients. It also omits the distilled-water row and does not structure the 10 ml, 20 ml, and 1 M stock additions that the source uses for vitamins, glucose, yeast extract, and KNO3.

## Findings

- The J1030 Trace elements solution and J197 Trace vitamins rows are both 100-fold too high if read as final medium concentrations because J1031 adds 10 ml of each stock per liter-scale recipe.
- `Glucose` 20 G_PER_L copies the 20 ml addition of a 10% w/v glucose stock rather than the stock or final mass concentration.
- `Yeast extract` 10 G_PER_L copies the 10 ml addition of a 1% yeast extract stock rather than the stock or final mass concentration.
- `KNO3` 10 G_PER_L copies the 10 ml addition volume and loses the source concentration of 1 M KNO3.
- The source pH check and possible readjustment to 7.6-8.0 is only prose in a preparation step and is not structured as a pH range.

## Recommended Edits

- Keep the J1030 trace-elements recipe and J197 trace-vitamin recipe under stock solution structure, then represent their 10 ml/L additions to J1031.
- Convert the glucose, yeast extract, and KNO3 rows into post-autoclave stock additions with source concentrations of 10% w/v, 1%, and 1 M respectively.
- Add the 1 L distilled-water row.
- Preserve the N2 boil/cool/autoclave handling and pH 7.6-8.0 check in structured preparation steps.
- Replace the stale `mediaingredientmech_term` links on KNO3, Na2SeO4, and KI with CHEBI-keyed links while editing this record.

## Follow-up Checks

- Verify whether final G_PER_L values should be derived over the source's 1060 ml total volume or whether the record should stay stock-volume based.
- Confirm that J1030 trace-elements stock sharing is preserved if the stock is deduplicated for reuse by other JCM records.

## Additional Notes

No target-organism evidence was reviewed. The exact local source search included ignored and hidden files and found only the expected J1031 normalized recipe for this record; linked JCM pages J1031, J1030, and J197 were fetched directly.
