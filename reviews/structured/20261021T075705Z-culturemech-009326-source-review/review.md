# Source and formulation review: 2xytg (CultureMech:009326)

- Review: 20261021T075705Z-culturemech-009326-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-21T07:45:35Z
- Finished UTC: 2026-10-21T07:57:05Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

TOGO M2778 and the recovered Little et al. 2018 paper identify this exact 2xYTG formulation. All four solute concentrations are supported: tryptone 16, yeast extract 10, NaCl 5 and glucose 5 g/L. Both local layers incorrectly encode the TOGO 1 L distilled-water input as 1 g/L and omit the source-scoped 37 C anaerobic culture context. The paper citation and claim-level formulation evidence are also absent. Generated and normalized recipe content otherwise agrees; there is no missing later owner curation. Four documented diagnostics pass.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Task review 89; batch 009 item 9 of 10, selected in Python lexicographic order of currently uncovered merged paths. The preceding eight task batches contain 80 ledger-owned validated record reviews; their complete validated lists also retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c contains 40 validated baseline bundles covering 2 current merged paths. Unioning all prior lists with this baseline covers 82 of 6320 current merged paths, including 2 paths beyond task-owned reviews. This target path is absent from that union. Task ordinals count task reviews, not current global path ranks or all upstream coverage. Only the named target is reviewed; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 24a1d277eb7f0437af53af0d178a30f9bfa6374c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009326 | data/merge_yaml/merged/2xYTG.yaml | generated | 2xytg |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:009326 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:009326 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-009/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch009/089/strict.tsv |
| validate-terms | passed | True | CultureMech:009326 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:009326 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:009326 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |
| Publisher primary-paper access | unavailable | False | CultureMech:009326 | Publisher HTML and direct PDF each returned 403; the complete published article was successfully retrieved from the German National Library, independently identified and inspected. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:009326.

The four documented recipes completed; interpret the scope of each separately.

### All asserted primary and current secondary ingredient identifiers

grounding: supported. Targets: CultureMech:009326.

3 primary CHEBI identities resolve with matching labels; 3 of 3 current secondary keys have live pinned-index rows. Unresolved keys: [].

5 direct ingredient instances; CHEBI-primary instance linkage 3/5 (60.00%), verified secondary coverage 3/5 (60.00%). Percentages use a 0–100 linkage scale, not a scientific correctness score. Complex mixtures without asserted IDs remain ungrounded rather than receiving invented pure-molecule identities.

### TOGO M2778 and Little 2018 source identity

identity: supported. Targets: CultureMech:009326.

The exact TOGO accession/title, all ingredient rows, explicit source concentration paragraph and full paper agree. The maintained owner is uniquely resolved within the data-tree ID lookup and singleton merge event. Little DOI 10.1002/biot.201700711 / PMID 29660854 is the recipe-bearing article; the CBM/CGM inline reference markers are not substituted for it.

### All five declared quantities

quantity: concern. Targets: CultureMech:009326.

Four solute concentrations are explicitly supported without arithmetic: yeast extract 10, NaCl 5, glucose 5 and tryptone 16 g/L. Water is the sole quantity error: literal source input 1 L became 1 g/L. There are no nested stocks or supplied solution doses to audit. No water density or total final-volume conversion is inferred.

[{"field": "ingredients[0].concentration", "material": "Distilled water", "record": {"value": "1", "unit": "G_PER_L"}, "source_amount": 1, "source_unit": "L", "source_locator": "components[0].items[0]", "source_evidence_ids": ["togo"], "decision": "correct: source solvent input 1 L was encoded as 1 G_PER_L; dimensional error, no mass/density conversion justified"}, {"field": "ingredients[1].concentration", "material": "Yeast extract", "record": {"value": "10", "unit": "G_PER_L"}, "source_amount": 10, "source_unit": "g", "source_locator": "components[0].items[1]", "source_evidence_ids": ["togo", "paper"], "decision": "verified: paper and source comment explicitly declare g/L; no batch-volume assumption needed"}, {"field": "ingredients[2].concentration", "material": "NaCl", "record": {"value": "5", "unit": "G_PER_L"}, "source_amount": 5, "source_unit": "g", "source_locator": "components[0].items[2]", "source_evidence_ids": ["togo", "paper"], "decision": "verified: paper and source comment explicitly declare g/L; no batch-volume assumption needed"}, {"field": "ingredients[3].concentration", "material": "Glucose", "record": {"value": "5", "unit": "G_PER_L"}, "source_amount": 5, "source_unit": "g", "source_locator": "components[0].items[3]", "source_evidence_ids": ["togo", "paper"], "decision": "verified: paper and source comment explicitly declare g/L; no batch-volume assumption needed"}, {"field": "ingredients[4].concentration", "material": "Tryptone", "record": {"value": "16", "unit": "G_PER_L"}, "source_amount": 16, "source_unit": "g", "source_locator": "components[0].items[4]", "source_evidence_ids": ["togo", "paper"], "decision": "verified: paper and source comment explicitly declare g/L; no batch-volume assumption needed"}]

### Pure compounds versus undefined extracts

grounding: supported. Targets: CultureMech:009326.

Water, sodium chloride and generic glucose carry canonical non-obsolete CHEBI labels and matching live packaged MIM keys. Both primary and current secondary linkage are 3/5 ingredient instances (60% on a 0–100 linkage scale), not accuracy scores. The source does not establish glucose anomer/hydrate or defined molecular compositions for yeast extract and tryptone. Imported role/property notes agree with TOGO without becoming experimental mechanism evidence.

### Source-scoped culture conditions and experimental boundaries

completeness: concern. Targets: CultureMech:009326.

The source explicitly reports clostridial culture at 37 C in an anaerobic cabinet, including 2xYTG among alternatives, but neither local layer preserves this context. The paper identifies a specific NCIMB 14988 transformation/culture use; it does not establish unrestricted growth for every mentioned organism. Context should remain qualified to the cited study, not an optimal range or universal strain claim.

### Missing source detail versus unrelated procedures

scope: supported. Targets: CultureMech:009326.

No 2xYTG sterilization, pH adjustment or specific make-to-volume instruction was established by the inspected formula. No default is invented. Antibiotics when required, mutant supplementation, counter-selection, CBM isolation, LB cultures, electroporation buffer, DNA extraction and solvent-analysis reagents remain separate from the unsupplemented five-row recipe. No obligatory recipe-variant or stock omission is inferred from their presence elsewhere in the paper.

