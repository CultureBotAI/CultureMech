# NMM/CgC paper citations, isotope variants and bounded organism evidence

- Review: 20261013T115530Z-nmm-cgc-paper-citations
- Repository: culturebotai/CultureMech
- Started UTC: 2026-10-13T11:09:31Z
- Finished UTC: 2026-10-13T11:55:30Z
- Reviewer: codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

18 paper-record citations across nine owners/four publications. Four inline CgC variants and three DOI/snippet-backed variant-only growth entries; six NMM owners receive bibliography and qualified unresolved notes. All 100 parent ingredients preserved. Nine strict/schema/term checks pass; nine reference checks and 2 global merge diagnostics fail.

## Scope And Provenance

Exact nine MediaDB source 54/95 normalized owners; focused citation, formulation-difference and organism-evidence review.

Selection: Exact source-owner joins, not a corpus sample or full recipe review.
Coverage: full; 9 reviewed / 9 in the declared population.
Source: working_tree at Git base 41d4d390123c0d8320cd53e994470c88a1b86d8c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007045 | data/normalized_yaml/bacterial/nmm_with_glucose.yaml | maintained | nmm_with_glucose |
| CultureMech:007046 | data/normalized_yaml/bacterial/nmm_with_pyruvate.yaml | maintained | nmm_with_pyruvate |
| CultureMech:007047 | data/normalized_yaml/bacterial/nmm_with_lactate.yaml | maintained | nmm_with_lactate |
| CultureMech:007048 | data/normalized_yaml/bacterial/nmm_with_malate.yaml | maintained | nmm_with_malate |
| CultureMech:007049 | data/normalized_yaml/bacterial/nmm_with_succinate.yaml | maintained | nmm_with_succinate |
| CultureMech:007051 | data/normalized_yaml/bacterial/nmm_with_acetate.yaml | maintained | nmm_with_acetate |
| CultureMech:007184 | data/normalized_yaml/bacterial/cgc_w_acetate.yaml | maintained | cgc_w_acetate |
| CultureMech:007185 | data/normalized_yaml/bacterial/cgc_w_acetate_glucose.yaml | maintained | cgc_w_acetate_glucose |
| CultureMech:007186 | data/normalized_yaml/bacterial/cgc_w_glucose.yaml | maintained | cgc_w_glucose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| just validate data/normalized_yaml/bacterial/nmm_with_glucose.yaml | passed | True | CultureMech:007045 | Baseline retained after exact input hashes verified. |
| just validate-strict data/normalized_yaml/bacterial/nmm_with_glucose.yaml | passed | True | CultureMech:007045 | Baseline retained after exact input hashes verified. |
| just validate data/normalized_yaml/bacterial/nmm_with_pyruvate.yaml | passed | True | CultureMech:007046 | Baseline retained after exact input hashes verified. |
| just validate-strict data/normalized_yaml/bacterial/nmm_with_pyruvate.yaml | passed | True | CultureMech:007046 | Baseline retained after exact input hashes verified. |
| just validate data/normalized_yaml/bacterial/nmm_with_lactate.yaml | passed | True | CultureMech:007047 | Baseline retained after exact input hashes verified. |
| just validate-strict data/normalized_yaml/bacterial/nmm_with_lactate.yaml | passed | True | CultureMech:007047 | Baseline retained after exact input hashes verified. |
| just validate data/normalized_yaml/bacterial/nmm_with_malate.yaml | passed | True | CultureMech:007048 | Baseline retained after exact input hashes verified. |
| just validate-strict data/normalized_yaml/bacterial/nmm_with_malate.yaml | passed | True | CultureMech:007048 | Baseline retained after exact input hashes verified. |
| just validate data/normalized_yaml/bacterial/nmm_with_succinate.yaml | passed | True | CultureMech:007049 | Baseline retained after exact input hashes verified. |
| just validate-strict data/normalized_yaml/bacterial/nmm_with_succinate.yaml | passed | True | CultureMech:007049 | Baseline retained after exact input hashes verified. |
| just validate data/normalized_yaml/bacterial/nmm_with_acetate.yaml | passed | True | CultureMech:007051 | Baseline retained after exact input hashes verified. |
| just validate-strict data/normalized_yaml/bacterial/nmm_with_acetate.yaml | passed | True | CultureMech:007051 | Baseline retained after exact input hashes verified. |
| just validate data/normalized_yaml/bacterial/cgc_w_acetate.yaml | passed | True | CultureMech:007184 | Baseline retained after exact input hashes verified. |
| just validate-strict data/normalized_yaml/bacterial/cgc_w_acetate.yaml | passed | True | CultureMech:007184 | Baseline retained after exact input hashes verified. |
| just validate data/normalized_yaml/bacterial/cgc_w_acetate_glucose.yaml | passed | True | CultureMech:007185 | Baseline retained after exact input hashes verified. |
| just validate-strict data/normalized_yaml/bacterial/cgc_w_acetate_glucose.yaml | passed | True | CultureMech:007185 | Baseline retained after exact input hashes verified. |
| just validate data/normalized_yaml/bacterial/cgc_w_glucose.yaml | passed | True | CultureMech:007186 | Baseline retained after exact input hashes verified. |
| just validate-strict data/normalized_yaml/bacterial/cgc_w_glucose.yaml | passed | True | CultureMech:007186 | Baseline retained after exact input hashes verified. |
| just validate data/normalized_yaml/bacterial/nmm_with_glucose.yaml | failed | True | CultureMech:007045 | Schema and terms pass; reference checks fail on title formatting and, for CgC, abstract-only retrieval of full-text excerpts. |
| just validate-strict data/normalized_yaml/bacterial/nmm_with_glucose.yaml | passed | True | CultureMech:007045 | Actual maintained check result. |
| just validate data/normalized_yaml/bacterial/nmm_with_pyruvate.yaml | failed | True | CultureMech:007046 | Schema and terms pass; reference checks fail on title formatting and, for CgC, abstract-only retrieval of full-text excerpts. |
| just validate-strict data/normalized_yaml/bacterial/nmm_with_pyruvate.yaml | passed | True | CultureMech:007046 | Actual maintained check result. |
| just validate data/normalized_yaml/bacterial/nmm_with_lactate.yaml | failed | True | CultureMech:007047 | Schema and terms pass; reference checks fail on title formatting and, for CgC, abstract-only retrieval of full-text excerpts. |
| just validate-strict data/normalized_yaml/bacterial/nmm_with_lactate.yaml | passed | True | CultureMech:007047 | Actual maintained check result. |
| just validate data/normalized_yaml/bacterial/nmm_with_malate.yaml | failed | True | CultureMech:007048 | Schema and terms pass; reference checks fail on title formatting and, for CgC, abstract-only retrieval of full-text excerpts. |
| just validate-strict data/normalized_yaml/bacterial/nmm_with_malate.yaml | passed | True | CultureMech:007048 | Actual maintained check result. |
| just validate data/normalized_yaml/bacterial/nmm_with_succinate.yaml | failed | True | CultureMech:007049 | Schema and terms pass; reference checks fail on title formatting and, for CgC, abstract-only retrieval of full-text excerpts. |
| just validate-strict data/normalized_yaml/bacterial/nmm_with_succinate.yaml | passed | True | CultureMech:007049 | Actual maintained check result. |
| just validate data/normalized_yaml/bacterial/nmm_with_acetate.yaml | failed | True | CultureMech:007051 | Schema and terms pass; reference checks fail on title formatting and, for CgC, abstract-only retrieval of full-text excerpts. |
| just validate-strict data/normalized_yaml/bacterial/nmm_with_acetate.yaml | passed | True | CultureMech:007051 | Actual maintained check result. |
| just validate data/normalized_yaml/bacterial/cgc_w_acetate.yaml | failed | True | CultureMech:007184 | Schema and terms pass; reference checks fail on title formatting and, for CgC, abstract-only retrieval of full-text excerpts. |
| just validate-strict data/normalized_yaml/bacterial/cgc_w_acetate.yaml | passed | True | CultureMech:007184 | Actual maintained check result. |
| just validate data/normalized_yaml/bacterial/cgc_w_acetate_glucose.yaml | failed | True | CultureMech:007185 | Schema and terms pass; reference checks fail on title formatting and, for CgC, abstract-only retrieval of full-text excerpts. |
| just validate-strict data/normalized_yaml/bacterial/cgc_w_acetate_glucose.yaml | passed | True | CultureMech:007185 | Actual maintained check result. |
| just validate data/normalized_yaml/bacterial/cgc_w_glucose.yaml | failed | True | CultureMech:007186 | Schema and terms pass; reference checks fail on title formatting and, for CgC, abstract-only retrieval of full-text excerpts. |
| just validate-strict data/normalized_yaml/bacterial/cgc_w_glucose.yaml | passed | True | CultureMech:007186 | Actual maintained check result. |
| just verify-merges | failed | True | CultureMech:007045, CultureMech:007046, CultureMech:007047, CultureMech:007048, CultureMech:007049, CultureMech:007051, CultureMech:007184, CultureMech:007185, CultureMech:007186 | Required global merge diagnostic; checked-in generated output unchanged. |
| just audit-merge-freshness --json | failed | True | CultureMech:007045, CultureMech:007046, CultureMech:007047, CultureMech:007048, CultureMech:007049, CultureMech:007051, CultureMech:007184, CultureMech:007185, CultureMech:007186 | Required global merge diagnostic; checked-in generated output unchanged. |
| /tmp/culturemech-parallel-env-20261012/bin/python -m pytest --no-cov -q -p no:cacheprovider tests/test_claude_skills.py tests/test_skill_frontmatter.py tests/test_fetch_pubmed_abstracts.py tests/test_record_io.py tests/test_media_variant_links.py tests/test_record_review_contract.py | passed | True | CultureMech:007045, CultureMech:007046, CultureMech:007047, CultureMech:007048, CultureMech:007049, CultureMech:007051, CultureMech:007184, CultureMech:007185, CultureMech:007186 | Actual maintained check result. |
| /tmp/culturemech-parallel-env-20261012/bin/python scripts/validate_claude_skills.py | passed | True | CultureMech:007045, CultureMech:007046, CultureMech:007047, CultureMech:007048, CultureMech:007049, CultureMech:007051, CultureMech:007184, CultureMech:007185, CultureMech:007186 | Actual maintained check result. |
| git diff --check | passed | True | CultureMech:007045, CultureMech:007046, CultureMech:007047, CultureMech:007048, CultureMech:007049, CultureMech:007051, CultureMech:007184, CultureMech:007185, CultureMech:007186 | Actual maintained check result. |

## Scientific And Domain Assessments

### Publication identity, bibliography and source access

evidence: supported. Targets: CultureMech:007045.

Two deduplicated citations with verified title, authors, year, identifiers, discovery mode, source type and raw/Markdown archives. Bibliographic relevance does not certify the complete parent recipe.

### Study formulation and supported differences

evidence: concern. Targets: CultureMech:007045.

Carbon mass dose is explicit, but complete base and chemical-form correspondence remain unresolved. No forced variant or parent concentration correction.

