# YAML Record Review: Gauze's Synthetic Medium No.1

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/gauzes_synthetic_medium_no_1__8978b869.yaml
- Started UTC: 2026-09-23T05:31:55Z
- Finished UTC: 2026-09-23T05:32:36Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:008059`, `gauzes_synthetic_medium_no_1`, category `bacterial`, for TOGO Medium `TOGO:M1514`.

The generated file has one source, `TOGO_M1514_Gauze_s_Synthetic_Medium_No.1`, with merge fingerprint `8978b869234e1420cd458936cdefa1c1a26f1af027ac58e61bf29a9e5caef58b`; future YAML edits belong in `data/normalized_yaml/bacterial/TOGO_M1514_Gauze_s_Synthetic_Medium_No.1.yaml`.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/gauzes_synthetic_medium_no_1__8978b869.yaml` | Passed with `No issues found`. |
| `python scripts/validate_strict.py data/merge_yaml/merged/gauzes_synthetic_medium_no_1__8978b869.yaml --out /private/tmp/gauzes_synthetic_medium_no_1_8978b869.strict.tsv --workers 1 --quiet` | Passed; the TSV had one header row and no error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/gauzes_synthetic_medium_no_1__8978b869.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the reference validator reported zero checks. |
| `linkml-term-validator validate-data data/merge_yaml/merged/gauzes_synthetic_medium_no_1__8978b869.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the repository documents `just validate-history` for standalone files under `history/`, not for generated `MediaRecipe.curation_history` entries. |

## Identity and Grounding

TOGO `M1514` resolves to `Gauze's Synthetic Medium No.1`, original medium `NBRC_M299`, original URL `https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=299`, and pH 7.2 - 7.4. The NBRC Medium 299 page confirms the same name, composition, tap-water row, optional agar row, and pH range.

An ignored-file-inclusive slug search over `data/normalized_yaml` and `data/merge_yaml/merged` found several related Gauze records: JCM/DSMZ base variants, this NBRC/TOGO M1514 record, a TOGO M72 snapshot, pH 5.3 variants, and 18% NaCl variants. This report covers only the TOGO M1514 / NBRC 299 target.

The mineral salt groundings are mostly exact, but `KNO3` still has a legacy `mediaingredientmech_term` and `Agar (if needed)` has no primary CHEBI grounding in this TOGO-derived record.

## Evidence

The inspected TOGO JSON and NBRC page agree on the following NBRC Medium 299 formula:

| Ingredient | Source amount |
|---|---:|
| Soluble starch | 20 g |
| KNO3 | 1 g |
| NaCl | 0.5 g |
| MgSO4 x 7 H2O | 0.5 g |
| K2HPO4 | 0.5 g |
| FeSO4 x 7 H2O | 10 mg |
| Tap water | 1 L |
| Agar, if needed | 15 g |

The generated YAML stores the FeSO4 x 7 H2O row as `10 G_PER_L`, three orders of magnitude above the source 10 mg in one liter. It also stores the 1 L tap-water row as `1 G_PER_L`, which is neither a volume nor the source's undefined tap-water identity.

The source says `Agar (if needed)`; the generated record stores a required 15 g/L agar ingredient and `physical_state: SOLID_AGAR`, so a user cannot tell that NBRC presents agar as conditional.

## Completeness

The pH 7.2 - 7.4 value is missing entirely even though TOGO exposes it in both `meta.ph` and a pH comment. The NBRC page also carries that range in the composition table.

The optional agar semantics are not representable in the generated flat row. If the schema cannot express an optional solidifier, the source wording should remain in a note and the physical state should avoid claiming that every preparation is solid agar.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | The FeSO4 x 7 H2O amount is off by a factor of 1000. | TOGO and NBRC say 10 mg; the generated YAML stores value `10` with unit `G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M1514_Gauze_s_Synthetic_Medium_No.1.yaml`. |
| Major | Tap water is represented as `1 G_PER_L` and grounded as pure water. | TOGO and NBRC say `Tap water`, 1 L; the row is a volume of an undefined solvent, not one gram of CHEBI water per liter. | `data/normalized_yaml/bacterial/TOGO_M1514_Gauze_s_Synthetic_Medium_No.1.yaml`. |
| Major | Optional agar is modeled as a required solid-agar ingredient. | The source row is `Agar (if needed)`, while the YAML sets `physical_state: SOLID_AGAR` and a required 15 g/L agar ingredient. | `data/normalized_yaml/bacterial/TOGO_M1514_Gauze_s_Synthetic_Medium_No.1.yaml`. |
| Major | The pH 7.2 - 7.4 range was dropped. | TOGO has `ph: "7.2 - 7.4"` and the NBRC table has the same pH range; the generated record has no `ph_value` or `ph_range`. | `data/normalized_yaml/bacterial/TOGO_M1514_Gauze_s_Synthetic_Medium_No.1.yaml`. |
| Minor | Two ingredient metadata rows are stale or incomplete. | `KNO3` still uses legacy `MediaIngredientMech:000170`, and `Agar (if needed)` lacks the CHEBI agar grounding already used in sibling Gauze records. | `data/normalized_yaml/bacterial/TOGO_M1514_Gauze_s_Synthetic_Medium_No.1.yaml`. |

## Recommended Edits

1. Convert FeSO4 x 7 H2O from 10 mg per liter to 0.01 g/L.
2. Preserve the tap-water row as 1 L of tap water and avoid grounding it as pure CHEBI water without qualification.
3. Represent agar as an optional solidifier or preserve `if needed` in the ingredient note and avoid unconditional `SOLID_AGAR`.
4. Add the pH 7.2 - 7.4 range from TOGO/NBRC.
5. Refresh the KNO3 MediaIngredientMech link and add exact agar grounding for the optional agar row.

## Follow-up Checks

After curation, regenerate this record and rerun focused schema, strict, reference, and term validation on `data/merge_yaml/merged/gauzes_synthetic_medium_no_1__8978b869.yaml`.

Manually compare against:

- TOGO API `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1514`
- NBRC `https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=299`

## Additional Notes

This NBRC/TOGO record is same-name but not identical to the JCM/DSMZ Gauze base record: NBRC uses tap water, while JCM and DSMZ use distilled water, and NBRC marks agar as conditional.
