# YAML Record Review: thermoplasma_volcanium_medium__5a145f50

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermoplasma_volcanium_medium__5a145f50.yaml
- Started UTC: 2026-09-25T12:00:32Z
- Finished UTC: 2026-09-25T12:00:32Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:001507`, `thermoplasma_volcanium_medium`, generated from DSMZ Medium 398 / MediaDive `mediadive.medium:398` and merged with a KOMODO `for_dsm_4301` derivative.

## Validation

- LinkML schema: Passed; the command exited 0 with no diagnostics.
- Strict validation: Passed with 0 ERROR rows; `/private/tmp/thermoplasma_volcanium_medium__5a145f50.strict.tsv` contained only the header.
- Reference validation: Passed; the command exited 0 with no diagnostics.
- Term validation: Passed.
- Embedded curation history: Not checked; the available history validator covers standalone `history/` records, not embedded `MediaRecipe.curation_history`.

## Identity and Grounding

The primary recipe is grounded to DSMZ Medium 398, "THERMOPLASMA VOLCANIUM MEDIUM". The merged KOMODO `for_dsm_4301` source corresponds to a DSM 4301-specific DSMZ instruction, not an exact duplicate of the base medium.

## Evidence

- DSMZ 398 lists 3.00 g KH2PO4, 1.00 g MgSO4 x 7 H2O, 0.25 g CaCl2 x 2 H2O, 0.20 g (NH4)2SO4, 1.00 g yeast extract, 5.00 g glucose, 4.00 g sulfur for anaerobic media only, and 1000 ml distilled water.
- DSMZ 398 says to adjust the mineral base to about pH 2 with sulfuric acid, autoclave it, add glucose and yeast extract from filter-sterilized stocks, and check final pH to be 2 to 3.
- DSMZ 398 also says that DSM 4301 receives 0.5 g/L meat extract and notes that aerobic growth of that strain can be difficult.
- For anaerobic growth, DSMZ 398 uses the acidified sulfur-containing mineral base under N2 + CO2 at 80 + 20 and tyndallises the bottles.

## Completeness

The base non-water ingredient masses and preparation text are present. The generated record drops the 1000 ml water row, drops the DSM 4301 meat-extract variant details while still merging `for_dsm_4301` as a source duplicate, and preserves anaerobic sulfur only as an ingredient note.

## Findings

- `Distilled water` 1000 ml from DSMZ 398 is absent.
- `for_dsm_4301` should not be a `SOURCE_DUPLICATE`: DSMZ 398 adds 0.5 g/L meat extract for DSM 4301 and discusses aerobic growth of that strain.
- The DSM 4301 meat-extract addition is lost entirely from the merged record.
- The pH range 2 to 3 is present only as a free-text `ADJUST_PH` step and is not structured.
- `Sulfur` loses some source specificity: it is for anaerobic media only and should remain scoped to anaerobic growth.

## Recommended Edits

- Add the 1000 ml distilled-water row.
- Split `for_dsm_4301` into a DSM 4301 variant that adds 0.5 g/L meat extract instead of keeping it as a source duplicate.
- Preserve the DSM 4301 aerobic-growth caution with the variant, not the base medium.
- Keep anaerobic sulfur and N2 + CO2 handling tied to anaerobic growth.
- Structure pH 2 to 3 if the schema can carry ranges for this recipe.

## Follow-up Checks

- Inspect the normalized KOMODO 398 and KOMODO 398.1 derivatives together to avoid another merge between the base and DSM 4301 variant.
- Consider whether the repository should model aerobic and anaerobic DSMZ 398 formulations as separate variants.

## Additional Notes

No target-organism evidence was reviewed. The exact source search included ignored and hidden files and found DSMZ 398 plus KOMODO 398-derived normalized records, including the `for_dsm_4301` source folded into this merge.
