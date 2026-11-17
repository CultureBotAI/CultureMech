# Polytomella and Volvox paper citation curation

- Review: 20261014T070225Z-polytomella-volvox-citations
- Repository: culturebotai/CultureMech
- Started UTC: 2026-10-14T05:48:52Z
- Finished UTC: 2026-10-14T07:02:25Z
- Reviewer: codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Eleven bibliography additions from seven publications across three owners. Exact primary excerpts and qualified organism taxonomy retained in notes. No variants, concentrations or growth assertions added; all prior data preserved. Four title-format reference failures remain.

## Scope And Provenance

Three normalized Polytomella and Volvox owners; bibliography and bounded notes

Selection: Primary named-medium cultivation passages and associated scientific-name/strain descriptions
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base 41d4d390123c0d8320cd53e994470c88a1b86d8c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:000186 | data/normalized_yaml/algae/Polytomella_Medium.yaml | maintained | polytomella_medium |
| CultureMech:000215 | data/normalized_yaml/algae/volvox.yaml | maintained | volvox |
| CultureMech:000238 | data/normalized_yaml/algae/Volvox_Medium.yaml | maintained | volvox_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate data/normalized_yaml/algae/Polytomella_Medium.yaml | passed | True | CultureMech:000186 | Actual outcome; failures retained without waiver. |
| just validate-strict data/normalized_yaml/algae/Polytomella_Medium.yaml | passed | True | CultureMech:000186 | Actual outcome; failures retained without waiver. |
| just validate data/normalized_yaml/algae/volvox.yaml | passed | True | CultureMech:000215 | Actual outcome; failures retained without waiver. |
| just validate-strict data/normalized_yaml/algae/volvox.yaml | passed | True | CultureMech:000215 | Actual outcome; failures retained without waiver. |
| just validate data/normalized_yaml/algae/Volvox_Medium.yaml | passed | True | CultureMech:000238 | Actual outcome; failures retained without waiver. |
| just validate-strict data/normalized_yaml/algae/Volvox_Medium.yaml | passed | True | CultureMech:000238 | Actual outcome; failures retained without waiver. |
| just validate data/normalized_yaml/algae/Polytomella_Medium.yaml | failed | True | CultureMech:000186 | Actual outcome; failures retained without waiver. |
| just validate-strict data/normalized_yaml/algae/Polytomella_Medium.yaml | passed | True | CultureMech:000186 | Actual outcome; failures retained without waiver. |
| just validate data/normalized_yaml/algae/volvox.yaml | failed | True | CultureMech:000215 | Actual outcome; failures retained without waiver. |
| just validate-strict data/normalized_yaml/algae/volvox.yaml | passed | True | CultureMech:000215 | Actual outcome; failures retained without waiver. |
| just validate data/normalized_yaml/algae/Volvox_Medium.yaml | failed | True | CultureMech:000238 | Actual outcome; failures retained without waiver. |
| just validate-strict data/normalized_yaml/algae/Volvox_Medium.yaml | passed | True | CultureMech:000238 | Actual outcome; failures retained without waiver. |
| just verify-merges | failed | True | CultureMech:000186, CultureMech:000215, CultureMech:000238 | Actual outcome; failures retained without waiver. |
| just audit-merge-freshness | failed | True | CultureMech:000186, CultureMech:000215, CultureMech:000238 | Actual outcome; failures retained without waiver. |
| /tmp/culturemech-parallel-env-20261012/bin/python scripts/validate_claude_skills.py | passed | True | CultureMech:000186, CultureMech:000215, CultureMech:000238 | Actual outcome; failures retained without waiver. |
| git diff --check | passed | True | CultureMech:000186, CultureMech:000215, CultureMech:000238 | Actual outcome; failures retained without waiver. |
| /tmp/culturemech-parallel-env-20261012/bin/python /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech/reports/paper_citation_curation/20261014-polytomella-volvox-citations/curate.py --apply | passed | True | CultureMech:000186, CultureMech:000215, CultureMech:000238 | Actual outcome; failures retained without waiver. |
| just test-fast | passed | True | CultureMech:000186, CultureMech:000215, CultureMech:000238 | Actual outcome; failures retained without waiver. |

## Scientific And Domain Assessments

### Bibliography identity and named-medium relevance

evidence: supported. Targets: CultureMech:000186.

Publication metadata, primary cultivation excerpts, original archives and Markdown linked. Relevance is named-medium use, not source-specific exact recipe certification.

### Recipe comparison and unresolved differences

evidence: unknown. Targets: CultureMech:000186.

Percentage bases and acetate hydration, or historical Volvox mineral/vitamin recipe, are unresolved. Supported observations remain in citation notes; no resolved variant, quantity or growth assertion invented.

### Scientific names, rank and role qualifications

evidence: supported. Targets: CultureMech:000186.

Scientific names and verified NCBI IDs/ranks retained in notes. Historical SAG63-4 disagreement uses a qualified genus fallback; Volvox nagariensis rank is forma. Species matches do not certify strains.

### Original record and byte preservation

evidence: supported. Targets: CultureMech:000186.

All 4 top-level ingredients, nested stocks, prior evidence and other fields preserved; original bytes recovered by reversing additions. One history event; no-op replay passed.

### Individual publication addition

evidence: supported. Targets: CultureMech:000186.

doi:10.1093/molbev/msm245: exact cultivation excerpt and qualified organism notes, not native growth or exact formula support.

### Individual publication addition

evidence: supported. Targets: CultureMech:000186.

doi:10.1007/s00294-010-0311-5: exact cultivation excerpt and qualified organism notes, not native growth or exact formula support.

### Individual publication addition

evidence: supported. Targets: CultureMech:000186.

doi:10.1093/gbe/evt122: exact cultivation excerpt and qualified organism notes, not native growth or exact formula support.

### Individual publication addition

evidence: supported. Targets: CultureMech:000186.

doi:10.1104/pp.113.233718: exact cultivation excerpt and qualified organism notes, not native growth or exact formula support.

### Individual publication addition

evidence: supported. Targets: CultureMech:000186.

doi:10.1104/pp.16.01628: exact cultivation excerpt and qualified organism notes, not native growth or exact formula support.

### Bibliography identity and named-medium relevance

evidence: supported. Targets: CultureMech:000215.

Publication metadata, primary cultivation excerpts, original archives and Markdown linked. Relevance is named-medium use, not source-specific exact recipe certification.

### Recipe comparison and unresolved differences

evidence: unknown. Targets: CultureMech:000215.

Percentage bases and acetate hydration, or historical Volvox mineral/vitamin recipe, are unresolved. Supported observations remain in citation notes; no resolved variant, quantity or growth assertion invented.

### Scientific names, rank and role qualifications

evidence: supported. Targets: CultureMech:000215.

Scientific names and verified NCBI IDs/ranks retained in notes. Historical SAG63-4 disagreement uses a qualified genus fallback; Volvox nagariensis rank is forma. Species matches do not certify strains.

### Original record and byte preservation

evidence: supported. Targets: CultureMech:000215.

All 5 top-level ingredients, nested stocks, prior evidence and other fields preserved; original bytes recovered by reversing additions. One history event; no-op replay passed.

### Individual publication addition

evidence: supported. Targets: CultureMech:000215.

doi:10.1093/molbev/msq110: exact cultivation excerpt and qualified organism notes, not native growth or exact formula support.

### Individual publication addition

