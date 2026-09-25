# YAML Record Review: Modified Balch's Methanogens Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_balchs_methanogens_medium.yaml
- Started UTC: 2026-09-24T10:20:22Z
- Finished UTC: 2026-09-24T10:20:22Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Record | `data/merge_yaml/merged/modified_balchs_methanogens_medium.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:000300` |
| Name | `modified_balchs_methanogens_medium` |
| Original name | `MODIFIED BALCH'S METHANOGENS MEDIUM` |
| Category | `archaea` |
| Medium source | MediaDive / JCM `J530` |
| Maintained owners | `data/normalized_yaml/archaea/modified_balchs_methanogens_medium.yaml`; `data/normalized_yaml/bacterial/jcm_medium_no_242.yaml`; reference-copy and merge logic |
| Generated status | Incorrectly merged output from a J530 overlay record and its J242 parent |

## Validation

| Check | Result |
| --- | --- |
| Open LinkML schema validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_balchs_methanogens_medium.yaml` | Passed; exited 0 with "No issues found". |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/modified_balchs_methanogens_medium.yaml --out /private/tmp/modified_balchs_methanogens_medium.strict.tsv --workers 1 --quiet` | Passed; 0 strict errors were reported and `/private/tmp/modified_balchs_methanogens_medium.strict.tsv` contained only the header line. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/modified_balchs_methanogens_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the focused run completed with 0 reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/modified_balchs_methanogens_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not inline `MediaRecipe.curation_history` entries in a merged YAML record. |

## Identity and Grounding

The record identity is not coherent. `CultureMech:000300` and `mediadive.medium:J530` identify MODIFIED BALCH'S METHANOGENS MEDIUM, a JCM 530 overlay that says to use Medium No. 242 supplemented with 20 ml/L Fatty acid mixture and 1 ml/L coenzyme M solution. The generated ingredient list is the copied and flattened parent JCM Medium No. 242 composition, and the generated merge also lists `jcm_medium_no_242` as a synonym.

Exact `find data/normalized_yaml -name ...` searches, which do not honor gitignore exclusions, found both maintained normalized inputs:

| Normalized file | Source |
| --- | --- |
| `data/normalized_yaml/archaea/modified_balchs_methanogens_medium.yaml` | MediaDive `J530`; overlay on JCM Medium No. 242 |
| `data/normalized_yaml/bacterial/jcm_medium_no_242.yaml` | MediaDive `J242`; parent medium |

The parent and overlay are related, but they should not be merged as duplicate records. J530 needs a parent/variant relationship or a copied parent composition plus the two explicit supplement rows; J242 should remain its own medium.

## Evidence

JCM `GRMD=530` and MediaDive `J530` support only one overlay instruction: use Medium No. 242 supplemented with 20 ml/L Fatty acid mixture from Medium No. 266 and 1 ml/L coenzyme M solution at 0.01% 2-mercaptoethanesulfonic acid, filter sterilized.

| Source claim | Record representation | Review |
| --- | --- | --- |
| J530 is Medium No. 242 with 20 ml/L Fatty acid mixture and 1 ml/L coenzyme M solution. | The generated record copies Medium 242's composition and has a prose preparation step naming the two supplements, but no structured Fatty acid mixture or coenzyme M ingredient. | Incomplete J530 overlay representation. |
| J530 references J242 as a parent medium. | The generated record merged J242 into the same record as a synonym with the same fingerprint. | Unsupported duplicate merge of a parent and its modified child. |
| JCM Medium 242 has 10 ml Trace minerals and 10 ml Trace vitamins stock additions. | Trace-mineral and trace-vitamin compounds are flattened into top-level final-medium rows at stock concentration. | Unsupported inherited stock flattening. |
| NaCl, MgSO4 x 7H2O, FeSO4 x 7H2O, and CaCl2 x 2H2O occur in both Medium 242 main medium and its Trace minerals stock. | Each is duplicate-merged into one top-level row, for example NaCl is `1.588235 G_PER_L` from 0.588235 + 1.0. | Unsupported inherited cross-compartment merge. |
| Medium 242 has main, Trace minerals, and Trace vitamins water rows. | No water row is present. | Incomplete inherited parent representation. |

