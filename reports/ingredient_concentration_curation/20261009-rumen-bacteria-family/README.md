# Rumen Bacteria Ingredient Review

**Thirteen normalized records are applied locally. The all-record goal is not
finished and still covers all 15,910 normalized records.**

The [proposal](plan.json) contains 717 evidence-linked claims covering all 187
old quantity fields and 214 ingredient/stock nodes. Independent applied
readback confirms **214 evidence additions, 15 bibliography entries and thirteen
curation events**. Guarded application changed only the thirteen intended YAML
files; verification and no-op pass. Current claim ledgers are in
`applied-records/`. Historical `records/`, `preview-documents/` and
`validation-preview.json` remain immutable, not duplicate canonical reports.

## Scientific Decisions

- Restore each KOMODO table's exact displayed rates, precision and nulls.
  The DSM17630 variant changes sixteen rates and adds rumen fluid at the
  provider's 29.13 g/L. This is not a density conversion of DSMZ's 30 ml/l.
  Replace unsupported exact-duplicate relationships with source derivation
  and strain-specific variant relationships.
- DSMZ330 explicitly states nominal final volume 1003 ml. Eleven main mass
  rates use 1.003 L and six-significant-digit arithmetic, not measured
  precision. Listed liquid inputs sum to 1003.6 ml; do not replace the stated
  denominator or assume volume additivity.
- Keep mineral stock batch masses without an explicit final denominator in
  notes. Preserve acid liquid input volumes. Hemin stock is made up to 100 ml;
  do not add another fixed 100 ml water. Keep reagent strengths, stock doses
  and final-medium concentrations distinct.
- JCM1029's live original recipe is unavailable. DJ1029 and TOGO M1093 use
  inspected dataset evidence with exact batch inputs and explicit limitations.
  MediaDive standalone rates remain qualified provider assertions, not new
  original-methods verification.
- M1093 explicitly links M124, which identifies JCM133. Only the seven VFA
  stock rows are imported; the other 24 Medium10 table rows are excluded.
- Preserve all thirteen old evidence entries at their existing paths. Stock607
  metadata corrections use the inspected parent dataset's explicit id/name
  and identical non-null recipe rows, preserving its six old evidence entries.
- Remove false LB expansions and placeholders. Withdraw copied sodium-salt
  groundings where KOMODO says only Resazurin; do not invent replacement IDs.
  Other existing chemical annotations are preserved, not recertified.

Every applied scientific change has a persistent source URL and literal
snippet in the YAML. Unknown authors, publication years and scientific
bases remain unknown. No organism-growth association is added.

## Checks

- `audit.json`: independent projection accounts for all 214 nodes and 187 old
  quantity fields without importing the builder.
- `references.json`: 245/245 checks pass using sixteen hash-checked official
  captures with networking disabled. This is not a new live refresh.
- `presentation-applied.json`: 98 unchanged root spans, 99 prior history text
  spans and all thirteen prior evidence entries and paths are preserved.
- `schema.json`: all 26 preview schema/strict commands pass.
- `focused-v2.json`: 700 tests pass with two dependency warnings, including
  guarded application, readback, no-op, concurrent modification and tampering.
  Historical `focused.json` retains the 695-pass disabled-application result.
- All 39 post-edit schema/strict/reference commands pass. Corpus strict
  validation scans 15,910 records; ID and product gates pass. Product checks
  retain 91 warnings and 96,003 no-adapter skips, not chemistry recertification.
- `qa.json`: 101 regression tests, lint, formatting and whitespace checks pass.
- Seven maintained indexes are refreshed. Runtime merge checks retain all
  seven medium-shaped targets and exclude six standalone solutions; no derived
  merged YAML was written.
- `fast.json`: the current full fast tier passes **12,698 tests**, with 16
  skipped, 1,980 deselected and two dependency warnings in 1,745.93 seconds.
  Its code and normalized-corpus hashes are unchanged throughout the run.
- [Terminal validation](validation.json) consolidates every result, including
  the failed global merge verification and freshness gates. The merge check
  reports 1,247 name conflicts and 3,287 fingerprint issues; temporary fresh
  generation produces 10,781 records versus 6,320 tracked merged files.

The existing partial locked Python 3.13 environment is not clean CI or full-suite
certification. [Cumulative accounting](cumulative-audit.json) is **5,255 edited
records and 35,651 added evidence entries**. Exact follow-up coverage is
**11,802 of 15,910**, leaving **4,108** outside these reports. Report presence
does not certify every concentration. Twelve existing canonical reports were
updated and one was added for M1093; each target has exactly one canonical report.
Global merge verification/freshness and publication remain unresolved. See
[source conflicts](issue-source-conflicts.md), [adversarial review](adversarial-review.md)
and [next work](next-work.md).
