# YAML Record Review: oatmeal_agar_isp_3_with_0_1_yeast_extract

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/oatmeal_agar_isp_3_with_0_1_yeast_extract.yaml
- Started UTC: 2026-09-24T19:03:07Z
- Finished UTC: 2026-09-24T19:03:48Z
- Verdict: needs curation

## Target

- Generated record: `data/merge_yaml/merged/oatmeal_agar_isp_3_with_0_1_yeast_extract.yaml`
- Maintained bacterial owner: `data/normalized_yaml/bacterial/oatmeal_agar_isp_3_with_0_1_yeast_extract.yaml`
- Badly merged archaeal owner: `data/normalized_yaml/archaea/TOGO_M713_Aerobic_Sulfolobales_Medium_Without_Sulfur.yaml`
- Direct JCM sibling: `data/normalized_yaml/fungal/oatmeal_agar_isp_3_with_0_1_yeast_extract.yaml`
- Class: `MediaRecipe`
- ID: `CultureMech:009825`
- Label: `oatmeal_agar_isp_3_with_0_1_yeast_extract`
- Source grounding: `TOGO:M43`, imported from JCM medium 51
- Inspected source URL: `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=51`
- Merge state: generated from two source recipes, `TOGO_M713_Aerobic_Sulfolobales_Medium_Without_Sulfur` and `oatmeal_agar_isp_3_with_0_1_yeast_extract`

## Validation

All focused validators passed for the generated YAML.

| Check | Command | Result |
| --- | --- | --- |
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/oatmeal_agar_isp_3_with_0_1_yeast_extract.yaml` | Passed with `No issues found`. |
| Strict schema wrapper | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/oatmeal_agar_isp_3_with_0_1_yeast_extract.yaml --out /private/tmp/oatmeal_agar_isp_3_with_0_1_yeast_extract.strict.tsv --workers 1 --quiet` | Passed; the output TSV had the header only, 1 line and 0 error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/oatmeal_agar_isp_3_with_0_1_yeast_extract.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 reference checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/oatmeal_agar_isp_3_with_0_1_yeast_extract.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils` deprecation warning. |
| Embedded history | Not run | Not checked: the available `just validate-history` target validates standalone `history/`, not embedded `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

The generated record is a wrong-identity merge. It is labelled and grounded as the TOGO `M43` copy of JCM medium 51, Oatmeal Agar (ISP-3) With 0.1% Yeast Extract, but it was merged with TOGO `M713`, Aerobic Sulfolobales Medium Without Sulfur, an archaeal medium derived from JCM medium 693.

The two source identities are unrelated. JCM 51 contains 1 L Oatmeal Agar (ISP-3) from JCM 50 plus 1 g Yeast extract (BD-Difco). TOGO M713/JCM 693 contains the Aerobic Sulfolobales Medium salt base from M711/JCM 691, omits elemental sulfur, targets pH 2.5, and has 0.5 g/L yeast extract among many salts.

## Evidence

The live TOGO/JCM sources confirm the split: TOGO M43 lists `Yeast extract (BD-Difco)` at 1 g and an Oatmeal agar ISP-3 reference at 1 L; the JCM 51 page lists the same two rows. TOGO M713 instead lists `Yeast extract (BD-Difco)` at 0.5 g and 1 L `Salt base solution (see Medium [M711])`, with a note to use JCM 691 without sulfur.

An ignored-inclusive exact search over `data`, `src`, `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found three same-stem owners that need to stay distinct or be explicitly reconciled: the repaired bacterial TOGO M43 owner, the repaired archaeal TOGO M713 owner, and a direct fungal JCM 51 import. It also found the stale generated merge that incorrectly combines M43 and M713.

## Completeness

The generated record is missing nearly all of the maintained bacterial M43 recipe: the 1 L Oatmeal Agar (ISP-3) base is represented as an empty `Unknown solution` at `1 G_PER_L`; the JCM 50 base ingredients, trace-salts stock, pH 7.2, preparation steps, `SUPPLEMENTED_VARIANT` parent link, references, curation history, and data-quality flags are absent.

The maintained bacterial owner already restores those details and correctly records the M43 supplement as 1 g/L Yeast extract (BD-Difco) on top of the M42 base. The generated record instead carries the stale 0.5 g/L yeast-extract mass from M713.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Blocker | The generated record merges TOGO M43/JCM 51 with unrelated TOGO M713/JCM 693. | The generated `merged_from` includes both `TOGO_M713_Aerobic_Sulfolobales_Medium_Without_Sulfur` and `oatmeal_agar_isp_3_with_0_1_yeast_extract`, and its `categories` include both `archaea` and `bacterial`; the inspected source identities have different base media, pH values, ingredient sets, and intended formulas. | Regenerate from repaired source records and prevent one-row cross-medium fingerprint collisions |
| Major | The JCM 51 yeast-extract amount is wrong in the generated record. | JCM 51 and TOGO M43 list 1 g Yeast extract (BD-Difco); the generated record has 0.5 g/L from M713. | Regenerate from `data/normalized_yaml/bacterial/oatmeal_agar_isp_3_with_0_1_yeast_extract.yaml` |
| Major | The Oatmeal Agar ISP-3 base is represented as an empty unknown solution with the wrong unit. | JCM 51 adds 1 L of JCM 50 Oatmeal Agar (ISP-3); the generated solution is `Unknown solution`, has empty `composition`, and uses `1 G_PER_L`. | Regenerate from `data/normalized_yaml/bacterial/oatmeal_agar_isp_3_with_0_1_yeast_extract.yaml` |
| Major | The direct JCM 51 sibling remains split from the repaired TOGO M43 owner. | The ignored-inclusive exact search found `data/normalized_yaml/fungal/oatmeal_agar_isp_3_with_0_1_yeast_extract.yaml` grounded to `GRMD=51`; it is the same JCM medium as TOGO M43 but remains a separate source record and still carries `kg_microbe_match: mediadive.medium:12`. | `data/normalized_yaml/fungal/oatmeal_agar_isp_3_with_0_1_yeast_extract.yaml` |

## Recommended Edits

1. Regenerate merged YAML from the repaired TOGO M43 and M713 owners so the stale M43/M713 collision disappears.
2. Add a merge guard that keeps media-reference-only parent recipes from colliding on a single yeast-extract row across unrelated base media.
3. Repair or de-duplicate the direct JCM 51 sibling so all JCM 51 imports agree on the 1 L Oatmeal Agar ISP-3 base and 1 g/L yeast-extract supplement.
4. Remove the false `kg_microbe_match: mediadive.medium:12` from the direct JCM 51 sibling before any future merge can select it as canonical.

## Follow-up Checks

- Rerun LinkML schema, strict schema, term, and reference validation on the regenerated Oatmeal Agar ISP-3 With 0.1% Yeast Extract record.
- Rerun an ignored-inclusive exact search for `TOGO:M43`, `JCM_M51`, `GRMD=51`, `TOGO:M713`, and `oatmeal_agar_isp_3_with_0_1_yeast_extract` to confirm the bacterial JCM 51 variant, fungal direct JCM 51 import, and archaeal M713 source are no longer conflated.
- Manually compare the regenerated M43 record against TOGO M43, JCM 51, and parent M42 to confirm it has the M42 base plus only the 1 g/L yeast-extract supplement.

## Additional Notes

The generated record should be regenerated, not patched. The bacterial TOGO M43 owner already contains the September 2026 repair for this supplemented variant; the remaining work is stale generation, merge guarding, and direct JCM 51 de-duplication.
