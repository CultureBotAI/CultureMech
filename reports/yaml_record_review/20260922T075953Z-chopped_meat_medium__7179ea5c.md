# YAML Record Review: Chopped Meat Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/chopped_meat_medium__7179ea5c.yaml
- Started UTC: 2026-09-22T07:59:09Z
- Finished UTC: 2026-09-22T07:59:54Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:009850 |
| Label | Chopped Meat Medium |
| Generated record | data/merge_yaml/merged/chopped_meat_medium__7179ea5c.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M462_Chopped_Meat_Medium.yaml |
| Source | TOGO Medium M462, JCM medium 461 |

The reviewed file is a generated one-source merge of JCM 461 through TOGO M462.
Future fixes belong in the maintained TOGO/JCM normalized owner or in the
TOGO/JCM importer rather than in the generated merge artifact.

## Validation

| Check | Result |
| --- | --- |
| Open LinkML validation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe` | Passed |
| `scripts/validate_strict.py` on the generated record | Passed; 0 errors in `/private/tmp/chopped_meat_medium__7179ea5c.strict.tsv` |
| `linkml-reference-validator validate data` on the generated record | Passed; 0 checks |
| `linkml-term-validator validate-data` on the generated record | Passed |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` objects in a merged YAML file |

The term validator emitted only the expected `eutils/pkg_resources is
deprecated` warning before passing.

## Identity and Grounding

The source identity is correct: `CultureMech:009850`, `TOGO:M462`, original
source `JCM_M461-2`, the JCM GRMD 461 URL, and the generated merge fingerprint
all denote JCM 461 Chopped Meat Medium.

An ignored-independent `rg --no-ignore --hidden` search across
`data/normalized_yaml` and `data/merge_yaml/merged` for the CultureMech ID,
TOGO M462 source ID, original JCM source token, maintained owner stem, and merge
fingerprint found this generated record, its maintained owner, normalized index
entries, and the expected TOGO M463 note that references JCM medium 462.

## Evidence

The JCM 461 page and TOGO M462 support a medium that first boils 500.0 g
fat-free ground beef, 1.0 L distilled water, and 25.0 mL 1 N NaOH for
15 minutes; cools and filters while retaining both meat particles and filtrate;
and restores the filtrate to 1.0 L. The source then adds 30.0 g Casitone, 5.0 g
Yeast extract, 5.0 g `K2HPO4`, and 1.0 mg resazurin; boils and cools the
medium; adds 0.5 g L-cysteine HCl monohydrate; adjusts to pH 7.0; dispenses
7 mL into tubes with one part meat particles to 4-5 parts fluid under an N2
atmosphere; seals with butyl rubber stoppers; autoclaves at 121 C for
30 minutes; and uses 15 g agar per 1 L only for agar slants.

The record stores 25 mL NaOH, 1 L water, and 1 mg resazurin as `G_PER_L`. It
also represents the N2 atmosphere as a variable gas ingredient, has no pH or
preparation steps, and promotes agar to an unconditional ingredient with
`physical_state: SOLID_AGAR` even though the source says agar is for agar
slants.

## Completeness

The empty `target_organisms` and growth-observation fields are not defects for
this TOGO/JCM source record.

The recipe is incomplete until source volume and milligram units, pH 7.0, the
staged chopped-meat filtrate, N2 dispensing, butyl-rubber stoppering, 121 C for
30 minutes autoclaving, and optional agar-slant handling are represented.

## Findings

| Severity | Finding |
| --- | --- |
| Major | Source volume and milligram quantities are imported as `G_PER_L`, including 25 mL 1 N NaOH, 1 L distilled water, and 1 mg resazurin. **Owner:** `data/normalized_yaml/bacterial/TOGO_M462_Chopped_Meat_Medium.yaml` or the TOGO/JCM unit-conversion importer. |
| Major | The base recipe is marked `SOLID_AGAR` and contains agar even though JCM specifies agar only for agar slants. **Owner:** the maintained TOGO M462 normalized owner or the TOGO/JCM importer. |
| Major | The pH 7.0 and all preparation instructions are missing, including filtrate restoration, N2 dispensing, one-to-four-or-five meat-particle ratio, butyl-rubber stoppering, and 121 C for 30 minutes autoclaving. **Owner:** the maintained TOGO M462 normalized owner or the TOGO/JCM importer. |

## Recommended Edits

1. Preserve source volume and mass units for NaOH, water, and resazurin.
2. Move agar out of the unconditional base recipe and represent it as an
   agar-slant option.
3. Add pH 7.0 and source-faithful preparation steps for the meat extraction,
   filtration, final-volume restoration, boiling, N2 dispensing, stoppering,
   and autoclaving workflow.
4. Regenerate merged YAML after repairing the maintained owner or importer.

## Follow-up Checks

Run the narrow generated-record validators after regeneration:

1. Open LinkML validation against `MediaRecipe`.
2. `scripts/validate_strict.py` on the regenerated record.
3. `linkml-reference-validator validate data` on the regenerated record.
4. `linkml-term-validator validate-data` on the regenerated record.

Then manually compare the regenerated record against TOGO M462 and the JCM 461
HTML page to confirm the units, pH, N2 condition, agar handling, and preparation
workflow are source-faithful.

## Additional Notes

None found.
