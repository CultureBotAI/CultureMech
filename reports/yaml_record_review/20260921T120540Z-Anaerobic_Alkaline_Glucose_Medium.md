# YAML Record Review: anaerobic_alkaline_glucose_medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml`
- Started UTC: 2026-09-21T12:05:40Z
- Finished UTC: 2026-09-21T12:06:39Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:007857` |
| Name | `anaerobic_alkaline_glucose_medium` |
| Original name | Anaerobic Alkaline Glucose Medium |
| Source identity | `TOGO:M1320`, imported from `JCM_M1228` |
| Category | `bacterial` |
| Physical state | `LIQUID` |
| Generated or maintained | Generated merge from `data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml` |
| Merge fingerprint | `01194ff7f606e12c3a0351a655e7290e6b7dcf2114f709db450a05e67b966585` |

This is a singleton generated merge. Its maintained owner currently has the same scientific content and lacks only the generated `MERGED_RECIPES`, `merge_fingerprint`, and `merged_from` block.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml` | Passed with no diagnostics |
| Strict closed schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml --out /private/tmp/Anaerobic_Alkaline_Glucose_Medium.strict.tsv --workers 1 --quiet` | Passed, 0 files with errors and 0 total error rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks for this file |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known `eutils` / `pkg_resources` deprecation warning |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, and no focused validator is documented for one generated record's embedded `MediaRecipe.curation_history` block |

## Identity and Grounding

The source accession is coherent: TOGO M1320 and JCM Medium 1228 both identify the source as Anaerobic Alkaline Glucose Medium. The record reviewed here is the bacterial TOGO M1320 import, not the separate `data/normalized_yaml/specialized/anaerobic_alkaline_glucose_medium.yaml` MediaDive J1228 import that shares its normalized name.

An ignored-inclusive exact search for `CultureMech:007857`, `TOGO:M1320`, `JCM_M1228`, `01194ff7f606e12c3a0351a655e7290e6b7dcf2114f709db450a05e67b966585`, and `anaerobic_alkaline_glucose_medium` across `data/`, `scripts/`, `reports/`, `history/`, `.claude/`, `CLAUDE.md`, and `justfile` found this bacterial owner and generated merge, the specialized same-name owner and generated merge, ID/catalog/index rows, import reports, archived validation rows, and manifest rows. `find reports/yaml_record_review -maxdepth 1 -type f -name '*Anaerobic_Alkaline_Glucose_Medium.md' -print` found no existing report for this exact target before this review.

The small-molecule groundings for NaCl, NaHCO3, Na2CO3, KH2PO4, NH4Cl, MgCl2.6H2O, Glucose, N2, and water are plausible. Two solution groundings are wrong: `mediadive.solution:5342` and `mediadive.solution:5343` are unrelated MediaDive stock records named Solution A and Solution B, not the local JCM 1228 Solution A and Solution B subrecipes.

## Evidence

JCM 1228 and TOGO M1320 agree that the source has:

- 900 ml Solution A containing NaCl, Na2CO3, NaHCO3, 900 ml distilled water, and N2 autoclaving.
- 100 ml Solution B containing MgCl2.6H2O, NH4Cl, KH2PO4, Yeast extract, Glucose, 1 ml Trace element solution, 100 ml distilled water, and N2 autoclaving.
- Aseptic anaerobic combination of Solutions A and B, final pH around 9.2, and 10 ml Trace vitamins that are filter-sterilized and stored under N2.
- A JCM 32929-specific note to add 10 ml 10% Peptone solution and 6 ml 5% Na2S.9H2O solution per liter, with those stocks autoclaved and stored under N2.

The generated record loses or alters key parts of that source structure:

| Source claim | YAML representation | Judgment |
|---|---|---|
| Solution A is a local 900 ml JCM 1228 stock | `Solution A` links to `mediadive.solution:5342` and `900 G_PER_L` | Wrong cross-record grounding and wrong unit |
| Solution B is a local 100 ml JCM 1228 stock | `Solution B` links to `mediadive.solution:5343` and `100 G_PER_L` | Wrong cross-record grounding and wrong unit |
| Solution A has 900 ml water; Solution B has 100 ml water | One top-level `Distilled water`, `1000 G_PER_L` | Stock water volumes were summed and converted to mass |
| Trace element solution, 1 ml | Empty `Unknown solution` at `1 G_PER_L` | Wrong unit; referenced stock not represented |
| Trace vitamins, 10 ml | Empty `Unknown solution` at `10 G_PER_L` | Wrong unit; referenced stock not represented |
| 5% Na2S.9H2O solution, 6 ml, only for JCM 32929 | Empty `Unknown solution` at `6 G_PER_L`, unconditional | Wrong unit and wrong scope |
| 10% Peptone solution, 10 ml, only for JCM 32929 | Empty `Unknown solution` at `10 G_PER_L`, unconditional | Wrong unit and wrong scope |
| Final pH around 9.2 | Missing | Missing condition |
| Autoclave Solution A and B under N2; filter-sterilize and store Trace vitamins under N2; store JCM 32929-specific stocks under N2 | Missing | Missing preparation and sterilization |

## Completeness

The record is materially incomplete. Following it would not reproduce JCM 1228 because it points at unrelated stock recipes for Solution A/B, omits the pH 9.2 target and N2-scoped sterilization steps, and treats conditional JCM 32929 amendments as universal components.

Empty `target_organisms` and `growth_metrics` are not defects on the inspected evidence. JCM 1228 gives a JCM strain-specific amendment, but it does not state a primary growth result.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | `Solution A` and `Solution B` are grounded to wrong MediaDive solution records. | The YAML links `Solution A` to `mediadive.solution:5342` and `Solution B` to `mediadive.solution:5343`. The tracked `mediadive_5342_Solution_A.yaml` and `mediadive_5343_Solution_B.yaml` compositions do not match the JCM 1228 Solution A/B recipes. | `data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml` |
| Major | Stock and final-volume water boundaries were flattened into top-level ingredients. | JCM 1228 has 900 ml water inside Solution A and 100 ml water inside Solution B. The YAML has one top-level `1000.0 G_PER_L` Distilled water row with a duplicate-merge note. | `data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml` |
| Major | Four milliliter solution additions use `G_PER_L` and empty `Unknown solution` stubs. | JCM 1228 gives 1 ml Trace element solution, 10 ml Trace vitamins, 6 ml 5% Na2S.9H2O solution, and 10 ml 10% Peptone solution. Each is represented as an empty `solutions` item with `unit: G_PER_L`. | `data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml` |
| Major | The JCM 32929-specific additions are unconditional. | JCM scopes the 10% Peptone and 5% Na2S.9H2O additions to JCM 32929. The YAML lists them as ordinary solutions for the base medium. | `data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml` |
| Major | pH, anaerobic combination, and sterilization details are missing. | JCM 1228 says to autoclave Solution A and Solution B under N2, aseptically and anaerobically combine them, check final pH around 9.2, add filter-sterilized Trace vitamins stored under N2, and use autoclaved N2-stored JCM 32929 stocks for the conditional amendment. | `data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml` |
| Minor | The record has only free-text source URLs in `notes`. | `references` is absent, so the reference validator reports 0 checks despite TOGO M1320 and JCM 1228 being the support for every value. | `data/normalized_yaml/bacterial/anaerobic_alkaline_glucose_medium.yaml` |

## Recommended Edits

1. Replace the `mediadive.solution:5342` and `mediadive.solution:5343` links with local nested compositions for the JCM 1228 Solution A and Solution B recipes, or leave them explicitly ungrounded if this schema cannot represent local same-medium subsolutions.
2. Move the 900 ml and 100 ml water amounts back under Solution A and Solution B instead of preserving a summed top-level `1000 G_PER_L` water row.
3. Correct all milliliter addition amounts to `ML_PER_L` and restore stock percentages for Trace elements, Trace vitamins, 5% Na2S.9H2O, and 10% Peptone.
4. Scope the 10% Peptone and 5% Na2S.9H2O additions as a JCM 32929-specific variant or conditional amendment instead of unconditional base-medium ingredients.
5. Add preparation and sterilization steps for N2 autoclaving of Solutions A/B, anaerobic aseptic combination, pH 9.2 checking, filter-sterilized Trace vitamins, and N2 storage of added stocks.
6. Add structured references for TOGO M1320 and JCM Medium 1228, then regenerate `data/merge_yaml/merged/Anaerobic_Alkaline_Glucose_Medium.yaml`.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validation on the normalized owner and regenerated merge.
- Run `just verify-merges` or the narrowest merge-freshness equivalent to prove the generated merge incorporates the normalized corrections.
- Manually inspect Solution A and Solution B in the regenerated YAML to ensure neither points to `mediadive.solution:5342` or `mediadive.solution:5343`.
- Manually compare the regenerated preparation steps with JCM 1228 so the N2 autoclaving, anaerobic combination, filter sterilization, final pH 9.2, and JCM 32929-only scope are all preserved.

## Additional Notes

- `data/import_tracking/reports/concentration_plausibility.tsv` already flags the `1000 G_PER_L` water row for `CultureMech:007857`; this review confirms the source rows are 900 ml and 100 ml in separate stock sections.
- `data/normalized_yaml/specialized/anaerobic_alkaline_glucose_medium.yaml` is a separate MediaDive J1228 import with the same normalized name and flattened trace/vitamin/addition chemistry. It was resolved by the ignored-inclusive search but was not reviewed here.