### Recoverable primary citation and claim-level support

evidence: concern. Targets: CultureMech:009326.

Both local files cite only TOGO M2778 in notes/media_term. Neither retains the identified primary paper or ingredient-level source support, despite an exact recoverable formula and the limited culture context. The generated reference validator performed zero checks; its success does not establish the article evidence. The recovered full paper resolves publisher-access failure without concealing the original 403 attempts.

### Complete owner correspondence and append-only history

provenance: supported. Targets: CultureMech:009326.

Generated and maintained content agree in every substantive top-level field; only merge metadata and the added singleton merge event differ. All owner history events are preserved with timezone-bearing timestamps. This record has no stale omitted owner citations or variants. Corrections belong to the normalized owner followed by authorized regeneration.

### Classification and asserted application

scope: supported. Targets: CultureMech:009326.

Bacterial category is consistent with the documented clostridial use; broth and absence of agar support LIQUID, and yeast extract/tryptone support COMPLEX and UNDEFINED. Generic microbial-cultivation application does not claim experimentally established growth for all microbes. No native organism, taxon, assembly or variant assertions are present.

## Findings

### f1: One litre of source water is encoded as one gram per litre

major / open / confirmed; issue key: CM009326-water-unit-corruption.

Both local files retain the numerical 1 but replace TOGO volume unit L with G_PER_L. This changes a solvent input into a mass concentration. The paper independently verifies the four solutes; it does not support the water mass assertion.

### f2: Documented anaerobic culture context is absent

major / open / confirmed; issue key: CM009326-culture-context-omitted.

TOGO reproduces the primary report of clostridial cultivation at 37 C in an anaerobic cabinet using CBM, 2xYTG or CGM. Neither local file preserves this context. Omitting oxygen/temperature context matters to the documented use, but the source does not authorize universal growth assertions or an optimal-temperature claim.

### f3: Exact primary formulation citation and support are not retained

minor / open / confirmed; issue key: CM009326-primary-evidence-unlinked.

The record contains a TOGO pointer but no reference or claim-level evidence for the four independently verified solute concentrations or the bounded culture context. The recipe-bearing paper is identifiable as Little et al. 2018, DOI 10.1002/biot.201700711 and PMID 29660854; inline CBM/CGM identifiers must not be substituted for it.

## Recommended Actions And Acceptance Checks

### a1

Restore the literal source 1 L water input in suitable solvent/batch or preparation context, or another schema-supported faithful representation. Do not invent density, a 1 g/L concentration or an unsupported final-volume instruction. Preserve all four verified solute concentrations.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a2

Preserve the paper-scoped 37 C anaerobic context with source evidence and its media/strain qualifications, using supported fields or qualified notes. Keep LB-grown E. coli, conditional supplements, extraction buffers and separate CBM/CGM protocols out of the unchanged parent recipe.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

### a3

Attach the verified primary citation and narrow formula/culture evidence in the maintained owner with exact locators and archived-source provenance. Preserve unsuccessful publisher access and successful institutional recovery; do not assert unverified strain taxonomy, genomic identity or universal culture conditions.

