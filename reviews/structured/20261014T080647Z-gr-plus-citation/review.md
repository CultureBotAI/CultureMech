# UTEX GR+ paper citation and cultivation observation

- Review: 20261014T080647Z-gr-plus-citation
- Repository: culturebotai/CultureMech
- Started UTC: 2026-10-14T07:09:11Z
- Finished UTC: 2026-10-14T08:06:47Z
- Reviewer: codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

One paper citation and one species-grounded, strain-scoped cultivation observation; source/Markdown retained. No variant or amount changes. Supplement-only excerpt validation and global merge findings remain open.

## Scope And Provenance

One normalized UTEX GR+ owner, new bibliography and cultivation claim only

Selection: The explicit purchased-UTEX GR+ culture row in the 2021 study supplement
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 41d4d390123c0d8320cd53e994470c88a1b86d8c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:000225 | data/normalized_yaml/algae/soilwater_gr_medium.yaml | maintained | soilwater_gr_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate data/normalized_yaml/algae/soilwater_gr_medium.yaml | passed | True | CultureMech:000225 | Actual outcome; failed gates retained without waiver. |
| just validate-strict data/normalized_yaml/algae/soilwater_gr_medium.yaml | passed | True | CultureMech:000225 | Actual outcome; failed gates retained without waiver. |
| just validate data/normalized_yaml/algae/soilwater_gr_medium.yaml | failed | True | CultureMech:000225 | Actual outcome; failed gates retained without waiver. |
| just validate-strict data/normalized_yaml/algae/soilwater_gr_medium.yaml | passed | True | CultureMech:000225 | Actual outcome; failed gates retained without waiver. |
| just verify-merges | failed | True | CultureMech:000225 | Actual outcome; failed gates retained without waiver. |
| just audit-merge-freshness | failed | True | CultureMech:000225 | Actual outcome; failed gates retained without waiver. |
| /tmp/culturemech-parallel-env-20261012/bin/python scripts/validate_claude_skills.py | passed | True | CultureMech:000225 | Actual outcome; failed gates retained without waiver. |
| git diff --check | passed | True | CultureMech:000225 | Actual outcome; failed gates retained without waiver. |
| /tmp/culturemech-parallel-env-20261012/bin/python /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech/reports/paper_citation_curation/20261014-gr-plus-citation/curate.py --apply | passed | True | CultureMech:000225 | Actual outcome; failed gates retained without waiver. |

## Scientific And Domain Assessments

### Publication identity and source retention

evidence: supported. Targets: CultureMech:000225.

One DOI bibliography addition with alternate PMID/PMCID, verified metadata, source/discovery provenance, original full text and supplement plus Markdown.

### Strain-scoped named-product cultivation

evidence: supported. Targets: CultureMech:000225.

Table S3 explicitly describes cultures and maps UTEX 2523 to purchased UTEX Soilwater: GR+. One positive cultivation observation, not axenic growth or a quantitative metric.

### Scientific name and actual taxonomic rank

evidence: supported. Targets: CultureMech:000225.

Pleodorina japonica is the unambiguous table-block expansion; NCBITaxon:47788 is a species node. The collection strain remains a paper-reported identifier.

### Historical product formulation and variant accounting

evidence: unknown. Targets: CultureMech:000225.

Named purchased product is resolved, but historical lot composition is not independently specified. No modification reported; no invented variant, no GR-minus/child transfer, and no amount changes.

### Original bytes, prior claims and idempotence

evidence: supported. Targets: CultureMech:000225.

All three prior ingredients and other original claims preserved; reverse patch recovers original bytes. One history event, no duplicate DOI/PMID alias, no-op replay passed, all 15910 normalized exact paths/hashes checked including ignored/hidden files.

## Findings

### merge-gates: Repository merge gates failed

major / open / confirmed; issue key: gr-plus-citation-merge-gates.

Actual terminal failures retained. Aggregate comparison is not proof of row equivalence or attribution; generated outputs not published.

### supplement-validation: Reference checker cannot verify the supplement excerpt from its abstract-only retrieval

minor / open / confirmed; issue key: gr-plus-citation-supplement-validation.

Baseline checks passed. Post-edit schema/terms and strict validation pass, but reference checking cannot find the exact Table S3 caption in the retrieved abstract. Original DOCX and rendered table verify the quote and row; the failure remains visible rather than replacing the quote with unrelated abstract text.

### historical-formulation: Exact historical purchased-lot composition is not established

