# YAML Record Review: Mollicutes H-RF3 Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mollicutes_h_rf3_medium.yaml
- Started UTC: 2026-09-24T13:53:49Z
- Finished UTC: 2026-09-24T13:54:53Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:007771 |
| Name | mollicutes_h_rf3_medium |
| Original name | Mollicutes H-RF3 Medium |
| Source owner | data/normalized_yaml/bacterial/TOGO_M1241_Mollicutes_H-RF3_Medium.yaml |
| Generated record | Yes; produced under data/merge_yaml/merged with merge_fingerprint aa2e79a5bbb8f52aeac762d514ee57d3cd20c3bbdb68f3bab9769715aa8068ee |

## Validation

| Check | Result |
| --- | --- |
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mollicutes_h_rf3_medium.yaml` | Passed; `No issues found`. |
| `python scripts/validate_strict.py data/merge_yaml/merged/mollicutes_h_rf3_medium.yaml --out /private/tmp/mollicutes_h_rf3_medium.strict.tsv --workers 1 --quiet` | Passed; the TSV contained only the header, so there were 0 strict errors. |
| `linkml-reference-validator validate data data/merge_yaml/merged/mollicutes_h_rf3_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 references were checked. |
| `linkml-term-validator validate-data data/merge_yaml/merged/mollicutes_h_rf3_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the expected `eutils` / `pkg_resources` warning. |
| Embedded `curation_history` | Not checked: the documented history validator targets the standalone `history/` corpus, not inline `MediaRecipe.curation_history`. |

## Identity and Grounding

The target is the generated TOGO import for TOGO:M1241. The TOGO API still resolves M1241 to `Mollicutes H-RF3 Medium`, `original_media_id` JCM_M1159, JCM GRMD 1159, and pH 7.0, matching the record's `media_term`, label, and original source identity.

The live JCM URL now returns `Nothing found.`, so TOGO is the inspected source for the formula. That formula supports 1 g yeast extract, 0.15 g CaCl2 x 2 H2O, 0.14 g KH2PO4, 0.54 g NH4Cl, 0.5 mg resazurin, 0.2 g MgCl2 x 6 H2O, 1 g Casamino acids, CO2, and N2 per liter, plus separate post-autoclave stock additions.

The ingredient groundings for water, KH2PO4, NH4Cl, resazurin, carbon dioxide, and nitrogen are appropriate at the reviewed granularity. The CaCl2 x 2 H2O and MgCl2 x 6 H2O ingredients have direct CHEBI `term` entries but are missing mirrored `mediaingredientmech_chebi_term` entries.

An ignored-inclusive search over `data/normalized_yaml` and `data/merge_yaml` for `TOGO:M1241`, bounded `M1241`, `JCM_M1159`, and `GRMD=1159` found the current TOGO owner, index references, two unrelated provider accessions containing `M1241`, and a second Mollicutes H-RF3 record at `data/merge_yaml/merged/mollicutes_h_rf3_medium__37b10622.yaml` from `data/normalized_yaml/bacterial/mollicutes_h_rf3_medium.yaml`. That sibling uses the same JCM GRMD 1159 URL with ID CultureMech:002331, so it appears to be the same source recipe imported through a separate JCM path rather than a distinct medium.

## Evidence

TOGO:M1241 supports the main ingredient list and the five stock additions, but the generated record changed the evidence in several consequential ways:

| Source claim | Generated representation | Assessment |
| --- | --- | --- |
| 1 ml Trace minerals from Medium M142 | `Trace minerals (see Medium [M142])`, concentration `1 G_PER_L`, empty composition | The dose is a volume addition, not 1 g/L, and the M142 stock reference is not structured. |
| 30 ml 8% NaHCO3 solution | `30 G_PER_L`, empty composition | The dose is a 30 ml stock addition per liter. |
| 6 ml 5% Na2S x 9 H2O solution | `6 G_PER_L`, empty composition | The dose is a 6 ml stock addition per liter. |
| 6 ml 5% L-Cysteine-HCl-H2O solution | `6 G_PER_L`, empty composition | The dose is a 6 ml stock addition per liter. |
| 10 ml Trace vitamins from Medium M190 | `10 G_PER_L`, empty composition | The dose is a volume addition, and the M190 vitamin stock reference is not structured. |
| 0.5 mg resazurin | `0.5 G_PER_L` | The concentration is 1000x too high if interpreted as grams per liter. |

The TOGO comments also support a preparation sequence that the generated record does not preserve: adjust the starting pH to 7.5, boil and cool under an N2-CO2 4:1 gas stream, dispense under the same gas into sealed butyl-stoppered culture vessels, autoclave, add the listed sterile stock solutions aseptically and anaerobically after cooling, and readjust to pH 7.0 if necessary.

## Completeness

No empty optional scalar fields are present, and the absent target organism list is not a schema or source-identity defect for this provider recipe.

The record is materially incomplete for anaerobic use because it has no pH 7.0 value, no starting pH 7.5 adjustment, no gas ratio or gas-stream instruction, no butyl-stopper vessel handling, no instruction to autoclave the basal recipe before the stock additions, and no instruction that the final stock additions are aseptic and anaerobic.

The cross-references to TOGO M142 and M190 are unresolved in structured form. Inspecting those TOGO records showed that M142 is a whole Pyrococcus Medium record that contains a local `Trace minerals` subcomponent, and M190 is a whole JCM_M197 record that contains local `Trace vitamins` and `Trace mineral solution` subcomponents. The Mollicutes record should retain resolvable stock references or copy the relevant subcomponent compositions, not flatten an entire referenced medium.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | All five stock-solution additions have the wrong concentration units and unresolved `Unknown solution` placeholders. | TOGO M1241 lists 1 ml M142 trace minerals, 30 ml 8% NaHCO3, 6 ml 5% Na2S x 9 H2O, 6 ml 5% L-Cysteine-HCl-H2O, and 10 ml M190 trace vitamins; the generated rows store 1/30/6/6/10 as `G_PER_L` with empty `composition`. | `data/normalized_yaml/bacterial/TOGO_M1241_Mollicutes_H-RF3_Medium.yaml`; if the error is systemic, the TOGO solution import and `solution-migrator-v1.0` path also need repair. |
| Major | The resazurin dose was promoted from milligrams to grams. | The source has 0.5 mg resazurin per liter, while the generated record has `0.5 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M1241_Mollicutes_H-RF3_Medium.yaml` and the TOGO unit importer. |
| Major | The anaerobic pH and preparation semantics are missing. | The TOGO record carries pH 7.0 and comments for pH 7.5, N2-CO2 4:1 boiling/cooling, sealed anaerobic dispensing, autoclaving, post-cooling stock additions, and final pH readjustment; the YAML only carries variable CO2/N2 ingredient rows. | `data/normalized_yaml/bacterial/TOGO_M1241_Mollicutes_H-RF3_Medium.yaml`; rerun merge generation after curation. |
| Major | The same JCM GRMD 1159 recipe is split into another generated Mollicutes H-RF3 record. | An ignored-inclusive search found `data/merge_yaml/merged/mollicutes_h_rf3_medium__37b10622.yaml` and `data/normalized_yaml/bacterial/mollicutes_h_rf3_medium.yaml`, both pointing at `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1159` with a second CultureMech ID. | The old JCM normalized record plus source de-duplication in the merge pipeline. |
| Minor | The source note relies on a stale JCM URL. | Live GRMD 1159 returned `Nothing found.` even though the same JCM identity remains available through TOGO M1241. | `data/normalized_yaml/bacterial/TOGO_M1241_Mollicutes_H-RF3_Medium.yaml` source metadata. |
| Minor | Two hydrate salts have direct CHEBI terms but no MediaIngredientMech CHEBI mirrors. | CaCl2 x 2 H2O has CHEBI:86158 and MgCl2 x 6 H2O has CHEBI:86345, but neither has `mediaingredientmech_chebi_term`. | MediaIngredientMech enrichment over the normalized TOGO owner. |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/TOGO_M1241_Mollicutes_H-RF3_Medium.yaml`, change the five stock additions from gram-per-liter concentrations to the source ml-per-liter additions and give each row a specific stock name.
2. Preserve the M142 and M190 cross-referenced stock evidence as resolvable internal medium references or copy only the relevant `Trace minerals` and `Trace vitamins` subcomponents from those TOGO records.
3. Correct resazurin to `0.0005 G_PER_L` or an equivalent 0.5 mg/L representation that does not change the source magnitude.
4. Add `ph_value: 7.0` and encode the pH 7.5 starting adjustment, N2-CO2 4:1 gas stream, butyl-stopper anaerobic dispensing, autoclave step, sterile post-cooling additions, and final pH check in the available preparation fields.
5. Reconcile `data/normalized_yaml/bacterial/mollicutes_h_rf3_medium.yaml` with the TOGO M1241 owner so JCM GRMD 1159 no longer produces two generated MediaRecipe records with different CultureMech IDs.
6. Refresh MediaIngredientMech CHEBI enrichment for CaCl2 x 2 H2O and MgCl2 x 6 H2O after the maintained source is updated.
7. Update the JCM note only if the curation model has a way to distinguish historical provider URLs from live provider URLs; do not discard the GRMD 1159 provenance.

## Follow-up Checks

- Rerun `linkml-validate`, `scripts/validate_strict.py`, `linkml-reference-validator`, and `linkml-term-validator` on the regenerated `data/merge_yaml/merged/mollicutes_h_rf3_medium.yaml`.
- Reinspect TOGO M1241 and verify that the regenerated record preserves 0.5 mg resazurin, all five ml-scale stock additions, pH 7.0, and the N2-CO2 4:1 preparation text.
- Run an ignored-inclusive search for `GRMD=1159`, `JCM_M1159`, and `TOGO:M1241` across `data/normalized_yaml` and `data/merge_yaml` to confirm the direct JCM and TOGO M1241 imports were de-duplicated.
- Verify that M142 and M190 stock references either resolve to structured stock recipes or inline only the named stock compositions, not the whole referenced media.

## Additional Notes

The formula evidence is still recoverable from TOGO M1241 even though the historical JCM page no longer serves GRMD 1159.

TOGO M142 and M190 are whole media records that happen to contain the referenced local stocks. A future repair should use those local stock definitions narrowly.
