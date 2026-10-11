# Geobacter Formulation Source Chain

State: read-only source investigation on 2026-10-09. No record edits, new
evidence entries, growth associations, or canonical review-coverage increment.
This supplements the pinned 56-record inventory in `source-review.json`; it
does not certify all 1,628 ingredient claims.

## Inspected Sources

Discovery mode for all sources below: `cross_reference`. Source type:
`journal_article`. Access date: `2026-10-09`. Subscripts and line breaks in
short scan transcriptions are normalized; no automated OCR pass is asserted.

1. Lovley et al. (1993), DOI `10.1007/BF00290916`. The
   [author-hosted scan](https://davidcwhite.org/fulltext/304.pdf) was inspected
   on printed pages 336-339 and 343. Page 337 cites Lovley and Phillips (1988b);
   the bibliography on page 343 identifies that article. Table 2 on page 339
   distinguishes utilized donors from conditions tested without utilization.
   Neither that table nor cytochrome assays justify indiscriminate positive
   growth assertions. Absence of a vitamin requirement does not mean the
   routine recipe omitted vitamins. Bibliographic metadata and PDF hash are
   recorded in `source-review.json`.

2. Derek R. Lovley and Elizabeth J. P. Phillips (1988),
   *Novel Mode of Microbial Energy Metabolism: Organic Carbon Oxidation Coupled
   to Dissimilatory Reduction of Iron or Manganese*, DOI
   `10.1128/aem.54.6.1472-1480.1988`, PMID `16347658`.
   [PMC article](https://pmc.ncbi.nlm.nih.gov/articles/PMC202682/).
   Printed pages 1472, 1473 and 1479 were visually inspected. The FWA-Fe(III)
   paragraph on page 1473 names sodium acetate, transcribed as
   `NaCH3COO, 6.8`, in its mass-per-liter ingredient list. This is a lead for
   resolving the 1993 generic acetate label, not permission to assume an
   acetic-acid molecular weight. Vitamins and trace elements cite reference
   24; page 1479 identifies Lovley, Greening and Ferry (1984). The 1988 iron
   dose differs from the later article, so those conditions are not identical.

3. Derek R. Lovley, Richard C. Greening and James G. Ferry (1984),
   *Rapidly Growing Rumen Methanogenic Organism That Synthesizes Coenzyme M and
   Has a High Affinity for Formate*, DOI `10.1128/aem.48.1.81-87.1984`,
   PMID `6433795`.
   [PMC article](https://pmc.ncbi.nlm.nih.gov/articles/PMC240316/).
   Printed pages 81-82 were visually inspected. Page 81 specifies a 1% v/v
   addition of each stock in that article's medium and cites reference 1 for
   both stock recipes. Its trace-stock modifications are 0.025 g/L sodium
   molybdate and 0.024 g/L nickel chloride hexahydrate. The latter is explicitly
   hydrated; the molybdate formula in this modification does not name a hydrate.
   The earlier 1979 molybdate dose must not override this modification. A stock
   recipe and a stock dose in this article do not independently establish the
   dose used in every 1993 condition.

4. W. E. Balch, G. E. Fox, L. J. Magrum, C. R. Woese and R. S. Wolfe (1979),
   *Methanogens: Reevaluation of a Unique Biological Group*, DOI
   `10.1128/mr.43.2.260-296.1979`, PMID `390357`.
   [PMC article](https://pmc.ncbi.nlm.nih.gov/articles/PMC281474/).
   Printed pages 260 and 262-265 were visually inspected. Table 1 on page 265,
   footnotes c and d, defines the trace-element and vitamin stocks. The trace
   recipe names cobalt chloride hexahydrate, not cobalt sulfate, and manganese
   sulfate dihydrate. The separate mineral-solution footnote is not the trace
   stock. No wholesale replacement of the 1993 medium by this article's media
   is warranted.

## Current Decisions

- Keep all 56 records unchanged until the complete per-record preview exists.
- MEDIADB:416 was read in full. It currently encodes generic acetate at
  113.2 mM, 100 mM ferric oxide, anhydrous calcium chloride, and other forms
  that need reconciliation with the cited supplied chemicals. Do not approve
  a molarity merely because its number resembles a mass conversion.
- Preserve an explicit distinction between an amount of Fe(III) and an amount
  of oxide formula units. The source's approximate iron dose is not an exact
  pure-Fe2O3 molarity.
- The earlier eight candidate omission conflicts remain conditional findings,
  not eight approved deletions. Check acceptor-specific quantities and the
  relationship between Methods and Table 1 for each record. Balch's trace
  stock also contains calcium chloride: omission of the basal calcium dose
  must not silently erase a separately supported trace-stock contribution.
  Reconstruct the two preparation stages before changing the combined node.
- Resolve the two database cobalt variants against the inspected chloride
  stock and any source-version evidence. Do not label sulfate as primary-source
  verified or silently collapse it into the chloride variant.
- Check the full vitamin and trace-stock chain, dilution denominator, and
  exact hydrate identities before deriving final concentrations. Existing
  direct ingredient entries may also conceal stock-preparation boundaries.
- Preserve prior evidence and repairs in MEDIADB:430 and MEDIADB:460. This
  source follow-up does not supersede their earlier dispositions.

## Capture Integrity

Raw captures are outside the repository in the existing temporary source
directory. These hashes pin the inspected content, not its scientific meaning.

| Capture | SHA256 |
| --- | --- |
| PMC202682-p1472.png | `449ad076df43020f9772de763f133a2a7c93be56575d8435c4930c9aac0228a2` |
| PMC202682-p1473.png | `82aae7d14cd71f7e1c5dad018a53c13c0bfd8630a858c43486fd4a2ee278d4a6` |
| PMC202682-p1479.png | `d967c94b4e2d80631e6724ab08fccfa126e1a1b3c105382017a0ef7e846d3343` |
| PMC240316.html | `e7dfca6dfe400195e6e295dac9ea86e7c96c5c10707f6615dfbfced8f4b60be9` |
| PMC240316-p81.png | `1119313adc0f0c16f6d6d4014347acfff322305d78f8e38225f0d8208f9dbf56` |
| PMC240316-p82.png | `779bdc58e3141bf863952fc2bbee3e0eb7b11b9e5a32cb788c0d9797d31e3095` |
| PMC281474.html | `dd007252c2cd5a5eb52cf6fc0b4aab6005b345b19caa5df94b2259f0a6af575c` |
| PMC281474-p265.png | `d9a549faf9225abc6bc3796486de25046fd586e3428ab04db113f4f04faf7e7e` |

The PMC pages expose the scanned-page links. DOI/title metadata was checked
against those pages; a successful publisher-site fetch is not claimed.
