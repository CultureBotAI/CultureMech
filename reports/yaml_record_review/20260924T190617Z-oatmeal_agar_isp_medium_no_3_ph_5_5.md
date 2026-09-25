# YAML Record Review: oatmeal_agar_isp_medium_no_3_ph_5_5

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/oatmeal_agar_isp_medium_no_3_ph_5_5.yaml
- Started UTC: 2026-09-24T19:05:39Z
- Finished UTC: 2026-09-24T19:06:17Z
- Verdict: needs curation

## Target

- Generated record: `data/merge_yaml/merged/oatmeal_agar_isp_medium_no_3_ph_5_5.yaml`
- Maintained owners:
  - `data/normalized_yaml/bacterial/oatmeal_agar_isp_medium_no_3.yaml`
  - `data/normalized_yaml/bacterial/oatmeal_agar_isp_medium_no_3_ph_5_5.yaml`
- Class: `MediaRecipe`
- ID: `CultureMech:008392`
- Label: `oatmeal_agar_isp_medium_no_3_ph_5_5`
- Canonical source grounding: `TOGO:M1820`, imported from NBRC medium 1052
- Inspected source URLs:
  - `https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1052`
  - `https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=245`
- Merge state: generated from two source recipes, `oatmeal_agar_isp_medium_no_3` and `oatmeal_agar_isp_medium_no_3_ph_5_5`

## Validation

All focused validators passed for the generated YAML.

| Check | Command | Result |
| --- | --- | --- |
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/oatmeal_agar_isp_medium_no_3_ph_5_5.yaml` | Passed with `No issues found`. |
| Strict schema wrapper | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/oatmeal_agar_isp_medium_no_3_ph_5_5.yaml --out /private/tmp/oatmeal_agar_isp_medium_no_3_ph_5_5.strict.tsv --workers 1 --quiet` | Passed; the output TSV had the header only, 1 line and 0 error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/oatmeal_agar_isp_medium_no_3_ph_5_5.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 reference checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/oatmeal_agar_isp_medium_no_3_ph_5_5.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils` deprecation warning. |
| Embedded history | Not run | Not checked: the available `just validate-history` target validates standalone `history/`, not embedded `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

The canonical record denotes TOGO M1820, Oatmeal Agar (ISP medium No. 3, pH 5.5), from NBRC medium 1052. It was merged as a `SOURCE_DUPLICATE` with TOGO M1467, Oatmeal Agar (ISP Medium No. 3), from NBRC medium 245.

That source-duplicate relationship is wrong. NBRC 1052 and TOGO M1820 state pH 5.5, while NBRC 245 and TOGO M1467 state pH 7.2. The formula signatures match aside from pH, but these are pH variants and should not be merged as one source-identical recipe.

## Evidence

Both inspected NBRC/TOGO source pairs contain the same nested formula: a finished medium with 20 g oatmeal, 1 ml Trace salts solution, 1 L distilled water, and 18 g agar, plus a 100 ml trace-salts stock containing 0.1 g each of FeSO4 x 7 H2O, MnCl2 x 4 H2O, and ZnSO4 x 7 H2O. The pH differs: 5.5 for M1820/NBRC 1052 and 7.2 for M1467/NBRC 245.

An ignored-inclusive exact search over `data`, `src`, `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found only the two maintained TOGO owners for `TOGO:M1820` and `TOGO:M1467`, their generated merge, and index/import report references. The import reports already flag the `101.0 G_PER_L` water row in both owners as a sum of distinct 1.0 and 100.0 parts.

## Completeness

The generated record loses the pH distinction entirely: it has neither `ph_value: 5.5` for the canonical M1820 record nor any variant representation of the pH 7.2 M1467 parent.

The stock formulation is also incomplete. The trace-salts solution should be added at 1 ml/L and should contain its own 100 ml water plus three 0.1 g stock salts. Instead, both normalized owners and the generated record flatten the stock salts into top-level final-medium ingredients, sum stock water with final-volume water, and attach an `Unknown solution` at `1 G_PER_L`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Blocker | pH 5.5 and pH 7.2 variants were merged as source duplicates. | M1820/NBRC 1052 is pH 5.5 and M1467/NBRC 245 is pH 7.2, but the generated `merged_from` includes both source records under one canonical pH 5.5 name. | Both normalized owners and source-duplicate merge metadata |
| Major | Nested trace-salts rows were flattened into final-medium ingredients. | TOGO and NBRC place FeSO4 x 7 H2O, MnCl2 x 4 H2O, ZnSO4 x 7 H2O, and 100 ml water inside `Trace salts solution*`; the generated record stores the three salts directly under `ingredients`. | Both normalized owners and the solution migration/import logic |
| Major | Two water volumes were summed and converted to the wrong unit. | The sources have 1 L distilled water for the finished medium and 100 ml distilled water for the trace-salts stock; the generated record has one top-level `Distilled water` at `101.0 G_PER_L`. | Both normalized owners |
| Major | The finished-medium trace-salts addition has the wrong unit. | Both sources add 1 ml trace-salts solution; the migrated `solutions` entry stores `value: 1`, `unit: G_PER_L`. | Both normalized owners |

## Recommended Edits

1. Split `oatmeal_agar_isp_medium_no_3_ph_5_5` and `oatmeal_agar_isp_medium_no_3` into a pH-variant relationship instead of a `SOURCE_DUPLICATE` merge.
2. Rebuild the NBRC/TOGO solution import for both records so the main medium adds 1 ml of trace-salts stock per liter and the three stock salts remain nested in the 100 ml trace-salts formulation.
3. Replace the erroneous `101.0 G_PER_L` top-level water row with the source's 1 L final-volume water representation and keep the stock 100 ml water only inside the trace-salts solution.
4. Store the two pH values explicitly: 5.5 on the M1820/NBRC 1052 record and 7.2 on the M1467/NBRC 245 record.

## Follow-up Checks

- Rerun LinkML schema, strict schema, term, and reference validation on the regenerated pH 5.5 record and its pH 7.2 parent.
- Rerun an ignored-inclusive exact search for `TOGO:M1820`, `NBRC_M1052`, `TOGO:M1467`, `M1467`, and both source filenames to confirm the two records no longer merge as source duplicates.
- Manually compare both regenerated formulas against NBRC 1052 and NBRC 245, verifying the common trace-salts stock and the distinct pH values.

## Additional Notes

This is the NBRC-flavored ISP Medium No. 3 family, not the JCM M42/JCM 50 Oatmeal Agar ISP-3 record. The same stock-solution flattening pattern appears in both families but should be repaired against their own source identifiers.
