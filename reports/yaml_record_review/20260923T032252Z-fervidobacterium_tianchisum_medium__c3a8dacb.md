# YAML Record Review: fervidobacterium_tianchisum_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/fervidobacterium_tianchisum_medium__c3a8dacb.yaml
- Started UTC: 2026-09-23T03:21:43Z
- Finished UTC: 2026-09-23T03:22:52Z
- Verdict: pass with minor issues

## Target

- Reviewed generated MediaRecipe `CultureMech:002972` / `fervidobacterium_tianchisum_medium`, the JCM J626 import for FERVIDOBACTERIUM TIANCHISUM MEDIUM.
- Cross-checked the generated record against the JCM 626 page and the MediaDive REST representation for JCM J626.
- Compared the generated merge with its normalized source at `data/normalized_yaml/bacterial/fervidobacterium_tianchisum_medium.yaml`.

## Validation

- LinkML open-schema validation: pass.
- Strict CultureMech validation: pass; 0 total ERROR rows in `/private/tmp/fervidobacterium_tianchisum_medium_c3a8dacb.strict.tsv`.
- LinkML reference validation: pass; 0 external reference checks.
- LinkML term validation: pass.
- Embedded curation history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding

- The record identity is correct: `mediadive.medium:J626`, the JCM GRMD 626 link, and the FERVIDOBACTERIUM TIANCHISUM MEDIUM label all agree with JCM and MediaDive.
- The formula rows match the source masses and milligram trace-element amounts.
- `Sulfur` is grounded to `CHEBI:26833` / sulfur atom, but the source row is Sulfur (powder). The local MediaIngredientMech label index maps Sulfur (powder) to `CHEBI:33403` / elemental sulfur.
- `Na2B4O7 x 10 H2O` has an appropriate primary CHEBI term but lacks a mirrored `mediaingredientmech_chebi_term`.
- Tryptone is appropriately left without a CHEBI term as a complex digest.

## Evidence

- JCM 626 and MediaDive J626 both assert the same direct one-liter ingredient list and pH 7.5.
- Glucose at 5 g/L and Na2S x 9 H2O at 0.5 g/L are correctly represented as final amounts; the 20% glucose and 5% Na2S x 9 H2O solutions are source preparation concentrations, not separate final-medium stock recipes.
- The JCM preparation text for N2 autoclaving, separate glucose and Na2S x 9 H2O sterilization, sulfur steaming, anaerobic addition, and final pH adjustment is present in the generated record.
- The generated record omits the `BD-Difco` attribute from the Tryptone row and the `powder` attribute from the Sulfur row.

## Completeness

- Ingredients, pH, preparation text, medium identity, and source URL are present.
- No source-specific target organism was asserted in this JCM import; target organism coverage was not evaluated for this direct recipe review.
- No nested stock solution was present in the source formula, so the lack of a `solutions` array is appropriate.

## Findings

- Minor issue: Sulfur powder should be grounded to the elemental sulfur mapping used elsewhere in CultureMech, not `CHEBI:26833` / sulfur atom.
- Minor issue: `Na2B4O7 x 10 H2O` is missing its mirrored `mediaingredientmech_chebi_term`.
- Minor issue: source attributes for Tryptone (BD-Difco) and Sulfur (powder) are lost.

## Recommended Edits

- Reground the Sulfur row to `CHEBI:33403` / elemental sulfur and update its MediaIngredientMech mirror accordingly.
- Add a `mediaingredientmech_chebi_term` mirror for `Na2B4O7 x 10 H2O`.
- Preserve the Tryptone `BD-Difco` and Sulfur `powder` source attributes in `preferred_term` or `notes`.

## Follow-up Checks

- After minor edits, rerun open-schema, strict, reference, and term validation on the generated JCM J626 YAML.
- Confirm glucose and Na2S x 9 H2O remain direct final ingredients, with the stock percentages only in preparation text.
- Confirm the sulfur row no longer uses the sulfur atom CHEBI term.

## Additional Notes

- No stock-boundary or duplicate-merge defect was found in this generated JCM J626 record.
