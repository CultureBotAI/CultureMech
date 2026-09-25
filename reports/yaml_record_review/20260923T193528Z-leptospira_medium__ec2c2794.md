# YAML Record Review: LEPTOSPIRA-MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/leptospira_medium__ec2c2794.yaml
- Started UTC: 2026-09-23T19:34:23Z
- Finished UTC: 2026-09-23T19:35:28Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:000549 |
| Name | leptospira_medium |
| Original name | LEPTOSPIRA-MEDIUM |
| Category | bacterial |
| Physical state | SOLID_AGAR |
| Media grounding | mediadive.medium:1113 |
| Source provenance | MediaDive DSMZ Medium 1113 |
| Generated file | data/merge_yaml/merged/leptospira_medium__ec2c2794.yaml |
| Maintained owner | data/normalized_yaml/bacterial/leptospira_medium.yaml |
| Merge fingerprint | ec2c27947dcb0c3af287fdad8ae8aff342bfac2e0a65ec026982f8159c297d8e |

The reviewed target is a generated one-source merge from MediaDive/DSMZ 1113. Future fixes belong in the maintained normalized owner, followed by regeneration of `data/merge_yaml/merged/` and downstream products.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/leptospira_medium__ec2c2794.yaml`. |
| Strict validator | Passed with zero error rows in `/private/tmp/leptospira_medium__ec2c2794.strict.tsv`. |
| LinkML reference validator | Passed; the reference validator completed with zero checks because this generated record has no `references` collection. |
| LinkML term validator | Passed. |
| Embedded curation history | Not checked: the repository history validator validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

MediaDive 1113 and the DSMZ Medium 1113 PDF identify the same solid Leptospira EMJH/agarose formulation. The `mediadive.medium:1113` media term, `SOLID_AGAR` physical state, pH 7.5, and autoclaving/cooling/enrichment steps are internally consistent with the DSMZ PDF.

An ignored-inclusive exact search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:000549`, `mediadive.medium:1113`, `DSMZ_Medium1113`, the shared slug, and the merge fingerprint found this generated record, its maintained MediaDive owner, the Togo M2409 owner for the same DSMZ PDF, separate generated Togo YAML, source indexes, and validation archives. The MediaDive and Togo imports should be merged or linked as source duplicates.

## Evidence

Supported in the inspected DSMZ PDF and MediaDive REST source:

- The DSMZ 1113 / MediaDive 1113 identity and LEPTOSPIRA-MEDIUM label are supported.
- The dry ingredients are supported: 2.3 g/L Leptospira Medium Base EMJH and 1.5 g/L agarose.
- The recipe includes 900 ml/L water and 100 ml/L Leptospira Enrichment EMJH.
- DSMZ and MediaDive specify autoclaving at 121 C for 15 min, cooling to 50-55 C, adding the enrichment to the warm medium, aseptic dispensing, and final pH 7.5 at 25 C.

Unsupported or incomplete in the generated record:

- The 900 ml water row from DSMZ and MediaDive is absent.
- Leptospira Enrichment EMJH is represented as `100 G_PER_L` instead of 100 ml/L.
- The record has no structured reference to MediaDive 1113 or the DSMZ PDF.
- The same DSMZ 1113 identity is split across a separate Togo-derived CultureMech record.

## Completeness

The record preserves the DSMZ/MediaDive identity, pH endpoint, agarose/base powder amounts, and preparation sequence. It is incomplete for the explicit water row, liquid enrichment units, structured references, and local deduplication with Togo M2409.

Empty optional organism, incubation, and storage fields are acceptable for this review because the inspected DSMZ and MediaDive entries do not provide those details.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | Leptospira Enrichment EMJH is represented with a mass unit. | DSMZ 1113 and MediaDive 1113 list 100 ml Leptospira Enrichment EMJH; the YAML stores `100 G_PER_L`. | `data/normalized_yaml/bacterial/leptospira_medium.yaml` or the MediaDive importer |
| Minor | The explicit water ingredient is omitted. | DSMZ 1113 and MediaDive 1113 list 900 ml water, but the generated YAML has no water ingredient. | `data/normalized_yaml/bacterial/leptospira_medium.yaml` or the MediaDive importer |
| Major | The same DSMZ recipe exists as a separate generated Togo record. | `data/merge_yaml/merged/leptospira_medium.yaml` is grounded to Togo M2409 for the same DSMZ PDF. | merge/import deduplication |
| Minor | Structured references are missing. | The generated record has only a free-text DSMZ URL, so the reference validator performed zero source checks. | `data/normalized_yaml/bacterial/leptospira_medium.yaml` |

## Recommended Edits

1. Convert Leptospira Enrichment EMJH to a volume quantity in the maintained DSMZ owner.
2. Restore the explicit 900 ml water ingredient or document that water is intentionally represented only in preparation text.
3. Merge or cross-link the MediaDive 1113 and Togo M2409 records for the same DSMZ PDF.
4. Add structured references for MediaDive 1113 and DSMZ Medium 1113.
5. Regenerate `data/merge_yaml/merged/` and downstream pages.

## Follow-up Checks

- Rerun open schema validation, the strict validator, the reference validator, and the term validator on the regenerated YAML.
- Manually compare the regenerated MediaDive record against the DSMZ 1113 PDF for 900 ml water, 100 ml Leptospira Enrichment EMJH, and final pH 7.5 at 25 C.
- Re-run an ignored-inclusive exact search for `TOGO:M2409`, `mediadive.medium:1113`, and `DSMZ_Medium1113` to confirm that the DSMZ 1113 imports are intentionally merged or linked.

## Additional Notes

The Togo M2409 sibling keeps the 900 ml water row but assigns mass units to both water and Leptospira Enrichment EMJH; use the DSMZ PDF as the source of truth when reconciling the imports.
