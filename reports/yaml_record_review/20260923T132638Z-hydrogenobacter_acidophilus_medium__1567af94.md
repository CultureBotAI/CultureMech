# YAML Record Review: HYDROGENOBACTER ACIDOPHILUS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/hydrogenobacter_acidophilus_medium__1567af94.yaml
- Started UTC: 2026-09-23T13:24:00Z
- Finished UTC: 2026-09-23T13:26:36Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| ID | CultureMech:001878 |
| Name | hydrogenobacter_acidophilus_medium |
| Original name | HYDROGENOBACTER ACIDOPHILUS MEDIUM |
| Class | MediaRecipe |
| Category | bacterial |
| Medium type | DEFINED |
| Composition type | DEFINED |
| Physical state | LIQUID |
| pH | 3.0 |
| Source identity | MediaDive/DSMZ Medium 743 |
| Generated path reviewed | data/merge_yaml/merged/hydrogenobacter_acidophilus_medium__1567af94.yaml |
| Maintained owner | data/normalized_yaml/bacterial/hydrogenobacter_acidophilus_medium.yaml |

The reviewed file is generated from
`data/normalized_yaml/bacterial/hydrogenobacter_acidophilus_medium.yaml`.
Future edits should update that normalized MediaDive import and the repeated
MediaDive/KOMODO trace-stock flattening logic, then regenerate
`data/merge_yaml/merged/`.

## Validation

