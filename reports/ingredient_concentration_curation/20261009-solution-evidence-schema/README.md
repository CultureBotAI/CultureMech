# Solution Formulation Evidence

This local schema follow-up supports the all-record ingredient-curation goal;
it does not complete that goal or apply any medium323 recipe proposal. The
preceding [variant checkpoint](../20261009-halobacteria-variants/validation.json)
remains the last applied ingredient batch.

## Change

`SolutionRecipe.evidence` is now an optional list of the existing `EvidenceItem`
class. It can support solution-level formulation, nested stock additions and
preparation claims without fabricating imported `source_data.origin` or putting
stock-dose evidence on an unrelated ingredient. Composition amounts keep their
own ingredient evidence. Full field paths and preparation stages remain required
by the concentration skill's evidence contract; a schema pass does not verify
the science or make an unsupported amount acceptable.

The new attribute is appended after existing attributes so generated constructor
positions remain compatible. `SolutionDescriptor` and `ConcentrationValue` do
not gain inline evidence fields. No existing field or required constraint is
removed. Python dataclasses, JSON Schema and 341 ignored Markdown documentation
files are regenerated from the authoritative LinkML schema.

The triggering evidence is the captured MediaDive solution599 row for a 1.4 ml
addition of solution6552. Its persistent-URL source details and schema-gap
probe are retained in the preceding batch. A byte-exact copy of that source
capture is now an offline regression fixture; the test's synthetic recipe ID
is not a new authoritative record or ID assignment.

## Checks

- [Baseline](baseline.json): full normalized corpus hash matches the preceding
  applied checkpoint, including ignored filesystem paths and exact git inventory.
- [Initial generation](generate.json): dataclasses and JSON Schema generated,
  but documentation was absent. The old `gen-docs` recipe falsely returned zero
  after the unavailable obsolete `gen-markdown` command failed. This failure is
  retained, not reclassified as a pass.
- [Repaired docs](docs-repaired.json): `gen-doc --directory` produces the docs.
  The recipe now propagates generator failure. Offline command tests exercise
  both a successful generator and a nonzero generator exit.
- [Constructor-compatible generation](generate-v2.json): all three maintained
  generation commands complete; later link checks exposed collisions in the
  flat documentation layout, rather than a schema-field defect.
- [Final documentation](docs-separated.json): classes and slots have separate
  directories, preserving both `Term`/`term` and `Descriptor`/`descriptor` pages
  on case-insensitive filesystems. All 341 pages are generated successfully.
  Staging preserves previous output on failure and removes stale pages only
  after successful generation. The maintained documentation references are updated.
- [Initial focused checks](focused-v3.json): 153 tests pass, with two dependency warnings.
  Coverage includes generated-artifact parity, constructor compatibility,
  write refusal on invalid evidence, exact snippet validation, independent root
  and composition evidence traversal, unsupported field rejection, and skills.
- [Corpus checks](corpus.json): closed-schema validation passes for all 15,910
  normalized records, and ID/product checks pass. The product check retains
  91 warnings and 96,010 unsupported-adapter skips; these are not new ontology
  certifications. The full normalized corpus hash remains unchanged.
- [Production-schema smoke](s599-production-smoke.json): the actual S599 record
  accepts the pending dose and evidence in memory, retains all prior composition
  and history through generated-dataclass round-trip, and passes eleven exact
  captured-source checks after the in-memory title correction. No recipe is
  written and this is not a complete ingredient proposal.
- [Full regression](full.json): 16,405 passed, 25 failed, nineteen skipped and
  two warnings in 2,967.28 seconds. It selects all test tiers with coverage
  collection disabled (`PYTEST_ADDOPTS=--no-cov`). This failed run is preserved.
- [Final targeted checks](focused-v4.json): 830 tests pass, with two dependency
  warnings, after repairing documentation and historical tests. This includes
  all Markdown links, affected historical cohorts, schema/evidence coverage,
  registered-successor source audits and negative history-chain cases. Skill
  validators, Ruff and Black also pass. This is not a green full-suite rerun.

## Placement Inventory

