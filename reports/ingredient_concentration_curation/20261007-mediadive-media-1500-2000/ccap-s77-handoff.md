# CCAP S77 Source Handoff

This is a source investigation for the next record, not an applied repair or a
per-record concentration review. Neither target below is added to this batch's
500 report paths or edited-record count.

- Next frozen target: `data/normalized_yaml/bacterial/s77_vitamins.yaml`.
- ID: `CultureMech:000309`; source accession: `mediadive.medium:C102`.
- Current target SHA256: `4c294191c19eca044a8b0713086c1784eb46a1e5e2a353e9836b995592da84bf`.
- Related authoritative target: `data/normalized_yaml/algae/s77_vitamins.yaml`.
- Related ID: `CultureMech:000125`; source accession: `CCAP:S77`.
- Related SHA256: `0cbcf1bdc71add7072d6f001f1ce64b57c48308959d40bff593e35d06344f76b`.
- Original recipe: [S77 + vitamins](https://www.ccap.ac.uk/wp-content/uploads/MR_S77.pdf).
- Source type: culture-collection recipe; discovery: existing record reference.
- Retrieved and visually inspected in full: 2026-10-07; one page.
- Printed recipe date: May 1989. Individual recipe authors are not supplied.
- PDF SHA256: `cb026d777138a2362601816874b21ec225b2587b9aa2fc8f32825b07b5639326`.

Independent text extraction with `pypdf 6.19.0` agrees with the visually inspected
amounts and subscripts. Its text retains nonbreaking spaces; preserve the exact
extracted substring in later evidence rather than fabricating normalized quotes.
The lightweight reader is available in an isolated temporary tool environment;
this does not imply the repository's full Python 3.13 dependencies installed.

The live MediaDive response links this PDF but has no ingredient recipe table;
its preparation is a placeholder. Do not merely widen the DSMZ API allowlist and
claim this is reviewed. The official PDF has explicit per-litre headings and
water make-up instructions, which must be used for the ingredient evidence.

Both whole normalized targets were inspected. Each has twelve ingredient rows;
the PDF has twenty-three, counting the later silicate addition. Missing rows
include Tris, four minor salts, five trace salts, and cyanocobalamin. Several
retained formula labels lost subscripts during earlier extraction. The PDF
itself prints unusual molybdate and silicate formulas: preserve and flag that
source ambiguity rather than silently supplying a chemical formula or ontology ID.

Exact scope excerpt, page 1, title context: "Marine diatoms". This contradicts
the algal copy's generic freshwater description and requires separate scrutiny
of the bacterial category. No taxon-specific growth claim follows from the heading.

Preparation scope excerpt, page 1: "Make up to 1 litre with distilled water."
The ordered pH and silicate steps also need restoration. Retained generic light
and temperature recommendations are not supported by this PDF. Every later edit,
including label/preparation repairs, needs its own scoped exact source support.

The historical [review](../../yaml_record_review/20260925T032807Z-s77_vitamins.md)
already identifies this incomplete expansion. A fresh ignored-file-inclusive
search of existing raw data, reports, scripts, and skills found that review and
both concentration audit reports. Two requested search roots (`data/raw_yaml`
and `research`) were absent; this is not a claim that all possible local captures
are absent. Before changing duplicate relationships or paths, perform the
repository-wide ignored-file-inclusive accession/link search required by that
review. Preserve both stable IDs and do not hand-edit the generated merged record.
