# YAML Record Review: flavobacterium_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/flavobacterium_medium__75f947ac.yaml
- Started UTC: 2026-09-23T03:25:59Z
- Finished UTC: 2026-09-23T03:26:46Z
- Verdict: pass with minor issues

## Target

- Reviewed generated MediaRecipe `CultureMech:002378` / `flavobacterium_medium`, the JCM J120 import for FLAVOBACTERIUM MEDIUM.
- Cross-checked the generated record against the MediaDive REST representation for JCM J120.
- Compared the generated merge with its normalized source at `data/normalized_yaml/bacterial/flavobacterium_medium.yaml`.

## Validation

- LinkML open-schema validation: pass.
- Strict CultureMech validation: pass; 0 total ERROR rows in `/private/tmp/flavobacterium_medium_75f947ac.strict.tsv`.
- LinkML reference validation: pass; 0 external reference checks.
- LinkML term validation: pass.
- Embedded curation history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding

- The medium identity is internally coherent: `mediadive.medium:J120`, `kg_microbe_match: mediadive.medium:J120`, the MediaDive J120 label, and the record name all point to FLAVOBACTERIUM MEDIUM.
- The JCM GRMD 120 URL currently returns a JCM "Nothing found" page, so the original JCM page is not directly verifiable even though MediaDive still serves the J120 payload.
- Na2SO4 has an appropriate CHEBI grounding.
- The generated record is stale relative to the normalized source's 2026-09-13 `GROUNDED_BACTERIAL_SCORE10_EXACT_TERMS_BATCH3` repair, which added local exact terms for Tryptone and Yeast extract.

## Evidence

- MediaDive J120 asserts Tryptone 1 g/L, Yeast extract 1 g/L, Na2SO4 1 g/L, Distilled water 1 L, and pH adjustment to 6.0 with H2SO4.
- The generated file preserves those three modeled ingredient amounts, `ph_value: 6.0`, the J120 medium identity, and the pH-adjustment preparation step.
- MediaDive J120 annotates Tryptone and Yeast extract as `BD-Difco`; those source attributes are absent from the generated row labels and notes.

## Completeness

- Ingredients, pH, preparation, medium identity, and source URL are present.
- No source-specific target organism was asserted in this JCM import; target organism coverage was not evaluated for this direct medium review.
- No nested stock solutions or strain-specific variants were found in the MediaDive J120 payload.

## Findings

- Minor issue: the generated record has not picked up the normalized source's September exact-term repair for Tryptone and Yeast extract.
- Minor issue: the BD-Difco source attributes for Tryptone and Yeast extract are missing.
- Minor issue: the embedded JCM GRMD 120 URL no longer resolves to a JCM recipe page, so this record needs either an archived JCM evidence link or a note that MediaDive is the only active source for J120.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/flavobacterium_medium__75f947ac.yaml` so Tryptone and Yeast extract retain their normalized exact terms.
- Preserve the BD-Difco attribute for Tryptone and Yeast extract in `preferred_term` or `notes`.
- Investigate whether JCM J120 has moved, been withdrawn, or needs an archived/source note because GRMD 120 is no longer served by JCM.

## Follow-up Checks

- After regeneration, rerun open-schema, strict, reference, and term validation on the generated JCM J120 YAML.
- Confirm the three direct ingredient amounts and `ph_value: 6.0` are unchanged.
- Confirm Tryptone and Yeast extract are no longer ungrounded in the generated artifact.

## Additional Notes

- No composition, pH, or stock-boundary defect was found in the MediaDive J120 payload.
