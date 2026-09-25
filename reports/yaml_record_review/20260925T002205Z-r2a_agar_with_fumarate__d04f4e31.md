# YAML Record Review: r2a_agar_with_fumarate

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/r2a_agar_with_fumarate__d04f4e31.yaml
- Started UTC: 2026-09-25T00:22:05Z
- Finished UTC: 2026-09-25T00:23:12Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| Generated record | data/merge_yaml/merged/r2a_agar_with_fumarate__d04f4e31.yaml |
| Maintained owner | data/normalized_yaml/bacterial/r2a_agar_with_fumarate.yaml |
| Stable ID | CultureMech:002402 |
| Name | r2a_agar_with_fumarate |
| Original name | R2A AGAR WITH FUMARATE |
| Category | bacterial |
| Medium type | COMPLEX |
| Composition type | UNDEFINED |
| Physical state | SOLID_AGAR |
| Source grounding | mediadive.medium:J1235, JCM Medium 1235 |
| Merge fingerprint | d04f4e312a9a77feb6ff6af05e6ac94f1465f2672395a7877e4c0ee4b5933c0e |
| Merged from | r2a_agar_with_fumarate |

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/r2a_agar_with_fumarate__d04f4e31.yaml` | Passed with `No issues found`. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/r2a_agar_with_fumarate__d04f4e31.yaml --out /private/tmp/r2a_agar_with_fumarate__d04f4e31.strict.tsv --workers 1 --quiet` | Passed. `/private/tmp/r2a_agar_with_fumarate__d04f4e31.strict.tsv` had one line, the header only, so 0 strict errors. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/r2a_agar_with_fumarate__d04f4e31.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the focused check reported 0 reference checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/r2a_agar_with_fumarate__d04f4e31.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

The generated direct JCM record denotes the right source medium: JCM Medium 1235, R2A AGAR WITH FUMARATE. The live JCM record lists R2A agar (BD-Difco), disodium fumarate, and distilled water, and its anaerobic-use comment is present in the generated record as a preparation step.

The medium identity is properly grounded to `mediadive.medium:J1235`, but the generated recipe is stale relative to the maintained owner. The owner now models this medium as a supplemented variant of the repaired base R2A Agar owner, linking 1000 ml/L `CultureMech:002706` R2A Agar and adding only 3.2 g/L disodium fumarate as the supplement. The generated record still flattens `R2A agar` as an 18.2 g/L ingredient, omits the water/component composition inherited from the parent, and maps that wrapper ingredient to `CHEBI:2509` agar.

## Evidence

- Supported: JCM Medium 1235 supports the target label and the source grounding to JCM 1235.
- Supported: JCM Medium 1235 supports the supplement, 3.2 g/L disodium fumarate.
- Supported: JCM Medium 1235 supports the anaerobic note represented in the generated preparation step.
- Over-flattened: JCM 1235 lists R2A agar as an input, but in this corpus the repaired direct owner treats that input as a 1000 ml/L `R2A Agar` solution link to `CultureMech:002706`, not as top-level agar with a CHEBI agar mapping.
- Stale duplicate: an ignored-inclusive exact search for `TOGO:M1328`, `togomedium.org/medium/M1328`, `JCM_M1235`, `mediadive.medium:J1235`, `Source: JCM, ID: J1235`, and `GRMD=1235` under `data/normalized_yaml` and `data/merge_yaml` found a separate TOGO M1328 owner and generated record for the same upstream JCM M1235 medium.

## Completeness

The generated record is missing the maintained repair that represents the formula as a supplemented variant of base R2A Agar, including `solutions`, `parent_media`, `variant_relationship`, `variant_modifications`, `data_quality_flags`, and `references` to the live JCM 1235 and base JCM 346 records.

The generated record is also incomplete as a direct flattened formula because it has no water ingredient. This is less important than the stale parent-solution representation, because the maintained owner should be regenerated from the repaired record rather than patched by adding only distilled water to the generated output.

The direct record has no `references` field in the generated copy, but its `media_term` and notes still identify JCM Medium 1235. Empty optional fields are not defects unless they hide the stale variant repair above.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The generated record is stale and still flattens R2A Agar With Fumarate instead of using the repaired base-medium solution and supplemented-variant model. | `data/normalized_yaml/bacterial/r2a_agar_with_fumarate.yaml` was repaired on 2026-09-08 with a `CultureMech:002706` R2A Agar solution, `SUPPLEMENTED_VARIANT` parent metadata, curated disodium fumarate, references, and quality flags; the generated record still has only top-level `R2A agar` and `Disodium fumarate` ingredients from the pre-repair import. | data/normalized_yaml/bacterial/r2a_agar_with_fumarate.yaml and merge generation |
| Major | The TOGO M1328 import duplicates the same JCM M1235 upstream source and remains unrepaired. | The ignored-inclusive exact search found `data/normalized_yaml/bacterial/TOGO_M1328_R2A_Agar_With_Fumarate.yaml` and `data/merge_yaml/merged/R2A_AGAR_WITH_FUMARATE.yaml`; both point at TOGO M1328 with original source `JCM_M1235`, contain the stale 1 g/L distilled-water import, flatten `R2A agar (BD-Difco)`, and add a variable `N2` ingredient for a gas-phase condition. | data/normalized_yaml/bacterial/TOGO_M1328_R2A_Agar_With_Fumarate.yaml and duplicate merge handling |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/r2a_agar_with_fumarate__d04f4e31.yaml` from `data/normalized_yaml/bacterial/r2a_agar_with_fumarate.yaml` so the generated record carries the repaired `CultureMech:002706` parent-medium solution, `SUPPLEMENTED_VARIANT` metadata, references, quality flags, and curated disodium fumarate representation.
2. Merge, retire, or repair `data/normalized_yaml/bacterial/TOGO_M1328_R2A_Agar_With_Fumarate.yaml` so TOGO M1328 no longer generates a second stale record for the same JCM M1235 formulation.
3. Rerun the merge/index generation so source indexes and merged records reflect only the maintained repaired owner for JCM Medium 1235.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation on the regenerated JCM record.
- Run an ignored-inclusive exact search for `TOGO:M1328`, `JCM_M1235`, and `mediadive.medium:J1235` under `data/normalized_yaml` and `data/merge_yaml` to confirm the duplicate TOGO import was intentionally reconciled.
- Inspect the regenerated `r2a_agar_with_fumarate` record and verify that its only supplemental ingredient is 3.2 g/L disodium fumarate and that the R2A Agar base appears as a `solutions` entry linked to `CultureMech:002706`.
- Verify that `data/normalized_yaml/bacterial/r2a_agar.yaml` still records JCM 1235 as the R2A Agar plus fumarate supplemented variant child.

## Additional Notes

The reviewed generated record's structure, CHEBI identifiers, and source CURIEs validate, so the defect is stale generation and duplicate source ownership rather than local YAML syntax.
