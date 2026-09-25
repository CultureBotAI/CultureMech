# YAML Record Review: Sulfer-Free Mineral Medium (SFMM)

- Repository: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech`
- Record: `data/merge_yaml/merged/sulfer_free_mineral_medium_sfmm.yaml` (`CultureMech:008622`)
- Started UTC: `2026-09-25T07:59:34Z`
- Finished UTC: `2026-09-25T08:00:09Z`
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated YAML | `data/merge_yaml/merged/sulfer_free_mineral_medium_sfmm.yaml` |
| Normalized source | `data/normalized_yaml/bacterial/sulfer_free_mineral_medium_sfmm.yaml` |
| CultureMech ID | `CultureMech:008622` |
| Media term | `TOGO:M2033` |
| Original source | NBRC `NBRC_M1326`, Sulfer-Free Mineral Medium (SFMM) |
| Merge fingerprint | `081306a1d78664dd8f8d765125e3dd4fdf6daa1276890f4cda3e8b935780d0a9` |
| Merged from | `sulfer_free_mineral_medium_sfmm` |

## Validation

| Check | Result |
| --- | --- |
| LinkML schema | Passed; `linkml-validate` exited 0 with no diagnostics for the generated YAML. |
| Strict validator | Passed; `scripts/validate_strict.py` reported 1 file, 0 total errors. |
| Reference validator | Passed; `linkml-reference-validator` reported 1 file, 0 checks, all passed. |
| Term validator | Passed; `linkml-term-validator` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

## Identity and Grounding

The generated record has the expected stable identifier, TOGO M2033 term, NBRC_M1326 source, and single-source merge fingerprint.

Exact gitignore-independent searches with `--no-ignore --hidden` for `TOGO:M2033`, `NBRC_M1326`, `CultureMech:008622`, `sulfer_free_mineral_medium_sfmm`, and `Sulfer-Free Mineral Medium` found only this maintained normalized source and its generated merge YAML for the current record. No duplicate owner or conflicting use of `CultureMech:008622` was found.

Most simple salts are grounded plausibly. `FeCl2*6H2O` is currently grounded to an anhydrous iron dichloride label, and `(NH4)6MoO7O24*4H2O` lacks a ChEBI term, so both need exact checks while the modified Hunter stock is being repaired.

## Evidence

TOGO M2033 and the NBRC 1326 page agree that the main recipe contains 975 ml water, 10 mg CaCl2*2H2O, 0.8 g KH2PO4, 10 mg MgCl2*6H2O, 2.2 g Na2HPO4, 10 g disodium succinate, 3 g NH4NO3, 5 ml dimethyl sulfoxide, optional 5 g agarose, 10 mg FeCl2*2H2O, and 20 ml modified Hunter's vitamin-free mineral base.

The modified Hunter base is its own stock: 950 ml water plus 3.3 g CaCl2*2H2O, 16 g MgCl2*6H2O, 0.102 g FeCl3*6H2O, 10 g nitrilotriacetic acid, 9.25 mg ammonium molybdate hydrate, 50 ml modified metals 44, and KOH for neutralizing the nitrilotriacetic acid. Modified metals 44 is another 1 L stock with its own water, trace salts, Na-EDTA, and 12 M HCl handling.

The generated record flattens all of those scopes. For example, water from the main recipe, the modified Hunter stock, and the modified metals stock is merged into `1926.0 G_PER_L`, while the 10 mg main CaCl2*2H2O row and the 3.3 g Hunter-stock CaCl2*2H2O row are summed into `13.3 G_PER_L`.

## Completeness

The generated record is incomplete because stock hierarchy, pH targets, and preparation comments are absent. NBRC gives pH 7.2 for the final medium, pH 6.8 for the modified Hunter base, filtration for dimethyl sulfoxide, and dark cold storage for modified metals 44.

The recipe is also conditionally agarized: agarose is listed only if needed. Treating the whole generated record as unconditional `SOLID_AGAR` overstates the physical state of the base medium.

`target_organisms` is absent. The fetched TOGO and NBRC medium pages do not assert a source-backed growth organism for this record.

## Findings

- Water, CaCl2*2H2O, and MgCl2*6H2O rows from different stock scopes were merged into top-level values (`1926.0`, `13.3`, and `26.0 G_PER_L`) that are not source final concentrations.
- Dimethyl sulfoxide, modified Hunter's vitamin-free mineral base, and modified metals 44 are empty solution entries with `G_PER_L` units even though the source uses 5 ml, 20 ml, and 50 ml additions.
- Components of the modified Hunter base and modified metals 44 stocks were promoted to top-level ingredients at stock strength.
- Milligram stock rows were not converted: 9.25 mg ammonium molybdate hydrate and 10 mg FeCl2*2H2O appear as `9.25 G_PER_L` and `10 G_PER_L`.
- KOH and HCl are variable top-level ingredients, losing their procedural roles in nitrilotriacetic-acid neutralization and metal-stock acidification.
- The generated record lacks final pH 7.2, modified Hunter pH 6.8, DMSO filtration, modified-metals acidification, and dark cold storage instructions.
- Optional agarose drove `physical_state: SOLID_AGAR`; the base recipe should either stay liquid with conditional agarose or split an agarose variant explicitly.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/sulfer_free_mineral_medium_sfmm.yaml` or the TOGO/NBRC solution migration path, then regenerate `data/merge_yaml/merged/sulfer_free_mineral_medium_sfmm.yaml`.
- Preserve the main recipe, modified Hunter's vitamin-free mineral base, and modified metals 44 as distinct solution scopes; do not merge water or duplicate salts across them.
- Store dimethyl sulfoxide, modified Hunter base, and modified metals 44 as volume additions or nested stocks, not empty `G_PER_L` solution records.
- Convert milligram quantities within their own scopes and leave the modified Hunter and modified metals stock concentrations nested.
- Add final pH 7.2, modified Hunter pH 6.8, KOH neutralization, DMSO filtration, and modified-metals acidification/storage preparation steps.
- Revisit the conditional agarose row so the base liquid recipe is not forced to `SOLID_AGAR` solely by an `if needed` supplement.
- Check exact ChEBI groundings for `FeCl2*6H2O` and ammonium molybdate hydrate.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regenerating the merged YAML.
- Re-run exact gitignore-independent searches for `TOGO:M2033`, `NBRC_M1326`, `CultureMech:008622`, and `sulfer_free_mineral_medium_sfmm` to confirm the NBRC recipe still has a single owner.
- Compare the regenerated row magnitudes against the NBRC 1326 page to verify no stock-strength trace salts remain at top level.

## Additional Notes

Empty optional fields that are unrelated to stock hierarchy and source-backed growth evidence were not treated as defects.

The generated YAML should not be hand-edited. The review findings target the maintained normalized TOGO source and the stock-aware generation path.
