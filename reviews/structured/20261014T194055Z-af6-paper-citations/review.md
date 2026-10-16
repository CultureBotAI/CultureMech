# AF6 paper citations and bounded organism observations

- Review: 20261014T194055Z-af6-paper-citations
- Repository: culturebotai/CultureMech
- Started UTC: 2026-10-14T08:18:16Z
- Finished UTC: 2026-10-14T19:40:55Z
- Reviewer: codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Four archived-paper bibliography additions and 41 qualified organism observations in notes; no native growth, variants or amounts added. JaLC retrieval, global merge and formulation findings remain open.

## Scope And Provenance

One normalized AF6 owner; newly added bibliography and source observations only

Selection: Four primary papers explicitly naming AF6 or NIES AF6/AF6/2
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 41d4d390123c0d8320cd53e994470c88a1b86d8c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:008317 | data/normalized_yaml/bacterial/af6.yaml | maintained | af6 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate data/normalized_yaml/bacterial/af6.yaml | passed | True | CultureMech:008317 | Actual result; failed gates retained without waiver. |
| just validate-strict data/normalized_yaml/bacterial/af6.yaml | passed | True | CultureMech:008317 | Actual result; failed gates retained without waiver. |
| just validate data/normalized_yaml/bacterial/af6.yaml | failed | True | CultureMech:008317 | Actual result; failed gates retained without waiver. |
| just validate-strict data/normalized_yaml/bacterial/af6.yaml | passed | True | CultureMech:008317 | Actual result; failed gates retained without waiver. |
| just verify-merges | failed | True | CultureMech:008317 | Actual result; failed gates retained without waiver. |
| just audit-merge-freshness | failed | True | CultureMech:008317 | Actual result; failed gates retained without waiver. |
| /tmp/culturemech-parallel-env-20261012/bin/python scripts/validate_claude_skills.py | passed | True | CultureMech:008317 | Actual result; failed gates retained without waiver. |
| git diff --check | passed | True | CultureMech:008317 | Actual result; failed gates retained without waiver. |
| /tmp/culturemech-parallel-env-20261012/bin/python /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech/reports/paper_citation_curation/20261014-af6-paper-citations/curate.py --apply | passed | True | CultureMech:008317 | Actual result; failed gates retained without waiver. |

## Scientific And Domain Assessments

### Publication identity and source archives

evidence: supported. Targets: CultureMech:008317.

Four DOI bibliography additions with verified titles, authors, years and alternate identifiers where available. Original paper/abstract files and Markdown exist for all four; 2009 is publication year, not 2025 online-archive availability.

### Bounded organism observations and study roles

evidence: supported. Targets: CultureMech:008317.

41 source-reported observations retained in notes: 29 AF6/AF6/2 rows, six FACHB strains, three Antarctic/control observations and three non-axenic/other-medium algal observations. No automatic positive growth assertion.

### Scientific names, synonyms and parent rank

evidence: supported. Targets: CultureMech:008317.

Actual species ranks retained including Chlamydomonas sp. ICE-L; reported Chlorella saccharophila maps by documented synonym. Ulothrix variabilis NIES-329 receives a qualified Klebsormidium genus mapping from collection reidentification, not an Ulothrix species assignment.

### Historical AF6 formulation and study variants

evidence: unknown. Targets: CultureMech:008317.

AF6-family relevance is explicit, but current NBRC-derived units/stock structure conflict with collection sources. NIES AF6 and one-half AF6/2 differences remain in notes pending base/historical formulation reconciliation. No resolved variant, base amount correction, pH-child transfer or growth metric invented.

### Prior content, exact paths and idempotence

evidence: supported. Targets: CultureMech:008317.

All original claims and 22 ingredients preserved; reverse patch recovers original bytes. Exactly one history event; no-op replay passed. All 15910 normalized exact paths and hashes verified against the predecessor, including ignored/hidden files.

## Findings

### merge-gates: Repository merge gates failed

major / open / confirmed; issue key: af6-citation-merge-gates.

