# YAML Record Review: halomonas_cug_medium__4aa6fdd3

- Repository: CultureMech
- Record: `data/merge_yaml/merged/halomonas_cug_medium__4aa6fdd3.yaml`
- Started UTC: 2026-09-23T10:31:35Z
- Finished UTC: 2026-09-23T10:32:28Z
- Verdict: needs curation

## Target

Generated merged YAML for TOGO `M1117`, the 15 g/L agar solid-medium variant of JCM medium 1050.

## Validation

- LinkML validation: passed for target class `MediaRecipe`.
- Strict validation: passed; `/private/tmp/halomonas_cug_medium__4aa6fdd3.strict.tsv` contained only the header row.
- Reference validation: passed with 0 checked references.
- Term validation: passed.
- Embedded history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The record identity matches TOGO `M1117`, original source `JCM_M1050-2`, and the historical JCM 1050 URL.
- JCM now returns no composition for medium 1050, but both MediaDive `J1050` and the TOGO M1116/M1117 archived payloads preserve the formula.
- A gitignore-independent exact search for `TOGO:M1116`, `TOGO:M1117`, `JCM_M1050`, and `GRMD=1050` found the direct JCM import, the TOGO liquid parse, the TOGO solid parse, and their expected normalized source files.
- Hydrated calcium and magnesium salts are grounded correctly.

## Evidence

- MediaDive `J1050` and TOGO `M1116`/`M1117` agree on the base components, pH 7.5, and final 1000 ml water volume.
- TOGO `M1117` represents the solid-medium form by adding 15 g/L agar, matching the archived TOGO comment from JCM 1050.
- The generated solid record preserves the base ingredient masses, the BD-Difco Casamino acids qualifier, and the 15 g/L agar row.

## Completeness

- Missing pH: TOGO M1117 carries `ph: 7.5`, but the generated solid record has no `ph_value`.
- The 1000 ml distilled-water row is represented as `1 G_PER_L`.
- Missing preparation: the generated record has no pH-adjustment or sterilization steps.
- Missing relationship: the M1117 solid variant is split from the M1116 liquid base and the direct MediaDive/JCM J1050 record.

## Findings

1. The record dropped pH 7.5 from the source.
2. The generated `Distilled water` row uses `1 G_PER_L` instead of the source 1 L final-volume solvent.
3. The archived source instruction to mix thoroughly, adjust pH to 7.5, and make the solid variant with 15 g/L agar is not represented as structured preparation or a variant relationship.
4. The generated record is isolated from the liquid M1116 and direct JCM J1050 forms of the same medium.

## Recommended Edits

- Add `ph_value: 7.5`.
- Replace the `1 G_PER_L` water artifact with the correct 1000 ml final-volume solvent representation.
- Add pH-adjustment and default JCM sterilization semantics.
- Link this solid agar form to the corresponding liquid base recipe.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation after curation.
- Verify that agar remains 15 g/L only on the solid variant and is absent from the liquid base recipe.
- Re-run an ignored-file-inclusive exact search for `TOGO:M1116`, `TOGO:M1117`, and `mediadive.medium:J1050` after regeneration.

## Additional Notes

- Empty optional fields were not treated as defects.
- Exact local searches used `rg --no-ignore --hidden`, so ignored files were included.
