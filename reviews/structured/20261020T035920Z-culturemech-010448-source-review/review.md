# Source and formulation review: 1_10_r2a_medium_modified_yeast_extract (CultureMech:010448)

- Review: 20261020T035920Z-culturemech-010448-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-20T03:56:56Z
- Finished UTC: 2026-10-20T03:59:20Z
- Reviewer: OpenAI Codex (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The generated record combines DSMZ 1365 and 1365a, preserving the enriched-variant identity but the base-medium yeast amount. Maintained inputs retain the distinction and current formulation-aware merge code rejects this combination. Other listed amounts and preparation are source-supported; supplied grades, water basis and claim-level evidence need fuller representation.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Record 31 in Python lexicographic repository-relative path order of the initially uncovered merged corpus; Batch 004 selects ordinals 31-40 after three validated local batches; saved bundles are published locally in path order. On fresh origin/main at this batch base, scripts/record_review.py list validated 34 existing bundles and none listed this target path or ID. This bundle selects only the named record; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7c568537897ee4bba1b8e97f8172133c1572aec0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:010448 | data/merge_yaml/merged/1_10_r2a_medium_modified_yeast_extract.yaml | generated | 1_10_r2a_medium_modified_yeast_extract |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:010448 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:010448 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-004/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch004/031/strict.tsv |
| validate-terms | passed | True | CultureMech:010448 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:010448 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:010448 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:010448.

The four documented recipes completed; interpret the scope of each separately.

### Accession, variant and generated ownership

identity: concern. Targets: CultureMech:010448.

The selected path and CultureMech:010448 resolve unambiguously. Its generated contents conflate two non-equivalent named formulations; owner 010448 and owner 000826 retain their source-specific amounts.

The shared ingredient-set fingerprint equals the target merge_fingerprint, but the two current formulation hashes differ. Current merge_formulation_evidence raises ValueError. Thus this is a verified stale/incompatible generated merge, not evidence that the present generator still permits concentration-blind consolidation. The base accession in synonyms is a distinct variant, not an exact source duplicate. Stable IDs are not to be reassigned by this review.

### ingredients[0].concentration: Yeast extract

quantity: concern. Targets: CultureMech:010448.

correct: target 0.05 G_PER_L; source API g_l=0.25 with volume=1000 mL and original amount 0.25 g. This is the complete medium, not a stock addition.

The PDF corroborates the ingredient mass and water batch; the API explicitly supplies the normalization basis. No density, molarity or additional dilution is inferred. The target amount belongs to DSMZ 1365; the enriched-variant owner already preserves the source value.

### ingredients[1].concentration: Proteose peptone

quantity: supported. Targets: CultureMech:010448.

verified: target 0.05 G_PER_L; source API g_l=0.05 with volume=1000 mL and original amount 0.05 g. This is the complete medium, not a stock addition.

The PDF corroborates the ingredient mass and water batch; the API explicitly supplies the normalization basis. No density, molarity or additional dilution is inferred. No numerical correction is proposed.

### ingredients[2].concentration: Casamino acids

quantity: supported. Targets: CultureMech:010448.

verified: target 0.05 G_PER_L; source API g_l=0.05 with volume=1000 mL and original amount 0.05 g. This is the complete medium, not a stock addition.

The PDF corroborates the ingredient mass and water batch; the API explicitly supplies the normalization basis. No density, molarity or additional dilution is inferred. No numerical correction is proposed.

### ingredients[3].concentration: Glucose

quantity: supported. Targets: CultureMech:010448.

verified: target 0.05 G_PER_L; source API g_l=0.05 with volume=1000 mL and original amount 0.05 g. This is the complete medium, not a stock addition.

The PDF corroborates the ingredient mass and water batch; the API explicitly supplies the normalization basis. No density, molarity or additional dilution is inferred. No numerical correction is proposed.

### ingredients[4].concentration: Starch

quantity: supported. Targets: CultureMech:010448.

verified: target 0.05 G_PER_L; source API g_l=0.05 with volume=1000 mL and original amount 0.05 g. This is the complete medium, not a stock addition.

The PDF corroborates the ingredient mass and water batch; the API explicitly supplies the normalization basis. No density, molarity or additional dilution is inferred. No numerical correction is proposed.

### ingredients[5].concentration: MgSO4 x 7 H2O

quantity: supported. Targets: CultureMech:010448.

verified: target 0.005 G_PER_L; source API g_l=0.005 with volume=1000 mL and original amount 5 mg. This is the complete medium, not a stock addition.

The PDF corroborates the ingredient mass and water batch; the API explicitly supplies the normalization basis. No density, molarity or additional dilution is inferred. No numerical correction is proposed.

### ingredients[6].concentration: Agar

quantity: supported. Targets: CultureMech:010448.

verified: target 15 G_PER_L; source API g_l=15 with volume=1000 mL and original amount 15 g. This is the complete medium, not a stock addition.

The PDF corroborates the ingredient mass and water batch; the API explicitly supplies the normalization basis. No density, molarity or additional dilution is inferred. No numerical correction is proposed.

### Chemical forms, mixtures and linkage

identity: concern. Targets: CultureMech:010448.

Four primary and four secondary CHEBI references resolve with matching labels and nonobsolete identities. The heptahydrate is correct and generic glucose is not narrowed to a stereoisomer. However, the source-specific peptone and starch attributes are lost.

Seven direct ingredient instances; zero nested or stock-addition assertions. Four of seven have both primary and secondary CHEBI links (57.14% linkage coverage, on a 0–100 percent scale; not scientific accuracy). Three complex mixtures remain ungrounded rather than being assigned an invented pure chemical identity. CHEBI:28017 identifies starch broadly, not its soluble preparation grade. The source peptone is Proteose Peptone (Difco no. 3). Broad valid ontology IDs do not preserve these supplied-form distinctions by themselves.

### pH, physical state and preparation

consistency: supported. Targets: CultureMech:010448.

The recorded pH range, alginic-acid adjustment ordering, agar dissolution and sterilization match the complete source paragraph. Agar supports SOLID_AGAR; G_PER_L for a source-specified agar formulation is dimensionally valid.

Alginic acid is named in preparation with no fixed amount; no dose, concentration or additional stock is inferred. The single source solution heading does not imply a missing stock dilution. No incubation temperature, atmosphere, storage, shelf life or growth endpoint is claimed. Source water batch is omitted from the structured recipe and reported separately below.

### Classification, organisms and optional fields

scope: supported. Targets: CultureMech:010448.

COMPLEX/UNDEFINED is consistent with undefined extracts and peptones; the API marks the medium complex. The generic cultivation application does not assert experimental growth.

No target organism, organism identifier, DOI, PMID, parent reference, variant relation, solution link or transcriptomics claim is present. Their absence is not a defect without a specific source claim. Bacterial and fungal categories reflect the combined owner filings and must not be treated as evidence of cross-variant growth or equivalence. No nutritional-role or mechanistic assertions require independent literature verification.

### Recoverable source versus claim-level evidence

provenance: concern. Targets: CultureMech:010448.

The collection accession, working URL and chronological import/enrichment/merge history are recoverable. Neither owner nor target has ingredient-level concentration evidence; deterministic reference validation examined zero excerpts.

Complete target and both maintained owners read, including history and all metadata. No historical operation was replayed or certified merely from its curator string. Existing timestamps with offsets are schema-valid. Explicit source attributes and water are not found anywhere in these three complete records except the peptone/starch generic labels; no repository-wide absence claim is made. The source distinguishes them clearly. There are no unresolved discussion flags to close.

## Findings

### f1: Generated enriched-variant identity carries the base-medium formulation

blocker / open / confirmed; issue key: culturemech-010448-conflated-dsmz-1365-1365a.

The target combines 1365 and 1365a as duplicates, yet their source yeast amounts differ fivefold. The target names 1365a while retaining the 1365 amount. Both maintained inputs are correct for their own accession; current formulation-aware code rejects merging them. This makes the generated record denote a different formulation from its declared variant.

### f2: Supplied ingredient grades and solvent basis are omitted

major / open / confirmed; issue key: culturemech-010448-source-form-and-water-omissions.

Both normalized owners and the target lose the source proteose-peptone grade and soluble-starch qualifier. They also omit the explicit distilled-water batch. Valid broad chemical labels and G_PER_L values do not preserve those preparation details.

### f3: Source quantities lack claim-level evidence entries

minor / open / confirmed; issue key: culturemech-010448-concentration-evidence-gap.

All seven concentration assertions lack scoped evidence in the maintained owners and generated target. The source is recoverable and six target amounts are corroborated; the wrong variant amount is separately a blocker. This finding concerns evidence placement, not an assertion that all numbers are unsupported.

## Recommended Actions And Acceptance Checks

### a1

Retain the distinct maintained formulations and regenerate stale merged outputs using current compatibility gates; do not patch this derived YAML or flatten the difference into a synonym.

- Confirm both normalized owners against their separate DSMZ source sheets; preserve their IDs and different yeast amounts.
- Regenerate through the maintained formulation-aware merge entrypoint; verify that the two accessions remain separate and the enriched variant retains its own formulation.
- Run just validate-schema, just validate-strict, just validate-terms and just validate-references on corrected outputs; run just verify-merges and just audit-merge-freshness for authorized regeneration.

### a2

Preserve supplied-form attributes and the stated water basis in maintained inputs with source evidence; inspect the importer attribute/water handling before regeneration. Do not invent a new grade-specific ontology ID or infer extra final-volume precision.

- Verify the two supplied-form qualifiers and water basis against each respective primary source.
- Retain accurate broad CHEBI identities with explicit grade/context notes if no exact term is available.
- Run focused schema/term/reference checks and authorized merge freshness checks.

### a3

Add concise exact source excerpts and batch-basis context at the narrowest applicable fields in the maintained owners, keeping the two formulations separate. Preserve history and regenerate only under separate curation authorization.

- Verify each excerpt against its own accession and exact ingredient row.
- Use schema-supported evidence fields; validate reference excerpts and confirm generated evidence remains attached to the correct claim.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/1_10_r2a_medium_modified_yeast_extract.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/fungal/1_10_r2a_medium_modified_yeast_extract.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/1_10_r2a_medium_modified.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/1_10_r2a_medium_modified_yeast_extract.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/1_10_r2a_medium_modified_yeast_extract.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch004/031/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-004/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch004/031/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/1_10_r2a_medium_modified_yeast_extract.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/1_10_r2a_medium_modified_yeast_extract.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| dsmz-a | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1365a.pdf; One-page source, title, eight formulation rows and final preparation paragraph | supports | DSMZ 1365a identifies the yeast-enriched variant. Its yeast row differs from the generated value. The sheet also specifies the peptone grade, soluble starch, water batch, pH and preparation. |
| dsmz-base | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1365.pdf; One-page source, title and formulation rows | supports | DSMZ 1365 is the base formulation. Its yeast row agrees with the generated ingredient array but not the generated accession or variant name. The six other solute rows and preparation agree with the enriched variant. |
| api-a | https://mediadive.dsmz.de/rest/medium/1365a; data.medium and data.solutions[0], including volume, recipe and steps | supports | Accession 1365a, complex-medium annotation, solution 2752, volume 1000, all eight recipe rows and preparation inspected. The API independently encodes g_l for the seven solutes and retains supplied-form attributes. The sole solution is the complete formulation, not a separately dosed stock. |
| api-base | https://mediadive.dsmz.de/rest/medium/1365; data.medium and data.solutions[0] | supports | Accession 1365, solution 2750, volume 1000 and all recipe rows inspected; the yeast amount differs from variant 1365a. No other listed solute differs. |
| chebi-17234 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234; OLS exact-IRI response: obo_id, label, definition, obsolete flag and synonyms | supports | CHEBI:17234 resolves to glucose; obsolete=False. Identity checked against the actual supplied ingredient; no molarity calculation made. |
| chebi-28017 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28017; OLS exact-IRI response: obo_id, label, definition, obsolete flag and synonyms | supports | CHEBI:28017 resolves to starch; obsolete=False. Identity checked against the actual supplied ingredient; no molarity calculation made. |
| chebi-31795 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795; OLS exact-IRI response: obo_id, label, definition, obsolete flag and synonyms | supports | CHEBI:31795 resolves to magnesium sulfate heptahydrate; obsolete=False. Identity checked against the actual supplied ingredient; no molarity calculation made. |
| chebi-2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509; OLS exact-IRI response: obo_id, label, definition, obsolete flag and synonyms | supports | CHEBI:2509 resolves to agar; obsolete=False. Identity checked against the actual supplied ingredient; no molarity calculation made. |
| mim-index | src/culturemech/data/mediaingredientmech/label_index.csv; All rows for four asserted CHEBI keys; pinned metadata included in input capture | supports | All four secondary links have live MAPPED preferred-term rows. Rejected alias rows do not invalidate the live identities. No legacy MIM numeric identifier is asserted. This checks the four asserted keys, not arbitrary alternative labels. |
| identity-search | repository checkout; Whole-checkout top-level ID search with rg --no-ignore --hidden | supports | ./data/normalized_yaml/fungal/1_10_r2a_medium_modified_yeast_extract.yaml:1:id: CultureMech:010448<br>./data/merge_yaml/merged/1_10_r2a_medium_modified_yeast_extract.yaml:1:id: CultureMech:010448<br>./data/normalized_yaml/bacterial/1_10_r2a_medium_modified.yaml:1:id: CultureMech:000826<br> |
| merge-current | src/culturemech/merge/formulation.py; FormulationFingerprinter and merge_formulation_evidence; matcher.group_formulations and merge entrypoint also inspected | supports | Bounded read-only evaluation on the two exact maintained owners: [{"path": "data/normalized_yaml/bacterial/1_10_r2a_medium_modified.yaml", "id": "CultureMech:000826", "ingredient_set_hash": "c32df5c9f3720e0f284dfc09cb15721b824ad4f2c63a831b05cac076bb7f3ed7", "formulation_hash": "23d6b0133ec205d4ca606557a9cad1106c193b19e8e1224ea130b9d11cee2391"}, {"path": "data/normalized_yaml/fungal/1_10_r2a_medium_modified_yeast_extract.yaml", "id": "CultureMech:010448", "ingredient_set_hash": "c32df5c9f3720e0f284dfc09cb15721b824ad4f2c63a831b05cac076bb7f3ed7", "formulation_hash": "3eb2b4dd2818c2f46e39922e3f36471dcd67ad4d7d810e5eadb4c7ac82bfddd5"}]; combined merge result: Incompatible formulations; ingredient-set similarity is insufficient. The current entrypoint groups by formulation; ingredient signatures remain candidate keys. The saved generated output is inconsistent with these current protections. |

## Limits And Additional Notes

- Collection recipes establish formulations, not organism-specific growth. Bacterial/fungal filing categories are not experimental growth evidence.
- Full corpus merge regeneration was not run. A bounded call proves these two exact owners are incompatible under current merge logic; it does not certify all merge outputs.
- The source batch and API volume support the recorded mass-per-liter normalization. No independent physical final-volume measurement or unspecified reagent dose is inferred.
- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- No publication or remote mutation was performed. Only this new review bundle is proposed for local saving.
- The native rule guide contains older ingredient-set grouping prose. Current executable formulation grouping and explicit source differences govern this finding; ingredient similarity alone is not equivalence.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T035920Z-culturemech-010448-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 1_10_r2a_medium_modified_yeast_extract (CultureMech:010448)'
started_at: '2026-10-20T03:56:56Z'
finished_at: '2026-10-20T03:59:20Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author or edit the assessed recipe bytes; this
    independent agent review compares captured local inputs with inspected collection
    sources and ontology entries, without experimental verification.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: The generated record combines DSMZ 1365 and 1365a, preserving the enriched-variant
  identity but the base-medium yeast amount. Maintained inputs retain the distinction
  and current formulation-aware merge code rejects this combination. Other listed
  amounts and preparation are source-supported; supplied grades, water basis and claim-level
  evidence need fuller representation.
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
  - path: data/merge_yaml/merged/1_10_r2a_medium_modified_yeast_extract.yaml
    sha256: 3b654dc502750c539bf1cf29904f6b06979fd63c69d937eb5ecced40183b11b6
    role: target
  - path: data/normalized_yaml/bacterial/1_10_r2a_medium_modified.yaml
    sha256: f3c3114378f61566625366e0f5c3d6ba1a5fc69185ac782ebb859277d69a2f4b
    role: context
  - path: data/normalized_yaml/fungal/1_10_r2a_medium_modified_yeast_extract.yaml
    sha256: c2388cef85fcb5ec6871a4dea871ca185285a86dbc460794dca5e46da3e1a493
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
  selection: Record 31 in Python lexicographic repository-relative path order of the
    initially uncovered merged corpus; Batch 004 selects ordinals 31-40 after three
    validated local batches; saved bundles are published locally in path order. On
    fresh origin/main at this batch base, scripts/record_review.py list validated
    34 existing bundles and none listed this target path or ID. This bundle selects
    only the named record; no sampling or fleet-wide scientific claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:010448
targets:
- target_id: CultureMech:010448
  path: data/merge_yaml/merged/1_10_r2a_medium_modified_yeast_extract.yaml
  label: 1_10_r2a_medium_modified_yeast_extract
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/fungal/1_10_r2a_medium_modified_yeast_extract.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_r2a_medium_modified.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/1_10_r2a_medium_modified_yeast_extract.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:010448
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/1_10_r2a_medium_modified_yeast_extract.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch004/031/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-004/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch004/031/strict.tsv"
  target_ids:
  - CultureMech:010448
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/1_10_r2a_medium_modified_yeast_extract.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:010448
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/1_10_r2a_medium_modified_yeast_extract.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:010448
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
  - CultureMech:010448
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/1_10_r2a_medium_modified_yeast_extract.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-20T03:59:20Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/fungal/1_10_r2a_medium_modified_yeast_extract.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-20T03:59:20Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/1_10_r2a_medium_modified.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-20T03:59:20Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/1_10_r2a_medium_modified_yeast_extract.yaml
  locator: Actual command output
  accessed_at: '2026-10-20T03:56:58.178633Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/1_10_r2a_medium_modified_yeast_extract.yaml
    --workers 1 --out /private/tmp/culturemech-review-work-batch004/031/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-20T03:56:59.478453Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-004/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch004/031/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/1_10_r2a_medium_modified_yeast_extract.yaml
  locator: Actual command output
  accessed_at: '2026-10-20T03:57:01.624959Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/1_10_r2a_medium_modified_yeast_extract.yaml
  locator: Actual command output
  accessed_at: '2026-10-20T03:57:02.642930Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: dsmz-a
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1365a.pdf
  locator: One-page source, title, eight formulation rows and final preparation paragraph
  accessed_at: '2026-10-20T03:57:30.202889Z'
  support: supports
  summary: DSMZ 1365a identifies the yeast-enriched variant. Its yeast row differs
    from the generated value. The sheet also specifies the peptone grade, soluble
    starch, water batch, pH and preparation.
  quote: Yeast extract 0.250 g
  snapshot_sha256: 62cd5e1a74626708ff66afcfca6ef7c3d7a86d85ea6dc79095ba323064f6d942
- evidence_id: dsmz-base
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1365.pdf
  locator: One-page source, title and formulation rows
  accessed_at: '2026-10-20T03:57:28.926118Z'
  support: supports
  summary: DSMZ 1365 is the base formulation. Its yeast row agrees with the generated
    ingredient array but not the generated accession or variant name. The six other
    solute rows and preparation agree with the enriched variant.
  quote: Yeast extract 0.050 g
  snapshot_sha256: b015f21986bdf4a5a48e357be33f9e6e2d5c8a5a36091c5b36efcb02f9147217
- evidence_id: api-a
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1365a
  locator: data.medium and data.solutions[0], including volume, recipe and steps
  accessed_at: '2026-10-20T03:57:32.004865Z'
  support: supports
  summary: Accession 1365a, complex-medium annotation, solution 2752, volume 1000,
    all eight recipe rows and preparation inspected. The API independently encodes
    g_l for the seven solutes and retains supplied-form attributes. The sole solution
    is the complete formulation, not a separately dosed stock.
  snapshot_sha256: 28a109c70aab1b2fb2538b1e0e35913074396d16d4872f1cdb79d3014c54b095
- evidence_id: api-base
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1365
  locator: data.medium and data.solutions[0]
  accessed_at: '2026-10-20T03:57:31.150483Z'
  support: supports
  summary: Accession 1365, solution 2750, volume 1000 and all recipe rows inspected;
    the yeast amount differs from variant 1365a. No other listed solute differs.
  snapshot_sha256: b09edc4d21c2773d91cb1391b6f179f62475134e3e96f40566eaac66ceefa359
- evidence_id: chebi-17234
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17234
  locator: 'OLS exact-IRI response: obo_id, label, definition, obsolete flag and synonyms'
  accessed_at: '2026-10-20T03:57:32.595833Z'
  support: supports
  summary: CHEBI:17234 resolves to glucose; obsolete=False. Identity checked against
    the actual supplied ingredient; no molarity calculation made.
  snapshot_sha256: e3b9cbcd7b1e08bb05564cf82f924b29c554767e9b40bf1e4c85ab1bce09330f
- evidence_id: chebi-28017
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_28017
  locator: 'OLS exact-IRI response: obo_id, label, definition, obsolete flag and synonyms'
  accessed_at: '2026-10-20T03:57:33.391810Z'
  support: supports
  summary: CHEBI:28017 resolves to starch; obsolete=False. Identity checked against
    the actual supplied ingredient; no molarity calculation made.
  snapshot_sha256: 959b4330165a7ff12d2e464f4a7b44e148376624d04cf7764b6a8671c1c99204
- evidence_id: chebi-31795
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31795
  locator: 'OLS exact-IRI response: obo_id, label, definition, obsolete flag and synonyms'
  accessed_at: '2026-10-20T03:57:34.006322Z'
  support: supports
  summary: CHEBI:31795 resolves to magnesium sulfate heptahydrate; obsolete=False.
    Identity checked against the actual supplied ingredient; no molarity calculation
    made.
  snapshot_sha256: 45b9cc51f5d062ae7e320b9f043d8cd770234d811ec3bf26bc247b51c22213bb
- evidence_id: chebi-2509
  kind: database
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_2509
  locator: 'OLS exact-IRI response: obo_id, label, definition, obsolete flag and synonyms'
  accessed_at: '2026-10-20T03:57:34.697126Z'
  support: supports
  summary: CHEBI:2509 resolves to agar; obsolete=False. Identity checked against the
    actual supplied ingredient; no molarity calculation made.
  snapshot_sha256: 8e9a8502590bbb760008a75161094eaca762e8edac19901d959bf6863692bd5a
- evidence_id: mim-index
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All rows for four asserted CHEBI keys; pinned metadata included in input
    capture
  accessed_at: '2026-10-20T03:59:20Z'
  support: supports
  summary: All four secondary links have live MAPPED preferred-term rows. Rejected
    alias rows do not invalidate the live identities. No legacy MIM numeric identifier
    is asserted. This checks the four asserted keys, not arbitrary alternative labels.
- evidence_id: identity-search
  kind: record_content
  reference: repository checkout
  locator: Whole-checkout top-level ID search with rg --no-ignore --hidden
  accessed_at: '2026-10-20T03:58:09.311521Z'
  support: supports
  summary: './data/normalized_yaml/fungal/1_10_r2a_medium_modified_yeast_extract.yaml:1:id:
    CultureMech:010448

    ./data/merge_yaml/merged/1_10_r2a_medium_modified_yeast_extract.yaml:1:id: CultureMech:010448

    ./data/normalized_yaml/bacterial/1_10_r2a_medium_modified.yaml:1:id: CultureMech:000826

    '
  search_scope: whole checkout including ignored and hidden files
- evidence_id: merge-current
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: FormulationFingerprinter and merge_formulation_evidence; matcher.group_formulations
    and merge entrypoint also inspected
  accessed_at: '2026-10-20T03:58:09.311521Z'
  support: supports
  summary: 'Bounded read-only evaluation on the two exact maintained owners: [{"path":
    "data/normalized_yaml/bacterial/1_10_r2a_medium_modified.yaml", "id": "CultureMech:000826",
    "ingredient_set_hash": "c32df5c9f3720e0f284dfc09cb15721b824ad4f2c63a831b05cac076bb7f3ed7",
    "formulation_hash": "23d6b0133ec205d4ca606557a9cad1106c193b19e8e1224ea130b9d11cee2391"},
    {"path": "data/normalized_yaml/fungal/1_10_r2a_medium_modified_yeast_extract.yaml",
    "id": "CultureMech:010448", "ingredient_set_hash": "c32df5c9f3720e0f284dfc09cb15721b824ad4f2c63a831b05cac076bb7f3ed7",
    "formulation_hash": "3eb2b4dd2818c2f46e39922e3f36471dcd67ad4d7d810e5eadb4c7ac82bfddd5"}];
    combined merge result: Incompatible formulations; ingredient-set similarity is
    insufficient. The current entrypoint groups by formulation; ingredient signatures
    remain candidate keys. The saved generated output is inconsistent with these current
    protections.'
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:010448
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Accession, variant and generated ownership
  outcome: concern
  summary: The selected path and CultureMech:010448 resolve unambiguously. Its generated
    contents conflate two non-equivalent named formulations; owner 010448 and owner
    000826 retain their source-specific amounts.
  target_ids:
  - CultureMech:010448
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz-a
  - dsmz-base
  - identity-search
  - merge-current
  details: The shared ingredient-set fingerprint equals the target merge_fingerprint,
    but the two current formulation hashes differ. Current merge_formulation_evidence
    raises ValueError. Thus this is a verified stale/incompatible generated merge,
    not evidence that the present generator still permits concentration-blind consolidation.
    The base accession in synonyms is a distinct variant, not an exact source duplicate.
    Stable IDs are not to be reassigned by this review.
