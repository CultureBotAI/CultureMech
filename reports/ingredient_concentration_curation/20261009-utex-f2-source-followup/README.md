# UTEX F/2 Source Follow-Up

## Read-Only Research, Not Applied Curation

This is the historical research stage. The subsequent
[F/2 curation batch](../20261010-utex-f2/README.md) now records local recipe
edits and their validation separately. In that batch, the previously
inaccessible cyanocobalamin ChEBI entry was retrieved and verified as
`CHEBI:17439`; the read-only observations below are retained as their original
research checkpoint, not current mutation or coverage totals.

The complete `data/normalized_yaml/algae/F_2_Medium.yaml` record was read as a
CHEV component and as a lead for subsequent ingredient review. Its normalized
bytes remain unchanged. This follow-up adds no curation events, concentration
edits, per-record coverage or organism associations.

[Source captures](source-captures.json) pin five official pages, their tables
and the linked F/2 PDF. HTML sources were inspected on 2026-10-09; the rendered
F/2 PDF page 1 was also visually inspected. The capture receipt's
`manual_pdf_inspection_asserted: false` describes the earlier retrieval stage,
not this subsequent inspection. The inspected image hash is
`b6630a18e10412cb548098beef3608abf034f2d60ee4991e5a61f6bfbd683d65`.

Source type is culture-collection page; discovery is the existing record URL
followed by linked stock recipes. Publisher: UTEX Culture Collection of Algae.
Named recipe authors and publication years were not established. Website
copyright years and the site's designer are not recipe authorship metadata.
This statement concerns the initial five pages; the subsequently inspected
8 ppt variant PDF has its own explicit revision date, recorded below.

## Findings To Resolve