informational / open / confirmed; issue key: gr-plus-citation-historical-formulation.

The supplier product and observed culture are resolved, not every contemporary or historical ingredient. No study-specific change is stated. No formula or growth claim is transferred to related recipes.

## Recommended Actions And Acceptance Checks

### resolve-merge-gates

Repository merge gates failed

- Diagnose maintained inputs/rules and pass both merge checks before publication.

### resolve-supplement-validation

Reference checker cannot verify the supplement excerpt from its abstract-only retrieval

- Support attributable supplement retrieval in the evidence checker or establish an explicit supported verification mechanism; rerun the check without weakening exact-quote rules.

### resolve-historical-formulation

Exact historical purchased-lot composition is not established

- Inspect a study-specific historical formulation before asserting lot-level formula equivalence or assigning a differing recipe variant.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| baseline-00 | reports/paper_citation_curation/20261014-gr-plus-citation/baseline-00.log; reports/paper_citation_curation/20261014-gr-plus-citation/baseline-00.log | context_only | Terminal exit code 0; not scientific approval. |
| baseline-01 | reports/paper_citation_curation/20261014-gr-plus-citation/baseline-01.log; reports/paper_citation_curation/20261014-gr-plus-citation/baseline-01.log | context_only | Terminal exit code 0; not scientific approval. |
| post-00 | reports/paper_citation_curation/20261014-gr-plus-citation/post-00.log; reports/paper_citation_curation/20261014-gr-plus-citation/post-00.log | context_only | Terminal exit code 1; not scientific approval. |
| post-01 | reports/paper_citation_curation/20261014-gr-plus-citation/post-01.log; reports/paper_citation_curation/20261014-gr-plus-citation/post-01.log | context_only | Terminal exit code 0; not scientific approval. |
| merge-00 | reports/paper_citation_curation/20261014-gr-plus-citation/merge-00.log; reports/paper_citation_curation/20261014-gr-plus-citation/merge-00.log | context_only | Terminal exit code 1; not scientific approval. |
| merge-01 | reports/paper_citation_curation/20261014-gr-plus-citation/merge-01.log; reports/paper_citation_curation/20261014-gr-plus-citation/merge-01.log | context_only | Terminal exit code 1; not scientific approval. |
| extra-00 | reports/paper_citation_curation/20261014-gr-plus-citation/extra-00.log; reports/paper_citation_curation/20261014-gr-plus-citation/extra-00.log | context_only | Terminal exit code 0; not scientific approval. |
| extra-01 | reports/paper_citation_curation/20261014-gr-plus-citation/extra-01.log; reports/paper_citation_curation/20261014-gr-plus-citation/extra-01.log | context_only | Terminal exit code 0; not scientific approval. |
| extra-02 | reports/paper_citation_curation/20261014-gr-plus-citation/extra-02.log; reports/paper_citation_curation/20261014-gr-plus-citation/extra-02.log | context_only | Terminal exit code 0; not scientific approval. |
| paper | doi:10.1186/s12915-021-01087-0; references_cache/papers/primary_xml/volvocine-2021-polytomella-volvox-followup-20261014.xml | supports | Archived full primary JATS; bounded methods and source identity checked. |
| metadata | PMID:34465312; references_cache/papers/PMID_34465312.xml | supports | PubMed title, authors, year and DOI/PMID pairing checked; no linked notice returned, not exhaustive notice discovery. |
| supplement | doi:10.1186/s12915-021-01087-0; references_cache/papers/primary_supplements/volvocine-2021-supplement1-20261014.docx | supports | Table S3 row P. japonica / UTEX 2523 / Soilwater: GR+ and both cultivation/purchase captions inspected against original DOCX and page 3 rendering. |
| taxonomy | NCBI Taxonomy:47788; references_cache/papers/taxonomy/volvocine-tap-20261014.xml | supports | Canonical Pleodorina japonica, rank species; this is not independent certification of UTEX 2523. |
| readback | Guarded curation receipt; reports/paper_citation_curation/20261014-gr-plus-citation/final-readback.json | context_only | Exact-path preservation, source readback, ignored-included deduplication or unfinished discovery. |
| pending | Guarded curation receipt; reports/paper_citation_curation/20261014-gr-plus-citation/pending-frontier.json | context_only | Exact-path preservation, source readback, ignored-included deduplication or unfinished discovery. |
| preflight | Guarded curation receipt; reports/paper_citation_curation/20261014-gr-plus-citation/preflight.json | context_only | Exact-path preservation, source readback, ignored-included deduplication or unfinished discovery. |

