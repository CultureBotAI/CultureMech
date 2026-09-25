# YAML Record Review: Methanothrix Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanothrix_medium__9bbb8dff.yaml
- Started UTC: 2026-09-24T05:27:18Z
- Finished UTC: 2026-09-24T05:28:22Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/methanothrix_medium__9bbb8dff.yaml`, a generated `MediaRecipe` for `CultureMech:008250` with `name: methanothrix_medium`, `original_name: Methanothrix Medium`, and source grounding `TOGO:M1690`.

The record was merged from one normalized input:

- `data/normalized_yaml/archaea/TOGO_M1690_Methanothrix_Medium.yaml`

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanothrix_medium__9bbb8dff.yaml` | Passed; exited 0 with no diagnostics. |
| `python scripts/validate_strict.py data/merge_yaml/merged/methanothrix_medium__9bbb8dff.yaml --out /private/tmp/methanothrix_medium__9bbb8dff.strict.tsv --workers 1 --quiet` | Passed; scanned 1 file and reported 0 error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/methanothrix_medium__9bbb8dff.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the reference validator performed 0 checks for this file. |
| `linkml-term-validator validate-data data/merge_yaml/merged/methanothrix_medium__9bbb8dff.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils` `pkg_resources` deprecation warning. |
| Embedded curation history | Not checked: the documented history validator is a standalone `history/` validator, not a focused check for `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

The medium identity is correct. TOGO M1690 is `Methanothrix Medium`, and its original source is NBRC medium 897 at `https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=897`.

The formulation graph is not correct. NBRC 897 has a final 1 L medium with 5 ml Trace elements solution and 10 ml Vitamin solution. Those two stock recipes are defined inline below the main formula, but the generated YAML moved both stocks into empty `solutions` rows, changed the stock-addition volumes to G_PER_L, flattened the stock constituents into final ingredients, and merged repeated water and CaCl2 rows across recipe scopes.

## Evidence

Supported source claims:

- TOGO M1690 and NBRC 897 support the record's identity, NBRC 897 original accession, 1 L distilled-water final medium, and direct final-medium rows for sodium acetate, NH4Cl, KH2PO4, NaCl, MgCl2 x 6 H2O, CaCl2 x 2 H2O, resazurin, NaHCO3, cysteine-HCl, and Na2S x 9 H2O.
- The source supports 5 ml Trace elements solution and 10 ml Vitamin solution as final-medium stock additions.
- The source supports autoclaving the main mix under N2/CO2 80/20, separately autoclaving cysteine-HCl and Na2S x 9 H2O as 5% solutions under N2, and aseptically adding filter-sterile vitamin solution and the two reducing solutions.
- The source supports the Trace elements stock preparation note that first dissolves NTA, adjusts pH to 6.5 with NaOH, then adds minerals to final pH 7.0.

Unsupported or over-scoped generated claims:

- Trace elements rows from NTA through Na2SeO3/Na2WO4 belong to the stock used at 5 ml per liter, not the final top-level medium.
- Vitamin rows from biotin through nicotinic acid belong to the stock used at 10 ml per liter, not the final top-level medium.
- CaCl2 x 2 H2O appears once in the main medium and once in Trace elements solution; the generated 0.098 G_PER_L row is an unsupported cross-scope sum.
- The three water rows are distinct 1 L final-medium, 1 L Trace elements, and 1 L Vitamin solution rows; the generated 3.0 G_PER_L row is an unsupported cross-scope sum.
- Source mg and ml rows were not converted: resazurin 1 mg, the 5 ml and 10 ml stock additions, KAl(SO4)2 x 12H2O 8 mg in TOGO, Na2WO4 1.6 mg, Na2SeO3 1.6 mg, and all vitamin-stock mg rows were serialized as G_PER_L values.
- Current NBRC 897 lists KAl(SO4)2 x 12H2O as 0.02 g, while the inspected TOGO M1690 payload lists 8 mg.

## Completeness

The schema-optional evidence, discussions, growth, target organism, and recipe variant arrays are empty; empty optional slots were not treated as defects.

Consequential gaps:

- The inline Trace elements solution and Vitamin solution have no scoped stock compositions.
- The final-medium anaerobic preparation, cysteine/sulfide stock sterilization, vitamin filtration, and Trace elements pH instructions are absent.
- The source N2/CO2 80/20 atmosphere is represented only as independent variable gas ingredients.
- The NBRC-vs-TOGO KAl(SO4)2 x 12H2O difference is unresolved.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Two NBRC stock solutions were flattened into final-medium ingredients. | NBRC 897 and TOGO M1690 use 5 ml Trace elements solution and 10 ml Vitamin solution in the main recipe and define each stock separately. The YAML keeps empty stock references and stores every stock constituent as a top-level ingredient. | `data/normalized_yaml/archaea/TOGO_M1690_Methanothrix_Medium.yaml`; TOGO import and solution migration. |
| Major | mg, ml, and L source units were serialized as G_PER_L. | The source has 1 mg resazurin, 5 ml and 10 ml stock additions, multiple mg stock ingredients, and 1 L water rows. The YAML stores those numeric values as G_PER_L. | `data/normalized_yaml/archaea/TOGO_M1690_Methanothrix_Medium.yaml`; TOGO import. |
| Major | Duplicate cleanup merged ingredients across final-medium and stock scopes. | CaCl2 x 2 H2O was summed from 0.08 g in the main medium and 0.018 g in Trace elements solution, and water was summed across the main, Trace elements, and Vitamin scopes. | `data/normalized_yaml/archaea/TOGO_M1690_Methanothrix_Medium.yaml`; duplicate cleanup. |
| Major | Preparation instructions were dropped. | NBRC 897 includes final-medium anaerobic preparation and a Trace elements pH protocol. No `preparation_steps` or equivalent field preserves those comments in the YAML. | `data/normalized_yaml/archaea/TOGO_M1690_Methanothrix_Medium.yaml`; TOGO import. |
| Major | One Trace elements quantity disagrees with the live NBRC source. | Current NBRC 897 lists KAl(SO4)2 x 12H2O as 0.02 g; TOGO M1690 and the generated record carry 8 mg, before the generated record further changes the unit to G_PER_L. | `data/normalized_yaml/archaea/TOGO_M1690_Methanothrix_Medium.yaml`; source-version review. |

## Recommended Edits

1. Preserve Trace elements solution and Vitamin solution as scoped stock recipes added to the final medium at 5 ml and 10 ml.
2. Preserve source mg, ml, and L units or convert them only with dimensionally valid stock/final-volume arithmetic.
3. Keep same-named water and CaCl2 rows separate when they belong to different recipe scopes.
4. Restore the NBRC preparation comments with final-medium text and Trace elements text scoped separately.
5. Resolve the KAl(SO4)2 x 12H2O discrepancy by checking whether NBRC 897 changed after the TOGO capture or whether TOGO imported the row incorrectly.
6. Regenerate `data/merge_yaml/merged/methanothrix_medium__9bbb8dff.yaml`.

## Follow-up Checks

- Run focused schema, strict, reference, and term validation on the regenerated record.
- Diff the regenerated record against TOGO M1690 and NBRC 897 and verify that no Trace elements or Vitamin solution constituent appears as a final-medium top-level ingredient.
- Verify that resazurin, KAl(SO4)2 x 12H2O, Na2WO4, Na2SeO3, and Vitamin solution ingredients are no longer over-stated by treating mg as G_PER_L.
- Re-fetch the NBRC 897 page and TOGO M1690 API and decide whether the maintained record should retain TOGO's 8 mg KAl(SO4)2 x 12H2O or update to the live NBRC 0.02 g value.

## Additional Notes

- Empty optional evidence and discussion fields were not treated as defects.
- Exact owner searches used `rg --no-ignore --hidden`, so ignored files were included when resolving `CultureMech:008250` and `data/normalized_yaml/archaea/TOGO_M1690_Methanothrix_Medium.yaml`.
