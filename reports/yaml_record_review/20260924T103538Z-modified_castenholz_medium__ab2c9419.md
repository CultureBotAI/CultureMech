# YAML Record Review: modified_castenholz_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_castenholz_medium__ab2c9419.yaml
- Started UTC: 2026-09-24T10:34:19Z
- Finished UTC: 2026-09-24T10:35:38Z
- Verdict: needs curation

## Target

Generated record `CultureMech:006702` for KOMODO medium `86a`, `MODIFIED CASTENHOLZ medium`.

The exact maintained owner is `data/normalized_yaml/bacterial/KOMODO_86a_MODIFIED_CASTENHOLZ_medium.yaml`, not `data/normalized_yaml/bacterial/modified_castenholz_medium.yaml`; the latter is a separate DSMZ 1470 record with the same normalized slug. The generated record was compared with the exact KOMODO owner, MediaDive medium `86a`, DSMZ Medium 86a PDF, DSMZ Medium 86 PDF, and MediaDive medium `86`.

## Validation

- Open LinkML validation: passed with no issues found.
- Strict validation: passed; `/private/tmp/modified_castenholz_medium__ab2c9419.strict.tsv` contained only the header row.
- Reference validation: passed with 0 reference checks.
- Term validation: passed.
- Embedded `curation_history`: Not checked: the available history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The record has the right top-level target, KOMODO/DSMZ `86a`, and the right final pH, 7.8.

The ingredients do not match DSMZ 86a. The history already exposes the failure mode: `dsmz-resolver-v1.0` copied ingredients from base DSMZ Medium 86, but DSMZ 86a is a modified derivative that replaces the base tryptone row and adds monosodium glutamate. `KNO3` and `NaNO3` also still carry legacy `mediaingredientmech_term` links even though both rows have primary CHEBI terms.

## Evidence

The DSMZ Medium 86a PDF defines medium 86a as DSMZ Medium 86 with tryptone replaced by 3 g/L peptone, 1 g/L monosodium glutamate added, final pH adjusted to 7.8 with NaOH, and solid medium prepared by adding 2 to 2.5% agar. MediaDive `86a` encodes the same delta: the base salt rows are followed by `Peptone` at 3 g/L, `Yeast extract` at 1 g/L, `Monosodium glutamate` at 1 g/L, `Distilled water` at 1000 ml, and conditional `Agar` at 2.25%.

The generated KOMODO `86a` record keeps the base DSMZ 86 `Tryptone` row at 1 g/L, keeps `Yeast extract` at 1 g/L, and omits the 3 g/L peptone and 1 g/L monosodium glutamate rows that distinguish 86a from 86. It also omits the 1000 ml distilled-water row, has no `preparation_steps`, and only captures pH adjustment by adding variable `NaOH` as an extracted ingredient.

The base-medium rows otherwise line up with DSMZ 86 and MediaDive `86`, including `KNO3` 103 mg, `NaNO3` 689 mg, `Na2HPO4 x 2 H2O` 140 mg, and the trace sulfate/chloride/molybdate rows.

## Completeness

The record preserves the KOMODO identifier, DSMZ 86a cross-reference in notes, the base Castenholz salt and trace rows, and pH 7.8.

It is incomplete for the actual modified Castenholz formulation because it lacks the 86a organic-component substitution and addition, lacks distilled water, lacks the conditional agar instruction, and lacks preparation prose.

## Findings

- High: DSMZ Medium 86 ingredients were copied into the DSMZ 86a/KOMODO 86a record without applying the 86a delta. This leaves an incorrect 1 g/L tryptone row and omits 3 g/L peptone plus 1 g/L monosodium glutamate.
- Medium: The source 1000 ml distilled-water row is missing.
- Medium: The pH adjustment and solid-medium agar instruction are not represented as preparation steps.
- Low: `KNO3` and `NaNO3` retain deprecated `mediaingredientmech_term` cross-links instead of id-safe `mediaingredientmech_chebi_term` links.

## Recommended Edits

- Recurate `data/normalized_yaml/bacterial/KOMODO_86a_MODIFIED_CASTENHOLZ_medium.yaml`, or the DSMZ resolver that enriched it, so DSMZ 86a is treated as a derivative of 86 with its documented replacement and addition.
- Remove the 1 g/L `Tryptone` row from this modified medium, add 3 g/L `Peptone`, and add 1 g/L `Monosodium glutamate`.
- Restore the 1000 ml distilled-water row from the DSMZ/MediaDive 86a formula.
- Add a pH-adjustment preparation step for pH 7.8 with NaOH and preserve the optional 2 to 2.5% agar instruction without making agar unconditional in the liquid formulation.
- Refresh `KNO3` and `NaNO3` so their MediaIngredientMech mappings use CHEBI-keyed links consistently.
- Regenerate `data/merge_yaml/merged/modified_castenholz_medium__ab2c9419.yaml` from the repaired maintained owner.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated YAML.
- Compare the regenerated formula against DSMZ Medium 86a and MediaDive `86a`, not only the base DSMZ 86 recipe.
- Confirm that the similarly named DSMZ 1470 owner remains distinct from KOMODO `86a`.

## Additional Notes

None found.