- assessment_id: amount-0
  area: quantity
  topic: 'ingredients[0].concentration: Yeast extract'
  outcome: concern
  summary: 'correct: target 0.05 G_PER_L; source API g_l=0.25 with volume=1000 mL
    and original amount 0.25 g. This is the complete medium, not a stock addition.'
  target_ids:
  - CultureMech:010448
  evidence_ids:
  - record
  - api-a
  - dsmz-a
  details: The PDF corroborates the ingredient mass and water batch; the API explicitly
    supplies the normalization basis. No density, molarity or additional dilution
    is inferred. The target amount belongs to DSMZ 1365; the enriched-variant owner
    already preserves the source value.
  dimensions:
  - name: concentration_decision
    value: correct
    definition: Decision for this exact generated ingredient amount relative to the
      named variant source
    evidence_ids:
    - api-a
    - dsmz-a
- assessment_id: amount-1
  area: quantity
  topic: 'ingredients[1].concentration: Proteose peptone'
  outcome: supported
  summary: 'verified: target 0.05 G_PER_L; source API g_l=0.05 with volume=1000 mL
    and original amount 0.05 g. This is the complete medium, not a stock addition.'
  target_ids:
  - CultureMech:010448
  evidence_ids:
  - record
  - api-a
  - dsmz-a
  details: The PDF corroborates the ingredient mass and water batch; the API explicitly
    supplies the normalization basis. No density, molarity or additional dilution
    is inferred. No numerical correction is proposed.
  dimensions:
  - name: concentration_decision
    value: verified
    definition: Decision for this exact generated ingredient amount relative to the
      named variant source
    evidence_ids:
    - api-a
    - dsmz-a
