# YAML Record Review: pelobacter_propionicus_medium_freshwater

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/pelobacter_propionicus_medium_freshwater.yaml`
- Started UTC: 2026-09-24T20:14:29Z
- Finished UTC: 2026-09-24T20:14:29Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/pelobacter_propionicus_medium_freshwater.yaml`, a generated `MediaRecipe` merge record.

- ID: `CultureMech:001394`
- Label: `pelobacter_propionicus_medium_freshwater`
- Category: `bacterial`
- Source term: `mediadive.medium:298`
- Source name: DSMZ Medium 298, PELOBACTER PROPIONICUS MEDIUM (FRESHWATER)
- Physical state: `LIQUID`
- Maintained owner: `data/normalized_yaml/bacterial/pelobacter_propionicus_medium_freshwater.yaml`
- Generated from: `pelobacter_propionicus_medium_freshwater`

## Validation

- Passed: open LinkML validation of `data/merge_yaml/merged/pelobacter_propionicus_medium_freshwater.yaml` against `src/culturemech/schema/culturemech.yaml` as `MediaRecipe`; no issues found.
- Passed: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/pelobacter_propionicus_medium_freshwater.yaml --out /private/tmp/pelobacter_propionicus_medium_freshwater.strict.tsv --workers 1 --quiet`; the TSV contained only its header, so strict validation found 0 errors.
- Passed: focused `linkml-reference-validator validate data data/merge_yaml/merged/pelobacter_propionicus_medium_freshwater.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`; 0 references were checked.
- Passed: focused `linkml-term-validator validate-data data/merge_yaml/merged/pelobacter_propionicus_medium_freshwater.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`.
- Not checked: embedded `curation_history`; the documented `just validate-history` target validates standalone `history/` YAML rather than `MediaRecipe.curation_history` embedded in generated records.

## Identity and Grounding

`mediadive.medium:298` resolves to DSMZ Medium 298, PELOBACTER PROPIONICUS MEDIUM (FRESHWATER), with source `DSMZ`, pH range 7.2 to 7.5, a 1001 ml final volume, and a 1 ml Trace element solution SL-10 addition. The DSMZ Medium 298 PDF confirms the same base recipe and its DSM-specific modification notes.

The record's DSMZ identity, bacterial category, liquid physical state, pH range, and final-medium salt/substrate rows are supported. The HCl and trace-metal rows are grounded to the right compounds but are scoped incorrectly: they belong to the 1000 ml SL-10 stock, not directly to the final medium.

## Evidence

- DSMZ 298 and MediaDive 298 list the final medium as KH2PO4, NH4Cl, NaCl, MgCl2 x 6 H2O, KCl, CaCl2 x 2 H2O, 1 ml Trace element solution SL-10, 0.5 ml Sodium resazurin stock, Na2CO3, 2,3-butanediol, Na2S x 9 H2O, and 1000 ml Distilled water.
- Trace element solution SL-10 is a separate 1000 ml stock made from 10 ml 25 percent HCl, FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, and 990 ml Distilled water.
- The generated record has no `solutions` block. It emits every SL-10 component as a direct final-medium `ingredient`, drops the 1 ml/L Trace element solution row, drops the final 1000 ml water row, and drops the SL-10 990 ml water row.

## Completeness

The generated record is materially incomplete because it cannot represent the 1 ml/L stock dilution that makes the SL-10 metals trace components of the final medium. It also scopes the SL-10-specific preparation instruction, "First dissolve FeCl2 in the HCl," as a top-level final-medium `DISSOLVE` step.

The maintained normalized owner gained a `for_dsm_3246` strain-specific child link on 2026-09-06. The generated merge record is older and does not carry that `variant_children` edge.

Empty optional fields are not defects.

An ignored-inclusive exact search of `data`, `src`, and `scripts` for `mediadive.medium:298`, `CultureMech:001394`, `DSMZ_Medium298`, and `pelobacter_propionicus_medium_freshwater` found the maintained owner, this generated record, related DSMZ 298 variant records, KOMODO records that reference DSMZ 298 variants in notes, and repair scripts for KOMODO 298-derived children.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Trace element solution SL-10 is flattened into direct final-medium ingredients. | DSMZ 298 adds 1 ml Trace element solution SL-10 to the final medium, and the SL-10 internals are prepared as a 1000 ml stock. The generated record emits HCl and every SL-10 trace metal directly under top-level `ingredients` at stock concentration. | `data/normalized_yaml/bacterial/pelobacter_propionicus_medium_freshwater.yaml` |
| Major | Final and stock water rows are missing, and the stock-specific preparation step is attached to the final medium. | DSMZ 298 includes 1000 ml Distilled water in the final medium and 990 ml Distilled water in SL-10. The generated record has no water ingredient, no SL-10 solution, and a top-level `DISSOLVE` step that only describes preparing SL-10. | `data/normalized_yaml/bacterial/pelobacter_propionicus_medium_freshwater.yaml` |
| Minor | The generated record is stale relative to the September strain-specific variant link repair. | The generated record has no `variant_children`; the maintained owner links `data/normalized_yaml/bacterial/for_dsm_3246.yaml` as a `STRAIN_SPECIFIC_VARIANT` replacing 2,3-butanediol with 1 g/L acetoin. | `data/normalized_yaml/bacterial/pelobacter_propionicus_medium_freshwater.yaml`, already repaired with the child edge. |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/pelobacter_propionicus_medium_freshwater.yaml`, keep the final DSMZ 298 base rows as direct ingredients and add the missing final 1000 ml Distilled water row.
2. Add a 1 ml/L `Trace element solution SL-10` entry under `solutions`, move HCl, FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, and 990 ml Distilled water into that solution, and keep the FeCl2/HCl preparation step scoped to it.
3. Regenerate `data/merge_yaml/merged/pelobacter_propionicus_medium_freshwater.yaml` after the normalized owner is repaired so the generated record also picks up the existing `for_dsm_3246` variant child edge.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation on `data/normalized_yaml/bacterial/pelobacter_propionicus_medium_freshwater.yaml`, then regenerate `data/merge_yaml/merged/pelobacter_propionicus_medium_freshwater.yaml` and rerun the same focused validators on the generated record.
- Manually compare the regenerated record against the DSMZ 298 PDF and the MediaDive 298 REST record, with special attention to the SL-10 stock dilution and its HCl amount.
- Confirm the regenerated merge output retains `variant_children` for `data/normalized_yaml/bacterial/for_dsm_3246.yaml`.

## Additional Notes

`data/import_tracking/reports/concentration_plausibility.tsv` already flags `FeCl2 x 4 H2O` at 1.5 g/L as a likely trace-salt stock concentration in this maintained owner.
