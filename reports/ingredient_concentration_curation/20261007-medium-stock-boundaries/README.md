# Reviewed Medium Stock Boundaries

Seven local repairs extend the first 500 receiving-medium source reviews. They
do not complete the all-record objective or create seven new reviewed paths.
The historical per-record reports retain their original hashes and decisions;
each links to one explicit successor below.

| DSMZ medium | Follow-up | Relocated ingredients | Added batch-volume fields | Preparation texts moved |
| --- | --- | ---: | ---: | ---: |
| 79, Leucothrix | [79.md](79.md) | 12 | 2 | 1 |
| 98, Rhizobium | [98.md](98.md) | 2 | 3 | 1 |
| 129, Potato dextrose agar | [129.md](129.md) | 1 | 2 | 1 |
| 260, Bacillus schlegelii heterotrophic | [260.md](260.md) | 7 | 3 | 0 |
| 261, Bacillus schlegelii chemolithotrophic | [261.md](261.md) | 7 | 3 | 0 |
| 369, Bacillus tusciae | [369.md](369.md) | 7 | 3 | 0 |
| 452, Glucose medium (Nakayama) | [452.md](452.md) | 8 | 7 | 0 |
| Total | 7 records | 44 | 23 | 3 |

The 105 scoped changes comprise 44 ingredient relocations, 35 evidence-only
concentrations, 9 stock doses, 14 water amounts, and 3 preparation-stage moves.
They add 100 evidence entries, 20 bibliography entries, and 7 append-only
curation events. Multiple stock-dose/preparation claims share a single scoped
root evidence entry for each API reference; no fake URL fragments are used.
Numeric values of existing ingredient concentrations are unchanged.

## Evidence And Scope

The receiving recipe's exact source solution IDs, complete ingredient inventory,
amounts, units, physical-state conditions, and preparation texts were checked.
Original official PDFs for all seven media were read and visually inspected;
SL-6 composition was cross-checked on the first page of DSMZ 27. DSMZ 261
explicitly uses 260 without pyruvate; DSMZ 369 modifies 261's pH and incubation.
The source chain is therefore 369 -> 261 -> 260 -> 27, not a name-based match.
Eight distinct PDF captures and seven API captures are hash-pinned.

Each edited scientific claim has an exact API excerpt and persistent recipe URL
in authoritative YAML. Source type, discovery mode, date, and capture hash are
recorded. Individual authors and publication years were not established and
are not invented from copyright dates. Stock doses and water use liters per
batch, not presumed liters of final medium. Source-declared `g_l` values are
explicitly scoped as provider preparation concentrations. In particular:

- DSMZ 98 soil and carbonate are inputs to extract preparation, not measured
  dissolved concentrations after settling and centrifugation.
- DSMZ 129 potato is an infusion input, not 200 g/L dissolved potato in the
  receiving agar. The sieving instruction is retained with the stock.
- DSMZ 260/261/369 each add 3 ml of SL-6; its constituents remain stock-strength
  values. No receiving-medium dilution is calculated from 1000 ml water alone.
- DSMZ 452 lists 980 ml water plus 10, 10, and 1 ml stocks. These are recorded
  separately; the 1001 ml arithmetic does not become an asserted final volume.

## Guards And Verification

`scripts/repair_reviewed_medium_stock_boundaries.py` defaults to preview and
requires `--apply` to write. It checks the pinned original review, exact tracked
targets, full before/after hashes, source metadata, PDF hashes, identities,
one-level stock graph, all ingredient amounts/forms, and preparation text.
All records are validated before the first write. Reapplication is idempotent.
The explicit selected cohort excludes unreviewed stocks, variants, repeated
ingredients, source attributes, conditional doses, and arithmetic conflicts.
This exclusion is not a claim that those records are resolved or out of scope.

