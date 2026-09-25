# YAML Record Review: Sulfolobus Solfataricus Medium

- Repository: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech`
- Record: `data/merge_yaml/merged/sulfolobus_solfataricus_medium__60eedb72.yaml` (`CultureMech:002531`)
- Started UTC: `2026-09-25T08:17:30Z`
- Finished UTC: `2026-09-25T08:18:17Z`
- Verdict: pass with minor issues

## Target

| Field | Value |
| --- | --- |
| Generated YAML | `data/merge_yaml/merged/sulfolobus_solfataricus_medium__60eedb72.yaml` |
| Normalized source | `data/normalized_yaml/archaea/sulfolobus_solfataricus_medium.yaml` |
| CultureMech ID | `CultureMech:002531` |
| Media term | `mediadive.medium:J171` |
| Original source | JCM Medium J171, SULFOLOBUS SOLFATARICUS MEDIUM |
| Merge fingerprint | `60eedb727003183c9e8da0008e3fefb4b4a699293b523a6559ce3d413d1f398e` |
| Merged from | `sulfolobus_solfataricus_medium` |

## Validation

| Check | Result |
| --- | --- |
| LinkML schema | Passed; `linkml-validate` reported `No issues found` for the generated YAML. |
| Strict validator | Passed; `scripts/validate_strict.py` reported 1 file, 0 total errors. |
| Reference validator | Passed; `linkml-reference-validator` reported 1 file, 0 checks, all passed. |
| Term validator | Passed; `linkml-term-validator` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

## Identity and Grounding

The generated record has the expected `CultureMech:002531` identifier, `mediadive.medium:J171` source term, JCM 171 identity, and pH 4.1 value. Exact gitignore-independent searches with `--no-ignore --hidden` for `CultureMech:002531`, `mediadive.medium:J171`, the merge fingerprint, and `sulfolobus_solfataricus_medium.yaml` found this normalized source and generated merge as the only direct recipe records.

The ingredient groundings are plausible for the MediaDive payload: KH2PO4, ammonium sulfate, MgSO4 x 7 H2O, CaCl2 x 2 H2O, MnCl2 x 4 H2O, Na2B4O7 x 10 H2O, ZnSO4 x 7 H2O, CuCl2 x 2 H2O, Na2MoO4 x 2 H2O, VOSO4 x n H2O, and CoSO4 x 7 H2O all carry matching final concentrations. Casamino acids is correctly ungrounded because it is a mixture, not a single ChEBI entity.

## Evidence

The live JCM 171 page lists 3.1 g KH2PO4, 2.5 g ammonium sulfate, 0.2 g MgSO4 x 7 H2O, 0.25 g CaCl2 x 2 H2O, low-milligram trace salts, 1 g yeast extract, 1 g Casamino acids, and 1 L distilled water, and instructs adjustment to pH 4.0-4.2 with 10 N H2SO4.

MediaDive J171 models the same recipe as a 1 L main solution, including the same salt, trace-salt, yeast-extract, Casamino-acid, and distilled-water rows, with a fixed pH of 4.1 and the same H2SO4 adjustment step.

The generated YAML preserves the salts, trace salts, yeast extract, Casamino acids, final concentrations, source pH, and sulfuric-acid pH adjustment. It flattens the 1 L main solution and omits the explicit distilled-water row.

## Completeness

The generated record is complete for the source identity, solute formulation, and pH adjustment from MediaDive J171. The only recipe detail lost is the explicit 1 L distilled-water row.

`target_organisms` is absent. The MediaDive and JCM recipe metadata reviewed here do not assert growth observations, so no growth target was inferred.

## Findings

- The 1 L distilled-water row from JCM and MediaDive is omitted from the flat generated record.

## Recommended Edits

- If source solvent rows are preserved for JCM media in a future generator pass, keep J171 with 1 L distilled water and the final pH 4.0-4.2 H2SO4 adjustment.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation if the normalized source or generated YAML changes.
- Re-run exact gitignore-independent searches for `CultureMech:002531`, `mediadive.medium:J171`, `60eedb727003183c9e8da0008e3fefb4b4a699293b523a6559ce3d413d1f398e`, and `sulfolobus_solfataricus_medium.yaml`.

## Additional Notes

Empty optional fields that are unrelated to source-backed growth evidence were not treated as defects.

The generated YAML should not be hand-edited. The review finding targets any future solvent-row generation pass.
