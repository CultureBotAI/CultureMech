# 2ASW paper citations and study-variant amount review

- Review: 20261014T031605Z-2asw-study-citations
- Repository: culturebotai/CultureMech
- Started UTC: 2026-10-14T02:39:14Z
- Finished UTC: 2026-10-14T03:16:05Z
- Reviewer: codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Five citations from three archived papers, four inline entries for two study-specific variants, and four DOI/excerpt-backed amount evidence items across two owners. All 27 pre-existing ingredients preserved. No new native growth association. Actual failing gates and unresolved full formulas retained.

## Scope And Provenance

Two 2ASW normalized owners; new bibliography and two study-variant amount claims per owner

Selection: Archived 2023 and 2015 explicit 2ASW methods, plus 2017 strain/BioProject identity evidence for the algae owner
Coverage: full; 2 reviewed / 2 in the declared population.
Source: working_tree at Git base 41d4d390123c0d8320cd53e994470c88a1b86d8c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:000038 | data/normalized_yaml/algae/2asw.yaml | maintained | 2asw |
| CultureMech:000415 | data/normalized_yaml/bacterial/2asw.yaml | maintained | 2asw |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate data/normalized_yaml/algae/2asw.yaml | passed | True | CultureMech:000038 | Actual check outcome; failures retained without waiver. |
| just validate-strict data/normalized_yaml/algae/2asw.yaml | passed | True | CultureMech:000038 | Actual check outcome; failures retained without waiver. |
| just validate data/normalized_yaml/bacterial/2asw.yaml | passed | True | CultureMech:000415 | Actual check outcome; failures retained without waiver. |
| just validate-strict data/normalized_yaml/bacterial/2asw.yaml | passed | True | CultureMech:000415 | Actual check outcome; failures retained without waiver. |
| just validate data/normalized_yaml/algae/2asw.yaml | failed | True | CultureMech:000038 | Actual check outcome; failures retained without waiver. |
| just validate-strict data/normalized_yaml/algae/2asw.yaml | passed | True | CultureMech:000038 | Actual check outcome; failures retained without waiver. |
| just validate data/normalized_yaml/bacterial/2asw.yaml | failed | True | CultureMech:000415 | Actual check outcome; failures retained without waiver. |
| just validate-strict data/normalized_yaml/bacterial/2asw.yaml | passed | True | CultureMech:000415 | Actual check outcome; failures retained without waiver. |
| just verify-merges | failed | True | CultureMech:000038, CultureMech:000415 | Actual check outcome; failures retained without waiver. |
| just audit-merge-freshness | failed | True | CultureMech:000038, CultureMech:000415 | Actual check outcome; failures retained without waiver. |
| /tmp/culturemech-parallel-env-20261012/bin/python scripts/validate_claude_skills.py | passed | True | CultureMech:000038, CultureMech:000415 | Actual check outcome; failures retained without waiver. |
| git diff --check | passed | True | CultureMech:000038, CultureMech:000415 | Actual check outcome; failures retained without waiver. |
| /tmp/culturemech-parallel-env-20261012/bin/python /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech/reports/paper_citation_curation/20261014-2asw-study-citations/curate.py --apply | passed | True | CultureMech:000038, CultureMech:000415 | Actual check outcome; failures retained without waiver. |
| just test-fast | passed | True | CultureMech:000038, CultureMech:000415 | Actual check outcome; failures retained without waiver. |

## Scientific And Domain Assessments

### Publication identity and source-owner relevance

evidence: supported. Targets: CultureMech:000038.

3 paper citations with verified title, authors, year, identifiers, primary archives and Markdown. Genome paper is identity-only and attached only to the owner already citing its BioProject.

### Study variants and unresolved full formulas

evidence: unknown. Targets: CultureMech:000038.

Two bounded inline variants capture explicit study statements; parent quantities and source-owner differences remain unchanged. Table S2 and the mismatched base citation prevent complete formulation certification.

### Scientific names, actual ranks and experimental roles

evidence: supported. Targets: CultureMech:000038.

Eighteen Dunaliella maintenance-strain rows retained separately; UTEX LB 200, genus-only strains and FACHB-847 have qualified parent matches. Other-media and background observations do not imply parent growth. No native growth association was added.

### Existing claims and recipe presentation

evidence: supported. Targets: CultureMech:000038.

13 ingredient entries and every pre-existing field preserved. Reversing the additions recovers original bytes; exactly one history event per owner; no-op replay passes.

### Evidence-backed inline variant concentration

evidence: supported. Targets: CultureMech:000038.

status=add; field=variants[name=2asw_1_5_m_nacl].modifications[0]; old=absent study-variant entry; new=1.5 M NaCl, explicitly stated medium concentration; parent amount unchanged.

Reference: doi:10.1128/spectrum.00069-23. Exact snippet: D. salina was cultivated in 2ASW (artificial seawater) medium containing 1.5 M NaCl Locator and claim linkage: Supports only variants[name=2asw_1_5_m_nacl].modifications[0]: explicitly reported 1.5 M NaCl for Dunaliella salina CCAP 19/18, in Materials and Methods / Algal strains and cultivation conditions. Not a complete recipe certification, stock value, conversion, or canonical parent amount. canonical scientific name=Dunaliella salina; NCBITaxon:3046; actual rank=species; taxonomy_match=exact_name_at_species_rank; lookup_url=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=3046; cultivation applies to this study formulation only. Table S2 is uninspected. Taxonomy checked against NCBI EFetch archived 2026-10-14 at references_cache/papers/taxonomy/2asw-20261014.xml. Species mappings do not verify exact strain identity.  Calculation: none. Complete stock/final-volume formulation remains unresolved. The DOI/excerpt evidence is attached to this variant in the owner YAML, not merely this report.

### Evidence-backed inline variant concentration

evidence: supported. Targets: CultureMech:000038.

status=add; field=variants[name=2asw_sea_salt_substitution_33_6_g_l].modifications[0]; old=absent study-variant entry; new=33.6 g/L sea-salt mixture replacing NaCl, explicitly stated maintenance-medium concentration; parent amount unchanged.

