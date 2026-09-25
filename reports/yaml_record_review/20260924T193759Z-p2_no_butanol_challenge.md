# YAML Record Review: p2_no_butanol_challenge

- Repository: CultureMech
- Record: data/merge_yaml/merged/p2_no_butanol_challenge.yaml
- Started UTC: 2026-09-24T19:37:59Z
- Finished UTC: 2026-09-24T19:37:59Z
- Verdict: pass with minor issues

## Target

Reviewed generated MediaRecipe `CultureMech:007436`, `p2_no_butanol_challenge`, generated from `data/normalized_yaml/bacterial/p2_no_butanol_challenge.yaml` for MediaDB Medium 89.

## Validation

- Open LinkML validation: Passed; exited 0 with `No issues found`.
- Strict validation: Passed; scanned 1 file with 0 ERROR rows. `/private/tmp/p2_no_butanol_challenge.strict.tsv` contained only the header row.
- Reference validation: Passed; the reference validator ran 0 checks.
- Term validation: Passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

The generated identity matches MediaDB Medium 89, `P2, no butanol challenge`. An ignored-inclusive exact search for `MEDIADB:89`, `p2_no_butanol_challenge`, and `P2, no butanol challenge` across `data/merge_yaml` and `data/normalized_yaml` found exactly one normalized MediaDB 89 source and this generated record.

## Evidence

The MediaDB text export for medium 89 lists the same 11 P2 base rows present in the generated YAML: D-Glucose, Biotin, Thiamine, 4-Aminobenzoate, Potassium dibasic phosphate, Sodium chloride, Potassium dihydrogen phosphate, Magnesium sulfate, Manganese sulfate, Ferrous sulfate, and Ammonium Acetate, with matching millimolar concentrations.

## Completeness

The generated record preserves the MediaDB 89 ingredient set and did not collapse the 1% or 1.5% butanol challenge records into this no-butanol parent. No required MediaDB 89 ingredient rows were missing or added.

## Findings

1. Thiamine still carries a legacy MediaIngredientMech link.

   The primary Thiamine term is `CHEBI:18385`, but the ingredient retains `mediaingredientmech_term: MediaIngredientMech:000898` instead of an id-safe `mediaingredientmech_chebi_term`.

2. The preparation steps include generic, weakly sourced import text.

   The MediaDB text export lists ingredient concentrations and does not provide a pH value or sterilization instruction. Generated steps such as `Adjust pH if specified in original formulation` and filter sterilization at 0.22 um should either be backed by a MediaDB source field or omitted.

## Recommended Edits

- Refresh the Thiamine legacy MediaIngredientMech link to ChEBI keying.
- Remove or source the generic pH-adjustment and filter-sterilization preparation steps in MediaDB imports.

## Follow-up Checks

- After cleanup, re-fetch the MediaDB 89 text export and confirm the regenerated YAML still has exactly the 11 source rows and no 1-Butanol row.
- Re-run open, strict, reference, and term validation on the regenerated YAML.

## Additional Notes

None found.
