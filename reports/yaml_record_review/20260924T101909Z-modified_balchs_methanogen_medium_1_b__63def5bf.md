# YAML Record Review: Modified Balch's Methanogen Medium 1/B

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_balchs_methanogen_medium_1_b__63def5bf.yaml
- Started UTC: 2026-09-24T10:19:09Z
- Finished UTC: 2026-09-24T10:19:09Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Record | `data/merge_yaml/merged/modified_balchs_methanogen_medium_1_b__63def5bf.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:000304` |
| Name | `modified_balchs_methanogen_medium_1_b` |
| Original name | `MODIFIED BALCH'S METHANOGEN MEDIUM 1/B` |
| Category | `archaea` |
| Medium source | MediaDive / JCM `J948` |
| Maintained owner | `data/normalized_yaml/archaea/modified_balchs_methanogen_medium_1_b.yaml` |
| Generated status | Generated merge output from one normalized MediaDive record |

## Validation

| Check | Result |
| --- | --- |
| Open LinkML schema validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_balchs_methanogen_medium_1_b__63def5bf.yaml` | Passed; exited 0 with "No issues found". |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/modified_balchs_methanogen_medium_1_b__63def5bf.yaml --out /private/tmp/modified_balchs_methanogen_medium_1_b__63def5bf.strict.tsv --workers 1 --quiet` | Passed; 0 strict errors were reported and `/private/tmp/modified_balchs_methanogen_medium_1_b__63def5bf.strict.tsv` contained only the header line. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/modified_balchs_methanogen_medium_1_b__63def5bf.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the focused run completed with 0 reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/modified_balchs_methanogen_medium_1_b__63def5bf.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not inline `MediaRecipe.curation_history` entries in a merged YAML record. |

## Identity and Grounding

The record identity is coherent: `CultureMech:000304` and MediaDive / JCM `J948` both identify MODIFIED BALCH'S METHANOGEN MEDIUM 1/B.

An exact `find data/normalized_yaml -name 'modified_balchs_methanogen_medium_1_b.yaml'` search, which does not honor gitignore exclusions, found `data/normalized_yaml/archaea/modified_balchs_methanogen_medium_1_b.yaml` as the generated record's maintained owner.

Most groundings preserve the source compound forms for the flattened MediaDive rows. The issue is placement and amount, not primarily chemical identity.

## Evidence

MediaDive `J948` models three compartments: `Main sol. J948` with 10 ml Trace minerals, 10 ml Trace vitamins, and two 10 ml 5% reducing solutions; a 1 L Trace minerals stock; and a 1 L Trace vitamins stock.

| Source claim | Record representation | Review |
| --- | --- | --- |
| Trace minerals is a 1 L stock added to the main medium at 10 ml. | Every trace-minerals compound is flattened into the top-level final medium at stock `G_PER_L` strength. | Unsupported stock flattening. |
| Trace vitamins is a 1 L stock added to the main medium at 10 ml. | Every trace-vitamin compound is flattened into the top-level final medium at stock `G_PER_L` strength. | Unsupported stock flattening. |
| NaCl, FeSO4 x 7 H2O, and CaCl2 x 2 H2O appear in both the main medium and the trace-mineral stock in different compartments. | Each is duplicate-merged into one top-level amount: `1.5769229999999999`, `0.10192308`, and `0.10769231 G_PER_L`. | Unsupported cross-compartment duplicate merge. |
| 5% L-Cysteine HCl x H2O and 5% Na2S x 9 H2O are 10 ml additions. | Both are direct ingredients at `10 G_PER_L`. | Unsupported unit and missing stock-strength context. |
| Main, trace-mineral, and trace-vitamin solutions each have 1000 ml distilled-water rows. | No distilled-water row is present. | Incomplete. |
| The source row amounts in `Main sol. J948` are 0.3 g KH2PO4, 0.3 g K2HPO4, 0.3 g NH4Cl, 0.6 g NaCl, and 5 g NaHCO3. | The record stores 1040-ml-scaled values such as 0.288462, 0.576923, and 4.80769 `G_PER_L`. | Dimensionally explainable from MediaDive `g_l`, but not source-faithful without an explicit final-volume conversion note. |

## Completeness

