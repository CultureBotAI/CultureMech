# YAML Record Review: acidified_mpob_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/ACIDIFIED_MPOB_MEDIUM.yaml`
- Started UTC: 2026-09-21T08:59:19Z
- Finished UTC: 2026-09-21T09:00:42Z
- Verdict: needs curation

## Target

Generated merge record `ACIDIFIED_MPOB_MEDIUM.yaml` is a singleton merge from `data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml`. It represents TOGO M1134, whose original source is JCM Medium 1065 / ACIDIFIED MPOB MEDIUM.

## Validation

- PASS: open LinkML schema validation with `linkml-validate`.
- PASS: strict schema layer validation with `scripts/validate_strict.py`.
- PASS: linkml-reference-validator on this generated record.
- PASS: linkml-term-validator on this generated record.
- Not checked: embedded `MediaRecipe.curation_history` entries; no focused generated-record history validator is documented, and `just validate-history` targets standalone `history/` files.

## Identity and Grounding

The TOGO and direct JCM identities agree. TOGO M1134 reports `original_media_id: JCM_M1065` and the same `GRMD=1065` URL used by the direct `mediadive.medium:J1065` normalized source. An ignored-inclusive exact source-ID search found one TOGO M1134 normalized source and one direct JCM J1065 normalized source, but they generated separately as `ACIDIFIED_MPOB_MEDIUM.yaml` and `acidified_mpob_medium__51005bb3.yaml`.

The six stock-solution rows are also source-grounded as JCM cross-references or molar/percent stock additions: JCM 1065 points FeCl2 and trace elements at JCM Medium 187, trace vitamins at JCM Medium 197, and lists the 1 M glycerin, 1 M K2HPO4, and 5% L-cysteine solutions as post-autoclave additions.

## Evidence

- Primary JCM source `GRMD=1065`: source page fetched from JCM during review. It lists NH4Cl, Na2SO4, CaCl2.2H2O, MgCl2.6H2O, NaCl, 1 ml FeCl2 solution, 1 ml trace element solution, 0.2 g yeast extract, 10 ml trace vitamins, 0.5 mg resazurin, and 1 L distilled water, followed by anaerobic autoclaving under N2-CO2 and 5 ml / 5 ml / 10 ml post-cooling additions of K2HPO4, glycerin, and L-cysteine solutions.
- TOGO source M1134: API record fetched during review. It preserves the `GRMD=1065` provenance, gas-mix comment, three cross-referenced solution rows, and three post-cooling stock-solution rows before CultureMech normalization moves all six stock additions into empty `solutions`.
- Direct JCM normalized record `data/normalized_yaml/bacterial/acidified_mpob_medium.yaml`: carries the same source URL and the anaerobic preparation text, but it flattens the stock solutions into top-level final ingredients and therefore fingerprints separately from TOGO M1134.

## Completeness

The generated target preserves the simple gram-scale basal salts and the yeast extract amount, but it is incomplete for every solution addition. The six stock rows survive only as empty `solutions` whose numeric values are the source milliliter volumes with `G_PER_L` units.

The target also lacks the source preparation step. It retains nitrogen and carbon dioxide as variable ingredients, but it does not say to bubble with an 80:20 N2-CO2 gas mixture, seal with a butyl rubber stopper, autoclave under that gas mixture, and add the final solutions aseptically and anaerobically after cooling.

## Findings

- CRITICAL: All six liquid additions use invalid mass-concentration units and empty solution compositions. The generated `FeCl2 solution`, `Trace element solution`, `Trace vitamins`, `1 M Glycerin solution`, `1 M K2HPO4 solution`, and `5% L--Cysteine.HCl.H2O solution` entries should be 1, 1, 10, 5, 5, and 10 ml additions, not 1, 1, 10, 5, 5, and 10 `G_PER_L`.
- MAJOR: The TOGO M1134 source and the direct JCM J1065 source are split into two generated records for the same `GRMD=1065` recipe. The direct import has the preparation text but flattens all stock solutions; the TOGO import keeps solution labels but drops the preparation text and uses malformed units.
- MAJOR: `Resazurin 0.5 mg` was imported as `0.5 G_PER_L` instead of 0.0005 g per liter.
- MAJOR: The anaerobic gas handling was reduced to variable `Carbon dioxide gas` and `Nitrogen gas` ingredients. The generated record loses the source's 80:20 ratio, N2 atmosphere for separately autoclaved stocks, stopper sealing, and anaerobic post-cooling addition requirements.
- MINOR: `Distilled water 1 L` was stored as `1 G_PER_L`; if water rows are retained, their unit should not be a mass concentration.

## Recommended Edits

- Re-curate `data/normalized_yaml/bacterial/TOGO_M1134_Acidified_MPOB_Medium.yaml` with stock-preserving `solutions`: FeCl2 and trace elements as 1 ml cross-references to JCM Medium 187 / TOGO M180, trace vitamins as a 10 ml cross-reference to JCM Medium 197 / TOGO M190, 1 M glycerin at 5 ml, 1 M K2HPO4 at 5 ml, and 5% L-cysteine.HCl.H2O at 10 ml.
- Convert the 0.5 mg resazurin row to `0.0005 G_PER_L` or an explicit milligram unit if the schema supports it.
- Restore the JCM/TOGO preparation text for the N2-CO2 80:20 gas mixture, autoclaving under that gas, butyl stopper sealing, and anaerobic post-cooling additions.
- Normalize the direct `data/normalized_yaml/bacterial/acidified_mpob_medium.yaml` source to the same stock-preserving representation and regenerate merged YAML so exact `TOGO:M1134` and exact `mediadive.medium:J1065` merge into one generated record.

## Follow-up Checks

- Run schema, strict, reference, and term validation on both corrected JCM 1065 normalized sources and on the regenerated merge target.
- Re-run an ignored-inclusive exact search for `TOGO:M1134`, `mediadive.medium:J1065`, and `GRMD=1065` to confirm only one generated JCM 1065 recipe remains.
- Verify the regenerated record has no empty `solutions` and no milliliter or milligram source rows represented as `G_PER_L`.

## Additional Notes

The direct JCM import's resazurin conversion is correct and its anaerobic preparation step is worth preserving, but it should not remain a separate generated record for the same JCM 1065 source.
