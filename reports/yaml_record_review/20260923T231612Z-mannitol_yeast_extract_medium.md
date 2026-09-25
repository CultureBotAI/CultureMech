# YAML Record Review: mannitol_yeast_extract_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mannitol_yeast_extract_medium.yaml
- Started UTC: 2026-09-23T23:16:12Z
- Finished UTC: 2026-09-23T23:16:12Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009045 |
| name | mannitol_yeast_extract_medium |
| original_name | Mannitol-Yeast Extract Medium |
| category | bacterial |
| medium_type | COMPLEX |
| composition_type | UNDEFINED |
| physical_state | LIQUID |
| source term | TOGO:M246, Mannitol-Yeast Extract Medium |
| generated path | data/merge_yaml/merged/mannitol_yeast_extract_medium.yaml |
| maintained owner | data/normalized_yaml/bacterial/mannitol_yeast_extract_medium.yaml |

The reviewed YAML is a derived merge artifact. Its `merged_from` value names the bacterial normalized owner `mannitol_yeast_extract_medium`, and the terminal curation event reports an August 2026 merge on fingerprint `0774cfa12a787303e4c2dc19c06d1443ecf1cbce3d8c8b0ef9a71c64eaf4b486`.

An ignored-file-inclusive exact search under `data/normalized_yaml` and `data/merge_yaml/merged` for `CultureMech:009045`, `TOGO:M246`, `Mannitol-Yeast Extract Medium`, and the exact JCM GRMD 254 URL found this bacterial TOGO owner, this generated copy, derived JSON indexes, and a separate fungal `mediadive.medium:J254` owner for the same JCM source page. The fungal owner is `data/normalized_yaml/fungal/mannitol_yeast_extract_medium.yaml`.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mannitol_yeast_extract_medium.yaml` |
| Strict validator | Passed with 0 ERROR rows; `/private/tmp/mannitol_yeast_extract_medium.strict.tsv` had the header row only |
| Reference validator | Passed structurally: 1 file validated, 0 reference checks, 0 failures |
| Term validator | Passed |
| Embedded history validation | Not checked: `just validate-history` validates standalone YAML records under `history/`, not embedded `MediaRecipe.curation_history` lists in merged media records |

The equivalent focused validators were run directly against the generated `MediaRecipe` because the project-level `just` wrappers currently resolve the default Python 3.13 project environment before running.

## Identity and Grounding

TOGO M246 and the JCM GRMD 254 page agree that this is `Mannitol-Yeast Extract Medium` / `MANNITOL-YEAST EXTRACT MEDIUM`. TOGO explicitly reports `original_media_id: JCM_M254` and links to GRMD 254.

JCM GRMD 254 supports a 1 L recipe with:

| Ingredient | Amount |
|---|---:|
| Mannitol | 10.0 g |
| Yeast extract | 1.0 g |
| K2HPO4 | 0.5 g |
| MgSO4 x 7H2O | 0.2 g |
| NaCl | 0.1 g |
| Distilled water | 1.0 L |

JCM then instructs adjustment to pH 6.8 with HCl. TOGO preserves the same 6.8 pH as structured metadata and represents HCl as an amountless adjustment reagent.

The CHEBI and MediaIngredientMech links on mannitol, magnesium sulfate heptahydrate, sodium chloride, dipotassium hydrogen phosphate, water, and hydrogen chloride align with the component identities. Yeast extract is correctly left ungrounded.

## Evidence

The generated record correctly carries the five non-water JCM ingredients and preserves the TOGO/JCM identity link.

Three source-supported details are wrong or missing:

- Distilled water is `1 L` in TOGO and JCM, but the record stores it as `1 G_PER_L`.
- The JCM and TOGO pH value, 6.8, is absent.
- The JCM procedure says to adjust pH to 6.8 with HCl, but the record stores HCl as a variable ingredient and has no `preparation_steps` entry for pH adjustment.

The fungal `mediadive.medium:J254` owner already represents pH 6.8 and the adjustment step, and it does not carry the TOGO water unit bug. This bacterial TOGO record and the fungal JCM record are independent imports of the same underlying JCM recipe and should become merge-equivalent after source-level normalization.

## Completeness

Missing or incomplete:

- The distilled-water row needs a volume unit.
- pH 6.8 is missing.
- The HCl adjustment needs to be procedural rather than only an amountless component.
- The original JCM page's default 121 C, 15 min autoclave condition is not represented.
- The duplicate JCM GRMD 254 import in `data/normalized_yaml/fungal/mannitol_yeast_extract_medium.yaml` remains unmerged with this bacterial TOGO copy.

Complete enough:

- No stock-solution references are needed.
- No agar correction is needed; JCM 254 is liquid.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The source water volume was converted to a mass concentration. | TOGO M246 and JCM GRMD 254 both list 1 L distilled water; the generated record stores `Distilled water` as `value: '1'`, `unit: G_PER_L`. | data/normalized_yaml/bacterial/mannitol_yeast_extract_medium.yaml; if other TOGO imports repeat this pattern, the TOGO unit-normalization code should be fixed before regenerating them |
| major | The pH and HCl adjustment are incomplete. | TOGO M246 reports `ph: 6.8`, and JCM GRMD 254 says to adjust pH to 6.8 with HCl. The record has no pH value or preparation step and represents HCl only as an amountless ingredient. | data/normalized_yaml/bacterial/mannitol_yeast_extract_medium.yaml |
| major | The same JCM GRMD 254 recipe is represented twice and not merged. | The bacterial target points to TOGO M246 with `original_media_id: JCM_M254`; `data/normalized_yaml/fungal/mannitol_yeast_extract_medium.yaml` points directly to JCM GRMD 254 as `mediadive.medium:J254`. The two records differ because the bacterial TOGO import has water and pH/procedure defects. | data/normalized_yaml/bacterial/mannitol_yeast_extract_medium.yaml, data/normalized_yaml/fungal/mannitol_yeast_extract_medium.yaml, and merge logic |
| minor | The default JCM autoclave setting is omitted. | JCM GRMD pages state 121 C for 15 min unless otherwise stated; this record has no autoclave step. | data/normalized_yaml/bacterial/mannitol_yeast_extract_medium.yaml |

## Recommended Edits

1. Change the distilled-water row in `data/normalized_yaml/bacterial/mannitol_yeast_extract_medium.yaml` from `1 G_PER_L` to a schema-supported one-liter volume basis, for example `1000 ML_PER_L`.
2. Add `ph_value: 6.8` and a preparation step that adjusts pH to 6.8 with HCl.
3. Compare the bacterial TOGO M246 owner against the fungal JCM J254 owner after those fixes; decide whether one category should own the direct record or whether the regenerated merge should combine both as duplicate source imports with `categories` for bacterial and fungal.
4. Add JCM's default 121 C, 15 min autoclave detail if the local JCM import policy records that default for simple media.

## Follow-up Checks

- Rerun open schema, strict, term, and reference validation on the normalized owner and regenerated merged record.
- Regenerate the merge output and verify whether this bacterial TOGO M246 record now fingerprints with the direct fungal JCM J254 record.
- Re-fetch TOGO M246 and JCM GRMD 254 and confirm the regenerated record preserves the same five solutes, fixes only the water unit, and carries pH 6.8 plus HCl adjustment.

## Additional Notes

None found.
