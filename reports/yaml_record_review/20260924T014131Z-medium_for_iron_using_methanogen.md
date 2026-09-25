# YAML Record Review: medium_for_iron_using_methanogen

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/medium_for_iron_using_methanogen.yaml
- Started UTC: 2026-09-24T01:41:03Z
- Finished UTC: 2026-09-24T01:41:31Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:008281 |
| Name | medium_for_iron_using_methanogen |
| Generated record | data/merge_yaml/merged/medium_for_iron_using_methanogen.yaml |
| Maintained owner | data/normalized_yaml/archaea/medium_for_iron_using_methanogen.yaml |
| Source identity | TOGO:M1718, original source NBRC_M927 |

This generated record is the single-source TOGO M1718 import of NBRC Medium 927,
"Medium for iron-using methanogen." The source formulation is a liquid,
iron-granule-containing archaeal medium with 1 ml/L trace and vitamin stock
additions.

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/medium_for_iron_using_methanogen.yaml` | Passed with no issues found. |
| Strict validation, `scripts/validate_strict.py data/merge_yaml/merged/medium_for_iron_using_methanogen.yaml --workers 1` | Passed; the TSV contained only its header and 0 error rows. |
| Reference validation, `linkml-reference-validator validate data ... --target-class MediaRecipe` | Passed with 0 reference checks. |
| Term validation, `linkml-term-validator validate-data ... -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented history validator targets standalone history files, not embedded generated-record events. |

The focused validators were run with Python 3.11 through `uv --no-project
--offline` to avoid the project-level Python 3.13 `llvmlite` build failure.

## Identity and Grounding

The TOGO M1718 payload, NBRC `NO=927` page, TOGO owner, and reviewed generated
record agree on the medium name, source accession, category, and liquid state.
A gitignore-independent exact scan for `TOGO:M1718`, `NBRC_M927`, the NBRC
`NO=927` URL, and `medium_for_iron_using_methanogen` found only this normalized
owner, this generated target, and indexes in the scanned data/report paths.
Ignored files were included.

Several ingredient groundings are too broad for the exact hydrated salts in the
source: `CoCl2 x 6 H2O` is grounded to generic cobalt dichloride and
`NiCl2 x 6 H2O` to generic nickel dichloride. `Ca-pantothenate` is grounded to
pantothenate rather than calcium pantothenate.

## Evidence

NBRC Medium 927 supports the base ingredients and the three additions at the
top level: 1 ml trace elements solution, 1 ml vitamin solution, 150 g iron
granules, 1 g/L Cysteine-HCl, 1 L distilled water, and the listed HEPES, NaCl,
MgCl2 x 6 H2O, CaCl2 x 2 H2O, sulfate, ammonium, phosphate, KCl, and
bicarbonate salts.

The generated record does not preserve the source boundaries:

- `Iron granule (1-2 mm)` is a 150 g final-medium component that should be
  autoclaved separately under N2; it was moved into `solutions` with an empty
  composition.
- The trace and vitamin stock additions are 1 ml each, not 1 G_PER_L solution
  rows.
- Trace-stock rows are flattened into final-medium ingredients. This also sums
  base and trace NaCl to 20.0 G_PER_L and base and trace CaCl2 x 2 H2O to
  0.25 G_PER_L, although the 1 g NaCl and 0.1 g CaCl2 rows belong to the trace
  stock.
- Vitamin stock rows are flattened as final G_PER_L ingredients while their
  NBRC stock amounts are in mg/L.
- NaOH belongs to the trace-stock pH 6.5 adjustment, not the final medium.

The generated record is also stale relative to the maintained TOGO owner: the
owner collapsed duplicate distilled-water rows back to 1.0 on 2026-09-02, but
the generated artifact still reports 3.0 G_PER_L water.

## Completeness

The generated record omits the NBRC anaerobic workflow: mix everything except
vitamin solution, bicarbonate, iron granules, and Cysteine-HCl; dispense under
N2/CO2 80/20; autoclave under butyl rubber stoppers; filter-sterilize the
vitamin and bicarbonate solutions; separately autoclave 5 percent Cysteine-HCl
and iron granules under N2; then aseptically and anaerobically add the sterile
vitamin, bicarbonate, iron, and cysteine before inoculation.

No target organisms are asserted. That is acceptable because the inspected TOGO
and NBRC source records define a formulation without strain-level growth
evidence.

## Findings

| Severity | Finding | Evidence | Maintained owner for future fix |
|---|---|---|---|
| major | Stock solutions and iron granules are misrepresented. | The source has 1 ml trace stock, 1 ml vitamin stock, and 150 g iron granules; the YAML has two 1 G_PER_L solution rows, flattened stock components, and the iron granules in `solutions` with no composition. | `data/normalized_yaml/archaea/medium_for_iron_using_methanogen.yaml`; TOGO solution migration/import code. |
| major | Stock components are flattened into the final medium and some duplicates are summed. | NBRC places NaCl and CaCl2 x 2 H2O both in the base medium and in the trace stock; the YAML merges them into final-medium 20.0 and 0.25 G_PER_L rows. Vitamin mg/L stock components are also emitted as final G_PER_L ingredients. | TOGO normalized owner and duplicate-merge logic. |
| major | Anaerobic preparation details are absent or represented as final ingredients. | NBRC gives anaerobic N2/CO2 dispensing, separate sterilization of bicarbonate, vitamin, Cysteine-HCl, and iron, and trace-stock pH adjustment with NaOH. The YAML has no `preparation_steps` and carries NaOH as a variable final-medium ingredient. | TOGO normalized owner. |
| major | The generated target is stale relative to the maintained owner. | The owner has a 2026-09-02 repair that collapsed three identical water rows to 1.0; the generated record still has 3.0 G_PER_L water and the old merge note. | Merge regeneration for `data/merge_yaml/merged/medium_for_iron_using_methanogen.yaml`. |
| minor | Several ingredient groundings are too broad. | CoCl2 x 6 H2O, NiCl2 x 6 H2O, and Ca-pantothenate have primary terms that do not preserve the exact salt or counterion. | TOGO normalized owner ingredient grounding. |

## Recommended Edits

1. Keep iron granules as a final-medium ingredient with their separate
   anaerobic autoclaving instruction; do not migrate them into `solutions`.
2. Restore trace and vitamin additions as 1 ML_PER_L stock additions and keep
   their recipes nested or linked rather than flattened into final-medium rows.
3. Stop summing base-medium and trace-stock duplicate names; the NaCl and
   CaCl2 x 2 H2O rows are in different solution boundaries.
4. Add the NBRC anaerobic dispensing, sterilization, post-autoclave addition,
   and trace-stock pH-preparation details to the maintained owner.
5. Re-ground the exact hydrated salts and calcium pantothenate where exact
   CHEBI or MediaIngredientMech mappings are available.
6. Regenerate the merge after the maintained TOGO owner is repaired.

## Follow-up Checks

- Run focused open schema, strict, reference, and term validators on the
  repaired TOGO owner and regenerated merge.
- Run `just verify-merges` to ensure the generated record reflects the repaired
  1 L water row and no longer contains flattened stock rows.
- Repeat a gitignore-independent exact scan for `TOGO:M1718`, `NBRC_M927`, and
  the NBRC `NO=927` URL to confirm the accession still appears only on the
  expected owner, generated artifact, and indexes.
- Manually compare the regenerated record against NBRC Medium 927 to confirm
  trace/vitamin stock boundaries, iron-granule handling, and anaerobic
  post-autoclave additions are preserved.

## Additional Notes

None found.
