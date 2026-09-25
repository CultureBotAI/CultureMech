# YAML Record Review: Cytophaga Hutchinsonii Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/cytophaga_hutchinsonii_medium__b6268d2c.yaml
- Started UTC: 2026-09-22T13:00:58Z
- Finished UTC: 2026-09-22T13:03:59Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:008924 |
| Name | cytophaga_hutchinsonii_medium |
| Source | TOGO Medium M2337 / DSMZ Medium 160 |
| Media term | TOGO:M2337, Cytophaga Hutchinsonii Medium |
| Generated record | data/merge_yaml/merged/cytophaga_hutchinsonii_medium__b6268d2c.yaml |
| Maintained input | data/normalized_yaml/bacterial/TOGO_M2337_Cytophaga_Hutchinsonii_Medium.yaml |

The generated record is a stale single-source copy of a TOGO/DSMZ input that
was repaired on 2026-09-11. Future repair should regenerate this merged output
from the maintained M2337 source state.

## Validation

| Check | Result |
|---|---|
| LinkML open-schema validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/cytophaga_hutchinsonii_medium__b6268d2c.yaml` | Passed |
| Closed-schema validation, `python scripts/validate_strict.py data/merge_yaml/merged/cytophaga_hutchinsonii_medium__b6268d2c.yaml --out /private/tmp/cytophaga_hutchinsonii_medium__b6268d2c.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 error rows |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/cytophaga_hutchinsonii_medium__b6268d2c.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/cytophaga_hutchinsonii_medium__b6268d2c.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history validation | Not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML |

The passing validators prove that the generated YAML is schema-shaped. They do
not detect that water is represented with a mass unit or that the output
predates the repaired normalized record.

## Identity and Grounding

The record identity is correct. `CultureMech:008924` denotes TOGO Medium M2337,
which imports DSMZ Medium 160, `CYTOPHAGA HUTCHINSONII MEDIUM`. The live TOGO
M2337 API points to `DSMZ_Medium160.pdf`, and the DSMZ PDF confirms that medium
160 is a Cytophaga hutchinsonii medium that adds cellobiose to DSMZ Medium 67
or uses agar-free DSMZ 67 with filter paper.

A gitignore-independent search with `rg --no-ignore --hidden` over
`data/normalized_yaml`, `data/raw`, and the generated target found the
maintained TOGO M2337 input, this generated record, and the older DSMZ-derived
`data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml`. The same
search found no exact raw capture for `TOGO:M2337` or `DSMZ_Medium160` under
`data/raw`.

The supported exact small-molecule groundings are water, calcium chloride
dihydrate, and cellobiose. Casitone and yeast extract are complex components
and are allowed to remain without ChEBI terms.

## Evidence

DSMZ Medium 160 adds 0.5% filter-sterilized cellobiose to DSMZ Medium 67.
DSMZ Medium 67 lists 3 g Casitone, 1.36 g CaCl2 x 2 H2O, 1 g yeast extract,
15 g agar, and 1000 ml distilled water at pH 7.2. The repaired M2337 branch
intentionally represents the liquid, no-agar interpretation with 0.5% w/v
cellobiose converted to 5 g/L.

The generated record still carries pre-repair projections:

| Field | Repaired M2337 | Generated record |
|---|---:|---:|
| Distilled water | 1 L | 1000 g/L |
| Cellobiose | 5 g/L | 0.5% w/v |
| pH | 7.2 | missing |
| Cellobiose handling | filter-sterilized preparation step | notes text only |
| Structured references | TOGO M2337, DSMZ 160, DSMZ 67 | none |

The generated `1000 G_PER_L` water row is dimensionally wrong. The generated
0.5% w/v cellobiose row matches DSMZ 160 in a broad sense, but the maintained
curation has already normalized that amount to the equivalent 5 g/L and made
the filter-sterilized addition explicit.

## Completeness

- The generated record has no `references`, `source_data`,
  `target_organisms`, `growth_metrics`, `ph_value`, `preparation_steps`, or
  data-quality flags. Empty target-organism and growth-metric slots are
  acceptable because TOGO M2337 is a recipe record, not a primary growth assay.
- The missing pH and cellobiose preparation are consequential: pH 7.2 comes from
  DSMZ Medium 67, and filter sterilization is part of the DSMZ Medium 160
  cellobiose branch.
- The normalized input already owns the needed corrections.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The generated record stores water as `1000 G_PER_L`. | TOGO M2337 and DSMZ Medium 67 list distilled water by volume; the repaired maintained input stores water as a volume, while the generated record uses a mass unit. | Regeneration from `data/normalized_yaml/bacterial/TOGO_M2337_Cytophaga_Hutchinsonii_Medium.yaml` |
| major | The generated record is stale relative to the 2026-09-11 repair. | The maintained input has pH, filter-sterilized cellobiose preparation, normalized 5 g/L cellobiose, curated flags, and three structured references that the generated record lacks. | Merge generation for TOGO M2337 |
| minor | The older DSMZ-derived duplicate remains separate from the TOGO M2337 source. | A gitignore-independent search found `data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml` as another local DSMZ 160 import. | Future duplicate reconciliation |

## Recommended Edits

1. Regenerate
   `data/merge_yaml/merged/cytophaga_hutchinsonii_medium__b6268d2c.yaml` from
   the repaired TOGO M2337 normalized input.
2. Preserve the repaired `ph_value`, `preparation_steps`, `references`,
   `data_quality_flags`, and `Cellobiose` grounding in the generated output.
3. Ensure the water row is emitted as a volume, not `1000 G_PER_L`.
4. Review whether the older DSMZ-derived
   `data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml` should be
   linked as a source duplicate of the TOGO M2337 repair.

## Follow-up Checks

- Re-run open-schema, closed-schema, reference, and term validation on the
  regenerated record.
- Diff the regenerated record against the repaired normalized input, TOGO M2337,
  DSMZ Medium 160, and DSMZ Medium 67.
- Verify that the regenerated record has pH 7.2, 5 g/L cellobiose, 1 L
  distilled water, and a filter-sterilized cellobiose preparation step.
- Re-run `rg --no-ignore --hidden` for `TOGO:M2337` and `DSMZ_Medium160`
  across `data/normalized_yaml` and `data/raw` to account for the old DSMZ
  duplicate after regeneration.

## Additional Notes

- The source leaves two alternative Cytophaga hutchinsonii preparations: a
  filter-sterilized cellobiose branch and a filter-paper branch. The repaired
  TOGO M2337 record explicitly represents the imported liquid cellobiose
  branch and omits the agar from DSMZ Medium 67.
