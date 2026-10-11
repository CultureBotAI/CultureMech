# Source-Explicit Water Inputs, pH 7.0

Applied locally to 52 exact tracked standalone solution records. Each correction
changes `1000 PERCENT_V_V` to `1 L`, representing the source's **1000 ml water
input per preparation batch**, not a measured final volume, percentage, stock
strength, or receiving-medium concentration. Each ingredient has its own exact
source-row snippet, persistent MediaDive API URL, locator, conversion, source
hash, and separately quoted pH-adjustment instruction.

The frozen [plan](plan.json) retains complete before/after texts and source
hashes. [Inspected context](inspected-context.json) retains complete responses,
retrieval metadata, and original records. The guarded mutator is
[`repair_solution_water_ph7.py`](../../../scripts/repair_solution_water_ph7.py).
The same source must still match byte-for-byte before any write or no-op rerun.
This is a source-specific follow-up, not a relaxation of the general reviewer's
rule withholding preparation-dependent water quantities.

## Scope

- 52 water quantity corrections and 52 new ingredient evidence entries.
- 52 appended `codex` curation events; 3 new root references, with 49 reused.
- No nutrient, chemical mapping, stock-strength, growth-association, identifier,
  preparation, placeholder, or existing evidence/history changes.
- The 18 other pH-7.0 candidates remain unchanged and are listed in
  [deferred.json](deferred.json). This is triage, not completed source review.
- Source type is the official DSMZ dataset, discovered from existing record
  source identifiers. Individual authors and publication year are not supplied;
  no DOI, author, or year was invented.

The complete source recipe rows, preparation, and equipment context were read
for every selected record. Repeated prior evidence was losslessly represented
by its existing reviewer and inputs: regenerating it had to reproduce the whole
original record exactly. This does not newly endorse the unchanged non-water
claims or ontology mappings. The neutralized sulfide stock's name is not used to
infer a final volume or a neutralizing-agent quantity.

Per-record `*-followup.md` files supplement the existing canonical per-record
reports. They deliberately use `- Follow-up target:` instead of duplicating
`- Record:` entries. These are revisits, not 52 newly covered unique paths.

## Validation

[Baseline validation](baseline-validation.json) is terminal: 52 records pass
open and closed schema checks, all 52 are excluded from medium groups by the
maintained matcher, and all 210 selected regression tests pass. The independent
[baseline inversion](baseline-inversion.json) reconstructs every original
record after removing only the proposed correction and append-only provenance.
Across the complete preview, the only deleted YAML lines were the old water
value and unit; all other changes were additions.

The [post-validation journal](post-validation.json) is terminal: 20 of 22
commands pass; two older-runtime availability failures are retained separately.
The cached Python 3.13 targeted selection passes 130 tests. The expanded Python 3.13
[runtime check](expanded-runtime-validation.json) explicitly excludes five
visualization packages after the full locked environment failed to build
`llvmlite`. That journal is now terminal: `just test-fast` passes with 7,490
passed, 16 skipped and 1,710 deselected in 1,144.46 seconds. It is not full
maintained-project CI; the separately recorded reference-title failure remains.

Completed post-edit checks include 210 passing selected tests, 52 passing open
and closed schema validations, strict validation of all 15,910 normalized
records, the permanent-ID gate, exact water-source read-back, and a rerun with
zero changes. The maintained matcher still excludes all 52 standalone roots.
The [ten earlier batches](prior-batches-readback.json) verify all 4,770 result
hashes through explicit successors, retaining 23,902 supported snippets and
four separately verified historical snippets whose quantity claims were
withdrawn by earlier repairs. The 52 water snippets are checked separately.

The expanded runtime successfully completes `just validate-products`: 2,005
canonical-label matches, 274,679 ID-only matches, 29 exceptions and 96,044
configured no-adapter skips. Its 91 non-blocking warnings comprise 50
implausible-label and 41 hydrate-on-anhydrous-term findings. This is a pass under
the configured waivers, not new manual validation of every ingredient identity.
It supersedes the missing-`oaklib` availability limitation in the older isolated
runtime; that historical failed attempt remains in the post journal.

The installed deterministic reference checker has independently matched all
52 new water snippets against retrieved/cached public URL content, with zero
failures: [automated snippet read-back](automated-snippet-readback.json). This
is complementary to the exact frozen-response/hash checks, not a replacement
for scientific scope review. The full sampled `validate-references` command
fails its separate bibliography-title check: the URL source adapter searches
for an HTML `<title>` and falls back to the URL for this JSON API. We retain the
descriptive dataset citation rather than replacing it with the fallback URL to
force a pass. The observed failure remains in the expanded-runtime journal.

The new [cumulative semantic diff](../20261007-diff-audit-after-water-ph7.json)
verifies 4,966 distinct edited records, 29,188 added evidence entries, and 1,238
quantity/unit corrections. Only three records in this water cohort were not
already edited by earlier curation. The [remaining handoff](remaining-handoff.json)
pins 2,658 unchanged water candidates and three unedited glycerol-unit leads;
those are triage, not newly verified quantities.

No medium merge input is changed by this batch. Generated media and pages are
not edited or published; the preceding global merge failures remain unresolved.
The all-record curation and publication workflows are not finished.
