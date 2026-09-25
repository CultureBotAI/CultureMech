# YAML Record Review: LEUCONOSTOC OENOS medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/leuconostoc_oenos_medium__43e8ebfb.yaml
- Started UTC: 2026-09-23T19:39:59Z
- Finished UTC: 2026-09-23T19:41:17Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:006080 |
| Name | leuconostoc_oenos_medium |
| Original name | LEUCONOSTOC OENOS medium |
| Category | bacterial |
| Physical state | LIQUID |
| Media grounding | komodo.medium:59 |
| Source provenance | KOMODO 59 enriched with DSMZ Medium 59 |
| Generated file | data/merge_yaml/merged/leuconostoc_oenos_medium__43e8ebfb.yaml |
| Maintained owners | data/normalized_yaml/bacterial/KOMODO_59_LEUCONOSTOC_OENOS_medium.yaml; data/normalized_yaml/bacterial/leuconostoc_oenos_medium.yaml |
| Merge fingerprint | 43e8ebfbf69c423aaa8a474c0bf760ffb9401b225b33777bfc4224884153249c |

The reviewed target is a generated two-source merge of a KOMODO 59 owner and its MediaDive DSMZ 59 source-duplicate parent. Future fixes belong in those maintained owners or in merge propagation, followed by regeneration of `data/merge_yaml/merged/` and downstream products.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/leuconostoc_oenos_medium__43e8ebfb.yaml`. |
| Strict validator | Passed with zero error rows in `/private/tmp/leuconostoc_oenos_medium__43e8ebfb.strict.tsv`. |
| LinkML reference validator | Passed; the reference validator completed with zero checks because this generated record has no `references` collection. |
| LinkML term validator | Passed. |
| Embedded curation history | Not checked: the repository history validator validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

KOMODO 59 points at DSMZ Medium 59, and the maintained KOMODO owner already marks the MediaDive DSMZ 59 owner as its `SOURCE_DUPLICATE` parent. The generated file preserves that source-duplicate relation.

An ignored-inclusive exact search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:006080`, `komodo.medium:59`, `mediadive.medium:59`, the maintained filename, the shared slug, and the merge fingerprint found this generated record, its KOMODO owner, its MediaDive DSMZ 59 parent, related Togo/JCM/NBRC Leuconostoc oenos records, generated siblings, source indexes, and an archived source-duplicate review that already paired the KOMODO and DSMZ owners.

## Evidence

Supported in the inspected DSMZ PDF and MediaDive source:

- The DSMZ 59 / KOMODO 59 identity and LEUCONOSTOC OENOS MEDIUM label are supported.
- The dry ingredient quantities are supported: 10 g casein peptone tryptic digest, 5 g yeast extract, 10 g glucose, 5 g fructose, 0.2 g MgSO4 x 7 H2O, 0.05 g MnSO4 x H2O, 3.5 g ammonium citrate, and 0.5 g cysteine-HCl x H2O in a 1001 ml recipe.
- The liquid additions are supported as 1 ml Tween 80, 100 ml filtered tomato juice, and 900 ml distilled water.
- DSMZ and MediaDive both give pH 4.8.
- The KOMODO owner correctly records that it is a source duplicate of the MediaDive DSMZ 59 owner.

Unsupported or incomplete in the generated record:

- The explicit 900 ml distilled water row is absent.
- Tween 80 and tomato juice are represented as `G_PER_L` even though the source gives them as ml additions.
- The source pH 4.8 adjustment is represented as `ph_value` but has not propagated as a preparation step from the MediaDive owner.
- The record has no structured references for KOMODO 59, MediaDive 59, or DSMZ Medium 59.

## Completeness

The record preserves the DSMZ/KOMODO source-duplicate relationship, pH endpoint, and all non-water source ingredients. It is incomplete for water, liquid-vs-mass units, the pH-adjustment step, and structured references.

Empty optional organism, incubation, storage, and sterilization fields are acceptable for this review because the inspected DSMZ and MediaDive entries do not provide those details.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | Two source volume ingredients are represented with mass units. | DSMZ 59 and MediaDive 59 list Tween 80 as 1 ml and filtered tomato juice as 100 ml; the YAML stores both as `G_PER_L`. | maintained DSMZ/KOMODO owners or the MediaDive importer |
| Minor | The explicit water row is omitted. | DSMZ 59 and MediaDive 59 list 900 ml distilled water, but the generated YAML has no water ingredient. | `data/normalized_yaml/bacterial/leuconostoc_oenos_medium.yaml` or the MediaDive importer |
| Minor | The pH adjustment step was dropped in the generated merge. | The MediaDive DSMZ owner has `Adjust pH to 4.8.` as a preparation step; the generated KOMODO/DSMZ merge has only `ph_value: 4.8`. | merge propagation |
| Minor | Structured references are missing. | The generated reference validator performed zero checks despite available KOMODO, MediaDive, and DSMZ identifiers. | maintained owners |

## Recommended Edits

1. Convert Tween 80 and filtered tomato juice to volume quantities in the maintained DSMZ/KOMODO path.
2. Restore the explicit 900 ml water ingredient or document that water is intentionally represented only by the final volume.
3. Preserve `Adjust pH to 4.8.` as a preparation step when merging the KOMODO source-duplicate child with its MediaDive DSMZ parent.
4. Add structured references for KOMODO 59, MediaDive 59, and DSMZ Medium 59.
5. Regenerate `data/merge_yaml/merged/` and downstream pages.

## Follow-up Checks

- Rerun open schema validation, the strict validator, the reference validator, and the term validator on the regenerated YAML.
- Manually compare the regenerated DSMZ/KOMODO record against DSMZ 59 for 900 ml water, 1 ml Tween 80, 100 ml filtered tomato juice, and pH 4.8.
- Re-run an ignored-inclusive exact search for `komodo.medium:59`, `mediadive.medium:59`, and `43e8ebfbf69c423aaa8a474c0bf760ffb9401b225b33777bfc4224884153249c` to confirm that the intended source-duplicate merge is still the only KOMODO 59 merge.

## Additional Notes

Separate Togo/JCM/NBRC Leuconostoc oenos records share this medium family but differ in exact source identity and some salt or hydrate labels; keep those in a separate reconciliation pass.