- assessment_id: amount-2
  area: quantity
  topic: 'ingredients[2].concentration: Casamino acids'
  outcome: supported
  summary: 'verified: target 0.05 G_PER_L; source API g_l=0.05 with volume=1000 mL
    and original amount 0.05 g. This is the complete medium, not a stock addition.'
  target_ids:
  - CultureMech:010448
  evidence_ids:
  - record
  - api-a
  - dsmz-a
  details: The PDF corroborates the ingredient mass and water batch; the API explicitly
    supplies the normalization basis. No density, molarity or additional dilution
    is inferred. No numerical correction is proposed.
  dimensions:
  - name: concentration_decision
    value: verified
    definition: Decision for this exact generated ingredient amount relative to the
      named variant source
    evidence_ids:
    - api-a
    - dsmz-a
- assessment_id: amount-3
  area: quantity
  topic: 'ingredients[3].concentration: Glucose'
  outcome: supported
  summary: 'verified: target 0.05 G_PER_L; source API g_l=0.05 with volume=1000 mL
    and original amount 0.05 g. This is the complete medium, not a stock addition.'
  target_ids:
  - CultureMech:010448
  evidence_ids:
  - record
  - api-a
  - dsmz-a
  details: The PDF corroborates the ingredient mass and water batch; the API explicitly
    supplies the normalization basis. No density, molarity or additional dilution
    is inferred. No numerical correction is proposed.
  dimensions:
  - name: concentration_decision
    value: verified
    definition: Decision for this exact generated ingredient amount relative to the
      named variant source
    evidence_ids:
    - api-a
    - dsmz-a