Reference: doi:10.3389/fenrg.2015.00020. Exact snippet: 33.6 g/L of sea salts were used in place of the NaCl. Locator and claim linkage: Supports only variants[name=2asw_sea_salt_substitution_33_6_g_l].modifications[0]: directly reported sea-salt replacement amount in Materials and Methods / Strains and media. It is the maintenance-medium mixture concentration, not a stock or pure NaCl value. No arithmetic was performed. The paragraph assigns this modified 2ASW to the 18 Dunaliella strain rows in Table 1, whose scientific names and taxonomy qualifications are preserved in this paper's citation notes. Centrate results are not parent or maintenance-medium growth metrics. Calculation: none. Complete stock/final-volume formulation remains unresolved. The DOI/excerpt evidence is attached to this variant in the owner YAML, not merely this report.

### Publication identity and source-owner relevance

evidence: supported. Targets: CultureMech:000415.

2 paper citations with verified title, authors, year, identifiers, primary archives and Markdown. Genome paper is identity-only and attached only to the owner already citing its BioProject.

### Study variants and unresolved full formulas

evidence: unknown. Targets: CultureMech:000415.

Two bounded inline variants capture explicit study statements; parent quantities and source-owner differences remain unchanged. Table S2 and the mismatched base citation prevent complete formulation certification.

### Scientific names, actual ranks and experimental roles

evidence: supported. Targets: CultureMech:000415.

Eighteen Dunaliella maintenance-strain rows retained separately; UTEX LB 200, genus-only strains and FACHB-847 have qualified parent matches. Other-media and background observations do not imply parent growth. No native growth association was added.

### Existing claims and recipe presentation

evidence: supported. Targets: CultureMech:000415.

14 ingredient entries and every pre-existing field preserved. Reversing the additions recovers original bytes; exactly one history event per owner; no-op replay passes.

### Evidence-backed inline variant concentration

evidence: supported. Targets: CultureMech:000415.

status=add; field=variants[name=2asw_1_5_m_nacl].modifications[0]; old=absent study-variant entry; new=1.5 M NaCl, explicitly stated medium concentration; parent amount unchanged.

Reference: doi:10.1128/spectrum.00069-23. Exact snippet: D. salina was cultivated in 2ASW (artificial seawater) medium containing 1.5 M NaCl Locator and claim linkage: Supports only variants[name=2asw_1_5_m_nacl].modifications[0]: explicitly reported 1.5 M NaCl for Dunaliella salina CCAP 19/18, in Materials and Methods / Algal strains and cultivation conditions. Not a complete recipe certification, stock value, conversion, or canonical parent amount. canonical scientific name=Dunaliella salina; NCBITaxon:3046; actual rank=species; taxonomy_match=exact_name_at_species_rank; lookup_url=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=3046; cultivation applies to this study formulation only. Table S2 is uninspected. Taxonomy checked against NCBI EFetch archived 2026-10-14 at references_cache/papers/taxonomy/2asw-20261014.xml. Species mappings do not verify exact strain identity.  Calculation: none. Complete stock/final-volume formulation remains unresolved. The DOI/excerpt evidence is attached to this variant in the owner YAML, not merely this report.

### Evidence-backed inline variant concentration

evidence: supported. Targets: CultureMech:000415.

status=add; field=variants[name=2asw_sea_salt_substitution_33_6_g_l].modifications[0]; old=absent study-variant entry; new=33.6 g/L sea-salt mixture replacing NaCl, explicitly stated maintenance-medium concentration; parent amount unchanged.

Reference: doi:10.3389/fenrg.2015.00020. Exact snippet: 33.6 g/L of sea salts were used in place of the NaCl. Locator and claim linkage: Supports only variants[name=2asw_sea_salt_substitution_33_6_g_l].modifications[0]: directly reported sea-salt replacement amount in Materials and Methods / Strains and media. It is the maintenance-medium mixture concentration, not a stock or pure NaCl value. No arithmetic was performed. The paragraph assigns this modified 2ASW to the 18 Dunaliella strain rows in Table 1, whose scientific names and taxonomy qualifications are preserved in this paper's citation notes. Centrate results are not parent or maintenance-medium growth metrics. Calculation: none. Complete stock/final-volume formulation remains unresolved. The DOI/excerpt evidence is attached to this variant in the owner YAML, not merely this report.

## Findings

### merge-gates: Repository merge gates failed

major / open / confirmed; issue key: 2asw-study-citations-merge-gates.

Actual failures retained, without assuming that equal counts prove unchanged rows or attributing all failures to this batch. No generated publication.

### reference-checks: Newly cited papers expose native reference-validation limitations

minor / open / confirmed; issue key: 2asw-study-citations-reference-checks.

Baseline passed. Post-edit checks report title differences containing publisher italic markup and full-text methods excerpts unavailable through the automatic DOI fetch. Raw JATS/HTML and Markdown support the stored plain titles and exact excerpts. These newly exposed failures are recorded, not mislabeled baseline failures or silently waived.

### formulation-and-scope: Complete study formulas and machine-readable growth scope remain unresolved

informational / open / confirmed; issue key: 2asw-study-citations-formulation-and-scope.

Only the documented study amounts are resolved. Missing supplement, mismatched base citation, disputed strain identity and the current organism/export scope model prevent complete formulations or parent growth assertions. Existing pre-curation claims were preserved, not scientifically recertified.

## Recommended Actions And Acceptance Checks

### resolve-merge-gates

Repository merge gates failed

- Diagnose maintained merge inputs/rules and rerun both gates before publication.

### resolve-reference-checks

Newly cited papers expose native reference-validation limitations

- Improve the maintained reference fetch/title normalization and full-text coverage; do not alter correct source claims just to pass an abstract-only check.

### resolve-formulation-and-scope

Complete study formulas and machine-readable growth scope remain unresolved

