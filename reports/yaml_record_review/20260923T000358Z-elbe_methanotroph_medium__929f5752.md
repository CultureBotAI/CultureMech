# YAML Record Review: ELBE METHANOTROPH MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/elbe_methanotroph_medium__929f5752.yaml
- Started UTC: 2026-09-23T00:01:00Z
- Finished UTC: 2026-09-23T00:03:58Z
- Verdict: needs curation

## Target

- Reviewed record: `data/merge_yaml/merged/elbe_methanotroph_medium__929f5752.yaml`
- Class: `MediaRecipe`
- ID: `CultureMech:002369`
- Name: `elbe_methanotroph_medium`
- Original label: `ELBE METHANOTROPH MEDIUM`
- Category: `bacterial`
- Medium term: `mediadive.medium:J1200` / `JCM Medium J1200`
- Generated status: generated merge record with fingerprint `929f5752ed85c10104aceb41174562b78fcc61004b684a3e2ab260e73c65d4c0`
- Maintained owner for future edits: `data/normalized_yaml/bacterial/elbe_methanotroph_medium.yaml`

The merge record adds only the `merge_recipes.py` history entry, `merge_fingerprint`, and `merged_from` metadata on top of the maintained normalized record.

## Validation

Focused validation was clean.

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/elbe_methanotroph_medium__929f5752.yaml` | Passed; `No issues found`. |
| Strict schema wrapper | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/elbe_methanotroph_medium__929f5752.yaml --out /private/tmp/elbe_methanotroph_medium__929f5752.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/elbe_methanotroph_medium__929f5752.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 reference checks, all validations passed. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/elbe_methanotroph_medium__929f5752.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; the run emitted the expected `eutils` / `pkg_resources` deprecation warning. |
| Embedded history | `just validate-history` | Not checked: the documented history validator validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

The record denotes the liquid JCM Medium 1200, `ELBE METHANOTROPH MEDIUM`. JCM and MediaDive agree on the `J1200` identity, the record's `mediadive.medium:J1200` term is correct, and the `LIQUID` physical state matches the base recipe. The separate TOGO M1286 record is the solid path for the same JCM recipe and is generated as `elbe_methanotroph_medium__0f131258.yaml`.

Most simple salts are correctly grounded. One stock ingredient is not: JCM Medium 187 defines the trace-element nickel component as `NiCl2 x 6 H2O`, while the reviewed record links that row to `CHEBI:34887` / `nickel dichloride`, which does not preserve the hexahydrate form.

## Evidence

JCM 1200 and MediaDive define the autoclaved base as four salts in 992 ml distilled water: MgCl2 x 6 H2O, KCl, CaCl2 x 2 H2O, and NaNO3. After cooling to 55C, the medium receives 5.0 ml 2 M HEPES buffer, 0.15 ml 1 M phosphate buffer, 1.0 ml FeCl2 solution, 1.0 ml trace element solution, and 1.0 ml filter-sterilized vitamin solution. The prepared culture tubes should leave more than 80 percent gas phase and receive methane to 50 percent of that gas phase by volume.

The source stock recipes are explicitly inspectable:

- JCM 1200 includes the phosphate buffer recipe in-line.
- JCM Medium 187 defines FeCl2 solution and Trace element solution.
- JCM Medium 556 defines the Vitamin solution.

The reviewed record keeps the main MgCl2, KCl, CaCl2, and NaNO3 masses, and its preparation text preserves the methane gas-phase instruction. It does not retain the post-autoclave solution boundary: HEPES, HCl, FeCl2, every trace element, and every vitamin are top-level final ingredients at the stock concentrations reported by MediaDive.

## Completeness

The liquid JCM identity and base salts are complete enough, and the optional solid agar path is correctly left out of this liquid record's ingredients.

The stock representation is incomplete. A curator or generator should be able to recover 0.15 ml phosphate buffer, 1 ml FeCl2 solution, 1 ml trace element solution, and 1 ml vitamin solution from the structured data; today those ingredients are not grouped into any stock and are present at orders of magnitude too high final concentrations.

The record has no DOI, PMID, target organism, or organism-growth evidence. Those empty optional areas are not defects for this imported JCM recipe.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| major | HEPES and all post-autoclave stocks were flattened into final ingredients. | JCM 1200 adds HEPES, phosphate buffer, FeCl2 solution, trace element solution, and vitamin solution by milliliter after cooling; the reviewed record lists the HEPES buffer as `5 G_PER_L` and expands every FeCl2, trace, and vitamin stock component to top-level stock-strength g/L rows. | `data/normalized_yaml/bacterial/elbe_methanotroph_medium.yaml` |
| major | The referenced stock solution boundaries are missing. | MediaDive J1200 exposes separate solution records for `1 M Phosphate buffer`, `FeCl2 solution`, `Trace element solution`, and `Vitamin solution`; the reviewed record has no `solutions` array. | `data/normalized_yaml/bacterial/elbe_methanotroph_medium.yaml` |
| major | `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride. | JCM Medium 187 names the stock component `NiCl2 x 6 H2O`; the reviewed row links `CHEBI:34887` / `nickel dichloride`. | `data/normalized_yaml/bacterial/elbe_methanotroph_medium.yaml` |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/elbe_methanotroph_medium.yaml`, keep only the four pre-autoclave salts in the flat ingredient table and model 5 ml HEPES buffer plus the phosphate, FeCl2, trace, and vitamin stocks as post-autoclave volume additions.
2. Add nested solution records for the 1 M phosphate buffer, FeCl2 solution, trace element solution, and vitamin solution using JCM 1200, JCM 187, and JCM 556.
3. Re-ground the nickel chloride hexahydrate stock row to a hydrate-specific term or leave it ungrounded if no exact CHEBI term is available.
4. Regenerate merged YAML and downstream pages.

## Follow-up Checks

1. Rerun LinkML schema, strict schema, reference, and term validation on the regenerated `data/merge_yaml/merged/elbe_methanotroph_medium__929f5752.yaml`.
2. Reopen JCM 1200, JCM 187, and JCM 556 and manually verify all stock additions remain post-autoclave volume additions.
3. Inspect the regenerated page and confirm it does not display HCl, FeCl2, trace elements, or vitamin rows as direct final ingredients.

## Additional Notes

- This record's preparation text mentions the optional JCM instruction for making a solid variant with 15 g/L agar. That instruction is correctly not promoted into the liquid JCM J1200 ingredient list here.
