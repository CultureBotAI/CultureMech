# P1 Primary-Source Handoff

Source acquisition and conflict review only; no P1 YAML change or completed
per-record follow-up is claimed.

Target: `data/normalized_yaml/bacterial/haha_agar.yaml`, `CultureMech:010431`.
The current record still matches the frozen public-medium inventory hash:
`4e307e8786fe54193afc7a2a823f257264942649ac290b4a1d8c4a328c67c840`.

## Inspected Source

Richard Hahnke, *Cultivation of Flavobacteria and other in situ abundant bacteria
from the North Sea*, University of Bremen dissertation, 2013.
The title page gives 24 May 2013; this is not inferred from PDF creation metadata.
Source type: `dissertation`; discovery mode: `manual_web_search`; accessed:
2026-10-07. [Institutional PDF](https://media.suub.uni-bremen.de/bitstream/elib/553/1/00103449-1.pdf).
No DOI for this dissertation was verified.

The 314-page capture is `/tmp/ingredient-media-20261007/P1-Hahnke-dissertation.pdf`;
SHA256 `69f40d059da76a240ffadabe36c241fef60aaceac97862ec1a2693c161559a35`.
PDF pages 127-129 (printed 109-111) were rendered and visually inspected in full.
Text extraction warns about missing `fontTools` for some embedded fonts, so the
decimal and hydration decisions below use page images as well as extracted text.
The method text on printed page 67 was also read, but not independently rendered.

## Findings

- The supporting recipe specifies 700 ml final makeup. Its 7 ml KH2PO4 stock
  dose at 50 g/L agrees with the page's dose inputs: `50 * 0.007 / 0.700 = 0.5 g/L`.
  This does not validate MediaDive's displayed 23.4 g/L calculation.
- Printed page 109 has the literal row `NaHCO3 0.19 g 0.038 g`, under one-liter
  1x and 2x ASW headings. The columns are inconsistent with a simple twofold
  relationship. Do not silently choose 0.38 g, 0.038 g, or the public page's
  1000 g entry as the intended 2x amount.
- The dissertation's trace stock differs from the page-linked SL-8 in amounts
  and manganese hydration. The selenium/tungsten stock also differs in NaOH
  amount. These sources must not be substituted wholesale for each other.

Compare the complete local P1 graph against both source formulations before
applying any claim. The author/protocol association does not establish exact
stock or variant identity. Earlier [public-page captures](20261007-public-medium-source-pages.json)
and the [acquisition handoff](20261007-public-medium-source-handoff.md) remain
historical snapshots; this file does not rewrite them.

## Journal Access

The P1-linked journal DOI is `10.1016/j.syapm.2013.06.006`, *Phylogenetic diversity
of Flavobacteria isolated from the North Sea on solid media*, Richard L. Hahnke
and Jens Harder, 2013. [PubMed](https://pubmed.ncbi.nlm.nih.gov/23957959/) confirms
bibliographic identity, not the recipe methods.

The DOI resolver and ScienceDirect page were unavailable through the web tool.
Both the indexed Max Planck [download](https://pure.mpg.de/pubman/item/item_2484446_2/component/file_3249945/Hahnke13.pdf)
and [repository content endpoint](https://pure.mpg.de/rest/items/item_2484446_2/component/file_3249945/content)
returned HTTP 403; the download also failed through `curl`. No journal full-text
snippet was promoted from a search result. The inspected dissertation is a
separate primary source, not a verified copy of the journal version.
