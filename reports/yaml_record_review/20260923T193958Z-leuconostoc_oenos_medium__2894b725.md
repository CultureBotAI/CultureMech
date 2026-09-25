# YAML Record Review: Leuconostoc Oenos Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/leuconostoc_oenos_medium__2894b725.yaml
- Started UTC: 2026-09-23T19:38:33Z
- Finished UTC: 2026-09-23T19:39:58Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:007886 |
| Name | leuconostoc_oenos_medium |
| Original name | Leuconostoc Oenos Medium |
| Category | bacterial |
| Physical state | LIQUID |
| Media grounding | TOGO:M134 |
| Source provenance | Togo M134 imported from JCM_M143 |
| Generated file | data/merge_yaml/merged/leuconostoc_oenos_medium__2894b725.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M134_Leuconostoc_Oenos_Medium.yaml |
| Merge fingerprint | 2894b725a6606fef7253345e71b0bbea909af19d343a0e03c5ab03de75f683f1 |

The reviewed target is a generated one-source Togo merge for JCM 143. Future fixes belong in the maintained Togo M134 owner, followed by regeneration of `data/merge_yaml/merged/` and downstream products.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/leuconostoc_oenos_medium__2894b725.yaml`. |
| Strict validator | Passed with zero error rows in `/private/tmp/leuconostoc_oenos_medium__2894b725.strict.tsv`. |
| LinkML reference validator | Passed; the reference validator completed with zero checks because this generated record has no `references` collection. |
| LinkML term validator | Passed. |
| Embedded curation history | Not checked: the repository history validator validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

Togo M134, JCM `GRMD=143`, and MediaDive J143 identify the same Leuconostoc oenos medium with pH 4.8. The `TOGO:M134` grounding and original JCM URL are internally consistent.

An ignored-inclusive exact search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:007886`, `TOGO:M134`, `JCM_M143`, `GRMD=143`, the maintained filename, the shared slug, and the merge fingerprint found this record, its Togo owner, a separate direct JCM J143 owner, DSMZ/KOMODO Leuconostoc oenos owners, a Togo/NBRC M1620 sibling, generated siblings, and archived duplicate-review material. The direct JCM J143 owner is the same source recipe and should be merged or cross-linked with this Togo M134 owner.

## Evidence

Supported in the inspected JCM, Togo, and MediaDive sources:

- The Togo M134 / JCM 143 identity and Leuconostoc oenos label are supported.
- The dry ingredient amounts are supported: 10 g/L casein peptone tryptic digest, 5 g/L yeast extract, 10 g/L glucose, 5 g/L fructose, 0.2 g/L MgSO4 x 7 H2O, 0.05 g/L MnSO4 x H2O, 3.5 g/L diammonium citrate, and 0.5 g/L L-cysteine HCl x H2O.
- The liquid additions are supported as 1 ml/L Tween 80, 100 ml/L filtered tomato juice, and 900 ml/L distilled water.
- JCM, Togo, and MediaDive all provide pH 4.8.

Unsupported or incomplete in the generated record:

- Distilled water, Tween 80, and tomato juice are represented as `G_PER_L` even though the JCM, Togo, and MediaDive sources give them as volumes.
- The pH 4.8 adjustment is absent from structured pH and preparation fields.
- The generic source ingredient `Fructose` is grounded to CHEBI:28645 / beta-D-fructofuranose rather than generic fructose.
- The same JCM 143 recipe exists in a separate direct MediaDive/JCM local record.
- The record has no structured reference to Togo M134 or JCM 143.

## Completeness

The record preserves all eleven source ingredient rows and the JCM/Togo source identity, but it is incomplete for volume units, pH/preparation, structured references, and local deduplication with the direct JCM J143 record.

Empty optional organism, incubation, storage, and sterilization fields are acceptable for this review because the inspected JCM, Togo, and MediaDive entries do not provide those details.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | Three volume ingredients are represented with mass units. | JCM 143, Togo M134, and MediaDive J143 list 900 ml distilled water, 1 ml Tween 80, and 100 ml filtered tomato juice; the YAML stores all three as `G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M134_Leuconostoc_Oenos_Medium.yaml` or the Togo importer |
| Major | pH 4.8 is missing. | JCM 143 says to adjust pH to 4.8, and both Togo and MediaDive expose pH 4.8; the generated record has no `ph_value` or pH-adjustment step. | `data/normalized_yaml/bacterial/TOGO_M134_Leuconostoc_Oenos_Medium.yaml` |
| Major | The same JCM 143 recipe exists as a separate generated record. | `data/normalized_yaml/bacterial/JCM_J143_LEUCONOSTOC_OENOS_MEDIUM.yaml` points at the same JCM `GRMD=143` recipe and generated `data/merge_yaml/merged/LEUCONOSTOC_OENOS_MEDIUM.yaml`. | merge/import deduplication |
| Minor | Fructose is over-specifically grounded. | The source ingredient is generic fructose, while the generated Togo record maps it to beta-D-fructofuranose. | `data/normalized_yaml/bacterial/TOGO_M134_Leuconostoc_Oenos_Medium.yaml` |
| Minor | Structured references are missing. | The generated reference validator performed zero checks despite available Togo and JCM source URLs. | `data/normalized_yaml/bacterial/TOGO_M134_Leuconostoc_Oenos_Medium.yaml` |

## Recommended Edits

1. Convert distilled water, Tween 80, and filtered tomato juice to volume quantities in the maintained Togo owner.
2. Add `ph_value: 4.8` and a pH-adjustment preparation step.
3. Merge or cross-link the Togo M134 and direct JCM J143 owners for the same source recipe.
4. Replace the beta-D-fructofuranose grounding with generic fructose.
5. Add structured references for Togo M134 and JCM 143.
6. Regenerate `data/merge_yaml/merged/` and downstream pages.

## Follow-up Checks

- Rerun open schema validation, the strict validator, the reference validator, and the term validator on the regenerated YAML.
- Manually compare the regenerated Togo record against JCM 143 for 900 ml water, 1 ml Tween 80, 100 ml filtered tomato juice, 0.5 g L-cysteine HCl x H2O, and pH 4.8.
- Re-run an ignored-inclusive exact search for `TOGO:M134`, `JCM_M143`, and `GRMD=143` to confirm that only intentional source duplicates remain for JCM 143.

## Additional Notes

The search also found DSMZ/KOMODO Leuconostoc oenos records and a related NBRC M1620 record; those share the medium family but should be reconciled separately because their manganese sulfate and cysteine hydrate labels differ from JCM 143.
