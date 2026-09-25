# YAML Record Review: Chopped Meat Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.yaml
- Started UTC: 2026-09-22T07:54:47Z
- Finished UTC: 2026-09-22T07:55:43Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:009156 |
| Label | Chopped Meat Medium |
| Generated record | data/merge_yaml/merged/CHOPPED_MEAT_MEDIUM.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml |
| Source | TOGO Medium M2588, DSMZ Medium 78 |

The reviewed file is a generated one-source merge of DSMZ Medium 78 through
TOGO M2588. Future fixes belong in the maintained normalized owner or in the
TOGO/DSMZ importer that handles staged meat-filtrate preparation, source units,
gas phases, pH, and optional agar rather than in the generated merge artifact.

## Validation

| Check | Result |
| --- | --- |
| Open LinkML validation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe` | Passed |
| `scripts/validate_strict.py` on the generated record | Passed; 0 errors in `/private/tmp/CHOPPED_MEAT_MEDIUM.strict.tsv` |
| `linkml-reference-validator validate data` on the generated record | Passed; 0 checks |
| `linkml-term-validator validate-data` on the generated record | Passed |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` objects in a merged YAML file |

The term validator emitted only the expected `eutils/pkg_resources is
deprecated` warning before passing.

## Identity and Grounding

The source identity is correct: `CultureMech:009156`, `TOGO:M2588`, the DSMZ
Medium 78 source URL, the maintained owner stem, and the generated merge
fingerprint all denote DSMZ 78 Chopped Meat Medium.

An ignored-independent `rg --no-ignore --hidden` search across
`data/normalized_yaml` and `data/merge_yaml/merged` for the CultureMech ID, TOGO
M2588 source ID, maintained owner stem, and merge fingerprint found this
generated record, its maintained owner, and normalized index entries. The same
source PDF is intentionally reused by the Vitamin K variants of DSMZ Medium 78.

## Evidence

DSMZ Medium 78 and TOGO M2588 support a chopped-meat medium that first boils
500.0 g fat-free ground beef or horse meat, 1000.0 mL distilled water, and
25.0 mL 1 N NaOH, then cools, skims, filters, retains both meat particles and
filtrate, and restores the filtrate to a final volume of 1000 mL. The source
then adds 30.0 g Casitone, 5.0 g yeast extract, 5.0 g `K2HPO4`, and 1.0 mg
resazurin, boils the medium, cools it under 100% N2, adds 0.5 g/L L-cysteine
hydrochloride, adjusts pH to 7.0, dispenses 7 mL under 100% N2 into anoxic
Hungate-type tubes, and autoclaves at 121 C for 30 minutes. The source also
states that 15.0 g agar per 1000.0 mL should be used for agar slants.

The record flattens the initial chopped-meat filtrate stage into direct
ingredients, so ground beef, water, and NaOH are represented as ordinary final
ingredients. It imports 1000 mL distilled water and 25 mL NaOH as `G_PER_L`,
and it turns the source 1.0 mg resazurin into 1 g/L, a thousand-fold mass error
before considering final-volume semantics.

The source's 100% N2 condition is present only as a variable `N2 gas`
ingredient. The record also includes 15 g/L agar and marks the whole recipe
`SOLID_AGAR`, although DSMZ only specifies agar for agar slants.

The pH 7.0 and all preparation instructions are absent from the generated
record.

## Completeness

The empty `target_organisms` and growth-observation fields are not defects for
this TOGO/DSMZ source record.

The recipe is incomplete until the meat-filtrate stage, source volume and
milligram quantities, optional agar-slant handling, 100% N2 gas phase, pH 7.0,
7 mL Hungate-tube dispensing, meat-particle ratio, and autoclave workflow are
represented.

## Findings

| Severity | Finding |
| --- | --- |
| Major | DSMZ's chopped-meat filtrate stage is flattened into direct final-medium ingredients. **Owner:** `data/normalized_yaml/bacterial/TOGO_M2588_Chopped_Meat_Medium.yaml` or the TOGO/DSMZ importer. |
| Major | Source volume and milligram quantities are imported as `G_PER_L`: 1000 mL water, 25 mL NaOH, and 1 mg resazurin are not gram-per-litre ingredients. **Owner:** the TOGO/DSMZ unit-conversion importer. |
| Major | The base recipe is marked `SOLID_AGAR` and includes 15 g/L agar even though DSMZ specifies agar only for agar slants. **Owner:** the maintained TOGO M2588 normalized owner or the TOGO/DSMZ importer. |
| Major | The 100% N2 gas phase, pH 7.0, 7 mL Hungate-tube dispensing, one-to-four-or-five meat-particle ratio, and 121 C for 30 minutes autoclave workflow are missing. **Owner:** the maintained normalized owner or the TOGO/DSMZ importer. |

## Recommended Edits

1. Model the initial beef-or-horse meat filtrate as a preparation stage instead
   of flat final-medium ingredients.
2. Preserve the source units for water, NaOH, and resazurin, including the
   1.0 mg resazurin quantity.
3. Represent agar as an optional agar-slant addition rather than making the base
   record unconditionally `SOLID_AGAR`.
4. Add pH 7.0, 100% N2 gas handling, Hungate-tube dispensing, meat-particle
   ratio, and 121 C for 30 minutes autoclaving.
5. Regenerate merged YAML after repairing the maintained owner or importer.

## Follow-up Checks

Run the narrow generated-record validators after regeneration:

1. Open LinkML validation against `MediaRecipe`.
2. `scripts/validate_strict.py` on the regenerated record.
3. `linkml-reference-validator validate data` on the regenerated record.
4. `linkml-term-validator validate-data` on the regenerated record.

Then manually compare the regenerated record against TOGO M2588 and the DSMZ
Medium 78 PDF to confirm the staged filtrate, milligram resazurin, optional
agar, 100% N2 gas phase, pH, dispensing, and autoclave claims are source-
faithful.

## Additional Notes

The generated record still carries a legacy `mediaingredientmech_term` for
L-cysteine hydrochloride without a current CHEBI `term`, despite the
`mim-legacy-to-chebi-migration-v1.0` curation event.
