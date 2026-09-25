# YAML Record Review: proteiniphilus_5mh_medium__7f222a31

- Repository: CultureMech
- Record: data/merge_yaml/merged/proteiniphilus_5mh_medium__7f222a31.yaml
- Started UTC: 2026-09-24T21:56:18Z
- Finished UTC: 2026-09-24T21:56:18Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:003218`, the generated bacterial liquid `PROTEINIPHILUS 5MH MEDIUM` record merged from one direct MediaDive/JCM normalized input, `data/normalized_yaml/bacterial/proteiniphilus_5mh_medium.yaml`.

## Validation

- LinkML validation: Passed; `linkml-validate` reported no issues.
- Strict validation: Passed; `scripts/validate_strict.py` scanned one file and reported zero `ERROR` rows.
- Reference validation: Passed; `linkml-reference-validator` validated one file and reported zero reference checks.
- Term validation: Passed; `linkml-term-validator` exited 0.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` files, not `MediaRecipe.curation_history` blocks in generated YAML.

## Identity and Grounding

The identity is clear: MediaDive `J871` preserves the former JCM `PROTEINIPHILUS 5MH MEDIUM` source, and TOGO `M910` imports the same retired JCM Medium 871 as `Proteiniphilus 5MH Medium`. The current JCM `GRMD=871` page returns no recipe. An exact ignored YAML search for `mediadive.medium:J871`, `JCM, ID: J871`, `GRMD=871`, and `proteiniphilus_5mh_medium` found this direct MediaDive branch, the direct normalized source, and a separate TOGO `M910` branch for the same retired JCM recipe.

## Evidence

MediaDive `J871` reports a 1012 ml recipe with 0.5 g NaCl, 0.5 g MgCl2 x 6 H2O, 0.1 g CaCl2 x 2 H2O, 0.3 g NH4Cl, 0.2 g KH2PO4, 0.5 g KCl, 2 g yeast extract, 1 ml Trace element solution, 1 ml Se/W solution, 2.5 g NaHCO3, 1 mg resazurin, 1000 ml distilled water, 5 ml 5% Na2S x 9 H2O, and 5 ml 5% L-Cysteine HCl x H2O. It also carries internal recipes for both 1 L stock solutions.

TOGO `M910` records the same retired JCM page as a 1 L main recipe with the same 1 ml Trace element solution, 1 ml Se/W solution, and two 5 ml 5% post-autoclave reducing-solution additions.

## Completeness

The generated direct record preserves most main dry masses after MediaDive volume scaling, but it is missing the 1000 ml water row and all four liquid solution additions. The trace-element and Se/W stock internals are flattened into final top-level ingredients, and the two reducing solution aliquots are treated as `5 G_PER_L` dry solutes.

## Findings

- The 1000 ml distilled water main-medium row from MediaDive and TOGO is absent.
- `Trace element solution` and `Se/W solution` are absent as 1 ml/L stock additions; their internal salts are modeled as final-medium ingredients.
- `CaCl2 x 2 H2O` combines the 0.1 g main calcium salt with the 0.1 g/L calcium row from the trace stock, producing the merged artifact `0.1988142 G_PER_L`.
- The 5 ml 5% Na2S x 9 H2O solution and 5 ml 5% L-Cysteine HCl x H2O solution are imported as `5 G_PER_L` solids instead of milliliter stock aliquots.
- The direct JCM/MediaDive record is split from `PROTEINIPHILUS_5MH_MEDIUM.yaml`, the TOGO `M910` branch for the same JCM 871 source.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/proteiniphilus_5mh_medium.yaml` by restoring the 1000 ml water row and representing the trace-element, Se/W, Na2S, and cysteine solution additions with milliliter units.
- Move NTA, FeCl3 x 6 H2O, MnCl2 x 4 H2O, CoCl2 x 6 H2O, CaCl2 x 2 H2O, ZnCl2, CuCl2 x 2 H2O, H3BO3, Na2MoO4 x 2 H2O, and NiCl2 x 6 H2O into a `Trace element solution` composition instead of final top-level ingredients.
- Move Na2SeO3 x 5 H2O and Na2WO4 x 2 H2O into a `Se/W solution` composition instead of final top-level ingredients.
- Repair or retire the TOGO `M910` branch so the retired JCM 871 source regenerates as one merged output.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation on the regenerated merged record.
- Repeat exact ignored YAML searches for `mediadive.medium:J871`, `TOGO:M910`, `GRMD=871`, and `proteiniphilus_5mh_medium` to verify that the direct MediaDive and TOGO branches were reconciled.

## Additional Notes

None.
