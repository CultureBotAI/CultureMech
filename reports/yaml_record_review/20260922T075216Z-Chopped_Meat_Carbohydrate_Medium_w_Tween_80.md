# YAML Record Review: Chopped Meat Carbohydrate Medium w/Tween 80

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/Chopped_Meat_Carbohydrate_Medium_w_Tween_80.yaml
- Started UTC: 2026-09-22T07:50:00Z
- Finished UTC: 2026-09-22T07:52:16Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:009272 |
| Label | Chopped Meat Carbohydrate Medium w/Tween 80 |
| Generated record | data/merge_yaml/merged/Chopped_Meat_Carbohydrate_Medium_w_Tween_80.yaml |
| Maintained owner | data/normalized_yaml/bacterial/chopped_meat_carbohydrate_medium_w_tween_80.yaml |
| Source | TOGO Medium M2721, ATCC Medium 1102 |

The reviewed file is a generated one-source merge of ATCC Medium 1102 through
TOGO M2721. Future fixes belong in the maintained normalized owner or in the
TOGO/ATCC importer that handles staged chopped-meat filtrates, liquid volumes,
and preparation comments rather than in the generated merge artifact.

## Validation

| Check | Result |
| --- | --- |
| Open LinkML validation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe` | Passed |
| `scripts/validate_strict.py` on the generated record | Passed; 0 errors in `/private/tmp/Chopped_Meat_Carbohydrate_Medium_w_Tween_80.strict.tsv` |
| `linkml-reference-validator validate data` on the generated record | Passed; 0 checks |
| `linkml-term-validator validate-data` on the generated record | Passed |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` objects in a merged YAML file |

The term validator emitted only the expected `eutils/pkg_resources is
deprecated` warning before passing.

## Identity and Grounding

The source identity is correct: `CultureMech:009272`, `TOGO:M2721`, the ATCC
PDF token in the source URL, and the generated merge fingerprint all denote
Chopped Meat Carbohydrate Medium w/Tween 80 / ATCC Medium 1102.

An ignored-independent `rg --no-ignore --hidden` search across
`data/normalized_yaml` and `data/merge_yaml/merged` for the CultureMech ID,
TOGO M2721 source ID, normalized owner stem, source URL token, and merge
fingerprint found only this generated record, its maintained owner, and
normalized index entries.

## Evidence

The ATCC Medium 1102 PDF and TOGO M2721 API support a chopped-meat formula that
first boils and clarifies a filtrate from 500.0 g fat-free ground beef, 1000 mL
deionized water, and 25.0 mL 1 N NaOH. The source then restores the filtrate to
1.0 L, adds 30.0 g peptone, 5.0 g yeast extract, 1.0 mL Tween 80, 5.0 g
`K2HPO4`, 4.0 g glucose, 1.0 g cellobiose, 1.0 g maltose, 1.0 g starch,
4.0 mL 0.025% resazurin solution, and optional 15.0 g agar before boiling,
cooling, adding 0.5 g cysteine, setting pH 7.0, anaerobic dispensing in 7 mL
volumes under nitrogen or nitrogen:hydrogen gas, stoppering, and autoclaving at
121 C for 15 minutes.

The record imports the medium as one flat ingredient list. That flattens the
initial meat-filtrate stage into direct parent ingredients and loses the
distinction between the retained filtrate, the final supplements, and the
optional use of one part meat particles per 4-5 parts broth.

The importer also converts liquid additions to grams per litre: 25 mL NaOH,
1000 mL deionized water, 1 mL Tween 80, and 4 mL 0.025% resazurin solution are
all present with `unit: G_PER_L`. The source's pH and preparation workflow are
not represented in the generated record.

## Completeness

The empty `target_organisms` and growth-observation fields are not defects for
this ATCC source record.

The recipe is incomplete until the ATCC meat-filtrate preparation is separated
from final supplements, source liquid volumes are preserved, optional agar and
meat-particle handling are represented, pH 7.0 is added, and the full
anaerobic dispensing, stoppering, and autoclave workflow is captured.

## Findings

| Severity | Finding |
| --- | --- |
| Major | The initial ATCC chopped-meat filtrate is flattened into direct parent ingredients, so ground beef, NaOH, and water appear as if they were ordinary final-medium ingredients. **Owner:** the TOGO M2721 normalized owner or the TOGO/ATCC importer. |
| Major | Source millilitre additions are imported as `G_PER_L`, affecting NaOH, deionized water, Tween 80, and 0.025% resazurin solution. **Owner:** the TOGO/ATCC unit-conversion importer. |
| Major | pH 7.0 and the source preparation workflow are missing, including fat removal, filtration, volume restoration, anaerobic 7 mL dispensing, rubber stoppers, 121 C autoclaving, and optional meat-particle handling. **Owner:** the maintained TOGO M2721 normalized owner or the TOGO/ATCC importer. |

## Recommended Edits

1. Model ATCC Medium 1102 as a staged chopped-meat filtrate with later Tween 80,
   sugar, starch, resazurin, cysteine, and optional agar additions.
2. Convert liquid quantities to source-faithful volume units for 25 mL NaOH,
   1000 mL deionized water, 1 mL Tween 80, and 4 mL resazurin solution.
3. Add pH 7.0 and preparation steps for the boil, fat removal, filtration,
   volume restoration, cysteine addition, anaerobic dispensing, rubber
   stoppers, autoclaving, and optional meat-particle ratio.
4. Regenerate merged YAML after repairing the maintained owner or importer.

## Follow-up Checks

Run the narrow generated-record validators after regeneration:

1. Open LinkML validation against `MediaRecipe`.
2. `scripts/validate_strict.py` on the regenerated record.
3. `linkml-reference-validator validate data` on the regenerated record.
4. `linkml-term-validator validate-data` on the regenerated record.

Then manually compare the regenerated record against TOGO M2721 and the ATCC
Medium 1102 PDF to confirm that the staged filtrate, volume units, pH, and
anaerobic preparation instructions match the source.

## Additional Notes

None found.
