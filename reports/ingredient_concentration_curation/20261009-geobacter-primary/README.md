# Geobacter Primary-Source Review: Applied, Checkpoint Recorded

Status checked 2026-10-09. The revised 56-record proposal is applied locally.
All 224 schema commands, 804 adversarial/equivalence tests and lint checks pass.
`apply-v2.json` verifies guarded writes, readback and a repeat no-op, with exactly
56 normalized paths changed. Per-record reports cover all 1,628 ingredient rows;
54 reports are new and two existing reports have an append-only follow-up.
Cumulative reconciliation verifies 5,357 edited records, 37,059 added evidence
entries, 5,997 references and 5,596 history events across all applied batches.
Follow-up coverage is 11,885 of 15,910, leaving 4,025 outside coverage. All 56
runtime merge-retention checks pass and generated indexes need no content change.
Production reference validation fails 350 snippets and twenty titles: 332 DOI
snippets have no fetched article content; eighteen snippets and eighteen titles
encounter a PMC browser-check page; two older SQL-export titles still mismatch.
Sixty older MediaDB snippets and 58 titles pass. These automated failures are
not waived by manual scan inspection. All 112 post-edit schema commands and 961
focused tests pass. Corpus strict, ID and product checks pass, with 91 product
warnings and 96,008 no-adapter skips. Global merge verification still fails
(1,247 name conflicts and 3,287 fingerprint issues); freshness reports 15,056
differences. The fresh fast tier passes 14,604 tests, with sixteen skipped,
3,498 deselected and two dependency deprecation warnings. This is not a full-suite
pass. No publication or full-formulation verification is claimed.

## Applied Revision

`plan-v2.json` separates acetate chemical-form support from amount support.
The 1993 Methods explicitly cites the 1988 procedure; the 1988 FWA-Fe(III)
definition names NaCH3COO. This cross-reference supports the sodium salt for
all eighteen acetate inputs without asserting hydration or converting mass
to molarity. Four database-selected 10/50 mM endpoint amounts remain
unsupported and unchanged. Their two new evidence entries explicitly support
identity only, not those amounts. The relevant scans were re-inspected.

The applied revision accounts for 1,628 ingredient rows and includes 238
quantity-field corrections, 56 phosphate-hydrate corrections, eighteen acetate-salt
corrections, 34 donor amount evidence-only decisions and 56 sterilization
corrections. It appends 350 evidence entries, 74 bibliography entries and
56 history events. Of the 350 evidence entries, 294 are on ingredients and 56
on preparation. These are batch counts, not cumulative corpus totals.
Of the 1,628 quantity claims, 238 are corrected and 34 receive evidence for
existing amounts; 1,218 remain unsupported and 138 conflicting. Those 1,356
unresolved quantities remain unchanged and are not certified by report coverage.

The new cohort check verifies all ten existing concentration-variant pairs,
including exact ingredient labels and available primary/secondary chemical IDs.
It rejects the original draft. Separate tests prevent identity-only support
from being upgraded to verified endpoint amounts. A first revised dry run
exposed a missing-ontology-ID assumption in this check; it was corrected to
compare labels and optional IDs without inventing a missing grounding.

All 224 baseline/proposed schema commands passed in `preview-v2.json`.
The following test run was deliberately interrupted after 119 passing tests
to remove repeated formatting work from forged inputs. Its nonzero outcome is
preserved. `preview-retest-v2.json` reuses only the hash-checked schema commands
for the identical proposal and unchanged production mutator, then reruns every
test. JSON/YAML-equivalence acceptance tests ensure that alternate formatting
cannot itself cause a false rejection. Production round-trip writing is unchanged.
The terminal retest passed and authorized guarded application.
`baseline-v2.json` pins the prior local state: 54 records were not previously
edited/reviewed in this follow-up; two already had canonical reports. The latter
were extended, not duplicated.

## Original Draft Hold

Adversarial inspection found a variant-link inconsistency in `plan.json`:
the proposed MEDIADB:416 and MEDIADB:444 parent recipes change acetate
(`CHEBI:30089`) to sodium acetate (`CHEBI:32954`), while their linked
MEDIADB:423, MEDIADB:424, MEDIADB:451 and MEDIADB:455 children retain acetate.
The unchanged relationship notes still assert identical ingredient identities
with concentration differences only. That assertion would be false after
applying this draft. Schema validation alone does not resolve this defect.

The disposition required resolving chemical-form evidence and relationship
semantics together while preserving uncertainty about endpoint quantities.
The applied revision does that and adds the regression checks described above.
It does not infer a molar conversion from 6.8 g/L without supported hydration
and quantity basis. The original proposal remains unapproved.

The read-only preview was deliberately interrupted after 50 completed checks.
`preview.json` records `terminal: true`, `passed: false`, `KeyboardInterrupt`,
and no changed normalized-record paths. The interrupted command remains listed
as `running_command` in that historical receipt; the process exited with code
130 and is no longer running. The focused test stage was not reached.

The [terminal checkpoint](validation.json) records all batch validation outcomes,
including the failed reference and global merge gates. It verifies that the
tested code, schema, audit registry and all 15,910 normalized-record hashes remain
unchanged after validation. The all-record objective remains active and
incomplete; the local work has not been committed or published.
