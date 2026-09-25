# YAML Record Review: Chopped Meat Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/chopped_meat_medium__fe8c0373.yaml
- Started UTC: 2026-09-22T08:00:39Z
- Finished UTC: 2026-09-22T08:01:27Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:009849 |
| Label | Chopped Meat Medium |
| Generated record | data/merge_yaml/merged/chopped_meat_medium__fe8c0373.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M461_Chopped_Meat_Medium.yaml |
| Source | TOGO Medium M461, JCM medium 461 |

The reviewed file is a generated one-source merge of the liquid JCM 461 Chopped
Meat Medium through TOGO M461. Future fixes belong in the maintained TOGO/JCM
normalized owner or in the TOGO/JCM importer rather than in the generated merge
artifact.

## Validation

| Check | Result |
| --- | --- |
| Open LinkML validation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe` | Passed |
| `scripts/validate_strict.py` on the generated record | Passed; 0 errors in `/private/tmp/chopped_meat_medium__fe8c0373.strict.tsv` |
| `linkml-reference-validator validate data` on the generated record | Passed; 0 checks |
| `linkml-term-validator validate-data` on the generated record | Passed |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` objects in a merged YAML file |

The term validator emitted only the expected `eutils/pkg_resources is
deprecated` warning before passing.

## Identity and Grounding

The source identity is correct: `CultureMech:009849`, `TOGO:M461`, original
source `JCM_M461`, the JCM GRMD 461 URL, and the generated merge fingerprint
all denote JCM 461 Chopped Meat Medium.

An ignored-independent `rg --no-ignore --hidden` search across
`data/normalized_yaml` and `data/merge_yaml/merged` for the CultureMech ID,
TOGO M461 source ID, original JCM source token, maintained owner stem, and merge
fingerprint found this generated record, its maintained owner, normalized index
entries, and the expected cross-reference from the related JCM carbohydrate
medium.

## Evidence

The JCM 461 page and TOGO M461 support a liquid chopped-meat medium that first
boils 500.0 g fat-free ground beef, 1.0 L distilled water, and 25.0 mL 1 N
NaOH for 15 minutes; cools and filters while retaining both meat particles and
filtrate; and restores the filtrate to 1.0 L. The source then adds 30.0 g
Casitone, 5.0 g Yeast extract, 5.0 g `K2HPO4`, and 1.0 mg resazurin; boils and
cools the medium; adds 0.5 g L-cysteine HCl monohydrate; adjusts to pH 7.0;
dispenses 7 mL into tubes with one part meat particles to 4-5 parts fluid under
an N2 atmosphere; seals with butyl rubber stoppers; and autoclaves at 121 C for
30 minutes.

The record keeps the correct liquid identity and omits the agar-slant option,
but it stores 25 mL NaOH, 1 L water, and 1 mg resazurin as `G_PER_L`. It also
represents the N2 atmosphere as a variable gas ingredient and lacks pH and
preparation steps.

## Completeness

The empty `target_organisms` and growth-observation fields are not defects for
this TOGO/JCM source record.

The recipe is incomplete until source volume and milligram units, pH 7.0, the
staged chopped-meat filtrate, N2 dispensing, butyl-rubber stoppering, and
121 C for 30 minutes autoclaving are represented.

## Findings

| Severity | Finding |
| --- | --- |
| Major | Source volume and milligram quantities are imported as `G_PER_L`, including 25 mL 1 N NaOH, 1 L distilled water, and 1 mg resazurin. **Owner:** `data/normalized_yaml/bacterial/TOGO_M461_Chopped_Meat_Medium.yaml` or the TOGO/JCM unit-conversion importer. |
| Major | The pH 7.0 and all preparation instructions are missing, including filtrate restoration, N2 dispensing, one-to-four-or-five meat-particle ratio, butyl-rubber stoppering, and 121 C for 30 minutes autoclaving. **Owner:** the maintained TOGO M461 normalized owner or the TOGO/JCM importer. |

## Recommended Edits

1. Preserve source volume and mass units for NaOH, water, and resazurin.
2. Add pH 7.0 and source-faithful preparation steps for the meat extraction,
   filtration, final-volume restoration, boiling, N2 dispensing, stoppering,
   and autoclaving workflow.
3. Regenerate merged YAML after repairing the maintained owner or importer.

## Follow-up Checks

Run the narrow generated-record validators after regeneration:

1. Open LinkML validation against `MediaRecipe`.
2. `scripts/validate_strict.py` on the regenerated record.
3. `linkml-reference-validator validate data` on the regenerated record.
4. `linkml-term-validator validate-data` on the regenerated record.

Then manually compare the regenerated record against TOGO M461 and the JCM 461
HTML page to confirm the liquid formula, units, pH, N2 condition, and
preparation workflow are source-faithful.

## Additional Notes

None found.
