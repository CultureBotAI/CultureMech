# Stock Review Dispositions

## Resolved Locally

- Scoped evidence is attached to the ten existing concentration claims. Nine
  are supported; the manganese amount/form claim remains explicitly partial.
- Three context notes no longer present unsupported micromolar annotations as
  established stock concentrations. Beijerinck's starting water is corrected
  from 900 mL to the source's approximately 800 mL before final makeup.
- Bibliography provenance and append-only history are present for each stock.

## Retained

- **Scientific conflict:** Bold Trace Stock prints MnCl.4H2O while the record
  assigns MnCl2.4H2O. Existing amount and identity are retained without claiming
  complete support. No silent formula correction is applied to the source.
- **Scientific conflict:** Bold Trace and Boron concentration annotations do
  not agree with their explicit stock preparations. No replacement molarity,
  density assumption or receiving-medium dilution is inferred.
- **Reference gate:** all thirteen snippets validate, but the three stored
  recipe headings differ from fetched titles containing the UTEX publisher
  suffix. The fetched Beijerinck title also contains an encoded apostrophe.
  Do not insert HTML entities into scientific metadata or broadly accept title
  substrings just to make this gate green. A separately tested title/source
  normalization follow-up is needed.
- **Derived corpus:** merge verification fails with 1,247 name conflicts and
  3,287 fingerprint issues. Freshness fails with 15,056 derivation differences;
  no derived files are overwritten to conceal drift.
- **Remaining cited sources:** other bibliography documents are uninspected
  leads for these exact stock formulations, not verified amount evidence.
- **Completed check:** current-code fast tier passes 15,565 tests, with sixteen
  skipped, 3,498 deselected and two dependency warnings. This does not resolve
  scientific conflicts or the failed reference and derived-corpus gates.
- **Publication:** commit, push, PR review and merge are not established by this
  local batch. The all-record goal remains incomplete.

See [reference results](references.json), [corpus results](corpus.json) and
[fast-tier results](fast.json), pinned by the [checkpoint](applied-checkpoint.json).
This is a local ledger, not a GitHub issue.
