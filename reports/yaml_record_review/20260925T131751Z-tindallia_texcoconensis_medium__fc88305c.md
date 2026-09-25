# YAML Record Review: tindallia_texcoconensis_medium__fc88305c

- Repository: CultureMech
- Record: `data/merge_yaml/merged/tindallia_texcoconensis_medium__fc88305c.yaml`
- Started UTC: 2026-09-25T13:17:51Z
- Finished UTC: 2026-09-25T13:17:51Z
- Verdict: needs curation

## Target

Reviewed generated merged YAML for JCM medium J543, `TINDALLIA TEXCOCONENSIS MEDIUM`.

The generated record is a single-source merge from `data/normalized_yaml/bacterial/tindallia_texcoconensis_medium.yaml`.

## Validation

- LinkML schema validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed with 0 errors; the TSV contained only the header row.
- Reference validation: Passed with 0 checks.
- Term validation: Passed; the only diagnostic was the known eutils/pkg_resources startup warning.
- Embedded curation history: Not checked; the available history validator targets standalone `history/` records, not `MediaRecipe.curation_history`.

## Identity and Grounding

The medium identity is grounded to JCM medium 543 by `media_term.term.id: mediadive.medium:J543` and the JCM link in `notes`.

The JCM page defines Solution A, Solution B, a 10 ml trace minerals addition to Solution A, and two final pre-inoculation additions from sterile 5.0% stocks.

## Evidence

The source gives Solution A in 700 ml distilled water with 10 ml trace minerals from JCM medium 151, Solution B in 300 ml, and combines A and B to complete a 1 liter base. It then adds 0.5 g/L final L-cysteine x HCl x H2O and 0.4 g/L final Na2S x 9H2O before inoculation.

The generated record has the trace-mineral rows but lacks the explicit final L-cysteine and Na2S ingredient rows.

## Completeness

No target organisms are present; that empty optional field is not a defect in this formulation review.

The generated ingredient list does not preserve the JCM two-solution assembly, and it omits two final reducing-agent additions that are explicitly required by the source.

## Findings

- Major issue: Solution A amounts were converted using the 710 ml Solution A working volume instead of the final A plus B liter. NaCl therefore became 105.634 g/L before trace-stock duplicate merging, instead of the source-backed 75 g/L per completed liter.
- Major issue: Solution B amounts were converted using the 300 ml Solution B stock volume instead of the final A plus B liter. NaHCO3 is recorded as 66.6667 g/L and Na2CO3 as 10 g/L, while the completed liter receives 20 g NaHCO3 and 3 g Na2CO3.
- Major issue: the required 0.5 g/L final L-cysteine x HCl x H2O and 0.4 g/L final Na2S x 9H2O additions are missing from `ingredients`; they are mentioned only in free-text preparation.
- Major issue: trace minerals from JCM medium 151 are flattened into the parent medium at stock concentrations rather than represented as a 10 ml component addition.

## Recommended Edits

- Preserve Solution A, Solution B, and trace minerals as nested components or calculate all ingredient amounts against the final completed liter.
- Add explicit final L-cysteine x HCl x H2O and Na2S x 9H2O ingredient rows at 0.5 g/L and 0.4 g/L.
- Prevent duplicate cleanup from adding trace-mineral salts into parent-medium salts across component boundaries.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after editing the normalized source YAML and regenerating the merge.
- Reconcile JCM medium 151 trace mineral hydration labels against the source before assigning or changing CHEBI IDs.

## Additional Notes

Exact local source search found only the expected normalized JCM source for `tindallia_texcoconensis_medium`. Ignored files were included for duplicate-report checks with `find`, and no pre-existing ignored report for this generated record was found.