- assessment_id: amount-4
  area: quantity
  topic: 'ingredients[4].concentration: Starch'
  outcome: supported
  summary: 'verified: target 0.05 G_PER_L; source API g_l=0.05 with volume=1000 mL
    and original amount 0.05 g. This is the complete medium, not a stock addition.'
  target_ids:
  - CultureMech:010448
  evidence_ids:
  - record
  - api-a
  - dsmz-a
  details: The PDF corroborates the ingredient mass and water batch; the API explicitly
    supplies the normalization basis. No density, molarity or additional dilution
    is inferred. No numerical correction is proposed.
  dimensions:
  - name: concentration_decision
    value: verified
    definition: Decision for this exact generated ingredient amount relative to the
      named variant source
    evidence_ids:
    - api-a
    - dsmz-a
- assessment_id: amount-5
  area: quantity
  topic: 'ingredients[5].concentration: MgSO4 x 7 H2O'
  outcome: supported
  summary: 'verified: target 0.005 G_PER_L; source API g_l=0.005 with volume=1000
    mL and original amount 5 mg. This is the complete medium, not a stock addition.'
  target_ids:
  - CultureMech:010448
  evidence_ids:
  - record
  - api-a
  - dsmz-a
  details: The PDF corroborates the ingredient mass and water batch; the API explicitly
    supplies the normalization basis. No density, molarity or additional dilution
    is inferred. No numerical correction is proposed.
  dimensions:
  - name: concentration_decision
    value: verified
    definition: Decision for this exact generated ingredient amount relative to the
      named variant source
    evidence_ids:
    - api-a
    - dsmz-a
