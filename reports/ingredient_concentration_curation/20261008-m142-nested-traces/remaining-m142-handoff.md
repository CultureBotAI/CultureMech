# Remaining M142-Dependent Queue

The seven records in this folder are applied. The other **91 records** in the
original 98-record queue remain unedited; their exact baseline hashes were
rechecked while creating [remaining-m142-context.json](remaining-m142-context.json).
This is a continuation of the all-record objective, not a replacement scope.
Those pending baselines contain 1,629 direct ingredient/stock quantity fields;
their receiving-source tables contain 1,676 rows before any referenced-stock
expansion. These are inventory counts, not source-verified concentration totals.

Later follow-up: [the M689 repair](../20261008-m689-stocks/README.md) applies one
of these baselines. Its [successor queue](../20261008-m689-stocks/remaining-queue.json)
verifies the other 90 remain unchanged. This 91-record capture is historical.

The remaining-context SHA256 is
`9adb71f8016160cb130f148d329de5e6c53f7c976f91ad1d1732fbd49d41c71f`.
It retains full baseline YAML and references the earlier receiving-source and
original-JCM captures. Captures are source leads, not completed reviews.

## Source Closure

A search of report JSON, including hidden and ignored files, located reusable
M180/JCM187, M190/JCM197 and M431/JCM431 captures. Their response hashes and
HTTP success were rechecked. New HTTP-200 captures add M641/JCM628 and
M401/JCM403. All ten extra captures are in the remaining context.

Inspected definitions:

- M180 section 1 is FeCl2 solution; section 2 is trace element solution.
- M190 section 1 is trace vitamins; section 2 is trace mineral solution.
- M431 section 3 is selenite-tungstate solution.
- M641 section 4 is Modified Wolfe's mineral solution, not a generic trace-metal
  stock and not the complete two-layer medium. Its five rows list water 1 L,
  MgSO4 heptahydrate 0.2 g, calcium chloride dihydrate 0.1 g, KH2PO4 0.05 g and
  ammonium chloride 1 g. JCM628 corroborates that definition. No final stock
  volume should be inferred merely from the water input.
- M401 section 3 is B12 solution: 5 mg vitamin B12 and 100 mL water. JCM403
  corroborates the inputs, but does not independently establish final stock
  volume. The other vitamin/thiamine formulations in M401 are different stocks.
  This capture also supports a later composition follow-up for repaired M1390.

## Decisions Still Required

- 12 records have explicit variant instructions: M197, M198, M361, M396, M440,
  M708, M725, M824, M853, M892, M972 and M1044. Apply those instructions to the
  correct inherited formulation, not as additive duplicate ingredients.
- Four records contain volume-making wording: M809, M823, M853 and M975.
  Determine which preparation stage it governs before calculating any rate.
- 41 records contain per-liter wording. This is triage, not proof that every
  stock in those records uses a per-liter dose.
- 16 original JCM URLs return no recipe, affecting 17 records: M395, M396,
  M397, M708, M725, M751, M824, M892, M923, M1003, M1107, M1241, M1256, M1257,
  M1374, M1375 and M1394. Their TOGO data remain accessible, but do not claim
  corroboration from an empty original page.
- M196/JCM203 and its M197/M198 variants need duplicate sulfide-row handling
  and a source gas-formula conflict review. M274 has a separate tenfold iron
  amount disagreement and a sulfur omission override. M258 contains copied
  ingredients not directly mapped to source rows. These are not safe blind
  unit-conversion cases.

Before the next apply: read complete target records and sources; preserve
chemical annotations/history; preview guarded source-specific changes; attach
exact PURL snippets; independently account for all old and new quantity fields.
Do not count the 91 pending records as reviewed or fully evidence-backed.
