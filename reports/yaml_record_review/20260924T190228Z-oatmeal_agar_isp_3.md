# YAML Record Review: oatmeal_agar_isp_3

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/oatmeal_agar_isp_3.yaml
- Started UTC: 2026-09-24T19:01:48Z
- Finished UTC: 2026-09-24T19:02:28Z
- Verdict: needs curation

## Target

- Generated record: `data/merge_yaml/merged/oatmeal_agar_isp_3.yaml`
- Maintained owner: `data/normalized_yaml/bacterial/TOGO_M42_Oatmeal_Agar_ISP-3.yaml`
- Direct JCM sibling: `data/normalized_yaml/bacterial/oatmeal_agar_isp_3.yaml`
- Class: `MediaRecipe`
- ID: `CultureMech:009815`
- Label: `oatmeal_agar_isp_3`
- Source grounding: `TOGO:M42`, imported from JCM medium 50
- Inspected source URL: `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=50`
- Merge state: generated from one source recipe, `TOGO_M42_Oatmeal_Agar_ISP-3`

## Validation

All focused validators passed for the generated YAML.

| Check | Command | Result |
| --- | --- | --- |
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/oatmeal_agar_isp_3.yaml` | Passed with `No issues found`. |
| Strict schema wrapper | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/oatmeal_agar_isp_3.yaml --out /private/tmp/oatmeal_agar_isp_3.strict.tsv --workers 1 --quiet` | Passed; the output TSV had the header only, 1 line and 0 error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/oatmeal_agar_isp_3.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 reference checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/oatmeal_agar_isp_3.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils` deprecation warning. |
| Embedded history | Not run | Not checked: the available `just validate-history` target validates standalone `history/`, not embedded `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

The record denotes the TOGO copy of JCM medium 50, Oatmeal Agar (ISP-3). TOGO `M42` and the JCM page agree on the finished medium: 20 g oatmeal, 1 ml trace-salts solution, 18 g agar, 1 L distilled water, and final pH 7.2.

The trace-salts stock is nested in the source. JCM lists 0.1 g each of FeSO4 x 7 H2O, MnCl2 x 4 H2O, and ZnSO4 x 7 H2O in 100 ml distilled water, then adds only 1 ml of that stock to the final liter.

## Evidence

The generated YAML is stale. The maintained TOGO `M42` owner was repaired in September 2026 to model 1 L as `1000 ML_PER_L`, keep stock-strength trace salts under `solutions`, add the pH 7.2 and preparation steps, add references, and link pH and yeast-extract child variants. The generated August record still flattens the three stock salts into final-medium ingredients, sums the main and stock water rows into `101.0 G_PER_L`, and gives an empty `Unknown solution` a `1 G_PER_L` concentration.

An ignored-inclusive exact search over `data`, `src`, `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found both the repaired TOGO owner and a direct JCM source sibling, `data/normalized_yaml/bacterial/oatmeal_agar_isp_3.yaml`. The direct JCM sibling still carries the same GRMD 50 source URL but stores oatmeal at 19.98 g/L and agar at 17.982 g/L, omits the 1 L water row, and is not represented as a duplicate of the repaired TOGO owner.

## Completeness

The reviewed generated record is materially incomplete because it predates the repaired source model. It is missing the nested trace-salts solution, the pH target, the oatmeal cooking and cheesecloth filtration, the final 1 L make-up, the source references, the curated quality flags, and variant links to JCM-derived pH or supplement variants.

The inspected source does not supply target organisms or literature citations, so those optional fields were correctly empty before the repair.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The generated record still flattens stock-strength trace salts into the final-medium ingredients. | JCM and TOGO place the Fe, Mn, and Zn salts inside a 100 ml trace-salts stock added at 1 ml/L; the generated YAML stores those salts as top-level 0.1 g/L ingredients. | Regenerate from `data/normalized_yaml/bacterial/TOGO_M42_Oatmeal_Agar_ISP-3.yaml` |
| Major | The generated water row is the sum of two distinct source volumes and has the wrong unit. | The source has 1 L final-medium water and 100 ml stock water; the generated YAML has `Distilled water` at `101.0 G_PER_L`. | Regenerate from `data/normalized_yaml/bacterial/TOGO_M42_Oatmeal_Agar_ISP-3.yaml` |
| Major | The generated trace-salts addition has the wrong unit and no composition. | The source adds 1 ml trace-salts solution per liter; the generated `solutions` entry says `1 G_PER_L`, has `name: Unknown solution`, and has an empty `composition`. | Regenerate from `data/normalized_yaml/bacterial/TOGO_M42_Oatmeal_Agar_ISP-3.yaml` |
| Major | The direct JCM GRMD 50 import remains an unrepaired duplicate of the TOGO owner. | `oatmeal_agar_isp_3.yaml` points at `GRMD=50` but keeps rescaled 19.98 and 17.982 g/L masses and lacks the TOGO owner's repaired 1 L water row and reciprocal duplicate relationship. | `data/normalized_yaml/bacterial/oatmeal_agar_isp_3.yaml` |

## Recommended Edits

1. Repair or de-duplicate the direct JCM `oatmeal_agar_isp_3.yaml` import so JCM medium 50 is not split across two inconsistent source records.
2. Regenerate the merged Oatmeal Agar (ISP-3) output from the repaired `TOGO_M42_Oatmeal_Agar_ISP-3.yaml` owner, preserving the nested trace-salts stock, pH 7.2, preparation protocol, references, quality flags, and child variant links.
3. Confirm no stock component is promoted into the regenerated finished medium at stock strength.

## Follow-up Checks

- Rerun LinkML schema, strict schema, term, and reference validation on the regenerated Oatmeal Agar (ISP-3) record.
- Rerun an ignored-inclusive exact search for `TOGO:M42`, `JCM_M50`, `GRMD=50`, and `oatmeal_agar_isp_3` to confirm JCM medium 50 has one canonical parent and only intended pH or supplement variants.
- Manually compare the regenerated main solution, trace-salts stock, pH, and preparation steps against TOGO `M42` or the JCM `GRMD=50` page.

## Additional Notes

No normalized TOGO edit is needed for the flattened stock or water-summing bug; the maintained TOGO owner already has the September 2026 repair. The generated artifact should be regenerated from maintained YAML rather than patched directly.
