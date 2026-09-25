# YAML Record Review: LENTIBACILLUS GANOUSIS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/lentibacillus_ganousis_medium__ca3c47fa.yaml
- Started UTC: 2026-09-23T19:29:47Z
- Finished UTC: 2026-09-23T19:31:23Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:002794 |
| Name | lentibacillus_ganousis_medium |
| Original name | LENTIBACILLUS GANOUSIS MEDIUM |
| Category | bacterial |
| Physical state | LIQUID |
| Media grounding | mediadive.medium:J444 |
| Source provenance | MediaDive JCM Medium J444 |
| Generated file | data/merge_yaml/merged/lentibacillus_ganousis_medium__ca3c47fa.yaml |
| Maintained owner | data/normalized_yaml/bacterial/lentibacillus_ganousis_medium.yaml |
| Merge fingerprint | ca3c47fa1752052ab852c428996a449ef5b2f29abed2b2bc95f061f7c49f6479 |

The reviewed file is a generated one-source merge from MediaDive J444. Future fixes belong in the maintained normalized owner, followed by regeneration of `data/merge_yaml/merged/` and downstream products.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/lentibacillus_ganousis_medium__ca3c47fa.yaml`. |
| Strict validator | Passed with zero error rows in `/private/tmp/lentibacillus_ganousis_medium__ca3c47fa.strict.tsv`. |
| LinkML reference validator | Passed; the reference validator completed with zero checks because this generated record has no `references` collection. |
| LinkML term validator | Passed. |
| Embedded curation history | Not checked: the repository history validator validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

JCM `GRMD=444` and MediaDive J444 identify the same liquid Lentibacillus ganousis medium at pH 7.2. Togo M444 is another import of the same JCM liquid recipe, and Togo M445 is a solid-agar variant generated from JCM's "For preparation of solid medium, add 20.0 g/L agar" instruction.

An ignored-inclusive exact search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:002794`, `mediadive.medium:J444`, `GRMD=444`, the maintained slug, and the merge fingerprint found this generated record, its maintained MediaDive owner, Togo M444 and M445 normalized owners, separate generated files for those Togo records, and source indexes. The liquid Togo M444 recipe is the same JCM liquid formula and should be merged or cross-linked with this MediaDive J444 record.

## Evidence

Supported in the inspected JCM and MediaDive sources:

- The MediaDive J444 and JCM 444 source identities are supported.
- The ingredient list and units are supported: 5 g/L proteose peptone no. 3, 10 g/L yeast extract, 1 g/L glucose, 100 g/L NaCl, 2 g/L KCl, 1 g/L MgSO4 x 7 H2O, 0.36 g/L CaCl2 x 2 H2O, 0.23 g/L NaBr, 0.06 g/L NaHCO3, and 0.2 mg/L FeCl2 x 4 H2O.
- pH 7.2 is supported by MediaDive and the JCM preparation text.
- The optional solid-medium instruction is supported by the JCM preparation text.

Unsupported or incomplete in the generated record:

- The MediaDive import drops the BD-Difco attributes from `Proteose peptone No. 3 (BD-Difco)` and `Yeast extract (BD-Difco)`.
- The duplicate liquid Togo M444 import of the same JCM recipe is not linked or merged with this record.
- The solid Togo M445 agar variant from the same JCM page is not linked to this liquid base.
- The record has no structured references for MediaDive J444 or JCM 444.

## Completeness

The record preserves all ten source ingredient amounts, the pH 7.2 endpoint, and both JCM preparation comments. It is incomplete for local Togo/MediaDive deduplication, solid-variant linkage, structured references, and the BD-Difco qualifiers on the undefined nutrient ingredients.

Empty optional organism, incubation, storage, and sterilization fields are acceptable for this review because the inspected JCM and MediaDive entries do not provide those details.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | The same liquid JCM recipe exists as a separate generated Togo record. | Togo M444 points at JCM `GRMD=444` and captures the same liquid base formula, but it generated `data/merge_yaml/merged/LENTIBACILLUS_GANOUSIS_MEDIUM.yaml` instead of merging with this MediaDive J444 record. | merge/import deduplication |
| Minor | The JCM solid-agar variant is not linked. | Togo M445 represents the JCM 444 solid variant with 20 g/L agar, and the MediaDive J444 record carries that solid-preparation note only as free text. | `data/normalized_yaml/bacterial/lentibacillus_ganousis_medium.yaml` |
| Minor | BD-Difco attributes are missing from two nutrient ingredients. | JCM 444 and MediaDive J444 identify the peptone and yeast extract rows as BD-Difco products; the YAML stores generic `Proteose peptone no. 3` and `Yeast extract`. | `data/normalized_yaml/bacterial/lentibacillus_ganousis_medium.yaml` or the MediaDive importer |
| Minor | Structured references are missing. | The generated reference validator performed zero checks despite available MediaDive and JCM source URLs. | `data/normalized_yaml/bacterial/lentibacillus_ganousis_medium.yaml` |

## Recommended Edits

1. Merge or cross-link the MediaDive J444 and Togo M444 liquid records for the same JCM `GRMD=444` formulation.
2. Link Togo M445 as the solid-agar variant of the JCM 444 liquid base rather than treating it as an unrelated duplicate.
3. Preserve the BD-Difco qualifiers on proteose peptone no. 3 and yeast extract.
4. Add structured references for MediaDive J444 and JCM 444.
5. Regenerate `data/merge_yaml/merged/` and downstream pages.

## Follow-up Checks

- Rerun open schema validation, the strict validator, the reference validator, and the term validator on the regenerated YAML.
- Manually compare the regenerated formula against JCM 444 for 0.2 mg/L FeCl2 x 4 H2O and pH 7.2, because both are easy to corrupt by unit or duplicate-step normalization.
- Re-run an ignored-inclusive exact search for `GRMD=444`, `mediadive.medium:J444`, `TOGO:M444`, and `TOGO:M445` to confirm that the liquid duplicate and solid variant are intentionally related.

## Additional Notes

The two pH 7.2 preparation statements in the generated MediaDive record come directly from JCM and MediaDive J444; they are redundant but source-derived.
