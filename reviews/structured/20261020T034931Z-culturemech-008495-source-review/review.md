# Source and formulation review: 1_10_brain_heart_infusion_agar_17_estradiol (CultureMech:008495)

- Review: 20261020T034931Z-culturemech-008495-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-19T23:41:08Z
- Finished UTC: 2026-10-20T03:49:31Z
- Reviewer: OpenAI Codex with delegated source and validator checks (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

TOGO M1917/NBRC1181 identity resolves, but the source commercial premix has been replaced by unsupported constituent amounts. Water and estradiol units also disagree with source. The review records one blocker and two major findings; catalog existence is verified separately from formulation suitability.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Record 28 in Python lexicographic repository-relative path order of the initially uncovered merged corpus; Batch 003 selects ordinals 21-30 after the first two reserved batches; saved bundles are published locally in path order. On fresh origin/main at this batch base, scripts/record_review.py list validated 34 existing bundles and none listed this target path or ID. This bundle selects only the named record; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7c568537897ee4bba1b8e97f8172133c1572aec0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:008495 | data/merge_yaml/merged/1_10_brain_heart_infusion_agar_17_estradiol.yaml | generated | 1_10_brain_heart_infusion_agar_17_estradiol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:008495 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:008495 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-003/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch003/028/strict.tsv |
| validate-terms | passed | True | CultureMech:008495 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:008495 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:008495 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:008495.

The four documented recipes completed; interpret the scope of each separately.

### Exact source accession and commercial boundary

identity: concern. Targets: CultureMech:008495.

The medium accession and original source link identify NBRC1181 correctly. Its commercial premix dose is absent, replaced by constituent rows not established for this recipe. Catalog237500 is real, but source accession resolution does not certify the expanded formulation.

### All nine direct quantities and source premix

quantity: concern. Targets: CultureMech:008495.

Water and supplement dimensions are wrong; optional agar source mass is retained nominally; six premix-derived rows are unsupported in this receiving formulation.

ingredients[0]: correct; source water is1L, not1G_PER_L. No density conversion is justified.
ingredients[1]: correct; source estradiol is1mg per batch. Target1G_PER_L uses the gram rather than milligram scale; 1mg=0.001g, while final-volume normalization remains unproved.
ingredients[2]: source15g optional agar is verified as batch mass; stored15G_PER_L is nominal on added water, not measured final volume.
ingredients[3] and [4]: variable concentration does not validate notes claiming infusion source200g/L calf brain and250g/L beef heart; these quantities are not supplied by NBRC1181. Tissue-source masses are not dry infusion masses.
ingredients[5] through [8]: direct10,2,5,2.5G_PER_L peptone/dextrose/NaCl/phosphate resemble the cited general table, not the source diluted product dose. Their sum is19.5g before infusion material, exceeding the source3.7g premix dose under the same nominal liter convention.
Source premix3.7g per batch is missing. Preserve its product boundary; do not assume scaling the listed constituents alone reconstructs the exact commercial formulation.

### All asserted ontology IDs and supplier accession

grounding: supported. Targets: CultureMech:008495.

Seven primary IDs resolve: four CHEBI, two UBERON organs and one MICRO peptone; the single secondary water key resolves. Primary linkage7/9 (77.8%) and secondary1/9 (11.1%) are linkage metrics only. Dextrose identity is supported; generic glucose synonym is broader. Organ mappings are meaningful only as tissue-source context, not precise infusion identities. No exact estradiol or agar chemical ID is asserted.

### Preparation, pH, roles and growth scope

scope: concern. Targets: CultureMech:008495.

The pH7.4±0.2 embedded in a constituent note comes from a general formulation context, not the NBRC recipe. No source-specific preparation or incubation protocol is supplied. TOGO growth-factor/solidifier annotations are database roles, not proof of organism growth. No organism or measured growth outcome is asserted. Do not transfer the cited article organisms or procedures to this record.

### Physical state and mixture class

scope: supported. Targets: CultureMech:008495.

COMPLEX/UNDEFINED agrees with source commercial mixture. SOLID_AGAR is compatible with the selected optional-agar branch; the source also permits its omission. Supplier names alone do not establish exact constituent or species provenance.

### Owner agreement and provenance limits

provenance: concern. Targets: CultureMech:008495.

Target and normalized owner contain the same scientific assertions apart from merge bookkeeping. The narrative says composition was researched from a product specification but links a secondary general article. Manufacturer catalog existence was independently verified; formulation attribution remains unsupported. Correct maintained source before authorized regeneration, without treating an importer-history event as scientific approval.

## Findings

### f1: Commercial premix was replaced by an unsupported formulation

blocker / open / confirmed; issue key: culturemech-008495-unsupported-premix-expansion.

NBRC1181 uses a specified premix dose. The target replaces it with six expanded components at amounts and tissue-source levels not supported for the diluted recipe. Citing a general BHI agar table and a real catalog number does not establish these quantities or final pH for this medium.

### f2: Estradiol source milligrams are represented on a gram scale

major / open / confirmed; issue key: culturemech-008495-estradiol-mg-to-g-error.

The source supplement is expressed in mg per batch; target and owner retain numerical1 but assert G_PER_L. The source does not justify this mass-unit change or an exact final-volume claim.

### f3: Preparation water is represented as mass concentration

major / open / confirmed; issue key: culturemech-008495-water-volume-as-mass-concentration.

Source water is1L; target and owner assert1G_PER_L. Volume is not mass concentration, and no density/final-volume evidence supports the conversion.

## Recommended Actions And Acceptance Checks

### a1

Restore the verified source premix boundary and dose in the normalized owner during authorized curation. Retain any constituent information only as separately supported product context with correct scope; do not silently scale a generic formula or transfer its pH.

- Compare repaired owner against exact source recipe, preserving premix identity and batch units.
- Run four documented target validators and inspect source-evidence coverage.
- After separately authorized regeneration run merge freshness and verification gates.

### a2

Preserve the literal source mass and batch basis during authorized curation, using dimensionally valid units and evidence. Do not infer a measured final concentration from water alone.

- Compare repaired owner against exact source recipe, preserving premix identity and batch units.
- Run four documented target validators and inspect source-evidence coverage.
- After separately authorized regeneration run merge freshness and verification gates.

### a3

Represent source water volume and preparation basis in the normalized owner during authorized curation, without guessing density or final volume.

- Compare repaired owner against exact source recipe, preserving premix identity and batch units.
- Run four documented target validators and inspect source-evidence coverage.
- After separately authorized regeneration run merge freshness and verification gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/1_10_brain_heart_infusion_agar_17_estradiol.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/1_10_brain_heart_infusion_agar_17_estradiol.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/1_10_brain_heart_infusion_agar_17_estradiol.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/1_10_brain_heart_infusion_agar_17_estradiol.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch003/028/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-003/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch003/028/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/1_10_brain_heart_infusion_agar_17_estradiol.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/1_10_brain_heart_infusion_agar_17_estradiol.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| nbrc | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1181; Complete composition section | supports | NBRC1181 specifies commercial Bacto Brain Heart Infusion, estradiol in mg, water in L and optional agar. It does not give the expanded six-component formula, pH or preparation protocol asserted or implied by the target. |
| togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1917; $.meta; $.components[0].items; $.comments | supports | M1917 maps explicitly to NBRC_M1181. Four source rows preserve the premix boundary, mg supplement unit, water volume and optional agar. Growth-factor wording is a database annotation, not experimental growth evidence. |
| manufacturer | https://www.bd.com/en-us/products-and-solutions/products/product-page.237500; Product title and SKU section, inspected live | partial | Manufacturer confirms catalog237500 as BD BACTO Brain Heart Infusion500g. This establishes a real product accession; the inspected page does not establish the target constituent amounts for NBRC1181. |
| cited-secondary | https://microbenotes.com/brain-heart-infusion-bhi-agar/; Cited article composition table and final-pH line, inspected live | context_only | The record-cited article presents a general BHI agar table and final pH7.4±0.2. It is not a manufacturer specification for this NBRC diluted formulation. It lists HM infusion powder and BHI powder rather than the target anatomical infusion-source rows. Inspected only to audit the record citation, not as authoritative formulation evidence. |
| uberon-0000955 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON:0000955; Official OLS API exact obo_id and label | supports | Resolved UBERON:0000955 to brain. Organ classes do not establish calf/beef taxon, extraction process or commercial infusion amount; proteose-peptone label does not prove inclusion at the recorded dose. |
| uberon-0000948 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON:0000948; Official OLS API exact obo_id and label | supports | Resolved UBERON:0000948 to heart. Organ classes do not establish calf/beef taxon, extraction process or commercial infusion amount; proteose-peptone label does not prove inclusion at the recorded dose. |
| micro-0000180 | https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?obo_id=MICRO:0000180; Official OLS API exact obo_id and label | supports | Resolved MICRO:0000180 to proteose peptone. Organ classes do not establish calf/beef taxon, extraction process or commercial infusion amount; proteose-peptone label does not prove inclusion at the recorded dose. |
| chebi-17634 | https://www.ebi.ac.uk/chebi/CHEBI:17634; Official ChEBI ID/name and definition/synonym context, inspected live | supports | D-glucose with D configuration; dextrose is an explicit synonym. Generic glucose is a broader parent class, so its EXACT synonym scope should not erase stereochemistry. |
| chebi-34683 | https://www.ebi.ac.uk/chebi/CHEBI:34683; Official ChEBI ID/name and definition/synonym context, inspected live | supports | disodium hydrogenphosphate; resolves the asserted identity, not the source powder form or quantity. |
| chebi-15377 | https://www.ebi.ac.uk/chebi/CHEBI:15377; ID/name/formula | supports | Resolved CHEBI:15377 water; identity alone does not validate supplied quantity. |
| chebi-26710 | https://www.ebi.ac.uk/chebi/CHEBI:26710; ID/name/formula | supports | Resolved CHEBI:26710 sodium chloride; identity alone does not validate supplied quantity. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Single asserted secondary key CHEBI:15377; companion metadata | supports | Water key resolves in the packaged index to MAPPED Distilled water. Snapshot source commit6643131b0f12ab40b66f98135245fca04027e0e9; CSV SHA2564765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5. |

## Limits And Additional Notes

- The manufacturer product page confirms catalog237500 identity, not the exact constituent formula or suitability of expansion for this diluted recipe. No corrected constituent recipe is synthesized.
- NBRC gives batch water volume, not measured final volume. All proposed quantity repairs must preserve source batch scope rather than infer density or final concentration.
- Anatomical IDs identify source organs, not species-specific processed infusions. Source-material notes are retained as context, not proof of commercial infusion composition.
- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T034931Z-culturemech-008495-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 1_10_brain_heart_infusion_agar_17_estradiol
  (CultureMech:008495)'
started_at: '2026-10-19T23:41:08Z'
finished_at: '2026-10-20T03:49:31Z'
reviewer:
  identity: OpenAI Codex with delegated source and validator checks
  kind: agent
  independence: independent
  independence_basis: Review team did not author or edit the assessed recipe bytes;
    findings were assessed against the frozen checkout and inspected source documents.
    This is an agent review, not experimental verification.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: TOGO M1917/NBRC1181 identity resolves, but the source commercial premix has
  been replaced by unsupported constituent amounts. Water and estradiol units also
  disagree with source. The review records one blocker and two major findings; catalog
  existence is verified separately from formulation suitability.
source:
  git_revision: 7c568537897ee4bba1b8e97f8172133c1572aec0
  state: working_tree
  inputs:
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
  - path: CLAUDE.md
    sha256: b5c5bb1c2293ba5f6c49cda8cb40bf36e021c0a2b9fe2d9497cf0a2fe19a1ac4
    role: context
  - path: conf/oak_config.yaml
    sha256: e35781d4fd66de4289411141b4c8a94189782d864ba6c45e49bf46537c46c5a1
    role: context
  - path: conf/record_review.yaml
    sha256: a76531e51214e559c97ab748a4cba169f8a9598ce6e3664518489b43dfc9bf88
    role: context
  - path: data/merge_yaml/merged/1_10_brain_heart_infusion_agar_17_estradiol.yaml
    sha256: 09ade61f4f6b6721c6f3d3f3ce8528dd47d8d2d00e077fdd6f430d5d31e58023
    role: target
  - path: data/normalized_yaml/bacterial/1_10_brain_heart_infusion_agar_17_estradiol.yaml
    sha256: 5acdbafc9ba20a9e4335cf36f78fca1e319138e2b1c81db2263346188e22ce8e
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
  - path: scripts/apply_mim_groundings.py
    sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/normalize_media_names_to_snake_case.py
    sha256: 59bd842b1982b7d62af9db3fe280df576d8c4ae2e9ee411bf2e52523355f95de
    role: context
  - path: scripts/validate_recipe_references.py
    sha256: 087e5f3128e774bc760b7dcfc8f194fe14820354f809be9e35cf6cacb8546a3b
    role: context
  - path: scripts/validate_strict.py
    sha256: d6775c8c53ee433426ad7d3ababdf1740fc6adc62cb8269cf07ca0cd251cef68
    role: context
  - path: src/culturemech/convert/togo_raw_yaml.py
    sha256: ce5e73545c9ecde54724259d2fd475676c0f3cb44dcfd283950e89fd49c10993
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
    role: context
  - path: src/culturemech/fetch/togo_fetcher.py
    sha256: 7aac40fe1d47e30810ae0be02f6e369ddb9bf657d630072595c62f46fb0bf339
    role: context
  - path: src/culturemech/import/togo_importer.py
    sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
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
  selection: Record 28 in Python lexicographic repository-relative path order of the
    initially uncovered merged corpus; Batch 003 selects ordinals 21-30 after the
    first two reserved batches; saved bundles are published locally in path order.
    On fresh origin/main at this batch base, scripts/record_review.py list validated
    34 existing bundles and none listed this target path or ID. This bundle selects
    only the named record; no sampling or fleet-wide scientific claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:008495
targets:
- target_id: CultureMech:008495
  path: data/merge_yaml/merged/1_10_brain_heart_infusion_agar_17_estradiol.yaml
  label: 1_10_brain_heart_infusion_agar_17_estradiol
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_brain_heart_infusion_agar_17_estradiol.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/1_10_brain_heart_infusion_agar_17_estradiol.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:008495
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/1_10_brain_heart_infusion_agar_17_estradiol.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch003/028/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-003/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch003/028/strict.tsv"
  target_ids:
  - CultureMech:008495
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/1_10_brain_heart_infusion_agar_17_estradiol.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:008495
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/1_10_brain_heart_infusion_agar_17_estradiol.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:008495
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
  - CultureMech:008495
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/1_10_brain_heart_infusion_agar_17_estradiol.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-20T03:49:31Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/1_10_brain_heart_infusion_agar_17_estradiol.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-20T03:49:31Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/1_10_brain_heart_infusion_agar_17_estradiol.yaml
  locator: Actual command output
  accessed_at: '2026-10-19T23:42:21.567465Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/1_10_brain_heart_infusion_agar_17_estradiol.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch003/028/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-19T23:42:23.378689Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-003/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch003/028/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/1_10_brain_heart_infusion_agar_17_estradiol.yaml
  locator: Actual command output
  accessed_at: '2026-10-19T23:42:26.156955Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/1_10_brain_heart_infusion_agar_17_estradiol.yaml
  locator: Actual command output
  accessed_at: '2026-10-19T23:42:27.456557Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: nbrc
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1181
  locator: Complete composition section
  accessed_at: '2026-10-19T23:37:54.168790Z'
  support: supports
  summary: NBRC1181 specifies commercial Bacto Brain Heart Infusion, estradiol in
    mg, water in L and optional agar. It does not give the expanded six-component
    formula, pH or preparation protocol asserted or implied by the target.
  snapshot_sha256: 2724a0074719e6a1ba3cb6b324fc3efb08557d978b430ab4a9f295af8fd57367
- evidence_id: togo
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1917
  locator: $.meta; $.components[0].items; $.comments
  accessed_at: '2026-10-19T23:37:54.015942Z'
  support: supports
  summary: M1917 maps explicitly to NBRC_M1181. Four source rows preserve the premix
    boundary, mg supplement unit, water volume and optional agar. Growth-factor wording
    is a database annotation, not experimental growth evidence.
  snapshot_sha256: 6977b91a697e0fde60c1aee818d1d26ab9bf24c817e76ee73e94c518ac618f36
- evidence_id: manufacturer
  kind: primary_source
  reference: https://www.bd.com/en-us/products-and-solutions/products/product-page.237500
  locator: Product title and SKU section, inspected live
  accessed_at: '2026-10-20T03:49:31Z'
  support: partial
  summary: Manufacturer confirms catalog237500 as BD BACTO Brain Heart Infusion500g.
    This establishes a real product accession; the inspected page does not establish
    the target constituent amounts for NBRC1181.
- evidence_id: cited-secondary
  kind: record_content
  reference: https://microbenotes.com/brain-heart-infusion-bhi-agar/
  locator: Cited article composition table and final-pH line, inspected live
  accessed_at: '2026-10-20T03:49:31Z'
  support: context_only
  summary: The record-cited article presents a general BHI agar table and final pH7.4±0.2.
    It is not a manufacturer specification for this NBRC diluted formulation. It lists
    HM infusion powder and BHI powder rather than the target anatomical infusion-source
    rows. Inspected only to audit the record citation, not as authoritative formulation
    evidence.
- evidence_id: uberon-0000955
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON:0000955
  locator: Official OLS API exact obo_id and label
  accessed_at: '2026-10-20T03:48:08.164681Z'
  support: supports
  summary: Resolved UBERON:0000955 to brain. Organ classes do not establish calf/beef
    taxon, extraction process or commercial infusion amount; proteose-peptone label
    does not prove inclusion at the recorded dose.
- evidence_id: uberon-0000948
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?obo_id=UBERON:0000948
  locator: Official OLS API exact obo_id and label
  accessed_at: '2026-10-20T03:48:09.196807Z'
  support: supports
  summary: Resolved UBERON:0000948 to heart. Organ classes do not establish calf/beef
    taxon, extraction process or commercial infusion amount; proteose-peptone label
    does not prove inclusion at the recorded dose.
- evidence_id: micro-0000180
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?obo_id=MICRO:0000180
  locator: Official OLS API exact obo_id and label
  accessed_at: '2026-10-20T03:48:10.128042Z'
  support: supports
  summary: Resolved MICRO:0000180 to proteose peptone. Organ classes do not establish
    calf/beef taxon, extraction process or commercial infusion amount; proteose-peptone
    label does not prove inclusion at the recorded dose.
- evidence_id: chebi-17634
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:17634
  locator: Official ChEBI ID/name and definition/synonym context, inspected live
  accessed_at: '2026-10-20T03:49:31Z'
  support: supports
  summary: D-glucose with D configuration; dextrose is an explicit synonym. Generic
    glucose is a broader parent class, so its EXACT synonym scope should not erase
    stereochemistry.
- evidence_id: chebi-34683
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:34683
  locator: Official ChEBI ID/name and definition/synonym context, inspected live
  accessed_at: '2026-10-20T03:49:31Z'
  support: supports
  summary: disodium hydrogenphosphate; resolves the asserted identity, not the source
    powder form or quantity.
- evidence_id: chebi-15377
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:15377
  locator: ID/name/formula
  accessed_at: '2026-10-19T23:32:48.413412Z'
  support: supports
  summary: Resolved CHEBI:15377 water; identity alone does not validate supplied quantity.
  snapshot_sha256: 1a98a50fba3aa8ec10dc2fd5c355cd22bc1a955252adbd43f4042fd2f1a3ee5d
- evidence_id: chebi-26710
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:26710
  locator: ID/name/formula
  accessed_at: '2026-10-19T23:32:12.913708Z'
  support: supports
  summary: Resolved CHEBI:26710 sodium chloride; identity alone does not validate
    supplied quantity.
  snapshot_sha256: 20d037f64aa7b26b83d04556c47a29bc5d4808bbdf7d25027e18ad22a5c5f02f
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Single asserted secondary key CHEBI:15377; companion metadata
  accessed_at: '2026-10-20T03:49:31Z'
  support: supports
  summary: Water key resolves in the packaged index to MAPPED Distilled water. Snapshot
    source commit6643131b0f12ab40b66f98135245fca04027e0e9; CSV SHA2564765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:008495
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Exact source accession and commercial boundary
  outcome: concern
  summary: The medium accession and original source link identify NBRC1181 correctly.
    Its commercial premix dose is absent, replaced by constituent rows not established
    for this recipe. Catalog237500 is real, but source accession resolution does not
    certify the expanded formulation.
  target_ids:
  - CultureMech:008495
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - togo
  - manufacturer
- assessment_id: amounts
  area: quantity
  topic: All nine direct quantities and source premix
  outcome: concern
  summary: Water and supplement dimensions are wrong; optional agar source mass is
    retained nominally; six premix-derived rows are unsupported in this receiving
    formulation.
  target_ids:
  - CultureMech:008495
  evidence_ids:
  - record
  - nbrc
  - togo
  - cited-secondary
  details: 'ingredients[0]: correct; source water is1L, not1G_PER_L. No density conversion
    is justified.

    ingredients[1]: correct; source estradiol is1mg per batch. Target1G_PER_L uses
    the gram rather than milligram scale; 1mg=0.001g, while final-volume normalization
    remains unproved.

    ingredients[2]: source15g optional agar is verified as batch mass; stored15G_PER_L
    is nominal on added water, not measured final volume.

    ingredients[3] and [4]: variable concentration does not validate notes claiming
    infusion source200g/L calf brain and250g/L beef heart; these quantities are not
    supplied by NBRC1181. Tissue-source masses are not dry infusion masses.

    ingredients[5] through [8]: direct10,2,5,2.5G_PER_L peptone/dextrose/NaCl/phosphate
    resemble the cited general table, not the source diluted product dose. Their sum
    is19.5g before infusion material, exceeding the source3.7g premix dose under the
    same nominal liter convention.

    Source premix3.7g per batch is missing. Preserve its product boundary; do not
    assume scaling the listed constituents alone reconstructs the exact commercial
    formulation.'
- assessment_id: grounding
  area: grounding
  topic: All asserted ontology IDs and supplier accession
  outcome: supported
  summary: 'Seven primary IDs resolve: four CHEBI, two UBERON organs and one MICRO
    peptone; the single secondary water key resolves. Primary linkage7/9 (77.8%) and
    secondary1/9 (11.1%) are linkage metrics only. Dextrose identity is supported;
    generic glucose synonym is broader. Organ mappings are meaningful only as tissue-source
    context, not precise infusion identities. No exact estradiol or agar chemical
    ID is asserted.'
  target_ids:
  - CultureMech:008495
  evidence_ids:
  - record
  - mim
  - manufacturer
  - uberon-0000955
  - uberon-0000948
  - micro-0000180
  - chebi-15377
  - chebi-17634
  - chebi-26710
  - chebi-34683
- assessment_id: conditions
  area: scope
  topic: Preparation, pH, roles and growth scope
  outcome: concern
  summary: The pH7.4±0.2 embedded in a constituent note comes from a general formulation
    context, not the NBRC recipe. No source-specific preparation or incubation protocol
    is supplied. TOGO growth-factor/solidifier annotations are database roles, not
    proof of organism growth. No organism or measured growth outcome is asserted.
    Do not transfer the cited article organisms or procedures to this record.
  target_ids:
  - CultureMech:008495
  evidence_ids:
  - record
  - nbrc
  - togo
  - cited-secondary
- assessment_id: classification
  area: scope
  topic: Physical state and mixture class
  outcome: supported
  summary: COMPLEX/UNDEFINED agrees with source commercial mixture. SOLID_AGAR is
    compatible with the selected optional-agar branch; the source also permits its
    omission. Supplier names alone do not establish exact constituent or species provenance.
  target_ids:
  - CultureMech:008495
  evidence_ids:
  - record
  - nbrc
  - togo
- assessment_id: ownership
  area: provenance
  topic: Owner agreement and provenance limits
  outcome: concern
  summary: Target and normalized owner contain the same scientific assertions apart
    from merge bookkeeping. The narrative says composition was researched from a product
    specification but links a secondary general article. Manufacturer catalog existence
    was independently verified; formulation attribution remains unsupported. Correct
    maintained source before authorized regeneration, without treating an importer-history
    event as scientific approval.
  target_ids:
  - CultureMech:008495
  evidence_ids:
  - record
  - owner-0
  - manufacturer
  - cited-secondary
  - nbrc
findings:
- finding_id: f1
  issue_key: culturemech-008495-unsupported-premix-expansion
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Commercial premix was replaced by an unsupported formulation
  description: NBRC1181 uses a specified premix dose. The target replaces it with
    six expanded components at amounts and tissue-source levels not supported for
    the diluted recipe. Citing a general BHI agar table and a real catalog number
    does not establish these quantities or final pH for this medium.
  target_ids:
  - CultureMech:008495
  field_paths:
  - ingredients[3]
  - ingredients[4]
  - ingredients[5]
  - ingredients[6]
  - ingredients[7]
  - ingredients[8]
  - notes
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - togo
  - manufacturer
  - cited-secondary
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_brain_heart_infusion_agar_17_estradiol.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f2
  issue_key: culturemech-008495-estradiol-mg-to-g-error
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Estradiol source milligrams are represented on a gram scale
  description: The source supplement is expressed in mg per batch; target and owner
    retain numerical1 but assert G_PER_L. The source does not justify this mass-unit
    change or an exact final-volume claim.
  target_ids:
  - CultureMech:008495
  field_paths:
  - ingredients[1].concentration
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - togo
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_brain_heart_infusion_agar_17_estradiol.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f3
  issue_key: culturemech-008495-water-volume-as-mass-concentration
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Preparation water is represented as mass concentration
  description: Source water is1L; target and owner assert1G_PER_L. Volume is not mass
    concentration, and no density/final-volume evidence supports the conversion.
  target_ids:
  - CultureMech:008495
  field_paths:
  - ingredients[0].concentration
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - togo
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_brain_heart_infusion_agar_17_estradiol.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Restore the verified source premix boundary and dose in the normalized
    owner during authorized curation. Retain any constituent information only as separately
    supported product context with correct scope; do not silently scale a generic
    formula or transfer its pH.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:008495
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_brain_heart_infusion_agar_17_estradiol.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Compare repaired owner against exact source recipe, preserving premix identity
    and batch units.
  - Run four documented target validators and inspect source-evidence coverage.
  - After separately authorized regeneration run merge freshness and verification
    gates.
- action_id: a2
  description: Preserve the literal source mass and batch basis during authorized
    curation, using dimensionally valid units and evidence. Do not infer a measured
    final concentration from water alone.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:008495
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_brain_heart_infusion_agar_17_estradiol.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Compare repaired owner against exact source recipe, preserving premix identity
    and batch units.
  - Run four documented target validators and inspect source-evidence coverage.
  - After separately authorized regeneration run merge freshness and verification
    gates.
- action_id: a3
  description: Represent source water volume and preparation basis in the normalized
    owner during authorized curation, without guessing density or final volume.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:008495
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_brain_heart_infusion_agar_17_estradiol.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Compare repaired owner against exact source recipe, preserving premix identity
    and batch units.
  - Run four documented target validators and inspect source-evidence coverage.
  - After separately authorized regeneration run merge freshness and verification
    gates.
limitations:
- The manufacturer product page confirms catalog237500 identity, not the exact constituent
  formula or suitability of expansion for this diluted recipe. No corrected constituent
  recipe is synthesized.
- NBRC gives batch water volume, not measured final volume. All proposed quantity
  repairs must preserve source batch scope rather than infer density or final concentration.
- Anatomical IDs identify source organs, not species-specific processed infusions.
  Source-material notes are retained as context, not proof of commercial infusion
  composition.
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
tags:
- unreviewed-records
- batch-003
- generated-medium
```
