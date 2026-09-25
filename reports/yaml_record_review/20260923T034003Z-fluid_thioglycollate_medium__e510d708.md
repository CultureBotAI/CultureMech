# YAML Record Review: fluid_thioglycollate_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/fluid_thioglycollate_medium__e510d708.yaml
- Started UTC: 2026-09-23T03:39:01Z
- Finished UTC: 2026-09-23T03:40:03Z
- Verdict: pass with minor issues

## Target

- Reviewed generated MediaRecipe `CultureMech:002809` / `fluid_thioglycollate_medium`, the JCM J460 import for FLUID THIOGLYCOLLATE MEDIUM.
- Cross-checked the generated record against the MediaDive REST representation for JCM J460.
- Compared the generated merge with its normalized source at `data/normalized_yaml/bacterial/fluid_thioglycollate_medium.yaml`.

## Validation

- LinkML open-schema validation: pass.
- Strict CultureMech validation: pass; `/private/tmp/fluid_thioglycollate_medium_e510d708.strict.tsv` contains only its header row.
- LinkML reference validation: pass; 0 external reference checks.
- LinkML term validation: pass.
- Embedded curation history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding

- The MediaDive J460 identity is coherent: `mediadive.medium:J460`, the FLUID THIOGLYCOLLATE MEDIUM label, and the stored source link all point at JCM GRMD 460.
- The live JCM GRMD 460 URL currently returns a JCM "Nothing found" page, so the original JCM page is not directly verifiable even though MediaDive still serves the J460 payload.
- L-Cystine, Glucose, NaCl, Sodium thioglycollate, Resazurin, and Agar have appropriate CHEBI groundings.
- Trypticase peptone and Yeast extract are ungrounded complex ingredients; that is acceptable.

## Evidence

- MediaDive J460 asserts Trypticase peptone 15 g/L, L-Cystine 0.5 g/L, Glucose 2 g/L, Yeast extract 5 g/L, NaCl 2.5 g/L, Sodium thioglycollate 0.5 g/L, Resazurin 1 mg/L, Agar 15 g/L for solid medium, and Distilled water 1 L.
- The generated record preserves those modeled ingredient amounts, including Resazurin as 0.001 g/L and Agar as a 15 g/L solid-medium row.
- MediaDive J460 asserts pH 7.1 and the generated preparation text preserves its Na2CO3 pH adjustment and N2-atmosphere handling.
- MediaDive J460 annotates Trypticase peptone as BD-BBL, Yeast extract as BD-Difco, and Agar as BD-Difco / Bacto; those source attributes are absent from the generated record.

## Completeness

- Ingredients, pH, preparation, medium identity, and source URL are present.
- No source-specific target organism was asserted in this JCM import; target organism coverage was not evaluated for this direct medium review.
- No nested stock solutions or strain-specific variants were found in the MediaDive J460 payload.

## Findings

- Minor issue: the brand/source attributes for Trypticase peptone, Yeast extract, and Agar are missing.
- Minor issue: the live JCM GRMD 460 URL no longer resolves to a JCM recipe page, so this record needs either an archived JCM evidence link or a note that MediaDive is the only active source for J460.
- Minor issue: Agar is a source row for solid medium, while the record's name is fluid; curation should confirm that the generated record intentionally models the agar variant.

## Recommended Edits

- Preserve the BD-BBL, BD-Difco, and Bacto source attributes in `preferred_term` or `notes`.
- Investigate whether JCM J460 has moved, been withdrawn, or needs an archived/source note because GRMD 460 is no longer served by JCM.
- Decide whether the JCM J460 agar form should remain a `SOLID_AGAR` record or be split from a fluid no-agar base recipe.

## Follow-up Checks

- After minor edits, rerun open-schema, strict, reference, and term validation on the generated JCM J460 YAML.
- Confirm Resazurin remains at 0.001 `G_PER_L` and pH remains 7.1.
- Confirm no erroneous small-molecule grounding is added for Trypticase peptone or Yeast extract.

## Additional Notes

- No composition, pH, preparation, or stock-boundary defect was found in the MediaDive J460 payload.