Terminal failures retained; aggregate similarity does not establish row equivalence or cause. No generated outputs published.

### jalc-retrieval: Automatic reference retrieval does not fetch the JaLC-registered paper

minor / open / confirmed; issue key: af6-citation-jalc-retrieval.

Schema, terms and strict validation pass; reference validation cannot fetch doi:10.60369/microresys.25.1_21 from Crossref/DataCite. J-STAGE, the archived original PDF and DOI agency response establish identity. Manual verification is not a passing automatic gate.

### unresolved-study-formulation: Exact AF6 study variants remain unresolved

major / open / confirmed; issue key: af6-citation-unresolved-study-formulation.

Native bibliography is AF6-family context only. The malformed imported base cannot be treated as the studied formula. Source differences are recorded, but no resolved variant or parent-medium growth entry is added. Older two-owner AF6 findings remain open and are not superseded by this one-owner citation review.

## Recommended Actions And Acceptance Checks

### resolve-merge-gates

Repository merge gates failed

- Diagnose maintained merge inputs/rules and pass both gates before publication.

### resolve-jalc-retrieval

Automatic reference retrieval does not fetch the JaLC-registered paper

- Add verified JaLC/publisher retrieval through maintained reference integration, or an explicit attributable verification mechanism; rerun without weakening identity checks.

### resolve-unresolved-study-formulation

Exact AF6 study variants remain unresolved

