# Remaining Ingredient Work

Superseded handoff: M194/M213/M244/J252 were subsequently repaired in the
[albumin-counterparts batch](../20261008-albumin-counterparts/README.md).
Use its [next-work](../20261008-albumin-counterparts/next-work.md) for the current
queue. The baselines and remaining-work descriptions below are historical.

The all-record goal is active and incomplete. J201/J220 are applied locally.
Coverage remains 11,781 of 15,910 exact normalized paths, with 4,129 outside
follow-up reports and unresolved claims within covered records.

## Frozen Queues

`next-lb-identity-context.json` retains 115 unchanged candidates: 76 acid-name
and 39 albumin-name substitutions. SHA256:
`b2e456d6d6a818d1b3952e26da2cdcf4e63dfb40b3caf1dc6b083d6185715d89`.
It links to the prior 117-record snapshot without rewriting that history.
The separate M142 queue remains 71 unchanged records in `remaining-queue.json`.
The queues are disjoint and are not additive to the uncovered-path total.

## Next TOGO Counterparts

`next-togo-context.json` pins two complete current baselines, two freshly fetched
TOGO responses and the four previously inspected J201/J220 responses. SHA256:
`0571cffa25db4745c96da9b9e67a9357865cfef582c6c3b2f6c4056505afe2df`.
All source bodies and both current records were read. The JCM201 body is explicitly
an unavailable-recipe response, not formulation evidence. No TOGO record was edited.

An ignored-inclusive search under `reports/ingredient_concentration_curation`
found no canonical `- Record:` line for either TOGO path. Recheck before creating
their reports; unlike J201/J220, these may require canonical reports rather than
supplemental `- Follow-up target:` reports.

### M194

Path: `data/normalized_yaml/bacterial/TOGO_M194_BSK_Medium.yaml`

ID: `CultureMech:008529`

Baseline SHA256:
`556940ee8975e500fcb09d72d3c1e4a8c34962248367fa9f23098e8ad2a8d192`

The record has 14 ingredients/quantity fields and eight history events, with no
current pH or preparation steps. The exact TOGO response identifies `JCM_M201`,
one component table with 12 rows, and one preparation comment.

- Remove only LB supplier nodes at indices 7-9. Restore `Bovine albumin, Fraction V`
  from its own 50 g row; do not assign a chemical ID from the source's GMO alias.
- Gelatin at index 0 is the 200 ml dose of a 7% preparation, not 200 g/L gelatin.
  Its table row and preparation comment describe the same addition, not two doses.
  Preserve the old gelatin annotation on the appropriate component without
  guessing percentage basis, stock mass or solvent volume.
- CMRL 1066 at index 11 is a 100 ml product input. Preserve the source's product
  qualifier and existing name spelling; no stock composition is supplied.
- Water at index 1 is 900 ml of batch input. The later gelatin and serum additions
  preclude inferring a one-liter final-medium rate from water plus CMRL.
- Sterile rabbit serum at index 13 has an invented VARIABLE placeholder. The
  source supplies final 6% but no basis or fixed volume. Retain that qualifier
  without promoting it to a percentage enum or guessed volume.
- The comment supplies pH 7.6, medium filtration and serum-after-filtration order.
  Use FILTER, not a pore-specific action. The source's `Filter--sterilize` and
  `N--Acetyl--D--glucosamine` spellings are literal source text, not permission
  to silently normalize unrelated labels.

### M213

Path: `data/normalized_yaml/bacterial/TOGO_M213_SC_Medium.yaml`

ID: `CultureMech:008734`

Baseline SHA256:
`a08043ac16220f12e9455e769ab5d22e539df1f675d4861f2976d0f7755d7357`

The record has 12 ingredients/quantity fields and eight history events, without
current pH or preparation steps. TOGO identifies `JCM_M220`, one ten-row component
table and two preparation comments. The original JCM220 table is available.

- Remove only LB supplier nodes at indices 2-4. Restore the 10 ml dose of
  `20% Bovine serum albumin, fraction V`; leave the percentage basis unknown.
- The 50% glucose, 10% cysteine and hemin solution rows are doses of 1, 10 and
  15 ml, not g/L. Preserve existing solution-label notes at the right scope.