- Inspect full study recipes and resolve taxon/strain/formulation scope before curating or exporting positive native growth associations.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| baseline-00 | reports/paper_citation_curation/20261014-2asw-study-citations/baseline-00.log; reports/paper_citation_curation/20261014-2asw-study-citations/baseline-00.log; Complete terminal output | context_only | Exit code 0; not scientific approval. |
| baseline-01 | reports/paper_citation_curation/20261014-2asw-study-citations/baseline-01.log; reports/paper_citation_curation/20261014-2asw-study-citations/baseline-01.log; Complete terminal output | context_only | Exit code 0; not scientific approval. |
| baseline-02 | reports/paper_citation_curation/20261014-2asw-study-citations/baseline-02.log; reports/paper_citation_curation/20261014-2asw-study-citations/baseline-02.log; Complete terminal output | context_only | Exit code 0; not scientific approval. |
| baseline-03 | reports/paper_citation_curation/20261014-2asw-study-citations/baseline-03.log; reports/paper_citation_curation/20261014-2asw-study-citations/baseline-03.log; Complete terminal output | context_only | Exit code 0; not scientific approval. |
| post-00 | reports/paper_citation_curation/20261014-2asw-study-citations/post-00.log; reports/paper_citation_curation/20261014-2asw-study-citations/post-00.log; Complete terminal output | context_only | Exit code 1; not scientific approval. |
| post-01 | reports/paper_citation_curation/20261014-2asw-study-citations/post-01.log; reports/paper_citation_curation/20261014-2asw-study-citations/post-01.log; Complete terminal output | context_only | Exit code 0; not scientific approval. |
| post-02 | reports/paper_citation_curation/20261014-2asw-study-citations/post-02.log; reports/paper_citation_curation/20261014-2asw-study-citations/post-02.log; Complete terminal output | context_only | Exit code 1; not scientific approval. |
| post-03 | reports/paper_citation_curation/20261014-2asw-study-citations/post-03.log; reports/paper_citation_curation/20261014-2asw-study-citations/post-03.log; Complete terminal output | context_only | Exit code 0; not scientific approval. |
| merge-00 | reports/paper_citation_curation/20261014-2asw-study-citations/merge-00.log; reports/paper_citation_curation/20261014-2asw-study-citations/merge-00.log; Complete terminal output | context_only | Exit code 1; not scientific approval. |
| merge-01 | reports/paper_citation_curation/20261014-2asw-study-citations/merge-01.log; reports/paper_citation_curation/20261014-2asw-study-citations/merge-01.log; Complete terminal output | context_only | Exit code 1; not scientific approval. |
| extra-00 | reports/paper_citation_curation/20261014-2asw-study-citations/extra-00.log; reports/paper_citation_curation/20261014-2asw-study-citations/extra-00.log; Complete terminal output | context_only | Exit code 0; not scientific approval. |
| extra-01 | reports/paper_citation_curation/20261014-2asw-study-citations/extra-01.log; reports/paper_citation_curation/20261014-2asw-study-citations/extra-01.log; Complete terminal output | context_only | Exit code 0; not scientific approval. |
| extra-02 | reports/paper_citation_curation/20261014-2asw-study-citations/extra-02.log; reports/paper_citation_curation/20261014-2asw-study-citations/extra-02.log; Complete terminal output | context_only | Exit code 0; not scientific approval. |
| fast-00 | reports/paper_citation_curation/20261014-2asw-study-citations/fast-test.log; reports/paper_citation_curation/20261014-2asw-study-citations/fast-test.log; Complete terminal output | context_only | Exit code 0; not scientific approval. |
| paper-2023 | doi:10.1128/spectrum.00069-23; references_cache/papers/primary_xml/2asw-spectrum-2023-europepmc-20261014.xml; full JATS body; external supplement not retrieved | supports | Original article identity and bounded methods/identity passages inspected; external supplement not inferred. |
| paper-2017 | doi:10.1128/genomeA.01105-17; references_cache/papers/primary_xml/ccap-19-18-PMC5658486-20261014.xml; full JATS article | supports | Original article identity and bounded methods/identity passages inspected; external supplement not inferred. |
| paper-2015 | doi:10.3389/fenrg.2015.00020; references_cache/papers/primary_html/2asw-frontiers-2015-20261014.html; publisher HTML full article including Table 1 | supports | Original article identity and bounded methods/identity passages inspected; external supplement not inferred. |
| taxonomy | NCBI Taxonomy; references_cache/papers/taxonomy/2asw-20261014.xml; Eleven used nodes: scientific names, actual ranks and synonyms | supports | Species name-level matches and parent-only genus fallbacks explicitly distinguished. |
| ccap-recipe | https://www.ccap.ac.uk/wp-content/uploads/MR_2ASW.pdf; references_cache/papers/primary_pdf/2asw-ccap-2asw-20261014.pdf; Revision 002, 29 May 2026; stock and seawater basis | context_only | Flattened imports are not a complete basis for a total-NaCl comparison or confirmation of historical study formulations. |
| exporter | Current KGX implementation; src/culturemech/export/kgx_export.py; organism_grows_in_medium_edge | context_only | Positive edges use the parent ID and do not honor scoped_to_variant; no new native growth assertions added. |
| claims | Guarded curation receipt; reports/paper_citation_curation/20261014-2asw-study-citations/claim-plan-v2.json; claim-plan-v2.json | context_only | Exact applied claims, source scope, preservation checks and unfinished discovery. |
| readback | Guarded curation receipt; reports/paper_citation_curation/20261014-2asw-study-citations/final-readback.json; final-readback.json | context_only | Exact applied claims, source scope, preservation checks and unfinished discovery. |
| excerpts | Guarded curation receipt; reports/paper_citation_curation/20261014-2asw-study-citations/evidence-readback.json; evidence-readback.json | context_only | Exact applied claims, source scope, preservation checks and unfinished discovery. |
| pending | Guarded curation receipt; reports/paper_citation_curation/20261014-2asw-study-citations/pending-frontier.json; pending-frontier.json | context_only | Exact applied claims, source scope, preservation checks and unfinished discovery. |

## Limits And Additional Notes

- Focused self-review, not independent adversarial or complete scientific review.
- Only 2ASW-relevant organism passages inventoried; no whole-paper inventory claim.
- Table S2 not retrieved; 2015 base-reference mismatch unresolved; other ingredients and total seawater salt contribution unverified.
- Species name mappings do not establish an exact strain match; parent-only matches stay in notes.
- No native positive growth assertions, parent amount changes, record merge, export, or GitHub publication.
- Reference and global merge gate failures remain open. Corpus-wide citation discovery remains active.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T031605Z-2asw-study-citations
kind: batch
repository: culturebotai/CultureMech
title: 2ASW paper citations and study-variant amount review
started_at: '2026-10-14T02:39:14Z'
finished_at: '2026-10-14T03:16:05Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Curator-performed focused assessment, not independent review.
skill: culturemech-add-paper-citation; review-ingredient-concentrations
completion: partial
verdict: needs_curation
scientific_review: false
summary: Five citations from three archived papers, four inline entries for two study-specific
  variants, and four DOI/excerpt-backed amount evidence items across two owners. All
  27 pre-existing ingredients preserved. No new native growth association. Actual
  failing gates and unresolved full formulas retained.
