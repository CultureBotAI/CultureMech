# KOMODO concentration review, first 500 pending paths

This is a bounded batch within the unfinished all-record objective. The frozen
[plan](plan.json) selects 500 exact normalized-record paths. The independent
[post-apply audit](diff-audit.json) verifies applied evidence-only edits to 25 records:
137 ingredient concentration entries and 25 separate source-identity entries,
50 bibliography entries and 25 appended curation events. It independently
inverts the full records and checks source arithmetic. No existing quantity,
ingredient identity, stock, variant, growth claim or prior history is changed.
All 500 paths have [per-record results](records), including 475 unchanged records.
The [preflight](preflight.json), guarded readback and zero-change rerun pass.

The [KOMODO inventory](../20261007-komodo-source-inventory.json) pins the actual
mapping-table HTML. Its original capture and the live recheck were byte-identical.
Exact base accessions are matched to the official DSMZ recipe link, then to
the independently captured MediaDive amount response. A name resemblance,
fingerprint, parent link, or SOURCE_DUPLICATE annotation cannot authorize a
variant's concentrations. Mapping evidence is explicitly identity-only.

The [source review](preparation-findings.md) records three withheld candidates
and other unresolved scientific gaps. One endpoint returned HTTP 404 and gets
an unchanged unsupported result. Source authors/publication years are not
invented; bibliography notes distinguish dataset source, discovery mode,
retrieval date, source hash and original recipe link. These are persistent-URL
evidence entries, not newly discovered DOI-backed experiments.
Source-duplicate records are not independent scientific confirmations.

The [actual-group retention check](merge-retention.json) fails: 117 of 137
amount/reference/snippet/field-scope matches survive, and only 103 complete new
evidence entries survive. Four records lose amount quotes. Eight lose complete
entries, eight lose mapping evidence, eight lose bibliography and eight lose
curation events; those sets overlap but are not identical. Nine records fail
at least one retention check, and sixteen pass all checked fields. All new
entries remain intact in the authoritative normalized YAML. Retaining a quote
does not establish exact formulation equivalence of a concentration-independent
merge group, and evidence is not copied across groups to force a pass.

Validation and application are recorded in [validation.json](validation.json).
All three baseline jobs and fifteen post-apply jobs are terminal. The 908 focused
tests pass with zero errors, failures or skips. Full strict validation passes
all 15,910 normalized records, as do canonical IDs, guarded apply/readback/no-op,
independent full-record inversion, source-snippet checks and exact-path coverage.
Black, Ruff and `git diff --check` pass. Product and automated reference
validation cannot pass without `oaklib` and `linkml-reference-validator`.
Global merge verification fails with 1,247 name conflicts and 3,287 fingerprint
issues. [Merge freshness](merge-freshness.json) fails with 6,320 tracked and 6,492
fresh records: 3,719 only tracked, 3,891 only fresh, 1,649 changed and 952 unchanged.
Together with the retention failures above, these prevent a publication-ready
result. Validation uses isolated Python 3.11, not maintained Python 3.13 or CI;
the full repository suite was not rerun. No generated merged records are
hand-edited or published. No commit, PR or merge is claimed for this batch.
