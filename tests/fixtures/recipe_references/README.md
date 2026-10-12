# Official Recipe Reference Fixtures

These are offline copies of public official-source responses, not invented
recipe evidence. Each JSON wrapper contains the requested and returned URL,
HTTP status, UTC capture time, SHA256 of the UTF-8 response and unmodified `raw`
response. Captured 2026-10-07/08/09; fixture tests verify the raw hashes.

PDF wrappers use cache version 2: `raw` is pypdf layout text, while `pdf_base64`
preserves the original binary with a separate `pdf_sha256`. Extraction library,
version, mode, page count and MIME type are recorded. Tests re-extract the binary
and compare the text, so an altered/rehashed quote cannot pass on its own.

- `M1124`: TOGO Medium M1124 API, including literal bracketed stock accessions.
- `JCM1084` and `JCM1282`: original JCM recipe HTML, including inline chemical
  subscripts, hydrate punctuation, table-cell boundaries and percentage basis.
- `J151`: MediaDive medium API, whose title is `data.medium.name`.
- `solution118`: MediaDive solution API, whose title is `data.name`.
- `DSMZ403`, `DSMZ751`, `DSMZ1829`: original official recipe PDFs, including
  batch amounts, stock strengths/doses, final-volume statements and symbols.
- `DSMZ261`: original PDF with a heading that wraps over two lines.
- `DSMZ605a` and `DSMZ104a`: original variant PDFs with letter-suffixed accessions,
  distinct from their base recipes and from other variants.
- `K1021` and `K1021_16929`: original KOMODO base and strain-variant detail
  pages. Their recipe tables, displayed decimal precision, null quantities and
  separate calculated SEED totals remain unmodified.
- `komodo_failed_excerpts.json`: 31 actual failing checks from the hydrolysate
  cohort's pre-fix `applied-live.json`, including the DSMZ record's KOMODO-linked
  variant claim. These quotations are regression cases, not source responses.
- `NBRC1219`: original NBRC Middlebrook 7H11 catalogue HTML. Its table-cell
  boundaries caused the historical `Distilled water 900 mL` matcher failure;
  the capture retains both main-preparation and separate OADC stock sections.

The URLs in the captures provide attribution and source identity. Test captures
are not automatically used as production cache entries. Synthetic mutations in
tests deliberately corrupt quantities, units, formulas and source identities.