- Reconcile base units, stock/final-volume basis, optional agar and historical recipes; then represent supported study variants with correctly scoped growth evidence.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| baseline-00 | reports/paper_citation_curation/20261014-af6-paper-citations/baseline-00.log; reports/paper_citation_curation/20261014-af6-paper-citations/baseline-00.log | context_only | Terminal exit code 0; not scientific approval. |
| baseline-01 | reports/paper_citation_curation/20261014-af6-paper-citations/baseline-01.log; reports/paper_citation_curation/20261014-af6-paper-citations/baseline-01.log | context_only | Terminal exit code 0; not scientific approval. |
| post-00 | reports/paper_citation_curation/20261014-af6-paper-citations/post-00.log; reports/paper_citation_curation/20261014-af6-paper-citations/post-00.log | context_only | Terminal exit code 1; not scientific approval. |
| post-01 | reports/paper_citation_curation/20261014-af6-paper-citations/post-01.log; reports/paper_citation_curation/20261014-af6-paper-citations/post-01.log | context_only | Terminal exit code 0; not scientific approval. |
| merge-00 | reports/paper_citation_curation/20261014-af6-paper-citations/merge-00.log; reports/paper_citation_curation/20261014-af6-paper-citations/merge-00.log | context_only | Terminal exit code 1; not scientific approval. |
| merge-01 | reports/paper_citation_curation/20261014-af6-paper-citations/merge-01.log; reports/paper_citation_curation/20261014-af6-paper-citations/merge-01.log | context_only | Terminal exit code 1; not scientific approval. |
| extra-00 | reports/paper_citation_curation/20261014-af6-paper-citations/extra-00.log; reports/paper_citation_curation/20261014-af6-paper-citations/extra-00.log | context_only | Terminal exit code 0; not scientific approval. |
| extra-01 | reports/paper_citation_curation/20261014-af6-paper-citations/extra-01.log; reports/paper_citation_curation/20261014-af6-paper-citations/extra-01.log | context_only | Terminal exit code 0; not scientific approval. |
| extra-02 | reports/paper_citation_curation/20261014-af6-paper-citations/extra-02.log; reports/paper_citation_curation/20261014-af6-paper-citations/extra-02.log | context_only | Terminal exit code 0; not scientific approval. |
| paper-0 | doi:10.1093/gbe/evz104; references_cache/papers/primary_xml/antarctic-2019-polytomella-volvox-followup-20261014.xml | supports | Full primary JATS plus PubMed abstract XML and Markdown; bounded medium-relevant passage assessment. |
| paper-1 | doi:10.3389/fmicb.2019.01351; references_cache/papers/primary_xml/volvocine-2019-gr-plus-followup-20261014.xml | supports | Full primary JATS plus PubMed abstract XML and Markdown; bounded medium-relevant passage assessment. |
| paper-2 | doi:10.60369/microresys.25.1_21; references_cache/papers/primary_pdf/algal-bacteria-2009-gr-plus-followup-20261014.pdf | supports | Full primary PDF and Markdown; publisher HTML plus Markdown. Page 21 cultivation paragraph visually verified. |
| paper-3 | doi:10.1186/s12915-021-01087-0; references_cache/papers/primary_xml/volvocine-2021-polytomella-volvox-followup-20261014.xml | supports | Full primary JATS plus PubMed abstract XML and Markdown; bounded medium-relevant passage assessment. Original DOCX and Markdown; all 29 AF6/AF6/2 Table S3 rows visually checked on rendered pages 3-4. |
| supplement | doi:10.1186/s12915-021-01087-0; references_cache/papers/primary_supplements/volvocine-2021-supplement1-20261014.docx | supports | All 29 AF6/AF6/2 Table S3 rows and cultivation/NIES captions checked against original cells and rendered pages 3-4. |
| taxonomy | NCBI Taxonomy; references_cache/papers/taxonomy/af6-citation-20261014.xml | supports | Names, synonyms and actual ranks checked for 41 bounded source observations; species identity does not independently certify a strain. |
| collection | NIES-329; references_cache/papers/primary_xml/nies-329-gr-plus-followup-20261014.html | supports | Reported Ulothrix variabilis NIES-329 is now Klebsormidium sp. after DNA reidentification. Verified genus fallback, not a species synonym or independent growth claim. |
| nies-formula | https://mcc.nbrp.jp/medium/ja/af6.pdf; references_cache/papers/primary_pdf/nies-af6-gr-plus-followup-20261014.pdf | context_only | Current NIES footnotes omit CaCO3 and specify P IV/MES; historical study formula is not completely established. |
| agency | https://doi.org/ra/10.60369/microresys.25.1_21; references_cache/papers/primary_xml/microresys-doi-agency-af6-followup-20261014.json | supports | DOI registration agency is JaLC, while the failing automatic checker reports only Crossref/DataCite retrieval attempts. |
| readback | Guarded curation receipt; reports/paper_citation_curation/20261014-af6-paper-citations/final-readback.json | context_only | Exact input preservation, bounded source qualification, ignored-included deduplication or unfinished discovery. |
| pending | Guarded curation receipt; reports/paper_citation_curation/20261014-af6-paper-citations/pending-frontier.json | context_only | Exact input preservation, bounded source qualification, ignored-included deduplication or unfinished discovery. |
| preflight | Guarded curation receipt; reports/paper_citation_curation/20261014-af6-paper-citations/preflight.json | context_only | Exact input preservation, bounded source qualification, ignored-included deduplication or unfinished discovery. |
| proposals | Guarded curation receipt; reports/paper_citation_curation/20261014-af6-paper-citations/source-preparation-v2.json | context_only | Exact input preservation, bounded source qualification, ignored-included deduplication or unfinished discovery. |

## Limits And Additional Notes

- Focused self-review, not independent or full-record scientific approval.
- Full test suite not rerun for this data-only batch; no maintained Python/schema change.
- Source archives and taxonomy do not prove exact historical recipe or strain identity.
- No generated export, new linked child, media merge, GitHub mutation or prior-finding closure.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T194055Z-af6-paper-citations
kind: record
repository: culturebotai/CultureMech
title: AF6 paper citations and bounded organism observations
started_at: '2026-10-14T08:18:16Z'
finished_at: '2026-10-14T19:40:55Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Curator-performed source/readback checks; not independent adversarial
    review.
skill: culturemech-add-paper-citation
completion: partial
verdict: needs_curation
scientific_review: false
summary: Four archived-paper bibliography additions and 41 qualified organism observations
  in notes; no native growth, variants or amounts added. JaLC retrieval, global merge
  and formulation findings remain open.
