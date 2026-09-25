# YAML Record Review: LIND BHT MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/lind_bht_medium__1c3a1bc4.yaml
- Started UTC: 2026-09-23T19:48:07Z
- Finished UTC: 2026-09-23T19:50:39Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:003188 |
| Name | lind_bht_medium |
| Original name | LIND BHT MEDIUM |
| Category | bacterial |
| Medium/composition type | COMPLEX / UNDEFINED |
| Physical state | LIQUID |
| Structured pH | None |
| Media grounding | mediadive.medium:J843 |
| Source provenance | JCM Medium 843 via MediaDive |
| Generated file | data/merge_yaml/merged/lind_bht_medium__1c3a1bc4.yaml |
| Maintained owner | data/normalized_yaml/bacterial/lind_bht_medium.yaml |
| Merge fingerprint | 1c3a1bc4ab0ce7066fd110a5a42106f8d948964f3757106074c473086e6f89c2 |

The reviewed target is the generated MediaDive import of JCM GRMD 843. Future fixes belong in `data/normalized_yaml/bacterial/lind_bht_medium.yaml` or the MediaDive importer, followed by regeneration of `data/merge_yaml/merged/` and downstream products.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/lind_bht_medium__1c3a1bc4.yaml`. |
| Strict validator | Passed with zero error rows in `/private/tmp/lind_bht_medium__1c3a1bc4.strict.tsv`. |
| LinkML reference validator | Passed; the reference validator completed with zero checks because this generated record has no `references` collection. |
| LinkML term validator | Passed. |
| Embedded curation history | Not checked: the repository history validator validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

The MediaDive REST record and the live JCM GRMD 843 page both identify the source as `LIND BHT MEDIUM` from JCM. They agree that the main recipe adds 1 ml of the JCM 439 trace-element solution, uses anaerobic post-autoclave stocks, is dispensed under H2-CO2, and is pressurized after inoculation to 200 kPa H2-CO2.

The generated record keeps the JCM 843/MediaDive identity and the non-water compound names, but it no longer clearly denotes the JCM formulation because 1 ml, 8 ml, 20 ml, 25 ml, and 30 ml stock additions are represented as gram-per-liter solute rows.

An ignored-inclusive exact search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:003188`, `mediadive.medium:J843`, `GRMD=843`, the maintained filename, the merge fingerprint, and the shared slug found this MediaDive/JCM owner, a separate Togo M879 Lind BHT owner that also points at JCM 843, both generated siblings, and source indexes.

## Evidence

Supported in the inspected JCM and MediaDive sources:

- JCM 843 supplies 0.3 g KH2PO4, 0.3 g K2HPO4, 1 g NH4Cl, 20 g NaCl, 0.1 g KCl, 0.1 g CaCl2 x 2 H2O, 1 ml trace element solution from JCM 439, 2 g yeast extract, 4.96 g Na2S2O3 x 5 H2O, 0.5 g L-cysteine-HCl-H2O, 1 mg resazurin, and 925 ml distilled water.
- After autoclaving under N2-CO2, the medium receives 25 ml 8 percent NaHCO3 stock, 30 ml 10 percent MgCl2 x 6 H2O stock, and 20 ml 1.0 M sodium acetate stock.
- Prior to inoculation, it receives 8 ml 5 percent Na2S x 9 H2O stock; inoculated vessels are pressurized to 200 kPa H2-CO2.
- JCM 439 defines the trace-element stock used by JCM 843 as a 987 ml water stock containing 12.5 ml 25 percent HCl plus FeSO4 x 7 H2O, H3BO3, MnCl2 x 4 H2O, CoCl2 x 6 H2O, NiCl2 x 6 H2O, CuCl2 x 2 H2O, ZnSO4 x 7 H2O, and Na2MoO4 x 2 H2O.

Unsupported or incomplete in the generated record:

- The 1 ml trace-element solution addition from JCM 439 is absent. Its internal stock ingredients are flattened into top-level medium rows at stock strength.
- The HCl trace-stock ingredient is represented as 12.5 g/L even though JCM 439 and MediaDive specify 12.5 ml of 25 percent HCl in the stock solution.
- The 25 ml NaHCO3, 30 ml MgCl2 x 6 H2O, 20 ml sodium acetate, and 8 ml Na2S x 9 H2O stock additions are represented as 25, 30, 20, and 8 g/L solute rows.
- NiCl2 x 6 H2O is grounded to CHEBI:34887 / nickel dichloride, which loses the source hydrate form.
- The generated record has no structured reference to MediaDive J843, JCM GRMD 843, or the linked JCM GRMD 439 stock.

## Completeness

The record is complete for the JCM 843 label, category, high-level complex liquid classification, all visible non-water source compound names, the H2-CO2/N2-CO2 gas ratios, and the 200 kPa final pressurization step.

