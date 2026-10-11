Local ingredient-repair progress for #150, not a completion or publication claim:

- Applied the guarded M689 / JCM670 repair (`CultureMech:010094`): four stock
  additions corrected from g/L to ml/L, the four named stock compositions
  expanded at the correct preparation stages, and the acid dose kept separate
  from its explicit reagent molarity.
- Withdrew four unsupported final-medium mass rates while preserving the source
  batch amounts, including resazurin 0.5 mg. Replaced gas/titrant quantity
  placeholders with source-backed atmosphere/pH context. No final volume,
  percentage basis, density, chemical grounding or growth association is inferred.
- Every scientific change has a source URL and literal excerpt in the YAML.
  All eight refreshed official responses match the inspected captures. The
  revised record passes 50 excerpt checks and eight title checks, schema and
  strict validation; guarded verify/no-op and the independent source audit pass.
- 324 focused tests and 8,278 fast-tier tests pass (16 skipped, 1,945 deselected
  in the fast tier; no clean full-suite/CI rerun claimed). Full-corpus merge routing retains the reviewed
  formulation and provenance in a schema-valid generated group. Global merge
  verification still fails with 1,247 name conflicts and 3,287 fingerprint issues.
  Freshness also fails: 6,320 tracked versus 10,777 fresh outputs, 2,045 changed
  shared paths, 4,275 tracked-only, 8,732 fresh-only and zero unchanged. These
  unresolved counts match the preceding pass.
- The cumulative independent audit now covers 5,135 edited records, 31,218
  evidence entries, 5,504 references and 5,339 curation events. Evidence totals
  are not counts of new final concentrations or taxa-media associations.
- The remaining M142-dependent queue has 90 unchanged baselines. Follow-up
  report coverage is 11,762/15,910 normalized paths; the other 4,148 paths remain
  outside this report set, and report presence does not certify all claims.

Artifacts are local and uncommitted under
`reports/ingredient_concentration_curation/20261008-m689-stocks/`, including the
canonical M689 report, source captures, plan, independent audit, self-review,
test/gate results and an inspected M809 preparation-boundary handoff. No PR has
been merged or branch deleted. Keep this issue open: the full corpus goal and
publication gates remain unresolved.