| Check | Result |
|---|---|
| Open LinkML validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/hydrogenobacter_acidophilus_medium__1567af94.yaml` | Passed; no issues found. |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/hydrogenobacter_acidophilus_medium__1567af94.yaml --out /private/tmp/hydrogenobacter_acidophilus_medium__1567af94.strict.tsv --workers 1 --quiet` | Passed; the TSV contained only the header and zero ERROR rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/hydrogenobacter_acidophilus_medium__1567af94.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with zero reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/hydrogenobacter_acidophilus_medium__1567af94.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` entry point validates standalone YAML under `history/`, not embedded MediaRecipe history arrays. |

The focused validators used Python 3.11 and the offline uv cache because the
project-level uv environment currently fails before validation while trying to
build `llvmlite==0.46.0` with Python 3.13.

## Identity and Grounding

- The record identity is coherent: `CultureMech:001878` denotes DSMZ Medium
  743 / MediaDive medium 743, `HYDROGENOBACTER ACIDOPHILUS MEDIUM`, with
  bacterial category, defined liquid composition, and pH 3.0.
- The inspected live MediaDive REST payload for medium 743 agrees with the
  linked DSMZ PDF for the final-medium rows, the 0.5 ml trace-element stock
  addition, pH 3.0 HCl adjustment, 3-day steaming, and H2/O2/CO2 7:1:1
  incubation gas phase at one atmosphere overpressure and 65 C.
- A gitignore-independent `hydrogenobacter_acidophilus_medium` slug search over
  `data/normalized_yaml`, `data/merge_yaml/merged`, and `reports` found this
  MediaDive record, a KOMODO import of DSMZ 743 with the same normalized name,
  plus JCM J164 and TOGO M155 sibling records that share the display label but
  encode a distinct JCM formulation.
- Ingredient grounding is exact enough for the visible salts, including
  magnesium sulfate heptahydrate, ferrous sulfate heptahydrate, calcium
  chloride, molybdenum trioxide, zinc sulfate heptahydrate, copper sulfate
  pentahydrate, boric acid, manganese sulfate pentahydrate, and cobalt
  chloride hexahydrate.

## Evidence

- The sulfur, ammonium sulfate, phosphate, sodium chloride, magnesium sulfate,
  ferrous sulfate, and calcium chloride final-medium rows match the DSMZ 743
  source quantities after milligram rows are converted to grams per liter.
- The trace elements are source-supported only as members of a separate 1 L
  stock solution. DSMZ 743 adds 0.5 ml of `Trace element solution` per liter;
  the reviewed record omits that solution boundary and lists MoO3, ZnSO4,
  CuSO4, H3BO3, MnSO4, and CoCl2 as final-medium ingredients at their
  undiluted stock g/L values.
- The 1000 ml distilled-water row from Main sol. 743 and the 1000 ml
  deionized-water row from the trace solution are both absent from the YAML.
- The preparation sentence is broadly faithful to MediaDive and the DSMZ PDF,
  but it is stored as a single `ADJUST_PH` step that also contains steaming and
  incubation instructions.

## Completeness

- The `solutions` array is missing the 0.5 ml/L trace-stock addition and the
  trace-stock composition. Following the flat YAML would over-add every trace
  element by roughly 2000-fold relative to a 0.5 ml stock addition.
- The record does not represent HCl as the pH adjuster ingredient even though
  the maintained KOMODO copy extracts an HCl variable row from the same DSMZ
  source.
- The generated corpus still contains `KOMODO_743_HYDROGENOBACTER_ACIDOPHILUS_MEDIUM`
  as a second record for DSMZ 743 rather than deduplicating it with this
  MediaDive-owned record.
- Empty optional fields such as synonyms, organisms, and external publication
  references are not defects for this imported medium.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The DSMZ 743 trace-element stock has been flattened into final-medium ingredients. | The inspected MediaDive/PDF source adds 0.5 ml trace solution per 1 L final medium, but the YAML emits all six trace stock compounds directly at their 1 L stock concentrations. | `data/normalized_yaml/bacterial/hydrogenobacter_acidophilus_medium.yaml`; MediaDive import should preserve `mediadive.solution:1178` or an equivalent source-specific stock. |
| Major | Water and stock boundaries are omitted. | MediaDive `Main sol. 743` includes 1000 ml distilled water, and the trace stock includes 1000 ml deionized water; neither row and no stock relation survive in the YAML. | `data/normalized_yaml/bacterial/hydrogenobacter_acidophilus_medium.yaml` and the generated merge output. |
| Minor | HCl is used in source preparation but not represented as a variable pH-adjustment ingredient. | The source states pH is adjusted to 3.0 with HCl; the MediaDive record leaves that only inside the free-text preparation step. | `data/normalized_yaml/bacterial/hydrogenobacter_acidophilus_medium.yaml`; compare the KOMODO 743 importer that added a variable HCl row. |
| Minor | The single preparation step mixes pH adjustment, sterilization, and incubation. | The YAML stores pH adjustment, 3-day steaming, gas phase, overpressure, and 65 C incubation in one `ADJUST_PH` item. | `data/normalized_yaml/bacterial/hydrogenobacter_acidophilus_medium.yaml`; split the imported note into scoped preparation and incubation fields when the schema can express them. |
| Minor | DSMZ 743 exists twice under different provider imports. | Ignored-inclusive local search found this MediaDive-derived CultureMech:001878 record and a KOMODO-derived CultureMech:006394 record for KOMODO/DSMZ 743. | MediaDive/KOMODO deduplication; generated merged YAML should be regenerated after reconciliation. |

## Recommended Edits

1. Move MoO3, ZnSO4 x 7 H2O, CuSO4 x 5 H2O, H3BO3, MnSO4 x 5 H2O, and
   CoCl2 x 6 H2O out of the final ingredient list and into a nested Trace
   element solution used at 0.5 ml/L.
2. Restore the final 1000 ml distilled-water row and trace-stock 1000 ml
   deionized-water row, preserving the distinct final-medium and stock scopes.
3. Add HCl as a variable pH-adjuster row or another structured pH-adjustment
   representation owned by the normalized DSMZ 743 record.
4. Split the preparation note into at least pH adjustment, 3-hour steaming on
   each of 3 successive days, and H2/O2/CO2 7:1:1 incubation under one
   atmosphere overpressure at 65 C.
5. Reconcile the MediaDive DSMZ 743 and KOMODO DSMZ 743 records so the same
   provider medium is not published as two independent CultureMech records.
6. Regenerate `data/merge_yaml/merged/` from the repaired normalized inputs.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation for the regenerated
  merged DSMZ 743 record.
- Manually compare every final-medium and trace-stock row against the live
  MediaDive medium 743 REST payload and `DSMZ_Medium743.pdf`.
- Verify the trace elements are reachable only through the 0.5 ml/L Trace
  element solution stock and no longer appear as direct final-medium
  concentrations.
- Search with ignored files included for `mediadive.medium:743`,
  `komodo.medium:743`, and `hydrogenobacter_acidophilus_medium` after
  regeneration to confirm that only intentional distinct JCM and TOGO
  siblings remain separate.

## Additional Notes

- JCM J164 and TOGO M155 share the `Hydrogenobacter acidophilus medium` label
  but differ from DSMZ 743 in composition, so they should not be deduplicated
  with this record by label alone.
- The reviewed MediaDive import has 13 ingredient rows; the KOMODO 743 sibling
  has the same 13 flat ingredients plus a variable HCl ingredient.
