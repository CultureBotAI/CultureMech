# YAML Record Review: modified_sea_water_agar

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_sea_water_agar__ac7be910.yaml
- Started UTC: 2026-09-24T13:04:43Z
- Finished UTC: 2026-09-24T13:06:50Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| CultureMech ID | CultureMech:009047 |
| Name | modified_sea_water_agar |
| Original name | Modified Sea Water Agar |
| Category | bacterial |
| Source identity | TOGO:M2471, sourced from DSMZ_Medium917.pdf |
| Generated status | Generated canonical merge under `data/merge_yaml/merged/`; maintain future fixes in `data/normalized_yaml/bacterial/TOGO_M2471_Modified_Sea_Water_Agar.yaml` or in the TOGO import/merge rules. |

The target resolves unambiguously to `TOGO:M2471`, a TOGO import of DSMZ Medium 917. An ignored-file-inclusive exact search for `TOGO:M2471`, `DSMZ_Medium917`, and `Medium917` under `data` and `reports` found this generated record, its maintained TOGO input, and a maintained DSMZ input for the same DSMZ PDF at `data/normalized_yaml/bacterial/modified_sea_water_agar.yaml`. A second exact ignored-file-inclusive search for `mediadive.medium:917`, `CultureMech:002085`, `KOMODO_917_MODIFIED_SEA_WATER_AGAR`, and `CultureMech:006794` found that the DSMZ branch is already duplicate-linked to the KOMODO copy and merged separately as `data/merge_yaml/merged/MODIFIED_SEA_WATER_AGAR.yaml`.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema, Python 3.11 `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_sea_water_agar__ac7be910.yaml` | Passed with `No issues found`. |
| Strict closed-schema validator, Python 3.11 `scripts/validate_strict.py data/merge_yaml/merged/modified_sea_water_agar__ac7be910.yaml --out /private/tmp/modified_sea_water_agar__ac7be910.strict.tsv --workers 1 --quiet` | Passed. TSV contained only the header row, so there were 0 strict errors. |
| Reference validator, Python 3.11 `linkml-reference-validator validate data data/merge_yaml/merged/modified_sea_water_agar__ac7be910.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed. |
| Term validator, Python 3.11 `linkml-term-validator validate-data data/merge_yaml/merged/modified_sea_water_agar__ac7be910.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils`/`pkg_resources` warning. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` target validates standalone YAML under `history/`, not inline `MediaRecipe.curation_history` entries. |

## Identity and Grounding

The record identity is correct: TOGO M2471 resolves to `Modified Sea Water Agar`, names DSMZ Medium 917 as its original source, and carries the same ingredients and gram amounts as the inspected DSMZ PDF. `SOLID_AGAR` is supported by the 15 g agar component, and the complex/undefined classification is consistent with peptone and yeast extract.

Most ingredient ChEBI groundings match the exact supplied forms: sodium chloride, calcium chloride dihydrate, magnesium chloride hexahydrate, magnesium sulfate heptahydrate, potassium chloride, agar, and hexadecane are all consistent with the component labels in the source recipe. The magnesium sulfate heptahydrate row is internally inconsistent because `term` was corrected to `CHEBI:31795` while `mediaingredientmech_chebi_term` still points at generic `CHEBI:32599`.

## Evidence

The inspected DSMZ PDF supports the nine solutes/components, agar, hexadecane, and their amounts, and the TOGO JSON for M2471 reproduces those values. The TOGO JSON also exposes the DSMZ preparation comment as a structured `comments` entry, so the missing preparation data are present upstream and lost before the generated merge.

Two formulation claims are not source-faithful in the reviewed branch:

- Distilled water is `1000 ml` in both the TOGO API payload and DSMZ PDF but is represented as `1000 G_PER_L` in the generated YAML. `ML_PER_L` is available in `ConcentrationUnitEnum`, so no schema limitation requires this volume-to-mass substitution.
- The source preparation text specifies adjustment to pH 7.2, autoclaving at 121 C for 20 min, separate sterilization of calcium chloride, and post-autoclave calcium chloride addition. None of these pH or preparation claims appears in the generated TOGO merge.