source:
  git_revision: 41d4d390123c0d8320cd53e994470c88a1b86d8c
  state: working_tree
  inputs:
  - path: data/normalized_yaml/bacterial/af6.yaml
    sha256: d89b97e27efd0c6076aa5d75b8728a0990f43f1fbd3f0fba6f7257e70f61be6d
    role: target
  - path: src/culturemech/export/kgx_export.py
    sha256: eacbc2e7b363488cc1ed96e91737f54244dc1a2425dfa05c77ba89d0a5cd10e0
    role: context
  - path: src/culturemech/schema/culturemech.yaml
    sha256: cb8e4b047647d41f47b91d83420799555c09696c8a2a890535a74076e6f8bba6
    role: context
scope:
  description: One normalized AF6 owner; newly added bibliography and source observations
    only
  selection: Four primary papers explicitly naming AF6 or NIES AF6/AF6/2
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:008317
  exclusions:
  - target: Existing ingredients, child record and whole-paper organism inventories
    reason: Preserved, not recertified; observations limited to identified passages
      and AF6 rows.
  - target: Citation exhaustion and unresolved source queues
    reason: Further sources and mappings remain open.
targets:
- target_id: CultureMech:008317
  path: data/normalized_yaml/bacterial/af6.yaml
  label: af6
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/af6.yaml
    role: authoritative normalized recipe
checks:
- check_id: baseline-00
  name: just validate data/normalized_yaml/bacterial/af6.yaml
  command: just validate data/normalized_yaml/bacterial/af6.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:008317
  evidence_ids:
  - baseline-00
  summary: Actual result; failed gates retained without waiver.
- check_id: baseline-01
  name: just validate-strict data/normalized_yaml/bacterial/af6.yaml
  command: just validate-strict data/normalized_yaml/bacterial/af6.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:008317
  evidence_ids:
  - baseline-01
  summary: Actual result; failed gates retained without waiver.
- check_id: post-00
  name: just validate data/normalized_yaml/bacterial/af6.yaml
  command: just validate data/normalized_yaml/bacterial/af6.yaml
  required: true
  status: failed
  exit_code: 1
  target_ids:
  - CultureMech:008317
  evidence_ids:
  - post-00
  summary: Actual result; failed gates retained without waiver.
- check_id: post-01
  name: just validate-strict data/normalized_yaml/bacterial/af6.yaml
  command: just validate-strict data/normalized_yaml/bacterial/af6.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:008317
  evidence_ids:
  - post-01
  summary: Actual result; failed gates retained without waiver.
- check_id: merge-00
  name: just verify-merges
  command: just verify-merges
  required: true
  status: failed
  exit_code: 1
  target_ids:
  - CultureMech:008317
  evidence_ids:
  - merge-00
  summary: Actual result; failed gates retained without waiver.
- check_id: merge-01
  name: just audit-merge-freshness
  command: just audit-merge-freshness
  required: true
  status: failed
  exit_code: 1
  target_ids:
  - CultureMech:008317
  evidence_ids:
  - merge-01
  summary: Actual result; failed gates retained without waiver.
- check_id: extra-00
  name: /tmp/culturemech-parallel-env-20261012/bin/python scripts/validate_claude_skills.py
  command: /tmp/culturemech-parallel-env-20261012/bin/python scripts/validate_claude_skills.py
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:008317
  evidence_ids:
  - extra-00
  summary: Actual result; failed gates retained without waiver.
- check_id: extra-01
  name: git diff --check
  command: git diff --check
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:008317
  evidence_ids:
  - extra-01
  summary: Actual result; failed gates retained without waiver.
- check_id: extra-02
  name: /tmp/culturemech-parallel-env-20261012/bin/python /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech/reports/paper_citation_curation/20261014-af6-paper-citations/curate.py
    --apply
  command: /tmp/culturemech-parallel-env-20261012/bin/python /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech/reports/paper_citation_curation/20261014-af6-paper-citations/curate.py
    --apply
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:008317
  evidence_ids:
  - extra-02
  summary: Actual result; failed gates retained without waiver.
