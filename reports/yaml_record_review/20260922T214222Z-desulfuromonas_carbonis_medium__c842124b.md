# YAML Record Review: desulfuromonas_carbonis_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfuromonas_carbonis_medium__c842124b.yaml`
- Started UTC: 2026-09-22T21:40:52Z
- Finished UTC: 2026-09-22T21:42:22Z
- Verdict: needs curation

## Target

`CultureMech:001059` represents MediaDive DSMZ Medium 1584, `DESULFUROMONAS CARBONIS MEDIUM`. The generated record is a single-source merge from `data/normalized_yaml/bacterial/desulfuromonas_carbonis_medium.yaml`.

## Validation

- LinkML open-world validation passed.
- Strict CultureMech validation passed with zero error rows.
- Reference validation passed with zero checks.
- LinkML term validation passed.
- Embedded curation history was not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged YAML.

## Identity and Grounding

DSMZ 1584 is a defined `Desulfuromonas carbonis` formulation with a 1015 ml MediaDive main solution. A gitignore-independent, case-insensitive `find` over `data/` found this DSMZ 1584 split, the TOGO M1131 and JCM J1062 `Desulfuromonas carbonis` recipes, and other nearby `Desulfuromonas` records; DSMZ 1584 should not be merged with the JCM 1062 formulation without source support because the salts, stock additions, and final assembly differ.

## Evidence

- MediaDive DSMZ 1584 defines `Main sol. 1584` as a 1015 ml solution with 1000 ml distilled water, main salts, 3 ml 0.1% Fe(NH4)2(SO4)2, 9 ml 0.1% NiCl2, 1 ml Trace element solution SL-10, 1 ml Selenite-tungstate solution, Na2CO3, Na2-fumarate, and 1 ml Wolin's vitamin solution (10x).
- Trace element solution SL-10 is a separate 1000 ml stock with HCl, FeCl2, ZnCl2, MnCl2, H3BO3, CoCl2, CuCl2, NiCl2, Na2MoO4, and 990 ml distilled water.
- Selenite-tungstate solution is a separate 1000 ml stock with NaOH, Na2SeO3, Na2WO4, and 1000 ml distilled water.
- Wolin's vitamin solution (10x) is a separate 1000 ml stock with ten vitamin rows and 1000 ml distilled water.

## Completeness

The record is incomplete because the generated YAML has only a flat `ingredients` list. The 1 ml SL-10, 1 ml selenite-tungstate, and 1 ml Wolin vitamin stock additions were not represented as stock additions; instead, every child component was copied to the top level at its stock strength and all source water rows were omitted.

## Findings

- Trace element solution SL-10 was flattened, so its HCl, FeCl2, ZnCl2, MnCl2, H3BO3, CoCl2, CuCl2, NiCl2, and Na2MoO4 rows look like final-medium ingredients instead of components of a 1000 ml stock added at 1 ml per 1015 ml.
- Selenite-tungstate solution was flattened, so 0.5 g/l NaOH, 0.003 g/l Na2SeO3, and 0.004 g/l Na2WO4 stock concentrations were promoted to top-level final concentrations.
- Wolin's vitamin solution (10x) was flattened, so ten vitamin rows appear at 10x stock strength rather than under a 1 ml stock addition.
- The direct main-medium NiCl2 row was merged with the SL-10 NiCl2 row into `0.03286699 G_PER_L`, even though the two values belong to different source scopes.
- The 1000 ml main water, 990 ml SL-10 water, 1000 ml selenite-tungstate water, and 1000 ml Wolin vitamin water rows are missing.
- The SL-10 dissolution instruction was appended as a generic top-level preparation step rather than staying attached to Trace element solution SL-10.

## Recommended Edits

- Restore `Main sol. 1584` as a 1015 ml recipe with explicit 1 ml SL-10, 1 ml selenite-tungstate, and 1 ml Wolin vitamin stock additions.
- Move the flattened SL-10, selenite-tungstate, and Wolin vitamin child rows under their source stocks, including each stock water row.
- Preserve the direct main-medium 0.1% Fe(NH4)2(SO4)2 and 0.1% NiCl2 liquid-stock additions separately from the trace stocks.
- Undo the cross-scope NiCl2 duplicate merge so main-medium nickel and SL-10 nickel remain distinct.
- Keep the DSMZ 1584 record distinct from the JCM 1062 and TOGO M1131 records unless a curator adds an explicit source-backed relationship.

## Follow-up Checks

- Re-run open-world, strict, reference, and term validation after normalization changes and regeneration.
- Verify that no SL-10, selenite-tungstate, or Wolin vitamin child component remains at the top level.
- Verify that no duplicate ingredient merge crosses a stock-solution boundary.
- Verify that all four source water rows are represented in their correct scopes.

## Additional Notes

None found.