- Hemin's solvent is 0.05 N NaOH; no stock solvent volume or molarity is supplied.
  Only albumin, glucose and cysteine have explicit separate filtration instructions.
- Water is 1 L of input, not one gram per liter or a measured final volume.
  Retain five solid source batch masses without unsupported final-rate arithmetic.
- Preserve the repaired MgSO4 heptahydrate grounding and history. Do not assign
  a pure-agar grounding to the named corn-meal-agar product by analogy to J220.
  Add source-backed pH 6.6 and preparation order without inventing a pore size.

For both records, validate each exact provider/formulation correspondence. The
newly curated J201/J220 YAMLs are not independent evidence. Use captured TOGO,
MediaDive and available original text, with per-claim PURLs and exact snippets.
Create a fresh guarded preview, run baseline gates, independently account for
every old field and source row, and verify no-op application and merge retention.

## Expanded Four-Record Handoff

`next-four-albumin-context.json` extends the two-record capture with M244/J252
baselines and three freshly fetched responses: TOGO M244, MediaDive J252 and
original JCM252. All nine source bodies have been inspected, including the
unavailable JCM201 response. None of these four candidate YAMLs has been edited.
SHA256:
`a4853a8d073e506bf37fb1952d47551a3b84a94f5429b687c33b13f1340cd7f8`.

### M244 And J252

- M244: `data/normalized_yaml/archaea/TOGO_M244_Sulfophobococcus_Medium.yaml`,
  `CultureMech:009029`, baseline
  `8a950a347a2350e29ea2c05da3e037f6a14760488a003a2943b68f1289605ceb`.
- J252: `data/normalized_yaml/archaea/sulfophobococcus_medium.yaml`,
  `CultureMech:002612`, baseline
  `6632430bd56fae7e7ba70e5396ff40ed1a7b58cf3a9d9d19d9791848c376b0cd`.

The TOGO table has 16 rows, including an unquantified nitrogen-gas row; MediaDive
and JCM have 15 formulation rows. M244 incorrectly stores source milligram
amounts with the same numeric value in g/L. J252 already scales those milligram
amounts to grams, but its final-volume denominator remains unsupported. One liter
of water is a batch input, not evidence of a measured final volume.

Remove only the false LB nodes: M244 indices 10-12 and J252 indices 1-3.
Preserve the genuine yeast extract at M244 index 15 and J252 index 0. J252's
genuine and false yeast nodes have identical names; use explicit path and supplier
provenance, not a name-only lookup or duplicate-rejecting generic constructor.
Restore the source's 1 g bovine serum albumin input with its own evidence.

Both original and TOGO preparation text explicitly specify albumin stock at
10% (w/v). Preserve that supported stock strength. A 10 ml dose can be derived
from the 1 g batch contribution divided by 100 g/L stock strength, provided the
exact stock-to-batch correspondence is independently verified and the arithmetic
is stated outside the quote. This calculation does not establish final-medium
volume. Yeast-extract 10% and neutralized-sulfide 5% bases remain unspecified;
do not infer their numeric strengths or doses by analogy to albumin.

Model separate autoclaving of yeast and neutralized sulfide, filtration of
albumin with no claimed pore size, and anaerobic additions under nitrogen.
Preserve the pH 7.6 measurement context at 80-90 C rather than assuming room
temperature. M244's nitrogen placeholder is not a dissolved-gas concentration.
Retain legacy chemical annotations and glycine links without recertifying them.
Investigate M244's existing `high_metal` flag separately; neither silently delete
it nor present it as verified after correcting the milligram errors.

Canonical-report coverage for M244/J252 has not been checked in this handoff.
Use an ignored-inclusive exact-path search before writing either report. These
source captures and repair constraints do not increment completed coverage.

## Other Outstanding Work

The prior M247/M272/M273/M274 source-inspected baselines, M273/M274 FeSO4 conflict
and variant distinctions, and J151/M142 bibliography gaps remain unresolved.
Global merge verification and generated-data freshness remain separate gates.
Chemical groundings are not all recertified.

The issue #150 progress draft remains unposted after the external-disclosure
rejection; no new authorization has arrived. The historical LB issue draft is
also local. Do not bypass that rejection through another channel. Commit, push,
PR, merge and branch cleanup remain unfinished; local curation can continue.