- Verify the exact source accession, ingredient form, original unit and batch/preparation context.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on separately authorized maintained-input corrections.
- Regenerate derived records only after owner verification; run just verify-merges and just audit-merge-freshness and confirm corrected fields/evidence survive.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/2xYTG.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/2xytg.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/2xYTG.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/2xYTG.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch009/089/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-009/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch009/089/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/2xYTG.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/2xYTG.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2778; $.meta; $.components[0].items[0:5]; $.comments[0].comment | supports | Exact M2778 API identifies 2xYTG and supplies five rows: distilled water 1 L, yeast extract 10 g, NaCl 5 g, glucose 5 g and tryptone 16 g. The comment explicitly states all four solute concentrations in g/L and clostridial culture at 37 C in an anaerobic cabinet. The adjacent PMID annotations belong to alternative CBM/CGM references in that comment, not the recovered 2xYTG paper identity. Ingredient role/property prose in both local files is retained from these rows. Source capture key=togoM2778api; original access timestamp and raw SHA256 retained. |
| paper | https://d-nb.info/1265485364/34; PDF pages 1–9 in full; page 1 title/authors/DOI; page 2 section 2.1, Media, Strains, and Growth Conditions | supports | Read complete nine-page published article. Little GT, Willson BJ, Heap JT, Winzer K and Minton NP, The Butanol Producing Microbe Clostridium beijerinckii NCIMB 14988 Manipulated Using Forward and Reverse Genetic Tools, Biotechnology Journal 2018, 13, 1700711; DOI 10.1002/biot.201700711. Section 2.1 directly defines the same four solute concentrations and the 37 C anaerobic culture context. Its formula was also checked visually on page 2. No sterilization or pH instruction for this formula is supplied. Source capture key=little2018dnbPDF; original access timestamp and raw SHA256 retained. |
| paper-scope | https://d-nb.info/1265485364/34; Sections 2.1, 2.2, 2.3, 2.5, 3.1 and 3.3; contextual figure/method references; full-paper scope | supports | Section 2.5 explicitly uses 2xYTG broth for growth and post-transformation recovery in the C. beijerinckii workflow; section 3.3 identifies the competent cells as NCIMB 14988. Section 3.1 states isolate 59B was deposited as NCIMB 14988. These observations remain specific to that study/workflow. The initial environmental isolation is on CBM, E. coli TOP10/DH10B are grown on LB, and conditional antibiotics, uracil and counter-selection conditions are separate. DNA extraction and analytical solvent extraction are not additions to or preparation of this 2xYTG recipe. Yeast extract is an undefined medium ingredient, not evidence of a cell-free extract-production medium. Source capture key=little2018dnbPDF; original access timestamp and raw SHA256 retained. |
| paper-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1002%2Fbiot.201700711&amp;format=json&amp;resultType=core; resultList.result[0]: id, source, doi, title, authorString, pubYear and journalInfo | supports | Europe PMC DOI lookup agrees with the recovered title, five authors and year and resolves PMID 29660854 (source MED). No PMCID is returned in this response; no exhaustive absence claim is made. Source capture key=little2018metadata; original access timestamp and raw SHA256 retained. |
| togo-page | https://togomedium.org/medium/M2778; Entire returned HTML shell | context_only | HTTP 200 returned a 750-byte JavaScript shell, not the scientific recipe text. The inspected structured API and complete paper supply the substantive evidence. Source capture key=togoM2778page; original access timestamp and raw SHA256 retained. |
| little2018publisher | https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/10.1002/biot.201700711; Exact publisher HTML or direct PDF request | unknown | HTTP Error 403: Forbidden. Failed attempt retained; substantive article access was recovered separately through the German National Library. This is not a new request during drafting. |
| little2018publisherPDF | https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/biot.201700711; Exact publisher HTML or direct PDF request | unknown | HTTP Error 403: Forbidden. Failed attempt retained; substantive article access was recovered separately through the German National Library. This is not a new request during drafting. |
| chebi15377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:15377 resolves to water and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:17234 resolves to glucose and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; Exact OLS term identifier, label, available definition/form and obsolete flag | supports | CHEBI:26710 resolves to sodium chloride and is not obsolete. This verifies the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond the record is inferred. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; All live preferred-term rows for asserted secondary CHEBI keys; metadata captured | supports | {"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term", "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id": "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710": [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710", "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term", "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234", "mapping_status": "MAPPED", "ambiguity": "unique"}]} |
| comparison | Full inspected target, owner, TOGO API and published-paper formula; All five amounts; all top-level target/owner fields and history timestamps; paper page 2 visual confirmation | supports | {"amounts": [{"field": "ingredients[0].concentration", "material": "Distilled water", "record": {"value": "1", "unit": "G_PER_L"}, "source_amount": 1, "source_unit": "L", "source_locator": "components[0].items[0]", "source_evidence_ids": ["togo"], "decision": "correct: source solvent input 1 L was encoded as 1 G_PER_L; dimensional error, no mass/density conversion justified"}, {"field": "ingredients[1].concentration", "material": "Yeast extract", "record": {"value": "10", "unit": "G_PER_L"}, "source_amount": 10, "source_unit": "g", "source_locator": "components[0].items[1]", "source_evidence_ids": ["togo", "paper"], "decision": "verified: paper and source comment explicitly declare g/L; no batch-volume assumption needed"}, {"field": "ingredients[2].concentration", "material": "NaCl", "record": {"value": "5", "unit": "G_PER_L"}, "source_amount": 5, "source_unit": "g", "source_locator": "components[0].items[2]", "source_evidence_ids": ["togo", "paper"], "decision": "verified: paper and source comment explicitly declare g/L; no batch-volume assumption needed"}, {"field": "ingredients[3].concentration", "material": "Glucose", "record": {"value": "5", "unit": "G_PER_L"}, "source_amount": 5, "source_unit": "g", "source_locator": "components[0].items[3]", "source_evidence_ids": ["togo", "paper"], "decision": "verified: paper and source comment explicitly declare g/L; no batch-volume assumption needed"}, {"field": "ingredients[4].concentration", "material": "Tryptone", "record": {"value": "16", "unit": "G_PER_L"}, "source_amount": 16, "source_unit": "g", "source_locator": "components[0].items[4]", "source_evidence_ids": ["togo", "paper"], "decision": "verified: paper and source comment explicitly declare g/L; no batch-volume assumption needed"}], "target_owner_differences": ["curation_history", "merge_fingerprint", "merged_from"], "owner_history_preserved": true, "paper_page2_render_sha256": "d8ec67d8b3438436349c734a95908f807b3547ead345dd90a0d74523bc328d19"} |
| ownership | owned batch009 data tree; Exact top-level stable ID search and complete merge event | supports | rg --no-ignore --hidden -n "^id: CultureMech:009326$" data returned only data/merge_yaml/merged/2xYTG.yaml and data/normalized_yaml/bacterial/2xytg.yaml. Their stable IDs and the singleton merge source agree. |

## Limits And Additional Notes

- Publisher HTML and direct PDF requests each returned HTTP 403. The complete nine-page published article was recovered from the German National Library; original access times, failed attempts and successful PDF hash are retained. The recovered paper is not merely a search-result abstract.
- The PDF text extractor corrupts degree/minus glyphs and some units. Page 2 was visually inspected to confirm all four g/L concentrations and 37 C. Exact experimental extraction/recovery quantities outside the medium review are not copied from corrupted text.
- The paper identifies C. beijerinckii NCIMB 14988 and uses 2xYTG in its transformation workflow, but no independent collection identity, current strain taxon or assembly record was verified here. The target itself asserts no organism, taxon or assembly accession; paper-reported identities are not new grounded growth assertions.
- The paper general methods allow CBM, 2xYTG or CGM and conditional supplements. Do not treat every mentioned strain, engineered derivative, antibiotic, uracil or counter-selection reagent as part of unchanged 2xYTG. E. coli TOP10/DH10B growth is assigned to LB in the inspected paragraph.
- Sterilization, pH, exact undefined-mixture composition and a measured final-volume preparation procedure are not established by the inspected 2xYTG formula. The TOGO water row is a literal 1 L solvent input, not a justified water mass concentration or independent proof of a make-to-volume instruction.
- The article supporting-information files and separately cited CBM/CGM primary papers were not retrieved. TOGO embeds PMIDs 4332793 and 16346566 adjacent to CBM/CGM; they are not adopted as the identity of the paper containing the 2xYTG paragraph.
- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T075705Z-culturemech-009326-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 2xytg (CultureMech:009326)'
started_at: '2026-10-21T07:45:35Z'
finished_at: '2026-10-21T07:57:05Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author or modify the assessed recipe bytes.
    This is an independent agent review of captured local inputs and inspected primary/database
    sources, not experimental validation.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'TOGO M2778 and the recovered Little et al. 2018 paper identify this exact
  2xYTG formulation. All four solute concentrations are supported: tryptone 16, yeast
  extract 10, NaCl 5 and glucose 5 g/L. Both local layers incorrectly encode the TOGO
  1 L distilled-water input as 1 g/L and omit the source-scoped 37 C anaerobic culture
  context. The paper citation and claim-level formulation evidence are also absent.
  Generated and normalized recipe content otherwise agrees; there is no missing later
  owner curation. Four documented diagnostics pass.'
source:
  git_revision: 24a1d277eb7f0437af53af0d178a30f9bfa6374c
  state: working_tree
  inputs:
  - path: .claude/skills/audit-schema-gaps/SKILL.md
    sha256: 86467f280ecdd2d60531d3b2a9249d7a38efa4cfeab714d55421b9a62cfabb7d
    role: context
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 846db73710b3134ef5267ce486d151e297295282dc5e9249658592432f8d6a7a
    role: context
  - path: .claude/skills/review-ingredient-concentrations/references/evidence-contract.md
    sha256: 5eb4783f02a0567b45b462dfb5e8c0393fb34daf842a3ce23ff7946652f157d1
    role: context
  - path: .claude/skills/review-recipes/reference/linkage-and-duplicates.md
    sha256: e792d47f2b9e169d2306ac920f87aa1ced9b9d07c7650dd7d2feb7aee48c2234
    role: context
  - path: .claude/skills/review-recipes/reference/validation-rules.md
    sha256: 3b8666d58fc0c9deb02981053a50760a937675e6e22a6ecd53e92678e8d422f0
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: e3f1aeccd3d249f78739c902ea8d95052fec26fc5db752b5ca732d96ab37e466
    role: context
  - path: .claude/skills/schema-gap-analysis/SKILL.md
    sha256: 09665fe53584559e776f75ab41dfabd997eff0cac10bafcca0a721b678ccee93
    role: context
  - path: AGENTS.md
    sha256: 72737a531548de8636bcf70b972e71a7630a0e579215b6ded392d88d1b51a4fc
    role: context
  - path: CLAUDE.md
    sha256: b5c5bb1c2293ba5f6c49cda8cb40bf36e021c0a2b9fe2d9497cf0a2fe19a1ac4
    role: context
  - path: conf/oak_config.yaml
    sha256: e35781d4fd66de4289411141b4c8a94189782d864ba6c45e49bf46537c46c5a1
    role: context
  - path: conf/record_review.yaml
    sha256: a76531e51214e559c97ab748a4cba169f8a9598ce6e3664518489b43dfc9bf88
    role: context
  - path: data/merge_yaml/merged/2xYTG.yaml
    sha256: 72c47781cf61a607c04354d1f64d0a315f52c8288988dac41ee035897f7cdfd8
    role: target
  - path: data/normalized_yaml/bacterial/2xytg.yaml
    sha256: b6b4a0ddea738953c01f31278d78da59a25d89f1a47c75a4a9df2ea2cb114746
    role: context
  - path: docs/DATA_LAYERS.md
    sha256: 381cbb9ad2ba80f2a849507c4ce8b10839546ae4ce2757dad065e86fe381d236
    role: context
  - path: docs/record-review-profile.md
    sha256: 99eebe27f0079cb816c974f58ee457148da5a3c346ec9c30ff853b95dade9127
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: justfile
    sha256: 552166976136ed158a253773f0b763e670d2484e7354b48ec0f9b77b4250da77
    role: context
  - path: project.justfile
    sha256: 3576f5ce2adee0179be4f2d3fd134841249eb9a54a7eed8b388c3b345883a5fe
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/validate_recipe_references.py
    sha256: 087e5f3128e774bc760b7dcfc8f194fe14820354f809be9e35cf6cacb8546a3b
    role: context
  - path: scripts/validate_strict.py
    sha256: d6775c8c53ee433426ad7d3ababdf1740fc6adc62cb8269cf07ca0cd251cef68
    role: context
  - path: src/culturemech/convert/mediadive_raw_yaml.py
    sha256: 70ba720001705c315f2c5bd40871e08f6f429b6229c78255e6c94dfdcc482432
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
    role: context
  - path: src/culturemech/fetch/mediadive_api_fetcher.py
    sha256: 60b15f231d96099bd76ff10bb215de2d0ca9ad71de5d7977b0054d1b7b622c5e
    role: context
  - path: src/culturemech/import/mediadive_importer.py
    sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
    role: context
  - path: src/culturemech/merge/fingerprint.py
    sha256: 9bc62b7f462b26775e7dff15bb91beb653ba8f1642b247466dba1c0366ed8a9e
    role: context
  - path: src/culturemech/merge/formulation.py
    sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
    role: context
  - path: src/culturemech/merge/matcher.py
    sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
    role: context
  - path: src/culturemech/merge/merge_recipes.py
    sha256: ce00a4b4e0bc2fa9a63e8b33f4a591cb20984569e125d395af40f5b7e84766a7
    role: context
  - path: src/culturemech/merge/merger.py
    sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
    role: context
  - path: src/culturemech/schema/culturemech.yaml
    sha256: cb8e4b047647d41f47b91d83420799555c09696c8a2a890535a74076e6f8bba6
    role: context
scope:
  description: One complete generated MediaRecipe, including source identity, every
    listed amount, chemical forms, stocks, conditions, preparation, classifications,
    provenance, and maintained-input correspondence.
  selection: Task review 89; batch 009 item 9 of 10, selected in Python lexicographic
    order of currently uncovered merged paths. The preceding eight task batches contain
    80 ledger-owned validated record reviews; their complete validated lists also
    retain upstream baseline reviews. Fresh origin/main at 24a1d277eb7f0437af53af0d178a30f9bfa6374c
    contains 40 validated baseline bundles covering 2 current merged paths. Unioning
    all prior lists with this baseline covers 82 of 6320 current merged paths, including
    2 paths beyond task-owned reviews. This target path is absent from that union.
    Task ordinals count task reviews, not current global path ranks or all upstream
    coverage. Only the named target is reviewed; no sampling or fleet-wide scientific
    claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009326
targets:
- target_id: CultureMech:009326
  path: data/merge_yaml/merged/2xYTG.yaml
  label: 2xytg
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/2xytg.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/2xYTG.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:009326
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/2xYTG.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch009/089/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-009/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch009/089/strict.tsv"
  target_ids:
  - CultureMech:009326
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/2xYTG.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:009326
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/2xYTG.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:009326
  evidence_ids:
  - validate-references
- check_id: structured-source-adapter
  name: iModulonDB applicability
  required: false
  status: not_applicable
  summary: The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic
    dataset requiring an iModulonDB cross-check; expression-module membership cannot
    establish this formulation.
  target_ids:
  - CultureMech:009326
- check_id: publisher-access
  name: Publisher primary-paper access
  required: false
  status: unavailable
  summary: Publisher HTML and direct PDF each returned 403; the complete published
    article was successfully retrieved from the German National Library, independently
    identified and inspected.
  target_ids:
  - CultureMech:009326
  evidence_ids:
  - little2018publisher
  - little2018publisherPDF
  - paper
  - paper-metadata
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/2xYTG.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-21T07:57:05Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/2xytg.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T07:57:05Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/2xYTG.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T07:48:28.133851Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/2xYTG.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch009/089/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-21T07:48:29.851629Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-009/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch009/089/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/2xYTG.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T07:48:32.243016Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/2xYTG.yaml
  locator: Actual command output
  accessed_at: '2026-10-21T07:48:33.445549Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: togo
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2778
  locator: $.meta; $.components[0].items[0:5]; $.comments[0].comment
  accessed_at: '2026-10-21T07:33:27.627052Z'
  support: supports
  summary: 'Exact M2778 API identifies 2xYTG and supplies five rows: distilled water
    1 L, yeast extract 10 g, NaCl 5 g, glucose 5 g and tryptone 16 g. The comment
    explicitly states all four solute concentrations in g/L and clostridial culture
    at 37 C in an anaerobic cabinet. The adjacent PMID annotations belong to alternative
    CBM/CGM references in that comment, not the recovered 2xYTG paper identity. Ingredient
    role/property prose in both local files is retained from these rows. Source capture
    key=togoM2778api; original access timestamp and raw SHA256 retained.'
  snapshot_sha256: 0c8a46cf22864371082dc767dc244d44e50df84fd201298adc42fd317f721659
- evidence_id: paper
  kind: primary_source
  reference: https://d-nb.info/1265485364/34
  locator: PDF pages 1–9 in full; page 1 title/authors/DOI; page 2 section 2.1, Media,
    Strains, and Growth Conditions
  accessed_at: '2026-10-21T07:35:03.107010Z'
  support: supports
  summary: Read complete nine-page published article. Little GT, Willson BJ, Heap
    JT, Winzer K and Minton NP, The Butanol Producing Microbe Clostridium beijerinckii
    NCIMB 14988 Manipulated Using Forward and Reverse Genetic Tools, Biotechnology
    Journal 2018, 13, 1700711; DOI 10.1002/biot.201700711. Section 2.1 directly defines
    the same four solute concentrations and the 37 C anaerobic culture context. Its
    formula was also checked visually on page 2. No sterilization or pH instruction
    for this formula is supplied. Source capture key=little2018dnbPDF; original access
    timestamp and raw SHA256 retained.
  snapshot_sha256: 154ddc7de0b1f46379c39514996f9167aaea02fb9b6f3bedd5b4e08e833ae453
- evidence_id: paper-scope
  kind: primary_source
  reference: https://d-nb.info/1265485364/34
  locator: Sections 2.1, 2.2, 2.3, 2.5, 3.1 and 3.3; contextual figure/method references;
    full-paper scope
  accessed_at: '2026-10-21T07:35:03.107010Z'
  support: supports
  summary: Section 2.5 explicitly uses 2xYTG broth for growth and post-transformation
    recovery in the C. beijerinckii workflow; section 3.3 identifies the competent
    cells as NCIMB 14988. Section 3.1 states isolate 59B was deposited as NCIMB 14988.
    These observations remain specific to that study/workflow. The initial environmental
    isolation is on CBM, E. coli TOP10/DH10B are grown on LB, and conditional antibiotics,
    uracil and counter-selection conditions are separate. DNA extraction and analytical
    solvent extraction are not additions to or preparation of this 2xYTG recipe. Yeast
    extract is an undefined medium ingredient, not evidence of a cell-free extract-production
    medium. Source capture key=little2018dnbPDF; original access timestamp and raw
    SHA256 retained.
  snapshot_sha256: 154ddc7de0b1f46379c39514996f9167aaea02fb9b6f3bedd5b4e08e833ae453
- evidence_id: paper-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1002%2Fbiot.201700711&format=json&resultType=core
  locator: 'resultList.result[0]: id, source, doi, title, authorString, pubYear and
    journalInfo'
  accessed_at: '2026-10-21T07:34:34.362234Z'
  support: supports
  summary: Europe PMC DOI lookup agrees with the recovered title, five authors and
    year and resolves PMID 29660854 (source MED). No PMCID is returned in this response;
    no exhaustive absence claim is made. Source capture key=little2018metadata; original
    access timestamp and raw SHA256 retained.
  snapshot_sha256: e71f57c8f5d708d1695f044398cd94853c5988801e0436676df3dc61b67ad0e0
- evidence_id: togo-page
  kind: database
  reference: https://togomedium.org/medium/M2778
  locator: Entire returned HTML shell
  accessed_at: '2026-10-21T07:34:34.361670Z'
  support: context_only
  summary: HTTP 200 returned a 750-byte JavaScript shell, not the scientific recipe
    text. The inspected structured API and complete paper supply the substantive evidence.
    Source capture key=togoM2778page; original access timestamp and raw SHA256 retained.
  snapshot_sha256: 78669d85db93e40276577aaf5073aa0bc2420fe5b7be6212de5619e445da93aa
- evidence_id: little2018publisher
  kind: search
  reference: https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/10.1002/biot.201700711
  locator: Exact publisher HTML or direct PDF request
  accessed_at: '2026-10-21T07:34:34.362123Z'
  support: unknown
  summary: 'HTTP Error 403: Forbidden. Failed attempt retained; substantive article
    access was recovered separately through the German National Library. This is not
    a new request during drafting.'
  snapshot_sha256: b1f8201aac565e464fa0bae7d4a4cb782f71855411f62edd70ab9f710ee3ef82
  search_scope: Exact free public article endpoint; HTTP 403 response, no paid access
    or bypass. Alternate public institutional archive supplied the published PDF.
- evidence_id: little2018publisherPDF
  kind: search
  reference: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/biot.201700711
  locator: Exact publisher HTML or direct PDF request
  accessed_at: '2026-10-21T07:35:03.106462Z'
  support: unknown
  summary: 'HTTP Error 403: Forbidden. Failed attempt retained; substantive article
    access was recovered separately through the German National Library. This is not
    a new request during drafting.'
  snapshot_sha256: 59673742dcd6b69072c0ee53a8629f545404c1d16288e9c688d229024a2c19b6
  search_scope: Exact free public article endpoint; HTTP 403 response, no paid access
    or bypass. Alternate public institutional archive supplied the published PDF.
- evidence_id: chebi15377
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15377
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T07:31:15.205780Z'
  support: supports
  summary: CHEBI:15377 resolves to water and is not obsolete. This verifies the asserted
    generic chemical identity; no source grade, salt, hydrate or stereochemistry beyond
    the record is inferred.
  snapshot_sha256: de9102073c3761a24130636f90e898445dce83eb118592609a618bf61149ff4b
- evidence_id: chebi17234
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T07:31:15.211005Z'
  support: supports
  summary: CHEBI:17234 resolves to glucose and is not obsolete. This verifies the
    asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: e3b9cbcd7b1e08bb05564cf82f924b29c554767e9b40bf1e4c85ab1bce09330f
- evidence_id: chebi26710
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: Exact OLS term identifier, label, available definition/form and obsolete
    flag
  accessed_at: '2026-10-21T07:31:15.881003Z'
  support: supports
  summary: CHEBI:26710 resolves to sodium chloride and is not obsolete. This verifies
    the asserted generic chemical identity; no source grade, salt, hydrate or stereochemistry
    beyond the record is inferred.
  snapshot_sha256: 2afe639e870dee30cad14e81231180e3ddea68f425ee849f7ca2b0c89414d97e
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All live preferred-term rows for asserted secondary CHEBI keys; metadata
    captured
  accessed_at: '2026-10-21T07:57:05Z'
  support: supports
  summary: '{"CHEBI:15377": [{"label": "Distilled water", "match_type": "preferred_term",
    "identifier": "CHEBI:15377", "preferred_term": "Distilled water", "ontology_id":
    "CHEBI:15377", "mapping_status": "MAPPED", "ambiguity": "unique"}], "CHEBI:26710":
    [{"label": "NaCl", "match_type": "preferred_term", "identifier": "CHEBI:26710",
    "preferred_term": "NaCl", "ontology_id": "CHEBI:26710", "mapping_status": "MAPPED",
    "ambiguity": "unique"}], "CHEBI:17234": [{"label": "Glucose", "match_type": "preferred_term",
    "identifier": "CHEBI:17234", "preferred_term": "Glucose", "ontology_id": "CHEBI:17234",
    "mapping_status": "MAPPED", "ambiguity": "unique"}]}'