evidence: supported. Targets: CultureMech:000215.

doi:10.1093/gbe/evv027: exact cultivation excerpt and qualified organism notes, not native growth or exact formula support.

### Individual publication addition

evidence: supported. Targets: CultureMech:000215.

doi:10.1104/pp.16.01628: exact cultivation excerpt and qualified organism notes, not native growth or exact formula support.

### Bibliography identity and named-medium relevance

evidence: supported. Targets: CultureMech:000238.

Publication metadata, primary cultivation excerpts, original archives and Markdown linked. Relevance is named-medium use, not source-specific exact recipe certification.

### Recipe comparison and unresolved differences

evidence: unknown. Targets: CultureMech:000238.

Percentage bases and acetate hydration, or historical Volvox mineral/vitamin recipe, are unresolved. Supported observations remain in citation notes; no resolved variant, quantity or growth assertion invented.

### Scientific names, rank and role qualifications

evidence: supported. Targets: CultureMech:000238.

Scientific names and verified NCBI IDs/ranks retained in notes. Historical SAG63-4 disagreement uses a qualified genus fallback; Volvox nagariensis rank is forma. Species matches do not certify strains.

### Original record and byte preservation

evidence: supported. Targets: CultureMech:000238.

All 6 top-level ingredients, nested stocks, prior evidence and other fields preserved; original bytes recovered by reversing additions. One history event; no-op replay passed.

### Individual publication addition

evidence: supported. Targets: CultureMech:000238.

doi:10.1093/molbev/msq110: exact cultivation excerpt and qualified organism notes, not native growth or exact formula support.

### Individual publication addition

evidence: supported. Targets: CultureMech:000238.

doi:10.1093/gbe/evv027: exact cultivation excerpt and qualified organism notes, not native growth or exact formula support.

### Individual publication addition

evidence: supported. Targets: CultureMech:000238.

doi:10.1104/pp.16.01628: exact cultivation excerpt and qualified organism notes, not native growth or exact formula support.

## Findings

### merge-gates: Repository merge gates failed

major / open / confirmed; issue key: polytomella-volvox-citations-merge-gates.

Terminal merge failures retained; aggregate count equality cannot prove row equivalence or attribution. No generated outputs published.

### title-normalization: Combined inline markup and final punctuation defeat title matching

minor / open / confirmed; issue key: polytomella-volvox-citations-title-normalization.

Four post-edit title failures across three owners affect two publications. All six baseline commands passed. Eight mock-fetcher cases show markup and final-period differences pass separately but fail in combination. Verified PubMed titles are preserved; schema, term and strict checks pass.

### formulation-scope: Exact study-to-owner formulation remains unresolved

informational / open / confirmed; issue key: polytomella-volvox-citations-formulation-scope.

Named-medium cultivation is bibliographically relevant, but unsupported percent conversions and unread base recipes cannot establish exact UTEX/SAG formula identity. No inline variant, native growth, amount change or exporter edge is added.

### historical-strain: Historical Polytomella strain labels remain qualified

informational / open / confirmed; issue key: polytomella-volvox-citations-historical-strain.

The 2013 paper assigns historically P. magna-labeled SAG63-4 to the P. parva lineage, while current taxonomy retains a different label association. Notes preserve the disagreement with Polytomella genus fallback, not asserted synonymy or strain reidentification.

## Recommended Actions And Acceptance Checks

### resolve-merge-gates

Repository merge gates failed

- Diagnose maintained inputs/rules and pass both merge checks before publication.

### resolve-title-normalization

Combined inline markup and final punctuation defeat title matching

- Compose safe bibliographic-formatting rules with regression tests for combinations and real title differences; retain exact excerpt validation and rerun without rewriting correct metadata.

### resolve-formulation-scope

Exact study-to-owner formulation remains unresolved

- Inspect original base formulations and resolve study-specific differences before adding scoped native formulation or growth claims.

### resolve-historical-strain

Historical Polytomella strain labels remain qualified

