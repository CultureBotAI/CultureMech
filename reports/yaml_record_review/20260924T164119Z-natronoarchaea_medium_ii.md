# YAML Record Review: NATRONOARCHAEA MEDIUM II

- Repository: CultureMech
- Record: data/merge_yaml/merged/natronoarchaea_medium_ii.yaml
- Started UTC: 2026-09-24T16:41:19Z
- Finished UTC: 2026-09-24T16:41:19Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:015832` for direct JCM `GRMD=1334`, `NATRONOARCHAEA MEDIUM II`.

## Validation

Open schema validation passed with no issues.

Strict validation passed with 0 errors; the strict TSV contained only the header row.

Reference validation passed with 0 checks.

Term validation passed.

Embedded `curation_history` was not checked: `just validate-history` validates the standalone `history/` tree, not `MediaRecipe.curation_history` inside merged generated YAML.

## Identity and Grounding

The record is grounded to the intended direct JCM `GRMD=1334` source with `jcm.grmd:1334`.

An exact repository search including ignored files for `CultureMech:015832`, `JCM_J1334_NATRONOARCHAEA_MEDIUM_II`, `jcm.grmd:1334`, `GRMD=1334`, and `natronoarchaea_medium_ii` found only the direct JCM owner and this generated record among normalized and merged YAML.

## Evidence

JCM Medium 1334 composes the medium from 750 ml Neutral base salt medium and 250 ml Base soda medium from JCM Medium 1207. It mixes the two media after separate autoclaving and aseptically adds 1 ml 1 M MgCl2, 5 ml Trace vitamins from JCM Medium 197, 1 ml Trace element solution from JCM Medium 1079, 0.5 ml Se/W solution from JCM Medium 852, 0.2 ml 10% yeast extract, and 10 ml 10% soluble starch.

JCM Medium 1334 defines Neutral base salt medium per 1 L as 240 g NaCl, 5 g KCl, 2.5 g K2HPO4, 0.4 g NH4Cl, and 0.1 g (NH4)2SO4, with pH adjusted to 7.0 using 0.5 M K2HPO4 before autoclaving.

JCM Medium 1207 defines Base soda medium per 1 L as 190 g Na2CO3, 30 g NaHCO3, 16 g NaCl, and 1 g K2HPO4 brought to volume with water and autoclaved.

JCM Medium 852 defines Se/W solution per 1 L as 1.7 mg Na2SeO3 x 5H2O and 3.3 mg Na2WO4 x 2H2O in water.

The normalized owner keeps `ingredients: []` and represents Neutral base salt medium, Base soda medium, MgCl2, Trace vitamins, Trace element solution, Se/W solution, yeast extract, and soluble starch as solution additions.

## Completeness

The generated record has no `solutions` array. It emits the top-level solution additions as direct ingredients, then emits the Neutral base salt medium internals as additional direct ingredients, losing the parent-child relationship and the Neutral base water row.

The generated record does not contain the nested compositions for 1 M MgCl2, 10% yeast extract, or 10% soluble starch that are present in the normalized owner. It also does not expand Base soda medium, JCM 197 Trace vitamins, JCM 1079 Trace element solution, or JCM 852 Se/W solution.

## Findings

- Generated merge output flattened `Neutral base salt medium` into sibling direct ingredients while retaining the 750 ml/L stock itself as a direct ingredient.
- Nested solution compositions present in the normalized owner were lost for 1 M MgCl2, 10% yeast extract, and 10% soluble starch.
- The 250 ml/L Base soda medium, 5 ml/L Trace vitamins, 1 ml/L Trace element solution, and 0.5 ml/L Se/W solution cross-references remain bare labels with no structured links or nested compositions.
- The Neutral base water row is missing, so the source's "bring volume to 1.0 L" fact is not represented.

## Recommended Edits

- Fix generation or merge handling so `solutions` stay nested instead of being flattened into `ingredients`.
- Preserve the MgCl2, yeast extract, and soluble starch subcomposition from `JCM_J1334_NATRONOARCHAEA_MEDIUM_II.yaml` in generated output.
- Curate or link the referenced JCM 1207, JCM 1079, JCM 852, and JCM 197 stock compositions so the generated record does not contain unresolved source-medium labels.
- Add the missing water row for the Neutral base salt medium.

## Follow-up Checks

- Regenerate `data/merge_yaml/merged/natronoarchaea_medium_ii.yaml` and verify it has a populated `solutions` array with Neutral base salt medium nested under the 750 ml/L addition.
- Re-run open schema, strict, reference, and term validation after curation.
- Search including ignored files for `GRMD=1334` and `jcm.grmd:1334` to confirm the direct JCM owner remains unique.

## Additional Notes

None found.
