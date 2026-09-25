# YAML Record Review: Sulfolobus Medium

- Repository: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech`
- Record: `data/merge_yaml/merged/sulfolobus_medium__108a0f1c.yaml` (`CultureMech:008977`)
- Started UTC: `2026-09-25T08:02:37Z`
- Finished UTC: `2026-09-25T08:03:24Z`
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated YAML | `data/merge_yaml/merged/sulfolobus_medium__108a0f1c.yaml` |
| Normalized source | `data/normalized_yaml/archaea/TOGO_M2396_Sulfolobus_Medium.yaml` |
| CultureMech ID | `CultureMech:008977` |
| Media term | `TOGO:M2396` |
| Original source | DSMZ Medium 88, Sulfolobus Medium |
| Merge fingerprint | `108a0f1cee620e55e68fcdd89acd0834e3663028d98d61225df7c7189d0db5c8` |
| Merged from | `TOGO_M2396_Sulfolobus_Medium` |

## Validation

| Check | Result |
| --- | --- |
| LinkML schema | Passed; `linkml-validate` exited 0 with no diagnostics for the generated YAML. |
| Strict validator | Passed; `scripts/validate_strict.py` reported 1 file, 0 total errors. |
| Reference validator | Passed; `linkml-reference-validator` reported 1 file, 0 checks, all passed. |
| Term validator | Passed; `linkml-term-validator` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

## Identity and Grounding

The generated record has the expected TOGO M2396 identifier and DSMZ Medium 88 source URL, but its row set is not the unmodified DSMZ 88 Sulfolobus Medium. The 0.7% Gelrite plus 0.5% yeast-extract rows match the DSM 18247 modification note in DSMZ 88, which also sets pH 9.0.

Exact gitignore-independent searches with `--no-ignore --hidden` for `TOGO:M2396`, `DSMZ_Medium88`, `CultureMech:008977`, and `sulfolobus_medium` found this TOGO owner plus many legitimate DSMZ 88 family variants: anaerobic variants, strain-specific DSMZ 88 variants, tryptone variants, JCM/J165, and KOMODO 88 copies. No conflicting use of `CultureMech:008977` was found.

Simple salt groundings are mostly plausible. `VOSO4 x 2 H2O` still carries a legacy `mediaingredientmech_term`, and the generated `CoSO4` row loses the heptahydrate present in the source Allen trace-element stock.

## Evidence

The DSMZ 88 base formula contains 1.3 g ammonium sulfate, 0.28 g KH2PO4, 0.25 g MgSO4*7H2O, 0.07 g CaCl2*2H2O, 0.02 g FeCl3*6H2O, 10 ml Allen trace-element solution, 1.0 g OXOID yeast extract, and 1 L water. It says to adjust the salt solution to pH 2.0 with 10 N H2SO4 and sterilize yeast extract separately from a neutral 10% stock.

DSMZ 88 later lists a DSM 18247 modification: 0.5% yeast extract, 0.7% Gelrite, and pH 9.0. The TOGO M2396 payload and generated YAML use 0.5% yeast extract and 0.7% Gelrite, but the generated record still identifies as generic Sulfolobus Medium and has no pH 9.0 field.

TOGO M2396 keeps Allen's trace-element solution as a 10 ml addition and a separate 1 L stock. The generated record flattens the 1 L Allen stock into the top-level ingredient list and sums its water with the basal 1 L water, yielding `2000.0 G_PER_L` distilled water and full-strength trace salts such as `450 G_PER_L` Na2B4O7*10H2O.

## Completeness

The generated record is incomplete because the Allen stock hierarchy, the salt-solution pH adjustment, the separate yeast-extract sterilization, the Allen-stock pH adjustment, and the strain-specific pH 9.0 context are absent.

`target_organisms` is absent. DSMZ 88 lists strain-specific variants but does not assert growth observations in this medium record, so no growth target was inferred.

## Findings

- The record appears to mix the generic DSMZ 88 source identity with the DSM 18247 modification rows for 0.7% Gelrite and 0.5% yeast extract while omitting the required pH 9.0.
- The basal 1 L water and the Allen trace-stock 1 L water were summed into `2000.0 G_PER_L`.
- The 10 ml/L Allen trace-element addition is an empty `G_PER_L` solution record.
- Allen-stock milligram quantities were promoted to top-level `G_PER_L` rows, including `450 G_PER_L` Na2B4O7*10H2O, `180 G_PER_L` MnCl2*4H2O, `22 G_PER_L` ZnSO4*7H2O, and `5 G_PER_L` CuCl2*2H2O.
- `H2SO4` and `HCl` are variable top-level ingredients rather than the 10 N sulfuric-acid pH adjustment for the salt solution and the 1 N HCl pH adjustment for the Allen stock.
- `CoSO4` lost the `x 7 H2O` hydrate state from DSMZ 88.

## Recommended Edits

- Repair `data/normalized_yaml/archaea/TOGO_M2396_Sulfolobus_Medium.yaml` or the TOGO import path, then regenerate `data/merge_yaml/merged/sulfolobus_medium__108a0f1c.yaml`.
- Decide whether TOGO M2396 should represent generic DSMZ 88 or the DSM 18247 modification; if it keeps Gelrite and 0.5% yeast extract, encode the pH 9.0 DSM 18247 context explicitly.
- Keep Allen's trace-element solution as a nested 1 L stock added at 10 ml/L, or as a structured stock reference, not as top-level full-strength trace salts.
- Convert Allen-stock milligram values within their own stock scope and prevent water merging across basal and stock scopes.
- Add preparation steps for pH 2.0 salt-solution adjustment with 10 N H2SO4, separate neutral-pH yeast-extract sterilization, and pH 2 Allen-stock adjustment with 1 N HCl.
- Check `CoSO4 x 7 H2O` and the legacy `VOSO4 x 2 H2O` link during trace-stock repair.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regenerating the merged YAML.
- Re-run exact gitignore-independent searches for `TOGO:M2396`, `DSMZ_Medium88`, `CultureMech:008977`, and `sulfolobus_medium` to confirm repaired M2396 remains distinct from strain-specific and anaerobic DSMZ 88 variants.
- Compare the repaired M2396 record with the DSMZ 88 parent record in `sulfolobus_medium__d528f768.yaml`.

## Additional Notes

Empty optional fields that are unrelated to stock hierarchy and source-backed growth evidence were not treated as defects.

The generated YAML should not be hand-edited. The review findings target the maintained normalized TOGO source and the stock-aware generation path.
