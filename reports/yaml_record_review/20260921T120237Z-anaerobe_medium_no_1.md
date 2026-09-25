# YAML Record Review: anaerobe_medium_no_1

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/anaerobe_medium_no_1.yaml`
- Started UTC: 2026-09-21T12:02:37Z
- Finished UTC: 2026-09-21T12:03:19Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:010106` |
| Name | `anaerobe_medium_no_1` |
| Original name | Anaerobe Medium NO. 1 |
| Source identity | `TOGO:M69`, imported from `JCM_M78` |
| Category | `bacterial` |
| Physical state | `LIQUID` |
| Generated or maintained | Generated merge from `data/normalized_yaml/bacterial/TOGO_M69_Anaerobe_Medium_NO._1.yaml` |
| Merge fingerprint | `b985b063c736027d9687b6bc10123684ee9bf4859340be01c4538d209a1f5afe` |

This is a singleton generated merge. Its normalized owner currently has the same scientific content and lacks only the generated `MERGED_RECIPES`, `merge_fingerprint`, and `merged_from` block.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/anaerobe_medium_no_1.yaml` | Passed with no diagnostics |
| Strict closed schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/anaerobe_medium_no_1.yaml --out /private/tmp/anaerobe_medium_no_1.strict.tsv --workers 1 --quiet` | Passed, 0 files with errors and 0 total error rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/anaerobe_medium_no_1.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with no diagnostics |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/anaerobe_medium_no_1.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known `eutils` / `pkg_resources` deprecation warning |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, and no focused validator is documented for one generated record's embedded `MediaRecipe.curation_history` block |

## Identity and Grounding

The source identity is coherent. The generated `TOGO:M69` medium term points to Anaerobe Medium NO. 1, and TOGO M69 records original source `JCM_M78`, matching the source URL embedded in the YAML notes.

An ignored-inclusive exact search for `CultureMech:010106`, `TOGO:M69`, `JCM_M78`, `b985b063c736027d9687b6bc10123684ee9bf4859340be01c4538d209a1f5afe`, and `TOGO_M69_Anaerobe_Medium_NO` across `data/`, `scripts/`, `reports/`, `history/`, `.claude/`, `CLAUDE.md`, and `justfile` found the normalized owner, generated merge, ID/catalog/index rows, import reports, media-content manifests, and archived validation rows. `find reports/yaml_record_review -maxdepth 1 -type f -name '*anaerobe_medium_no_1.md' -print` found no existing report for this target before this review.

The available small-molecule groundings are source-faithful: magnesium sulfate heptahydrate, potassium dihydrogen phosphate, ammonium chloride, dipotassium hydrogen phosphate, glucose, water, and the three undefined BD-Difco product labels match TOGO M69 and JCM 78. The stock-addition labels name three additional chemicals but the generated `solutions` objects have no composition, stock concentration, or hydrated CHEBI terms.

## Evidence

TOGO M69 and the original JCM Medium 78 page agree on the base composition, three solution additions, final-volume water, and pH 7.5.

| Source claim | YAML representation | Judgment |
|---|---|---|
| Bacto peptone (BD-Difco), 10 g | `10 G_PER_L` ingredient | Supported |
| Beef extract (BD-Difco), 10 g | `10 G_PER_L` ingredient | Supported |
| Yeast extract (BD-Difco), 5 g | `5 G_PER_L` ingredient | Supported |
| Glucose, 5 g | `5 G_PER_L` ingredient | Supported |
| K2HPO4, 0.45 g | `0.45 G_PER_L` ingredient | Supported |
| KH2PO4, 0.33 g | `0.33 G_PER_L` ingredient | Supported |
| NH4Cl, 1 g | `1 G_PER_L` ingredient | Supported |
| MgSO4 x 7H2O, 0.1 g | `0.1 G_PER_L` ingredient | Supported |
| 5% L-Cysteine HCl H2O solution, 10 ml, separately sterilized | Empty solution stub at `10 G_PER_L` | Wrong unit and missing stock composition |
| 0.1% Resazurin solution, 1 ml | Empty solution stub at `1 G_PER_L` | Wrong unit and missing stock composition |
| 5% Na2S x 9H2O solution, 10 ml | Empty solution stub at `10 G_PER_L` | Wrong unit and missing stock composition |
| Distilled water, 1 L | `1 G_PER_L` ingredient | Wrong unit |
| Adjust pH to 7.5 | Missing | Unsupported omission |
| Unless otherwise stated, autoclave at 121 C for 15 min | Missing | Unsupported omission |

