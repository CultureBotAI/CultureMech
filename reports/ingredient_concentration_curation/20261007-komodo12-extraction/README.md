# KOMODO 12 Extraction Repair

One additional authoritative record is curated, with one exact-path
[per-record report](12.md). This continues the all-record ingredient goal; it is
not completion of the corpus review or a general repair of the merger.

## Source And Scope

The fresh official KOMODO table's exact ID 12 row names SOIL EXTRACT medium and
links the original DSMZ 12 PDF. Its literal HTML row, response hash, timestamp,
and locator are preserved in the [source-identity handoff](../20261007-extraction-boundaries/komodo12-source-handoff.json).
The row has no submedium flag. The guarded parser checks a unique exact ID,
name, pH, original recipe link, metadata, and the whole capture hash. This is a
source linkage, not concentration evidence or proof based on matching names.

The [original DSMZ 12 recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium12.pdf)
was visually inspected again. The exact pinned [MediaDive recipe response](https://mediadive.dsmz.de/rest/medium/12)
provides literal ingredient and preparation snippets. The same source-aware
extraction builder used for DSMZ 12 reconstructs the formulation from those
sources; it does not treat another curated YAML as primary evidence. Existing
KOMODO inputs and formulation context must match before any edit is allowed.

- Soil is an extraction starting material, not a quantified retained solute.
  Its unsupported 400 `G_PER_L` field is removed, with the explicit 400 g
  starting mass retained in notes and source evidence.
- Initial tap water changes from 1000 `G_PER_L` to 1 `L`, without assuming
  density, recovered volume, or final-medium volume.
- The two inputs move into an inline extraction preparation. Its name is
  curator-described, not an invented source accession or stock dose.
- Agar remains 15 `G_PER_L`, explicitly per liter of clarified supernatant.
  The missing preparation instructions are restored from the original source,
  preserving extraction, agar addition, and pH/sterilization order.
- Recovered extract volume, dissolved yield, and absolute extract dose remain
  unspecified. Source evidence is not used to fill those unknowns.

Ten scoped report rows cover the three ingredients, preparation representation,
and source identity. Five evidence entries are added: three ingredient entries,
one recipe-preparation entry, and one source-mapping entry. Three bibliography
entries and one curation event are appended. Stable identifiers, prior history,
original source metadata, and unrelated fields are preserved. Authors and
publication year were not established; title, institutional source, source type,
discovery mode, access date, and hashes are recorded without inventing them.
Duplicate-source entries are not independent scientific confirmations. No
taxa-media associations are added.

## Verification

The frozen [plan](plan.json) is preview-first and requires explicit apply. It
pins the exact tracked target, baseline, original DSMZ review, PDF, API capture,
KOMODO table, and verified mapping handoff. It rejects source or local drift,
extra ingredients, unreviewed variants/preparation/evidence, and concurrent edits.
Read-back verifies the rebuilt persisted record and all ten scoped claims;
reapplication changes zero records and appends no additional evidence/history.

All 36 pre-apply regression cases passed, with the applied-state case excluded
until the record existed. Independent inversion of the preview verifies two
ingredient relocations, one water correction, one unsupported concentration
removal, restored preparation, five new evidence entries, three references,
one history event, and unchanged unrelated data. Ruff and Black passed for the
new mutator, regression tests, retention checker, and updated independent audit.
Post-edit outcomes are recorded in [validation.json](validation.json). All 486
focused tests passed. Before/after open-schema checks, full strict validation of
15,910 normalized records, and the ID gate passed. The earlier two-record
extraction repair still verifies all 19 claims unchanged. The
[cumulative semantic diff](../20261007-diff-audit-after-komodo12.json) verifies
4,422 edited records and 25,685 new evidence entries. The
[coverage inventory](../20261007-followup-coverage-after-komodo12.json) now has
5,780 reported paths and 10,130 outside this follow-up.

The cohort's retention check requires exact complete ingredient, stock,
preparation, physical-state, and pH structures, including all ingredient
evidence. At the root, every prior evidence and bibliography entry must survive
unchanged; additional unique-reference source entries are allowed. Regression
tests reject removed fields, modified quotes/support/explanations, and duplicate
references. This avoids falsely calling an additional KOMODO citation evidence
loss without weakening checks for the original recipe claims.

The [actual maintained merge-group result](merge-retention.json) passes for
KOMODO 12, DSMZ 12, and DSMZ 657. Both soil records share a group; the resulting
`CultureMech:004048` retains the complete corrected formulation and evidence
from both, including the extra KOMODO source citation. Thus the specific soil
evidence/preparation loss observed before this repair is resolved without
changing the merger or copying generated records into the worktree.

Product validation remains unavailable because OAK adapters cannot load;
automated reference validation cannot launch `linkml-reference-validator`.
The full suite was not rerun for this dedicated mutator: the preceding batch
confirmed missing coverage support and four missing collection dependencies
(dotenv, rapidfuzz, pandas, bs4), and the runtime dependencies are unchanged.
No maintained Python 3.13 or CI pass is asserted. The global merge verifier
still fails with 1,247 name conflicts and 3,287 fingerprint issues. The completed
[freshness check](merge-freshness.json) also fails: 6,320 tracked versus 6,491 fresh
records, 3,718 only tracked, 3,889 only fresh, 1,513 changed, and 1,089 unchanged.

## Remaining Work

Other KOMODO links and formulations need independent source review. This repair
does not validate all source-duplicate relationships, secondary ontology
mappings, or biological claims. The broader mixed-formulation/evidence-loss
defect in other merge groups remains open; ingredient-set fingerprints alone
do not establish equal recipes. All changes are local and uncommitted, and no
generated merge products are manually patched or copied into the repository.