- assessment_id: amount-6
  area: quantity
  topic: 'ingredients[6].concentration: Agar'
  outcome: supported
  summary: 'verified: target 15 G_PER_L; source API g_l=15 with volume=1000 mL and
    original amount 15 g. This is the complete medium, not a stock addition.'
  target_ids:
  - CultureMech:010448
  evidence_ids:
  - record
  - api-a
  - dsmz-a
  details: The PDF corroborates the ingredient mass and water batch; the API explicitly
    supplies the normalization basis. No density, molarity or additional dilution
    is inferred. No numerical correction is proposed.
  dimensions:
  - name: concentration_decision
    value: verified
    definition: Decision for this exact generated ingredient amount relative to the
      named variant source
    evidence_ids:
    - api-a
    - dsmz-a
- assessment_id: ingredients
  area: identity
  topic: Chemical forms, mixtures and linkage
  outcome: concern
  summary: Four primary and four secondary CHEBI references resolve with matching
    labels and nonobsolete identities. The heptahydrate is correct and generic glucose
    is not narrowed to a stereoisomer. However, the source-specific peptone and starch
    attributes are lost.
  target_ids:
  - CultureMech:010448
  evidence_ids:
  - record
  - owner-0
  - api-a
  - dsmz-a
  - chebi-17234
  - chebi-28017
  - chebi-31795
  - chebi-2509
  - mim-index
  details: Seven direct ingredient instances; zero nested or stock-addition assertions.
    Four of seven have both primary and secondary CHEBI links (57.14% linkage coverage,
    on a 0–100 percent scale; not scientific accuracy). Three complex mixtures remain
    ungrounded rather than being assigned an invented pure chemical identity. CHEBI:28017
    identifies starch broadly, not its soluble preparation grade. The source peptone
    is Proteose Peptone (Difco no. 3). Broad valid ontology IDs do not preserve these
    supplied-form distinctions by themselves.