## Limits And Additional Notes

- Focused self-review, not independent or full-record scientific approval.
- No full test suite rerun for this data-only batch; predecessor results are context, not fresh checks.
- Species identity does not certify strain identity; named product does not prove historical lot composition.
- No generated export, record merge, linked child creation or GitHub mutation.
- AF6 source research is separate and no AF6 owner was edited.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T080647Z-gr-plus-citation
kind: record
repository: culturebotai/CultureMech
title: UTEX GR+ paper citation and cultivation observation
started_at: '2026-10-14T07:09:11Z'
finished_at: '2026-10-14T08:06:47Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Curator-performed source and data readback; not independent
    adversarial review.
skill: culturemech-add-paper-citation
completion: partial
verdict: needs_curation
scientific_review: false
summary: One paper citation and one species-grounded, strain-scoped cultivation observation;
  source/Markdown retained. No variant or amount changes. Supplement-only excerpt
  validation and global merge findings remain open.
source:
  git_revision: 41d4d390123c0d8320cd53e994470c88a1b86d8c
  state: working_tree
  inputs:
  - path: data/normalized_yaml/algae/soilwater_gr_medium.yaml
    sha256: 8a5de01df480d3ea043fef326f1122435ccf936c28e06b4569420a60fbff1f2b
    role: target
  - path: src/culturemech/export/kgx_export.py
    sha256: eacbc2e7b363488cc1ed96e91737f54244dc1a2425dfa05c77ba89d0a5cd10e0
    role: context
  - path: src/culturemech/schema/culturemech.yaml
    sha256: cb8e4b047647d41f47b91d83420799555c09696c8a2a890535a74076e6f8bba6
    role: context
scope:
  description: One normalized UTEX GR+ owner, new bibliography and cultivation claim
    only
  selection: The explicit purchased-UTEX GR+ culture row in the 2021 study supplement
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:000225
  exclusions:
  - target: Prior record claims and whole-paper organism inventory
    reason: Preserved, not recertified; only the medium-relevant GR+ row is in scope.
  - target: Citation exhaustion and source follow-up owners
    reason: Further source and formulation queues remain open.
targets:
- target_id: CultureMech:000225
  path: data/normalized_yaml/algae/soilwater_gr_medium.yaml
  label: soilwater_gr_medium
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/soilwater_gr_medium.yaml
    role: authoritative normalized recipe
checks:
- check_id: baseline-00
  name: just validate data/normalized_yaml/algae/soilwater_gr_medium.yaml
  command: just validate data/normalized_yaml/algae/soilwater_gr_medium.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000225
  evidence_ids:
  - baseline-00
  summary: Actual outcome; failed gates retained without waiver.
- check_id: baseline-01
  name: just validate-strict data/normalized_yaml/algae/soilwater_gr_medium.yaml
  command: just validate-strict data/normalized_yaml/algae/soilwater_gr_medium.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000225
  evidence_ids:
  - baseline-01
  summary: Actual outcome; failed gates retained without waiver.
- check_id: post-00
  name: just validate data/normalized_yaml/algae/soilwater_gr_medium.yaml
  command: just validate data/normalized_yaml/algae/soilwater_gr_medium.yaml
  required: true
  status: failed
  exit_code: 1
  target_ids:
  - CultureMech:000225
  evidence_ids:
  - post-00
  summary: Actual outcome; failed gates retained without waiver.
- check_id: post-01
  name: just validate-strict data/normalized_yaml/algae/soilwater_gr_medium.yaml
  command: just validate-strict data/normalized_yaml/algae/soilwater_gr_medium.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000225
  evidence_ids:
  - post-01
  summary: Actual outcome; failed gates retained without waiver.
- check_id: merge-00
  name: just verify-merges
  command: just verify-merges
  required: true
  status: failed
  exit_code: 1
  target_ids:
  - CultureMech:000225
  evidence_ids:
  - merge-00
  summary: Actual outcome; failed gates retained without waiver.
- check_id: merge-01
  name: just audit-merge-freshness
  command: just audit-merge-freshness
  required: true
  status: failed
  exit_code: 1
  target_ids:
  - CultureMech:000225
  evidence_ids:
  - merge-01
  summary: Actual outcome; failed gates retained without waiver.