source:
  git_revision: 41d4d390123c0d8320cd53e994470c88a1b86d8c
  state: working_tree
  inputs:
  - path: data/normalized_yaml/algae/2asw.yaml
    sha256: 0ba654a5395797550d80a1b3f3e48930862a2188d4568d58c6cda673c47f1ee7
    role: target
  - path: data/normalized_yaml/bacterial/2asw.yaml
    sha256: 53791685ae44730a58fbbe48317248326a162377283a40c727eec72b7509bdb9
    role: target
  - path: src/culturemech/export/kgx_export.py
    sha256: eacbc2e7b363488cc1ed96e91737f54244dc1a2425dfa05c77ba89d0a5cd10e0
    role: context
  - path: src/culturemech/schema/culturemech.yaml
    sha256: cb8e4b047647d41f47b91d83420799555c09696c8a2a890535a74076e6f8bba6
    role: context
scope:
  description: Two 2ASW normalized owners; new bibliography and two study-variant
    amount claims per owner
  selection: Archived 2023 and 2015 explicit 2ASW methods, plus 2017 strain/BioProject
    identity evidence for the algae owner
  coverage: full
  population_size: 2
  reviewed_target_ids:
  - CultureMech:000038
  - CultureMech:000415
  exclusions:
  - target: Existing ingredients, growth claims and full-record approval
    reason: Preserved without new scientific certification; no canonical concentration
      audit.
  - target: Other media and all possible citations
    reason: Separate active discovery queue; not an exhaustion claim.
targets:
- target_id: CultureMech:000038
  path: data/normalized_yaml/algae/2asw.yaml
  label: 2asw
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/2asw.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:000415
  path: data/normalized_yaml/bacterial/2asw.yaml
  label: 2asw
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/2asw.yaml
    role: authoritative normalized recipe
checks:
- check_id: baseline-00
  name: just validate data/normalized_yaml/algae/2asw.yaml
  command: just validate data/normalized_yaml/algae/2asw.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000038
  evidence_ids:
  - baseline-00
  summary: Actual check outcome; failures retained without waiver.
- check_id: baseline-01
  name: just validate-strict data/normalized_yaml/algae/2asw.yaml
  command: just validate-strict data/normalized_yaml/algae/2asw.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000038
  evidence_ids:
  - baseline-01
  summary: Actual check outcome; failures retained without waiver.
- check_id: baseline-02
  name: just validate data/normalized_yaml/bacterial/2asw.yaml
  command: just validate data/normalized_yaml/bacterial/2asw.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000415
  evidence_ids:
  - baseline-02
  summary: Actual check outcome; failures retained without waiver.
- check_id: baseline-03
  name: just validate-strict data/normalized_yaml/bacterial/2asw.yaml
  command: just validate-strict data/normalized_yaml/bacterial/2asw.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000415
  evidence_ids:
  - baseline-03
  summary: Actual check outcome; failures retained without waiver.
- check_id: post-00
  name: just validate data/normalized_yaml/algae/2asw.yaml
  command: just validate data/normalized_yaml/algae/2asw.yaml
  required: true
  status: failed
  exit_code: 1
  target_ids:
  - CultureMech:000038
  evidence_ids:
  - post-00
  summary: Actual check outcome; failures retained without waiver.
- check_id: post-01
  name: just validate-strict data/normalized_yaml/algae/2asw.yaml
  command: just validate-strict data/normalized_yaml/algae/2asw.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000038
  evidence_ids:
  - post-01
  summary: Actual check outcome; failures retained without waiver.
- check_id: post-02
  name: just validate data/normalized_yaml/bacterial/2asw.yaml
  command: just validate data/normalized_yaml/bacterial/2asw.yaml
  required: true
  status: failed
  exit_code: 1
  target_ids:
  - CultureMech:000415
  evidence_ids:
  - post-02
  summary: Actual check outcome; failures retained without waiver.
- check_id: post-03
  name: just validate-strict data/normalized_yaml/bacterial/2asw.yaml
  command: just validate-strict data/normalized_yaml/bacterial/2asw.yaml
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000415
  evidence_ids:
  - post-03
  summary: Actual check outcome; failures retained without waiver.
- check_id: merge-00
  name: just verify-merges
  command: just verify-merges
  required: true
  status: failed
  exit_code: 1
  target_ids:
  - CultureMech:000038
  - CultureMech:000415
  evidence_ids:
  - merge-00
  summary: Actual check outcome; failures retained without waiver.
- check_id: merge-01
  name: just audit-merge-freshness
  command: just audit-merge-freshness
  required: true
  status: failed
  exit_code: 1
  target_ids:
  - CultureMech:000038
  - CultureMech:000415
  evidence_ids:
  - merge-01
  summary: Actual check outcome; failures retained without waiver.
- check_id: extra-00
  name: /tmp/culturemech-parallel-env-20261012/bin/python scripts/validate_claude_skills.py
  command: /tmp/culturemech-parallel-env-20261012/bin/python scripts/validate_claude_skills.py
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000038
  - CultureMech:000415
  evidence_ids:
  - extra-00
  summary: Actual check outcome; failures retained without waiver.
- check_id: extra-01
  name: git diff --check
  command: git diff --check
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000038
  - CultureMech:000415
  evidence_ids:
  - extra-01
  summary: Actual check outcome; failures retained without waiver.
- check_id: extra-02
  name: /tmp/culturemech-parallel-env-20261012/bin/python /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech/reports/paper_citation_curation/20261014-2asw-study-citations/curate.py
    --apply
  command: /tmp/culturemech-parallel-env-20261012/bin/python /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech/reports/paper_citation_curation/20261014-2asw-study-citations/curate.py
    --apply
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000038
  - CultureMech:000415
  evidence_ids:
  - extra-02
  summary: Actual check outcome; failures retained without waiver.