## Completeness

The generated record is incomplete for J530 because the two defining supplements are absent from the structured composition. It is also incomplete for J242 because the copied parent composition was imported after flattening trace-mineral and trace-vitamin stocks into the final medium.

Empty target-organism and growth-evidence fields were not treated as defects. JCM 530 and MediaDive `J530` are medium formulation pages, not growth-evidence pages.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| blocker | JCM Medium 530 and its JCM Medium 242 parent were merged as duplicate generated records. | JCM 530 is an overlay that uses Medium No. 242 with two supplements; it is not the same recipe as Medium No. 242. The generated record has J530 identity and J242 as a synonym. | `data/normalized_yaml/archaea/modified_balchs_methanogens_medium.yaml`; `data/normalized_yaml/bacterial/jcm_medium_no_242.yaml`; reference-copy and merge logic. |
| major | The two J530-specific supplements are unstructured. | JCM 530 requires 20 ml/L Fatty acid mixture and 1 ml/L 0.01% coenzyme M solution; the generated record has only a prose step naming them. | `data/normalized_yaml/archaea/modified_balchs_methanogens_medium.yaml`; referenced-medium overlay curation. |
| major | The inherited J242 trace stocks were flattened at stock concentration. | J242 has Trace minerals and Trace vitamins as stock additions; the generated record stores each stock compound as a final-medium ingredient. | `data/normalized_yaml/bacterial/jcm_medium_no_242.yaml`; MediaDive stock migration and copied-reference repair. |
| major | Parent-medium duplicate ingredients were merged across main and trace-stock compartments. | NaCl, MgSO4 x 7H2O, FeSO4 x 7H2O, and CaCl2 x 2H2O occur in both J242 main solution and Trace minerals; the record sums each pair into one row. | `data/normalized_yaml/bacterial/jcm_medium_no_242.yaml`; duplicate cleanup must preserve compartment boundaries. |
| major | Water rows from the parent main and stock solutions are absent. | J242 Main sol., Trace minerals, and Trace vitamins each contain 1000 ml distilled water; the generated copied composition has no water row. | `data/normalized_yaml/bacterial/jcm_medium_no_242.yaml`; MediaDive water import. |

## Recommended Edits

1. Stop merging `modified_balchs_methanogens_medium` with `jcm_medium_no_242`; preserve JCM 530 as a child or variant of JCM 242 rather than a duplicate.
2. Structure the 20 ml/L Fatty acid mixture and 1 ml/L 0.01% coenzyme M additions in `data/normalized_yaml/archaea/modified_balchs_methanogens_medium.yaml`.
3. Re-curate `data/normalized_yaml/bacterial/jcm_medium_no_242.yaml` so Trace minerals and Trace vitamins remain stock additions with stock-scoped recipes.
4. Keep same-named main-medium and trace-stock rows separate in JCM 242, and restore main and stock water rows.
5. Regenerate `data/merge_yaml/merged/modified_balchs_methanogens_medium.yaml` after the normalized parent and child sources are corrected.

## Follow-up Checks

1. Re-run focused open-schema, strict, reference, and term validators on both normalized owners and on the regenerated merge outputs.
2. Manually compare regenerated J530 against JCM `GRMD=530`, checking that Medium 242 is represented as the parent and the 20 ml/L fatty-acid plus 1 ml/L coenzyme M supplements are structured.
3. Manually compare regenerated J242 against MediaDive `J242`, checking stock boundaries, water rows, and all labels that occur in multiple compartments.
4. Verify that no generated record mixes J530 identity with J242 duplicate metadata.

## Additional Notes

This review inspected exact normalized inputs for both the child and parent with gitignore-independent `find` searches. The JCM `GRMD=530` page still resolves and supports the MediaDive J530 overlay description.

The repository-level `just` validators were not used for this focused record review because the project currently attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The focused validators above were run with Python 3.11 and the offline uv cache.
