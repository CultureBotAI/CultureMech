# Medium-119 Family Ingredient Review

The complete nineteen-record repair preview is validated, but **not applied**.
No normalized records have been changed by this batch yet. The broader
15,910-record objective remains open.

The immutable context is copied from the Allisonella next-family handoff. Its
23 source captures include four original DSMZ PDFs (nine visually inspected
pages), four MediaDive API records and fifteen exact-accession KOMODO tables.
The original preflight and visual receipts remain in that handoff directory.

All nineteen baselines have now been read, including lossless comparisons of
the thirteen underscore variants against their identical copied ingredient list.
KOMODO 119_1224 explicitly reports pH 7.0; 119_15163 reports 6.0. The eleven other
underscore variants report null pH, not the copied 7.6 in their normalized YAML.

The [frozen proposal](plan.json) contains **3,095 claims**, accounting for all
**633 old quantity slots** and **650 source/input nodes**. Its proposed additions
are **847 evidence entries, 57 references and nineteen history events**. These
must not be added to cumulative applied totals yet. All nineteen per-record
ledgers under `records/` explicitly identify their unapplied state.

All **1,187 focused tests** pass (two dependency deprecation warnings), including
the corrected source-label expectation recorded in [adversarial review](adversarial-review.md).
All **38 baseline schema/strict commands** and **904 offline reference checks**
pass. The independent source projection, deterministic rebuilds, temporary-repo
write/readback/no-op/concurrency tests, lint and formatting also pass. Offline
reference checks use hash-verified captures; they are not a new live refresh.
See [consolidated preview validation](validation-preview.json) for the receipts
and unchanged 15,910-record corpus hash. This is not clean CI or a fast-tier run.

The proposal preserves source disagreements, separates stock and medium stages,
and provides PURLs and literal supporting snippets for scientific changes.
[Source conflicts](issue-source-conflicts.md) remain explicit. The
[next-work handoff](next-work.md) retains guarded application, post-edit record
and corpus gates, generated indexes, merge retention/freshness, fast tests and
cumulative/canonical-report reconciliation. The all-record objective and
publication remain unfinished.
