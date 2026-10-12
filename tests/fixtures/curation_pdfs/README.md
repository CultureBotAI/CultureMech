# Curation PDF Fixtures

These official recipe PDFs are the small byte-pinned inputs required by the
concentration-curation guard tests. Each JSON file records its original URL,
capture metadata and SHA-256 digest alongside base64-encoded PDF bytes. They are
test fixtures, not an export of the local reference cache.

Historical contexts retain their original cache paths and hashes. The shared
`curation_source_fixtures.read_pdf_capture` reader resolves only the digest here,
checks provenance and bytes, and never downloads or falls back to a local cache.
Changing the pinned source requires a new reviewed fixture, not replacing bytes
under an existing digest. Issue: https://github.com/CultureBotAI/CultureMech/issues/575.
