# Public Direct-Ingredient Evidence

Two existing authoritative records were updated locally against baseline commit
`f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`:

| Record | Stable ID | Concentrations | Added evidence entries |
| --- | --- | --- | --- |
| `data/normalized_yaml/bacterial/king_b.yaml` | `CultureMech:010433` | 5 | 5 |
| `data/normalized_yaml/bacterial/mta10.yaml` | `CultureMech:010436` | 6 | 12 |

All 11 amounts, units, ingredient forms, ontology annotations, physical states,
pH values, existing references and prior history are unchanged. The independent
[diff audit](diff-audit.json) verifies that only 17 evidence entries, three
bibliographic entries and two append-only curation events were added. No record,
variant, or organism-medium association was created. The all-record goal remains
unfinished and the curation remains uncommitted.

## Source Scope

[P3](https://mediadive.dsmz.de/medium/P3) and
[P6](https://mediadive.dsmz.de/medium/P6) are user-contributed dataset pages.
Their source identity, complete ingredient tables, ingredient links, declared
1000 ml main-recipe scale and bibliographic/context metadata were checked against
the captured HTML. The page publication year is 2023, not the year of a journal
paper. The named creator is explicitly credited as the page author in the notes.

King B's glycerol remains `10 ML_PER_L`: the source supplies a 10 ml input at
its declared 1000 ml recipe scale. It is not a 10 g/L claim or a density-based
conversion. Dataset evidence does not establish an unpublished makeup or
sterilization protocol. No calculated mM column is promoted to a molarity claim.

The complete six-ingredient base mTA10 clause in the independently inspected
[2020 article, Section 2.2.1](https://pmc.ncbi.nlm.nih.gov/articles/PMC7564587/)
matches the six local g/L quantities. Its DOI is
`10.3390/microorganisms8091359`; authors are Sarah Azinheiro, Joana Carvalho,
Marta Prado and Alejandro Garrido-Maestu. The methods distinguish the base from
MOPS and supplemented variants. None of those variant changes, supplier
restrictions, experimental conditions, growth or performance claims was imported.
Each of the six ingredient nodes receives its own short DOI-backed snippet.

The [published correction](https://pmc.ncbi.nlm.nih.gov/articles/PMC8306464/)
was also inspected; it concerns primer sequences, not this formulation.
The DOI resolver redirected to the correct MDPI article URL, where the publisher
returned HTTP 403. The inspected full text is the PMC copy with matching DOI,
title, authors and date. Europe PMC XML requests returned HTTP 502/503; their
failures are not treated as successful source captures.

The older `10.1016/j.foodcont.2012.06.029` citation in P6 is preserved. Its methods
were not accessed: DOI/ScienceDirect access failed and a bounded search did not
yield an inspected full text. A search excerpt was not used as a concentration
snippet. The new 2020 source is independent evidence, not a claimed reading of
the 2013 paper.

## Replay

The guarded reviewer is `scripts/review_public_direct_concentrations.py`.
It defaults to preview and reuses the existing batch reader/writer. The
[frozen plan](plan.json) retains the exact before text, baseline/result hashes,
claim pointers, snippets, locators and evidence scope. Apply reconstructs the
whole result from the source captures before writing and rejects non-exact git
paths, symlinks and concurrent edits. Readback and no-op replay pass.

Captures accessed on 2026-10-07:

| Capture | SHA256 |
| --- | --- |
| `P3-medium-page.html` | `5ef4a1c49d241bfd226d2b343c94f3693832d3f93b29ab9ed5b976febc449e1b` |
| `P6-medium-page.html` | `d308ad98c3128738c64a92d2666a8e17202c1f80aaa1ff3f99143c0848b091db` |
| `P6-article-PMC7564587.html` | `4ba4130ab6f9e90804020f94a01f214a23fd3e2b1957d4934a8efefd7a77ffdc` |
| `P6-correction-PMC8306464.html` | `0d478c33c9abef1ebfacffda39f04bb84ff9a5b8394b679e00da89aed9280bf1` |

The source bundle hash covers the named capture hashes. HTML extraction decodes
entities, concatenates inline chemical subscripts and collapses whitespace;
table snippets retain cell order. Full byte hashes and a separate normalized
base-clause hash guard against source-context changes. Original captures remain
in `/tmp/ingredient-media-20261007`, not in the authoritative corpus.

## Validation

Baseline and post-edit strict scans passed all 15,910 normalized records with
zero errors. Both targets passed baseline and post-edit schema checks. Guarded
apply, readback, no-op, canonical IDs, independent diff and coverage checks pass.
The 45 pre-apply offline tests passed, followed by **750 passing focused tests**
after apply, including 46 tests for this reviewer. Synthetic HTML fixtures are
explicitly distinguished from real source captures. Black, Ruff and
`git diff --check` pass. Checks use isolated Python 3.11, not the maintained
Python 3.13 environment or CI; the full suite was not rerun for this batch.

The [actual-group retention audit](merge-retention.json) passes both records
in their two singleton groups after building groups from the full current
corpus. All checked ingredient, stock, preparation, state, pH, evidence and
reference fields survive. This does not resolve losses in other merge groups.
Global merge verification still fails with 1,247 name conflicts and 3,287
fingerprint issues. Product validation fails because `oaklib` is unavailable,
and both reference checks fail because `linkml-reference-validator` is missing.
These are recorded failures, not automated evidence-validation passes.
Source content was inspected manually as described above.

The [cumulative semantic diff](../20261007-diff-audit-after-public-direct.json)
now counts 4,851 edited records, 28,091 new evidence entries, 4,885 references,
4,857 curation events and 1,164 quantity/unit corrections. The latter count is
unchanged by this evidence-only batch. [Current exact-path coverage](../20261007-followup-coverage-after-public-direct.json)
is 8,104 of 15,910 normalized paths, leaving 7,806 outside these follow-up
reports. Presence of a report is not full scientific resolution.

All two target baseline jobs and 18 post-apply jobs are terminal in
[validation.json](validation.json), in addition to the separate baseline strict
scan. Thirteen post-apply jobs pass; the five failed jobs are product validation,
two reference validations, global merge verification and freshness.
[Freshness](merge-freshness.json) finds 6,320 tracked and 6,492 fresh records:
3,719 only tracked, 3,891 only fresh, 1,645 changed and 956 unchanged.
Regeneration was temporary only; no generated merge has been published.

The original ten-page [acquisition snapshot](../20261007-public-medium-source-pages.json)
remains unchanged. P3 and P6 now have per-record follow-up reports under
[records](records/); the other eight public targets remain unfinished.
