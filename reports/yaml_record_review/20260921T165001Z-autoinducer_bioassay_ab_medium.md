# YAML Record Review: autoinducer_bioassay_ab_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/autoinducer_bioassay_ab_medium.yaml
- Started UTC: 2026-09-21T16:47:10Z
- Finished UTC: 2026-09-21T16:50:01Z
- Verdict: needs curation

## Target

| Field | Observed |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:008854 |
| name | autoinducer_bioassay_ab_medium |
| original_name | Autoinducer Bioassay (AB) Medium |
| category | bacterial |
| media_term | TOGO:M2267, Autoinducer Bioassay (AB) Medium |
| generated status | Generated merge artifact in data/merge_yaml/merged |
| maintained owner | data/normalized_yaml/bacterial/autoinducer_bioassay_ab_medium.yaml |

The target is the canonical generated merge for one normalized source recipe,
`autoinducer_bioassay_ab_medium`, with merge fingerprint
`0ff097c87495529e57af45d5db48a9d1da167ac97a53aa2aac3763100856f533`.

## Validation

| Check | Result |
|---|---|
| Open schema | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/autoinducer_bioassay_ab_medium.yaml` completed with no errors. |
| Strict validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/autoinducer_bioassay_ab_medium.yaml --out /private/tmp/autoinducer_bioassay_ab_medium.strict.tsv --workers 1 --quiet` completed with no errors. |
| Reference validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/autoinducer_bioassay_ab_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` completed with 0 checks. |
| Term validation | Pass. `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/autoinducer_bioassay_ab_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` completed with no errors, aside from a non-fatal `eutils`/`pkg_resources` deprecation warning. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for standalone `history/` files, not a focused embedded `MediaRecipe.curation_history` validator for one merge record. |
| Direct `just` validators | Not checked: the project-level `uv` environment currently fails before target-specific validation while building `llvmlite==0.46.0` under Python 3.13, with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The no-project LinkML validator workaround above exercised the target schema, strict, reference, and term checks. |

## Identity and Grounding

- The record identity is supported. TOGO API data for `M2267` names the source medium `Autoinducer Bioassay (AB) Medium`, points to the same ATCC PDF URL in the target notes, and reports pH 7.5.
- The ATCC asset at `https://www.atcc.org/~/media/F0C5AC9D96C345049F8AA78CCC2AB46A.ashx` resolves to a one-page PDF for `ATCC Medium: 2746 Autoinducer Bioassay (AB) Medium`. Its formulation and preparation text match TOGO M2267.
- The `TOGO:M2267` media term label exactly matches the TOGO API medium name and the target's `original_name`.
- The generated target is stale relative to its maintained owner. `data/normalized_yaml/bacterial/autoinducer_bioassay_ab_medium.yaml` carries the September 2026 source-backed repair, including pH, source references, corrected ml/L stock rows, and separated stock solutions. The generated record was last stamped by `merge_recipes.py` on 2026-08-06 and still has the earlier flattened TOGO import.

## Evidence

Supported by inspected source text:

- NaCl is 17.5 g in the base medium.
- MgSO4 is 12.3 g in the base medium.
- Casamino Acids are 2.0 g in the base medium.
- DI Water is 970 ml in the base medium.
- The base is brought to pH 7.5 with 3 N NaOH.
- The base is autoclaved at 121 C, then cooled completely.
- The separate sterile stock additions are 10 ml 1 M Potassium Phosphate at pH 7.0, 10 ml 0.1 M L-arginine, and 10 ml Glycerol.

Unsupported or stale in the generated target:

- `Base Medium` appears as a direct ingredient at `970 G_PER_L`. The inspected sources use `Base Medium` only as a sub-recipe heading and top-level TOGO wrapper, not as a gram-per-liter ingredient.
- DI Water is represented as `970 G_PER_L`; the ATCC source and TOGO API both specify `970 ml`.
- The three 10 ml stock additions are represented as `10 G_PER_L` ingredients, losing their ml addition units, stock concentrations, and the boundary between sterile stocks and the base.
- The generated `Stock Solutions` child solution has an empty composition and a `30 G_PER_L` concentration. TOGO's top-level 30 ml stock wrapper is a sum of three separate 10 ml stock additions, not a single 30 g/L stock solution.
- The generated record omits the pH 7.5, autoclave, cooling, and post-autoclave stock-addition steps that ATCC and TOGO both state.
- `3N NaOH` appears as a bare variable direct ingredient. The maintained repair correctly represents it as a pH-adjustment solution containing 3.0 M NaOH.

## Completeness

- Source provenance is sufficient to recover the original formulation: the generated record names TOGO M2267 and embeds the ATCC PDF URL as the original URL.
- The normalized owner has explicit `references` entries for both TOGO M2267 and the ATCC PDF; the stale generated target only has these under `notes`.
- Empty `target_organisms`, `growth_metrics`, variants, and incubation-condition slots are acceptable for this source. The inspected ATCC/TOGO source recipe establishes the formulation, not growth of a specific organism or strain.
- The potassium phosphate stock is intentionally not expanded to KH2PO4/K2HPO4 components in the maintained normalized record because the inspected source only reports a 1 M pH 7.0 potassium phosphate stock and does not disclose the acid/base salt ratio.
- Gitignore-independent search covered `data`, `reports`, `history`, and `.claude` for `CultureMech:008854`, `TOGO:M2267`, `M2267`, the ATCC asset token, and `Autoinducer Bioassay`; no prior Markdown report for this generated record was found under `reports/yaml_record_review`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated merge record is stale and still exposes the original bad TOGO flattening artifacts instead of the repaired source-backed recipe. | The generated record still contains `Base Medium` as `970 G_PER_L`, DI Water as `970 G_PER_L`, 10 ml stocks as `G_PER_L` rows, and an empty 30 g/L `Stock Solutions` solution. The authoritative normalized owner already corrected the ATCC base, stock additions, pH, NaOH adjustment, and preparation steps on 2026-09-12. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/bacterial/autoinducer_bioassay_ab_medium.yaml`; do not edit the generated target directly. |

No blocker or minor findings found.

## Recommended Edits

1. Regenerate the merge layer with `just merge-recipes`, or the equivalent `uv run python -m culturemech.merge.merge_recipes --normalized-dir data/normalized_yaml --output-dir data/merge_yaml/merged --stats-file data/merge_yaml/merge_stats.json`, so `data/merge_yaml/merged/autoinducer_bioassay_ab_medium.yaml` is rebuilt from the repaired normalized owner.
2. Regenerate downstream browser/page products that read from `data/merge_yaml/merged/` after the merge layer is refreshed.

## Follow-up Checks

- Run `just audit-merge-freshness --list` or `just audit-merge-freshness --json` to confirm this record no longer differs from a fresh merge.
- Run `just verify-merges` after `just merge-recipes` to validate the generated merge corpus against the normalized corpus and `data/merge_yaml/merge_stats.json`.
- Run `just validate-products` after downstream product regeneration to enforce id/label consistency across rendered recipe products and SSSOM outputs.
- Manually compare the regenerated `autoinducer_bioassay_ab_medium` merge against `data/normalized_yaml/bacterial/autoinducer_bioassay_ab_medium.yaml` and ATCC Medium 2746 to verify that no stale `G_PER_L` stock-wrapper rows remain.

## Additional Notes

- The generated record passes schema, strict, term, and reference validators because the defect is stale scientific content, not invalid YAML shape.
- TOGO M2267 exposes the ATCC source as structured JSON through `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2267`; the public `/medium/M2267` page itself renders as an application shell.
