# YAML Record Review: HYDROGENOBACTER ACIDOPHILUS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/hydrogenobacter_acidophilus_medium__b9459be6.yaml
- Started UTC: 2026-09-23T13:30:00Z
- Finished UTC: 2026-09-23T13:31:53Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| ID | CultureMech:006394 |
| Name | hydrogenobacter_acidophilus_medium |
| Original name | HYDROGENOBACTER ACIDOPHILUS MEDIUM |
| Class | MediaRecipe |
| Category | bacterial |
| Medium type | DEFINED |
| Composition type | DEFINED |
| Physical state | LIQUID |
| pH | 3.0 |
| Source identity | KOMODO Medium 743; copied from DSMZ Medium 743 |
| Generated path reviewed | data/merge_yaml/merged/hydrogenobacter_acidophilus_medium__b9459be6.yaml |
| Maintained owner | data/normalized_yaml/bacterial/KOMODO_743_HYDROGENOBACTER_ACIDOPHILUS_MEDIUM.yaml |

The reviewed file is generated from the KOMODO normalized record above. Future
fixes should update the KOMODO/DSMZ-resolved normalized input and the shared
DSMZ trace-stock handling that also affects the MediaDive 743 import, then
regenerate `data/merge_yaml/merged/`.

## Validation

| Check | Result |
|---|---|
| Open LinkML validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/hydrogenobacter_acidophilus_medium__b9459be6.yaml` | Passed; no issues found. |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/hydrogenobacter_acidophilus_medium__b9459be6.yaml --out /private/tmp/hydrogenobacter_acidophilus_medium__b9459be6.strict.tsv --workers 1 --quiet` | Passed; zero ERROR rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/hydrogenobacter_acidophilus_medium__b9459be6.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with zero reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/hydrogenobacter_acidophilus_medium__b9459be6.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` entry point validates standalone YAML under `history/`, not embedded MediaRecipe history arrays. |

The focused validators used Python 3.11 and the offline uv cache because the
project-level uv environment currently fails before validation while trying to
build `llvmlite==0.46.0` with Python 3.13.

## Identity and Grounding

- The record identity is coherent: `CultureMech:006394` is the KOMODO 743
  record for `HYDROGENOBACTER ACIDOPHILUS MEDIUM`, and its notes explicitly
  identify DSMZ Medium 743 / `mediadive.medium:743` as the copied composition.
- The inspected DSMZ 743 PDF and MediaDive REST payload support the main
  sulfur, ammonium sulfate, K2HPO4, NaCl, MgSO4 x 7H2O, FeSO4 x 7H2O, and
  CaCl2 rows and the source pH 3.0.
- An ignored-inclusive exact search for
  `KOMODO_743_HYDROGENOBACTER_ACIDOPHILUS_MEDIUM` across
  `data/normalized_yaml`, `data/merge_yaml/merged`, and `reports` found the
  maintained file, generated merged file, generated indexes, and archive/report
  references for this same KOMODO source.
- A gitignore-independent `komodo.medium:743` search over the same local areas
  found only this KOMODO 743 normalized/generated record and generated indexes
  or reports that refer to it.
- Ingredient grounding is exact enough for the visible hydrated sulfate and
  chloride salts. The elemental sulfur row uses the broader sulfur-atom CHEBI
  term, but the source does not require a different sulfur allotrope.

## Evidence

- The main seven non-stock ingredient concentrations match DSMZ 743 after the
  source 1 mg FeSO4 and CaCl2 rows are converted to 0.001 g/L.
- The added variable HCl row is supported by the DSMZ 743 pH-adjustment
  instruction and is a useful structured improvement over the sibling MediaDive
  743 import.
- The six trace elements are unsupported as final-medium concentrations. DSMZ
  743 adds 0.5 ml of a trace-element solution; the YAML lists MoO3, ZnSO4,
  CuSO4, H3BO3, MnSO4, and CoCl2 directly at the concentrations of the 1 L
  stock.
- The DSMZ 743 source water rows are absent: 1000 ml distilled water from Main
  sol. 743 and 1000 ml deionized water from the trace stock are not represented.
- The source steaming and incubation instructions did not survive the KOMODO
  import. The YAML has pH and HCl, but no steps for steaming the medium for 3
  hours on each of 3 successive days or incubating under H2/O2/CO2 7:1:1 with
  one atmosphere overpressure at 65 C.

## Completeness

- The record is missing a structured trace-stock addition at 0.5 ml/L and a
  nested trace-stock composition.
- The source sterilization and incubation conditions are missing.
- The record is one of two local records for the same DSMZ 743 provider medium;
  the duplicate MediaDive-derived CultureMech:001878 record has the same
  flattened trace-stock defect without the HCl row.
- Empty optional fields such as target organisms, synonyms, and publication
  references are not defects for this provider import.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | DSMZ 743 trace-stock members were flattened at stock strength. | The source adds 0.5 ml/L of Trace element solution, but the KOMODO record emits all six trace stock compounds as direct final-medium rows. | `data/normalized_yaml/bacterial/KOMODO_743_HYDROGENOBACTER_ACIDOPHILUS_MEDIUM.yaml`; the KOMODO DSMZ resolver should preserve stock scope. |
| Major | Water and trace-stock structure are absent. | Main sol. 743 and the trace stock each include a 1000 ml water row in the live MediaDive/DSMZ source; neither water row nor a `solutions` reference appears in the YAML. | `data/normalized_yaml/bacterial/KOMODO_743_HYDROGENOBACTER_ACIDOPHILUS_MEDIUM.yaml`. |
| Major | Preparation and incubation conditions were dropped. | DSMZ 743 includes 3-day steaming and H2/O2/CO2 7:1:1 incubation with one atmosphere overpressure at 65 C, while the KOMODO YAML has no `preparation_steps`. | `data/normalized_yaml/bacterial/KOMODO_743_HYDROGENOBACTER_ACIDOPHILUS_MEDIUM.yaml`; copy DSMZ preparation metadata during resolver enrichment. |
| Minor | DSMZ 743 is duplicated under MediaDive and KOMODO source records. | The reviewed KOMODO 743 record and MediaDive CultureMech:001878 both represent DSMZ Medium 743 but were not merged. | MediaDive/KOMODO source reconciliation and recipe deduplication. |

## Recommended Edits

1. Move MoO3, ZnSO4 x 7H2O, CuSO4 x 5H2O, H3BO3, MnSO4 x 5H2O, and CoCl2 x
   6H2O into a nested Trace element solution stock and add that stock to the
   final medium at 0.5 ml/L.
2. Restore the source 1000 ml water rows for the final medium and trace stock.
3. Add structured preparation/incubation content for 3-hour steaming on each of
   3 successive days and H2/O2/CO2 7:1:1 incubation with one atmosphere
   overpressure at 65 C.
4. Reconcile the KOMODO 743 and MediaDive 743 records so the same DSMZ provider
   medium is published once with alternate source provenance.
5. Regenerate the merged YAML after the KOMODO normalized record and
   cross-source duplicate handling are fixed.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation for the regenerated
  KOMODO 743 record.
- Manually compare the regenerated ingredient list and stock solution against
  the live MediaDive 743 REST payload and the DSMZ 743 PDF.
- Confirm all six trace elements are scoped to the 0.5 ml/L trace stock and
  are absent as direct final-medium ingredients.
- Run ignored-inclusive searches for `komodo.medium:743`,
  `mediadive.medium:743`, and `hydrogenobacter_acidophilus_medium` to confirm
  the duplicate DSMZ 743 records have been reconciled without collapsing the
  distinct JCM J164 or TOGO M155 formulas.

## Additional Notes

- This record improves on the MediaDive 743 import by preserving pH 3.0 and a
  variable HCl ingredient.
- KOMODO's `Aerobic: No` note is compatible with the inspected DSMZ gas phase;
  the problem is that the specific H2/O2/CO2 ratio and overpressure are not
  represented.