evidence:
- evidence_id: baseline-00
  kind: validation
  reference: reports/paper_citation_curation/20261014-af6-paper-citations/baseline-00.log
  locator: reports/paper_citation_curation/20261014-af6-paper-citations/baseline-00.log
  accessed_at: '2026-10-14T19:40:55Z'
  summary: Terminal exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 8e85fad3683d76bd6c3fb545f47c457c6d20f0a3795b6abae6b05d87f12134d1
- evidence_id: baseline-01
  kind: validation
  reference: reports/paper_citation_curation/20261014-af6-paper-citations/baseline-01.log
  locator: reports/paper_citation_curation/20261014-af6-paper-citations/baseline-01.log
  accessed_at: '2026-10-14T19:40:55Z'
  summary: Terminal exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-00
  kind: validation
  reference: reports/paper_citation_curation/20261014-af6-paper-citations/post-00.log
  locator: reports/paper_citation_curation/20261014-af6-paper-citations/post-00.log
  accessed_at: '2026-10-14T19:40:55Z'
  summary: Terminal exit code 1; not scientific approval.
  support: context_only
  snapshot_sha256: dc7394dfc9e49fbb3563366b2c97269da3f54c6fb888587008fab8b5fb6988a1
- evidence_id: post-01
  kind: validation
  reference: reports/paper_citation_curation/20261014-af6-paper-citations/post-01.log
  locator: reports/paper_citation_curation/20261014-af6-paper-citations/post-01.log
  accessed_at: '2026-10-14T19:40:55Z'
  summary: Terminal exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: merge-00
  kind: validation
  reference: reports/paper_citation_curation/20261014-af6-paper-citations/merge-00.log
  locator: reports/paper_citation_curation/20261014-af6-paper-citations/merge-00.log
  accessed_at: '2026-10-14T19:40:55Z'
  summary: Terminal exit code 1; not scientific approval.
  support: context_only
  snapshot_sha256: 09a2922082db841587410042dc33d7d3f72b2601f1d6b6f2b33322471ee47f2c
- evidence_id: merge-01
  kind: validation
  reference: reports/paper_citation_curation/20261014-af6-paper-citations/merge-01.log
  locator: reports/paper_citation_curation/20261014-af6-paper-citations/merge-01.log
  accessed_at: '2026-10-14T19:40:55Z'
  summary: Terminal exit code 1; not scientific approval.
  support: context_only
  snapshot_sha256: ac00ef1e453e740274bb0522995d48d882cd4593410681bb0ef405aab4e818ed
- evidence_id: extra-00
  kind: validation
  reference: reports/paper_citation_curation/20261014-af6-paper-citations/extra-00.log
  locator: reports/paper_citation_curation/20261014-af6-paper-citations/extra-00.log
  accessed_at: '2026-10-14T19:40:55Z'
  summary: Terminal exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 441bdd6ab36f5b87c9edccf771321e1c5f6c11f43bec7799e6e98cd4d756c24c
- evidence_id: extra-01
  kind: validation
  reference: reports/paper_citation_curation/20261014-af6-paper-citations/extra-01.log
  locator: reports/paper_citation_curation/20261014-af6-paper-citations/extra-01.log
  accessed_at: '2026-10-14T19:40:55Z'
  summary: Terminal exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: extra-02
  kind: validation
  reference: reports/paper_citation_curation/20261014-af6-paper-citations/extra-02.log
  locator: reports/paper_citation_curation/20261014-af6-paper-citations/extra-02.log
  accessed_at: '2026-10-14T19:40:55Z'
  summary: Terminal exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: de183bbaaa70a8188c222647fa4f41efd0e7619a62beff0a4289c72f0d8edae2
- evidence_id: paper-0
  kind: primary_source
  reference: doi:10.1093/gbe/evz104
  locator: references_cache/papers/primary_xml/antarctic-2019-polytomella-volvox-followup-20261014.xml
  accessed_at: '2026-10-14T19:40:55Z'
  summary: Full primary JATS plus PubMed abstract XML and Markdown; bounded medium-relevant
    passage assessment.
  support: supports
  snapshot_sha256: 30f904b8138b973c83a364ff413061041034eefe56ac2f78ff2134ace1938e81
