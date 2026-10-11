# DSMZ 1157/1164 Stock-Stage Repair

Six exact normalized records were changed locally. This repairs two reviewed
formulations; it does not finish the all-record objective or add unique report
coverage. No taxa-media growth associations, IDs or generated merges were added.

## Evidence and Decisions

The original [DSMZ 1157 PDF](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1157.pdf)
specifies a 5 ml riboflavin addition from a 0.2 mg/ml stock. Its other additions
are 2 ml glucose stock, 1 ml magnesium sulfate stock and 1 ml calcium chloride
stock. These are separate additions after autoclaving and cooling. Their 50%,
20% and 10% labels do not specify a percentage basis. Numeric stock strengths
for these three components were therefore withdrawn, not converted by assumption.

The original [DSMZ 1164 PDF](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1164.pdf)
specifies seven drops of a 0.5% iron chloride hexahydrate stock, not 7 g/L.
Neither percentage basis nor drop volume is specified. The dose is preserved
in evidence-backed notes without a fabricated numeric volume or concentration.

Both PDF pages were visually inspected. Actual captured bytes and extracted
page text are hash-checked against [the frozen context](inspected-context.json).
The context includes the exact medium and standalone-solution API captures,
KOMODO original-recipe mappings, complete baseline records and historical plans.
Unknown individual authors and publication years remain absent; the PDFs'
2008 copyright notices are not treated as publication years.

Water is represented as a 1 L source batch input, not a percentage or final
volume. Direct mass rates are retained only as explicitly provider-nominal
rates, with the source batch masses and scope stated. Historical high_metal
flags and chemical mappings remain unverified by this repair, not negated.

## Applied Scope

| Follow-up | Stable ID | Stock descriptors | Result |
| --- | --- | --- | --- |
| [1157 KOMODO](records/1157-komodo.md) | CultureMech:003867 | 4 | Stock stages and water input restored |
| [1157 medium](records/1157-medium.md) | CultureMech:000595 | 4 | Stock stages and water input restored |
| [1157 main solution](records/1157-solution.md) | CultureMech:011703 | 4 | Stock stages and water unit corrected |
| [1164 KOMODO](records/1164-komodo.md) | CultureMech:003877 | 1 | Drop dose restored; exact parent path corrected |
| [1164 medium](records/1164-medium.md) | CultureMech:000605 | 1 | Drop dose restored; exact child path corrected |
| [1164 main solution](records/1164-solution.md) | CultureMech:011713 | 1 | Drop dose restored; water unit corrected |

The [independent applied audit](diff-audit.json) counts:

- 15 ingredient nodes relocated into 15 stock descriptors;
- 3 riboflavin stock-stage concentration rebases;
- 12 unsupported stock-stage quantity slots removed;
- 12 stock-dose quantities and 4 water-input quantities added;
- 2 existing water quantities corrected;
- 47 new evidence entries, 10 references and 6 curation events;
- 24 historical evidence explanations rescoped, with original quotes and
  explanations retained;
- 1 parent path and 1 child path corrected against exact tracked IDs/paths.

These categories are distinct; they must not be added together as a count of
concentration corrections. The 136 report rows include ancillary evidence
claims and the two unchanged legacy solution placeholders, not just quantities.
Follow-up reports supplement existing exact-path reports and deliberately do
not create duplicate `- Record:` review entries.

## Verification

Guarded application, persisted readback, zero-change rerun, whole-record
inversion and source arithmetic checks pass. Baseline and post-edit open-schema
checks pass for all six records using the correct root classes. Closed-schema
validation scans all 15,910 normalized records without errors; ID and
variant-link gates pass. See [baseline](baseline.json),
[application](application.json), [validation journal](validation.json) and
[historical readback](historical-readback.json).

The first focused integration run found a test manifest missing this explicit
successor plan. Its hash assertion was preserved and the manifest updated.
The [focused recheck](focused-recheck.json) passes all **156 tests**, including
the 39 new repair tests. The fast suite passes **7,713 tests**, with 16 skipped
and 1,889 deselected, in 402.30 seconds. Ruff and Black pass for all seven
Python files touched in this repair. Product validation exits 0 with 91
warnings and 96,061 entries skipped for lack of an adapter; this does not
establish complete ontology validation.

The [actual merge-retention check](merge-retention.json) fails for two of the
four medium inputs. Stock structures and quantities survive. A
[more detailed check](merge-evidence-details.json) verifies zero exact
ingredient-quotation losses, but twelve complete ingredient evidence entries
and two new curation events are not retained. Root evidence/reference metadata
also lose source-specific content. Standalone solutions are excluded from the
medium merger as expected. Nothing was hand-patched into generated merges.

The initial reference run failed on sandbox DNS resolution. The
[network-enabled retry](reference-validation-network-recheck.json) completes:
65 of 71 new/rescoped snippets pass the installed matcher. Six PDF snippets do
not pass its text matcher despite matching the actual extracted PDF pages and
visual inspection. Full citation checks report six PDF text and twelve API/PDF
title errors; the validator supplies URLs as retrieved titles. Neither source
titles nor quotations were falsified to satisfy that behavior. Actual PDF
bytes/text checks and automated matcher outcomes remain distinct.

Global merge verification fails with 1,247 name conflicts and 3,287 fingerprint
issues. [Freshness](merge-freshness.json) also fails: 6,320 tracked versus 6,498
fresh records, with 3,720 tracked-only paths, 3,898 fresh-only paths, 1,708 changed
shared paths and 892 unchanged. The freshness command completed; its collector
initially rejected the trailing `just` error line after the JSON. The journal
records recovery from that completed output, with the exit-1 trailer verified.
No validator was restarted or failed result relabeled as a pass.

The [terminal aggregate check](final-checks.json) verifies all six persisted
hashes, all 136 report rows, both original PDF captures, four API captures and
the two exact KOMODO mappings. All started processes are terminal.

`preview-v1-not-applied.json` is a superseded, unapplied preview. Before applying
the final `plan.json`, repeated excerpts were deduplicated within evidence
explanations and new API reference titles changed to the actual source names.
`preflight.json` describes that first preview; `preflight-v2.json` describes the
applied plan. No record was written from the first preview.

Checks use a partial locked Python 3.13 runtime, not full CI. Publication and
all-record completion remain unproven. No commit, push, PR merge or branch
deletion has been performed for these local changes.
