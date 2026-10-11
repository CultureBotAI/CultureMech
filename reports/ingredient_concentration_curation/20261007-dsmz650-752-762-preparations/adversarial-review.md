# Adversarial Review

This is a local self-review, not an independent human or external-agent approval.

## Addressed

1. **False stock concentrations and water percentages.** Source-explicit stock
   strengths, molar pyruvate and absolute input volumes replace flattened values.
   The mutator pins record/source hashes, IDs, exact git paths and old values.
   The independent audit checks source arithmetic and completely reconstructs
   every prior record, rejecting unrelated edits.
2. **Invalid final-volume inference.** Neither added water nor its sum with
   stock doses establishes a measured final litre. Carbonate stock concentration
   and dose remain unspecified. Regression tests reject invented 54 g/L and
   0.1 L stock claims.
3. **Erasing prior evidence.** All 32 earlier excerpts and explanations survive.
   Four carbonate concentration claims are explicitly withdrawn, with verified
   source-linked replacements. Earlier cohorts verify through the new resolutions,
   rather than silently treating historical claims as current assertions.
4. **Liquid/agar conflation.** Only the medium record explicitly classified as
   liquid is narrowed to the liquid branch. The standalone solution retains
   the conditional agar instructions. Tests reject both opposite mistakes.
5. **Nonportable testing and incomplete report rows.** Historical-cohort tests
   reconstruct source caches under their temporary fixtures. Follow-up reports
   explicitly list unchanged concentration claims, not just their new scope notes.

## Open

1. **Merge evidence loss, publication-blocking.** Actual current groups do not
   retain the three DSMZ records' full evidence, bibliography and events. The
   merger selects a canonical record and an ingredient list rather than merging
   claim-scoped provenance. Group 650 also includes a strain-modified recipe.
   Do not append evidence to a different concentration or preparation merely to
   pass retention. Resolve formulation/variant identity before publishing a merge.
2. **Reference metadata checks fail.** All six full reference checks fail on
   the API fetcher's URL-as-title fallback. All 52 snippets separately match
   retrieved/cached content. Snippet matching does not excuse the failed gate,
   and replacing descriptive source titles with URLs would not establish truth.
3. **Global merge/freshness gates fail.** Merge verification reports 1,247 name
   conflicts and 3,287 fingerprint issues. Freshness reports 6,320 tracked versus
   6,495 fresh files: 3,720 only tracked, 3,895 only fresh, 1,683 changed and 917
   unchanged. Terminal outcomes are recorded in validation.json and
   merge-freshness.json, not inferred from the six-record source checks.
   Generated artifacts are not manually edited to conceal mismatches.
4. **All-record coverage remains incomplete.** Five thousand three hundred
   normalized paths are outside these reports; previously reported unsupported
   claims, chemical grounding and variant links are not globally resolved.

No GitHub issue or PR mutation is claimed. No paid source retrieval or author
contact was performed.

## Final Checks

The focused suite passes 264 tests and the fast suite passes 7,557 tests (16
skipped, 1,839 deselected). Source readbacks, complete-record inversion, report
coverage, schema, strict corpus, IDs, historical-cohort verification, cumulative
diff, Black, Ruff and diff whitespace checks pass. These results do not override
the open publication failures above.

Product validation initially failed on sandbox FoodOn-cache access. After that
process was terminal, an authorized retry refreshed the public cache and passed
without disabling adapters: 91 warnings and 96,051 no-adapter skips remain.
Both outcomes are retained in the artifacts. The runtime was partial locked
Python 3.13, not full CI.