- check_id: fast-00
  name: just test-fast
  command: just test-fast
  required: true
  status: passed
  exit_code: 0
  target_ids:
  - CultureMech:000038
  - CultureMech:000415
  evidence_ids:
  - fast-00
  summary: Actual check outcome; failures retained without waiver.
evidence:
- evidence_id: baseline-00
  kind: validation
  reference: reports/paper_citation_curation/20261014-2asw-study-citations/baseline-00.log
  locator: reports/paper_citation_curation/20261014-2asw-study-citations/baseline-00.log;
    Complete terminal output
  accessed_at: '2026-10-14T03:16:05Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 74af7630dce4ef7dd0c2840a1e2157dd4bbdf7ac949b2106357a70147c972025
- evidence_id: baseline-01
  kind: validation
  reference: reports/paper_citation_curation/20261014-2asw-study-citations/baseline-01.log
  locator: reports/paper_citation_curation/20261014-2asw-study-citations/baseline-01.log;
    Complete terminal output
  accessed_at: '2026-10-14T03:16:05Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: baseline-02
  kind: validation
  reference: reports/paper_citation_curation/20261014-2asw-study-citations/baseline-02.log
  locator: reports/paper_citation_curation/20261014-2asw-study-citations/baseline-02.log;
    Complete terminal output
  accessed_at: '2026-10-14T03:16:05Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 8e85fad3683d76bd6c3fb545f47c457c6d20f0a3795b6abae6b05d87f12134d1
- evidence_id: baseline-03
  kind: validation
  reference: reports/paper_citation_curation/20261014-2asw-study-citations/baseline-03.log
  locator: reports/paper_citation_curation/20261014-2asw-study-citations/baseline-03.log;
    Complete terminal output
  accessed_at: '2026-10-14T03:16:05Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-00
  kind: validation
  reference: reports/paper_citation_curation/20261014-2asw-study-citations/post-00.log
  locator: reports/paper_citation_curation/20261014-2asw-study-citations/post-00.log;
    Complete terminal output
  accessed_at: '2026-10-14T03:16:05Z'
  summary: Exit code 1; not scientific approval.
  support: context_only
  snapshot_sha256: d7d5e25ef6c19fc5c90fad80df1c0a904d8075d0a2748bcd3e28d6cc8629e6bd
- evidence_id: post-01
  kind: validation
  reference: reports/paper_citation_curation/20261014-2asw-study-citations/post-01.log
  locator: reports/paper_citation_curation/20261014-2asw-study-citations/post-01.log;
    Complete terminal output
  accessed_at: '2026-10-14T03:16:05Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-02
  kind: validation
  reference: reports/paper_citation_curation/20261014-2asw-study-citations/post-02.log
  locator: reports/paper_citation_curation/20261014-2asw-study-citations/post-02.log;
    Complete terminal output
  accessed_at: '2026-10-14T03:16:05Z'
  summary: Exit code 1; not scientific approval.
  support: context_only
  snapshot_sha256: 086cb1b7a910e231f6ea2a539e3e0544ef6bafffd250a699f04320cca98e215c
- evidence_id: post-03
  kind: validation
  reference: reports/paper_citation_curation/20261014-2asw-study-citations/post-03.log
  locator: reports/paper_citation_curation/20261014-2asw-study-citations/post-03.log;
    Complete terminal output
  accessed_at: '2026-10-14T03:16:05Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: merge-00
  kind: validation
  reference: reports/paper_citation_curation/20261014-2asw-study-citations/merge-00.log
  locator: reports/paper_citation_curation/20261014-2asw-study-citations/merge-00.log;
    Complete terminal output
  accessed_at: '2026-10-14T03:16:05Z'
  summary: Exit code 1; not scientific approval.
  support: context_only
  snapshot_sha256: 09a2922082db841587410042dc33d7d3f72b2601f1d6b6f2b33322471ee47f2c
- evidence_id: merge-01
  kind: validation
  reference: reports/paper_citation_curation/20261014-2asw-study-citations/merge-01.log
  locator: reports/paper_citation_curation/20261014-2asw-study-citations/merge-01.log;
    Complete terminal output
  accessed_at: '2026-10-14T03:16:05Z'
  summary: Exit code 1; not scientific approval.
  support: context_only
  snapshot_sha256: a8208a11981c6c9bc3b4bd12944261bd9a4333f2aa667bad64a0309cbfb06601
- evidence_id: extra-00
  kind: validation
  reference: reports/paper_citation_curation/20261014-2asw-study-citations/extra-00.log
  locator: reports/paper_citation_curation/20261014-2asw-study-citations/extra-00.log;
    Complete terminal output
  accessed_at: '2026-10-14T03:16:05Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 441bdd6ab36f5b87c9edccf771321e1c5f6c11f43bec7799e6e98cd4d756c24c
- evidence_id: extra-01
  kind: validation
  reference: reports/paper_citation_curation/20261014-2asw-study-citations/extra-01.log
  locator: reports/paper_citation_curation/20261014-2asw-study-citations/extra-01.log;
    Complete terminal output
  accessed_at: '2026-10-14T03:16:05Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: extra-02
  kind: validation
  reference: reports/paper_citation_curation/20261014-2asw-study-citations/extra-02.log
  locator: reports/paper_citation_curation/20261014-2asw-study-citations/extra-02.log;
    Complete terminal output
  accessed_at: '2026-10-14T03:16:05Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: 20c33226792ef5793b8a4ab8d318419cf95daed03f495488ce181087f65ea543
- evidence_id: fast-00
  kind: validation
  reference: reports/paper_citation_curation/20261014-2asw-study-citations/fast-test.log
  locator: reports/paper_citation_curation/20261014-2asw-study-citations/fast-test.log;
    Complete terminal output
  accessed_at: '2026-10-14T03:16:05Z'
  summary: Exit code 0; not scientific approval.
  support: context_only
  snapshot_sha256: c815b27c2e216701e84e5f51c020447a6e5579c3bddfff8fa2603b93d8eb712e
- evidence_id: paper-2023
  kind: primary_source
  reference: doi:10.1128/spectrum.00069-23
  locator: references_cache/papers/primary_xml/2asw-spectrum-2023-europepmc-20261014.xml;
    full JATS body; external supplement not retrieved
  accessed_at: '2026-10-14T03:16:05Z'
  summary: Original article identity and bounded methods/identity passages inspected;
    external supplement not inferred.
  support: supports
  snapshot_sha256: 35398747e184a6699fa12f46288848dcc97932d087fa49e4056ea90f2debf22d
