# YAML Record Review: marine_acidophilic_sulfur_oxidizing_bacteria_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/marine_acidophilic_sulfur_oxidizing_bacteria_medium.yaml
- Started UTC: 2026-09-23T23:24:00Z
- Finished UTC: 2026-09-23T23:24:00Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:008228 |
| name | marine_acidophilic_sulfur_oxidizing_bacteria_medium |
| original_name | Marine acidophilic sulfur-oxidizing bacteria Medium |
| category | bacterial |
| medium_type | COMPLEX |
| composition_type | UNDEFINED |
| physical_state | LIQUID |
| source term | TOGO:M1670, Marine acidophilic sulfur-oxidizing bacteria Medium |
| generated path | data/merge_yaml/merged/marine_acidophilic_sulfur_oxidizing_bacteria_medium.yaml |
| maintained owner | data/normalized_yaml/bacterial/marine_acidophilic_sulfur_oxidizing_bacteria_medium.yaml |

The reviewed YAML is a derived merge artifact. Its `merged_from` value names the single normalized owner `marine_acidophilic_sulfur_oxidizing_bacteria_medium`, and the terminal curation event reports an August 2026 merge on fingerprint `0c3bcf85283e175ee5789e34445314f328efd711e4b7b772160f207ebfa039ad`.

An ignored-file-inclusive exact search under `data/normalized_yaml` and `data/merge_yaml/merged` for `CultureMech:008228`, `TOGO:M1670`, `NBRC_M874`, `NO=874`, and `Marine acidophilic sulfur-oxidizing bacteria Medium` found this normalized owner, this generated copy, and derived JSON indexes; no second YAML in those searched trees claimed the same exact CultureMech or TOGO identifier.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/marine_acidophilic_sulfur_oxidizing_bacteria_medium.yaml` |
| Strict validator | Passed with 0 ERROR rows; `/private/tmp/marine_acidophilic_sulfur_oxidizing_bacteria_medium.strict.tsv` had the header row only |
| Reference validator | Passed structurally: 1 file validated, 0 reference checks, 0 failures |
| Term validator | Passed |
| Embedded history validation | Not checked: `just validate-history` validates standalone YAML records under `history/`, not embedded `MediaRecipe.curation_history` lists in merged media records |

The equivalent focused validators were run directly against the generated `MediaRecipe` because the project-level `just` wrappers currently resolve the default Python 3.13 project environment before running.

## Identity and Grounding

The record denotes TOGO M1670, which reports NBRC Medium 874 as its original medium. The TOGO and NBRC pages agree on the medium name and ingredient amounts.

TOGO M1670 and NBRC M874 support:

| Ingredient | Amount |
|---|---:|
| Distilled water | 1 L |
| MgSO4 x 7H2O | 5 g |
| NaCl | 20 g |
| K2HPO4 | 5 g |
| KCl | 1 g |
| (NH4)2SO4 | 3 g |
| Sulfur powder | 10 g |
| Ca(NO3)2 | 0.3 g |

The six non-sulfur salts are present at the right numeric gram amounts and are consistently grounded to CHEBI. Sulfur powder is no longer an ingredient in the generated record; it was moved to an empty placeholder solution.

## Evidence

Three source details are missing or distorted:

- TOGO M1670 and NBRC M874 list 1 L distilled water. The record stores `Distilled water` as `1 G_PER_L`.
- TOGO has `ph: 4.0`, and NBRC prints pH 4. The record has no pH field.
- NBRC and TOGO both list `Sulfur (powder)*` as a 10 g component and explain the asterisk with a special sterilization and post-inoculation instruction. The record stores sulfur under `solutions` with `composition: []` and `name: Unknown solution`, which makes a direct powder look like an empty stock solution.

The sulfur footnote is procedural: sterilize sulfur powder separately by autoclaving for 60 min at 105 C on each of 3 successive days, then add it after inoculation. The record omits that entire preparation instruction.

## Completeness

Missing or incomplete:

- Distilled water needs a volume unit.
- pH 4.0 is absent.
- Sulfur powder needs to be restored as a direct 10 G_PER_L ingredient.
- Sulfur's special sterilization and after-inoculation addition steps are absent.

Complete enough:

- No stock-solution references are needed.
- No target-organism evidence is required for this NBRC recipe import.
- The physical state can remain liquid despite the sulfur powder component.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | A direct sulfur ingredient was migrated into an empty placeholder solution. | TOGO M1670 and NBRC M874 list `Sulfur (powder)*` as a 10 g recipe component. The record instead has `solutions: [{ preferred_term: Sulfur (powder)*, composition: [], concentration: 10 G_PER_L, name: Unknown solution }]`. | data/normalized_yaml/bacterial/marine_acidophilic_sulfur_oxidizing_bacteria_medium.yaml and the solution migrator if it still classifies sulfur powder as a solution |
| major | The source water volume was converted to a mass concentration. | TOGO and NBRC list 1 L distilled water; the record stores `Distilled water` as `1 G_PER_L`. | data/normalized_yaml/bacterial/marine_acidophilic_sulfur_oxidizing_bacteria_medium.yaml; if other TOGO imports repeat this pattern, the TOGO unit-normalization code should be fixed before regenerating them |
| major | pH 4.0 is missing. | TOGO reports `ph: 4.0`, and NBRC reports pH 4. The record has no pH field. | data/normalized_yaml/bacterial/marine_acidophilic_sulfur_oxidizing_bacteria_medium.yaml |
| major | Sulfur's required sterilization and addition timing are missing. | The NBRC asterisk states that sulfur powder is sterilized separately at 105 C for 60 min on each of 3 successive days and added after inoculation; the record has no preparation steps. | data/normalized_yaml/bacterial/marine_acidophilic_sulfur_oxidizing_bacteria_medium.yaml |

## Recommended Edits

1. Move `Sulfur (powder)*` out of `solutions` and back into `ingredients` as a direct 10 G_PER_L component.
2. Change distilled water from `1 G_PER_L` to a schema-supported one-liter volume basis, for example `1000 ML_PER_L`.
3. Add pH 4.0.
4. Add preparation steps or notes preserving the sulfur powder autoclaving schedule and its addition after inoculation.
5. If the solution migrator is still maintained, teach it not to treat literal sulfur powder as a stock solution.

## Follow-up Checks

- Rerun open schema, strict, term, and reference validation on the normalized owner and regenerated merged record.
- Re-fetch TOGO M1670 and NBRC M874 and verify the regenerated recipe has eight direct ingredients, no sulfur stock solution, pH 4.0, and the sulfur footnote.
- Add a regression test that `Sulfur (powder)` remains an ingredient during any future ingredient-to-solution migration.

## Additional Notes

None found.
