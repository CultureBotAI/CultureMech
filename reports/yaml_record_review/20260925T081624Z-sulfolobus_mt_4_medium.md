# YAML Record Review: Sulfolobus MT-4 Medium

- Repository: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech`
- Record: `data/merge_yaml/merged/sulfolobus_mt_4_medium.yaml` (`CultureMech:004206`)
- Started UTC: `2026-09-25T08:16:24Z`
- Finished UTC: `2026-09-25T08:16:51Z`
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated YAML | `data/merge_yaml/merged/sulfolobus_mt_4_medium.yaml` |
| Normalized sources | `data/normalized_yaml/archaea/sulfolobus_mt_4_medium.yaml`, `data/normalized_yaml/archaea/KOMODO_182_SULFOLOBUS_medium.yaml` |
| CultureMech ID | `CultureMech:004206` |
| Media term | `komodo.medium:182a` |
| Original source | DSMZ Medium 182a, Saccharolobus (MT-4) Medium |
| Merge fingerprint | `9672ae6a15d028a0a4d8add316c364c1dc2f19ec9a76bfd3adffeef814f2dc2b` |
| Merged from | `KOMODO_182_SULFOLOBUS_medium`, `sulfolobus_mt_4_medium` |

## Validation

| Check | Result |
| --- | --- |
| LinkML schema | Passed; `linkml-validate` reported `No issues found` for the generated YAML. |
| Strict validator | Passed; `scripts/validate_strict.py` reported 1 file, 0 total errors. |
| Reference validator | Passed; `linkml-reference-validator` reported 1 file, 0 checks, all passed. |
| Term validator | Passed; `linkml-term-validator` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

## Identity and Grounding

The generated record has the expected `CultureMech:004206` identifier and canonical `komodo.medium:182a` source term. Exact gitignore-independent searches with `--no-ignore --hidden` for `CultureMech:004206`, `komodo.medium:182a`, the merge fingerprint, `sulfolobus_mt_4_medium.yaml`, and `KOMODO_182_SULFOLOBUS_medium.yaml` found this normalized 182a source, the normalized KOMODO 182 source, and this generated merge as expected.

The merge grouping is not grounded against DSMZ. DSMZ Medium 182a is Saccharolobus (MT-4) Medium at pH 3.5 with 2 g/L yeast extract and Trace element solution SL-10. DSMZ Medium 182 is Saccharolobus solfataricus Medium at pH 4.0 to 4.2 with 1 g/L yeast extract, 1 g/L Casamino acids, and Allen's trace-element solution. Those records are related, but they are not exact duplicates.

Most simple salts are plausibly grounded, but `NiCl2 x 6 H2O` is linked to generic nickel dichloride rather than a hydrate-specific term.

## Evidence

DSMZ 182a contains 2 g OXOID yeast extract, 3.10 g KH2PO4, 2.50 g ammonium sulfate, 0.20 g MgSO4 x 7 H2O, 0.25 g CaCl2 x 2 H2O, 1 ml Trace element solution SL-10, and 1000 ml distilled water. Its only preparation instruction is to adjust pH to 3.5 with 10 N H2SO4 before autoclaving.

The SL-10 stock contains 10 ml 25% HCl, 1.50 g FeCl2 x 4 H2O, 70 mg ZnCl2, 100 mg MnCl2 x 4 H2O, 6 mg H3BO3, 190 mg CoCl2 x 6 H2O, 2 mg CuCl2 x 2 H2O, 24 mg NiCl2 x 6 H2O, 36 mg Na2MoO4 x 2 H2O, and 990 ml distilled water per 1 L stock. DSMZ says to dissolve FeCl2 in the HCl, dilute in water, add and dissolve the other salts, and make the solution up to 1000 ml.

The generated YAML flattens SL-10 into top-level ingredients at stock concentration: `2.5 G_PER_L` HCl, `1.5 G_PER_L` FeCl2 x 4 H2O, `0.07 G_PER_L` ZnCl2, and so on. Because the completed medium should receive only 1 ml/L of SL-10, those trace-stock rows are about 1000-fold too concentrated in the generated final-medium representation.

## Completeness

The generated record is incomplete because it lacks the 1 ml/L SL-10 stock addition, the 1 L SL-10 stock scope, the SL-10 preparation step, the basal water row, and the explicit pH 3.5 H2SO4 preparation step. It also carries generic KOMODO 182 as a duplicate when DSMZ 182 has different yeast, Casamino-acid, pH, and trace-element requirements.

`target_organisms` is absent. The DSMZ 182 and 182a PDF recipes reviewed here do not assert growth observations, so no growth target was inferred.

## Findings

- KOMODO 182 and KOMODO 182a are over-merged even though DSMZ 182 and DSMZ 182a are distinct source recipes.
- The 1 ml Trace element solution SL-10 addition is missing.
- SL-10 stock ingredients are flattened into the final medium at stock-strength `G_PER_L` values.
- The 990 ml SL-10 water row and the basal 1 L water row are both absent.
- The SL-10 FeCl2/HCl dissolution step is absent.
- The pH 3.5 adjustment with 10 N H2SO4 is stored only as a variable H2SO4 ingredient with a note.
- `NiCl2 x 6 H2O` lost hydrate-specific grounding.

## Recommended Edits

- Repair `data/normalized_yaml/archaea/sulfolobus_mt_4_medium.yaml`, `data/normalized_yaml/archaea/KOMODO_182_SULFOLOBUS_medium.yaml`, or the KOMODO/DSMZ resolver path, then regenerate `data/merge_yaml/merged/sulfolobus_mt_4_medium.yaml`.
- Split KOMODO 182 and KOMODO 182a unless a source-backed variant relationship can preserve the recipe differences.
- Keep SL-10 as a nested 1 L stock added at 1 ml/L, with HCl and trace salts scoped to the stock.
- Add the SL-10 preparation step and the pH 3.5 adjustment with 10 N H2SO4 as preparation instructions rather than final ingredients.
- Correct `NiCl2 x 6 H2O` to a hydrate-specific term if one is available.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regenerating the merged YAML.
- Re-run exact gitignore-independent searches for `CultureMech:004206`, `komodo.medium:182a`, `9672ae6a15d028a0a4d8add316c364c1dc2f19ec9a76bfd3adffeef814f2dc2b`, `sulfolobus_mt_4_medium.yaml`, and `KOMODO_182_SULFOLOBUS_medium.yaml`.
- Compare regenerated KOMODO 182 and 182a against DSMZ Medium 182 and DSMZ Medium 182a separately.

## Additional Notes

Empty optional fields that are unrelated to source identity, SL-10 stock structure, and source-backed growth evidence were not treated as defects.

The generated YAML should not be hand-edited. The review findings target the normalized KOMODO sources, the DSMZ resolver, and merge grouping.
