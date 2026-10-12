# Basal Makeup Repair: Self-Review

This is an agent self-review with independent source assertions and adversarial
tests, not a separate human review or a GitHub PR review.

## Checked Before Application

- Each basal recipe explicitly makes up to 1.0 L before pH adjustment,
  heating, and later supplements. Basal rates are nested at that stage; no
  final supplemented volume or fixed dose of heated/titrated basal medium is
  asserted. Water is a makeup reagent, not a fixed 1 L input.
- M975's original table also lists 1 L water. The conflicting fixed-input
  interpretation remains documented rather than silently discarded.
- M809's two later 25 ml doses are absolute batch additions. M823, M853 and
  M975 explicitly specify later additions per liter. Neither is treated as
  a verified final dilution denominator.
- M809's historical 26 g/L water merged 1 L basal makeup with 25 ml reducing
  stock water. Basal makeup and reducing-stock water are now distinct; only
  the former retains the old chemical annotation and superseded history.
- M823 and M853 resazurin is 1 mg, not 1 g, per explicit 1 L basal makeup.
- M975's KOH is a 10 M reagent, with unknown titration dose. The explicit
  1 M glucose stocks have stock-level strengths. Unspecified percentage
  bases remain unresolved; no w/v or final-medium value is fabricated.
- M853 replaces, rather than supplements, the parent's basal calcium chloride
  with magnesium sulfate heptahydrate. Its effective inherited preparation
  uses pH 7.5, not 7.0. Exact source text preserves the parent's instruction
  separately from the child override. Reciprocal links use current IDs/paths.
- Only M142 trace minerals and M190 vitamins are inherited. Separate stock
  batch amounts and stock-specific preparation remain scoped to those stocks.
  No unverified stock final volume is inferred from a water-input row.

## Evidence And Guard Tests

The independent audit reconstructs all source-row memberships without invoking
the mutator, checks all 65 original quantity fields and 133 distinct source
rows across the four reviews, verifies literal excerpts against pinned raw
responses, and accounts for every original ingredient/solution annotation.
All prior history remains byte-equivalent as parsed values; one event is appended
per record. It also checks evidence attachment, reference uniqueness and
bibliographic metadata without inventing authors or publication years.

The new test file passes 92 tests. Deliberately bad water inputs, dose units,
basal/final rates, copied stock compositions, percent bases, missing ingredients,
rewritten history, invented excerpts, gas placeholders, parent/child links,
resazurin units, and KOH/glucose strengths are rejected. Application tests cover
preview, apply, verify, no-op rerun, symlink targets, forged plans and concurrent
edits to the last record before any file is written. The broader focused run
passes 416 tests. See `validation.json` for terminal wider-gate results.

## Remaining Risks

The first default-root strict command exited zero but reported only 15,909
files. The current exact inventory contains 15,910. That first run does not
certify full coverage; `strict-full.json` records the repeat against the explicit
normalized root after the fast suite finished, with required inventory/count
equality. The initial omission's cause was not established. Product validation
exits zero with 91 non-blocking warnings and 96,083 no-adapter skips; it does
not recertify every chemical grounding.

The generated metadata indexer counts only top-level ingredient/composition
nodes for `has_hierarchy_enrichment`. Moving M975's preserved legacy KNO3
annotation into its basal preparation therefore decreases that generated count
by one. The maintained generator produced the indexes; the guarded refresh
accepts only the four reviewed records' structural metadata changes and this
known aggregate effect. The flag is not a complete nested-annotation inventory.
No ingredient annotation was deleted or recertified by this repair.

The corpus-wide merge verification still reports 1,247 name conflicts and
3,287 fingerprint issues. Passing scoped merge retention does not clear those
publication gates. Final medium volumes, unspecified percentage bases, and
unreviewed chemical groundings remain unresolved. Full all-record review,
independent PR review, publication, merge, and branch cleanup remain unfinished.