- Resolve authoritative strain identity and historical label provenance before replacing the parent-only qualification.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| baseline-00 | reports/paper_citation_curation/20261014-polytomella-volvox-citations/baseline-00.log; reports/paper_citation_curation/20261014-polytomella-volvox-citations/baseline-00.log | context_only | Terminal exit code 0; not scientific approval. |
| baseline-01 | reports/paper_citation_curation/20261014-polytomella-volvox-citations/baseline-01.log; reports/paper_citation_curation/20261014-polytomella-volvox-citations/baseline-01.log | context_only | Terminal exit code 0; not scientific approval. |
| baseline-02 | reports/paper_citation_curation/20261014-polytomella-volvox-citations/baseline-02.log; reports/paper_citation_curation/20261014-polytomella-volvox-citations/baseline-02.log | context_only | Terminal exit code 0; not scientific approval. |
| baseline-03 | reports/paper_citation_curation/20261014-polytomella-volvox-citations/baseline-03.log; reports/paper_citation_curation/20261014-polytomella-volvox-citations/baseline-03.log | context_only | Terminal exit code 0; not scientific approval. |
| baseline-04 | reports/paper_citation_curation/20261014-polytomella-volvox-citations/baseline-04.log; reports/paper_citation_curation/20261014-polytomella-volvox-citations/baseline-04.log | context_only | Terminal exit code 0; not scientific approval. |
| baseline-05 | reports/paper_citation_curation/20261014-polytomella-volvox-citations/baseline-05.log; reports/paper_citation_curation/20261014-polytomella-volvox-citations/baseline-05.log | context_only | Terminal exit code 0; not scientific approval. |
| post-00 | reports/paper_citation_curation/20261014-polytomella-volvox-citations/post-00.log; reports/paper_citation_curation/20261014-polytomella-volvox-citations/post-00.log | context_only | Terminal exit code 1; not scientific approval. |
| post-01 | reports/paper_citation_curation/20261014-polytomella-volvox-citations/post-01.log; reports/paper_citation_curation/20261014-polytomella-volvox-citations/post-01.log | context_only | Terminal exit code 0; not scientific approval. |
| post-02 | reports/paper_citation_curation/20261014-polytomella-volvox-citations/post-02.log; reports/paper_citation_curation/20261014-polytomella-volvox-citations/post-02.log | context_only | Terminal exit code 1; not scientific approval. |
| post-03 | reports/paper_citation_curation/20261014-polytomella-volvox-citations/post-03.log; reports/paper_citation_curation/20261014-polytomella-volvox-citations/post-03.log | context_only | Terminal exit code 0; not scientific approval. |
| post-04 | reports/paper_citation_curation/20261014-polytomella-volvox-citations/post-04.log; reports/paper_citation_curation/20261014-polytomella-volvox-citations/post-04.log | context_only | Terminal exit code 1; not scientific approval. |
| post-05 | reports/paper_citation_curation/20261014-polytomella-volvox-citations/post-05.log; reports/paper_citation_curation/20261014-polytomella-volvox-citations/post-05.log | context_only | Terminal exit code 0; not scientific approval. |
| merge-00 | reports/paper_citation_curation/20261014-polytomella-volvox-citations/merge-00.log; reports/paper_citation_curation/20261014-polytomella-volvox-citations/merge-00.log | context_only | Terminal exit code 1; not scientific approval. |
| merge-01 | reports/paper_citation_curation/20261014-polytomella-volvox-citations/merge-01.log; reports/paper_citation_curation/20261014-polytomella-volvox-citations/merge-01.log | context_only | Terminal exit code 1; not scientific approval. |
| extra-00 | reports/paper_citation_curation/20261014-polytomella-volvox-citations/extra-00.log; reports/paper_citation_curation/20261014-polytomella-volvox-citations/extra-00.log | context_only | Terminal exit code 0; not scientific approval. |
| extra-01 | reports/paper_citation_curation/20261014-polytomella-volvox-citations/extra-01.log; reports/paper_citation_curation/20261014-polytomella-volvox-citations/extra-01.log | context_only | Terminal exit code 0; not scientific approval. |
| extra-02 | reports/paper_citation_curation/20261014-polytomella-volvox-citations/extra-02.log; reports/paper_citation_curation/20261014-polytomella-volvox-citations/extra-02.log | context_only | Terminal exit code 0; not scientific approval. |
| fast-00 | reports/paper_citation_curation/20261014-polytomella-volvox-citations/fast-test.log; reports/paper_citation_curation/20261014-polytomella-volvox-citations/fast-test.log | context_only | Terminal exit code 0; not scientific approval. |
| capuana2008 | doi:10.1093/molbev/msm245; references_cache/papers/primary_pdf/polytomella-2008-author-egjm-bristol-followup-20261014.pdf | supports | Verified publication and bounded cultivation passages; not proof of exact local formulation. |
| capuana2008-metadata | PMID:18222946; references_cache/papers/PMID_18222946.xml | supports | Title, authors, year and DOI/PMID pairing verified against PubMed XML. |
| polytomella2010 | doi:10.1007/s00294-010-0311-5; references_cache/papers/primary_pdf/polytomella-2010-author-egjm-bristol-followup-20261014.pdf | supports | Verified publication and bounded cultivation passages; not proof of exact local formulation. |
| polytomella2010-metadata | PMID:20574726; references_cache/papers/PMID_20574726.xml | supports | Title, authors, year and DOI/PMID pairing verified against PubMed XML. |
| magna2013 | doi:10.1093/gbe/evt122; references_cache/papers/primary_pdf/polytomella-2013-author-egjm-bristol-followup-20261014.pdf | supports | Verified publication and bounded cultivation passages; not proof of exact local formulation. |
| magna2013-metadata | PMID:23940100; references_cache/papers/PMID_23940100.xml | supports | Title, authors, year and DOI/PMID pairing verified against PubMed XML. |
| polytomella2014 | doi:10.1104/pp.113.233718; references_cache/papers/primary_pdf/polytomella-2014-author-egjm-bristol-followup-20261014.pdf | supports | Verified publication and bounded cultivation passages; not proof of exact local formulation. |
| polytomella2014-metadata | PMID:24563281; references_cache/papers/PMID_24563281.xml | supports | Title, authors, year and DOI/PMID pairing verified against PubMed XML. |
| polytoma2017 | doi:10.1104/pp.16.01628; references_cache/papers/primary_pdf/polytoma-2017-author-egjm-bristol-followup-20261014.pdf | supports | Verified publication and bounded cultivation passages; not proof of exact local formulation. |
| polytoma2017-metadata | PMID:27932420; references_cache/papers/PMID_27932420.xml | supports | Title, authors, year and DOI/PMID pairing verified against PubMed XML. |
| volvox2010 | doi:10.1093/molbev/msq110; references_cache/papers/primary_pdf/volvox-2010-author-egjm-bristol-followup-20261014.pdf | supports | Verified publication and bounded cultivation passages; not proof of exact local formulation. |
| volvox2010-metadata | PMID:20430860; references_cache/papers/PMID_20430860.xml | supports | Title, authors, year and DOI/PMID pairing verified against PubMed XML. |
| delvasto2015 | doi:10.1093/gbe/evv027; references_cache/papers/primary_xml/ccap-19-18-PMC5322560-20261014.xml | supports | Verified publication and bounded cultivation passages; not proof of exact local formulation. |
| delvasto2015-metadata | PMID:25663488; references_cache/papers/PMID_25663488.xml | supports | Title, authors, year and DOI/PMID pairing verified against PubMed XML. |
| taxonomy | NCBI Taxonomy; references_cache/papers/taxonomy/polytomella-volvox-20261014.xml | supports | Eight NCBI nodes used for 22 paper/organism/strain rows; source name/rank matching is not independent strain identification. |
| commentary | PMID:28377793; references_cache/papers/PMID_28377793.xml | supports | Archived abstract identifies an evolutionary addendum linked to PMID27932420; not exhaustive notice discovery. |
| claims | Guarded curation receipt; reports/paper_citation_curation/20261014-polytomella-volvox-citations/claim-plan.json | context_only | Applied scope, exact source readback, preservation, title diagnostic or unfinished discovery. |
| readback | Guarded curation receipt; reports/paper_citation_curation/20261014-polytomella-volvox-citations/final-readback.json | context_only | Applied scope, exact source readback, preservation, title diagnostic or unfinished discovery. |
| excerpts | Guarded curation receipt; reports/paper_citation_curation/20261014-polytomella-volvox-citations/evidence-readback.json | context_only | Applied scope, exact source readback, preservation, title diagnostic or unfinished discovery. |
| pending | Guarded curation receipt; reports/paper_citation_curation/20261014-polytomella-volvox-citations/pending-frontier.json | context_only | Applied scope, exact source readback, preservation, title diagnostic or unfinished discovery. |
| title-diagnostic | Guarded curation receipt; reports/paper_citation_curation/20261014-polytomella-volvox-citations/title-check-diagnostic.json | context_only | Applied scope, exact source readback, preservation, title diagnostic or unfinished discovery. |

## Limits And Additional Notes

- Self-review only; not an independent adversarial or full scientific review.
- Twenty-two medium-relevant paper/organism/strain rows, not a whole-paper inventory of background organisms.
- NCBI species/forma identity does not independently certify culture-collection strains.
- No new linked child, record merge, generated export or GitHub mutation.
- Reference-format failures, global merge findings, source gaps and broader citation discovery remain open.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T070225Z-polytomella-volvox-citations
kind: batch
repository: culturebotai/CultureMech
title: Polytomella and Volvox paper citation curation
started_at: '2026-10-14T05:48:52Z'
finished_at: '2026-10-14T07:02:25Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Curator-performed bounded assessment, not independent review.
skill: culturemech-add-paper-citation
completion: partial
verdict: needs_curation
scientific_review: false
summary: Eleven bibliography additions from seven publications across three owners.
  Exact primary excerpts and qualified organism taxonomy retained in notes. No variants,
  concentrations or growth assertions added; all prior data preserved. Four title-format
  reference failures remain.
source:
  git_revision: 41d4d390123c0d8320cd53e994470c88a1b86d8c
  state: working_tree
  inputs:
  - path: data/normalized_yaml/algae/Polytomella_Medium.yaml
    sha256: 1df5444b239e8af4b0fb10628b1cb03813df861fd8bdf386c98ee97bab02d11a
    role: target
  - path: data/normalized_yaml/algae/Volvox_Medium.yaml
    sha256: 0020b8cb596b4295e9b203785516d4a80282101350deeb7c45ec3a074a78cbd4
    role: target
  - path: data/normalized_yaml/algae/volvox.yaml
    sha256: c22680632996a260aa3e30e6592a9fed5f18d54f62f8c21c9d3ecd00c2cb4dd8
    role: target
  - path: src/culturemech/export/kgx_export.py
    sha256: eacbc2e7b363488cc1ed96e91737f54244dc1a2425dfa05c77ba89d0a5cd10e0
    role: context
  - path: src/culturemech/schema/culturemech.yaml
    sha256: cb8e4b047647d41f47b91d83420799555c09696c8a2a890535a74076e6f8bba6
    role: context