## Completeness

Consequential missing content:

- `ph_value: 7.2` is absent from the generated TOGO merge even though it is source-supported and already present in the maintained DSMZ normalized branch for the same source PDF.
- `preparation_steps` is absent, losing autoclaving and separate calcium chloride sterilization instructions that materially affect how to make the medium.

Empty `target_organisms`, `discussion`, and `evidence` slots are not defects for this source-only import. The reviewed source is a recipe sheet, not a growth study, and I found no record-local organism or growth assertion that needs evidence support.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Distilled water has the wrong unit. The source states 1000 ml, but the generated record says `1000 G_PER_L`. | DSMZ Medium 917 lists distilled water as 1000.00 ml; the TOGO M2471 API payload has `"unit": "ml"` for `Distilled water`; the generated YAML uses `unit: G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M2471_Modified_Sea_Water_Agar.yaml`, or the TOGO unit importer if this affects every imported ml component. |
| major | Source-supported pH and sterilization/preparation instructions are dropped. | The TOGO API and DSMZ PDF both carry the pH 7.2/autoclave/separate calcium chloride sterilization comment; `ph_value` and `preparation_steps` are absent from the generated TOGO merge. | `data/normalized_yaml/bacterial/TOGO_M2471_Modified_Sea_Water_Agar.yaml`, the TOGO comment importer, or merge logic that should merge DSMZ Medium 917 data with TOGO M2471 when they name the same DSMZ source. |
| major | The MgSO4 x 7 H2O row has stale MediaIngredientMech ChEBI grounding. | The primary row term is `CHEBI:31795` for magnesium sulfate heptahydrate, but `mediaingredientmech_chebi_term` remains `CHEBI:32599` for generic magnesium sulfate; the curation history records the heptahydrate fix as having changed only the primary grounding. | `data/normalized_yaml/bacterial/TOGO_M2471_Modified_Sea_Water_Agar.yaml`, or the legacy MediaIngredientMech-to-ChEBI migration that failed to refresh this row after the hydrate correction. |

No blocker findings.

No minor findings.

## Recommended Edits

1. In the maintained TOGO source branch, change the distilled water concentration unit from `G_PER_L` to `ML_PER_L`, preserving value `1000`.
2. Preserve TOGO M2471 comment text by parsing pH 7.2 into `ph_value` and adding a preparation step for agar addition, autoclaving at 121 C for 20 min, separate calcium chloride sterilization, and post-autoclave calcium chloride addition.
3. Refresh the MgSO4 x 7 H2O `mediaingredientmech_chebi_term` to `CHEBI:31795` / `magnesium sulfate heptahydrate` so it matches the primary ChEBI grounding.
4. Re-run the merge generator after the normalized TOGO branch is corrected. While doing that, review why the TOGO M2471 import from DSMZ Medium 917 and the MediaDive 917/KOMODO duplicate branch publish as separate merged records.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validation on the corrected normalized branch and regenerated `data/merge_yaml/merged/modified_sea_water_agar__ac7be910.yaml`.
- Re-run merge freshness verification so the generated record is proven to reflect `data/normalized_yaml/bacterial/TOGO_M2471_Modified_Sea_Water_Agar.yaml`.
- Inspect the regenerated YAML to confirm the water unit is `ML_PER_L`, the MgSO4 x 7 H2O primary and MediaIngredientMech ChEBI terms are both `CHEBI:31795`, `ph_value` is 7.2, and calcium chloride is modeled as separately sterilized and added after autoclaving.

## Additional Notes

The maintained direct DSMZ branch at `data/normalized_yaml/bacterial/modified_sea_water_agar.yaml` already has `ph_value: 7.2`, the preparation step, and the corrected `CHEBI:31795` MediaIngredientMech ChEBI link. It omits the 1000 ml distilled-water line from its ingredient list, which is less misleading than the TOGO branch's conversion to `1000 G_PER_L` but still means the two branches cannot currently fingerprint together.
