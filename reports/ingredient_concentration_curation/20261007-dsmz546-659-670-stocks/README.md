# DSMZ 546, 659, And 670 Stock Stages

Nine authoritative normalized records are corrected locally: each DSMZ medium,
its KOMODO counterpart, and standalone MediaDive solutions 1205, 1390 and 1413.
This is a source-backed repair, not completion of the all-record goal.

## Changes

- **546:** restore separate 1 M calcium chloride dihydrate and magnesium sulfate
  heptahydrate stocks, each added as 0.005 L after cooling. Represent 0.99 L base
  water as a batch input, not a percentage or measured final volume.
- **659:** restore a 1 M calcium chloride dihydrate stock with a 0.0012 L dose.
  Retain lactose at the source-explicit final-medium target of 8 g/L, with its
  filtered, post-autoclave addition documented. Lactose stock strength and dose
  remain unspecified. Base water is 1 L input, not established final volume.
- **670:** restore the 40% w/v ferrous sulfate heptahydrate stock and 0.05 L
  addition. Distinguish its 0.2 N sulfuric-acid carrier from the 4 N pH reagent;
  both acid amounts remain unquantified, with normality preserved in source text.
  Base water is 0.95 L. Preserve the base/stock sterilization boundaries and
  static incubation instruction. Strain-specific alternatives are not applied
  to the base or claimed reviewed.

The [independent applied audit](diff-audit.json) verifies **57 new evidence
entries**, **30 clarified existing evidence scopes**, **six new references**
and **nine append-only curation events**. Changes include three water-unit
corrections, twelve stock-stage concentration rebases, twelve constituent
relocations and eighteen new quantity slots. Those are distinct counting units.
The six unquantified acid input nodes comprise three stock carriers and three
pH-adjustment reagents; the existing `unquantified_carrier_nodes_added` audit
bucket includes both kinds of input.
All pre-existing ingredient mappings, bibliography and historical excerpts are
preserved; ontology grounding was not independently re-curated. No taxa-media
growth association was added.

## Evidence

The [frozen plan](plan.json) stores before/after text, exact tracked paths, hashes,
literal API excerpts, source locators and claim-specific explanations. The nine
`*-followup.md` files supplement their existing exact-path reports without
duplicating `- Record:` entries. Unknown quantities, source authors and publication
years are not filled with guesses.

The official [546 PDF](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium546.pdf),
[659 PDF](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium659.pdf) and
[670 PDF](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium670.pdf) were
text-inspected again and corroborate the repaired preparation stages. The later
[670/673/266 PDF captures](next-variant-source-captures.json) pin the unresolved
variant/conflict sources by response hash and extracted page text; no PDF visual
inspection or new 546/659 PDF capture is claimed. Amounts are supported by
the traceable official API captures; the captured KOMODO rows establish source
identity only. Repeated source records are not independent confirmations.

## Verification

Baseline: 270 focused tests, nine open-schema checks and strict validation of all
15,910 normalized records passed. Application, readback, no-op reapplication and
independent full-record inversion passed. Additional guards exercise source
drift, concurrent edits, symlinks and scientifically incorrect proposal values.

Post-edit focused tests pass **273 cases**. `just test-fast` passes **7,592 tests**,
with 16 skipped and 1,839 deselected. Nine post-edit open-schema checks, full
strict validation, IDs, three affected historical-cohort readbacks, cumulative
diff and coverage checks pass. [Final checks](final-checks.json) verify all nine
live result hashes, source snippets, complete-record inversion, quantity-report
coverage, Black, Ruff and `git diff --check`.

Product validation passes with all configured adapters retained, 91 non-blocking
warnings and 96,057 no-adapter skips. This is not independent validation of every
chemical mapping. Results are recorded in [validation.json](validation.json),
[extra-checks.json](extra-checks.json) and
[reference-validation.json](reference-validation.json). All jobs are terminal.
Runtime is the partial locked Python 3.13 environment, not full CI.

All 87 evidence snippets pass the installed text matcher against retrieved or
cached source content. Full bibliography checks still fail once per record on
the API URL-as-title fallback mismatch; valid descriptive titles were not
replaced with URLs to force a pass.

The [actual-group retention check](merge-retention.json) passes the two KOMODO
546/659 records and all three standalone routing checks, but fails exact
formulation/provenance retention for the other four media. All six medium stock
lists and preparation instructions survive; differing per-record evidence,
notes, references and history do not all survive. This is not a claim that the
numeric stock strengths differ between those counterparts.

Global merge verification fails with **1,247 name conflicts and 3,287 fingerprint
issues**. [Freshness](merge-freshness.json) also fails: 6,320 tracked versus
6,496 fresh files, 3,720 only tracked, 3,896 only fresh, 1,684 changed and 916
unchanged. Regeneration was temporary only. No tracked merge output, schema,
lockfile or runtime-version file changed.

## Remaining Work

The [adversarial review](adversarial-review.md) identifies unresolved 670 strain
formulations and the inherited 673/266 source conflict. The old flat-recipe
migration remains fail-closed; its tests now use pinned historical inputs rather
than constrain the current corpus. Their legacy scoring assertions are not
scientific approval of those variants.

The [next-variant handoff](next-variant-handoff.json) pins seven unchanged live
records and the new PDF-source capture hash. The captured KOMODO 670.3 row also
states pH 3.5, so its disagreement with the current DSMZ PDF's pH 3.0 is a
source/version conflict, not merely a local typo. That read-only handoff adds no
unique completed reviews. The next unreviewed KOMODO cohort remains offset 2500.

Global coverage and publication gates remain open. No commit, push, PR, merge,
branch deletion or generated-page publication is claimed by this batch.

The [cumulative diff](../20261007-diff-audit-after-dsmz-stock-stages.json) now
verifies 5,020 edited paths, 29,667 new evidence entries and 1,356 quantity
corrections. [Coverage](../20261007-followup-coverage-after-dsmz-stock-stages.json)
is unchanged at 10,610 of 15,910 normalized paths; report presence is not
scientific completion.

## Later Source-Version Follow-Up

The [five-record successor](../20261007-komodo670-source-versions/README.md)
curates the four DSM 9463/9466/9467/9468 children and updates this batch's KOMODO
670 parent links. The original frozen plan, source captures and historical
validation remain unchanged. Its parent result is now an intermediate state:
use the explicit successor hash chain for current readback. The 673/266 conflict
remains open. The archive supports the older DSM 9466 pH 3.5 formulation, so the
successor preserves separate source versions rather than treating pH 3.5 as a typo.
