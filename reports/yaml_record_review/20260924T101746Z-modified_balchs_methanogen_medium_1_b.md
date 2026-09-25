# YAML Record Review: Modified Balch's Methanogen Medium 1/B

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_balchs_methanogen_medium_1_b.yaml
- Started UTC: 2026-09-24T10:17:46Z
- Finished UTC: 2026-09-24T10:17:46Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Record | `data/merge_yaml/merged/modified_balchs_methanogen_medium_1_b.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:010423` |
| Name | `modified_balchs_methanogen_medium_1_b` |
| Original name | `Modified Balch's Methanogen Medium 1/B` |
| Category | `archaea` |
| Medium source | TOGO `M995`; original source JCM `JCM_M948` |
| Maintained owner | `data/normalized_yaml/archaea/TOGO_M995_Modified_Balch_s_Methanogen_Medium_1_B.yaml` |
| Generated status | Generated merge output from one normalized TOGO record |

## Validation

| Check | Result |
| --- | --- |
| Open LinkML schema validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_balchs_methanogen_medium_1_b.yaml` | Passed; exited 0 with "No issues found". |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/modified_balchs_methanogen_medium_1_b.yaml --out /private/tmp/modified_balchs_methanogen_medium_1_b.strict.tsv --workers 1 --quiet` | Passed; 0 strict errors were reported and `/private/tmp/modified_balchs_methanogen_medium_1_b.strict.tsv` contained only the header line. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/modified_balchs_methanogen_medium_1_b.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the focused run completed with 0 reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/modified_balchs_methanogen_medium_1_b.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not inline `MediaRecipe.curation_history` entries in a merged YAML record. |

## Identity and Grounding

The record identity is coherent: `CultureMech:010423`, `TOGO:M995`, and JCM `JCM_M948` all identify Modified Balch's Methanogen Medium 1/B.

An exact `find data/normalized_yaml -name 'TOGO_M995_Modified_Balch_s_Methanogen_Medium_1_B.yaml'` search, which does not honor gitignore exclusions, found `data/normalized_yaml/archaea/TOGO_M995_Modified_Balch_s_Methanogen_Medium_1_B.yaml` as the generated record's maintained owner.

The resolved direct-ingredient groundings preserve the source chemical forms closely enough for the exact compounds represented, including the calcium chloride, magnesium chloride, and iron sulfate hydrates.

## Evidence

JCM 948 and TOGO `M995` support the same formula: a base liter containing salt/buffer rows, 10 ml trace minerals, 10 ml trace vitamins, NaHCO3 added after cooling under 80:20 H2-CO2, and two 10 ml 5% reducing solutions added aseptically just before inoculation after the medium has stood overnight.

| Source claim | Record representation | Review |
| --- | --- | --- |
| The base contains 1 L distilled water. | `Distilled water` is stored as `1 G_PER_L`. | Unsupported final-volume import. |
| CaCl2 x 2H2O is 8 mg, FeSO4 x 7H2O is 2 mg, and resazurin is 1 mg. | The record stores those rows as 8, 2, and 1 `G_PER_L`. | Unsupported milligram-to-gram promotion. |
| Trace minerals and trace vitamins are 10 ml additions referencing other media. | Both are empty solution stubs at `10 G_PER_L`. | Unsupported unit and missing referenced-stock representation. |
| 5% Na2S x 9H2O and 5% L-cysteine HCl x H2O are 10 ml additions per liter prior to inoculation. | Both are empty solution stubs at `10 G_PER_L`. | Unsupported unit and missing stock-strength/post-autoclave context. |
| The medium is boiled without NaHCO3, cooled under 80:20 H2-CO2, supplemented with NaHCO3, dispensed under the same gas, sealed, autoclaved, allowed to stand overnight, and pressurized to 200 kPa 80:20 H2-CO2 after inoculation. | CO2, N2, and H2 are variable ingredients; no preparation step or gas ratio is represented. | Incomplete gas and preparation modeling. |

## Completeness