- evidence_id: paper-1
  kind: primary_source
  reference: doi:10.3389/fmicb.2019.01351
  locator: references_cache/papers/primary_xml/volvocine-2019-gr-plus-followup-20261014.xml
  accessed_at: '2026-10-14T19:40:55Z'
  summary: Full primary JATS plus PubMed abstract XML and Markdown; bounded medium-relevant
    passage assessment.
  support: supports
  snapshot_sha256: 778c0decdf0903eed6e34ba442eb62206d972e345be62e67fc96f67d17071952
- evidence_id: paper-2
  kind: primary_source
  reference: doi:10.60369/microresys.25.1_21
  locator: references_cache/papers/primary_pdf/algal-bacteria-2009-gr-plus-followup-20261014.pdf
  accessed_at: '2026-10-14T19:40:55Z'
  summary: Full primary PDF and Markdown; publisher HTML plus Markdown. Page 21 cultivation
    paragraph visually verified.
  support: supports
  snapshot_sha256: fa14c121824afb8feb7cf0fc82708d94c09c14549b43cdb1950a2e9495aa5d59
- evidence_id: paper-3
  kind: primary_source
  reference: doi:10.1186/s12915-021-01087-0
  locator: references_cache/papers/primary_xml/volvocine-2021-polytomella-volvox-followup-20261014.xml
  accessed_at: '2026-10-14T19:40:55Z'
  summary: Full primary JATS plus PubMed abstract XML and Markdown; bounded medium-relevant
    passage assessment. Original DOCX and Markdown; all 29 AF6/AF6/2 Table S3 rows
    visually checked on rendered pages 3-4.
  support: supports
  snapshot_sha256: 4a12d0351f18d5f8216769997652184573ae6c4b4d17bd785c05ede492f2162e
- evidence_id: supplement
  kind: primary_source
  reference: doi:10.1186/s12915-021-01087-0
  locator: references_cache/papers/primary_supplements/volvocine-2021-supplement1-20261014.docx
  accessed_at: '2026-10-14T19:40:55Z'
  summary: All 29 AF6/AF6/2 Table S3 rows and cultivation/NIES captions checked against
    original cells and rendered pages 3-4.
  support: supports
  snapshot_sha256: 415e2e98c16abe2bad435b0541a83662745478d884c5ab9a764c92ce1b29209d
- evidence_id: taxonomy
  kind: authority
  reference: NCBI Taxonomy
  locator: references_cache/papers/taxonomy/af6-citation-20261014.xml
  accessed_at: '2026-10-14T19:40:55Z'
  summary: Names, synonyms and actual ranks checked for 41 bounded source observations;
    species identity does not independently certify a strain.
  support: supports
  snapshot_sha256: 0013513ca784094f01f8b798d00e6b5cb6b0e471b9a61943e9b3cbd11e6d3e00
- evidence_id: collection
  kind: authority
  reference: NIES-329
  locator: references_cache/papers/primary_xml/nies-329-gr-plus-followup-20261014.html
  accessed_at: '2026-10-14T19:40:55Z'
  summary: Reported Ulothrix variabilis NIES-329 is now Klebsormidium sp. after DNA
    reidentification. Verified genus fallback, not a species synonym or independent
    growth claim.
  support: supports
  snapshot_sha256: 4545836a7cebb1f2d01400594b7370de8465a37c9f9dc399d0bff36729092765
- evidence_id: nies-formula
  kind: primary_source
  reference: https://mcc.nbrp.jp/medium/ja/af6.pdf
  locator: references_cache/papers/primary_pdf/nies-af6-gr-plus-followup-20261014.pdf
  accessed_at: '2026-10-14T19:40:55Z'
  summary: Current NIES footnotes omit CaCO3 and specify P IV/MES; historical study
    formula is not completely established.
  support: context_only
  snapshot_sha256: 807ee6da94079cb2292a764a519d4a3bb009377dc7602c0a113e35d22881c4a1