scope:
  description: Three normalized Polytomella and Volvox owners; bibliography and bounded
    notes
  selection: Primary named-medium cultivation passages and associated scientific-name/strain
    descriptions
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - CultureMech:000186
  - CultureMech:000215
  - CultureMech:000238
  exclusions:
  - target: Full-record scientific approval
    reason: Prior fields preserved, not recertified.
  - target: All possible citations and newly discovered follow-up papers
    reason: Active source queue; this is not citation exhaustion.
targets:
- target_id: CultureMech:000186
  path: data/normalized_yaml/algae/Polytomella_Medium.yaml
  label: polytomella_medium
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/Polytomella_Medium.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:000215
  path: data/normalized_yaml/algae/volvox.yaml
  label: volvox
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/volvox.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:000238
  path: data/normalized_yaml/algae/Volvox_Medium.yaml
  label: volvox_medium
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/Volvox_Medium.yaml
    role: authoritative normalized recipe
checks:
- check_id: baseline-00
  name: just validate data/normalized_yaml/algae/Polytomella_Medium.yaml
  command: just validate data/normalized_yaml/algae/Polytomella_Medium.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000186
  evidence_ids:
  - baseline-00
  summary: Actual outcome; failures retained without waiver.
- check_id: baseline-01
  name: just validate-strict data/normalized_yaml/algae/Polytomella_Medium.yaml
  command: just validate-strict data/normalized_yaml/algae/Polytomella_Medium.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000186
  evidence_ids:
  - baseline-01
  summary: Actual outcome; failures retained without waiver.
- check_id: baseline-02
  name: just validate data/normalized_yaml/algae/volvox.yaml
  command: just validate data/normalized_yaml/algae/volvox.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000215
  evidence_ids:
  - baseline-02
  summary: Actual outcome; failures retained without waiver.
- check_id: baseline-03
  name: just validate-strict data/normalized_yaml/algae/volvox.yaml
  command: just validate-strict data/normalized_yaml/algae/volvox.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000215
  evidence_ids:
  - baseline-03
  summary: Actual outcome; failures retained without waiver.
- check_id: baseline-04
  name: just validate data/normalized_yaml/algae/Volvox_Medium.yaml
  command: just validate data/normalized_yaml/algae/Volvox_Medium.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000238
  evidence_ids:
  - baseline-04
  summary: Actual outcome; failures retained without waiver.
- check_id: baseline-05
  name: just validate-strict data/normalized_yaml/algae/Volvox_Medium.yaml
  command: just validate-strict data/normalized_yaml/algae/Volvox_Medium.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000238
  evidence_ids:
  - baseline-05
  summary: Actual outcome; failures retained without waiver.
- check_id: post-00
  name: just validate data/normalized_yaml/algae/Polytomella_Medium.yaml
  command: just validate data/normalized_yaml/algae/Polytomella_Medium.yaml
  required: true
  status: failed
  exit_code: 1
  target_ids:
  - CultureMech:000186
  evidence_ids:
  - post-00
  summary: Actual outcome; failures retained without waiver.
- check_id: post-01
  name: just validate-strict data/normalized_yaml/algae/Polytomella_Medium.yaml
  command: just validate-strict data/normalized_yaml/algae/Polytomella_Medium.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000186
  evidence_ids:
  - post-01
  summary: Actual outcome; failures retained without waiver.
- check_id: post-02
  name: just validate data/normalized_yaml/algae/volvox.yaml
  command: just validate data/normalized_yaml/algae/volvox.yaml
  required: true
  status: failed
  exit_code: 1
  target_ids:
  - CultureMech:000215
  evidence_ids:
  - post-02
  summary: Actual outcome; failures retained without waiver.
- check_id: post-03
  name: just validate-strict data/normalized_yaml/algae/volvox.yaml
  command: just validate-strict data/normalized_yaml/algae/volvox.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000215
  evidence_ids:
  - post-03
  summary: Actual outcome; failures retained without waiver.
- check_id: post-04
  name: just validate data/normalized_yaml/algae/Volvox_Medium.yaml
  command: just validate data/normalized_yaml/algae/Volvox_Medium.yaml
  required: true
  status: failed
  exit_code: 1
  target_ids:
  - CultureMech:000238
  evidence_ids:
  - post-04
  summary: Actual outcome; failures retained without waiver.
- check_id: post-05
  name: just validate-strict data/normalized_yaml/algae/Volvox_Medium.yaml
  command: just validate-strict data/normalized_yaml/algae/Volvox_Medium.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000238
  evidence_ids:
  - post-05
  summary: Actual outcome; failures retained without waiver.
- check_id: merge-00
  name: just verify-merges
  command: just verify-merges
  required: true
  status: failed
  exit_code: 1
  target_ids:
  - CultureMech:000186
  - CultureMech:000215
  - CultureMech:000238
  evidence_ids:
  - merge-00
  summary: Actual outcome; failures retained without waiver.
- check_id: merge-01
  name: just audit-merge-freshness
  command: just audit-merge-freshness
  required: true
  status: failed
  exit_code: 1
  target_ids:
  - CultureMech:000186
  - CultureMech:000215
  - CultureMech:000238
  evidence_ids:
  - merge-01
  summary: Actual outcome; failures retained without waiver.
- check_id: extra-00
  name: /tmp/culturemech-parallel-env-20261012/bin/python scripts/validate_claude_skills.py
  command: /tmp/culturemech-parallel-env-20261012/bin/python scripts/validate_claude_skills.py
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000186
  - CultureMech:000215
  - CultureMech:000238
  evidence_ids:
  - extra-00
  summary: Actual outcome; failures retained without waiver.
- check_id: extra-01
  name: git diff --check
  command: git diff --check
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000186
  - CultureMech:000215
  - CultureMech:000238
  evidence_ids:
  - extra-01
  summary: Actual outcome; failures retained without waiver.
- check_id: extra-02
  name: /tmp/culturemech-parallel-env-20261012/bin/python /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech/reports/paper_citation_curation/20261014-polytomella-volvox-citations/curate.py
    --apply
  command: /tmp/culturemech-parallel-env-20261012/bin/python /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech/reports/paper_citation_curation/20261014-polytomella-volvox-citations/curate.py
    --apply
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000186
  - CultureMech:000215
  - CultureMech:000238
  evidence_ids:
  - extra-02
  summary: Actual outcome; failures retained without waiver.
- check_id: fast-00
  name: just test-fast
  command: just test-fast
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000186
  - CultureMech:000215
  - CultureMech:000238
  evidence_ids:
  - fast-00
  summary: Actual outcome; failures retained without waiver.
