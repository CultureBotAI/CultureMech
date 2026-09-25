# YAML Record Review: freshwater_r2a_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/freshwater_r2a_medium.yaml
- Started UTC: 2026-09-23T04:44:25Z
- Finished UTC: 2026-09-23T04:45:28Z
- Verdict: needs curation

## Target

- Reviewed generated MediaRecipe `CultureMech:015874` / `freshwater_r2a_medium`, the direct JCM GRMD=1468 import.
- Compared it with maintained source `data/normalized_yaml/bacterial/JCM_J1468_FRESHWATER_R2A_MEDIUM.yaml`.
- Cross-checked the live JCM GRMD=1468 page.

## Validation

- LinkML open-schema validation: pass.
- Strict CultureMech validation: pass with 0 error rows.
- LinkML reference validation: pass; 0 external reference checks.
- LinkML term validation: pass.
- Embedded curation history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding

- `jcm.grmd:1468` correctly identifies JCM Medium 1468, FRESHWATER R2A MEDIUM.
- Exact ignored-inclusive lookup for `jcm.grmd:1468`, `CultureMech:015874`, `JCM_J1468_FRESHWATER_R2A_MEDIUM`, and `freshwater_r2a_medium` covered normalized and generated YAML; it found this single maintained JCM J1468 owner, index entries for the owner, and the unsuffixed generated file.
- The generated file is stale relative to the maintained JCM owner: a September score-10 exact-term repair grounded Yeast extract (BD-Difco), Proteose peptone No. 3 (BD-Difco), and Casamino acids (BD-Difco) in normalized YAML, but the August generated merge lacks those terms.
- JCM cross-medium stock references to Medium 187, Medium 403, and Medium 431 are preserved only as `preferred_term` text, not as structured source links or nested solutions.

## Evidence

- The live JCM source lists 0.5 g/L Yeast extract, Proteose peptone No. 3, Casamino acids, Glucose, KH2PO4, Soluble starch, and Sodium pyruvate, plus 1.5 g/L NH4Cl, 0.5 mg/L Resazurin, 1 ml/L FeCl2 solution, 1 ml/L Trace element solution, 0.5 ml/L Selenite tungstate solution, and three 1 ml/L Medium 403 vitamin stocks.
- JCM 1468 lists Distilled water as 1.0 L, but the generated record imported that row as `1.0 ML_PER_L`.
- The live JCM source adds 5 ml/L 1 M NaHCO3 solution, 0.5 ml/L 1 M Coenzyme M solution, and 6 ml/L 5% Na2S x 9 H2O solution after cooling from anaerobic stocks; the generated record preserves those three post-autoclave rows as `ML_PER_L`.
- The maintained normalized owner has FOODON/MICRO term grounding for the three complex BD-Difco ingredients; the generated file predates that repair and leaves them ungrounded.

## Completeness

- The source water volume is not represented correctly because 1 L became 1 ml per L.
- The referenced Medium 187 FeCl2 and trace-element stocks, Medium 403 vitamin stocks, and Medium 431 Selenite-tungstate stock are not expanded or linked structurally.
- Recent normalized term grounding for three complex organic ingredients is absent from generated YAML.

## Findings

- Major: `Distilled water` has the wrong unit; the JCM 1.0 L source row is represented as `1.0 ML_PER_L`.
- Minor: the generated file is stale relative to the September normalized score-10 exact-term grounding for Yeast extract, Proteose peptone, and Casamino acids.
- Minor: cross-medium stock references remain free text, so the Medium 187, Medium 403, and Medium 431 dependencies cannot be followed structurally.

## Recommended Edits

- Correct the `Distilled water` row in the maintained JCM J1468 normalized record so 1.0 L is not emitted as `1.0 ML_PER_L`.
- Preserve the three September exact-term groundings when the generated record is rebuilt.
- Consider modeling Medium 187, Medium 403, and Medium 431 stock references as structured solution references instead of only parenthetical text.
- Regenerate `data/merge_yaml/merged/freshwater_r2a_medium.yaml` after normalized/import curation.

## Follow-up Checks

- After repair, rerun open-schema, strict, reference, and term validation on the generated JCM J1468 YAML.
- Confirm no `Distilled water` row says `1.0 ML_PER_L`.
- Confirm Yeast extract, Proteose peptone, and Casamino acids retain their repaired FOODON/MICRO term grounding in the generated file.
- Confirm the 5 ml/L NaHCO3, 0.5 ml/L Coenzyme M, and 6 ml/L Na2S x 9 H2O post-autoclave additions are unchanged.

## Additional Notes

- The generated file is derived data and is a one-source merge. The water-unit issue is present in the maintained direct JCM YAML; the missing exact-term grounding is a stale generated artifact.
