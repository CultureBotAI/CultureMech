# YAML Record Review: methanocaldococcus_jannaschii_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/methanocaldococcus_jannaschii_medium__682e654d.yaml`
- Started UTC: 2026-09-24T03:22:11Z
- Finished UTC: 2026-09-24T03:22:11Z
- Verdict: needs curation

## Target

- Stable ID: `CultureMech:002593`
- Label: `methanocaldococcus_jannaschii_medium`
- Category: `archaea`
- Maintained owners: `data/normalized_yaml/archaea/methanocaldococcus_jannaschii_medium.yaml`; merged with `data/normalized_yaml/bacterial/kosmotoga_pacifica_medium.yaml`
- Source identity: MediaDive/JCM medium J232, `METHANOCALDOCOCCUS JANNASCHII MEDIUM`

## Validation

- Open schema: Passed; `linkml-validate` reported no issues.
- Strict validator: Passed; 1 file scanned, 0 files with errors, and 0 error rows.
- Reference validator: Passed; 0 reference checks were applicable.
- Term validator: Passed.
- Embedded history: Not checked: the repository history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

- `media_term` grounds the canonical record to MediaDive/JCM `J232`.
- Exact ignored-file search for `CultureMech:002593`, `CultureMech:003331`, `mediadive.medium:J232`, `mediadive.medium:J982`, `kosmotoga_pacifica_medium`, and `methanocaldococcus_jannaschii_medium.yaml` confirmed that the generated record merges JCM 232 with JCM 982 / Kosmotoga pacifica as a `SOURCE_DUPLICATE`.
- JCM 982 is not the same formula as JCM 232: the live source says to use medium 232 supplemented with 3.0 g/L yeast extract and 2.4 g/L L-cystine and to cultivate under N2/CO2 at 4:1.
- A TOGO M225 import of the same JCM 232 source also exists as `data/merge_yaml/merged/methanocaldococcus_jannaschii_medium__078beb48.yaml`, so the direct JCM 232 recipe is duplicated elsewhere in generated output even before considering the J982 variant.

## Evidence

- The live JCM 232 page and MediaDive REST record both encode a 1000 ml main solution with 10 ml `Trace minerals`, 10 ml `Trace vitamins`, 980 ml water, 30 g NaCl, 3.4 g `MgSO4 x 7 H2O`, 0.14 g `CaCl2 x 2 H2O`, and the remaining defined salts, reductants, and resazurin.
- MediaDive solution 3804, `Trace minerals`, is a 1 L stock containing 1.5 g nitrilotriacetic acid, 3 g `MgSO4 x 7 H2O`, 1 g NaCl, 0.5 g `MnSO4 x n H2O`, 0.1 g `FeSO4 x 7 H2O`, 0.1 g `CoSO4 x 7 H2O`, 0.1 g `CaCl2 x 2 H2O`, 0.1 g `ZnSO4 x 7 H2O`, and 0.01 g each of `CuSO4 x 5 H2O`, `AlK(SO4)2`, H3BO3, and `Na2MoO4 x 2 H2O`.
- MediaDive solution 3861, `Trace vitamins`, is a 1 L stock containing milligram-per-liter vitamin amounts, including 2 mg/L biotin and folic acid, 0.1 mg/L vitamin B12, and 5 to 10 mg/L for the other listed vitamins.
- MediaDive keeps the nitrilotriacetic-acid pH adjustment inside `Trace minerals`, not as a main-medium pH adjustment.

## Completeness

- The MediaDive REST source and live JCM page provide enough evidence to encode the JCM 232 main formula, both trace stocks, pH 6.0, and preparation sequence.
- Empty `target_organisms` and `growth_data` are optional-field omissions, not review findings for this record.

## Findings

- Blocker: the `Trace minerals` and `Trace vitamins` stocks are flattened into top-level final-medium ingredients instead of being represented as 10 ml stock additions. This loses both stock identity and the 100-fold dilution into the 1000 ml final recipe.
- Blocker: duplicate salts that occur in both the main solution and the trace-minerals stock were summed at incompatible scales. `MgSO4 x 7 H2O` is `6.4` g/L because 3.4 g/L main plus 3 g/L stock were added, NaCl is `31.0` g/L because 30 g/L main plus 1 g/L stock were added, and `CaCl2 x 2 H2O` is `0.24000000000000002` g/L because 0.14 g/L main plus 0.1 g/L stock were added.
- Major: stock-only trace-mineral ingredients such as nitrilotriacetic acid, `MnSO4 x n H2O`, `FeSO4 x 7 H2O`, and the minor salts are recorded at 1 L stock concentration even though the final recipe adds only 10 ml of the stock.
- Major: stock-vitamin entries such as biotin, folic acid, thiamine HCl, riboflavin, nicotinic acid, calcium pantothenate, vitamin B12, p-aminobenzoic acid, and lipoic acid are likewise recorded as undiluted trace-vitamin stock concentrations.
- Major: the nitrilotriacetic-acid dissolution and pH 6.5 to 7.0 adjustment belong to the trace-minerals stock but appear as top-level `preparation_steps[1]`.
- Major: `kosmotoga_pacifica_medium` / JCM 982 was merged as a source duplicate of JCM 232 even though its source adds 3.0 g/L yeast extract, 2.4 g/L L-cystine, and a distinct N2/CO2 4:1 cultivation atmosphere.
- Minor: the generated corpus also contains the TOGO M225 import of JCM 232 as a separate generated record; direct JCM and TOGO copies need a canonicalization policy after their formula-level errors are fixed.

## Recommended Edits

- In `data/normalized_yaml/archaea/methanocaldococcus_jannaschii_medium.yaml`, restore `Trace minerals` and `Trace vitamins` as structured child solutions dosed at 10 ml per 1000 ml final medium.
- Move nitrilotriacetic acid, the trace metals, and the trace vitamins under their respective child solutions at the MediaDive stock concentrations instead of leaving them in top-level `ingredients`.
- Keep main-solution NaCl, `MgSO4 x 7 H2O`, and `CaCl2 x 2 H2O` at the JCM 232 main values and remove the `Merged 2 duplicates` sums caused by stock flattening.
- Scope the nitrilotriacetic-acid KOH preparation step to the trace-minerals stock.
- Split JCM 982 back out of this source duplicate merge and represent Kosmotoga pacifica as a medium-232 variant supplemented with 3.0 g/L yeast extract, 2.4 g/L L-cystine, and the N2/CO2 4:1 cultivation atmosphere.
- After curating JCM 232, reconcile it with the separate TOGO M225 generated record so the same JCM source is not published twice.

## Follow-up Checks

- Rerun open-schema, strict, reference, and term validation after nesting both trace stocks.
- Rebuild merged YAML and verify the JCM 232 record has no `Merged 2 duplicates` notes for NaCl, `MgSO4 x 7 H2O`, or `CaCl2 x 2 H2O`.
- Confirm generated Kosmotoga pacifica output contains yeast extract and L-cystine as explicit supplements instead of appearing as a synonym on the JCM 232 record.
- Compare the regenerated JCM 232 direct record with regenerated TOGO M225 and verify only one active canonical record remains for that source formula.

## Additional Notes

None found.
