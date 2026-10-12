# Extract Official Recipe PDFs Before Validating Snippets

Status: fixed locally in the subsequent
[PDF validation follow-up](../20261008-recipe-pdf-validation/README.md).
This draft was not submitted to GitHub. The original reproduction below is
preserved; all 122 checks for the four unchanged records now pass. A separate
bibliography-title issue found by the broader check remains open.

## Finding

`just validate-references` rejects genuine DSMZ 403/751 excerpts and titles.
The generic URL cache stores a URL title and raw `%PDF-1.5` document content,
including compressed streams, rather than extracted recipe text. The failing
checks are therefore not reliable evidence that the recipe snippets are absent.

Reproduced on all four records in this batch: 58 of 122 automated reference
checks pass; 60 PDF snippets and four PDF bibliography titles fail. The API
checks pass. `live.json` preserves each result and the refreshed binary hashes.
The PDF text captures in `context.json` and inspected page images independently
support the quotations. The source binaries are cached under ignored
`references_cache/ingredient-albumin-next/`, not staged as repository output.

The current `recipe_source()` in `src/culturemech/validation/recipe_references.py`
recognizes TOGO API, JCM HTML and MediaDive API URLs, but not DSMZ PDF URLs, so
these PDFs fall through to the generic literature URL path. The maintained
official-source cache already rejects redirects, bounds response size and checks
hashes. Extend that path without weakening those checks. `pypdf>=6.0.0` is already
declared in `pyproject.toml` and locked in `uv.lock`; no new PDF dependency is
needed. This was checked with an ignored-inclusive search of the dependency files,
source, scripts and tests.

## Required Resolution

- Add a bounded official-recipe PDF path with content-type/size checks and a
  maintained text extractor. Do not treat decoded PDF bytes as article text.
- Preserve source URL, response URL, HTTP status, binary hash, extraction method
  and access time. Parse the actual recipe heading instead of using the URL as
  its title. Copyright dates must not become inferred publication years.
- Retain exact recipe amounts, column association and symbols. Normalize layout
  whitespace only for matching; do not normalize away numbers or chemical forms.
- Add positive and negative tests for these PDFs, changed amount/hydrate/dose,
  corrupt or scanned-only PDFs and inaccessible sources. Failed extraction must
  remain an explicit failure, not automatic evidence acceptance.
- Re-run reference checks and preserve the original failures alongside retries.

Do not patch the ignored Markdown cache by hand or weaken valid YAML evidence
to bypass the failing checker. This draft is not external issue submission.
