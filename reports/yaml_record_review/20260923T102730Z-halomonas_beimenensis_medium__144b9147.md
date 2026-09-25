# YAML Record Review: halomonas_beimenensis_medium__144b9147

- Repository: CultureMech
- Record: `data/merge_yaml/merged/halomonas_beimenensis_medium__144b9147.yaml`
- Started UTC: 2026-09-23T10:27:30Z
- Finished UTC: 2026-09-23T10:28:34Z
- Verdict: needs curation

## Target

Generated merged YAML for TOGO `M800`, the 18 g/L agar solid-medium variant parsed from JCM medium 771.

## Validation

- LinkML validation: passed for target class `MediaRecipe`.
- Strict validation: passed with 0 error rows.
- Reference validation: passed with 0 checked references.
- Term validation: passed.
- Embedded history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The record identity matches TOGO `M800`, original source `JCM_M771-2`, and the JCM 771 source page.
- A gitignore-independent exact search for `TOGO:M799`, `TOGO:M800`, `JCM_M771`, and `JCM_M771-2` found the expected liquid and solid TOGO parses plus their generated merged records.
- MgSO4 7H2O, KCl, NaCl, sodium glutamate, agar, and undefined BD-Difco complex ingredients are grounded or ungrounded appropriately.
- `Trisodium citrate` is grounded to generic sodium citrate; this may be acceptable if no trisodium-citrate-specific term is available, but should be checked during curation.

## Evidence

- JCM 771 lists 5 g Casamino acids (BD-Difco), 5 g Yeast extract (BD-Difco), 1 g Sodium glutamate, 3 g Trisodium citrate, 5 g MgSO4 x 7H2O, 2 g KCl, and 50 g NaCl, then instructs curators to bring the recipe to 1.0 L with distilled water.
- JCM separately states that 18.0 g/L agar should be added to prepare solid medium.
- TOGO `M799` parses the base recipe and TOGO `M800` parses the agar-containing solid variant from the same JCM page.

## Completeness

- Missing preparation: the generated record has no explicit final-volume, pH, or sterilization steps.
- Water is present as `1 G_PER_L`, a TOGO artifact for the 1.0 L distilled-water final volume.
- Missing relationship: the M800 solid variant is split from the M799 liquid base recipe.

## Findings

1. The `Distilled water` ingredient has the wrong unit. The source says to bring the medium to 1.0 L, not to add 1 g/L water.
2. The JCM preparation semantics were not converted into `preparation_steps`; both the 1.0 L final volume and default 121 C for 15 min autoclaving are absent.
3. The solid agar recipe is not linked to TOGO `M799` as the solid form of the same JCM 771 recipe.

## Recommended Edits

- Replace the `1 G_PER_L` water row with a correct final-volume solvent representation.
- Add preparation steps for bringing the medium to 1.0 L and JCM default autoclaving.
- Link TOGO `M800` to TOGO `M799` as the solid agar variant.
- Check whether trisodium citrate can be grounded more specifically than generic sodium citrate.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation after curation.
- Verify that M800 keeps `physical_state: SOLID_AGAR` and agar at exactly 18.0 g/L.
- Re-run an ignored-file-inclusive exact search for `TOGO:M799`, `TOGO:M800`, and `JCM_M771` to confirm the liquid and solid records are consistently regenerated.

## Additional Notes

- Empty optional fields were not treated as defects.
- Exact local searches used `rg --no-ignore --hidden`, so ignored files were included.
