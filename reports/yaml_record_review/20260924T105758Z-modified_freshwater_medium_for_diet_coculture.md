# YAML Record Review: modified_freshwater_medium_for_diet_coculture

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_freshwater_medium_for_diet_coculture.yaml
- Started UTC: 2026-09-24T10:55:17Z
- Finished UTC: 2026-09-24T10:57:58Z
- Verdict: pass with minor issues

## Target

Generated record `CultureMech:015435` for the CommunityMech-derived specialized record `Modified Freshwater Medium for DIET Coculture`.

The generated record merges `Modified_Freshwater_Medium_for_DIET_Coculture` from `data/normalized_yaml/specialized/Modified_Freshwater_Medium_for_DIET_Coculture.yaml`. The generated YAML was compared with that maintained owner and Crossref metadata for DOI `10.1039/C3EE42189A`.

## Validation

- Open LinkML validation: passed with no issues found.
- Strict validation: passed with no error rows.
- Reference validation: failed because DOI `10.1039/C3EE42189A` resolved but no snippet-checkable content was available through the validator providers.
- Term validation: passed.
- Embedded `curation_history`: Not checked: the available history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The generated record has the correct CommunityMech-derived identity, specialized liquid classification, anaerobic atmosphere, 37 C incubation temperature, and CommunityMech `CommunityMech:000032` upstream identifier.

It is stale relative to a 2026-09-13 `ADDED_COMMUNITYMECH_STRUCTURED_SOURCES_BATCH10` repair in the maintained owner. The owner now promotes `CommunityMech:000032` into `sources[]`; the generated artifact still carries the upstream identifier only under `source_data.community_ids`.

## Evidence

The maintained owner and generated YAML agree on the three structured rows: 20 mM ethanol, 1 mM L-cysteine, and 0.5 mM sodium sulfide nonahydrate. The generated notes retain the N2/CO2 headspace, anaerobic pressure tube and serum bottle vessels, modified freshwater medium wording, and the anaerobic sterile-stock addition details imported from CommunityMech.

Crossref resolves DOI `10.1039/C3EE42189A` to the Rotaru et al. 2014 `Energy & Environmental Science` paper on direct interspecies electron transfer to `Methanosaeta` for carbon dioxide reduction to methane, matching the CommunityMech evidence reference.

The validator could not retrieve snippet-checkable full text for that DOI, so the article methods were not independently compared to the formula during this review.

## Completeness

The generated record is complete for the CommunityMech formula rows and CommunityMech source-data block.

It is incomplete for the new structured `sources[]` block that already exists in the maintained owner, and the DOI evidence snippet in `source_data.evidence` supports the DIET coculture phenotype rather than the modified freshwater recipe text directly.

## Findings

- Low: The generated YAML is stale relative to the 2026-09-13 repair that added a structured `sources[]` entry for `CommunityMech:000032`.
- Low: The sodium sulfide nonahydrate row still uses a legacy `mediaingredientmech_term` field even though the row also has a CHEBI term.
- Low: The DOI evidence is valid at the Crossref metadata layer but is not directly verifiable by the reference validator; add medium-specific full-text evidence if DOI `10.1039/C3EE42189A` or an upstream CommunityMech citation contains the exact modified freshwater formula.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/modified_freshwater_medium_for_diet_coculture.yaml` from the repaired 2026-09-13 maintained owner so `sources[]` is present.
- Replace the remaining sodium sulfide nonahydrate `mediaingredientmech_term` with a CHEBI-keyed `mediaingredientmech_chebi_term`.
- Add a validator-accessible, medium-specific evidence snippet or citation for the three-row modified freshwater formula.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated YAML.
- Confirm that regeneration preserves the three CommunityMech ingredient rows, the anaerobic N2/CO2 headspace note, the 37 C incubation temperature, `source_data.community_ids`, and the new `sources[]` entry.

## Additional Notes

None found.
