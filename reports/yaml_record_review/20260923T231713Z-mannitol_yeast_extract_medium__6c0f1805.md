# YAML Record Review: mannitol_yeast_extract_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mannitol_yeast_extract_medium__6c0f1805.yaml
- Started UTC: 2026-09-23T23:17:13Z
- Finished UTC: 2026-09-23T23:17:13Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:010515 |
| name | mannitol_yeast_extract_medium |
| original_name | MANNITOL-YEAST EXTRACT MEDIUM |
| category | fungal |
| medium_type | COMPLEX |
| composition_type | UNDEFINED |
| physical_state | LIQUID |
| pH | 6.8 |
| source term | mediadive.medium:J254, MANNITOL-YEAST EXTRACT MEDIUM |
| generated path | data/merge_yaml/merged/mannitol_yeast_extract_medium__6c0f1805.yaml |
| maintained owner | data/normalized_yaml/fungal/mannitol_yeast_extract_medium.yaml |

The reviewed YAML is a derived merge artifact. Its `merged_from` value names the fungal normalized owner `mannitol_yeast_extract_medium`, and the terminal curation event reports an August 2026 merge on fingerprint `6c0f180521eb181e07eeeb2b79fdee1a073950ba974670155f475bb8b09ff1c4`.

An ignored-file-inclusive exact search under `data/normalized_yaml` and `data/merge_yaml/merged` for `CultureMech:010515`, `mediadive.medium:J254`, `JCM Medium J254`, and the exact JCM GRMD 254 URL found this fungal owner, this generated copy, derived JSON indexes, and a bacterial TOGO M246 owner that also points at GRMD 254 as its original JCM source.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mannitol_yeast_extract_medium__6c0f1805.yaml` |
| Strict validator | Passed with 0 ERROR rows; `/private/tmp/mannitol_yeast_extract_medium__6c0f1805.strict.tsv` had the header row only |
| Reference validator | Passed structurally: 1 file validated, 0 reference checks, 0 failures |
| Term validator | Passed |
| Embedded history validation | Not checked: `just validate-history` validates standalone YAML records under `history/`, not embedded `MediaRecipe.curation_history` lists in merged media records |

The equivalent focused validators were run directly against the generated `MediaRecipe` because the project-level `just` wrappers currently resolve the default Python 3.13 project environment before running.

## Identity and Grounding

The generated record correctly denotes JCM GRMD 254, `MANNITOL-YEAST EXTRACT MEDIUM`. It preserves the pH 6.8 adjustment from JCM and represents HCl as a preparation step, which is the right level for an amountless acid titration instruction.

JCM GRMD 254 supports a 1 L recipe with:

| Ingredient | Amount |
|---|---:|
| Mannitol | 10.0 g |
| Yeast extract | 1.0 g |
| K2HPO4 | 0.5 g |
| MgSO4 x 7H2O | 0.2 g |
| NaCl | 0.1 g |
| Distilled water | 1.0 L |

The five solute rows match JCM numerically. The CHEBI and MediaIngredientMech links on mannitol, potassium phosphate, magnesium sulfate heptahydrate, and sodium chloride are consistent with the JCM strings. Yeast extract is correctly left as an ungrounded undefined ingredient.

## Evidence

The inspected JCM GRMD 254 page supports the formula, liquid state, pH 6.8, and HCl adjustment.

Two evidence gaps remain:

- The JCM 1.0 L distilled-water row is missing from the generated record and from its normalized owner.
- The JCM page's default 121 C, 15 min autoclave condition is not represented.

The exact JCM GRMD 254 URL also appears in the bacterial TOGO M246 owner as its `Original URL`. That owner is a separate import of this same JCM formula, but it has TOGO-specific water-unit and pH/procedure defects that prevent the two source records from merging today.

## Completeness

Missing or incomplete:

- Add the 1.0 L distilled-water basis.
- Add JCM's default autoclave condition if the local JCM import policy records it for simple media.
- Reconcile this direct JCM import with the bacterial TOGO M246 mirror of JCM GRMD 254 after the TOGO mirror is fixed.

Complete enough:

- No stock-solution references are needed.
- The pH/HCl instruction is already captured procedurally.
- No physical-state correction is needed.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The source water row is missing. | JCM GRMD 254 lists `Distilled water` as 1.0 L after the five solutes; the generated record and `data/normalized_yaml/fungal/mannitol_yeast_extract_medium.yaml` contain only mannitol, yeast extract, K2HPO4, MgSO4 x 7H2O, and NaCl. | data/normalized_yaml/fungal/mannitol_yeast_extract_medium.yaml |
| major | The same JCM GRMD 254 recipe is represented twice and not merged. | This record points directly to JCM GRMD 254 as `mediadive.medium:J254`; the bacterial `data/normalized_yaml/bacterial/mannitol_yeast_extract_medium.yaml` record points to TOGO M246, which reports `original_media_id: JCM_M254`. | data/normalized_yaml/fungal/mannitol_yeast_extract_medium.yaml, data/normalized_yaml/bacterial/mannitol_yeast_extract_medium.yaml, and merge logic |
| minor | The default JCM autoclave setting is omitted. | JCM GRMD pages state 121 C for 15 min unless otherwise stated; this record has no autoclave step. | data/normalized_yaml/fungal/mannitol_yeast_extract_medium.yaml |

## Recommended Edits

1. Add the JCM 1.0 L distilled-water row to `data/normalized_yaml/fungal/mannitol_yeast_extract_medium.yaml` using a schema-supported one-liter volume basis, for example `1000 ML_PER_L`.
2. Add JCM's default 121 C, 15 min autoclave condition if the local JCM import policy records that default for simple media.
3. After the bacterial TOGO M246 owner is fixed, regenerate merges and verify whether the TOGO M246 and direct JCM J254 records should merge into one canonical record with both bacterial and fungal category provenance.

## Follow-up Checks

- Rerun open schema, strict, term, and reference validation on the normalized owner and regenerated merged record.
- Re-fetch JCM GRMD 254 and confirm the regenerated record contains the five solutes, 1.0 L water, and pH 6.8.
- Regenerate merges and compare this record's fingerprint with the corrected bacterial TOGO M246 import.

## Additional Notes

None found.
