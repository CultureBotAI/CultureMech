# YAML Record Review: flavobacterium_m1_agar

- Repository: CultureMech
- Record: data/merge_yaml/merged/flavobacterium_m1_agar__55975ca4.yaml
- Started UTC: 2026-09-23T03:24:00Z
- Finished UTC: 2026-09-23T03:24:54Z
- Verdict: pass with minor issues

## Target

- Reviewed generated MediaRecipe `CultureMech:002882` / `flavobacterium_m1_agar`, the JCM J534 import for FLAVOBACTERIUM M1 AGAR.
- Cross-checked the generated record against the JCM 534 page and the MediaDive REST representation for JCM J534.
- Compared the generated merge with its normalized source at `data/normalized_yaml/bacterial/flavobacterium_m1_agar.yaml`.

## Validation

- LinkML open-schema validation: pass.
- Strict CultureMech validation: pass; 0 total ERROR rows in `/private/tmp/flavobacterium_m1_agar_55975ca4.strict.tsv`.
- LinkML reference validation: pass; 0 external reference checks.
- LinkML term validation: pass.
- Embedded curation history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding

- The primary JCM identity is correct: `mediadive.medium:J534`, the JCM GRMD 534 link, and the FLAVOBACTERIUM M1 AGAR label all agree with JCM and MediaDive.
- NaCl and Agar have appropriate CHEBI groundings.
- The generated record is stale relative to the normalized source's 2026-09-13 `GROUNDED_BACTERIAL_SCORE10_EXACT_TERMS_BATCH3` repair, which added local MICRO/FOODON terms for Proteose peptone, Yeast extract, and Beef extract.
- The `kg_microbe_match: mediadive.medium:101` annotation is questionable. DSMZ 101 is NUTRIENT AGAR or BROTH WITH NaCl and does not match the JCM J534 formula.

## Evidence

- JCM 534 and MediaDive J534 both assert Proteose peptone 5 g/L, Yeast extract 1 g/L, Beef extract 2 g/L, NaCl 3 g/L, Agar 15 g/L, Distilled water 1 L, and pH adjustment to 7.0-7.2.
- The generated file preserves those ingredient amounts, the solid agar state, `ph_value: 7.1`, and the pH-adjustment preparation step.
- JCM and MediaDive both annotate Proteose peptone, Yeast extract, and Beef extract as `BD-Difco`; those source attributes are omitted from the generated preferred terms and notes.
- MediaDive medium 101 differs materially from JCM J534, including 30 g/L rather than 3 g/L NaCl and a Peptone/Meat extract formula instead of Proteose peptone/Yeast extract/Beef extract.

## Completeness

- Ingredients, agar state, pH, preparation, medium identity, and source URL are present.
- No source-specific target organism was asserted in this JCM import; target organism coverage was not evaluated for this direct agar review.
- No nested stock solutions or strain-specific variants were found.

## Findings

- Minor issue: the generated record has not picked up the normalized source's September MICRO/FOODON exact-term repair for Proteose peptone, Yeast extract, and Beef extract.
- Minor issue: the BD-Difco source attributes for the three complex ingredients are missing.
- Minor issue: `kg_microbe_match: mediadive.medium:101` appears mismatched because DSMZ 101 has a different composition.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/flavobacterium_m1_agar__55975ca4.yaml` so Proteose peptone, Yeast extract, and Beef extract retain their normalized exact terms.
- Preserve the BD-Difco attribute for each complex ingredient in `preferred_term` or `notes`.
- Remove or correct the `kg_microbe_match: mediadive.medium:101` annotation unless a non-composition rationale for that mapping is documented.

## Follow-up Checks

- After regeneration, rerun open-schema, strict, reference, and term validation on the generated JCM J534 YAML.
- Confirm the five direct ingredient amounts, `SOLID_AGAR` physical state, and `ph_value: 7.1` are unchanged.
- Confirm Proteose peptone, Yeast extract, and Beef extract are no longer ungrounded in the generated artifact.

## Additional Notes

- No composition, pH, or stock-boundary defect was found in the JCM J534 formula itself.
