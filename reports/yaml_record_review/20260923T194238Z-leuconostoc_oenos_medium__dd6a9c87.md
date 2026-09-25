# YAML Record Review: Leuconostoc oenos Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/leuconostoc_oenos_medium__dd6a9c87.yaml
- Started UTC: 2026-09-23T19:41:18Z
- Finished UTC: 2026-09-23T19:42:38Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:008175 |
| Name | leuconostoc_oenos_medium |
| Original name | Leuconostoc oenos Medium |
| Category | bacterial |
| Physical state | LIQUID |
| Media grounding | TOGO:M1620 |
| Source provenance | Togo M1620 imported from NBRC_M820 |
| Generated file | data/merge_yaml/merged/leuconostoc_oenos_medium__dd6a9c87.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M1620_Leuconostoc_oenos_Medium.yaml |
| Merge fingerprint | dd6a9c872779a41617f28de1f5f5485f3cdf33634c8d20cd4293100e1a16ffc7 |

The reviewed target is a generated one-source Togo merge for NBRC 820. Future fixes belong in the maintained Togo M1620 owner, followed by regeneration of `data/merge_yaml/merged/` and downstream products.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/leuconostoc_oenos_medium__dd6a9c87.yaml`. |
| Strict validator | Passed with zero error rows in `/private/tmp/leuconostoc_oenos_medium__dd6a9c87.strict.tsv`. |
| LinkML reference validator | Passed; the reference validator completed with zero checks because this generated record has no `references` collection. |
| LinkML term validator | Passed. |
| Embedded curation history | Not checked: the repository history validator validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

Togo M1620 and NBRC Medium 820 identify a pH 4.8 Leuconostoc oenos recipe that is closely related to the JCM 143 and DSMZ 59 records, but not identical: NBRC 820 names MnSO4 x H2O and Cysteine-HCl, while JCM 143 names MnSO4 x H2O with an unspecified hydration count and L-cysteine HCl x H2O. Those source distinctions should be preserved while linking the records as a related medium family.

An ignored-inclusive exact search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:008175`, `TOGO:M1620`, `NBRC_M820`, `NO=820`, the maintained filename, the shared slug, and the merge fingerprint found this record, its Togo owner, the related JCM/Togo and DSMZ/KOMODO owners, generated siblings, source indexes, and archived validation rows.

## Evidence

Supported in the inspected NBRC and Togo sources:

- The Togo M1620 / NBRC 820 identity, Leuconostoc oenos label, and pH 4.8 endpoint are supported.
- The dry ingredient amounts are supported: 10 g/L casein peptone tryptic digest, 5 g/L yeast extract, 10 g/L glucose, 5 g/L fructose, 0.2 g/L MgSO4 x 7 H2O, 0.05 g/L MnSO4 x H2O, 3.5 g/L diammonium hydrogencitrate, and 0.5 g/L cysteine-HCl.
- The liquid additions are supported as 1 ml/L Tween 80, 100 ml/L filtered tomato juice, and 900 ml/L distilled water.

Unsupported or incomplete in the generated record:

- Distilled water, Tween 80, and tomato juice are represented as `G_PER_L` even though NBRC and Togo give them as volumes.
- The pH 4.8 endpoint is absent from structured pH and preparation fields.
- The generic source ingredient `Fructose` is grounded to CHEBI:28645 / beta-D-fructofuranose rather than generic fructose.
- The record has no structured reference to Togo M1620 or NBRC 820.

## Completeness

The record preserves all eleven NBRC ingredient rows and the Togo/NBRC source identity, but it is incomplete for volume units, pH, structured references, and related-variant links to the other Leuconostoc oenos records.

Empty optional organism, incubation, storage, and sterilization fields are acceptable for this review because the inspected NBRC and Togo entries do not provide those details.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | Three volume ingredients are represented with mass units. | NBRC 820 and Togo M1620 list 900 ml distilled water, 1 ml Tween 80, and 100 ml filtered tomato juice; the YAML stores all three as `G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M1620_Leuconostoc_oenos_Medium.yaml` or the Togo importer |
| Major | pH 4.8 is missing. | NBRC 820 and Togo M1620 expose pH 4.8; the generated record has no `ph_value` or pH-adjustment step. | `data/normalized_yaml/bacterial/TOGO_M1620_Leuconostoc_oenos_Medium.yaml` |
| Minor | Fructose is over-specifically grounded. | The source ingredient is generic fructose, while the generated Togo record maps it to beta-D-fructofuranose. | `data/normalized_yaml/bacterial/TOGO_M1620_Leuconostoc_oenos_Medium.yaml` |
| Minor | Structured references are missing. | The generated reference validator performed zero checks despite available Togo and NBRC source URLs. | `data/normalized_yaml/bacterial/TOGO_M1620_Leuconostoc_oenos_Medium.yaml` |

## Recommended Edits

1. Convert distilled water, Tween 80, and filtered tomato juice to volume quantities in the maintained Togo owner.
2. Add `ph_value: 4.8`.
3. Replace the beta-D-fructofuranose grounding with generic fructose.
4. Add structured references for Togo M1620 and NBRC 820.
5. Link NBRC 820 as a related Leuconostoc oenos variant without collapsing its MnSO4 x H2O and cysteine-HCl labels into the JCM/DSMZ hydrate variants.
6. Regenerate `data/merge_yaml/merged/` and downstream pages.

## Follow-up Checks

- Rerun open schema validation, the strict validator, the reference validator, and the term validator on the regenerated YAML.
- Manually compare the regenerated Togo record against NBRC 820 for 900 ml water, 1 ml Tween 80, 100 ml filtered tomato juice, 0.5 g cysteine-HCl, and pH 4.8.
- Re-run an ignored-inclusive exact search for `TOGO:M1620`, `NBRC_M820`, and `leuconostoc_oenos_medium` to confirm the NBRC sibling is linked to related records without losing its source-specific hydrate labels.

## Additional Notes

No sterilization, incubation, or storage instructions were present on the inspected NBRC 820 page.