- assessment_id: conditions
  area: consistency
  topic: pH, physical state and preparation
  outcome: supported
  summary: The recorded pH range, alginic-acid adjustment ordering, agar dissolution
    and sterilization match the complete source paragraph. Agar supports SOLID_AGAR;
    G_PER_L for a source-specified agar formulation is dimensionally valid.
  target_ids:
  - CultureMech:010448
  evidence_ids:
  - record
  - dsmz-a
  - api-a
  details: Alginic acid is named in preparation with no fixed amount; no dose, concentration
    or additional stock is inferred. The single source solution heading does not imply
    a missing stock dilution. No incubation temperature, atmosphere, storage, shelf
    life or growth endpoint is claimed. Source water batch is omitted from the structured
    recipe and reported separately below.
- assessment_id: scope
  area: scope
  topic: Classification, organisms and optional fields
  outcome: supported
  summary: COMPLEX/UNDEFINED is consistent with undefined extracts and peptones; the
    API marks the medium complex. The generic cultivation application does not assert
    experimental growth.
  target_ids:
  - CultureMech:010448
  evidence_ids:
  - record
  - api-a
  details: No target organism, organism identifier, DOI, PMID, parent reference, variant
    relation, solution link or transcriptomics claim is present. Their absence is
    not a defect without a specific source claim. Bacterial and fungal categories
    reflect the combined owner filings and must not be treated as evidence of cross-variant
    growth or equivalence. No nutritional-role or mechanistic assertions require independent
    literature verification.
