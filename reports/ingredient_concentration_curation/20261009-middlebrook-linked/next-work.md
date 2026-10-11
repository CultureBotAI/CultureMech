# Remaining Ingredient Work

The eleven linked Middlebrook records are applied. The all-record objective
remains open: 76 unchanged acid-name candidates, the separate 71-record M142
queue, and 4,112 normalized paths outside the current follow-up reports remain.
These counts are not additive, and report presence is not scientific completion.

The current coverage inventory's 4,112 outside-report paths have these literal
source prefixes (not inferred collection identities): TOGO 2,860, unspecified
538, MEDIADB 469, UTEX 98, nbrc.medium 75, jcm.grmd 60, MediaIngredientMech 10,
and mediadive.medium 2. They contain 58,199 ingredient, 5,631 stock-addition
and 35 variant-text claim rows needing follow-up. These are structural counts,
not a determination that every value is wrong or every source is unavailable.

The [full family inventory](next-acid-family-inventory-resolved.json) places
the 76 acid-name candidates in 41 ID-resolved components and identifies one
additional neighbor, CultureMech:002222 (Methanobacterium medium VI). There are
21 stale exact references across those components, hidden by the current link
validator's ID fallback. Preserve this extra related scope when selecting later
cohorts; see the [path issue](issue-stale-family-paths.md). The original
literal-path-only inventory is retained as an explicitly weaker preflight.

## Next Allisonella Pair

The DSMZ 1006 record `bacterial/allisonella_medium.yaml` (CultureMech:000422)
and KOMODO 1006 record `bacterial/KOMODO_1006_ALLISONELLA_medium.yaml`
(CultureMech:003506), both under `data/normalized_yaml/`, were read in full.
Their exact unchanged snapshots and three successful source captures are in
[next-allisonella-context.json](next-allisonella-context.json). The original
one-page DSMZ PDF was visually inspected after rendering with `sips`;
`pdftoppm` and PyMuPDF were unavailable in the selected runtime.

The [preflight](next-allisonella-preflight.json) inventories 42 actual API/HTML
recipe rows. It parses all 15,910 normalized records and compares the tracked
set with an ignored-inclusive filesystem inventory. The two records have
reciprocal references with no external neighbors or path/ID/name mismatches.
This is structural preflight, not validation of their exact-duplicate assertion.
Neither record has been edited or counted as newly reviewed by this preparation.

### Verified Problems and Proposed Scope

- Both records contain a false supplier-tagged LB expansion and omit
  DL-2-methylbutyric acid. Preserve the genuine yeast extract, Trypticase and
  NaCl when removing that expansion.
- DSMZ's 3.10 ml volatile-fatty-acid mixture dose is missing as a stock
  boundary. Its seven stock inputs are liquid volumes, including 548.50 ml
  acetic acid and 32.25 ml DL-2-methylbutyric acid, not grams added to the
  receiving medium. Restore stock composition and dose separately. The API
  supplies some stock g/L fields, but the PDF does not verify their density
  conversions; direct ml-to-L batch inputs avoid inventing density or final
  medium concentrations. Do not turn the butyric-acid 129 ml input into 129 g/L.
- DSMZ specifies 0.50 ml sodium resazurin at 0.1% w/v. Preserve the addition
  dose and stock strength separately, with both literals. The 1,000 ml water
  input does not establish final volume after additions. Its API main volume
  of 1,004 ml is a provider encoding, not a measured final-volume statement.
- KOMODO's own table has 21 ingredient rows. All seven acid amounts, water
  and CO2 are null; null is not zero. The provider's Gram Amount rates include
  histidine 7.78, yeast extract/carbonate 3.99 and resazurin 9.97E-4 per liter.
  These do not match all copied DSMZ rates. Do not transfer the separate SEED
  metabolite aggregate concentrations to chemically different ingredient forms.
- KOMODO says `Is Aerobic: true`, while its linked DSMZ preparation uses 100%
  CO2 and anoxic tubes. Preserve the source conflict rather than silently
  normalizing it; no quantitative gas addition or growth claim is supported.
- KOMODO's resazurin and cysteine labels differ from the copied DSMZ labels.
  Review those chemical-form identities explicitly rather than merely using
  case-insensitive or fuzzy aliases. Groundings require their own evidence.
- The current `SOURCE_DUPLICATE` pair relies on a copied composition.
  The explicit DSMZ Instructions link supports considering `DERIVED_FROM`,
  with source-specific amounts and uncertainty; reconcile both endpoints.

Build a new guarded preview, per-claim evidence, independent projection audit,
mutation tests and baseline checks before any write. Preserve stable IDs and
all prior history. Then verify applied claims, no-op behavior, per-record
references, corpus checks, current indexes and runtime merge retention.

## Other Open Work

Keep the remaining 74 acid-name candidates after any eventual Allisonella
repair and the newly identified VI neighbor, the separate M142 queue, the 41
earlier PDF bibliography title
mismatches, reducing-stage/source conflicts, M2410 addition-order question and
the rest of the corpus. Global merge/freshness checks and publication remain
open. Earlier outbound-payload approval remains unresolved; do not bypass it.
Every further ingredient edit requires its own source-linked exact snippet.
