# Medium-829 Adversarial Review

This is a local review of an unapplied proposal, not a GitHub review or a
claim of all-record completion. The current `plan-v2.json` covers fourteen identified
source-linked candidates. Nineteen pinned captures support 435 source rows;
the proposed structure contains 447 ingredient, stock and preparation nodes.
The additional nodes represent separate indicator strengths and unquantified
preparation titrants, not invented source amounts.

## Findings Addressed In The Proposal

1. **Wrong stock provenance container.** The first builder draft created
   `source_data` on the standalone solution merely to obtain an evidence slot.
   Removed that change. Explicitly scoped water/composition/context claims use
   the reviewed water ingredient's supported evidence list. All six existing
   acid nodes and their evidence remain unchanged.
2. **Lost stock-candidate history.** The shared claim helper assumed that an
   old field's parent was a dictionary. List-indexed dose candidates caused a
   dry-run failure. The scoped wrapper now archives their exact old values and
   paths; it never promotes cross-medium inference to a concentration.
3. **Uninitialized conditional variants.** The initial dry run stopped before
   writing because the new variants list did not exist. The list is now created
   only for DSMZ829 and DSMZ829c, each with its exact original instruction.
4. **Weak conflict and removal snippets.** Title-only archival anchors were
   replaced with actual recipe-table excerpts. Added direct source comparisons
   for KOMODO dithionite and TOGO's bicarbonate versus DSMZ's NaOH carrier.
5. **Unnecessary loss of equivalent-label annotations.** Explicit, narrow
   aliases preserve prior annotations for MES, water, biotin, pyridoxine HCl
   and sodium dithionite. No fuzzy matching, borrowed identifiers or hydrate
   stripping is used. Copied annotations that do not establish the source's
   nickel hydrate, sodium-resazurin or stereospecific pantothenate are withdrawn.
6. **Nonliteral standalone-source title.** The first frozen proposal's
   capture-backed validator passed 660 of 661 checks. Its sole failure was the
   existing S1680 title `MediaDive solution 1680: Growth-stimulating factors`,
   which contains a curator-added accession prefix. The successor corrects the
   title to the captured `Growth-stimulating factors`, with a scoped excerpt
   and old/new history claim. The six pre-existing ingredient evidence entries
   remain untouched. `plan.json` and `cached.json` preserve the original failed
   proposal and terminal result; they are not overwritten by the successor.

Two development dry runs stopped before any recipe write. A subsequent complete
fourteen-record development proposal passed an independent source projection.
The successor proposal is tested separately; terminal validation receipts, not
this description, determine which gates have finished.

## Independent Checks

`audit.py` does not import or execute the mutator. It checks the frozen source
decisions, reconstructs source-stage placement, and compares the proposal with
all 416 prior quantity fields and eight dose candidates. The early source-only
reviews left liquid inputs in notes; the guarded proposal uses the schema's
`L` enum for exact milliliter-to-liter inputs, without a per-liter denominator.
That representation is independently recalculated in the audit.

Regression tests challenge every proposed node with an invented concentration,
as well as omitted/extra ingredients, grounding, evidence, historical events,
claim accounting and bibliographic metadata. Additional tests check genuine
versus false-LB yeast, carrier differences, unquantified titration, B12 stock
amounts, source-specific family links, deterministic rebuilding, no-op writes,
concurrent edits, symlinks and source-capture drift.

S1680 must remain SolutionRecipe-shaped and excluded from medium fingerprinting.
KOMODO2027 remains MediaRecipe-shaped with its supported semantic stock marker.
Its marker participates in formulation equality; it is not misrepresented as
automatically excluded by schema-shape routing. Thirteen medium-shaped proposed
records must retain their complete claims through separate runtime merges.

See `issue-source-conflicts.md` for intentionally unresolved source assertions
and `next-work.md` for application, validation and remaining corpus work.