- assessment_id: provenance
  area: provenance
  topic: Recoverable source versus claim-level evidence
  outcome: concern
  summary: The collection accession, working URL and chronological import/enrichment/merge
    history are recoverable. Neither owner nor target has ingredient-level concentration
    evidence; deterministic reference validation examined zero excerpts.
  target_ids:
  - CultureMech:010448
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - validate-references
  - dsmz-a
  details: Complete target and both maintained owners read, including history and
    all metadata. No historical operation was replayed or certified merely from its
    curator string. Existing timestamps with offsets are schema-valid. Explicit source
    attributes and water are not found anywhere in these three complete records except
    the peptone/starch generic labels; no repository-wide absence claim is made. The
    source distinguishes them clearly. There are no unresolved discussion flags to
    close.
findings:
- finding_id: f1
  issue_key: culturemech-010448-conflated-dsmz-1365-1365a
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Generated enriched-variant identity carries the base-medium formulation
  description: The target combines 1365 and 1365a as duplicates, yet their source
    yeast amounts differ fivefold. The target names 1365a while retaining the 1365
    amount. Both maintained inputs are correct for their own accession; current formulation-aware
    code rejects merging them. This makes the generated record denote a different
    formulation from its declared variant.
  target_ids:
  - CultureMech:010448
  field_paths:
  - media_term
  - ingredients[0].concentration
  - synonyms
  - merged_from
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz-a
  - dsmz-base
  - api-a
  - api-base
  - merge-current
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/fungal/1_10_r2a_medium_modified_yeast_extract.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_r2a_medium_modified.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  rule_id: P2.5
  native_severity: P2
  normalization_reason: P2 normalized to blocker based on the specific formulation,
    identity or representation impact described here; deterministic passing checks
    do not negate it.
