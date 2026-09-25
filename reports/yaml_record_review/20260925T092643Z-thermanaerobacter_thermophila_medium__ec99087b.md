# YAML Record Review: thermanaerobacter_thermophila_medium__ec99087b

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermanaerobacter_thermophila_medium__ec99087b.yaml
- Started UTC: 2026-09-25T09:26:43Z
- Finished UTC: 2026-09-25T09:27:45Z
- Verdict: needs curation

## Target

Generated merged MediaRecipe `CultureMech:007521`, `thermanaerobacter_thermophila_medium`, produced by merging TOGO `M883` / C5BEL Medium with TOGO `M1008` / JCM `M959`.

## Validation

- LinkML schema validation passed.
- Strict validation passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows.
- Reference validation passed: 1 file validated, 0 reference checks, all validations passed.
- Term validation passed.
- Embedded `curation_history` was not checked because the standalone history validator targets files under `history/`, not merged `MediaRecipe.curation_history`.

## Identity and Grounding

- TOGO `M1008` identifies `Thermanaerobacter Thermophila Medium`, `original_media_id: JCM_M959`, with source URL JCM `GRMD=959`.
- TOGO `M883` identifies `C5BEL Medium`, `original_media_id: JCM_M847`, with source URL JCM `GRMD=847`.
- The live JCM `GRMD=959` page currently reports `Nothing found`; TOGO `M1008` and the separate MediaDive `J959` import preserve the JCM-derived Thermanaerobacter thermophila formulation.
- An exact `TOGO:M1008` / `TOGO:M883` / `GRMD=959` / `JCM_M959` / `C5BEL` / `thermanaerobacter_thermophila_medium` search scoped to `data/merge_yaml/merged` and `data/normalized_yaml/bacterial` with ignored files included found the generated false merge, the unmerged MediaDive `J959` generated record, the standalone generated `C5BEL_MEDIUM.yaml`, and their normalized source files.

## Evidence

- TOGO `M1008` has the JCM `M959` Thermanaerobacter thermophila base at 935 ml water with 0.5 g yeast extract, 1 g NaCl, 0.15 g `CaCl2 x 2 H2O`, 0.3 g KH2PO4, 0.3 g NH4Cl, 0.3 g K2HPO4, 1 mg resazurin, 0.5 g `MgCl2 x 6 H2O`, 0.1 g KCl, 1 ml trace metal solution `M288`, and later 25 ml 8% NaHCO3, 20 ml 1 M glucose, 8 ml 5% `Na2S x 9 H2O`, and 20 ml 1 M `Na2S2O3 x 5 H2O`.
- TOGO `M883` has C5BEL Medium from JCM `M847`, not `M959`; it has 1 L water, 1 g yeast extract, 1 g NaCl, 0.1 g `CaCl2 x 2 H2O`, 0.3 g KH2PO4, 0.5 g NH4Cl, 0.3 g K2HPO4, 1 mg resazurin, 0.06 g `MgCl2 x 6 H2O`, 0.1 g KCl, 10 ml trace minerals `M142`, and later 25 ml 8% NaHCO3, 20 ml 1.0 M glucose, and 8 ml 5% sodium sulfide.
- The separate MediaDive `J959` generated record matches the JCM `M959` / TOGO `M1008` quantities after scaling to the final 1009 ml volume and keeps the trace-element addition as a separate solution placeholder.

## Completeness

- The generated target is not internally source-faithful: its top-level base medium reflects C5BEL values for yeast extract, NH4Cl, `MgCl2 x 6 H2O`, and `CaCl2 x 2 H2O`, while its solution list contains the M1008-only 1 M thiosulfate stock.
- All five solution additions are empty `Unknown solution` entries with `G_PER_L` units, even though the source values are milliliter stock additions.
- The generated target retains `c5bel_medium` as a synonym even though C5BEL is a different JCM medium, not a synonym of Thermanaerobacter thermophila Medium.
- The source-equivalent MediaDive `J959` import remains split out in `data/merge_yaml/merged/THERMANAEROBACTER_THERMOPHILA_MEDIUM.yaml`.

## Findings

- The merge between TOGO `M883` and TOGO `M1008` is a false positive. It combines recipes from two different JCM source media, `M847` and `M959`, into one `CultureMech` record.
- The false merge overwrote M1008 direct ingredients with C5BEL values while retaining the M1008 1 M `Na2S2O3 x 5 H2O` stock addition, creating a hybrid formula absent from either source.
- Stock additions are unit-corrupted: 25 ml 8% NaHCO3, 20 ml 1 M glucose, 8 ml 5% sodium sulfide, and 20 ml 1 M thiosulfate appear as `25`, `20`, `8`, and `20` `G_PER_L` unknown solutions.
- The trace-metal cross-reference is ambiguous after the false merge because C5BEL points to TOGO `M142` while M1008 points to TOGO `M288`.

## Recommended Edits

- Do not hand-edit `data/merge_yaml/merged/thermanaerobacter_thermophila_medium__ec99087b.yaml`; repair the normalized records or merge fingerprint logic, then regenerate it.
- Split TOGO `M883` / C5BEL Medium back out from TOGO `M1008`; they have different JCM original media IDs, different direct salts, and different trace-mineral cross-references.
- Merge TOGO `M1008` with the MediaDive `J959` record only after source identity reconciliation by shared `JCM_M959` / `GRMD=959`.
- Represent the M1008 and M883 stock additions as milliliter stock additions, not as `G_PER_L` unknown solutions.

## Follow-up Checks

- After merge repair, rerun schema, strict, reference, and term validation on the regenerated M1008 and M883 records.
- Re-run an exact duplicate search for `TOGO:M1008`, `TOGO:M883`, `JCM_M959`, `JCM_M847`, `GRMD=959`, and `GRMD=847` with ignored files included.
- Verify that `c5bel_medium` is no longer a synonym of `thermanaerobacter_thermophila_medium`.
- Verify that the regenerated Thermanaerobacter thermophila record has the M1008 base values and the M1008 `M288` trace-metal reference.

## Additional Notes

The first local source search included bare `M1008`; that was too broad because it matched unrelated `NBRC_M1008` and `JCM_M1008` lines. Those hits were discarded, and the local search was rerun with exact `TOGO:M1008`, `TOGO:M883`, `GRMD=959`, `JCM_M959`, `C5BEL`, and `thermanaerobacter_thermophila_medium` patterns.