evidence:
- evidence_id: baseline-00
  kind: validation
  reference: reports/paper_citation_curation/20261014-polytomella-volvox-citations/baseline-00.log
  locator: reports/paper_citation_curation/20261014-polytomella-volvox-citations/baseline-00.log
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Terminal exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 1b57289f81ee40378fd4cf02db916fff1b15f774301de00c88c66e94646bedac
- evidence_id: baseline-01
  kind: validation
  reference: reports/paper_citation_curation/20261014-polytomella-volvox-citations/baseline-01.log
  locator: reports/paper_citation_curation/20261014-polytomella-volvox-citations/baseline-01.log
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Terminal exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: baseline-02
  kind: validation
  reference: reports/paper_citation_curation/20261014-polytomella-volvox-citations/baseline-02.log
  locator: reports/paper_citation_curation/20261014-polytomella-volvox-citations/baseline-02.log
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Terminal exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 8e85fad3683d76bd6c3fb545f47c457c6d20f0a3795b6abae6b05d87f12134d1
- evidence_id: baseline-03
  kind: validation
  reference: reports/paper_citation_curation/20261014-polytomella-volvox-citations/baseline-03.log
  locator: reports/paper_citation_curation/20261014-polytomella-volvox-citations/baseline-03.log
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Terminal exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: baseline-04
  kind: validation
  reference: reports/paper_citation_curation/20261014-polytomella-volvox-citations/baseline-04.log
  locator: reports/paper_citation_curation/20261014-polytomella-volvox-citations/baseline-04.log
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Terminal exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 8e85fad3683d76bd6c3fb545f47c457c6d20f0a3795b6abae6b05d87f12134d1
- evidence_id: baseline-05
  kind: validation
  reference: reports/paper_citation_curation/20261014-polytomella-volvox-citations/baseline-05.log
  locator: reports/paper_citation_curation/20261014-polytomella-volvox-citations/baseline-05.log
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Terminal exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-00
  kind: validation
  reference: reports/paper_citation_curation/20261014-polytomella-volvox-citations/post-00.log
  locator: reports/paper_citation_curation/20261014-polytomella-volvox-citations/post-00.log
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Terminal exit code 1; not scientific approval.
  support: context_only
  snapshot_sha256: f6d19050d9b2a6464efe77d4ddc22663a233ed2511550355968b07a4b0d9cc3f
- evidence_id: post-01
  kind: validation
  reference: reports/paper_citation_curation/20261014-polytomella-volvox-citations/post-01.log
  locator: reports/paper_citation_curation/20261014-polytomella-volvox-citations/post-01.log
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Terminal exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-02
  kind: validation
  reference: reports/paper_citation_curation/20261014-polytomella-volvox-citations/post-02.log
  locator: reports/paper_citation_curation/20261014-polytomella-volvox-citations/post-02.log
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Terminal exit code 1; not scientific approval.
  support: context_only
  snapshot_sha256: 4b7ed9f5b8b97bb7ec7d352bac6bebe4b000e2b2bb634e824a707d2306072073
- evidence_id: post-03
  kind: validation
  reference: reports/paper_citation_curation/20261014-polytomella-volvox-citations/post-03.log
  locator: reports/paper_citation_curation/20261014-polytomella-volvox-citations/post-03.log
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Terminal exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-04
  kind: validation
  reference: reports/paper_citation_curation/20261014-polytomella-volvox-citations/post-04.log
  locator: reports/paper_citation_curation/20261014-polytomella-volvox-citations/post-04.log
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Terminal exit code 1; not scientific approval.
  support: context_only
  snapshot_sha256: d5139f0ce0b361f72ce00c66e8d33108a0c95b288bcb7f1818705c67a7b57bd9
- evidence_id: post-05
  kind: validation
  reference: reports/paper_citation_curation/20261014-polytomella-volvox-citations/post-05.log
  locator: reports/paper_citation_curation/20261014-polytomella-volvox-citations/post-05.log
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Terminal exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: merge-00
  kind: validation
  reference: reports/paper_citation_curation/20261014-polytomella-volvox-citations/merge-00.log
  locator: reports/paper_citation_curation/20261014-polytomella-volvox-citations/merge-00.log
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Terminal exit code 1; not scientific approval.
  support: context_only
  snapshot_sha256: 09a2922082db841587410042dc33d7d3f72b2601f1d6b6f2b33322471ee47f2c
- evidence_id: merge-01
  kind: validation
  reference: reports/paper_citation_curation/20261014-polytomella-volvox-citations/merge-01.log
  locator: reports/paper_citation_curation/20261014-polytomella-volvox-citations/merge-01.log
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Terminal exit code 1; not scientific approval.
  support: context_only
  snapshot_sha256: ad9620ae17ddbf4f5e08c957edda5529d5b8bfceafd402c2f784f3a6808ee191
- evidence_id: extra-00
  kind: validation
  reference: reports/paper_citation_curation/20261014-polytomella-volvox-citations/extra-00.log
  locator: reports/paper_citation_curation/20261014-polytomella-volvox-citations/extra-00.log
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Terminal exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 441bdd6ab36f5b87c9edccf771321e1c5f6c11f43bec7799e6e98cd4d756c24c
- evidence_id: extra-01
  kind: validation
  reference: reports/paper_citation_curation/20261014-polytomella-volvox-citations/extra-01.log
  locator: reports/paper_citation_curation/20261014-polytomella-volvox-citations/extra-01.log
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Terminal exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: extra-02
  kind: validation
  reference: reports/paper_citation_curation/20261014-polytomella-volvox-citations/extra-02.log
  locator: reports/paper_citation_curation/20261014-polytomella-volvox-citations/extra-02.log
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Terminal exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 598d2130e8f4eae6081e53bfe4fe10311a5384d2841a82a02509229c0e1a5df8
- evidence_id: fast-00
  kind: validation
  reference: reports/paper_citation_curation/20261014-polytomella-volvox-citations/fast-test.log
  locator: reports/paper_citation_curation/20261014-polytomella-volvox-citations/fast-test.log
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Terminal exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 65df786f0508ffeb6832f59f80543e68aa19614bd607f55b61af35f2e07d6985
- evidence_id: capuana2008
  kind: primary_source
  reference: doi:10.1093/molbev/msm245
  locator: references_cache/papers/primary_pdf/polytomella-2008-author-egjm-bristol-followup-20261014.pdf
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Verified publication and bounded cultivation passages; not proof of exact
    local formulation.
  support: supports
  snapshot_sha256: 40a3ec9781c76387cf1b184fe3e189f14fae494e7558dfd4d27a9c7597d5090e
- evidence_id: capuana2008-metadata
  kind: authority
  reference: PMID:18222946
  locator: references_cache/papers/PMID_18222946.xml
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Title, authors, year and DOI/PMID pairing verified against PubMed XML.
  support: supports
  snapshot_sha256: 729cb60ed332fd0eeac1dd8821423f159f954953a2c1c6ccd1d88f73dafb0544
- evidence_id: polytomella2010
  kind: primary_source
  reference: doi:10.1007/s00294-010-0311-5
  locator: references_cache/papers/primary_pdf/polytomella-2010-author-egjm-bristol-followup-20261014.pdf
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Verified publication and bounded cultivation passages; not proof of exact
    local formulation.
  support: supports
  snapshot_sha256: 24b70cb7e045f1f318da8d3b89e3a9609df3c8b02ddb26c1ac19089c666587e0
- evidence_id: polytomella2010-metadata
  kind: authority
  reference: PMID:20574726
  locator: references_cache/papers/PMID_20574726.xml
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Title, authors, year and DOI/PMID pairing verified against PubMed XML.
  support: supports
  snapshot_sha256: 89d8f669f438b353ce654e46acea8de37135607700a309b180ff85bffc74c02a
