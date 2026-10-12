# Water Input Follow-Up Review

## Open Findings

- **Publication remains gated.** Full reference validation fails for API/PDF
  title extraction and PDF supporting-text retrieval. Manual PDF verification
  and the nine passing API snippet checks do not turn that command into a pass.
  The initial restricted-network failure and successful-fetch retry are both
  retained. The terminal global merge rerun fails with 1,247 name conflicts and
  3,287 fingerprint issues. Freshness also fails: 3,720 tracked-only paths, 3,898
  fresh-only paths and 1,700 changed shared paths. The fresh run skips 342 recipe
  inputs in addition to the expected standalone-solution exclusion. Earlier
  evidence-retention failures outside these six media are not resolved here.
- **Review coverage is not scientific completion.** Three legacy placeholder
  concentration rows are explicitly unsupported and unchanged. Chemical mapping,
  atmospheric-note and older source-scope issues are outside this water-only
  repair. No entire record is declared scientifically resolved by this batch.
- **Water amount does not prove final volume.** The API/PDF water rows support
  1000 ml of input water. They do not establish a final-medium volume, water
  density, percentage or downstream dilution. Existing non-water `g_l` claims
  remain scoped to the provider's declared recipe concentrations.
- **Repeated records do not multiply independent evidence.** The nine records
  represent three linked formulations. The API and original PDF share a provider;
  these are not eighteen independent scientific confirmations. Concentration-
  independent fingerprint grouping does not establish formulation identity.

## Checked And Addressed

- All nine full before-records and the exact source inventories are frozen.
  Medium-to-solution links are explicit, paired API amounts agree, and water rows
  match the original PDFs. The complete context hash is pinned in both mutator
  and independent audit.
- The guarded mutator rejects changed identifiers, record contents, units,
  quantities, source hashes/URLs/status, PDF text and mapping. Preview is default;
  apply is explicit. Whole-batch preflight prevents writes on a late conflicting
  input. A no-op reapplication does not duplicate history or evidence.
- An independent audit restores each changed record to its entire frozen
  before-object after reversing only the water quantity and new provenance.
  Mutation tests reject altered non-water amounts, misleading final-volume
  scope, fabricated snippets, rewritten history and invented publication year.
- The nine reports list all 57 concentration slots without adding duplicate
  exact-path review headers. An early table-formatting defect was corrected
  before application. A later scratch assertion assumed backticks around field
  labels; its failure is preserved and the separate corrected check passes.
- Historical plans and expected hashes were not rewritten. Tests and historical
  readbacks explicitly follow the new source-pinned successor plan.
- Actual merger execution retains the corrected water amount, both full evidence
  entries, input note, reference and event for all six media. Standalone solutions
  remain outside medium merge groups. This is narrower than global merge health.

## Limits

This is a local adversarial review, not a GitHub PR review or issue closure.
The checks ran in a partial locked Python 3.13 environment. Full CI, global
publication readiness and completion of all concentration comments remain
unproven. No generated merged data or pages were manually edited.
