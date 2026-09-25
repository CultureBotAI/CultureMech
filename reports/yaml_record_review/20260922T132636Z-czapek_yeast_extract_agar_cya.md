# YAML Record Review: czapek_yeast_extract_agar_cya

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/czapek_yeast_extract_agar_cya.yaml`
- Started UTC: 2026-09-22T13:23:00Z
- Finished UTC: 2026-09-22T13:26:36Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `MediaRecipe` |
| Generated ID | `CultureMech:008792` |
| Name | `czapek_yeast_extract_agar_cya` |
| Original name | `Czapek Yeast Extract Agar (CYA)` |
| Source term | `TOGO:M219` / TOGO Medium M219 |
| Original source | JCM Medium 226 |
| Generated from | `czapek_yeast_extract_agar_cya` |
| Merge fingerprint | `d593f2d657e1359d550199e49e5d933cb1add7c24247c02df84d011e6d95edf0` |

This generated record projects
`data/normalized_yaml/bacterial/czapek_yeast_extract_agar_cya.yaml`; the
normalized source owns any correction.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open-schema LinkML | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/czapek_yeast_extract_agar_cya.yaml` | Passed with `No issues found`. |
| Strict closed-schema validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/czapek_yeast_extract_agar_cya.yaml --out /private/tmp/czapek_yeast_extract_agar_cya.strict.tsv --workers 1 --quiet` | Passed with 0 error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/czapek_yeast_extract_agar_cya.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 references were checked. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/czapek_yeast_extract_agar_cya.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed with no diagnostics. |
| Embedded history | `just validate-history` equivalent for `curation_history` | Not checked: the repository history validator targets standalone `history/*.yaml` records, not embedded generated `MediaRecipe.curation_history` events. |

## Identity and Grounding

- TOGO M219 identifies `Czapek Yeast Extract Agar (CYA)` and cites JCM Medium
  226. The JCM page for medium 226 has the same title and ingredient list.
- JCM 226 has a final medium containing K2HPO4 1 g, Czapek concentrate 10 ml,
  yeast extract 5 g, sucrose 30 g, agar 15 g, and distilled water 1 L.
- JCM 226 then defines `Czapek concentrate` as a separate 100 ml stock with
  NaNO3 30 g, KCl 5 g, MgSO4 x 7 H2O 5 g, FeSO4 x 7 H2O 0.1 g,
  ZnSO4 x 7 H2O 0.1 g, and CuSO4 x 5 H2O 0.05 g.
- The generated record preserves the source label and most ingredient
  identities, but it flattens the Czapek concentrate stock into top-level final
  ingredients and gives the 10 ml concentrate addition a `G_PER_L` unit.
- A gitignore-independent search with `rg --no-ignore --hidden` over
  `data/normalized_yaml/bacterial`, `data/normalized_yaml/fungal`, and
  `data/merge_yaml/merged` found the maintained TOGO M219 record, the generated
  TOGO M219 record, the direct JCM/MediaDive 226 fungal record, and generated
  TOGO source-ID neighbor matches. It found no additional exact CYA source
  record outside those two CYA imports.

## Evidence

- Supported as final-medium ingredients: yeast extract 5 g/L, K2HPO4 1 g/L,
  sucrose 30 g/L, agar 15 g/L, and 10 ml/L Czapek concentrate.
- Unsupported in the generated record: `Distilled water` at `101.0 G_PER_L`.
  The source has 1 L final-medium water and 100 ml stock-solution water, not a
  summed mass concentration.
- Unsupported in the generated record: `Czapek concentrate (see below)` at
  `10 G_PER_L`. The source addition is 10 ml/L of a stock solution.
- Unsupported in the generated record: top-level NaNO3 30 g/L, KCl 5 g/L,
  MgSO4 x 7 H2O 5 g/L, FeSO4 x 7 H2O 0.1 g/L, ZnSO4 x 7 H2O 0.1 g/L, and
  CuSO4 x 5 H2O 0.05 g/L as final-medium ingredients. Those are raw amounts in
  the Czapek concentrate recipe, whose final-medium contribution is diluted
  100-fold when 10 ml concentrate is added per liter.
- No pH, target-organism, growth-evidence, or incubation claims are present.

## Completeness

- Missing solution boundary: Czapek concentrate should be a separate stock or
  nested recipe, not a plain top-level ingredient with the stock components
  flattened beside final-medium ingredients.
- Missing references: the generated record embeds TOGO and JCM URLs in `notes`
  but has no `references` entries, so the reference validator had no checks.
- Correctly empty: the inspected JCM and TOGO sources did not state pH,
  incubation temperature, storage, target organisms, or growth outcomes.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The generated record flattens the Czapek concentrate stock into final-medium ingredients. | JCM 226 separates 10 ml/L Czapek concentrate from a 100 ml stock recipe; the generated record stores the stock components as top-level G_PER_L rows. | Re-curate `data/normalized_yaml/bacterial/czapek_yeast_extract_agar_cya.yaml` with an explicit Czapek concentrate solution boundary, then regenerate. |
| Major | Water was summed across unrelated final and stock contexts. | The generated `Distilled water` row says `101.0 G_PER_L` and notes merged `1.0, 100.0`; JCM 226 lists 1 L in the final medium and 100 ml in the Czapek concentrate. | Preserve both water rows in their own scopes in the normalized source. |
| Major | The Czapek concentrate addition has the wrong unit. | TOGO and JCM list `Czapek concentrate (see below)` as 10 ml; the generated record stores `10 G_PER_L`. | Convert that row to a 10 ml/L solution addition or another schema-supported equivalent in the maintained normalized source. |
| Minor | The direct JCM/MediaDive 226 import generates separately under `czapek_yeast_extract_agar_cya__3e4a6aef.yaml`. | Both the TOGO record and the direct JCM record cite JCM 226, but their malformed formula projections do not merge. | After repairing the TOGO and JCM imports, regenerate and verify both exact JCM 226 imports coalesce. |

## Recommended Edits

1. Model `Czapek concentrate` as a stock solution containing its six solutes
   and 100 ml distilled water.
2. Replace the generated final-medium `10 G_PER_L` Czapek concentrate row with
   a 10 ml/L addition of that stock.
3. Keep final-medium distilled water separate from the stock water; do not sum
   them into one ingredient.
4. Regenerate merged YAML and confirm TOGO M219 and JCM/MediaDive J226 produce
   one CYA generated record with source boundaries intact.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation on the repaired
  normalized CYA record and regenerated merge.
- Run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Manually compare both regenerated CYA inputs against TOGO M219 and JCM 226,
  checking the 10 ml/L stock addition and the 100 ml Czapek concentrate volume.

## Additional Notes

- JCM's global header says to autoclave media at 121 deg C for 15 minutes
  unless otherwise stated. The current record does not encode that default.
