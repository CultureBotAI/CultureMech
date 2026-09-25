# YAML Record Review: methanococcoides_medium__1f16238c
- Repository: CultureMech
- Record: data/merge_yaml/merged/methanococcoides_medium__1f16238c.yaml
- Started UTC: 2026-09-24T03:29:49Z
- Finished UTC: 2026-09-24T03:32:14Z
- Verdict: needs curation

## Target
- ID: CultureMech:008485
- Name: methanococcoides_medium
- Label: Methanococcoides medium
- Category: archaea
- Source: TOGO:M1908, imported from NBRC_M1168
- Merge fingerprint: 1f16238cfff8aa6576d9b6e2f3661ff2d7225952110f8d04acf587f25af03154
- Merged from: TOGO_M1908_Methanococcoides_medium

## Validation
- Open schema validation: Passed; no issues found.
- Strict validation: Passed; 1 file scanned and the strict TSV contained only the header row.
- LinkML reference validation: Passed; 0 reference checks, all passed.
- Term validation: Passed.
- Embedded curation history: Not checked: the history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding
- The record represents the NBRC 1168 Methanococcoides medium via TOGO M1908, and the main medium identity is specific.
- The two solution references do not carry the NBRC stock identities. NBRC 1168 defines local `Vitamin solution*` and `Trace elements solution**` stocks, but the YAML stubs point to `mediadive.solution:6241` and `mediadive.solution:6129`, which are unrelated standalone MediaDive solution records with different compositions.
- Most base salts are chemically grounded to hydrate-specific CHEBI terms, including MgSO4 x 7 H2O, CaCl2 x 2 H2O, MgCl2 x 6 H2O, Na2S x 9 H2O, Na2MoO4 x 2 H2O, CuCl2 x 2 H2O, FeCl3 x 6 H2O, and KAl(SO4)2 x 12 H2O.
- CoCl2 x 6 H2O is grounded to generic cobalt dichloride, and NiCl2 x 6 H2O is grounded to generic nickel dichloride despite hydrate-specific source labels.

## Evidence
- NBRC 1168 lists a 1 L final formula with 10 ml each of `Vitamin solution*` and `Trace elements solution**`.
- The same NBRC formula puts Biotin, Folic acid, Pyridoxine-HCl, Thiamine-HCl, Riboflavin, Nicotinic acid, Ca-pantothenate, p-Aminobenzoic acid, Vitamin B12, and 1 L distilled water inside `Vitamin solution*`.
- The same NBRC formula puts nitrilotriacetic acid, FeCl3 x 6 H2O, MnCl2 x 4 H2O, CoCl2 x 6 H2O, CaCl2 x 2 H2O, ZnCl2, CuCl2 x 2 H2O, H3BO3, Na2MoO4 x 2 H2O, NaCl, NiCl2 x 6 H2O, Na2SeO4, Na2WO4, KAl(SO4)2 x 12 H2O, and 1 L distilled water inside `Trace elements solution**`.
- NBRC instructs curators to mix ingredients except vitamin solution, Cysteine-HCl, and Na2S x 9 H2O; autoclave under an 80/20 N2/CO2 atmosphere; separately autoclave 5% Cysteine-HCl and Na2S x 9 H2O solutions under N2; add the filter-sterile vitamin solution before inoculation; first dissolve NTA and adjust the trace-elements stock to pH 6.5 with NaOH before adding minerals; and target final pH 7.0.
- The generated record has no `preparation_steps` or preparation notes.
- The generated `solutions` array keeps `Vitamin solution*` and `Trace elements solution**` as empty `Unknown solution` stubs with `10 G_PER_L` concentrations.

## Completeness
- The base final-medium ingredients are present.
- The two stock solutions are not curated as nested stock recipes and therefore all stock rows were promoted to final-medium ingredient scope.
- Anaerobic handling, gas ratio, filter sterilization of the vitamin solution, separate 5% reducing-agent stock handling, trace-solution pH adjustment, and final pH are absent.
- Empty optional fields are acceptable, but the absent stock structure and preparation text change the recipe.