- evidence_id: agency
  kind: authority
  reference: https://doi.org/ra/10.60369/microresys.25.1_21
  locator: references_cache/papers/primary_xml/microresys-doi-agency-af6-followup-20261014.json
  accessed_at: '2026-10-14T19:40:55Z'
  summary: DOI registration agency is JaLC, while the failing automatic checker reports
    only Crossref/DataCite retrieval attempts.
  support: supports
  snapshot_sha256: 1d51058659d246acdf7250be19a3da1109dd746320a1bb516733d1f56e1d6cc8
- evidence_id: readback
  kind: record_content
  reference: Guarded curation receipt
  locator: reports/paper_citation_curation/20261014-af6-paper-citations/final-readback.json
  accessed_at: '2026-10-14T19:40:55Z'
  summary: Exact input preservation, bounded source qualification, ignored-included
    deduplication or unfinished discovery.
  support: context_only
  snapshot_sha256: 5832421f3844d4e8bacfd631fd09ee8695713999e9c4f6003ea3337238c64e6a
- evidence_id: pending
  kind: record_content
  reference: Guarded curation receipt
  locator: reports/paper_citation_curation/20261014-af6-paper-citations/pending-frontier.json
  accessed_at: '2026-10-14T19:40:55Z'
  summary: Exact input preservation, bounded source qualification, ignored-included
    deduplication or unfinished discovery.
  support: context_only
  snapshot_sha256: c7b245ec4869ed1b61835de354714da33c79954284a467d617dee74f219e77e9
- evidence_id: preflight
  kind: record_content
  reference: Guarded curation receipt
  locator: reports/paper_citation_curation/20261014-af6-paper-citations/preflight.json
  accessed_at: '2026-10-14T19:40:55Z'
  summary: Exact input preservation, bounded source qualification, ignored-included
    deduplication or unfinished discovery.
  support: context_only
  snapshot_sha256: 55e5a46c07fea4ee6916be518e249c64d069399e04f5997aa959f1794ab658f3
- evidence_id: proposals
  kind: record_content
  reference: Guarded curation receipt
  locator: reports/paper_citation_curation/20261014-af6-paper-citations/source-preparation-v2.json
  accessed_at: '2026-10-14T19:40:55Z'
  summary: Exact input preservation, bounded source qualification, ignored-included
    deduplication or unfinished discovery.
  support: context_only
  snapshot_sha256: fca0f073ff4659065a909a30ed813e33dd8aa2bf170e60f781613593993115cf
assessments:
- assessment_id: bibliography
  area: evidence
  topic: Publication identity and source archives
  outcome: supported
  target_ids:
  - CultureMech:008317
  evidence_ids:
  - paper-0
  - paper-1
  - paper-2
  - paper-3
  - proposals
  summary: Four DOI bibliography additions with verified titles, authors, years and
    alternate identifiers where available. Original paper/abstract files and Markdown
    exist for all four; 2009 is publication year, not 2025 online-archive availability.
- assessment_id: observations
  area: evidence
  topic: Bounded organism observations and study roles
  outcome: supported
  target_ids:
  - CultureMech:008317
  evidence_ids:
  - proposals
  - supplement
  - readback
  summary: '41 source-reported observations retained in notes: 29 AF6/AF6/2 rows,
    six FACHB strains, three Antarctic/control observations and three non-axenic/other-medium
    algal observations. No automatic positive growth assertion.'
- assessment_id: taxonomy
  area: evidence
  topic: Scientific names, synonyms and parent rank
  outcome: supported
  target_ids:
  - CultureMech:008317
  evidence_ids:
  - taxonomy
  - collection
  - proposals
  summary: Actual species ranks retained including Chlamydomonas sp. ICE-L; reported
    Chlorella saccharophila maps by documented synonym. Ulothrix variabilis NIES-329
    receives a qualified Klebsormidium genus mapping from collection reidentification,
    not an Ulothrix species assignment.
