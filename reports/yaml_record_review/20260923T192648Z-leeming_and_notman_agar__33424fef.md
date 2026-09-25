# YAML Record Review: LEEMING AND NOTMAN AGAR

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/leeming_and_notman_agar__33424fef.yaml
- Started UTC: 2026-09-23T19:24:27Z
- Finished UTC: 2026-09-23T19:26:48Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:002512 |
| Name | leeming_and_notman_agar |
| Original name | LEEMING AND NOTMAN AGAR |
| Category | bacterial |
| Physical state | SOLID_AGAR |
| Media grounding | mediadive.medium:J153 |
| Source provenance | MediaDive JCM Medium J153 |
| Generated file | data/merge_yaml/merged/leeming_and_notman_agar__33424fef.yaml |
| Maintained owner | data/normalized_yaml/bacterial/leeming_and_notman_agar.yaml |
| Merge fingerprint | 33424fefd3be01b798b2adb03b0673f9ef2465275082cb88ca934094d4921e6a |

The reviewed file is a generated one-source merge from the MediaDive JCM 153 import. Future fixes belong in `data/normalized_yaml/bacterial/leeming_and_notman_agar.yaml`, followed by regeneration of `data/merge_yaml/merged/` and downstream products.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/leeming_and_notman_agar__33424fef.yaml`. |
| Strict validator | Passed with zero error rows in `/private/tmp/leeming_and_notman_agar__33424fef.strict.tsv`. |
| LinkML reference validator | Passed; the reference validator completed with zero checks because this generated record has no `references` collection. |
| LinkML term validator | Passed. |
| Embedded curation history | Not checked: the repository history validator validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

JCM `GRMD=153`, MediaDive J153, and Togo M144 all identify the same Leeming and Notman agar recipe. The solid-agar physical state, MediaDive grounding, JCM link, and `110C for 15 min` autoclave step are internally consistent.

The `bacterial` category is not supported by the inspected JCM, MediaDive, or Togo source pages: they identify Leeming and Notman agar but do not assert bacterial use. An ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:002512`, `mediadive.medium:J153`, `JCM Medium J153`, `GRMD=153`, the maintained slug, and the merge fingerprint found this generated record, its maintained owner, source indexes, and a separate Togo M144 import of the same JCM `GRMD=153` recipe in `data/merge_yaml/merged/LEEMING_AND_NOTMAN_AGAR.yaml`.

## Evidence

Supported in the inspected JCM, MediaDive, and Togo sources:

- The JCM 153, MediaDive J153, and Togo M144 source identities are supported.
- The mass ingredients match MediaDive's per-final-volume conversions: Bacto peptone 9.88142 g/L, glucose 4.94071 g/L, yeast extract 0.0988142 g/L, oxgall 7.90514 g/L, glycerol monostearate 0.494071 g/L, and agar 11.8577 g/L.
- The volume ingredients are source-supported as 1 ml glycerol, 0.5 ml Tween 60, and 10 ml whole-fat cow's milk in the recipe containing 1 L distilled water.
- JCM and MediaDive both instruct autoclaving at 110C for 15 min.

Unsupported or incomplete in the generated record:

- Glycerol, Tween 60, and cow's milk are stored as `G_PER_L` even though JCM, MediaDive, and Togo give these additions as liquid volumes.
- The explicit distilled water source row is absent.
- The cow's milk row drops the source's `whole fat` qualifier.
- `Glycerol monostearate` is grounded to CHEBI:75456 / 2-stearoylglycerol, which is narrower than the generic glycerol monostearate ingredient named by JCM, MediaDive, and Togo.
- The record has no structured reference to MediaDive J153, JCM 153, or the equivalent Togo M144 record.

## Completeness

The record preserves the MediaDive identity, nine non-water ingredients, and autoclave step. It is incomplete for liquid-vs-mass units, the explicit water addition, the whole-fat milk qualifier, structured references, and local deduplication against the Togo M144 import of the same JCM recipe.

Empty optional organism, pH, incubation, and storage fields are acceptable for this review because the inspected JCM, MediaDive, and Togo source entries do not provide those details.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | Three liquid ingredients are represented with mass units. | JCM 153, MediaDive J153, and Togo M144 list glycerol, Tween 60, and whole-fat cow's milk in ml, but the YAML stores each as `G_PER_L`. | `data/normalized_yaml/bacterial/leeming_and_notman_agar.yaml` or the MediaDive importer |
| Major | The same JCM recipe exists as a separate generated CultureMech record. | The ignored-inclusive search found Togo M144 and `data/merge_yaml/merged/LEEMING_AND_NOTMAN_AGAR.yaml`, which also points at JCM `GRMD=153`; it did not merge with this MediaDive J153 record. | merge/import deduplication |
| Major | The record is filed as `bacterial` without source support. | The inspected JCM, MediaDive, and Togo records identify Leeming and Notman agar and do not assert bacterial use. | `data/normalized_yaml/bacterial/leeming_and_notman_agar.yaml` |
| Minor | The explicit source water ingredient is omitted. | JCM 153 lists 1 L distilled water and Togo M144 captures that row; this MediaDive-derived YAML has no water ingredient. | `data/normalized_yaml/bacterial/leeming_and_notman_agar.yaml` or the MediaDive importer |
| Minor | The whole-fat milk qualifier is dropped. | JCM 153 and MediaDive J153 list cow's milk with the whole-fat qualifier; the YAML stores only `Cow's milk`. | `data/normalized_yaml/bacterial/leeming_and_notman_agar.yaml` or the MediaDive importer |
| Minor | Glycerol monostearate has an over-specific ChEBI mapping. | The source ingredient is generic glycerol monostearate, while the mapped ChEBI label is 2-stearoylglycerol. | `data/normalized_yaml/bacterial/leeming_and_notman_agar.yaml` |
| Minor | Structured references are missing. | The generated reference validator performed zero checks despite available MediaDive, JCM, and Togo source identifiers. | `data/normalized_yaml/bacterial/leeming_and_notman_agar.yaml` |

## Recommended Edits

1. Convert glycerol, Tween 60, and whole-fat cow's milk to volume quantities in the maintained owner.
2. Preserve the explicit distilled water ingredient or document that MediaDive imports intentionally normalize against final volume while omitting water.
3. Merge or cross-link the MediaDive J153 and Togo M144 records for the same JCM `GRMD=153` recipe.
4. Move or reclassify the record from bacterial if curator review confirms that Leeming and Notman agar should be filed under a yeast or fungal category.
5. Preserve the `whole fat` qualifier on cow's milk.
6. Replace the over-specific glycerol monostearate grounding with a term that matches the generic source ingredient, or leave it unmapped if no suitable term exists.
7. Add structured references for MediaDive J153, JCM 153, and Togo M144.
8. Regenerate `data/merge_yaml/merged/` and downstream pages.

## Follow-up Checks

- Rerun open schema validation, the strict validator, the reference validator, and the term validator on the regenerated YAML.
- Manually compare the regenerated quantities against JCM 153 and MediaDive J153 for 1 ml glycerol, 0.5 ml Tween 60, 10 ml whole-fat cow's milk, 1 L distilled water, and autoclaving at 110C for 15 min.
- Re-run an ignored-inclusive search for `GRMD=153`, `mediadive.medium:J153`, and `TOGO:M144` to confirm that the MediaDive and Togo imports are intentionally merged or linked.

## Additional Notes

The Togo M144 sibling preserves original ingredient amounts and source labels more closely than the MediaDive-derived record, but also maps the volume rows to `G_PER_L`; use the JCM source or MediaDive REST amounts, not the Togo-derived unit enums, when repairing liquid concentrations.
