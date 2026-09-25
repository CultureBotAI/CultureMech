# YAML Record Review: rhodovulum_iodosum_and_r_robiginosum_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/rhodovulum_iodosum_and_r_robiginosum_medium.yaml`
- Started UTC: 2026-09-25T02:27:41Z
- Finished UTC: 2026-09-25T02:27:51Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:006847` for KOMODO Medium 929 / `komodo.medium:929`, merged with direct DSMZ Medium 929 / `mediadive.medium:929`.

## Validation

- Open schema validation: passed; exited 0 with no diagnostics.
- Strict validation: passed; `scripts/validate_strict.py` reported 0 errors and wrote only the TSV header.
- Reference validation: passed; 0 checks.
- Term validation: passed with the known `eutils` / `pkg_resources` deprecation warning.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

KOMODO Medium 929 explicitly cites DSMZ Medium 929, and the direct `mediadive.medium:929` owner is the matching DSMZ source record. An exact ignored-inclusive search for `komodo.medium:929`, `mediadive.medium:929`, and `DSMZ_Medium929.pdf` found only the expected KOMODO and DSMZ owners, their generated target, and their indexes under the relevant data trees.

## Evidence

The DSMZ 929 PDF lists artificial sea-water salts plus 1000 ml distilled water, then says to prepare the medium anaerobically under N2:CO2 and add 30 ml/L NaHCO3 stock, KH2PO4, NH4Cl, 0.5 mM Na2S2O3, 1 ml/L Trace elements, 1 ml/L Selenite/tungstate solution, 1 ml/L Vitamin solution, 1 ml/L Vitamin B12 solution, and 1 ml/L Vitamin B1 solution. It adjusts pH to 6.8, defines the three stock recipes plus two separate vitamin stocks, and adds 5 mM acetate plus 10 mM FeSO4 from a 1 M stock under nitrogen.

The generated target flattens trace elements, selenite/tungstate solution, the vitamin stocks, sodium acetate, and FeSO4 into final gram-per-liter rows. Its `FeSO4 x 7 H2O` row is explicitly summed from 2.78015 and 2.1 g/L even though those are different claims: 10 mM final FeSO4 and the FeSO4 concentration inside the 1 ml/L Trace elements stock.

## Completeness

The target is missing the DSMZ final distilled-water row, the NaHCO3 stock row, all five named stock additions, all stock waters, and the cultivation note about long light incubation. The KOMODO owner is a valid source duplicate of DSMZ 929, but both maintained owners are still flattened.

Empty optional organism fields are not defects.

## Findings

- Major: `data/normalized_yaml/bacterial/rhodovulum_iodosum_and_r_robiginosum_medium.yaml` and `data/normalized_yaml/bacterial/KOMODO_929_RHODOVULUM_IODOSUM_AND_R._ROBIGINOSUM_MEDIUM.yaml` collapse distinct stock and final-medium rows into one flat ingredient list.
- Major: `FeSO4 x 7 H2O` is summed to `4.88015 G_PER_L` from final 10 mM FeSO4 and FeSO4 inside the Trace elements stock. DSMZ 929 does not contain a 4.88015 g/L final FeSO4 ingredient.
- Major: the Trace elements, Selenite/tungstate solution, Vitamin solution, Vitamin B12 solution, and Vitamin B1 solution source rows are absent as 1 ml/L final additions; their components are emitted at stock concentrations as if they were final-medium ingredients.
- Major: the 30 ml/L NaHCO3 stock is represented only as final 2.52 g/L NaHCO3, so the stock addition itself is lost.
- Major: 1000 ml final distilled water and each nested stock water row are absent.
- Minor: several stock-vitamin labels remain weak or ungrounded in the flat owner, including `Pyridoxin`, `Thiamin`, and `Cyanocobalamine`.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/rhodovulum_iodosum_and_r_robiginosum_medium.yaml` so DSMZ 929 has final artificial sea-water salts, final distilled water, KH2PO4, NH4Cl, 0.5 mM Na2S2O3, 5 mM acetate, 10 mM FeSO4, and six stock additions: NaHCO3, Trace elements, Selenite/tungstate solution, Vitamin solution, Vitamin B12 solution, and Vitamin B1 solution.
- Move Trace elements, Selenite/tungstate, Vitamin solution, Vitamin B12 solution, and Vitamin B1 ingredients under nested stock compositions with their stock water rows.
- Mirror the same repaired structure in `data/normalized_yaml/bacterial/KOMODO_929_RHODOVULUM_IODOSUM_AND_R._ROBIGINOSUM_MEDIUM.yaml` or regenerate that owner from the repaired DSMZ parent, then regenerate `data/merge_yaml/merged`.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation for regenerated DSMZ/KOMODO 929.
- Confirm no regenerated `FeSO4 x 7 H2O` row contains a summed `4.88015 G_PER_L` value.
- Confirm stock components appear only in nested stock recipes and not as top-level final ingredients.
- Confirm KOMODO 929 remains a source duplicate of DSMZ 929 after repair.

## Additional Notes

No additional issues.
