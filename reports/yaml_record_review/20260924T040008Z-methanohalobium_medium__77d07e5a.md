# YAML Record Review: methanohalobium_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/methanohalobium_medium__77d07e5a.yaml
- Started UTC: 2026-09-24T04:00:08Z
- Finished UTC: 2026-09-24T04:04:02Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:009203` / `methanohalobium_medium`, produced from one normalized TOGO import:

- `data/normalized_yaml/archaea/TOGO_M2647_Methanohalobium_Medium.yaml`
- `merged_from`: `TOGO_M2647_Methanohalobium_Medium`
- `merge_fingerprint`: `77d07e5ae17a17520f3f56f8ebdb26ccb9784ae4025c5fc823148d34c10ffa2a`
- Upstream identity: TOGO Medium `M2647`, original URL `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium375.pdf`

## Validation

- LinkML open validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed with 0 error rows in `/private/tmp/methanohalobium_medium__77d07e5a.strict.tsv`.
- Reference validation: Passed; 0 checks.
- Term validation: Passed.
- Embedded history: Not checked: `just validate-history` validates standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in merged YAML.

## Identity and Grounding

The generated record keeps the expected CultureMech identifier, TOGO `M2647` medium term, original name, original URL, and single-source merge fingerprint. The normalized owner already contains the same duplicated water total, flattened SL-10 components, and empty solution placeholders, so these defects need to be fixed in `data/normalized_yaml/archaea/TOGO_M2647_Methanohalobium_Medium.yaml` or in the TOGO solution migration path.

The linked current DSMZ 375 PDF and MediaDive DSMZ 375 REST record no longer match TOGO `M2647`: the current DSMZ recipe has DTT, cysteine, Wolin's vitamin solution, 1.5 g `Na2CO3`, and no direct `Na2S x 9 H2O` addition, while TOGO `M2647` has 0.5 g `Na2S x 9 H2O`, 2.5 g `Na2CO3`, and no Wolin vitamin block. The review below therefore treats the TOGO `M2647` API as the direct import evidence and treats the live DSMZ URL as revision-drift context.

## Evidence

- TOGO `M2647` lists `Na-resazurin solution (0.1% w/v)` at 0.5 ml, 1000 ml distilled water, 4 g `MgSO4 x 7 H2O`, 250 g NaCl, 0.33 g each of `CaCl2 x 2 H2O`, `KH2PO4`, `NH4Cl`, `MgCl2 x 6 H2O`, and KCl, 0.5 g `Na2S x 9 H2O`, 2.5 g `Na2CO3`, 5 g trimethylamine-HCl, 0.05 g Oxoid yeast extract, 1 ml Trace element solution SL-10, and `CO2`/`N2` gas annotations.
- TOGO `M2647` defines Trace element solution SL-10 as 990 ml distilled water, 36 mg `Na2MoO4 x 2 H2O`, 6 mg `H3BO3`, 100 mg `MnCl2 x 4 H2O`, 190 mg `CoCl2 x 6 H2O`, 24 mg `NiCl2 x 6 H2O`, 2 mg `CuCl2 x 2 H2O`, 70 mg `ZnCl2`, 10 ml 25% 7.7 M HCl, and 1.5 g `FeCl2 x 4 H2O`.
- The repository has a separate MediaDive `mediadive.solution:4178` SL-10 normalized record with stock concentrations matching MediaDive REST `/rest/solution/4178`.
- TOGO `M2647` preserves preparation guidance for SL-10 dissolution order, sparging with 80% `N2` / 20% `CO2` for 30 to 45 min, dispensing and autoclaving under the same gas atmosphere, adding trace elements, yeast extract, trimethylamine, and sulfide from sterile anoxic stocks under 100% `N2`, adding carbonate from a sterile anoxic stock under 80% `N2` / 20% `CO2`, adjusting the complete medium to pH 7.4 with 5% w/v `Na2CO3` if necessary, and retaining the white-precipitate storage note.

## Completeness

The main salt rows, TOGO identity, and high-salt classification are present. The recipe is not complete for reconstruction because SL-10 has been both flattened into top-level ingredients and left as an empty `Unknown solution`, resazurin is another empty `Unknown solution`, stock-water volume has been summed with main-water volume, and all source preparation comments were dropped.

## Findings

- The SL-10 stock was flattened with severe unit errors. Source milligram stock components are stored as gram-per-liter main-medium components: 36 mg `Na2MoO4 x 2 H2O` became `36 G_PER_L`, 6 mg `H3BO3` became `6 G_PER_L`, 100 mg `MnCl2 x 4 H2O` became `100 G_PER_L`, and similarly for cobalt, nickel, copper, and zinc. Since only 1 ml of SL-10 is added per liter-scale medium, these values are not source amounts or final concentrations.
- The stock hierarchy is internally contradictory. The YAML has top-level SL-10 component rows and still has a `Trace element solution SL-10` entry with `composition: []`, `name: Unknown solution`, and `1 G_PER_L`, so the recipe cannot tell whether the stock was expanded, referenced, or applied volumetrically.
- The `Na-resazurin solution (0.1% w/v)` addition was converted from a 0.5 ml stock addition into an empty `Unknown solution` with `0.5 G_PER_L`, losing both the stock strength and its volume.
- Stock and main solvent rows were summed. The generated `Distilled water` row is `1990 G_PER_L` with a duplicate-merge note for `1000.0` and `990.0`, which merged the main-medium water with SL-10 stock water instead of keeping them in separate formula scopes.
- The 10 ml 25% HCl row from SL-10 was imported as `10 G_PER_L` with no ontology grounding and no indication that it is part of the stock-acid solvent, not a direct main-medium component.
- Preparation conditions are absent. The source's gas mixture, sparging duration, 100% `N2` stock atmosphere, carbonate stock atmosphere, pH 7.4 adjustment, SL-10 mixing order, and storage note are needed to reproduce the DSMZ/TOGO protocol but are not represented in the YAML.

## Recommended Edits

- Replace the flattened SL-10 top-level ingredients with a structured `Trace element solution SL-10` stock or a direct reference to `mediadive.solution:4178`; preserve the source 1 ml addition in the main formula.
- Preserve `Na-resazurin solution (0.1% w/v)` as a 0.5 ml stock addition instead of an empty gram-per-liter placeholder.
- Keep 1000 ml main water and 990 ml SL-10 water scoped to their own formula blocks and prevent duplicate cleanup from summing them.
- Reattach TOGO preparation comments to the normalized recipe, including the gas ratios, pH 7.4 final adjustment, stock atmospheres, and the precipitate note.
- Add an explicit curation note that the live DSMZ 375 recipe has drifted from the archived TOGO `M2647` payload before deciding whether this record should stay TOGO-based or be superseded by a fresh DSMZ/MediaDive import.
- Regenerate `data/merge_yaml/merged/methanohalobium_medium__77d07e5a.yaml` from the curated normalized owner.

## Follow-up Checks

- Re-run open, strict, reference, and term validation after regeneration.
- Compare the regenerated record against TOGO `M2647` and confirm that the 1 ml SL-10 addition and the 0.5 ml 0.1% sodium-resazurin addition survive as stock invocations.
- Compare TOGO `M2647` with the current DSMZ 375 PDF and decide whether revision drift requires a separate issue or an explicit source-version annotation.

## Additional Notes

None found
