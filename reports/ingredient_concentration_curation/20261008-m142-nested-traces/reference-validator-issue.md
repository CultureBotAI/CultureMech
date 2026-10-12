# Official Recipe Evidence Is Rejected by Reference Validation

Related concentration-repair tracking: #150. This is distinct from #565's
source-check-to-ingredient binding defect.

## Reproduction

Observed on 2026-10-08 in the local concentration-curation worktree at baseline
`f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`, with
`linkml-reference-validator==0.1.6` and Python 3.13. The new curation records and
reports are not yet committed or published; the underlying public source and
matcher examples below do not require those record edits.

1. **Literal brackets are stripped as though they were citations.** For
   `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1124`, the
   source JSON names `Trace vitamins (see Medium [M190])`. An exact JSON snippet
   including that label and its 10 ml dose is rejected. The error instead
   searches for `Trace vitamins (see Medium  )`.
2. **HTML chemical subscripts change excerpt matching.** At
   `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1084`, the exact rendered-text
   excerpt `40.0 g FeSO4·7H2O in 0.1 N H2SO4 solution and fill up to 100.0 ml.`
   fails the installed matcher. At JCM1282, `8% (w/v) NaHCO3 solution` also fails.
   Both match whitespace-normalized text extracted from the captured source
   HTML with BeautifulSoup. The chemical numbers must not be discarded.
3. **JSON dataset titles fall back to the URL.** For the TOGO M1153 endpoint,
   the verified `meta.name` is `Thiobacillus Prosperus Medium`. Reference
   validation instead extracts the URL as the title and rejects the correct
   supplied title. The same occurs for M142's `Pyrococcus Medium` and other
   receiving datasets.

The public-source snippet checks can be reproduced using
`SupportingTextValidator(ReferenceValidationConfig(cache_dir=...)).validate(snippet, url)`.
Use a fresh cache to distinguish parser behavior from stale cached content.

## Impact and Evidence

The seven-record nested-stock review adds 206 primary evidence entries.
All 206 snippets are literal matches to hash-pinned HTTP-200 captures; the
installed matcher accepts 200 and rejects six. All seven
`just validate-references <record>` commands fail, also including API title
mismatches. Independent literal checks are not represented as an automated
reference-gate pass.

Local reproducibility artifacts are under
`reports/ingredient_concentration_curation/20261008-m142-nested-traces/`:
`context.json`, `plan.json`, `reference-validation.json`, `audit.py`, and one
report per exact record path. No source quote was rewritten to hide a failure.

## Acceptance Criteria

- Preserve literal accession brackets in structured-source snippets; do not
  treat `[M190]` as removable Markdown citation syntax.
- Normalize HTML presentation of chemical subscripts consistently without
  losing formula digits, hydrate numbers, signs, units or decimal precision.
- Extract or explicitly support structured recipe titles from the official
  API metadata instead of comparing a verified title with a URL fallback.
- Add fixture-backed positive and negative regressions. Wrong ingredient,
  amount, unit, stock/final scope and title must still fail. Avoid a broad fuzzy
  matcher or disabling title/snippet checks to turn the gate green.
- Re-run the seven records and representative earlier JCM/TOGO cohorts; retain
  distinct reporting for source-access failure, unavailable metadata, a parser
  limitation and a genuine contradiction.

The corpus-wide merge/freshness failures are separate publication blockers.
