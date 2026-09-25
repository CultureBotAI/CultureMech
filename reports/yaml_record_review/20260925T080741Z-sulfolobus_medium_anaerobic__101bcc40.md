# YAML Record Review: Sulfolobus Medium (Anaerobic)

- Repository: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech`
- Record: `data/merge_yaml/merged/sulfolobus_medium_anaerobic__101bcc40.yaml` (`CultureMech:015370`)
- Started UTC: `2026-09-25T08:07:41Z`
- Finished UTC: `2026-09-25T08:08:09Z`
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated YAML | `data/merge_yaml/merged/sulfolobus_medium_anaerobic__101bcc40.yaml` |
| Normalized sources | `KOMODO_88-2_For_DSM_18786`, `medium_88_modified_for_dsm_10039`, `medium_88_modified_for_dsm_12421`, `medium_88_modified_for_dsm_18247`, `medium_88_modified_for_dsm_5389`, `medium_88_modified_for_dsm_6482`, `medium_88_modified_for_dsm_7519`, `sulfolobus_medium_anaerobic` |
| CultureMech ID | `CultureMech:015370` |
| Media term | `mediadive.medium:88a` |
| Original source | DSMZ Medium 88a plus seven KOMODO DSMZ Medium 88 strain modifications |
| Merge fingerprint | `101bcc40e84f854160a00e35bbaee8be1b04c6627afc93ff5949c5a98e0dc7f8` |
| Merged from | 8 source records |

## Validation

| Check | Result |
| --- | --- |
| LinkML schema | Passed; `linkml-validate` reported `No issues found` for the generated YAML. |
| Strict validator | Passed; `scripts/validate_strict.py` reported 1 file, 0 total errors. |
| Reference validator | Passed; `linkml-reference-validator` reported 1 file, 0 checks, all passed. |
| Term validator | Passed; `linkml-term-validator` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

## Identity and Grounding

The primary `CultureMech:015370` and `mediadive.medium:88a` identity belongs to the specialized MediaDive DSMZ 88a Sulfolobus Medium (Anaerobic) source. Exact gitignore-independent searches with `--no-ignore --hidden` for `CultureMech:015370`, `mediadive.medium:88a`, and the merge fingerprint found this source and generated record as the only owners of the stable identifier, exact MediaDive term, and fingerprint.

The merge grouping is not grounded. It combines the DSMZ 88a anaerobic recipe with seven KOMODO records whose source notes identify DSMZ Medium 88 strain-specific variants: DSM 18786, DSM 10039, DSM 12421, DSM 18247, DSM 5389, DSM 6482, and DSM 7519. Those are modifications of DSMZ 88, not aliases for DSMZ 88a.

An exact gitignore-independent search for `sulfolobus_medium_anaerobic.yaml` also showed that the TOGO M2387 file appears both in this eight-source merge and in the generated singleton `sulfolobus_medium_anaerobic.yaml`, so source ownership is duplicated across generated outputs.

## Evidence

DSMZ 88a contains the anaerobic pH 4.0 formula with 10 g sulfur powder, 0.5 g yeast extract, 0.5 g Na2S x 9 H2O, and 10 ml Allen trace-element solution. It requires pH 4.0 adjustment with 1 N H2SO4, 100% N2 sparging, anoxic dispensing into sulfur-containing vessels, three successive boiling-water sterilization cycles, and sterile anoxic yeast-extract and sulfide stocks.

DSMZ 88 lists different strain-specific changes for the merged KOMODO records. DSM 18786 uses only 0.10 g/L yeast extract, adds 10 g/L sulfide ore, and adjusts pH to 0.8. DSM 18247 uses 0.5% yeast extract, 0.7% Gelrite, and pH 9.0. DSM 5389, DSM 7519, and DSM 12421 adjust pH to 3.0 to 3.5. DSM 6482 and DSM 10039 use 0.20 g/L yeast extract and add 5 g/L powdered sulfur.

The normalized KOMODO records instead share the DSMZ 88a-like signature with 10 g/L sulfur, 0.5 g/L yeast extract, 0.5 g/L Na2S x 9 H2O, and flattened Allen trace-stock components. That copied signature is why the merge considered them source duplicates.

The generated record also lacks a 10 ml Allen stock reference. It lifts stock quantities such as `0.18 G_PER_L` MnCl2 x 4 H2O and `0.45 G_PER_L` Na2B4O7 x 10 H2O into the final ingredient list, then applies the DSMZ 88a pH 4.0 anaerobic procedure and the Allen-stock pH 2 HCl adjustment to the whole merged record.

## Completeness

The generated record is incomplete because it cannot faithfully represent any one member of the merge cluster. It loses the distinct DSMZ 88 pH and supplement changes, leaves Allen's trace-element solution flattened, and erases which preparation steps apply to the anaerobic DSMZ 88a recipe versus the aerobic or strain-specific DSMZ 88 derivatives.

`target_organisms` is absent. The reviewed DSMZ medium PDFs describe recipes and strain-specific modifications but do not assert growth observations, so no growth target was inferred.

## Findings

- Seven DSMZ 88 strain-specific KOMODO sources were over-merged into the canonical DSMZ 88a anaerobic record as `SOURCE_DUPLICATE` variants.
- The TOGO `sulfolobus_medium_anaerobic.yaml` source is claimed by this suffixed merge and by the stale generated singleton with the same basename.
- DSM 18786, DSM 18247, DSM 5389, DSM 7519, DSM 12421, DSM 6482, and DSM 10039 have distinct DSMZ 88 modification instructions that are absent from the generated record.
- The KOMODO DSMZ 88 variant records share an erroneous DSMZ 88a-like ingredient signature, including sulfur, Na2S x 9 H2O, and 0.5 g/L yeast extract.
- Allen trace-stock components are flattened into final `G_PER_L` ingredients.
- The Allen-stock pH 2 HCl adjustment appears as a top-level `ADJUST_PH` step after the DSMZ 88a pH 4.0 anaerobic procedure.

## Recommended Edits

- Repair the seven normalized KOMODO DSMZ 88 variant sources so each encodes its actual DSMZ 88 modification rather than the DSMZ 88a anaerobic ingredient signature.
- Regenerate `data/merge_yaml/merged/sulfolobus_medium_anaerobic__101bcc40.yaml` after the source records no longer share a false ingredient fingerprint.
- Split DSMZ 88a away from DSMZ 88 strain variants; do not preserve the `SOURCE_DUPLICATE` relationship for sources with different pH, yeast, sulfur, sulfide ore, or Gelrite instructions.
- Ensure `data/normalized_yaml/archaea/sulfolobus_medium_anaerobic.yaml` is owned by only one generated merge output.
- Preserve Allen's trace-element solution as a stock scoped to DSMZ 88/88a imports rather than flattening it into top-level final-medium concentrations.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after repairing the normalized sources and regenerating merged YAML.
- Re-run exact gitignore-independent searches for `CultureMech:015370`, `mediadive.medium:88a`, `101bcc40e84f854160a00e35bbaee8be1b04c6627afc93ff5949c5a98e0dc7f8`, and the eight `merged_from` basenames.
- Compare each regenerated DSMZ 88 strain variant against the DSMZ 88 PDF note for the named DSM accession.

## Additional Notes

Empty optional fields that are unrelated to source identity, strain-specific modifications, and source-backed growth evidence were not treated as defects.

The generated YAML should not be hand-edited. The review findings target the maintained normalized KOMODO and MediaDive sources plus the fingerprint merge grouping.
