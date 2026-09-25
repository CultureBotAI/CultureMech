# YAML Record Review: Modified Nitrosospaera Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_Nitrosospaera_medium.yaml
- Started UTC: 2026-09-24T10:09:26Z
- Finished UTC: 2026-09-24T10:09:26Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Record | `data/merge_yaml/merged/modified_Nitrosospaera_medium.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:001113` |
| Name | `modified_nitrosospaera_medium` |
| Original name | `modified Nitrosospaera medium` |
| Category | `bacterial` |
| Medium source | MediaDive / DSMZ `mediadive.medium:1630c` |
| Maintained owner | `data/normalized_yaml/bacterial/modified_nitrosospaera_medium.yaml` |
| Generated status | Generated merge output from one normalized MediaDive record |

## Validation

| Check | Result |
| --- | --- |
| Open LinkML schema validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_Nitrosospaera_medium.yaml` | Passed; exited 0 with "No issues found". |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/modified_Nitrosospaera_medium.yaml --out /private/tmp/modified_Nitrosospaera_medium.strict.tsv --workers 1 --quiet` | Passed; 0 strict errors were reported and `/private/tmp/modified_Nitrosospaera_medium.strict.tsv` contained only the header line. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/modified_Nitrosospaera_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the focused run completed with 0 reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/modified_Nitrosospaera_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not inline `MediaRecipe.curation_history` entries in a merged YAML record. |

## Identity and Grounding

The record identity is coherent: `CultureMech:001113` and MediaDive / DSMZ `1630c` both identify modified Nitrosospaera medium.

An exact `find data/normalized_yaml -name 'modified_nitrosospaera_medium.yaml'` search, which does not honor gitignore exclusions, found `data/normalized_yaml/bacterial/modified_nitrosospaera_medium.yaml` as the generated record's maintained owner.

Most source chemical forms are preserved, but `NiCl2 x 6 H2O` is grounded to `CHEBI:34887` with label `nickel dichloride`, which does not preserve the source hexahydrate form.

## Evidence

MediaDive 1630c describes a nested recipe: 1 L of `Main sol. 1630c` contains six gram-scale salts in Basic-FWM, six named sterile stock additions, and 1 L double-distilled water. The six stock additions are 1 ml Trace element solution (Nitrososphaera), 1 ml FeNaEDTA solution, 2 ml 1 M NaHCO3 buffer, 10 ml HEPES buffer solution, 2 ml 1 M NH4Cl, and 1 ml 1 M Sodiumpyruvate.

| Source claim | Record representation | Review |
| --- | --- | --- |
| Basic-FWM contains NaCl, MgCl2 x 6 H2O, CaCl2 x 2 H2O, KH2PO4, KCl, and Na2SO4 at 1, 0.4, 0.1, 0.2, 0.5, and 0.05 g/L, respectively. | The same six base salts are represented with matching `G_PER_L` values. | Supported. |
| The final medium receives small milliliter additions from six sterile stocks. | No stock additions are represented; all stock recipes are flattened into top-level final-medium ingredients. | Unsupported stock flattening. |
| The 1 L trace-element stock contains 8 ml 12.5 M HCl, mg-scale trace salts, and 1 L water, then only 1 ml of that stock is added to the final liter. | HCl and every trace metal salt are top-level `G_PER_L` ingredients at their stock concentrations. | Unsupported by the final-medium recipe. |
| The NaHCO3, NH4Cl, and sodium pyruvate stocks are 50 ml stocks at 1 M, with 2 ml, 2 ml, and 1 ml added to the final liter, respectively. | `NaHCO3`, `NH4Cl`, and `Sodium pyruvate` are top-level `G_PER_L` ingredients at 84, 53.4, and 110 g/L. | Unsupported by the final-medium recipe. |
| Main, trace, HEPES, FeNaEDTA, NaHCO3, NH4Cl, and sodium-pyruvate solutions each have their own water rows. | Six water rows are flattened and duplicate-merged into `3150 G_PER_L`. | Unsupported compartment collapse and volume-to-mass import. |
| The final pH is 7.5. | `ph_value: 7.5` is represented. | Supported. |

## Completeness

