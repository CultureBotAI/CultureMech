# YAML Record Review: Leeming &amp; Notman agar (LNA) (Leeming &amp; Notman 1987) in The Yeasts, a Taxonomic Study, 5th edn

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/leeming_amp_notman_agar_lna_leeming_amp_notman_1987_in_the_yeasts_a_taxonomic_study_5th_edn.yaml
- Started UTC: 2026-09-23T19:21:24Z
- Finished UTC: 2026-09-23T19:22:28Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:008670 |
| Name | leeming_amp_notman_agar_lna_leeming_amp_notman_1987_in_the_yeasts_a_taxonomic_study_5th_edn |
| Original name | Leeming &amp; Notman agar (LNA) (Leeming &amp; Notman 1987) in The Yeasts, a Taxonomic Study, 5th edn |
| Category | bacterial |
| Physical state | SOLID_AGAR |
| Media grounding | TOGO:M2080 |
| Source provenance | Togo M2080 imported from NBRC_M1390 |
| Generated file | data/merge_yaml/merged/leeming_amp_notman_agar_lna_leeming_amp_notman_1987_in_the_yeasts_a_taxonomic_study_5th_edn.yaml |
| Maintained owner | data/normalized_yaml/bacterial/leeming_amp_notman_agar_lna_leeming_amp_notman_1987_in_the_yeasts_a_taxonomic_study_5th_edn.yaml |
| Merge fingerprint | 77a72e2c85c8bc90cc26fad91ff4ed5086e29a443dbaada730c9722cede848e0 |

The reviewed file is a generated merge from a single Togo M2080 owner. Future fixes belong in the maintained normalized owner, followed by regeneration of `data/merge_yaml/merged/` and downstream products.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/leeming_amp_notman_agar_lna_leeming_amp_notman_1987_in_the_yeasts_a_taxonomic_study_5th_edn.yaml`. |
| Strict validator | Passed with zero error rows in `/private/tmp/leeming_amp_notman_agar_lna.strict.tsv`. |
| LinkML reference validator | Passed; the reference validator completed with zero checks because this generated record has no `references` collection. |
| LinkML term validator | Passed. |
| Embedded curation history | Not checked: the repository history validator validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

Togo M2080 and NBRC Medium 1390 both identify the same Leeming & Notman agar (LNA) recipe. The NBRC page names the Leeming & Notman 1987 `J Clin Microbiol` paper and `The Yeasts, a Taxonomic Study, 5th edn, vol. 1, pp98` as references.

The `TOGO:M2080` grounding, original NBRC 1390 provenance, and solid agar state are internally consistent. The `bacterial` category is not source-supported for this recipe: NBRC identifies the medium as Leeming & Notman agar, and the embedded bibliographic context points at yeast media rather than bacterial cultivation. An ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:008670`, `TOGO:M2080`, `NBRC_M1390`, `NO=1390`, the Leeming source slug, and the merge fingerprint found the generated record, the maintained owner, sibling Leeming & Notman medium records, source indexes, and archived validation rows.

## Evidence

Supported in the inspected NBRC and Togo sources:

- The source label and Togo/NBRC identity are supported.
- The dry ingredient amounts are supported: 10 g/L bacteriological peptone, 5 g/L glucose, 0.1 g/L yeast extract, 8 g/L desiccated ox bile, 0.5 g/L glycerol monostearate, 12 g/L agar, and 1000 ml distilled water.
- The liquid additions are supported as liquid volumes: 1 ml/L glycerol, 0.5 ml/L Tween 60, and 10 ml/L whole-fat cow's milk.
- NBRC 1390 and Togo M2080 both instruct sterilization by autoclaving at 110 C for 15 minutes.

Unsupported or incomplete in the generated record:

- Distilled water is represented as `1000 G_PER_L` instead of 1000 ml/L.
- Glycerol, Tween 60, and whole-fat cow's milk are represented as g/L even though the source gives them in ml/L.
- The autoclaving condition is absent.
- NBRC's bibliographic comment is absent from structured references and notes.
- `Glycerol monostearate` is grounded to CHEBI:75456 / 2-stearoylglycerol, which is narrower than the source's generic glycerol monostearate ingredient.

## Completeness

The record preserves the full list of ten source ingredients and the NBRC/Togo source identity. It is incomplete for liquid-vs-mass units, preparation conditions, recoverable references, and the likely yeast/fungal filing context.

Empty optional organism, pH, incubation, and storage fields are acceptable here because NBRC 1390 does not provide those details on the inspected page.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | Four liquid ingredients are represented with mass units. | NBRC 1390 and Togo M2080 list distilled water as 1000 ml, glycerol as 1 ml, Tween 60 as 0.5 ml, and whole-fat cow's milk as 10 ml; the YAML stores each as `G_PER_L`. | `data/normalized_yaml/bacterial/leeming_amp_notman_agar_lna_leeming_amp_notman_1987_in_the_yeasts_a_taxonomic_study_5th_edn.yaml` or the Togo importer |
| Major | The recipe omits the source sterilization condition. | NBRC 1390 and Togo M2080 say to autoclave at 110 C for 15 minutes. | `data/normalized_yaml/bacterial/leeming_amp_notman_agar_lna_leeming_amp_notman_1987_in_the_yeasts_a_taxonomic_study_5th_edn.yaml` |
| Major | The record is filed as `bacterial` without source support. | The NBRC title is Leeming & Notman agar from yeast references, and the inspected source page does not assert bacterial use. | `data/normalized_yaml/bacterial/leeming_amp_notman_agar_lna_leeming_amp_notman_1987_in_the_yeasts_a_taxonomic_study_5th_edn.yaml` |
| Minor | Glycerol monostearate has an over-specific ChEBI mapping. | The source ingredient is generic glycerol monostearate, while the mapped ChEBI label is 2-stearoylglycerol. | `data/normalized_yaml/bacterial/leeming_amp_notman_agar_lna_leeming_amp_notman_1987_in_the_yeasts_a_taxonomic_study_5th_edn.yaml` |
| Minor | Structured references are missing. | The generated reference validator performed zero checks even though the NBRC page provides an NBRC source URL and Leeming/Notman bibliography. | `data/normalized_yaml/bacterial/leeming_amp_notman_agar_lna_leeming_amp_notman_1987_in_the_yeasts_a_taxonomic_study_5th_edn.yaml` |

## Recommended Edits

1. Convert distilled water, glycerol, Tween 60, and whole-fat cow's milk to ml/L quantities in the maintained owner.
2. Add an autoclaving step for 110 C for 15 minutes.
3. Move or reclassify the record from bacterial if curator review confirms that Leeming & Notman agar should be filed under a yeast or fungal category.
4. Replace the over-specific glycerol monostearate grounding with a term that matches the generic source ingredient, or leave it unmapped if no suitable term exists.
5. Add structured Togo M2080, NBRC 1390, and bibliographic references where the schema can represent them.
6. Regenerate `data/merge_yaml/merged/` and downstream pages.

## Follow-up Checks

- Rerun open schema validation, the strict validator, the reference validator, and the term validator on the regenerated YAML.
- Manually compare the regenerated quantities against NBRC 1390 for 1 ml/L glycerol, 0.5 ml/L Tween 60, 10 ml/L whole-fat cow's milk, 1000 ml/L water, and 110 C autoclaving.
- Re-run an ignored-inclusive search for `TOGO:M2080`, `NBRC_M1390`, and the Leeming/Notman slug to confirm only the maintained M2080 owner feeds this generated record.

## Additional Notes

Sibling local records for older and modified Leeming & Notman agar recipes were found by the ignored-inclusive search, but their labels and Togo IDs are distinct from M2080 and they were not conflated into this generated record.
