# Remaining Ingredient Work

Superseded handoff: M225, M229, M234, M236 and M243 have since been applied
locally with evidence-backed repairs. See
`../20261008-reducing-stages/next-work.md` for the current queue and coverage.
The earlier frozen candidate context and historical counts below are retained.

The all-record goal remains incomplete. Current follow-up reports cover 11,774
of 15,910 exact normalized paths; 4,136 are outside this report set. Report
presence does not establish resolution of every scientific claim. The unchanged
M142-dependent queue has 78 records in `remaining-queue.json`.

## Next Reducing-Agent Preparation Cohort

`next-reducing-stages-context.json` has SHA256
`d533397760814f2f6a25f877d6d4331041e7f2b6449c590c9528063ef27b96a0`.
It freezes unchanged complete M225/M229/M234 baselines plus ten official source
captures. The complete records and source tables/preparation were inspected.
This is read-only preparation, not a fresh source check or applied review.

- M225/JCM232 has 980 ml water, 10 ml M142 trace minerals and 10 ml M190 vitamins.
  It separately autoclaves cysteine hydrochloride and sulfide as 5% solutions;
  each 0.5 g table amount is a receiving-batch contribution. Percentage bases,
  stock preparation volumes and doses are not stated. Bicarbonate is added
  after brief boiling/cooling, not necessarily as a prepared stock.
- M225 explicitly says to stand the autoclaved medium overnight. It gives
  20 ml in 120 ml serum bottles as an example aliquot/vessel, not a final batch
  volume. Do not turn that example into a concentration denominator. Preserve
  the H2-CO2 80:20 atmosphere and later 200 kPa pressure as preparation context.
- M229/JCM237 collapses 750 ml main water and 1 L stock water to 751 g/L, and
  combines 20 g main NaCl and 27.7 g stock NaCl to 47.7 g/L. Both need explicit
  deaggregation with preserved annotations and audited old-slot accounting.
- M229's 250 ml artificial-seawater input is still a root ingredient, not a
  solution descriptor. Restore that stock boundary and its 11-row table. The
  15 ml M142 trace-mineral input remains a batch dose, not ml/L. Its separate
  5% sulfide preparation specifies pH 7.0; receiving-medium pH is 6.5. Do not
  interchange these stages or infer percentage basis/addition volume.
- M234/JCM242 states 1 L water plus two 10 ml stocks and other later additions;
  it does not establish final volume. Its 8 mg CaCl2 dihydrate, 2 mg FeSO4
  heptahydrate and 1 mg resazurin must not retain g/L assertions. It has the
  same two separately prepared 0.5 g reducing-agent contributions, but does
  not repeat M225's explicit overnight instruction.
- Expand only M142 section 2 (trace minerals, including unquantified KOH) and
  M190 section 1 (vitamins). Do not inherit those parent media or M190's trace
  mineral table/preparation. Preserve exact hydrates and legacy groundings
  without treating concentration evidence as ontology recertification.

Before applying: recheck current baselines, refresh all ten official sources,
run baseline gates, preview every old field/source row, independently audit
quantities and preparation stages, and test deaggregation and no-op behavior.
Keep new numeric concentrations unasserted when the source lacks final volume.

## Later Three-Water Collapses

The full current M236 and M243 records and their archived TOGO/original JCM
tables were also inspected, without editing them or refreshing those sources.
Their original baselines/captures remain in
`../20261008-j261-variant/next-m142-dependents-context.json` and
`../20261008-j261-variant/next-m142-originals.json`. They are not included in
the three-record frozen context above.

- M236/JCM244 combines 500 ml main water and two separate 1 L stock-water
  inputs into 502 g/L. The 500 ml synthetic-seawater input is still a root
  ingredient; the 10 ml Ni-Se-W input and 15 ml M142 trace input are separate
  stocks. Preserve all three stock definitions. The `2 x` label does not
  establish final stock or medium volume. Sulfur is steamed separately;
  sulfide is neutralized/autoclaved separately with an unspecified 5% basis.
  The original specifies 1 N acid at the later pH readjustment, not explicitly
  at the initial adjustment. Keep the H2-CO2 4:1 v/v ratio at its stated stage.
- M243/JCM251 combines 920 ml main water and two separate 1 L mineral-stock
  water inputs into 922 g/L. Mineral solutions I and II are each added as
  37.5 ml inputs, alongside 10 ml vitamins and 10 ml trace minerals. Their
  stock constituents must not be flattened into main-medium rates. Preserve
  its overnight rest and optional pH 6.5 adjustment plus separately prepared
  cysteine and sulfide additions.
- The reused `repair_m142_nested_traces.Review.leaf` currently annotates only
  `[Merged 2 duplicates: ...]` notes. A future repair of these records must
  explicitly handle their three-input collapse annotations and one-old-to-three
  lineage without triple-counting the old quantity correction. Do not assume
  the M208/M209 audit covers this case.

## Other Outstanding Work

J151/M142 bibliography-title mismatches remain described in
`../20261008-recipe-reference-validator/next-work.md`. Global merge verification
and freshness remain separate unresolved work. No generated merged YAML was
hand-edited in this pair.

The issue #150 progress draft remains unposted following the earlier
external-disclosure rejection; no new authorization has arrived. Do not retry
through another channel. The commit/push/PR/merge/branch-cleanup workflow is
still unfinished; local ingredient curation can continue.