- evidence_id: paper-2017
  kind: primary_source
  reference: doi:10.1128/genomeA.01105-17
  locator: references_cache/papers/primary_xml/ccap-19-18-PMC5658486-20261014.xml;
    full JATS article
  accessed_at: '2026-10-14T03:16:05Z'
  summary: Original article identity and bounded methods/identity passages inspected;
    external supplement not inferred.
  support: supports
  snapshot_sha256: 3c50cdccf710f636997b8456be886fb9344ab3720dab14884190d148b6f1eb59
- evidence_id: paper-2015
  kind: primary_source
  reference: doi:10.3389/fenrg.2015.00020
  locator: references_cache/papers/primary_html/2asw-frontiers-2015-20261014.html;
    publisher HTML full article including Table 1
  accessed_at: '2026-10-14T03:16:05Z'
  summary: Original article identity and bounded methods/identity passages inspected;
    external supplement not inferred.
  support: supports
  snapshot_sha256: 194d2a1a9fb3f25d569d26651d548a877d0e2cc1ec372e68466de4d41de93c52
- evidence_id: taxonomy
  kind: authority
  reference: NCBI Taxonomy
  locator: 'references_cache/papers/taxonomy/2asw-20261014.xml; Eleven used nodes:
    scientific names, actual ranks and synonyms'
  accessed_at: '2026-10-14T03:16:05Z'
  summary: Species name-level matches and parent-only genus fallbacks explicitly distinguished.
  support: supports
  snapshot_sha256: ef67ee5146f432fcdb8810a24c38a6a6cc5e87b98cbdc018314bca1837a20c06
- evidence_id: ccap-recipe
  kind: primary_source
  reference: https://www.ccap.ac.uk/wp-content/uploads/MR_2ASW.pdf
  locator: references_cache/papers/primary_pdf/2asw-ccap-2asw-20261014.pdf; Revision
    002, 29 May 2026; stock and seawater basis
  accessed_at: '2026-10-14T03:16:05Z'
  summary: Flattened imports are not a complete basis for a total-NaCl comparison
    or confirmation of historical study formulations.
  support: context_only
  snapshot_sha256: d5d658702a3640ed17c4d9d494f198f7122be90cbc81e64ccdc8afad1c4401cc
- evidence_id: exporter
  kind: record_content
  reference: Current KGX implementation
  locator: src/culturemech/export/kgx_export.py; organism_grows_in_medium_edge
  accessed_at: '2026-10-14T03:16:05Z'
  summary: Positive edges use the parent ID and do not honor scoped_to_variant; no
    new native growth assertions added.
  support: context_only
  snapshot_sha256: eacbc2e7b363488cc1ed96e91737f54244dc1a2425dfa05c77ba89d0a5cd10e0
- evidence_id: claims
  kind: record_content
  reference: Guarded curation receipt
  locator: reports/paper_citation_curation/20261014-2asw-study-citations/claim-plan-v2.json;
    claim-plan-v2.json
  accessed_at: '2026-10-14T03:16:05Z'
  summary: Exact applied claims, source scope, preservation checks and unfinished
    discovery.
  support: context_only
  snapshot_sha256: d731e4fb56acedb4935c6ac9bc5cb09bcd5379af4d18ba418e6ca767ee6ad8c4
- evidence_id: readback
  kind: record_content
  reference: Guarded curation receipt
  locator: reports/paper_citation_curation/20261014-2asw-study-citations/final-readback.json;
    final-readback.json
  accessed_at: '2026-10-14T03:16:05Z'
  summary: Exact applied claims, source scope, preservation checks and unfinished
    discovery.
  support: context_only
  snapshot_sha256: 9c64d76b02845aed83775c8fc0ccbbf35aad4b3b64b0e7494014ab9bed1d88e6
- evidence_id: excerpts
  kind: record_content
  reference: Guarded curation receipt
  locator: reports/paper_citation_curation/20261014-2asw-study-citations/evidence-readback.json;
    evidence-readback.json
  accessed_at: '2026-10-14T03:16:05Z'
  summary: Exact applied claims, source scope, preservation checks and unfinished
    discovery.
  support: context_only
  snapshot_sha256: e1b75425e456ba10ec19a4d511d3533c8248785086a7de8748dbadc00f5ec757
- evidence_id: pending
  kind: record_content
  reference: Guarded curation receipt
  locator: reports/paper_citation_curation/20261014-2asw-study-citations/pending-frontier.json;
    pending-frontier.json
  accessed_at: '2026-10-14T03:16:05Z'
  summary: Exact applied claims, source scope, preservation checks and unfinished
    discovery.
  support: context_only
  snapshot_sha256: 9026ba8e43af20cd768adbf6e9bad80d37f68c048bc3caa38931b8f0055293cf
assessments:
- assessment_id: identity-000038
  area: evidence
  topic: Publication identity and source-owner relevance
  outcome: supported
  target_ids:
  - CultureMech:000038
  evidence_ids:
  - paper-2023
  - paper-2015
  - paper-2017
  - claims
  summary: 3 paper citations with verified title, authors, year, identifiers, primary
    archives and Markdown. Genome paper is identity-only and attached only to the
    owner already citing its BioProject.
- assessment_id: formulation-000038
  area: evidence
  topic: Study variants and unresolved full formulas
  outcome: unknown
  target_ids:
  - CultureMech:000038
  evidence_ids:
  - paper-2023
  - paper-2015
  - ccap-recipe
  - claims
  summary: Two bounded inline variants capture explicit study statements; parent quantities
    and source-owner differences remain unchanged. Table S2 and the mismatched base
    citation prevent complete formulation certification.
- assessment_id: taxonomy-000038
  area: evidence
  topic: Scientific names, actual ranks and experimental roles
  outcome: supported
  target_ids:
  - CultureMech:000038
  evidence_ids:
  - paper-2023
  - paper-2015
  - paper-2017
  - taxonomy
  - exporter
  - excerpts
  summary: Eighteen Dunaliella maintenance-strain rows retained separately; UTEX LB
    200, genus-only strains and FACHB-847 have qualified parent matches. Other-media
    and background observations do not imply parent growth. No native growth association
    was added.
