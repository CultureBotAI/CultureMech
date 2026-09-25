# YAML Record Review: Leptospirillum (HH) Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/leptospirillum_hh_medium__a790ec43.yaml
- Started UTC: 2026-09-23T19:37:02Z
- Finished UTC: 2026-09-23T19:38:32Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:008627 |
| Name | leptospirillum_hh_medium |
| Original name | Leptospirillum (HH) Medium |
| Category | bacterial |
| Physical state | LIQUID |
| Media grounding | TOGO:M2038 |
| Source provenance | Togo M2038 imported from NBRC_M1336 |
| Generated file | data/merge_yaml/merged/leptospirillum_hh_medium__a790ec43.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M2038_Leptospirillum_HH_Medium.yaml |
| Merge fingerprint | a790ec437dedf9b03d08078b9dbe903d13c18195c56dd253e5fcf99bde7f8506 |

The reviewed target is a generated one-source Togo merge for NBRC 1336. Future fixes belong in the maintained Togo normalized owner, followed by regeneration of `data/merge_yaml/merged/` and downstream products.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/leptospirillum_hh_medium__a790ec43.yaml`. |
| Strict validator | Passed with zero error rows in `/private/tmp/leptospirillum_hh_medium__a790ec43.strict.tsv`. |
| LinkML reference validator | Passed; the reference validator completed with zero checks because this generated record has no `references` collection. |
| LinkML term validator | Passed. |
| Embedded curation history | Not checked: the repository history validator validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

Togo M2038 and NBRC Medium 1336 identify the pH 1.8 Leptospirillum HH medium. This is related to DSMZ Medium 882, but it is not an exact duplicate: NBRC uses final pH 1.8, adjusts the Trace element solution to pH 1.8, and specifies MnCl2 x 2 H2O at 62 mg rather than DSMZ's MnCl2 x 4 H2O at 76 mg.

An ignored-inclusive exact search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:008627`, `TOGO:M2038`, `NBRC_M1336`, `NO=1336`, the maintained filename, the shared slug, and the merge fingerprint found this generated record, its Togo owner, the related KOMODO/MediaDive DSMZ 882 owners, a separate generated DSMZ/KOMODO merge, source indexes, and validation archives. NBRC 1336 should be linked as a variant of HH medium rather than collapsed into the DSMZ 882 default.

## Evidence

Supported in the inspected NBRC and Togo sources:

- The Togo M2038 / NBRC 1336 identity, pH 1.8 endpoint, and Leptospirillum HH label are supported.
- The main mixture contains 950 ml Solution A, 50 ml Solution B, and 1 ml Trace element solution.
- Solution A contains 132 mg (NH4)2SO4, 53 mg MgCl2 x 6 H2O, 27 mg KH2PO4, 147 mg CaCl2 x 2 H2O, and 950 ml distilled water, adjusted to pH 1.8 with 10 N H2SO4.
- Solution B contains 20 g FeSO4 x 7 H2O and 50 ml H2SO4 Solution 0.25 N; the solution pH should be 1.2.
- The Trace element solution contains 62 mg MnCl2 x 2 H2O, 68 mg ZnCl2, 64 mg CoCl2 x 6 H2O, 31 mg H3BO3, 10 mg Na2MoO4, 67 mg CuCl2 x 2 H2O, and 1 L distilled water.
- NBRC instructs separate autoclaving at 112 C for 30 min before mixing.

Unsupported or incomplete in the generated record:

- Main-solution, Solution A, Solution B, and Trace element solution quantities are mixed together as top-level ingredients and separate `solutions`, duplicating the same material in incompatible units.
- The Solution A milligram rows are represented as very large g/L rows, such as 147 g/L CaCl2 x 2 H2O instead of 147 mg in 950 ml.
- Distilled water is merged into `951 G_PER_L` from unrelated 950 ml and 1 L stock-solution rows.
- The sulfuric acid roles are not recoverable: 10 N H2SO4 pH adjustment is defaulted to `VARIABLE`, and 50 ml of 0.25 N H2SO4 is stored as `50 G_PER_L`.
- The pH 1.8 endpoint and NBRC autoclaving/mixing instructions are absent from structured fields.
- CoCl2 x 6 H2O is grounded only to cobalt dichloride.
- The record has no structured reference to Togo M2038 or NBRC 1336.

