# Halobacteria Ingredient Review

The reviewed successor is **applied locally to all five records**, not a
completed corpus review. Guarded application, independent readback and no-op
checks pass. The active
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
evidence-linked claims**, adding **94 evidence entries, eleven references
and five history events**. `apply.json` verifies that only these five normalized
records changed and that the written output matches the reviewed proposal.

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

The independent audit passes all five proposals and their actual written
results. The historical preview has **103 focused-test passes**.
The terminal `validation-preview.json` records twenty passing baseline/proposal
schema/strict commands, five passing reference CLI commands and **105 of 105
captured-source reference checks**. Ruff and Black pass. The ignored-inclusive
15,910-record corpus hash remained unchanged during those preview checks.
These are isolated preview checks
in the existing partial Python 3.13 environment, not clean CI or an applied
full-suite result. The old
`plan.json` remains immutable. Its ordered preparation steps were removed in
the successor because the source does not establish every relative step order.

The builder now pins the reviewed proposal and terminal reference/test receipt,
checks every referenced validation log, and delegates target identity, schema,
concurrent-edit and no-op protection to the established guarded writer.
**332 focused tests pass** with the application code, including altered-plan,
receipt, log, symlink and concurrent-edit attacks. The first application-focused
attempt stopped at Black's formatting check; its receipt is retained and the
corrected successor is `focused-v2.json`. Original preview code and documents
are archived without rewriting their receipts.

The corpus hash after application is
`4c2df727dbf13031b4473181f389ab53b3fa59f048abbec823a314bba3a5bd94`.
All ten actual-written schema/strict commands, five reference CLI commands and
105 supported reference checks pass. Corpus strict validation scans all 15,910
records; ID, product and presentation checks pass. Product checking reports
91 non-blocking warnings and 96,007 no-adapter skips, not complete ontology
verification. Report reconciliation verifies 5,268 cumulatively edited records,
36,049 added evidence entries and 11,805 exact follow-up paths, leaving 4,105
outside the reports. Report presence does not certify every concentration.
Three generated indexes change for two metadata records. All five reviewed
targets retain their claims through runtime merging; no derived YAML is written.
All **260 final QA tests** pass, along with Ruff, Black and whitespace checks.
The current fast tier passes **12,701 tests**, with 16 skipped, 2,962 deselected
and two dependency warnings in 1,664.48 seconds. The 117 family tests are
classified as corpus-tier by the existing collection rules and pass separately
within the focused and QA runs. The terminal applied checkpoint is recorded in
`validation.json`; it is not clean CI or full-suite certification. Global merge
verification still reports 1,247 name conflicts and 3,287 fingerprint issues.
Freshness also fails: 6,320 tracked versus 10,781 fresh records, with 4,275 only
tracked, 8,736 only fresh, 2,045 changed and none unchanged. Neither failure is
waived or represented as a pass.
The five per-record Markdown ledgers in `records-preview/` link each claim to
its exact record path, source URL and snippet. `preview-ledgers.json` records
their hashes and excludes them from canonical follow-up coverage. They are
immutable historical preview reports, not additional applied changes.

The twelve related records in `next-variants-source-inspection.json` remain
unchanged. Their 117 existing quantity fields have source-linked dispositions:
sixteen corrections, 76 evidence-only candidates, seven unquantified inputs,
nine M1212 preparation-scope conflicts and nine JCM1132 source-access gaps.
Those are review inputs, not additional applied counts or complete reviews.
The later `next-variants-stage-adjudication.json` retains that first inspection
and adds a captured MediaDive J1132 export plus the original JCM page's negative
response. It distinguishes the 1 L prepared-base input from the later pH
adjustment and adds existing preparation S3823 to the next review, for thirteen
unchanged records and 127 old quantity fields. The JCM original remains
unavailable; the provider dataset is not represented as that original source.

## Primary Sources

- [JCM168](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=168)
- [JCM1007](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1007)
- [TOGO M159 API](https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M159)
- [TOGO M160 API](https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M160)
- [TOGO M1064 API](https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1064)
