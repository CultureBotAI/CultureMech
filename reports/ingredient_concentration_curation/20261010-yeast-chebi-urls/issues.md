# Citation Repair Dispositions

- Resolved: eighty live encoded-colon ChEBI reference fields in four records.
  Forty evidence and forty bibliography fields now use verified canonical URLs.
  The live comparison records eighty newly passing checks and no regressions.
- Retained: 94 snippet retrieval failures, split equally between abstract-only
  and unavailable-content results. They are not treated as scientific rejection
  or automatic validation success; primary PDF checks remain separate evidence.
- Retained: merge verification and derivation freshness failures. The temporary
  regeneration differs from 15,056 tracked/generated paths; no derived corpus
  was overwritten to hide that drift.
- Pending at the applied checkpoint: current-code full fast tier and publication
  workflow. Historical test runs do not certify subsequently added code.

See [checkpoint](applied-checkpoint.json), [reference comparison](reference-reconciliation.json)
and [corpus commands](corpus.json). This is a local issue ledger, not a GitHub issue.
