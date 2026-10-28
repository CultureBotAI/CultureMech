# Brucella FEBA broth: supported current rates with an incomplete import trail

- Review: 20261028T051730Z-batch056-record01-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T05:11:00.221392Z
- Finished UTC: 2026-10-28T05:17:30.480330Z
- Reviewer: Codex independent source reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact FEBA Brucella block explicitly supports all eight current g/L values. The CultureBotHT repository and candidate file are unavailable, so the March import chain is not authenticated by the later FEBA revision. A malformed yeast-extract identifier label remains a bounded metadata defect.

## Scope And Provenance

Full selected record and exact maintained contributors; explicitly scoped dependency and external-source limits retained.

Selection: Actual batch056 native selection index 01.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:015499 | data/merge_yaml/merged/Brucella.yaml | generated | Brucella |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:015499 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-strict | passed | True | CultureMech:015499 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-terms | passed | True | CultureMech:015499 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-references | passed | True | CultureMech:015499 | Native reference checker performed zero reference checks; this is not claim authentication. |

## Scientific And Domain Assessments

### Exact FEBA block and generated ownership

identity: supported. Targets: CultureMech:015499.

The selected record is the one-owner CultureBotHT Brucella broth import. Its label, description, eight component names and all eight values match the current exact FEBA block. Similarly named blood-agar formulations are not this target.

### Unchanged classification and missing optional claims

scope: supported. Targets: CultureMech:015499.

COMPLEX, UNDEFINED and LIQUID agree with the named broth and undefined digests/extract. Specialized filing is the importer fallback, not an organism claim. No organism, strain growth, preparation, pH or missing stock dose is asserted by the scoped FEBA block; empty optional fields are not filled from familiar Brucella recipes.

### Chemical identity and catalog limits

grounding: supported. Targets: CultureMech:015499.

All five primary CHEBI labels match current non-obsolete OLS objects; their CAS identities correspond. Three undefined components lack primary mappings and all eight ingredients lack secondary MIM slots; these are linkage counts, not scientific-failure percentages. The existing unmapped flag is accurate. Confidence0.90 notes are historical mapping metadata rather than an independently reproduced calibration.

### Quantity scope and inventory

quantity: concern. Targets: CultureMech:015499.

Every selected target/owner concentration field has an explicit disposition; scoped dependency fields and source-only preparation are separate from receiving-medium rates.

