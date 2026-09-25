# YAML Record Review: Methanothrix Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanothrix_medium__0ac02978.yaml
- Started UTC: 2026-09-24T05:24:02Z
- Finished UTC: 2026-09-24T05:25:59Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/methanothrix_medium__0ac02978.yaml`, a generated `MediaRecipe` for `CultureMech:008945` with `name: methanothrix_medium`, `original_name: Methanothrix Medium`, and source grounding `TOGO:M235`.

The record was merged from one normalized input:

- `data/normalized_yaml/archaea/TOGO_M235_Methanothrix_Medium.yaml`

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanothrix_medium__0ac02978.yaml` | Passed; exited 0 with no diagnostics. |
| `python scripts/validate_strict.py data/merge_yaml/merged/methanothrix_medium__0ac02978.yaml --out /private/tmp/methanothrix_medium__0ac02978.strict.tsv --workers 1 --quiet` | Passed; scanned 1 file and reported 0 error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/methanothrix_medium__0ac02978.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the reference validator performed 0 checks for this file. |
| `linkml-term-validator validate-data data/merge_yaml/merged/methanothrix_medium__0ac02978.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils` `pkg_resources` deprecation warning. |
| Embedded curation history | Not checked: the documented history validator is a standalone `history/` validator, not a focused check for `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

The medium identity is correct. TOGO M235 is `Methanothrix Medium`, and its original source is JCM medium 243 at `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=243`.

The ingredient graph is not correct. JCM 243 has a main 1 L medium, adds 10 ml Trace element solution made separately to 1 L, and adds 10 ml Trace vitamins from JCM Medium 197 through TOGO M190. The generated record flattens Trace element solution into final top-level ingredients, leaves both `solutions` entries empty, changes 10 ml stock additions into 10 G_PER_L concentrations, and then merges same-named final-medium and stock ingredients.

## Evidence

Supported source claims:

- JCM 243 and TOGO M235 support the record's name, TOGO identifier, JCM source accession, liquid archaeal culture-medium identity, and the direct final-medium rows for KH2PO4, NH4Cl, MgCl2 x 6 H2O, sodium acetate, KHCO3, cysteine, and Na2S x 9 H2O.
- JCM 243 supports one main-medium water row, 0.6 g NaCl, 0.08 g CaCl2 x 2 H2O, and 1 mg resazurin in the 1 L final medium.
- JCM 243 supports adding 10 ml Trace element solution from the inline stock recipe and 10 ml Trace vitamins from JCM 197.
- JCM 243 supports an N2-CO2 80:20 anaerobic atmosphere, separate stock sterilization under N2, and 100 kPa N2-CO2 pressurization after inoculation.

Unsupported or over-scoped generated claims:

- NaCl and CaCl2 x 2 H2O are final-medium ingredients and also Trace element solution ingredients, but the record sums them into single final-medium concentrations of 1.6 G_PER_L and 0.18 G_PER_L.
- H3BO3, MnCl2 x 4 H2O, CoCl2 x 6 H2O, NiCl2 x 6 H2O, CuCl2 x 2 H2O, ZnCl2, Na2SeO3 x 5 H2O, FeCl3 x 6 H2O, nitrilotriacetic acid, and KOH belong to Trace element solution, not the final medium.
- The final-medium and Trace element solution water rows are not 2.0 G_PER_L of final-medium water.
- Resazurin is a 1 mg addition in 1 L; the generated 1 G_PER_L row is not source-equivalent.
- The two 10 ml stock additions are volumetric additions, not 10 G_PER_L chemical concentrations.
- Carbon dioxide and N2 are preparation and headspace gases in an 80:20 atmosphere, not unspecified variable final ingredients.

## Completeness

The schema-optional evidence, discussions, growth, target organism, and recipe variant arrays are empty; empty optional slots were not treated as defects.

Consequential gaps:

- The inline Trace element solution has no scoped stock composition.
- The referenced Trace vitamins from JCM 197 is a named cross-reference only; TOGO M190 identifies the target stock, but the `solutions` row carries no composition.
- The complete JCM preparation text is absent, including pH adjustment to 7.0, boiling and cooling under N2-CO2, anaerobic dispensing, overnight post-autoclave standing, separate cysteine and sulfide 5% solutions, filter-sterilized Trace vitamins, anaerobic post-autoclave addition, 100 kPa pressurization, Trace element solution pH steps, and the JCM 10134 inoculum comment.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The inline Trace element solution was flattened into final-medium ingredients. | JCM 243 lists Trace element solution as a 10 ml stock addition and then defines that stock separately. The YAML leaves `Trace element solution (see below)` with an empty `composition` array and stores all stock constituents as top-level ingredients. | `data/normalized_yaml/archaea/TOGO_M235_Methanothrix_Medium.yaml`; TOGO import and solution migration. |
| Major | Original units were serialized as G_PER_L. | JCM 243 lists 10 ml Trace element solution, 10 ml Trace vitamins, 1 mg resazurin, and 1 L distilled water rows. The YAML stores the solution additions as 10 G_PER_L, resazurin as 1 G_PER_L, and water as G_PER_L. | `data/normalized_yaml/archaea/TOGO_M235_Methanothrix_Medium.yaml`; TOGO import. |
| Major | Duplicate cleanup merged ingredients across final-medium and stock scopes. | The source has separate NaCl, CaCl2 x 2 H2O, and distilled-water rows in the final medium and Trace element solution. The generated YAML carries single merged NaCl, CaCl2 x 2 H2O, and water rows. | `data/normalized_yaml/archaea/TOGO_M235_Methanothrix_Medium.yaml`; duplicate cleanup. |
| Major | JCM preparation instructions were dropped. | JCM 243 gives final-medium anaerobic preparation, stock sterilization, pre-inoculation addition, and Trace element solution pH instructions. No preparation or condition field in the YAML preserves them. | `data/normalized_yaml/archaea/TOGO_M235_Methanothrix_Medium.yaml`; TOGO import. |

## Recommended Edits

1. Preserve Trace element solution as a scoped stock recipe containing nitrilotriacetic acid, FeCl3 x 6 H2O, MnCl2 x 4 H2O, CoCl2 x 6 H2O, CaCl2 x 2 H2O, ZnCl2, CuCl2 x 2 H2O, H3BO3, NaCl, NiCl2 x 6 H2O, Na2SeO3 x 5 H2O, and 1 L distilled water.
2. Preserve Trace vitamins as a 10 ml cross-reference to TOGO M190/JCM 197 rather than an empty 10 G_PER_L stock.
3. Retain source units for ml, mg, and L rows instead of assigning every TOGO amount to G_PER_L.
4. Keep same-named ingredients separate when they belong to the final medium versus Trace element solution.
5. Carry the JCM final-medium and Trace element solution preparation paragraphs into scoped preparation fields or another maintained representation that survives merge generation.
6. Regenerate `data/merge_yaml/merged/methanothrix_medium__0ac02978.yaml`.

## Follow-up Checks

- Run focused schema, strict, reference, and term validation on the regenerated record.
- Diff the regenerated record against TOGO M235 and JCM 243 and verify that no Trace element solution constituent appears as a final-medium top-level ingredient.
- Verify that the two stock additions remain 10 ml additions and that resazurin remains a 1 mg addition or a dimensionally equivalent 0.001 G_PER_L concentration.
- Verify that the N2-CO2 atmosphere, pH 7.0 adjustment, separate 5% cysteine and sulfide stock sterilization, Trace vitamins filter sterilization, Trace element solution pH steps, and JCM 10134 inoculum comment are represented in scoped fields.

## Additional Notes

- Empty optional evidence and discussion fields were not treated as defects.
- Exact owner searches used `rg --no-ignore --hidden`, so ignored files were included when resolving `CultureMech:008945` and `data/normalized_yaml/archaea/TOGO_M235_Methanothrix_Medium.yaml`.