- assessment_id: formulation
  area: evidence
  topic: Historical AF6 formulation and study variants
  outcome: unknown
  target_ids:
  - CultureMech:008317
  evidence_ids:
  - nies-formula
  - proposals
  - supplement
  summary: AF6-family relevance is explicit, but current NBRC-derived units/stock
    structure conflict with collection sources. NIES AF6 and one-half AF6/2 differences
    remain in notes pending base/historical formulation reconciliation. No resolved
    variant, base amount correction, pH-child transfer or growth metric invented.
- assessment_id: preservation
  area: evidence
  topic: Prior content, exact paths and idempotence
  outcome: supported
  target_ids:
  - CultureMech:008317
  evidence_ids:
  - readback
  - preflight
  - extra-02
  summary: All original claims and 22 ingredients preserved; reverse patch recovers
    original bytes. Exactly one history event; no-op replay passed. All 15910 normalized
    exact paths and hashes verified against the predecessor, including ignored/hidden
    files.
findings:
- finding_id: merge-gates
  issue_key: af6-citation-merge-gates
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Repository merge gates failed
  description: Terminal failures retained; aggregate similarity does not establish
    row equivalence or cause. No generated outputs published.
  target_ids:
  - CultureMech:008317
  evidence_ids:
  - merge-00
  - merge-01
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/af6.yaml
    role: authoritative normalized recipe
- finding_id: jalc-retrieval
  issue_key: af6-citation-jalc-retrieval
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Automatic reference retrieval does not fetch the JaLC-registered paper
  description: Schema, terms and strict validation pass; reference validation cannot
    fetch doi:10.60369/microresys.25.1_21 from Crossref/DataCite. J-STAGE, the archived
    original PDF and DOI agency response establish identity. Manual verification is
    not a passing automatic gate.
  target_ids:
  - CultureMech:008317
  evidence_ids:
  - post-00
  - paper-2
  - agency
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/af6.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: src/culturemech/validation/recipe_references.py
    role: maintained reference-validator integration
- finding_id: unresolved-study-formulation
  issue_key: af6-citation-unresolved-study-formulation
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Exact AF6 study variants remain unresolved
  description: Native bibliography is AF6-family context only. The malformed imported
    base cannot be treated as the studied formula. Source differences are recorded,
    but no resolved variant or parent-medium growth entry is added. Older two-owner
    AF6 findings remain open and are not superseded by this one-owner citation review.
  target_ids:
  - CultureMech:008317
  evidence_ids:
  - nies-formula
  - proposals
  - supplement
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/af6.yaml
    role: authoritative normalized recipe
actions:
- action_id: resolve-merge-gates
  description: Repository merge gates failed
  finding_ids:
  - merge-gates
  target_ids:
  - CultureMech:008317
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/af6.yaml
    role: authoritative normalized recipe
  acceptance_checks:
  - Diagnose maintained merge inputs/rules and pass both gates before publication.
- action_id: resolve-jalc-retrieval
  description: Automatic reference retrieval does not fetch the JaLC-registered paper
  finding_ids:
  - jalc-retrieval
  target_ids:
  - CultureMech:008317
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/af6.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: src/culturemech/validation/recipe_references.py
    role: maintained reference-validator integration
  acceptance_checks:
  - Add verified JaLC/publisher retrieval through maintained reference integration,
    or an explicit attributable verification mechanism; rerun without weakening identity
    checks.
- action_id: resolve-unresolved-study-formulation
  description: Exact AF6 study variants remain unresolved
  finding_ids:
  - unresolved-study-formulation
  target_ids:
  - CultureMech:008317
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/af6.yaml
    role: authoritative normalized recipe
  acceptance_checks:
  - Reconcile base units, stock/final-volume basis, optional agar and historical recipes;
    then represent supported study variants with correctly scoped growth evidence.
limitations:
- Focused self-review, not independent or full-record scientific approval.
- Full test suite not rerun for this data-only batch; no maintained Python/schema
  change.
- Source archives and taxonomy do not prove exact historical recipe or strain identity.
- No generated export, new linked child, media merge, GitHub mutation or prior-finding
  closure.
```
