# YAML Record Review: Leptospira-Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/leptospira_medium.yaml
- Started UTC: 2026-09-23T19:32:42Z
- Finished UTC: 2026-09-23T19:34:22Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:008992 |
| Name | leptospira_medium |
| Original name | Leptospira-Medium |
| Category | bacterial |
| Physical state | SOLID_AGAR |
| Media grounding | TOGO:M2409 |
| Source provenance | Togo M2409 imported from DSMZ Medium 1113 |
| Generated file | data/merge_yaml/merged/leptospira_medium.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M2409_Leptospira-Medium.yaml |
| Merge fingerprint | 10a3ecd21d78e9c7c06275311f1e4395ac9f422e495802d7693704d14d57c9cb |

The reviewed target is a generated one-source merge from Togo M2409. Future fixes belong in the maintained Togo normalized owner, followed by regeneration of `data/merge_yaml/merged/` and downstream products.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/leptospira_medium.yaml`. |
| Strict validator | Passed with zero error rows in `/private/tmp/leptospira_medium.strict.tsv`. |
| LinkML reference validator | Passed; this generated record has no `references` collection. |
| LinkML term validator | Passed. |
| Embedded curation history | Not checked: the repository history validator validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

Togo M2409, DSMZ Medium 1113, and MediaDive 1113 all identify the same solid Leptospira EMJH/agarose formulation. The `TOGO:M2409` media term and DSMZ PDF provenance are consistent with the reviewed file.

An ignored-inclusive exact search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:008992`, `TOGO:M2409`, `DSMZ_Medium1113`, the maintained filename, the shared slug, and the merge fingerprint found this Togo record, the separate MediaDive/DSMZ 1113 normalized record `data/normalized_yaml/bacterial/leptospira_medium.yaml`, and separate generated YAML for that same DSMZ recipe. The Togo and MediaDive records should be merged or linked as source duplicates.

## Evidence

Supported in the inspected DSMZ PDF, Togo, and MediaDive sources:

- The DSMZ 1113 / Togo M2409 identity and Leptospira-Medium label are supported.
- The dry ingredients are supported: 2.3 g/L Leptospira Medium Base EMJH and 1.5 g/L agarose.
- The liquid additions are supported as volumes: 900 ml/L water and 100 ml/L Leptospira Enrichment EMJH.
- DSMZ and MediaDive specify autoclaving at 121 C for 15 min, cooling to 50-55 C, adding the enrichment to the warm medium, aseptic dispensing, and final pH 7.5 at 25 C.

Unsupported or incomplete in the generated record:

- Water is represented as `900 G_PER_L` instead of 900 ml/L.
- Leptospira Enrichment EMJH is represented as `100 G_PER_L` instead of 100 ml/L.
- The pH 7.5 endpoint and complete DSMZ preparation instructions are absent.
- The record has no structured reference to Togo M2409 or the DSMZ PDF.
- The same DSMZ 1113 identity is split across a separate MediaDive-derived CultureMech record.

## Completeness

The record preserves all four source ingredients, solid-agar state, and the Togo/DSMZ source identity, but it is incomplete for liquid units, pH, preparation and sterilization, structured references, and local deduplication with the MediaDive DSMZ 1113 record.

Empty optional organism, incubation, and storage fields are acceptable for this review because the inspected DSMZ, Togo, and MediaDive entries do not provide those details.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | Two source volume ingredients are represented with mass units. | DSMZ 1113 and Togo M2409 list 900 ml water and 100 ml Leptospira Enrichment EMJH; the YAML stores both as `G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M2409_Leptospira-Medium.yaml` or the Togo importer |
| Major | pH and preparation instructions are missing. | The DSMZ PDF specifies the boiling, 121 C autoclaving, cooling, enrichment addition, aseptic dispensing, and final pH 7.5 steps; the generated Togo record has no `ph_value` or `preparation_steps`. | `data/normalized_yaml/bacterial/TOGO_M2409_Leptospira-Medium.yaml` |
| Major | The same DSMZ recipe exists as a separate generated record. | `data/merge_yaml/merged/leptospira_medium__ec2c2794.yaml` is grounded to MediaDive 1113 for the same DSMZ PDF. | merge/import deduplication |
| Minor | Structured references are missing. | The generated record has only free-text Togo and DSMZ URLs, so the reference validator performed no source checks. | `data/normalized_yaml/bacterial/TOGO_M2409_Leptospira-Medium.yaml` |

## Recommended Edits

1. Convert water and Leptospira Enrichment EMJH to ml/L quantities in the maintained Togo owner.
2. Add `ph_value: 7.5` and the DSMZ preparation sequence for boiling agarose, autoclaving, cooling, adding enrichment, and aseptic dispensing.
3. Merge or cross-link the Togo M2409 and MediaDive 1113 records for the same DSMZ PDF.
4. Add structured references for Togo M2409 and DSMZ Medium 1113.
5. Regenerate `data/merge_yaml/merged/` and downstream pages.

## Follow-up Checks

- Rerun open schema validation, the strict validator, the reference validator, and the term validator on the regenerated YAML.
- Manually compare the regenerated Togo record against the DSMZ 1113 PDF for 900 ml water, 100 ml Leptospira Enrichment EMJH, and final pH 7.5 at 25 C.
- Re-run an ignored-inclusive exact search for `TOGO:M2409`, `mediadive.medium:1113`, and `DSMZ_Medium1113` to confirm that only intentional source duplicates remain for the DSMZ 1113 recipe.

## Additional Notes

The MediaDive-derived DSMZ 1113 sibling carries the pH and preparation text, but omits the 900 ml water row; use the DSMZ PDF as the source of truth when reconciling the two imports.