The generated record has all visible JCM 948 row labels, but it loses several source units and all of the process ordering that distinguishes base-medium ingredients from post-cooling NaHCO3 addition and pre-inoculation reducing solutions.

Empty target-organism and growth-evidence fields were not treated as defects. JCM 948 is a medium formulation page, not a growth-evidence page.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | Three milligram quantities are promoted to gram-per-liter concentrations. | JCM lists 8 mg CaCl2 x 2H2O, 2 mg FeSO4 x 7H2O, and 1 mg resazurin; the record stores them as 8, 2, and 1 `G_PER_L`. | `data/normalized_yaml/archaea/TOGO_M995_Modified_Balch_s_Methanogen_Medium_1_B.yaml`; TOGO unit normalization. |
| major | Four 10 ml additions are represented as empty `G_PER_L` solution stubs. | JCM lists 10 ml trace minerals, 10 ml trace vitamins, 10 ml 5% L-cysteine HCl x H2O, and 10 ml 5% Na2S x 9H2O; the YAML gives each migrated solution a concentration of `10 G_PER_L` and an empty composition. | `data/normalized_yaml/archaea/TOGO_M995_Modified_Balch_s_Methanogen_Medium_1_B.yaml`; solution migration. |
| major | The 1 L water row is represented as a mass concentration. | JCM and TOGO list 1 L distilled water; the record stores `Distilled water` as `1 G_PER_L`. | `data/normalized_yaml/archaea/TOGO_M995_Modified_Balch_s_Methanogen_Medium_1_B.yaml`; TOGO unit normalization. |
| major | H2-CO2 atmosphere handling and 200 kPa pressurization are absent. | JCM cools and dispenses under 80:20 H2-CO2 and pressurizes inoculated vessels to 200 kPa of the same gas mixture; the record has no preparation step or structured 80:20 ratio. | `data/normalized_yaml/archaea/TOGO_M995_Modified_Balch_s_Methanogen_Medium_1_B.yaml`; TOGO comment import and gas parsing. |
| major | Ordered anaerobic preparation is absent. | JCM excludes NaHCO3 during boiling, adds it after cooling, adds reducing solutions just before inoculation, and stands the autoclaved medium overnight; no preparation steps are represented. | `data/normalized_yaml/archaea/TOGO_M995_Modified_Balch_s_Methanogen_Medium_1_B.yaml`; TOGO comment import. |

## Recommended Edits

1. Re-curate `data/normalized_yaml/archaea/TOGO_M995_Modified_Balch_s_Methanogen_Medium_1_B.yaml` from JCM 948 so CaCl2 x 2H2O, FeSO4 x 7H2O, and resazurin retain milligram quantities and water is represented as 1 L.
2. Replace the empty `10 G_PER_L` solution stubs with 10 ml additions for trace minerals, trace vitamins, 5% Na2S x 9H2O, and 5% L-cysteine HCl x H2O, preserving the Medium No. cross-references and 5% stock strengths.
3. Import the boil, cool, NaHCO3 addition, dispense, autoclave, stand-overnight, reducing-solution addition, and 200 kPa H2-CO2 pressurization steps.
4. Structure the H2-CO2 80:20 gas mixture and post-inoculation 200 kPa condition if the schema supports it; remove default variable gas ingredients if a structured representation replaces them.
5. Regenerate `data/merge_yaml/merged/modified_balchs_methanogen_medium_1_b.yaml` after the normalized source is corrected.

## Follow-up Checks

1. Re-run focused open-schema, strict, reference, and term validators on `data/normalized_yaml/archaea/TOGO_M995_Modified_Balch_s_Methanogen_Medium_1_B.yaml` and the regenerated merge output.
2. Manually compare the regenerated record against JCM `GRMD=948`, checking all mg/g/L/ml units, trace-mineral and trace-vitamin cross-references, the two 5% reducing stocks, and the 80:20 H2-CO2 handling.
3. Verify that no 10 ml stock addition remains as `10 G_PER_L`.

## Additional Notes

The repository-level `just` validators were not used for this focused record review because the project currently attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The focused validators above were run with Python 3.11 and the offline uv cache.