It is incomplete for the JCM 439 trace-element stock boundary, the four other liquid stock boundaries, the trace-stock water amount, exact hydrate grounding for NiCl2 x 6 H2O, cross-import linkage to the Togo M879 sibling, and structured references. Empty optional pH, target-organism, incubation, and storage fields are acceptable for this review because the inspected MediaDive/JCM J843 sources do not state those values.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | JCM 439 `Trace element solution` is flattened and its 1 ml/L use is missing. | JCM 843 adds 1 ml of trace element stock from JCM 439; the generated record lists only the stock's internal 1 L recipe rows as top-level medium ingredients. | `data/normalized_yaml/bacterial/lind_bht_medium.yaml` or the MediaDive importer |
| Major | Four milliliter stock additions were converted to gram-per-liter solute rows. | JCM 843 gives 25 ml of 8 percent NaHCO3 stock, 30 ml of 10 percent MgCl2 x 6 H2O stock, 20 ml of 1.0 M sodium acetate stock, and 8 ml of 5 percent Na2S x 9 H2O stock; the YAML stores them as 25, 30, 20, and 8 `G_PER_L`. | `data/normalized_yaml/bacterial/lind_bht_medium.yaml` or the MediaDive importer |
| Major | The HCl trace-stock row has the wrong unit and solution context. | JCM 439 defines the stock with 12.5 ml 25 percent HCl in 987 ml water; the YAML records `HCl` as 12.5 g/L at the main-medium level. | `data/normalized_yaml/bacterial/lind_bht_medium.yaml` or the MediaDive importer |
| Major | NiCl2 x 6 H2O is over-broadly grounded. | The JCM 439 trace-element stock names nickel chloride hexahydrate, while the YAML maps that row to CHEBI:34887 / nickel dichloride. | `data/normalized_yaml/bacterial/lind_bht_medium.yaml` |
| Minor | JCM's page-level autoclave temperature and time are missing. | The JCM page states that media are sterilized by autoclaving at 121 C for 15 min unless otherwise stated; the YAML records autoclaving under N2-CO2 but omits the default temperature and duration. | `data/normalized_yaml/bacterial/lind_bht_medium.yaml` or the MediaDive importer |
| Minor | A Togo M879 sibling also resolves to JCM 843 but remains a separate generated record. | The ignored-inclusive search found `data/normalized_yaml/bacterial/TOGO_M879_Lind_BHT_Medium.yaml`, and its notes name the same JCM GRMD 843 URL as the original source. | `data/normalized_yaml/bacterial/lind_bht_medium.yaml`, `data/normalized_yaml/bacterial/TOGO_M879_Lind_BHT_Medium.yaml`, or merge reconciliation logic |
| Minor | Structured references are missing. | The generated target carries only a free-text JCM URL in `notes`, and the reference validator performed zero checks. | `data/normalized_yaml/bacterial/lind_bht_medium.yaml` |

## Recommended Edits

1. Recreate `Trace element solution` as a nested 1 ml/L stock with the JCM 439 12.5 ml HCl row, eight hydrated salt rows, and 987 ml water context.
2. Restore 8 percent NaHCO3, 10 percent MgCl2 x 6 H2O, 1.0 M sodium acetate, and 5 percent Na2S x 9 H2O as 25, 30, 20, and 8 ml stock additions.
3. Correct the HCl row to 12.5 ml in the trace-element stock instead of 12.5 g/L in the main recipe.
4. Replace the NiCl2 x 6 H2O CHEBI grounding with a hydrate-specific term if one is available in the ingredient index; otherwise leave the exact preferred term unresolved.
5. Add the JCM default autoclave condition, 121 C for 15 min, to the preparation detail.
6. Add structured references for MediaDive J843, JCM GRMD 843, and JCM GRMD 439.
7. Reconcile or explicitly link the MediaDive J843 and Togo M879 Lind BHT records so two imports of the same JCM 843 source are not isolated.
8. Regenerate `data/merge_yaml/merged/` and downstream pages.

## Follow-up Checks

- Rerun open schema validation, the strict validator, the reference validator, and the term validator on the regenerated YAML.
- Manually compare the regenerated record against MediaDive J843, JCM 843, and JCM 439 for the 1 ml trace-element stock and the four post-autoclave/prior-to-use stock additions.
- Re-run an ignored-inclusive exact search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` for `CultureMech:003188`, `mediadive.medium:J843`, `GRMD=843`, `TOGO:M879`, and `lind_bht_medium` to confirm the MediaDive and Togo siblings are linked or intentionally distinguished.

## Additional Notes

The related Togo M879 normalized owner has its own unit problems, including 925 ml water imported as 925 g/L and 1 mg resazurin imported as 1 g/L. Fixing the MediaDive owner alone will not repair that Togo sibling.