## Findings
- The NBRC stock hierarchy is flattened. Vitamin rows, trace-elements rows, their water, and trace-stock NaOH appear as top-level ingredients even though they belong under `Vitamin solution*` or `Trace elements solution**`.
- Stock additions use the wrong unit. Both 10 ml stock additions are represented as `10 G_PER_L`; they should remain volume additions or be explicitly normalized from the 10 ml per liter source quantities.
- Unit conversion is wrong for several milligram rows. The final-medium Fe(NH4)2(SO4)2 x 7 H2O and Resazurin entries are sourced as 2 mg and 1 mg but are represented as `2 G_PER_L` and `1 G_PER_L`, and every NBRC vitamin-stock milligram value was likewise promoted as a grams-per-liter concentration.
- Duplicate cleanup summed across stock boundaries. Generated water is `3.0 G_PER_L` from three 1 L rows, NaCl is `19.0 G_PER_L` from final-medium 18 g plus trace-stock 1 g, and CaCl2 x 2 H2O is `0.24000000000000002 G_PER_L` from final-medium 0.14 g plus trace-stock 0.1 g. The normalized owner now collapses water to 1.0 but still leaves the NaCl and CaCl2 sums.
- Preparation metadata was lost. The generated record lists Carbon dioxide gas and Nitrogen gas as variable ingredients but omits the 80/20 N2/CO2 atmosphere, separate N2 autoclaving of 5% reducing-agent solutions, filter-sterile vitamin addition, NTA pH 6.5 adjustment, and final pH 7.0.
- Two hydrated trace salts are grounded too broadly: CoCl2 x 6 H2O is linked to cobalt dichloride and NiCl2 x 6 H2O is linked to nickel dichloride.

## Recommended Edits
- Re-curate NBRC 1168 into `data/normalized_yaml/archaea/TOGO_M1908_Methanococcoides_medium.yaml`.
- Keep the final medium at the 1 L formula scope, with 18 g NaCl and 0.14 g CaCl2 x 2 H2O as final-medium quantities.
- Move the NBRC vitamin and trace rows into nested local stock recipes and retain their own 1 L water rows inside those stocks.
- Represent `Vitamin solution*` and `Trace elements solution**` as 10 ml per 1 L additions; do not point them at the unrelated `mediadive.solution:6241` and `mediadive.solution:6129` records.
- Convert source milligram rows to grams per liter only after respecting their stock scope. In particular, 1 mg Resazurin per liter is 0.001 G_PER_L in the final medium, and 2 mg Fe(NH4)2(SO4)2 x 7 H2O per liter is 0.002 G_PER_L.
- Restore preparation notes for the N2/CO2 80/20 atmosphere, N2-reduced 5% Cysteine-HCl and Na2S x 9 H2O stocks, filter-sterile vitamin addition, trace-solution NaOH pH adjustment, and final pH 7.0.
- Re-ground CoCl2 x 6 H2O and NiCl2 x 6 H2O to hydrate-specific terms if suitable CHEBI identifiers are available.

## Follow-up Checks
- Regenerate `data/merge_yaml/merged/methanococcoides_medium__1f16238c.yaml` after editing the normalized TOGO owner.
- Confirm that the regenerated record no longer has `Unknown solution`, `mediadive.solution:6241`, or `mediadive.solution:6129` under this NBRC-derived record.
- Confirm that no 10 ml stock addition is normalized as `10 G_PER_L`.
- Confirm that final-medium NaCl remains 18 g/L and final-medium CaCl2 x 2 H2O remains 0.14 g/L.
- Confirm that source milligram entries do not survive as whole-number `G_PER_L` values.
- Rerun open schema, strict, reference, and term validation.

## Additional Notes
- The generated merge fingerprint only contains one source recipe, so these issues are in the TOGO M1908 normalized owner or import/migration logic rather than a multi-record merge conflict.
