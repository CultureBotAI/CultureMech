# KOMODO concentration review, pending paths 1000-1499

This is a bounded batch within the unfinished all-record objective. The frozen
[plan](plan.json) covers 500 exact tracked normalized paths: 227 base accessions
and 273 strain/variant accessions. All 500 have [per-record results](records),
including 454 unchanged records. These are concentration-source reviews, not
proof that every formulation, ontology mapping or variant is fully reconciled.

The independent [applied audit](diff-audit.json) verifies 46 evidence-only edits:
264 ingredient concentration entries, 46 separate identity-mapping entries,
92 references and 46 appended curation events. No quantity, unit, ingredient
identity, stock, variant, stable ID, growth claim or prior history was changed.
Each concentration addition includes its source URL and literal snippet in the
YAML. The mapping source establishes recipe identity, not amounts or growth.
Duplicate-source records are not independent scientific confirmations.

The [source inventory](source-captures.json) pins 227 endpoints: 193 accessible
responses and 34 actual HTTP 404 responses affecting 40 selected paths. A sandbox
DNS failure was retried with authorized network access; it was not counted as a
source 404. The unavailable endpoints remain unresolved, not empty recipes.

Scientific ingredient, preparation and source context was inspected for all
61 preliminary candidate records; complete before-records and source responses
are preserved in [the context snapshot](inspected-candidate-context.json).
Fifteen [source-pinned withholdings](withholdings.json) veto 97 preliminary
ingredient endorsements. The final plan retains 12,781 unsupported and 7,823
conflict rows. Those row counts include unresolved stock/variant context and
are not counts of independent concentration facts. The
[preparation findings](preparation-findings.md) explain these decisions and
the limited scope of accepted claims. Fifteen corresponding earlier DSMZ
records are captured in a read-only [prior-cohort handoff](prior-cohort-handoff.json);
their 97 existing same-source ingredient entries need preparation-scope review.
Neither those records nor their historical reports were rewritten here.

The [actual-group retention audit](merge-retention.json) checks all 46 edited
records in 45 groups and fails for seven distinct records; 39 pass every checked
field. Of 264 concentration claims, 257 retain the exact amount/reference/snippet/
field-scope match and 240 retain the complete evidence entry. Two records lose
amount quotes, four lose full entries, and six each lose mapping evidence,
references or curation events. These sets overlap. All additions remain intact
in authoritative normalized YAML; no evidence is copied across unverified
formulations to force retention to pass.

The [preflight](preflight.json), applied full-record inversion, literal-snippet
readback and zero-change rerun pass. The presentation comparison records 8,977
inserted lines with no removed lines or replacement blocks. The first baseline
attempt used an incorrect representative filename; [that failure](baseline.json)
is preserved alongside the successful [corrected retry](baseline-retry.json).
The retry passes all 15,910 records under strict validation and 162 pre-apply
guard tests. Post-apply focused runs pass 242 tests on isolated Python 3.11 and
165 on cached Python 3.13, with no errors, failures or skips. These are not
full-suite or CI passes. All 21 post-apply checks in
[validation.json](validation.json) are terminal: sixteen pass, two are unavailable
and three merge gates fail. Full strict validation passes all 15,910 records;
the representative schema, IDs, variant links, prior medium/solution/KOMODO
readbacks, semantic diff, exact-path coverage and whitespace checks also pass.
Black and Ruff pass for the updated KOMODO regression tests. Product and automated
reference checks are unavailable because `oaklib` and
`linkml-reference-validator` are missing.

Global merge verification reports 1,247 name conflicts and 3,287 fingerprint
issues. [Freshness](merge-freshness.json) fails with 6,320 tracked and 6,493
temporarily regenerated records: 3,719 only tracked, 3,892 only fresh,
1,665 changed and 936 unchanged. All 6,493 temporary groups were written;
no tracked merged output changed. Alongside the evidence-retention failure,
these results prevent a publication-ready claim.

Authoritative evidence remains in normalized YAML. No generated merge is
hand-edited or published, and no commit, PR or merge is claimed for this batch.