- evidence_id: comparison
  kind: validation
  reference: Full inspected target, owner, TOGO API and published-paper formula
  locator: All five amounts; all top-level target/owner fields and history timestamps;
    paper page 2 visual confirmation
  accessed_at: '2026-10-21T07:57:05Z'
  support: supports
  summary: '{"amounts": [{"field": "ingredients[0].concentration", "material": "Distilled
    water", "record": {"value": "1", "unit": "G_PER_L"}, "source_amount": 1, "source_unit":
    "L", "source_locator": "components[0].items[0]", "source_evidence_ids": ["togo"],
    "decision": "correct: source solvent input 1 L was encoded as 1 G_PER_L; dimensional
    error, no mass/density conversion justified"}, {"field": "ingredients[1].concentration",
    "material": "Yeast extract", "record": {"value": "10", "unit": "G_PER_L"}, "source_amount":
    10, "source_unit": "g", "source_locator": "components[0].items[1]", "source_evidence_ids":
    ["togo", "paper"], "decision": "verified: paper and source comment explicitly
    declare g/L; no batch-volume assumption needed"}, {"field": "ingredients[2].concentration",
    "material": "NaCl", "record": {"value": "5", "unit": "G_PER_L"}, "source_amount":
    5, "source_unit": "g", "source_locator": "components[0].items[2]", "source_evidence_ids":
    ["togo", "paper"], "decision": "verified: paper and source comment explicitly
    declare g/L; no batch-volume assumption needed"}, {"field": "ingredients[3].concentration",
    "material": "Glucose", "record": {"value": "5", "unit": "G_PER_L"}, "source_amount":
    5, "source_unit": "g", "source_locator": "components[0].items[3]", "source_evidence_ids":
    ["togo", "paper"], "decision": "verified: paper and source comment explicitly
    declare g/L; no batch-volume assumption needed"}, {"field": "ingredients[4].concentration",
    "material": "Tryptone", "record": {"value": "16", "unit": "G_PER_L"}, "source_amount":
    16, "source_unit": "g", "source_locator": "components[0].items[4]", "source_evidence_ids":
    ["togo", "paper"], "decision": "verified: paper and source comment explicitly
    declare g/L; no batch-volume assumption needed"}], "target_owner_differences":
    ["curation_history", "merge_fingerprint", "merged_from"], "owner_history_preserved":
    true, "paper_page2_render_sha256": "d8ec67d8b3438436349c734a95908f807b3547ead345dd90a0d74523bc328d19"}'
