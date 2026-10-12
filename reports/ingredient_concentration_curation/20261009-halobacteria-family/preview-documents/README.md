# Halobacteria Ingredient Review

This is an **unapplied five-record preview**, not a completed corpus review.
All five authoritative YAML files remain byte-exact unchanged. The active
objective still covers all 15,910 normalized records. Local HEAD is
`f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`; upstream was not refreshed.

## Sources And Scope

The exact records are JCM168, JCM1007, TOGO M159, M160 and M1064. The two JCM
pages and three TOGO API responses are captured with URLs, response hashes,
retrieval timestamps and source accessions. Initial sandbox network failures
remain preserved separately from the successful public-source GETs. No
repository content was sent and no GitHub action was performed.

The source inspection accounts for **51 existing quantity fields**, with
24 packaged MIM lookups. The reviewed successor is `plan-v2.json`, SHA256
`53bccdac789d6ff3e8cbb3df230fa241d0da39b21ed2acc5b11fd2367b7036be`.
Independent projection covers **55 output ingredient/stock nodes and 171
evidence-linked claims**, proposing **94 evidence entries, eleven references
and five history events**. These are not applied cumulative additions.

## Decisions

- Six TOGO iron/manganese chloride quantities use the JCM table's milligrams
  per explicit one-liter final preparation, not grams per liter. Salt hydration
  states and existing chemical mappings are preserved.
- Water is make-up to a one-liter final volume, not a fixed one-liter water
  input and not one gram per liter. Three false water concentrations are
  withdrawn; the two JCM records gain the omitted unquantified water input.
- JCM1007 gains the omitted sodium pyruvate at the explicit 1 g/L rate and
  the sterile sodium carbonate solution used to reach pH 8.0. Neither the
  carbonate stock strength nor a numerical dose is invented.
- Modified-medium magnesium uses the source-stated **1 g/L final target**,
  corroborated by TOGO M1064. The source's word "supplemented" is in tension
  with the base's 20 g/L. This preparation ambiguity remains explicit; neither
  a 21 g/L sum nor a claim that literal addition can lower the rate is made.
- Preserve pH 7.0-7.2 for the base and pH 8.0 for the modified formulation.
  Do not replace the base range with its midpoint. Agar belongs only to the
  reviewed solid M160 formulation.
- JCM1007 is derived from JCM168, not its exact duplicate. Correct only this
  reviewed reciprocal relationship and its stale category paths. Other
  linked variants remain outside this five-record source decision.
- Retain `high_metal`: its schema definition includes sodium and potassium,
  not only trace metals. Repairing the iron/manganese units does not justify
  withdrawing this flag from a recipe containing 200 g/L sodium chloride.

Source authors and publication years are not supplied. Copyright years are
not publication dates. Evidence uses inspected persistent source URLs, not an
invented DOI. Existing strain-growth assertions and historical events remain
unchanged; no taxa-media association is added.

## Validation And Limits

The independent audit passes all five proposals, and **103 focused tests pass**.
The terminal `validation-preview.json` records twenty passing baseline/proposal
schema/strict commands, five passing reference CLI commands and **105 of 105
captured-source reference checks**. Ruff and Black pass. The ignored-inclusive
15,910-record corpus hash remains unchanged. These are isolated preview checks
in the existing partial Python 3.13 environment, not clean CI or an applied
full-suite result. The old
`plan.json` remains immutable. Its ordered preparation steps were removed in
the successor because the source does not establish every relative step order.

The builder deliberately rejects apply and verify modes. Guarded application,
actual-written validation, cumulative/report reconciliation, indexes and merge
checks are still required. Do not add the proposed evidence to applied totals.
The five per-record Markdown ledgers in `records-preview/` link each claim to
its exact record path, source URL and snippet. `preview-ledgers.json` records
their hashes and excludes them from canonical follow-up coverage. They are
preview reports, not applied changes.

## Primary Sources

- [JCM168](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=168)
- [JCM1007](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1007)
- [TOGO M159 API](https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M159)
- [TOGO M160 API](https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M160)
- [TOGO M1064 API](https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1064)