- finding_id: f2
  issue_key: culturemech-010448-source-form-and-water-omissions
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Supplied ingredient grades and solvent basis are omitted
  description: Both normalized owners and the target lose the source proteose-peptone
    grade and soluble-starch qualifier. They also omit the explicit distilled-water
    batch. Valid broad chemical labels and G_PER_L values do not preserve those preparation
    details.
  target_ids:
  - CultureMech:010448
  field_paths:
  - ingredients[1].preferred_term
  - ingredients[4].preferred_term
  - ingredients
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz-a
  - api-a
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/fungal/1_10_r2a_medium_modified_yeast_extract.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_r2a_medium_modified.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f3
  issue_key: culturemech-010448-concentration-evidence-gap
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Source quantities lack claim-level evidence entries
  description: All seven concentration assertions lack scoped evidence in the maintained
    owners and generated target. The source is recoverable and six target amounts
    are corroborated; the wrong variant amount is separately a blocker. This finding
    concerns evidence placement, not an assertion that all numbers are unsupported.
  target_ids:
  - CultureMech:010448
  field_paths:
  - ingredients[*].evidence
  - references
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - validate-references
  - api-a
  - dsmz-a
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/fungal/1_10_r2a_medium_modified_yeast_extract.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_r2a_medium_modified.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Retain the distinct maintained formulations and regenerate stale merged
    outputs using current compatibility gates; do not patch this derived YAML or flatten
    the difference into a synonym.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:010448
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/fungal/1_10_r2a_medium_modified_yeast_extract.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_r2a_medium_modified.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Confirm both normalized owners against their separate DSMZ source sheets; preserve
    their IDs and different yeast amounts.
  - Regenerate through the maintained formulation-aware merge entrypoint; verify that
    the two accessions remain separate and the enriched variant retains its own formulation.
  - Run just validate-schema, just validate-strict, just validate-terms and just validate-references
    on corrected outputs; run just verify-merges and just audit-merge-freshness for
    authorized regeneration.
- action_id: a2
  description: Preserve supplied-form attributes and the stated water basis in maintained
    inputs with source evidence; inspect the importer attribute/water handling before
    regeneration. Do not invent a new grade-specific ontology ID or infer extra final-volume
    precision.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:010448
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/fungal/1_10_r2a_medium_modified_yeast_extract.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_r2a_medium_modified.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify the two supplied-form qualifiers and water basis against each respective
    primary source.
  - Retain accurate broad CHEBI identities with explicit grade/context notes if no
    exact term is available.
  - Run focused schema/term/reference checks and authorized merge freshness checks.
- action_id: a3
  description: Add concise exact source excerpts and batch-basis context at the narrowest
    applicable fields in the maintained owners, keeping the two formulations separate.
    Preserve history and regenerate only under separate curation authorization.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:010448
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/fungal/1_10_r2a_medium_modified_yeast_extract.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/1_10_r2a_medium_modified.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Verify each excerpt against its own accession and exact ingredient row.
  - Use schema-supported evidence fields; validate reference excerpts and confirm
    generated evidence remains attached to the correct claim.
limitations:
- Collection recipes establish formulations, not organism-specific growth. Bacterial/fungal
  filing categories are not experimental growth evidence.
- Full corpus merge regeneration was not run. A bounded call proves these two exact
  owners are incompatible under current merge logic; it does not certify all merge
  outputs.
- The source batch and API volume support the recorded mass-per-liter normalization.
  No independent physical final-volume measurement or unspecified reagent dose is
  inferred.
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. Reference-check coverage must be read from its actual output; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
tags:
- unreviewed-records
- batch-004
- generated-medium
notes:
- No publication or remote mutation was performed. Only this new review bundle is
  proposed for local saving.
- The native rule guide contains older ingredient-set grouping prose. Current executable
  formulation grouping and explicit source differences govern this finding; ingredient
  similarity alone is not equivalence.
```
