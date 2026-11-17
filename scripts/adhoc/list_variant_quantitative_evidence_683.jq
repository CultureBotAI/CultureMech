# Purpose: enumerate source-bound quantitative evidence for claim review.
# Input: a #683 proposal JSON. Output: per-event dose, snippet and locator JSON.
# Issue: CultureMech #683 evidence-granularity review. Date: 2026-11-16.
.records | to_entries[] as $r |
$r.value.variants | to_entries[] as $v |
$v.value.ingredient_changes | to_entries[] |
select(.value.ingredient.concentration != null) |
{path: $r.value.path, record_index: $r.key, variant_index: $v.value.variant_index,
 change_index: .key, ingredient: .value.ingredient.preferred_term,
 concentration: .value.ingredient.concentration, evidence: .value.evidence}
