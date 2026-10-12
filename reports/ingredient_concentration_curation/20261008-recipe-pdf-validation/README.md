# Official Recipe PDF Validation

This follow-up fixes the official DSMZ PDF evidence path. It does not edit any
normalized recipe, add evidence entries or increase completed-review coverage.
The all-record ingredient goal and publication workflow remain incomplete.

## Implementation

Official `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_MediumN.pdf`
URLs now use the maintained recipe cache, not the generic literature fetcher's
raw-PDF-as-text fallback. Numeric and letter-suffixed accessions are supported;
a variant cannot match its base accession or a different suffix. HTTP redirects
and unexpected response URLs are
rejected. PDF responses require the correct MIME type and magic bytes, remain
limited to 5 MiB, and have page-count, decoded content-stream and output-text
limits. These checks are not an operating-system memory or CPU sandbox.

The cache preserves the original binary as base64, its SHA256, extracted text
and SHA256, requested/returned URL, HTTP status, access time, page count and
pypdf version/layout mode. Replay verifies both hashes and re-extracts from the
binary; rehashing altered text alone cannot make it valid. Existing JSON/HTML
cache entries remain version 1; PDF entries use version 2. Generic caches are
not patched or trusted. Changed extractor versions require explicit refresh.

The title comes from the actual first heading block, including wrapped headings,
and its accession must agree with the requested source. Copyright dates are not
inferred publication years. Quote matching still folds whitespace only: numbers,
units, chemical forms, signs, case and punctuation remain significant. An
extraction or source error is a failure, not permission to use fuzzy fallback.

[pypdf's extraction guidance](https://pypdf.readthedocs.io/en/stable/user/extract-text.html)
documents layout mode and the limits of extracting image-only PDFs. This
adapter does not guess OCR text. Blank or image-only pages require manual review.
Literal matches establish occurrence, not the scientific scope of a claim.

## Verified Results

The complete reference gate now passes for all four DSMZ/KOMODO 403/751 records:
**122 of 122 checks**, versus 58 passes and 64 PDF-related failures in the
preserved earlier receipt. No YAML snippets, titles or quantities changed.
The PDFs for 403, 751 and the next 1829 candidate were freshly retrieved and
matched their previously inspected binary and text hashes exactly.

A tracked/filesystem-reconciled inventory covered all 15,910 normalized paths.
It found **233 records referencing 118 DSMZ PDF URLs**. Only 61 of those
records contain explicit PDF snippet/title claims: 220 checks against 30 sources.
All 152 snippets pass, as do 27 of 68 titles. The remaining **41 title mismatches
in 34 records** concern 21 sources and remain open. The 172 records with no
explicit PDF snippet/title claim were inventoried, not scientifically verified;
88 referenced sources were not fetched by this claim-level check; separate
regression fixtures include a letter-suffixed source without current YAML claims.

The corpus check caught a wrapped-heading truncation for DSMZ 261. That parser
bug is fixed and covered by a real offline fixture. Original and retry receipts
remain separate. The earlier blank-page error-reporting test failures and
import-order lint failure were corrected before the final test run. The first
inventory was numeric-only. An ignored-inclusive audit found letter-suffixed
recipes; the adapter and inventory now include them. The initial fast run was
deliberately terminated (exit 143) for this extension, not counted as a pass.

The final focused selection passes 288 tests, with lint and formatting checks
passing. It includes reference-specific and concentration-repair tests. The fast
tier passes 9,357 tests, with 16 skipped and 1,945 deselected. Both runs have two
dependency deprecation warnings. The terminal
[validation receipt](validation.json) preserves the unchanged corpus and claims.
This uses the existing
partial locked Python 3.13 environment, not a clean CI installation. Global
merge/freshness failures and other curation queues are not resolved by this fix.

## Artifacts

- `sources.json`: six real fixtures, including wrapped and letter-suffixed titles.
- `pdf-scope-all.json`, `pdf-checks-all-final.json`: final complete official-PDF
  reference inventory and explicit-claim check; no whole-corpus scientific pass.
- `pdf-scope.json`, `pdf-checks.json`, `pdf-checks-final.json`: retained earlier
  numeric-only inventories/checks, including the wrapped-heading finding.
- `references-final.json`: complete reference CLI checks for the four records.
- `focused-complete.json`, `fast-complete.json`: final test/lint receipts.
- `validation.json`: consolidated terminal checks, source/code hashes and
  unchanged normalized-corpus/evidence accounting.
- `references.json`, `focused.json`, `focused-final.json`, `fast.json`: earlier
  receipts; the last is an interrupted run, not a passing fast tier.
- `issue-dsmz-pdf-bibliography-titles.md`: separate, unposted curation issue.
- `title-followup.json`: 41 unapplied, hash-pinned title candidates with exact
  original-heading snippets and provenance.
- `next-work.md`: source-backed next ingredient corrections and remaining scope.
- `barbour-source-access.md`: M2410 article text match and remaining binary/visual
  access gaps; not a new accepted YAML evidence source.

No commit, push, GitHub issue, PR, merge or branch deletion occurred here.
