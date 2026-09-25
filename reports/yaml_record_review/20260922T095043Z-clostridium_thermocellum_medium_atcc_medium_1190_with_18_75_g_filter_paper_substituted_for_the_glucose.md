# YAML Record Review: Clostridium thermocellum medium (ATCC medium 1190) with 18.75 g filter paper substituted for the glucose

- Repository: CultureMech
- Record: `data/merge_yaml/merged/clostridium_thermocellum_medium_atcc_medium_1190_with_18_75_g_filter_paper_substituted_for_the_glucose.yaml`
- Started UTC: `2026-09-22T09:50:43Z`
- Finished UTC: `2026-09-22T09:51:49Z`
- Verdict: needs curation

## Target

Generated bacterial `MediaRecipe` record `CultureMech:009249` for TOGO Medium `M2697`, generated from `data/normalized_yaml/bacterial/clostridium_thermocellum_medium_atcc_medium_1190_with_18_75_g_filter_paper_substituted_for_the_glucose.yaml` on merge fingerprint `a19f04f343c393f865cc45dc04e05651b66c091604c818d5e55dfcee8bf3486c`.

## Validation

- LinkML open schema validation: passed.
- Strict validation: passed with no errors in `/private/tmp/clostridium_thermocellum_medium_atcc_filter.strict.tsv`.
- LinkML reference validation: passed; the validator reported 0 total checks.
- LinkML term validation: passed.
- Embedded `curation_history` entries: not checked by the standalone history validator.

## Identity and Grounding

The source identity is correct: TOGO `M2697` points to the ATCC source URL for ATCC Medium 1191, whose title is ATCC 1190 with 18.75 g filter paper substituted for the glucose. The generated record correctly preserves that named filter-paper variant rather than treating the missing ATCC 1190 glucose as an omission.

The chemical grounding is incomplete. `Whatman #1 filter paper`, `Wolfe's Modified Mineral Elixir`, `0.2 N NaOH`, `L-Cysteine . HCl`, `Thiamine . HCl`, `Pantothenic acid calcium salt`, and `2-3 N KOH` remain ungrounded. Several trace salts are grounded but lack MediaIngredientMech back-links.

The high-level medium identity is not duplicated elsewhere: an ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml/merged`, `data/import_tracking`, and `reports` found this source only as its normalized input and this merged output. Ignored files were included.

## Evidence

The ATCC document defines ATCC Medium 1191 as ATCC Medium 1190 with 18.75 g/L filter paper substituted for glucose. Its final recipe contains KH2PO4 1.5 g/L, Na2HPO4 . 12H2O 4.2 g/L, NH4Cl 0.5 g/L, MgCl2 . 6H2O 0.18 g/L, yeast extract 2.0 g/L, 0.5 ml/L vitamin solution, 5.0 ml/L Wolfe's Modified Mineral Elixir, 1.0 ml/L 0.1% resazurin, 40.0 ml/L reducing solution, and distilled deionized water to 1.0 L.

The same document defines the reducing solution as a separate stock made from 200.0 ml 0.2 N NaOH, 2.5 g Na2S . 9H2O, and 2.5 g L-Cysteine . HCl, handled under 95% N2 / 5% H2 and autoclaved under anaerobic conditions. Those are not separate final-medium 200, 2.5, and 2.5 g/L ingredients.

The vitamin solution is a separate 500 ml stock with milligram masses of Biotin, p-Aminobenzoic acid, Folic acid, Pantothenic acid calcium salt, Nicotinic acid, Vitamin B12, Thiamine . HCl, Pyridoxine hydrochloride, Thioctic acid, and Riboflavin; only 0.05 ml of that stock is used per 100 ml medium. The generated record instead keeps those stock milligram values as final `G_PER_L` rows.

Wolfe's Modified Mineral Elixir is also a separate 1 L stock. It includes 1.5 g nitrilotriacetic acid, 3.0 g MgSO4 . 7H2O, 1.0 g NaCl, and multiple 1 to 500 mg trace salts, is adjusted to pH 6.5 with 2-3 N KOH, and is added at 0.5 ml per 100 ml of medium. Most trace salts were imported as if source milligrams were final g/L values.

## Completeness

The generated record is incomplete for culture-relevant handling. The ATCC cautions about hydrogen sulfide evolution during boiling, initial boiling under 95% N2 / 5% H2, disappearance of the resazurin pink color after adding reducing solution, Hungate dispensing into tubes flushed with the same gas mixture, butyl-rubber stoppers, and 15 minute autoclaving of both the final medium and the reducing solution are absent from `preparation_steps`.

The two nested stock recipes are represented only as empty `solutions` entries with MediaDive solution identifiers, while their internal ingredients remain flattened into the top-level final formula. No target organism or growth evidence is present.

## Findings

- Severe: nested stock ingredients from the reducing solution, vitamin solution, and Wolfe's Modified Mineral Elixir were flattened into top-level final ingredients.
- Severe: source milligram masses in the vitamin and mineral stocks were converted to `G_PER_L`, producing multiple 1000x unit errors before any stock-dilution error is considered.
- Severe: the two nested waters were flattened into final rows. `Distilled deionized water` was summed to `501.0 G_PER_L`, and `Distilled water` from the mineral elixir remains as another `1 G_PER_L` final ingredient.
- Major: `0.2 N NaOH` is stored as `200 G_PER_L` even though the source says 200 ml in the reducing stock.
- Major: `Resazurin (0.1%)` is stored as `1 G_PER_L` even though the source adds 1.0 ml/L of a 0.1% solution.
- Major: `Vitamin Solution` and `Reducing Solution` are present as `solutions` rows with empty composition and `G_PER_L` units even though the source expresses those additions in ml/L.
- Major: gas and preparation details were not materialized into structured preparation steps.

## Recommended Edits

- Rebuild TOGO nested-stock handling for this record so reducing solution, vitamin solution, and Wolfe's Modified Mineral Elixir stay as solution additions instead of final ingredients.
- Convert the final additions from the ATCC source as 0.5 ml/L vitamin solution, 5.0 ml/L Wolfe's Modified Mineral Elixir, 1.0 ml/L 0.1% resazurin, and 40.0 ml/L reducing solution.
- Remove the flattened top-level vitamin, trace-metal, stock-water, 0.2 N NaOH, Na2S, L-Cysteine, and KOH rows after the stocks are represented correctly.
- Add preparation steps for boiling and reducing the medium under 95% N2 / 5% H2, Hungate dispensing under the same gas, butyl-rubber stoppering, autoclaving, the sodium sulfide hazard, anaerobic reducing-solution preparation, vitamin-solution storage away from light, and Wolfe elixir pH adjustment to 6.5.
- Ground the remaining ungrounded named chemicals or link them to solution/container terms where they are stock names rather than chemical formulae.

## Follow-up Checks

- Validate the regenerated record with open schema, strict, reference, and term validators.
- Confirm the regenerated top-level formula contains filter paper rather than glucose.
- Confirm no vitamin or trace mineral source milligram value appears as a final `G_PER_L` concentration.
- Confirm final waters do not include the 500 ml vitamin-solution solvent or 1 L mineral-elixir solvent.
- Confirm the TOGO `M2697` source still merges as a single-source recipe and does not create a duplicate ATCC branch.

## Additional Notes

Empty optional fields are not defects. This review treats the title-level ATCC 1190 to ATCC 1191 substitution as intentional because ATCC says this variant substitutes 18.75 g filter paper for glucose and allows one Whatman #1 strip per tube when preparing tubed medium.
