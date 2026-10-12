# Adversarial Review

This is local self-review, not an independent human or GitHub PR approval.

## Findings Addressed Before Apply

- Stock-only amounts had been flattened and added across preparations.
  Independent expected source trees now check every constituent and stock
  addition, including separate water nodes and M180's M190 vitamin reference.
- Main-medium pH and stock pH were conflated; a source range was collapsed
  to a midpoint. Main and stock pH are now separately scoped and evidenced.
- Unstated percentage bases could produce plausible but unsupported strength
  and dose conversions. No such conversions are asserted. The preview was
  refined to label full preparation quotations as receiving-medium context.
- Exact source spelling conflict could be hidden by a plausible chemical ID.
  Both source spellings remain explicit, with existing annotations preserved
  but not recertified and no asserted numeric sulfide concentration.
- Initial adversarial annotation tests inadvertently assigned water its
  existing water term in two cases. Corrected tests genuinely alter the
  annotation and the independent audit rejects them.
- Quantity-removal accounting initially counted a split old slot more than
  once. It now counts unique old quantity fields removed.
- The index publication guard stopped twice before writing: first on J151's
  derived enrichment-flag change and then on recipe-statistics change. Both
  are now explicitly bounded to the current generator's direct-only rule;
  source annotations are independently preserved. No blanket acceptance of
  unrelated metadata changes was added.

## Remaining Findings

- Reference commands are red: API-title/URL-fallback mismatches and four JCM
  HTML-table snippet matches. Literal source checks pass but do not replace
  the installed gate. Correct source-aware validation without substituting
  unsupported snippets or declaring the failures irrelevant.
- Legacy merge integrity/freshness remain unresolved. Exact-formulation
  routing preserves these six records separately; it does not justify
  ingredient-set-only consolidation or publication of stale merged outputs.
- The index hierarchy flag is not nested-aware. The annotation is intact in
  YAML, but the generated flag/count no longer includes J151's nested KI.
- Existing candidate duplicate relationships, coarse grounding, M180's metal
  flag, source spelling disagreement and preparation ambiguity need further
  evidence or scoped follow-up. They are not silently reclassified.

## Tests

The six-record repair has 91 focused tests. Together with the 56 existing
methanogen repair tests, 147 passed. Checks cover wrong units and concentrations,
water quantities, removed/extra stocks, changed annotations, invented excerpts,
history changes, invented publication years, wrong pH, inferred percentage
strength, baseline/capture drift, omitted old claims, forged plans, concurrent
edits, preview non-mutation, applied readback and no-op reruns.

The prior three-record builder remains byte-for-byte compatible with its
frozen plan after adding optional dependency inputs to the shared helper.
The cumulative diff auditor validates the new six-record repair before
inverting it into the earlier audited state.
