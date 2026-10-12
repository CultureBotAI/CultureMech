# TOGO JCM954/JCM973 Concentration Review

This is a four-record follow-up, not completion of the all-record objective.
The exact tracked paths, IDs, complete original records, six source responses,
retrieval metadata and hashes are in [inspected-context.json](inspected-context.json).
The [plan](plan.json) was previewed before any recipe edits. The first preview
was not applied; the final preview uses shorter literal source excerpts.

## Decisions

| Record | Source | Decision |
| --- | --- | --- |
| [M1001](records/M1001.md) | TOGO M1001 / JCM954 liquid | Correct four input-volume units and add the explicit NH4Cl stock strength. |
| [M1002](records/M1002.md) | TOGO M1002 / JCM954 solid | Same corrections; support the source-explicit 20 g/L agar preparation. |
| [M1023](records/M1023.md) | TOGO M1023 / JCM973 liquid | Unchanged: source recovery and preparation-aware repair required. |
| [M1024](records/M1024.md) | TOGO M1024 / JCM973 solid | Unchanged: do not treat the 20 g agar batch amount as explicit g/L. |

The two changed records receive **eight quantity corrections**, **two new
stock-strength slots**, **38 evidence entries**, **four references** and **two
append-only events**. Twelve existing mass concentrations remain unverified;
their new notes and evidence establish batch masses only. The reports cover
all 38 original concentration slots and two new stock-strength slots. There
are 29 unresolved original claims, eight corrected claims, one evidence-only
agar claim, and two added stock-strength claims.

JCM954 specifies 233 ml water, 767 ml MDS salt water, 5 ml ammonium chloride
stock and 2 ml phosphate buffer. These become 0.233, 0.767, 0.005 and 0.002 L
**batch inputs**, respectively, not ml/L. The last two stocks are added after
autoclaving/cooling; a one-litre final-volume assumption is not supported.
The 1 M NH4Cl stock is represented separately from its 5 ml addition. Chemical
groundings, physical-state variants, historical events and organism claims
are unchanged. No DOI, author list or publication year was invented; the
original JCM page title is `Medium data`, and its copyright year is not used
as a publication year.

The referenced MDS salt-water and potassium-phosphate-buffer compositions
remain empty. Their addition volumes are supported; their stock strengths and
any resulting final-medium concentrations are not newly established. The 40
report rows count represented concentration claims, not invented ingredient
rows for these unresolved reference-only stocks.

## Deferred JCM973 Pair

The cited JCM973 page returned HTTP 200 but its actual content was `Nothing
found.` This is a content failure, not source verification. The TOGO API still
provides a table and preparation text. That text instructs preparation of a
magnesium chloride solution **made up to 500 ml** and a separate solution of
the remaining components **in 500 ml water**, followed by separate autoclaving
and combination. These are not interchangeable volume bases. The table's
1000 ml water cannot simply become an asserted one-litre water input or
one-litre final mixture. Agar is 20 g added to the latter solution, not an
explicit 20 g/L statement. Both records remain byte-for-byte unchanged.

Ignored-inclusive `find` searches covered the repository (excluding `.git`
and `.venv`) and the working source cache for 973/1023/1024 names. Existing
MediaDive J973 captures and earlier reports were located as leads, not treated
as the missing original recipe. Bounded web searches did not recover a usable
original document. This does not establish that no archived source exists.
The [dated MediaDive J973 capture](jcm973-comparison-handoff.json) was then
hash-checked and inspected: it points to the same
unavailable JCM page and preserves the same two-stage preparation. A related
DSMZ1468 capture is not a substitute: it states 41 g NaCl (not 40.1 g), identifies
Casamino acids with vitamins, and describes the split preparation for solid
medium. Next: use the corroborating JCM973 dataset instructions to design a
preparation-aware stock repair, seek the original recipe where possible, and
retain unknown final-medium volume and the liquid/agar split. Do not borrow
DSMZ1468's reported g/L values to fill the JCM973 evidence gap.

The next structural review should also include the exact tracked sibling
`data/normalized_yaml/archaea/halorhabdus_segorensis_medium.yaml`
(`CultureMech:003322`, `mediadive.medium:J973`) and standalone solution
`data/normalized_yaml/bacterial/mediadive_4996_Main_sol_J973.yaml`
(`CultureMech:013919`, `mediadive.solution:4996`). Both complete records were
read during this follow-up; neither was edited or counted as a new report.
Their flattened magnesium value is 203 g/L, while the preserved preparation
specifies 203 g magnesium chloride hexahydrate made up to 500 ml for a separate
stock. A source-scoped **stock** value of 406 g/L is a candidate for the next
guarded structural repair, not a new assertion about the final medium. The
standalone solution's previous report already leaves all its concentrations
unverified. Recovering this preparation stage must not promote the remaining
batch masses to final-medium concentrations.

## Verification

- [Final preview audit](preview-v2-audit.json): independent source checks and
  complete semantic inversion of allowed edits.
- [Baseline](baseline.json): pre-apply checks and exit-code journal.
- [Post-apply validation](validation.json): current gate results when terminal.
- [Diff audit](diff-audit.json), [reference validation](reference-validation.json)
  and [actual merge retention](merge-retention.json): separate checks, not
  interchangeable claims of scientific or publication completion.

All validation processes have completed. Applied hashes, no-op rerun,
independent semantic inversion, all four open-schema checks, full-corpus
strict schema, IDs, variant links, 64 focused tests and the fast suite pass.
The fast result is 7,739 passed, 16 skipped and 1,889 deselected. Ruff, Black,
and tracked-file diff checks pass. Product validation exits 0 with 91 warnings
and 96,061 no-adapter skips; it is not complete ontology validation.

Both changed records preserve their full entries and provenance in their
actual singleton merge groups. Global merge verification still fails with
1,247 name conflicts and 3,287 fingerprint issues. Freshness compares 6,320
tracked and 6,498 freshly derived merged paths: 3,721 tracked-only, 3,899
fresh-only, 1,709 changed and 890 unchanged. It fails. The citation gate below
also fails. The [terminal local check](final-checks.json) verifies the four
current record hashes, all six curation source captures and 40 report rows.
The environment is partial locked Python 3.13, not full CI. Publication
remains gated; no commit, push, merge or publication was performed.

### Citation Gate Limitations

The network-enabled installed validator completed with 22 errors: 20 snippet
failures and two TOGO API title mismatches. Its separate snippet matcher passed
18 of 38 new evidence entries. Eighteen failures concern JCM HTML table rows:
the validator cache contains raw HTML tags between the quoted words and cells.
Two concern TOGO's literal `[M578]`: the installed `SupportingTextValidator`
removes square-bracketed content from the query as an editorial note, but not
from the source. The API cache title is the URL, despite the inspected JSON
`meta.name` containing the recorded recipe title. These are diagnosed adapter
limitations, not an automated pass. Source hashes, literal JSON slices and
HTML table-cell text were checked independently. No validator cache was
rewritten, no evidence was weakened to make the gate pass, and no third-party
validator code was changed.