{"variants": [], "preserved_parent_amounts": [{"field_path": "ingredients[0].concentration", "chemical": "D-Glucose", "term": {"id": "CHEBI:17634", "label": "D-glucose"}, "concentration": {"value": "28.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[1].concentration", "chemical": "Magnesium chloride", "term": {"id": "CHEBI:86345", "label": "magnesium dichloride hexahydrate"}, "concentration": {"value": "0.523", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[2].concentration", "chemical": "Calcium chloride anhydrous", "term": {"id": "CHEBI:3312", "label": "calcium dichloride"}, "concentration": {"value": "0.0005", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[3].concentration", "chemical": "Potassium sulfate", "term": {"id": "CHEBI:32036", "label": "potassium sulfate"}, "concentration": {"value": "0.276", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[4].concentration", "chemical": "Potassium dibasic phosphate", "term": {"id": "CHEBI:131527", "label": "dipotassium hydrogen phosphate"}, "concentration": {"value": "1.32", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[5].concentration", "chemical": "Sodium chloride", "term": {"id": "CHEBI:26710", "label": "sodium chloride"}, "concentration": {"value": "50.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[6].concentration", "chemical": "Ammonium chloride", "term": {"id": "CHEBI:31206", "label": "ammonium chloride"}, "concentration": {"value": "9.52", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[7].concentration", "chemical": "Ferrous sulfate", "term": {"id": "CHEBI:75832", "label": "iron(2+) sulfate (anhydrous)"}, "concentration": {"value": "0.01", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[8].concentration", "chemical": "MOPS", "term": {"id": "CHEBI:39074", "label": "MOPS"}, "concentration": {"value": "40.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[9].concentration", "chemical": "Tricine", "term": {"id": "CHEBI:46760", "label": "tricine"}, "concentration": {"value": "4.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}]}

### Taxonomy and growth-versus-mention scope

evidence: supported. Targets: CultureMech:007045.

Source growth observations and organisms have explicit mappings, but unresolved local formulation prevents a native positive target. Strains, mutants, plates and mixed competition are kept separate.

[]

### Publication boundary

evidence: supported. Targets: CultureMech:007045.

No native positive growth entry added. No generated output published.

### Publication identity, bibliography and source access

evidence: supported. Targets: CultureMech:007046.

Two deduplicated citations with verified title, authors, year, identifiers, discovery mode, source type and raw/Markdown archives. Bibliographic relevance does not certify the complete parent recipe.

### Study formulation and supported differences

evidence: concern. Targets: CultureMech:007046.

Carbon mass dose is explicit, but complete base and chemical-form correspondence remain unresolved. No forced variant or parent concentration correction.

{"variants": [], "preserved_parent_amounts": [{"field_path": "ingredients[0].concentration", "chemical": "Pyruvate", "term": {"id": "CHEBI:15361", "label": "pyruvate"}, "concentration": {"value": "57.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[1].concentration", "chemical": "Magnesium chloride", "term": {"id": "CHEBI:86345", "label": "magnesium dichloride hexahydrate"}, "concentration": {"value": "0.523", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[2].concentration", "chemical": "Calcium chloride anhydrous", "term": {"id": "CHEBI:3312", "label": "calcium dichloride"}, "concentration": {"value": "0.0005", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[3].concentration", "chemical": "Potassium sulfate", "term": {"id": "CHEBI:32036", "label": "potassium sulfate"}, "concentration": {"value": "0.276", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[4].concentration", "chemical": "Potassium dibasic phosphate", "term": {"id": "CHEBI:131527", "label": "dipotassium hydrogen phosphate"}, "concentration": {"value": "1.32", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[5].concentration", "chemical": "Sodium chloride", "term": {"id": "CHEBI:26710", "label": "sodium chloride"}, "concentration": {"value": "50.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[6].concentration", "chemical": "Ammonium chloride", "term": {"id": "CHEBI:31206", "label": "ammonium chloride"}, "concentration": {"value": "9.52", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[7].concentration", "chemical": "Ferrous sulfate", "term": {"id": "CHEBI:75832", "label": "iron(2+) sulfate (anhydrous)"}, "concentration": {"value": "0.01", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[8].concentration", "chemical": "MOPS", "term": {"id": "CHEBI:39074", "label": "MOPS"}, "concentration": {"value": "40.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[9].concentration", "chemical": "Tricine", "term": {"id": "CHEBI:46760", "label": "tricine"}, "concentration": {"value": "4.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}]}

### Taxonomy and growth-versus-mention scope

evidence: supported. Targets: CultureMech:007046.

Source growth observations and organisms have explicit mappings, but unresolved local formulation prevents a native positive target. Strains, mutants, plates and mixed competition are kept separate.

[]

### Publication boundary

evidence: supported. Targets: CultureMech:007046.

No native positive growth entry added. No generated output published.

### Publication identity, bibliography and source access

evidence: supported. Targets: CultureMech:007047.

Two deduplicated citations with verified title, authors, year, identifiers, discovery mode, source type and raw/Markdown archives. Bibliographic relevance does not certify the complete parent recipe.

### Study formulation and supported differences

evidence: concern. Targets: CultureMech:007047.

Carbon mass dose is explicit, but complete base and chemical-form correspondence remain unresolved. No forced variant or parent concentration correction.

{"variants": [], "preserved_parent_amounts": [{"field_path": "ingredients[0].concentration", "chemical": "(R)-Lactate", "term": null, "concentration": {"value": "56.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[1].concentration", "chemical": "Magnesium chloride", "term": {"id": "CHEBI:86345", "label": "magnesium dichloride hexahydrate"}, "concentration": {"value": "0.523", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[2].concentration", "chemical": "Calcium chloride anhydrous", "term": {"id": "CHEBI:3312", "label": "calcium dichloride"}, "concentration": {"value": "0.0005", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[3].concentration", "chemical": "Potassium sulfate", "term": {"id": "CHEBI:32036", "label": "potassium sulfate"}, "concentration": {"value": "0.276", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[4].concentration", "chemical": "Potassium dibasic phosphate", "term": {"id": "CHEBI:131527", "label": "dipotassium hydrogen phosphate"}, "concentration": {"value": "1.32", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[5].concentration", "chemical": "Sodium chloride", "term": {"id": "CHEBI:26710", "label": "sodium chloride"}, "concentration": {"value": "50.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[6].concentration", "chemical": "Ammonium chloride", "term": {"id": "CHEBI:31206", "label": "ammonium chloride"}, "concentration": {"value": "9.52", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[7].concentration", "chemical": "Ferrous sulfate", "term": {"id": "CHEBI:75832", "label": "iron(2+) sulfate (anhydrous)"}, "concentration": {"value": "0.01", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[8].concentration", "chemical": "MOPS", "term": {"id": "CHEBI:39074", "label": "MOPS"}, "concentration": {"value": "40.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[9].concentration", "chemical": "Tricine", "term": {"id": "CHEBI:46760", "label": "tricine"}, "concentration": {"value": "4.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}]}

### Taxonomy and growth-versus-mention scope

evidence: supported. Targets: CultureMech:007047.

Source growth observations and organisms have explicit mappings, but unresolved local formulation prevents a native positive target. Strains, mutants, plates and mixed competition are kept separate.

[]

### Publication boundary

evidence: supported. Targets: CultureMech:007047.

No native positive growth entry added. No generated output published.

### Publication identity, bibliography and source access

evidence: supported. Targets: CultureMech:007048.

Two deduplicated citations with verified title, authors, year, identifiers, discovery mode, source type and raw/Markdown archives. Bibliographic relevance does not certify the complete parent recipe.

### Study formulation and supported differences

evidence: concern. Targets: CultureMech:007048.

Carbon mass dose is explicit, but complete base and chemical-form correspondence remain unresolved. No forced variant or parent concentration correction.

{"variants": [], "preserved_parent_amounts": [{"field_path": "ingredients[0].concentration", "chemical": "(S)-Malate", "term": null, "concentration": {"value": "38.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[1].concentration", "chemical": "Magnesium chloride", "term": {"id": "CHEBI:86345", "label": "magnesium dichloride hexahydrate"}, "concentration": {"value": "0.523", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[2].concentration", "chemical": "Calcium chloride anhydrous", "term": {"id": "CHEBI:3312", "label": "calcium dichloride"}, "concentration": {"value": "0.0005", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[3].concentration", "chemical": "Potassium sulfate", "term": {"id": "CHEBI:32036", "label": "potassium sulfate"}, "concentration": {"value": "0.276", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[4].concentration", "chemical": "Potassium dibasic phosphate", "term": {"id": "CHEBI:131527", "label": "dipotassium hydrogen phosphate"}, "concentration": {"value": "1.32", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[5].concentration", "chemical": "Sodium chloride", "term": {"id": "CHEBI:26710", "label": "sodium chloride"}, "concentration": {"value": "50.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[6].concentration", "chemical": "Ammonium chloride", "term": {"id": "CHEBI:31206", "label": "ammonium chloride"}, "concentration": {"value": "9.52", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[7].concentration", "chemical": "Ferrous sulfate", "term": {"id": "CHEBI:75832", "label": "iron(2+) sulfate (anhydrous)"}, "concentration": {"value": "0.01", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[8].concentration", "chemical": "MOPS", "term": {"id": "CHEBI:39074", "label": "MOPS"}, "concentration": {"value": "40.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[9].concentration", "chemical": "Tricine", "term": {"id": "CHEBI:46760", "label": "tricine"}, "concentration": {"value": "4.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}]}

### Taxonomy and growth-versus-mention scope

evidence: supported. Targets: CultureMech:007048.

Source growth observations and organisms have explicit mappings, but unresolved local formulation prevents a native positive target. Strains, mutants, plates and mixed competition are kept separate.

[]

### Publication boundary

evidence: supported. Targets: CultureMech:007048.

No native positive growth entry added. No generated output published.

### Publication identity, bibliography and source access

evidence: supported. Targets: CultureMech:007049.

Two deduplicated citations with verified title, authors, year, identifiers, discovery mode, source type and raw/Markdown archives. Bibliographic relevance does not certify the complete parent recipe.

### Study formulation and supported differences

evidence: concern. Targets: CultureMech:007049.

Carbon mass dose is explicit, but complete base and chemical-form correspondence remain unresolved. No forced variant or parent concentration correction.

{"variants": [], "preserved_parent_amounts": [{"field_path": "ingredients[0].concentration", "chemical": "Succinate", "term": {"id": "CHEBI:26806", "label": "succinate"}, "concentration": {"value": "43.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[1].concentration", "chemical": "Magnesium chloride", "term": {"id": "CHEBI:86345", "label": "magnesium dichloride hexahydrate"}, "concentration": {"value": "0.523", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[2].concentration", "chemical": "Calcium chloride anhydrous", "term": {"id": "CHEBI:3312", "label": "calcium dichloride"}, "concentration": {"value": "0.0005", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[3].concentration", "chemical": "Potassium sulfate", "term": {"id": "CHEBI:32036", "label": "potassium sulfate"}, "concentration": {"value": "0.276", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[4].concentration", "chemical": "Potassium dibasic phosphate", "term": {"id": "CHEBI:131527", "label": "dipotassium hydrogen phosphate"}, "concentration": {"value": "1.32", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[5].concentration", "chemical": "Sodium chloride", "term": {"id": "CHEBI:26710", "label": "sodium chloride"}, "concentration": {"value": "50.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[6].concentration", "chemical": "Ammonium chloride", "term": {"id": "CHEBI:31206", "label": "ammonium chloride"}, "concentration": {"value": "9.52", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[7].concentration", "chemical": "Ferrous sulfate", "term": {"id": "CHEBI:75832", "label": "iron(2+) sulfate (anhydrous)"}, "concentration": {"value": "0.01", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[8].concentration", "chemical": "MOPS", "term": {"id": "CHEBI:39074", "label": "MOPS"}, "concentration": {"value": "40.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[9].concentration", "chemical": "Tricine", "term": {"id": "CHEBI:46760", "label": "tricine"}, "concentration": {"value": "4.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}]}

### Taxonomy and growth-versus-mention scope

evidence: supported. Targets: CultureMech:007049.

Source growth observations and organisms have explicit mappings, but unresolved local formulation prevents a native positive target. Strains, mutants, plates and mixed competition are kept separate.

[]

### Publication boundary

evidence: supported. Targets: CultureMech:007049.

No native positive growth entry added. No generated output published.

### Publication identity, bibliography and source access

evidence: supported. Targets: CultureMech:007051.

Two deduplicated citations with verified title, authors, year, identifiers, discovery mode, source type and raw/Markdown archives. Bibliographic relevance does not certify the complete parent recipe.

### Study formulation and supported differences

evidence: concern. Targets: CultureMech:007051.

Carbon mass dose is explicit, but complete base and chemical-form correspondence remain unresolved. No forced variant or parent concentration correction.

{"variants": [], "preserved_parent_amounts": [{"field_path": "ingredients[0].concentration", "chemical": "Acetate", "term": {"id": "CHEBI:30089", "label": "acetate"}, "concentration": {"value": "85.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[1].concentration", "chemical": "Magnesium chloride", "term": {"id": "CHEBI:86345", "label": "magnesium dichloride hexahydrate"}, "concentration": {"value": "0.523", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[2].concentration", "chemical": "Calcium chloride anhydrous", "term": {"id": "CHEBI:3312", "label": "calcium dichloride"}, "concentration": {"value": "0.0005", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[3].concentration", "chemical": "Potassium sulfate", "term": {"id": "CHEBI:32036", "label": "potassium sulfate"}, "concentration": {"value": "0.276", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[4].concentration", "chemical": "Potassium dibasic phosphate", "term": {"id": "CHEBI:131527", "label": "dipotassium hydrogen phosphate"}, "concentration": {"value": "1.32", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[5].concentration", "chemical": "Sodium chloride", "term": {"id": "CHEBI:26710", "label": "sodium chloride"}, "concentration": {"value": "50.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[6].concentration", "chemical": "Ammonium chloride", "term": {"id": "CHEBI:31206", "label": "ammonium chloride"}, "concentration": {"value": "9.52", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[7].concentration", "chemical": "Ferrous sulfate", "term": {"id": "CHEBI:75832", "label": "iron(2+) sulfate (anhydrous)"}, "concentration": {"value": "0.01", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[8].concentration", "chemical": "MOPS", "term": {"id": "CHEBI:39074", "label": "MOPS"}, "concentration": {"value": "40.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[9].concentration", "chemical": "Tricine", "term": {"id": "CHEBI:46760", "label": "tricine"}, "concentration": {"value": "4.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}]}

### Taxonomy and growth-versus-mention scope

evidence: supported. Targets: CultureMech:007051.

Source growth observations and organisms have explicit mappings, but unresolved local formulation prevents a native positive target. Strains, mutants, plates and mixed competition are kept separate.

[]

### Publication boundary

evidence: supported. Targets: CultureMech:007051.

No native positive growth entry added. No generated output published.

### Publication identity, bibliography and source access

evidence: supported. Targets: CultureMech:007184.

Two deduplicated citations with verified title, authors, year, identifiers, discovery mode, source type and raw/Markdown archives. Bibliographic relevance does not certify the complete parent recipe.

### Study formulation and supported differences

evidence: concern. Targets: CultureMech:007184.

Explicit isotope substitution and, on the mixed owner, a separate concentration variant; mass/molar and base-protocol uncertainty retained.

{"variants": [{"name": "Wendisch 2000 CgC with sodium [1-13C]acetate", "relationship": "SUBSTITUTED_COMPONENT_VARIANT", "description": "This is a source-described CgC assay variant, not certification of all imported parent amounts. The Eikmanns 1991 base protocol is available only as abstract/metadata; its full base composition and preparation remain unresolved. The paper's sodium acetate is not silently equated with an unspecified acetate counterion or hydration state. Keep reported mass doses and Table 2 nominal molar headings separate; no conversion or correction of the parent's minerals, vitamins, carbon amounts or filter step is made. Materials/Methods specify 99% atom enrichment, whereas the flux-quantitation paragraph uses 99.9% glucose in its inoculum correction; that discrepancy is unresolved. ", "modifications": ["Use sodium [1-13C]acetate at the Methods dose of 10 g/L; Table 2 reports nominal 120 mM acetate. The parent acetate descriptor has no isotope specification and reports 120 mM."], "purpose": "The paper's 13C-labeling and metabolic-flux experiment", "evidence": [{"reference": "doi:10.1128/JB.182.11.3088-3096.2000", "supports": "SUPPORT", "snippet": "sodium [1- 13 C]acetate (99% atom enrichment) (10 g/liter)", "explanation": "Supports this variant's explicitly labeled carbon source, source mass dose and isotope substitution. Table 2, carbon-source headings in order; exact excerpt='120 mM acetate 120 mM acetate + 55 mM glucose 110 mM glucose'. Table 2 column order is acetate, mixed acetate/glucose, glucose. Headers are reported nominal values, not curator conversions. This is a source-described CgC assay variant, not certification of all imported parent amounts. The Eikmanns 1991 base protocol is available only as abstract/metadata; its full base composition and preparation remain unresolved. The paper's sodium acetate is not silently equated with an unspecified acetate counterion or hydration state. Keep reported mass doses and Table 2 nominal molar headings separate; no conversion or correction of the parent's minerals, vitamins, carbon amounts or filter step is made. Materials/Methods specify 99% atom enrichment, whereas the flux-quantitation paragraph uses 99.9% glucose in its inoculum correction; that discrepancy is unresolved. "}]}], "preserved_parent_amounts": [{"field_path": "ingredients[0].concentration", "chemical": "Acetate", "term": {"id": "CHEBI:30089", "label": "acetate"}, "concentration": {"value": "120.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[1].concentration", "chemical": "Urea", "term": {"id": "CHEBI:16199", "label": "urea"}, "concentration": {"value": "83.3", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[2].concentration", "chemical": "Biotin", "term": {"id": "CHEBI:15956", "label": "biotin"}, "concentration": {"value": "0.000819", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[3].concentration", "chemical": "Calcium chloride anhydrous", "term": {"id": "CHEBI:3312", "label": "calcium dichloride"}, "concentration": {"value": "0.0775", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[4].concentration", "chemical": "Potassium dibasic phosphate", "term": {"id": "CHEBI:131527", "label": "dipotassium hydrogen phosphate"}, "concentration": {"value": "2.87", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[5].concentration", "chemical": "Potassium dihydrogen phosphate", "term": {"id": "CHEBI:63036", "label": "potassium dihydrogen phosphate"}, "concentration": {"value": "3.67", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[6].concentration", "chemical": "Magnesium sulfate", "term": {"id": "CHEBI:32599", "label": "magnesium sulfate"}, "concentration": {"value": "1.01", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[7].concentration", "chemical": "Manganese sulfate", "term": {"id": "CHEBI:86364", "label": "manganese(II) sulfate monohydrate"}, "concentration": {"value": "0.0592", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[8].concentration", "chemical": "Ferrous sulfate", "term": {"id": "CHEBI:75832", "label": "iron(2+) sulfate (anhydrous)"}, "concentration": {"value": "0.036", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[9].concentration", "chemical": "Zinc sulfate", "term": {"id": "CHEBI:35176", "label": "zinc sulfate"}, "concentration": {"value": "0.00348", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[10].concentration", "chemical": "Ammonium sulfate", "term": {"id": "CHEBI:62946", "label": "ammonium sulfate"}, "concentration": {"value": "37.8", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[11].concentration", "chemical": "Cupric sulfate", "term": {"id": "CHEBI:23414", "label": "copper(II) sulfate"}, "concentration": {"value": "0.00125", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[12].concentration", "chemical": "MOPS", "term": {"id": "CHEBI:39074", "label": "MOPS"}, "concentration": {"value": "100.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}]}

### Taxonomy and growth-versus-mention scope

evidence: supported. Targets: CultureMech:007184.

One qualitative ATCC13032 growth assertion with exact strain taxonomy and exact isotope-variant scope. Mutants and background organisms remain qualified notes; Figure 1 growth stays in variant evidence.

[{"preferred_term": "Corynebacterium glutamicum", "strain": "ATCC 13032", "term": {"id": "NCBITaxon:196627", "label": "Corynebacterium glutamicum ATCC 13032"}, "scoped_to_variant": "Wendisch 2000 CgC with sodium [1-13C]acetate", "evidence": [{"reference": "doi:10.1128/JB.182.11.3088-3096.2000", "supports": "SUPPORT", "snippet": "The growth characteristics of the three cultures are summarized in Table 2", "explanation": "Reported organism=Corynebacterium glutamicum ATCC 13032 (WT); scientific name/canonical mapping=Corynebacterium glutamicum ATCC 13032; NCBITaxon:196627; actual rank=strain; taxonomy_match=exact strain; role=wild type used in the Table 2 labeled-carbon assays. Lookup_on=2026-10-13; https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=196627&amp;retmode=xml. Methods, Microorganisms and cultivation conditions; exact excerpt='The wild-type (WT) strain of C. glutamicum ATCC 13032'. Table 2, carbon-source headings in order; exact excerpt='120 mM acetate 120 mM acetate + 55 mM glucose 110 mM glucose'. Table 2, growth-rate row in the same column order; exact excerpt='Growth rate (h −1 ) 0.28 0.36 0.32'. The positive Table 2 growth-rate cells support qualitative growth on each corresponding source-described labeled variant; quantitative metrics are not imported. Methods specify 60-mL cultures in 500-mL baffled flasks, 30 C, 140 rpm. These are experimental settings, not optima or universal requirements. Table 2 footnote a; exact excerpt='These data coincided with values obtained from at least three independent cultures with unlabeled substrates.'. Unlabeled-control agreement does not erase isotope scope or certify all local base amounts. This is a source-described CgC assay variant, not certification of all imported parent amounts. The Eikmanns 1991 base protocol is available only as abstract/metadata; its full base composition and preparation remain unresolved. The paper's sodium acetate is not silently equated with an unspecified acetate counterion or hydration state. Keep reported mass doses and Table 2 nominal molar headings separate; no conversion or correction of the parent's minerals, vitamins, carbon amounts or filter step is made. Materials/Methods specify 99% atom enrichment, whereas the flux-quantitation paragraph uses 99.9% glucose in its inoculum correction; that discrepancy is unresolved. Current KGX does not honor scoped_to_variant; these claims must not be published as unqualified parent-medium growth edges. Taxonomy archive=references_cache/papers/taxonomy/nmm-cgc-20261013.xml and .md."}]}]

### Publication boundary

evidence: concern. Targets: CultureMech:007184.

KGX would lose variant-only scope; publication remains blocked.

### Publication identity, bibliography and source access

evidence: supported. Targets: CultureMech:007185.

Two deduplicated citations with verified title, authors, year, identifiers, discovery mode, source type and raw/Markdown archives. Bibliographic relevance does not certify the complete parent recipe.

### Study formulation and supported differences

evidence: concern. Targets: CultureMech:007185.

Explicit isotope substitution and, on the mixed owner, a separate concentration variant; mass/molar and base-protocol uncertainty retained.

{"variants": [{"name": "Wendisch 2000 CgC with sodium [1-13C]acetate and unlabeled glucose", "relationship": "SUBSTITUTED_COMPONENT_VARIANT", "description": "This is a source-described CgC assay variant, not certification of all imported parent amounts. The Eikmanns 1991 base protocol is available only as abstract/metadata; its full base composition and preparation remain unresolved. The paper's sodium acetate is not silently equated with an unspecified acetate counterion or hydration state. Keep reported mass doses and Table 2 nominal molar headings separate; no conversion or correction of the parent's minerals, vitamins, carbon amounts or filter step is made. Materials/Methods specify 99% atom enrichment, whereas the flux-quantitation paragraph uses 99.9% glucose in its inoculum correction; that discrepancy is unresolved. ", "modifications": ["Use sodium [1-13C]acetate and unlabeled glucose at 10 g/L each; Table 2 reports nominal 120 mM acetate plus 55 mM glucose. Preserve the isotope/counterion substitution rather than treating the local acetate descriptor as identical."], "purpose": "The paper's 13C-labeling and metabolic-flux experiment", "evidence": [{"reference": "doi:10.1128/JB.182.11.3088-3096.2000", "supports": "SUPPORT", "snippet": "sodium [1- 13 C]acetate (99% atom enrichment) plus unlabeled glucose (10 g/liter each)", "explanation": "Supports this variant's explicitly labeled carbon source, source mass dose and isotope substitution. Table 2, carbon-source headings in order; exact excerpt='120 mM acetate 120 mM acetate + 55 mM glucose 110 mM glucose'. Table 2 column order is acetate, mixed acetate/glucose, glucose. Headers are reported nominal values, not curator conversions. This is a source-described CgC assay variant, not certification of all imported parent amounts. The Eikmanns 1991 base protocol is available only as abstract/metadata; its full base composition and preparation remain unresolved. The paper's sodium acetate is not silently equated with an unspecified acetate counterion or hydration state. Keep reported mass doses and Table 2 nominal molar headings separate; no conversion or correction of the parent's minerals, vitamins, carbon amounts or filter step is made. Materials/Methods specify 99% atom enrichment, whereas the flux-quantitation paragraph uses 99.9% glucose in its inoculum correction; that discrepancy is unresolved. "}]}, {"name": "Wendisch 2000 Figure 1 CgC with 35 mM glucose and 120 mM acetate", "relationship": "CONCENTRATION_VARIANT", "description": "Separate Figure 1 time-course assay; not Table 2's 55 mM glucose mixture. The caption does not specify isotope enrichment; Table 2's labeling treatment is not inherited. This is a source-described CgC assay variant, not certification of all imported parent amounts. The Eikmanns 1991 base protocol is available only as abstract/metadata; its full base composition and preparation remain unresolved. The paper's sodium acetate is not silently equated with an unspecified acetate counterion or hydration state. Keep reported mass doses and Table 2 nominal molar headings separate; no conversion or correction of the parent's minerals, vitamins, carbon amounts or filter step is made. Materials/Methods specify 99% atom enrichment, whereas the flux-quantitation paragraph uses 99.9% glucose in its inoculum correction; that discrepancy is unresolved. ", "modifications": ["Use the Figure 1 caption's 35 mM glucose rather than the parent's 55 mM; retain the stated 120 mM acetate."], "purpose": "Growth and substrate-consumption time course", "evidence": [{"reference": "doi:10.1128/JB.182.11.3088-3096.2000", "supports": "SUPPORT", "snippet": "Growth of C. glutamicum WT on mineral medium with 35 mM glucose and 120 mM acetate.", "explanation": "The caption establishes both carbon concentrations and WT cultivation. The inspected Figure 1 black-circle OD600 curve rises while substrate concentrations fall; no plotted values digitized. Reported organism=Corynebacterium glutamicum ATCC 13032 (WT); scientific name/canonical mapping=Corynebacterium glutamicum ATCC 13032; NCBITaxon:196627; actual rank=strain; taxonomy_match=exact strain; role=wild type used in the Table 2 labeled-carbon assays. Lookup_on=2026-10-13; https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=196627&amp;retmode=xml. This same organism also has Table 2 growth evidence under a different inline variant. The preferred_term identifier prevents independent repeated target entries; retain this figure's qualitative growth in variant evidence and citation notes rather than overwriting the Table 2 scope or inventing a different organism name. This is a source-described CgC assay variant, not certification of all imported parent amounts. The Eikmanns 1991 base protocol is available only as abstract/metadata; its full base composition and preparation remain unresolved. The paper's sodium acetate is not silently equated with an unspecified acetate counterion or hydration state. Keep reported mass doses and Table 2 nominal molar headings separate; no conversion or correction of the parent's minerals, vitamins, carbon amounts or filter step is made. Materials/Methods specify 99% atom enrichment, whereas the flux-quantitation paragraph uses 99.9% glucose in its inoculum correction; that discrepancy is unresolved. Current KGX does not honor scoped_to_variant; these claims must not be published as unqualified parent-medium growth edges. "}]}], "preserved_parent_amounts": [{"field_path": "ingredients[0].concentration", "chemical": "D-Glucose", "term": {"id": "CHEBI:17634", "label": "D-glucose"}, "concentration": {"value": "55.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[1].concentration", "chemical": "Acetate", "term": {"id": "CHEBI:30089", "label": "acetate"}, "concentration": {"value": "120.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[2].concentration", "chemical": "Urea", "term": {"id": "CHEBI:16199", "label": "urea"}, "concentration": {"value": "83.3", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[3].concentration", "chemical": "Biotin", "term": {"id": "CHEBI:15956", "label": "biotin"}, "concentration": {"value": "0.000819", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[4].concentration", "chemical": "Calcium chloride anhydrous", "term": {"id": "CHEBI:3312", "label": "calcium dichloride"}, "concentration": {"value": "0.0775", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[5].concentration", "chemical": "Potassium dibasic phosphate", "term": {"id": "CHEBI:131527", "label": "dipotassium hydrogen phosphate"}, "concentration": {"value": "2.87", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[6].concentration", "chemical": "Potassium dihydrogen phosphate", "term": {"id": "CHEBI:63036", "label": "potassium dihydrogen phosphate"}, "concentration": {"value": "3.67", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[7].concentration", "chemical": "Magnesium sulfate", "term": {"id": "CHEBI:32599", "label": "magnesium sulfate"}, "concentration": {"value": "1.01", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[8].concentration", "chemical": "Manganese sulfate", "term": {"id": "CHEBI:86364", "label": "manganese(II) sulfate monohydrate"}, "concentration": {"value": "0.0592", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[9].concentration", "chemical": "Ferrous sulfate", "term": {"id": "CHEBI:75832", "label": "iron(2+) sulfate (anhydrous)"}, "concentration": {"value": "0.036", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[10].concentration", "chemical": "Zinc sulfate", "term": {"id": "CHEBI:35176", "label": "zinc sulfate"}, "concentration": {"value": "0.00348", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[11].concentration", "chemical": "Ammonium sulfate", "term": {"id": "CHEBI:62946", "label": "ammonium sulfate"}, "concentration": {"value": "37.8", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[12].concentration", "chemical": "Cupric sulfate", "term": {"id": "CHEBI:23414", "label": "copper(II) sulfate"}, "concentration": {"value": "0.00125", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[13].concentration", "chemical": "MOPS", "term": {"id": "CHEBI:39074", "label": "MOPS"}, "concentration": {"value": "100.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}]}

### Taxonomy and growth-versus-mention scope

evidence: supported. Targets: CultureMech:007185.

One qualitative ATCC13032 growth assertion with exact strain taxonomy and exact isotope-variant scope. Mutants and background organisms remain qualified notes; Figure 1 growth stays in variant evidence.

[{"preferred_term": "Corynebacterium glutamicum", "strain": "ATCC 13032", "term": {"id": "NCBITaxon:196627", "label": "Corynebacterium glutamicum ATCC 13032"}, "scoped_to_variant": "Wendisch 2000 CgC with sodium [1-13C]acetate and unlabeled glucose", "evidence": [{"reference": "doi:10.1128/JB.182.11.3088-3096.2000", "supports": "SUPPORT", "snippet": "The growth characteristics of the three cultures are summarized in Table 2", "explanation": "Reported organism=Corynebacterium glutamicum ATCC 13032 (WT); scientific name/canonical mapping=Corynebacterium glutamicum ATCC 13032; NCBITaxon:196627; actual rank=strain; taxonomy_match=exact strain; role=wild type used in the Table 2 labeled-carbon assays. Lookup_on=2026-10-13; https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=196627&amp;retmode=xml. Methods, Microorganisms and cultivation conditions; exact excerpt='The wild-type (WT) strain of C. glutamicum ATCC 13032'. Table 2, carbon-source headings in order; exact excerpt='120 mM acetate 120 mM acetate + 55 mM glucose 110 mM glucose'. Table 2, growth-rate row in the same column order; exact excerpt='Growth rate (h −1 ) 0.28 0.36 0.32'. The positive Table 2 growth-rate cells support qualitative growth on each corresponding source-described labeled variant; quantitative metrics are not imported. Methods specify 60-mL cultures in 500-mL baffled flasks, 30 C, 140 rpm. These are experimental settings, not optima or universal requirements. Table 2 footnote a; exact excerpt='These data coincided with values obtained from at least three independent cultures with unlabeled substrates.'. Unlabeled-control agreement does not erase isotope scope or certify all local base amounts. This is a source-described CgC assay variant, not certification of all imported parent amounts. The Eikmanns 1991 base protocol is available only as abstract/metadata; its full base composition and preparation remain unresolved. The paper's sodium acetate is not silently equated with an unspecified acetate counterion or hydration state. Keep reported mass doses and Table 2 nominal molar headings separate; no conversion or correction of the parent's minerals, vitamins, carbon amounts or filter step is made. Materials/Methods specify 99% atom enrichment, whereas the flux-quantitation paragraph uses 99.9% glucose in its inoculum correction; that discrepancy is unresolved. Current KGX does not honor scoped_to_variant; these claims must not be published as unqualified parent-medium growth edges. Taxonomy archive=references_cache/papers/taxonomy/nmm-cgc-20261013.xml and .md."}]}]

### Publication boundary

evidence: concern. Targets: CultureMech:007185.

KGX would lose variant-only scope; publication remains blocked.

### Publication identity, bibliography and source access

evidence: supported. Targets: CultureMech:007186.

Two deduplicated citations with verified title, authors, year, identifiers, discovery mode, source type and raw/Markdown archives. Bibliographic relevance does not certify the complete parent recipe.

### Study formulation and supported differences

evidence: concern. Targets: CultureMech:007186.

Explicit isotope substitution and, on the mixed owner, a separate concentration variant; mass/molar and base-protocol uncertainty retained.

{"variants": [{"name": "Wendisch 2000 CgC with [5-13C]glucose", "relationship": "SUBSTITUTED_COMPONENT_VARIANT", "description": "This is a source-described CgC assay variant, not certification of all imported parent amounts. The Eikmanns 1991 base protocol is available only as abstract/metadata; its full base composition and preparation remain unresolved. The paper's sodium acetate is not silently equated with an unspecified acetate counterion or hydration state. Keep reported mass doses and Table 2 nominal molar headings separate; no conversion or correction of the parent's minerals, vitamins, carbon amounts or filter step is made. Materials/Methods specify 99% atom enrichment, whereas the flux-quantitation paragraph uses 99.9% glucose in its inoculum correction; that discrepancy is unresolved. ", "modifications": ["Use [5-13C]glucose at the Methods dose of 20 g/L; Table 2 reports nominal 110 mM glucose. The parent D-glucose descriptor does not specify this isotope label."], "purpose": "The paper's 13C-labeling and metabolic-flux experiment", "evidence": [{"reference": "doi:10.1128/JB.182.11.3088-3096.2000", "supports": "SUPPORT", "snippet": "[5- 13 C]glucose (99% atom enrichment) (20 g/liter)", "explanation": "Supports this variant's explicitly labeled carbon source, source mass dose and isotope substitution. Table 2, carbon-source headings in order; exact excerpt='120 mM acetate 120 mM acetate + 55 mM glucose 110 mM glucose'. Table 2 column order is acetate, mixed acetate/glucose, glucose. Headers are reported nominal values, not curator conversions. This is a source-described CgC assay variant, not certification of all imported parent amounts. The Eikmanns 1991 base protocol is available only as abstract/metadata; its full base composition and preparation remain unresolved. The paper's sodium acetate is not silently equated with an unspecified acetate counterion or hydration state. Keep reported mass doses and Table 2 nominal molar headings separate; no conversion or correction of the parent's minerals, vitamins, carbon amounts or filter step is made. Materials/Methods specify 99% atom enrichment, whereas the flux-quantitation paragraph uses 99.9% glucose in its inoculum correction; that discrepancy is unresolved. "}]}], "preserved_parent_amounts": [{"field_path": "ingredients[0].concentration", "chemical": "D-Glucose", "term": {"id": "CHEBI:17634", "label": "D-glucose"}, "concentration": {"value": "110.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[1].concentration", "chemical": "Urea", "term": {"id": "CHEBI:16199", "label": "urea"}, "concentration": {"value": "83.3", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[2].concentration", "chemical": "Biotin", "term": {"id": "CHEBI:15956", "label": "biotin"}, "concentration": {"value": "0.000819", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[3].concentration", "chemical": "Calcium chloride anhydrous", "term": {"id": "CHEBI:3312", "label": "calcium dichloride"}, "concentration": {"value": "0.0775", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[4].concentration", "chemical": "Potassium dibasic phosphate", "term": {"id": "CHEBI:131527", "label": "dipotassium hydrogen phosphate"}, "concentration": {"value": "2.87", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[5].concentration", "chemical": "Potassium dihydrogen phosphate", "term": {"id": "CHEBI:63036", "label": "potassium dihydrogen phosphate"}, "concentration": {"value": "3.67", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[6].concentration", "chemical": "Magnesium sulfate", "term": {"id": "CHEBI:32599", "label": "magnesium sulfate"}, "concentration": {"value": "1.01", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[7].concentration", "chemical": "Manganese sulfate", "term": {"id": "CHEBI:86364", "label": "manganese(II) sulfate monohydrate"}, "concentration": {"value": "0.0592", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[8].concentration", "chemical": "Ferrous sulfate", "term": {"id": "CHEBI:75832", "label": "iron(2+) sulfate (anhydrous)"}, "concentration": {"value": "0.036", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[9].concentration", "chemical": "Zinc sulfate", "term": {"id": "CHEBI:35176", "label": "zinc sulfate"}, "concentration": {"value": "0.00348", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[10].concentration", "chemical": "Ammonium sulfate", "term": {"id": "CHEBI:62946", "label": "ammonium sulfate"}, "concentration": {"value": "37.8", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[11].concentration", "chemical": "Cupric sulfate", "term": {"id": "CHEBI:23414", "label": "copper(II) sulfate"}, "concentration": {"value": "0.00125", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[12].concentration", "chemical": "MOPS", "term": {"id": "CHEBI:39074", "label": "MOPS"}, "concentration": {"value": "100.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent concentration-review scope"}]}

### Taxonomy and growth-versus-mention scope

evidence: supported. Targets: CultureMech:007186.

One qualitative ATCC13032 growth assertion with exact strain taxonomy and exact isotope-variant scope. Mutants and background organisms remain qualified notes; Figure 1 growth stays in variant evidence.

[{"preferred_term": "Corynebacterium glutamicum", "strain": "ATCC 13032", "term": {"id": "NCBITaxon:196627", "label": "Corynebacterium glutamicum ATCC 13032"}, "scoped_to_variant": "Wendisch 2000 CgC with [5-13C]glucose", "evidence": [{"reference": "doi:10.1128/JB.182.11.3088-3096.2000", "supports": "SUPPORT", "snippet": "The growth characteristics of the three cultures are summarized in Table 2", "explanation": "Reported organism=Corynebacterium glutamicum ATCC 13032 (WT); scientific name/canonical mapping=Corynebacterium glutamicum ATCC 13032; NCBITaxon:196627; actual rank=strain; taxonomy_match=exact strain; role=wild type used in the Table 2 labeled-carbon assays. Lookup_on=2026-10-13; https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=196627&amp;retmode=xml. Methods, Microorganisms and cultivation conditions; exact excerpt='The wild-type (WT) strain of C. glutamicum ATCC 13032'. Table 2, carbon-source headings in order; exact excerpt='120 mM acetate 120 mM acetate + 55 mM glucose 110 mM glucose'. Table 2, growth-rate row in the same column order; exact excerpt='Growth rate (h −1 ) 0.28 0.36 0.32'. The positive Table 2 growth-rate cells support qualitative growth on each corresponding source-described labeled variant; quantitative metrics are not imported. Methods specify 60-mL cultures in 500-mL baffled flasks, 30 C, 140 rpm. These are experimental settings, not optima or universal requirements. Table 2 footnote a; exact excerpt='These data coincided with values obtained from at least three independent cultures with unlabeled substrates.'. Unlabeled-control agreement does not erase isotope scope or certify all local base amounts. This is a source-described CgC assay variant, not certification of all imported parent amounts. The Eikmanns 1991 base protocol is available only as abstract/metadata; its full base composition and preparation remain unresolved. The paper's sodium acetate is not silently equated with an unspecified acetate counterion or hydration state. Keep reported mass doses and Table 2 nominal molar headings separate; no conversion or correction of the parent's minerals, vitamins, carbon amounts or filter step is made. Materials/Methods specify 99% atom enrichment, whereas the flux-quantitation paragraph uses 99.9% glucose in its inoculum correction; that discrepancy is unresolved. Current KGX does not honor scoped_to_variant; these claims must not be published as unqualified parent-medium growth edges. Taxonomy archive=references_cache/papers/taxonomy/nmm-cgc-20261013.xml and .md."}]}]

### Publication boundary

evidence: concern. Targets: CultureMech:007186.

KGX would lose variant-only scope; publication remains blocked.

## Findings

### nmm-formulation: NMM base and mass-to-molar correspondence remain unresolved

major / open / confirmed; issue key: nmm-cgc-citations-nmm-formulation.

Full Neidhardt body was not obtained. Chemical form, stereochemistry, hydrates, rounded molarity, micronutrients, pH and generic preparation cannot be certified from the carbon-dose statement. No forced variant or parent growth assertion.

### cgc-formulation: CgC full base and isotope/concentration normalization remain incomplete

major / open / confirmed; issue key: nmm-cgc-citations-cgc-formulation.

Eikmanns is abstract-only. Preserve reported isotope doses and nominal molarity without assuming equivalence. The 99 versus 99.9 percent enrichment discrepancy is explicit; source variants do not certify all parent chemistry.

### multiple-variant-growth: One organism identifier cannot represent two separately scoped inline growth assertions

major / open / confirmed; issue key: nmm-cgc-citations-multiple-variant-growth.

The mixed owner has Table 2 tracer growth and distinct Figure 1 growth. Only tracer growth is a target entry; Figure 1 support remains in its variant evidence and citation notes. Do not fabricate organism names or collapse scopes.

### kgx-scope: KGX export would lose three variant-only growth scopes

major / open / confirmed; issue key: nmm-cgc-citations-kgx-scope.

Current exporter targets the parent despite scoped_to_variant. No affected edges are published; this finding does not supersede older reviews of other owners.

### reference-gates: Nine required reference checks fail on formatting and content coverage

major / open / confirmed; issue key: nmm-cgc-citations-reference-gates.

Verified plain PubMed titles differ from HTML-bearing or whitespace-defective Crossref titles. CgC full-text excerpts also exceed abstract-only retrieval coverage. Accurate source claims were not changed to game the checks; manual readback does not waive failure.

## Recommended Actions And Acceptance Checks

### resolve-nmm-formulation

NMM base and mass-to-molar correspondence remain unresolved

- Inspect an authorized complete base protocol and exact carbon chemical forms.
- Require primary DOI/PURL and literal excerpts for each proposed amount correction; retain arithmetic separately.

### resolve-cgc-formulation

CgC full base and isotope/concentration normalization remain incomplete

- Obtain and inspect the complete CgC base source.
- Reconcile exact chemical mass basis and conflicting enrichment statements before changing parent amounts or variant scope.

### resolve-multiple-variant-growth

One organism identifier cannot represent two separately scoped inline growth assertions

- Provide a tested native representation for repeated organism/strain observations scoped to different inline variants, or curate separately authorized linked records.
- Preserve both independent scopes and primary excerpts.

### resolve-kgx-scope

KGX export would lose three variant-only growth scopes

- Add tests proving scoped entries cannot produce unqualified parent edges.
- Preserve ordinary targets and exact primary evidence.

### resolve-reference-gates

Nine required reference checks fail on formatting and content coverage

- Make normalized bibliography metadata and archived primary full-text excerpts auditable without altering correct source claims.
- Rerun maintained gates after any separately scoped validator fix.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| vanderrest | doi:10.1128/JB.182.24.6892-6899.2000; references_cache/papers/primary_html/vanderrest-2000-pmc.html; Methods; Figures 2/3; Tables 3/4; Results and Discussion | supports | NMM carbon mass doses and wild-type growth are explicit, but correspondence to each imported molar chemical form and the complete base remains unresolved. Mutants, plasmid induction, plate assays, mixed competition and enzyme-assay reagents are kept distinct. |
| wendisch | doi:10.1128/JB.182.11.3088-3096.2000; references_cache/papers/primary_html/wendisch-2000-pmc.html; Methods; Figure 1; Table 2 including headings and footnote; isotope-flux discussion | supports | Three isotope tracer variants have explicit qualitative wild-type growth. Figure 1 uses a distinct mixed-carbon concentration and unspecified isotope status. Reported mass doses, nominal molar headings and conflicting atom-enrichment statements are not silently reconciled. |
| nmm-figure | doi:10.1128/JB.182.24.6892-6899.2000; references_cache/papers/primary_images/vanderrest-2000-figure3.jpg; Figure 3 visually inspected with caption | supports | Black MC4100 bars support growth on six carbon sources. Mutant bars remain separate; no plotted rates were digitized or native parent growth asserted. |
| cgc-figure | doi:10.1128/JB.182.11.3088-3096.2000; references_cache/papers/primary_images/wendisch-2000-figure1.jpg; Figure 1 visually inspected with caption | supports | WT biomass increases in the distinct concentration experiment. This observation stays in variant evidence/notes because one preferred_term cannot encode two independently scoped growth entries. |
| neidhardt | PMID:4604283; references_cache/papers/primary_xml/neidhardt-1974-pmc-abstract.xml; Abstract only; no full scanned body | supports | The base-protocol abstract names Escherichia coli and Salmonella typhimurium but does not enumerate the complete NMM formulation. Bibliography and qualified notes only. |
| eikmanns | doi:10.1007/BF00167910; references_cache/papers/primary_html/eikmanns-1991-publisher-abstract.html; Publisher bibliography and accessible abstract | supports | Base protocol remains abstract-only. Publisher/PubMed bibliography contradicts the citing paper's volume/pages and incomplete author list; verified source metadata retained, conflict documented. Background strain outcomes do not become CgC targets. |
| pubmed-11092847 | PMID:11092847; references_cache/papers/PMID_11092847.xml; Title, authors, year, ArticleIdList and notices | supports | Publication identity verified. No notice in the archived PubMed entry; not an exhaustive correction/retraction audit. |
| pubmed-10809686 | PMID:10809686; references_cache/papers/PMID_10809686.xml; Title, authors, year, ArticleIdList and notices | supports | Publication identity verified. No notice in the archived PubMed entry; not an exhaustive correction/retraction audit. |
| pubmed-4604283 | PMID:4604283; references_cache/papers/PMID_4604283.xml; Title, authors, year, ArticleIdList and notices | supports | Publication identity verified. No notice in the archived PubMed entry; not an exhaustive correction/retraction audit. |
| pubmed-1369320 | PMID:1369320; references_cache/papers/PMID_1369320.xml; Title, authors, year, ArticleIdList and notices | supports | Publication identity verified. No notice in the archived PubMed entry; not an exhaustive correction/retraction audit. |
| taxonomy-main | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1403831,668369,196627,562,1718&amp;retmode=xml; references_cache/papers/taxonomy/nmm-cgc-20261013.xml; TaxId, ScientificName, Rank, synonyms and lineage | supports | MC4100 actual rank is no rank, DH5alpha and C. glutamicum ATCC13032 ranks are strain; species parents support qualified background mappings, not growth. |
| taxonomy-background | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=83333,90371&amp;retmode=xml; references_cache/papers/taxonomy/nmm-cgc-background-20261013.xml; TaxId, ScientificName, Rank, synonyms and lineage | supports | E. coli K-12 is strain rank; historical Salmonella typhimurium maps to the current serovar node at no rank. Derivatives retain explicit parent-only qualifications. |
| taxonomy-additional | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1247,1423&amp;retmode=xml; references_cache/papers/taxonomy/nmm-cgc-additional-20261013.xml; TaxId, ScientificName, Rank, synonyms and lineage | supports | Leuconostoc oenos is a verified synonym of Oenococcus oeni. Bacillus subtilis is species-rank. Both are background only; bounded exact-strain searches do not prove node absence. |
| joins | MediaDB SQL 07Oct2015; references_cache/papers/mediadb/media_database.07Oct2015.sql; Sources 54/95 and nine exact owner joins frozen in preflight.json | supports | Discovery provenance only, not primary proof of imported concentrations or growth outcomes. |
| claims | Guarded citation curation receipt; reports/paper_citation_curation/20261013-nmm-cgc-citations/claim-plan.json; claim-plan.json | context_only | Twenty registered exact excerpts with assay locators and nine taxonomy records. |
| archives | Guarded citation curation receipt; reports/paper_citation_curation/20261013-nmm-cgc-citations/source-preparation.json; source-preparation.json | context_only | 39 hashed archives; all four cited papers have raw content or abstract and attributable Markdown, with source-access limits explicit. |
| readback | Guarded citation curation receipt; reports/paper_citation_curation/20261013-nmm-cgc-citations/final-readback.json; final-readback.json | context_only | All 15,910 normalized hashes checked; exactly nine expected edits. All 100 parent ingredients and original bytes preserved; 18 citations, four variants, three variant-only growth entries. |
| evidence-readback | Guarded citation curation receipt; reports/paper_citation_curation/20261013-nmm-cgc-citations/evidence-readback.json; evidence-readback.json | context_only | Seven evidence items, 105 additional exact excerpts and 20 registered quotes checked against primary text. This does not waive failed native checks. |
| plan | Guarded citation curation receipt; reports/paper_citation_curation/20261013-nmm-cgc-citations/applied.json; applied.json | context_only | Guarded applied additions match the preview. No parent amounts, preparation, quantitative metrics or generic parent growth added. |
| exporter | Current KGX exporter; src/culturemech/export/kgx_export.py; organism_grows_in_medium_edge and target_organisms export loop | context_only | Exporter ignores scoped_to_variant and would target the parent. No graph or page publication performed. |
| schema | Current CultureMech schema; src/culturemech/schema/culturemech.yaml; OrganismDescriptor.preferred_term identifier and inline MediaVariant slots | context_only | Repeated same-organism entries cannot independently encode two inline growth scopes under the current identifier contract. Figure 1 observation retained in variant evidence/notes without inventing a second name. |
| baseline-00 | reports/paper_citation_curation/20261013-lab-citations/next-baseline-00.log; reports/paper_citation_curation/20261013-lab-citations/next-baseline-00.log; Complete command output | context_only | Actual exit code 0; not scientific certification. |
| baseline-01 | reports/paper_citation_curation/20261013-lab-citations/next-baseline-01.log; reports/paper_citation_curation/20261013-lab-citations/next-baseline-01.log; Complete command output | context_only | Actual exit code 0; not scientific certification. |
| baseline-02 | reports/paper_citation_curation/20261013-lab-citations/next-baseline-02.log; reports/paper_citation_curation/20261013-lab-citations/next-baseline-02.log; Complete command output | context_only | Actual exit code 0; not scientific certification. |
| baseline-03 | reports/paper_citation_curation/20261013-lab-citations/next-baseline-03.log; reports/paper_citation_curation/20261013-lab-citations/next-baseline-03.log; Complete command output | context_only | Actual exit code 0; not scientific certification. |
| baseline-04 | reports/paper_citation_curation/20261013-lab-citations/next-baseline-04.log; reports/paper_citation_curation/20261013-lab-citations/next-baseline-04.log; Complete command output | context_only | Actual exit code 0; not scientific certification. |
| baseline-05 | reports/paper_citation_curation/20261013-lab-citations/next-baseline-05.log; reports/paper_citation_curation/20261013-lab-citations/next-baseline-05.log; Complete command output | context_only | Actual exit code 0; not scientific certification. |
| baseline-06 | reports/paper_citation_curation/20261013-lab-citations/next-baseline-06.log; reports/paper_citation_curation/20261013-lab-citations/next-baseline-06.log; Complete command output | context_only | Actual exit code 0; not scientific certification. |
| baseline-07 | reports/paper_citation_curation/20261013-lab-citations/next-baseline-07.log; reports/paper_citation_curation/20261013-lab-citations/next-baseline-07.log; Complete command output | context_only | Actual exit code 0; not scientific certification. |
| baseline-08 | reports/paper_citation_curation/20261013-lab-citations/next-baseline-08.log; reports/paper_citation_curation/20261013-lab-citations/next-baseline-08.log; Complete command output | context_only | Actual exit code 0; not scientific certification. |
| baseline-09 | reports/paper_citation_curation/20261013-lab-citations/next-baseline-09.log; reports/paper_citation_curation/20261013-lab-citations/next-baseline-09.log; Complete command output | context_only | Actual exit code 0; not scientific certification. |
| baseline-10 | reports/paper_citation_curation/20261013-lab-citations/next-baseline-10.log; reports/paper_citation_curation/20261013-lab-citations/next-baseline-10.log; Complete command output | context_only | Actual exit code 0; not scientific certification. |
| baseline-11 | reports/paper_citation_curation/20261013-lab-citations/next-baseline-11.log; reports/paper_citation_curation/20261013-lab-citations/next-baseline-11.log; Complete command output | context_only | Actual exit code 0; not scientific certification. |
| baseline-12 | reports/paper_citation_curation/20261013-lab-citations/next-baseline-12.log; reports/paper_citation_curation/20261013-lab-citations/next-baseline-12.log; Complete command output | context_only | Actual exit code 0; not scientific certification. |
| baseline-13 | reports/paper_citation_curation/20261013-lab-citations/next-baseline-13.log; reports/paper_citation_curation/20261013-lab-citations/next-baseline-13.log; Complete command output | context_only | Actual exit code 0; not scientific certification. |
| baseline-14 | reports/paper_citation_curation/20261013-lab-citations/next-baseline-14.log; reports/paper_citation_curation/20261013-lab-citations/next-baseline-14.log; Complete command output | context_only | Actual exit code 0; not scientific certification. |
| baseline-15 | reports/paper_citation_curation/20261013-lab-citations/next-baseline-15.log; reports/paper_citation_curation/20261013-lab-citations/next-baseline-15.log; Complete command output | context_only | Actual exit code 0; not scientific certification. |
| baseline-16 | reports/paper_citation_curation/20261013-lab-citations/next-baseline-16.log; reports/paper_citation_curation/20261013-lab-citations/next-baseline-16.log; Complete command output | context_only | Actual exit code 0; not scientific certification. |
| baseline-17 | reports/paper_citation_curation/20261013-lab-citations/next-baseline-17.log; reports/paper_citation_curation/20261013-lab-citations/next-baseline-17.log; Complete command output | context_only | Actual exit code 0; not scientific certification. |
| post-00 | reports/paper_citation_curation/20261013-nmm-cgc-citations/post-00.log; reports/paper_citation_curation/20261013-nmm-cgc-citations/post-00.log; Complete command output | context_only | Actual exit code 1; not scientific certification. |
| post-01 | reports/paper_citation_curation/20261013-nmm-cgc-citations/post-01.log; reports/paper_citation_curation/20261013-nmm-cgc-citations/post-01.log; Complete command output | context_only | Actual exit code 0; not scientific certification. |
| post-02 | reports/paper_citation_curation/20261013-nmm-cgc-citations/post-02.log; reports/paper_citation_curation/20261013-nmm-cgc-citations/post-02.log; Complete command output | context_only | Actual exit code 1; not scientific certification. |
| post-03 | reports/paper_citation_curation/20261013-nmm-cgc-citations/post-03.log; reports/paper_citation_curation/20261013-nmm-cgc-citations/post-03.log; Complete command output | context_only | Actual exit code 0; not scientific certification. |
| post-04 | reports/paper_citation_curation/20261013-nmm-cgc-citations/post-04.log; reports/paper_citation_curation/20261013-nmm-cgc-citations/post-04.log; Complete command output | context_only | Actual exit code 1; not scientific certification. |
| post-05 | reports/paper_citation_curation/20261013-nmm-cgc-citations/post-05.log; reports/paper_citation_curation/20261013-nmm-cgc-citations/post-05.log; Complete command output | context_only | Actual exit code 0; not scientific certification. |
| post-06 | reports/paper_citation_curation/20261013-nmm-cgc-citations/post-06.log; reports/paper_citation_curation/20261013-nmm-cgc-citations/post-06.log; Complete command output | context_only | Actual exit code 1; not scientific certification. |
| post-07 | reports/paper_citation_curation/20261013-nmm-cgc-citations/post-07.log; reports/paper_citation_curation/20261013-nmm-cgc-citations/post-07.log; Complete command output | context_only | Actual exit code 0; not scientific certification. |
| post-08 | reports/paper_citation_curation/20261013-nmm-cgc-citations/post-08.log; reports/paper_citation_curation/20261013-nmm-cgc-citations/post-08.log; Complete command output | context_only | Actual exit code 1; not scientific certification. |
| post-09 | reports/paper_citation_curation/20261013-nmm-cgc-citations/post-09.log; reports/paper_citation_curation/20261013-nmm-cgc-citations/post-09.log; Complete command output | context_only | Actual exit code 0; not scientific certification. |
| post-10 | reports/paper_citation_curation/20261013-nmm-cgc-citations/post-10.log; reports/paper_citation_curation/20261013-nmm-cgc-citations/post-10.log; Complete command output | context_only | Actual exit code 1; not scientific certification. |
| post-11 | reports/paper_citation_curation/20261013-nmm-cgc-citations/post-11.log; reports/paper_citation_curation/20261013-nmm-cgc-citations/post-11.log; Complete command output | context_only | Actual exit code 0; not scientific certification. |
| post-12 | reports/paper_citation_curation/20261013-nmm-cgc-citations/post-12.log; reports/paper_citation_curation/20261013-nmm-cgc-citations/post-12.log; Complete command output | context_only | Actual exit code 1; not scientific certification. |
| post-13 | reports/paper_citation_curation/20261013-nmm-cgc-citations/post-13.log; reports/paper_citation_curation/20261013-nmm-cgc-citations/post-13.log; Complete command output | context_only | Actual exit code 0; not scientific certification. |
| post-14 | reports/paper_citation_curation/20261013-nmm-cgc-citations/post-14.log; reports/paper_citation_curation/20261013-nmm-cgc-citations/post-14.log; Complete command output | context_only | Actual exit code 1; not scientific certification. |
| post-15 | reports/paper_citation_curation/20261013-nmm-cgc-citations/post-15.log; reports/paper_citation_curation/20261013-nmm-cgc-citations/post-15.log; Complete command output | context_only | Actual exit code 0; not scientific certification. |
| post-16 | reports/paper_citation_curation/20261013-nmm-cgc-citations/post-16.log; reports/paper_citation_curation/20261013-nmm-cgc-citations/post-16.log; Complete command output | context_only | Actual exit code 1; not scientific certification. |
| post-17 | reports/paper_citation_curation/20261013-nmm-cgc-citations/post-17.log; reports/paper_citation_curation/20261013-nmm-cgc-citations/post-17.log; Complete command output | context_only | Actual exit code 0; not scientific certification. |
| merge-00 | reports/paper_citation_curation/20261013-nmm-cgc-citations/merge-00.log; reports/paper_citation_curation/20261013-nmm-cgc-citations/merge-00.log; Complete command output | context_only | Actual exit code 1; not scientific certification. |
| merge-01 | reports/paper_citation_curation/20261013-nmm-cgc-citations/merge-01.log; reports/paper_citation_curation/20261013-nmm-cgc-citations/merge-01.log; Complete command output | context_only | Actual exit code 1; not scientific certification. |
| extra-00 | reports/paper_citation_curation/20261013-nmm-cgc-citations/extra-00.log; reports/paper_citation_curation/20261013-nmm-cgc-citations/extra-00.log; Complete command output | context_only | Actual exit code 0; not scientific certification. |
| extra-01 | reports/paper_citation_curation/20261013-nmm-cgc-citations/extra-01.log; reports/paper_citation_curation/20261013-nmm-cgc-citations/extra-01.log; Complete command output | context_only | Actual exit code 0; not scientific certification. |
| extra-02 | reports/paper_citation_curation/20261013-nmm-cgc-citations/extra-02.log; reports/paper_citation_curation/20261013-nmm-cgc-citations/extra-02.log; Complete command output | context_only | Actual exit code 0; not scientific certification. |

## Limits And Additional Notes

- Focused scientific self-review only; all 100 parent amounts enumerated as preserved, not newly verified.
- NMM source wild-type growth does not resolve exact parent formulation; no positive native growth entry added.
- CgC Table 2 tracer cultures, unlabeled controls, Figure 1 mixture and mutant assays remain distinct.
- Neidhardt and Eikmanns base protocols are abstract-only; no complete formulation inherited from them.
- Mass/molar, chemical-form, enrichment and citing-bibliography conflicts remain explicit.
- Taxonomy includes actual rank, reported strain, background role and parent-only qualifications; taxonomy alone is not cultivation evidence.
- Required reference failures and global merge diagnostics are not waived. No generated publication or status promotion.
- 286 MediaDB candidate source-owner links remain; the queue is not an exhaustive literature inventory.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T115530Z-nmm-cgc-paper-citations
kind: batch
repository: culturebotai/CultureMech
title: NMM/CgC paper citations, isotope variants and bounded organism evidence
started_at: '2026-10-13T11:09:31Z'
finished_at: '2026-10-13T11:55:30Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: The curator performed this assessment; no independent scientific
    review claimed.
skill: culturemech-add-paper-citation
completion: partial
verdict: needs_curation
scientific_review: true
summary: 18 paper-record citations across nine owners/four publications. Four inline
  CgC variants and three DOI/snippet-backed variant-only growth entries; six NMM owners
  receive bibliography and qualified unresolved notes. All 100 parent ingredients
  preserved. Nine strict/schema/term checks pass; nine reference checks and 2 global
  merge diagnostics fail.
source:
  git_revision: 41d4d390123c0d8320cd53e994470c88a1b86d8c
  state: working_tree
  inputs:
  - path: data/normalized_yaml/bacterial/cgc_w_acetate.yaml
    sha256: 03e61bf2717255009095abe870544fa50dcb260d86590b8496b615bb49d55675
    role: target
  - path: data/normalized_yaml/bacterial/cgc_w_acetate_glucose.yaml
    sha256: 800dab9329a224f8661d30d9f80402db4702a9cf69d5102b69bd1a6f540cb537
    role: target
  - path: data/normalized_yaml/bacterial/cgc_w_glucose.yaml
    sha256: 406ca920b05bb55070d44c5912bad0772f8c64fb5ba790cd4cf65c960f3214b2
    role: target
  - path: data/normalized_yaml/bacterial/nmm_with_acetate.yaml
    sha256: b421e26edf6ba19b6c924b7fb8f59014b2796c1fa61877d98cfdcae33cbce738
    role: target
  - path: data/normalized_yaml/bacterial/nmm_with_glucose.yaml
    sha256: 8b60c7312005b9e618d42b4b0cc8e3b94b0a0a53e7ac58cff7cc02520ee8e213
    role: target
  - path: data/normalized_yaml/bacterial/nmm_with_lactate.yaml
    sha256: 02cdb78dda9b3698ead62b6ca1f431e01ea81cdd30172399f798731b681b7694
    role: target
  - path: data/normalized_yaml/bacterial/nmm_with_malate.yaml
    sha256: 8505ebf958b13eef8f9de573e717bbc34e8bd7ce343b24c3164da63785c0eeeb
    role: target
  - path: data/normalized_yaml/bacterial/nmm_with_pyruvate.yaml
    sha256: 8869d187c1315645eb396df49161ef96f51981ee53f381df04794f72f257647d
    role: target
  - path: data/normalized_yaml/bacterial/nmm_with_succinate.yaml
    sha256: 8752bd119362111a6d2d72c371d18b16586fa572a6076301df036e3cf58c664c
    role: target
  - path: src/culturemech/export/kgx_export.py
    sha256: eacbc2e7b363488cc1ed96e91737f54244dc1a2425dfa05c77ba89d0a5cd10e0
    role: context
  - path: src/culturemech/schema/culturemech.yaml
    sha256: cb8e4b047647d41f47b91d83420799555c09696c8a2a890535a74076e6f8bba6
    role: context
scope:
  description: Exact nine MediaDB source 54/95 normalized owners; focused citation,
    formulation-difference and organism-evidence review.
  selection: Exact source-owner joins, not a corpus sample or full recipe review.
  coverage: full
  population_size: 9
  reviewed_target_ids:
  - CultureMech:007045
  - CultureMech:007046
  - CultureMech:007047
  - CultureMech:007048
  - CultureMech:007049
  - CultureMech:007051
  - CultureMech:007184
  - CultureMech:007185
  - CultureMech:007186
  exclusions:
  - target: Full parent concentration certification, unseen base-protocol bodies,
      all-paper organism inventory, quantitative growth and generated publication
    reason: Not established by inspected evidence or authorized by this focused citation
      task.
targets:
- target_id: CultureMech:007045
  path: data/normalized_yaml/bacterial/nmm_with_glucose.yaml
  label: nmm_with_glucose
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/nmm_with_glucose.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007046
  path: data/normalized_yaml/bacterial/nmm_with_pyruvate.yaml
  label: nmm_with_pyruvate
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/nmm_with_pyruvate.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007047
  path: data/normalized_yaml/bacterial/nmm_with_lactate.yaml
  label: nmm_with_lactate
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/nmm_with_lactate.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007048
  path: data/normalized_yaml/bacterial/nmm_with_malate.yaml
  label: nmm_with_malate
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/nmm_with_malate.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007049
  path: data/normalized_yaml/bacterial/nmm_with_succinate.yaml
  label: nmm_with_succinate
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/nmm_with_succinate.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007051
  path: data/normalized_yaml/bacterial/nmm_with_acetate.yaml
  label: nmm_with_acetate
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/nmm_with_acetate.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007184
  path: data/normalized_yaml/bacterial/cgc_w_acetate.yaml
  label: cgc_w_acetate
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/cgc_w_acetate.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007185
  path: data/normalized_yaml/bacterial/cgc_w_acetate_glucose.yaml
  label: cgc_w_acetate_glucose
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/cgc_w_acetate_glucose.yaml
    role: authoritative normalized recipe
- target_id: CultureMech:007186
  path: data/normalized_yaml/bacterial/cgc_w_glucose.yaml
  label: cgc_w_glucose
  kind: maintained
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/cgc_w_glucose.yaml
    role: authoritative normalized recipe
checks:
- check_id: baseline-00
  name: just validate data/normalized_yaml/bacterial/nmm_with_glucose.yaml
  command: just validate data/normalized_yaml/bacterial/nmm_with_glucose.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Baseline retained after exact input hashes verified.
  target_ids:
  - CultureMech:007045
  evidence_ids:
  - baseline-00
- check_id: baseline-01
  name: just validate-strict data/normalized_yaml/bacterial/nmm_with_glucose.yaml
  command: just validate-strict data/normalized_yaml/bacterial/nmm_with_glucose.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Baseline retained after exact input hashes verified.
  target_ids:
  - CultureMech:007045
  evidence_ids:
  - baseline-01
- check_id: baseline-02
  name: just validate data/normalized_yaml/bacterial/nmm_with_pyruvate.yaml
  command: just validate data/normalized_yaml/bacterial/nmm_with_pyruvate.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Baseline retained after exact input hashes verified.
  target_ids:
  - CultureMech:007046
  evidence_ids:
  - baseline-02
- check_id: baseline-03
  name: just validate-strict data/normalized_yaml/bacterial/nmm_with_pyruvate.yaml
  command: just validate-strict data/normalized_yaml/bacterial/nmm_with_pyruvate.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Baseline retained after exact input hashes verified.
  target_ids:
  - CultureMech:007046
  evidence_ids:
  - baseline-03
- check_id: baseline-04
  name: just validate data/normalized_yaml/bacterial/nmm_with_lactate.yaml
  command: just validate data/normalized_yaml/bacterial/nmm_with_lactate.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Baseline retained after exact input hashes verified.
  target_ids:
  - CultureMech:007047
  evidence_ids:
  - baseline-04
- check_id: baseline-05
  name: just validate-strict data/normalized_yaml/bacterial/nmm_with_lactate.yaml
  command: just validate-strict data/normalized_yaml/bacterial/nmm_with_lactate.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Baseline retained after exact input hashes verified.
  target_ids:
  - CultureMech:007047
  evidence_ids:
  - baseline-05
- check_id: baseline-06
  name: just validate data/normalized_yaml/bacterial/nmm_with_malate.yaml
  command: just validate data/normalized_yaml/bacterial/nmm_with_malate.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Baseline retained after exact input hashes verified.
  target_ids:
  - CultureMech:007048
  evidence_ids:
  - baseline-06
- check_id: baseline-07
  name: just validate-strict data/normalized_yaml/bacterial/nmm_with_malate.yaml
  command: just validate-strict data/normalized_yaml/bacterial/nmm_with_malate.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Baseline retained after exact input hashes verified.
  target_ids:
  - CultureMech:007048
  evidence_ids:
  - baseline-07
- check_id: baseline-08
  name: just validate data/normalized_yaml/bacterial/nmm_with_succinate.yaml
  command: just validate data/normalized_yaml/bacterial/nmm_with_succinate.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Baseline retained after exact input hashes verified.
  target_ids:
  - CultureMech:007049
  evidence_ids:
  - baseline-08
- check_id: baseline-09
  name: just validate-strict data/normalized_yaml/bacterial/nmm_with_succinate.yaml
  command: just validate-strict data/normalized_yaml/bacterial/nmm_with_succinate.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Baseline retained after exact input hashes verified.
  target_ids:
  - CultureMech:007049
  evidence_ids:
  - baseline-09
- check_id: baseline-10
  name: just validate data/normalized_yaml/bacterial/nmm_with_acetate.yaml
  command: just validate data/normalized_yaml/bacterial/nmm_with_acetate.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Baseline retained after exact input hashes verified.
  target_ids:
  - CultureMech:007051
  evidence_ids:
  - baseline-10
- check_id: baseline-11
  name: just validate-strict data/normalized_yaml/bacterial/nmm_with_acetate.yaml
  command: just validate-strict data/normalized_yaml/bacterial/nmm_with_acetate.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Baseline retained after exact input hashes verified.
  target_ids:
  - CultureMech:007051
  evidence_ids:
  - baseline-11
- check_id: baseline-12
  name: just validate data/normalized_yaml/bacterial/cgc_w_acetate.yaml
  command: just validate data/normalized_yaml/bacterial/cgc_w_acetate.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Baseline retained after exact input hashes verified.
  target_ids:
  - CultureMech:007184
  evidence_ids:
  - baseline-12
- check_id: baseline-13
  name: just validate-strict data/normalized_yaml/bacterial/cgc_w_acetate.yaml
  command: just validate-strict data/normalized_yaml/bacterial/cgc_w_acetate.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Baseline retained after exact input hashes verified.
  target_ids:
  - CultureMech:007184
  evidence_ids:
  - baseline-13
- check_id: baseline-14
  name: just validate data/normalized_yaml/bacterial/cgc_w_acetate_glucose.yaml
  command: just validate data/normalized_yaml/bacterial/cgc_w_acetate_glucose.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Baseline retained after exact input hashes verified.
  target_ids:
  - CultureMech:007185
  evidence_ids:
  - baseline-14
- check_id: baseline-15
  name: just validate-strict data/normalized_yaml/bacterial/cgc_w_acetate_glucose.yaml
  command: just validate-strict data/normalized_yaml/bacterial/cgc_w_acetate_glucose.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Baseline retained after exact input hashes verified.
  target_ids:
  - CultureMech:007185
  evidence_ids:
  - baseline-15
- check_id: baseline-16
  name: just validate data/normalized_yaml/bacterial/cgc_w_glucose.yaml
  command: just validate data/normalized_yaml/bacterial/cgc_w_glucose.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Baseline retained after exact input hashes verified.
  target_ids:
  - CultureMech:007186
  evidence_ids:
  - baseline-16
- check_id: baseline-17
  name: just validate-strict data/normalized_yaml/bacterial/cgc_w_glucose.yaml
  command: just validate-strict data/normalized_yaml/bacterial/cgc_w_glucose.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Baseline retained after exact input hashes verified.
  target_ids:
  - CultureMech:007186
  evidence_ids:
  - baseline-17
- check_id: post-00
  name: just validate data/normalized_yaml/bacterial/nmm_with_glucose.yaml
  command: just validate data/normalized_yaml/bacterial/nmm_with_glucose.yaml
  status: failed
  required: true
  exit_code: 1
  summary: Schema and terms pass; reference checks fail on title formatting and, for
    CgC, abstract-only retrieval of full-text excerpts.
  target_ids:
  - CultureMech:007045
  evidence_ids:
  - post-00
- check_id: post-01
  name: just validate-strict data/normalized_yaml/bacterial/nmm_with_glucose.yaml
  command: just validate-strict data/normalized_yaml/bacterial/nmm_with_glucose.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Actual maintained check result.
  target_ids:
  - CultureMech:007045
  evidence_ids:
  - post-01
- check_id: post-02
  name: just validate data/normalized_yaml/bacterial/nmm_with_pyruvate.yaml
  command: just validate data/normalized_yaml/bacterial/nmm_with_pyruvate.yaml
  status: failed
  required: true
  exit_code: 1
  summary: Schema and terms pass; reference checks fail on title formatting and, for
    CgC, abstract-only retrieval of full-text excerpts.
  target_ids:
  - CultureMech:007046
  evidence_ids:
  - post-02
- check_id: post-03
  name: just validate-strict data/normalized_yaml/bacterial/nmm_with_pyruvate.yaml
  command: just validate-strict data/normalized_yaml/bacterial/nmm_with_pyruvate.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Actual maintained check result.
  target_ids:
  - CultureMech:007046
  evidence_ids:
  - post-03
- check_id: post-04
  name: just validate data/normalized_yaml/bacterial/nmm_with_lactate.yaml
  command: just validate data/normalized_yaml/bacterial/nmm_with_lactate.yaml
  status: failed
  required: true
  exit_code: 1
  summary: Schema and terms pass; reference checks fail on title formatting and, for
    CgC, abstract-only retrieval of full-text excerpts.
  target_ids:
  - CultureMech:007047
  evidence_ids:
  - post-04
- check_id: post-05
  name: just validate-strict data/normalized_yaml/bacterial/nmm_with_lactate.yaml
  command: just validate-strict data/normalized_yaml/bacterial/nmm_with_lactate.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Actual maintained check result.
  target_ids:
  - CultureMech:007047
  evidence_ids:
  - post-05
- check_id: post-06
  name: just validate data/normalized_yaml/bacterial/nmm_with_malate.yaml
  command: just validate data/normalized_yaml/bacterial/nmm_with_malate.yaml
  status: failed
  required: true
  exit_code: 1
  summary: Schema and terms pass; reference checks fail on title formatting and, for
    CgC, abstract-only retrieval of full-text excerpts.
  target_ids:
  - CultureMech:007048
  evidence_ids:
  - post-06
- check_id: post-07
  name: just validate-strict data/normalized_yaml/bacterial/nmm_with_malate.yaml
  command: just validate-strict data/normalized_yaml/bacterial/nmm_with_malate.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Actual maintained check result.
  target_ids:
  - CultureMech:007048
  evidence_ids:
  - post-07
- check_id: post-08
  name: just validate data/normalized_yaml/bacterial/nmm_with_succinate.yaml
  command: just validate data/normalized_yaml/bacterial/nmm_with_succinate.yaml
  status: failed
  required: true
  exit_code: 1
  summary: Schema and terms pass; reference checks fail on title formatting and, for
    CgC, abstract-only retrieval of full-text excerpts.
  target_ids:
  - CultureMech:007049
  evidence_ids:
  - post-08
- check_id: post-09
  name: just validate-strict data/normalized_yaml/bacterial/nmm_with_succinate.yaml
  command: just validate-strict data/normalized_yaml/bacterial/nmm_with_succinate.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Actual maintained check result.
  target_ids:
  - CultureMech:007049
  evidence_ids:
  - post-09
- check_id: post-10
  name: just validate data/normalized_yaml/bacterial/nmm_with_acetate.yaml
  command: just validate data/normalized_yaml/bacterial/nmm_with_acetate.yaml
  status: failed
  required: true
  exit_code: 1
  summary: Schema and terms pass; reference checks fail on title formatting and, for
    CgC, abstract-only retrieval of full-text excerpts.
  target_ids:
  - CultureMech:007051
  evidence_ids:
  - post-10
- check_id: post-11
  name: just validate-strict data/normalized_yaml/bacterial/nmm_with_acetate.yaml
  command: just validate-strict data/normalized_yaml/bacterial/nmm_with_acetate.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Actual maintained check result.
  target_ids:
  - CultureMech:007051
  evidence_ids:
  - post-11
- check_id: post-12
  name: just validate data/normalized_yaml/bacterial/cgc_w_acetate.yaml
  command: just validate data/normalized_yaml/bacterial/cgc_w_acetate.yaml
  status: failed
  required: true
  exit_code: 1
  summary: Schema and terms pass; reference checks fail on title formatting and, for
    CgC, abstract-only retrieval of full-text excerpts.
  target_ids:
  - CultureMech:007184
  evidence_ids:
  - post-12
- check_id: post-13
  name: just validate-strict data/normalized_yaml/bacterial/cgc_w_acetate.yaml
  command: just validate-strict data/normalized_yaml/bacterial/cgc_w_acetate.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Actual maintained check result.
  target_ids:
  - CultureMech:007184
  evidence_ids:
  - post-13
- check_id: post-14
  name: just validate data/normalized_yaml/bacterial/cgc_w_acetate_glucose.yaml
  command: just validate data/normalized_yaml/bacterial/cgc_w_acetate_glucose.yaml
  status: failed
  required: true
  exit_code: 1
  summary: Schema and terms pass; reference checks fail on title formatting and, for
    CgC, abstract-only retrieval of full-text excerpts.
  target_ids:
  - CultureMech:007185
  evidence_ids:
  - post-14
- check_id: post-15
  name: just validate-strict data/normalized_yaml/bacterial/cgc_w_acetate_glucose.yaml
  command: just validate-strict data/normalized_yaml/bacterial/cgc_w_acetate_glucose.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Actual maintained check result.
  target_ids:
  - CultureMech:007185
  evidence_ids:
  - post-15
- check_id: post-16
  name: just validate data/normalized_yaml/bacterial/cgc_w_glucose.yaml
  command: just validate data/normalized_yaml/bacterial/cgc_w_glucose.yaml
  status: failed
  required: true
  exit_code: 1
  summary: Schema and terms pass; reference checks fail on title formatting and, for
    CgC, abstract-only retrieval of full-text excerpts.
  target_ids:
  - CultureMech:007186
  evidence_ids:
  - post-16
- check_id: post-17
  name: just validate-strict data/normalized_yaml/bacterial/cgc_w_glucose.yaml
  command: just validate-strict data/normalized_yaml/bacterial/cgc_w_glucose.yaml
  status: passed
  required: true
  exit_code: 0
  summary: Actual maintained check result.
  target_ids:
  - CultureMech:007186
  evidence_ids:
  - post-17
- check_id: merge-00
  name: just verify-merges
  command: just verify-merges
  status: failed
  required: true
  exit_code: 1
  summary: Required global merge diagnostic; checked-in generated output unchanged.
  target_ids:
  - CultureMech:007045
  - CultureMech:007046
  - CultureMech:007047
  - CultureMech:007048
  - CultureMech:007049
  - CultureMech:007051
  - CultureMech:007184
  - CultureMech:007185
  - CultureMech:007186
  evidence_ids:
  - merge-00
- check_id: merge-01
  name: just audit-merge-freshness --json
  command: just audit-merge-freshness --json
  status: failed
  required: true
  exit_code: 1
  summary: Required global merge diagnostic; checked-in generated output unchanged.
  target_ids:
  - CultureMech:007045
  - CultureMech:007046
  - CultureMech:007047
  - CultureMech:007048
  - CultureMech:007049
  - CultureMech:007051
  - CultureMech:007184
  - CultureMech:007185
  - CultureMech:007186
  evidence_ids:
  - merge-01
- check_id: extra-00
  name: /tmp/culturemech-parallel-env-20261012/bin/python -m pytest --no-cov -q -p
    no:cacheprovider tests/test_claude_skills.py tests/test_skill_frontmatter.py tests/test_fetch_pubmed_abstracts.py
    tests/test_record_io.py tests/test_media_variant_links.py tests/test_record_review_contract.py
  command: /tmp/culturemech-parallel-env-20261012/bin/python -m pytest --no-cov -q
    -p no:cacheprovider tests/test_claude_skills.py tests/test_skill_frontmatter.py
    tests/test_fetch_pubmed_abstracts.py tests/test_record_io.py tests/test_media_variant_links.py
    tests/test_record_review_contract.py
  status: passed
  required: true
  exit_code: 0
  summary: Actual maintained check result.
  target_ids:
  - CultureMech:007045
  - CultureMech:007046
  - CultureMech:007047
  - CultureMech:007048
  - CultureMech:007049
  - CultureMech:007051
  - CultureMech:007184
  - CultureMech:007185
  - CultureMech:007186
  evidence_ids:
  - extra-00
- check_id: extra-01
  name: /tmp/culturemech-parallel-env-20261012/bin/python scripts/validate_claude_skills.py
  command: /tmp/culturemech-parallel-env-20261012/bin/python scripts/validate_claude_skills.py
  status: passed
  required: true
  exit_code: 0
  summary: Actual maintained check result.
  target_ids:
  - CultureMech:007045
  - CultureMech:007046
  - CultureMech:007047
  - CultureMech:007048
  - CultureMech:007049
  - CultureMech:007051
  - CultureMech:007184
  - CultureMech:007185
  - CultureMech:007186
  evidence_ids:
  - extra-01
- check_id: extra-02
  name: git diff --check
  command: git diff --check
  status: passed
  required: true
  exit_code: 0
  summary: Actual maintained check result.
  target_ids:
  - CultureMech:007045
  - CultureMech:007046
  - CultureMech:007047
  - CultureMech:007048
  - CultureMech:007049
  - CultureMech:007051
  - CultureMech:007184
  - CultureMech:007185
  - CultureMech:007186
  evidence_ids:
  - extra-02
evidence:
- evidence_id: vanderrest
  kind: primary_source
  reference: doi:10.1128/JB.182.24.6892-6899.2000
  locator: references_cache/papers/primary_html/vanderrest-2000-pmc.html; Methods;
    Figures 2/3; Tables 3/4; Results and Discussion
  accessed_at: '2026-10-13T11:55:30Z'
  summary: NMM carbon mass doses and wild-type growth are explicit, but correspondence
    to each imported molar chemical form and the complete base remains unresolved.
    Mutants, plasmid induction, plate assays, mixed competition and enzyme-assay reagents
    are kept distinct.
  support: supports
  snapshot_sha256: 3b1d38a6f8c180f93d4e3c29fc5f9dee060a126b7f7c8f2241d06307af283901
- evidence_id: wendisch
  kind: primary_source
  reference: doi:10.1128/JB.182.11.3088-3096.2000
  locator: references_cache/papers/primary_html/wendisch-2000-pmc.html; Methods; Figure
    1; Table 2 including headings and footnote; isotope-flux discussion
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Three isotope tracer variants have explicit qualitative wild-type growth.
    Figure 1 uses a distinct mixed-carbon concentration and unspecified isotope status.
    Reported mass doses, nominal molar headings and conflicting atom-enrichment statements
    are not silently reconciled.
  support: supports
  snapshot_sha256: 5e492630eec91e8a48c8ce9a27dcfbeffc9b834084418e47bfca7fa29660e53d
- evidence_id: nmm-figure
  kind: primary_source
  reference: doi:10.1128/JB.182.24.6892-6899.2000
  locator: references_cache/papers/primary_images/vanderrest-2000-figure3.jpg; Figure
    3 visually inspected with caption
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Black MC4100 bars support growth on six carbon sources. Mutant bars remain
    separate; no plotted rates were digitized or native parent growth asserted.
  support: supports
  snapshot_sha256: da27bae11c95295557c6fc855cd8818f10791793f8fd7ef3d90c545482a42380
- evidence_id: cgc-figure
  kind: primary_source
  reference: doi:10.1128/JB.182.11.3088-3096.2000
  locator: references_cache/papers/primary_images/wendisch-2000-figure1.jpg; Figure
    1 visually inspected with caption
  accessed_at: '2026-10-13T11:55:30Z'
  summary: WT biomass increases in the distinct concentration experiment. This observation
    stays in variant evidence/notes because one preferred_term cannot encode two independently
    scoped growth entries.
  support: supports
  snapshot_sha256: 41aa9f8a6a11851163cfda22274dd91057f13ec8432a078ffc9443ee05374a88
- evidence_id: neidhardt
  kind: primary_source
  reference: PMID:4604283
  locator: references_cache/papers/primary_xml/neidhardt-1974-pmc-abstract.xml; Abstract
    only; no full scanned body
  accessed_at: '2026-10-13T11:55:30Z'
  summary: The base-protocol abstract names Escherichia coli and Salmonella typhimurium
    but does not enumerate the complete NMM formulation. Bibliography and qualified
    notes only.
  support: supports
  snapshot_sha256: bbb2f6a29e6a71530b6ecb8dab621339e9ff850d44f02779d4b66d5e3a49d8e3
- evidence_id: eikmanns
  kind: primary_source
  reference: doi:10.1007/BF00167910
  locator: references_cache/papers/primary_html/eikmanns-1991-publisher-abstract.html;
    Publisher bibliography and accessible abstract
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Base protocol remains abstract-only. Publisher/PubMed bibliography contradicts
    the citing paper's volume/pages and incomplete author list; verified source metadata
    retained, conflict documented. Background strain outcomes do not become CgC targets.
  support: supports
  snapshot_sha256: d9074dc6fa40d21201ea8046734cac38cb49de249de238271a1f7ee65c006f8c
- evidence_id: pubmed-11092847
  kind: authority
  reference: PMID:11092847
  locator: references_cache/papers/PMID_11092847.xml; Title, authors, year, ArticleIdList
    and notices
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Publication identity verified. No notice in the archived PubMed entry;
    not an exhaustive correction/retraction audit.
  support: supports
  snapshot_sha256: 34f00cc11338ecd81e80e274654f52d12c20ca1800730e21a83b7e907335c863
- evidence_id: pubmed-10809686
  kind: authority
  reference: PMID:10809686
  locator: references_cache/papers/PMID_10809686.xml; Title, authors, year, ArticleIdList
    and notices
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Publication identity verified. No notice in the archived PubMed entry;
    not an exhaustive correction/retraction audit.
  support: supports
  snapshot_sha256: 2371770b52028de05a07225d3c45c04115850384a484bdf0e2af5bde8ae9ca25
- evidence_id: pubmed-4604283
  kind: authority
  reference: PMID:4604283
  locator: references_cache/papers/PMID_4604283.xml; Title, authors, year, ArticleIdList
    and notices
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Publication identity verified. No notice in the archived PubMed entry;
    not an exhaustive correction/retraction audit.
  support: supports
  snapshot_sha256: 4f42df7ad451cb276ad4263724ba3a4e3935f794f3febef93d0b4dc256f1fa46
- evidence_id: pubmed-1369320
  kind: authority
  reference: PMID:1369320
  locator: references_cache/papers/PMID_1369320.xml; Title, authors, year, ArticleIdList
    and notices
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Publication identity verified. No notice in the archived PubMed entry;
    not an exhaustive correction/retraction audit.
  support: supports
  snapshot_sha256: bcf60c17e766eca1b1ffd2b2c619ac5a96059bbbe2496ed92d61c6d5e32bce96
- evidence_id: taxonomy-main
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1403831,668369,196627,562,1718&retmode=xml
  locator: references_cache/papers/taxonomy/nmm-cgc-20261013.xml; TaxId, ScientificName,
    Rank, synonyms and lineage
  accessed_at: '2026-10-13T11:55:30Z'
  summary: MC4100 actual rank is no rank, DH5alpha and C. glutamicum ATCC13032 ranks
    are strain; species parents support qualified background mappings, not growth.
  support: supports
  snapshot_sha256: e2fd2b2c83e1483e3e03de83d1ffb6c987501ac68614a896ad0396c780c2d60f
- evidence_id: taxonomy-background
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=83333,90371&retmode=xml
  locator: references_cache/papers/taxonomy/nmm-cgc-background-20261013.xml; TaxId,
    ScientificName, Rank, synonyms and lineage
  accessed_at: '2026-10-13T11:55:30Z'
  summary: E. coli K-12 is strain rank; historical Salmonella typhimurium maps to
    the current serovar node at no rank. Derivatives retain explicit parent-only qualifications.
  support: supports
  snapshot_sha256: 2ecaf2d2e63f0141b0c3ec1562528354fc155ad7fa5e99acaffd292f99557520
- evidence_id: taxonomy-additional
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1247,1423&retmode=xml
  locator: references_cache/papers/taxonomy/nmm-cgc-additional-20261013.xml; TaxId,
    ScientificName, Rank, synonyms and lineage
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Leuconostoc oenos is a verified synonym of Oenococcus oeni. Bacillus subtilis
    is species-rank. Both are background only; bounded exact-strain searches do not
    prove node absence.
  support: supports
  snapshot_sha256: 94ff76371d9d519ec7912abec33bf0685f77178a899ae69cab67ce1489724cdc
- evidence_id: joins
  kind: database
  reference: MediaDB SQL 07Oct2015
  locator: references_cache/papers/mediadb/media_database.07Oct2015.sql; Sources 54/95
    and nine exact owner joins frozen in preflight.json
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Discovery provenance only, not primary proof of imported concentrations
    or growth outcomes.
  support: supports
  snapshot_sha256: e2c60258e2389d4ad383695eb3e01429a67eac90807fe14d02a6728777d35b5c
- evidence_id: claims
  kind: record_content
  reference: Guarded citation curation receipt
  locator: reports/paper_citation_curation/20261013-nmm-cgc-citations/claim-plan.json;
    claim-plan.json
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Twenty registered exact excerpts with assay locators and nine taxonomy
    records.
  support: context_only
  snapshot_sha256: 60d4bee2ab4502d145303d2d8b3b407bf9f54d6ea0fba101591b5fa23eb640aa
- evidence_id: archives
  kind: record_content
  reference: Guarded citation curation receipt
  locator: reports/paper_citation_curation/20261013-nmm-cgc-citations/source-preparation.json;
    source-preparation.json
  accessed_at: '2026-10-13T11:55:30Z'
  summary: 39 hashed archives; all four cited papers have raw content or abstract
    and attributable Markdown, with source-access limits explicit.
  support: context_only
  snapshot_sha256: fb4410fb1c922716019d05d02ca6ccd63109c044c3a9bb098663b67a6fbdb18a
- evidence_id: readback
  kind: record_content
  reference: Guarded citation curation receipt
  locator: reports/paper_citation_curation/20261013-nmm-cgc-citations/final-readback.json;
    final-readback.json
  accessed_at: '2026-10-13T11:55:30Z'
  summary: All 15,910 normalized hashes checked; exactly nine expected edits. All
    100 parent ingredients and original bytes preserved; 18 citations, four variants,
    three variant-only growth entries.
  support: context_only
  snapshot_sha256: 3f0406d8f77ef796b06c507351293c913b38a4ec98120f5ba020a90e0f98f343
- evidence_id: evidence-readback
  kind: record_content
  reference: Guarded citation curation receipt
  locator: reports/paper_citation_curation/20261013-nmm-cgc-citations/evidence-readback.json;
    evidence-readback.json
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Seven evidence items, 105 additional exact excerpts and 20 registered quotes
    checked against primary text. This does not waive failed native checks.
  support: context_only
  snapshot_sha256: 99a73e27e3e376f8f366692302feb41ab80e791d260bf021447a6d07363561e7
- evidence_id: plan
  kind: record_content
  reference: Guarded citation curation receipt
  locator: reports/paper_citation_curation/20261013-nmm-cgc-citations/applied.json;
    applied.json
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Guarded applied additions match the preview. No parent amounts, preparation,
    quantitative metrics or generic parent growth added.
  support: context_only
  snapshot_sha256: 4ecbefdbe5802951bdc4b9ff64ea91313b3254235e715f47a21fa886528169c0
- evidence_id: exporter
  kind: record_content
  reference: Current KGX exporter
  locator: src/culturemech/export/kgx_export.py; organism_grows_in_medium_edge and
    target_organisms export loop
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Exporter ignores scoped_to_variant and would target the parent. No graph
    or page publication performed.
  support: context_only
  snapshot_sha256: eacbc2e7b363488cc1ed96e91737f54244dc1a2425dfa05c77ba89d0a5cd10e0
- evidence_id: schema
  kind: record_content
  reference: Current CultureMech schema
  locator: src/culturemech/schema/culturemech.yaml; OrganismDescriptor.preferred_term
    identifier and inline MediaVariant slots
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Repeated same-organism entries cannot independently encode two inline growth
    scopes under the current identifier contract. Figure 1 observation retained in
    variant evidence/notes without inventing a second name.
  support: context_only
  snapshot_sha256: cb8e4b047647d41f47b91d83420799555c09696c8a2a890535a74076e6f8bba6
- evidence_id: baseline-00
  kind: validation
  reference: reports/paper_citation_curation/20261013-lab-citations/next-baseline-00.log
  locator: reports/paper_citation_curation/20261013-lab-citations/next-baseline-00.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 0; not scientific certification.
  support: context_only
  snapshot_sha256: 8e85fad3683d76bd6c3fb545f47c457c6d20f0a3795b6abae6b05d87f12134d1
- evidence_id: baseline-01
  kind: validation
  reference: reports/paper_citation_curation/20261013-lab-citations/next-baseline-01.log
  locator: reports/paper_citation_curation/20261013-lab-citations/next-baseline-01.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 0; not scientific certification.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: baseline-02
  kind: validation
  reference: reports/paper_citation_curation/20261013-lab-citations/next-baseline-02.log
  locator: reports/paper_citation_curation/20261013-lab-citations/next-baseline-02.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 0; not scientific certification.
  support: context_only
  snapshot_sha256: 8e85fad3683d76bd6c3fb545f47c457c6d20f0a3795b6abae6b05d87f12134d1
- evidence_id: baseline-03
  kind: validation
  reference: reports/paper_citation_curation/20261013-lab-citations/next-baseline-03.log
  locator: reports/paper_citation_curation/20261013-lab-citations/next-baseline-03.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 0; not scientific certification.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: baseline-04
  kind: validation
  reference: reports/paper_citation_curation/20261013-lab-citations/next-baseline-04.log
  locator: reports/paper_citation_curation/20261013-lab-citations/next-baseline-04.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 0; not scientific certification.
  support: context_only
  snapshot_sha256: 8e85fad3683d76bd6c3fb545f47c457c6d20f0a3795b6abae6b05d87f12134d1
- evidence_id: baseline-05
  kind: validation
  reference: reports/paper_citation_curation/20261013-lab-citations/next-baseline-05.log
  locator: reports/paper_citation_curation/20261013-lab-citations/next-baseline-05.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 0; not scientific certification.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: baseline-06
  kind: validation
  reference: reports/paper_citation_curation/20261013-lab-citations/next-baseline-06.log
  locator: reports/paper_citation_curation/20261013-lab-citations/next-baseline-06.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 0; not scientific certification.
  support: context_only
  snapshot_sha256: 8e85fad3683d76bd6c3fb545f47c457c6d20f0a3795b6abae6b05d87f12134d1
- evidence_id: baseline-07
  kind: validation
  reference: reports/paper_citation_curation/20261013-lab-citations/next-baseline-07.log
  locator: reports/paper_citation_curation/20261013-lab-citations/next-baseline-07.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 0; not scientific certification.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: baseline-08
  kind: validation
  reference: reports/paper_citation_curation/20261013-lab-citations/next-baseline-08.log
  locator: reports/paper_citation_curation/20261013-lab-citations/next-baseline-08.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 0; not scientific certification.
  support: context_only
  snapshot_sha256: 8e85fad3683d76bd6c3fb545f47c457c6d20f0a3795b6abae6b05d87f12134d1
- evidence_id: baseline-09
  kind: validation
  reference: reports/paper_citation_curation/20261013-lab-citations/next-baseline-09.log
  locator: reports/paper_citation_curation/20261013-lab-citations/next-baseline-09.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 0; not scientific certification.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: baseline-10
  kind: validation
  reference: reports/paper_citation_curation/20261013-lab-citations/next-baseline-10.log
  locator: reports/paper_citation_curation/20261013-lab-citations/next-baseline-10.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 0; not scientific certification.
  support: context_only
  snapshot_sha256: 8e85fad3683d76bd6c3fb545f47c457c6d20f0a3795b6abae6b05d87f12134d1
- evidence_id: baseline-11
  kind: validation
  reference: reports/paper_citation_curation/20261013-lab-citations/next-baseline-11.log
  locator: reports/paper_citation_curation/20261013-lab-citations/next-baseline-11.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 0; not scientific certification.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: baseline-12
  kind: validation
  reference: reports/paper_citation_curation/20261013-lab-citations/next-baseline-12.log
  locator: reports/paper_citation_curation/20261013-lab-citations/next-baseline-12.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 0; not scientific certification.
  support: context_only
  snapshot_sha256: 8e85fad3683d76bd6c3fb545f47c457c6d20f0a3795b6abae6b05d87f12134d1
- evidence_id: baseline-13
  kind: validation
  reference: reports/paper_citation_curation/20261013-lab-citations/next-baseline-13.log
  locator: reports/paper_citation_curation/20261013-lab-citations/next-baseline-13.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 0; not scientific certification.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: baseline-14
  kind: validation
  reference: reports/paper_citation_curation/20261013-lab-citations/next-baseline-14.log
  locator: reports/paper_citation_curation/20261013-lab-citations/next-baseline-14.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 0; not scientific certification.
  support: context_only
  snapshot_sha256: 8e85fad3683d76bd6c3fb545f47c457c6d20f0a3795b6abae6b05d87f12134d1
- evidence_id: baseline-15
  kind: validation
  reference: reports/paper_citation_curation/20261013-lab-citations/next-baseline-15.log
  locator: reports/paper_citation_curation/20261013-lab-citations/next-baseline-15.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 0; not scientific certification.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: baseline-16
  kind: validation
  reference: reports/paper_citation_curation/20261013-lab-citations/next-baseline-16.log
  locator: reports/paper_citation_curation/20261013-lab-citations/next-baseline-16.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 0; not scientific certification.
  support: context_only
  snapshot_sha256: 8e85fad3683d76bd6c3fb545f47c457c6d20f0a3795b6abae6b05d87f12134d1
- evidence_id: baseline-17
  kind: validation
  reference: reports/paper_citation_curation/20261013-lab-citations/next-baseline-17.log
  locator: reports/paper_citation_curation/20261013-lab-citations/next-baseline-17.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 0; not scientific certification.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-00
  kind: validation
  reference: reports/paper_citation_curation/20261013-nmm-cgc-citations/post-00.log
  locator: reports/paper_citation_curation/20261013-nmm-cgc-citations/post-00.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 1; not scientific certification.
  support: context_only
  snapshot_sha256: 3329bd508a1662b5b9ba634a24dd8d1e50618f88e75da3562d51c61a811585bc
- evidence_id: post-01
  kind: validation
  reference: reports/paper_citation_curation/20261013-nmm-cgc-citations/post-01.log
  locator: reports/paper_citation_curation/20261013-nmm-cgc-citations/post-01.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 0; not scientific certification.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-02
  kind: validation
  reference: reports/paper_citation_curation/20261013-nmm-cgc-citations/post-02.log
  locator: reports/paper_citation_curation/20261013-nmm-cgc-citations/post-02.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 1; not scientific certification.
  support: context_only
  snapshot_sha256: fd0ae46c20f2518b4a24870501a07c16511ea65706d1eb324ea2a30af93702f0
- evidence_id: post-03
  kind: validation
  reference: reports/paper_citation_curation/20261013-nmm-cgc-citations/post-03.log
  locator: reports/paper_citation_curation/20261013-nmm-cgc-citations/post-03.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 0; not scientific certification.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-04
  kind: validation
  reference: reports/paper_citation_curation/20261013-nmm-cgc-citations/post-04.log
  locator: reports/paper_citation_curation/20261013-nmm-cgc-citations/post-04.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 1; not scientific certification.
  support: context_only
  snapshot_sha256: fd0ae46c20f2518b4a24870501a07c16511ea65706d1eb324ea2a30af93702f0
- evidence_id: post-05
  kind: validation
  reference: reports/paper_citation_curation/20261013-nmm-cgc-citations/post-05.log
  locator: reports/paper_citation_curation/20261013-nmm-cgc-citations/post-05.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 0; not scientific certification.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-06
  kind: validation
  reference: reports/paper_citation_curation/20261013-nmm-cgc-citations/post-06.log
  locator: reports/paper_citation_curation/20261013-nmm-cgc-citations/post-06.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 1; not scientific certification.
  support: context_only
  snapshot_sha256: fd0ae46c20f2518b4a24870501a07c16511ea65706d1eb324ea2a30af93702f0
- evidence_id: post-07
  kind: validation
  reference: reports/paper_citation_curation/20261013-nmm-cgc-citations/post-07.log
  locator: reports/paper_citation_curation/20261013-nmm-cgc-citations/post-07.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 0; not scientific certification.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-08
  kind: validation
  reference: reports/paper_citation_curation/20261013-nmm-cgc-citations/post-08.log
  locator: reports/paper_citation_curation/20261013-nmm-cgc-citations/post-08.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 1; not scientific certification.
  support: context_only
  snapshot_sha256: fd0ae46c20f2518b4a24870501a07c16511ea65706d1eb324ea2a30af93702f0
- evidence_id: post-09
  kind: validation
  reference: reports/paper_citation_curation/20261013-nmm-cgc-citations/post-09.log
  locator: reports/paper_citation_curation/20261013-nmm-cgc-citations/post-09.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 0; not scientific certification.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-10
  kind: validation
  reference: reports/paper_citation_curation/20261013-nmm-cgc-citations/post-10.log
  locator: reports/paper_citation_curation/20261013-nmm-cgc-citations/post-10.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 1; not scientific certification.
  support: context_only
  snapshot_sha256: fd0ae46c20f2518b4a24870501a07c16511ea65706d1eb324ea2a30af93702f0
- evidence_id: post-11
  kind: validation
  reference: reports/paper_citation_curation/20261013-nmm-cgc-citations/post-11.log
  locator: reports/paper_citation_curation/20261013-nmm-cgc-citations/post-11.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 0; not scientific certification.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-12
  kind: validation
  reference: reports/paper_citation_curation/20261013-nmm-cgc-citations/post-12.log
  locator: reports/paper_citation_curation/20261013-nmm-cgc-citations/post-12.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 1; not scientific certification.
  support: context_only
  snapshot_sha256: 4dc7f19c2220f263843e4c3c339fe3221ae582a9f97d31f1faa31238364edfbd
- evidence_id: post-13
  kind: validation
  reference: reports/paper_citation_curation/20261013-nmm-cgc-citations/post-13.log
  locator: reports/paper_citation_curation/20261013-nmm-cgc-citations/post-13.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 0; not scientific certification.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-14
  kind: validation
  reference: reports/paper_citation_curation/20261013-nmm-cgc-citations/post-14.log
  locator: reports/paper_citation_curation/20261013-nmm-cgc-citations/post-14.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 1; not scientific certification.
  support: context_only
  snapshot_sha256: f105585d7f44bee6c4d2469b134f3a38e3261af9fb0ee76f6faf4444ef97a0d5
- evidence_id: post-15
  kind: validation
  reference: reports/paper_citation_curation/20261013-nmm-cgc-citations/post-15.log
  locator: reports/paper_citation_curation/20261013-nmm-cgc-citations/post-15.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 0; not scientific certification.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: post-16
  kind: validation
  reference: reports/paper_citation_curation/20261013-nmm-cgc-citations/post-16.log
  locator: reports/paper_citation_curation/20261013-nmm-cgc-citations/post-16.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 1; not scientific certification.
  support: context_only
  snapshot_sha256: ea83f8f858ebc6b3a92249033f53b6a3513a98cdf1a4e95d84fb4907619ecfee
- evidence_id: post-17
  kind: validation
  reference: reports/paper_citation_curation/20261013-nmm-cgc-citations/post-17.log
  locator: reports/paper_citation_curation/20261013-nmm-cgc-citations/post-17.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 0; not scientific certification.
  support: context_only
  snapshot_sha256: 43d41e93d345e8e6931f22d3052c43d862f37370ea812df8ff8db7d2f6e5247a
- evidence_id: merge-00
  kind: validation
  reference: reports/paper_citation_curation/20261013-nmm-cgc-citations/merge-00.log
  locator: reports/paper_citation_curation/20261013-nmm-cgc-citations/merge-00.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 1; not scientific certification.
  support: context_only
  snapshot_sha256: 09a2922082db841587410042dc33d7d3f72b2601f1d6b6f2b33322471ee47f2c
- evidence_id: merge-01
  kind: validation
  reference: reports/paper_citation_curation/20261013-nmm-cgc-citations/merge-01.log
  locator: reports/paper_citation_curation/20261013-nmm-cgc-citations/merge-01.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 1; not scientific certification.
  support: context_only
  snapshot_sha256: 0796b224ed4c4fdab0175cc15af5f3b9322bba1c7ff41fc7514d82530480899a
- evidence_id: extra-00
  kind: validation
  reference: reports/paper_citation_curation/20261013-nmm-cgc-citations/extra-00.log
  locator: reports/paper_citation_curation/20261013-nmm-cgc-citations/extra-00.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 0; not scientific certification.
  support: context_only
  snapshot_sha256: 6297b68fd96bf9431dfb755876fc757ab3c99f4888478ae417b4b5d5a91c8bff
- evidence_id: extra-01
  kind: validation
  reference: reports/paper_citation_curation/20261013-nmm-cgc-citations/extra-01.log
  locator: reports/paper_citation_curation/20261013-nmm-cgc-citations/extra-01.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 0; not scientific certification.
  support: context_only
  snapshot_sha256: 441bdd6ab36f5b87c9edccf771321e1c5f6c11f43bec7799e6e98cd4d756c24c
- evidence_id: extra-02
  kind: validation
  reference: reports/paper_citation_curation/20261013-nmm-cgc-citations/extra-02.log
  locator: reports/paper_citation_curation/20261013-nmm-cgc-citations/extra-02.log;
    Complete command output
  accessed_at: '2026-10-13T11:55:30Z'
  summary: Actual exit code 0; not scientific certification.
  support: context_only
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
assessments:
- assessment_id: citation-007045
  area: evidence
  topic: Publication identity, bibliography and source access
  outcome: supported
  target_ids:
  - CultureMech:007045
  evidence_ids:
  - vanderrest
  - nmm-figure
  - neidhardt
  - joins
  - archives
  - readback
  summary: Two deduplicated citations with verified title, authors, year, identifiers,
    discovery mode, source type and raw/Markdown archives. Bibliographic relevance
    does not certify the complete parent recipe.
- assessment_id: formulation-007045
  area: evidence
  topic: Study formulation and supported differences
  outcome: concern
  target_ids:
  - CultureMech:007045
  evidence_ids:
  - vanderrest
  - nmm-figure
  - neidhardt
  - claims
  - readback
  - evidence-readback
  summary: Carbon mass dose is explicit, but complete base and chemical-form correspondence
    remain unresolved. No forced variant or parent concentration correction.
  details: '{"variants": [], "preserved_parent_amounts": [{"field_path": "ingredients[0].concentration",
    "chemical": "D-Glucose", "term": {"id": "CHEBI:17634", "label": "D-glucose"},
    "concentration": {"value": "28.0", "unit": "MILLIMOLAR"}, "disposition": "preserved;
    not newly certified; outside full parent concentration-review scope"}, {"field_path":
    "ingredients[1].concentration", "chemical": "Magnesium chloride", "term": {"id":
    "CHEBI:86345", "label": "magnesium dichloride hexahydrate"}, "concentration":
    {"value": "0.523", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly
    certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[2].concentration",
    "chemical": "Calcium chloride anhydrous", "term": {"id": "CHEBI:3312", "label":
    "calcium dichloride"}, "concentration": {"value": "0.0005", "unit": "MILLIMOLAR"},
    "disposition": "preserved; not newly certified; outside full parent concentration-review
    scope"}, {"field_path": "ingredients[3].concentration", "chemical": "Potassium
    sulfate", "term": {"id": "CHEBI:32036", "label": "potassium sulfate"}, "concentration":
    {"value": "0.276", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly
    certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[4].concentration",
    "chemical": "Potassium dibasic phosphate", "term": {"id": "CHEBI:131527", "label":
    "dipotassium hydrogen phosphate"}, "concentration": {"value": "1.32", "unit":
    "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent
    concentration-review scope"}, {"field_path": "ingredients[5].concentration", "chemical":
    "Sodium chloride", "term": {"id": "CHEBI:26710", "label": "sodium chloride"},
    "concentration": {"value": "50.0", "unit": "MILLIMOLAR"}, "disposition": "preserved;
    not newly certified; outside full parent concentration-review scope"}, {"field_path":
    "ingredients[6].concentration", "chemical": "Ammonium chloride", "term": {"id":
    "CHEBI:31206", "label": "ammonium chloride"}, "concentration": {"value": "9.52",
    "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside
    full parent concentration-review scope"}, {"field_path": "ingredients[7].concentration",
    "chemical": "Ferrous sulfate", "term": {"id": "CHEBI:75832", "label": "iron(2+)
    sulfate (anhydrous)"}, "concentration": {"value": "0.01", "unit": "MILLIMOLAR"},
    "disposition": "preserved; not newly certified; outside full parent concentration-review
    scope"}, {"field_path": "ingredients[8].concentration", "chemical": "MOPS", "term":
    {"id": "CHEBI:39074", "label": "MOPS"}, "concentration": {"value": "40.0", "unit":
    "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent
    concentration-review scope"}, {"field_path": "ingredients[9].concentration", "chemical":
    "Tricine", "term": {"id": "CHEBI:46760", "label": "tricine"}, "concentration":
    {"value": "4.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified;
    outside full parent concentration-review scope"}]}'
  dimensions:
  - name: concentration_decision
    value: unsupported
    definition: Only explicit variant modifications have new primary support; every
      parent amount remains preserved and unverified in this focused task.
    evidence_ids:
    - vanderrest
    - nmm-figure
    - neidhardt
    - claims
  metrics:
  - name: preserved parent ingredient instances
    value: 10
    unit: instances
    denominator: 10
    minimum: 0
    maximum: 10
    definition: Unchanged direct ingredients, not a verified-concentration score.
- assessment_id: organism-007045
  area: evidence
  topic: Taxonomy and growth-versus-mention scope
  outcome: supported
  target_ids:
  - CultureMech:007045
  evidence_ids:
  - vanderrest
  - nmm-figure
  - neidhardt
  - taxonomy-main
  - taxonomy-background
  - taxonomy-additional
  - readback
  - evidence-readback
  summary: Source growth observations and organisms have explicit mappings, but unresolved
    local formulation prevents a native positive target. Strains, mutants, plates
    and mixed competition are kept separate.
  details: '[]'
- assessment_id: scope-007045
  area: evidence
  topic: Publication boundary
  outcome: supported
  target_ids:
  - CultureMech:007045
  evidence_ids:
  - exporter
  - schema
  - readback
  summary: No native positive growth entry added. No generated output published.
- assessment_id: citation-007046
  area: evidence
  topic: Publication identity, bibliography and source access
  outcome: supported
  target_ids:
  - CultureMech:007046
  evidence_ids:
  - vanderrest
  - nmm-figure
  - neidhardt
  - joins
  - archives
  - readback
  summary: Two deduplicated citations with verified title, authors, year, identifiers,
    discovery mode, source type and raw/Markdown archives. Bibliographic relevance
    does not certify the complete parent recipe.
- assessment_id: formulation-007046
  area: evidence
  topic: Study formulation and supported differences
  outcome: concern
  target_ids:
  - CultureMech:007046
  evidence_ids:
  - vanderrest
  - nmm-figure
  - neidhardt
  - claims
  - readback
  - evidence-readback
  summary: Carbon mass dose is explicit, but complete base and chemical-form correspondence
    remain unresolved. No forced variant or parent concentration correction.
  details: '{"variants": [], "preserved_parent_amounts": [{"field_path": "ingredients[0].concentration",
    "chemical": "Pyruvate", "term": {"id": "CHEBI:15361", "label": "pyruvate"}, "concentration":
    {"value": "57.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly
    certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[1].concentration",
    "chemical": "Magnesium chloride", "term": {"id": "CHEBI:86345", "label": "magnesium
    dichloride hexahydrate"}, "concentration": {"value": "0.523", "unit": "MILLIMOLAR"},
    "disposition": "preserved; not newly certified; outside full parent concentration-review
    scope"}, {"field_path": "ingredients[2].concentration", "chemical": "Calcium chloride
    anhydrous", "term": {"id": "CHEBI:3312", "label": "calcium dichloride"}, "concentration":
    {"value": "0.0005", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly
    certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[3].concentration",
    "chemical": "Potassium sulfate", "term": {"id": "CHEBI:32036", "label": "potassium
    sulfate"}, "concentration": {"value": "0.276", "unit": "MILLIMOLAR"}, "disposition":
    "preserved; not newly certified; outside full parent concentration-review scope"},
    {"field_path": "ingredients[4].concentration", "chemical": "Potassium dibasic
    phosphate", "term": {"id": "CHEBI:131527", "label": "dipotassium hydrogen phosphate"},
    "concentration": {"value": "1.32", "unit": "MILLIMOLAR"}, "disposition": "preserved;
    not newly certified; outside full parent concentration-review scope"}, {"field_path":
    "ingredients[5].concentration", "chemical": "Sodium chloride", "term": {"id":
    "CHEBI:26710", "label": "sodium chloride"}, "concentration": {"value": "50.0",
    "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside
    full parent concentration-review scope"}, {"field_path": "ingredients[6].concentration",
    "chemical": "Ammonium chloride", "term": {"id": "CHEBI:31206", "label": "ammonium
    chloride"}, "concentration": {"value": "9.52", "unit": "MILLIMOLAR"}, "disposition":
    "preserved; not newly certified; outside full parent concentration-review scope"},
    {"field_path": "ingredients[7].concentration", "chemical": "Ferrous sulfate",
    "term": {"id": "CHEBI:75832", "label": "iron(2+) sulfate (anhydrous)"}, "concentration":
    {"value": "0.01", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly
    certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[8].concentration",
    "chemical": "MOPS", "term": {"id": "CHEBI:39074", "label": "MOPS"}, "concentration":
    {"value": "40.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly
    certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[9].concentration",
    "chemical": "Tricine", "term": {"id": "CHEBI:46760", "label": "tricine"}, "concentration":
    {"value": "4.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified;
    outside full parent concentration-review scope"}]}'
  dimensions:
  - name: concentration_decision
    value: unsupported
    definition: Only explicit variant modifications have new primary support; every
      parent amount remains preserved and unverified in this focused task.
    evidence_ids:
    - vanderrest
    - nmm-figure
    - neidhardt
    - claims
  metrics:
  - name: preserved parent ingredient instances
    value: 10
    unit: instances
    denominator: 10
    minimum: 0
    maximum: 10
    definition: Unchanged direct ingredients, not a verified-concentration score.
- assessment_id: organism-007046
  area: evidence
  topic: Taxonomy and growth-versus-mention scope
  outcome: supported
  target_ids:
  - CultureMech:007046
  evidence_ids:
  - vanderrest
  - nmm-figure
  - neidhardt
  - taxonomy-main
  - taxonomy-background
  - taxonomy-additional
  - readback
  - evidence-readback
  summary: Source growth observations and organisms have explicit mappings, but unresolved
    local formulation prevents a native positive target. Strains, mutants, plates
    and mixed competition are kept separate.
  details: '[]'
- assessment_id: scope-007046
  area: evidence
  topic: Publication boundary
  outcome: supported
  target_ids:
  - CultureMech:007046
  evidence_ids:
  - exporter
  - schema
  - readback
  summary: No native positive growth entry added. No generated output published.
- assessment_id: citation-007047
  area: evidence
  topic: Publication identity, bibliography and source access
  outcome: supported
  target_ids:
  - CultureMech:007047
  evidence_ids:
  - vanderrest
  - nmm-figure
  - neidhardt
  - joins
  - archives
  - readback
  summary: Two deduplicated citations with verified title, authors, year, identifiers,
    discovery mode, source type and raw/Markdown archives. Bibliographic relevance
    does not certify the complete parent recipe.
- assessment_id: formulation-007047
  area: evidence
  topic: Study formulation and supported differences
  outcome: concern
  target_ids:
  - CultureMech:007047
  evidence_ids:
  - vanderrest
  - nmm-figure
  - neidhardt
  - claims
  - readback
  - evidence-readback
  summary: Carbon mass dose is explicit, but complete base and chemical-form correspondence
    remain unresolved. No forced variant or parent concentration correction.
  details: '{"variants": [], "preserved_parent_amounts": [{"field_path": "ingredients[0].concentration",
    "chemical": "(R)-Lactate", "term": null, "concentration": {"value": "56.0", "unit":
    "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent
    concentration-review scope"}, {"field_path": "ingredients[1].concentration", "chemical":
    "Magnesium chloride", "term": {"id": "CHEBI:86345", "label": "magnesium dichloride
    hexahydrate"}, "concentration": {"value": "0.523", "unit": "MILLIMOLAR"}, "disposition":
    "preserved; not newly certified; outside full parent concentration-review scope"},
    {"field_path": "ingredients[2].concentration", "chemical": "Calcium chloride anhydrous",
    "term": {"id": "CHEBI:3312", "label": "calcium dichloride"}, "concentration":
    {"value": "0.0005", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly
    certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[3].concentration",
    "chemical": "Potassium sulfate", "term": {"id": "CHEBI:32036", "label": "potassium
    sulfate"}, "concentration": {"value": "0.276", "unit": "MILLIMOLAR"}, "disposition":
    "preserved; not newly certified; outside full parent concentration-review scope"},
    {"field_path": "ingredients[4].concentration", "chemical": "Potassium dibasic
    phosphate", "term": {"id": "CHEBI:131527", "label": "dipotassium hydrogen phosphate"},
    "concentration": {"value": "1.32", "unit": "MILLIMOLAR"}, "disposition": "preserved;
    not newly certified; outside full parent concentration-review scope"}, {"field_path":
    "ingredients[5].concentration", "chemical": "Sodium chloride", "term": {"id":
    "CHEBI:26710", "label": "sodium chloride"}, "concentration": {"value": "50.0",
    "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside
    full parent concentration-review scope"}, {"field_path": "ingredients[6].concentration",
    "chemical": "Ammonium chloride", "term": {"id": "CHEBI:31206", "label": "ammonium
    chloride"}, "concentration": {"value": "9.52", "unit": "MILLIMOLAR"}, "disposition":
    "preserved; not newly certified; outside full parent concentration-review scope"},
    {"field_path": "ingredients[7].concentration", "chemical": "Ferrous sulfate",
    "term": {"id": "CHEBI:75832", "label": "iron(2+) sulfate (anhydrous)"}, "concentration":
    {"value": "0.01", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly
    certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[8].concentration",
    "chemical": "MOPS", "term": {"id": "CHEBI:39074", "label": "MOPS"}, "concentration":
    {"value": "40.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly
    certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[9].concentration",
    "chemical": "Tricine", "term": {"id": "CHEBI:46760", "label": "tricine"}, "concentration":
    {"value": "4.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified;
    outside full parent concentration-review scope"}]}'
  dimensions:
  - name: concentration_decision
    value: unsupported
    definition: Only explicit variant modifications have new primary support; every
      parent amount remains preserved and unverified in this focused task.
    evidence_ids:
    - vanderrest
    - nmm-figure
    - neidhardt
    - claims
  metrics:
  - name: preserved parent ingredient instances
    value: 10
    unit: instances
    denominator: 10
    minimum: 0
    maximum: 10
    definition: Unchanged direct ingredients, not a verified-concentration score.
- assessment_id: organism-007047
  area: evidence
  topic: Taxonomy and growth-versus-mention scope
  outcome: supported
  target_ids:
  - CultureMech:007047
  evidence_ids:
  - vanderrest
  - nmm-figure
  - neidhardt
  - taxonomy-main
  - taxonomy-background
  - taxonomy-additional
  - readback
  - evidence-readback
  summary: Source growth observations and organisms have explicit mappings, but unresolved
    local formulation prevents a native positive target. Strains, mutants, plates
    and mixed competition are kept separate.
  details: '[]'
- assessment_id: scope-007047
  area: evidence
  topic: Publication boundary
  outcome: supported
  target_ids:
  - CultureMech:007047
  evidence_ids:
  - exporter
  - schema
  - readback
  summary: No native positive growth entry added. No generated output published.
- assessment_id: citation-007048
  area: evidence
  topic: Publication identity, bibliography and source access
  outcome: supported
  target_ids:
  - CultureMech:007048
  evidence_ids:
  - vanderrest
  - nmm-figure
  - neidhardt
  - joins
  - archives
  - readback
  summary: Two deduplicated citations with verified title, authors, year, identifiers,
    discovery mode, source type and raw/Markdown archives. Bibliographic relevance
    does not certify the complete parent recipe.
- assessment_id: formulation-007048
  area: evidence
  topic: Study formulation and supported differences
  outcome: concern
  target_ids:
  - CultureMech:007048
  evidence_ids:
  - vanderrest
  - nmm-figure
  - neidhardt
  - claims
  - readback
  - evidence-readback
  summary: Carbon mass dose is explicit, but complete base and chemical-form correspondence
    remain unresolved. No forced variant or parent concentration correction.
  details: '{"variants": [], "preserved_parent_amounts": [{"field_path": "ingredients[0].concentration",
    "chemical": "(S)-Malate", "term": null, "concentration": {"value": "38.0", "unit":
    "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent
    concentration-review scope"}, {"field_path": "ingredients[1].concentration", "chemical":
    "Magnesium chloride", "term": {"id": "CHEBI:86345", "label": "magnesium dichloride
    hexahydrate"}, "concentration": {"value": "0.523", "unit": "MILLIMOLAR"}, "disposition":
    "preserved; not newly certified; outside full parent concentration-review scope"},
    {"field_path": "ingredients[2].concentration", "chemical": "Calcium chloride anhydrous",
    "term": {"id": "CHEBI:3312", "label": "calcium dichloride"}, "concentration":
    {"value": "0.0005", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly
    certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[3].concentration",
    "chemical": "Potassium sulfate", "term": {"id": "CHEBI:32036", "label": "potassium
    sulfate"}, "concentration": {"value": "0.276", "unit": "MILLIMOLAR"}, "disposition":
    "preserved; not newly certified; outside full parent concentration-review scope"},
    {"field_path": "ingredients[4].concentration", "chemical": "Potassium dibasic
    phosphate", "term": {"id": "CHEBI:131527", "label": "dipotassium hydrogen phosphate"},
    "concentration": {"value": "1.32", "unit": "MILLIMOLAR"}, "disposition": "preserved;
    not newly certified; outside full parent concentration-review scope"}, {"field_path":
    "ingredients[5].concentration", "chemical": "Sodium chloride", "term": {"id":
    "CHEBI:26710", "label": "sodium chloride"}, "concentration": {"value": "50.0",
    "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside
    full parent concentration-review scope"}, {"field_path": "ingredients[6].concentration",
    "chemical": "Ammonium chloride", "term": {"id": "CHEBI:31206", "label": "ammonium
    chloride"}, "concentration": {"value": "9.52", "unit": "MILLIMOLAR"}, "disposition":
    "preserved; not newly certified; outside full parent concentration-review scope"},
    {"field_path": "ingredients[7].concentration", "chemical": "Ferrous sulfate",
    "term": {"id": "CHEBI:75832", "label": "iron(2+) sulfate (anhydrous)"}, "concentration":
    {"value": "0.01", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly
    certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[8].concentration",
    "chemical": "MOPS", "term": {"id": "CHEBI:39074", "label": "MOPS"}, "concentration":
    {"value": "40.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly
    certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[9].concentration",
    "chemical": "Tricine", "term": {"id": "CHEBI:46760", "label": "tricine"}, "concentration":
    {"value": "4.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified;
    outside full parent concentration-review scope"}]}'
  dimensions:
  - name: concentration_decision
    value: unsupported
    definition: Only explicit variant modifications have new primary support; every
      parent amount remains preserved and unverified in this focused task.
    evidence_ids:
    - vanderrest
    - nmm-figure
    - neidhardt
    - claims
  metrics:
  - name: preserved parent ingredient instances
    value: 10
    unit: instances
    denominator: 10
    minimum: 0
    maximum: 10
    definition: Unchanged direct ingredients, not a verified-concentration score.
- assessment_id: organism-007048
  area: evidence
  topic: Taxonomy and growth-versus-mention scope
  outcome: supported
  target_ids:
  - CultureMech:007048
  evidence_ids:
  - vanderrest
  - nmm-figure
  - neidhardt
  - taxonomy-main
  - taxonomy-background
  - taxonomy-additional
  - readback
  - evidence-readback
  summary: Source growth observations and organisms have explicit mappings, but unresolved
    local formulation prevents a native positive target. Strains, mutants, plates
    and mixed competition are kept separate.
  details: '[]'
- assessment_id: scope-007048
  area: evidence
  topic: Publication boundary
  outcome: supported
  target_ids:
  - CultureMech:007048
  evidence_ids:
  - exporter
  - schema
  - readback
  summary: No native positive growth entry added. No generated output published.
- assessment_id: citation-007049
  area: evidence
  topic: Publication identity, bibliography and source access
  outcome: supported
  target_ids:
  - CultureMech:007049
  evidence_ids:
  - vanderrest
  - nmm-figure
  - neidhardt
  - joins
  - archives
  - readback
  summary: Two deduplicated citations with verified title, authors, year, identifiers,
    discovery mode, source type and raw/Markdown archives. Bibliographic relevance
    does not certify the complete parent recipe.
- assessment_id: formulation-007049
  area: evidence
  topic: Study formulation and supported differences
  outcome: concern
  target_ids:
  - CultureMech:007049
  evidence_ids:
  - vanderrest
  - nmm-figure
  - neidhardt
  - claims
  - readback
  - evidence-readback
  summary: Carbon mass dose is explicit, but complete base and chemical-form correspondence
    remain unresolved. No forced variant or parent concentration correction.
  details: '{"variants": [], "preserved_parent_amounts": [{"field_path": "ingredients[0].concentration",
    "chemical": "Succinate", "term": {"id": "CHEBI:26806", "label": "succinate"},
    "concentration": {"value": "43.0", "unit": "MILLIMOLAR"}, "disposition": "preserved;
    not newly certified; outside full parent concentration-review scope"}, {"field_path":
    "ingredients[1].concentration", "chemical": "Magnesium chloride", "term": {"id":
    "CHEBI:86345", "label": "magnesium dichloride hexahydrate"}, "concentration":
    {"value": "0.523", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly
    certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[2].concentration",
    "chemical": "Calcium chloride anhydrous", "term": {"id": "CHEBI:3312", "label":
    "calcium dichloride"}, "concentration": {"value": "0.0005", "unit": "MILLIMOLAR"},
    "disposition": "preserved; not newly certified; outside full parent concentration-review
    scope"}, {"field_path": "ingredients[3].concentration", "chemical": "Potassium
    sulfate", "term": {"id": "CHEBI:32036", "label": "potassium sulfate"}, "concentration":
    {"value": "0.276", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly
    certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[4].concentration",
    "chemical": "Potassium dibasic phosphate", "term": {"id": "CHEBI:131527", "label":
    "dipotassium hydrogen phosphate"}, "concentration": {"value": "1.32", "unit":
    "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent
    concentration-review scope"}, {"field_path": "ingredients[5].concentration", "chemical":
    "Sodium chloride", "term": {"id": "CHEBI:26710", "label": "sodium chloride"},
    "concentration": {"value": "50.0", "unit": "MILLIMOLAR"}, "disposition": "preserved;
    not newly certified; outside full parent concentration-review scope"}, {"field_path":
    "ingredients[6].concentration", "chemical": "Ammonium chloride", "term": {"id":
    "CHEBI:31206", "label": "ammonium chloride"}, "concentration": {"value": "9.52",
    "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside
    full parent concentration-review scope"}, {"field_path": "ingredients[7].concentration",
    "chemical": "Ferrous sulfate", "term": {"id": "CHEBI:75832", "label": "iron(2+)
    sulfate (anhydrous)"}, "concentration": {"value": "0.01", "unit": "MILLIMOLAR"},
    "disposition": "preserved; not newly certified; outside full parent concentration-review
    scope"}, {"field_path": "ingredients[8].concentration", "chemical": "MOPS", "term":
    {"id": "CHEBI:39074", "label": "MOPS"}, "concentration": {"value": "40.0", "unit":
    "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent
    concentration-review scope"}, {"field_path": "ingredients[9].concentration", "chemical":
    "Tricine", "term": {"id": "CHEBI:46760", "label": "tricine"}, "concentration":
    {"value": "4.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified;
    outside full parent concentration-review scope"}]}'
  dimensions:
  - name: concentration_decision
    value: unsupported
    definition: Only explicit variant modifications have new primary support; every
      parent amount remains preserved and unverified in this focused task.
    evidence_ids:
    - vanderrest
    - nmm-figure
    - neidhardt
    - claims
  metrics:
  - name: preserved parent ingredient instances
    value: 10
    unit: instances
    denominator: 10
    minimum: 0
    maximum: 10
    definition: Unchanged direct ingredients, not a verified-concentration score.
- assessment_id: organism-007049
  area: evidence
  topic: Taxonomy and growth-versus-mention scope
  outcome: supported
  target_ids:
  - CultureMech:007049
  evidence_ids:
  - vanderrest
  - nmm-figure
  - neidhardt
  - taxonomy-main
  - taxonomy-background
  - taxonomy-additional
  - readback
  - evidence-readback
  summary: Source growth observations and organisms have explicit mappings, but unresolved
    local formulation prevents a native positive target. Strains, mutants, plates
    and mixed competition are kept separate.
  details: '[]'
- assessment_id: scope-007049
  area: evidence
  topic: Publication boundary
  outcome: supported
  target_ids:
  - CultureMech:007049
  evidence_ids:
  - exporter
  - schema
  - readback
  summary: No native positive growth entry added. No generated output published.
- assessment_id: citation-007051
  area: evidence
  topic: Publication identity, bibliography and source access
  outcome: supported
  target_ids:
  - CultureMech:007051
  evidence_ids:
  - vanderrest
  - nmm-figure
  - neidhardt
  - joins
  - archives
  - readback
  summary: Two deduplicated citations with verified title, authors, year, identifiers,
    discovery mode, source type and raw/Markdown archives. Bibliographic relevance
    does not certify the complete parent recipe.
- assessment_id: formulation-007051
  area: evidence
  topic: Study formulation and supported differences
  outcome: concern
  target_ids:
  - CultureMech:007051
  evidence_ids:
  - vanderrest
  - nmm-figure
  - neidhardt
  - claims
  - readback
  - evidence-readback
  summary: Carbon mass dose is explicit, but complete base and chemical-form correspondence
    remain unresolved. No forced variant or parent concentration correction.
  details: '{"variants": [], "preserved_parent_amounts": [{"field_path": "ingredients[0].concentration",
    "chemical": "Acetate", "term": {"id": "CHEBI:30089", "label": "acetate"}, "concentration":
    {"value": "85.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly
    certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[1].concentration",
    "chemical": "Magnesium chloride", "term": {"id": "CHEBI:86345", "label": "magnesium
    dichloride hexahydrate"}, "concentration": {"value": "0.523", "unit": "MILLIMOLAR"},
    "disposition": "preserved; not newly certified; outside full parent concentration-review
    scope"}, {"field_path": "ingredients[2].concentration", "chemical": "Calcium chloride
    anhydrous", "term": {"id": "CHEBI:3312", "label": "calcium dichloride"}, "concentration":
    {"value": "0.0005", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly
    certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[3].concentration",
    "chemical": "Potassium sulfate", "term": {"id": "CHEBI:32036", "label": "potassium
    sulfate"}, "concentration": {"value": "0.276", "unit": "MILLIMOLAR"}, "disposition":
    "preserved; not newly certified; outside full parent concentration-review scope"},
    {"field_path": "ingredients[4].concentration", "chemical": "Potassium dibasic
    phosphate", "term": {"id": "CHEBI:131527", "label": "dipotassium hydrogen phosphate"},
    "concentration": {"value": "1.32", "unit": "MILLIMOLAR"}, "disposition": "preserved;
    not newly certified; outside full parent concentration-review scope"}, {"field_path":
    "ingredients[5].concentration", "chemical": "Sodium chloride", "term": {"id":
    "CHEBI:26710", "label": "sodium chloride"}, "concentration": {"value": "50.0",
    "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside
    full parent concentration-review scope"}, {"field_path": "ingredients[6].concentration",
    "chemical": "Ammonium chloride", "term": {"id": "CHEBI:31206", "label": "ammonium
    chloride"}, "concentration": {"value": "9.52", "unit": "MILLIMOLAR"}, "disposition":
    "preserved; not newly certified; outside full parent concentration-review scope"},
    {"field_path": "ingredients[7].concentration", "chemical": "Ferrous sulfate",
    "term": {"id": "CHEBI:75832", "label": "iron(2+) sulfate (anhydrous)"}, "concentration":
    {"value": "0.01", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly
    certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[8].concentration",
    "chemical": "MOPS", "term": {"id": "CHEBI:39074", "label": "MOPS"}, "concentration":
    {"value": "40.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly
    certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[9].concentration",
    "chemical": "Tricine", "term": {"id": "CHEBI:46760", "label": "tricine"}, "concentration":
    {"value": "4.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified;
    outside full parent concentration-review scope"}]}'
  dimensions:
  - name: concentration_decision
    value: unsupported
    definition: Only explicit variant modifications have new primary support; every
      parent amount remains preserved and unverified in this focused task.
    evidence_ids:
    - vanderrest
    - nmm-figure
    - neidhardt
    - claims
  metrics:
  - name: preserved parent ingredient instances
    value: 10
    unit: instances
    denominator: 10
    minimum: 0
    maximum: 10
    definition: Unchanged direct ingredients, not a verified-concentration score.
- assessment_id: organism-007051
  area: evidence
  topic: Taxonomy and growth-versus-mention scope
  outcome: supported
  target_ids:
  - CultureMech:007051
  evidence_ids:
  - vanderrest
  - nmm-figure
  - neidhardt
  - taxonomy-main
  - taxonomy-background
  - taxonomy-additional
  - readback
  - evidence-readback
  summary: Source growth observations and organisms have explicit mappings, but unresolved
    local formulation prevents a native positive target. Strains, mutants, plates
    and mixed competition are kept separate.
  details: '[]'
- assessment_id: scope-007051
  area: evidence
  topic: Publication boundary
  outcome: supported
  target_ids:
  - CultureMech:007051
  evidence_ids:
  - exporter
  - schema
  - readback
  summary: No native positive growth entry added. No generated output published.
- assessment_id: citation-007184
  area: evidence
  topic: Publication identity, bibliography and source access
  outcome: supported
  target_ids:
  - CultureMech:007184
  evidence_ids:
  - wendisch
  - cgc-figure
  - eikmanns
  - joins
  - archives
  - readback
  summary: Two deduplicated citations with verified title, authors, year, identifiers,
    discovery mode, source type and raw/Markdown archives. Bibliographic relevance
    does not certify the complete parent recipe.
- assessment_id: formulation-007184
  area: evidence
  topic: Study formulation and supported differences
  outcome: concern
  target_ids:
  - CultureMech:007184
  evidence_ids:
  - wendisch
  - cgc-figure
  - eikmanns
  - claims
  - readback
  - evidence-readback
  summary: Explicit isotope substitution and, on the mixed owner, a separate concentration
    variant; mass/molar and base-protocol uncertainty retained.
  details: '{"variants": [{"name": "Wendisch 2000 CgC with sodium [1-13C]acetate",
    "relationship": "SUBSTITUTED_COMPONENT_VARIANT", "description": "This is a source-described
    CgC assay variant, not certification of all imported parent amounts. The Eikmanns
    1991 base protocol is available only as abstract/metadata; its full base composition
    and preparation remain unresolved. The paper''s sodium acetate is not silently
    equated with an unspecified acetate counterion or hydration state. Keep reported
    mass doses and Table 2 nominal molar headings separate; no conversion or correction
    of the parent''s minerals, vitamins, carbon amounts or filter step is made. Materials/Methods
    specify 99% atom enrichment, whereas the flux-quantitation paragraph uses 99.9%
    glucose in its inoculum correction; that discrepancy is unresolved. ", "modifications":
    ["Use sodium [1-13C]acetate at the Methods dose of 10 g/L; Table 2 reports nominal
    120 mM acetate. The parent acetate descriptor has no isotope specification and
    reports 120 mM."], "purpose": "The paper''s 13C-labeling and metabolic-flux experiment",
    "evidence": [{"reference": "doi:10.1128/JB.182.11.3088-3096.2000", "supports":
    "SUPPORT", "snippet": "sodium [1- 13 C]acetate (99% atom enrichment) (10 g/liter)",
    "explanation": "Supports this variant''s explicitly labeled carbon source, source
    mass dose and isotope substitution. Table 2, carbon-source headings in order;
    exact excerpt=''120 mM acetate 120 mM acetate + 55 mM glucose 110 mM glucose''.
    Table 2 column order is acetate, mixed acetate/glucose, glucose. Headers are reported
    nominal values, not curator conversions. This is a source-described CgC assay
    variant, not certification of all imported parent amounts. The Eikmanns 1991 base
    protocol is available only as abstract/metadata; its full base composition and
    preparation remain unresolved. The paper''s sodium acetate is not silently equated
    with an unspecified acetate counterion or hydration state. Keep reported mass
    doses and Table 2 nominal molar headings separate; no conversion or correction
    of the parent''s minerals, vitamins, carbon amounts or filter step is made. Materials/Methods
    specify 99% atom enrichment, whereas the flux-quantitation paragraph uses 99.9%
    glucose in its inoculum correction; that discrepancy is unresolved. "}]}], "preserved_parent_amounts":
    [{"field_path": "ingredients[0].concentration", "chemical": "Acetate", "term":
    {"id": "CHEBI:30089", "label": "acetate"}, "concentration": {"value": "120.0",
    "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside
    full parent concentration-review scope"}, {"field_path": "ingredients[1].concentration",
    "chemical": "Urea", "term": {"id": "CHEBI:16199", "label": "urea"}, "concentration":
    {"value": "83.3", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly
    certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[2].concentration",
    "chemical": "Biotin", "term": {"id": "CHEBI:15956", "label": "biotin"}, "concentration":
    {"value": "0.000819", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly
    certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[3].concentration",
    "chemical": "Calcium chloride anhydrous", "term": {"id": "CHEBI:3312", "label":
    "calcium dichloride"}, "concentration": {"value": "0.0775", "unit": "MILLIMOLAR"},
    "disposition": "preserved; not newly certified; outside full parent concentration-review
    scope"}, {"field_path": "ingredients[4].concentration", "chemical": "Potassium
    dibasic phosphate", "term": {"id": "CHEBI:131527", "label": "dipotassium hydrogen
    phosphate"}, "concentration": {"value": "2.87", "unit": "MILLIMOLAR"}, "disposition":
    "preserved; not newly certified; outside full parent concentration-review scope"},
    {"field_path": "ingredients[5].concentration", "chemical": "Potassium dihydrogen
    phosphate", "term": {"id": "CHEBI:63036", "label": "potassium dihydrogen phosphate"},
    "concentration": {"value": "3.67", "unit": "MILLIMOLAR"}, "disposition": "preserved;
    not newly certified; outside full parent concentration-review scope"}, {"field_path":
    "ingredients[6].concentration", "chemical": "Magnesium sulfate", "term": {"id":
    "CHEBI:32599", "label": "magnesium sulfate"}, "concentration": {"value": "1.01",
    "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside
    full parent concentration-review scope"}, {"field_path": "ingredients[7].concentration",
    "chemical": "Manganese sulfate", "term": {"id": "CHEBI:86364", "label": "manganese(II)
    sulfate monohydrate"}, "concentration": {"value": "0.0592", "unit": "MILLIMOLAR"},
    "disposition": "preserved; not newly certified; outside full parent concentration-review
    scope"}, {"field_path": "ingredients[8].concentration", "chemical": "Ferrous sulfate",
    "term": {"id": "CHEBI:75832", "label": "iron(2+) sulfate (anhydrous)"}, "concentration":
    {"value": "0.036", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly
    certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[9].concentration",
    "chemical": "Zinc sulfate", "term": {"id": "CHEBI:35176", "label": "zinc sulfate"},
    "concentration": {"value": "0.00348", "unit": "MILLIMOLAR"}, "disposition": "preserved;
    not newly certified; outside full parent concentration-review scope"}, {"field_path":
    "ingredients[10].concentration", "chemical": "Ammonium sulfate", "term": {"id":
    "CHEBI:62946", "label": "ammonium sulfate"}, "concentration": {"value": "37.8",
    "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside
    full parent concentration-review scope"}, {"field_path": "ingredients[11].concentration",
    "chemical": "Cupric sulfate", "term": {"id": "CHEBI:23414", "label": "copper(II)
    sulfate"}, "concentration": {"value": "0.00125", "unit": "MILLIMOLAR"}, "disposition":
    "preserved; not newly certified; outside full parent concentration-review scope"},
    {"field_path": "ingredients[12].concentration", "chemical": "MOPS", "term": {"id":
    "CHEBI:39074", "label": "MOPS"}, "concentration": {"value": "100.0", "unit": "MILLIMOLAR"},
    "disposition": "preserved; not newly certified; outside full parent concentration-review
    scope"}]}'
  dimensions:
  - name: concentration_decision
    value: evidence_only
    definition: Only explicit variant modifications have new primary support; every
      parent amount remains preserved and unverified in this focused task.
    evidence_ids:
    - wendisch
    - cgc-figure
    - eikmanns
    - claims
  metrics:
  - name: preserved parent ingredient instances
    value: 13
    unit: instances
    denominator: 13
    minimum: 0
    maximum: 13
    definition: Unchanged direct ingredients, not a verified-concentration score.
- assessment_id: organism-007184
  area: evidence
  topic: Taxonomy and growth-versus-mention scope
  outcome: supported
  target_ids:
  - CultureMech:007184
  evidence_ids:
  - wendisch
  - cgc-figure
  - eikmanns
  - taxonomy-main
  - taxonomy-background
  - taxonomy-additional
  - readback
  - evidence-readback
  summary: One qualitative ATCC13032 growth assertion with exact strain taxonomy and
    exact isotope-variant scope. Mutants and background organisms remain qualified
    notes; Figure 1 growth stays in variant evidence.
  details: '[{"preferred_term": "Corynebacterium glutamicum", "strain": "ATCC 13032",
    "term": {"id": "NCBITaxon:196627", "label": "Corynebacterium glutamicum ATCC 13032"},
    "scoped_to_variant": "Wendisch 2000 CgC with sodium [1-13C]acetate", "evidence":
    [{"reference": "doi:10.1128/JB.182.11.3088-3096.2000", "supports": "SUPPORT",
    "snippet": "The growth characteristics of the three cultures are summarized in
    Table 2", "explanation": "Reported organism=Corynebacterium glutamicum ATCC 13032
    (WT); scientific name/canonical mapping=Corynebacterium glutamicum ATCC 13032;
    NCBITaxon:196627; actual rank=strain; taxonomy_match=exact strain; role=wild type
    used in the Table 2 labeled-carbon assays. Lookup_on=2026-10-13; https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=196627&retmode=xml.
    Methods, Microorganisms and cultivation conditions; exact excerpt=''The wild-type
    (WT) strain of C. glutamicum ATCC 13032''. Table 2, carbon-source headings in
    order; exact excerpt=''120 mM acetate 120 mM acetate + 55 mM glucose 110 mM glucose''.
    Table 2, growth-rate row in the same column order; exact excerpt=''Growth rate
    (h −1 ) 0.28 0.36 0.32''. The positive Table 2 growth-rate cells support qualitative
    growth on each corresponding source-described labeled variant; quantitative metrics
    are not imported. Methods specify 60-mL cultures in 500-mL baffled flasks, 30
    C, 140 rpm. These are experimental settings, not optima or universal requirements.
    Table 2 footnote a; exact excerpt=''These data coincided with values obtained
    from at least three independent cultures with unlabeled substrates.''. Unlabeled-control
    agreement does not erase isotope scope or certify all local base amounts. This
    is a source-described CgC assay variant, not certification of all imported parent
    amounts. The Eikmanns 1991 base protocol is available only as abstract/metadata;
    its full base composition and preparation remain unresolved. The paper''s sodium
    acetate is not silently equated with an unspecified acetate counterion or hydration
    state. Keep reported mass doses and Table 2 nominal molar headings separate; no
    conversion or correction of the parent''s minerals, vitamins, carbon amounts or
    filter step is made. Materials/Methods specify 99% atom enrichment, whereas the
    flux-quantitation paragraph uses 99.9% glucose in its inoculum correction; that
    discrepancy is unresolved. Current KGX does not honor scoped_to_variant; these
    claims must not be published as unqualified parent-medium growth edges. Taxonomy
    archive=references_cache/papers/taxonomy/nmm-cgc-20261013.xml and .md."}]}]'
- assessment_id: scope-007184
  area: evidence
  topic: Publication boundary
  outcome: concern
  target_ids:
  - CultureMech:007184
  evidence_ids:
  - exporter
  - schema
  - readback
  summary: KGX would lose variant-only scope; publication remains blocked.
- assessment_id: citation-007185
  area: evidence
  topic: Publication identity, bibliography and source access
  outcome: supported
  target_ids:
  - CultureMech:007185
  evidence_ids:
  - wendisch
  - cgc-figure
  - eikmanns
  - joins
  - archives
  - readback
  summary: Two deduplicated citations with verified title, authors, year, identifiers,
    discovery mode, source type and raw/Markdown archives. Bibliographic relevance
    does not certify the complete parent recipe.
- assessment_id: formulation-007185
  area: evidence
  topic: Study formulation and supported differences
  outcome: concern
  target_ids:
  - CultureMech:007185
  evidence_ids:
  - wendisch
  - cgc-figure
  - eikmanns
  - claims
  - readback
  - evidence-readback
  summary: Explicit isotope substitution and, on the mixed owner, a separate concentration
    variant; mass/molar and base-protocol uncertainty retained.
  details: '{"variants": [{"name": "Wendisch 2000 CgC with sodium [1-13C]acetate and
    unlabeled glucose", "relationship": "SUBSTITUTED_COMPONENT_VARIANT", "description":
    "This is a source-described CgC assay variant, not certification of all imported
    parent amounts. The Eikmanns 1991 base protocol is available only as abstract/metadata;
    its full base composition and preparation remain unresolved. The paper''s sodium
    acetate is not silently equated with an unspecified acetate counterion or hydration
    state. Keep reported mass doses and Table 2 nominal molar headings separate; no
    conversion or correction of the parent''s minerals, vitamins, carbon amounts or
    filter step is made. Materials/Methods specify 99% atom enrichment, whereas the
    flux-quantitation paragraph uses 99.9% glucose in its inoculum correction; that
    discrepancy is unresolved. ", "modifications": ["Use sodium [1-13C]acetate and
    unlabeled glucose at 10 g/L each; Table 2 reports nominal 120 mM acetate plus
    55 mM glucose. Preserve the isotope/counterion substitution rather than treating
    the local acetate descriptor as identical."], "purpose": "The paper''s 13C-labeling
    and metabolic-flux experiment", "evidence": [{"reference": "doi:10.1128/JB.182.11.3088-3096.2000",
    "supports": "SUPPORT", "snippet": "sodium [1- 13 C]acetate (99% atom enrichment)
    plus unlabeled glucose (10 g/liter each)", "explanation": "Supports this variant''s
    explicitly labeled carbon source, source mass dose and isotope substitution. Table
    2, carbon-source headings in order; exact excerpt=''120 mM acetate 120 mM acetate
    + 55 mM glucose 110 mM glucose''. Table 2 column order is acetate, mixed acetate/glucose,
    glucose. Headers are reported nominal values, not curator conversions. This is
    a source-described CgC assay variant, not certification of all imported parent
    amounts. The Eikmanns 1991 base protocol is available only as abstract/metadata;
    its full base composition and preparation remain unresolved. The paper''s sodium
    acetate is not silently equated with an unspecified acetate counterion or hydration
    state. Keep reported mass doses and Table 2 nominal molar headings separate; no
    conversion or correction of the parent''s minerals, vitamins, carbon amounts or
    filter step is made. Materials/Methods specify 99% atom enrichment, whereas the
    flux-quantitation paragraph uses 99.9% glucose in its inoculum correction; that
    discrepancy is unresolved. "}]}, {"name": "Wendisch 2000 Figure 1 CgC with 35
    mM glucose and 120 mM acetate", "relationship": "CONCENTRATION_VARIANT", "description":
    "Separate Figure 1 time-course assay; not Table 2''s 55 mM glucose mixture. The
    caption does not specify isotope enrichment; Table 2''s labeling treatment is
    not inherited. This is a source-described CgC assay variant, not certification
    of all imported parent amounts. The Eikmanns 1991 base protocol is available only
    as abstract/metadata; its full base composition and preparation remain unresolved.
    The paper''s sodium acetate is not silently equated with an unspecified acetate
    counterion or hydration state. Keep reported mass doses and Table 2 nominal molar
    headings separate; no conversion or correction of the parent''s minerals, vitamins,
    carbon amounts or filter step is made. Materials/Methods specify 99% atom enrichment,
    whereas the flux-quantitation paragraph uses 99.9% glucose in its inoculum correction;
    that discrepancy is unresolved. ", "modifications": ["Use the Figure 1 caption''s
    35 mM glucose rather than the parent''s 55 mM; retain the stated 120 mM acetate."],
    "purpose": "Growth and substrate-consumption time course", "evidence": [{"reference":
    "doi:10.1128/JB.182.11.3088-3096.2000", "supports": "SUPPORT", "snippet": "Growth
    of C. glutamicum WT on mineral medium with 35 mM glucose and 120 mM acetate.",
    "explanation": "The caption establishes both carbon concentrations and WT cultivation.
    The inspected Figure 1 black-circle OD600 curve rises while substrate concentrations
    fall; no plotted values digitized. Reported organism=Corynebacterium glutamicum
    ATCC 13032 (WT); scientific name/canonical mapping=Corynebacterium glutamicum
    ATCC 13032; NCBITaxon:196627; actual rank=strain; taxonomy_match=exact strain;
    role=wild type used in the Table 2 labeled-carbon assays. Lookup_on=2026-10-13;
    https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=196627&retmode=xml.
    This same organism also has Table 2 growth evidence under a different inline variant.
    The preferred_term identifier prevents independent repeated target entries; retain
    this figure''s qualitative growth in variant evidence and citation notes rather
    than overwriting the Table 2 scope or inventing a different organism name. This
    is a source-described CgC assay variant, not certification of all imported parent
    amounts. The Eikmanns 1991 base protocol is available only as abstract/metadata;
    its full base composition and preparation remain unresolved. The paper''s sodium
    acetate is not silently equated with an unspecified acetate counterion or hydration
    state. Keep reported mass doses and Table 2 nominal molar headings separate; no
    conversion or correction of the parent''s minerals, vitamins, carbon amounts or
    filter step is made. Materials/Methods specify 99% atom enrichment, whereas the
    flux-quantitation paragraph uses 99.9% glucose in its inoculum correction; that
    discrepancy is unresolved. Current KGX does not honor scoped_to_variant; these
    claims must not be published as unqualified parent-medium growth edges. "}]}],
    "preserved_parent_amounts": [{"field_path": "ingredients[0].concentration", "chemical":
    "D-Glucose", "term": {"id": "CHEBI:17634", "label": "D-glucose"}, "concentration":
    {"value": "55.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly
    certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[1].concentration",
    "chemical": "Acetate", "term": {"id": "CHEBI:30089", "label": "acetate"}, "concentration":
    {"value": "120.0", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly
    certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[2].concentration",
    "chemical": "Urea", "term": {"id": "CHEBI:16199", "label": "urea"}, "concentration":
    {"value": "83.3", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly
    certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[3].concentration",
    "chemical": "Biotin", "term": {"id": "CHEBI:15956", "label": "biotin"}, "concentration":
    {"value": "0.000819", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly
    certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[4].concentration",
    "chemical": "Calcium chloride anhydrous", "term": {"id": "CHEBI:3312", "label":
    "calcium dichloride"}, "concentration": {"value": "0.0775", "unit": "MILLIMOLAR"},
    "disposition": "preserved; not newly certified; outside full parent concentration-review
    scope"}, {"field_path": "ingredients[5].concentration", "chemical": "Potassium
    dibasic phosphate", "term": {"id": "CHEBI:131527", "label": "dipotassium hydrogen
    phosphate"}, "concentration": {"value": "2.87", "unit": "MILLIMOLAR"}, "disposition":
    "preserved; not newly certified; outside full parent concentration-review scope"},
    {"field_path": "ingredients[6].concentration", "chemical": "Potassium dihydrogen
    phosphate", "term": {"id": "CHEBI:63036", "label": "potassium dihydrogen phosphate"},
    "concentration": {"value": "3.67", "unit": "MILLIMOLAR"}, "disposition": "preserved;
    not newly certified; outside full parent concentration-review scope"}, {"field_path":
    "ingredients[7].concentration", "chemical": "Magnesium sulfate", "term": {"id":
    "CHEBI:32599", "label": "magnesium sulfate"}, "concentration": {"value": "1.01",
    "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside
    full parent concentration-review scope"}, {"field_path": "ingredients[8].concentration",
    "chemical": "Manganese sulfate", "term": {"id": "CHEBI:86364", "label": "manganese(II)
    sulfate monohydrate"}, "concentration": {"value": "0.0592", "unit": "MILLIMOLAR"},
    "disposition": "preserved; not newly certified; outside full parent concentration-review
    scope"}, {"field_path": "ingredients[9].concentration", "chemical": "Ferrous sulfate",
    "term": {"id": "CHEBI:75832", "label": "iron(2+) sulfate (anhydrous)"}, "concentration":
    {"value": "0.036", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly
    certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[10].concentration",
    "chemical": "Zinc sulfate", "term": {"id": "CHEBI:35176", "label": "zinc sulfate"},
    "concentration": {"value": "0.00348", "unit": "MILLIMOLAR"}, "disposition": "preserved;
    not newly certified; outside full parent concentration-review scope"}, {"field_path":
    "ingredients[11].concentration", "chemical": "Ammonium sulfate", "term": {"id":
    "CHEBI:62946", "label": "ammonium sulfate"}, "concentration": {"value": "37.8",
    "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside
    full parent concentration-review scope"}, {"field_path": "ingredients[12].concentration",
    "chemical": "Cupric sulfate", "term": {"id": "CHEBI:23414", "label": "copper(II)
    sulfate"}, "concentration": {"value": "0.00125", "unit": "MILLIMOLAR"}, "disposition":
    "preserved; not newly certified; outside full parent concentration-review scope"},
    {"field_path": "ingredients[13].concentration", "chemical": "MOPS", "term": {"id":
    "CHEBI:39074", "label": "MOPS"}, "concentration": {"value": "100.0", "unit": "MILLIMOLAR"},
    "disposition": "preserved; not newly certified; outside full parent concentration-review
    scope"}]}'
  dimensions:
  - name: concentration_decision
    value: evidence_only
    definition: Only explicit variant modifications have new primary support; every
      parent amount remains preserved and unverified in this focused task.
    evidence_ids:
    - wendisch
    - cgc-figure
    - eikmanns
    - claims
  metrics:
  - name: preserved parent ingredient instances
    value: 14
    unit: instances
    denominator: 14
    minimum: 0
    maximum: 14
    definition: Unchanged direct ingredients, not a verified-concentration score.
- assessment_id: organism-007185
  area: evidence
  topic: Taxonomy and growth-versus-mention scope
  outcome: supported
  target_ids:
  - CultureMech:007185
  evidence_ids:
  - wendisch
  - cgc-figure
  - eikmanns
  - taxonomy-main
  - taxonomy-background
  - taxonomy-additional
  - readback
  - evidence-readback
  summary: One qualitative ATCC13032 growth assertion with exact strain taxonomy and
    exact isotope-variant scope. Mutants and background organisms remain qualified
    notes; Figure 1 growth stays in variant evidence.
  details: '[{"preferred_term": "Corynebacterium glutamicum", "strain": "ATCC 13032",
    "term": {"id": "NCBITaxon:196627", "label": "Corynebacterium glutamicum ATCC 13032"},
    "scoped_to_variant": "Wendisch 2000 CgC with sodium [1-13C]acetate and unlabeled
    glucose", "evidence": [{"reference": "doi:10.1128/JB.182.11.3088-3096.2000", "supports":
    "SUPPORT", "snippet": "The growth characteristics of the three cultures are summarized
    in Table 2", "explanation": "Reported organism=Corynebacterium glutamicum ATCC
    13032 (WT); scientific name/canonical mapping=Corynebacterium glutamicum ATCC
    13032; NCBITaxon:196627; actual rank=strain; taxonomy_match=exact strain; role=wild
    type used in the Table 2 labeled-carbon assays. Lookup_on=2026-10-13; https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=196627&retmode=xml.
    Methods, Microorganisms and cultivation conditions; exact excerpt=''The wild-type
    (WT) strain of C. glutamicum ATCC 13032''. Table 2, carbon-source headings in
    order; exact excerpt=''120 mM acetate 120 mM acetate + 55 mM glucose 110 mM glucose''.
    Table 2, growth-rate row in the same column order; exact excerpt=''Growth rate
    (h −1 ) 0.28 0.36 0.32''. The positive Table 2 growth-rate cells support qualitative
    growth on each corresponding source-described labeled variant; quantitative metrics
    are not imported. Methods specify 60-mL cultures in 500-mL baffled flasks, 30
    C, 140 rpm. These are experimental settings, not optima or universal requirements.
    Table 2 footnote a; exact excerpt=''These data coincided with values obtained
    from at least three independent cultures with unlabeled substrates.''. Unlabeled-control
    agreement does not erase isotope scope or certify all local base amounts. This
    is a source-described CgC assay variant, not certification of all imported parent
    amounts. The Eikmanns 1991 base protocol is available only as abstract/metadata;
    its full base composition and preparation remain unresolved. The paper''s sodium
    acetate is not silently equated with an unspecified acetate counterion or hydration
    state. Keep reported mass doses and Table 2 nominal molar headings separate; no
    conversion or correction of the parent''s minerals, vitamins, carbon amounts or
    filter step is made. Materials/Methods specify 99% atom enrichment, whereas the
    flux-quantitation paragraph uses 99.9% glucose in its inoculum correction; that
    discrepancy is unresolved. Current KGX does not honor scoped_to_variant; these
    claims must not be published as unqualified parent-medium growth edges. Taxonomy
    archive=references_cache/papers/taxonomy/nmm-cgc-20261013.xml and .md."}]}]'
- assessment_id: scope-007185
  area: evidence
  topic: Publication boundary
  outcome: concern
  target_ids:
  - CultureMech:007185
  evidence_ids:
  - exporter
  - schema
  - readback
  summary: KGX would lose variant-only scope; publication remains blocked.
- assessment_id: citation-007186
  area: evidence
  topic: Publication identity, bibliography and source access
  outcome: supported
  target_ids:
  - CultureMech:007186
  evidence_ids:
  - wendisch
  - cgc-figure
  - eikmanns
  - joins
  - archives
  - readback
  summary: Two deduplicated citations with verified title, authors, year, identifiers,
    discovery mode, source type and raw/Markdown archives. Bibliographic relevance
    does not certify the complete parent recipe.
- assessment_id: formulation-007186
  area: evidence
  topic: Study formulation and supported differences
  outcome: concern
  target_ids:
  - CultureMech:007186
  evidence_ids:
  - wendisch
  - cgc-figure
  - eikmanns
  - claims
  - readback
  - evidence-readback
  summary: Explicit isotope substitution and, on the mixed owner, a separate concentration
    variant; mass/molar and base-protocol uncertainty retained.
  details: '{"variants": [{"name": "Wendisch 2000 CgC with [5-13C]glucose", "relationship":
    "SUBSTITUTED_COMPONENT_VARIANT", "description": "This is a source-described CgC
    assay variant, not certification of all imported parent amounts. The Eikmanns
    1991 base protocol is available only as abstract/metadata; its full base composition
    and preparation remain unresolved. The paper''s sodium acetate is not silently
    equated with an unspecified acetate counterion or hydration state. Keep reported
    mass doses and Table 2 nominal molar headings separate; no conversion or correction
    of the parent''s minerals, vitamins, carbon amounts or filter step is made. Materials/Methods
    specify 99% atom enrichment, whereas the flux-quantitation paragraph uses 99.9%
    glucose in its inoculum correction; that discrepancy is unresolved. ", "modifications":
    ["Use [5-13C]glucose at the Methods dose of 20 g/L; Table 2 reports nominal 110
    mM glucose. The parent D-glucose descriptor does not specify this isotope label."],
    "purpose": "The paper''s 13C-labeling and metabolic-flux experiment", "evidence":
    [{"reference": "doi:10.1128/JB.182.11.3088-3096.2000", "supports": "SUPPORT",
    "snippet": "[5- 13 C]glucose (99% atom enrichment) (20 g/liter)", "explanation":
    "Supports this variant''s explicitly labeled carbon source, source mass dose and
    isotope substitution. Table 2, carbon-source headings in order; exact excerpt=''120
    mM acetate 120 mM acetate + 55 mM glucose 110 mM glucose''. Table 2 column order
    is acetate, mixed acetate/glucose, glucose. Headers are reported nominal values,
    not curator conversions. This is a source-described CgC assay variant, not certification
    of all imported parent amounts. The Eikmanns 1991 base protocol is available only
    as abstract/metadata; its full base composition and preparation remain unresolved.
    The paper''s sodium acetate is not silently equated with an unspecified acetate
    counterion or hydration state. Keep reported mass doses and Table 2 nominal molar
    headings separate; no conversion or correction of the parent''s minerals, vitamins,
    carbon amounts or filter step is made. Materials/Methods specify 99% atom enrichment,
    whereas the flux-quantitation paragraph uses 99.9% glucose in its inoculum correction;
    that discrepancy is unresolved. "}]}], "preserved_parent_amounts": [{"field_path":
    "ingredients[0].concentration", "chemical": "D-Glucose", "term": {"id": "CHEBI:17634",
    "label": "D-glucose"}, "concentration": {"value": "110.0", "unit": "MILLIMOLAR"},
    "disposition": "preserved; not newly certified; outside full parent concentration-review
    scope"}, {"field_path": "ingredients[1].concentration", "chemical": "Urea", "term":
    {"id": "CHEBI:16199", "label": "urea"}, "concentration": {"value": "83.3", "unit":
    "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside full parent
    concentration-review scope"}, {"field_path": "ingredients[2].concentration", "chemical":
    "Biotin", "term": {"id": "CHEBI:15956", "label": "biotin"}, "concentration": {"value":
    "0.000819", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified;
    outside full parent concentration-review scope"}, {"field_path": "ingredients[3].concentration",
    "chemical": "Calcium chloride anhydrous", "term": {"id": "CHEBI:3312", "label":
    "calcium dichloride"}, "concentration": {"value": "0.0775", "unit": "MILLIMOLAR"},
    "disposition": "preserved; not newly certified; outside full parent concentration-review
    scope"}, {"field_path": "ingredients[4].concentration", "chemical": "Potassium
    dibasic phosphate", "term": {"id": "CHEBI:131527", "label": "dipotassium hydrogen
    phosphate"}, "concentration": {"value": "2.87", "unit": "MILLIMOLAR"}, "disposition":
    "preserved; not newly certified; outside full parent concentration-review scope"},
    {"field_path": "ingredients[5].concentration", "chemical": "Potassium dihydrogen
    phosphate", "term": {"id": "CHEBI:63036", "label": "potassium dihydrogen phosphate"},
    "concentration": {"value": "3.67", "unit": "MILLIMOLAR"}, "disposition": "preserved;
    not newly certified; outside full parent concentration-review scope"}, {"field_path":
    "ingredients[6].concentration", "chemical": "Magnesium sulfate", "term": {"id":
    "CHEBI:32599", "label": "magnesium sulfate"}, "concentration": {"value": "1.01",
    "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside
    full parent concentration-review scope"}, {"field_path": "ingredients[7].concentration",
    "chemical": "Manganese sulfate", "term": {"id": "CHEBI:86364", "label": "manganese(II)
    sulfate monohydrate"}, "concentration": {"value": "0.0592", "unit": "MILLIMOLAR"},
    "disposition": "preserved; not newly certified; outside full parent concentration-review
    scope"}, {"field_path": "ingredients[8].concentration", "chemical": "Ferrous sulfate",
    "term": {"id": "CHEBI:75832", "label": "iron(2+) sulfate (anhydrous)"}, "concentration":
    {"value": "0.036", "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly
    certified; outside full parent concentration-review scope"}, {"field_path": "ingredients[9].concentration",
    "chemical": "Zinc sulfate", "term": {"id": "CHEBI:35176", "label": "zinc sulfate"},
    "concentration": {"value": "0.00348", "unit": "MILLIMOLAR"}, "disposition": "preserved;
    not newly certified; outside full parent concentration-review scope"}, {"field_path":
    "ingredients[10].concentration", "chemical": "Ammonium sulfate", "term": {"id":
    "CHEBI:62946", "label": "ammonium sulfate"}, "concentration": {"value": "37.8",
    "unit": "MILLIMOLAR"}, "disposition": "preserved; not newly certified; outside
    full parent concentration-review scope"}, {"field_path": "ingredients[11].concentration",
    "chemical": "Cupric sulfate", "term": {"id": "CHEBI:23414", "label": "copper(II)
    sulfate"}, "concentration": {"value": "0.00125", "unit": "MILLIMOLAR"}, "disposition":
    "preserved; not newly certified; outside full parent concentration-review scope"},
    {"field_path": "ingredients[12].concentration", "chemical": "MOPS", "term": {"id":
    "CHEBI:39074", "label": "MOPS"}, "concentration": {"value": "100.0", "unit": "MILLIMOLAR"},
    "disposition": "preserved; not newly certified; outside full parent concentration-review
    scope"}]}'
  dimensions:
  - name: concentration_decision
    value: evidence_only
    definition: Only explicit variant modifications have new primary support; every
      parent amount remains preserved and unverified in this focused task.
    evidence_ids:
    - wendisch
    - cgc-figure
    - eikmanns
    - claims
  metrics:
  - name: preserved parent ingredient instances
    value: 13
    unit: instances
    denominator: 13
    minimum: 0
    maximum: 13
    definition: Unchanged direct ingredients, not a verified-concentration score.
- assessment_id: organism-007186
  area: evidence
  topic: Taxonomy and growth-versus-mention scope
  outcome: supported
  target_ids:
  - CultureMech:007186
  evidence_ids:
  - wendisch
  - cgc-figure
  - eikmanns
  - taxonomy-main
  - taxonomy-background
  - taxonomy-additional
  - readback
  - evidence-readback
  summary: One qualitative ATCC13032 growth assertion with exact strain taxonomy and
    exact isotope-variant scope. Mutants and background organisms remain qualified
    notes; Figure 1 growth stays in variant evidence.
  details: '[{"preferred_term": "Corynebacterium glutamicum", "strain": "ATCC 13032",
    "term": {"id": "NCBITaxon:196627", "label": "Corynebacterium glutamicum ATCC 13032"},
    "scoped_to_variant": "Wendisch 2000 CgC with [5-13C]glucose", "evidence": [{"reference":
    "doi:10.1128/JB.182.11.3088-3096.2000", "supports": "SUPPORT", "snippet": "The
    growth characteristics of the three cultures are summarized in Table 2", "explanation":
    "Reported organism=Corynebacterium glutamicum ATCC 13032 (WT); scientific name/canonical
    mapping=Corynebacterium glutamicum ATCC 13032; NCBITaxon:196627; actual rank=strain;
    taxonomy_match=exact strain; role=wild type used in the Table 2 labeled-carbon
    assays. Lookup_on=2026-10-13; https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=196627&retmode=xml.
    Methods, Microorganisms and cultivation conditions; exact excerpt=''The wild-type
    (WT) strain of C. glutamicum ATCC 13032''. Table 2, carbon-source headings in
    order; exact excerpt=''120 mM acetate 120 mM acetate + 55 mM glucose 110 mM glucose''.
    Table 2, growth-rate row in the same column order; exact excerpt=''Growth rate
    (h −1 ) 0.28 0.36 0.32''. The positive Table 2 growth-rate cells support qualitative
    growth on each corresponding source-described labeled variant; quantitative metrics
    are not imported. Methods specify 60-mL cultures in 500-mL baffled flasks, 30
    C, 140 rpm. These are experimental settings, not optima or universal requirements.
    Table 2 footnote a; exact excerpt=''These data coincided with values obtained
    from at least three independent cultures with unlabeled substrates.''. Unlabeled-control
    agreement does not erase isotope scope or certify all local base amounts. This
    is a source-described CgC assay variant, not certification of all imported parent
    amounts. The Eikmanns 1991 base protocol is available only as abstract/metadata;
    its full base composition and preparation remain unresolved. The paper''s sodium
    acetate is not silently equated with an unspecified acetate counterion or hydration
    state. Keep reported mass doses and Table 2 nominal molar headings separate; no
    conversion or correction of the parent''s minerals, vitamins, carbon amounts or
    filter step is made. Materials/Methods specify 99% atom enrichment, whereas the
    flux-quantitation paragraph uses 99.9% glucose in its inoculum correction; that
    discrepancy is unresolved. Current KGX does not honor scoped_to_variant; these
    claims must not be published as unqualified parent-medium growth edges. Taxonomy
    archive=references_cache/papers/taxonomy/nmm-cgc-20261013.xml and .md."}]}]'
- assessment_id: scope-007186
  area: evidence
  topic: Publication boundary
  outcome: concern
  target_ids:
  - CultureMech:007186
  evidence_ids:
  - exporter
  - schema
  - readback
  summary: KGX would lose variant-only scope; publication remains blocked.
findings:
- finding_id: nmm-formulation
  issue_key: nmm-cgc-citations-nmm-formulation
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: NMM base and mass-to-molar correspondence remain unresolved
  target_ids:
  - CultureMech:007045
  - CultureMech:007046
  - CultureMech:007047
  - CultureMech:007048
  - CultureMech:007049
  - CultureMech:007051
  field_paths:
  - ingredients
  - preparation_steps
  - references
  description: Full Neidhardt body was not obtained. Chemical form, stereochemistry,
    hydrates, rounded molarity, micronutrients, pH and generic preparation cannot
    be certified from the carbon-dose statement. No forced variant or parent growth
    assertion.
  evidence_ids:
  - vanderrest
  - neidhardt
  - claims
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/nmm_with_glucose.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/nmm_with_pyruvate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/nmm_with_lactate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/nmm_with_malate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/nmm_with_succinate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/nmm_with_acetate.yaml
    role: authoritative normalized recipe
- finding_id: cgc-formulation
  issue_key: nmm-cgc-citations-cgc-formulation
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: CgC full base and isotope/concentration normalization remain incomplete
  target_ids:
  - CultureMech:007184
  - CultureMech:007185
  - CultureMech:007186
  field_paths:
  - ingredients
  - variants
  - references
  description: Eikmanns is abstract-only. Preserve reported isotope doses and nominal
    molarity without assuming equivalence. The 99 versus 99.9 percent enrichment discrepancy
    is explicit; source variants do not certify all parent chemistry.
  evidence_ids:
  - wendisch
  - eikmanns
  - claims
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/cgc_w_acetate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/cgc_w_acetate_glucose.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/cgc_w_glucose.yaml
    role: authoritative normalized recipe
- finding_id: multiple-variant-growth
  issue_key: nmm-cgc-citations-multiple-variant-growth
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: One organism identifier cannot represent two separately scoped inline growth
    assertions
  target_ids:
  - CultureMech:007185
  field_paths:
  - target_organisms
  - variants
  description: The mixed owner has Table 2 tracer growth and distinct Figure 1 growth.
    Only tracer growth is a target entry; Figure 1 support remains in its variant
    evidence and citation notes. Do not fabricate organism names or collapse scopes.
  evidence_ids:
  - wendisch
  - cgc-figure
  - schema
  - readback
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/cgc_w_acetate_glucose.yaml
    role: authoritative normalized recipe
- finding_id: kgx-scope
  issue_key: nmm-cgc-citations-kgx-scope
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: KGX export would lose three variant-only growth scopes
  target_ids:
  - CultureMech:007184
  - CultureMech:007185
  - CultureMech:007186
  field_paths:
  - target_organisms.scoped_to_variant
  description: Current exporter targets the parent despite scoped_to_variant. No affected
    edges are published; this finding does not supersede older reviews of other owners.
  evidence_ids:
  - exporter
  - readback
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/cgc_w_acetate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/cgc_w_acetate_glucose.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/cgc_w_glucose.yaml
    role: authoritative normalized recipe
- finding_id: reference-gates
  issue_key: nmm-cgc-citations-reference-gates
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Nine required reference checks fail on formatting and content coverage
  target_ids:
  - CultureMech:007045
  - CultureMech:007046
  - CultureMech:007047
  - CultureMech:007048
  - CultureMech:007049
  - CultureMech:007051
  - CultureMech:007184
  - CultureMech:007185
  - CultureMech:007186
  field_paths:
  - references
  - variants.evidence
  - target_organisms.evidence
  description: Verified plain PubMed titles differ from HTML-bearing or whitespace-defective
    Crossref titles. CgC full-text excerpts also exceed abstract-only retrieval coverage.
    Accurate source claims were not changed to game the checks; manual readback does
    not waive failure.
  evidence_ids:
  - evidence-readback
  - post-00
  - post-02
  - post-04
  - post-06
  - post-08
  - post-10
  - post-12
  - post-14
  - post-16
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/nmm_with_glucose.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/nmm_with_pyruvate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/nmm_with_lactate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/nmm_with_malate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/nmm_with_succinate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/nmm_with_acetate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/cgc_w_acetate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/cgc_w_acetate_glucose.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/cgc_w_glucose.yaml
    role: authoritative normalized recipe
actions:
- action_id: resolve-nmm-formulation
  description: NMM base and mass-to-molar correspondence remain unresolved
  finding_ids:
  - nmm-formulation
  target_ids:
  - CultureMech:007045
  - CultureMech:007046
  - CultureMech:007047
  - CultureMech:007048
  - CultureMech:007049
  - CultureMech:007051
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/nmm_with_glucose.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/nmm_with_pyruvate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/nmm_with_lactate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/nmm_with_malate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/nmm_with_succinate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/nmm_with_acetate.yaml
    role: authoritative normalized recipe
  acceptance_checks:
  - Inspect an authorized complete base protocol and exact carbon chemical forms.
  - Require primary DOI/PURL and literal excerpts for each proposed amount correction;
    retain arithmetic separately.
- action_id: resolve-cgc-formulation
  description: CgC full base and isotope/concentration normalization remain incomplete
  finding_ids:
  - cgc-formulation
  target_ids:
  - CultureMech:007184
  - CultureMech:007185
  - CultureMech:007186
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/cgc_w_acetate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/cgc_w_acetate_glucose.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/cgc_w_glucose.yaml
    role: authoritative normalized recipe
  acceptance_checks:
  - Obtain and inspect the complete CgC base source.
  - Reconcile exact chemical mass basis and conflicting enrichment statements before
    changing parent amounts or variant scope.
- action_id: resolve-multiple-variant-growth
  description: One organism identifier cannot represent two separately scoped inline
    growth assertions
  finding_ids:
  - multiple-variant-growth
  target_ids:
  - CultureMech:007185
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/cgc_w_acetate_glucose.yaml
    role: authoritative normalized recipe
  acceptance_checks:
  - Provide a tested native representation for repeated organism/strain observations
    scoped to different inline variants, or curate separately authorized linked records.
  - Preserve both independent scopes and primary excerpts.
- action_id: resolve-kgx-scope
  description: KGX export would lose three variant-only growth scopes
  finding_ids:
  - kgx-scope
  target_ids:
  - CultureMech:007184
  - CultureMech:007185
  - CultureMech:007186
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/cgc_w_acetate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/cgc_w_acetate_glucose.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/cgc_w_glucose.yaml
    role: authoritative normalized recipe
  acceptance_checks:
  - Add tests proving scoped entries cannot produce unqualified parent edges.
  - Preserve ordinary targets and exact primary evidence.
- action_id: resolve-reference-gates
  description: Nine required reference checks fail on formatting and content coverage
  finding_ids:
  - reference-gates
  target_ids:
  - CultureMech:007045
  - CultureMech:007046
  - CultureMech:007047
  - CultureMech:007048
  - CultureMech:007049
  - CultureMech:007051
  - CultureMech:007184
  - CultureMech:007185
  - CultureMech:007186
  owner_paths:
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/nmm_with_glucose.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/nmm_with_pyruvate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/nmm_with_lactate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/nmm_with_malate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/nmm_with_succinate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/nmm_with_acetate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/cgc_w_acetate.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/cgc_w_acetate_glucose.yaml
    role: authoritative normalized recipe
  - repository: culturebotai/CultureMech
    path: data/normalized_yaml/bacterial/cgc_w_glucose.yaml
    role: authoritative normalized recipe
  acceptance_checks:
  - Make normalized bibliography metadata and archived primary full-text excerpts
    auditable without altering correct source claims.
  - Rerun maintained gates after any separately scoped validator fix.
limitations:
- Focused scientific self-review only; all 100 parent amounts enumerated as preserved,
  not newly verified.
- NMM source wild-type growth does not resolve exact parent formulation; no positive
  native growth entry added.
- CgC Table 2 tracer cultures, unlabeled controls, Figure 1 mixture and mutant assays
  remain distinct.
- Neidhardt and Eikmanns base protocols are abstract-only; no complete formulation
  inherited from them.
- Mass/molar, chemical-form, enrichment and citing-bibliography conflicts remain explicit.
- Taxonomy includes actual rank, reported strain, background role and parent-only
  qualifications; taxonomy alone is not cultivation evidence.
- Required reference failures and global merge diagnostics are not waived. No generated
  publication or status promotion.
- 286 MediaDB candidate source-owner links remain; the queue is not an exhaustive
  literature inventory.
```