The generated solution names encode the source stock concentrations, but this leaves the actual resazurin, sodium sulfide nonahydrate, and L-cysteine HCl H2O stock recipes unqueryable and makes the addition amounts look like grams per liter of each stock rather than milliliters of stock per liter of medium.

## Completeness

The generated record is incomplete for both formulation and preparation:

- The final-volume solvent should be a liter or milliliter amount, not `G_PER_L`.
- The three stock additions need `ML_PER_L` addition amounts and nested stock concentrations of `0.1 PERCENT_W_V` or `5 PERCENT_W_V`.
- `ph_value: 7.5` is missing.
- JCM's default autoclaving rule is not represented.
- The inspected TOGO and JCM URLs are not present in a structured `references` block.

Empty `target_organisms` and `growth_metrics` are not defects on the inspected evidence. TOGO M69 and JCM 78 document a recipe, not a primary growth assay for a specific organism.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Final-volume water is represented as `1 G_PER_L`. | TOGO M69 and JCM 78 list 1 L distilled water; the YAML stores one gram per liter. | `data/normalized_yaml/bacterial/TOGO_M69_Anaerobe_Medium_NO._1.yaml` |
| Major | Three solution additions are empty `Unknown solution` stubs with mass units. | JCM 78 lists 1 ml 0.1% Resazurin solution, 10 ml 5% Na2S x 9H2O solution, and 10 ml 5% L-Cysteine HCl H2O solution; the YAML stores each as a solution with `composition: []`, `name: Unknown solution`, and `G_PER_L` concentration units. | `data/normalized_yaml/bacterial/TOGO_M69_Anaerobe_Medium_NO._1.yaml` |
| Major | The source pH is missing. | TOGO M69 and JCM 78 both state pH 7.5, but the YAML has no `ph_value` or preparation step for pH adjustment. | `data/normalized_yaml/bacterial/TOGO_M69_Anaerobe_Medium_NO._1.yaml` |
| Major | Default JCM autoclaving is missing. | The original JCM page states that media are autoclaved at 121 C for 15 min unless otherwise stated. Medium 78 gives no exception, and the YAML has no `sterilization` block. | `data/normalized_yaml/bacterial/TOGO_M69_Anaerobe_Medium_NO._1.yaml` |
| Minor | The record has only free-text source URLs in `notes`. | `references` is absent, so the reference validator has no structured URLs to check despite TOGO M69 and JCM 78 being the support for all formulation claims. | `data/normalized_yaml/bacterial/TOGO_M69_Anaerobe_Medium_NO._1.yaml` |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/TOGO_M69_Anaerobe_Medium_NO._1.yaml`, change Distilled water to a final-volume unit such as `1 L` or `1000 ML_PER_L`.
2. Replace the three empty solution stubs with structured stock additions: `1 ML_PER_L` of 0.1% Resazurin, `10 ML_PER_L` of 5% sodium sulfide nonahydrate, and `10 ML_PER_L` of 5% L-Cysteine HCl H2O, with each stock component grounded exactly.
3. Add `ph_value: 7.5` and a pH-adjustment preparation step.
4. Add sterilization at 121 C for 15 min under the JCM default rule, preserving any separately sterilized handling for the cysteine stock.
5. Add structured references for TOGO M69 and JCM Medium 78.
6. Regenerate `data/merge_yaml/merged/anaerobe_medium_no_1.yaml` from the corrected normalized owner.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validation on the normalized owner and regenerated merge.
- Run `just verify-merges` or the narrowest merge-freshness equivalent to prove the generated merge incorporates the normalized corrections.
- Manually compare the regenerated solution objects against JCM 78 to ensure milliliter addition amounts and percent stock concentrations were not flattened into `G_PER_L`.
- Manually confirm the regeneration keeps the JCM-specific pH 7.5 and 121 C for 15 min autoclaving details.

## Additional Notes

- The generated merge and normalized owner are current with each other; these defects live in the maintained TOGO M69 normalized file rather than only in a stale merge.
- The TOGO M69 API mirrors JCM 78, so the source identity did not require choosing between conflicting TOGO and JCM formulations.
