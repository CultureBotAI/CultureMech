# YAML Record Review: mw_medium_for_methanosarcina__1a2a32c7

- Repository: CultureMech
- Record: data/merge_yaml/merged/mw_medium_for_methanosarcina__1a2a32c7.yaml
- Started UTC: 2026-09-24T15:53:29Z
- Finished UTC: 2026-09-24T15:55:34Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/mw_medium_for_methanosarcina__1a2a32c7.yaml`.

The generated record represents the direct MediaDive/JCM owner for JCM Medium
944:

- canonical `id`: `CultureMech:003292`
- canonical `media_term`: `mediadive.medium:J944`
- canonical `name`: `mw_medium_for_methanosarcina`
- canonical `original_name`: `MW MEDIUM FOR METHANOSARCINA`
- `medium_type`: `DEFINED`
- `composition_type`: `DEFINED`
- `physical_state`: `LIQUID`
- `ph_value`: `6.5`
- `ingredients`: 31
- `solutions`: 0
- `merged_from`: `mw_medium_for_methanosarcina`

## Validation

- Open schema validation: Passed; exited 0 with no diagnostics.
- Strict schema validation: Passed with 0 errors; the TSV contained only the
  header row.
- Reference validation: Passed with 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked; `just validate-history` validates
  standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The high-level MediaDive/JCM identity is correct for JCM Medium 944. However,
the generated record preserves the old flat MediaDive import rather than the
JCM recipe's structure of a main solution, two referenced stock solutions,
post-autoclave percentage stocks, and separate gas-phase handling steps.

An exact ignored-file-inclusive search for `CultureMech:003292`, `GRMD=944`,
`mediadive.medium:J944`, `TOGO:M991`, and `CultureMech:010419` found two
active normalized owners for the same JCM 944 page:

- `CultureMech:003292`:
  `data/normalized_yaml/archaea/mw_medium_for_methanosarcina.yaml`
- `CultureMech:010419`:
  `data/normalized_yaml/archaea/TOGO_M991_MW_Medium_For_Methanosarcina.yaml`

Those owners are not linked as source duplicates, and the TOGO M991 import
also still generates a separate `data/merge_yaml/merged/MW_MEDIUM_FOR_METHANOSARCINA.yaml`
record.

`NiCl2 x 6 H2O` is over-broadened to generic `CHEBI:34887` / `nickel
dichloride`; the hydrate-specific source label should not resolve to generic
nickel dichloride.

## Evidence

The current JCM 944 page lists a base solution containing 1.0 g NaCl, 0.5 g
KCl, 0.4 g MgCl2 x 6 H2O, 0.25 g NH4Cl, 0.15 g CaCl2 x 2 H2O, 10 ml Trace
elements solution, 1 mg Resazurin, and 946 ml distilled water. After
autoclaving under N2-CO2 at 80:20, the source instructs anaerobic addition of
2 ml 10% KH2PO4, 32 ml 8% NaHCO3, and 10 ml Vitamin solution, then
distribution under H2-CO2 at 80:20, then final per-liter addition of 6 ml each
of 5% L-Cysteine HCl x H2O and 5% Na2S x 9 H2O from anaerobic stocks.

The current JCM page separately defines a 1 L Trace elements solution and a 1 L
Vitamin solution, and the current MediaDive REST record mirrors that structure
as `Trace elements solution` and `Vitamin solution` stock references in a
1012 ml main solution.

The current TOGO M991 API points back to JCM 944 and carries the same base
solution, staged post-autoclave additions, gas instructions, trace-elements
stock, and vitamin stock, confirming it is a source duplicate rather than a
separate formulation.

## Completeness

The first six simple ingredients in the generated record are internally
consistent with MediaDive's 1012 ml main-solution denominator, including the
1 mg Resazurin entry scaled to 0.000988142 g/L. After that point, the generated
record treats stock additions as final ingredients.

The generated record omits the 946 ml main distilled water and has no nested
`solutions` for the 10 ml Trace elements solution or the 10 ml Vitamin
solution. Every trace-element and vitamin component is therefore present at
stock strength: for example, nitrilotriacetic acid is 1.5 g/L, p-Aminobenzoic
acid is 0.01 g/L, and Vitamin B12 is 0.005 g/L in their stocks, not in the
final MW Medium.

The intermediate and final anaerobic stock additions have the same unit error.
JCM calls for 2 ml of 10% KH2PO4, 32 ml of 8% NaHCO3, and 6 ml each of 5%
L-Cysteine HCl x H2O and 5% Na2S x 9 H2O; the generated record casts those
addition volumes directly as 2, 32, 6, and 6 g/L final ingredients.

## Findings

- The main 946 ml distilled-water ingredient is missing.
- The 10 ml/L Trace elements solution and 10 ml/L Vitamin solution were
  flattened into stock-strength top-level ingredients.
- The 2 ml 10% KH2PO4, 32 ml 8% NaHCO3, 6 ml 5% L-Cysteine HCl x H2O, and
  6 ml 5% Na2S x 9 H2O additions were cast as final g/L concentrations.
- The TOGO M991 source duplicate remains an active, unlinked owner and a
  separate generated record.
- `NiCl2 x 6 H2O` is grounded to generic `CHEBI:34887` / `nickel dichloride`.

## Recommended Edits

- Repair `data/normalized_yaml/archaea/mw_medium_for_methanosarcina.yaml` to
  preserve the main water ingredient, Trace elements solution, Vitamin
  solution, and four percentage-stock additions.
- Link `data/normalized_yaml/archaea/TOGO_M991_MW_Medium_For_Methanosarcina.yaml`
  to the direct JCM/MediaDive owner as a `SOURCE_DUPLICATE` after correcting
  the TOGO stock-solution stubs.
- Represent KH2PO4, NaHCO3, L-Cysteine HCl x H2O, and Na2S x 9 H2O as
  percentage stock additions, or scale their solutes by the 1012 ml main
  recipe before emitting flat generated ingredients.
- Preserve the JCM trace-element and vitamin compositions under nested stock
  solutions if the schema can carry them.
- Ground `NiCl2 x 6 H2O` to a hydrate-specific CHEBI term.
- Regenerate the merged YAML after repairing the maintained owners.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validation on the
  regenerated YAML.
- Confirm the regenerated record has one 10 ml/L Trace elements solution and
  one 10 ml/L Vitamin solution.
- Confirm `KH2PO4`, `NaHCO3`, `L-Cysteine HCl x H2O`, and `Na2S x 9 H2O` no
  longer appear with concentrations of 2, 32, 6, and 6 g/L.
- Confirm an ignored-file-inclusive exact search for `TOGO:M991` and
  `GRMD=944` shows one generated MW Medium for Methanosarcina record after
  regeneration.

## Additional Notes

The TOGO M991 generated record sorted earlier as an uppercase filename, so this
review only records its duplicate relationship to the lowercase direct
MediaDive/JCM record.
