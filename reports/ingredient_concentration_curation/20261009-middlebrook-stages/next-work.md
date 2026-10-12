# Remaining Ingredient Work

The 13-record Middlebrook stage repair is applied, not all-record completion.
The current remaining identity context has 87 unchanged records: 76 acid-name
candidates and 11 linked Middlebrook candidates. Preserve the separate 71-record
M142 queue. These queues are not additive to the 4,112 paths outside follow-up
reports, and covered records can still have unresolved scientific claims.

## Next Linked Middlebrook Batch

All 11 current YAMLs were read in full during this turn: DSMZ 645/911,
KOMODO 645/645a/911, five KOMODO 645 strain entries (44338, 44339, 44482,
44483, 44680), and KOMODO 911_44536. Their hashes still equal the baselines in
`../20261008-lactalbumin-formulations/next-middlebrook-context.json`.
That immutable 24-record context also contains the now-applied 13 records;
exclude those 13 when constructing the next guarded cohort.

All nine KOMODO recipe/feature tables, both DSMZ API responses, and the three
original PDF page images (645, 645a, 911) have been inspected. The sources are
captured, not a completed per-record proposal, and need freshness validation
before applying a future edit. No edits, review-coverage increment, or growth
association is claimed for these 11 candidates yet.

### Verified Local Problems

- All nine KOMODO YAML histories explicitly say they copied DSMZ composition.
  The 645a YAML consequently omits its own source's hemin and NAOH entries.
  Its current 7H10 commercial powder is additionally mapped to pure agar.
- The 645 group contains copied powder plus basal ingredients plus flattened
  OADC stock rates. The actual KOMODO tables report different rates, including
  albumin 2.49 and agar 7.48 in the per-liter Gram Amount column. Water and
  glycerol have null amounts. Never convert null to zero or reuse copied 5 g/L.
- KOMODO 645a reports hemin 0.04 in Gram Amount, albumin 5.00 and agar 15.00.
  Its original PDF states 60 micromoles hemin and dissolution in 1N NAOH,
  without a volume denominator or NaOH dose. This does not establish 60 uM or
  independently verify a mass conversion. The KOMODO table has no glycerol row;
  do not claim that omission proves a glycerol-free experimental preparation.
- The two KOMODO 911 tables report albumin 2.49 and agar 8.31 per liter, while
  the copied YAMLs still hold DSMZ stock rates. Their genuine pancreatic casein
  digest and NaCl must not be deleted with the false LB constituents.
- The current 645a parent has seven SOURCE_DUPLICATE children: five strain
  records, plain KOMODO 645 and DSMZ 645. The hemin-containing source is not an
  exact formulation duplicate of the plain entries. Reconcile both directions
  of each link; do not reparent by label similarity or create a cycle.
- DSMZ 911 -> KOMODO 911 -> KOMODO 911_44536 links are also SOURCE_DUPLICATE.
  Source-specific quantity encodings and the explicit strain-modified title
  require review; a shared copied ingredient signature is not identity proof.

### Preparation Decisions Still Required

DSMZ 645 presents a commercial 19 g powder route using 900 ml water plus 5 ml
glycerol, and a distinct from-scratch alternative whose table lists 1,000 ml
water. OADC is added later at 100 ml. Do not count both preparation alternatives
or sum their water inputs. The API's 20.9945 g/L powder rate is provider-derived
from a 905 ml encoding, not a verified final-medium concentration.

DSMZ 911 specifies 21 g commercial 7H11, 900 ml water and 5 ml glycerol, then
100 ml OADC after cooling. The detailed basal table itself also lists 900 ml
water. Its API powder g/L and individual basal g/L fields have different
normalization contexts; do not treat them as additional simultaneous inputs.

Keep exact per-source amounts and ambiguity. No mechanism producing the
KOMODO/DSMZ discrepancies has been proven, so do not label them as a verified
dilution calculation. All nine KOMODO PH Info values are null. The provider's
secondary chemical-name columns sometimes differ from the displayed name
(for example pyridoxine/HCl); existing chemical groundings are not thereby
recertified. Original supplier specifications have not been inspected.

## Other Open Work

The [NBRC reference matcher](../20261009-nbrc-reference-validation/README.md) is
now repaired for the inspected 1219 page without changing recipe evidence.
The [next eleven-record source inventory and decisions](../20261009-middlebrook-linked/decisions.md)
are prepared, not applied. Continue the 41 earlier PDF bibliography
title mismatches, source-conflict and reducing-stage reviews, M2410 addition
order, global merge/freshness and the remaining corpus. Publication remains
unapproved after the earlier outbound-payload rejection; do not bypass it.
Each further data edit requires its own source-linked snippet in YAML,
guarded preview, append-only history, independent audit and validation.
