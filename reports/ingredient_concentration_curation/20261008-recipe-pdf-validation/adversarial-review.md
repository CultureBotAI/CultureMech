# Adversarial Review

This is local adversarial self-review, not independent human or PR approval.

## Addressed

- A successful PDF download is not valid extracted evidence. The adapter checks
  MIME, magic bytes and bounds; malformed, encrypted and image-only documents
  fail rather than becoming decoded binary text or guessed OCR.
- Rehashing altered extracted text must not detach a quote from its PDF. Cache
  replay re-extracts the stored binary and requires exact text agreement.
- A source accession cannot be inferred from the URL alone. The actual heading
  must identify the requested medium. Redirects, wrong headings, unsupported
  URL forms, corrupt caches and symlink entries remain failures.
- Numeric-only routing omitted official letter-suffixed variants. An
  ignored-inclusive audit exposed this gap; both URL and heading parsing now
  preserve suffixes, with real 605a/104a fixtures and cross-variant rejection tests.
  The first fast run was terminated for this correction and is not counted as a pass.
- Titles can wrap. The corpus-scope run exposed DSMZ 261's two-line heading;
  the parser now retains the entire first heading block. A real binary fixture
  prevents first-line truncation from returning.
- Amount/chemical matching must not weaken when supporting PDFs. Tests mutate
  decimals, hydrates, units, normality and stock doses; these remain failures.
- Blank pages initially surfaced a library KeyError instead of the intended
  explicit no-text result. That is fixed; blank pages, textless streams, real
  image-only content, and mixed readable/unreadable pages are covered.
- Missing network access, wrong content type, HTTP errors, excessive response
  size, page count, decoded content size and extracted text size fail closed.
- Production lookups do not use offline test fixtures. Fresh public responses
  verified the original 403/751/1829 binaries/text; the four full reference CLI
  gates pass without patching caches or editing YAML snippets.

## Limits And Open Work

Literal occurrence is not semantic verification of formulation, stock scope or
denominator. Normalized record counts and completed-review coverage do not
increase when a parser is fixed. Blank ancillary pages are conservatively
rejected, and unreadable layouts need manual review. PDF limits are practical
checks, not a hard process-level resource sandbox; pypdf parses/decompresses
content before its decoded length can be checked.

The broader check preserves 41 bibliography title mismatches in 34 records,
172 references-only records without explicit snippet/title claims, and all
existing curation/merge/publication gaps. The complete test suite and clean CI
are not claimed from focused/fast-tier results.

Final local checks pass: 288 focused tests, 9,357 fast-tier tests (16 skipped),
lint, formatting and all 122 complete reference checks for the four unchanged
records. The [terminal receipt](validation.json) verifies code/fixture hashes,
the unchanged normalized inventory and unchanged checked claim text. The earlier
interrupted fast run remains recorded separately and is not counted as a pass.
