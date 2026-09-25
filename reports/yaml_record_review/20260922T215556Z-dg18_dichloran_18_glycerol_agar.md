# YAML Record Review: dg18_dichloran_18_glycerol_agar

- Repository: CultureMech
- Record: `data/merge_yaml/merged/dg18_dichloran_18_glycerol_agar.yaml`
- Started UTC: 2026-09-22T21:53:30Z
- Finished UTC: 2026-09-22T21:55:56Z
- Verdict: needs curation

## Target

`CultureMech:008510` represents TOGO Medium M1931, `DG18: Dichloran 18% Glycerol Agar`, imported from NBRC Medium 1198. The generated record is a single-source merge from `data/normalized_yaml/bacterial/TOGO_M1931_DG18_Dichloran_18_Glycerol_Agar.yaml`.

## Validation

- LinkML open-world validation passed.
- Strict CultureMech validation passed with zero error rows.
- Reference validation passed with zero checks.
- LinkML term validation passed.
- Embedded curation history was not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged YAML.

## Identity and Grounding

TOGO M1931 points back to NBRC Medium 1198. A gitignore-independent `find` over `data/` found this TOGO M1931 record, a separate DSMZ 1775/MediaDive generated fingerprint, and their two normalized sources; the two sources both normalize to `dg18_dichloran_18_glycerol_agar` but should stay separate because DSMZ 1775 uses a commercial Dichloran-Glycerol-agar base with zinc and copper additions.

## Evidence

- The live TOGO M1931 API lists 1 L distilled water, 5 g peptone, 10 g glucose, 1 g KH2PO4, 0.5 g MgSO4 x 7 H2O, 1 ml Dichloran at 0.2% in ethanol, 220 g glycerol, 0.1 g chloramphenicol, and 15 g agar.
- The live NBRC 1198 page lists the same DG18 composition and the same 1.0 ml dichloran-in-ethanol addition.
- TOGO preserves the NBRC preparation text: add minor ingredients and agar to about 800 ml distilled water, steam to dissolve agar, make to one liter with distilled water, add 220 g glycerol, autoclave at 121 C for 15 min, and finish at water activity 0.955 and pH 5.6 +/- 0.2.
- TOGO stores a pH range of 5.4 to 5.8, matching the NBRC final-pH text.
- DSMZ 1775 is a different DG18 record with 31.5 g/l Dichloran-Glycerol-agar base, 220 g/l glycerol, 0.01 g/l ZnSO4 x 7 H2O, 0.005 g/l CuSO4 x 5 H2O, 1000 ml distilled water, and pH 5.6.

## Completeness

The record is incomplete because the TOGO/NBRC pH range and preparation text were dropped. The source milliliter dichloran addition and liter water volume were also represented as gram-per-liter concentrations.

## Findings

- The source pH range, `5.4 - 5.8`, is absent from the generated record.
- `Dichloran (0.2% in ethanol)` is stored as `1 G_PER_L`, but the source adds 1 ml of a 0.2% solution in ethanol.
- `Distilled water` is stored as `1 G_PER_L`, but the source row is 1 L final-volume water.
- The steaming, one-liter make-up, glycerol addition, autoclaving, final water activity, and final pH preparation text is absent.
- The useful source comment about a commercial Dichloran glycerol agar base is absent.
- The generated record is stale relative to the normalized TOGO source, which gained a chloramphenicol CHEBI grounding in August.

## Recommended Edits

- Preserve the TOGO pH range as 5.4 to 5.8 or the equivalent final pH 5.6 +/- 0.2 range from NBRC.
- Represent 1 ml `Dichloran (0.2% in ethanol)` as a volume addition or source-backed stock addition, not as `1 G_PER_L`.
- Represent distilled water as the one-liter make-up volume instead of a gram-per-liter solute.
- Convert the TOGO/NBRC preparation text into scoped preparation steps.
- Regenerate the merged record after the normalized chloramphenicol grounding is propagated.
- Keep this TOGO M1931/NBRC 1198 formula distinct from the DSMZ 1775 commercial-base formula.

## Follow-up Checks

- Re-run open-world, strict, reference, and term validation after normalization changes and regeneration.
- Verify that no source milliliter or liter volume remains as a gram-per-liter concentration.
- Verify that the regenerated record carries a pH range of 5.4 to 5.8.
- Verify that the NBRC steaming, make-up, glycerol, autoclave, water-activity, and pH instructions are present.
- Verify that the TOGO/NBRC and DSMZ DG18 records still emit as distinct generated variants.

## Additional Notes

None found.