- evidence_id: ownership
  kind: record_content
  reference: owned batch009 data tree
  locator: Exact top-level stable ID search and complete merge event
  accessed_at: '2026-10-21T07:57:05Z'
  support: supports
  summary: 'rg --no-ignore --hidden -n "^id: CultureMech:009326$" data returned only
    data/merge_yaml/merged/2xYTG.yaml and data/normalized_yaml/bacterial/2xytg.yaml.
    Their stable IDs and the singleton merge source agree.'
  search_scope: Owned batch009 data tree, including ignored and hidden files; exact
    top-level ID. No absence claim outside this bounded tree.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:009326
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: grounding
  area: grounding
  topic: All asserted primary and current secondary ingredient identifiers
  outcome: supported
  summary: '3 primary CHEBI identities resolve with matching labels; 3 of 3 current
    secondary keys have live pinned-index rows. Unresolved keys: [].'
  target_ids:
  - CultureMech:009326
  evidence_ids:
  - record
  - mim
  - chebi15377
  - chebi17234
  - chebi26710
  details: 5 direct ingredient instances; CHEBI-primary instance linkage 3/5 (60.00%),
    verified secondary coverage 3/5 (60.00%). Percentages use a 0–100 linkage scale,
    not a scientific correctness score. Complex mixtures without asserted IDs remain
    ungrounded rather than receiving invented pure-molecule identities.