1. The parent currently encodes makeup seawater as 1000 mL/L of ingredient.
   The [official F/2 page](https://utex.org/products/f-2-medium) instead specifies
   an initial seawater charge followed by makeup to a total volume. Capture that
   preparation distinction without treating 1000 mL as the seawater amount.
2. The F/2 table names phosphate monohydrate. The record carries a generic
   sodium-dihydrogenphosphate label in its two chemical mappings. Verify the
   exact hydrate grounding before proposing any identifier correction.
3. The [Trace Metals Solution](https://utex.org/products/trace-metals-solution)
   specifies a one-liter stock preparation, mass amounts, a molarity column,
   and a note assigning that column to stock concentration. Reconcile that
   combination explicitly; do not silently substitute receiving-medium
   concentrations for stock composition or infer a molecular-weight correction.
4. [B12](https://utex.org/products/vitamin-b-12),
   [biotin](https://utex.org/products/biotin-vitamin-solution), and
   [thiamine](https://utex.org/products/thiamine-vitamin-solution) use a buffered
   stock-preparation stage. The parent copies separate water nodes at 1000 mL/L.
   Review those solvent amounts against the buffer directions, rather than
   assuming they are independently measured final-stock concentrations. Preserve
   the approximate qualifiers printed for biotin and thiamine molarities.
5. The B12 source explicitly specifies cyanocobalamin; the thiamine page provides
   a supplier catalogue number. Check supplied chemical forms separately from
   quantities before attaching form-specific concentration evidence.
6. The linked [F/2 PDF](https://web.biosci.utexas.edu/utex/Media%20PDF/f-2-medium.pdf)
   and HTML agree on the ingredient table but differ in preparation detail: the
   PDF has 30-35 ppt seawater and autoclaving, whereas the HTML specifies 30 ppt
   and offers filtration as an alternative. Do not combine them into an undated
   synthetic protocol or claim complete version agreement.

The parent includes three literature-specific inline variants and existing
organism evidence. These were read but their articles were not independently
reviewed in this follow-up. The UTEX sources cannot certify those claims.

## Four Variant Sources Inspected

The whole normalized records below were also read, followed by their official
HTML recipes and PDF page images on 2026-10-09. Their normalized data remains
unchanged. [Variant captures](variant-source-captures.json) preserve source
URLs, source hashes, tables, directions and rendered-page hashes. This is
source research, not completed claim-level review or additional report coverage.

| Exact normalized path under `data/normalized_yaml/algae/` | Stable ID | Source-specific observation |
| --- | --- | --- |
| `1_F_2_Medium.yaml` | `CultureMech:000012` | 285 mL initial seawater and 600 mL water precede seawater makeup to 1 L; makeup volume is not independently quantified. |
| `5_F_2_Medium.yaml` | `CultureMech:000020` | 15 g sea salt is dissolved in approximately 900 mL seawater, followed by makeup to 1 L. The table's seawater `1 L` is not an independently measured input. |
| `8_ppt_F_2_Medium.yaml` | `CultureMech:000021` | Approximately 950 mL of 8 ppt seawater precedes makeup to 1 L. Both captured sources specify autoclaving, not the record's alternative filtration step. |
| `f_2_nh4_medium.yaml` | `CultureMech:000169` | F/2 is dispensed in 175 mL aliquots into 250 mL flasks before an unquantified pinch of ammonium magnesium phosphate is added. |

The [1% recipe](https://utex.org/products/1-percent-f-2-medium) and
[5% recipe](https://utex.org/products/5-percent-f-2-medium) each report silicate
stock at 2 g/100 mL and a final concentration of 70 micromolar. The
[8 ppt recipe](https://utex.org/products/8-ppt-f-2-medium) instead reports
3 g/100 mL and 106 micromolar, like the parent F/2 recipe. These differences
must not be erased by inheriting the parent's ingredient amounts.

The 1% HTML gives initial seawater salinity as 30 ppt; its PDF gives 30-35 ppt.
The 5% HTML and PDF exclude vitamins from initial mixing but do not supply a
later vitamin-addition step. The table still lists the vitamin doses. Record
this preparation gap rather than importing another formulation's procedure.
The [ammonium recipe](https://utex.org/products/f-2-nh4-medium) provides no
mass for the pinch in either source; vessel capacity is not the aliquot size
and neither establishes a final post-addition concentration.

The [8 ppt PDF](https://web.biosci.utexas.edu/utex/Media%20PDF/8-ppt-f-2-medium.pdf)
explicitly says `Updated: January 2020`. That is a document revision date,
not a publication year inferred from the website copyright. The other three
inspected variant PDF pages have no established revision date in this review.

Visually inspected page-1 image SHA-256 values:

| Variant | SHA-256 |
| --- | --- |
| 1% | `7391e85877e1eeadafb4e0b6b433232f406c3c3676d1f00d4ee733738c3f9fe5` |
| 5% | `59fb8d70be6d5c9f70204c5aa49eccbba8728f2c6fb7b0bc93261bd66a161a3c` |
| 8 ppt | `f83f4230cd67cf7e59292aa071f82e12f166e6680f2b3d9c7ec710f6abfcf4d1` |
| F/2 +NH4 | `069bf2353bce04884692de8c56016fbf37059859e92e8110810433b1dd9ec928` |

The capture receipt's `manual_pdf_inspection_asserted: false` predates this
visual inspection and is retained as a truthful retrieval-stage record.

## Chemical Identity Follow-Up, Not Applied

Primary database/product pages were inspected on 2026-10-10 UTC (2026-10-09
local time). These sources establish identity candidates, not recipe doses.
Discovery mode is an ontology-ID lookup or the catalogue identifier in UTEX's
stock recipe; source type is chemical database or supplier product page.
No recipe authorship or publication year is inferred from database update dates.

- The four expanded F/2 formulations map their explicitly named phosphate
  monohydrate to `CHEBI:37585` in both chemical slots. That
  [ChEBI entry](https://www.ebi.ac.uk/chebi/CHEBI:37585) gives the non-hydrated
  formula `H2O4P.Na`. The dedicated
  [monohydrate entry](https://www.ebi.ac.uk/chebi/CHEBI:114249) is
  `CHEBI:114249`, formula `H2O.H2O4P.Na`, with this exact definition snippet:
  "A hydrate that is the monohydrate form of sodium dihydrogenphosphate."
  Combined with each UTEX recipe's own hydrate-labelled row, this supports
  proposing identity corrections; it does not recalculate the reported
  36 micromolar amounts.
- UTEX's thiamine stock names Sigma T-1270. The inspected
  [T1270 supplier page](https://www.sigmaaldrich.com/US/en/product/sigma/t1270)
  names "Thiamine hydrochloride", CAS `67-03-8`, and molecular weight
  337.27 g/mol. The matching
  [ChEBI salt entry](https://www.ebi.ac.uk/chebi/CHEBI:49105) is `CHEBI:49105`;
  its CAS and InChIKey `DPJRMOMPQZCRJU-UHFFFAOYSA-M` agree with the product.
  The four inline stocks instead carry
  [`CHEBI:18385`](https://www.ebi.ac.uk/chebi/CHEBI:18385), the isolated
  thiamine(1+) ion. This supports a salt-identity proposal, not converting
  their retained 0.335 g/L using the cation's molecular weight. The current
  product page is not a certificate for a historical UTEX reagent lot.
- The four B12 stock nodes use
  [`CHEBI:176843`](https://www.ebi.ac.uk/chebi/CHEBI:176843), a vitamin-B12
  vitamer class. UTEX specifically names cyanocobalamin. A specific replacement
  identifier remains pending: attempted cyanocobalamin ChEBI page retrievals
  failed, so no replacement is claimed verified from search excerpts.

These findings remain unimplemented and do not change the inventory's pending
claim dispositions. Source amount evidence must still come from the exact UTEX
recipe/stock, not from the ontology or supplier page. Complete source capture
and pinned claim previews remain prerequisites for a subsequent guarded batch.

## Scope Boundary

[The read-only inventory](source-lead-inventory.json) searches all normalized
YAML, including ignored and hidden files, for the nine captured source URLs
and F/2 source identifier. It identifies 31 exact git-tracked source-mention
paths and no untracked matches. Five are the bounded F/2 family above, including
the parent; the remaining 26 are additional leads, not reviewed formulations.
The initial inventory attempt stopped before writing because the parent/stock
URL search did not include every family member; the terminal inventory adds
the four variant source URLs explicitly.

The five family records have 105 structured concentration fields: 25 in the
parent, 27 in 1%, 26 in 5%, 25 in 8 ppt and two in F/2 +NH4. The inventory
preserves each field's old amount, chemical mappings, notes and evidence, plus
preparation, references and relationships. All decisions remain pending. The
parent's narrative literature-variant amounts are recorded separately and are
not included in the 105-field count. Shared URLs do not establish identical
stock doses or a complete semantic recipient set. No sibling or stock record
is claimed absent or equivalent on this basis.

Hashes of all 15,910 normalized records were unchanged across inventory
generation. No validation or scientific pass is implied by inventory success.
Next: reconcile the source conflicts and chemical forms, produce claim-level
previews for the bounded family, then run baseline/proposed validation before
any guarded edits. Each additional recipient requires its own dose evidence.
