# YAML Record Review: dg18_dichloran_18_glycerol_agar

- Repository: CultureMech
- Record: `data/merge_yaml/merged/dg18_dichloran_18_glycerol_agar__59d0b17f.yaml`
- Started UTC: 2026-09-22T21:57:32Z
- Finished UTC: 2026-09-22T21:58:00Z
- Verdict: pass with minor issues

## Target

`CultureMech:001234` represents DSMZ Medium 1775, `DG18 Dichloran 18 % Glycerol agar`, from MediaDive. The generated record is a single-source merge from `data/normalized_yaml/bacterial/dg18_dichloran_18_glycerol_agar.yaml`.

## Validation

- LinkML open-world validation passed.
- Strict CultureMech validation passed with zero error rows.
- Reference validation passed with zero checks.
- LinkML term validation passed.
- Embedded curation history was not checked: `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged YAML.

## Identity and Grounding

A gitignore-independent `find` over `data/` found this DSMZ 1775/MediaDive fingerprint, a separate TOGO M1931/NBRC generated fingerprint, and their two normalized sources. DSMZ 1775 should stay separate from the TOGO/NBRC DG18 recipe because it uses a commercial `Dichloran-Glycerol-agar base` plus zinc and copper amendments instead of the fully expanded NBRC peptone, glucose, KH2PO4, MgSO4, dichloran, chloramphenicol, and agar formula.

## Evidence

- The live MediaDive 1775 payload defines `Main sol. 1775` as a 1000 ml solution with 31.5 g Dichloran-Glycerol-agar base, 220 g glycerol, 0.01 g ZnSO4 x 7 H2O, 5 mg CuSO4 x 5 H2O, and 1000 ml distilled water.
- MediaDive converts the 5 mg CuSO4 x 5 H2O row to 0.005 g/l, which matches the generated `0.005 G_PER_L` value.
- The MediaDive step says to adjust pH to 5.6 and sterilize at 121 C for 15 min; the generated preparation step preserves that instruction.
- The sibling TOGO M1931 record points to NBRC Medium 1198 and expands a different DG18 formulation, so the two `dg18_dichloran_18_glycerol_agar` fingerprints are appropriately distinct.

## Completeness

The core DSMZ 1775 formula is represented, but the 1000 ml water row from the source is absent and the generated literature reference appears stale relative to the current MediaDive 1775 metadata.

## Findings

- `Distilled water`, 1000 ml, is present in the live MediaDive recipe but absent from the generated record.
- The generated reference cites Samson et al. 2019, while the current MediaDive 1775 `description` cites Hocking and Pitt 1980 for Dichloran-glycerol medium.

## Recommended Edits

- Add or intentionally omit the 1000 ml distilled-water row according to the current CultureMech water-handling convention, and document that choice in the curation history.
- Refresh the DSMZ 1775 source metadata so the generated reference agrees with the current MediaDive source.

## Follow-up Checks

- Re-run open-world, strict, reference, and term validation after any normalization change and regeneration.
- Verify that DSMZ 1775 and TOGO M1931 still emit as distinct generated variants.
- Verify that the generated reference is source-backed after the MediaDive metadata refresh.

## Additional Notes

None found.