- evidence_id: magna2013
  kind: primary_source
  reference: doi:10.1093/gbe/evt122
  locator: references_cache/papers/primary_pdf/polytomella-2013-author-egjm-bristol-followup-20261014.pdf
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Verified publication and bounded cultivation passages; not proof of exact
    local formulation.
  support: supports
  snapshot_sha256: 0a450af76fdd97dfe951f0db3b604525cb3a1ad1127b484fd30024bc45b21f8d
- evidence_id: magna2013-metadata
  kind: authority
  reference: PMID:23940100
  locator: references_cache/papers/PMID_23940100.xml
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Title, authors, year and DOI/PMID pairing verified against PubMed XML.
  support: supports
  snapshot_sha256: 83f8314d7cd8bf010b1b2f6b81ba9561f1ad2562e2cb3df60d1531968189a512
- evidence_id: polytomella2014
  kind: primary_source
  reference: doi:10.1104/pp.113.233718
  locator: references_cache/papers/primary_pdf/polytomella-2014-author-egjm-bristol-followup-20261014.pdf
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Verified publication and bounded cultivation passages; not proof of exact
    local formulation.
  support: supports
  snapshot_sha256: bfe070cb589e89ca645e51b197d28619b871269ef420a8fcfeb542cc2f52cd9c
- evidence_id: polytomella2014-metadata
  kind: authority
  reference: PMID:24563281
  locator: references_cache/papers/PMID_24563281.xml
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Title, authors, year and DOI/PMID pairing verified against PubMed XML.
  support: supports
  snapshot_sha256: 5324f29c778bd77b40a7f646bfda51961329e3299b2fda6c65ace4ad2049ba8b
- evidence_id: polytoma2017
  kind: primary_source
  reference: doi:10.1104/pp.16.01628
  locator: references_cache/papers/primary_pdf/polytoma-2017-author-egjm-bristol-followup-20261014.pdf
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Verified publication and bounded cultivation passages; not proof of exact
    local formulation.
  support: supports
  snapshot_sha256: 675a87ce196cca85d043e5ce1862aadba693ea19723b61cbb0dede88260557af
- evidence_id: polytoma2017-metadata
  kind: authority
  reference: PMID:27932420
  locator: references_cache/papers/PMID_27932420.xml
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Title, authors, year and DOI/PMID pairing verified against PubMed XML.
  support: supports
  snapshot_sha256: a11c1a4cd92365012f9bcea9cf3361f3da59675c342bf900d0cfa594fbf9dc5b
- evidence_id: volvox2010
  kind: primary_source
  reference: doi:10.1093/molbev/msq110
  locator: references_cache/papers/primary_pdf/volvox-2010-author-egjm-bristol-followup-20261014.pdf
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Verified publication and bounded cultivation passages; not proof of exact
    local formulation.
  support: supports
  snapshot_sha256: f1b7c3842386fcfeb79057fb1326fd1e78f40568bc544a2aaf9523123f30eef1
- evidence_id: volvox2010-metadata
  kind: authority
  reference: PMID:20430860
  locator: references_cache/papers/PMID_20430860.xml
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Title, authors, year and DOI/PMID pairing verified against PubMed XML.
  support: supports
  snapshot_sha256: 881142128646ce098276b1eac288969d9f1ba4e1747622361238154d70d8ba04
- evidence_id: delvasto2015
  kind: primary_source
  reference: doi:10.1093/gbe/evv027
  locator: references_cache/papers/primary_xml/ccap-19-18-PMC5322560-20261014.xml
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Verified publication and bounded cultivation passages; not proof of exact
    local formulation.
  support: supports
  snapshot_sha256: 0d76cf45c8eb1b5db566eb98c99a22d1b26c174d4058496c9912c146ca9b7bc0
- evidence_id: delvasto2015-metadata
  kind: authority
  reference: PMID:25663488
  locator: references_cache/papers/PMID_25663488.xml
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Title, authors, year and DOI/PMID pairing verified against PubMed XML.
  support: supports
  snapshot_sha256: d14ad03a584b05bedcf7432c5234abc80b32ddcc0cb529609bfdd39ed418d56d
- evidence_id: taxonomy
  kind: authority
  reference: NCBI Taxonomy
  locator: references_cache/papers/taxonomy/polytomella-volvox-20261014.xml
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Eight NCBI nodes used for 22 paper/organism/strain rows; source name/rank
    matching is not independent strain identification.
  support: supports
  snapshot_sha256: b3751c364b2c314bce41787a0b953001a23402cfc5bdc6330631dbd493c1429c
- evidence_id: commentary
  kind: primary_source
  reference: PMID:28377793
  locator: references_cache/papers/PMID_28377793.xml
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Archived abstract identifies an evolutionary addendum linked to PMID27932420;
    not exhaustive notice discovery.
  support: supports
  snapshot_sha256: 1e986b8f7f71de1931fe64e4855cb0155d31aa4133d62b0534d9c5aa13bb3bf3
- evidence_id: claims
  kind: record_content
  reference: Guarded curation receipt
  locator: reports/paper_citation_curation/20261014-polytomella-volvox-citations/claim-plan.json
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Applied scope, exact source readback, preservation, title diagnostic or
    unfinished discovery.
  support: context_only
  snapshot_sha256: e252c23bb0f105ba99e82fce7dca2969f4283d29e131f51253d7f3a99a7ef64c
- evidence_id: readback
  kind: record_content
  reference: Guarded curation receipt
  locator: reports/paper_citation_curation/20261014-polytomella-volvox-citations/final-readback.json
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Applied scope, exact source readback, preservation, title diagnostic or
    unfinished discovery.
  support: context_only
  snapshot_sha256: 84022f82271182661975838b4c6a9140c32e580eb2ab2d9357943ad569ebc990
- evidence_id: excerpts
  kind: record_content
  reference: Guarded curation receipt
  locator: reports/paper_citation_curation/20261014-polytomella-volvox-citations/evidence-readback.json
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Applied scope, exact source readback, preservation, title diagnostic or
    unfinished discovery.
  support: context_only
  snapshot_sha256: d6ea075a985cd32d9707b4ae2ab9508ddce49601dd89d388e368fcc44cb55dce
- evidence_id: pending
  kind: record_content
  reference: Guarded curation receipt
  locator: reports/paper_citation_curation/20261014-polytomella-volvox-citations/pending-frontier.json
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Applied scope, exact source readback, preservation, title diagnostic or
    unfinished discovery.
  support: context_only
  snapshot_sha256: febe3ba5558a39adfcc5c66f4da98904e5dc0b5eab4ca1a75a18407edb50babf
- evidence_id: title-diagnostic
  kind: record_content
  reference: Guarded curation receipt
  locator: reports/paper_citation_curation/20261014-polytomella-volvox-citations/title-check-diagnostic.json
  accessed_at: '2026-10-14T07:02:25Z'
  summary: Applied scope, exact source readback, preservation, title diagnostic or
    unfinished discovery.
  support: context_only
  snapshot_sha256: 372b0b6885ac21435bae7aaf7316c107286a4a73a0827056139d12b04f74be27
assessments:
- assessment_id: identity-000186
  area: evidence
  topic: Bibliography identity and named-medium relevance
  outcome: supported
  target_ids:
  - CultureMech:000186
  evidence_ids:
  - capuana2008
  - polytomella2010
  - magna2013
  - polytomella2014
  - polytoma2017
  - claims
  summary: Publication metadata, primary cultivation excerpts, original archives and
    Markdown linked. Relevance is named-medium use, not source-specific exact recipe
    certification.
