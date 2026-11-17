# Source and formulation review: 1210 (CultureMech:007464)

- Review: 20261019T233419Z-culturemech-007464-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-19T23:30:22Z
- Finished UTC: 2026-10-19T23:34:19Z
- Reviewer: OpenAI Codex with delegated source and validator checks (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The generated NBRC 1209 5×R2A Medium record collapses ten components into an ingredient-name blob and stores a product name as a concentration. Its pH 7.2 ± 0.2 survives only in that blob; structured pH and source identity are missing. The maintained owner restores ingredient rows and pH range, but remains numerically named, and generic generated autoclaving is unsupported by the inspected source.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Record 14 in Python lexicographic repository-relative path order of the initially uncovered merged corpus; batch 002 covers ordinals 11–20 after batch 001. On this batch base, scripts/record_review.py list validated 34 existing bundles and none listed this target path or ID. Exactly one named record is assessed; no sampling or fleet-wide scientific conclusion.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7c568537897ee4bba1b8e97f8172133c1572aec0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:007464 | data/merge_yaml/merged/1210.yaml | generated | 1210 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:007464 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:007464 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-002/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch002/014/strict.tsv |
| validate-terms | passed | True | CultureMech:007464 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:007464 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:007464 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:007464.

The four documented recipes completed; interpret the scope of each separately.

### Stable target, maintained owner and official source accession

identity: supported. Targets: CultureMech:007464.

The target ID resolves to the captured normalized owner via merged_from and the MERGED_RECIPES event. Description/import provenance names NBRC 1209, which the live official catalogue identifies as 5×R2A Medium. The numeric local filename/name is not the verified NBRC source accession.

This is one generated MediaRecipe. The inspected generated and maintained records carry the same stable CultureMech ID. No corpus-wide uniqueness test or independent historical import replay is claimed. The current merge engine is the future regeneration entrypoint; a fingerprint alone is not source-identity evidence.

### Every encoded concentration and every source composition row

quantity: concern. Targets: CultureMech:007464.

All 10 source rows were checked against the complete generated blob and structured maintained owner. The source numbers survive textually, but the target has no usable per-ingredient amounts. Source mass-to-final-volume conversion remains a separate unresolved issue.

The generated target has only two concentration objects. ingredients[0] is variable/VARIABLE attached to the entire composition text; ingredients[1] has an empty preferred_term and 'Bacto Yeast Extract (Difco)'/G_PER_L. Neither is an ingredient-specific quantitative recipe. The source amount/unit pairs below are factual transcriptions; formula typography is normalized from source subscripts, without changing chemical identities.

&#124; Owner row / component recovered from target blob &#124; Exact source amount &#124; Maintained encoding &#124; Review decision &#124;
&#124;---&#124;---&#124;---&#124;---&#124;
&#124; owner ingredients[0]: Bacto Yeast Extract (Difco) &#124; 2.5 g &#124; 2.5 G_PER_L &#124; source batch mass verified; final-volume concentration remains unsupported by this page alone &#124;
&#124; owner ingredients[1]: Bacto Proteose Peptone No. 3 (Difco) &#124; 2.5 g &#124; 2.5 G_PER_L &#124; source batch mass verified; final-volume concentration remains unsupported by this page alone &#124;
&#124; owner ingredients[2]: Bacto Casamino Acids (Difco) &#124; 2.5 g &#124; 2.5 G_PER_L &#124; source batch mass verified; final-volume concentration remains unsupported by this page alone &#124;
&#124; owner ingredients[3]: Glucose &#124; 2.5 g &#124; 2.5 G_PER_L &#124; source batch mass verified; final-volume concentration remains unsupported by this page alone &#124;
&#124; owner ingredients[4]: Soluble starch &#124; 2.5 g &#124; 2.5 G_PER_L &#124; source batch mass verified; final-volume concentration remains unsupported by this page alone &#124;
&#124; owner ingredients[5]: Sodium pyruvate &#124; 1.5 g &#124; 1.5 G_PER_L &#124; source batch mass verified; final-volume concentration remains unsupported by this page alone &#124;
&#124; owner ingredients[6]: K2HPO4 &#124; 1.5 g &#124; 1.5 G_PER_L &#124; source batch mass verified; final-volume concentration remains unsupported by this page alone &#124;
&#124; owner ingredients[7]: MgSO4·7H2O &#124; 0.25 g &#124; 0.25 G_PER_L &#124; source batch mass verified; final-volume concentration remains unsupported by this page alone &#124;
&#124; owner ingredients[8]: Agar (if needed) &#124; 15 g &#124; 15 G_PER_L &#124; source batch mass verified; final-volume concentration remains unsupported by this page alone &#124;
&#124; owner ingredients[9]: Distilled water &#124; 1 L &#124; 1 L &#124; verified source volume addition; not a measured final-volume marker &#124;

The source is the main formulation, not a stock. No stock strength or dilution is inferred. The existing concentration enum lacks standalone g, mg and μL batch-dose units: retain literal batch amounts and water context in supported evidence/notes or preparation wording until a defensible concentration representation is available; do not conceal known amounts under VARIABLE or invent schema slots.

### Identifier assertions and commercial ingredient boundaries

grounding: unknown. Targets: CultureMech:007464.

No chemical CURIE or MIM linkage is asserted by either generated ingredient object. This is an absent structured mapping surface, not proof of invalid ontology IDs. Owner-only terms require exact-form and canonical-label verification before regeneration.

No whole-owner grounding approval is given. Keep named commercial preparations at their source product boundary; no catalogue number, supplier formulation, chemical replacement, organism growth or functional mechanism is inferred. The official NBRC accession and local target/owner identity were checked separately.

### Evidence placement, generated freshness and history scope

provenance: concern. Targets: CultureMech:007464.

The generated target retains an August merge event and earlier import/default history. The maintained owner records later composition recovery and source metadata absent from the generated content. This establishes a current owner/output discrepancy without proving that every later owner change is scientifically correct.

The entire embedded curation_history was read. It is provenance, not experimental evidence. Standalone HistoryRecord validation is not applicable to this MediaRecipe; embedded history is covered by the schema check and manual review. No historical entry was changed or independently reconstructed across all Git revisions. The reference recipe checked zero excerpts for the generated target. Future curation should attach exact claim-level source evidence and bibliographic context, and regeneration must retain it.

### pH range, optional agar and formulation classification

completeness: concern. Targets: CultureMech:007464.

NBRC specifies pH 7.2 +/- 0.2; the generated blob retains those characters but ph_range is absent and its generic adjustment step carries no target. The owner range 7.0–7.4 is an exact arithmetic restatement. COMPLEX/UNDEFINED is supported by yeast extract, proteose peptone and casamino acids; agar is optional and SOLID_AGAR selects the solid variant.

7.2 - 0.2 = 7.0 and 7.2 + 0.2 = 7.4. Do not replace the tolerance with only midpoint 7.2, invent a pH-adjusting reagent or infer an autoclave cycle. Despite the 5×R2A title, use the listed formulation directly: the source says optional agar 15 g, not five times 15 g.

### Source support for generated preparation

evidence: concern. Targets: CultureMech:007464.

The inspected catalogue supplies a pH condition but no sterilization method or cycle. The generic dissolution line is a curator/importer paraphrase of the composition, not a verified order of operations. Autoclaving is described under action DISSOLVE, an internal action/text mismatch.

The maintained owner has an empty preparation_steps list; regenerating its current state can remove unsupported generated steps, but is not evidence of a new validated protocol. No incubation temperature, atmosphere, storage instruction or organism growth claim is inferred. Source silence is bounded to the inspected page; this is not a claim that no protocol exists elsewhere.

## Findings

### f1: Generated composition is a text blob plus an unusable placeholder

blocker / open / confirmed; issue key: culturemech-007464-collapsed-nbrc-composition.

ingredients[0].preferred_term concatenates the 10-row NBRC composition and source numbers into one ingredient with VARIABLE concentration. ingredients[1] has an empty name and a product/substrate string in concentration.value with unit G_PER_L. The maintained owner has separate rows, but the generated record cannot be interpreted as the intended quantitative formulation. Its numerical name also omits the verified source title.

### f2: Source pH tolerance remains stranded in an ingredient name

major / open / confirmed; issue key: culturemech-007464-structured-ph-omission.

The text pH 7.2+/-0.2 is present inside ingredients[0].preferred_term, but the target has no ph_range and preparation_steps[1] only says Adjust pH if needed. The maintained owner already has source-consistent min 7.0 and max 7.4. The source condition is not wholly lost, but it is not represented as an actionable pH requirement.

### f3: Generated generic preparation lacks source support and miscodes autoclaving

major / open / confirmed; issue key: culturemech-007464-unsupported-generic-preparation.

The inspected catalogue supplies a pH condition but no sterilization method or cycle. Generated preparation_steps[2] says Sterilize by autoclaving while its action is DISSOLVE. The current importer supplies these defaults when preparation is absent, so recurrence must be addressed at the maintained source/importer boundary.

## Recommended Actions And Acceptance Checks

### a1

Use data/normalized_yaml/bacterial/NBRC_1210.yaml as the maintained correction surface. Verify its separate component rows, source title and accession against NBRC 1209; preserve source batch doses and justify any final-volume normalization before regeneration. Retain exact chemical forms, supplier qualifiers and alternatives, then regenerate through the merge entrypoint and check evidence retention.

- Compare every recovered source row, chemical form, optional component and batch instruction against the cited NBRC composition table; preserve exact supporting excerpts and locators.
- Verify owner-only chemical identifiers and canonical labels before promoting them into the generated target; a schema-bound term pass does not cover all ingredient mappings.
- Run the documented schema, strict, term and reference recipes on the resulting target; after separately authorized regeneration run just verify-merges and just audit-merge-freshness.
- Locate regenerated output by stable CultureMech ID; source-title corrections may change its filename. Do not manually patch the existing merged YAML.

### a2

Preserve the verified 7.0–7.4 pH range and the original 7.2 +/- 0.2 context from the maintained owner during regeneration; do not add an unsupported adjustment reagent.

- Compare every recovered source row, chemical form, optional component and batch instruction against the cited NBRC composition table; preserve exact supporting excerpts and locators.
- Verify owner-only chemical identifiers and canonical labels before promoting them into the generated target; a schema-bound term pass does not cover all ingredient mappings.
- Run the documented schema, strict, term and reference recipes on the resulting target; after separately authorized regeneration run just verify-merges and just audit-merge-freshness.
- Locate regenerated output by stable CultureMech ID; source-title corrections may change its filename. Do not manually patch the existing merged YAML.
- The generated pH representation retains both bounds and its NBRC locator; no midpoint-only replacement.

### a3

Verify each retained preparation instruction against an inspected collection protocol; remove unsupported defaults or mark unresolved protocol scope in the maintained record. Correct action/text semantics only for supported instructions. Prevent the source importer from regenerating scientific protocol claims solely because source text is absent, then regenerate the merged output.

- Compare every recovered source row, chemical form, optional component and batch instruction against the cited NBRC composition table; preserve exact supporting excerpts and locators.
- Verify owner-only chemical identifiers and canonical labels before promoting them into the generated target; a schema-bound term pass does not cover all ingredient mappings.
- Run the documented schema, strict, term and reference recipes on the resulting target; after separately authorized regeneration run just verify-merges and just audit-merge-freshness.
- Locate regenerated output by stable CultureMech ID; source-title corrections may change its filename. Do not manually patch the existing merged YAML.
- No inferred sterilization cycle, pH target or reagent is promoted to source-supported preparation; retained action tokens describe the supported operation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/1210.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/NBRC_1210.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/1210.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/1210.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch002/014/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-002/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch002/014/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/1210.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/1210.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| nbrc | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1209; Medium No., Medium, entire Composition table and footnotes; Comment section | supports | Official NBRC Medium 1209, 5×R2A Medium; the composition table establishes source identity, literal ingredient batch amounts and the stated conditions. It does not certify every maintained-owner inference. |
| schema-rules | src/culturemech/schema/culturemech.yaml; MediumTypeEnum; MediumCompositionTypeEnum; ConcentrationUnitEnum; PreparationActionEnum | context_only | The schema distinguishes chemically defined and undefined mixtures and defines action/unit semantics. Valid string-valued concentrations can still be scientifically malformed. |
| quantity-contract | .claude/skills/review-ingredient-concentrations/references/evidence-contract.md; Units and preparation boundaries; Required support for every assertion | context_only | Conversion of a batch mass to a concentration requires explicit final volume; preserve source forms, unit scales, alternatives and exact evidence snippets. |
| importer | src/culturemech/import/nbrc_importer.py; NBRCImporter._map_ingredients and _map_preparation_steps | context_only | Current importer maps bare source g/mg to per-liter enums. When preparation text is absent it supplies generic dissolution, pH adjustment and autoclaving; its action inference defaults to DISSOLVE and tests the literal substring autoclave. These current code paths explain a recurrence risk; historical execution was not independently replayed. |

## Limits And Additional Notes

- The NBRC catalogue lists ingredient batch masses and 1 L distilled water; it does not explicitly prescribe making up to a measured final volume. Maintained G_PER_L, MG_PER_L or ML_PER_L values are not independently certified by numerical agreement alone.
- The generated target contains no chemical ontology or MIM ingredient identifiers, DOI, PMID, organism identifier or stock-solution reference. Owner-only ontology mappings were read as future curation context, not certified by this target review.
- The inspected NBRC page provides no publication year or individual recipe authors. Source metadata is the official NBRC catalogue title/accession, persistent page URL, actual access time and captured body hash.
- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T233419Z-culturemech-007464-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 1210 (CultureMech:007464)'
started_at: '2026-10-19T23:30:22Z'
finished_at: '2026-10-19T23:34:19Z'
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
summary: The generated NBRC 1209 5×R2A Medium record collapses ten components into
  an ingredient-name blob and stores a product name as a concentration. Its pH 7.2
  ± 0.2 survives only in that blob; structured pH and source identity are missing.
  The maintained owner restores ingredient rows and pH range, but remains numerically
  named, and generic generated autoclaving is unsupported by the inspected source.
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
  - path: data/merge_yaml/merged/1210.yaml
    sha256: dc23d6676396f89e92ea7bf61624e14e828d2dffd5df1c266b6778b594c1734d
    role: target
  - path: data/normalized_yaml/bacterial/NBRC_1210.yaml
    sha256: 830da33d6a7182b89f1f35c6e00750527355bca7978692658a646abaab824bc4
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
  selection: Record 14 in Python lexicographic repository-relative path order of the
    initially uncovered merged corpus; batch 002 covers ordinals 11–20 after batch
    001. On this batch base, scripts/record_review.py list validated 34 existing bundles
    and none listed this target path or ID. Exactly one named record is assessed;
    no sampling or fleet-wide scientific conclusion.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:007464
targets:
- target_id: CultureMech:007464
  path: data/merge_yaml/merged/1210.yaml
  label: '1210'
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_1210.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/1210.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:007464
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/1210.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch002/014/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-002/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch002/014/strict.tsv"
  target_ids:
  - CultureMech:007464
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/1210.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:007464
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/1210.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:007464
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
  - CultureMech:007464
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/1210.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-19T23:34:19Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/NBRC_1210.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-19T23:34:19Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/1210.yaml
  locator: Actual command output
  accessed_at: '2026-10-19T23:31:19.345947Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/1210.yaml --workers 1 --out
    /private/tmp/culturemech-review-work-batch002/014/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-19T23:31:22.221878Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-002/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch002/014/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/1210.yaml
  locator: Actual command output
  accessed_at: '2026-10-19T23:31:25.737016Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/1210.yaml
  locator: Actual command output
  accessed_at: '2026-10-19T23:31:28.547467Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: nbrc
  kind: primary_source
  reference: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1209
  locator: Medium No., Medium, entire Composition table and footnotes; Comment section
  accessed_at: '2026-10-19T23:29:37Z'
  support: supports
  summary: Official NBRC Medium 1209, 5×R2A Medium; the composition table establishes
    source identity, literal ingredient batch amounts and the stated conditions. It
    does not certify every maintained-owner inference.
  quote: pH 7.2+/-0.2
  snapshot_sha256: d55d43a7be9fd7a3c454c739c74b91cc2c21e0cc98e0f60da95f5ce5e17e0fd5
- evidence_id: schema-rules
  kind: authority
  reference: src/culturemech/schema/culturemech.yaml
  locator: MediumTypeEnum; MediumCompositionTypeEnum; ConcentrationUnitEnum; PreparationActionEnum
  accessed_at: '2026-10-19T23:34:19Z'
  support: context_only
  summary: The schema distinguishes chemically defined and undefined mixtures and
    defines action/unit semantics. Valid string-valued concentrations can still be
    scientifically malformed.
- evidence_id: quantity-contract
  kind: authority
  reference: .claude/skills/review-ingredient-concentrations/references/evidence-contract.md
  locator: Units and preparation boundaries; Required support for every assertion
  accessed_at: '2026-10-19T23:34:19Z'
  support: context_only
  summary: Conversion of a batch mass to a concentration requires explicit final volume;
    preserve source forms, unit scales, alternatives and exact evidence snippets.
- evidence_id: importer
  kind: record_content
  reference: src/culturemech/import/nbrc_importer.py
  locator: NBRCImporter._map_ingredients and _map_preparation_steps
  accessed_at: '2026-10-19T23:34:19Z'
  support: context_only
  summary: Current importer maps bare source g/mg to per-liter enums. When preparation
    text is absent it supplies generic dissolution, pH adjustment and autoclaving;
    its action inference defaults to DISSOLVE and tests the literal substring autoclave.
    These current code paths explain a recurrence risk; historical execution was not
    independently replayed.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:007464
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Stable target, maintained owner and official source accession
  outcome: supported
  summary: The target ID resolves to the captured normalized owner via merged_from
    and the MERGED_RECIPES event. Description/import provenance names NBRC 1209, which
    the live official catalogue identifies as 5×R2A Medium. The numeric local filename/name
    is not the verified NBRC source accession.
  target_ids:
  - CultureMech:007464
  evidence_ids:
  - record
  - owner-0
  - nbrc
  details: This is one generated MediaRecipe. The inspected generated and maintained
    records carry the same stable CultureMech ID. No corpus-wide uniqueness test or
    independent historical import replay is claimed. The current merge engine is the
    future regeneration entrypoint; a fingerprint alone is not source-identity evidence.
- assessment_id: amounts
  area: quantity
  topic: Every encoded concentration and every source composition row
  outcome: concern
  summary: All 10 source rows were checked against the complete generated blob and
    structured maintained owner. The source numbers survive textually, but the target
    has no usable per-ingredient amounts. Source mass-to-final-volume conversion remains
    a separate unresolved issue.
  target_ids:
  - CultureMech:007464
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - quantity-contract
  - schema-rules
  details: 'The generated target has only two concentration objects. ingredients[0]
    is variable/VARIABLE attached to the entire composition text; ingredients[1] has
    an empty preferred_term and ''Bacto Yeast Extract (Difco)''/G_PER_L. Neither is
    an ingredient-specific quantitative recipe. The source amount/unit pairs below
    are factual transcriptions; formula typography is normalized from source subscripts,
    without changing chemical identities.


    | Owner row / component recovered from target blob | Exact source amount | Maintained
    encoding | Review decision |

    |---|---|---|---|

    | owner ingredients[0]: Bacto Yeast Extract (Difco) | 2.5 g | 2.5 G_PER_L | source
    batch mass verified; final-volume concentration remains unsupported by this page
    alone |

    | owner ingredients[1]: Bacto Proteose Peptone No. 3 (Difco) | 2.5 g | 2.5 G_PER_L
    | source batch mass verified; final-volume concentration remains unsupported by
    this page alone |

    | owner ingredients[2]: Bacto Casamino Acids (Difco) | 2.5 g | 2.5 G_PER_L | source
    batch mass verified; final-volume concentration remains unsupported by this page
    alone |

    | owner ingredients[3]: Glucose | 2.5 g | 2.5 G_PER_L | source batch mass verified;
    final-volume concentration remains unsupported by this page alone |

    | owner ingredients[4]: Soluble starch | 2.5 g | 2.5 G_PER_L | source batch mass
    verified; final-volume concentration remains unsupported by this page alone |

    | owner ingredients[5]: Sodium pyruvate | 1.5 g | 1.5 G_PER_L | source batch mass
    verified; final-volume concentration remains unsupported by this page alone |

    | owner ingredients[6]: K2HPO4 | 1.5 g | 1.5 G_PER_L | source batch mass verified;
    final-volume concentration remains unsupported by this page alone |

    | owner ingredients[7]: MgSO4·7H2O | 0.25 g | 0.25 G_PER_L | source batch mass
    verified; final-volume concentration remains unsupported by this page alone |

    | owner ingredients[8]: Agar (if needed) | 15 g | 15 G_PER_L | source batch mass
    verified; final-volume concentration remains unsupported by this page alone |

    | owner ingredients[9]: Distilled water | 1 L | 1 L | verified source volume addition;
    not a measured final-volume marker |


    The source is the main formulation, not a stock. No stock strength or dilution
    is inferred. The existing concentration enum lacks standalone g, mg and μL batch-dose
    units: retain literal batch amounts and water context in supported evidence/notes
    or preparation wording until a defensible concentration representation is available;
    do not conceal known amounts under VARIABLE or invent schema slots.'
  dimensions:
  - name: concentration_decisions
    value: 'correct: both generated concentration objects; evidence_only: literal
      source batch amounts; unsupported: unverified final-volume normalization'
    definition: Decisions apply to the two generated concentration objects and the
      individually enumerated source/owner rows; they are review context rather than
      recipe fields.
    evidence_ids:
    - record
    - owner-0
    - nbrc
    - quantity-contract
- assessment_id: grounding
  area: grounding
  topic: Identifier assertions and commercial ingredient boundaries
  outcome: unknown
  summary: No chemical CURIE or MIM linkage is asserted by either generated ingredient
    object. This is an absent structured mapping surface, not proof of invalid ontology
    IDs. Owner-only terms require exact-form and canonical-label verification before
    regeneration.
  target_ids:
  - CultureMech:007464
  evidence_ids:
  - record
  - owner-0
  - nbrc
  details: No whole-owner grounding approval is given. Keep named commercial preparations
    at their source product boundary; no catalogue number, supplier formulation, chemical
    replacement, organism growth or functional mechanism is inferred. The official
    NBRC accession and local target/owner identity were checked separately.
- assessment_id: provenance
  area: provenance
  topic: Evidence placement, generated freshness and history scope
  outcome: concern
  summary: The generated target retains an August merge event and earlier import/default
    history. The maintained owner records later composition recovery and source metadata
    absent from the generated content. This establishes a current owner/output discrepancy
    without proving that every later owner change is scientifically correct.
  target_ids:
  - CultureMech:007464
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - importer
  details: The entire embedded curation_history was read. It is provenance, not experimental
    evidence. Standalone HistoryRecord validation is not applicable to this MediaRecipe;
    embedded history is covered by the schema check and manual review. No historical
    entry was changed or independently reconstructed across all Git revisions. The
    reference recipe checked zero excerpts for the generated target. Future curation
    should attach exact claim-level source evidence and bibliographic context, and
    regeneration must retain it.
- assessment_id: conditions
  area: completeness
  topic: pH range, optional agar and formulation classification
  outcome: concern
  summary: NBRC specifies pH 7.2 +/- 0.2; the generated blob retains those characters
    but ph_range is absent and its generic adjustment step carries no target. The
    owner range 7.0–7.4 is an exact arithmetic restatement. COMPLEX/UNDEFINED is supported
    by yeast extract, proteose peptone and casamino acids; agar is optional and SOLID_AGAR
    selects the solid variant.
  target_ids:
  - CultureMech:007464
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - schema-rules
  details: '7.2 - 0.2 = 7.0 and 7.2 + 0.2 = 7.4. Do not replace the tolerance with
    only midpoint 7.2, invent a pH-adjusting reagent or infer an autoclave cycle.
    Despite the 5×R2A title, use the listed formulation directly: the source says
    optional agar 15 g, not five times 15 g.'
- assessment_id: preparation
  area: evidence
  topic: Source support for generated preparation
  outcome: concern
  summary: The inspected catalogue supplies a pH condition but no sterilization method
    or cycle. The generic dissolution line is a curator/importer paraphrase of the
    composition, not a verified order of operations. Autoclaving is described under
    action DISSOLVE, an internal action/text mismatch.
  target_ids:
  - CultureMech:007464
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - importer
  - schema-rules
  details: The maintained owner has an empty preparation_steps list; regenerating
    its current state can remove unsupported generated steps, but is not evidence
    of a new validated protocol. No incubation temperature, atmosphere, storage instruction
    or organism growth claim is inferred. Source silence is bounded to the inspected
    page; this is not a claim that no protocol exists elsewhere.
findings:
- finding_id: f1
  issue_key: culturemech-007464-collapsed-nbrc-composition
  category: representation
  severity: blocker
  status: open
  certainty: confirmed
  title: Generated composition is a text blob plus an unusable placeholder
  description: ingredients[0].preferred_term concatenates the 10-row NBRC composition
    and source numbers into one ingredient with VARIABLE concentration. ingredients[1]
    has an empty name and a product/substrate string in concentration.value with unit
    G_PER_L. The maintained owner has separate rows, but the generated record cannot
    be interpreted as the intended quantitative formulation. Its numerical name also
    omits the verified source title.
  target_ids:
  - CultureMech:007464
  field_paths:
  - ingredients[0]
  - ingredients[1]
  - name
  - original_name
  - media_term
  - references
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - quantity-contract
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_1210.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/nbrc_importer.py
    role: source importer; prevent repeat unit/preparation inference on reimport
  rule_id: P3.1
  native_severity: P3
  normalization_reason: Although P3.1 normally denotes a minor placeholder problem,
    the entire quantitative formulation is collapsed into a single ingredient and
    an empty second entry. This invalid scientific representation warrants blocker;
    passing schema validation only confirms accepted field types.
- finding_id: f2
  issue_key: culturemech-007464-structured-ph-omission
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source pH tolerance remains stranded in an ingredient name
  description: The text pH 7.2+/-0.2 is present inside ingredients[0].preferred_term,
    but the target has no ph_range and preparation_steps[1] only says Adjust pH if
    needed. The maintained owner already has source-consistent min 7.0 and max 7.4.
    The source condition is not wholly lost, but it is not represented as an actionable
    pH requirement.
  target_ids:
  - CultureMech:007464
  field_paths:
  - ph_range
  - ingredients[0].preferred_term
  - preparation_steps[1]
  evidence_ids:
  - record
  - owner-0
  - nbrc
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_1210.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f3
  issue_key: culturemech-007464-unsupported-generic-preparation
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Generated generic preparation lacks source support and miscodes autoclaving
  description: The inspected catalogue supplies a pH condition but no sterilization
    method or cycle. Generated preparation_steps[2] says Sterilize by autoclaving
    while its action is DISSOLVE. The current importer supplies these defaults when
    preparation is absent, so recurrence must be addressed at the maintained source/importer
    boundary.
  target_ids:
  - CultureMech:007464
  field_paths:
  - preparation_steps[2]
  evidence_ids:
  - record
  - owner-0
  - nbrc
  - importer
  - schema-rules
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_1210.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/nbrc_importer.py
    role: source importer; prevent unsupported preparation defaults
actions:
- action_id: a1
  description: Use data/normalized_yaml/bacterial/NBRC_1210.yaml as the maintained
    correction surface. Verify its separate component rows, source title and accession
    against NBRC 1209; preserve source batch doses and justify any final-volume normalization
    before regeneration. Retain exact chemical forms, supplier qualifiers and alternatives,
    then regenerate through the merge entrypoint and check evidence retention.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:007464
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_1210.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/nbrc_importer.py
    role: source importer; prevent repeat unit/preparation inference on reimport
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Compare every recovered source row, chemical form, optional component and batch
    instruction against the cited NBRC composition table; preserve exact supporting
    excerpts and locators.
  - Verify owner-only chemical identifiers and canonical labels before promoting them
    into the generated target; a schema-bound term pass does not cover all ingredient
    mappings.
  - Run the documented schema, strict, term and reference recipes on the resulting
    target; after separately authorized regeneration run just verify-merges and just
    audit-merge-freshness.
  - Locate regenerated output by stable CultureMech ID; source-title corrections may
    change its filename. Do not manually patch the existing merged YAML.
- action_id: a2
  description: Preserve the verified 7.0–7.4 pH range and the original 7.2 +/- 0.2
    context from the maintained owner during regeneration; do not add an unsupported
    adjustment reagent.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:007464
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_1210.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Compare every recovered source row, chemical form, optional component and batch
    instruction against the cited NBRC composition table; preserve exact supporting
    excerpts and locators.
  - Verify owner-only chemical identifiers and canonical labels before promoting them
    into the generated target; a schema-bound term pass does not cover all ingredient
    mappings.
  - Run the documented schema, strict, term and reference recipes on the resulting
    target; after separately authorized regeneration run just verify-merges and just
    audit-merge-freshness.
  - Locate regenerated output by stable CultureMech ID; source-title corrections may
    change its filename. Do not manually patch the existing merged YAML.
  - The generated pH representation retains both bounds and its NBRC locator; no midpoint-only
    replacement.
- action_id: a3
  description: Verify each retained preparation instruction against an inspected collection
    protocol; remove unsupported defaults or mark unresolved protocol scope in the
    maintained record. Correct action/text semantics only for supported instructions.
    Prevent the source importer from regenerating scientific protocol claims solely
    because source text is absent, then regenerate the merged output.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:007464
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/NBRC_1210.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/import/nbrc_importer.py
    role: source importer; prevent unsupported preparation defaults
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Compare every recovered source row, chemical form, optional component and batch
    instruction against the cited NBRC composition table; preserve exact supporting
    excerpts and locators.
  - Verify owner-only chemical identifiers and canonical labels before promoting them
    into the generated target; a schema-bound term pass does not cover all ingredient
    mappings.
  - Run the documented schema, strict, term and reference recipes on the resulting
    target; after separately authorized regeneration run just verify-merges and just
    audit-merge-freshness.
  - Locate regenerated output by stable CultureMech ID; source-title corrections may
    change its filename. Do not manually patch the existing merged YAML.
  - No inferred sterilization cycle, pH target or reagent is promoted to source-supported
    preparation; retained action tokens describe the supported operation.
limitations:
- The NBRC catalogue lists ingredient batch masses and 1 L distilled water; it does
  not explicitly prescribe making up to a measured final volume. Maintained G_PER_L,
  MG_PER_L or ML_PER_L values are not independently certified by numerical agreement
  alone.
- The generated target contains no chemical ontology or MIM ingredient identifiers,
  DOI, PMID, organism identifier or stock-solution reference. Owner-only ontology
  mappings were read as future curation context, not certified by this target review.
- The inspected NBRC page provides no publication year or individual recipe authors.
  Source metadata is the official NBRC catalogue title/accession, persistent page
  URL, actual access time and captured body hash.
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
tags:
- unreviewed-records
- batch-002
- generated-medium
```
