# YAML Record Review: db_characterization_medium_no_2_with_1_sea_salts

- Repository: CultureMech
- Record: data/merge_yaml/merged/db_characterization_medium_no_2_with_1_sea_salts__65dd27c4.yaml
- Started UTC: 2026-09-22T13:41:43Z
- Finished UTC: 2026-09-22T13:44:40Z
- Verdict: needs curation

## Target

Reviewed generated record `data/merge_yaml/merged/db_characterization_medium_no_2_with_1_sea_salts__65dd27c4.yaml` with generated identifier `CultureMech:002239`, media term `mediadive.medium:J1058`, original name `DB CHARACTERIZATION MEDIUM NO.2 WITH 1% SEA SALTS`, category `bacterial`, and two merged sources, `db_characterization_medium_no_2` and `db_characterization_medium_no_2_with_1_sea_salts`.

## Validation

- LinkML open-schema validation: passed.
- Strict validation: passed with 0 error rows in `/private/tmp/db_characterization_medium_no_2_with_1_sea_salts__65dd27c4.strict.tsv`.
- Reference validation: passed with 0 references checked.
- Term validation: passed.
- Embedded curation history: not checked; `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` blocks.

## Identity and Grounding

JCM GRMD 1058 is `DB CHARACTERIZATION MEDIUM NO.2 WITH 1% SEA SALTS`. The entire source recipe is a reference to JCM Medium 574 plus a differentiating supplement: use Medium 574 supplemented with 10.0 g/L sea salts (Sigma).

The generated identity is only partially grounded. Its media term points to JCM 1058, but its formula does not contain the 10 g/L sea-salts supplement and its merge history shows that it false-merged the unsupplemented JCM 574 base record `db_characterization_medium_no_2` with the JCM 1058 variant.

An exact gitignore-independent search for `mediadive.medium:J1058`, `mediadive.medium:J574`, `GRMD=1058`, and `db_characterization_medium_no_2_with_1_sea_salts` across normalized YAML, merged YAML, and prior YAML record reviews found the direct JCM 1058 owner, the unsupplemented direct JCM 574 owner, the repaired TOGO M1125 mirror, this false-merged generated target, and the split TOGO M1125 generated sibling.

## Evidence

JCM 1058 says only to use Medium 574 supplemented with 10.0 g/L sea salts (Sigma). The maintained direct JCM source records that it resolved a reference by copying 30 ingredients from `CultureMech:002922` / JCM 574, but it has no ingredient row for sea salts (Sigma). The generated merge therefore inherited an already-underdetermined expansion and then collapsed it back together with the unsupplemented JCM 574 base.

## Completeness

The generated record has a large copied JCM 574 formula and a one-step preparation note copied from JCM 1058, but it omits the defining 10 g/L sea-salts supplement. It also inherits the older direct JCM 574 flattening model, which represents MDS salt-water, potassium-phosphate-buffer, vitamin-stock, and trace-element stock constituents as if they were direct final-medium ingredients.

## Findings

1. **The 1% sea-salts supplement is missing.** JCM 1058 differs from JCM 574 by 10.0 g/L sea salts (Sigma). Neither `data/normalized_yaml/bacterial/db_characterization_medium_no_2_with_1_sea_salts.yaml` nor this generated target contains that row.

2. **A supplemented variant was false-merged with its parent.** The generated record merged `db_characterization_medium_no_2.yaml` / JCM 574 and `db_characterization_medium_no_2_with_1_sea_salts.yaml` / JCM 1058 as duplicate recipes. Those media are not duplicates once the 10 g/L sea-salts supplement is represented.

3. **The same JCM 1058 medium remains split.** TOGO M1125 is a mirror of JCM 1058 and has a repaired normalized source, but it is emitted separately as `db_characterization_medium_no_2_with_1_sea_salts.yaml`.

4. **Copied base-medium contents are over-flattened.** The JCM 574 base is a staged medium with MDS salt water, potassium phosphate buffer, and vitamin solution stocks. This generated output expands the older direct JCM 574 import as 29 final `G_PER_L` ingredients rather than preserving final stock-addition volumes and nested stock recipes.

## Recommended Edits

- Add the 10.0 g/L sea-salts supplement to `data/normalized_yaml/bacterial/db_characterization_medium_no_2_with_1_sea_salts.yaml`, or replace that direct JCM path with a `CultureMech:009974` parent-medium reference matching the repaired TOGO M1125 record.
- Prevent JCM 1058 from merging with the unsupplemented JCM 574 base.
- Merge or reconcile the direct JCM 1058 and TOGO M1125 outputs after both carry the same parent-medium-plus-sea-salts representation.
- Repair the underlying JCM 574 base representation so any expanded child uses correctly scoped stocks and final ml/L additions.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regenerating the two JCM 1058 outputs.
- Confirm the regenerated output contains exactly one JCM 1058/TOGO M1125 record, has 10 g/L sea salts, and no longer lists `db_characterization_medium_no_2` as a duplicate `merged_from` source.

## Additional Notes

The review used gitignore-independent `rg --no-ignore --hidden` searches for `mediadive.medium:J1058`, `mediadive.medium:J574`, `GRMD=1058`, and `db_characterization_medium_no_2_with_1_sea_salts`, so ignored files were included in the duplicate/source scan.
