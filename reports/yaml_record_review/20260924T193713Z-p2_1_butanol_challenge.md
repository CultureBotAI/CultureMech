# YAML Record Review: p2_1_butanol_challenge

- Repository: CultureMech
- Record: data/merge_yaml/merged/p2_1_butanol_challenge.yaml
- Started UTC: 2026-09-24T19:37:13Z
- Finished UTC: 2026-09-24T19:37:13Z
- Verdict: needs curation

## Target

Reviewed generated MediaRecipe `CultureMech:007438`, `p2_1_butanol_challenge`, generated from MediaDB P2 butanol challenge records 90 and 91.

## Validation

- Open LinkML validation: Passed; exited 0 with `No issues found`.
- Strict validation: Passed; scanned 1 file with 0 ERROR rows. `/private/tmp/p2_1_butanol_challenge.strict.tsv` contained only the header row.
- Reference validation: Passed; the reference validator ran 0 checks.
- Term validation: Passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

The generated record names and grounds itself as MediaDB Medium 90, `P2, 1% butanol challenge`. An ignored-inclusive exact search for `MEDIADB:90`, `MEDIADB:91`, `p2_1_butanol_challenge`, `p2_1_5_butanol_challenge`, `1% butanol`, and `1.5% butanol` across `data/merge_yaml` and `data/normalized_yaml` found the two expected normalized MediaDB sources and one generated record that merged them.

## Evidence

The MediaDB text export for medium 90 lists 1-Butanol at 98.4633 mM. The export for medium 91 lists the same P2 base recipe but changes 1-Butanol to 147.695 mM. The normalized medium 90 record captures medium 91 as a `CONCENTRATION_VARIANT` child with a note saying 1-Butanol increased from 98.4633 mM to 147.695 mM.

## Completeness

The generated record keeps all 12 P2 ingredient rows and the MediaDB 90 medium term, but it is not a faithful 1% butanol challenge record because the 1-Butanol concentration was overwritten with the 1.5% challenge value and MediaDB 91 was collapsed into `merged_from`.

## Findings

1. A concentration variant was merged into its parent and changed the defining 1-Butanol concentration.

   MediaDB 90 is the 1% butanol challenge with 1-Butanol 98.4633 `MILLIMOLAR`; MediaDB 91 is the 1.5% butanol challenge with 1-Butanol 147.695 `MILLIMOLAR`. The generated record is still labeled `MEDIADB:90` / `P2, 1% butanol challenge` but uses the 147.695 mM value and lists both `p2_1_5_butanol_challenge` and `p2_1_butanol_challenge` in `merged_from`.

2. The 1-Butanol ingredient is ungrounded despite source ontology metadata.

   The MediaDB export carries ChEBI 28885 for 1-Butanol. The generated ingredient has no `term` or `mediaingredientmech_chebi_term`, so the key challenge compound lacks the chemical grounding available from the source.

3. Thiamine still carries a legacy MediaIngredientMech link.

   The primary Thiamine term is `CHEBI:18385`, but the ingredient retains `mediaingredientmech_term: MediaIngredientMech:000898` instead of an id-safe `mediaingredientmech_chebi_term`.

## Recommended Edits

- Update merge generation so `CONCENTRATION_VARIANT` records remain separate generated records instead of being merged on their shared non-varying ingredient fingerprint.
- Regenerate MediaDB 90 with 1-Butanol 98.4633 `MILLIMOLAR` and MediaDB 91 with 1-Butanol 147.695 `MILLIMOLAR`, preserving the concentration-variant relationship between them.
- Ground 1-Butanol to the source-supplied ChEBI term and refresh the Thiamine legacy MediaIngredientMech link.

## Follow-up Checks

- Re-run an ignored-inclusive exact search for `MEDIADB:90`, `MEDIADB:91`, `98.4633`, and `147.695` in `data/merge_yaml/merged` after regeneration and confirm the two MediaDB challenge concentrations remain distinct.
- Re-run open, strict, reference, and term validation on both regenerated MediaDB YAML files.

## Additional Notes

The MediaDB exports do not supply a pH value, so the generic imported preparation step `Adjust pH if specified in original formulation` should also be reviewed for source support while fixing these records.