- assessment_id: identity
  area: identity
  topic: TOGO M2778 and Little 2018 source identity
  outcome: supported
  summary: The exact TOGO accession/title, all ingredient rows, explicit source concentration
    paragraph and full paper agree. The maintained owner is uniquely resolved within
    the data-tree ID lookup and singleton merge event. Little DOI 10.1002/biot.201700711
    / PMID 29660854 is the recipe-bearing article; the CBM/CGM inline reference markers
    are not substituted for it.
  target_ids:
  - CultureMech:009326
  evidence_ids:
  - record
  - owner-0
  - ownership
  - togo
  - paper
  - paper-metadata
- assessment_id: amounts
  area: quantity
  topic: All five declared quantities
  outcome: concern
  summary: 'Four solute concentrations are explicitly supported without arithmetic:
    yeast extract 10, NaCl 5, glucose 5 and tryptone 16 g/L. Water is the sole quantity
    error: literal source input 1 L became 1 g/L. There are no nested stocks or supplied
    solution doses to audit. No water density or total final-volume conversion is
    inferred.'
  target_ids:
  - CultureMech:009326
  evidence_ids:
  - record
  - owner-0
  - togo
  - paper
  - comparison
  details: '[{"field": "ingredients[0].concentration", "material": "Distilled water",
    "record": {"value": "1", "unit": "G_PER_L"}, "source_amount": 1, "source_unit":
    "L", "source_locator": "components[0].items[0]", "source_evidence_ids": ["togo"],
    "decision": "correct: source solvent input 1 L was encoded as 1 G_PER_L; dimensional
    error, no mass/density conversion justified"}, {"field": "ingredients[1].concentration",
    "material": "Yeast extract", "record": {"value": "10", "unit": "G_PER_L"}, "source_amount":
    10, "source_unit": "g", "source_locator": "components[0].items[1]", "source_evidence_ids":
    ["togo", "paper"], "decision": "verified: paper and source comment explicitly
    declare g/L; no batch-volume assumption needed"}, {"field": "ingredients[2].concentration",
    "material": "NaCl", "record": {"value": "5", "unit": "G_PER_L"}, "source_amount":
    5, "source_unit": "g", "source_locator": "components[0].items[2]", "source_evidence_ids":
    ["togo", "paper"], "decision": "verified: paper and source comment explicitly
    declare g/L; no batch-volume assumption needed"}, {"field": "ingredients[3].concentration",
    "material": "Glucose", "record": {"value": "5", "unit": "G_PER_L"}, "source_amount":
    5, "source_unit": "g", "source_locator": "components[0].items[3]", "source_evidence_ids":
    ["togo", "paper"], "decision": "verified: paper and source comment explicitly
    declare g/L; no batch-volume assumption needed"}, {"field": "ingredients[4].concentration",
    "material": "Tryptone", "record": {"value": "16", "unit": "G_PER_L"}, "source_amount":
    16, "source_unit": "g", "source_locator": "components[0].items[4]", "source_evidence_ids":
    ["togo", "paper"], "decision": "verified: paper and source comment explicitly
    declare g/L; no batch-volume assumption needed"}]'
