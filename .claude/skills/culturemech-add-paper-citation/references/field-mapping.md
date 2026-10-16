# Native field mapping and limitations

Re-read `src/culturemech/schema/culturemech.yaml` before use. This skill adds no
schema fields. The notation below describes slots, not a record to copy.

| Information | Existing storage |
| --- | --- |
| Paper | `references[].reference`: verified `PMID:<digits>` or `doi:<resolved-doi>`. |
| Bibliography | `references[].title`, `authors` (string), `year` (integer). Leave unavailable metadata absent and explain the gap. |
| Provenance | `references[].notes`: `source_type=journal_article; discovery_mode=user_supplied` (or actual discovery mode), `accessed_on=YYYY-MM-DD`, alternate DOI/PMID/PMCID, version and locator. These are notes conventions, not dedicated slots. |
| Formulation support | Root `evidence[]` with the specific supported formulation fields in `explanation`. |
| Inline study variant | `variants[]`: `name`, optional `relationship`, `description`, `modifications` (list of strings), `purpose`, `evidence`. No nested `ingredients` or `target_organisms` slots. |
| Full child variant | Child `parent_media` reference, `variant_relationship`, `variant_modifications`; reciprocal parent `variant_children[]`. Recipe references accept `id`, `name`, `path`, `relationship`, `notes`, `evidence`. |
| Growth organism | `target_organisms[].preferred_term` holds the scientific/source name; `strain` holds the reported strain. `term.id` and `term.label` hold an exact verified taxon and its canonical label. |
| Organism growth evidence | `target_organisms[].evidence[]`; `scoped_to_variant` names an existing inline variant on this same record when support is variant-only. |
| Quantitative observation | Supported `target_organisms[].growth_metrics[]` fields with their own `evidence[]`; never infer a metric from qualitative cultivation. |
| Parent-rank mapping or taxonomy qualification | Organism `evidence[].explanation` for supported growth; otherwise the paper's `references[].notes`. Include reported name, parent scientific name/ID/rank, `taxonomy_match=parent_rank_only`, lookup URL/date, and reason. |
| Mere mention, negative result, or unresolved recipe association | `references[].notes` with organism name, taxonomy mapping, role/result, labeled exact excerpt and locator; no positive growth edge. |
| Change history | Append-only `curation_history[]` through the curation-event helper. |

`EvidenceItem` has `reference`, `supports`, `snippet`, and `explanation`.
`SUPPORT` means support for the precise attached claim, not a general paper
relevance score. Do not use `PARTIAL` to promote an unresolved recipe match
into verified parent-medium growth. An NCBI taxonomy page supports a mapping,
not cultivation; keep its URL and lookup details in the explanation separately
from the paper's growth quote.

Each individual evidence list is keyed by `reference`. Reuse an existing entry
without erasing prior support; additional short exact excerpts and their
locators can be labeled separately in `explanation`. Do not concatenate
noncontiguous passages into one purported exact `snippet`. The same paper may
support distinct claims in different evidence lists. Do not fabricate citation
suffixes or URL fragments to evade duplicate-reference checks.

## Taxonomic precision

`OrganismDescriptor` and `OrganismTerm` have no dedicated taxonomic-rank,
parent-match, or general notes slot. `term.match_type` has a constrained enum;
`parent_rank_only` is **not** an allowed value. Nor is `manual_curated`
appropriate for an agent-only decision (the enum denotes a human choice).

For a parent-rank fallback, leave the organism's `term` absent and record the
parent ID, canonical scientific name, rank, provenance, and explicit limitation
in the supported text fields above. This includes the requested parent match
without making it the identity of the reported organism. If an existing term
is contradicted, propose a separately justified correction; do not delete or
replace it solely because this paper's identification is less precise.

An exact species-level identification and an unverified strain-level match
are different facts: a verified species `term` can accompany a paper-supported
`strain`, but the explanation must say that the taxon match is at species rank.
Read the rank from the returned NCBI record, not from its label: a taxon name
containing a strain designation can still have species rank. Report that actual
rank alongside the preserved strain designation rather than relabeling the node.
Keep original names/synonyms and co-culture dependence explicit. Do not turn an
unresolved species into a genus-wide positive growth assertion.

## Validator and export boundaries

- `just validate-references <record-path>` is the maintained per-record
  reference route. Check actual fetched coverage: DOI resolution alone does
  not verify a quote, and a methods/supplement excerpt may require manual
  verification against the inspected document.
- `just validate-growth` currently scans the corpus, not one file: its script
  accepts `--strict` but not `--file`. It checks cached PMID abstracts and
  reports DOI-only evidence as `MISSING_CACHE`. A full-text excerpt absent
  from the abstract is not necessarily false. Do not rewrite a correct quote
  to make this abstract-only check pass, or claim it verified a supplement.
- Inspect `src/culturemech/export/kgx_export.py` before any requested export.
  Its current `transform`/`organism_grows_in_medium_edge` path creates an edge
  to the parent record using `term.id`, without honoring `scoped_to_variant`
  or a parent-match caveat in prose. Thus an inline variant can be represented
  in YAML but must not be advertised as safely scoped in KGX. Do not publish
  affected edges without a verified scope-preserving exporter or an existing
  full child record. Report this limitation; changing the exporter is a
  separate task. Omitting `term` for a parent-only mapping also avoids an
  unjustified broader-taxon edge in this exporter.

## Source archives

For requested paper/abstract archiving, use the maintained helper rather than
reimplementing PMID parsing or DOI-to-PMID identity checks:

```bash
uv run python scripts/fetch_pubmed_abstracts.py --pmids <numeric-pmid> --report <report.json>
uv run python scripts/fetch_pubmed_abstracts.py --dois <doi> --report <report.json>
```

It stores raw PubMed XML, rendered Markdown and provenance/hash sidecars under
`references_cache/papers/`. DOI lookup is not a full-text fetch. A missing abstract
remains metadata-only; a failed DOI lookup does not establish that the paper or
PMID does not exist. Inspect the command result and actual archived content.

For other primary sources, preserve the original HTML, PDF, page scans or
supplement, a Markdown conversion or explicitly bounded transcription, source
URL, retrieval date, conversion method and byte hashes. Check the payload type:
an HTML error/challenge page is not a successfully downloaded PDF or spreadsheet.
Keep table headings, units, footnotes, stock/final bases and locators; verify
OCR against the original before using it as an exact snippet. Link these local
archives in citation notes without replacing the DOI/PMID with a local path.
Do not force-add ignored caches or claim their contents were published.
