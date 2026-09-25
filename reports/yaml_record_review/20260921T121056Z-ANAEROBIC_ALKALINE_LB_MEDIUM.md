# YAML Record Review: ANAEROBIC ALKALINE LB MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ANAEROBIC_ALKALINE_LB_MEDIUM.yaml
- Started UTC: 2026-09-21T12:10:56Z
- Finished UTC: 2026-09-21T12:11:51Z
- Verdict: needs curation

## Target

- Reviewed record: `data/merge_yaml/merged/ANAEROBIC_ALKALINE_LB_MEDIUM.yaml`
- Class: `MediaRecipe`
- Stable ID: `CultureMech:015381`
- Label: `ANAEROBIC ALKALINE LB MEDIUM`
- Category: `specialized`
- Source identity: MediaDive `mediadive.medium:J1111`, source `JCM`, original JCM URL `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1111`
- Generated status: generated merge record with fingerprint `1e17c5d4c2861f78c5f839a2abc0683c3ad1f1367e9906d305e9a3f4fb8b9224`
- Merge lineage: one source, `data/normalized_yaml/specialized/anaerobic_alkaline_lb_medium.yaml`
- Maintained owner for future record edits: `data/normalized_yaml/specialized/anaerobic_alkaline_lb_medium.yaml`; the MediaDive importer owns any general fix for converting milliliter stock additions

## Validation

- Open schema:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ANAEROBIC_ALKALINE_LB_MEDIUM.yaml`
  - Result: passed; no issues found
- Strict schema:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ANAEROBIC_ALKALINE_LB_MEDIUM.yaml --out /private/tmp/ANAEROBIC_ALKALINE_LB_MEDIUM.strict.tsv --workers 1 --quiet`
  - Result: passed; 1 file scanned, 0 files with errors, 0 total error rows
- Reference validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ANAEROBIC_ALKALINE_LB_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Result: passed; 1 file validated, 0 total checks
- Term validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ANAEROBIC_ALKALINE_LB_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Result: passed
- Embedded curation history: Not checked. The documented `just validate-history` recipe validates standalone records under `history/`; I did not find a focused embedded `MediaRecipe.curation_history` validator for one merge file.

## Identity and Grounding

The record correctly denotes MediaDive medium `J1111`, `ANAEROBIC ALKALINE LB MEDIUM`. The inspected MediaDive REST payload reports the same medium ID, label, JCM source, pH `9.5`, and JCM `GRMD=1111` link, and the inspected JCM page is medium 1111 with the same title.

Ingredient grounding is mostly shape-valid but partly source-misleading. `Tris base`, `Na2CO3`, and `Na2S x 9 H2O` have plausible ChEBI terms for those literal strings, but the sodium carbonate and sodium sulfide rows do not represent the source materials as used: both are stock solutions added by volume after autoclaving, not top-level dry compounds weighed into the base recipe.

## Evidence

Supported:

- MediaDive `J1111` and JCM medium 1111 both support a pH target of `9.5` and the medium name `ANAEROBIC ALKALINE LB MEDIUM`.
- MediaDive supports importing `25 g` LB broth powder and `3 g` Tris base as `24.8016 G_PER_L` and `2.97619 G_PER_L` after dividing by its recorded 1008 ml final volume.
- JCM supports mixing the base powder, Tris, and water, adjusting the pH to 9.5 with NaOH, autoclaving under an N2-CO2 gas mixture, cooling, and then aseptically and anaerobically adding autoclaved stock solutions stored under N2.

Unsupported or over-scoped:

- JCM and MediaDive list `Na2CO3` as 200 ml of an 8 percent sodium carbonate solution. The YAML instead states `Na2CO3` at `200 G_PER_L`, which is a milliliter amount retyped as a grams-per-liter dry-compound concentration.
- JCM and MediaDive list `Na2S x 9 H2O` as 8 ml of a 5 percent sodium sulfide nonahydrate solution. The YAML instead states `Na2S x 9 H2O` at `8 G_PER_L`, again retyping a stock volume as a dry-compound concentration.
- The JCM and MediaDive `800 ml` distilled-water row is absent.
- The only preparation step is typed as `AUTOCLAVE` but includes post-cooling aseptic additions that happen after autoclaving.

## Completeness

Consequential gaps:

- The stock-solution nature, percentage strength, and volume of the 8 percent `Na2CO3` and 5 percent `Na2S x 9 H2O` additions are not represented.
- The 800 ml water component is missing, so the base medium volume cannot be audited.
- The preparation procedure is not split into base mixing, pH adjustment, N2-CO2 autoclaving, cooling, and anaerobic addition of autoclaved stocks.
- The `high_metal: true` flag is unsupported by the source formulation and appears downstream of the erroneous `200 G_PER_L` sodium carbonate row.
- No structured `references` entry captures the JCM page or MediaDive source beyond the prose `notes` field.