- assessment_id: chemical-forms
  area: grounding
  topic: Pure compounds versus undefined extracts
  outcome: supported
  summary: Water, sodium chloride and generic glucose carry canonical non-obsolete
    CHEBI labels and matching live packaged MIM keys. Both primary and current secondary
    linkage are 3/5 ingredient instances (60% on a 0–100 linkage scale), not accuracy
    scores. The source does not establish glucose anomer/hydrate or defined molecular
    compositions for yeast extract and tryptone. Imported role/property notes agree
    with TOGO without becoming experimental mechanism evidence.
  target_ids:
  - CultureMech:009326
  evidence_ids:
  - record
  - togo
  - paper
  - mim
  - chebi15377
  - chebi26710
  - chebi17234
- assessment_id: culture-context
  area: completeness
  topic: Source-scoped culture conditions and experimental boundaries
  outcome: concern
  summary: The source explicitly reports clostridial culture at 37 C in an anaerobic
    cabinet, including 2xYTG among alternatives, but neither local layer preserves
    this context. The paper identifies a specific NCIMB 14988 transformation/culture
    use; it does not establish unrestricted growth for every mentioned organism. Context
    should remain qualified to the cited study, not an optimal range or universal
    strain claim.
  target_ids:
  - CultureMech:009326
  evidence_ids:
  - record
  - owner-0
  - togo
  - paper
  - paper-scope
- assessment_id: preparation
  area: scope
  topic: Missing source detail versus unrelated procedures
  outcome: supported
  summary: No 2xYTG sterilization, pH adjustment or specific make-to-volume instruction
    was established by the inspected formula. No default is invented. Antibiotics
    when required, mutant supplementation, counter-selection, CBM isolation, LB cultures,
    electroporation buffer, DNA extraction and solvent-analysis reagents remain separate
    from the unsupplemented five-row recipe. No obligatory recipe-variant or stock
    omission is inferred from their presence elsewhere in the paper.
  target_ids:
  - CultureMech:009326
  evidence_ids:
  - record
  - owner-0
  - togo
  - paper
  - paper-scope
- assessment_id: evidence
  area: evidence
  topic: Recoverable primary citation and claim-level support
  outcome: concern
  summary: Both local files cite only TOGO M2778 in notes/media_term. Neither retains
    the identified primary paper or ingredient-level source support, despite an exact
    recoverable formula and the limited culture context. The generated reference validator
    performed zero checks; its success does not establish the article evidence. The
    recovered full paper resolves publisher-access failure without concealing the
    original 403 attempts.
  target_ids:
  - CultureMech:009326
  evidence_ids:
  - record
  - owner-0
  - togo
  - paper
  - paper-metadata
  - little2018publisher
  - little2018publisherPDF
  - validate-references