The generated record preserves the JCM anaerobic preparation prose and the trace-minerals pH preparation step, but it loses every solution boundary in the composition itself. Following the flat ingredient list would add trace minerals and vitamins at their 1 L stock strengths rather than as 10 ml per main recipe.

The record also omits water from the main solution and both stocks, and it leaves no way to recover that NaCl, FeSO4 x 7H2O, and CaCl2 x 2H2O occur in both the base recipe and the trace-minerals stock.

Empty target-organism and growth-evidence fields were not treated as defects. MediaDive `J948` is a medium formulation page, not a growth-evidence page.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | Trace minerals and Trace vitamins were flattened at stock concentration. | MediaDive adds each stock at 10 ml; the YAML stores every stock compound as if its 1 L stock `G_PER_L` concentration were a final-medium ingredient. | `data/normalized_yaml/archaea/modified_balchs_methanogen_medium_1_b.yaml`; MediaDive stock migration. |
| major | Ingredients shared by the main medium and trace-mineral stock were duplicate-merged across compartments. | NaCl, FeSO4 x 7H2O, and CaCl2 x 2H2O occur in both source compartments; the record sums each pair into one top-level ingredient. | `data/normalized_yaml/archaea/modified_balchs_methanogen_medium_1_b.yaml`; duplicate cleanup must preserve compartment boundaries. |
| major | 10 ml reducing-stock additions are represented as gram-per-liter ingredients. | MediaDive has 10 ml 5% L-Cysteine HCl x H2O and 10 ml 5% Na2S x 9H2O additions; the record stores both as `10 G_PER_L`. | `data/normalized_yaml/archaea/modified_balchs_methanogen_medium_1_b.yaml`; MediaDive stock migration. |
| major | Water rows from the main recipe and both stocks are absent. | Each MediaDive solution has a 1000 ml distilled-water row; no water row appears in the YAML. | `data/normalized_yaml/archaea/modified_balchs_methanogen_medium_1_b.yaml`; MediaDive water import. |
| minor | Source row amounts were converted to 1040 ml final-volume `G_PER_L` values without provenance. | MediaDive reports `g_l` values scaled from `Main sol. J948`'s 1040 ml volume; the YAML keeps only those decimal values and drops the source grams listed by JCM. | `data/normalized_yaml/archaea/modified_balchs_methanogen_medium_1_b.yaml`; MediaDive amount import. |

## Recommended Edits

1. Re-curate `data/normalized_yaml/archaea/modified_balchs_methanogen_medium_1_b.yaml` so Trace minerals and Trace vitamins remain stock solutions added at 10 ml, with their stock recipes nested or referenced.
2. Keep NaCl, FeSO4 x 7H2O, and CaCl2 x 2H2O rows separate in the main and trace-mineral compartments instead of duplicate-merging them across compartments.
3. Represent the 10 ml 5% L-Cysteine HCl x H2O and 10 ml 5% Na2S x 9H2O additions as stock additions rather than `10 G_PER_L` ingredients.
4. Restore water rows for the main, trace-mineral, and trace-vitamin solutions.
5. Either preserve source gram amounts from JCM or explicitly annotate any final-volume conversion from the MediaDive 1040 ml recipe.
6. Regenerate `data/merge_yaml/merged/modified_balchs_methanogen_medium_1_b__63def5bf.yaml` after the normalized source is corrected.

## Follow-up Checks

1. Re-run focused open-schema, strict, reference, and term validators on `data/normalized_yaml/archaea/modified_balchs_methanogen_medium_1_b.yaml` and the regenerated merge output.
2. Manually compare the regenerated record against MediaDive `J948` and JCM `GRMD=948`, checking the 10 ml stock additions, stock-level recipes, water rows, reducing solutions, and all duplicate labels that appear in multiple compartments.
3. Verify that no trace-mineral or trace-vitamin stock ingredient remains as a top-level final-medium ingredient unless a final concentration is explicitly calculated and marked as such.

## Additional Notes

This MediaDive `J948` record and TOGO `M995` are currently separate CultureMech IDs for the same JCM source formula, but they fail in different ways: MediaDive expands the trace-mineral and vitamin stocks and then flattens them, while TOGO keeps those rows as empty stock stubs. Unifying them safely needs the stock-boundary fixes above first.

The repository-level `just` validators were not used for this focused record review because the project currently attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The focused validators above were run with Python 3.11 and the offline uv cache.