- check_id: extra-00
  name: /tmp/culturemech-parallel-env-20261012/bin/python scripts/validate_claude_skills.py
  command: /tmp/culturemech-parallel-env-20261012/bin/python scripts/validate_claude_skills.py
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000225
  evidence_ids:
  - extra-00
  summary: Actual outcome; failed gates retained without waiver.
- check_id: extra-01
  name: git diff --check
  command: git diff --check
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000225
  evidence_ids:
  - extra-01
  summary: Actual outcome; failed gates retained without waiver.
- check_id: extra-02
  name: /tmp/culturemech-parallel-env-20261012/bin/python /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech/reports/paper_citation_curation/20261014-gr-plus-citation/curate.py
    --apply
  command: /tmp/culturemech-parallel-env-20261012/bin/python /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech/reports/paper_citation_curation/20261014-gr-plus-citation/curate.py
    --apply
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000225
  evidence_ids:
  - extra-02
  summary: Actual outcome; failed gates retained without waiver.
evidence:
- evidence_id: baseline-00
  kind: validation
  reference: reports/paper_citation_curation/20261014-gr-plus-citation/baseline-00.log
  locator: reports/paper_citation_curation/20261014-gr-plus-citation/baseline-00.log
  accessed_at: '2026-10-14T08:06:47Z'
  summary: Terminal exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 8e85fad3683d76bd6c3fb545f47c457c6d20f0a3795b6abae6b05d87f12134d1
- evidence_id: baseline-01
  kind: validation
  reference: reports/paper_citation_curation/20261014-gr-plus-citation/baseline-01.log
  locator: reports/paper_citation_curation/20261014-gr-plus-citation/baseline-01.log
  accessed_at: '2026-10-14T08:06:47Z'
  summary: Terminal exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-00
  kind: validation
  reference: reports/paper_citation_curation/20261014-gr-plus-citation/post-00.log
  locator: reports/paper_citation_curation/20261014-gr-plus-citation/post-00.log
  accessed_at: '2026-10-14T08:06:47Z'
  summary: Terminal exit code 1; not scientific approval.
  support: context_only
  snapshot_sha256: eb21c61fc205f6946c9ea67c487533fc0ea62137fc6b8fd334fa324fa797d880
- evidence_id: post-01
  kind: validation
  reference: reports/paper_citation_curation/20261014-gr-plus-citation/post-01.log
  locator: reports/paper_citation_curation/20261014-gr-plus-citation/post-01.log
  accessed_at: '2026-10-14T08:06:47Z'
  summary: Terminal exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: merge-00
  kind: validation
  reference: reports/paper_citation_curation/20261014-gr-plus-citation/merge-00.log
  locator: reports/paper_citation_curation/20261014-gr-plus-citation/merge-00.log
  accessed_at: '2026-10-14T08:06:47Z'
  summary: Terminal exit code 1; not scientific approval.
  support: context_only
  snapshot_sha256: 09a2922082db841587410042dc33d7d3f72b2601f1d6b6f2b33322471ee47f2c
- evidence_id: merge-01
  kind: validation
  reference: reports/paper_citation_curation/20261014-gr-plus-citation/merge-01.log
  locator: reports/paper_citation_curation/20261014-gr-plus-citation/merge-01.log
  accessed_at: '2026-10-14T08:06:47Z'
  summary: Terminal exit code 1; not scientific approval.
  support: context_only
  snapshot_sha256: f630c1f5c692573042d032b814bc9332040266728999f41c8b52c25846950351
- evidence_id: extra-00
  kind: validation
  reference: reports/paper_citation_curation/20261014-gr-plus-citation/extra-00.log
  locator: reports/paper_citation_curation/20261014-gr-plus-citation/extra-00.log
  accessed_at: '2026-10-14T08:06:47Z'
  summary: Terminal exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 441bdd6ab36f5b87c9edccf771321e1c5f6c11f43bec7799e6e98cd4d756c24c
- evidence_id: extra-01
  kind: validation
  reference: reports/paper_citation_curation/20261014-gr-plus-citation/extra-01.log
  locator: reports/paper_citation_curation/20261014-gr-plus-citation/extra-01.log
  accessed_at: '2026-10-14T08:06:47Z'
  summary: Terminal exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: extra-02
  kind: validation
  reference: reports/paper_citation_curation/20261014-gr-plus-citation/extra-02.log
  locator: reports/paper_citation_curation/20261014-gr-plus-citation/extra-02.log
  accessed_at: '2026-10-14T08:06:47Z'
  summary: Terminal exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 92988608e6fc5d98372726d8b73b307bfb6b5be333281dccbf162aebb8ec1895
