# YAML Record Review: HALOTHIOBACILLUS LS2 MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/halothiobacillus_ls2_medium.yaml`
- Started UTC: 2026-09-23T11:34:35Z
- Finished UTC: 2026-09-23T11:35:25Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:015859` |
| Name | `halothiobacillus_ls2_medium` |
| Original name | `HALOTHIOBACILLUS LS2 MEDIUM` |
| Category | `bacterial` |
| Physical state | `LIQUID` |
| pH | `6.5` |
| Generated from | `data/normalized_yaml/bacterial/JCM_J1419_HALOTHIOBACILLUS_LS2_MEDIUM.yaml` |
| Source accession | `jcm.grmd:1419` |
| Source URL | `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1419` |
| Merge fingerprint | `c71068f0022b8e70114a020aa7b66fd36c9ebb687c44f56b150c77dfed9a1b58` |

I reviewed the generated merged record, its direct JCM normalized owner, and
the live JCM 1419 page.

I searched `data/normalized_yaml` and `data/merge_yaml` YAML files with
`rg --no-ignore --hidden` for `jcm.grmd:1419`, `JCM Medium J1419`,
`jcm_grmd?GRMD=1419`, `GRMD=1419`, `HALOTHIOBACILLUS LS2 MEDIUM`, and
`halothiobacillus_ls2_medium`. Ignored files were included. The search found
only the direct JCM J1419 normalized owner and the reviewed generated record.

## Validation

| Check | Result |
|---|---|
| Open schema | Passed: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/halothiobacillus_ls2_medium.yaml` reported `No issues found`. |
| Strict schema | Passed: `python scripts/validate_strict.py data/merge_yaml/merged/halothiobacillus_ls2_medium.yaml --out /private/tmp/halothiobacillus_ls2_medium.strict.tsv --workers 1 --quiet` scanned one file and reported `total ERROR rows: 0`. |
| References | Passed with no checked references: `linkml-reference-validator validate data data/merge_yaml/merged/halothiobacillus_ls2_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` reported `Total checks: 0`. |
| Terms | Passed: `linkml-term-validator validate-data data/merge_yaml/merged/halothiobacillus_ls2_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone records under `history/`, not embedded `MediaRecipe.curation_history` entries. |

The `just` validator entrypoints were not used because this checkout attempts
to resolve a Python 3.13 environment with `llvmlite==0.46.0`; the focused
validators above were run offline with Python 3.11 against the local uv cache.

## Identity and Grounding

The record correctly identifies JCM medium 1419,
`HALOTHIOBACILLUS LS2 MEDIUM`, and its bacterial category is consistent with
the medium name. The directly weighed main ingredients KH2PO4, NaCl, and
`MgCl2 x 6 H2O` match the JCM amounts.

The generated record does not preserve the stock boundaries for Modified A5 or
the four post-cooling filter-sterilized solutions. It also contains a
`NiCl2 x 6 H2O` ingredient that is not listed on the inspected JCM 1419 page.

## Evidence

JCM 1419 lists the final-medium base as 0.4 g KH2PO4, 1.0 g NaCl, 0.12 g
`MgCl2 x 6 H2O`, 1.0 ml Modified A5 solution, and 1.0 L distilled water. The
generated record imports the water as `1.0 ML_PER_L` and flattens Modified A5
components into top-level ingredients at stock g/L concentration.

JCM 1419 then says that, after cooling, four filter-sterilized solutions are
added: 2.5 ml 8% NaHCO3, 0.4 ml 0.1 M FeCl2, 1.0 ml 1.0 M NH4Cl, and 10.0 ml
1.0 M sodium thiosulfate. The generated record imports those labels and ml/L
amounts as plain ingredient rows; it does not model them as post-autoclave
filter-sterilized solution additions.

The JCM Modified A5 stock contains H3BO3, `ZnSO4 x 7 H2O`,
`Na2MoO4 x 2 H2O`, `MnCl2 x 4 H2O`, `CuSO4 x 5 H2O`, `CoCl2 x 6 H2O`, and
1.0 L distilled water. The generated record has those compounds but also
includes unsupported `NiCl2 x 6 H2O`.

## Completeness

The generated record is missing the 1 L final-medium water volume, the 1 L
Modified A5 water row, the 1 ml/L Modified A5 reference, and the structured
post-cooling addition of four filter-sterilized solutions.

The solid-medium option is present only as free text. JCM says to add 15 g/L
agar and 0.1 g/L Na2SO4 before autoclaving for solid media.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Modified A5 was flattened into top-level ingredients. | JCM lists `Modified A5 solution` as a 1 ml addition and defines its composition in a separate table; the generated H3BO3, Zn, Mo, Mn, Cu, and Co rows are stock ingredients. | `data/normalized_yaml/bacterial/JCM_J1419_HALOTHIOBACILLUS_LS2_MEDIUM.yaml` or the JCM scraper |
| Major | The final water row was imported with the wrong unit. | JCM lists `Distilled water` as 1.0 L; the generated concentration is `1.0 ML_PER_L`. | `data/normalized_yaml/bacterial/JCM_J1419_HALOTHIOBACILLUS_LS2_MEDIUM.yaml` or the JCM scraper |
| Major | Four filter-sterilized post-cooling additions are unstructured. | JCM scopes 8% NaHCO3, 0.1 M FeCl2, 1.0 M NH4Cl, and 1.0 M sodium thiosulfate to after-cooling, filter-sterilized addition; the generated record stores them as simple ingredients. | `data/normalized_yaml/bacterial/JCM_J1419_HALOTHIOBACILLUS_LS2_MEDIUM.yaml` or the JCM scraper |
| Major | The record has an unsupported `NiCl2 x 6 H2O` row. | The inspected JCM 1419 Modified A5 table has no nickel chloride row. | `data/normalized_yaml/bacterial/JCM_J1419_HALOTHIOBACILLUS_LS2_MEDIUM.yaml` or the JCM scraper |
| Minor | Solid-medium agar and Na2SO4 are not structured as a variant. | JCM says to add 15 g/L agar and 0.1 g/L Na2SO4 before autoclaving for solid media; the record keeps that only as preparation prose. | `data/normalized_yaml/bacterial/JCM_J1419_HALOTHIOBACILLUS_LS2_MEDIUM.yaml` |
| Minor | `CoCl2 x 6 H2O` is grounded to generic cobalt dichloride through its MIM/CHEBI field. | The source ingredient is a hexahydrate; the generated row's only ontology link is `CHEBI:35696` / cobalt dichloride. | Ingredient grounding for the JCM normalized record |

## Recommended Edits

1. In the JCM scraper or
   `data/normalized_yaml/bacterial/JCM_J1419_HALOTHIOBACILLUS_LS2_MEDIUM.yaml`,
   preserve Modified A5 as a stock solution and reference it from the main
   medium at 1 ml/L.
2. Restore 1 L distilled water to the final medium and 1 L distilled water to
   Modified A5.
3. Represent 8% NaHCO3, 0.1 M FeCl2, 1.0 M NH4Cl, and 1.0 M sodium
   thiosulfate as filter-sterilized post-cooling solution additions.
4. Remove the unsupported `NiCl2 x 6 H2O` row unless a separate inspected
   source is found for a nickel-containing Modified A5 variant.
5. Model the optional solid recipe as a variant that adds 15 g/L agar and
   0.1 g/L Na2SO4 before autoclaving.
6. Resolve exact hexahydrate grounding for `CoCl2 x 6 H2O`.
7. Regenerate merged recipes from the corrected normalized owner; do not patch
   `data/merge_yaml/merged/halothiobacillus_ls2_medium.yaml` directly.

## Follow-up Checks

1. Run `just validate data/normalized_yaml/bacterial/JCM_J1419_HALOTHIOBACILLUS_LS2_MEDIUM.yaml`
   after the normalized JCM 1419 record or scraper is corrected.
2. Run `just validate-terms data/normalized_yaml/bacterial/JCM_J1419_HALOTHIOBACILLUS_LS2_MEDIUM.yaml`
   to confirm exact cobalt hexahydrate grounding.
3. Run `just validate-media-variant-links` if the optional solid recipe is
   modeled as a variant.
4. Run `just verify-merges` to prove the generated JCM 1419 branch regenerates
   from the corrected normalized source.

## Additional Notes

None found.
