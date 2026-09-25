# YAML Record Review: NASU IRON REDUCER MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/nasu_iron_reducer_medium__1ba60e59.yaml
- Started UTC: 2026-09-24T16:35:04Z
- Finished UTC: 2026-09-24T16:35:04Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:002199` for the direct JCM import of JCM Medium 1014, `NASU IRON REDUCER MEDIUM`, with MediaDive term `mediadive.medium:J1014`.

## Validation

Open schema validation passed with no issues.

Strict validation passed with 0 errors; the strict TSV contained only the header row.

Reference validation passed with 0 checks.

Term validation passed.

Embedded `curation_history` was not checked: `just validate-history` validates the standalone `history/` tree, not `MediaRecipe.curation_history` inside merged generated YAML.

## Identity and Grounding

The record is grounded to the intended direct JCM `GRMD=1014` source through `mediadive.medium:J1014`.

An exact repository search including ignored files for `nasu_iron_reducer_medium`, `GRMD=1014`, `mediadive.medium:J1014`, and `TOGO:M1072` found this direct JCM owner and generated file plus the active TOGO M1072 owner at `data/normalized_yaml/bacterial/TOGO_M1072_NASU_Iron_Reducer_Medium.yaml`. Both owners cite JCM Medium 1014 and both still generate.

`L-Cysteine HCl` is still keyed through legacy `mediaingredientmech_term` rather than a CHEBI-safe `mediaingredientmech_chebi_term`.

## Evidence

JCM Medium 1014 lists 0.2 g (NH4)2SO4, 3.0 g KH2PO4, 0.5 g MgSO4 x 7H2O, 0.25 g CaCl2 x 2H2O, 0.5 g yeast extract, 1.0 ml Modified Allen's trace metal solution, 10.0 ml Trace vitamins from Medium 197, 100.0 ml Iron(III) citrate solution, and 900.0 ml distilled water. The base medium is adjusted to pH 6.0, autoclaved under N2-CO2 at 4:1, and then receives 10.0 ml 25 mM L-cysteine HCl and 10.0 ml 130 mM FeCl2.

JCM Medium 1014 defines the Modified Allen's trace metal solution per 1 L as MnCl2 x 4H2O, Na2B4O7 x 10H2O, ZnSO4 x 7H2O, CuCl2 x 2H2O, Na2MoO4 x 2H2O, VOSO4 x xH2O, CoSO4 x 7H2O, and distilled water.

JCM Medium 1014 defines the Iron(III) citrate solution by dissolving 2.4 g iron(III) citrate in 90 ml distilled water, adjusting to pH 6.0 with 10 N NaOH, and filling to 100 ml with distilled water.

MediaDive J1014 keeps Modified Allen's trace metal solution, Iron(III) citrate solution, and Trace vitamins as separate solutions. Its main solution final volume is 1031 ml, which explains the normalized base-salt values such as 0.193986 g/L (NH4)2SO4 and 2.9098 g/L KH2PO4.

## Completeness

The generated record is missing the main 900 ml distilled water row, the 100 ml Iron(III) citrate solution addition and its iron citrate composition, the 1.0 ml Modified Allen's trace metal solution addition, the 10.0 ml Trace vitamins addition, the 10.0 ml L-cysteine HCl stock addition, and the 10.0 ml FeCl2 stock addition.

It keeps the main pH and the Iron(III) citrate preparation sentence, but it does not structurally represent the N2-CO2 4:1 gas mixture, the N2 storage instruction, or the aseptic post-autoclave addition order.

## Findings

- The generated record flattens the Modified Allen's trace metal solution and Trace vitamins internals into final top-level ingredients at stock concentrations.
- The 100 ml Iron(III) citrate solution addition is absent as a structured solution; the direct record only preserves its preparation text.
- The generated `L-Cysteine HCl` and `FeCl2` rows use the 10 ml addition volumes as `10 G_PER_L` final concentrations instead of preserving 25 mM and 130 mM stock additions.
- Distilled water from the main solution and water from the nested stocks are absent.
- The active TOGO M1072 mirror is unmerged. Its generated record has empty solution stubs and an over-merged `1001.0 G_PER_L` water row derived from the 900 ml main water, 1 L Modified Allen stock water, and 100 ml Iron(III) citrate stock water.
- Legacy `mediaingredientmech_term` remains on `L-Cysteine HCl`.

## Recommended Edits

- Re-curate the direct JCM owner with nested Modified Allen's trace metal, Trace vitamins, Iron(III) citrate, L-cysteine HCl, and FeCl2 stock additions instead of direct final rows.
- Restore the 100 ml Iron(III) citrate solution addition with its 2.4 g iron citrate, 90 ml water, 10 N NaOH pH adjustment, and fill-to-100-ml water context.
- Link or retire the TOGO M1072 owner so JCM Medium 1014 does not produce a second active NASU Iron Reducer record.
- Refresh `L-Cysteine HCl` to a CHEBI-safe MediaIngredientMech link keyed on `CHEBI:91247`.

## Follow-up Checks

- Regenerate `data/merge_yaml/merged/nasu_iron_reducer_medium__1ba60e59.yaml` and verify the stock internals remain nested and the Iron(III) citrate solution is no longer dropped.
- Re-run open schema, strict, reference, and term validation after curation.
- Search including ignored files for `GRMD=1014`, `mediadive.medium:J1014`, and `TOGO:M1072` to verify the duplicate is resolved.

## Additional Notes

None found.
