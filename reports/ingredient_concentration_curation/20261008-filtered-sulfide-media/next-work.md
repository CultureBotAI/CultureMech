# Remaining Ingredient Work

M208/M209 have since been repaired locally in
[`../20261008-marine-stock-pair/`](../20261008-marine-stock-pair/).
That cohort's reconciliation and handoff supersede the counts and pending-pair
status below; the frozen candidate context here remains unchanged.

The all-record ingredient goal remains incomplete. Follow-up reports now cover
11,772 of 15,910 exact normalized paths; 4,138 are outside this report set.
Reports can still contain unresolved scientific claims. The unchanged
M142-dependent queue in `remaining-queue.json` contains 80 records.

## M208 And M209 Candidates

`next-marine-pair-context.json` has SHA256
`03204b85c0510e83182322363d7722b7a492f333ed3d3f1e13b8c3f9d6c034c1`.
It freezes both unchanged complete baselines and eight official source captures.
The complete current YAMLs, TOGO rows/comments and original JCM215/JCM216
preparation were inspected, together with the referenced trace-mineral and
vitamin stock tables. This is read-only preparation, not fresh source validation,
an applied repair or completed concentration review.

- M208/JCM215 lists 865 ml water, 125 ml local marine/seawater stock and
  10 ml M142 trace minerals. Their sum is not an explicit final-volume statement.
  Its stored 866 g/L water incorrectly collapses 865 ml main water and 1 L
  stock water. Restore both scopes without losing the historical annotation.
- M208's local marine stock has its own 15-row table including 1 L water.
  Several source milligram amounts are stored as g/L. Preserve the source
  batch amounts, stock dose and unresolved final stock/medium volumes separately.
- Both original JCM215 and TOGO print `NaWO4` for the hydrated tungstate row.
  Do not silently normalize that formula based on its legacy ontology mapping
  or use a molecular-weight conversion. The source formula/mapping discrepancy
  needs explicit context; concentration review does not recertify grounding.
- M208's 1 N H2SO4 is a titrant strength with no dose. Preserve the source
  N2-CO2-O2 ratio of 80:20:1; do not normalize it into percentages or an oxygen
  concentration. Filtration, dispensing and post-inoculation pressure are distinct.
- M209/JCM216 lists 970 ml water and three 10 ml stock inputs: M142 trace
  minerals, its local marine trace elements and M190/JCM197 trace vitamins.
  Restore the 970 ml main water and separate 1 L stock water from the stored
  971 g/L collapsed node. Expand only the named stock sections.
- M209's separate sulfide contribution is 0.5 g per receiving batch. Its
  5% label has unspecified basis and does not establish addition volume.
  Preserve initial pH 6.0 and later pH 6.5 instructions rather than flattening
  them to one pH. Do not inherit JCM197's entire main preparation into M209.
- M209 retains a legacy `high_metal` flag and a hydrate-labelled phosphate
  with a generic ontology annotation. These are not recertified. Moving its
  legacy KNO3 annotation into stock scope may also expose the known index
  generator's top-level-only hierarchy-enrichment limitation.

Before editing: recheck current hashes, refresh all eight sources, run baseline
gates, preview all old fields and source rows, independently audit every
quantity/stock boundary, and test deaggregation, source-specific preparation,
annotation preservation and no-op behavior. Do not borrow M199's explicit
stock-rate exceptions or M206's reagent strengths into these recipes.

## Other Outstanding Work

J151/M142 bibliography-title mismatches remain in
`../20261008-recipe-reference-validator/next-work.md`. Global merge verification
and freshness remain unresolved. The requested publication workflow is not
complete, and no tracked merged YAML is rewritten by this cohort.

The issue #150 progress draft remains unposted after its external-disclosure
approval rejection. Do not retry through another channel without new
authorization. Local ingredient review can continue.
