# Kaminskyj Stock-Boundary Correction

Applied locally to `CultureMech:007206` / `MEDIADB:308`. The
[per-record review](records/308.md) accounts for all fourteen original ingredients,
three added ingredient contexts, four stock additions and two optional variants.

## Applied Changes

- Restore the 20X nitrate stock (50 mL/L), trace stock (1 mL/L) and thiamine
  solution (1 mL/L) as separate stock preparations. Thirteen original ingredient
  nodes move into their proper stock compositions without duplicate base entries.
- Replace imported molar assertions with the primary protocol's mass and volume
  basis. Nitrate salts are per one-litre stock; trace salts use 100 mL final stock,
  not the initial 60 mL water. No molecular weights were inferred.
- Correct seven supplied hydrate identities and identify Na4EDTA as tetrasodium
  EDTA without inventing a hydrate or ontology mapping.
- Withdraw the unsupported thiamine molarity. The source's 1% label does not
  establish its percentage basis or supplied form.
- Represent water makeup and unquantified KOH/NaOH titration explicitly. The
  NaOH stock strength is 1 M; its dose remains unknown. Restore source pH 6.5
  and autoclaving without invented time/temperature.
- Preserve the anhydrous magnesium sulfate option and solid agar formulation as
  separate inline variants. No organism-medium associations are added.

The record gains **20 source-linked evidence entries, two references and one
history event**. Bibliography includes the verified DOI, title, author, year,
source type and discovery mode. Recipe quotations come from the inspected
[FGSC protocol](https://www.fgsc.net/fgn48/Kaminskyj.htm), with metadata checked
against [the publisher](https://journals.newprairiepress.org/fgr/article/id/1112/).
Captured-source hashes and extracts are in [source-review.json](source-review.json).

## Verification

- All 49 focused tests pass, including rehashed semantic forgeries and guarded
  write failures. Source checks re-extract all 20 snippets and volume contexts.
- [Application](apply.json) changes exactly the intended normalized record;
  independent readback and repeat no-op pass. Prior history and unrelated fields
  are preserved.
- Actual-written schema, strict schema and term checks pass. The initial
  [combined check](post.json) fails on sandbox DNS. The
  [completed post-edit checks](post-v2.json) include 113 passing regressions;
  failing reference commands are recorded rather than waived.
- The [network-enabled reference run](references-live.json) reaches the source
  but fails sixteen table excerpts because the generic validator compares against
  raw HTML. Both titles pass. These failures are distinct from the passing
  captured-source checks; no automated reference pass is claimed.
- [Runtime merge retention](reconcile-retention.json) preserves all claims in
  a separate formulation. [Four indexes](index-refresh-plan.json) are refreshed
  through the maintained generator, with unrelated metadata unchanged.
- [Cumulative accounting](cumulative-audit.json) verifies 5,291 edited records,
  36,625 new evidence entries, 5,899 new references and 5,528 history events.
  Follow-up coverage is 11,819 of 15,910 exact normalized paths; 4,091 remain
  outside these reports. Report presence is not complete scientific verification.

The [corpus run](corpus.json) is terminal: strict schema validation passes all
15,910 normalized records, and ID/product gates pass with existing warnings and
unsupported-adapter limits. Global merge verification still fails with 1,247
name conflicts and 3,287 fingerprint issues. Freshness still reports 15,056
differences (2,045 changed, 4,275 only tracked and 8,736 only fresh). The terminal
[fast-tier run](fast.json) has **13,208 passed, sixteen skipped, 3,498 deselected
and two dependency warnings** in 28 minutes 30 seconds. Source inventory and
tested code hashes remain unchanged. The [final checkpoint](validation.json)
keeps reference and global merge/freshness gates failed; passing fast tests do
not replace earlier failed full-suite runs. The full all-record goal remains
active, and the work is local and uncommitted, not publication-ready.

## Remaining Scope

Thiamine strength/form, titrant amounts and exact water input amounts remain
unresolved or not quantified. Existing bacterial filing, high-metal flag and
generic applications were not certified by this ingredient correction.

This applied primary-source correction supersedes only record 308's candidate
in the historical 453-record MediaDB draft. Do not apply that draft: its old
record hash is now stale, and its other scientific holds remain open. The
remaining 452 candidates and ten AMS1 records stay within the all-record goal.
The [AMS1 source follow-up](../20261009-ams1-source-review/README.md) inventories
all 200 current ingredient claims without applying unresolved corrections.