- assessment_id: preservation-000038
  area: evidence
  topic: Existing claims and recipe presentation
  outcome: supported
  target_ids:
  - CultureMech:000038
  evidence_ids:
  - readback
  - extra-02
  summary: 13 ingredient entries and every pre-existing field preserved. Reversing
    the additions recovers original bytes; exactly one history event per owner; no-op
    replay passes.
- assessment_id: variant-amount-000038-0
  area: evidence
  topic: Evidence-backed inline variant concentration
  outcome: supported
  target_ids:
  - CultureMech:000038
  evidence_ids:
  - paper-2023
  - claims
  - excerpts
  - readback
  summary: status=add; field=variants[name=2asw_1_5_m_nacl].modifications[0]; old=absent
    study-variant entry; new=1.5 M NaCl, explicitly stated medium concentration; parent
    amount unchanged.
  details: 'Reference: doi:10.1128/spectrum.00069-23. Exact snippet: D. salina was
    cultivated in 2ASW (artificial seawater) medium containing 1.5 M NaCl Locator
    and claim linkage: Supports only variants[name=2asw_1_5_m_nacl].modifications[0]:
    explicitly reported 1.5 M NaCl for Dunaliella salina CCAP 19/18, in Materials
    and Methods / Algal strains and cultivation conditions. Not a complete recipe
    certification, stock value, conversion, or canonical parent amount. canonical
    scientific name=Dunaliella salina; NCBITaxon:3046; actual rank=species; taxonomy_match=exact_name_at_species_rank;
    lookup_url=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=3046; cultivation
    applies to this study formulation only. Table S2 is uninspected. Taxonomy checked
    against NCBI EFetch archived 2026-10-14 at references_cache/papers/taxonomy/2asw-20261014.xml.
    Species mappings do not verify exact strain identity.  Calculation: none. Complete
    stock/final-volume formulation remains unresolved. The DOI/excerpt evidence is
    attached to this variant in the owner YAML, not merely this report.'
  dimensions:
  - name: concentration_decision
    value: add
    definition: Directly stated study-variant amount, not correction of the canonical
      parent
    evidence_ids:
    - paper-2023
- assessment_id: variant-amount-000038-1
  area: evidence
  topic: Evidence-backed inline variant concentration
  outcome: supported
  target_ids:
  - CultureMech:000038
  evidence_ids:
  - paper-2015
  - claims
  - excerpts
  - readback
  summary: status=add; field=variants[name=2asw_sea_salt_substitution_33_6_g_l].modifications[0];
    old=absent study-variant entry; new=33.6 g/L sea-salt mixture replacing NaCl,
    explicitly stated maintenance-medium concentration; parent amount unchanged.
  details: 'Reference: doi:10.3389/fenrg.2015.00020. Exact snippet: 33.6 g/L of sea
    salts were used in place of the NaCl. Locator and claim linkage: Supports only
    variants[name=2asw_sea_salt_substitution_33_6_g_l].modifications[0]: directly
    reported sea-salt replacement amount in Materials and Methods / Strains and media.
    It is the maintenance-medium mixture concentration, not a stock or pure NaCl value.
    No arithmetic was performed. The paragraph assigns this modified 2ASW to the 18
    Dunaliella strain rows in Table 1, whose scientific names and taxonomy qualifications
    are preserved in this paper''s citation notes. Centrate results are not parent
    or maintenance-medium growth metrics. Calculation: none. Complete stock/final-volume
    formulation remains unresolved. The DOI/excerpt evidence is attached to this variant
    in the owner YAML, not merely this report.'
  dimensions:
  - name: concentration_decision
    value: add
    definition: Directly stated study-variant amount, not correction of the canonical
      parent
    evidence_ids:
    - paper-2015
- assessment_id: identity-000415
  area: evidence
  topic: Publication identity and source-owner relevance
  outcome: supported
  target_ids:
  - CultureMech:000415
  evidence_ids:
  - paper-2023
  - paper-2015
  - claims
  summary: 2 paper citations with verified title, authors, year, identifiers, primary
    archives and Markdown. Genome paper is identity-only and attached only to the
    owner already citing its BioProject.
- assessment_id: formulation-000415
  area: evidence
  topic: Study variants and unresolved full formulas
  outcome: unknown
  target_ids:
  - CultureMech:000415
  evidence_ids:
  - paper-2023
  - paper-2015
  - ccap-recipe
  - claims
  summary: Two bounded inline variants capture explicit study statements; parent quantities
    and source-owner differences remain unchanged. Table S2 and the mismatched base
    citation prevent complete formulation certification.
- assessment_id: taxonomy-000415
  area: evidence
  topic: Scientific names, actual ranks and experimental roles
  outcome: supported
  target_ids:
  - CultureMech:000415
  evidence_ids:
  - paper-2023
  - paper-2015
  - taxonomy
  - exporter
  - excerpts
  summary: Eighteen Dunaliella maintenance-strain rows retained separately; UTEX LB
    200, genus-only strains and FACHB-847 have qualified parent matches. Other-media
    and background observations do not imply parent growth. No native growth association
    was added.
- assessment_id: preservation-000415
  area: evidence
  topic: Existing claims and recipe presentation
  outcome: supported
  target_ids:
  - CultureMech:000415
  evidence_ids:
  - readback
  - extra-02
  summary: 14 ingredient entries and every pre-existing field preserved. Reversing
    the additions recovers original bytes; exactly one history event per owner; no-op
    replay passes.