- assessment_id: formulation-000186
  area: evidence
  topic: Recipe comparison and unresolved differences
  outcome: unknown
  target_ids:
  - CultureMech:000186
  evidence_ids:
  - capuana2008
  - polytomella2010
  - magna2013
  - polytomella2014
  - polytoma2017
  - claims
  - excerpts
  summary: Percentage bases and acetate hydration, or historical Volvox mineral/vitamin
    recipe, are unresolved. Supported observations remain in citation notes; no resolved
    variant, quantity or growth assertion invented.
- assessment_id: taxonomy-000186
  area: evidence
  topic: Scientific names, rank and role qualifications
  outcome: supported
  target_ids:
  - CultureMech:000186
  evidence_ids:
  - capuana2008
  - polytomella2010
  - magna2013
  - polytomella2014
  - polytoma2017
  - taxonomy
  - claims
  - excerpts
  summary: Scientific names and verified NCBI IDs/ranks retained in notes. Historical
    SAG63-4 disagreement uses a qualified genus fallback; Volvox nagariensis rank
    is forma. Species matches do not certify strains.
- assessment_id: preservation-000186
  area: evidence
  topic: Original record and byte preservation
  outcome: supported
  target_ids:
  - CultureMech:000186
  evidence_ids:
  - capuana2008
  - polytomella2010
  - magna2013
  - polytomella2014
  - polytoma2017
  - readback
  - extra-02
  summary: All 4 top-level ingredients, nested stocks, prior evidence and other fields
    preserved; original bytes recovered by reversing additions. One history event;
    no-op replay passed.
- assessment_id: citation-000186-0
  area: evidence
  topic: Individual publication addition
  outcome: supported
  target_ids:
  - CultureMech:000186
  evidence_ids:
  - capuana2008
  - capuana2008-metadata
  - claims
  - excerpts
  summary: 'doi:10.1093/molbev/msm245: exact cultivation excerpt and qualified organism
    notes, not native growth or exact formula support.'
- assessment_id: citation-000186-1
  area: evidence
  topic: Individual publication addition
  outcome: supported
  target_ids:
  - CultureMech:000186
  evidence_ids:
  - polytomella2010
  - polytomella2010-metadata
  - claims
  - excerpts
  summary: 'doi:10.1007/s00294-010-0311-5: exact cultivation excerpt and qualified
    organism notes, not native growth or exact formula support.'
- assessment_id: citation-000186-2
  area: evidence
  topic: Individual publication addition
  outcome: supported
  target_ids:
  - CultureMech:000186
  evidence_ids:
  - magna2013
  - magna2013-metadata
  - claims
  - excerpts
  summary: 'doi:10.1093/gbe/evt122: exact cultivation excerpt and qualified organism
    notes, not native growth or exact formula support.'
- assessment_id: citation-000186-3
  area: evidence
  topic: Individual publication addition
  outcome: supported
  target_ids:
  - CultureMech:000186
  evidence_ids:
  - polytomella2014
  - polytomella2014-metadata
  - claims
  - excerpts
  summary: 'doi:10.1104/pp.113.233718: exact cultivation excerpt and qualified organism
    notes, not native growth or exact formula support.'
- assessment_id: citation-000186-4
  area: evidence
  topic: Individual publication addition
  outcome: supported
  target_ids:
  - CultureMech:000186
  evidence_ids:
  - polytoma2017
  - polytoma2017-metadata
  - claims
  - excerpts
  summary: 'doi:10.1104/pp.16.01628: exact cultivation excerpt and qualified organism
    notes, not native growth or exact formula support.'
- assessment_id: identity-000215
  area: evidence
  topic: Bibliography identity and named-medium relevance
  outcome: supported
  target_ids:
  - CultureMech:000215
  evidence_ids:
  - volvox2010
  - delvasto2015
  - polytoma2017
  - claims
  summary: Publication metadata, primary cultivation excerpts, original archives and
    Markdown linked. Relevance is named-medium use, not source-specific exact recipe
    certification.
- assessment_id: formulation-000215
  area: evidence
  topic: Recipe comparison and unresolved differences
  outcome: unknown
  target_ids:
  - CultureMech:000215
  evidence_ids:
  - volvox2010
  - delvasto2015
  - polytoma2017
  - claims
  - excerpts
  summary: Percentage bases and acetate hydration, or historical Volvox mineral/vitamin
    recipe, are unresolved. Supported observations remain in citation notes; no resolved
    variant, quantity or growth assertion invented.
- assessment_id: taxonomy-000215
  area: evidence
  topic: Scientific names, rank and role qualifications
  outcome: supported
  target_ids:
  - CultureMech:000215
  evidence_ids:
  - volvox2010
  - delvasto2015
  - polytoma2017
  - taxonomy
  - claims
  - excerpts
  summary: Scientific names and verified NCBI IDs/ranks retained in notes. Historical
    SAG63-4 disagreement uses a qualified genus fallback; Volvox nagariensis rank
    is forma. Species matches do not certify strains.
- assessment_id: preservation-000215
  area: evidence
  topic: Original record and byte preservation
  outcome: supported
  target_ids:
  - CultureMech:000215
  evidence_ids:
  - volvox2010
  - delvasto2015
  - polytoma2017
  - readback
  - extra-02
  summary: All 5 top-level ingredients, nested stocks, prior evidence and other fields
    preserved; original bytes recovered by reversing additions. One history event;
    no-op replay passed.
- assessment_id: citation-000215-0
  area: evidence
  topic: Individual publication addition
  outcome: supported
  target_ids:
  - CultureMech:000215
  evidence_ids:
  - volvox2010
  - volvox2010-metadata
  - claims
  - excerpts
  summary: 'doi:10.1093/molbev/msq110: exact cultivation excerpt and qualified organism
    notes, not native growth or exact formula support.'
- assessment_id: citation-000215-1
  area: evidence
  topic: Individual publication addition
  outcome: supported
  target_ids:
  - CultureMech:000215
  evidence_ids:
  - delvasto2015
  - delvasto2015-metadata
  - claims
  - excerpts
  summary: 'doi:10.1093/gbe/evv027: exact cultivation excerpt and qualified organism
    notes, not native growth or exact formula support.'
- assessment_id: citation-000215-2
  area: evidence
  topic: Individual publication addition
  outcome: supported
  target_ids:
  - CultureMech:000215
  evidence_ids:
  - polytoma2017
  - polytoma2017-metadata
  - claims
  - excerpts
  summary: 'doi:10.1104/pp.16.01628: exact cultivation excerpt and qualified organism
    notes, not native growth or exact formula support.'
- assessment_id: identity-000238
  area: evidence
  topic: Bibliography identity and named-medium relevance
  outcome: supported
  target_ids:
  - CultureMech:000238
  evidence_ids:
  - volvox2010
  - delvasto2015
  - polytoma2017
  - claims
  summary: Publication metadata, primary cultivation excerpts, original archives and
    Markdown linked. Relevance is named-medium use, not source-specific exact recipe
    certification.
- assessment_id: formulation-000238
  area: evidence
  topic: Recipe comparison and unresolved differences
  outcome: unknown
  target_ids:
  - CultureMech:000238
  evidence_ids:
  - volvox2010
  - delvasto2015
  - polytoma2017
  - claims
  - excerpts
  summary: Percentage bases and acetate hydration, or historical Volvox mineral/vitamin
    recipe, are unresolved. Supported observations remain in citation notes; no resolved
    variant, quantity or growth assertion invented.
