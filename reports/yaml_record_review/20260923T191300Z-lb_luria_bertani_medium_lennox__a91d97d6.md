# YAML Record Review: LB (Luria-Bertani) Medium (Lennox)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/lb_luria_bertani_medium_lennox__a91d97d6.yaml
- Started UTC: 2026-09-23T19:11:56Z
- Finished UTC: 2026-09-23T19:13:00Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:007864 |
| Name | lb_luria_bertani_medium_lennox |
| Original name | LB (Luria-Bertani) Medium (Lennox) |
| Category | bacterial |
| Physical state | LIQUID |
| Media grounding | TOGO:M1329 |
| Source provenance | Togo Medium M1329 imported from JCM_M1236 / GRMD=1236 |
| Generated file | data/merge_yaml/merged/lb_luria_bertani_medium_lennox__a91d97d6.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M1329_LB_Luria-Bertani_Medium_Lennox.yaml |
| Merge fingerprint | a91d97d67b6854837fbd7d2074adc31888886642fd8e8368bfee7b8a2f63d465 |

The reviewed target is a generated merged record from a single Togo M1329 owner. Future fixes belong in that maintained owner, followed by regeneration of `data/merge_yaml/merged/` and downstream products.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/lb_luria_bertani_medium_lennox__a91d97d6.yaml`. |
| Strict validator | Passed with zero error rows in `/private/tmp/lb_luria_bertani_medium_lennox__a91d97d6.strict.tsv`. |
| LinkML reference validator | Passed; the reference validator completed with zero checks because this generated record has no `references` collection. |
| LinkML term validator | Passed. |
| Embedded curation history | Not checked: the repository history validator validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

Togo M1329 identifies the liquid `LB (Luria-Bertani) Medium (Lennox)` recipe from JCM_M1236. Its inspected source payload lists 1 L distilled water, 5 g NaCl, 5 g Yeast extract (BD-Difco), 10 g Tryptone (BD-Difco), and pH 7.0, with an instruction that solid medium is prepared by adding 15.0 g/L agar. MediaDive J1236 agrees on the JCM identity, liquid base ingredients, 5 g/L NaCl, pH 7.0, and the solid-medium agar addendum.

The generated `CultureMech:007864` record preserves the liquid Lennox identity and the 5 g/L NaCl level. It is distinct from the Togo M1330 solid Lennox record and the local MediaDive J1236 import, which represent the same JCM source with the solid-medium agar condition exposed differently.

An ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:007864`, `TOGO:M1329`, `JCM_M1236`, `GRMD=1236`, the Togo M1329 slug, and the merge fingerprint found the reviewed generated record, its maintained Togo owner, the direct MediaDive J1236 normalized record, the related solid Togo M1330 owner, source indexes, and archived validation rows.

## Evidence

Supported in the inspected sources:

- The M1329 label, JCM_M1236 provenance, `TOGO:M1329` grounding, and pH 7.0 are supported by the Togo M1329 API record.
- The liquid base composition is supported by Togo M1329 and MediaDive J1236: 1 L or 1000 ml water, 5 g/L NaCl, 5 g/L Yeast extract with the BD-Difco attribute, and 10 g/L Tryptone with the BD-Difco attribute.
- The generated record's `LIQUID` physical state is appropriate for M1329 because the source keeps the 15 g/L agar as a conditional addition for solid medium rather than a base ingredient.

Unsupported or incomplete in the generated record:

- `Distilled water` is represented as `1 G_PER_L`, but Togo M1329 lists 1 L water and MediaDive J1236 lists 1000 ml water.
- The generated record omits pH 7.0 and the source instruction for preparing solid medium by adding 15.0 g/L agar.
- The generated record omits structured Togo and JCM/MediaDive references.

The current direct JCM URL for GRMD=1236 was not rechecked in this review; Togo M1329 and MediaDive J1236 were sufficient to verify the recoverable formulation.

## Completeness

The generated record is complete enough for the liquid Lennox identity, category, physical state, salt concentration, undefined complex nutrients, and ChEBI grounding for water and sodium chloride. It is materially incomplete for the water unit, pH, conditional solid-medium preparation instruction, structured references, and source-duplicate relationship to MediaDive J1236.

The direct MediaDive J1236 normalized record already contains `ph_value: 7.0` and the solid-medium agar instruction, but it omits the 1000 ml water row and has not been linked to the Togo M1329 owner. Empty optional organism, incubation, and storage fields are acceptable because the inspected sources are formulation records.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | The maintained Togo owner and generated record convert 1 L distilled water to `1 G_PER_L`. | Togo M1329 lists 1 L distilled water; MediaDive J1236 lists 1000 ml distilled water in a 1 L main solution. | `data/normalized_yaml/bacterial/TOGO_M1329_LB_Luria-Bertani_Medium_Lennox.yaml` or the Togo importer |
| Major | The maintained Togo owner and generated record omit pH 7.0 and the conditional solid-medium agar instruction. | Togo M1329 and MediaDive J1236 both carry pH 7.0 and the instruction to add 15.0 g/L agar for solid medium. | `data/normalized_yaml/bacterial/TOGO_M1329_LB_Luria-Bertani_Medium_Lennox.yaml` |
| Minor | The record has only free-text provenance and no structured references or source-duplicate relationship. | The generated reference validator performed zero checks; an exact ignored-inclusive search found the direct MediaDive J1236 owner for the same JCM source. | `data/normalized_yaml/bacterial/TOGO_M1329_LB_Luria-Bertani_Medium_Lennox.yaml` |

## Recommended Edits

1. Correct M1329 distilled water to 1000 ml/L in the maintained owner, or fix the Togo importer if 1 L water is systematically becoming 1 g/L.
2. Add pH 7.0 and preserve the conditional `15.0 g/L agar` solid-medium instruction without changing the base M1329 physical state from liquid.
3. Add structured source references and link Togo M1329 to the MediaDive J1236 import as the same liquid Lennox JCM source.
4. Regenerate `data/merge_yaml/merged/` and downstream pages.

## Follow-up Checks

- Rerun open schema validation, the strict validator, the reference validator, and the term validator on `data/merge_yaml/merged/lb_luria_bertani_medium_lennox__a91d97d6.yaml` after regeneration.
- Manually compare the regenerated M1329 record with Togo M1329 and MediaDive J1236 for 5 g/L NaCl, 1000 ml/L distilled water, pH 7.0, and the retained conditional agar instruction.
- Re-run an ignored-inclusive search for `TOGO:M1329`, `mediadive.medium:J1236`, and `TOGO:M1330` to confirm that the liquid and solid Lennox views are intentionally linked rather than accidentally merged.

## Additional Notes

Unlike the sibling generated Lennox merge under fingerprint `6b5c3f0c...`, this record has not absorbed high-salt or one-third LB variants. Its defects are confined to the stale one-source Togo import.