[{"quantity_id": "q1", "topic": "Pancreatic digest of casein", "source": {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch056/source01-03-supplement/febaMedia.bin", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "Brucella block; physical line4581; explicit concentration/unit header line4580", "accessed_at": "2026-10-28T05:12:08.334028Z", "quote": "Pancreatic digest of casein\t10\tg/L"}, "decision": "evidence_only", "rationale": "The exact commit-pinned FEBA Brucella row explicitly declares this numerical value in g/L. Retain it and add claim-level source linkage; no water-input assumption or stock dilution is used. This current correspondence does not authenticate the unavailable historical CultureBotHT export.", "layer_assessments": [{"path": "data/merge_yaml/merged/Brucella.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact commit-pinned FEBA Brucella row explicitly declares this numerical value in g/L. Retain it and add claim-level source linkage; no water-input assumption or stock dilution is used. This current correspondence does not authenticate the unavailable historical CultureBotHT export."}, {"path": "data/normalized_yaml/specialized/brucella.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact commit-pinned FEBA Brucella row explicitly declares this numerical value in g/L. Retain it and add claim-level source linkage; no water-input assumption or stock dilution is used. This current correspondence does not authenticate the unavailable historical CultureBotHT export."}]}, {"quantity_id": "q2", "topic": "Peptic digest of animal tissue", "source": {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch056/source01-03-supplement/febaMedia.bin", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "Brucella block; physical line4582; explicit concentration/unit header line4580", "accessed_at": "2026-10-28T05:12:08.334028Z", "quote": "Peptic digest of animal tissue\t10\tg/L"}, "decision": "evidence_only", "rationale": "The exact commit-pinned FEBA Brucella row explicitly declares this numerical value in g/L. Retain it and add claim-level source linkage; no water-input assumption or stock dilution is used. This current correspondence does not authenticate the unavailable historical CultureBotHT export.", "layer_assessments": [{"path": "data/merge_yaml/merged/Brucella.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact commit-pinned FEBA Brucella row explicitly declares this numerical value in g/L. Retain it and add claim-level source linkage; no water-input assumption or stock dilution is used. This current correspondence does not authenticate the unavailable historical CultureBotHT export."}, {"path": "data/normalized_yaml/specialized/brucella.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact commit-pinned FEBA Brucella row explicitly declares this numerical value in g/L. Retain it and add claim-level source linkage; no water-input assumption or stock dilution is used. This current correspondence does not authenticate the unavailable historical CultureBotHT export."}]}, {"quantity_id": "q3", "topic": "D-Glucose", "source": {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch056/source01-03-supplement/febaMedia.bin", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "Brucella block; physical line4583; explicit concentration/unit header line4580", "accessed_at": "2026-10-28T05:12:08.334028Z", "quote": "D-Glucose\t1\tg/L"}, "decision": "evidence_only", "rationale": "The exact commit-pinned FEBA Brucella row explicitly declares this numerical value in g/L. Retain it and add claim-level source linkage; no water-input assumption or stock dilution is used. This current correspondence does not authenticate the unavailable historical CultureBotHT export.", "layer_assessments": [{"path": "data/merge_yaml/merged/Brucella.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact commit-pinned FEBA Brucella row explicitly declares this numerical value in g/L. Retain it and add claim-level source linkage; no water-input assumption or stock dilution is used. This current correspondence does not authenticate the unavailable historical CultureBotHT export."}, {"path": "data/normalized_yaml/specialized/brucella.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact commit-pinned FEBA Brucella row explicitly declares this numerical value in g/L. Retain it and add claim-level source linkage; no water-input assumption or stock dilution is used. This current correspondence does not authenticate the unavailable historical CultureBotHT export."}]}, {"quantity_id": "q4", "topic": "Yeast Extract", "source": {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch056/source01-03-supplement/febaMedia.bin", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "Brucella block; physical line4584; explicit concentration/unit header line4580", "accessed_at": "2026-10-28T05:12:08.334028Z", "quote": "Yeast Extract\t2\tg/L"}, "decision": "evidence_only", "rationale": "The exact commit-pinned FEBA Brucella row explicitly declares this numerical value in g/L. Retain it and add claim-level source linkage; no water-input assumption or stock dilution is used. This current correspondence does not authenticate the unavailable historical CultureBotHT export.", "layer_assessments": [{"path": "data/merge_yaml/merged/Brucella.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "2", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact commit-pinned FEBA Brucella row explicitly declares this numerical value in g/L. Retain it and add claim-level source linkage; no water-input assumption or stock dilution is used. This current correspondence does not authenticate the unavailable historical CultureBotHT export."}, {"path": "data/normalized_yaml/specialized/brucella.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "2", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact commit-pinned FEBA Brucella row explicitly declares this numerical value in g/L. Retain it and add claim-level source linkage; no water-input assumption or stock dilution is used. This current correspondence does not authenticate the unavailable historical CultureBotHT export."}]}, {"quantity_id": "q5", "topic": "Sodium Chloride", "source": {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch056/source01-03-supplement/febaMedia.bin", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "Brucella block; physical line4585; explicit concentration/unit header line4580", "accessed_at": "2026-10-28T05:12:08.334028Z", "quote": "Sodium Chloride\t5\tg/L"}, "decision": "evidence_only", "rationale": "The exact commit-pinned FEBA Brucella row explicitly declares this numerical value in g/L. Retain it and add claim-level source linkage; no water-input assumption or stock dilution is used. This current correspondence does not authenticate the unavailable historical CultureBotHT export.", "layer_assessments": [{"path": "data/merge_yaml/merged/Brucella.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact commit-pinned FEBA Brucella row explicitly declares this numerical value in g/L. Retain it and add claim-level source linkage; no water-input assumption or stock dilution is used. This current correspondence does not authenticate the unavailable historical CultureBotHT export."}, {"path": "data/normalized_yaml/specialized/brucella.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact commit-pinned FEBA Brucella row explicitly declares this numerical value in g/L. Retain it and add claim-level source linkage; no water-input assumption or stock dilution is used. This current correspondence does not authenticate the unavailable historical CultureBotHT export."}]}, {"quantity_id": "q6", "topic": "Sodium bisulfite", "source": {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch056/source01-03-supplement/febaMedia.bin", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "Brucella block; physical line4586; explicit concentration/unit header line4580", "accessed_at": "2026-10-28T05:12:08.334028Z", "quote": "Sodium bisulfite\t0.1\tg/L"}, "decision": "evidence_only", "rationale": "The exact commit-pinned FEBA Brucella row explicitly declares this numerical value in g/L. Retain it and add claim-level source linkage; no water-input assumption or stock dilution is used. This current correspondence does not authenticate the unavailable historical CultureBotHT export.", "layer_assessments": [{"path": "data/merge_yaml/merged/Brucella.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact commit-pinned FEBA Brucella row explicitly declares this numerical value in g/L. Retain it and add claim-level source linkage; no water-input assumption or stock dilution is used. This current correspondence does not authenticate the unavailable historical CultureBotHT export."}, {"path": "data/normalized_yaml/specialized/brucella.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact commit-pinned FEBA Brucella row explicitly declares this numerical value in g/L. Retain it and add claim-level source linkage; no water-input assumption or stock dilution is used. This current correspondence does not authenticate the unavailable historical CultureBotHT export."}]}, {"quantity_id": "q7", "topic": "Hemin", "source": {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch056/source01-03-supplement/febaMedia.bin", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "Brucella block; physical line4587; explicit concentration/unit header line4580", "accessed_at": "2026-10-28T05:12:08.334028Z", "quote": "Hemin\t0.005\tg/L"}, "decision": "evidence_only", "rationale": "The exact commit-pinned FEBA Brucella row explicitly declares this numerical value in g/L. Retain it and add claim-level source linkage; no water-input assumption or stock dilution is used. This current correspondence does not authenticate the unavailable historical CultureBotHT export.", "layer_assessments": [{"path": "data/merge_yaml/merged/Brucella.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.005", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact commit-pinned FEBA Brucella row explicitly declares this numerical value in g/L. Retain it and add claim-level source linkage; no water-input assumption or stock dilution is used. This current correspondence does not authenticate the unavailable historical CultureBotHT export."}, {"path": "data/normalized_yaml/specialized/brucella.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.005", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact commit-pinned FEBA Brucella row explicitly declares this numerical value in g/L. Retain it and add claim-level source linkage; no water-input assumption or stock dilution is used. This current correspondence does not authenticate the unavailable historical CultureBotHT export."}]}, {"quantity_id": "q8", "topic": "Menadione", "source": {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media", "raw_path": "REVIEW_WORK/batch056/source01-03-supplement/febaMedia.bin", "raw_sha256": "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator": "Brucella block; physical line4588; explicit concentration/unit header line4580", "accessed_at": "2026-10-28T05:12:08.334028Z", "quote": "Menadione\t0.001\tg/L"}, "decision": "evidence_only", "rationale": "The exact commit-pinned FEBA Brucella row explicitly declares this numerical value in g/L. Retain it and add claim-level source linkage; no water-input assumption or stock dilution is used. This current correspondence does not authenticate the unavailable historical CultureBotHT export.", "layer_assessments": [{"path": "data/merge_yaml/merged/Brucella.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.001", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact commit-pinned FEBA Brucella row explicitly declares this numerical value in g/L. Retain it and add claim-level source linkage; no water-input assumption or stock dilution is used. This current correspondence does not authenticate the unavailable historical CultureBotHT export."}, {"path": "data/normalized_yaml/specialized/brucella.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.001", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact commit-pinned FEBA Brucella row explicitly declares this numerical value in g/L. Retain it and add claim-level source linkage; no water-input assumption or stock dilution is used. This current correspondence does not authenticate the unavailable historical CultureBotHT export."}]}, {"quantity_id": "q9", "topic": "D-Glucose descriptive molecular-weight note", "source": {"evidence_id": "febaCompounds", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv", "raw_path": "REVIEW_WORK/batch056/source01-03-supplement/febaCompounds.bin", "raw_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774", "locator": "Exact Compound row D-Glucose", "accessed_at": "2026-10-28T05:12:08.363539Z", "quote": "D-Glucose\t50-99-7\tSigma\tG7528\t180.16\tglucose\t\t\t\tyes\t\t\t"}, "decision": "evidence_only", "rationale": "The local CAS and listed molecular-weight digits correspond to this exact FEBA compound metadata row. Current OLS independently supports the accession/CAS identity. These metadata digits are not used for a molar conversion; hemin FW651.94 is retained as FEBA metadata rather than silently replaced with current OLS651.952.", "layer_assessments": [{"path": "data/merge_yaml/merged/Brucella.yaml", "field_path": "ingredients[2].notes", "stored_value": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 50-99-7; MW: 180.16", "decision": "evidence_only", "rationale": "The local CAS and listed molecular-weight digits correspond to this exact FEBA compound metadata row. Current OLS independently supports the accession/CAS identity. These metadata digits are not used for a molar conversion; hemin FW651.94 is retained as FEBA metadata rather than silently replaced with current OLS651.952."}, {"path": "data/normalized_yaml/specialized/brucella.yaml", "field_path": "ingredients[2].notes", "stored_value": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 50-99-7; MW: 180.16", "decision": "evidence_only", "rationale": "The local CAS and listed molecular-weight digits correspond to this exact FEBA compound metadata row. Current OLS independently supports the accession/CAS identity. These metadata digits are not used for a molar conversion; hemin FW651.94 is retained as FEBA metadata rather than silently replaced with current OLS651.952."}]}, {"quantity_id": "q10", "topic": "Sodium Chloride descriptive molecular-weight note", "source": {"evidence_id": "febaCompounds", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv", "raw_path": "REVIEW_WORK/batch056/source01-03-supplement/febaCompounds.bin", "raw_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774", "locator": "Exact Compound row Sodium Chloride", "accessed_at": "2026-10-28T05:12:08.363539Z", "quote": "Sodium Chloride\t7647-14-5\tSigma\tS3014\t58.44\tNaCl\t\t\tyes\t\t\tyes\t"}, "decision": "evidence_only", "rationale": "The local CAS and listed molecular-weight digits correspond to this exact FEBA compound metadata row. Current OLS independently supports the accession/CAS identity. These metadata digits are not used for a molar conversion; hemin FW651.94 is retained as FEBA metadata rather than silently replaced with current OLS651.952.", "layer_assessments": [{"path": "data/merge_yaml/merged/Brucella.yaml", "field_path": "ingredients[4].notes", "stored_value": "CAS: 7647-14-5; MW: 58.44", "decision": "evidence_only", "rationale": "The local CAS and listed molecular-weight digits correspond to this exact FEBA compound metadata row. Current OLS independently supports the accession/CAS identity. These metadata digits are not used for a molar conversion; hemin FW651.94 is retained as FEBA metadata rather than silently replaced with current OLS651.952."}, {"path": "data/normalized_yaml/specialized/brucella.yaml", "field_path": "ingredients[4].notes", "stored_value": "CAS: 7647-14-5; MW: 58.44", "decision": "evidence_only", "rationale": "The local CAS and listed molecular-weight digits correspond to this exact FEBA compound metadata row. Current OLS independently supports the accession/CAS identity. These metadata digits are not used for a molar conversion; hemin FW651.94 is retained as FEBA metadata rather than silently replaced with current OLS651.952."}]}, {"quantity_id": "q11", "topic": "Hemin descriptive molecular-weight note", "source": {"evidence_id": "febaCompounds", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv", "raw_path": "REVIEW_WORK/batch056/source01-03-supplement/febaCompounds.bin", "raw_sha256": "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774", "locator": "Exact Compound row Hemin", "accessed_at": "2026-10-28T05:12:08.363539Z", "quote": "Hemin\t16009-13-5\tsigmaaldrich\tH9039-10G\t651.94\tChloro(protoporphyrinato)iron(III), Chlorohemin, Chloroprotoporphyrin IX iron(III), Ferriprotoporphyrin IX chloride, Hemin(chloride)\t\t\t\t\t\t\t"}, "decision": "evidence_only", "rationale": "The local CAS and listed molecular-weight digits correspond to this exact FEBA compound metadata row. Current OLS independently supports the accession/CAS identity. These metadata digits are not used for a molar conversion; hemin FW651.94 is retained as FEBA metadata rather than silently replaced with current OLS651.952.", "layer_assessments": [{"path": "data/merge_yaml/merged/Brucella.yaml", "field_path": "ingredients[6].notes", "stored_value": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 16009-13-5; MW: 651.94", "decision": "evidence_only", "rationale": "The local CAS and listed molecular-weight digits correspond to this exact FEBA compound metadata row. Current OLS independently supports the accession/CAS identity. These metadata digits are not used for a molar conversion; hemin FW651.94 is retained as FEBA metadata rather than silently replaced with current OLS651.952."}, {"path": "data/normalized_yaml/specialized/brucella.yaml", "field_path": "ingredients[6].notes", "stored_value": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 16009-13-5; MW: 651.94", "decision": "evidence_only", "rationale": "The local CAS and listed molecular-weight digits correspond to this exact FEBA compound metadata row. Current OLS independently supports the accession/CAS identity. These metadata digits are not used for a molar conversion; hemin FW651.94 is retained as FEBA metadata rather than silently replaced with current OLS651.952."}]}]

### Current ontology and MIM correspondence

grounding: supported. Targets: CultureMech:015499.

The grounding inventory enumerates every asserted identifier and exact preferred label. Exact identifier rows and ontology-linked rows are recorded separately, including mapping_status. Present catalog membership does not validate supplied hydrate form or historical identity; specific limits are assessed separately.

### History and evidence scope

provenance: supported. Targets: CultureMech:015499.

Complete owner and target histories were read. Current source bytes and inspected code are independent evidence; historical timestamps remain historical claims unless an exact cited raw digest is recovered.

### Growth and taxonomic evidence

scope: unknown. Targets: CultureMech:015499.

Generic cultivation applications and bacterial filing are not strain-level growth evidence. No organism-specific growth, temperature or atmosphere is inferred from names or source catalog identifiers.

### Canonical diagnostics

schema: supported. Targets: CultureMech:015499.

All four original canonical diagnostics passed. Reference checks were zero; structural and term diagnostics do not establish formulation accuracy.

## Findings

### f1: The exact current FEBA support is absent from the import trail

major / open / confirmed; issue key: culturemech-015499-the-exact-current-feba-support-is-absent-from-the-import-trail.

The record cites only an unavailable CultureBotHT repository root. The newly inspected commit-pinned FEBA block positively supports the eight current concentrations, but neither that later revision nor a candidate raw-file404 proves the exact bytes imported in March. No claim-level source evidence or pinned FEBA reference is stored.

### f2: Yeast extract notes label a non-CAS-shaped token as CAS

minor / open / confirmed; issue key: culturemech-015499-yeast-extract-notes-label-a-non-cas-shaped-token-as-cas.

ingredients[3].notes says CAS:232-387-9. The FEBA compound table repeats that token, but its three-digit middle group does not meet CAS-RN syntax. Agreement with a source table does not validate its identifier namespace. No alternative identifier or EC identity has been independently established.

## Recommended Actions And Acceptance Checks

### action1

Add exact commit-pinned FEBA reference and row-level support for the existing values. Keep the unverified historical CultureBotHT export/version as a separate limitation; do not claim it was recovered. Maintain original history and regenerate the generated record after owner curation.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action2

Qualify or remove the unsupported CAS namespace assertion while preserving the literal historical source token. Resolve any replacement namespace/identifier independently; do not guess one.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local-target | data/merge_yaml/merged/Brucella.yaml; Complete document | context_only | Complete selected generated record; no changes made. |
| owner-1 | data/normalized_yaml/specialized/brucella.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| febaCommit | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/commits/master?pagelen=1; $.values[0].hash/date | supports | The current FEBA branch resolves to commit803273865ea9e83fab770ec4f13670db80e1180b dated September2026. This is current version context, not proof of the March import. |
| febaMedia | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media; metadata/media lines4577–4588, exact Brucella block | supports | Exact Brucella block, its description and explicit concentration/unit header, plus all eight rows were read. These are direct g/L declarations, requiring no inferred final-volume conversion. |
| febaCompounds | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv; metadata/Compounds.tsv; exact Compound rows and Tryptone synonym | supports | Eight exact or explicitly synonymous compound rows and their column headers were read; descriptive CAS/FW metadata is separate from recipe quantity support. |
| febaReadme | https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/README; Project description and attribution | context_only | FEBA repository README identifies the dataset/software project and author. It does not establish the missing CultureBotHT file or a historical export event. |
| culturebotht | https://github.com/CultureBotAI/CultureBotHT; Current HTTP response | unknown | The exact source repository URL returned404. Its failure is preserved, not evidence that the repository never existed. |
| culturebothtRaw | https://raw.githubusercontent.com/CultureBotAI/CultureBotHT/main/media_yaml/Brucella.yaml; Current HTTP response for candidate raw path | unknown | The candidate main/media_yaml/Brucella.yaml path returned404. This bounded path attempt does not prove absence of every branch or private historical export. |
| writer-culturebotht | scripts/import_from_culturebotht.py; CultureBotHTImporter.transform_medium/infer_category | context_only | Current transform_medium copies incoming content, appends the repository-root source URL and import history, and uses a name-pattern category fallback to SPECIALIZED. It does not supply a pinned upstream file/commit or independently verify chemical metadata. |
| writer-merge | src/culturemech/merge/merger.py; merge_group | context_only | Current merge_group copies a sole maintained contributor and adds merge metadata; it cannot authenticate an absent upstream export. Multi-owner inputs pass through compatibility-checking merge_formulation_evidence. |
| historical-1 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Brucella.md; Entire report; exact Record header and all claim rows | context_only | Full exact selected-path historical report read. Its past source-access statements and snippets are derivative evidence; the cited raw response is not automatically authenticated. |
| historical-2 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/specialized/brucella.md; Entire report; exact Record header and all claim rows | context_only | Full exact selected-path historical report read. Its past source-access statements and snippets are derivative evidence; the cited raw response is not automatically authenticated. |
| historical-3 | reports/yaml_record_review/20260922T003205Z-Brucella.md; Entire report; exact Record header and all claim rows | context_only | Full exact selected-path historical report read. Its past source-access statements and snippets are derivative evidence; the cited raw response is not automatically authenticated. |
| historical-reader | REVIEW_WORK/batch056/record01/historical-reader.json | context_only | Complete selected target/owner historical reports and exact report hashes, preserving derivative-only limits. |
| identity-search | REVIEW_WORK/batch056/record01/identity-search.json | supports | Exact stable ID resolves the selected generated record and its declared maintained contributor. |
| chebi17634 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17634; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_26710; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi26709 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_26709; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi50385 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_50385; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi28869 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_28869; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| quantities | REVIEW_WORK/batch056/record01/quantity-inventory.json | context_only | Complete local concentration and source-stage decision inventory; includes exact local paths and source failure limits. |
| grounding | REVIEW_WORK/batch056/record01/grounding-inventory.json | context_only | All recursive asserted identifier/label slots, exact current OLS objects and current packaged MIM preferred-row joins. |
| history | REVIEW_WORK/batch056/record01/history-and-evidence-inventory.json | context_only | Complete current history, references and attached evidence; source-specific claims are assessed without authenticating historical execution from code. |
| scalars | REVIEW_WORK/batch056/record01/scalar-census.json | context_only | Lossless scalar census of the selected target and all maintained contributors. |
| validate-schema | REVIEW_WORK/batch056/record01/validate-schema.json | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed<br> |
| validate-strict | REVIEW_WORK/batch056/record01/validate-strict.json | supports | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch056/record01/strict.tsv<br> |
| validate-terms | REVIEW_WORK/batch056/record01/validate-terms.json | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed<br> |
| validate-references | REVIEW_WORK/batch056/record01/validate-references.json | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed<br> |

## Limits And Additional Notes

- The March CultureBotHT file and export revision were not recovered; both current repository and candidate main-file access returned404. The exact FEBA source accessed here is a later pinned revision.
- The scoped FEBA block gives explicit g/L rates but no preparation, pH, organism or growth claim. No generic recipe or supplier variant was imported to fill these omissions.
- Current OLS/MIM metadata does not establish historical mapping validity. Undefined digests and extract remain mixtures; no density or molar conversion is inferred.
- All three exact historical reports were read as derivative observations. Their old access events and unrecovered raw payloads are not authenticated by current source agreement.
- Fresh review; historical lost snapshots were not reconstructed. All inspected source files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T051730Z-batch056-record01-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Brucella FEBA broth: supported current rates with an incomplete import trail'
started_at: '2026-10-28T05:11:00.221392Z'
finished_at: '2026-10-28T05:17:30.480330Z'
reviewer:
  identity: Codex independent source reviewer
  kind: agent
  independence: independent
  independence_basis: Fresh assessment of the inspected checkout and newly captured
    primary/provider/ontology evidence; no reconstruction of lost reviews and no record
    edits.
skill: .claude/skills/review-yaml-record/SKILL.md; .claude/skills/review-ingredient-concentrations/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: The exact FEBA Brucella block explicitly supports all eight current g/L values.
  The CultureBotHT repository and candidate file are unavailable, so the March import
  chain is not authenticated by the later FEBA revision. A malformed yeast-extract
  identifier label remains a bounded metadata defect.
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
  - path: data/merge_yaml/merged/Brucella.yaml
    sha256: c47bdf77d0bac63578821d419ab2ad48384d97e99cff3c0b98b7e288a225ce9b
    role: target
  - path: data/normalized_yaml/specialized/brucella.yaml
    sha256: d49fbb1a5895320823554dd083d02d6d42850d9c08542f4b5f4d78fd5995a864
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Brucella.md
    sha256: 5ceeb37728d101fc00c05f2ab6cd90c2a3b278fb18a8674bfa7e04ebffedb6b4
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/specialized/brucella.md
    sha256: b53d362c4e635cb547eece796487388456710531444cf4cdf3bc195ed1dad433
    role: context
  - path: reports/yaml_record_review/20260922T003205Z-Brucella.md
    sha256: e3210a4997842a3da74b5e47ccf83661cc05fef38692852860ecb84c30a04192
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/cleanup_recipe_ingredients.py
    sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
    role: context
  - path: scripts/import_from_culturebotht.py
    sha256: d835addf5fff423a9b0b1231848ed3103c5b2d97015c1c294365970d15be0fe1
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
  - path: src/culturemech/import/mediadb_importer.py
    sha256: 5c2d98caf450ee8bb2f73f112e4edab7c3e0f2fa5f2aa7bd2a34e6fd2fdfd4d0
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
  description: Full selected record and exact maintained contributors; explicitly
    scoped dependency and external-source limits retained.
  selection: Actual batch056 native selection index 01.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:015499
targets:
- target_id: CultureMech:015499
  path: data/merge_yaml/merged/Brucella.yaml
  label: Brucella
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/brucella.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:015499
  command: just validate-schema data/merge_yaml/merged/Brucella.yaml
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
  - CultureMech:015499
  command: just validate-strict data/merge_yaml/merged/Brucella.yaml --out REVIEW_WORK/batch056/record01/strict.tsv
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
  - CultureMech:015499
  command: just validate-terms data/merge_yaml/merged/Brucella.yaml
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
  - CultureMech:015499
  command: just validate-references data/merge_yaml/merged/Brucella.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
  scope_note: Exact selected target; scientific source and owner assessments are separate.
evidence:
- evidence_id: local-target
  kind: record_content
  reference: data/merge_yaml/merged/Brucella.yaml
  locator: Complete document
  accessed_at: '2026-10-28T05:17:30.144809Z'
  support: context_only
  summary: Complete selected generated record; no changes made.
  snapshot_sha256: c47bdf77d0bac63578821d419ab2ad48384d97e99cff3c0b98b7e288a225ce9b
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/specialized/brucella.yaml
  locator: Complete document
  accessed_at: '2026-10-28T05:17:30.144809Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: d49fbb1a5895320823554dd083d02d6d42850d9c08542f4b5f4d78fd5995a864
- evidence_id: febaCommit
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/commits/master?pagelen=1
  locator: $.values[0].hash/date
  accessed_at: '2026-10-28T05:11:33.526642Z'
  support: supports
  summary: The current FEBA branch resolves to commit803273865ea9e83fab770ec4f13670db80e1180b
    dated September2026. This is current version context, not proof of the March import.
  snapshot_sha256: e802ea5aee4c66aa42d5425b9aac40af420f9072365b3963288985afa771a498
- evidence_id: febaMedia
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media
  locator: metadata/media lines4577–4588, exact Brucella block
  accessed_at: '2026-10-28T05:12:08.334028Z'
  support: supports
  summary: Exact Brucella block, its description and explicit concentration/unit header,
    plus all eight rows were read. These are direct g/L declarations, requiring no
    inferred final-volume conversion.
  snapshot_sha256: a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848
- evidence_id: febaCompounds
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv
  locator: metadata/Compounds.tsv; exact Compound rows and Tryptone synonym
  accessed_at: '2026-10-28T05:12:08.363539Z'
  support: supports
  summary: Eight exact or explicitly synonymous compound rows and their column headers
    were read; descriptive CAS/FW metadata is separate from recipe quantity support.
  snapshot_sha256: 25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774
- evidence_id: febaReadme
  kind: database
  reference: https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/README
  locator: Project description and attribution
  accessed_at: '2026-10-28T05:12:08.251072Z'
  support: context_only
  summary: FEBA repository README identifies the dataset/software project and author.
    It does not establish the missing CultureBotHT file or a historical export event.
  snapshot_sha256: 3d02ae42d3e650a4275a45e73b98c41a6b2444b744ef676365047db490cbe585
- evidence_id: culturebotht
  kind: database
  reference: https://github.com/CultureBotAI/CultureBotHT
  locator: Current HTTP response
  accessed_at: '2026-10-28T05:11:33.084955Z'
  support: unknown
  summary: The exact source repository URL returned404. Its failure is preserved,
    not evidence that the repository never existed.
  snapshot_sha256: 00e959b750106b46201394388f77dc5b9fa8b6d5514d5e5834a1241bdb8b85a8
- evidence_id: culturebothtRaw
  kind: database
  reference: https://raw.githubusercontent.com/CultureBotAI/CultureBotHT/main/media_yaml/Brucella.yaml
  locator: Current HTTP response for candidate raw path
  accessed_at: '2026-10-28T05:11:32.874094Z'
  support: unknown
  summary: The candidate main/media_yaml/Brucella.yaml path returned404. This bounded
    path attempt does not prove absence of every branch or private historical export.
  snapshot_sha256: d5558cd419c8d46bdc958064cb97f963d1ea793866414c025906ec15033512ed
- evidence_id: writer-culturebotht
  kind: record_content
  reference: scripts/import_from_culturebotht.py
  locator: CultureBotHTImporter.transform_medium/infer_category
  accessed_at: '2026-10-28T05:17:30.144809Z'
  support: context_only
  summary: Current transform_medium copies incoming content, appends the repository-root
    source URL and import history, and uses a name-pattern category fallback to SPECIALIZED.
    It does not supply a pinned upstream file/commit or independently verify chemical
    metadata.
  snapshot_sha256: d835addf5fff423a9b0b1231848ed3103c5b2d97015c1c294365970d15be0fe1
- evidence_id: writer-merge
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: merge_group
  accessed_at: '2026-10-28T05:17:30.144809Z'
  support: context_only
  summary: Current merge_group copies a sole maintained contributor and adds merge
    metadata; it cannot authenticate an absent upstream export. Multi-owner inputs
    pass through compatibility-checking merge_formulation_evidence.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: historical-1
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Brucella.md
  locator: Entire report; exact Record header and all claim rows
  accessed_at: '2026-10-28T05:17:30.144809Z'
  support: context_only
  summary: Full exact selected-path historical report read. Its past source-access
    statements and snippets are derivative evidence; the cited raw response is not
    automatically authenticated.
  snapshot_sha256: 5ceeb37728d101fc00c05f2ab6cd90c2a3b278fb18a8674bfa7e04ebffedb6b4
- evidence_id: historical-2
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/specialized/brucella.md
  locator: Entire report; exact Record header and all claim rows
  accessed_at: '2026-10-28T05:17:30.144809Z'
  support: context_only
  summary: Full exact selected-path historical report read. Its past source-access
    statements and snippets are derivative evidence; the cited raw response is not
    automatically authenticated.
  snapshot_sha256: b53d362c4e635cb547eece796487388456710531444cf4cdf3bc195ed1dad433
- evidence_id: historical-3
  kind: record_content
  reference: reports/yaml_record_review/20260922T003205Z-Brucella.md
  locator: Entire report; exact Record header and all claim rows
  accessed_at: '2026-10-28T05:17:30.144809Z'
  support: context_only
  summary: Full exact selected-path historical report read. Its past source-access
    statements and snippets are derivative evidence; the cited raw response is not
    automatically authenticated.
  snapshot_sha256: e3210a4997842a3da74b5e47ccf83661cc05fef38692852860ecb84c30a04192
- evidence_id: historical-reader
  kind: record_content
  reference: REVIEW_WORK/batch056/record01/historical-reader.json
  accessed_at: '2026-10-28T05:17:30.154600Z'
  support: context_only
  summary: Complete selected target/owner historical reports and exact report hashes,
    preserving derivative-only limits.
  snapshot_sha256: 01bdb15bb8664dfa529105bcae06229abfaf9d131a6c004e548bc5d895f08811
- evidence_id: identity-search
  kind: search
  reference: REVIEW_WORK/batch056/record01/identity-search.json
  accessed_at: '2026-10-28T05:17:30.475410Z'
  support: supports
  summary: Exact stable ID resolves the selected generated record and its declared
    maintained contributor.
  snapshot_sha256: d514adf7a9175b3b3d3a9d308bad174e245167c92f68dcf74268020611c17334
  search_scope: Exact stable record ID across complete normalized and merged YAML
    trees, including hidden and ignored files. Other accession/name records are not
    automatically contributing owners.
- evidence_id: chebi17634
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17634
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:11:34.653693Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 6e02f3cee82012b7f630c04f122676c0029753074a4421cb005301b8bf24cedb
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_26710
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:11:35.261154Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: b145f4ff9b90ebb993ff576d9ab35a6c10b7c42a3b99e18feffcc8d75c0e1e50
- evidence_id: chebi26709
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_26709
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:11:35.257752Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: f72f44fc092597deea0396efe53f8fe7e6088b16ac68c8540265991f6b3415a7
- evidence_id: chebi50385
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_50385
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:11:35.867181Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 9531274295a20e5b89ae5c0a87c0772ec355c40948c99661eacec8d887712a8a
- evidence_id: chebi28869
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_28869
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T05:11:35.629824Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 4715ccbed9d157f51f1faec46f5f0a552319f187925f9119582a93b84e8c829b
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch056/record01/quantity-inventory.json
  accessed_at: '2026-10-28T05:17:30.479497Z'
  support: context_only
  summary: Complete local concentration and source-stage decision inventory; includes
    exact local paths and source failure limits.
  snapshot_sha256: 9aa6ad700327ed5a22c7f93d18c7824ae6c4542338aae633ba4a2979eda3c0bc
- evidence_id: grounding
  kind: record_content
  reference: REVIEW_WORK/batch056/record01/grounding-inventory.json
  accessed_at: '2026-10-28T05:17:30.479532Z'
  support: context_only
  summary: All recursive asserted identifier/label slots, exact current OLS objects
    and current packaged MIM preferred-row joins.
  snapshot_sha256: 39f6a0e87708ceacb278736d23f9a3cf09ef4f1fb5c2c3d607a1fb685163d79c
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch056/record01/history-and-evidence-inventory.json
  accessed_at: '2026-10-28T05:17:30.479564Z'
  support: context_only
  summary: Complete current history, references and attached evidence; source-specific
    claims are assessed without authenticating historical execution from code.
  snapshot_sha256: 82a4840337dbc7d64ced5c293eec5899558a2eafe4526d110647e88933a1c768
- evidence_id: scalars
  kind: record_content
  reference: REVIEW_WORK/batch056/record01/scalar-census.json
  accessed_at: '2026-10-28T05:17:30.479590Z'
  support: context_only
  summary: Lossless scalar census of the selected target and all maintained contributors.
  snapshot_sha256: 8222d70cfd3568cdf9324e080c91c5ffc845eb6479ca4b2aaf3bbf5ed0fce859
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch056/record01/validate-schema.json
  accessed_at: '2026-10-28T05:11:01.412857Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed

    '
  snapshot_sha256: 90a43bd5cdf79e9d644934c45e2fd1416d381bd1a457f58aab1c730dd3724f0b
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch056/record01/validate-strict.json
  accessed_at: '2026-10-28T05:11:02.474407Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch056/record01/strict.tsv\n"
  snapshot_sha256: 2416eada814b28c3787bde8ce5954130c9e2216d2df369856b466ea8ea2815a7
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch056/record01/validate-terms.json
  accessed_at: '2026-10-28T05:11:03.683621Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed

    '
  snapshot_sha256: c1526183417e7f0377f9cebb963fd88254549950e07dccf833ae42dad8ffbe2b
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch056/record01/validate-references.json
  accessed_at: '2026-10-28T05:11:04.406822Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed

    '
  snapshot_sha256: e8cd2f8c567183a57b35e6029a31180f1e6b4321ec63a8afd67a240d35e3625e
assessments:
- assessment_id: a1
  area: identity
  topic: Exact FEBA block and generated ownership
  outcome: supported
  summary: The selected record is the one-owner CultureBotHT Brucella broth import.
    Its label, description, eight component names and all eight values match the current
    exact FEBA block. Similarly named blood-agar formulations are not this target.
  target_ids:
  - CultureMech:015499
  evidence_ids:
  - local-target
  - owner-1
  - febaMedia
  - identity-search
- assessment_id: a2
  area: scope
  topic: Unchanged classification and missing optional claims
  outcome: supported
  summary: COMPLEX, UNDEFINED and LIQUID agree with the named broth and undefined
    digests/extract. Specialized filing is the importer fallback, not an organism
    claim. No organism, strain growth, preparation, pH or missing stock dose is asserted
    by the scoped FEBA block; empty optional fields are not filled from familiar Brucella
    recipes.
  target_ids:
  - CultureMech:015499
  evidence_ids:
  - febaMedia
  - writer-culturebotht
  - owner-1
- assessment_id: a3
  area: grounding
  topic: Chemical identity and catalog limits
  outcome: supported
  summary: All five primary CHEBI labels match current non-obsolete OLS objects; their
    CAS identities correspond. Three undefined components lack primary mappings and
    all eight ingredients lack secondary MIM slots; these are linkage counts, not
    scientific-failure percentages. The existing unmapped flag is accurate. Confidence0.90
    notes are historical mapping metadata rather than an independently reproduced
    calibration.
  target_ids:
  - CultureMech:015499
  evidence_ids:
  - grounding
  - febaCompounds
  - local-target
- assessment_id: a4
  area: quantity
  topic: Quantity scope and inventory
  outcome: concern
  summary: Every selected target/owner concentration field has an explicit disposition;
    scoped dependency fields and source-only preparation are separate from receiving-medium
    rates.
  target_ids:
  - CultureMech:015499
  evidence_ids:
  - quantities
  details: '[{"quantity_id": "q1", "topic": "Pancreatic digest of casein", "source":
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch056/source01-03-supplement/febaMedia.bin", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "Brucella block; physical line4581; explicit concentration/unit header line4580",
    "accessed_at": "2026-10-28T05:12:08.334028Z", "quote": "Pancreatic digest of casein\t10\tg/L"},
    "decision": "evidence_only", "rationale": "The exact commit-pinned FEBA Brucella
    row explicitly declares this numerical value in g/L. Retain it and add claim-level
    source linkage; no water-input assumption or stock dilution is used. This current
    correspondence does not authenticate the unavailable historical CultureBotHT export.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/Brucella.yaml", "field_path":
    "ingredients[0].concentration", "stored_value": {"value": "10", "unit": "G_PER_L"},
    "decision": "evidence_only", "rationale": "The exact commit-pinned FEBA Brucella
    row explicitly declares this numerical value in g/L. Retain it and add claim-level
    source linkage; no water-input assumption or stock dilution is used. This current
    correspondence does not authenticate the unavailable historical CultureBotHT export."},
    {"path": "data/normalized_yaml/specialized/brucella.yaml", "field_path": "ingredients[0].concentration",
    "stored_value": {"value": "10", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "The exact commit-pinned FEBA Brucella row explicitly declares this
    numerical value in g/L. Retain it and add claim-level source linkage; no water-input
    assumption or stock dilution is used. This current correspondence does not authenticate
    the unavailable historical CultureBotHT export."}]}, {"quantity_id": "q2", "topic":
    "Peptic digest of animal tissue", "source": {"evidence_id": "febaMedia", "reference":
    "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch056/source01-03-supplement/febaMedia.bin", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "Brucella block; physical line4582; explicit concentration/unit header line4580",
    "accessed_at": "2026-10-28T05:12:08.334028Z", "quote": "Peptic digest of animal
    tissue\t10\tg/L"}, "decision": "evidence_only", "rationale": "The exact commit-pinned
    FEBA Brucella row explicitly declares this numerical value in g/L. Retain it and
    add claim-level source linkage; no water-input assumption or stock dilution is
    used. This current correspondence does not authenticate the unavailable historical
    CultureBotHT export.", "layer_assessments": [{"path": "data/merge_yaml/merged/Brucella.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "10",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact commit-pinned
    FEBA Brucella row explicitly declares this numerical value in g/L. Retain it and
    add claim-level source linkage; no water-input assumption or stock dilution is
    used. This current correspondence does not authenticate the unavailable historical
    CultureBotHT export."}, {"path": "data/normalized_yaml/specialized/brucella.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "10",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact commit-pinned
    FEBA Brucella row explicitly declares this numerical value in g/L. Retain it and
    add claim-level source linkage; no water-input assumption or stock dilution is
    used. This current correspondence does not authenticate the unavailable historical
    CultureBotHT export."}]}, {"quantity_id": "q3", "topic": "D-Glucose", "source":
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch056/source01-03-supplement/febaMedia.bin", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "Brucella block; physical line4583; explicit concentration/unit header line4580",
    "accessed_at": "2026-10-28T05:12:08.334028Z", "quote": "D-Glucose\t1\tg/L"}, "decision":
    "evidence_only", "rationale": "The exact commit-pinned FEBA Brucella row explicitly
    declares this numerical value in g/L. Retain it and add claim-level source linkage;
    no water-input assumption or stock dilution is used. This current correspondence
    does not authenticate the unavailable historical CultureBotHT export.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Brucella.yaml", "field_path": "ingredients[2].concentration",
    "stored_value": {"value": "1", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "The exact commit-pinned FEBA Brucella row explicitly declares this
    numerical value in g/L. Retain it and add claim-level source linkage; no water-input
    assumption or stock dilution is used. This current correspondence does not authenticate
    the unavailable historical CultureBotHT export."}, {"path": "data/normalized_yaml/specialized/brucella.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "1", "unit":
    "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact commit-pinned
    FEBA Brucella row explicitly declares this numerical value in g/L. Retain it and
    add claim-level source linkage; no water-input assumption or stock dilution is
    used. This current correspondence does not authenticate the unavailable historical
    CultureBotHT export."}]}, {"quantity_id": "q4", "topic": "Yeast Extract", "source":
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch056/source01-03-supplement/febaMedia.bin", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "Brucella block; physical line4584; explicit concentration/unit header line4580",
    "accessed_at": "2026-10-28T05:12:08.334028Z", "quote": "Yeast Extract\t2\tg/L"},
    "decision": "evidence_only", "rationale": "The exact commit-pinned FEBA Brucella
    row explicitly declares this numerical value in g/L. Retain it and add claim-level
    source linkage; no water-input assumption or stock dilution is used. This current
    correspondence does not authenticate the unavailable historical CultureBotHT export.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/Brucella.yaml", "field_path":
    "ingredients[3].concentration", "stored_value": {"value": "2", "unit": "G_PER_L"},
    "decision": "evidence_only", "rationale": "The exact commit-pinned FEBA Brucella
    row explicitly declares this numerical value in g/L. Retain it and add claim-level
    source linkage; no water-input assumption or stock dilution is used. This current
    correspondence does not authenticate the unavailable historical CultureBotHT export."},
    {"path": "data/normalized_yaml/specialized/brucella.yaml", "field_path": "ingredients[3].concentration",
    "stored_value": {"value": "2", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "The exact commit-pinned FEBA Brucella row explicitly declares this
    numerical value in g/L. Retain it and add claim-level source linkage; no water-input
    assumption or stock dilution is used. This current correspondence does not authenticate
    the unavailable historical CultureBotHT export."}]}, {"quantity_id": "q5", "topic":
    "Sodium Chloride", "source": {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch056/source01-03-supplement/febaMedia.bin", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "Brucella block; physical line4585; explicit concentration/unit header line4580",
    "accessed_at": "2026-10-28T05:12:08.334028Z", "quote": "Sodium Chloride\t5\tg/L"},
    "decision": "evidence_only", "rationale": "The exact commit-pinned FEBA Brucella
    row explicitly declares this numerical value in g/L. Retain it and add claim-level
    source linkage; no water-input assumption or stock dilution is used. This current
    correspondence does not authenticate the unavailable historical CultureBotHT export.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/Brucella.yaml", "field_path":
    "ingredients[4].concentration", "stored_value": {"value": "5", "unit": "G_PER_L"},
    "decision": "evidence_only", "rationale": "The exact commit-pinned FEBA Brucella
    row explicitly declares this numerical value in g/L. Retain it and add claim-level
    source linkage; no water-input assumption or stock dilution is used. This current
    correspondence does not authenticate the unavailable historical CultureBotHT export."},
    {"path": "data/normalized_yaml/specialized/brucella.yaml", "field_path": "ingredients[4].concentration",
    "stored_value": {"value": "5", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "The exact commit-pinned FEBA Brucella row explicitly declares this
    numerical value in g/L. Retain it and add claim-level source linkage; no water-input
    assumption or stock dilution is used. This current correspondence does not authenticate
    the unavailable historical CultureBotHT export."}]}, {"quantity_id": "q6", "topic":
    "Sodium bisulfite", "source": {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch056/source01-03-supplement/febaMedia.bin", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "Brucella block; physical line4586; explicit concentration/unit header line4580",
    "accessed_at": "2026-10-28T05:12:08.334028Z", "quote": "Sodium bisulfite\t0.1\tg/L"},
    "decision": "evidence_only", "rationale": "The exact commit-pinned FEBA Brucella
    row explicitly declares this numerical value in g/L. Retain it and add claim-level
    source linkage; no water-input assumption or stock dilution is used. This current
    correspondence does not authenticate the unavailable historical CultureBotHT export.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/Brucella.yaml", "field_path":
    "ingredients[5].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"},
    "decision": "evidence_only", "rationale": "The exact commit-pinned FEBA Brucella
    row explicitly declares this numerical value in g/L. Retain it and add claim-level
    source linkage; no water-input assumption or stock dilution is used. This current
    correspondence does not authenticate the unavailable historical CultureBotHT export."},
    {"path": "data/normalized_yaml/specialized/brucella.yaml", "field_path": "ingredients[5].concentration",
    "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "The exact commit-pinned FEBA Brucella row explicitly declares this
    numerical value in g/L. Retain it and add claim-level source linkage; no water-input
    assumption or stock dilution is used. This current correspondence does not authenticate
    the unavailable historical CultureBotHT export."}]}, {"quantity_id": "q7", "topic":
    "Hemin", "source": {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch056/source01-03-supplement/febaMedia.bin", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "Brucella block; physical line4587; explicit concentration/unit header line4580",
    "accessed_at": "2026-10-28T05:12:08.334028Z", "quote": "Hemin\t0.005\tg/L"}, "decision":
    "evidence_only", "rationale": "The exact commit-pinned FEBA Brucella row explicitly
    declares this numerical value in g/L. Retain it and add claim-level source linkage;
    no water-input assumption or stock dilution is used. This current correspondence
    does not authenticate the unavailable historical CultureBotHT export.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Brucella.yaml", "field_path": "ingredients[6].concentration",
    "stored_value": {"value": "0.005", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "The exact commit-pinned FEBA Brucella row explicitly declares this
    numerical value in g/L. Retain it and add claim-level source linkage; no water-input
    assumption or stock dilution is used. This current correspondence does not authenticate
    the unavailable historical CultureBotHT export."}, {"path": "data/normalized_yaml/specialized/brucella.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "0.005",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "The exact commit-pinned
    FEBA Brucella row explicitly declares this numerical value in g/L. Retain it and
    add claim-level source linkage; no water-input assumption or stock dilution is
    used. This current correspondence does not authenticate the unavailable historical
    CultureBotHT export."}]}, {"quantity_id": "q8", "topic": "Menadione", "source":
    {"evidence_id": "febaMedia", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/media",
    "raw_path": "REVIEW_WORK/batch056/source01-03-supplement/febaMedia.bin", "raw_sha256":
    "a15dc82b1cbb0ae2c1a9a5d4b4d83b80364da1fc9a55b6ff1357d7988ce14848", "locator":
    "Brucella block; physical line4588; explicit concentration/unit header line4580",
    "accessed_at": "2026-10-28T05:12:08.334028Z", "quote": "Menadione\t0.001\tg/L"},
    "decision": "evidence_only", "rationale": "The exact commit-pinned FEBA Brucella
    row explicitly declares this numerical value in g/L. Retain it and add claim-level
    source linkage; no water-input assumption or stock dilution is used. This current
    correspondence does not authenticate the unavailable historical CultureBotHT export.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/Brucella.yaml", "field_path":
    "ingredients[7].concentration", "stored_value": {"value": "0.001", "unit": "G_PER_L"},
    "decision": "evidence_only", "rationale": "The exact commit-pinned FEBA Brucella
    row explicitly declares this numerical value in g/L. Retain it and add claim-level
    source linkage; no water-input assumption or stock dilution is used. This current
    correspondence does not authenticate the unavailable historical CultureBotHT export."},
    {"path": "data/normalized_yaml/specialized/brucella.yaml", "field_path": "ingredients[7].concentration",
    "stored_value": {"value": "0.001", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "The exact commit-pinned FEBA Brucella row explicitly declares this
    numerical value in g/L. Retain it and add claim-level source linkage; no water-input
    assumption or stock dilution is used. This current correspondence does not authenticate
    the unavailable historical CultureBotHT export."}]}, {"quantity_id": "q9", "topic":
    "D-Glucose descriptive molecular-weight note", "source": {"evidence_id": "febaCompounds",
    "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
    "raw_path": "REVIEW_WORK/batch056/source01-03-supplement/febaCompounds.bin", "raw_sha256":
    "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774", "locator":
    "Exact Compound row D-Glucose", "accessed_at": "2026-10-28T05:12:08.363539Z",
    "quote": "D-Glucose\t50-99-7\tSigma\tG7528\t180.16\tglucose\t\t\t\tyes\t\t\t"},
    "decision": "evidence_only", "rationale": "The local CAS and listed molecular-weight
    digits correspond to this exact FEBA compound metadata row. Current OLS independently
    supports the accession/CAS identity. These metadata digits are not used for a
    molar conversion; hemin FW651.94 is retained as FEBA metadata rather than silently
    replaced with current OLS651.952.", "layer_assessments": [{"path": "data/merge_yaml/merged/Brucella.yaml",
    "field_path": "ingredients[2].notes", "stored_value": "Mapping: micromediaparam_legacy
    (confidence: 0.90); CAS: 50-99-7; MW: 180.16", "decision": "evidence_only", "rationale":
    "The local CAS and listed molecular-weight digits correspond to this exact FEBA
    compound metadata row. Current OLS independently supports the accession/CAS identity.
    These metadata digits are not used for a molar conversion; hemin FW651.94 is retained
    as FEBA metadata rather than silently replaced with current OLS651.952."}, {"path":
    "data/normalized_yaml/specialized/brucella.yaml", "field_path": "ingredients[2].notes",
    "stored_value": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 50-99-7;
    MW: 180.16", "decision": "evidence_only", "rationale": "The local CAS and listed
    molecular-weight digits correspond to this exact FEBA compound metadata row. Current
    OLS independently supports the accession/CAS identity. These metadata digits are
    not used for a molar conversion; hemin FW651.94 is retained as FEBA metadata rather
    than silently replaced with current OLS651.952."}]}, {"quantity_id": "q10", "topic":
    "Sodium Chloride descriptive molecular-weight note", "source": {"evidence_id":
    "febaCompounds", "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
    "raw_path": "REVIEW_WORK/batch056/source01-03-supplement/febaCompounds.bin", "raw_sha256":
    "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774", "locator":
    "Exact Compound row Sodium Chloride", "accessed_at": "2026-10-28T05:12:08.363539Z",
    "quote": "Sodium Chloride\t7647-14-5\tSigma\tS3014\t58.44\tNaCl\t\t\tyes\t\t\tyes\t"},
    "decision": "evidence_only", "rationale": "The local CAS and listed molecular-weight
    digits correspond to this exact FEBA compound metadata row. Current OLS independently
    supports the accession/CAS identity. These metadata digits are not used for a
    molar conversion; hemin FW651.94 is retained as FEBA metadata rather than silently
    replaced with current OLS651.952.", "layer_assessments": [{"path": "data/merge_yaml/merged/Brucella.yaml",
    "field_path": "ingredients[4].notes", "stored_value": "CAS: 7647-14-5; MW: 58.44",
    "decision": "evidence_only", "rationale": "The local CAS and listed molecular-weight
    digits correspond to this exact FEBA compound metadata row. Current OLS independently
    supports the accession/CAS identity. These metadata digits are not used for a
    molar conversion; hemin FW651.94 is retained as FEBA metadata rather than silently
    replaced with current OLS651.952."}, {"path": "data/normalized_yaml/specialized/brucella.yaml",
    "field_path": "ingredients[4].notes", "stored_value": "CAS: 7647-14-5; MW: 58.44",
    "decision": "evidence_only", "rationale": "The local CAS and listed molecular-weight
    digits correspond to this exact FEBA compound metadata row. Current OLS independently
    supports the accession/CAS identity. These metadata digits are not used for a
    molar conversion; hemin FW651.94 is retained as FEBA metadata rather than silently
    replaced with current OLS651.952."}]}, {"quantity_id": "q11", "topic": "Hemin
    descriptive molecular-weight note", "source": {"evidence_id": "febaCompounds",
    "reference": "https://api.bitbucket.org/2.0/repositories/berkeleylab/feba/src/803273865ea9e83fab770ec4f13670db80e1180b/metadata/Compounds.tsv",
    "raw_path": "REVIEW_WORK/batch056/source01-03-supplement/febaCompounds.bin", "raw_sha256":
    "25a74faf66ea4a186ff1e7b779b6d03e552c565aa138c42cb737347ac35df774", "locator":
    "Exact Compound row Hemin", "accessed_at": "2026-10-28T05:12:08.363539Z", "quote":
    "Hemin\t16009-13-5\tsigmaaldrich\tH9039-10G\t651.94\tChloro(protoporphyrinato)iron(III),
    Chlorohemin, Chloroprotoporphyrin IX iron(III), Ferriprotoporphyrin IX chloride,
    Hemin(chloride)\t\t\t\t\t\t\t"}, "decision": "evidence_only", "rationale": "The
    local CAS and listed molecular-weight digits correspond to this exact FEBA compound
    metadata row. Current OLS independently supports the accession/CAS identity. These
    metadata digits are not used for a molar conversion; hemin FW651.94 is retained
    as FEBA metadata rather than silently replaced with current OLS651.952.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/Brucella.yaml", "field_path": "ingredients[6].notes",
    "stored_value": "Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 16009-13-5;
    MW: 651.94", "decision": "evidence_only", "rationale": "The local CAS and listed
    molecular-weight digits correspond to this exact FEBA compound metadata row. Current
    OLS independently supports the accession/CAS identity. These metadata digits are
    not used for a molar conversion; hemin FW651.94 is retained as FEBA metadata rather
    than silently replaced with current OLS651.952."}, {"path": "data/normalized_yaml/specialized/brucella.yaml",
    "field_path": "ingredients[6].notes", "stored_value": "Mapping: micromediaparam_legacy
    (confidence: 0.90); CAS: 16009-13-5; MW: 651.94", "decision": "evidence_only",
    "rationale": "The local CAS and listed molecular-weight digits correspond to this
    exact FEBA compound metadata row. Current OLS independently supports the accession/CAS
    identity. These metadata digits are not used for a molar conversion; hemin FW651.94
    is retained as FEBA metadata rather than silently replaced with current OLS651.952."}]}]'
- assessment_id: a5
  area: grounding
  topic: Current ontology and MIM correspondence
  outcome: supported
  summary: The grounding inventory enumerates every asserted identifier and exact
    preferred label. Exact identifier rows and ontology-linked rows are recorded separately,
    including mapping_status. Present catalog membership does not validate supplied
    hydrate form or historical identity; specific limits are assessed separately.
  target_ids:
  - CultureMech:015499
  evidence_ids:
  - grounding
- assessment_id: a6
  area: provenance
  topic: History and evidence scope
  outcome: supported
  summary: Complete owner and target histories were read. Current source bytes and
    inspected code are independent evidence; historical timestamps remain historical
    claims unless an exact cited raw digest is recovered.
  target_ids:
  - CultureMech:015499
  evidence_ids:
  - history
  - scalars
- assessment_id: a7
  area: scope
  topic: Growth and taxonomic evidence
  outcome: unknown
  summary: Generic cultivation applications and bacterial filing are not strain-level
    growth evidence. No organism-specific growth, temperature or atmosphere is inferred
    from names or source catalog identifiers.
  target_ids:
  - CultureMech:015499
  evidence_ids:
  - local-target
- assessment_id: a8
  area: schema
  topic: Canonical diagnostics
  outcome: supported
  summary: All four original canonical diagnostics passed. Reference checks were zero;
    structural and term diagnostics do not establish formulation accuracy.
  target_ids:
  - CultureMech:015499
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-015499-the-exact-current-feba-support-is-absent-from-the-import-trail
  category: provenance
  severity: major
  status: open
  certainty: confirmed
  title: The exact current FEBA support is absent from the import trail
  description: The record cites only an unavailable CultureBotHT repository root.
    The newly inspected commit-pinned FEBA block positively supports the eight current
    concentrations, but neither that later revision nor a candidate raw-file404 proves
    the exact bytes imported in March. No claim-level source evidence or pinned FEBA
    reference is stored.
  target_ids:
  - CultureMech:015499
  field_paths:
  - sources
  - references
  - ingredients
  evidence_ids:
  - febaMedia
  - febaCommit
  - culturebotht
  - culturebothtRaw
  - writer-culturebotht
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/brucella.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f2
  issue_key: culturemech-015499-yeast-extract-notes-label-a-non-cas-shaped-token-as-cas
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Yeast extract notes label a non-CAS-shaped token as CAS
  description: ingredients[3].notes says CAS:232-387-9. The FEBA compound table repeats
    that token, but its three-digit middle group does not meet CAS-RN syntax. Agreement
    with a source table does not validate its identifier namespace. No alternative
    identifier or EC identity has been independently established.
  target_ids:
  - CultureMech:015499
  field_paths:
  - ingredients[3].notes
  evidence_ids:
  - febaCompounds
  - local-target
  rule_id: identifier-namespace-format
  native_severity: P3
  normalization_reason: 'Minor: bounded metadata or traceability defect without establishing
    a new formulation.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/brucella.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
actions:
- action_id: action1
  description: Add exact commit-pinned FEBA reference and row-level support for the
    existing values. Keep the unverified historical CultureBotHT export/version as
    a separate limitation; do not claim it was recovered. Maintain original history
    and regenerate the generated record after owner curation.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:015499
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/brucella.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action2
  description: Qualify or remove the unsupported CAS namespace assertion while preserving
    the literal historical source token. Resolve any replacement namespace/identifier
    independently; do not guess one.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:015499
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/specialized/brucella.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
limitations:
- The March CultureBotHT file and export revision were not recovered; both current
  repository and candidate main-file access returned404. The exact FEBA source accessed
  here is a later pinned revision.
- The scoped FEBA block gives explicit g/L rates but no preparation, pH, organism
  or growth claim. No generic recipe or supplier variant was imported to fill these
  omissions.
- Current OLS/MIM metadata does not establish historical mapping validity. Undefined
  digests and extract remain mixtures; no density or molar conversion is inferred.
- All three exact historical reports were read as derivative observations. Their old
  access events and unrecovered raw payloads are not authenticated by current source
  agreement.
notes:
- Fresh review; historical lost snapshots were not reconstructed. All inspected source
  files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this
  author.
```
