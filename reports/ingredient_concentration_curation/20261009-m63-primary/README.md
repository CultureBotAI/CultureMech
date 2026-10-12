# Modified M63 Primary-Source Review

State: `plan-v3.json` applied locally to twelve exact records. Guarded write,
readback and repeat no-op pass in [apply.json](apply.json). Post-edit checks and
merge retention pass; global merge and reference gates still fail. The fresh
fast tier passes 13,799 tests. The [terminal checkpoint](validation.json) pins
the tested code, source records and individual gate outcomes. The full all-record goal
remains incomplete; nothing is committed or publication-ready.

## Scientific Decision

The twelve exact MediaDB records 4-15 contain 84 ingredient amounts. The
[2010 primary article](https://pmc.ncbi.nlm.nih.gov/articles/PMC2964678/), DOI
10.1186/1471-2180-10-256, directly supports the separate carbon and salt
conditions. Its Methods explicitly cites reference 48 for the M63 definition.
That [1982 source](https://pmc.ncbi.nlm.nih.gov/articles/PMC220425/), DOI
10.1128/jb.151.3.1433-1443.1982, was inspected visually on printed pages 1433-1434
using PMC's linked scan images. The base recipe is on page 1433.

This source chain supports all seven existing numeric amounts, with no numeric
changes. It also supports correcting monobasic phosphate and the magnesium and
iron sulfate heptahydrates: three chemical-form corrections per record. Exact
MIM label resolution and local ChEBI labels are pinned in
[source-review-v2.json](source-review-v2.json). The 2010 carbon/salt conditions
override the older source's conditions; unrelated organism-specific additions
and experiments are not imported. The evidence explicitly describes this
cross-reference inference rather than pretending all seven amounts were printed
in the 2010 article.

The applied result adds 84 in-record evidence entries, 24 bibliography entries
and twelve history events. Preparation, classifications, growth associations,
permanent IDs, numeric quantities and parent/variant links remain unchanged.
Existing glucose stereochemistry and hydroxyectoine positional naming are not
independently certified by this concentration review. KOH in the base recipe is
distinct from the unquantified pH-adjustment dose.

## Preview History

- `plan.json` is an unapplied evidence-only draft from before the base source
  was inspected. Its 394 focused tests and 48 schema commands passed, but its
  checkpoint failed two lint findings. It is not an application approval.
- `plan-v2.json` incorporates the base source. Diff review caught a shared-object
  YAML alias, so its validation run was deliberately interrupted. It is not a
  successful checkpoint or an applied plan.
- `plan-v3.json` separates the two magnesium term objects. A regression assertion
  rejects new YAML anchors/aliases. All 48 baseline/proposed schema commands
  passed, but one adversarial test fixture still used 7 as an invalid count
  after the expected count changed to 7. The forged count was corrected to 999.
  The [terminal retest](preview-retest.json) passes 395 tests plus Ruff and Black,
  reusing the 48 successful schema commands for the unchanged plan/writer.

The raw captures remain outside the repository. Their URLs and SHA256 hashes
are retained, alongside short supporting excerpts. The historical PDF endpoint
returned HTML, so no successful PDF download or OCR verification is claimed.

## Reconciliation

The independent [cumulative audit](cumulative-audit.json) verifies 5,303 edited
records, 36,709 added evidence entries, 5,923 added references and 5,540 appended
history events. [Coverage](followup-coverage.json) is 11,831 exact paths, leaving
4,079 outside follow-up reports. Each of the twelve new reports has one exact
record line and seven ingredient-claim rows. Coverage is not a claim that every
record field or every covered concentration has been scientifically verified.

## Validation

- [Post-edit checks](post.json): 24 actual schema/strict CLI checks and 552
  selected tests pass. Whole-worktree whitespace validation passes.
- [Merge retention](reconcile-retention.json): all twelve changed inputs retain
  checked fields and evidence through their actual maintained merge groups.
  No generated merged YAML was written into the repository.
- [Index reconciliation](reconcile-indexes.json): fresh outputs are semantically
  identical; no index content changes or timestamp-only rewrites were applied.
- [Corpus checks](corpus.json): strict validation of all 15,910 records, permanent
  IDs and product validation pass. Existing global merge verification fails
  with 1,247 name conflicts and 3,287 fingerprint issues. Freshness fails with
  15,056 differences: 2,045 changed, 4,275 only in the existing merged corpus,
  and 8,736 only in a fresh derivation. Source-record hashes are unchanged.
- [Reference checks](references.json): the commands completed, but the production
  gate fails. Its 2010 DOI fetch exposes only the abstract (24 snippet failures);
  the 1982 HTML does not expose the scanned text (60 failures); twelve PMC title
  checks differ by a site suffix. Twelve DOI title checks pass. Actual full-text
  and scan inspection is documented separately and does not waive these failures.
- [Fast-tier run](fast.json): exit 0, 13,799 passed, sixteen skipped and 3,498
  deselected, in 1,645.58 seconds. Tested code and normalized-record hashes
  remain unchanged. No full-suite pass is asserted.

The [final checkpoint](validation.json) verifies all terminal receipt/log hashes
and repeats read-only application verification. The all-record objective,
automated reference gate and publication workflow remain incomplete.
