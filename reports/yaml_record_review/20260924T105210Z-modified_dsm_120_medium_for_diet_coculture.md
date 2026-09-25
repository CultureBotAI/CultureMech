# YAML Record Review: modified_dsm_120_medium_for_diet_coculture

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_dsm_120_medium_for_diet_coculture.yaml
- Started UTC: 2026-09-24T10:50:53Z
- Finished UTC: 2026-09-24T10:52:10Z
- Verdict: pass with minor issues

## Target

Generated record `CultureMech:015434` for the CommunityMech-derived specialized record `Modified DSM 120 Medium for DIET Coculture`.

The generated record merges `Modified_DSM_120_Medium_for_DIET_Coculture` from `data/normalized_yaml/specialized/Modified_DSM_120_Medium_for_DIET_Coculture.yaml`. The generated YAML was compared with that maintained owner and the PubMed metadata for PMID 24837373.

## Validation

- Open LinkML validation: passed with no issues found.
- Strict validation: passed with no error rows.
- Reference validation: passed with 0 reference checks.
- Term validation: passed.
- Embedded `curation_history`: Not checked: the available history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The generated record has the correct CommunityMech-derived identity, specialized liquid classification, anaerobic atmosphere, 37 C incubation temperature, and CommunityMech `CommunityMech:000033` upstream identifier.

It is stale relative to a 2026-09-13 `ADDED_COMMUNITYMECH_STRUCTURED_SOURCES_BATCH10` repair in the maintained owner. The owner now promotes `CommunityMech:000033` into `sources[]`; the generated artifact still carries the upstream identifier only under `source_data.community_ids`.

## Evidence

The maintained owner and generated YAML agree on the six structured rows: 20 mM ethanol, 2 g/L sodium bicarbonate, 1 g/L sodium chloride, 0.002 g/L calcium chloride dihydrate, 1 mM L-cysteine, and 0.5 mM sodium sulfide. The generated notes also retain the N2/CO2 headspace, serum-bottle vessel, no-yeast-extract/no-Casitone/no-resazurin modifications from DSM 120, and inoculation-volume details imported from CommunityMech.

PubMed resolves PMID 24837373 to the Rotaru et al. 2014 `Applied and Environmental Microbiology` article on direct interspecies electron transfer between `Geobacter metallireducens` and `Methanosarcina barkeri`, matching the CommunityMech evidence reference.

The full-text PMC PDF endpoint returned a JavaScript proof-of-work interstitial during review, so the paper methods were not independently extracted for a method-line comparison.

## Completeness

The generated record is complete for the CommunityMech formula rows and CommunityMech source-data block.

It is incomplete for the new structured `sources[]` block that already exists in the maintained owner, and the PMID evidence snippet in `source_data.evidence` supports the DIET coculture phenotype rather than the modified DSM 120 recipe text directly.

## Findings

- Low: The generated YAML is stale relative to the 2026-09-13 repair that added a structured `sources[]` entry for `CommunityMech:000033`.
- Low: The sodium sulfide row still uses a legacy `mediaingredientmech_term` field even though the row also has the CHEBI identity needed for a modern `mediaingredientmech_chebi_term`.
- Low: Add medium-specific literature evidence if PMID 24837373 or an upstream CommunityMech citation contains the exact modified DSM 120 formula.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/modified_dsm_120_medium_for_diet_coculture.yaml` from the repaired 2026-09-13 maintained owner so `sources[]` is present.
- Replace the remaining sodium sulfide `mediaingredientmech_term` with a CHEBI-keyed `mediaingredientmech_chebi_term`.
- Add a medium-specific evidence snippet or citation for the six-row modified DSM 120 formula when the article methods text or upstream CommunityMech provenance is available.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated YAML.
- Confirm that regeneration preserves the six CommunityMech ingredient rows, the anaerobic N2/CO2 headspace note, the 37 C incubation temperature, `source_data.community_ids`, and the new `sources[]` entry.

## Additional Notes

None found.
