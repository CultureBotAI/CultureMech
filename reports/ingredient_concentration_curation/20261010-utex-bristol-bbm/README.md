# Bristol/BBM Ingredient Evidence Review

The five-record [guarded plan](plan.json) is applied locally. Readback and repeat
no-op checks pass; only the five intended normalized records changed. This batch
does not complete the all-record objective.

## Evidence And Scope

The [source ledger](source-review.json) covers 40 structured ingredient/stock
quantity claims and five narrative/relationship claims. Nine official UTEX
pages, five linked PDFs (seven visually inspected pages), and the BBM study
full text are hash-pinned. Source titles, authors, source type, discovery mode,
access date and known publication years are preserved. Unknown UTEX recipe
publication years are not replaced with copyright dates.

Applied changes add 40 evidence entries, enrich nine bibliography entries,
add two references and append five curation events. Seven unsupported water
quantities and one unsupported completed-Bristol dose are removed without
replacement numbers. All retained structured amounts are unchanged. The BBM
study's estradiol range is replaced with its five separately tested levels;
NH4Cl remains scoped to pre-experiment stock culture with no ppm conversion.
Botryococcus stock/final wording and its liquid-stock mixing action are repaired.
Bristol-NaCl preparation-stage notes agree on both sides of the parent link.

BBM manganese chemical identity remains conflicted; its new evidence supports
the source-spelling conflict, not the existing concentration. Trace-source
concentration columns remain inconsistent with their stated stock preparation.
No new final-medium conversion, chemical identifier, taxon-media association,
or unsupported stock strength is added. Existing growth and role assertions
are preserved, not blanket-certified.

## Validation

[Preview](preview.json): twenty baseline/proposed schema commands, 64 focused
tests, Ruff, Black and diff checks passed with no normalized record changed.
Source capture hashes and all ledger snippets were rechecked. All ten post-edit
schema/strict commands and 418 regression tests pass. Fourteen regenerated
indexes have no semantic changes. All five full-corpus runtime merge-retention
checks pass, retaining distinct formulations and their edited data.

Five canonical [per-record reports](records/) cover all forty structured and
five narrative claims. Cumulative reconciliation verifies 5,382 edited records,
37,379 evidence entries, 1,751 structured quantity corrections and 968 removed
unsupported quantity fields. Follow-up coverage is 11,910 / 15,910 exact paths;
4,000 remain outside coverage, and report presence is not complete verification.

The five initial reference commands abort on sandbox DNS, without per-claim
results. The [network-enabled rerun](references-live.json) passes four records,
43 snippets and twelve titles. The BBM estradiol snippet fails because the
validator obtains only the article abstract; the pinned full-text methods were
inspected separately. This is a remaining reference gate failure, not a reason
to replace the supported quote with abstract text.

[Corpus gates](corpus.json) are terminal: strict validation, IDs, products and
the MIM index pass, with 91 identity warnings and 96,008 no-adapter skips.
Global merge verification fails with 1,247 name conflicts and 3,287 fingerprint
issues; freshness fails with 15,056 differences (2,045 changed, 4,275 only in
tracked and 8,736 only in fresh output). These are not passing gates.

The fresh [fast-tier run](fast.json) is terminal: **15,154 passed, sixteen skipped,
3,498 deselected and two dependency warnings** in 32:01. This is not a full-suite
pass. The code, schema, audit registry and all 15,910 normalized-record hashes
stayed unchanged during the run.

The [terminal checkpoint](validation.json) rechecks actual recipe hashes, source
captures, canonical reports and validation receipts. All scheduled validation
runs are terminal, but the reference and global merge/freshness gates above
still fail. The earlier [applied checkpoint](applied-checkpoint.json) remains a
historical receipt of the state before the fast tier finished.

Nothing is committed, merged or publication-ready. The full objective remains
all 15,910 normalized records, including unresolved claims in reviewed records.