- evidence_id: paper
  kind: primary_source
  reference: doi:10.1186/s12915-021-01087-0
  locator: references_cache/papers/primary_xml/volvocine-2021-polytomella-volvox-followup-20261014.xml
  accessed_at: '2026-10-14T08:06:47Z'
  summary: Archived full primary JATS; bounded methods and source identity checked.
  support: supports
  snapshot_sha256: 4a12d0351f18d5f8216769997652184573ae6c4b4d17bd785c05ede492f2162e
- evidence_id: metadata
  kind: authority
  reference: PMID:34465312
  locator: references_cache/papers/PMID_34465312.xml
  accessed_at: '2026-10-14T08:06:47Z'
  summary: PubMed title, authors, year and DOI/PMID pairing checked; no linked notice
    returned, not exhaustive notice discovery.
  support: supports
  snapshot_sha256: 85aa40f7b87f29b2130601e9f008c5abc9920dad90f48dfa49bbdbe6e5502c4a
- evidence_id: supplement
  kind: primary_source
  reference: doi:10.1186/s12915-021-01087-0
  locator: references_cache/papers/primary_supplements/volvocine-2021-supplement1-20261014.docx
  accessed_at: '2026-10-14T08:06:47Z'
  summary: 'Table S3 row P. japonica / UTEX 2523 / Soilwater: GR+ and both cultivation/purchase
    captions inspected against original DOCX and page 3 rendering.'
  support: supports
  snapshot_sha256: 415e2e98c16abe2bad435b0541a83662745478d884c5ab9a764c92ce1b29209d
- evidence_id: taxonomy
  kind: authority
  reference: NCBI Taxonomy:47788
  locator: references_cache/papers/taxonomy/volvocine-tap-20261014.xml
  accessed_at: '2026-10-14T08:06:47Z'
  summary: Canonical Pleodorina japonica, rank species; this is not independent certification
    of UTEX 2523.
  support: supports
  snapshot_sha256: 1109bfe01d246520a0de0680077ee46aaa77237c710619b9643782dc84225f5b
- evidence_id: readback
  kind: record_content
  reference: Guarded curation receipt
  locator: reports/paper_citation_curation/20261014-gr-plus-citation/final-readback.json
  accessed_at: '2026-10-14T08:06:47Z'
  summary: Exact-path preservation, source readback, ignored-included deduplication
    or unfinished discovery.
  support: context_only
  snapshot_sha256: 7e37665517f7e7a917153c650d47043b8037072e4d4e861c41cea1b8120827e0
- evidence_id: pending
  kind: record_content
  reference: Guarded curation receipt
  locator: reports/paper_citation_curation/20261014-gr-plus-citation/pending-frontier.json
  accessed_at: '2026-10-14T08:06:47Z'
  summary: Exact-path preservation, source readback, ignored-included deduplication
    or unfinished discovery.
  support: context_only
  snapshot_sha256: c69e620bb93024ed63654444e5d5a36dfc3ee3e54d054efbb1f4f24da75dab8b
- evidence_id: preflight
  kind: record_content
  reference: Guarded curation receipt
  locator: reports/paper_citation_curation/20261014-gr-plus-citation/preflight.json
  accessed_at: '2026-10-14T08:06:47Z'
  summary: Exact-path preservation, source readback, ignored-included deduplication
    or unfinished discovery.
  support: context_only
  snapshot_sha256: c51c79f414ca98365221811a0365621a576933e098cdf659672b0a626fd73cc2
assessments:
- assessment_id: bibliography
  area: evidence
  topic: Publication identity and source retention
  outcome: supported
  target_ids:
  - CultureMech:000225
  evidence_ids:
  - paper
  - metadata
  - supplement
  summary: One DOI bibliography addition with alternate PMID/PMCID, verified metadata,
    source/discovery provenance, original full text and supplement plus Markdown.
- assessment_id: cultivation
  area: evidence
  topic: Strain-scoped named-product cultivation
  outcome: supported
  target_ids:
  - CultureMech:000225
  evidence_ids:
  - supplement
  - readback
  summary: 'Table S3 explicitly describes cultures and maps UTEX 2523 to purchased
    UTEX Soilwater: GR+. One positive cultivation observation, not axenic growth or
    a quantitative metric.'