## Completeness

The record preserves the NBRC source identity and most named stock ingredients, but it is incomplete for nested stock-solution semantics, pH and sterilization, sulfuric-acid normality, cobalt chloride hexahydrate grounding, structured references, and variant linkage to the DSMZ 882 HH formulation.

Empty optional organism, incubation, and storage fields are acceptable for this review because the inspected NBRC and Togo entries do not provide them.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Critical | Nested stock solutions were flattened and duplicated into incompatible top-level rows. | NBRC 1336 has 950 ml Solution A, 50 ml Solution B, and 1 ml Trace element solution; the YAML contains those solution rows and also lists their internal stock ingredients as final ingredients. | `data/normalized_yaml/bacterial/TOGO_M2038_Leptospirillum_HH_Medium.yaml` or the Togo importer |
| Critical | Sulfuric acid quantities lose their normality and purpose. | NBRC uses 10 N H2SO4 only to adjust Solution A to pH 1.8, and 50 ml of 0.25 N H2SO4 in Solution B; the YAML stores one H2SO4 row as `VARIABLE` and another as `50 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M2038_Leptospirillum_HH_Medium.yaml` or the Togo importer |
| Major | Solution A milligram-scale rows are off by orders of magnitude. | NBRC lists 132, 53, 27, and 147 mg of the Solution A salts; the YAML stores 132, 53, 27, and 147 g/L. | `data/normalized_yaml/bacterial/TOGO_M2038_Leptospirillum_HH_Medium.yaml` or the Togo importer |
| Major | pH and sterilization instructions are missing. | NBRC specifies pH 1.8 for the final medium, pH 1.8 for Solution A and the trace-element solution, pH 1.2 for Solution B, and separate autoclaving at 112 C for 30 min. | `data/normalized_yaml/bacterial/TOGO_M2038_Leptospirillum_HH_Medium.yaml` |
| Minor | CoCl2 x 6 H2O is over-broadly grounded. | The NBRC ingredient is cobalt chloride hexahydrate, while the row's ChEBI term is cobalt dichloride. | `data/normalized_yaml/bacterial/TOGO_M2038_Leptospirillum_HH_Medium.yaml` |
| Minor | Structured references are missing. | The generated reference validator performed zero checks despite available Togo and NBRC source URLs. | `data/normalized_yaml/bacterial/TOGO_M2038_Leptospirillum_HH_Medium.yaml` |

## Recommended Edits

1. Preserve NBRC 1336 as a hierarchical solution recipe with Solution A, Solution B, and Trace element solution.
2. Represent Solution A salts as milligram amounts in 950 ml water or normalized g/L values within Solution A only.
3. Represent 10 N H2SO4 as a pH adjustment and 50 ml of 0.25 N H2SO4 as the liquid acid component of Solution B.
4. Add pH 1.8, pH 1.2 for Solution B, and the 112 C autoclaving/mixing instructions from NBRC.
5. Replace the CoCl2 x 6 H2O grounding with a hexahydrate-specific term if one is available, or leave that hydrate row unmapped.
6. Add structured references for Togo M2038 and NBRC 1336, and link the NBRC pH-1.8 medium as a related variant of DSMZ 882.
7. Regenerate `data/merge_yaml/merged/` and downstream pages.

## Follow-up Checks

- Rerun open schema validation, the strict validator, the reference validator, and the term validator on the regenerated YAML.
- Manually compare the regenerated NBRC recipe against NBRC 1336 for Solution A, Solution B, Trace element solution, 0.25 N H2SO4, final pH 1.8, and MnCl2 x 2 H2O.
- Re-run an ignored-inclusive exact search for `TOGO:M2038`, `NBRC_M1336`, and `mediadive.medium:882` to confirm that the NBRC and DSMZ HH media are linked but preserve their pH and manganese-hydrate differences.

## Additional Notes

The separate DSMZ 882 generated merge has a pH 2.3 default and uses MnCl2 x 4 H2O; the NBRC 1336 recipe reviewed here should not be used to overwrite those DSMZ details.
