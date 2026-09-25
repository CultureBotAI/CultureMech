# YAML Record Review: methanosarcina_thermophila_bcyt_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/methanosarcina_thermophila_bcyt_medium.yaml
- Started UTC: 2026-09-24T05:09:02Z
- Finished UTC: 2026-09-24T05:09:02Z
- Verdict: needs curation

## Target

Generated `MediaRecipe` `CultureMech:000260` for DSMZ/MediaDive medium 318, "METHANOSARCINA THERMOPHILA (BCYT) MEDIUM", merged with KOMODO parents for medium 318 and 318a.

## Validation

- LinkML open schema validation: Passed with "No issues found".
- Strict recipe validation: Passed; `/private/tmp/methanosarcina_thermophila_bcyt_medium.strict.tsv` contained only the header row.
- Reference validation: Passed with 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked: the history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

- The primary DSMZ 318 identity is grounded correctly and the generated pH 6.8 matches the MediaDive record and DSMZ PDF.
- DSMZ 318 has one parent formula plus two child stocks: 10 ml Trace element solution and 1 ml Wolin's vitamin solution (10x).
- The generated formula has no child solutions and folds the trace and vitamin stocks into the parent `ingredients` list.
- The merge with KOMODO `318a` is not source-faithful to live DSMZ 318a: the current MediaDive `318a` record is "PELOBACTER (FUF) MEDIUM", a distinct pH 7.0-7.2 recipe with HEPES and 2-furoic acid.

## Evidence

- DSMZ Medium 318 lists 0.30 g KH2PO4, 0.60 g NaCl, 0.10 g MgCl2 x 6 H2O, 0.08 g CaCl2 x 2 H2O, 10 ml trace element solution, NH4Cl, yeast extract, Trypticase peptone, 0.50 ml 0.1% sodium resazurin, KHCO3, 10 ml 50% methanol, 1 ml Wolin's vitamin solution (10x), L-Cysteine HCl x H2O, Na2S x 9 H2O, and 1000 ml distilled water.
- MediaDive models the Trace element solution as solution 589 and the 10x Wolin vitamin solution as solution 5980, matching the child stock sections in the DSMZ PDF.
- The generated `NaCl` and `CaCl2 x 2 H2O` rows show duplicate sums, `0.587659 + 1.0` and `0.0783546 + 0.1`, demonstrating that the trace element stock was added to the parent salts.
- DSMZ/MediaDive 318a is not the same medium as DSMZ/MediaDive 318 and does not share the generated BCYT ingredient set.

## Completeness

- The DSMZ 318 preparation prose and final pH are present.
- The main 1000 ml distilled water row is absent.
- Trace element and Wolin vitamin stock boundaries are absent.
- The record has stale `fuf_medium` synonym/category data from a KOMODO 318a mapping that should be reconciled against the distinct live DSMZ 318a source.

## Findings

1. Major - Trace element stock components are flattened into the parent formula. DSMZ 318 adds 10 ml of solution 589, but the generated record adds the stock's NTA, FeCl2 x 4 H2O, MnCl2 x 4 H2O, CoCl2 x 6 H2O, CaCl2 x 2 H2O, ZnCl2, CuCl2, H3BO3, Na2MoO4 x 2 H2O, NiCl2 x 6 H2O, NaCl, Na2SeO3 x 5 H2O, and Na2WO4 x 2 H2O as full-strength parent ingredients.
2. Major - The Wolin 10x vitamin stock is flattened into the parent formula. The source adds only 1 ml stock per liter, but the generated vitamin rows carry the stock concentrations such as `0.02 G_PER_L` biotin and folic acid, `0.1 G_PER_L` pyridoxine, and `0.001 G_PER_L` Vitamin B12.
3. Major - The main 1000 ml distilled water row and both stock solvent rows were dropped, leaving no explicit solvent for the parent or child formulas.
4. Major - The duplicate merge includes a stale or wrong KOMODO 318a parent. Live DSMZ/MediaDive 318a is Pelobacter FUF medium with HEPES, 2-furoic acid, pH 7.0-7.2, and a different main formula, so `fuf_medium` should not be synonymized into DSMZ 318 without a separate source proving KOMODO 318a meant DSMZ 318.
5. Minor - The 0.50 ml 0.1% sodium-resazurin and 10 ml 50% methanol additions are reduced to computed final masses; their stock-addition form should remain traceable.

## Recommended Edits

- Recurate DSMZ/MediaDive 318 with child solution records for Trace element solution 589 and Wolin's vitamin solution 5980, or dilute those stocks with explicit volume provenance if the schema requires a flat output.
- Restore the parent and stock water rows in their proper solution scopes.
- Remove `fuf_medium`/KOMODO 318a from this merge unless a current, source-backed crosswalk shows it is actually DSMZ 318 rather than DSMZ 318a.
- Preserve stock-addition details for sodium resazurin and 50% methanol.

## Follow-up Checks

- Re-run focused schema, strict, reference, and term validators on the regenerated merged YAML.
- Compare the regenerated BCYT parent salts against DSMZ 318 to confirm NaCl is not inflated by 1.0 g/l and CaCl2 x 2 H2O is not inflated by 0.10 g/l.
- Confirm that DSMZ 318a remains separate from DSMZ 318 in merge outputs.

## Additional Notes

The preserved preparation text is a useful guardrail: it explicitly says vitamins are filter-sterilized and methanol, cysteine, sulfide, and bicarbonate are added from sterile anoxic stock solutions. That stock-oriented prose should align with the formula structure after repair.
