# OTEB Ingredient Review

**Six-record preview, not applied curation or all-record completion.**
The normalized scope remains all 15,910 records. No OTEB recipe YAML has been
changed by this batch, and its proposed evidence is not part of cumulative
applied counts.

## Evidence And Proposal

`context.json` freezes six exact tracked paths, their permanent IDs and full
before-text, the reviewed commit and corpus hash, and seven official captures.
It also pins the earlier source inventory, twelve passing baseline commands,
old-slot inventory and source coverage. The original DSMZ1245 PDF's two pages
were visually inspected, including the repeated maltose rows and volume text.

`source-review.json` makes explicit decisions for 126 API/KOMODO table rows,
30 original-PDF rows and nine metadata/procedural claims. It preserves unknown
denominators, percentage bases and chemical forms instead of estimating them.
`plan.json` freezes **449 claims**, **127 ingredient/stock nodes** and all
**115 prior quantity fields**. The proposed additions are **154 evidence
entries, nine references and six history events**; these are preview counts.
Every scientific edit carries a persistent source URL and an exact excerpt in
the proposed YAML itself. Authors and publication years remain unknown when
the source supplies none. No organism-growth association is proposed.

The preview uses source-specific KOMODO displayed Gram Amounts and nulls,
restores the original medium's stock/preparation boundaries, and repairs liquid
input units. It keeps the serum identities and duplicate maltose ambiguity
explicit. Existing API-qualified standalone concentrations are not upgraded
to independently measured final concentrations. Fifteen earlier supported
evidence entries remain unchanged.

## Checks

- `audit.json`: independent source projection passes for all six proposals,
  including every old amount, exact source row, evidence link and history item.
  The auditor neither imports nor executes the repair builder.
- `cached.json`: **180/180** reference checks pass against seven hash-checked
  official captures, with network disabled. This is not a new live refresh.
- `presentation.json`: 48 unchanged root metadata spans and all 45 prior
  history text spans are preserved.
- `ledgers.json` and `records/*.md`: six proposal ledgers supplement the six
  existing exact-path reports; they intentionally use `Follow-up target` rather
  than creating duplicate canonical `Record` markers.
- `focused.json`: **495 tests pass**, with lint, formatting and whitespace
  checks also passing.
- `schema-preview.json`: all twelve command-line schema/strict checks pass
  against the six exact preview files, without altering authoritative YAML.

`validation-preview.json` consolidates the completed preview gates and pins
their receipts, source context, code, ledgers and six existing canonical reports.
The preview is ready for guarded application after the preceding pinned
checkpoint finishes; actual readback and post-edit gates remain required.

The broader medium-829 fast-tier rerun is a separate in-progress checkpoint.
No normalized YAML is changed while that pinned run is live. Its historical
global merge/freshness failures are not cleared by this preview.

See [source conflicts](issue-source-conflicts.md),
[adversarial review](adversarial-review.md) and [remaining work](next-work.md).
No commit, push, public issue, PR, merge or branch cleanup occurred here.