The [saved-plan inventory](placement-candidates.json) scans 93 plan files,
including ignored paths, and finds 111 root-formulation claims stored on
composition evidence in 35 current stock records. Current field values and
the recorded excerpts still match all 111 claims. They concern placeholder
removal (35), quality flags (35), notes (39) and preparation notes (two), not
nested stock quantities. No evidence is moved or newly certified by this scan.

This is a plan-backed candidate inventory, not an exhaustive corpus-wide
placement audit or proof that the old claims are scientifically wrong.
Preserve existing ingredient support; reconsider placement when each record
is next curated. A new optional field alone is not a reason to rewrite all
previous evidence or history.

These checks use the existing local Python 3.13 environment, not clean CI.
No GitHub writes, publication, or new ingredient-record edits are claimed.

## Next Curation

The [stock-quantity projection](stock-quantity-projection.json) covers nineteen
existing composition quantities and the missing nested dose: nine existing
supported claims, six evidence additions, three quantity/unit corrections,
one new dose and one retained conditional-agar conflict. It preserves the
four-record inventory of 62 existing quantity fields and all nine prior
evidence entries. This is source adjudication, not a guarded apply plan or
new canonical review coverage. The original PDF page was visually reinspected.

The [remaining quantity projection](remaining-quantity-projection.json) adds
43 old-field dispositions for both media and the stock placeholders. Together
with the nineteen existing stock-composition fields above, it accounts for all
62 original quantities exactly once. It identifies unrelated LB product nodes,
misplaced fatty-acid stock components, exact KOMODO rates, unquantified source
rows and missing formulation nodes. Salt/stereochemistry and KOMODO physical
state remain explicit unresolved decisions, not guessed replacements.

The four [medium323 candidates](../20261009-halobacteria-variants/next-323-review-notes.md)
remain in scope. Before applying their stock doses, recheck record/source hashes,
build the complete guarded proposal, preserve S599's nine prior evidence entries,
and retain separate KOMODO and DSMZ formulations. Fix the source-title mismatch
in S599 only within its evidence-backed proposal. The schema change does not
resolve its water unit, conditional agar, false placeholder or nested dose by
itself. S6552's unsupported percentages and the medium records' misplaced stock
components and unrelated LB entries likewise remain unedited.

## Broader Test Findings

The full suite exposed four historical KOMODO cohort-audit failures. The
[diagnostic](historical-komodo-diagnostic.json) finds 41 current
record states omitted by those tests' limited successor lists. All 41 match
later registered hashes, pass independent source-audit inversion and preserve
the historical accepted claims. The repaired tests use the complete applied
registry and independent audits, not arbitrary hash exemptions. The
[stock diagnostic](historical-stock-diagnostic.json) similarly verifies two
later states while retaining all five original stock-report checks.

The older KOMODO829 relationship mutator is tested against its pinned historical
inputs. New tests require it to refuse the currently source-curated records;
its composition guard and production behavior are not weakened. Temporary
candidate checks are retained, including the first two-failure fixture run and
the corrected twelve-pass successor.

Documentation failures came from fifteen wrong-case links in thirteen pages.
The [import-rendering probe](docs-imports-probe.json) did not solve them. The
[type-separated probe](docs-separated-probe.json) generated 341 distinct pages
with zero broken Markdown links; that layout is now the maintained output.

The [remaining grounding diagnostic](resazurin-grounding-diagnostic.json) uses
an ignored-inclusive search followed by structured YAML traversal. Three current
normalized records attach `CHEBI:8806` to sodium-resazurin stock inputs. Their
exact primary-PDF excerpts support the existing 0.0005 L doses, while the local
ontology snapshot describes sodium-free resazurin. No broader detector exemption,
replacement chemical ID or data edit is applied. Direct live ontology lookups
were unavailable through the web tool; no claim about the absence of a salt term
is made. An independently audited, source-backed identity follow-up remains open.

The terminal [checkpoint](validation.json) pins the final code, generated docs,
checks and unchanged normalized corpus. All-record curation, the remaining
grounding failure, global merge/freshness failures and publication remain open.