An independent inversion in the cumulative diff audit verifies that every old
ingredient occurs exactly once, new water/dose fields match their source rows,
preparation moves preserve literal descriptions, and unrelated data is unchanged.
Before and after open/closed validation passed for all seven records. Full strict
validation scanned all 15,910 records with zero errors, and the ID gate passed.
The final selected regression run passed 327 tests, including 44 batch guard and
independent-inversion tests. Ruff, Black, and `git diff --check` also passed.
Current validation
commands and exit codes are recorded in [validation.json](validation.json);
merge-group retention is checked separately in [merge-retention.json](merge-retention.json).
No generated merge recipes or pages are hand-edited or copied into the worktree.

The actual maintained merger retains all checked fields for five of seven
records. DSMZ 261 and 369 are grouped together despite their different pH and
incubation conditions: the canonical record supplies the 261 stocks/procedure,
while ingredient-list selection takes 369's ingredient evidence. The check
exits 1 and exposes a mixed-source result, not a successful publication gate.
Both authoritative source records retain their own correct evidence.

The full `verify-merges` gate also exits 1. `validate-products` exits 2 because
`oaklib` adapters are unavailable; `validate-references` exits 2 because
`linkml-reference-validator` is not installed. Neither is counted as a pass.
Source capture and exact-snippet read-back are separate checks, not substitutes
for ontology validation or a claim that the automated reference validator ran.
Checks used the isolated Python 3.11 environment, not a passing maintained
Python 3.13/CI run.

Final guarded read-back verified all seven current hashes and 105 scoped source
claims; reapplication changed zero records. The full freshness comparison exits
1: 6,320 tracked versus 6,468 freshly generated records, with 3,723 only tracked,
3,871 only fresh, 1,488 changed, and 1,109 unchanged. Fresh output was generated
only in a temporary directory. The independent cumulative audit now counts
4,303 edited normalized records and 25,012 new evidence entries; see the parent
status report for all earlier quantities and remaining corpus coverage.

## Remaining Findings

- DSMZ 13 had two source solutions and no direct ingredients. Its exact source
  graph can be represented with `ingredients: []` and passes the open-schema
  validator, but the maintained fingerprinter rejected an empty direct list
  before traversing stocks. No misleading direct ingredient was retained or
  invented merely to satisfy that pipeline assumption. The subsequent
  [DSMZ 13 follow-up](../20261007-dsmz13-stock-only/README.md) now supplies
  stock-only/nested fingerprint support and its own guarded evidence-backed repair.
  Source: [DSMZ 13](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf).
- DSMZ 464a is not an unconditional agar formulation. Its original PDF says
  "Agar, if required" and specifies liquid reactivation before optional agar
  subculture. The API's embedded medium 464 lacks that condition. Its local
  `SOLID_AGAR` state and mandatory agar remain a formulation/stage conflict;
  the generic stock relocation was deliberately not applied.
  Source: [DSMZ 464a](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium464a.pdf),
  contrasted with the unconditional agar table in [DSMZ 464](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium464.pdf).
- DSMZ 261 still has a `SOURCE_DUPLICATE` parent link to KOMODO 369. Original
  recipes distinguish pH 7.1/65 C from pH 4.0/50 C, so ingredient-set equality
  does not justify that relationship. Parent/variant metadata was not silently
  rewritten during this quantity/stock batch; it needs a separate source-linked
  relationship correction across the affected records.
  Sources: [DSMZ 261](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium261.pdf),
  [DSMZ 260](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium260.pdf),
  [DSMZ 369](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium369.pdf).
- Existing secondary ChEBI mappings are preserved, not revalidated. In particular,
  SL-6's `NiCl2 x 6 H2O` is mapped to nickel dichloride in these records. The
  exact source form is retained; amount evidence does not certify that mapping.
- The earlier concentration-independent merge evidence-loss findings, importer
  unit handling, other stock conflicts, variants, and unreviewed corpus remain
  open. Completion of this seven-record batch is not completion of curation.

Changes remain local and uncommitted. No new taxa-media associations were added.
