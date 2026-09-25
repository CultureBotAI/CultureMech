# YAML Record Review: methanosarcina_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/methanosarcina_medium__046448c4.yaml
- Started UTC: 2026-09-24T04:59:18Z
- Finished UTC: 2026-09-24T04:59:18Z
- Verdict: needs curation

## Target

Generated `MediaRecipe` `CultureMech:000660` for DSMZ/MediaDive medium 120, "METHANOSARCINA MEDIUM", derived from `data/normalized_yaml/archaea/methanosarcina_medium.yaml`.

## Validation

- LinkML open schema validation: Passed; exited 0 with no diagnostics.
- Strict recipe validation: Passed; `/private/tmp/methanosarcina_medium_046448c4.strict.tsv` contained only the header row.
- Reference validation: Passed.
- Term validation: Passed.
- Embedded curation history: Not checked: the history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

- The recipe identity is grounded to DSMZ/MediaDive medium 120 and retains the DSMZ label, DSMZ PDF link, liquid state, undefined complex composition, and final pH range of 6.8-7.0.
- The top-level source identity is not ambiguous: the generated record has a single `merged_from` value and no evidence of cross-medium merge conflation.
- The ingredient list is not a faithful single-solution rendering of DSMZ 120 because three nested stock solutions are flattened at stock strength into the main formula and the source solvent rows are dropped.
- The `Methanosarcina acetivorans` slow-growth target organism and variant cite a real `M. acetivorans` growth result from PMID:21097629, but the inspected article text grew strain C2A in HS medium, not this DSMZ 120 recipe.

## Evidence

- DSMZ Medium 120 and the MediaDive REST record agree on the main formula: 1000 ml distilled water plus K2HPO4, KH2PO4, NH4Cl, MgSO4 x 7 H2O, CaCl2 x 2 H2O, NaCl, 2 ml FeSO4 x 7 H2O solution, 1 ml Trace element solution SL-10, yeast extract, Casitone, Na-acetate, 0.5 ml 0.1% sodium resazurin, NaHCO3, 20 ml 50% methanol, 1 ml Wolin's vitamin solution, L-Cysteine HCl x H2O, and Na2S x 9 H2O.
- MediaDive models the FeSO4 x 7 H2O solution, SL-10, and Wolin's vitamin solution as separate solution records, matching the DSMZ PDF's nested stock sections. Their stock concentrations are not final medium concentrations.
- DSMZ lists in-source strain variants for DSM 1538, DSM 7058, DSM 9195, DSM 1825, DSM 7081, DSM 11855, and DSM 21571; none are represented in the generated YAML.
- PMID:21097629 supports `Methanosarcina acetivorans` C2A growth under anaerobic conditions at 37 C in high-salt medium with either 125 mM methanol or 120 mM sodium acetate as the sole energy source. It supports the cited 49 h slow-growth metric in that literature context, but not exact growth on DSMZ Medium 120.

## Completeness

- The main salts, bicarbonate, organics, 0.1% resazurin stock addition, 50% methanol stock addition, cysteine, sulfide, pH, and anoxic/autoclave/filtration instructions are present.
- The three stock solution boundaries are missing from the represented formula even though their preparation text is partially present.
- Main and stock water rows are absent.
- Source-specific variant substitutions and supplements are absent.

## Findings

1. Major - Nested stock solutions are flattened at stock strength. DSMZ 120 adds 2 ml FeSO4 solution, 1 ml SL-10, and 1 ml Wolin's vitamin solution to the main 1000 ml water recipe, but the generated main ingredient list includes each nested component at its stock concentration, including `FeSO4 x 7 H2O` at `1 G_PER_L`, `H2SO4` at `1000 G_PER_L`, SL-10 metals at full SL-10 strength, and vitamins at full 10x stock strength. This overstates every nested additive and loses the stock-addition semantics.
2. Major - Solvent rows were dropped from all solution scopes. DSMZ has 1000 ml distilled water in the main recipe, 990 ml distilled water in SL-10, and 1000 ml distilled water in the Wolin vitamin solution; none appear as `Water` ingredients or explicit child-solution solvents in the generated record.
3. Major - DSMZ 120 source variants are missing. The PDF says some DSM strains replace methanol with 5.00 g/l trimethylamine-HCl, others require 5% clarified rumen fluid and a 6.5-6.8 pH, and DSM 21571 requires an added 6.00 g/l NaCl. A consumer cannot reconstruct those in-source alternatives from this YAML.
4. Major - The growth metric is scoped to DSMZ 120 without source support. PMID:21097629 reports `Methanosarcina acetivorans` C2A growth in HS medium with methanol or sodium acetate, while the generated target organism and the `slow_growth_phase_methanosarcina_acetivorans` variant assert that the 49 h slow-growth value belongs under the parent Methanosarcina Medium record.
5. Minor - The sodium resazurin entry loses stock-addition context by preserving only the MediaDive-computed final mass of resazurin. The source row is a 0.50 ml addition of a 0.1% stock solution and should keep that experimental form.

## Recommended Edits

- Recurate the normalized source so DSMZ/MediaDive solution IDs 5861, 595, and 5980 remain nested stock solutions, or update the import/merge step to dilute child solutions into the parent solution with traceable source-volume provenance.
- Restore water or solvent rows for the main recipe, SL-10 stock, and Wolin vitamin stock if the schema can represent them; otherwise leave an explicit structured note that those source rows were intentionally omitted.
- Add explicit variant records for the DSMZ 120 methanol-to-trimethylamine-HCl replacement, clarified-rumen-fluid supplement with altered pH, and extra-NaCl supplement.
- Move the PMID:21097629 49 h slow-growth evidence to a medium record that is grounded to HS medium, or add a source showing that the HS medium used in that paper is equivalent to DSMZ 120 before attaching the metric here.
- Preserve the 0.50 ml 0.1% sodium-resazurin-stock source row in stock-addition form rather than only as a final resazurin mass concentration.

## Follow-up Checks

- Re-run focused schema, strict, reference, and term validators on the regenerated merged YAML.
- Confirm that no regenerated DSMZ 120 record duplicates FeSO4, SL-10, or Wolin vitamin stock components in the parent ingredient list.
- Confirm that variant rows remain strain-scoped and do not pollute the canonical DSMZ 120 parent formula.

## Additional Notes

The source preparation text is unusually important for this record because it identifies which compounds are added before autoclaving, which reducing-agent and methanol stocks are separately autoclaved under N2, and which vitamins are filter-sterilized. The generated `preparation_steps` preserve that prose, so the repair should focus on formula structure and on the unsupported literature attachment rather than on source identity.