The generated record carries the visible base-salt rows and the pH, but it is missing every `solution_id` boundary from MediaDive 1630c. The per-stock concentrations are not final-medium concentrations; following the flattened record would add full trace, bicarbonate, ammonium chloride, sodium pyruvate, HEPES, and FeNaEDTA stock strengths directly to the base medium.

Preparation instructions are copied as top-level steps without structured ownership by their source stocks. They preserve useful text, but the record no longer connects the trace-stock dark storage step, HEPES pH step, or 50 ml stock filter-sterilization steps to the solution recipes they prepare.

Empty target-organism and growth-evidence fields were not treated as defects. MediaDive 1630c is a medium formulation page, not a primary growth-evidence page.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | Six MediaDive stock additions are flattened into final-medium ingredients. | MediaDive adds 1, 1, 2, 10, 2, and 1 ml from six sterile stocks to 1 L Basic-FWM; the record stores the stock compounds themselves as top-level final ingredients. | `data/normalized_yaml/bacterial/modified_nitrosospaera_medium.yaml`; MediaDive stock migration. |
| major | Water rows from multiple compartments are duplicate-merged into an impossible final-medium mass concentration. | MediaDive has separate 1000 ml or 50 ml water rows inside the main recipe and individual stocks; the record has `3150.0 G_PER_L` with a duplicate-merge note. | `data/normalized_yaml/bacterial/modified_nitrosospaera_medium.yaml`; duplicate cleanup must preserve compartment boundaries. |
| major | Several concentrated 50 ml and 1 L stock recipes are recorded as final-medium concentrations. | NaHCO3 is the 84 g/L concentration of a 1 M 50 ml stock, NH4Cl is 53.4 g/L in a 50 ml stock, sodium pyruvate is 110 g/L in a 50 ml stock, and HEPES is 238.4 g/L in a 1 L stock; the final medium uses only small ml additions of those stocks. | `data/normalized_yaml/bacterial/modified_nitrosospaera_medium.yaml`; MediaDive stock migration. |
| major | `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride. | MediaDive specifies `NiCl2 x 6 H2O`; the record links `CHEBI:34887` / `nickel dichloride`. | `data/normalized_yaml/bacterial/modified_nitrosospaera_medium.yaml`; compound grounding. |
| minor | Preparation steps lost structured stock ownership. | MediaDive attaches sterile-stock storage and filtration steps to the trace-element, HEPES, FeNaEDTA, NaHCO3, NH4Cl, and sodium-pyruvate solutions; the record stores those directions as one top-level sequence. | `data/normalized_yaml/bacterial/modified_nitrosospaera_medium.yaml`; preparation-step migration. |

## Recommended Edits

1. Re-curate `data/normalized_yaml/bacterial/modified_nitrosospaera_medium.yaml` so it represents MediaDive 1630c as Basic-FWM plus six stock additions, preserving each `solution_id`, stock amount, and stock composition.
2. Preserve separate water rows within the main medium and each stock instead of flattening them into a duplicate-merged `3150.0 G_PER_L` ingredient.
3. Move HCl and the trace metals, FeNa-EDTA, NaHCO3, NaOH/HEPES, NH4Cl, and sodium pyruvate into their source stock compartments and keep only the source ml stock additions at the main-medium level.
4. Re-ground `NiCl2 x 6 H2O` to the exact nickel chloride hexahydrate form or leave it unresolved instead of linking the anhydrous salt.
5. Regenerate `data/merge_yaml/merged/modified_Nitrosospaera_medium.yaml` after the normalized source is corrected.

## Follow-up Checks

1. Re-run focused open-schema, strict, reference, and term validators on `data/normalized_yaml/bacterial/modified_nitrosospaera_medium.yaml` and the regenerated merge output.
2. Manually compare the regenerated record against MediaDive `1630c`, checking all six stock-solution addition volumes, all stock-level recipe amounts, pH 7.5, and the stock-scoped preparation steps.
3. Verify that no water row from a stock recipe is merged with the 1000 ml Basic-FWM water row.

## Additional Notes

The repository-level `just` validators were not used for this focused record review because the project currently attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The focused validators above were run with Python 3.11 and the offline uv cache.
