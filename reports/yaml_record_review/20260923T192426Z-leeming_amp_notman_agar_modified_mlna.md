# YAML Record Review: Leeming &amp; Notman agar Modified (MLNA)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/leeming_amp_notman_agar_modified_mlna.yaml
- Started UTC: 2026-09-23T19:23:22Z
- Finished UTC: 2026-09-23T19:24:26Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:008353 |
| Name | leeming_amp_notman_agar_modified_mlna |
| Original name | Leeming &amp; Notman agar Modified (MLNA) |
| Category | bacterial |
| Physical state | SOLID_AGAR |
| Media grounding | TOGO:M1786 |
| Source provenance | Togo M1786 imported from NBRC_M1004 |
| Generated file | data/merge_yaml/merged/leeming_amp_notman_agar_modified_mlna.yaml |
| Maintained owner | data/normalized_yaml/bacterial/leeming_amp_notman_agar_modified_mlna.yaml |
| Merge fingerprint | b73174b097d397d0798b4d49d4b3196ea6d8bb5bdf1fa04568a76f48c54966b1 |

The reviewed target is a generated one-source merge. Future fixes belong in the maintained M1786 normalized owner, followed by regeneration of `data/merge_yaml/merged/` and downstream products.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/leeming_amp_notman_agar_modified_mlna.yaml`. |
| Strict validator | Passed with zero error rows in `/private/tmp/leeming_amp_notman_agar_modified_mlna.strict.tsv`. |
| LinkML reference validator | Passed; the reference validator completed with zero checks because this generated record has no `references` collection. |
| LinkML term validator | Passed. |
| Embedded curation history | Not checked: the repository history validator validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

Togo M1786 and NBRC Medium 1004 both identify the same `Leeming & Notman agar Modified (MLNA)` recipe. The `TOGO:M1786` media term, NBRC 1004 provenance, and solid-agar physical state are internally consistent.

The `bacterial` category is not supported by the inspected source page: NBRC 1004 identifies a modified Leeming & Notman agar formulation and does not assert bacterial use. An ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:008353`, `TOGO:M1786`, `NBRC_M1004`, `NO=1004`, the maintained MLNA slug, and the merge fingerprint found only the reviewed generated record, its maintained owner, source indexes, and archived validation rows for this exact Togo identity.

## Evidence

Supported in the inspected NBRC and Togo sources:

- The Togo/NBRC identity and MLNA label are supported.
- The dry ingredient amounts are supported: 10 g/L bacteriological peptone, 10 g/L glucose, 2 g/L yeast extract, 8 g/L desiccated ox bile, 0.5 g/L glycerol monostearate, and 15 g/L agar.
- The liquid additions are supported as liquid volumes: 10 ml/L glycerol, 20 ml/L olive oil, 5 ml/L Tween 60, and 965 ml/L distilled water.

Unsupported or incomplete in the generated record:

- Distilled water is represented as `965 G_PER_L` instead of 965 ml/L.
- Glycerol, olive oil, and Tween 60 are represented as g/L even though the source gives them in ml/L.
- `Glycerol monostearate` is grounded to CHEBI:75456 / 2-stearoylglycerol, which is narrower than the generic glycerol monostearate ingredient named by NBRC and Togo.
- The record has no structured reference to either Togo M1786 or NBRC 1004.

## Completeness

The record preserves all ten source ingredients and the source identity, but it is incomplete for liquid-vs-mass units, the likely yeast/fungal filing context, and structured references.

Empty optional organism, pH, incubation, storage, and preparation fields are acceptable for this review because NBRC 1004 does not provide those details on the inspected page.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | Four liquid ingredients are represented with mass units. | NBRC 1004 and Togo M1786 list distilled water as 965 ml, glycerol as 10 ml, olive oil as 20 ml, and Tween 60 as 5 ml; the YAML stores each as `G_PER_L`. | `data/normalized_yaml/bacterial/leeming_amp_notman_agar_modified_mlna.yaml` or the Togo importer |
| Major | The record is filed as `bacterial` without source support. | The NBRC and Togo label is Leeming & Notman agar Modified (MLNA), and the inspected NBRC page does not assert bacterial use. | `data/normalized_yaml/bacterial/leeming_amp_notman_agar_modified_mlna.yaml` |
| Minor | Glycerol monostearate has an over-specific ChEBI mapping. | The source ingredient is generic glycerol monostearate, while the mapped ChEBI label is 2-stearoylglycerol. | `data/normalized_yaml/bacterial/leeming_amp_notman_agar_modified_mlna.yaml` |
| Minor | Structured references are missing. | The generated reference validator performed zero checks despite available Togo and NBRC URLs. | `data/normalized_yaml/bacterial/leeming_amp_notman_agar_modified_mlna.yaml` |

## Recommended Edits

1. Convert distilled water, glycerol, olive oil, and Tween 60 to ml/L quantities in the maintained owner.
2. Move or reclassify the record from bacterial if curator review confirms that MLNA should be filed under a yeast or fungal category.
3. Replace the over-specific glycerol monostearate grounding with a term that matches the generic source ingredient, or leave it unmapped if no suitable term exists.
4. Add structured references for Togo M1786 and NBRC 1004.
5. Regenerate `data/merge_yaml/merged/` and downstream pages.

## Follow-up Checks

- Rerun open schema validation, the strict validator, the reference validator, and the term validator on the regenerated YAML.
- Manually compare the regenerated quantities against NBRC 1004 for 10 ml/L glycerol, 20 ml/L olive oil, 5 ml/L Tween 60, and 965 ml/L water.
- Re-run an ignored-inclusive search for `TOGO:M1786`, `NBRC_M1004`, and `b73174b097d397d0798b4d49d4b3196ea6d8bb5bdf1fa04568a76f48c54966b1` to confirm that only the intended MLNA owner feeds this generated record.

## Additional Notes

No pH, sterilization, incubation, storage, or bibliography comment was present on the inspected Togo M1786 or NBRC 1004 pages.
