# Adversarial Review

## Findings Addressed

1. **Water units were dimensionally wrong.** Medium 467 and solution 959 use
   1000 ml of tap-water input, not 1000 g/L or a percentage. Source row and PDF
   snippets support 1 L. Existing chemical mappings remain unchanged.
2. **Medium 469 flattened two filtered preparations.** The MgSO4 hydrate and
   catalase input rows belong in separate preparations. Merely attaching the
   API's flat `g_l` fields would endorse the wrong stage. The fix relocates both
   nodes, preserves their mass inputs with snippets, and leaves stock strength
   and numeric stock dose unasserted.
3. **API and PDF details must not be blended.** Only the API gives 980/10/10 ml
   allocation. The PDF's unpartitioned 1000 ml is preserved as a source-detail
   difference, not described as independent confirmation of the API allocation.
4. **The history verifier rejected legitimate later curation.** KOMODO 467
   already had an evidence-curation event. The old verifier required that event
   to remain last. It now requires an explicit hash-linked successor, exact
   mapping evidence/reference preservation, and preservation of the original
   history prefix. Tests reject an unannounced successor and loss of the old
   event. No arbitrary later history event is accepted as authorization.
   The initial post-apply tests exposed a diagnostic-order regression: mapping
   tampering was rejected by the hash check before the more specific provenance
   check. Both guards remain enforced; checking provenance first restores the
   precise error. The initial failures and subsequent reruns remain separately
   recorded in the validation journal.
5. **The retention checker assumed a literal `solution` batch key.** This batch
   has two solution records with different keys. The checker now recognizes the
   explicit `SolutionRecipe` class; it still verifies that neither participates
   in medium merge groups. This is not permission to skip media that fail merge
   retention.

## Guards And Remaining Limits

The bounded mutator refuses changed source bytes, altered preparation/water
allocation, wrong hydrate or catalase attribute, altered unit/volume/identity,
optional ingredient drift, concurrent target edits, symlinks, untracked or
case-drifted paths, plan tampering and preview overwrite. Its all-target
preflight precedes any write. Independent inversion tests reject invented stock
strengths/doses, changed mappings/history/pH, incorrect stock-stage instructions,
fabricated excerpts and erased source differences.

This is a self-contained adversarial test/review pass, not an independent human
review or hosted PR review. Whole-project dependency availability and actual
merge/provenance retention are separate checks in validation.json. Stock final
volumes, measured final-medium concentrations, exact unrelated variants and
other corpus findings remain unresolved. No GitHub issues were created by this
batch.
