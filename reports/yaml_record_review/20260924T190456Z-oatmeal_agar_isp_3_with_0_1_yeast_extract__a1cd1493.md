# YAML Record Review: oatmeal_agar_isp_3_with_0_1_yeast_extract

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/oatmeal_agar_isp_3_with_0_1_yeast_extract__a1cd1493.yaml
- Started UTC: 2026-09-24T19:04:29Z
- Finished UTC: 2026-09-24T19:04:56Z
- Verdict: needs curation

## Target

- Generated record: `data/merge_yaml/merged/oatmeal_agar_isp_3_with_0_1_yeast_extract__a1cd1493.yaml`
- Maintained owners:
  - `data/normalized_yaml/fungal/oatmeal_agar_isp_3_with_0_1_yeast_extract.yaml`
  - `data/normalized_yaml/fungal/inorganic_salts_starch_agar_isp_4_with_0_05_yeast_extract.yaml`
- Class: `MediaRecipe`
- ID: `CultureMech:010531`
- Label: `oatmeal_agar_isp_3_with_0_1_yeast_extract`
- Source grounding: `mediadive.medium:J51`, imported from JCM medium 51
- Inspected related source URLs:
  - `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=51`
  - `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=217`
- Merge state: generated from two source recipes, `inorganic_salts_starch_agar_isp_4_with_0_05_yeast_extract` and `oatmeal_agar_isp_3_with_0_1_yeast_extract`

## Validation

All focused validators passed for the generated YAML.

| Check | Command | Result |
| --- | --- | --- |
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/oatmeal_agar_isp_3_with_0_1_yeast_extract__a1cd1493.yaml` | Passed with `No issues found`. |
| Strict schema wrapper | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/oatmeal_agar_isp_3_with_0_1_yeast_extract__a1cd1493.yaml --out /private/tmp/oatmeal_agar_isp_3_with_0_1_yeast_extract__a1cd1493.strict.tsv --workers 1 --quiet` | Passed; the output TSV had the header only, 1 line and 0 error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/oatmeal_agar_isp_3_with_0_1_yeast_extract__a1cd1493.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 reference checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/oatmeal_agar_isp_3_with_0_1_yeast_extract__a1cd1493.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils` deprecation warning. |
| Embedded history | Not run | Not checked: the available `just validate-history` target validates standalone `history/`, not embedded `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

The generated record is a wrong-identity merge. It is grounded to JCM medium 51, Oatmeal Agar (ISP-3) With 0.1% Yeast Extract, but it also merged JCM medium 217, Inorganic Salts-Starch Agar (ISP-4) With 0.05% Yeast Extract.

The inspected JCM pages show different base media and different yeast-extract masses. JCM 51 uses 1 L Oatmeal agar (ISP-3), JCM medium 50, plus 1.0 g Yeast extract (BD-Difco). JCM 217 uses 1 L Inorganic salts-starch agar (ISP-4), JCM medium 58, plus 0.5 g Yeast extract.

## Evidence

The two maintained fungal owners were repaired in September 2026 to model those different base media as 1000 ml `solutions` with `CultureMech` parent links and to preserve the JCM source masses. The generated August record predates that repair and collapsed the two official-simple recipes because both old imports looked like a base-medium row plus yeast extract.

An ignored-inclusive exact search over `data`, `src`, `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the JCM 51 owner, the JCM 217 owner, their bacterial TOGO counterparts, the repair scripts that touched both official-simple records, and the generated merge that currently conflates the two fungal direct imports.

## Completeness

The generated record is missing both repaired parent-solution links. It stores `Inorganic salts-starch agar` as `1000 G_PER_L` under `ingredients`, grounds that base medium row to CHEBI agar, and has no representation of the 1 L Oatmeal agar ISP-3 base required by JCM 51.

The repaired maintained JCM 51 and JCM 217 records already contain their source references, `MIX` steps, `SUPPLEMENTED_VARIANT` parent links, and quality flags. Those are absent from the generated YAML because it has not been regenerated.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Blocker | The generated record merges JCM 51 and JCM 217, which are different media. | `merged_from` contains both same-stem direct JCM sources; JCM 51 uses Oatmeal Agar ISP-3 plus 1.0 g yeast extract, while JCM 217 uses Inorganic Salts-Starch Agar ISP-4 plus 0.5 g yeast extract. | Regenerate from repaired source records and prevent official-simple base-media collisions |
| Major | The JCM 51 yeast-extract amount is wrong in the canonical generated record. | JCM 51 lists 1.0 g Yeast extract (BD-Difco), but the generated JCM 51 record carries the 0.5 g amount from JCM 217. | Regenerate from `data/normalized_yaml/fungal/oatmeal_agar_isp_3_with_0_1_yeast_extract.yaml` |
| Major | The JCM 217 base-medium row is mis-modeled as a CHEBI-grounded agar ingredient. | JCM 217 adds 1 L Inorganic Salts-Starch Agar ISP-4 from JCM 58; the generated record stores `Inorganic salts-starch agar` as `1000 G_PER_L` and links it to CHEBI agar. | Regenerate from `data/normalized_yaml/fungal/inorganic_salts_starch_agar_isp_4_with_0_05_yeast_extract.yaml` |
| Major | `kg_microbe_match` points at the wrong medium. | Both repaired fungal parents still carry `kg_microbe_match: mediadive.medium:12`, and MediaDive medium 12 is Soil Extract Medium. | Both maintained fungal parents |

## Recommended Edits

1. Regenerate merged YAML from the repaired fungal JCM 51 and JCM 217 owners so these different official-simple variants no longer merge together.
2. Add a merge guard that includes official-simple base media in the fingerprint rather than reducing both recipes to a sparse yeast-extract signature.
3. Remove `kg_microbe_match: mediadive.medium:12` from the JCM 51 and JCM 217 direct fungal owners.

## Follow-up Checks

- Rerun LinkML schema, strict schema, term, and reference validation on the regenerated JCM 51 and JCM 217 records.
- Rerun an ignored-inclusive exact search for `mediadive.medium:J51`, `GRMD=51`, `mediadive.medium:J217`, `GRMD=217`, and both same-stem filenames to confirm the direct fungal imports no longer collide.
- Manually compare the regenerated JCM 51 and JCM 217 records against their JCM pages and confirm each has the correct 1 L base medium and yeast-extract mass.

## Additional Notes

The related bacterial TOGO owners for these official-simple variants were also repaired after this generated August merge. Regeneration should be validated across both direct JCM and TOGO copies so each official-simple recipe chooses the right base medium and avoids same-stem filename collisions.
