# Extraction Input Boundaries

Two previously reported normalized records are repaired locally. This does not
complete the all-record objective or add new unique reviewed paths. Historical
per-record reports remain intact and link to [DSMZ 12](12.md) and [DSMZ 657](657.md).

The later [KOMODO 12 source-linked repair](../20261007-komodo12-extraction/README.md)
now also corrects the legacy soil record identified by this batch. Results below
remain the historical extraction-batch snapshot; consult that follow-up for
current merge retention and cumulative coverage.

## Source Decisions

Both original one-page DSMZ recipes were visually inspected, along with the
exact recipe and preparation excerpts in their pinned official MediaDive
captures. Each authoritative YAML edit has a persistent recipe URL, exact
snippet, source locator, and scoped explanation. The API and original PDF
references are linked in each record's bibliography. Individual authors and
publication year were not established; institutional source, discovery mode,
access date, and hashes are recorded without inventing those fields.

| Source | Extraction input | Initial water | Recovered extract basis | Agar |
| --- | --- | --- | --- | --- |
| [DSMZ 12](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium12.pdf) | 400 g air-dried garden soil | 1 L | Recovered volume and absolute dose unspecified | 15 g per liter of clarified supernatant |
| [DSMZ 657](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium657.pdf) | 50 g dry cow-manure | 1 L | Filtered extract made up to 1 L before agar addition | 20 g added to that prepared extract |

The solid input and starting water now belong to an inline extraction
preparation. Its name is curator-described, not a fabricated accession. The
soil/manure `G_PER_L` slots are removed: they did not quantify retained solids
or dissolved extraction yield. Starting masses remain in ingredient notes
because the schema has no absolute-mass unit. Water changes from `1000 G_PER_L`
to `1 L`, without assuming density or equating starting water with recovered
volume. DSMZ 657's later make-up-water amount remains unspecified.

Only DSMZ 657 receives an explicit 1 L prepared-extract quantity, supported by
its make-up instruction. DSMZ 12 has no invented extract dose or yield. Agar
values remain numerically unchanged, with evidence now explicitly scoped to
the recovered liquid. Cloth/paper filtration is no longer mislabeled as filter
sterilization. The complete original preparation text is preserved across
extraction notes and subsequent agar/pH steps, in order.

## Evidence Accounting

The frozen plan contains 19 scoped claims across two records. It relocates four
input nodes, corrects two water quantities, removes two unsupported concentration
slots, adds one explicit prepared-extract quantity, and restructures two
preparations. These are separate count categories. Five new evidence entries,
two bibliography entries, and two curation events are added; three prior
evidence explanations are corrected without losing their exact source snippets.

The first medium pass had accepted the soil loading as a main-medium
concentration. That scientific interpretation is explicitly withdrawn, not
silently counted as supported after relocation. The two earlier agar claims
are retained at their new field paths. `claim_resolutions` links old and new
fields through verified before/after hashes, identity, unchanged original
quotes, and exact preparation-source evidence. The existing historical report
rows and curation events are not rewritten to hide the error.

The guarded runner defaults to preview, checks the entire cohort before writes,
pins exact tracked paths and historical/source/PDF hashes, and rejects drift or
unreviewed variants. Read-back confirms both result hashes and all 19 scoped
claims; a second apply changes zero records and adds no evidence/history.

## Verification

Both records passed baseline open- and closed-schema validation. All 42
pre-apply regression cases passed; the applied-state case was deliberately
excluded until the YAML edits existed. Ruff and Black checks passed for the
five Python files changed for this repair and its verification.

Post-edit gate outcomes are recorded in [validation.json](validation.json).
The focused suite passed 449 tests. Both post-edit open-schema checks, strict
validation of all 15,910 normalized records, and the ID gate passed. Independent
inversion of the repairs verifies preservation of unrelated fields and the
[cumulative semantic diff](../20261007-diff-audit-after-extraction.json).
The [refreshed exact-path coverage](../20261007-followup-coverage-after-extraction.json)
remains 5,779 reported paths and 10,131 outside this follow-up.

Read-back of both 500-record medium batches passed. The first has ten explicit
successor records, 906 retained supported-claim snippets, and one separately
verified withdrawn soil claim; the second retains all 653 snippets through one
successor. Each batch has one relocated agar claim. Historical acceptance totals
are preserved separately from current supported-claim counts.

This batch's [historical merge-group check](merge-retention.json) failed for soil
extract and passed for manure agar. The soil record grouped with
`KOMODO_12_SOIL_EXTRACT_medium.yaml`; the merged ID is `CultureMech:004048`, and
its ingredients, solutions, preparation, root evidence, and references differed
from the corrected source record. The manure record is its own group and keeps
all checked fields. Correct normalized data does not make the soil merge
publishable; do not blindly union evidence across ingredient-set fingerprints.

Full-suite verification is unavailable in the isolated Python 3.11 environment:
`just test` lacks coverage support, and a no-coverage retry stops during collection
on missing dotenv, rapidfuzz, pandas, and bs4. Product validation cannot load OAK
adapters; both reference checks cannot launch `linkml-reference-validator`.
These are not successful validations or claims of maintained Python 3.13/CI
compatibility. The completed global merge verifier still finds 1,247 name
conflicts and 3,287 fingerprint issues. The [freshness snapshot](merge-freshness.json)
has 6,320 tracked and 6,491 fresh records: 3,718 only tracked, 3,889 only fresh,
1,513 changed, and 1,089 unchanged. Both global gates exit 1; `git diff --check`
passes. The temporary build was not copied into authoritative or generated
repository data.

## Remaining Scope

These corrections do not revalidate secondary ontology mappings or the legacy
DSMZ 12 to KOMODO 12 source-duplicate relationship, whose old note claims
matching local concentration signatures. A subsequent fresh HTTP-200 capture
of the official KOMODO table verifies that exact row 12 names SOIL EXTRACT medium
and links the original DSMZ 12 PDF. The [source-identity handoff](komodo12-source-handoff.json)
records its exact HTML row, link, locator, timestamp, and whole-response hash.
That handoff established the source mapping, not ingredient quantities or an
applied repair. The subsequent KOMODO 12 follow-up now uses the original recipe
to curate that authoritative record. Other source
records and extraction recipes need their own exact-source review. No final liquid/solid-medium volume,
dissolved yield, density, unspecified stock dose, or taxa-media association was
inferred. The broader importer, variant, and mixed-source merge defects remain
open. No generated merge products were copied into the worktree; all curation
changes remain local and uncommitted.
