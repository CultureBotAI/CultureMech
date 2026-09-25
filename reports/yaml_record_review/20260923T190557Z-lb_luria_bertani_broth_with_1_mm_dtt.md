# YAML Record Review: LB (Luria-Bertani) Broth With 1 mM DTT

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/lb_luria_bertani_broth_with_1_mm_dtt.yaml
- Started UTC: 2026-09-23T19:04:50Z
- Finished UTC: 2026-09-23T19:05:57Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:010263 |
| Name | lb_luria_bertani_broth_with_1_mm_dtt |
| Original name | LB (Luria-Bertani) Broth With 1 mM DTT |
| Category | bacterial |
| Physical state | LIQUID |
| Media grounding | TOGO:M848 |
| Source provenance | Togo Medium M848 imported from JCM_M813 / GRMD=813 |
| Generated file | data/merge_yaml/merged/lb_luria_bertani_broth_with_1_mm_dtt.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M848_LB_Luria-Bertani_Broth_With_1_mM_DTT.yaml |
| Merge fingerprint | f24f8fdcc4c5fe7a10e320657b80ae94c101788e63e5e0602c3acd16d1c69f74 |

The reviewed file is a generated merged copy. Future fixes belong in the maintained Togo M848 owner or in its linked direct MediaDive J813 source duplicate, followed by regeneration of `data/merge_yaml/merged/` and downstream products.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/lb_luria_bertani_broth_with_1_mm_dtt.yaml`. |
| Strict validator | Passed with zero error rows in `/private/tmp/lb_luria_bertani_broth_with_1_mm_dtt.strict.tsv`. |
| LinkML reference validator | Passed; the reference validator completed with zero checks because this generated record has no `references` collection. |
| LinkML term validator | Passed. |
| Embedded curation history | Not checked: the repository history validator validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

Togo M848 identifies `LB (Luria-Bertani) Broth With 1 mM DTT`, gives the original media ID as `JCM_M813`, records pH 7.0, and lists LB broth with a 1 mM 1,4--dithiothreitol addition. MediaDive J813 agrees on the JCM identity, pH 7.0, a 1 L main solution with BD-Difco tryptone, BD-Difco yeast extract, NaCl, distilled water, and post-autoclave aseptic addition of 1 mM final 1,4-dithiothreitol.

The generated CultureMech ID, name, bacterial category, liquid physical state, and `TOGO:M848` media term all identify the intended source medium. An ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:010263`, `TOGO:M848`, `JCM_M813`, `GRMD=813`, the Togo M848 slug, and the merge fingerprint found the generated target, its maintained owner, validation archive rows, and the direct MediaDive J813 source-duplicate record `data/normalized_yaml/bacterial/lb_luria_bertani_broth_with_1_mm_dtt.yaml`.

## Evidence

Supported in the inspected sources:

- The Togo M848 label, `JCM_M813` provenance, `TOGO:M848` grounding, and pH 7.0 are supported by Togo's M848 API record.
- The five source components are supported by Togo M848: 1 L Distilled water, 10 g NaCl, 5 g Yeast extract (BD-Difco), 10 g Tryptone (BD-Difco), and 1 mM 1,4--dithiothreitol.
- MediaDive J813 supports the same source formula as 10 g/L Tryptone with the BD-Difco attribute, 5 g/L Yeast extract with the BD-Difco attribute, 10 g/L NaCl, 1000 ml distilled water in a 1 L main solution, and post-autoclave addition of 1 mM final 1,4-dithiothreitol.
- MediaDive J813 supports the pH-adjustment and post-autoclave DTT addition steps.

Unsupported or stale in the generated record:

- `Distilled water` is represented as `1 G_PER_L`; the inspected sources encode 1 L / 1000 ml water for a 1 L recipe.
- `1,4--dithiothreitol (DTT)` is represented as `variable VARIABLE`; the inspected sources encode 1 mM final 1,4-dithiothreitol.
- The generated record omits pH 7.0 and the post-autoclave DTT addition step.
- The generated record lacks structured references, even though the maintained owner now records Togo, MediaDive, and JCM source URLs.