- assessment_id: variant-amount-000415-0
  area: evidence
  topic: Evidence-backed inline variant concentration
  outcome: supported
  target_ids:
  - CultureMech:000415
  evidence_ids:
  - paper-2023
  - claims
  - excerpts
  - readback
  summary: status=add; field=variants[name=2asw_1_5_m_nacl].modifications[0]; old=absent
    study-variant entry; new=1.5 M NaCl, explicitly stated medium concentration; parent
    amount unchanged.
  details: 'Reference: doi:10.1128/spectrum.00069-23. Exact snippet: D. salina was
    cultivated in 2ASW (artificial seawater) medium containing 1.5 M NaCl Locator
    and claim linkage: Supports only variants[name=2asw_1_5_m_nacl].modifications[0]:
    explicitly reported 1.5 M NaCl for Dunaliella salina CCAP 19/18, in Materials
    and Methods / Algal strains and cultivation conditions. Not a complete recipe
    certification, stock value, conversion, or canonical parent amount. canonical
    scientific name=Dunaliella salina; NCBITaxon:3046; actual rank=species; taxonomy_match=exact_name_at_species_rank;
    lookup_url=https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=3046; cultivation
    applies to this study formulation only. Table S2 is uninspected. Taxonomy checked
    against NCBI EFetch archived 2026-10-14 at references_cache/papers/taxonomy/2asw-20261014.xml.
    Species mappings do not verify exact strain identity.  Calculation: none. Complete
    stock/final-volume formulation remains unresolved. The DOI/excerpt evidence is
    attached to this variant in the owner YAML, not merely this report.'
  dimensions:
  - name: concentration_decision
    value: add
    definition: Directly stated study-variant amount, not correction of the canonical
      parent
    evidence_ids:
    - paper-2023
- assessment_id: variant-amount-000415-1
  area: evidence
  topic: Evidence-backed inline variant concentration
  outcome: supported
  target_ids:
  - CultureMech:000415
  evidence_ids:
  - paper-2015
  - claims
  - excerpts
  - readback
  summary: status=add; field=variants[name=2asw_sea_salt_substitution_33_6_g_l].modifications[0];
    old=absent study-variant entry; new=33.6 g/L sea-salt mixture replacing NaCl,
    explicitly stated maintenance-medium concentration; parent amount unchanged.
  details: 'Reference: doi:10.3389/fenrg.2015.00020. Exact snippet: 33.6 g/L of sea
    salts were used in place of the NaCl. Locator and claim linkage: Supports only
    variants[name=2asw_sea_salt_substitution_33_6_g_l].modifications[0]: directly
    reported sea-salt replacement amount in Materials and Methods / Strains and media.
    It is the maintenance-medium mixture concentration, not a stock or pure NaCl value.
    No arithmetic was performed. The paragraph assigns this modified 2ASW to the 18
    Dunaliella strain rows in Table 1, whose scientific names and taxonomy qualifications
    are preserved in this paper''s citation notes. Centrate results are not parent
    or maintenance-medium growth metrics. Calculation: none. Complete stock/final-volume
    formulation remains unresolved. The DOI/excerpt evidence is attached to this variant
    in the owner YAML, not merely this report.'
  dimensions:
  - name: concentration_decision
    value: add
    definition: Directly stated study-variant amount, not correction of the canonical
      parent
    evidence_ids:
    - paper-2015
findings:
- finding_id: merge-gates
  issue_key: 2asw-study-citations-merge-gates
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Repository merge gates failed
  description: Actual failures retained, without assuming that equal counts prove
    unchanged rows or attributing all failures to this batch. No generated publication.
  target_ids:
  - CultureMech:000038
  - CultureMech:000415
  evidence_ids:
  - merge-00
  - merge-01
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/2asw.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/2asw.yaml
    role: authoritative normalized recipe
- finding_id: reference-checks
  issue_key: 2asw-study-citations-reference-checks
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Newly cited papers expose native reference-validation limitations
  description: Baseline passed. Post-edit checks report title differences containing
    publisher italic markup and full-text methods excerpts unavailable through the
    automatic DOI fetch. Raw JATS/HTML and Markdown support the stored plain titles
    and exact excerpts. These newly exposed failures are recorded, not mislabeled
    baseline failures or silently waived.
  target_ids:
  - CultureMech:000038
  - CultureMech:000415
  evidence_ids:
  - post-00
  - post-02
  - paper-2023
  - paper-2015
  - paper-2017
  - excerpts
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/2asw.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/2asw.yaml
    role: authoritative normalized recipe
- finding_id: formulation-and-scope
  issue_key: 2asw-study-citations-formulation-and-scope
  category: evidence
  severity: informational
  status: open
  certainty: confirmed
  title: Complete study formulas and machine-readable growth scope remain unresolved
  description: Only the documented study amounts are resolved. Missing supplement,
    mismatched base citation, disputed strain identity and the current organism/export
    scope model prevent complete formulations or parent growth assertions. Existing
    pre-curation claims were preserved, not scientifically recertified.
  target_ids:
  - CultureMech:000038
  - CultureMech:000415
  evidence_ids:
  - claims
  - taxonomy
  - ccap-recipe
  - exporter
  - pending
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/2asw.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/2asw.yaml
    role: authoritative normalized recipe
actions:
- action_id: resolve-merge-gates
  description: Repository merge gates failed
  finding_ids:
  - merge-gates
  target_ids:
  - CultureMech:000038
  - CultureMech:000415
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/2asw.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/2asw.yaml
    role: authoritative normalized recipe
  acceptance_checks:
  - Diagnose maintained merge inputs/rules and rerun both gates before publication.
- action_id: resolve-reference-checks
  description: Newly cited papers expose native reference-validation limitations
  finding_ids:
  - reference-checks
  target_ids:
  - CultureMech:000038
  - CultureMech:000415
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/2asw.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/2asw.yaml
    role: authoritative normalized recipe
  acceptance_checks:
  - Improve the maintained reference fetch/title normalization and full-text coverage;
    do not alter correct source claims just to pass an abstract-only check.
- action_id: resolve-formulation-and-scope
  description: Complete study formulas and machine-readable growth scope remain unresolved
  finding_ids:
  - formulation-and-scope
  target_ids:
  - CultureMech:000038
  - CultureMech:000415
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/algae/2asw.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/2asw.yaml
    role: authoritative normalized recipe
  acceptance_checks:
  - Inspect full study recipes and resolve taxon/strain/formulation scope before curating
    or exporting positive native growth associations.
limitations:
- Focused self-review, not independent adversarial or complete scientific review.
- Only 2ASW-relevant organism passages inventoried; no whole-paper inventory claim.
- Table S2 not retrieved; 2015 base-reference mismatch unresolved; other ingredients
  and total seawater salt contribution unverified.
- Species name mappings do not establish an exact strain match; parent-only matches
  stay in notes.
- No native positive growth assertions, parent amount changes, record merge, export,
  or GitHub publication.
- Reference and global merge gate failures remain open. Corpus-wide citation discovery
  remains active.
```
