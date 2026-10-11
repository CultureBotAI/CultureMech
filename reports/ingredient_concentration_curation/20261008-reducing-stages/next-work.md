# Remaining Ingredient Work

Superseded by the [M258/M260 follow-up](../20261008-m258-m260-stocks/next-work.md).
M258 and M260 are now repaired locally; the frozen context below remains an
unchanged historical capture and must not be reapplied to those two records.
M247, M272, M273 and M274 remain source-inspected candidates, not applied reviews.

The all-record goal remains incomplete. Follow-up coverage is 11,779 of 15,910
exact normalized paths, leaving 4,131 outside this report set. Covered records
can still contain unresolved claims. The M142-dependent queue now contains
73 unchanged records in `remaining-queue.json`.

## Next Source-Inspected Candidates

`next-six-context.json` has SHA256
`f04c81701b42a8961942d5f954d454e494edcd16c82be6424cb3c10b0af659dd`.
It freezes unchanged complete baselines for M247, M258, M260, M272, M273 and
M274 plus 15 archived official source captures. The six full current YAMLs,
TOGO quantity tables and JCM recipe text were inspected. This is read-only
preparation, not a fresh-source check, applied review, or coverage increment.

### M258 Requires An Identity Repair

M258/JCM266 has 660 ml main water and 20 ml fatty-acid-stock water collapsed
to 680 g/L. Its 300 ml clarified-rumen-fluid and 20 ml fatty-acid additions
are still root ingredients. Restore these separate preparations and the
M142/M190 stock boundaries without inventing final volumes.

The current record also has three LB-commercial-product ingredients: Tryptone
10 g/L, Yeast extract 5 g/L and Sodium chloride 10 g/L, plus a root LB-product
provenance paragraph. The inspected exact TOGO and JCM266 recipes instead list
alpha-methylbutyric acid, 0.5 g, in the fatty-acid stock. That ingredient is
missing from the current record. Do not preserve the unrelated LB expansion
as an asserted formulation, or silently erase its provenance. Investigate the
edit history/source capture and explicitly supersede the wrong product claim
with supporting evidence, preserving append-only history. Do not invent a
chemical grounding for the restored acid.

The replacement is directly verified in historical commit
`7e8bd7c6026306323b6d86bc0238fa35b8fa1d17` (2026-03-28), at the former
`data/normalized_yaml/bacterial/TOGO_M258_Methanomicrobium_Mobile_Medium.yaml`
path. `git show` demonstrates that alpha-methylbutyric acid was removed and
replaced by those three LB ingredients and the product paragraph. The commit
names `culturebotai-claw/scripts/expand_commercial_product.py`. Its current
sibling-checkout version was inspected read-only (SHA256
`b025762b4e734715c691dda7e95c59cdea1ff10bd5452049500ba151be80e417`). Both
discovery and replacement use `any(pattern in term ...)` after lowercasing.
A read-only expression check confirms that `lb` matches within methylbutyric.
This reproduces the failure mode if `lb` is an alias; it does not prove the
historical invocation/configuration. An ignored-inclusive `find` of CultureMech
and culturebotai-claw did not locate `lb_composition.yaml`. Do not run the
expansion tool to test this: its CLI writes by default. No sibling files changed.
An ignored-inclusive filename search of data/scripts/reports found the current
record and its earlier structural report; that report explicitly has zero
source-checked rows and is not validation of the LB substitution.

The other three fatty acids each have 0.5 g source amounts. Concentrated NaOH
adjusts only that stock to pH 7.5; no concentration is specified. Rumen-fluid
preparation gives heating at 120C for 15 min and centrifugation at 25,000 x g
for 15 min. Do not convert g-force to rpm or use an unrelated action enum.
The unquantified clarified-fluid row is an extraction/product description,
not an additional independent dose. Preserve the receiving-medium pH 6.5,
overnight rest and two separately prepared reducing agents without assuming
a 5% basis or dose.

### M273/M274 Are Source Variants With A Conflict

Both point to the same original JCM280 page, but M274's TOGO accession is
`JCM_M280-2`, not a separate `GRMD=280-2` source. The original comment explicitly
describes 5.0 g/L maltodextrin with sulfur omitted. M273 retains sulfur;
M274 contains maltodextrin and omits sulfur. Preserve this distinction and
review typed reciprocal variant links rather than merging by shared name.
M273 already has a pH-variant child M345; preserve that independent relationship.

Both TOGO versions list FeSO4 heptahydrate as 0.025 g (25 mg), while the original
JCM280 table says 2.5 mg. This is a tenfold source disagreement, not a unit-only
conversion. Record both excerpts and their source versions; do not silently
select or average them. The 5.0 g/L maltodextrin exception does not establish
final-volume denominators for the rest of either recipe. M274 must not inherit
the sulfur steaming/addition instructions from the unmodified base recipe.

### Other Prepared Candidates

- M247/JCM255: water is 1 L input plus two 10 ml stocks, not explicit final
  volume. Preserve initial pH 6.0 and optional 5.5-6.0 readjustment, filtration,
  H2-CO2 4:1 dispensing atmosphere, and subsequent 79:20:1 H2-CO2-O2 gas
  replacement/200 kPa. Do not add N2 or a guessed acid.
- M260/JCM268: 900 ml main water and 1 L local-stock water were collapsed to
  901 g/L. The 100 ml MJ(-N) seawater input is still a root ingredient. M142's
  10 ml trace-mineral dose belongs INSIDE that local seawater stock, not directly
  to the receiving medium. Preserve exact salts and pH 7.5 without inventing a
  stock denominator or final-medium concentration.
- M272/JCM279: preserve its own pH 7.0, autoclave/overnight stages, 20 ml medium
  in 120 ml bottles and subsequent 15 ml filter-sterilized air addition before
  pressurization. The air amount belongs to that vessel preparation, not a
  per-liter gas amount or dissolved concentration. Do not inherit M247's O2
  fraction, phosphate, NaCl, vitamins or filtration sequence by analogy.

Before application, refresh the exact official sources, recheck all baselines,
preview each claim, run baseline gates and independent audits, and test record-
specific differences and guarded application. Do not mutate the frozen context
to conceal a changed baseline or source disagreement.

## Other Outstanding Work

J151/M142 bibliography-title mismatches remain described in
`../20261008-recipe-reference-validator/next-work.md`. Global merge verification
and generated-data freshness remain unresolved. No tracked merged YAML was
hand-edited in this five-record repair.

The prior issue #150 progress draft remains unposted following the external-
disclosure rejection; no new authorization has arrived. Do not retry through
another channel. Commit/push/PR/merge/branch cleanup remains unfinished; local
ingredient curation can continue.