- assessment_id: taxonomy
  area: evidence
  topic: Scientific name and actual taxonomic rank
  outcome: supported
  target_ids:
  - CultureMech:000225
  evidence_ids:
  - taxonomy
  - supplement
  summary: Pleodorina japonica is the unambiguous table-block expansion; NCBITaxon:47788
    is a species node. The collection strain remains a paper-reported identifier.
- assessment_id: formulation
  area: evidence
  topic: Historical product formulation and variant accounting
  outcome: unknown
  target_ids:
  - CultureMech:000225
  evidence_ids:
  - paper
  - supplement
  - pending
  summary: Named purchased product is resolved, but historical lot composition is
    not independently specified. No modification reported; no invented variant, no
    GR-minus/child transfer, and no amount changes.
- assessment_id: preservation
  area: evidence
  topic: Original bytes, prior claims and idempotence
  outcome: supported
  target_ids:
  - CultureMech:000225
  evidence_ids:
  - readback
  - preflight
  - extra-02
  summary: All three prior ingredients and other original claims preserved; reverse
    patch recovers original bytes. One history event, no duplicate DOI/PMID alias,
    no-op replay passed, all 15910 normalized exact paths/hashes checked including
    ignored/hidden files.
findings:
- finding_id: merge-gates
  issue_key: gr-plus-citation-merge-gates
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Repository merge gates failed
  description: Actual terminal failures retained. Aggregate comparison is not proof
    of row equivalence or attribution; generated outputs not published.
  target_ids:
  - CultureMech:000225
  evidence_ids:
  - merge-00
  - merge-01
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/soilwater_gr_medium.yaml
    role: authoritative normalized recipe
- finding_id: supplement-validation
  issue_key: gr-plus-citation-supplement-validation
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Reference checker cannot verify the supplement excerpt from its abstract-only
    retrieval
  description: Baseline checks passed. Post-edit schema/terms and strict validation
    pass, but reference checking cannot find the exact Table S3 caption in the retrieved
    abstract. Original DOCX and rendered table verify the quote and row; the failure
    remains visible rather than replacing the quote with unrelated abstract text.
  target_ids:
  - CultureMech:000225
  evidence_ids:
  - post-00
  - supplement
  - readback
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/soilwater_gr_medium.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: src/culturemech/validation/recipe_references.py
    role: maintained reference-validator integration; upstream literature fetcher
      may also need support
- finding_id: historical-formulation
  issue_key: gr-plus-citation-historical-formulation
  category: evidence
  severity: informational
  status: open
  certainty: confirmed
  title: Exact historical purchased-lot composition is not established
  description: The supplier product and observed culture are resolved, not every contemporary
    or historical ingredient. No study-specific change is stated. No formula or growth
    claim is transferred to related recipes.
  target_ids:
  - CultureMech:000225
  evidence_ids:
  - paper
  - supplement
  - pending
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/soilwater_gr_medium.yaml
    role: authoritative normalized recipe
actions:
- action_id: resolve-merge-gates
  description: Repository merge gates failed
  finding_ids:
  - merge-gates
  target_ids:
  - CultureMech:000225
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/soilwater_gr_medium.yaml
    role: authoritative normalized recipe
  acceptance_checks:
  - Diagnose maintained inputs/rules and pass both merge checks before publication.
- action_id: resolve-supplement-validation
  description: Reference checker cannot verify the supplement excerpt from its abstract-only
    retrieval
  finding_ids:
  - supplement-validation
  target_ids:
  - CultureMech:000225
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/soilwater_gr_medium.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: src/culturemech/validation/recipe_references.py
    role: maintained reference-validator integration; upstream literature fetcher
      may also need support
  acceptance_checks:
  - Support attributable supplement retrieval in the evidence checker or establish
    an explicit supported verification mechanism; rerun the check without weakening
    exact-quote rules.
- action_id: resolve-historical-formulation
  description: Exact historical purchased-lot composition is not established
  finding_ids:
  - historical-formulation
  target_ids:
  - CultureMech:000225
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/soilwater_gr_medium.yaml
    role: authoritative normalized recipe
  acceptance_checks:
  - Inspect a study-specific historical formulation before asserting lot-level formula
    equivalence or assigning a differing recipe variant.
limitations:
- Focused self-review, not independent or full-record scientific approval.
- No full test suite rerun for this data-only batch; predecessor results are context,
  not fresh checks.
- Species identity does not certify strain identity; named product does not prove
  historical lot composition.
- No generated export, record merge, linked child creation or GitHub mutation.
- AF6 source research is separate and no AF6 owner was edited.
```
