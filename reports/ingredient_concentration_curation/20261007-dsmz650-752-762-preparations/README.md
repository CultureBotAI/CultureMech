# DSMZ 650, 752, And 762 Preparation Follow-Up

Six authoritative normalized records are corrected locally: the DSMZ media and
their standalone MediaDive solutions 1378, 1538 and 1552. All six already had
reports and local edits; this adds no unique reviewed or edited paths.

## Changes

- **650:** correct tap water to a 1 L batch input and pyruvate to the explicit
  20 mM post-autoclave addition. Existing preparation text is retained.
- **752:** restore separate manganese and iron stocks at 0.36 g/L and 50 g/L,
  each with a 0.001 L batch dose. Restore/correct the 1 L water input. The liquid
  medium uses only the liquid preparation branch; the standalone solution keeps
  the full conditional liquid/agar instructions, without adding the alternative
  carbonate dose simultaneously.
- **762:** preserve 5.4 g carbonate and 4.2 g bicarbonate as input masses in a
  separate preparation. Withdraw their earlier flattened concentration claims,
  retain the original excerpts and explanations with explicit supersession, and
  restore 0.9 L base water and 0.1 L preparation water. Water input does not prove
  stock final volume or dose; no 54/42 g/L stock strengths or 0.1 L dose is added.

The [independent applied audit](diff-audit.json) verifies six quantity/unit
corrections, four stock-stage concentration rebases, eight constituent relocations,
eight new quantity slots and four withdrawals. These are separate count categories.
There are **20 new evidence entries**, **32 corrected existing evidence scopes**,
six appended curation events and no added references. All original ingredient
identities, chemical mappings, bibliography entries and historical excerpts are
preserved. No taxa-media growth association is added.

## Evidence And Reports

The frozen [plan](plan.json) includes full before/after texts, hashes, exact API
excerpts, locators and explicit historical-claim resolutions. Each of the six
`*-followup.md` files supplements its existing exact-path report without creating
a duplicate `- Record:` entry. It reports retained quantities, applied changes
and unresolved amount claims, including legacy standalone placeholders.

Amounts are supported by inspected, traceable official API captures, not copied
from a neighboring record. The official [650 PDF](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium650.pdf),
[752 recipe page](https://www.bacmedia.dsmz.de/medium/752?mobile=1) and
[762 PDF](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium762.pdf)
were also text-inspected in this follow-up and corroborate the relevant stages.
No PDF visual inspection or new hashed PDF capture is claimed. Unknown authors
and publication years remain unknown; a copyright footer is not a publication
date. Repeated source records are not independent scientific confirmations.

## Verification

Baseline: 264 focused tests, six open-schema checks and strict validation of all
15,910 normalized records passed. A further isolated test confirms the historical
claim check uses self-contained frozen captures, not workstation caches.

Application, source readback, no-op rerun, independent complete-record inversion,
six post-edit open-schema checks, full strict validation and ID checks passed.
All three affected 500-record historical cohorts verify through the explicit
follow-up chain, including the four new carbonate withdrawals. Cumulative diff
and coverage checks pass. Post-edit focused tests pass **264/264**; `just test-fast`
passes **7,557 tests**, with 16 skipped and 1,839 deselected. Final source readback,
complete-record inversion, report coverage, Black, Ruff and `git diff --check`
pass. All runs are terminal in [validation.json](validation.json) and
[final-checks.json](final-checks.json). Checks use the partial locked Python 3.13
environment, not full CI.

Initial product validation failed because the sandbox prevented refreshing the
existing FoodOn cache. The authorized [cache-access retry](product-cache-retry.json)
passes with all configured adapters retained, 91 non-blocking warnings and 96,051
no-adapter skips. The initial failure remains recorded; this does not claim every
chemical mapping was checked or corrected.

All **52** evidence snippets in these records pass the installed text matcher
against retrieved/cached content. Full reference checks nevertheless fail once
per record on API URL-as-title fallback mismatches. See
[reference-validation.json](reference-validation.json). No valid descriptive title
was replaced with a URL merely to satisfy that check.

The [actual-group merge check](merge-retention.json) fails exact formulation and
provenance retention for all three media; their record-specific evidence,
references and events do not all survive selection of their KOMODO counterpart.
The three standalone solutions pass routing checks and are correctly excluded
from medium groups. This is not a claim that numeric values alone necessarily
differ, nor proof that all group members are equivalent. In particular, the 650
group also contains a strain-modified record. Publication remains unverified.

Global merge verification fails with **1,247 name conflicts and 3,287 fingerprint
issues**. The [freshness comparison](merge-freshness.json) also fails: 6,320 tracked
versus 6,495 freshly generated files, 3,720 only tracked, 3,895 only fresh, 1,683
changed and 917 unchanged. Regeneration occurred in temporary storage only.
No tracked merged output, schema file, lockfile or runtime-version file changed.

## Remaining Scope

The [current cumulative audit](../20261007-diff-audit-after-dsmz-preparations.json)
verifies **5,017 distinct edited records, 29,610 new evidence entries, 5,224 new
references and 5,196 appended events**, including **1,353 quantity corrections**.
The [current coverage](../20261007-followup-coverage-after-dsmz-preparations.json)
is still **10,610 of 15,910 normalized paths**, with **5,300** outside these reports
and unresolved claims inside reported records. The all-record objective remains
active; review-report presence is not scientific completion.

[Next stock candidates](next-stock-candidates.md) preserve twelve unedited candidate
snapshots and an original-source conflict requiring special care. That investigation
is not an approved apply plan. No commit, push, PR, merge, branch deletion or
generated-page publication is claimed by this batch.

The subsequent [546/659/670 stock-stage repair](../20261007-dsmz546-659-670-stocks/README.md)
has now applied nine of those targets with explicit evidence. The handoff JSON
is preserved unchanged as historical input; its three 673 targets remain open.
