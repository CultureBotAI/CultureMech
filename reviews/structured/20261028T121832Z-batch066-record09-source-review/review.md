# Source and chemical identity review of CRBTM UGA Aerobic MES

- Review: 20261028T121832Z-batch066-record09-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T12:03:06.254229Z
- Finished UTC: 2026-10-28T12:18:32.961514Z
- Reviewer: Codex independent source reviewer (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact FEBA MES definition and its two named 1X mixtures support all 32 stored numerical amounts, but a phosphate component is omitted and the D,L-lactate label conflicts with its L-specific ontology term. The local calcium pantothenate molecular-weight note omits the hemicalcium basis named in source vocabulary. The inaccessible CultureBotHT import snapshot prevents full historical authentication; all four canonical diagnostics pass.

## Scope And Provenance

Full selected record and exact maintained contributors; explicitly scoped dependency and external-source limits retained.

Selection: Actual batch066 native selection index 09.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:015505 | data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml | generated | CRBTM UGA Aerobic MES |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:015505 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-strict | passed | True | CultureMech:015505 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-terms | passed | True | CultureMech:015505 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-references | passed | True | CultureMech:015505 | Native reference checker performed zero reference checks; this is not claim authentication. |

## Scientific And Domain Assessments

### Exact medium and maintained owner

identity: supported. Targets: CultureMech:015505.

The singleton generated lineage resolves to the exact normalized MES record. FEBA names and describes this same MES/aerobic variant; nearby MOPS and anaerobic media are excluded.

### Classification and mixture boundaries

representation: concern. Targets: CultureMech:015505.

Defined liquid formulation is consistent with the exact source chemical components and Minimal TRUE metadata. Repeated magnesium, sodium chloride and calcium entries denote basal versus mineral-mixture contributions; they are not automatically duplicates. The missing vitamin-mixture phosphate is material.

### Conditions and preparation

completeness: unknown. Targets: CultureMech:015505.

The descriptive aerobic/pH5.5 context matches FEBA. The inspected FEBA block supplies no sterilization, vessel, inoculum, temperature or final preparation protocol. Optional absent fields are not populated by borrowing from siblings or the organism abstract.

### Organism context versus tested formulation

scope: supported. Targets: CultureMech:015505.

PMID41615186 and DOI10.1128/aem.01942-25 support environmental Castellaniella MT123 identity/context. They do not, from the inspected abstract alone, prove this exact source MES definition was used or that every listed condition is experimentally validated. No taxonomy identifier or new growth assertion is proposed.

### Linkage coverage and legacy flag

grounding: concern. Targets: CultureMech:015505.

Each of32 direct ingredients has a CHEBI term; zero of32 carries a mediaingredientmech_term field. These are linkage counts, not accuracy scores. The current has_unmapped_ingredients flag is stale relative to present term occupancy, but removing it must not conceal the lactate identity defect.

### Quantity scope and inventory

quantity: concern. Targets: CultureMech:015505.

Every selected target/owner concentration field has an explicit disposition; scoped dependency fields and source-only preparation are separate from receiving-medium rates.

[{"quantity_id": "q1", "topic": "Ammonium Chloride", "source": {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "line 4803", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "Ammonium Chloride\t3.74E+00\tmM"}, "decision": "evidence_only", "rationale": "Direct medium component. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "3.74E+00", "unit": "MILLIMOLAR"}, "decision": "evidence_only", "rationale": "Direct medium component. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "3.74E+00", "unit": "MILLIMOLAR"}, "decision": "evidence_only", "rationale": "Direct medium component. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}]}, {"quantity_id": "q2", "topic": "Potassium Chloride", "source": {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "line 4804", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "Potassium Chloride\t1.34E+00\tmM"}, "decision": "evidence_only", "rationale": "Direct medium component. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "1.34E+00", "unit": "MILLIMOLAR"}, "decision": "evidence_only", "rationale": "Direct medium component. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "1.34E+00", "unit": "MILLIMOLAR"}, "decision": "evidence_only", "rationale": "Direct medium component. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}]}, {"quantity_id": "q3", "topic": "Magnesium sulfate heptahydrate", "source": {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "line 4805", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "Magnesium sulfate heptahydrate\t2\tmM"}, "decision": "evidence_only", "rationale": "Direct medium component. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "2", "unit": "MILLIMOLAR"}, "decision": "evidence_only", "rationale": "Direct medium component. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "2", "unit": "MILLIMOLAR"}, "decision": "evidence_only", "rationale": "Direct medium component. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}]}, {"quantity_id": "q4", "topic": "Calcium chloride dihydrate", "source": {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "line 4806", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "Calcium chloride dihydrate\t0.1\tmM"}, "decision": "evidence_only", "rationale": "Direct medium component. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.1", "unit": "MILLIMOLAR"}, "decision": "evidence_only", "rationale": "Direct medium component. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "0.1", "unit": "MILLIMOLAR"}, "decision": "evidence_only", "rationale": "Direct medium component. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}]}, {"quantity_id": "q5", "topic": "Sodium Chloride", "source": {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "line 4807", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "Sodium Chloride\t0.17\tmM"}, "decision": "evidence_only", "rationale": "Direct medium component. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.17", "unit": "MILLIMOLAR"}, "decision": "evidence_only", "rationale": "Direct medium component. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.17", "unit": "MILLIMOLAR"}, "decision": "evidence_only", "rationale": "Direct medium component. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}]}, {"quantity_id": "q6", "topic": "EDTA", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 886", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "EDTA\t5\tmg/L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "5.0", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "5.0", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 884", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "line 4808", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe's mineral mix\t1\tX"}]}, {"quantity_id": "q7", "topic": "Magnesium Sulfate Heptahydrate", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 887", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Magnesium Sulfate Heptahydrate\t3\tmg/L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "3.0", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "3.0", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 884", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "line 4808", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe's mineral mix\t1\tX"}]}, {"quantity_id": "q8", "topic": "Manganese (II) sulfate monohydrate", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 888", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Manganese (II) sulfate monohydrate\t5\tmg/L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "5.0", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "5.0", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 884", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "line 4808", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe's mineral mix\t1\tX"}]}, {"quantity_id": "q9", "topic": "Sodium Chloride", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 889", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Sodium Chloride\t10\tmg/L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "10.0", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "10.0", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 884", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "line 4808", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe's mineral mix\t1\tX"}]}, {"quantity_id": "q10", "topic": "Iron (II) sulfate heptahydrate", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 890", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Iron (II) sulfate heptahydrate\t1\tmg/L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "1.0", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "1.0", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 884", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "line 4808", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe's mineral mix\t1\tX"}]}, {"quantity_id": "q11", "topic": "Cobalt(II) nitrate hexahydrate", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 891", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Cobalt(II) nitrate hexahydrate\t1\tmg/L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "1.0", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "1.0", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 884", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "line 4808", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe's mineral mix\t1\tX"}]}, {"quantity_id": "q12", "topic": "Calcium Chloride Dihydrate", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 892", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Calcium Chloride Dihydrate\t1\tmg/L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "1.0", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "1.0", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 884", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "line 4808", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe's mineral mix\t1\tX"}]}, {"quantity_id": "q13", "topic": "Zinc sulfate heptahydrate", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 893", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Zinc sulfate heptahydrate\t1\tmg/L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "1.0", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "1.0", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 884", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "line 4808", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe's mineral mix\t1\tX"}]}, {"quantity_id": "q14", "topic": "Copper (II) sulfate pentahydrate", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 894", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Copper (II) sulfate pentahydrate\t0.1\tmg/L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.1", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.1", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 884", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "line 4808", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe's mineral mix\t1\tX"}]}, {"quantity_id": "q15", "topic": "Aluminum potassium sulfate dodecahydrate", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 895", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Aluminum potassium sulfate dodecahydrate\t0.1\tmg/L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "0.1", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path": "ingredients[14].concentration", "stored_value": {"value": "0.1", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 884", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "line 4808", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe's mineral mix\t1\tX"}]}, {"quantity_id": "q16", "topic": "Boric Acid", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 896", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Boric Acid\t0.1\tmg/L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.1", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.1", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 884", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "line 4808", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe's mineral mix\t1\tX"}]}, {"quantity_id": "q17", "topic": "Sodium Molybdate Dihydrate", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 897", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Sodium Molybdate Dihydrate\t0.1\tmg/L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.1", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.1", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 884", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "line 4808", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe's mineral mix\t1\tX"}]}, {"quantity_id": "q18", "topic": "Sodium selenite pentahydrate", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 898", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Sodium selenite pentahydrate\t0.01\tmg/L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.01", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.01", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 884", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "line 4808", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe's mineral mix\t1\tX"}]}, {"quantity_id": "q19", "topic": "Sodium tungstate dihydrate", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 899", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Sodium tungstate dihydrate\t0.1\tmg/L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.1", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.1", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 884", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "line 4808", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe's mineral mix\t1\tX"}]}, {"quantity_id": "q20", "topic": "Nickel (II) chloride hexahydrate", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 900", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Nickel (II) chloride hexahydrate\t0.2\tmg/L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[19].concentration", "stored_value": {"value": "0.2", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path": "ingredients[19].concentration", "stored_value": {"value": "0.2", "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 884", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "line 4808", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe's mineral mix\t1\tX"}]}, {"quantity_id": "q21", "topic": "Folic Acid", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 855", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Folic Acid\t20\tug/L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[20].concentration", "stored_value": {"value": "20.0", "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path": "ingredients[20].concentration", "stored_value": {"value": "20.0", "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 853", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "line 4809", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe's vitamin mix\t1\tX"}]}, {"quantity_id": "q22", "topic": "Pyridoxine HCl", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 856", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Pyridoxine HCl\t100\tug/L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[21].concentration", "stored_value": {"value": "100.0", "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path": "ingredients[21].concentration", "stored_value": {"value": "100.0", "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 853", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "line 4809", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe's vitamin mix\t1\tX"}]}, {"quantity_id": "q23", "topic": "Riboflavin", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 857", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Riboflavin\t50\tug/L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[22].concentration", "stored_value": {"value": "50.0", "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path": "ingredients[22].concentration", "stored_value": {"value": "50.0", "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 853", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "line 4809", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe's vitamin mix\t1\tX"}]}, {"quantity_id": "q24", "topic": "biotin", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 858", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "biotin\t20\tug/L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[23].concentration", "stored_value": {"value": "20.0", "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path": "ingredients[23].concentration", "stored_value": {"value": "20.0", "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 853", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "line 4809", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe's vitamin mix\t1\tX"}]}, {"quantity_id": "q25", "topic": "Thiamine HCl", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 859", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Thiamine HCl\t50\tug/L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[24].concentration", "stored_value": {"value": "50.0", "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path": "ingredients[24].concentration", "stored_value": {"value": "50.0", "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 853", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "line 4809", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe's vitamin mix\t1\tX"}]}, {"quantity_id": "q26", "topic": "Nicotinic Acid", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 860", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Nicotinic Acid\t50\tug/L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[25].concentration", "stored_value": {"value": "50.0", "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path": "ingredients[25].concentration", "stored_value": {"value": "50.0", "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 853", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "line 4809", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe's vitamin mix\t1\tX"}]}, {"quantity_id": "q27", "topic": "calcium pantothenate", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 861", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "calcium pantothenate\t50\tug/L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot. The mass amount needs no molecular-weight conversion. FEBA explicitly includes a hemicalcium-salt synonym, consistent with approximately half the OLS full calcium-salt formula mass of 476.536. The local MW 238.27 note omits that basis; clarify the note without converting the supported mass amount. The source mixed D/D,L aliases remain a stereochemical limitation.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[26].concentration", "stored_value": {"value": "50.0", "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot. The mass amount needs no molecular-weight conversion. FEBA explicitly includes a hemicalcium-salt synonym, consistent with approximately half the OLS full calcium-salt formula mass of 476.536. The local MW 238.27 note omits that basis; clarify the note without converting the supported mass amount. The source mixed D/D,L aliases remain a stereochemical limitation."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path": "ingredients[26].concentration", "stored_value": {"value": "50.0", "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot. The mass amount needs no molecular-weight conversion. FEBA explicitly includes a hemicalcium-salt synonym, consistent with approximately half the OLS full calcium-salt formula mass of 476.536. The local MW 238.27 note omits that basis; clarify the note without converting the supported mass amount. The source mixed D/D,L aliases remain a stereochemical limitation."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 853", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "line 4809", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe's vitamin mix\t1\tX"}]}, {"quantity_id": "q28", "topic": "Cyanocobalamin", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 862", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Cyanocobalamin\t1\tug/L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[27].concentration", "stored_value": {"value": "1.0", "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path": "ingredients[27].concentration", "stored_value": {"value": "1.0", "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 853", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "line 4809", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe's vitamin mix\t1\tX"}]}, {"quantity_id": "q29", "topic": "4-Aminobenzoic acid", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 863", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "4-Aminobenzoic acid\t50\tug/L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[28].concentration", "stored_value": {"value": "50.0", "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path": "ingredients[28].concentration", "stored_value": {"value": "50.0", "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 853", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "line 4809", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe's vitamin mix\t1\tX"}]}, {"quantity_id": "q30", "topic": "Lipoic acid", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 864", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Lipoic acid\t50\tug/L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[29].concentration", "stored_value": {"value": "50.0", "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path": "ingredients[29].concentration", "stored_value": {"value": "50.0", "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly defined at X=1 and included at1X in this exact medium. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 853", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "line 4809", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe's vitamin mix\t1\tX"}]}, {"quantity_id": "q31", "topic": "Sodium D,L-Lactate", "source": {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "line 4810", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "Sodium D,L-Lactate\t20\tmM"}, "decision": "evidence_only", "rationale": "Direct medium component. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot. The numerical amount is supported for source Sodium D,L-Lactate, but CHEBI232798 is L-specific; do not treat the current ontology term or molecular-weight note as verified.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[30].concentration", "stored_value": {"value": "20", "unit": "MILLIMOLAR"}, "decision": "evidence_only", "rationale": "Direct medium component. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot. The numerical amount is supported for source Sodium D,L-Lactate, but CHEBI232798 is L-specific; do not treat the current ontology term or molecular-weight note as verified."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path": "ingredients[30].concentration", "stored_value": {"value": "20", "unit": "MILLIMOLAR"}, "decision": "evidence_only", "rationale": "Direct medium component. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot. The numerical amount is supported for source Sodium D,L-Lactate, but CHEBI232798 is L-specific; do not treat the current ontology term or molecular-weight note as verified."}]}, {"quantity_id": "q32", "topic": "MES sodium salt", "source": {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "line 4811", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "MES sodium salt\t40\tmM"}, "decision": "evidence_only", "rationale": "Direct medium component. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[31].concentration", "stored_value": {"value": "40", "unit": "MILLIMOLAR"}, "decision": "evidence_only", "rationale": "Direct medium component. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path": "ingredients[31].concentration", "stored_value": {"value": "40", "unit": "MILLIMOLAR"}, "decision": "evidence_only", "rationale": "Direct medium component. The stored numerical amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level evidence; this decision does not authenticate the inaccessible historical import snapshot."}]}, {"quantity_id": "q33", "topic": "Omitted vitamin-mixture phosphate", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 865", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Potassium phosphate monobasic\t0.9\tg/L"}, "decision": "add", "rationale": "The selected vitamin mixture includes potassium phosphate monobasic at0.9g/L atX=1 and the exact MES definition includes that mixture at1X. Both local ingredient arrays omit this component. The separate phosphate-free mixture is not named by the selected source. Reconcile the missing component against the historical import version before curation; preserve explicit source disagreement if intentional variant evidence emerges.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[32]", "stored_value": null, "decision": "add", "rationale": "The selected vitamin mixture includes potassium phosphate monobasic at0.9g/L atX=1 and the exact MES definition includes that mixture at1X. Both local ingredient arrays omit this component. The separate phosphate-free mixture is not named by the selected source. Reconcile the missing component against the historical import version before curation; preserve explicit source disagreement if intentional variant evidence emerges.", "missing": true}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path": "ingredients[32]", "stored_value": null, "decision": "add", "rationale": "The selected vitamin mixture includes potassium phosphate monobasic at0.9g/L atX=1 and the exact MES definition includes that mixture at1X. Both local ingredient arrays omit this component. The separate phosphate-free mixture is not named by the selected source. Reconcile the missing component against the historical import version before curation; preserve explicit source disagreement if intentional variant evidence emerges.", "missing": true}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256": "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator": "line 853", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"}, {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "line 4809", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe's vitamin mix\t1\tX"}]}, {"quantity_id": "q34", "topic": "Source mixture inclusion", "source": {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "line 4808", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe's mineral mix\t1\tX"}, "decision": "evidence_only", "rationale": "Source1X inclusion is represented by component-level contributions. Retain its provenance; do not add a full stock again on top of the expanded ingredients. No mixing volume or preparation protocol is supplied.", "layer_assessments": []}, {"quantity_id": "q35", "topic": "Source mixture inclusion", "source": {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "line 4809", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe's vitamin mix\t1\tX"}, "decision": "evidence_only", "rationale": "Source1X inclusion is represented by component-level contributions. Retain its provenance; do not add a full stock again on top of the expanded ingredients. No mixing volume or preparation protocol is supplied.", "layer_assessments": []}, {"quantity_id": "q36", "topic": "Source condition description", "source": {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "line 4800", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "Description\tUGA media for MT123 aerobic growth with MES buffer, for growth at pH5.5\t"}, "decision": "verified", "rationale": "Source description retained without transfer from MOPS or anaerobic sibling. Structured pH can be considered only with this source-description scope.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "description", "stored_value": "UGA media for MT123 aerobic growth with MES buffer, for growth at pH5.5", "decision": "verified", "rationale": "The current description matches the exact FEBA MES description, including its aerobic context and pH5.5 label; no incubation protocol or demonstrated growth yield is inferred."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path": "description", "stored_value": "UGA media for MT123 aerobic growth with MES buffer, for growth at pH5.5", "decision": "verified", "rationale": "The current description matches the exact FEBA MES description, including its aerobic context and pH5.5 label; no incubation protocol or demonstrated growth yield is inferred."}]}]

### Current ontology and MIM correspondence

grounding: concern. Targets: CultureMech:015505.

All64 target/owner term slots join to current OLS exact objects and the packaged MIM index. The L-specific lactate identity conflicts with the source D,L descriptor. Hydrate labels including corrected manganese sulfate monohydrate agree. The source hemicalcium wording is credited; its basis is missing from the local molecular-weight note, and mixed D/D,L aliases plus lipoic-acid CAS cross-reference coverage remain bounded; catalog coverage alone does not establish source form.

### History and evidence scope

provenance: concern. Targets: CultureMech:015505.

Complete target/owner histories and both historical32-row reports were inspected. Present manganese grounding is credited. Generic CultureBotHT provenance is not recoverable through the exact API endpoints; FEBA revision and source-locator evidence are independently recoverable. No existing history or scientific record was changed.

### Growth and taxonomic evidence

scope: unknown. Targets: CultureMech:015505.

Generic cultivation applications and bacterial filing are not strain-level growth evidence. No organism-specific growth, temperature or atmosphere is inferred from names or source catalog identifiers.

### Canonical diagnostics

schema: supported. Targets: CultureMech:015505.

All four original canonical diagnostics passed. Reference checks were zero; structural and term diagnostics do not establish formulation accuracy.

## Findings

### f1: A named mixture component is missing

major / open / confirmed; issue key: culturemech-015505-a-named-mixture-component-is-missing.

The exact FEBA MES definition includes ATCC Wolfe vitamin mixture at1X. That definition includes potassium phosphate monobasic, absent from target and owner. A separately named phosphate-free variant exists but is not referenced here. Reconcile this source discrepancy with the missing historical CultureBotHT snapshot; do not claim an intentional omission or blend variants without evidence.

### f2: Lactate stereochemistry does not match the source

major / open / confirmed; issue key: culturemech-015505-lactate-stereochemistry-does-not-match-the-source.

Source and local preferred term specify Sodium D,L-Lactate, while CHEBI232798 is sodium L-lactate. The exact ontology label exists but denotes a narrower stereochemical identity. Source compound and local notes also carry CAS50-21-5/MW90.08, which do not match the current term CAS867-56-1/MW112.06. Resolve the source identity with supplier/form evidence before assigning a replacement; retain the source-stated numerical concentration without using these notes for conversion.

### f3: Molecular weight notes need an explicit formula basis

minor / open / confirmed; issue key: culturemech-015505-molecular-weight-notes-need-an-explicit-formula-basis.

The local calcium pantothenate note records MW 238.27 without a formula basis. FEBA explicitly includes a hemicalcium-salt synonym, consistent with approximately half the current OLS full calcium-salt formula mass of 476.536. Credit that source wording and clarify the local note; the source mixed D/D,L aliases remain a separate stereochemical limitation. Preserve the supported mass concentration and do not silently convert it to molarity.

### f4: Exact source evidence and current quality metadata are missing

minor / open / confirmed; issue key: culturemech-015505-exact-source-evidence-and-current-quality-metadata-are-missing.

The generic CultureBotHT URL currently returns404 through its API, and no imported commit is recorded. Attach the recoverable versioned FEBA definition and mixture locators to supported ingredient evidence, preserving that the historical import remains unavailable. Reassess the unmapped flag against current term occupancy and retain the grounding conflict explicitly. Preserve all existing history entries.

## Recommended Actions And Acceptance Checks

### action1

The exact FEBA MES definition includes ATCC Wolfe vitamin mixture at1X. That definition includes potassium phosphate monobasic, absent from target and owner. A separately named phosphate-free variant exists but is not referenced here. Reconcile this source discrepancy with the missing historical CultureBotHT snapshot; do not claim an intentional omission or blend variants without evidence.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action2

Source and local preferred term specify Sodium D,L-Lactate, while CHEBI232798 is sodium L-lactate. The exact ontology label exists but denotes a narrower stereochemical identity. Source compound and local notes also carry CAS50-21-5/MW90.08, which do not match the current term CAS867-56-1/MW112.06. Resolve the source identity with supplier/form evidence before assigning a replacement; retain the source-stated numerical concentration without using these notes for conversion.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action3

The local calcium pantothenate note records MW 238.27 without a formula basis. FEBA explicitly includes a hemicalcium-salt synonym, consistent with approximately half the current OLS full calcium-salt formula mass of 476.536. Credit that source wording and clarify the local note; the source mixed D/D,L aliases remain a separate stereochemical limitation. Preserve the supported mass concentration and do not silently convert it to molarity.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action4

The generic CultureBotHT URL currently returns404 through its API, and no imported commit is recorded. Attach the recoverable versioned FEBA definition and mixture locators to supported ingredient evidence, preserving that the historical import remains unavailable. Reassess the unmapped flag against current term occupancy and retain the grounding conflict explicitly. Preserve all existing history entries.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local-target | data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml; Complete document | context_only | Complete selected generated record; no changes made. |
| owner-1 | data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| identity-search | REVIEW_WORK/batch066/record09/identity-search.json | supports | Exact generated lineage resolves every maintained contributor; no filename-only transfer from neighboring variants. |
| febaCommit | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/commits/master?pagelen=1; Commit hash | context_only | Current FEBA revision resolved to 803273865ea9e83fab770ec4f13670db80e1180b; the source captures use this exact immutable revision. |
| febaMedia | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media; lines 4799–4812 | supports | Exact selected MES block, including source name, description, seven direct components and two 1X mixture references. MOPS and anaerobic blocks are separate variants. |
| febaMixes | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes; lines 851–901 | supports | Complete named ATCC vitamin and mineral mixture definitions, including their X=1 headers. The separately named phosphate-free vitamin variant is a boundary control, not the selected source. |
| febaCompounds | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv; Exact corresponding ingredient vocabulary rows, particularly lines 92,283,380 | context_only | Exact vocabulary rows corresponding to local ingredient labels checked as source metadata. Chemical notes do not by themselves validate chemical identity. |
| culturebotRepo | https://api.github.com/repos/CultureBotAI/CultureBotHT; HTTP404 response | context_only | The declared CultureBotHT repository API returned404. This does not establish deletion or public/private status. |
| culturebotCommit | https://api.github.com/repos/CultureBotAI/CultureBotHT/commits/main; HTTP404 response | context_only | The declared CultureBotHT main revision endpoint returned404; no historical imported revision is authenticated. |
| mt123RecentMetadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1128/aem.01942-25&amp;format=json&amp;resultType=core; resultList.result[0]: id41615186, doi, title, abstractText, affiliation | supports | Europe PMC primary-publication abstract explicitly identifies Castellaniella sp. strain MT123 as an isolate from acidic nitrate-contaminated groundwater; UGA affiliation and DOI10.1128/aem.01942-25 are returned. This is organism-context evidence, not an exact MES recipe or growth-protocol validation. |
| chemical-notes | REVIEW_WORK/batch066/record09/chemical-note-joins.json | context_only | All32 chemical descriptors retain exact source vocabulary matches, current OLS formula/mass/CAS and explicit limits. No conversion uses unresolved metadata. |
| historical-1 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/specialized/crbtm_uga_aerobic_mes.md; Complete document | context_only | Full exact-header report; all32 rows were previously source-unchecked. The two bodies after Ownership are byte-identical. Their source-incomplete conclusions are historical context, not current source verification. |
| historical-2 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.md; Complete document | context_only | Full exact-header report; all32 rows were previously source-unchecked. The two bodies after Ownership are byte-identical. Their source-incomplete conclusions are historical context, not current source verification. |
| writer-import | scripts/import_from_culturebotht.py; CultureBotHTImporter.transform_medium; import_file | context_only | Current transform copies the source record, appends the generic repository URL and import history, and sets an unmapped flag when term IDs are missing. It neither expands FEBA mixtures nor adds source version or narrow evidence. Present code does not authenticate the historical import. |
| writer-merge | src/culturemech/merge/merger.py; merge_group single-contributor branch | context_only | Current single-contributor merge copies the owner and adds lineage/fingerprint. It cannot restore omitted source components. Generated targets must be regenerated after maintained-input curation. |
| writer-omissions | scripts/repair_culturebotht_omissions_score30.py; TARGETS; _require_source; _omitted_components; repair_record; plan_repairs | context_only | Current repair uses a fixed selected list of omission variants; an exhaustive exact-text check of this file found neither the target slug nor ID. It is not an applied repair for this record. No execution is proposed. |
| chebi31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31795; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86158; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi4735 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:4735; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86364 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86364; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi75836 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75836; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86214 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86214; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi32312 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32312; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi31440 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31440; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi86465 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86465; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131361; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63939; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53542; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:27470; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30961; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17015; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15956; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49105; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31345; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi17439 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17439; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16494; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi232798 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:232798; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi62955 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:62955; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| quantities | REVIEW_WORK/batch066/record09/quantity-inventory.json | context_only | Complete local concentration and source-stage decision inventory; includes exact local paths and source failure limits. |
| grounding | REVIEW_WORK/batch066/record09/grounding-inventory.json | context_only | All recursive asserted identifier/label slots, exact current OLS objects and current packaged MIM preferred-row joins. |
| history | REVIEW_WORK/batch066/record09/history-and-evidence-inventory.json | context_only | Complete current history, references and attached evidence; source-specific claims are assessed without authenticating historical execution from code. |
| scalars | REVIEW_WORK/batch066/record09/scalar-census.json | context_only | Lossless scalar census of the selected target and all maintained contributors. |
| validate-schema | REVIEW_WORK/batch066/record09/validate-schema.json | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed<br> |
| validate-strict | REVIEW_WORK/batch066/record09/validate-strict.json | supports | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch066/record09/strict.tsv<br> |
| validate-terms | REVIEW_WORK/batch066/record09/validate-terms.json | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed<br> |
| validate-references | REVIEW_WORK/batch066/record09/validate-references.json | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed<br> |

## Limits And Additional Notes

- The CultureBotHT repository and revision API endpoints returned404. This cannot establish repository deletion or reconstruct the historical imported snapshot. The review is partial for that provenance gap.
- Current versioned FEBA is source evidence for its own definition, not proof that its content exactly matches the historical CultureBotHT import. The missing component finding preserves that distinction.
- The exact MES source block and its named mixtures were assessed; sibling MOPS, anaerobic and phosphate-free variants are excluded from adopted formulation. No extra stock is added on top of expanded ingredients.
- The MT123 primary-publication abstract establishes organism context only. Full-paper recipe equivalence, taxonomy grounding, actual growth performance and incubation protocol were not established. iModulonDB is not applicable to this formulation review.
- All source numerical amounts agree with existing fields, but missing ingredient-level evidence and the lactate identity conflict remain. FEBA hemicalcium wording provides a formula-basis explanation omitted from the local note; mixed D/D,L source aliases do not independently settle stereochemistry. No mass/molar conversion is performed.
- OLS lipoic-acid CAS cross-references do not include the source/local CAS; this is unresolved cross-reference coverage, not a confirmed incorrect CAS assertion.
- Canonical reference validation performed zero reference checks. Current history and source provenance were reviewed manually; unchanged-recipe whole-corpus product/ID/merge gates were not rerun.
- No recipe, generated data, scientific status or history was changed. Current writer functions are ownership context and do not prove historical execution.
- Fresh review; historical lost snapshots were not reconstructed. All inspected source files remain unchanged.
- This draft authoring step performed no formal review validation/save, Git mutation or publication.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T121832Z-batch066-record09-source-review
kind: record
repository: CultureBotAI/CultureMech
title: Source and chemical identity review of CRBTM UGA Aerobic MES
started_at: '2026-10-28T12:03:06.254229Z'
finished_at: '2026-10-28T12:18:32.961514Z'
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
summary: The exact FEBA MES definition and its two named 1X mixtures support all 32
  stored numerical amounts, but a phosphate component is omitted and the D,L-lactate
  label conflicts with its L-specific ontology term. The local calcium pantothenate
  molecular-weight note omits the hemicalcium basis named in source vocabulary. The
  inaccessible CultureBotHT import snapshot prevents full historical authentication;
  all four canonical diagnostics pass.
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
  - path: data/culturemech_id_registry.tsv
    sha256: 0d059720f5c474b63daff8d5010fc56942a5a3ac30761ee75ce9e84801d555a5
    role: context
  - path: data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml
    sha256: ce9b2cdcc3f8dc392f9f6cef523cc85c56780239e7d786c0f7681dde04a14eb4
    role: target
  - path: data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml
    sha256: ae513c9223b5de161333af84b646e8e1fad5a47b0844aa2029b40612dc0baf46
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.md
    sha256: 4b56a2d1d1c840158cec737613b0c951540b784d682923475ff04e7b47e39ef5
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/specialized/crbtm_uga_aerobic_mes.md
    sha256: 48256f60eb824200a5e0eabb6ba4f5d0d43f3dd4bf2e96a23ea59b722a1a1dd2
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/assign_culturemech_ids.py
    sha256: 81ed213c52804ae98a8add02730d757595e3287fa7b01bc88aee0e587bbb01e1
    role: context
  - path: scripts/cleanup_media_quality.py
    sha256: 8cf7e2c2dfce42ac20b69a73d571d1b81e8f60617d85350aefaa300426dc28fc
    role: context
  - path: scripts/cleanup_recipe_ingredients.py
    sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
    role: context
  - path: scripts/import_from_culturebotht.py
    sha256: d835addf5fff423a9b0b1231848ed3103c5b2d97015c1c294365970d15be0fe1
    role: context
  - path: scripts/migrate_chebi_regrounding.py
    sha256: bb174120fd6fcd1d3ed56092000fe54e6660fea4aabae7fece43a122dbd8d544
    role: context
  - path: scripts/migrate_legacy_fields.py
    sha256: 13738616213c958af4a3d6d37bd22c798f530544b52829ca81780279abcd2a73
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
    role: context
  - path: scripts/normalize_media_names_to_snake_case.py
    sha256: 59bd842b1982b7d62af9db3fe280df576d8c4ae2e9ee411bf2e52523355f95de
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/record_target_class.py
    sha256: 468fcbfd2362ca08b7066d6f21adf85c04f21ab40f80e60995522b4edc0f6349
    role: context
  - path: scripts/repair_culturebotht_omissions_score30.py
    sha256: 3f415d4f8037ebd1f21154c4e63b675dfbda53c0ff3544e2b9cc69e7d6e82b0b
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
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
  description: Full selected record and exact maintained contributors; explicitly
    scoped dependency and external-source limits retained.
  selection: Actual batch066 native selection index 09.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:015505
targets:
- target_id: CultureMech:015505
  path: data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml
  label: CRBTM UGA Aerobic MES
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:015505
  command: just validate-schema data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml
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
  - CultureMech:015505
  command: just validate-strict data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml
    --out REVIEW_WORK/batch066/record09/strict.tsv --workers 1 --quiet
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
  - CultureMech:015505
  command: just validate-terms data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml
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
  - CultureMech:015505
  command: just validate-references data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
  scope_note: Exact selected target; scientific source and owner assessments are separate.
evidence:
- evidence_id: local-target
  kind: record_content
  reference: data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml
  locator: Complete document
  accessed_at: '2026-10-28T12:11:37.794731Z'
  support: context_only
  summary: Complete selected generated record; no changes made.
  snapshot_sha256: ce9b2cdcc3f8dc392f9f6cef523cc85c56780239e7d786c0f7681dde04a14eb4
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml
  locator: Complete document
  accessed_at: '2026-10-28T12:11:37.794731Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: ae513c9223b5de161333af84b646e8e1fad5a47b0844aa2029b40612dc0baf46
- evidence_id: identity-search
  kind: search
  reference: REVIEW_WORK/batch066/record09/identity-search.json
  accessed_at: '2026-10-28T12:11:37.848681Z'
  support: supports
  summary: Exact generated lineage resolves every maintained contributor; no filename-only
    transfer from neighboring variants.
  search_scope: Complete recursive normalized YAML filename census including ignored
    and hidden paths; exact merged_from stems and stable identity resolve the owner;
    excluded namesakes are retained in the census. Similar names and source accessions
    are not promoted to owners.
  snapshot_sha256: d0385e11b916a83feb2c9f98ce531d4706c78b035beb0b78156f3d139ab20491
- evidence_id: febaCommit
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/commits/master?pagelen=1
  locator: Commit hash
  accessed_at: '2026-10-28T12:03:13.671489Z'
  support: context_only
  summary: Current FEBA revision resolved to 803273865ea9e83fab770ec4f13670db80e1180b;
    the source captures use this exact immutable revision.
  snapshot_sha256: e802ea5aee4c66aa42d5425b9aac40af420f9072365b3963288985afa771a498
- evidence_id: febaMedia
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media
  locator: lines 4799–4812
  accessed_at: '2026-10-28T12:04:02.975336Z'
  support: supports
  summary: Exact selected MES block, including source name, description, seven direct
    components and two 1X mixture references. MOPS and anaerobic blocks are separate
    variants.
  snapshot_sha256: a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848
- evidence_id: febaMixes
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes
  locator: lines 851–901
  accessed_at: '2026-10-28T12:04:02.959506Z'
  support: supports
  summary: Complete named ATCC vitamin and mineral mixture definitions, including
    their X=1 headers. The separately named phosphate-free vitamin variant is a boundary
    control, not the selected source.
  snapshot_sha256: b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4
- evidence_id: febaCompounds
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv
  locator: Exact corresponding ingredient vocabulary rows, particularly lines 92,283,380
  accessed_at: '2026-10-28T12:04:02.986663Z'
  support: context_only
  summary: Exact vocabulary rows corresponding to local ingredient labels checked
    as source metadata. Chemical notes do not by themselves validate chemical identity.
  snapshot_sha256: 25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774
- evidence_id: culturebotRepo
  kind: database
  reference: https://api.github.com/repos/CultureBotAI/CultureBotHT
  locator: HTTP404 response
  accessed_at: '2026-10-28T12:04:03.173550Z'
  support: context_only
  summary: The declared CultureBotHT repository API returned404. This does not establish
    deletion or public/private status.
  snapshot_sha256: 4f50e254a719a6b1b06b529bdaa08980e4acf0878aad0090cba7771f6ebdf0b9
- evidence_id: culturebotCommit
  kind: database
  reference: https://api.github.com/repos/CultureBotAI/CultureBotHT/commits/main
  locator: HTTP404 response
  accessed_at: '2026-10-28T12:03:13.163513Z'
  support: context_only
  summary: The declared CultureBotHT main revision endpoint returned404; no historical
    imported revision is authenticated.
  snapshot_sha256: c391981e33b3d73d489d22c8ae4da47417d407010e28de24ee4b1a1673554ba5
- evidence_id: mt123RecentMetadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1128/aem.01942-25&format=json&resultType=core
  locator: 'resultList.result[0]: id41615186, doi, title, abstractText, affiliation'
  accessed_at: '2026-10-28T12:04:58.377798Z'
  support: supports
  summary: Europe PMC primary-publication abstract explicitly identifies Castellaniella
    sp. strain MT123 as an isolate from acidic nitrate-contaminated groundwater; UGA
    affiliation and DOI10.1128/aem.01942-25 are returned. This is organism-context
    evidence, not an exact MES recipe or growth-protocol validation.
  snapshot_sha256: 25197943a5914d0567965f1943f40e964ef72025df8232c885e4c495447e178d
- evidence_id: chemical-notes
  kind: record_content
  reference: REVIEW_WORK/batch066/record09/chemical-note-joins.json
  accessed_at: '2026-10-28T12:18:32.961451Z'
  support: context_only
  summary: All32 chemical descriptors retain exact source vocabulary matches, current
    OLS formula/mass/CAS and explicit limits. No conversion uses unresolved metadata.
  snapshot_sha256: 5b6481330e792971ac2d7ca05363d360dc3c5df7d4ce0db8a46ac18b21969c2d
- evidence_id: historical-1
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/specialized/crbtm_uga_aerobic_mes.md
  locator: Complete document
  accessed_at: '2026-10-28T12:11:37.794731Z'
  support: context_only
  summary: Full exact-header report; all32 rows were previously source-unchecked.
    The two bodies after Ownership are byte-identical. Their source-incomplete conclusions
    are historical context, not current source verification.
  snapshot_sha256: 48256f60eb824200a5e0eabb6ba4f5d0d43f3dd4bf2e96a23ea59b722a1a1dd2
- evidence_id: historical-2
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.md
  locator: Complete document
  accessed_at: '2026-10-28T12:11:37.794731Z'
  support: context_only
  summary: Full exact-header report; all32 rows were previously source-unchecked.
    The two bodies after Ownership are byte-identical. Their source-incomplete conclusions
    are historical context, not current source verification.
  snapshot_sha256: 4b56a2d1d1c840158cec737613b0c951540b784d682923475ff04e7b47e39ef5
- evidence_id: writer-import
  kind: record_content
  reference: scripts/import_from_culturebotht.py
  locator: CultureBotHTImporter.transform_medium; import_file
  accessed_at: '2026-10-28T12:11:37.794731Z'
  support: context_only
  summary: Current transform copies the source record, appends the generic repository
    URL and import history, and sets an unmapped flag when term IDs are missing. It
    neither expands FEBA mixtures nor adds source version or narrow evidence. Present
    code does not authenticate the historical import.
  snapshot_sha256: d835addf5fff423a9b0b1231848ed3103c5b2d97015c1c294365970d15be0fe1
- evidence_id: writer-merge
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: merge_group single-contributor branch
  accessed_at: '2026-10-28T12:11:37.794731Z'
  support: context_only
  summary: Current single-contributor merge copies the owner and adds lineage/fingerprint.
    It cannot restore omitted source components. Generated targets must be regenerated
    after maintained-input curation.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-omissions
  kind: record_content
  reference: scripts/repair_culturebotht_omissions_score30.py
  locator: TARGETS; _require_source; _omitted_components; repair_record; plan_repairs
  accessed_at: '2026-10-28T12:11:37.794731Z'
  support: context_only
  summary: Current repair uses a fixed selected list of omission variants; an exhaustive
    exact-text check of this file found neither the target slug nor ID. It is not
    an applied repair for this record. No execution is proposed.
  snapshot_sha256: 3f415d4f8037ebd1f21154c4e63b675dfbda53c0ff3544e2b9cc69e7d6e82b0b
- evidence_id: chebi31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31206
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T12:04:05.530922Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 645112dbfa7f1c565489070586f5d4018429259ff0400500ca10dfe6e43a5449
- evidence_id: chebi32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32588
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T12:04:06.137446Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 9494b26ad5d3ce43942c3e859cdefe4114e111b1d45328c0cd5faf3b75faec00
- evidence_id: chebi31795
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31795
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T12:04:05.863763Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: ceb0c93d1964844e99454d74730971855710441d92eec74aff5c873c833e324a
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86158
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T12:04:07.380188Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: eacf58308fa876cb17661b82d08a64d9be24814fde8014ac82da7696b3684841
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:26710
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T12:04:04.970972Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 70cf14c35e06f40427c1a2aa30e99794518eda976b5e5b3c86610efc28b7f25a
- evidence_id: chebi4735
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:4735
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T12:04:06.571299Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: cbb8a2d2fd80b7e771711746d09aee7aaf9a8ac2dabc853617c1c08b49db4908
- evidence_id: chebi86364
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86364
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T12:04:07.534858Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 6e685ea7654bc1f4e16b3e3a05d73d8541e84cddcc28de59c4ae57ac288a1505
- evidence_id: chebi75836
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75836
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T12:04:07.251146Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: ab9922083bab0fb07df977855094d11fe3a5ca1f14bc6bddd10dc80ad9055569
- evidence_id: chebi86214
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86214
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T12:04:07.468312Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 9523f9163575dfb800448b401eb6eb5e75e892c56ff33c1134894e2b5d58779c
- evidence_id: chebi32312
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:32312
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T12:04:06.039368Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 19bbc18dfc582e76457c6f08d51bb777a2f7a2cbd2f810cb3b58bdb0004b4d60
- evidence_id: chebi31440
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31440
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T12:04:05.646922Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: a0af950191bab322f858a701486e40e51a4780a18d9d03913d351b383f05cb7d
- evidence_id: chebi86465
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86465
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T12:04:07.537086Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 76cce7fa8230c57138e3569858ecf6a79119be85281bd5d2864ada3223785dc1
- evidence_id: chebi33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:33118
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T12:04:06.256766Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: eef160dcdcd93f231064bc7b59da1e05a2efe1f96089b9cd2fdbdf68a9a4e5fc
- evidence_id: chebi75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:75213
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T12:04:06.942745Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: f99a2d8b28ac44913a666745dd70098c5d5f21c9513fee921a35f0fd18f2c445
- evidence_id: chebi131361
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:131361
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T12:04:03.589968Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: d88b30f797a300c3935e550a4770cb598bbed342a9c2a343f77bdce496e99db9
- evidence_id: chebi63939
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:63939
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T12:04:06.910977Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 01f41117ab89dbd1d514a894850dc06afd5d95c0bee7fd89f7dfdb54c309c514
- evidence_id: chebi53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:53542
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T12:04:06.734994Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 1e44a068cfe6b98d7bb3b0240ffdc0611e1be59f2d3dab9f04e4162ed94e4444
- evidence_id: chebi27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:27470
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T12:04:05.036224Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: e1820a7a704794fa20995eea5037e03c2b22b847817c28bb2f45f80762c275d1
- evidence_id: chebi30961
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30961
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T12:04:05.419301Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 855ea2cf0e89d25ab4a560ab1c2dab6ac861d215bc5473cb4d3a0a2d4cdff438
- evidence_id: chebi17015
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17015
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T12:04:04.351031Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 17f7ac7c03d75b85a96f951321902906266f3ce8fa44faea4814fac46560e3e6
- evidence_id: chebi15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15956
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T12:04:04.170018Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 5135a39e8b52c878896db22443f00507125db80e5ce4bb1dcc97914b9bdd7316
- evidence_id: chebi49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:49105
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T12:04:06.652675Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: f9dbae8cd2dcbd38d914abb99730e341ff280d3a44f20f95b2663e47664780cf
- evidence_id: chebi15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:15940
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T12:04:04.023322Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: c291a1c1bb0d6af05ac4005af0957534f430db47e7df9cec874f8a94d961dba1
- evidence_id: chebi31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:31345
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T12:04:05.733083Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: c3341e7cf8a7ea0768d505265376c1514f161c9048b6e878314e204341d702eb
- evidence_id: chebi17439
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17439
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T12:04:04.621730Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 71dca75ee64801424c519bde7667291decd3b97f0c4e46c3d9b9405fa04a71d4
- evidence_id: chebi30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:30753
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T12:04:05.254182Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 1340e054634ce960494b9388f6e3fd231d9e7d66969c3c11932ee2058171fd2c
- evidence_id: chebi16494
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16494
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T12:04:04.252461Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 192c51f672f633c6071a3397d5785fb2bca6eaf8f9b787f7aaaa6c2aeb3b1a2f
- evidence_id: chebi232798
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:232798
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T12:04:04.803766Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: e4ec30f25cb150a18cf079d820943cdc9f6b849b2fae5b6448d6cad204994a4c
- evidence_id: chebi62955
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:62955
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T12:08:01.855788Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 7012589f7e4d0b6a7f2fa050105239ba13d1ddf1dc6afd112378312dec9b5e68
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch066/record09/quantity-inventory.json
  accessed_at: '2026-10-28T12:18:32.961511Z'
  support: context_only
  summary: Complete local concentration and source-stage decision inventory; includes
    exact local paths and source failure limits.
  snapshot_sha256: 8c4524c4258ee305121f834907fcb49bded7baf331554cafd3838c473036450b
- evidence_id: grounding
  kind: record_content
  reference: REVIEW_WORK/batch066/record09/grounding-inventory.json
  accessed_at: '2026-10-28T12:11:37.905625Z'
  support: context_only
  summary: All recursive asserted identifier/label slots, exact current OLS objects
    and current packaged MIM preferred-row joins.
  snapshot_sha256: 6e82b99381e5767c12ecb587d5b32dc8b8f285952d417c42b0128401a5aa90dd
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch066/record09/history-and-evidence-inventory.json
  accessed_at: '2026-10-28T12:11:37.905713Z'
  support: context_only
  summary: Complete current history, references and attached evidence; source-specific
    claims are assessed without authenticating historical execution from code.
  snapshot_sha256: 603a84a853a468f0982823399c3b4b437e2a991847064e94b5d2723f8e0c4eec
- evidence_id: scalars
  kind: record_content
  reference: REVIEW_WORK/batch066/record09/scalar-census.json
  accessed_at: '2026-10-28T12:11:37.905735Z'
  support: context_only
  summary: Lossless scalar census of the selected target and all maintained contributors.
  snapshot_sha256: 11e5c0288eea6bec87ab63af43f5ad1a9fe271cbce2be7ed1f0f6bbeefc93230
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch066/record09/validate-schema.json
  accessed_at: '2026-10-28T12:03:07.428735Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed

    '
  snapshot_sha256: f6d040b13c18416d56cd479cc614fcd6e5b6974ae2e93c93188e8b34ed520715
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch066/record09/validate-strict.json
  accessed_at: '2026-10-28T12:03:08.422909Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch066/record09/strict.tsv\n"
  snapshot_sha256: 3a114a3a7085014f824acbe9b52987d4396371969b84b8263ebd339c533dfc70
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch066/record09/validate-terms.json
  accessed_at: '2026-10-28T12:03:09.517916Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed

    '
  snapshot_sha256: 9ea5e04bc5255039ada8d75e0e3f882c0e5f6972a43b88d2a2efb26ed6fcc180
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch066/record09/validate-references.json
  accessed_at: '2026-10-28T12:03:10.277540Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed

    '
  snapshot_sha256: 6a446c0d10ca4b34d491789d96d5b12a6a6a6e0b2e713afefc6c511370ca95d9
assessments:
- assessment_id: a1
  area: identity
  topic: Exact medium and maintained owner
  outcome: supported
  summary: The singleton generated lineage resolves to the exact normalized MES record.
    FEBA names and describes this same MES/aerobic variant; nearby MOPS and anaerobic
    media are excluded.
  target_ids:
  - CultureMech:015505
  evidence_ids:
  - local-target
  - owner-1
  - identity-search
  - febaMedia
- assessment_id: a2
  area: representation
  topic: Classification and mixture boundaries
  outcome: concern
  summary: Defined liquid formulation is consistent with the exact source chemical
    components and Minimal TRUE metadata. Repeated magnesium, sodium chloride and
    calcium entries denote basal versus mineral-mixture contributions; they are not
    automatically duplicates. The missing vitamin-mixture phosphate is material.
  target_ids:
  - CultureMech:015505
  evidence_ids:
  - local-target
  - febaMedia
  - febaMixes
- assessment_id: a3
  area: completeness
  topic: Conditions and preparation
  outcome: unknown
  summary: The descriptive aerobic/pH5.5 context matches FEBA. The inspected FEBA
    block supplies no sterilization, vessel, inoculum, temperature or final preparation
    protocol. Optional absent fields are not populated by borrowing from siblings
    or the organism abstract.
  target_ids:
  - CultureMech:015505
  evidence_ids:
  - local-target
  - febaMedia
  - mt123RecentMetadata
- assessment_id: a4
  area: scope
  topic: Organism context versus tested formulation
  outcome: supported
  summary: PMID41615186 and DOI10.1128/aem.01942-25 support environmental Castellaniella
    MT123 identity/context. They do not, from the inspected abstract alone, prove
    this exact source MES definition was used or that every listed condition is experimentally
    validated. No taxonomy identifier or new growth assertion is proposed.
  target_ids:
  - CultureMech:015505
  evidence_ids:
  - febaMedia
  - mt123RecentMetadata
- assessment_id: a5
  area: grounding
  topic: Linkage coverage and legacy flag
  outcome: concern
  summary: Each of32 direct ingredients has a CHEBI term; zero of32 carries a mediaingredientmech_term
    field. These are linkage counts, not accuracy scores. The current has_unmapped_ingredients
    flag is stale relative to present term occupancy, but removing it must not conceal
    the lactate identity defect.
  target_ids:
  - CultureMech:015505
  evidence_ids:
  - local-target
  - owner-1
- assessment_id: a6
  area: quantity
  topic: Quantity scope and inventory
  outcome: concern
  summary: Every selected target/owner concentration field has an explicit disposition;
    scoped dependency fields and source-only preparation are separate from receiving-medium
    rates.
  target_ids:
  - CultureMech:015505
  evidence_ids:
  - quantities
  details: '[{"quantity_id": "q1", "topic": "Ammonium Chloride", "source": {"evidence_id":
    "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "line 4803", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "Ammonium
    Chloride\t3.74E+00\tmM"}, "decision": "evidence_only", "rationale": "Direct medium
    component. The stored numerical amount and unit agree with versioned FEBA. Retain
    the amount and attach ingredient-level evidence; this decision does not authenticate
    the inaccessible historical import snapshot.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[0].concentration",
    "stored_value": {"value": "3.74E+00", "unit": "MILLIMOLAR"}, "decision": "evidence_only",
    "rationale": "Direct medium component. The stored numerical amount and unit agree
    with versioned FEBA. Retain the amount and attach ingredient-level evidence; this
    decision does not authenticate the inaccessible historical import snapshot."},
    {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path":
    "ingredients[0].concentration", "stored_value": {"value": "3.74E+00", "unit":
    "MILLIMOLAR"}, "decision": "evidence_only", "rationale": "Direct medium component.
    The stored numerical amount and unit agree with versioned FEBA. Retain the amount
    and attach ingredient-level evidence; this decision does not authenticate the
    inaccessible historical import snapshot."}]}, {"quantity_id": "q2", "topic": "Potassium
    Chloride", "source": {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "line 4804", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "Potassium
    Chloride\t1.34E+00\tmM"}, "decision": "evidence_only", "rationale": "Direct medium
    component. The stored numerical amount and unit agree with versioned FEBA. Retain
    the amount and attach ingredient-level evidence; this decision does not authenticate
    the inaccessible historical import snapshot.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[1].concentration",
    "stored_value": {"value": "1.34E+00", "unit": "MILLIMOLAR"}, "decision": "evidence_only",
    "rationale": "Direct medium component. The stored numerical amount and unit agree
    with versioned FEBA. Retain the amount and attach ingredient-level evidence; this
    decision does not authenticate the inaccessible historical import snapshot."},
    {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path":
    "ingredients[1].concentration", "stored_value": {"value": "1.34E+00", "unit":
    "MILLIMOLAR"}, "decision": "evidence_only", "rationale": "Direct medium component.
    The stored numerical amount and unit agree with versioned FEBA. Retain the amount
    and attach ingredient-level evidence; this decision does not authenticate the
    inaccessible historical import snapshot."}]}, {"quantity_id": "q3", "topic": "Magnesium
    sulfate heptahydrate", "source": {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "line 4805", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "Magnesium
    sulfate heptahydrate\t2\tmM"}, "decision": "evidence_only", "rationale": "Direct
    medium component. The stored numerical amount and unit agree with versioned FEBA.
    Retain the amount and attach ingredient-level evidence; this decision does not
    authenticate the inaccessible historical import snapshot.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[2].concentration",
    "stored_value": {"value": "2", "unit": "MILLIMOLAR"}, "decision": "evidence_only",
    "rationale": "Direct medium component. The stored numerical amount and unit agree
    with versioned FEBA. Retain the amount and attach ingredient-level evidence; this
    decision does not authenticate the inaccessible historical import snapshot."},
    {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path":
    "ingredients[2].concentration", "stored_value": {"value": "2", "unit": "MILLIMOLAR"},
    "decision": "evidence_only", "rationale": "Direct medium component. The stored
    numerical amount and unit agree with versioned FEBA. Retain the amount and attach
    ingredient-level evidence; this decision does not authenticate the inaccessible
    historical import snapshot."}]}, {"quantity_id": "q4", "topic": "Calcium chloride
    dihydrate", "source": {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "line 4806", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "Calcium chloride
    dihydrate\t0.1\tmM"}, "decision": "evidence_only", "rationale": "Direct medium
    component. The stored numerical amount and unit agree with versioned FEBA. Retain
    the amount and attach ingredient-level evidence; this decision does not authenticate
    the inaccessible historical import snapshot.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml", "field_path": "ingredients[3].concentration",
    "stored_value": {"value": "0.1", "unit": "MILLIMOLAR"}, "decision": "evidence_only",
    "rationale": "Direct medium component. The stored numerical amount and unit agree
    with versioned FEBA. Retain the amount and attach ingredient-level evidence; this
    decision does not authenticate the inaccessible historical import snapshot."},
    {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml", "field_path":
    "ingredients[3].concentration", "stored_value": {"value": "0.1", "unit": "MILLIMOLAR"},
    "decision": "evidence_only", "rationale": "Direct medium component. The stored
    numerical amount and unit agree with versioned FEBA. Retain the amount and attach
    ingredient-level evidence; this decision does not authenticate the inaccessible
    historical import snapshot."}]}, {"quantity_id": "q5", "topic": "Sodium Chloride",
    "source": {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "line 4807", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "Sodium Chloride\t0.17\tmM"},
    "decision": "evidence_only", "rationale": "Direct medium component. The stored
    numerical amount and unit agree with versioned FEBA. Retain the amount and attach
    ingredient-level evidence; this decision does not authenticate the inaccessible
    historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.17",
    "unit": "MILLIMOLAR"}, "decision": "evidence_only", "rationale": "Direct medium
    component. The stored numerical amount and unit agree with versioned FEBA. Retain
    the amount and attach ingredient-level evidence; this decision does not authenticate
    the inaccessible historical import snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "0.17",
    "unit": "MILLIMOLAR"}, "decision": "evidence_only", "rationale": "Direct medium
    component. The stored numerical amount and unit agree with versioned FEBA. Retain
    the amount and attach ingredient-level evidence; this decision does not authenticate
    the inaccessible historical import snapshot."}]}, {"quantity_id": "q6", "topic":
    "EDTA", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 886", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "EDTA\t5\tmg/L"},
    "decision": "evidence_only", "rationale": "Named mixture explicitly defined at
    X=1 and included at1X in this exact medium. The stored numerical amount and unit
    agree with versioned FEBA. Retain the amount and attach ingredient-level evidence;
    this decision does not authenticate the inaccessible historical import snapshot.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "5.0",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "5.0",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 884", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "line 4808", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe''s
    mineral mix\t1\tX"}]}, {"quantity_id": "q7", "topic": "Magnesium Sulfate Heptahydrate",
    "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 887", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Magnesium
    Sulfate Heptahydrate\t3\tmg/L"}, "decision": "evidence_only", "rationale": "Named
    mixture explicitly defined at X=1 and included at1X in this exact medium. The
    stored numerical amount and unit agree with versioned FEBA. Retain the amount
    and attach ingredient-level evidence; this decision does not authenticate the
    inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "3.0",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "3.0",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 884", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "line 4808", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe''s
    mineral mix\t1\tX"}]}, {"quantity_id": "q8", "topic": "Manganese (II) sulfate
    monohydrate", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 888", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Manganese
    (II) sulfate monohydrate\t5\tmg/L"}, "decision": "evidence_only", "rationale":
    "Named mixture explicitly defined at X=1 and included at1X in this exact medium.
    The stored numerical amount and unit agree with versioned FEBA. Retain the amount
    and attach ingredient-level evidence; this decision does not authenticate the
    inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "5.0",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "5.0",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 884", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "line 4808", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe''s
    mineral mix\t1\tX"}]}, {"quantity_id": "q9", "topic": "Sodium Chloride", "source":
    {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 889", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Sodium Chloride\t10\tmg/L"},
    "decision": "evidence_only", "rationale": "Named mixture explicitly defined at
    X=1 and included at1X in this exact medium. The stored numerical amount and unit
    agree with versioned FEBA. Retain the amount and attach ingredient-level evidence;
    this decision does not authenticate the inaccessible historical import snapshot.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "10.0",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "10.0",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 884", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "line 4808", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe''s
    mineral mix\t1\tX"}]}, {"quantity_id": "q10", "topic": "Iron (II) sulfate heptahydrate",
    "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 890", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Iron (II)
    sulfate heptahydrate\t1\tmg/L"}, "decision": "evidence_only", "rationale": "Named
    mixture explicitly defined at X=1 and included at1X in this exact medium. The
    stored numerical amount and unit agree with versioned FEBA. Retain the amount
    and attach ingredient-level evidence; this decision does not authenticate the
    inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "1.0",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "1.0",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 884", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "line 4808", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe''s
    mineral mix\t1\tX"}]}, {"quantity_id": "q11", "topic": "Cobalt(II) nitrate hexahydrate",
    "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 891", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Cobalt(II)
    nitrate hexahydrate\t1\tmg/L"}, "decision": "evidence_only", "rationale": "Named
    mixture explicitly defined at X=1 and included at1X in this exact medium. The
    stored numerical amount and unit agree with versioned FEBA. Retain the amount
    and attach ingredient-level evidence; this decision does not authenticate the
    inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "1.0",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "1.0",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 884", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "line 4808", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe''s
    mineral mix\t1\tX"}]}, {"quantity_id": "q12", "topic": "Calcium Chloride Dihydrate",
    "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 892", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Calcium Chloride
    Dihydrate\t1\tmg/L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "1.0",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "1.0",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 884", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "line 4808", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe''s
    mineral mix\t1\tX"}]}, {"quantity_id": "q13", "topic": "Zinc sulfate heptahydrate",
    "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 893", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Zinc sulfate
    heptahydrate\t1\tmg/L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "1.0",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "1.0",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 884", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "line 4808", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe''s
    mineral mix\t1\tX"}]}, {"quantity_id": "q14", "topic": "Copper (II) sulfate pentahydrate",
    "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 894", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Copper (II)
    sulfate pentahydrate\t0.1\tmg/L"}, "decision": "evidence_only", "rationale": "Named
    mixture explicitly defined at X=1 and included at1X in this exact medium. The
    stored numerical amount and unit agree with versioned FEBA. Retain the amount
    and attach ingredient-level evidence; this decision does not authenticate the
    inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.1",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.1",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 884", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "line 4808", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe''s
    mineral mix\t1\tX"}]}, {"quantity_id": "q15", "topic": "Aluminum potassium sulfate
    dodecahydrate", "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 895", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Aluminum potassium
    sulfate dodecahydrate\t0.1\tmg/L"}, "decision": "evidence_only", "rationale":
    "Named mixture explicitly defined at X=1 and included at1X in this exact medium.
    The stored numerical amount and unit agree with versioned FEBA. Retain the amount
    and attach ingredient-level evidence; this decision does not authenticate the
    inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml",
    "field_path": "ingredients[14].concentration", "stored_value": {"value": "0.1",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml",
    "field_path": "ingredients[14].concentration", "stored_value": {"value": "0.1",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 884", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "line 4808", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe''s
    mineral mix\t1\tX"}]}, {"quantity_id": "q16", "topic": "Boric Acid", "source":
    {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 896", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Boric Acid\t0.1\tmg/L"},
    "decision": "evidence_only", "rationale": "Named mixture explicitly defined at
    X=1 and included at1X in this exact medium. The stored numerical amount and unit
    agree with versioned FEBA. Retain the amount and attach ingredient-level evidence;
    this decision does not authenticate the inaccessible historical import snapshot.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml",
    "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.1",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml",
    "field_path": "ingredients[15].concentration", "stored_value": {"value": "0.1",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 884", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "line 4808", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe''s
    mineral mix\t1\tX"}]}, {"quantity_id": "q17", "topic": "Sodium Molybdate Dihydrate",
    "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 897", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Sodium Molybdate
    Dihydrate\t0.1\tmg/L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml",
    "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.1",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml",
    "field_path": "ingredients[16].concentration", "stored_value": {"value": "0.1",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 884", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "line 4808", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe''s
    mineral mix\t1\tX"}]}, {"quantity_id": "q18", "topic": "Sodium selenite pentahydrate",
    "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 898", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Sodium selenite
    pentahydrate\t0.01\tmg/L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml",
    "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.01",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml",
    "field_path": "ingredients[17].concentration", "stored_value": {"value": "0.01",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 884", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "line 4808", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe''s
    mineral mix\t1\tX"}]}, {"quantity_id": "q19", "topic": "Sodium tungstate dihydrate",
    "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 899", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Sodium tungstate
    dihydrate\t0.1\tmg/L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml",
    "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.1",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml",
    "field_path": "ingredients[18].concentration", "stored_value": {"value": "0.1",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 884", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "line 4808", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe''s
    mineral mix\t1\tX"}]}, {"quantity_id": "q20", "topic": "Nickel (II) chloride hexahydrate",
    "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 900", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Nickel (II)
    chloride hexahydrate\t0.2\tmg/L"}, "decision": "evidence_only", "rationale": "Named
    mixture explicitly defined at X=1 and included at1X in this exact medium. The
    stored numerical amount and unit agree with versioned FEBA. Retain the amount
    and attach ingredient-level evidence; this decision does not authenticate the
    inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml",
    "field_path": "ingredients[19].concentration", "stored_value": {"value": "0.2",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml",
    "field_path": "ingredients[19].concentration", "stored_value": {"value": "0.2",
    "unit": "MG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 884", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "line 4808", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe''s
    mineral mix\t1\tX"}]}, {"quantity_id": "q21", "topic": "Folic Acid", "source":
    {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 855", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Folic Acid\t20\tug/L"},
    "decision": "evidence_only", "rationale": "Named mixture explicitly defined at
    X=1 and included at1X in this exact medium. The stored numerical amount and unit
    agree with versioned FEBA. Retain the amount and attach ingredient-level evidence;
    this decision does not authenticate the inaccessible historical import snapshot.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml",
    "field_path": "ingredients[20].concentration", "stored_value": {"value": "20.0",
    "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml",
    "field_path": "ingredients[20].concentration", "stored_value": {"value": "20.0",
    "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 853", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "line 4809", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe''s
    vitamin mix\t1\tX"}]}, {"quantity_id": "q22", "topic": "Pyridoxine HCl", "source":
    {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 856", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Pyridoxine
    HCl\t100\tug/L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly
    defined at X=1 and included at1X in this exact medium. The stored numerical amount
    and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml",
    "field_path": "ingredients[21].concentration", "stored_value": {"value": "100.0",
    "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml",
    "field_path": "ingredients[21].concentration", "stored_value": {"value": "100.0",
    "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 853", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "line 4809", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe''s
    vitamin mix\t1\tX"}]}, {"quantity_id": "q23", "topic": "Riboflavin", "source":
    {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 857", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Riboflavin\t50\tug/L"},
    "decision": "evidence_only", "rationale": "Named mixture explicitly defined at
    X=1 and included at1X in this exact medium. The stored numerical amount and unit
    agree with versioned FEBA. Retain the amount and attach ingredient-level evidence;
    this decision does not authenticate the inaccessible historical import snapshot.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml",
    "field_path": "ingredients[22].concentration", "stored_value": {"value": "50.0",
    "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml",
    "field_path": "ingredients[22].concentration", "stored_value": {"value": "50.0",
    "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 853", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "line 4809", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe''s
    vitamin mix\t1\tX"}]}, {"quantity_id": "q24", "topic": "biotin", "source": {"evidence_id":
    "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 858", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "biotin\t20\tug/L"},
    "decision": "evidence_only", "rationale": "Named mixture explicitly defined at
    X=1 and included at1X in this exact medium. The stored numerical amount and unit
    agree with versioned FEBA. Retain the amount and attach ingredient-level evidence;
    this decision does not authenticate the inaccessible historical import snapshot.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml",
    "field_path": "ingredients[23].concentration", "stored_value": {"value": "20.0",
    "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml",
    "field_path": "ingredients[23].concentration", "stored_value": {"value": "20.0",
    "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 853", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "line 4809", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe''s
    vitamin mix\t1\tX"}]}, {"quantity_id": "q25", "topic": "Thiamine HCl", "source":
    {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 859", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Thiamine HCl\t50\tug/L"},
    "decision": "evidence_only", "rationale": "Named mixture explicitly defined at
    X=1 and included at1X in this exact medium. The stored numerical amount and unit
    agree with versioned FEBA. Retain the amount and attach ingredient-level evidence;
    this decision does not authenticate the inaccessible historical import snapshot.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml",
    "field_path": "ingredients[24].concentration", "stored_value": {"value": "50.0",
    "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml",
    "field_path": "ingredients[24].concentration", "stored_value": {"value": "50.0",
    "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 853", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "line 4809", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe''s
    vitamin mix\t1\tX"}]}, {"quantity_id": "q26", "topic": "Nicotinic Acid", "source":
    {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 860", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Nicotinic
    Acid\t50\tug/L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly
    defined at X=1 and included at1X in this exact medium. The stored numerical amount
    and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml",
    "field_path": "ingredients[25].concentration", "stored_value": {"value": "50.0",
    "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml",
    "field_path": "ingredients[25].concentration", "stored_value": {"value": "50.0",
    "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 853", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "line 4809", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe''s
    vitamin mix\t1\tX"}]}, {"quantity_id": "q27", "topic": "calcium pantothenate",
    "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 861", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "calcium pantothenate\t50\tug/L"},
    "decision": "evidence_only", "rationale": "Named mixture explicitly defined at
    X=1 and included at1X in this exact medium. The stored numerical amount and unit
    agree with versioned FEBA. Retain the amount and attach ingredient-level evidence;
    this decision does not authenticate the inaccessible historical import snapshot.
    The mass amount needs no molecular-weight conversion. FEBA explicitly includes
    a hemicalcium-salt synonym, consistent with approximately half the OLS full calcium-salt
    formula mass of 476.536. The local MW 238.27 note omits that basis; clarify the
    note without converting the supported mass amount. The source mixed D/D,L aliases
    remain a stereochemical limitation.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml",
    "field_path": "ingredients[26].concentration", "stored_value": {"value": "50.0",
    "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot. The mass amount needs no molecular-weight conversion. FEBA explicitly
    includes a hemicalcium-salt synonym, consistent with approximately half the OLS
    full calcium-salt formula mass of 476.536. The local MW 238.27 note omits that
    basis; clarify the note without converting the supported mass amount. The source
    mixed D/D,L aliases remain a stereochemical limitation."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml",
    "field_path": "ingredients[26].concentration", "stored_value": {"value": "50.0",
    "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot. The mass amount needs no molecular-weight conversion. FEBA explicitly
    includes a hemicalcium-salt synonym, consistent with approximately half the OLS
    full calcium-salt formula mass of 476.536. The local MW 238.27 note omits that
    basis; clarify the note without converting the supported mass amount. The source
    mixed D/D,L aliases remain a stereochemical limitation."}], "basis_controls":
    [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 853", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "line 4809", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe''s
    vitamin mix\t1\tX"}]}, {"quantity_id": "q28", "topic": "Cyanocobalamin", "source":
    {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 862", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Cyanocobalamin\t1\tug/L"},
    "decision": "evidence_only", "rationale": "Named mixture explicitly defined at
    X=1 and included at1X in this exact medium. The stored numerical amount and unit
    agree with versioned FEBA. Retain the amount and attach ingredient-level evidence;
    this decision does not authenticate the inaccessible historical import snapshot.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml",
    "field_path": "ingredients[27].concentration", "stored_value": {"value": "1.0",
    "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml",
    "field_path": "ingredients[27].concentration", "stored_value": {"value": "1.0",
    "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 853", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "line 4809", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe''s
    vitamin mix\t1\tX"}]}, {"quantity_id": "q29", "topic": "4-Aminobenzoic acid",
    "source": {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 863", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "4-Aminobenzoic
    acid\t50\tug/L"}, "decision": "evidence_only", "rationale": "Named mixture explicitly
    defined at X=1 and included at1X in this exact medium. The stored numerical amount
    and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml",
    "field_path": "ingredients[28].concentration", "stored_value": {"value": "50.0",
    "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml",
    "field_path": "ingredients[28].concentration", "stored_value": {"value": "50.0",
    "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 853", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "line 4809", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe''s
    vitamin mix\t1\tX"}]}, {"quantity_id": "q30", "topic": "Lipoic acid", "source":
    {"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 864", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Lipoic acid\t50\tug/L"},
    "decision": "evidence_only", "rationale": "Named mixture explicitly defined at
    X=1 and included at1X in this exact medium. The stored numerical amount and unit
    agree with versioned FEBA. Retain the amount and attach ingredient-level evidence;
    this decision does not authenticate the inaccessible historical import snapshot.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml",
    "field_path": "ingredients[29].concentration", "stored_value": {"value": "50.0",
    "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml",
    "field_path": "ingredients[29].concentration", "stored_value": {"value": "50.0",
    "unit": "MICROG_PER_L"}, "decision": "evidence_only", "rationale": "Named mixture
    explicitly defined at X=1 and included at1X in this exact medium. The stored numerical
    amount and unit agree with versioned FEBA. Retain the amount and attach ingredient-level
    evidence; this decision does not authenticate the inaccessible historical import
    snapshot."}], "basis_controls": [{"evidence_id": "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 853", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "line 4809", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe''s
    vitamin mix\t1\tX"}]}, {"quantity_id": "q31", "topic": "Sodium D,L-Lactate", "source":
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "line 4810", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "Sodium D,L-Lactate\t20\tmM"},
    "decision": "evidence_only", "rationale": "Direct medium component. The stored
    numerical amount and unit agree with versioned FEBA. Retain the amount and attach
    ingredient-level evidence; this decision does not authenticate the inaccessible
    historical import snapshot. The numerical amount is supported for source Sodium
    D,L-Lactate, but CHEBI232798 is L-specific; do not treat the current ontology
    term or molecular-weight note as verified.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml",
    "field_path": "ingredients[30].concentration", "stored_value": {"value": "20",
    "unit": "MILLIMOLAR"}, "decision": "evidence_only", "rationale": "Direct medium
    component. The stored numerical amount and unit agree with versioned FEBA. Retain
    the amount and attach ingredient-level evidence; this decision does not authenticate
    the inaccessible historical import snapshot. The numerical amount is supported
    for source Sodium D,L-Lactate, but CHEBI232798 is L-specific; do not treat the
    current ontology term or molecular-weight note as verified."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml",
    "field_path": "ingredients[30].concentration", "stored_value": {"value": "20",
    "unit": "MILLIMOLAR"}, "decision": "evidence_only", "rationale": "Direct medium
    component. The stored numerical amount and unit agree with versioned FEBA. Retain
    the amount and attach ingredient-level evidence; this decision does not authenticate
    the inaccessible historical import snapshot. The numerical amount is supported
    for source Sodium D,L-Lactate, but CHEBI232798 is L-specific; do not treat the
    current ontology term or molecular-weight note as verified."}]}, {"quantity_id":
    "q32", "topic": "MES sodium salt", "source": {"evidence_id": "febaMedia", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "line 4811", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "MES sodium
    salt\t40\tmM"}, "decision": "evidence_only", "rationale": "Direct medium component.
    The stored numerical amount and unit agree with versioned FEBA. Retain the amount
    and attach ingredient-level evidence; this decision does not authenticate the
    inaccessible historical import snapshot.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml",
    "field_path": "ingredients[31].concentration", "stored_value": {"value": "40",
    "unit": "MILLIMOLAR"}, "decision": "evidence_only", "rationale": "Direct medium
    component. The stored numerical amount and unit agree with versioned FEBA. Retain
    the amount and attach ingredient-level evidence; this decision does not authenticate
    the inaccessible historical import snapshot."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml",
    "field_path": "ingredients[31].concentration", "stored_value": {"value": "40",
    "unit": "MILLIMOLAR"}, "decision": "evidence_only", "rationale": "Direct medium
    component. The stored numerical amount and unit agree with versioned FEBA. Retain
    the amount and attach ingredient-level evidence; this decision does not authenticate
    the inaccessible historical import snapshot."}]}, {"quantity_id": "q33", "topic":
    "Omitted vitamin-mixture phosphate", "source": {"evidence_id": "febaMixes", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 865", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "Potassium
    phosphate monobasic\t0.9\tg/L"}, "decision": "add", "rationale": "The selected
    vitamin mixture includes potassium phosphate monobasic at0.9g/L atX=1 and the
    exact MES definition includes that mixture at1X. Both local ingredient arrays
    omit this component. The separate phosphate-free mixture is not named by the selected
    source. Reconcile the missing component against the historical import version
    before curation; preserve explicit source disagreement if intentional variant
    evidence emerges.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml",
    "field_path": "ingredients[32]", "stored_value": null, "decision": "add", "rationale":
    "The selected vitamin mixture includes potassium phosphate monobasic at0.9g/L
    atX=1 and the exact MES definition includes that mixture at1X. Both local ingredient
    arrays omit this component. The separate phosphate-free mixture is not named by
    the selected source. Reconcile the missing component against the historical import
    version before curation; preserve explicit source disagreement if intentional
    variant evidence emerges.", "missing": true}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml",
    "field_path": "ingredients[32]", "stored_value": null, "decision": "add", "rationale":
    "The selected vitamin mixture includes potassium phosphate monobasic at0.9g/L
    atX=1 and the exact MES definition includes that mixture at1X. Both local ingredient
    arrays omit this component. The separate phosphate-free mixture is not named by
    the selected source. Reconcile the missing component against the historical import
    version before curation; preserve explicit source disagreement if intentional
    variant evidence emerges.", "missing": true}], "basis_controls": [{"evidence_id":
    "febaMixes", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/mixes",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMixes.raw", "raw_sha256":
    "b10abf37b8ea1774feb90e93541ad8f895e6cb2a08ac0cfb70c0266530a518e4", "locator":
    "line 853", "accessed_at": "2026-10-28T12:04:02.959506Z", "quote": "X\t1\t"},
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "line 4809", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe''s
    vitamin mix\t1\tX"}]}, {"quantity_id": "q34", "topic": "Source mixture inclusion",
    "source": {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "line 4808", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe''s
    mineral mix\t1\tX"}, "decision": "evidence_only", "rationale": "Source1X inclusion
    is represented by component-level contributions. Retain its provenance; do not
    add a full stock again on top of the expanded ingredients. No mixing volume or
    preparation protocol is supplied.", "layer_assessments": []}, {"quantity_id":
    "q35", "topic": "Source mixture inclusion", "source": {"evidence_id": "febaMedia",
    "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "line 4809", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "ATCC Wolfe''s
    vitamin mix\t1\tX"}, "decision": "evidence_only", "rationale": "Source1X inclusion
    is represented by component-level contributions. Retain its provenance; do not
    add a full stock again on top of the expanded ingredients. No mixing volume or
    preparation protocol is supplied.", "layer_assessments": []}, {"quantity_id":
    "q36", "topic": "Source condition description", "source": {"evidence_id": "febaMedia",
    "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch066/source07-08-10/febaMedia.raw", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "line 4800", "accessed_at": "2026-10-28T12:04:02.975336Z", "quote": "Description\tUGA
    media for MT123 aerobic growth with MES buffer, for growth at pH5.5\t"}, "decision":
    "verified", "rationale": "Source description retained without transfer from MOPS
    or anaerobic sibling. Structured pH can be considered only with this source-description
    scope.", "layer_assessments": [{"path": "data/merge_yaml/merged/CRBTM_UGA_Aerobic_MES.yaml",
    "field_path": "description", "stored_value": "UGA media for MT123 aerobic growth
    with MES buffer, for growth at pH5.5", "decision": "verified", "rationale": "The
    current description matches the exact FEBA MES description, including its aerobic
    context and pH5.5 label; no incubation protocol or demonstrated growth yield is
    inferred."}, {"path": "data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml",
    "field_path": "description", "stored_value": "UGA media for MT123 aerobic growth
    with MES buffer, for growth at pH5.5", "decision": "verified", "rationale": "The
    current description matches the exact FEBA MES description, including its aerobic
    context and pH5.5 label; no incubation protocol or demonstrated growth yield is
    inferred."}]}]'
- assessment_id: a7
  area: grounding
  topic: Current ontology and MIM correspondence
  outcome: concern
  summary: All64 target/owner term slots join to current OLS exact objects and the
    packaged MIM index. The L-specific lactate identity conflicts with the source
    D,L descriptor. Hydrate labels including corrected manganese sulfate monohydrate
    agree. The source hemicalcium wording is credited; its basis is missing from the
    local molecular-weight note, and mixed D/D,L aliases plus lipoic-acid CAS cross-reference
    coverage remain bounded; catalog coverage alone does not establish source form.
  target_ids:
  - CultureMech:015505
  evidence_ids:
  - grounding
- assessment_id: a8
  area: provenance
  topic: History and evidence scope
  outcome: concern
  summary: Complete target/owner histories and both historical32-row reports were
    inspected. Present manganese grounding is credited. Generic CultureBotHT provenance
    is not recoverable through the exact API endpoints; FEBA revision and source-locator
    evidence are independently recoverable. No existing history or scientific record
    was changed.
  target_ids:
  - CultureMech:015505
  evidence_ids:
  - history
  - scalars
- assessment_id: a9
  area: scope
  topic: Growth and taxonomic evidence
  outcome: unknown
  summary: Generic cultivation applications and bacterial filing are not strain-level
    growth evidence. No organism-specific growth, temperature or atmosphere is inferred
    from names or source catalog identifiers.
  target_ids:
  - CultureMech:015505
  evidence_ids:
  - local-target
- assessment_id: a10
  area: schema
  topic: Canonical diagnostics
  outcome: supported
  summary: All four original canonical diagnostics passed. Reference checks were zero;
    structural and term diagnostics do not establish formulation accuracy.
  target_ids:
  - CultureMech:015505
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-015505-a-named-mixture-component-is-missing
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: A named mixture component is missing
  description: The exact FEBA MES definition includes ATCC Wolfe vitamin mixture at1X.
    That definition includes potassium phosphate monobasic, absent from target and
    owner. A separately named phosphate-free variant exists but is not referenced
    here. Reconcile this source discrepancy with the missing historical CultureBotHT
    snapshot; do not claim an intentional omission or blend variants without evidence.
  target_ids:
  - CultureMech:015505
  field_paths:
  - ingredients
  - notes
  evidence_ids:
  - quantities
  - febaMedia
  - febaMixes
  - writer-import
  rule_id: source-formulation-completeness
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f2
  issue_key: culturemech-015505-lactate-stereochemistry-does-not-match-the-source
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Lactate stereochemistry does not match the source
  description: Source and local preferred term specify Sodium D,L-Lactate, while CHEBI232798
    is sodium L-lactate. The exact ontology label exists but denotes a narrower stereochemical
    identity. Source compound and local notes also carry CAS50-21-5/MW90.08, which
    do not match the current term CAS867-56-1/MW112.06. Resolve the source identity
    with supplier/form evidence before assigning a replacement; retain the source-stated
    numerical concentration without using these notes for conversion.
  target_ids:
  - CultureMech:015505
  field_paths:
  - ingredients[30].term
  - ingredients[30].notes
  evidence_ids:
  - febaMedia
  - febaCompounds
  - chemical-notes
  - chebi232798
  rule_id: source-chemical-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f3
  issue_key: culturemech-015505-molecular-weight-notes-need-an-explicit-formula-basis
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Molecular weight notes need an explicit formula basis
  description: The local calcium pantothenate note records MW 238.27 without a formula
    basis. FEBA explicitly includes a hemicalcium-salt synonym, consistent with approximately
    half the current OLS full calcium-salt formula mass of 476.536. Credit that source
    wording and clarify the local note; the source mixed D/D,L aliases remain a separate
    stereochemical limitation. Preserve the supported mass concentration and do not
    silently convert it to molarity.
  target_ids:
  - CultureMech:015505
  field_paths:
  - ingredients[26].notes
  evidence_ids:
  - febaCompounds
  - chemical-notes
  - chebi31345
  rule_id: chemical-note-basis
  native_severity: P3
  normalization_reason: 'Minor: bounded metadata or traceability defect without establishing
    a new formulation.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f4
  issue_key: culturemech-015505-exact-source-evidence-and-current-quality-metadata-are-missing
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Exact source evidence and current quality metadata are missing
  description: The generic CultureBotHT URL currently returns404 through its API,
    and no imported commit is recorded. Attach the recoverable versioned FEBA definition
    and mixture locators to supported ingredient evidence, preserving that the historical
    import remains unavailable. Reassess the unmapped flag against current term occupancy
    and retain the grounding conflict explicitly. Preserve all existing history entries.
  target_ids:
  - CultureMech:015505
  field_paths:
  - sources
  - ingredients
  - data_quality_flags
  - curation_history
  evidence_ids:
  - local-target
  - owner-1
  - culturebotRepo
  - culturebotCommit
  - febaMedia
  - febaMixes
  - writer-import
  rule_id: source-traceability
  native_severity: P3
  normalization_reason: 'Minor: bounded metadata or traceability defect without establishing
    a new formulation.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
actions:
- action_id: action1
  description: The exact FEBA MES definition includes ATCC Wolfe vitamin mixture at1X.
    That definition includes potassium phosphate monobasic, absent from target and
    owner. A separately named phosphate-free variant exists but is not referenced
    here. Reconcile this source discrepancy with the missing historical CultureBotHT
    snapshot; do not claim an intentional omission or blend variants without evidence.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:015505
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action2
  description: Source and local preferred term specify Sodium D,L-Lactate, while CHEBI232798
    is sodium L-lactate. The exact ontology label exists but denotes a narrower stereochemical
    identity. Source compound and local notes also carry CAS50-21-5/MW90.08, which
    do not match the current term CAS867-56-1/MW112.06. Resolve the source identity
    with supplier/form evidence before assigning a replacement; retain the source-stated
    numerical concentration without using these notes for conversion.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:015505
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action3
  description: The local calcium pantothenate note records MW 238.27 without a formula
    basis. FEBA explicitly includes a hemicalcium-salt synonym, consistent with approximately
    half the current OLS full calcium-salt formula mass of 476.536. Credit that source
    wording and clarify the local note; the source mixed D/D,L aliases remain a separate
    stereochemical limitation. Preserve the supported mass concentration and do not
    silently convert it to molarity.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:015505
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action4
  description: The generic CultureBotHT URL currently returns404 through its API,
    and no imported commit is recorded. Attach the recoverable versioned FEBA definition
    and mixture locators to supported ingredient evidence, preserving that the historical
    import remains unavailable. Reassess the unmapped flag against current term occupancy
    and retain the grounding conflict explicitly. Preserve all existing history entries.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:015505
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/crbtm_uga_aerobic_mes.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
limitations:
- The CultureBotHT repository and revision API endpoints returned404. This cannot
  establish repository deletion or reconstruct the historical imported snapshot. The
  review is partial for that provenance gap.
- Current versioned FEBA is source evidence for its own definition, not proof that
  its content exactly matches the historical CultureBotHT import. The missing component
  finding preserves that distinction.
- The exact MES source block and its named mixtures were assessed; sibling MOPS, anaerobic
  and phosphate-free variants are excluded from adopted formulation. No extra stock
  is added on top of expanded ingredients.
- The MT123 primary-publication abstract establishes organism context only. Full-paper
  recipe equivalence, taxonomy grounding, actual growth performance and incubation
  protocol were not established. iModulonDB is not applicable to this formulation
  review.
- All source numerical amounts agree with existing fields, but missing ingredient-level
  evidence and the lactate identity conflict remain. FEBA hemicalcium wording provides
  a formula-basis explanation omitted from the local note; mixed D/D,L source aliases
  do not independently settle stereochemistry. No mass/molar conversion is performed.
- OLS lipoic-acid CAS cross-references do not include the source/local CAS; this is
  unresolved cross-reference coverage, not a confirmed incorrect CAS assertion.
- Canonical reference validation performed zero reference checks. Current history
  and source provenance were reviewed manually; unchanged-recipe whole-corpus product/ID/merge
  gates were not rerun.
- No recipe, generated data, scientific status or history was changed. Current writer
  functions are ownership context and do not prove historical execution.
notes:
- Fresh review; historical lost snapshots were not reconstructed. All inspected source
  files remain unchanged.
- This draft authoring step performed no formal review validation/save, Git mutation
  or publication.
```
