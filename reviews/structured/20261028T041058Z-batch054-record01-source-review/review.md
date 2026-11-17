# BSW3 Agar: stale generated units and identity after owner repair

- Review: 20261028T041058Z-batch054-record01-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T03:58:26.953469Z
- Finished UTC: 2026-10-28T04:10:58.329118Z
- Reviewer: Codex independent source reviewer (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The generated BSW3 record preserves an erroneous seawater mass unit and unrelated DSM7 match despite an already repaired maintained owner. Current TOGO and MediaDive agree on identity and recipe scale; JCM1216 currently returns Nothing found, so original supplier preparation and seawater composition remain limited.

## Scope And Provenance

Full selected record and exact maintained contributors; external source limits explicitly retained.

Selection: Actual batch054 native selection index 01.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007839 | data/merge_yaml/merged/BSW3_Agar.yaml | generated | bsw3_agar |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007839 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-strict | passed | True | CultureMech:007839 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-terms | passed | True | CultureMech:007839 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-references | passed | True | CultureMech:007839 | Native reference checker performed zero reference checks; this is not claim authentication. |

## Scientific And Domain Assessments

### Exact accession boundary

identity: concern. Targets: CultureMech:007839.

TOGO M1304 and provider J1216 agree on BSW3. DSM7 is a different medium. The maintained owner already removed this mismatch.

### Complete quantity and numeric preparation audit

quantity: concern. Targets: CultureMech:007839.

Every local concentration field has an explicit disposition; source-only doses, batch volumes and conditional preparation are separate from receiving-medium rates.

[{"quantity_id": "q1", "topic": "Malt extract (BD-Difco)", "source": {"evidence_id": "apiJ1216", "reference": "https://mediadive.dsmz.de/rest/medium/J1216", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/apiJ1216.bin", "raw_sha256": "0e70509369f906661249869e31e5de092c4bc604494aaa82796e1f7b92b5e217", "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T04:02:49.091609+00:00"}, "decision": "evidence_only", "rationale": "Retain the rate: current provider explicitly declares g_l on its 1000 mL main-solution basis; the TOGO batch amount agrees.", "layer_assessments": [{"path": "data/merge_yaml/merged/BSW3_Agar.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Retain the rate: current provider explicitly declares g_l on its 1000 mL main-solution basis; the TOGO batch amount agrees."}]}, {"quantity_id": "q2", "topic": "0.1 x Artificial seawater", "source": {"evidence_id": "apiJ1216", "reference": "https://mediadive.dsmz.de/rest/medium/J1216", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/apiJ1216.bin", "raw_sha256": "0e70509369f906661249869e31e5de092c4bc604494aaa82796e1f7b92b5e217", "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T04:02:49.091609+00:00"}, "decision": "correct", "rationale": "Replace stale mass dimension using the already repaired owner: source specifies a liquid input, not 1 g/L.", "layer_assessments": [{"path": "data/merge_yaml/merged/BSW3_Agar.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Replace stale mass dimension using the already repaired owner: source specifies a liquid input, not 1 g/L."}]}, {"quantity_id": "q3", "topic": "Glucose", "source": {"evidence_id": "apiJ1216", "reference": "https://mediadive.dsmz.de/rest/medium/J1216", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/apiJ1216.bin", "raw_sha256": "0e70509369f906661249869e31e5de092c4bc604494aaa82796e1f7b92b5e217", "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T04:02:49.091609+00:00"}, "decision": "evidence_only", "rationale": "Retain the rate: current provider explicitly declares g_l on its 1000 mL main-solution basis; the TOGO batch amount agrees.", "layer_assessments": [{"path": "data/merge_yaml/merged/BSW3_Agar.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.4", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Retain the rate: current provider explicitly declares g_l on its 1000 mL main-solution basis; the TOGO batch amount agrees."}]}, {"quantity_id": "q4", "topic": "Agar", "source": {"evidence_id": "apiJ1216", "reference": "https://mediadive.dsmz.de/rest/medium/J1216", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/apiJ1216.bin", "raw_sha256": "0e70509369f906661249869e31e5de092c4bc604494aaa82796e1f7b92b5e217", "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T04:02:49.091609+00:00"}, "decision": "evidence_only", "rationale": "Retain the rate: current provider explicitly declares g_l on its 1000 mL main-solution basis; the TOGO batch amount agrees.", "layer_assessments": [{"path": "data/merge_yaml/merged/BSW3_Agar.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "15", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Retain the rate: current provider explicitly declares g_l on its 1000 mL main-solution basis; the TOGO batch amount agrees."}]}, {"quantity_id": "q5", "topic": "Yeast extract (BD-Difco)", "source": {"evidence_id": "apiJ1216", "reference": "https://mediadive.dsmz.de/rest/medium/J1216", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/apiJ1216.bin", "raw_sha256": "0e70509369f906661249869e31e5de092c4bc604494aaa82796e1f7b92b5e217", "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T04:02:49.091609+00:00"}, "decision": "evidence_only", "rationale": "Retain the rate: current provider explicitly declares g_l on its 1000 mL main-solution basis; the TOGO batch amount agrees.", "layer_assessments": [{"path": "data/merge_yaml/merged/BSW3_Agar.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.4", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Retain the rate: current provider explicitly declares g_l on its 1000 mL main-solution basis; the TOGO batch amount agrees."}]}, {"quantity_id": "q6", "topic": "Yeast extract (BD-Difco)", "source": {"evidence_id": "apiJ1216", "reference": "https://mediadive.dsmz.de/rest/medium/J1216", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/apiJ1216.bin", "raw_sha256": "0e70509369f906661249869e31e5de092c4bc604494aaa82796e1f7b92b5e217", "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T04:02:49.091609+00:00"}, "decision": "evidence_only", "rationale": "Retain the rate: current provider explicitly declares g_l on its 1000 mL main-solution basis; the TOGO batch amount agrees.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/TOGO_M1304_BSW3_Agar.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "0.4", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Retain the rate: current provider explicitly declares g_l on its 1000 mL main-solution basis; the TOGO batch amount agrees."}]}, {"quantity_id": "q7", "topic": "Malt extract (BD-Difco)", "source": {"evidence_id": "apiJ1216", "reference": "https://mediadive.dsmz.de/rest/medium/J1216", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/apiJ1216.bin", "raw_sha256": "0e70509369f906661249869e31e5de092c4bc604494aaa82796e1f7b92b5e217", "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T04:02:49.091609+00:00"}, "decision": "evidence_only", "rationale": "Retain the rate: current provider explicitly declares g_l on its 1000 mL main-solution basis; the TOGO batch amount agrees.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/TOGO_M1304_BSW3_Agar.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Retain the rate: current provider explicitly declares g_l on its 1000 mL main-solution basis; the TOGO batch amount agrees."}]}, {"quantity_id": "q8", "topic": "Glucose", "source": {"evidence_id": "apiJ1216", "reference": "https://mediadive.dsmz.de/rest/medium/J1216", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/apiJ1216.bin", "raw_sha256": "0e70509369f906661249869e31e5de092c4bc604494aaa82796e1f7b92b5e217", "locator": "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T04:02:49.091609+00:00"}, "decision": "evidence_only", "rationale": "Retain the rate: current provider explicitly declares g_l on its 1000 mL main-solution basis; the TOGO batch amount agrees.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/TOGO_M1304_BSW3_Agar.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.4", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Retain the rate: current provider explicitly declares g_l on its 1000 mL main-solution basis; the TOGO batch amount agrees."}]}, {"quantity_id": "q9", "topic": "Agar", "source": {"evidence_id": "apiJ1216", "reference": "https://mediadive.dsmz.de/rest/medium/J1216", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/apiJ1216.bin", "raw_sha256": "0e70509369f906661249869e31e5de092c4bc604494aaa82796e1f7b92b5e217", "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T04:02:49.091609+00:00"}, "decision": "evidence_only", "rationale": "Retain the rate: current provider explicitly declares g_l on its 1000 mL main-solution basis; the TOGO batch amount agrees.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/TOGO_M1304_BSW3_Agar.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "15", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Retain the rate: current provider explicitly declares g_l on its 1000 mL main-solution basis; the TOGO batch amount agrees."}]}, {"quantity_id": "q10", "topic": "0.1 x Artificial seawater", "source": {"evidence_id": "apiJ1216", "reference": "https://mediadive.dsmz.de/rest/medium/J1216", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/apiJ1216.bin", "raw_sha256": "0e70509369f906661249869e31e5de092c4bc604494aaa82796e1f7b92b5e217", "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T04:02:49.091609+00:00"}, "decision": "evidence_only", "rationale": "Retain 1000 ML_PER_L as the provider recipe-basis liquid amount; 0.1 x is source identity, not an independently reconstructed seawater composition.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/TOGO_M1304_BSW3_Agar.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "1000", "unit": "ML_PER_L"}, "decision": "evidence_only", "rationale": "Retain 1000 ML_PER_L as the provider recipe-basis liquid amount; 0.1 x is source identity, not an independently reconstructed seawater composition."}]}, {"quantity_id": "q11", "topic": "pH and pH adjustment", "source": {"evidence_id": "togo1304", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1304", "raw_path": "REVIEW_WORK/batch054/source01-03/togo1304.bin", "raw_sha256": "07a3cc9c3c1e63553208fbc3cdcaed47191f92f9e4197d2d735a2f1f55f2efb5", "locator": "$.meta.ph and $.comments[0]", "accessed_at": "2026-10-28T03:59:20.689934+00:00", "quote": "Adjust pH to 7.3."}, "decision": "mixed", "rationale": "No sterilization cycle is inferred from the unavailable JCM1216 page.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/TOGO_M1304_BSW3_Agar.yaml", "field_path": "ph_value", "stored_value": 7.3, "decision": "evidence_only", "rationale": "Current owner already retains source pH 7.3."}, {"path": "data/normalized_yaml/bacterial/TOGO_M1304_BSW3_Agar.yaml", "field_path": "preparation_steps[0].description", "stored_value": "Adjust BSW3 Agar to pH 7.3.", "decision": "evidence_only", "rationale": "Existing adjustment instruction is supported."}, {"path": "data/merge_yaml/merged/BSW3_Agar.yaml", "field_path": "ph_value", "stored_value": null, "decision": "add", "rationale": "Propagate already repaired owner pH.", "missing": true}, {"path": "data/merge_yaml/merged/BSW3_Agar.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "Propagate existing owner instruction.", "missing": true}]}, {"quantity_id": "q12", "topic": "Artificial seawater stock composition and 0.1 x identity", "source": {"evidence_id": "togo1304", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1304", "raw_path": "REVIEW_WORK/batch054/source01-03/togo1304.bin", "raw_sha256": "07a3cc9c3c1e63553208fbc3cdcaed47191f92f9e4197d2d735a2f1f55f2efb5", "locator": "$.components[0].items[1]", "accessed_at": "2026-10-28T03:59:20.689934+00:00", "quote": "0.1 x Artificial seawater"}, "decision": "unsupported", "rationale": "Retain the stated dilution identity and liquid amount. Exact stock composition and manufacture are not supplied in these accessible captures; do not guess constituent salts.", "layer_assessments": []}]

### Current ontology and MIM correspondence

grounding: supported. Targets: CultureMech:007839.

The grounding inventory enumerates every asserted identifier and exact preferred label. Current catalog joins establish present correspondence only; unmapped mixtures are not assigned invented chemical identities.

### History and evidence scope

provenance: supported. Targets: CultureMech:007839.

Complete owner and target histories were read. Current source bytes and inspected code are independent evidence; historical timestamps remain historical claims unless an exact cited raw digest is recovered.

### Growth and taxonomic evidence

scope: unknown. Targets: CultureMech:007839.

Generic cultivation applications and bacterial filing are not strain-level growth evidence. No organism-specific growth, temperature or atmosphere is inferred from names or source catalog identifiers.

### Canonical diagnostics

schema: supported. Targets: CultureMech:007839.

All four original canonical diagnostics passed. Reference checks were zero; structural and term diagnostics do not establish formulation accuracy.

## Findings

### f1: Generated seawater unit contradicts its repaired owner

major / open / confirmed; issue key: culturemech-007839-generated-seawater-unit-contradicts-its-repaired-owner.

Selected ingredients[1] still says 1 G_PER_L for 0.1 x artificial seawater. Both current sources specify 1 L/1000 mL liquid, and the owner already stores 1000 ML_PER_L. Preserve the existing owner repair and regenerate; this is not a new unperformed owner correction.

### f2: Generated DSM7 identity persists after owner correction

major / open / confirmed; issue key: culturemech-007839-generated-dsm7-identity-persists-after-owner-correction.

The selected kg_microbe_match points to mediadive.medium:7. The exact primary DSM7 is a different named formulation; its recipe and strain exception do not transfer. The owner already removed this match.

### f3: Generated pH, preparation and composition metadata are stale

minor / open / confirmed; issue key: culturemech-007839-generated-ph-preparation-and-composition-metadata-are-stale.

The owner now contains pH 7.3, its adjustment instruction and SEMI_DEFINED classification, with explicit current curation history. The generated target lacks the pH/instruction and retains UNDEFINED. Named undefined extracts remain present; SEMI_DEFINED does not make their chemical compositions known.

## Recommended Actions And Acceptance Checks

### action1

Regenerate BSW3 from the repaired sole owner and verify the exact liquid amount/unit. Keep the unknown seawater composition explicit rather than inventing a stock.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action2

Preserve removal of the unrelated DSM7 match when regenerating the selected record; retain M1304/J1216 provenance.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action3

Regenerate from the current owner, preserving its supported pH, preparation and mixture classification and existing repair history. Attach the exact source captures to future quantitative curation.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local-target | data/merge_yaml/merged/BSW3_Agar.yaml; Complete document | context_only | Complete selected generated record; no changes made. |
| owner-1 | data/normalized_yaml/bacterial/TOGO_M1304_BSW3_Agar.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| togo1304 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1304; Exact source identity and scoped formulation/preparation | supports | Exact M1304/JCM1216 identity, five batch components and pH 7.3. |
| apiJ1216 | https://mediadive.dsmz.de/rest/medium/J1216; Exact source identity and scoped formulation/preparation | supports | Exact J1216: 1000 mL main-solution basis, four explicit g_l rows, 1000 mL artificial 0.1 x seawater and pH 7.3. |
| jcm1216 | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1216; Exact source identity and scoped formulation/preparation | unknown | HTTP200 page explicitly says Nothing found; no recipe authenticated from this supplier page. |
| dsm7 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium7.pdf; Exact source identity and scoped formulation/preparation | refutes | Exact medium 7 is ANCYLOBACTER–SPIROSOMA MEDIUM; distinct formulation and pH. Identity comparison only, excluded from BSW3 recipe. |
| writer-merge | src/culturemech/merge/merger.py; merge_group | context_only | merge_group preserves a sole contributor with generated merge metadata; for multiple contributors it calls merge_formulation_evidence. Current source code does not prove historical generation execution. |
| writer-togo | src/culturemech/import/togo_importer.py; _extract_primary_components/_solution_from_item/_extract_preparation_steps | context_only | Current primary-component extraction separates named solutions from final ingredients and retains source comments; historical import behavior cannot be inferred solely from this version. |
| chebi17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17234; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_2509; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| quantities | REVIEW_WORK/batch054/record01/quantity-inventory.json | context_only | Complete local concentration and source-stage decision inventory; includes exact local paths and source failure limits. |
| grounding | REVIEW_WORK/batch054/record01/grounding-inventory.json | context_only | All recursive asserted identifier/label slots, exact current OLS objects and current packaged MIM preferred-row joins. |
| history | REVIEW_WORK/batch054/record01/history-and-evidence-inventory.json | context_only | Complete current history, references and attached evidence; source-specific claims are assessed without authenticating historical execution from code. |
| scalars | REVIEW_WORK/batch054/record01/scalar-census.json | context_only | Lossless scalar census of the selected target and all maintained contributors. |
| validate-schema | REVIEW_WORK/batch054/record01/validate-schema.json | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed<br> |
| validate-strict | REVIEW_WORK/batch054/record01/validate-strict.json | supports | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch054/record01/strict.tsv<br> |
| validate-terms | REVIEW_WORK/batch054/record01/validate-terms.json | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed<br> |
| validate-references | REVIEW_WORK/batch054/record01/validate-references.json | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed<br> |

## Limits And Additional Notes

- JCM1216 currently returns Nothing found despite HTTP200; no original supplier preparation beyond the accessible TOGO/provider content is authenticated.
- Exact 0.1 x artificial-seawater composition is absent from the accessible formulation; no salt recipe, sterilization cycle or growth claim is inferred.
- Current ontology objects establish label/identifier correspondence, not strain growth or biochemical purity.
- Fresh review; historical lost snapshots were not reconstructed. All inspected source files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T041058Z-batch054-record01-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'BSW3 Agar: stale generated units and identity after owner repair'
started_at: '2026-10-28T03:58:26.953469Z'
finished_at: '2026-10-28T04:10:58.329118Z'
reviewer:
  identity: Codex independent source reviewer
  kind: agent
  independence: independent
  independence_basis: Fresh assessment of the inspected checkout and newly captured
    primary/provider/ontology evidence; no reconstruction of lost reviews and no record
    edits.
skill: .claude/skills/review-yaml-record/SKILL.md; .claude/skills/review-ingredient-concentrations/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The generated BSW3 record preserves an erroneous seawater mass unit and unrelated
  DSM7 match despite an already repaired maintained owner. Current TOGO and MediaDive
  agree on identity and recipe scale; JCM1216 currently returns Nothing found, so
  original supplier preparation and seawater composition remain limited.
source:
  git_revision: 9ea7ff33d354e37b791df96a880005153e446ce3
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 846db73710b3134ef5267ce486d151e297295282dc5e9249658592432f8d6a7a
    role: context
  - path: .claude/skills/review-ingredient-concentrations/SKILL.md
    sha256: a67993ef11cf374ac579c53252bc603f9894ebd69cad711b11f293714c76621e
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
  - path: CLAUDE.md
    sha256: b5c5bb1c2293ba5f6c49cda8cb40bf36e021c0a2b9fe2d9497cf0a2fe19a1ac4
    role: context
  - path: conf/record_review.yaml
    sha256: a76531e51214e559c97ab748a4cba169f8a9598ce6e3664518489b43dfc9bf88
    role: context
  - path: data/merge_yaml/merged/BSW3_Agar.yaml
    sha256: 12913d3ef71d01eb8b9e6547e0a250481d9f27bcc0559fca3a2138bde123bb53
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M1304_BSW3_Agar.yaml
    sha256: f1d4f6127490173c36e1ef1ce8f982c3de9a591d071aa119b1d1c226ea9a2a5f
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
    sha256: 8cb892e67e1d94bc93c77f3a03d8d4ced32d8d31aa8e5b0346853cbc05077d6f
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/cleanup_recipe_ingredients.py
    sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/record_target_class.py
    sha256: 468fcbfd2362ca08b7066d6f21adf85c04f21ab40f80e60995522b4edc0f6349
    role: context
  - path: scripts/validate_recipe_references.py
    sha256: 087e5f3128e774bc760b7dcfc8f194fe14820354f809be9e35cf6cacb8546a3b
    role: context
  - path: scripts/validate_strict.py
    sha256: 6116d95493b8f91faed19956301291a73d090a3b83671303650a561798933456
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
    role: context
  - path: src/culturemech/import/komodo_web_importer.py
    sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
    role: context
  - path: src/culturemech/import/mediadive_importer.py
    sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
    role: context
  - path: src/culturemech/import/togo_importer.py
    sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
    role: context
  - path: src/culturemech/ingredients/mim_label_index.py
    sha256: e07eb72fe91743859451d1998dfeafe58a40dad43baa82d710a740c47dc4bf61
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
  - path: src/culturemech/merge/merger.py
    sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
    role: context
  - path: src/culturemech/schema/culturemech.yaml
    sha256: 8551fa65e4e96f36847368641282948cffd393356648fd9fb6947831ab985fae
    role: context
scope:
  description: Full selected record and exact maintained contributors; external source
    limits explicitly retained.
  selection: Actual batch054 native selection index 01.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:007839
targets:
- target_id: CultureMech:007839
  path: data/merge_yaml/merged/BSW3_Agar.yaml
  label: bsw3_agar
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1304_BSW3_Agar.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:007839
  command: just validate-schema data/merge_yaml/merged/BSW3_Agar.yaml
  exit_code: 0
  evidence_ids:
  - validate-schema
  scope_note: Exact selected target; scientific source and owner assessments are separate.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:007839
  command: just validate-strict data/merge_yaml/merged/BSW3_Agar.yaml --out REVIEW_WORK/batch054/record01/strict.tsv
    --workers 1
  exit_code: 0
  evidence_ids:
  - validate-strict
  scope_note: Exact selected target; scientific source and owner assessments are separate.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:007839
  command: just validate-terms data/merge_yaml/merged/BSW3_Agar.yaml
  exit_code: 0
  evidence_ids:
  - validate-terms
  scope_note: Exact selected target; scientific source and owner assessments are separate.
- check_id: validate-references
  name: validate-references
  status: passed
  required: true
  summary: Native reference checker performed zero reference checks; this is not claim
    authentication.
  target_ids:
  - CultureMech:007839
  command: just validate-references data/merge_yaml/merged/BSW3_Agar.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
  scope_note: Exact selected target; scientific source and owner assessments are separate.
evidence:
- evidence_id: local-target
  kind: record_content
  reference: data/merge_yaml/merged/BSW3_Agar.yaml
  locator: Complete document
  accessed_at: '2026-10-28T04:06:00.128545Z'
  support: context_only
  summary: Complete selected generated record; no changes made.
  snapshot_sha256: 12913d3ef71d01eb8b9e6547e0a250481d9f27bcc0559fca3a2138bde123bb53
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M1304_BSW3_Agar.yaml
  locator: Complete document
  accessed_at: '2026-10-28T04:06:00.128545Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: f1d4f6127490173c36e1ef1ce8f982c3de9a591d071aa119b1d1c226ea9a2a5f
- evidence_id: togo1304
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1304
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T03:59:20.689934Z'
  support: supports
  summary: Exact M1304/JCM1216 identity, five batch components and pH 7.3.
  snapshot_sha256: 07a3cc9c3c1e63553208fbc3cdcaed47191f92f9e4197d2d735a2f1f55f2efb5
- evidence_id: apiJ1216
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/J1216
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T04:02:49.091609Z'
  support: supports
  summary: 'Exact J1216: 1000 mL main-solution basis, four explicit g_l rows, 1000
    mL artificial 0.1 x seawater and pH 7.3.'
  snapshot_sha256: 0e70509369f906661249869e31e5de092c4bc604494aaa82796e1f7b92b5e217
- evidence_id: jcm1216
  kind: primary_source
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1216
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T03:59:20.990848Z'
  support: unknown
  summary: HTTP200 page explicitly says Nothing found; no recipe authenticated from
    this supplier page.
  snapshot_sha256: f707db2e2146950ffb8649c234f48f8ed93f4a4fc171adc4f46b5fdcdd4aed7b
- evidence_id: dsm7
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium7.pdf
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T03:59:21.288331Z'
  support: refutes
  summary: Exact medium 7 is ANCYLOBACTER–SPIROSOMA MEDIUM; distinct formulation and
    pH. Identity comparison only, excluded from BSW3 recipe.
  snapshot_sha256: 43a684b88223fa21a603e6f91419150ad434584b2028d7e43bda73b6ab93aa8e
- evidence_id: writer-merge
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: merge_group
  accessed_at: '2026-10-28T04:06:00.128545Z'
  support: context_only
  summary: merge_group preserves a sole contributor with generated merge metadata;
    for multiple contributors it calls merge_formulation_evidence. Current source
    code does not prove historical generation execution.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-togo
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  locator: _extract_primary_components/_solution_from_item/_extract_preparation_steps
  accessed_at: '2026-10-28T04:06:00.128545Z'
  support: context_only
  summary: Current primary-component extraction separates named solutions from final
    ingredients and retains source comments; historical import behavior cannot be
    inferred solely from this version.
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: chebi17234
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17234
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T03:59:22.470692Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 2d78d31a7829da999c31ae102da842c5b5c37a5d334be6389539d92ecd786de7
- evidence_id: chebi2509
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_2509
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T03:59:22.926393Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 348b20478bba221cc21e285237104281145111be6ea3aa30d381d6eae19c0a90
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch054/record01/quantity-inventory.json
  accessed_at: '2026-10-28T04:06:00.137769Z'
  support: context_only
  summary: Complete local concentration and source-stage decision inventory; includes
    exact local paths and source failure limits.
  snapshot_sha256: a4e1f9247f505090f669fe5e431fab6c2cd4a319d299f7039ba428ff23a33868
- evidence_id: grounding
  kind: record_content
  reference: REVIEW_WORK/batch054/record01/grounding-inventory.json
  accessed_at: '2026-10-28T04:06:00.137805Z'
  support: context_only
  summary: All recursive asserted identifier/label slots, exact current OLS objects
    and current packaged MIM preferred-row joins.
  snapshot_sha256: 5d6007bcf7a5fa727ded8c9d164b88e1e31fe1131e7ab67ed1daa839c67e10b0
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch054/record01/history-and-evidence-inventory.json
  accessed_at: '2026-10-28T04:06:00.137831Z'
  support: context_only
  summary: Complete current history, references and attached evidence; source-specific
    claims are assessed without authenticating historical execution from code.
  snapshot_sha256: dd8dc7f244f63474f0f209dddfb647dbfaf5162e7f3e7f73b5643d2760892f40
- evidence_id: scalars
  kind: record_content
  reference: REVIEW_WORK/batch054/record01/scalar-census.json
  accessed_at: '2026-10-28T04:06:00.137852Z'
  support: context_only
  summary: Lossless scalar census of the selected target and all maintained contributors.
  snapshot_sha256: dc6e12271605e3b018b8ad157913228ad9a21a9027ac9c0329102d0691136dd6
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch054/record01/validate-schema.json
  accessed_at: '2026-10-28T03:58:28.447953Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed

    '
  snapshot_sha256: 7338344269087081fa335f6d5bd6bf5d41eb4808295a48e851c466679c00a22d
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch054/record01/validate-strict.json
  accessed_at: '2026-10-28T03:58:29.551381Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch054/record01/strict.tsv\n"
  snapshot_sha256: 312c416bebe95ed9ea96124bf590aab80b3d7aaf101f7b3ea24273afe5f5c908
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch054/record01/validate-terms.json
  accessed_at: '2026-10-28T03:58:32.431105Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed

    '
  snapshot_sha256: 105c2b598d4d76354702897461a41e99de544fc3ee1e33b116093205dfb18304
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch054/record01/validate-references.json
  accessed_at: '2026-10-28T03:58:33.592067Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed

    '
  snapshot_sha256: 1640efb8fa9ec6d14a467a2145b7e4e6350ad0f49bda5bf360b0920e16dd147e
assessments:
- assessment_id: a1
  area: identity
  topic: Exact accession boundary
  outcome: concern
  summary: TOGO M1304 and provider J1216 agree on BSW3. DSM7 is a different medium.
    The maintained owner already removed this mismatch.
  target_ids:
  - CultureMech:007839
  evidence_ids:
  - togo1304
  - apiJ1216
  - dsm7
  - owner-1
- assessment_id: a2
  area: quantity
  topic: Complete quantity and numeric preparation audit
  outcome: concern
  summary: Every local concentration field has an explicit disposition; source-only
    doses, batch volumes and conditional preparation are separate from receiving-medium
    rates.
  target_ids:
  - CultureMech:007839
  evidence_ids:
  - quantities
  details: '[{"quantity_id": "q1", "topic": "Malt extract (BD-Difco)", "source": {"evidence_id":
    "apiJ1216", "reference": "https://mediadive.dsmz.de/rest/medium/J1216", "raw_path":
    "REVIEW_WORK/batch054/source01-03-extra/apiJ1216.bin", "raw_sha256": "0e70509369f906661249869e31e5de092c4bc604494aaa82796e1f7b92b5e217",
    "locator": "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T04:02:49.091609+00:00"},
    "decision": "evidence_only", "rationale": "Retain the rate: current provider explicitly
    declares g_l on its 1000 mL main-solution basis; the TOGO batch amount agrees.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/BSW3_Agar.yaml", "field_path":
    "ingredients[0].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"},
    "decision": "evidence_only", "rationale": "Retain the rate: current provider explicitly
    declares g_l on its 1000 mL main-solution basis; the TOGO batch amount agrees."}]},
    {"quantity_id": "q2", "topic": "0.1 x Artificial seawater", "source": {"evidence_id":
    "apiJ1216", "reference": "https://mediadive.dsmz.de/rest/medium/J1216", "raw_path":
    "REVIEW_WORK/batch054/source01-03-extra/apiJ1216.bin", "raw_sha256": "0e70509369f906661249869e31e5de092c4bc604494aaa82796e1f7b92b5e217",
    "locator": "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T04:02:49.091609+00:00"},
    "decision": "correct", "rationale": "Replace stale mass dimension using the already
    repaired owner: source specifies a liquid input, not 1 g/L.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/BSW3_Agar.yaml", "field_path": "ingredients[1].concentration",
    "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "Replace stale mass dimension using the already repaired owner: source specifies
    a liquid input, not 1 g/L."}]}, {"quantity_id": "q3", "topic": "Glucose", "source":
    {"evidence_id": "apiJ1216", "reference": "https://mediadive.dsmz.de/rest/medium/J1216",
    "raw_path": "REVIEW_WORK/batch054/source01-03-extra/apiJ1216.bin", "raw_sha256":
    "0e70509369f906661249869e31e5de092c4bc604494aaa82796e1f7b92b5e217", "locator":
    "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T04:02:49.091609+00:00"},
    "decision": "evidence_only", "rationale": "Retain the rate: current provider explicitly
    declares g_l on its 1000 mL main-solution basis; the TOGO batch amount agrees.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/BSW3_Agar.yaml", "field_path":
    "ingredients[2].concentration", "stored_value": {"value": "0.4", "unit": "G_PER_L"},
    "decision": "evidence_only", "rationale": "Retain the rate: current provider explicitly
    declares g_l on its 1000 mL main-solution basis; the TOGO batch amount agrees."}]},
    {"quantity_id": "q4", "topic": "Agar", "source": {"evidence_id": "apiJ1216", "reference":
    "https://mediadive.dsmz.de/rest/medium/J1216", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/apiJ1216.bin",
    "raw_sha256": "0e70509369f906661249869e31e5de092c4bc604494aaa82796e1f7b92b5e217",
    "locator": "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T04:02:49.091609+00:00"},
    "decision": "evidence_only", "rationale": "Retain the rate: current provider explicitly
    declares g_l on its 1000 mL main-solution basis; the TOGO batch amount agrees.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/BSW3_Agar.yaml", "field_path":
    "ingredients[3].concentration", "stored_value": {"value": "15", "unit": "G_PER_L"},
    "decision": "evidence_only", "rationale": "Retain the rate: current provider explicitly
    declares g_l on its 1000 mL main-solution basis; the TOGO batch amount agrees."}]},
    {"quantity_id": "q5", "topic": "Yeast extract (BD-Difco)", "source": {"evidence_id":
    "apiJ1216", "reference": "https://mediadive.dsmz.de/rest/medium/J1216", "raw_path":
    "REVIEW_WORK/batch054/source01-03-extra/apiJ1216.bin", "raw_sha256": "0e70509369f906661249869e31e5de092c4bc604494aaa82796e1f7b92b5e217",
    "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T04:02:49.091609+00:00"},
    "decision": "evidence_only", "rationale": "Retain the rate: current provider explicitly
    declares g_l on its 1000 mL main-solution basis; the TOGO batch amount agrees.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/BSW3_Agar.yaml", "field_path":
    "ingredients[4].concentration", "stored_value": {"value": "0.4", "unit": "G_PER_L"},
    "decision": "evidence_only", "rationale": "Retain the rate: current provider explicitly
    declares g_l on its 1000 mL main-solution basis; the TOGO batch amount agrees."}]},
    {"quantity_id": "q6", "topic": "Yeast extract (BD-Difco)", "source": {"evidence_id":
    "apiJ1216", "reference": "https://mediadive.dsmz.de/rest/medium/J1216", "raw_path":
    "REVIEW_WORK/batch054/source01-03-extra/apiJ1216.bin", "raw_sha256": "0e70509369f906661249869e31e5de092c4bc604494aaa82796e1f7b92b5e217",
    "locator": "$.data.solutions[0].recipe[0]", "accessed_at": "2026-10-28T04:02:49.091609+00:00"},
    "decision": "evidence_only", "rationale": "Retain the rate: current provider explicitly
    declares g_l on its 1000 mL main-solution basis; the TOGO batch amount agrees.",
    "layer_assessments": [{"path": "data/normalized_yaml/bacterial/TOGO_M1304_BSW3_Agar.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "0.4",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Retain the rate:
    current provider explicitly declares g_l on its 1000 mL main-solution basis; the
    TOGO batch amount agrees."}]}, {"quantity_id": "q7", "topic": "Malt extract (BD-Difco)",
    "source": {"evidence_id": "apiJ1216", "reference": "https://mediadive.dsmz.de/rest/medium/J1216",
    "raw_path": "REVIEW_WORK/batch054/source01-03-extra/apiJ1216.bin", "raw_sha256":
    "0e70509369f906661249869e31e5de092c4bc604494aaa82796e1f7b92b5e217", "locator":
    "$.data.solutions[0].recipe[1]", "accessed_at": "2026-10-28T04:02:49.091609+00:00"},
    "decision": "evidence_only", "rationale": "Retain the rate: current provider explicitly
    declares g_l on its 1000 mL main-solution basis; the TOGO batch amount agrees.",
    "layer_assessments": [{"path": "data/normalized_yaml/bacterial/TOGO_M1304_BSW3_Agar.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "evidence_only", "rationale": "Retain the rate: current
    provider explicitly declares g_l on its 1000 mL main-solution basis; the TOGO
    batch amount agrees."}]}, {"quantity_id": "q8", "topic": "Glucose", "source":
    {"evidence_id": "apiJ1216", "reference": "https://mediadive.dsmz.de/rest/medium/J1216",
    "raw_path": "REVIEW_WORK/batch054/source01-03-extra/apiJ1216.bin", "raw_sha256":
    "0e70509369f906661249869e31e5de092c4bc604494aaa82796e1f7b92b5e217", "locator":
    "$.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T04:02:49.091609+00:00"},
    "decision": "evidence_only", "rationale": "Retain the rate: current provider explicitly
    declares g_l on its 1000 mL main-solution basis; the TOGO batch amount agrees.",
    "layer_assessments": [{"path": "data/normalized_yaml/bacterial/TOGO_M1304_BSW3_Agar.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "0.4",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Retain the rate:
    current provider explicitly declares g_l on its 1000 mL main-solution basis; the
    TOGO batch amount agrees."}]}, {"quantity_id": "q9", "topic": "Agar", "source":
    {"evidence_id": "apiJ1216", "reference": "https://mediadive.dsmz.de/rest/medium/J1216",
    "raw_path": "REVIEW_WORK/batch054/source01-03-extra/apiJ1216.bin", "raw_sha256":
    "0e70509369f906661249869e31e5de092c4bc604494aaa82796e1f7b92b5e217", "locator":
    "$.data.solutions[0].recipe[3]", "accessed_at": "2026-10-28T04:02:49.091609+00:00"},
    "decision": "evidence_only", "rationale": "Retain the rate: current provider explicitly
    declares g_l on its 1000 mL main-solution basis; the TOGO batch amount agrees.",
    "layer_assessments": [{"path": "data/normalized_yaml/bacterial/TOGO_M1304_BSW3_Agar.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "15",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Retain the rate:
    current provider explicitly declares g_l on its 1000 mL main-solution basis; the
    TOGO batch amount agrees."}]}, {"quantity_id": "q10", "topic": "0.1 x Artificial
    seawater", "source": {"evidence_id": "apiJ1216", "reference": "https://mediadive.dsmz.de/rest/medium/J1216",
    "raw_path": "REVIEW_WORK/batch054/source01-03-extra/apiJ1216.bin", "raw_sha256":
    "0e70509369f906661249869e31e5de092c4bc604494aaa82796e1f7b92b5e217", "locator":
    "$.data.solutions[0].recipe[4]", "accessed_at": "2026-10-28T04:02:49.091609+00:00"},
    "decision": "evidence_only", "rationale": "Retain 1000 ML_PER_L as the provider
    recipe-basis liquid amount; 0.1 x is source identity, not an independently reconstructed
    seawater composition.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/TOGO_M1304_BSW3_Agar.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "1000",
    "unit": "ML_PER_L"}, "decision": "evidence_only", "rationale": "Retain 1000 ML_PER_L
    as the provider recipe-basis liquid amount; 0.1 x is source identity, not an independently
    reconstructed seawater composition."}]}, {"quantity_id": "q11", "topic": "pH and
    pH adjustment", "source": {"evidence_id": "togo1304", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1304",
    "raw_path": "REVIEW_WORK/batch054/source01-03/togo1304.bin", "raw_sha256": "07a3cc9c3c1e63553208fbc3cdcaed47191f92f9e4197d2d735a2f1f55f2efb5",
    "locator": "$.meta.ph and $.comments[0]", "accessed_at": "2026-10-28T03:59:20.689934+00:00",
    "quote": "Adjust pH to 7.3."}, "decision": "mixed", "rationale": "No sterilization
    cycle is inferred from the unavailable JCM1216 page.", "layer_assessments": [{"path":
    "data/normalized_yaml/bacterial/TOGO_M1304_BSW3_Agar.yaml", "field_path": "ph_value",
    "stored_value": 7.3, "decision": "evidence_only", "rationale": "Current owner
    already retains source pH 7.3."}, {"path": "data/normalized_yaml/bacterial/TOGO_M1304_BSW3_Agar.yaml",
    "field_path": "preparation_steps[0].description", "stored_value": "Adjust BSW3
    Agar to pH 7.3.", "decision": "evidence_only", "rationale": "Existing adjustment
    instruction is supported."}, {"path": "data/merge_yaml/merged/BSW3_Agar.yaml",
    "field_path": "ph_value", "stored_value": null, "decision": "add", "rationale":
    "Propagate already repaired owner pH.", "missing": true}, {"path": "data/merge_yaml/merged/BSW3_Agar.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "Propagate existing owner instruction.", "missing": true}]}, {"quantity_id": "q12",
    "topic": "Artificial seawater stock composition and 0.1 x identity", "source":
    {"evidence_id": "togo1304", "reference": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1304",
    "raw_path": "REVIEW_WORK/batch054/source01-03/togo1304.bin", "raw_sha256": "07a3cc9c3c1e63553208fbc3cdcaed47191f92f9e4197d2d735a2f1f55f2efb5",
    "locator": "$.components[0].items[1]", "accessed_at": "2026-10-28T03:59:20.689934+00:00",
    "quote": "0.1 x Artificial seawater"}, "decision": "unsupported", "rationale":
    "Retain the stated dilution identity and liquid amount. Exact stock composition
    and manufacture are not supplied in these accessible captures; do not guess constituent
    salts.", "layer_assessments": []}]'
- assessment_id: a3
  area: grounding
  topic: Current ontology and MIM correspondence
  outcome: supported
  summary: The grounding inventory enumerates every asserted identifier and exact
    preferred label. Current catalog joins establish present correspondence only;
    unmapped mixtures are not assigned invented chemical identities.
  target_ids:
  - CultureMech:007839
  evidence_ids:
  - grounding
- assessment_id: a4
  area: provenance
  topic: History and evidence scope
  outcome: supported
  summary: Complete owner and target histories were read. Current source bytes and
    inspected code are independent evidence; historical timestamps remain historical
    claims unless an exact cited raw digest is recovered.
  target_ids:
  - CultureMech:007839
  evidence_ids:
  - history
  - scalars
- assessment_id: a5
  area: scope
  topic: Growth and taxonomic evidence
  outcome: unknown
  summary: Generic cultivation applications and bacterial filing are not strain-level
    growth evidence. No organism-specific growth, temperature or atmosphere is inferred
    from names or source catalog identifiers.
  target_ids:
  - CultureMech:007839
  evidence_ids:
  - local-target
- assessment_id: a6
  area: schema
  topic: Canonical diagnostics
  outcome: supported
  summary: All four original canonical diagnostics passed. Reference checks were zero;
    structural and term diagnostics do not establish formulation accuracy.
  target_ids:
  - CultureMech:007839
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Generated seawater unit contradicts its repaired owner
  description: Selected ingredients[1] still says 1 G_PER_L for 0.1 x artificial seawater.
    Both current sources specify 1 L/1000 mL liquid, and the owner already stores
    1000 ML_PER_L. Preserve the existing owner repair and regenerate; this is not
    a new unperformed owner correction.
  target_ids:
  - CultureMech:007839
  field_paths:
  - ingredients[1].concentration
  evidence_ids:
  - local-target
  - owner-1
  - togo1304
  - apiJ1216
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1304_BSW3_Agar.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
  issue_key: culturemech-007839-generated-seawater-unit-contradicts-its-repaired-owner
- finding_id: f2
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Generated DSM7 identity persists after owner correction
  description: The selected kg_microbe_match points to mediadive.medium:7. The exact
    primary DSM7 is a different named formulation; its recipe and strain exception
    do not transfer. The owner already removed this match.
  target_ids:
  - CultureMech:007839
  field_paths:
  - kg_microbe_match
  evidence_ids:
  - local-target
  - owner-1
  - dsm7
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1304_BSW3_Agar.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
  issue_key: culturemech-007839-generated-dsm7-identity-persists-after-owner-correction
- finding_id: f3
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Generated pH, preparation and composition metadata are stale
  description: The owner now contains pH 7.3, its adjustment instruction and SEMI_DEFINED
    classification, with explicit current curation history. The generated target lacks
    the pH/instruction and retains UNDEFINED. Named undefined extracts remain present;
    SEMI_DEFINED does not make their chemical compositions known.
  target_ids:
  - CultureMech:007839
  field_paths:
  - composition_type
  - curation_history
  - ph_value
  - preparation_steps
  evidence_ids:
  - local-target
  - owner-1
  - togo1304
  - apiJ1216
  rule_id: source-stage-or-identity
  native_severity: P3
  normalization_reason: 'Minor: bounded metadata or traceability defect without establishing
    a new formulation.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1304_BSW3_Agar.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
  issue_key: culturemech-007839-generated-ph-preparation-and-composition-metadata-are-stale
actions:
- action_id: action1
  description: Regenerate BSW3 from the repaired sole owner and verify the exact liquid
    amount/unit. Keep the unknown seawater composition explicit rather than inventing
    a stock.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007839
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1304_BSW3_Agar.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action2
  description: Preserve removal of the unrelated DSM7 match when regenerating the
    selected record; retain M1304/J1216 provenance.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007839
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1304_BSW3_Agar.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action3
  description: Regenerate from the current owner, preserving its supported pH, preparation
    and mixture classification and existing repair history. Attach the exact source
    captures to future quantitative curation.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:007839
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M1304_BSW3_Agar.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
limitations:
- JCM1216 currently returns Nothing found despite HTTP200; no original supplier preparation
  beyond the accessible TOGO/provider content is authenticated.
- Exact 0.1 x artificial-seawater composition is absent from the accessible formulation;
  no salt recipe, sterilization cycle or growth claim is inferred.
- Current ontology objects establish label/identifier correspondence, not strain growth
  or biochemical purity.
notes:
- Fresh review; historical lost snapshots were not reconstructed. All inspected source
  files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this
  author.
```