- assessment_id: correspondence
  area: provenance
  topic: Complete owner correspondence and append-only history
  outcome: supported
  summary: Generated and maintained content agree in every substantive top-level field;
    only merge metadata and the added singleton merge event differ. All owner history
    events are preserved with timezone-bearing timestamps. This record has no stale
    omitted owner citations or variants. Corrections belong to the normalized owner
    followed by authorized regeneration.
  target_ids:
  - CultureMech:009326
  evidence_ids:
  - record
  - owner-0
  - comparison
  - ownership
- assessment_id: classification
  area: scope
  topic: Classification and asserted application
  outcome: supported
  summary: Bacterial category is consistent with the documented clostridial use; broth
    and absence of agar support LIQUID, and yeast extract/tryptone support COMPLEX
    and UNDEFINED. Generic microbial-cultivation application does not claim experimentally
    established growth for all microbes. No native organism, taxon, assembly or variant
    assertions are present.
  target_ids:
  - CultureMech:009326
  evidence_ids:
  - record
  - owner-0
  - togo
  - paper
  - paper-scope
findings:
- finding_id: f1
  issue_key: CM009326-water-unit-corruption
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: One litre of source water is encoded as one gram per litre
  description: Both local files retain the numerical 1 but replace TOGO volume unit
    L with G_PER_L. This changes a solvent input into a mass concentration. The paper
    independently verifies the four solutes; it does not support the water mass assertion.
  target_ids:
  - CultureMech:009326
  field_paths:
  - ingredients[0].concentration
  evidence_ids:
  - record
  - owner-0
  - togo
  - paper
  - comparison
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/2xytg.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: CM009326-culture-context-omitted
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Documented anaerobic culture context is absent
  description: TOGO reproduces the primary report of clostridial cultivation at 37
    C in an anaerobic cabinet using CBM, 2xYTG or CGM. Neither local file preserves
    this context. Omitting oxygen/temperature context matters to the documented use,
    but the source does not authorize universal growth assertions or an optimal-temperature
    claim.
  target_ids:
  - CultureMech:009326
  field_paths:
  - notes
  - temperature_value
  - incubation_atmosphere
  evidence_ids:
  - record
  - owner-0
  - togo
  - paper
  - paper-scope
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/2xytg.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P2
  normalization_reason: P2 normalized to major based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f3
  issue_key: CM009326-primary-evidence-unlinked
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Exact primary formulation citation and support are not retained
  description: The record contains a TOGO pointer but no reference or claim-level
    evidence for the four independently verified solute concentrations or the bounded
    culture context. The recipe-bearing paper is identifiable as Little et al. 2018,
    DOI 10.1002/biot.201700711 and PMID 29660854; inline CBM/CGM identifiers must
    not be substituted for it.
  target_ids:
  - CultureMech:009326
  field_paths:
  - references
  - ingredients[1].evidence
  - ingredients[2].evidence
  - ingredients[3].evidence
  - ingredients[4].evidence
  - notes
  evidence_ids:
  - record
  - owner-0
  - togo
  - paper
  - paper-metadata
  - validate-references
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/2xytg.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  native_severity: P3
  normalization_reason: P3 normalized to minor based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
actions:
- action_id: a1
  description: Restore the literal source 1 L water input in suitable solvent/batch
    or preparation context, or another schema-supported faithful representation. Do
    not invent density, a 1 g/L concentration or an unsupported final-volume instruction.
    Preserve all four verified solute concentrations.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:009326
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/2xytg.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify the exact source accession, ingredient form, original unit and batch/preparation
    context.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on separately authorized maintained-input corrections.
  - Regenerate derived records only after owner verification; run just verify-merges
    and just audit-merge-freshness and confirm corrected fields/evidence survive.
- action_id: a2
  description: Preserve the paper-scoped 37 C anaerobic context with source evidence
    and its media/strain qualifications, using supported fields or qualified notes.
    Keep LB-grown E. coli, conditional supplements, extraction buffers and separate
    CBM/CGM protocols out of the unchanged parent recipe.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:009326
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/2xytg.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify the exact source accession, ingredient form, original unit and batch/preparation
    context.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on separately authorized maintained-input corrections.
  - Regenerate derived records only after owner verification; run just verify-merges
    and just audit-merge-freshness and confirm corrected fields/evidence survive.
- action_id: a3
  description: Attach the verified primary citation and narrow formula/culture evidence
    in the maintained owner with exact locators and archived-source provenance. Preserve
    unsuccessful publisher access and successful institutional recovery; do not assert
    unverified strain taxonomy, genomic identity or universal culture conditions.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:009326
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/2xytg.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify the exact source accession, ingredient form, original unit and batch/preparation
    context.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on separately authorized maintained-input corrections.
  - Regenerate derived records only after owner verification; run just verify-merges
    and just audit-merge-freshness and confirm corrected fields/evidence survive.
limitations:
- Publisher HTML and direct PDF requests each returned HTTP 403. The complete nine-page
  published article was recovered from the German National Library; original access
  times, failed attempts and successful PDF hash are retained. The recovered paper
  is not merely a search-result abstract.
- The PDF text extractor corrupts degree/minus glyphs and some units. Page 2 was visually
  inspected to confirm all four g/L concentrations and 37 C. Exact experimental extraction/recovery
  quantities outside the medium review are not copied from corrupted text.
- The paper identifies C. beijerinckii NCIMB 14988 and uses 2xYTG in its transformation
  workflow, but no independent collection identity, current strain taxon or assembly
  record was verified here. The target itself asserts no organism, taxon or assembly
  accession; paper-reported identities are not new grounded growth assertions.
- The paper general methods allow CBM, 2xYTG or CGM and conditional supplements. Do
  not treat every mentioned strain, engineered derivative, antibiotic, uracil or counter-selection
  reagent as part of unchanged 2xYTG. E. coli TOP10/DH10B growth is assigned to LB
  in the inspected paragraph.
- Sterilization, pH, exact undefined-mixture composition and a measured final-volume
  preparation procedure are not established by the inspected 2xYTG formula. The TOGO
  water row is a literal 1 L solvent input, not a justified water mass concentration
  or independent proof of a make-to-volume instruction.
- The article supporting-information files and separately cited CBM/CGM primary papers
  were not retrieved. TOGO embeds PMIDs 4332793 and 16346566 adjacent to CBM/CGM;
  they are not adopted as the identity of the paper containing the 2xYTG paragraph.
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
tags:
- unreviewed-records
- batch-009
- generated-medium
```
