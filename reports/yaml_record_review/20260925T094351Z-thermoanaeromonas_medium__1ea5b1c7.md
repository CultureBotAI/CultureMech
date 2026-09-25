# YAML Record Review: Thermoanaeromonas Medium
- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermoanaeromonas_medium__1ea5b1c7.yaml`
- Started UTC: `2026-09-25T09:43:51Z`
- Finished UTC: `2026-09-25T09:45:16Z`
- Verdict: needs curation

## Target
Generated TOGO bacterial recipe `CultureMech:010220`, `thermoanaeromonas_medium`, with medium term `TOGO:M808` and label `Thermoanaeromonas Medium`.

It is a single-source generated record from `TOGO_M808_Thermoanaeromonas_Medium`.

## Validation
- LinkML schema validation: passed; `linkml-validate` reported `No issues found`.
- Strict validation: passed; `scripts/validate_strict.py` scanned 1 file with 0 files containing errors and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` checked 1 file and reported all checked references passed.
- Term validation: passed; `linkml-term-validator` reported `Validation passed`.
- Embedded `curation_history`: Not checked. The available history validator targets standalone `history/` entries rather than `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding
The record correctly points to JCM Medium 778, `THERMOANAEROMONAS MEDIUM`, through TOGO M808.

The same JCM 778 URL is also present in a direct JCM import emitted as `data/merge_yaml/merged/THERMOANAEROMONAS_MEDIUM.yaml`, so JCM 778 remains split across exact source-equivalent generated branches.

Most reviewed ingredient groundings match their source strings, though several hydrate names still use source punctuation and should be normalized to the ASCII hydrate style used elsewhere before merge comparison.

## Evidence
JCM 778 specifies KH2PO4, K2HPO4, NH4Cl, NaCl, KCl, CaCl2 x 2 H2O, MgCl2 x 6 H2O, 10 ml Trace minerals cross-referenced to JCM Medium 151, yeast extract, trypticase peptone, 1 mg resazurin, and water to 1 L in the base medium.

After autoclaving under an N2/CO2 gas phase, JCM adds 25 ml of 8% NaHCO3 solution, 8 ml of 5% Na2S x 9 H2O solution, and 20 ml of 1 M glucose solution per liter.

The generated TOGO branch converts the source's 1 L water row into `1 G_PER_L` and its 1 mg resazurin row into `1 G_PER_L`.

The post-autoclave stock additions are retained only as empty solution stubs with their milliliter source volumes placed into `G_PER_L` concentration fields: `25 G_PER_L` for 8% NaHCO3 solution, `20 G_PER_L` for 1 M Glucose solution, and `8 G_PER_L` for 5% Na2S x 9 H2O solution.

The 10 ml Trace minerals stock remains an unresolved empty cross-reference to JCM Medium 151 rather than a structured stock addition.

## Completeness
The TOGO branch loses the JCM preparation step describing N2/CO2 dispensing, butyl-rubber sealing, autoclaving, and anaerobic post-autoclave addition of bicarbonate, sulfide, and glucose stocks.

The source trace-mineral cross-reference is not resolved or structured, so any downstream consumer sees a stock name with no composition.

## Findings
1. Needs curation: source volumes in liters and milliliters were converted to `G_PER_L`, including `Distilled water` at `1 G_PER_L` and three stock solution additions.
2. Needs curation: source `1 mg` resazurin was converted to `1 G_PER_L`.
3. Needs curation: Trace minerals from JCM Medium 151 are represented as an empty `Unknown solution`.
4. Needs curation: the JCM 778 direct import remains an unmerged duplicate branch for the same source URL.

## Recommended Edits
1. Normalize `TOGO_M808_Thermoanaeromonas_Medium` in `data/normalized_yaml`, not the generated merge file, so source liters, milliliters, and milligrams are parsed by unit rather than as grams per liter.
2. Represent the 8% NaHCO3, 5% Na2S x 9 H2O, and 1 M glucose rows as 25 ml, 8 ml, and 20 ml post-autoclave stock additions.
3. Resolve the Trace minerals cross-reference to JCM Medium 151 or keep it as an explicit external stock reference instead of an empty unnamed solution.
4. Merge `TOGO:M808` with the direct JCM 778 import after both branches use equivalent stock and preparation semantics.

## Follow-up Checks
After source normalization and merge regeneration, re-run schema, strict, reference, and term validation.

Run an exact duplicate search with ignored files included for `TOGO:M808`, `JCM_J778_THERMOANAEROMONAS_MEDIUM`, and `jcm_grmd?GRMD=778` and confirm that JCM 778 regenerates as one canonical output.

## Additional Notes
Exact duplicate-source searches included ignored files.