The direct JCM `GRMD=813` URL preserved in the record currently returns `Nothing found`, so it remains useful only as historical provenance; Togo M848 and MediaDive J813 are the recoverable source records for the formulation.

## Completeness

The generated merged copy is materially incomplete because it omits the source pH, post-autoclave DTT handling, the supported 1 mM DTT concentration, structured references, and the current cross-link to the direct MediaDive J813 duplicate.

The maintained Togo M848 owner has already been repaired: it now records 1000.0 ml/L water, 1.0 mM 1,4-dithiothreitol with CHEBI:18320, pH 7.0, explicit mixing, pH-adjustment, autoclaving, and post-autoclave DTT addition steps, structured references, and the `SOURCE_DUPLICATE` relationship to the direct MediaDive J813 owner. The generated review target has not been regenerated from that repair.

Empty optional organism, incubation, storage, and discussion fields are acceptable because the inspected medium sources specify a formulation, not strain-level growth outcomes or incubation conditions.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | The generated record is stale and still carries the old Togo-imported water and DTT conversion failures. | Togo M848 encodes 1 L water and 1 mM DTT; MediaDive J813 encodes 1000 ml water and post-autoclave 1 mM final 1,4-dithiothreitol. The generated record still has `1 G_PER_L` for water and `variable VARIABLE` for DTT, while the maintained owner has 1000.0 ml/L water and 1.0 mM DTT. | `data/merge_yaml/merged/` regeneration from `data/normalized_yaml/bacterial/TOGO_M848_LB_Luria-Bertani_Broth_With_1_mM_DTT.yaml` |
| Major | The generated record omits pH 7.0 and the required post-autoclave DTT addition. | Togo M848 carries pH 7.0 and a comment to add 1 mM final DTT after autoclaving; MediaDive J813 carries the same two preparation facts. The maintained Togo M848 owner has already restored both. | `data/merge_yaml/merged/` regeneration from `data/normalized_yaml/bacterial/TOGO_M848_LB_Luria-Bertani_Broth_With_1_mM_DTT.yaml` |
| Minor | The generated record has no structured references or source-duplicate relationship. | The maintained Togo M848 owner has Togo, MediaDive, and JCM references plus `parent_media` pointing at the direct MediaDive J813 import; the generated copy still has only free-text `notes`. | `data/merge_yaml/merged/` regeneration from `data/normalized_yaml/bacterial/TOGO_M848_LB_Luria-Bertani_Broth_With_1_mM_DTT.yaml` |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/` from the maintained normalized corpus so `lb_luria_bertani_broth_with_1_mm_dtt.yaml` receives the September 2026 M848 repair.
2. Regenerate downstream pages and indexes from the refreshed merged YAML so CultureMech:010263 no longer publishes 1 g/L water or a variable placeholder for 1 mM DTT.
3. After regeneration, verify whether the maintained `SOURCE_DUPLICATE` relationship to CultureMech:003157 should remain as a relationship or whether the Togo M848 and MediaDive J813 inputs should collapse to one generated record.

## Follow-up Checks

- Rerun open schema validation, the strict validator, the reference validator, and the term validator on `data/merge_yaml/merged/lb_luria_bertani_broth_with_1_mm_dtt.yaml` after regeneration.
- Manually inspect the regenerated YAML for 1000.0 ml/L water, 1.0 mM DTT, CHEBI:18320, `ph_range` 7.0 to 7.0, the post-autoclave DTT preparation step, and structured source references.
- Re-run an ignored-inclusive search for `TOGO:M848`, `JCM_M813`, and `mediadive.medium:J813` after regeneration to confirm that only the intended source-duplicate records remain.

## Additional Notes

The record passed every focused structural validator because placeholder concentrations and stale generated outputs can remain schema-valid. The source error is visible only by comparing the merged YAML to Togo M848, MediaDive J813, and the September 2026 maintained repair.
