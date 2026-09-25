# YAML Record Review: flexistipes_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/flexistipes_medium__94d1aaba.yaml
- Started UTC: 2026-09-23T03:34:08Z
- Finished UTC: 2026-09-23T03:35:21Z
- Verdict: pass with minor issues

## Target

- Reviewed generated MediaRecipe `CultureMech:001656` / `flexistipes_medium`, the DSMZ 524 import for FLEXISTIPES MEDIUM.
- Cross-checked the generated record against the DSMZ Medium 524 PDF and the MediaDive REST payload for medium 524.
- Compared the generated merge with its normalized source at `data/normalized_yaml/bacterial/flexistipes_medium.yaml`.

## Validation

- LinkML open-schema validation: pass.
- Strict CultureMech validation: pass; `/private/tmp/flexistipes_medium_94d1aaba.strict.tsv` contains only its header row.
- LinkML reference validation: pass; 0 external reference checks.
- LinkML term validation: pass.
- Embedded curation history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding

- The DSMZ identity is coherent: `mediadive.medium:524`, the FLEXISTIPES MEDIUM label, and the DSMZ Medium 524 URL all agree with MediaDive and the DSMZ PDF.
- Most defined salts have appropriate CHEBI groundings.
- `Na-meta silicate` is ungrounded.
- `KNO3` still has a legacy `mediaingredientmech_term` identifier rather than an id-safe CHEBI mirror.
- Yeast extract is an ungrounded complex ingredient; that is acceptable.

## Evidence

- DSMZ 524 and MediaDive 524 both assert the same flat 17-row main recipe; no nested stock formula is present.
- The generated file preserves the expected g/L amounts, including 12 mg/L Na-meta silicate as 0.012 g/L, 7 ml of 0.1% NaF as 0.007 g/L, and 0.5 ml of 0.1% Sodium resazurin as 0.0005 g/L.
- `ph_value: 6.5` agrees with the final complete-medium pH in DSMZ and MediaDive.
- The generated preparation text preserves the source instructions to adjust pH to 6.0-6.2 before autoclaving, sparge under 100% N2, add bicarbonate/yeast extract/nitrate/sulfide from sterile anoxic stock solutions, and adjust the complete medium to pH 6.5.
- The 0.1% source attributes for NaF and Sodium resazurin are not retained in the generated rows even though their final masses were calculated correctly.

## Completeness

- Ingredients, pH, anaerobic preparation, medium identity, and source URL are present.
- No source-specific target organism was asserted in this DSMZ import; target organism coverage was not evaluated for this direct medium review.
- No source nested stock recipe needs a `solutions` entry in this generated record.

## Findings

- Minor issue: `Na-meta silicate` is ungrounded.
- Minor issue: KNO3 still uses a legacy MediaIngredientMech ID.
- Minor issue: the 0.1% w/v source attributes for NaF and Sodium resazurin were dropped after conversion to final g/L masses.

## Recommended Edits

- Ground `Na-meta silicate` if a precise local or ontology mapping exists.
- Replace the KNO3 legacy MediaIngredientMech mirror with an id-safe CHEBI mirror.
- Preserve the NaF and Sodium resazurin 0.1% w/v stock attributes in `preferred_term` or `notes`.

## Follow-up Checks

- After minor edits, rerun open-schema, strict, reference, and term validation on the generated DSMZ 524 YAML.
- Confirm the NaF and Sodium resazurin rows remain at their calculated final g/L concentrations.
- Confirm the anaerobic preparation instruction remains a single coherent source-backed step.

## Additional Notes

- No composition, pH, preparation, or stock-boundary defect was found in this DSMZ 524 record.
