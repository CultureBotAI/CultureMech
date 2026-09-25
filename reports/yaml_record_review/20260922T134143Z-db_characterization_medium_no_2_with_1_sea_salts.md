# YAML Record Review: db_characterization_medium_no_2_with_1_sea_salts

- Repository: CultureMech
- Record: data/merge_yaml/merged/db_characterization_medium_no_2_with_1_sea_salts.yaml
- Started UTC: 2026-09-22T13:39:20Z
- Finished UTC: 2026-09-22T13:41:43Z
- Verdict: needs curation

## Target

Reviewed generated record `data/merge_yaml/merged/db_characterization_medium_no_2_with_1_sea_salts.yaml` with generated identifier `CultureMech:007646`, media term `TOGO:M1125`, original name `DB Characterization Medium NO.2 With 1% Sea Salts`, category `bacterial`, and one merged source, `TOGO_M1125_DB_Characterization_Medium_NO.2_With_1_Sea_Salts`.

## Validation

- LinkML open-schema validation: passed.
- Strict validation: passed with 0 error rows in `/private/tmp/db_characterization_medium_no_2_with_1_sea_salts.strict.tsv`.
- Reference validation: passed with 0 references checked.
- Term validation: passed.
- Embedded curation history: not checked; `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` blocks.

## Identity and Grounding

TOGO M1125 maps directly to JCM Medium 1058, `DB CHARACTERIZATION MEDIUM NO.2 WITH 1% SEA SALTS`. The source recipe is intentionally terse: both TOGO and JCM say to use DB Characterization Medium No. 2 / JCM 574 and supplement it with 10.0 g/L sea salts (Sigma).

The generated record is stale relative to its maintained source. `data/normalized_yaml/bacterial/TOGO_M1125_DB_Characterization_Medium_NO.2_With_1_Sea_Salts.yaml` was repaired in September 2026 to keep the JCM 574 base as a `1000 ML_PER_L` `solutions` reference, preserve JCM 1058/JCM 574 references, add a preparation step, mark salinity, and record `SUPPLEMENTED_VARIANT` parentage.

An exact gitignore-independent search for `M1125`, `JCM_M1058`, `GRMD=1058`, and `db_characterization_medium_no_2_with_1_sea_salts` across normalized YAML, merged YAML, and prior YAML record reviews found this TOGO owner, the direct JCM 1058 owner, and two generated sibling records that still split the same JCM 1058 concept.

## Evidence

JCM GRMD 1058 contains one instruction: use Medium 574 supplemented with 10.0 g/L sea salts (Sigma). TOGO M1125 has the same model as `sea salts (Sigma)` at 10 `g/L` plus `DB CHARACTERIZATION MEDIUM NO. 2 (see Medium [M578])` at 1 `L`.

## Completeness

The generated target has the 10 g/L sea salts row, but it still encodes the 1 L M578 base as an empty `Unknown solution` with `1 G_PER_L`; it also lacks the maintained source's `ML_PER_L` unit, CultureMech base-medium link, salinity, preparation step, parent-media relationship, data-quality flags, and explicit references.

## Findings

1. **The base-medium volume is in the wrong unit and is unresolved.** TOGO M1125/JCM 1058 use 1 L of DB Characterization Medium No. 2 as the base. The generated YAML stores that cross-reference as an empty solution named `Unknown solution` at `1 G_PER_L` rather than a 1000 ml/L parent-medium addition.

2. **The generated record is stale relative to the repaired normalized source.** The maintained TOGO source has 2026-09-05 and 2026-09-10 curation events resolving the JCM cross-reference as a typed `SUPPLEMENTED_VARIANT` and a `CultureMech:009974` solution reference; none of that repair is present in the generated record.

3. **The same JCM 1058 medium remains split in generated output.** The exact search found the direct JCM 1058 path emitted separately as `db_characterization_medium_no_2_with_1_sea_salts__65dd27c4.yaml`, while this generated record represents the TOGO M1125 mirror of that same source.

## Recommended Edits

- Regenerate this target from `data/normalized_yaml/bacterial/TOGO_M1125_DB_Characterization_Medium_NO.2_With_1_Sea_Salts.yaml` so the base medium is represented as `1000 ML_PER_L` of `CultureMech:009974`, not an empty `1 G_PER_L` unknown solution.
- Merge or otherwise reconcile the TOGO M1125 and direct JCM 1058 generated outputs once both owners use the same parent-medium model.
- Preserve the JCM 1058 and JCM 574 references, salinity, `SUPPLEMENTED_VARIANT` parentage, and preparation step in the regenerated record.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Re-review the sibling `db_characterization_medium_no_2_with_1_sea_salts__65dd27c4.yaml` because it currently expands the older direct JCM 1058 import instead of sharing this repaired compact representation.

## Additional Notes

The review used gitignore-independent `rg --no-ignore --hidden` searches for `M1125`, `JCM_M1058`, `GRMD=1058`, and `db_characterization_medium_no_2_with_1_sea_salts`, so ignored files were included in the duplicate/source scan.