Correctly empty or not scored:

- `target_organisms`, `growth_metrics`, and variant links are empty. The inspected sources are recipe sources and do not provide strain-specific growth evidence.
- `LB broth powder` remains ungrounded to ChEBI, which is acceptable for an undefined complex powder.

Bounded searches:

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ANAEROBIC_ALKALINE_LB_MEDIUM.md' -print` found no prior report for this generated record before the report was written; `find` included ignored report files.
- `rg --no-ignore --hidden -F 'https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1111' data/normalized_yaml data/merge_yaml` found only the specialized normalized owner and this generated merge among maintained normalized records and ignored merge records.

## Findings

| ID | Severity | Finding | Maintained owner |
| --- | --- | --- | --- |
| F1 | major | The 8 percent sodium carbonate stock addition is represented as `200 G_PER_L` `Na2CO3` instead of 200 ml of stock. This changes a post-autoclave stock addition into a massive dry-compound amount and likely drives the unsupported `high_metal: true` flag. | `data/normalized_yaml/specialized/anaerobic_alkaline_lb_medium.yaml` and the MediaDive importer |
| F2 | major | The 5 percent sodium sulfide nonahydrate stock addition is represented as `8 G_PER_L` `Na2S x 9 H2O` instead of 8 ml of stock. | `data/normalized_yaml/specialized/anaerobic_alkaline_lb_medium.yaml` and the MediaDive importer |
| F3 | major | The source recipe's 800 ml distilled-water component is missing, so the main solution volume and dilution cannot be reconstructed. | `data/normalized_yaml/specialized/anaerobic_alkaline_lb_medium.yaml` and the MediaDive importer |
| F4 | major | One `AUTOCLAVE` step conflates several operations and covers aseptic additions that occur after cooling; it does not preserve stock addition boundaries. | `data/normalized_yaml/specialized/anaerobic_alkaline_lb_medium.yaml` and the MediaDive step importer |
| F5 | minor | The record has no structured references for the MediaDive or JCM source used to generate it, leaving the reference validator with zero checks. | `data/normalized_yaml/specialized/anaerobic_alkaline_lb_medium.yaml` |

## Recommended Edits

1. Replace the `Na2CO3` top-level dry-compound row with an addition of 200 ml of 8 percent sodium carbonate solution, preserving that it is autoclaved and stored under N2 before anaerobic addition.
2. Replace the `Na2S x 9 H2O` top-level dry-compound row with an addition of 8 ml of 5 percent sodium sulfide nonahydrate solution, preserving that it is autoclaved and stored under N2 before anaerobic addition.
3. Restore the 800 ml distilled-water row in the base recipe.
4. Split the preparation into the source operations: mix LB broth powder, Tris, and water; adjust pH to 9.5 with NaOH; autoclave under N2-CO2 4:1 v/v; cool; aseptically and anaerobically add the two autoclaved stock solutions.
5. Remove or recompute `high_metal: true` after the stock-volume unit errors are fixed.
6. Add structured references for MediaDive `J1111` and JCM medium 1111.
7. Regenerate `data/merge_yaml/merged/ANAEROBIC_ALKALINE_LB_MEDIUM.yaml` from the normalized owner.

## Follow-up Checks

- Re-run open schema, strict schema, reference validation, and term validation on `data/normalized_yaml/specialized/anaerobic_alkaline_lb_medium.yaml`.
- Re-run the same focused validators on regenerated `data/merge_yaml/merged/ANAEROBIC_ALKALINE_LB_MEDIUM.yaml`.
- Run `just verify-merges` and `just audit-merge-freshness` after regeneration to prove the normalized owner and generated merge match.
- Manually compare the regenerated record against MediaDive `J1111` and JCM medium 1111, checking the two percentage stock additions, 800 ml water row, pH 9.5, and N2-CO2 4:1 v/v autoclave atmosphere.

## Additional Notes

- Direct `just validate-schema`, `just validate-strict`, `just validate-terms`, and `just validate-references` were not used for this report because the project `uv` environment attempted to build `llvmlite==0.46.0` under Python 3.13 and failed before target-specific validation. The no-project Python 3.11 commands above were used as focused equivalents.
- The separate `data/normalized_yaml/bacterial/mediadive_5200_Main_sol_J1111.yaml` solution record also comes from MediaDive solution `5200`; it was not treated as an independent `MediaRecipe` duplicate for this review.
- The inspected generated merge and normalized owner are identical through the source-owned fields; the generated record only adds the `merge_recipes.py` curation event, `merge_fingerprint`, and `merged_from`.