- assessment_id: taxonomy-000238
  area: evidence
  topic: Scientific names, rank and role qualifications
  outcome: supported
  target_ids:
  - CultureMech:000238
  evidence_ids:
  - volvox2010
  - delvasto2015
  - polytoma2017
  - taxonomy
  - claims
  - excerpts
  summary: Scientific names and verified NCBI IDs/ranks retained in notes. Historical
    SAG63-4 disagreement uses a qualified genus fallback; Volvox nagariensis rank
    is forma. Species matches do not certify strains.
- assessment_id: preservation-000238
  area: evidence
  topic: Original record and byte preservation
  outcome: supported
  target_ids:
  - CultureMech:000238
  evidence_ids:
  - volvox2010
  - delvasto2015
  - polytoma2017
  - readback
  - extra-02
  summary: All 6 top-level ingredients, nested stocks, prior evidence and other fields
    preserved; original bytes recovered by reversing additions. One history event;
    no-op replay passed.
- assessment_id: citation-000238-0
  area: evidence
  topic: Individual publication addition
  outcome: supported
  target_ids:
  - CultureMech:000238
  evidence_ids:
  - volvox2010
  - volvox2010-metadata
  - claims
  - excerpts
  summary: 'doi:10.1093/molbev/msq110: exact cultivation excerpt and qualified organism
    notes, not native growth or exact formula support.'
- assessment_id: citation-000238-1
  area: evidence
  topic: Individual publication addition
  outcome: supported
  target_ids:
  - CultureMech:000238
  evidence_ids:
  - delvasto2015
  - delvasto2015-metadata
  - claims
  - excerpts
  summary: 'doi:10.1093/gbe/evv027: exact cultivation excerpt and qualified organism
    notes, not native growth or exact formula support.'
- assessment_id: citation-000238-2
  area: evidence
  topic: Individual publication addition
  outcome: supported
  target_ids:
  - CultureMech:000238
  evidence_ids:
  - polytoma2017
  - polytoma2017-metadata
  - claims
  - excerpts
  summary: 'doi:10.1104/pp.16.01628: exact cultivation excerpt and qualified organism
    notes, not native growth or exact formula support.'
findings:
- finding_id: merge-gates
  issue_key: polytomella-volvox-citations-merge-gates
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Repository merge gates failed
  description: Terminal merge failures retained; aggregate count equality cannot prove
    row equivalence or attribution. No generated outputs published.
  target_ids:
  - CultureMech:000186
  - CultureMech:000215
  - CultureMech:000238
  evidence_ids:
  - merge-00
  - merge-01
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/Polytomella_Medium.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/volvox.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/Volvox_Medium.yaml
    role: authoritative normalized recipe
- finding_id: title-normalization
  issue_key: polytomella-volvox-citations-title-normalization
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Combined inline markup and final punctuation defeat title matching
  description: Four post-edit title failures across three owners affect two publications.
    All six baseline commands passed. Eight mock-fetcher cases show markup and final-period
    differences pass separately but fail in combination. Verified PubMed titles are
    preserved; schema, term and strict checks pass.
  target_ids:
  - CultureMech:000186
  - CultureMech:000215
  - CultureMech:000238
  evidence_ids:
  - post-00
  - post-02
  - post-04
  - title-diagnostic
  - polytomella2014-metadata
  - polytoma2017-metadata
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/Polytomella_Medium.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/volvox.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/Volvox_Medium.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: src/culturemech/validation/recipe_references.py
    role: maintained title validation or regression coverage
  - repository: culturebotai/CultureMech
    path: tests/test_literature_title_markup.py
    role: maintained title validation or regression coverage
- finding_id: formulation-scope
  issue_key: polytomella-volvox-citations-formulation-scope
  category: evidence
  severity: informational
  status: open
  certainty: confirmed
  title: Exact study-to-owner formulation remains unresolved
  description: Named-medium cultivation is bibliographically relevant, but unsupported
    percent conversions and unread base recipes cannot establish exact UTEX/SAG formula
    identity. No inline variant, native growth, amount change or exporter edge is
    added.
  target_ids:
  - CultureMech:000186
  - CultureMech:000215
  - CultureMech:000238
  evidence_ids:
  - claims
  - excerpts
  - pending
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/Polytomella_Medium.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/volvox.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/Volvox_Medium.yaml
    role: authoritative normalized recipe
- finding_id: historical-strain
  issue_key: polytomella-volvox-citations-historical-strain
  category: evidence
  severity: informational
  status: open
  certainty: confirmed
  title: Historical Polytomella strain labels remain qualified
  description: The 2013 paper assigns historically P. magna-labeled SAG63-4 to the
    P. parva lineage, while current taxonomy retains a different label association.
    Notes preserve the disagreement with Polytomella genus fallback, not asserted
    synonymy or strain reidentification.
  target_ids:
  - CultureMech:000186
  evidence_ids:
  - magna2013
  - taxonomy
  - claims
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/Polytomella_Medium.yaml
    role: authoritative normalized recipe
actions:
- action_id: resolve-merge-gates
  description: Repository merge gates failed
  finding_ids:
  - merge-gates
  target_ids:
  - CultureMech:000186
  - CultureMech:000215
  - CultureMech:000238
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/Polytomella_Medium.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/volvox.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/Volvox_Medium.yaml
    role: authoritative normalized recipe
  acceptance_checks:
  - Diagnose maintained inputs/rules and pass both merge checks before publication.
- action_id: resolve-title-normalization
  description: Combined inline markup and final punctuation defeat title matching
  finding_ids:
  - title-normalization
  target_ids:
  - CultureMech:000186
  - CultureMech:000215
  - CultureMech:000238
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/Polytomella_Medium.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/volvox.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/Volvox_Medium.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: src/culturemech/validation/recipe_references.py
    role: maintained title validation or regression coverage
  - repository: culturebotai/CultureMech
    path: tests/test_literature_title_markup.py
    role: maintained title validation or regression coverage
  acceptance_checks:
  - Compose safe bibliographic-formatting rules with regression tests for combinations
    and real title differences; retain exact excerpt validation and rerun without
    rewriting correct metadata.
- action_id: resolve-formulation-scope
  description: Exact study-to-owner formulation remains unresolved
  finding_ids:
  - formulation-scope
  target_ids:
  - CultureMech:000186
  - CultureMech:000215
  - CultureMech:000238
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/Polytomella_Medium.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/volvox.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/Volvox_Medium.yaml
    role: authoritative normalized recipe
  acceptance_checks:
  - Inspect original base formulations and resolve study-specific differences before
    adding scoped native formulation or growth claims.
- action_id: resolve-historical-strain
  description: Historical Polytomella strain labels remain qualified
  finding_ids:
  - historical-strain
  target_ids:
  - CultureMech:000186
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/Polytomella_Medium.yaml
    role: authoritative normalized recipe
  acceptance_checks:
  - Resolve authoritative strain identity and historical label provenance before replacing
    the parent-only qualification.
limitations:
- Self-review only; not an independent adversarial or full scientific review.
- Twenty-two medium-relevant paper/organism/strain rows, not a whole-paper inventory
  of background organisms.
- NCBI species/forma identity does not independently certify culture-collection strains.
- No new linked child, record merge, generated export or GitHub mutation.
- Reference-format failures, global merge findings, source gaps and broader citation
  discovery remain open.
```
