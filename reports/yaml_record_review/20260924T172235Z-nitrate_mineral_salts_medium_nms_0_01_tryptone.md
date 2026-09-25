# YAML Record Review: Nitrate mineral salts medium (NMS) + 0.01% Tryptone
- Repository: CultureMech
- Record: data/merge_yaml/merged/nitrate_mineral_salts_medium_nms_0_01_tryptone.yaml
- Started UTC: 2026-09-24T17:22:35Z
- Finished UTC: 2026-09-24T17:23:10Z
- Verdict: needs curation

## Target
Reviewed `CultureMech:008446`, `nitrate_mineral_salts_medium_nms_0_01_tryptone`, generated from `data/normalized_yaml/bacterial/nitrate_mineral_salts_medium_nms_0_01_tryptone.yaml`.

The record represents TOGO `M1871` / NBRC `NBRC_M1116`, "Nitrate mineral salts medium (NMS) + 0.01% Tryptone".

## Validation
- Open LinkML validation passed; `linkml-validate` exited 0 with no diagnostics.
- Strict validation passed; the strict TSV had only the header row.
- Reference validation passed.
- Term validation passed.
- Embedded `curation_history` was not checked: the available `just validate-history` target validates standalone files under `history/`, not inline `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding
The record is grounded to the correct upstream medium. TOGO `M1871` reports the original media ID as `NBRC_M1116`, links to NBRC `NO=1116`, and has the same original label as the generated YAML.

An exact hidden/no-ignore search of `data/normalized_yaml` and `data/merge_yaml` for `TOGO:M1871`, `NBRC_M1116`, `NO=1116`, the original title, and the normalized slug found only one normalized owner and this generated merged YAML for this exact upstream medium. The active generated artifact is therefore a singleton, not an unintended merge of separate source records.

## Evidence
The NBRC and TOGO records agree on the main medium: 1 g MgSO4.7H2O, 0.2 g CaCl2.6H2O, 2 ml Chelated Iron Solution, 1 g KNO3, 0.5 ml Trace Element Solution, 0.272 g KH2PO4, 0.717 g Na2HPO4.12H2O, 0.1 g Bacto Tryptone, 12.5 g Purified Agar, and 1 L distilled deionized water, with pH 6.8.

The generated YAML preserves the non-stock main ingredients and the TOGO-derived methane and air gas components, but it omits `ph_value` and has no `preparation` block. The provider instructions say to dispense the medium into vessels, seal with butyl rubber stoppers, autoclave at 121 C for 15 min, then aseptically add filter-sterilized high-purity methane with an approximately 1:4 methane-to-air headspace before inoculation.

The provider formula has two nested stock recipes, Chelated Iron Solution and Trace Element Solution. The generated record keeps references to those solutions, but it also moved the contents of both stocks into the top-level ingredient list and normalized original milliliter and milligram amounts as gram-per-liter values. Examples include 100 ml plus 1 L of distilled water becoming one 101.0 G_PER_L top-level ingredient, 0.3 ml HCl becoming 0.3 G_PER_L, 1 mg CaCl2.2H2O becoming 1 G_PER_L, 3 mg Na2MoO4.2H2O becoming 3 G_PER_L, 30 mg H3BO3 becoming 30 G_PER_L, 200 mg FeSO4.7H2O becoming 200 G_PER_L, and 500 mg EDTA becoming 500 G_PER_L.

The generated `solutions` block also turns `Ferric ammonium citrate***` into an empty `Unknown solution`. In NBRC and TOGO, this is not a stock solution; it is the 0.1 g ferric ammonium citrate component of the Chelated Iron Solution, with a note that 0.05 g ferric chloride may be substituted.

## Completeness
The record is structurally valid but chemically incomplete because the preparation sequence, final pH, and nested stock hierarchy are not represented. The high-metal flag is plausible given the stock solution content, but those stock ingredients cannot remain flattened at the final medium level.

## Findings
- The Chelated Iron Solution and Trace Element Solution compositions were flattened into top-level medium ingredients, with milligram and milliliter source units converted to `G_PER_L`.
- `Ferric ammonium citrate***` was migrated to an empty `solutions` entry even though it is a component of Chelated Iron Solution and carries an alternative ferric chloride note.
- The final pH 6.8 instruction is missing.
- The final sealed-vessel autoclave and methane-to-air headspace preparation is missing.

## Recommended Edits
- Fix the TOGO import or solution migration path for `data/normalized_yaml/bacterial/nitrate_mineral_salts_medium_nms_0_01_tryptone.yaml` so nested stock ingredients stay inside their parent stock recipe or are omitted in favor of source-linked reusable `solutions`.
- Restore `ph_value: 6.8` on the final medium.
- Add the NBRC/TOGO final preparation instruction covering rubber-stopper sealing, autoclaving at 121 C for 15 min, and aseptic high-purity filter-sterilized methane addition at approximately 1:4 methane:air headspace.
- Move ferric ammonium citrate back into Chelated Iron Solution and preserve the ferric chloride substitution note.

## Follow-up Checks
- Regenerate `data/merge_yaml/merged/nitrate_mineral_salts_medium_nms_0_01_tryptone.yaml` from the corrected normalized owner.
- Re-run open, strict, reference, and term validation on the regenerated artifact.
- Re-check the regenerated recipe against TOGO `M1871` and NBRC `NO=1116`, especially stock nesting, milligram stock units, final pH, and methane headspace preparation.

## Additional Notes
None.
