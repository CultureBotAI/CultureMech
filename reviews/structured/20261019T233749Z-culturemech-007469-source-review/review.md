# Source and formulation review: 1287 (CultureMech:007469)

- Review: 20261019T233749Z-culturemech-007469-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-19T23:30:23Z
- Finished UTC: 2026-10-19T23:37:49Z
- Reviewer: OpenAI Codex with delegated source and validator checks (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

NBRC Medium 1286 is identifiable, but the generated record preserves a concatenated composition blob and a blank nonnumeric ingredient instead of the corrected maintained formulation. Source amounts, pH and vapor-phase biphenyl handling are recoverable from the official page. The review is complete with curation required.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Record 15 in Python lexicographic repository-relative path order of the initially uncovered merged corpus; batch 002 covers ordinals 11–20 after batch 001. On fresh origin/main at this batch base, scripts/record_review.py list validated 34 existing bundles and none listed this target path or ID. This bundle selects only the named record; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7c568537897ee4bba1b8e97f8172133c1572aec0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007469 | data/merge_yaml/merged/1287.yaml | generated | 1287 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007469 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:007469 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-002/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch002/015/strict.tsv |
| validate-terms | passed | True | CultureMech:007469 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:007469 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:007469 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:007469.

The four documented recipes completed; interpret the scope of each separately.

### Limits of passing deterministic checks

evidence: concern. Targets: CultureMech:007469.

All four documented target commands exited 0. Strict validation used only layers=schema; reference validation explicitly checked 0 references. These results do not validate recipe identity, source support, concentrations or embedded history claims.

### Organism, growth and cultivation-condition scope

scope: not_applicable. Targets: CultureMech:007469.

The target contains no organism, strain, growth experiment, temperature, incubation duration, oxygen requirement, DOI or PMID assertion. Recipe availability and generic cultivation wording establish no strain-specific growth result. No organism enrichment was inferred from ingredients.

### Field-level source support

evidence: concern. Targets: CultureMech:007469.

The generated record has no claim-level quantity evidence. Source URLs or historical import notes are useful provenance but do not bind an excerpt, denominator and chemical form to each amount. Follow-up should attach source evidence at each corrected ingredient or stock and preparation claim.

### Target, maintained owner and source number

identity: supported. Targets: CultureMech:007469.

CultureMech:007469 agrees between target and NBRC_1287.yaml. The target description and import URL identify NBRC 1286; 1287 is the local legacy slug, not the source medium accession. The official title and nbrc.medium:1286 are present in the corrected owner.

### Complexity and physical state

consistency: supported. Targets: CultureMech:007469.

COMPLEX and UNDEFINED suit the tryptone/yeast mixture; SOLID_AGAR agrees with the source agar recipe. The title alone is not evidence for a measured biphenyl concentration or organism-specific growth.

### ingredients[0]

quantity: concern. Targets: CultureMech:007469.

The row combines five measured components, pH and a vapor-exposure instruction into one ingredient with value=variable. It does not represent any single chemical amount and cannot be normalized as an actual ingredient.

### ingredients[1]

quantity: concern. Targets: CultureMech:007469.

The name is empty and concentration.value is the ingredient name Bacto tryptone despite unit G_PER_L. This is a parsing remnant, not a quantitative observation.

### owner NBRC_1287.yaml ingredients[0].concentration

quantity: concern. Targets: CultureMech:007469.

The source supports a batch addition of 3.3 g Bacto tryptone with 1 L distilled water. The owner encodes 3.3 G_PER_L, which is not independently verified because source water volume is not an explicit final-medium volume. Preserve the literal batch mass and resolve the denominator or use a source-faithful batch-amount representation before regeneration; do not certify the existing rate.

### owner NBRC_1287.yaml ingredients[1].concentration

quantity: concern. Targets: CultureMech:007469.

The source supports a batch addition of 1.6 g yeast extract with 1 L distilled water. The owner encodes 1.6 G_PER_L, which is not independently verified because source water volume is not an explicit final-medium volume. Preserve the literal batch mass and resolve the denominator or use a source-faithful batch-amount representation before regeneration; do not certify the existing rate.

### owner NBRC_1287.yaml ingredients[2].concentration

quantity: concern. Targets: CultureMech:007469.

The source supports a batch addition of 3.3 g NaCl with 1 L distilled water. The owner encodes 3.3 G_PER_L, which is not independently verified because source water volume is not an explicit final-medium volume. Preserve the literal batch mass and resolve the denominator or use a source-faithful batch-amount representation before regeneration; do not certify the existing rate.

### owner NBRC_1287.yaml ingredients[3].concentration

quantity: supported. Targets: CultureMech:007469.

The official recipe lists 1 L Distilled water. The owner preserves this amount; non-water g/L values use the nominal 1 L water recipe basis. The generated target does not expose the amount as an independent numeric ingredient.

### owner NBRC_1287.yaml ingredients[4].concentration

quantity: concern. Targets: CultureMech:007469.

The source supports a batch addition of 15 g agar with 1 L distilled water. The owner encodes 15 G_PER_L, which is not independently verified because source water volume is not an explicit final-medium volume. Preserve the literal batch mass and resolve the denominator or use a source-faithful batch-amount representation before regeneration; do not certify the existing rate.

### owner NBRC_1287.yaml ingredients[5].concentration

quantity: supported. Targets: CultureMech:007469.

The source specifies lid placement and vapor-phase delivery but no crystal mass, exposure concentration, duration or temperature. Owner VARIABLE is an honest missing-amount representation for biphenyl only; it cannot justify VARIABLE for the entire medium.

### All asserted and proposed-owner identifiers

grounding: supported. Targets: CultureMech:007469.

The target asserts no ingredient CURIE or media term, so its term-validator pass has no ingredient grounding content. Owner MICRO:0000182, FOODON:03315426 and the four CHEBI IDs were independently resolved; all four MIM links are in the pinned index. No DOI, PMID, taxon or internal stock identifier is asserted.

### pH, vapor addition and sterilization

completeness: concern. Targets: CultureMech:007469.

Source pH 7.0 and vapor-phase lid placement are only buried in the malformed generated ingredient. Generic dissolution is not an instruction to dissolve biphenyl; the target adds unsupported autoclaving and encodes that step as DISSOLVE. The owner provides explicit pH and delivery handling without inventing a biphenyl dose. The owner vapor-placement action MIX also needs review: supported delivery text does not validate an action token suggesting that the crystal is mixed into the medium.

### Embedded history and stale generation

provenance: concern. Targets: CultureMech:007469.

The target ends with the 6 August 2026 merge. The maintained owner records later composition recovery, grounding and the 11 September source correction. Earlier history stating duplicate merging and default VARIABLE does not establish scientific support. Present generated bytes demonstrably omit the owner corrections; no claim is made about what an unexecuted regeneration would emit.

## Findings

### f1: Measured formulation is trapped in a blob and blank ingredient

blocker / open / confirmed; issue key: nbrc1286-malformed-formulation.

The two generated descriptors are not usable ingredient observations: the first concatenates recipe text and the second assigns a name as a g/L value. Five measured components and unquantified biphenyl are already separately represented in the maintained owner. The whole quantitative formulation is collapsed into invalid scientific rows, so no usable source recipe is represented. Owner g/L values also require correction or explicit final-volume support before regeneration.

### f2: pH and biphenyl delivery are missing from usable preparation

major / open / confirmed; issue key: nbrc1286-preparation-scope.

The target does not express pH 7.0 as ph_value or preserve vapor-phase lid exposure as an actionable preparation step. Its generic autoclaving is not stated by this source and its action enum says dissolution. The maintained owner action MIX for vapor-phase lid placement is likewise not automatically validated by the correct descriptive text.

### f3: Generated identity and source attribution lag the maintained owner

minor / open / confirmed; issue key: nbrc1286-stale-identity-provenance.

The numeric name/original_name and historical import note omit the official title, media term, current reference and documented source correction present in the owner. The description still resolves NBRC 1286, so this is a provenance defect rather than a different-medium identity.

## Recommended Actions And Acceptance Checks

### a1

Verify the NBRC_1287 owner against NBRC 1286, retain literal source batch masses, resolve the unverified G_PER_L denominator or use a faithful batch-amount representation, and retain the unquantified vapor component. Then regenerate through the normal merge pipeline; do not hand-patch this generated file.

- Generated output has six distinct source-backed components and no blank names or nonnumeric values paired with numeric units.
- Preserve 1 L water as the source solvent amount; do not infer final-medium volume or certify g/L solely from it. Biphenyl dose remains unspecified.
- Run the four documented recipe checks and appropriate full regeneration/product gates after an authorized change.

### a2

Carry the owner pH and vapor-placement instructions into regenerated output. Either support additional sterilization details from an exact source or leave them explicitly unspecified. Review the maintained vapor-delivery action token so it does not imply mixing biphenyl into the liquid.

- Generated preparation separates dissolved ingredients from vapor-delivered biphenyl.
- pH is 7.0 and no unsupported sterilization time, temperature or chemical exposure dose is added.

### a3

Regenerate after owner verification so the official title, nbrc.medium:1286 and source reference accompany the corrected formulation; preserve history as history.

- Canonical output retains CultureMech:007469 while representing the exact NBRC medium number and source title.
- Claim-level source evidence is attached to corrected quantities and preparation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/1287.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/NBRC_1287.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/1287.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/1287.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch002/015/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-002/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch002/015/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/1287.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/1287.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| bounded-search | data/merge_yaml/merged/1287.yaml; Whole target and named normalized owners; explicit-file rg --no-ignore --hidden search plus full YAML reads | context_only | Checked ingredient names, identifiers, stock and source fields, pH, growth conditions, evidence, references and history in every selected file. Ignored files were included through explicit file arguments. Absence statements in this review concern those records only; this was not a corpus-wide claim that no supporting material exists. |
| merge-owner | src/culturemech/merge/formulation.py; formulation_content, FormulationFingerprinter and merge_formulation_evidence; matcher.group_formulations and merger.merge_group | context_only | Current generator requires equality of scientific formulation fields and preserves scoped evidence; ingredient-set similarity alone is not proof of interchangeable formulations. A future correction belongs in normalized owners followed by reviewed regeneration. Current code was inspected without executing regeneration. |
| nbrc | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1286; Medium No., Medium and complete Composition fields | supports | Official medium number 1286 and title identify a diluted LB agar containing biphenyl supplied through the vapor phase; the component table and pH provide the comparison basis. |
| tryptone | https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000182; terms[0]: obo_id, label, definition, synonyms and is_obsolete | supports | MICRO:0000182 is active tryptone; its definition is a trypsin digest of casein and its listed synonyms include Bacto Tryptone. |
| yeast | https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315426; terms[0]: obo_id, label and is_obsolete | supports | FOODON:03315426 is active yeast extract. This verifies the maintained owner label, not a specific brand or lot. |
| biphenyl | https://www.ebi.ac.uk/chebi/CHEBI:17097; ChEBI Name and formula | supports | CHEBI:17097 is biphenyl, formula C12H10. The owner mapping identifies the substance but supplies no dose. |
| chebi-26710 | https://www.ebi.ac.uk/chebi/CHEBI:26710; ChEBI Name, definition, formula and ontology relationships | supports | CHEBI:26710 is sodium chloride, Cl.Na; it matches owner NaCl. |
| chebi-15377 | https://www.ebi.ac.uk/chebi/CHEBI:15377; ChEBI Name, definition, formula and ontology relationships | supports | CHEBI:15377 is water, H2O; it matches owner distilled water at the substance level. |
| chebi-2509 | https://www.ebi.ac.uk/chebi/CHEBI:2509; ChEBI Name, definition, formula and ontology relationships | supports | CHEBI:2509 is agar, a polysaccharide mixture; it matches the owner agar ingredient. |
| mim-index | src/culturemech/data/mediaingredientmech/label_index.csv; Exact rows for CHEBI:26710, CHEBI:15377, CHEBI:2509 and CHEBI:17097; pinned metadata captured in source.inputs | supports | All four maintained MIM CHEBI links occur as mapped unique entries. The index is a pinned linkage artifact, not independent proof of amount or vapor exposure. |

## Limits And Additional Notes

- NBRC specifies 1 L distilled water, not final solution volume. Literal component masses are verified, but owner G_PER_L normalizations remain unverified and must not be accepted solely from that water amount. Biphenyl quantity and source sterilization parameters are unspecified; none were invented.
- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Embedded curation_history was read and compared with present target and owner bytes. Historical assertions are not retroactively certified; no history edits, status promotion or experimental verification were performed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T233749Z-culturemech-007469-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 1287 (CultureMech:007469)'
started_at: '2026-10-19T23:30:23Z'
finished_at: '2026-10-19T23:37:49Z'
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
summary: NBRC Medium 1286 is identifiable, but the generated record preserves a concatenated
  composition blob and a blank nonnumeric ingredient instead of the corrected maintained
  formulation. Source amounts, pH and vapor-phase biphenyl handling are recoverable
  from the official page. The review is complete with curation required.
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
  - path: data/merge_yaml/merged/1287.yaml
    sha256: ced2ebea17b5cbff385a73883a73c7e00935490a7d9f2afcf4e6f0b898bf820d
    role: target
  - path: data/normalized_yaml/bacterial/NBRC_1287.yaml
    sha256: 3edaa8c741e810f8d9b8c9d92ffacc3d7b4eb40d210e9680013f118586432d2b
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
  - path: scripts/migrate_legacy_fields.py
    sha256: 13738616213c958af4a3d6d37bd22c798f530544b52829ca81780279abcd2a73
    role: context
  - path: scripts/recover_nbrc_composition.py
    sha256: a723e458895350a68ffae3e446006205b2e00cb185bee13976d5047be56405f0
    role: context
  - path: scripts/repair_nbrc_1287_score15.py
    sha256: 683f67c0f5bdc48ec0dbd8150e9c55089679bd13597fa23a7984eef37f46c710
    role: context
  - path: scripts/validate_recipe_references.py
    sha256: 087e5f3128e774bc760b7dcfc8f194fe14820354f809be9e35cf6cacb8546a3b
    role: context
  - path: scripts/validate_strict.py
    sha256: d6775c8c53ee433426ad7d3ababdf1740fc6adc62cb8269cf07ca0cd251cef68
    role: context
  - path: src/culturemech/convert/nbrc_raw_yaml.py
    sha256: de5654d4eed2e01a2383dcf417b7d8e2779dbb622de9351c28373fb691812ec1
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
    role: context
  - path: src/culturemech/fetch/nbrc_scraper.py
    sha256: 5c5bbda489abe0b6d000b9318a76913ab5496ee83aff58b530c2b42b5989d1e3
    role: context
  - path: src/culturemech/import/nbrc_importer.py
    sha256: 857b7e0ac88aef783ce4bc9b35c4c6a3d9fc38824a5d463010a6046ac4180924
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
  selection: Record 15 in Python lexicographic repository-relative path order of the
    initially uncovered merged corpus; batch 002 covers ordinals 11–20 after batch
    001. On fresh origin/main at this batch base, scripts/record_review.py list validated
    34 existing bundles and none listed this target path or ID. This bundle selects
    only the named record; no sampling or fleet-wide scientific claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:007469
targets:
- target_id: CultureMech:007469
  path: data/merge_yaml/merged/1287.yaml
  label: '1287'
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_1287.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/1287.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:007469
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/1287.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch002/015/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-002/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch002/015/strict.tsv"
  target_ids:
  - CultureMech:007469
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/1287.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:007469
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/1287.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:007469
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
  - CultureMech:007469
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/1287.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-19T23:36:44Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/NBRC_1287.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-19T23:36:44Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/1287.yaml
  locator: Actual command output
  accessed_at: '2026-10-19T23:31:29.836168Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/1287.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch002/015/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-19T23:31:31.689176Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-002/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch002/015/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/1287.yaml
  locator: Actual command output
  accessed_at: '2026-10-19T23:31:34.567596Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/1287.yaml
  locator: Actual command output
  accessed_at: '2026-10-19T23:31:36.666013Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: bounded-search
  kind: search
  reference: data/merge_yaml/merged/1287.yaml
  locator: Whole target and named normalized owners; explicit-file rg --no-ignore
    --hidden search plus full YAML reads
  accessed_at: '2026-10-19T23:36:44Z'
  support: context_only
  summary: Checked ingredient names, identifiers, stock and source fields, pH, growth
    conditions, evidence, references and history in every selected file. Ignored files
    were included through explicit file arguments. Absence statements in this review
    concern those records only; this was not a corpus-wide claim that no supporting
    material exists.
  search_scope: Generated target and its source.inputs authoritative normalized owner
    paths; no remote or corpus-wide absence inference.
- evidence_id: merge-owner
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: formulation_content, FormulationFingerprinter and merge_formulation_evidence;
    matcher.group_formulations and merger.merge_group
  accessed_at: '2026-10-19T23:36:44Z'
  support: context_only
  summary: Current generator requires equality of scientific formulation fields and
    preserves scoped evidence; ingredient-set similarity alone is not proof of interchangeable
    formulations. A future correction belongs in normalized owners followed by reviewed
    regeneration. Current code was inspected without executing regeneration.
- evidence_id: nbrc
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1286
  locator: Medium No., Medium and complete Composition fields
  accessed_at: '2026-10-19T23:29:37Z'
  support: supports
  summary: Official medium number 1286 and title identify a diluted LB agar containing
    biphenyl supplied through the vapor phase; the component table and pH provide
    the comparison basis.
  snapshot_sha256: 9896d9499c009fff27e883be8117a84b4ac836c95b232d9a6834ec25e3a21da3
- evidence_id: tryptone
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000182
  locator: 'terms[0]: obo_id, label, definition, synonyms and is_obsolete'
  accessed_at: '2026-10-19T23:33:02Z'
  support: supports
  summary: MICRO:0000182 is active tryptone; its definition is a trypsin digest of
    casein and its listed synonyms include Bacto Tryptone.
  snapshot_sha256: 01875997c482a49e4d41eb35c6c697e190afd236a8527625e94b6f96df3872b0
- evidence_id: yeast
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/foodon/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FFOODON_03315426
  locator: 'terms[0]: obo_id, label and is_obsolete'
  accessed_at: '2026-10-19T23:33:02Z'
  support: supports
  summary: FOODON:03315426 is active yeast extract. This verifies the maintained owner
    label, not a specific brand or lot.
  snapshot_sha256: cf2b158469d7dedbe7c31242b5901230a29b5765e04bb37c92f0b1ddd6ea9c44
- evidence_id: biphenyl
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:17097
  locator: ChEBI Name and formula
  accessed_at: '2026-10-19T23:33:02Z'
  support: supports
  summary: CHEBI:17097 is biphenyl, formula C12H10. The owner mapping identifies the
    substance but supplies no dose.
  snapshot_sha256: f93fa7765ee5320f818d6b9643321e08eb09dcbc24212ae32d938397b51feb5c
- evidence_id: chebi-26710
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:26710
  locator: ChEBI Name, definition, formula and ontology relationships
  accessed_at: '2026-10-19T23:32:12.913708Z'
  support: supports
  summary: CHEBI:26710 is sodium chloride, Cl.Na; it matches owner NaCl.
  snapshot_sha256: 20d037f64aa7b26b83d04556c47a29bc5d4808bbdf7d25027e18ad22a5c5f02f
- evidence_id: chebi-15377
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:15377
  locator: ChEBI Name, definition, formula and ontology relationships
  accessed_at: '2026-10-19T23:32:48.413412Z'
  support: supports
  summary: CHEBI:15377 is water, H2O; it matches owner distilled water at the substance
    level.
  snapshot_sha256: 1a98a50fba3aa8ec10dc2fd5c355cd22bc1a955252adbd43f4042fd2f1a3ee5d
- evidence_id: chebi-2509
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:2509
  locator: ChEBI Name, definition, formula and ontology relationships
  accessed_at: '2026-10-19T23:32:11.347108Z'
  support: supports
  summary: CHEBI:2509 is agar, a polysaccharide mixture; it matches the owner agar
    ingredient.
  snapshot_sha256: fdf12a8280861ef7a97ff6940adfaeba3e1bbe69671dbc1e4ee58869fc4f6bd3
- evidence_id: mim-index
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Exact rows for CHEBI:26710, CHEBI:15377, CHEBI:2509 and CHEBI:17097; pinned
    metadata captured in source.inputs
  accessed_at: '2026-10-19T23:36:44Z'
  support: supports
  summary: All four maintained MIM CHEBI links occur as mapped unique entries. The
    index is a pinned linkage artifact, not independent proof of amount or vapor exposure.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:007469
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: check-scope
  area: evidence
  topic: Limits of passing deterministic checks
  outcome: concern
  summary: All four documented target commands exited 0. Strict validation used only
    layers=schema; reference validation explicitly checked 0 references. These results
    do not validate recipe identity, source support, concentrations or embedded history
    claims.
  target_ids:
  - CultureMech:007469
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: growth
  area: scope
  topic: Organism, growth and cultivation-condition scope
  outcome: not_applicable
  summary: The target contains no organism, strain, growth experiment, temperature,
    incubation duration, oxygen requirement, DOI or PMID assertion. Recipe availability
    and generic cultivation wording establish no strain-specific growth result. No
    organism enrichment was inferred from ingredients.
  target_ids:
  - CultureMech:007469
  evidence_ids:
  - record
  - bounded-search
- assessment_id: evidence-placement
  area: evidence
  topic: Field-level source support
  outcome: concern
  summary: The generated record has no claim-level quantity evidence. Source URLs
    or historical import notes are useful provenance but do not bind an excerpt, denominator
    and chemical form to each amount. Follow-up should attach source evidence at each
    corrected ingredient or stock and preparation claim.
  target_ids:
  - CultureMech:007469
  evidence_ids:
  - record
  - bounded-search
  - validate-references
- assessment_id: identity
  area: identity
  topic: Target, maintained owner and source number
  outcome: supported
  summary: CultureMech:007469 agrees between target and NBRC_1287.yaml. The target
    description and import URL identify NBRC 1286; 1287 is the local legacy slug,
    not the source medium accession. The official title and nbrc.medium:1286 are present
    in the corrected owner.
  target_ids:
  - CultureMech:007469
  evidence_ids:
  - record
  - owner-0
  - nbrc
- assessment_id: classification
  area: consistency
  topic: Complexity and physical state
  outcome: supported
  summary: COMPLEX and UNDEFINED suit the tryptone/yeast mixture; SOLID_AGAR agrees
    with the source agar recipe. The title alone is not evidence for a measured biphenyl
    concentration or organism-specific growth.
  target_ids:
  - CultureMech:007469
  evidence_ids:
  - record
  - owner-0
  - nbrc
- assessment_id: q-blob
  area: quantity
  topic: ingredients[0]
  outcome: concern
  summary: The row combines five measured components, pH and a vapor-exposure instruction
    into one ingredient with value=variable. It does not represent any single chemical
    amount and cannot be normalized as an actual ingredient.
  target_ids:
  - CultureMech:007469
  evidence_ids:
  - record
  - nbrc
  dimensions:
  - name: decision
    value: replace malformed composite row through verified owner regeneration
    definition: Claim-level quantity decision for the stated field; source amount,
      preparation basis and any derivation are distinguished.
    evidence_ids:
    - record
    - nbrc
- assessment_id: q-empty
  area: quantity
  topic: ingredients[1]
  outcome: concern
  summary: The name is empty and concentration.value is the ingredient name Bacto
    tryptone despite unit G_PER_L. This is a parsing remnant, not a quantitative observation.
  target_ids:
  - CultureMech:007469
  evidence_ids:
  - record
  - nbrc
  dimensions:
  - name: decision
    value: remove corrupt row when regenerating corrected owner
    definition: Claim-level quantity decision for the stated field; source amount,
      preparation basis and any derivation are distinguished.
    evidence_ids:
    - record
    - nbrc
- assessment_id: q-owner-0
  area: quantity
  topic: owner NBRC_1287.yaml ingredients[0].concentration
  outcome: concern
  summary: The source supports a batch addition of 3.3 g Bacto tryptone with 1 L distilled
    water. The owner encodes 3.3 G_PER_L, which is not independently verified because
    source water volume is not an explicit final-medium volume. Preserve the literal
    batch mass and resolve the denominator or use a source-faithful batch-amount representation
    before regeneration; do not certify the existing rate.
  target_ids:
  - CultureMech:007469
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - tryptone
  dimensions:
  - name: decision
    value: literal batch mass supported; encoded final-volume rate unverified
    definition: Claim-level quantity decision for the stated field; source amount,
      preparation basis and any derivation are distinguished.
    evidence_ids:
    - record
    - owner-0
    - nbrc
    - tryptone
- assessment_id: q-owner-1
  area: quantity
  topic: owner NBRC_1287.yaml ingredients[1].concentration
  outcome: concern
  summary: The source supports a batch addition of 1.6 g yeast extract with 1 L distilled
    water. The owner encodes 1.6 G_PER_L, which is not independently verified because
    source water volume is not an explicit final-medium volume. Preserve the literal
    batch mass and resolve the denominator or use a source-faithful batch-amount representation
    before regeneration; do not certify the existing rate.
  target_ids:
  - CultureMech:007469
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - yeast
  dimensions:
  - name: decision
    value: literal batch mass supported; encoded final-volume rate unverified
    definition: Claim-level quantity decision for the stated field; source amount,
      preparation basis and any derivation are distinguished.
    evidence_ids:
    - record
    - owner-0
    - nbrc
    - yeast
- assessment_id: q-owner-2
  area: quantity
  topic: owner NBRC_1287.yaml ingredients[2].concentration
  outcome: concern
  summary: The source supports a batch addition of 3.3 g NaCl with 1 L distilled water.
    The owner encodes 3.3 G_PER_L, which is not independently verified because source
    water volume is not an explicit final-medium volume. Preserve the literal batch
    mass and resolve the denominator or use a source-faithful batch-amount representation
    before regeneration; do not certify the existing rate.
  target_ids:
  - CultureMech:007469
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - chebi-26710
  dimensions:
  - name: decision
    value: literal batch mass supported; encoded final-volume rate unverified
    definition: Claim-level quantity decision for the stated field; source amount,
      preparation basis and any derivation are distinguished.
    evidence_ids:
    - record
    - owner-0
    - nbrc
    - chebi-26710
- assessment_id: q-owner-3
  area: quantity
  topic: owner NBRC_1287.yaml ingredients[3].concentration
  outcome: supported
  summary: The official recipe lists 1 L Distilled water. The owner preserves this
    amount; non-water g/L values use the nominal 1 L water recipe basis. The generated
    target does not expose the amount as an independent numeric ingredient.
  target_ids:
  - CultureMech:007469
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - chebi-15377
  dimensions:
  - name: decision
    value: retain source amount and explicit nominal batch basis
    definition: Claim-level quantity decision for the stated field; source amount,
      preparation basis and any derivation are distinguished.
    evidence_ids:
    - record
    - owner-0
    - nbrc
    - chebi-15377
- assessment_id: q-owner-4
  area: quantity
  topic: owner NBRC_1287.yaml ingredients[4].concentration
  outcome: concern
  summary: The source supports a batch addition of 15 g agar with 1 L distilled water.
    The owner encodes 15 G_PER_L, which is not independently verified because source
    water volume is not an explicit final-medium volume. Preserve the literal batch
    mass and resolve the denominator or use a source-faithful batch-amount representation
    before regeneration; do not certify the existing rate.
  target_ids:
  - CultureMech:007469
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - chebi-2509
  dimensions:
  - name: decision
    value: literal batch mass supported; encoded final-volume rate unverified
    definition: Claim-level quantity decision for the stated field; source amount,
      preparation basis and any derivation are distinguished.
    evidence_ids:
    - record
    - owner-0
    - nbrc
    - chebi-2509
- assessment_id: q-biphenyl
  area: quantity
  topic: owner NBRC_1287.yaml ingredients[5].concentration
  outcome: supported
  summary: The source specifies lid placement and vapor-phase delivery but no crystal
    mass, exposure concentration, duration or temperature. Owner VARIABLE is an honest
    missing-amount representation for biphenyl only; it cannot justify VARIABLE for
    the entire medium.
  target_ids:
  - CultureMech:007469
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - biphenyl
  dimensions:
  - name: decision
    value: retain unspecified amount and vapor-delivery scope; do not infer a mass
    definition: Claim-level quantity decision for the stated field; source amount,
      preparation basis and any derivation are distinguished.
    evidence_ids:
    - record
    - owner-0
    - nbrc
    - biphenyl
- assessment_id: grounding
  area: grounding
  topic: All asserted and proposed-owner identifiers
  outcome: supported
  summary: The target asserts no ingredient CURIE or media term, so its term-validator
    pass has no ingredient grounding content. Owner MICRO:0000182, FOODON:03315426
    and the four CHEBI IDs were independently resolved; all four MIM links are in
    the pinned index. No DOI, PMID, taxon or internal stock identifier is asserted.
  target_ids:
  - CultureMech:007469
  evidence_ids:
  - record
  - owner-0
  - tryptone
  - yeast
  - biphenyl
  - chebi-26710
  - chebi-15377
  - chebi-2509
  - mim-index
  - nbrc
- assessment_id: preparation
  area: completeness
  topic: pH, vapor addition and sterilization
  outcome: concern
  summary: 'Source pH 7.0 and vapor-phase lid placement are only buried in the malformed
    generated ingredient. Generic dissolution is not an instruction to dissolve biphenyl;
    the target adds unsupported autoclaving and encodes that step as DISSOLVE. The
    owner provides explicit pH and delivery handling without inventing a biphenyl
    dose. The owner vapor-placement action MIX also needs review: supported delivery
    text does not validate an action token suggesting that the crystal is mixed into
    the medium.'
  target_ids:
  - CultureMech:007469
  evidence_ids:
  - record
  - owner-0
  - nbrc
- assessment_id: history
  area: provenance
  topic: Embedded history and stale generation
  outcome: concern
  summary: The target ends with the 6 August 2026 merge. The maintained owner records
    later composition recovery, grounding and the 11 September source correction.
    Earlier history stating duplicate merging and default VARIABLE does not establish
    scientific support. Present generated bytes demonstrably omit the owner corrections;
    no claim is made about what an unexecuted regeneration would emit.
  target_ids:
  - CultureMech:007469
  evidence_ids:
  - record
  - owner-0
  - merge-owner
findings:
- finding_id: f1
  issue_key: nbrc1286-malformed-formulation
  category: representation
  severity: blocker
  status: open
  certainty: confirmed
  title: Measured formulation is trapped in a blob and blank ingredient
  description: 'The two generated descriptors are not usable ingredient observations:
    the first concatenates recipe text and the second assigns a name as a g/L value.
    Five measured components and unquantified biphenyl are already separately represented
    in the maintained owner. The whole quantitative formulation is collapsed into
    invalid scientific rows, so no usable source recipe is represented. Owner g/L
    values also require correction or explicit final-volume support before regeneration.'
  target_ids:
  - CultureMech:007469
  field_paths:
  - ingredients[0]
  - ingredients[1]
  evidence_ids:
  - record
  - owner-0
  - nbrc
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_1287.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f2
  issue_key: nbrc1286-preparation-scope
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: pH and biphenyl delivery are missing from usable preparation
  description: The target does not express pH 7.0 as ph_value or preserve vapor-phase
    lid exposure as an actionable preparation step. Its generic autoclaving is not
    stated by this source and its action enum says dissolution. The maintained owner
    action MIX for vapor-phase lid placement is likewise not automatically validated
    by the correct descriptive text.
  target_ids:
  - CultureMech:007469
  field_paths:
  - ph_value
  - preparation_steps[0]
  - preparation_steps[1]
  - preparation_steps[2]
  - owner NBRC_1287.yaml preparation_steps[2].action
  evidence_ids:
  - record
  - owner-0
  - nbrc
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_1287.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f3
  issue_key: nbrc1286-stale-identity-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Generated identity and source attribution lag the maintained owner
  description: The numeric name/original_name and historical import note omit the
    official title, media term, current reference and documented source correction
    present in the owner. The description still resolves NBRC 1286, so this is a provenance
    defect rather than a different-medium identity.
  target_ids:
  - CultureMech:007469
  field_paths:
  - name
  - original_name
  - media_term
  - references
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - nbrc
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_1287.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Verify the NBRC_1287 owner against NBRC 1286, retain literal source
    batch masses, resolve the unverified G_PER_L denominator or use a faithful batch-amount
    representation, and retain the unquantified vapor component. Then regenerate through
    the normal merge pipeline; do not hand-patch this generated file.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007469
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_1287.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Generated output has six distinct source-backed components and no blank names
    or nonnumeric values paired with numeric units.
  - Preserve 1 L water as the source solvent amount; do not infer final-medium volume
    or certify g/L solely from it. Biphenyl dose remains unspecified.
  - Run the four documented recipe checks and appropriate full regeneration/product
    gates after an authorized change.
- action_id: a2
  description: Carry the owner pH and vapor-placement instructions into regenerated
    output. Either support additional sterilization details from an exact source or
    leave them explicitly unspecified. Review the maintained vapor-delivery action
    token so it does not imply mixing biphenyl into the liquid.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007469
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_1287.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Generated preparation separates dissolved ingredients from vapor-delivered biphenyl.
  - pH is 7.0 and no unsupported sterilization time, temperature or chemical exposure
    dose is added.
- action_id: a3
  description: Regenerate after owner verification so the official title, nbrc.medium:1286
    and source reference accompany the corrected formulation; preserve history as
    history.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:007469
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_1287.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Canonical output retains CultureMech:007469 while representing the exact NBRC
    medium number and source title.
  - Claim-level source evidence is attached to corrected quantities and preparation.
limitations:
- NBRC specifies 1 L distilled water, not final solution volume. Literal component
  masses are verified, but owner G_PER_L normalizations remain unverified and must
  not be accepted solely from that water amount. Biphenyl quantity and source sterilization
  parameters are unspecified; none were invented.
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
- Embedded curation_history was read and compared with present target and owner bytes.
  Historical assertions are not retroactively certified; no history edits, status
  promotion or experimental verification were performed.
tags:
- unreviewed-records
- batch-002
- generated-medium
```
