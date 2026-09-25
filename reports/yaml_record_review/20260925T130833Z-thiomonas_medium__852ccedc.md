# YAML Record Review: thiomonas_medium__852ccedc

- Repository: CultureMech
- Record: `data/merge_yaml/merged/thiomonas_medium__852ccedc.yaml`
- Started UTC: 2026-09-25T13:08:33Z
- Finished UTC: 2026-09-25T13:08:33Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:001460`
- Name: `thiomonas_medium`
- Source grounding: direct DSMZ/MediaDive Medium 35a merged with KOMODO 35 and 35a family records

## Validation

- Schema validation: passed; exited 0 with no diagnostics.
- Strict validation: passed with zero errors; `/private/tmp/thiomonas_medium__852ccedc.strict.tsv` was header-only.
- Reference validation: passed; exited 0 with no diagnostics.
- Term validation: passed after the known EUtils warning.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding

- The canonical merged record is grounded to DSMZ Medium 35a, `THIOMONAS MEDIUM`.
- Its `merged_from` list also includes KOMODO `35`, `35.1`, `35a`, and `35a.1` records; the normalized sources already classify those KOMODO records as variants under the THIOBACILLUS THIOOXIDANS MEDIUM family.
- The source search for DSMZ 35, DSMZ 35a, and the KOMODO 35/35a family was exact and included ignored and hidden files.

## Evidence

- DSMZ 35a is a 1030 ml medium assembled from 900 ml Solution A, 100 ml Solution B, 20 ml Solution C, and 10 ml Solution D.
- Solution A contains 0.10 g NH4Cl, 3.00 g KH2PO4, optional 20.00 g agar, and 900 ml water, and is adjusted to pH 6.0 with NaOH.
- Solution B contains 0.10 g MgCl2 x 6 H2O, 0.14 g CaCl2 x 2 H2O, and 100 ml water.
- Solution C contains 5.00 g Na2S2O3 x 5 H2O and 20 ml water; Solution D contains 1.00 g yeast extract and 10 ml water.
- DSMZ 35 is a distinct 1000 ml acidithiobacillus formulation with 0.10 g NH4Cl, 3.00 g KH2PO4, 0.10 g MgCl2 x 6 H2O, 0.14 g CaCl2 x 2 H2O, 10.00 g powdered sulfur, 1000 ml water, and final pH 4.2.

## Completeness

- The generated record has the DSMZ 35a non-water ingredients and its main assembly instruction.
- Solution water rows are absent and the solution hierarchy is flattened away, leaving stock-strength Solution C and Solution D ingredients as if they were final g/L concentrations.
- The generated record has no `target_organisms`; there are no growth claims to verify.

## Findings

- DSMZ 35a Solution B, C, and D concentrations were imported at stock strength: MgCl2 x 6 H2O `1`, CaCl2 x 2 H2O `1.4`, Na2S2O3 x 5 H2O `250`, and yeast extract `100` g/L.
- The generated parent should account for 100 ml Solution B, 20 ml Solution C, and 10 ml Solution D in 1030 ml final volume instead of treating each solution as one liter of final medium.
- The merge grouped DSMZ 35 and DSMZ 35a descendants under one fingerprint even though DSMZ 35 is a sulfur medium at pH 4.2 and DSMZ 35a is a thiosulfate and yeast-extract medium at pH 6.0.
- The source normalized records keep variant metadata for the KOMODO 35/35a family, but the merged record demotes that to `SOURCE_DUPLICATE`, which erases the intended PH_VARIANT and STRAIN_SPECIFIC_VARIANT relationships.

## Recommended Edits

- Reconstruct DSMZ 35a as a four-solution assembly, preserving 900 ml, 100 ml, 20 ml, and 10 ml solution doses.
- Keep DSMZ 35 sulfur medium and DSMZ 35a Thiomonas medium as related variants rather than exact duplicate source records.
- Preserve the KOMODO 35.1, 35a, and 35a.1 variant relationships when the generated merge is repaired.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after repairing DSMZ 35a stock topology.
- Re-run the merge review for all DSMZ 35 and 35a records so the pH and sulfur/thiosulfate split is explicit.

## Additional Notes

- Empty optional fields were not treated as defects.
