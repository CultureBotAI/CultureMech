# Source and formulation review: 15_mgm_medium (CultureMech:000848)

- Review: 20261019T233801Z-culturemech-000848-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-19T23:30:32Z
- Finished UTC: 2026-10-19T23:38:01Z
- Reviewer: OpenAI Codex with delegated source and validator checks (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The record merges distinct DSMZ 10% and 15% MGM recipes after flattening their shared salt stock into undiluted final-medium amounts. Both source identities resolve, but their stock doses and preparation differ. Primary PDF and MediaDive disagreements must remain explicit. The review is complete with a blocking identity defect and additional quantity, preparation and provenance findings.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Record 20 in Python lexicographic repository-relative path order of the initially uncovered merged corpus; batch 002 covers ordinals 11–20 after batch 001. On fresh origin/main at this batch base, scripts/record_review.py list validated 34 existing bundles and none listed this target path or ID. This bundle selects only the named record; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7c568537897ee4bba1b8e97f8172133c1572aec0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:000848 | data/merge_yaml/merged/15_mgm_medium.yaml | generated | 15_mgm_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:000848 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:000848 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-002/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch002/020/strict.tsv |
| validate-terms | passed | True | CultureMech:000848 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:000848 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:000848 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:000848.

The four documented recipes completed; interpret the scope of each separately.

### Limits of passing deterministic checks

evidence: concern. Targets: CultureMech:000848.

All four documented target commands exited 0. Strict validation used only layers=schema; reference validation explicitly checked 0 references. These results do not validate recipe identity, source support, concentrations or embedded history claims.

### Organism, growth and cultivation-condition scope

scope: not_applicable. Targets: CultureMech:000848.

The target contains no organism, strain, growth experiment, temperature, incubation duration, oxygen requirement, DOI or PMID assertion. Recipe availability and generic cultivation wording establish no strain-specific growth result. No organism enrichment was inferred from ingredients.

### Field-level source support

evidence: concern. Targets: CultureMech:000848.

The generated record has no claim-level quantity evidence. Source URLs or historical import notes are useful provenance but do not bind an excerpt, denominator and chemical form to each amount. Follow-up should attach source evidence at each corrected ingredient or stock and preparation claim.

### Source accessions, CultureMech IDs and merged variants

identity: concern. Targets: CultureMech:000848.

The target CultureMech:000848/media term mediadive.medium:1388 resolve to 15% MGM; synonym mediadive.medium:1339 and parent CultureMech:000796 resolve to 10% MGM in the captured other owner and official sources. The parent path and both merged_from entries resolve. The two source recipes differ in stock dose and preparation, so SOURCE_DUPLICATE and synonym equivalence are false for these formulations.

### Primary source and API disagreements

evidence: concern. Targets: CultureMech:000848.

Both PDFs were read as text and visually rendered. Their magnesium-salt spelling is MgSO2 and calcium stock is CaCl 1M; API stock 2686 instead specifies MgSO4 heptahydrate and CaCl2. Both PDFs list 1000 mL stock water; APIs use 995 mL plus the 5 mL calcium stock. PDF 1388 and its API also disagree on the stock Tris reagent. These are source conflicts requiring explicit curation, not evidence that the encoded salts are chemically nonexistent.

### ingredients[0].concentration

quantity: supported. Targets: CultureMech:000848.

Peptone 5 g/L agrees with the 15% recipe 5 g per 1000 mL final medium and API. Preserve the source Difco qualifier, which is omitted from the target. The 10% PDF has the same mass but a less explicit water denominator; its nominal g/L interpretation is supplied by MediaDive.

### ingredients[1].concentration

quantity: supported. Targets: CultureMech:000848.

Yeast extract 1 g/L agrees with the 15% final-medium basis and API. This complex ingredient has no target ontology ID; a specific molecular composition is not implied. The 10% mass agrees, with its water-basis ambiguity retained separately.

### ingredients[2].concentration

quantity: supported. Targets: CultureMech:000848.

Agar 20 g/L is supported for the optional solid-medium variant. SOLID_AGAR together with the dose and conditional ingredient note explicitly selects that option. Retain the condition and do not infer that the source also requires agar for broth.

### ingredients[3].concentration

quantity: concern. Targets: CultureMech:000848.

Target NaCl 240 g/L is the API stock concentration, not the final 15% medium value. Under API stock volume 1 L, multiply by 0.500 L stock / 1.000 L final medium to derive 120 g/L. Preserve the stock amount and dose separately; the PDF stock-water wording and magnesium formula conflict must not be erased.

### ingredients[4].concentration

quantity: concern. Targets: CultureMech:000848.

Target KCl 7 g/L is the API stock concentration, not the final 15% medium value. Under API stock volume 1 L, multiply by 0.500 L stock / 1.000 L final medium to derive 3.5 g/L. Preserve the stock amount and dose separately; the PDF stock-water wording and magnesium formula conflict must not be erased.

### ingredients[5].concentration

quantity: concern. Targets: CultureMech:000848.

Target MgCl2 hexahydrate 30 g/L is the API stock concentration, not the final 15% medium value. Under API stock volume 1 L, multiply by 0.500 L stock / 1.000 L final medium to derive 15 g/L. Preserve the stock amount and dose separately; the PDF stock-water wording and magnesium formula conflict must not be erased.

### ingredients[6].concentration

quantity: concern. Targets: CultureMech:000848.

Target MgSO4 heptahydrate 35 g/L is the API stock concentration, not the final 15% medium value. Under API stock volume 1 L, multiply by 0.500 L stock / 1.000 L final medium to derive 17.5 g/L. Preserve the stock amount and dose separately; the PDF stock-water wording and magnesium formula conflict must not be erased.

### ingredients[7].concentration

quantity: concern. Targets: CultureMech:000848.

Target CaCl2 0.5549 g/L copies the API stock solute equivalent. Source addition is 5 mL of 1 M calcium stock: 0.005 L × 1 mol/L = 0.005 mol. With API salt-stock volume 1 L and the 500 mL main dose, final calcium is 2.5 mmol/L or about 0.27746 g/L CaCl2 equivalent using 110.984 g/mol. This is not a weighed 0.5549 g final-medium ingredient or evidence for a particular starting hydrate.

### solutions (missing stock addition)

quantity: concern. Targets: CultureMech:000848.

15% MGM requires 500 mL salt stock in the final 1000 mL medium. The target contains no solution descriptor or preparation-volume instruction encoding this dose. A direct ingredient list at stock strength cannot substitute for it.

### parent_media and synonym formulation basis

quantity: concern. Targets: CultureMech:000848.

10% MGM requires 333.33 mL salt stock, rather than 500 mL. The API assigns final volume 1000 mL, implying a stock dilution factor 0.33333; the primary 10% PDF only lists 1000 mL water, so that exact denominator is not independently established by its wording. This uncertainty does not make the two prescribed stock doses equivalent.

### ingredients / solutions / preparation_steps water basis

quantity: concern. Targets: CultureMech:000848.

15% main-volume instruction is explicitly make up to 1000 mL. For the stock, the PDF 1000 mL water and API 995 mL water plus 5 mL calcium solution are inconsistent descriptions. No target water or preparation-volume field retains either basis. Preserve source statements; do not silently add all water volumes or assert a precise final stock volume from the PDF.

### preparation_steps[0:2]

quantity: concern. Targets: CultureMech:000848.

Neither source provides a volume of Tris titrant, only reagent molarity and pH endpoint. Main 15% medium uses 1 M Tris-base to pH 7.0; its PDF stock uses 1 M Tris-HCl to pH 7.5. The target/API stock instead says 2 M Tris-base. The 10% PDF specifies 2 M Tris-base for both scoped adjustments. No titrant mass or final concentration can be calculated.

### Every asserted CHEBI and MIM identifier

grounding: supported. Targets: CultureMech:000848.

All six target CHEBI terms and six identical MIM CHEBI links match the encoded names/forms and resolve in official ChEBI; the pinned index contains all six. Magnesium hydrate identity is preserved, and calcium is anhydrous solute identity rather than a specified weighed solid. Peptone and yeast extract have no ontology assertions. Media/source and local parent IDs were independently resolved; no DOI, PMID, taxon or gene identifier is asserted.

### Main medium versus stock preparation

consistency: concern. Targets: CultureMech:000848.

pH 7.0 is supported for the main medium and pH 7.5 for the separate stock. Flattening both paragraphs into one sequential main-medium preparation obscures that distinction and appears to readjust the finished medium. Autoclaving is source-supported, but neither PDF states temperature or duration. The 15% stock reagent disagrees with the target and shared API stock.

### Complexity, optional physical state and high_metal

consistency: supported. Targets: CultureMech:000848.

COMPLEX/UNDEFINED agree with peptone and yeast extract. SOLID_AGAR is supportable for an explicitly selected agar variant. high_metal is not disproved by dilution: under the API 1 L stock basis, NaCl alone gives 4106.78 mmol/L × 0.5 = 2053.39 mM sodium, above the schema threshold 1049.84 mM. This is qualified classification support, not a verified complete total or metal-toxicity claim; recompute after correcting source-volume representation.

### Embedded history, maintained inputs and generator behavior

provenance: concern. Targets: CultureMech:000848.

Both owners carry the same flattened stock amounts and retain different main-medium preparation text. The target August merge calls them duplicates, but that event is not scientific evidence. June MIM migration copied the ingredient CHEBI keys; current independent checks support those links only. Current formulation grouping rejects mismatching scientific fields, while legacy ingredient-set fingerprinting ignores doses. No historical cause beyond the observed stored data is asserted.

## Findings

### f1: Distinct 10% and 15% MGM formulations are merged as source duplicates

blocker / open / confirmed; issue key: mgm10-15-false-duplicate.

DSMZ 1339 and 1388 use different salt-stock volumes and main adjustment reagents. The target presents 10% MGM as a synonym and parent SOURCE_DUPLICATE of 15% MGM. Shared ingredient signatures and copied stock concentrations do not establish formulation identity.

### f2: Salt-stock concentrations are represented as final-medium amounts

major / open / confirmed; issue key: mgm-stock-flattening.

The five salt rows retain the undiluted stock values, while the 500 mL stock dose, parent stock, water basis and calcium solution strength are absent from structured preparation. The generated formulation therefore encodes the wrong main-medium concentrations and cannot be reconstructed faithfully. Both maintained owners share this defect.

### f3: Stock pH adjustment is both mis-scoped and inconsistent with DSMZ 1388

major / open / confirmed; issue key: mgm-stock-preparation-conflict.

The target applies the stock pH 7.5 paragraph as an unscoped second main preparation step and says 2 M Tris-base. The current DSMZ 1388 PDF specifies 1 M Tris-HCl for the stock, unlike the shared API stock and DSMZ 1339. These distinctions affect both reagent identity and preparation.

### f4: Chemical spelling and water normalization conflicts are hidden

major / open / confirmed; issue key: mgm-unrecorded-source-normalization.

The target cites the DSMZ PDF but silently follows API interpretations of MgSO2 as MgSO4 heptahydrate and CaCl as calcium chloride, plus API stock-volume normalization. The PDFs and API are not identical sources. Correct encoded CHEBI identities cannot resolve the primary transcription or denominator ambiguity.

## Recommended Actions And Acceptance Checks

### a1

Correct both normalized MGM owners and their variant relationships to preserve distinct formulations, then regenerate with formulation-aware grouping. Retain source identities and document a concentration variant relationship supported by the recipes rather than source-duplicate equivalence.

- DSMZ 1339 and 1388 remain distinct with their respective 333.33 mL and 500 mL stock additions.
- No synonym or SOURCE_DUPLICATE assertion conflates the two formulations.
- Run documented target validators, relationship checks and the appropriate full regeneration/ID/product gates after authorized curation.

### a2

Represent the Salt Water Solution separately from main ingredients, including its own composition and calcium-stock addition. Retain each variant dose and explicit source volume wording; derive final amounts only with a documented denominator. Update maintained owners before regeneration.

- 15% main mixture includes 500 mL stock and make-up to 1000 mL; 10% retains its distinct dose and volume limitation.
- Under the explicitly adopted API 1 L stock basis, derived 15% salt equivalents are 120, 3.5, 15, 17.5 and about 0.27746 g/L; these are derivations, not substitute primary-source weighings.
- No undiluted stock dose is silently exported as a final-medium quantity; recompute derived classifications afterward.

### a3

Scope each pH adjustment and autoclaving step to main medium or stock. Preserve the primary/API disagreement explicitly and support any chosen 15% stock instruction with its exact source; do not reuse the 10% instruction without qualification.

- Main pH 7.0 and stock pH 7.5 belong to separate preparation objects.
- The 15% stock 1 M Tris-HCl statement and conflicting API 2 M Tris-base statement remain traceable until resolved.
- No titrant volume, autoclave duration or temperature is invented.

### a4

Attach claim-level primary and API evidence to the corrected stock and document the spelling/volume interpretations and unresolved conflicts. Seek an unambiguous exact-source corroboration before treating a primary typo correction as verified; preserve original wording in provenance.

- MgSO2 versus MgSO4, CaCl versus CaCl2 and 1000 mL versus 995 mL stock-water differences are explicitly attributed.
- Neither a hydrate nor an exact stock denominator is silently inferred from ambiguous text.
- Narrow evidence binds each retained amount and form to the source or documented arithmetic that supports it.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/15_mgm_medium.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/10_mgm_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/15_mgm_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/15_mgm_medium.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/15_mgm_medium.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch002/020/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-002/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch002/020/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/15_mgm_medium.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/15_mgm_medium.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| bounded-search | data/merge_yaml/merged/15_mgm_medium.yaml; Whole target and named normalized owners; explicit-file rg --no-ignore --hidden search plus full YAML reads | context_only | Checked ingredient names, identifiers, stock and source fields, pH, growth conditions, evidence, references and history in every selected file. Ignored files were included through explicit file arguments. Absence statements in this review concern those records only; this was not a corpus-wide claim that no supporting material exists. |
| merge-owner | src/culturemech/merge/formulation.py; formulation_content, FormulationFingerprinter and merge_formulation_evidence; matcher.group_formulations and merger.merge_group | context_only | Current generator requires equality of scientific formulation fields and preserves scoped evidence; ingredient-set similarity alone is not proof of interchangeable formulations. A future correction belongs in normalized owners followed by reviewed regeneration. Current code was inspected without executing regeneration. |
| dsmz1339 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1339.pdf; Page 1: title, Mineral Salts Solution, Salt Water Solution and both preparation paragraphs | supports | The primary one-page 10% MGM recipe specifies a 333.33 mL salt-stock addition; its main medium uses 2 M Tris-base at pH 7.0. Its lower table is a separate 30% stock, adjusted to pH 7.5 with 2 M Tris-base. |
| dsmz1388 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1388.pdf; Page 1: title, both formulation tables and both preparation paragraphs | supports | The primary one-page 15% MGM recipe specifies a 500 mL salt-stock addition and an explicit 1000 mL final main-medium volume. Main adjustment uses 1 M Tris-base; the separate stock uses 1 M Tris-HCl at pH 7.5. |
| api1339 | https://mediadive.dsmz.de/rest/medium/1339; data.medium and data.solutions[0:2], including recipe and steps | supports | DSMZ MediaDive resolves medium 1339, main solution 2685 and salt stock 2686. It preserves the 333.33 mL stock dose and distinguishes main from stock ingredients, while assigning each solution volume 1000 mL. |
| api1388 | https://mediadive.dsmz.de/rest/medium/1388; data.medium and data.solutions[0:2], including recipe and steps | supports | MediaDive resolves medium 1388, main solution 2817 and shared salt stock 2686. It preserves the 500 mL dose and stock amounts, but reuses stock instructions from 1339 that conflict with the 1388 PDF. It normalizes formula spellings and stock water volume without explaining those differences. |
| chebi-2509 | https://www.ebi.ac.uk/chebi/CHEBI:2509; ChEBI Name, definition, formula and ontology relationships | supports | CHEBI:2509 is agar, a polysaccharide mixture; target term and MIM label match. |
| chebi-26710 | https://www.ebi.ac.uk/chebi/CHEBI:26710; ChEBI Name, definition, formula and ontology relationships | supports | CHEBI:26710 is sodium chloride, Cl.Na; target term and MIM label match. |
| chebi-32588 | https://www.ebi.ac.uk/chebi/CHEBI:32588; ChEBI Name, definition, formula and ontology relationships | supports | CHEBI:32588 is potassium chloride, Cl.K; target term and MIM label match. |
| chebi-86345 | https://www.ebi.ac.uk/chebi/CHEBI:86345; ChEBI Name, definition, formula and ontology relationships | supports | CHEBI:86345 is magnesium dichloride hexahydrate, 2Cl.6H2O.Mg; target term and MIM label preserve the hydrate. |
| chebi-31795 | https://www.ebi.ac.uk/chebi/CHEBI:31795; ChEBI Name, definition, formula and ontology relationships | supports | CHEBI:31795 is magnesium sulfate heptahydrate, 7H2O.Mg.O4S; target term and MIM label match the encoded form and API interpretation, but not the literal PDF MgSO2 spelling. |
| chebi-3312 | https://www.ebi.ac.uk/chebi/CHEBI:3312; ChEBI Name, definition, formula and ontology relationships | supports | CHEBI:3312 is calcium dichloride, Ca.2Cl, average mass 110.984. Target term and MIM label match the API solute form; the PDF abbreviates the calcium stock without specifying a starting-solid hydrate. |
| mim-index | src/culturemech/data/mediaingredientmech/label_index.csv; Exact entries for the six target CHEBI links; metadata pinned in source.inputs | supports | All six target mediaingredientmech_chebi_term identifiers occur in the pinned index as mapped unique entries with compatible substance identities. This supports linkage only, not amount, stock placement or source fidelity. |
| importer | src/culturemech/import/mediadive_importer.py; _parse_api_composition, _parse_api_solutions and _parse_preparation_steps | context_only | The current importer restricts direct ingredient parsing to the first solution and has a stock-reference path, while preparation steps still aggregate text from all solutions without retaining the source solution association. The present owner/target contain flattened historical data. The current code was inspected, not executed or asserted to reproduce the historical event. |
| fingerprint | src/culturemech/merge/fingerprint.py; RecipeFingerprinter.fingerprint and _extract_signatures | context_only | The ingredient-set key intentionally ignores quantities and conditions. Current formulation.py and the merge entrypoint distinguish this candidate key from exact formulation grouping; the old merged fingerprint therefore proves neither scientific equivalence nor current regeneration behavior. |
| high-metal-definition | src/culturemech/schema/culturemech.yaml; MediaRecipe.high_metal description | context_only | high_metal denotes total included-metal concentration at least 1049.84 mM; sodium is one included element. This is a schema-defined classification, not a toxicity or growth claim. |

## Limits And Additional Notes

- The PDFs visibly print MgSO2 x 7 H2O and CaCl 1M, while MediaDive interprets magnesium sulfate heptahydrate and 1 M calcium chloride. This review verifies that conflict without silently correcting the primary source.
- DSMZ 1339 lists 1000 mL water without explicitly saying final volume; DSMZ 1388 explicitly makes the main mixture up to 1000 mL. Both PDFs list 1000 mL stock water, whereas the APIs give 995 mL water plus 5 mL calcium stock and a nominal 1000 mL stock volume. Derived concentrations below use the stated MediaDive basis and are not an assertion that every PDF water convention is resolved.
- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.
- Embedded curation_history was read and compared with present target and owner bytes. Historical assertions are not retroactively certified; no history edits, status promotion or experimental verification were performed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T233801Z-culturemech-000848-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 15_mgm_medium (CultureMech:000848)'
started_at: '2026-10-19T23:30:32Z'
finished_at: '2026-10-19T23:38:01Z'
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
summary: The record merges distinct DSMZ 10% and 15% MGM recipes after flattening
  their shared salt stock into undiluted final-medium amounts. Both source identities
  resolve, but their stock doses and preparation differ. Primary PDF and MediaDive
  disagreements must remain explicit. The review is complete with a blocking identity
  defect and additional quantity, preparation and provenance findings.
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
  - path: data/merge_yaml/merged/15_mgm_medium.yaml
    sha256: 8dc3e6b51af4e083adeff2ce1a4ef53e7a2d86d946e68829cc69e43f54ba3841
    role: target
  - path: data/normalized_yaml/bacterial/10_mgm_medium.yaml
    sha256: f6d0aebf8d2c23eccc21c23ba0cf34152bcae8e5fa1adacfce615e0eb4e74150
    role: context
  - path: data/normalized_yaml/bacterial/15_mgm_medium.yaml
    sha256: 9c48897c64bcef15af59b525aab68ed3bb95c6a654092d0d400aa86b7224859c
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
  - path: scripts/normalize_media_names_to_snake_case.py
    sha256: 59bd842b1982b7d62af9db3fe280df576d8c4ae2e9ee411bf2e52523355f95de
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
  selection: Record 20 in Python lexicographic repository-relative path order of the
    initially uncovered merged corpus; batch 002 covers ordinals 11–20 after batch
    001. On fresh origin/main at this batch base, scripts/record_review.py list validated
    34 existing bundles and none listed this target path or ID. This bundle selects
    only the named record; no sampling or fleet-wide scientific claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:000848
targets:
- target_id: CultureMech:000848
  path: data/merge_yaml/merged/15_mgm_medium.yaml
  label: 15_mgm_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/10_mgm_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/15_mgm_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/15_mgm_medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:000848
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/15_mgm_medium.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch002/020/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-002/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch002/020/strict.tsv"
  target_ids:
  - CultureMech:000848
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/15_mgm_medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:000848
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/15_mgm_medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:000848
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
  - CultureMech:000848
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/15_mgm_medium.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-19T23:36:44Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/10_mgm_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-19T23:36:44Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/15_mgm_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-19T23:36:44Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/15_mgm_medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-19T23:32:18.457931Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/15_mgm_medium.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch002/020/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-19T23:32:20.075402Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-002/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch002/020/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/15_mgm_medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-19T23:32:22.387277Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/15_mgm_medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-19T23:32:23.536351Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: bounded-search
  kind: search
  reference: data/merge_yaml/merged/15_mgm_medium.yaml
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
- evidence_id: dsmz1339
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1339.pdf
  locator: 'Page 1: title, Mineral Salts Solution, Salt Water Solution and both preparation
    paragraphs'
  accessed_at: '2026-10-19T23:29:39Z'
  support: supports
  summary: The primary one-page 10% MGM recipe specifies a 333.33 mL salt-stock addition;
    its main medium uses 2 M Tris-base at pH 7.0. Its lower table is a separate 30%
    stock, adjusted to pH 7.5 with 2 M Tris-base.
  snapshot_sha256: 637304d4494f898e2b54705b6fbd4db1a70a848682e4455bdb64357fb81c1715
- evidence_id: dsmz1388
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1388.pdf
  locator: 'Page 1: title, both formulation tables and both preparation paragraphs'
  accessed_at: '2026-10-19T23:29:39Z'
  support: supports
  summary: The primary one-page 15% MGM recipe specifies a 500 mL salt-stock addition
    and an explicit 1000 mL final main-medium volume. Main adjustment uses 1 M Tris-base;
    the separate stock uses 1 M Tris-HCl at pH 7.5.
  snapshot_sha256: 362f1d9be32a2597dfcb199dfde9f35285edec742a6a3c3bacb22ea45d66c6dc
- evidence_id: api1339
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1339
  locator: data.medium and data.solutions[0:2], including recipe and steps
  accessed_at: '2026-10-19T23:29:39Z'
  support: supports
  summary: DSMZ MediaDive resolves medium 1339, main solution 2685 and salt stock
    2686. It preserves the 333.33 mL stock dose and distinguishes main from stock
    ingredients, while assigning each solution volume 1000 mL.
  snapshot_sha256: facfb22242b9f9f0b3d7ff1ee2cfee53d64e8cba1f26c494a64b00c168eefb64
- evidence_id: api1388
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/1388
  locator: data.medium and data.solutions[0:2], including recipe and steps
  accessed_at: '2026-10-19T23:29:39Z'
  support: supports
  summary: MediaDive resolves medium 1388, main solution 2817 and shared salt stock
    2686. It preserves the 500 mL dose and stock amounts, but reuses stock instructions
    from 1339 that conflict with the 1388 PDF. It normalizes formula spellings and
    stock water volume without explaining those differences.
  snapshot_sha256: 9fd7113348dcb50344bd5e520f3e31c1b9e33ec7fd6ecdc01404bf49bed3da38
- evidence_id: chebi-2509
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:2509
  locator: ChEBI Name, definition, formula and ontology relationships
  accessed_at: '2026-10-19T23:32:11.347108Z'
  support: supports
  summary: CHEBI:2509 is agar, a polysaccharide mixture; target term and MIM label
    match.
  snapshot_sha256: fdf12a8280861ef7a97ff6940adfaeba3e1bbe69671dbc1e4ee58869fc4f6bd3
- evidence_id: chebi-26710
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:26710
  locator: ChEBI Name, definition, formula and ontology relationships
  accessed_at: '2026-10-19T23:32:12.913708Z'
  support: supports
  summary: CHEBI:26710 is sodium chloride, Cl.Na; target term and MIM label match.
  snapshot_sha256: 20d037f64aa7b26b83d04556c47a29bc5d4808bbdf7d25027e18ad22a5c5f02f
- evidence_id: chebi-32588
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:32588
  locator: ChEBI Name, definition, formula and ontology relationships
  accessed_at: '2026-10-19T23:32:12.858281Z'
  support: supports
  summary: CHEBI:32588 is potassium chloride, Cl.K; target term and MIM label match.
  snapshot_sha256: 135d8318fe8cde9dc1b0ead7c50c12650a3d09d69cf4aa8541a1da01fc7abdce
- evidence_id: chebi-86345
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:86345
  locator: ChEBI Name, definition, formula and ontology relationships
  accessed_at: '2026-10-19T23:32:17.170913Z'
  support: supports
  summary: CHEBI:86345 is magnesium dichloride hexahydrate, 2Cl.6H2O.Mg; target term
    and MIM label preserve the hydrate.
  snapshot_sha256: d062e9207108ff5bf00ad827c62bf1d0dbec89095cc819ae88092349d82a7797
- evidence_id: chebi-31795
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:31795
  locator: ChEBI Name, definition, formula and ontology relationships
  accessed_at: '2026-10-19T23:32:12.808273Z'
  support: supports
  summary: CHEBI:31795 is magnesium sulfate heptahydrate, 7H2O.Mg.O4S; target term
    and MIM label match the encoded form and API interpretation, but not the literal
    PDF MgSO2 spelling.
  snapshot_sha256: 3ce9de4739bdf41bafd0b99fb9db23c45dfe90cf5ccc0ac3f59e5b2e351f8981
- evidence_id: chebi-3312
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:3312
  locator: ChEBI Name, definition, formula and ontology relationships
  accessed_at: '2026-10-19T23:32:19.179614Z'
  support: supports
  summary: CHEBI:3312 is calcium dichloride, Ca.2Cl, average mass 110.984. Target
    term and MIM label match the API solute form; the PDF abbreviates the calcium
    stock without specifying a starting-solid hydrate.
  snapshot_sha256: 44c71301c55f2a281eb5df66c3a53c281d48cf770d3b553e24cafd42a7b2f99f
- evidence_id: mim-index
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Exact entries for the six target CHEBI links; metadata pinned in source.inputs
  accessed_at: '2026-10-19T23:36:44Z'
  support: supports
  summary: All six target mediaingredientmech_chebi_term identifiers occur in the
    pinned index as mapped unique entries with compatible substance identities. This
    supports linkage only, not amount, stock placement or source fidelity.
- evidence_id: importer
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition, _parse_api_solutions and _parse_preparation_steps
  accessed_at: '2026-10-19T23:36:44Z'
  support: context_only
  summary: The current importer restricts direct ingredient parsing to the first solution
    and has a stock-reference path, while preparation steps still aggregate text from
    all solutions without retaining the source solution association. The present owner/target
    contain flattened historical data. The current code was inspected, not executed
    or asserted to reproduce the historical event.
- evidence_id: fingerprint
  kind: record_content
  reference: src/culturemech/merge/fingerprint.py
  locator: RecipeFingerprinter.fingerprint and _extract_signatures
  accessed_at: '2026-10-19T23:36:44Z'
  support: context_only
  summary: The ingredient-set key intentionally ignores quantities and conditions.
    Current formulation.py and the merge entrypoint distinguish this candidate key
    from exact formulation grouping; the old merged fingerprint therefore proves neither
    scientific equivalence nor current regeneration behavior.
- evidence_id: high-metal-definition
  kind: record_content
  reference: src/culturemech/schema/culturemech.yaml
  locator: MediaRecipe.high_metal description
  accessed_at: '2026-10-19T23:36:44Z'
  support: context_only
  summary: high_metal denotes total included-metal concentration at least 1049.84
    mM; sodium is one included element. This is a schema-defined classification, not
    a toxicity or growth claim.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:000848
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
  - CultureMech:000848
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
  - CultureMech:000848
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
  - CultureMech:000848
  evidence_ids:
  - record
  - bounded-search
  - validate-references
- assessment_id: identity
  area: identity
  topic: Source accessions, CultureMech IDs and merged variants
  outcome: concern
  summary: The target CultureMech:000848/media term mediadive.medium:1388 resolve
    to 15% MGM; synonym mediadive.medium:1339 and parent CultureMech:000796 resolve
    to 10% MGM in the captured other owner and official sources. The parent path and
    both merged_from entries resolve. The two source recipes differ in stock dose
    and preparation, so SOURCE_DUPLICATE and synonym equivalence are false for these
    formulations.
  target_ids:
  - CultureMech:000848
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz1339
  - dsmz1388
  - api1339
  - api1388
- assessment_id: source-transcription
  area: evidence
  topic: Primary source and API disagreements
  outcome: concern
  summary: Both PDFs were read as text and visually rendered. Their magnesium-salt
    spelling is MgSO2 and calcium stock is CaCl 1M; API stock 2686 instead specifies
    MgSO4 heptahydrate and CaCl2. Both PDFs list 1000 mL stock water; APIs use 995
    mL plus the 5 mL calcium stock. PDF 1388 and its API also disagree on the stock
    Tris reagent. These are source conflicts requiring explicit curation, not evidence
    that the encoded salts are chemically nonexistent.
  target_ids:
  - CultureMech:000848
  evidence_ids:
  - dsmz1339
  - dsmz1388
  - api1339
  - api1388
  - chebi-31795
  - chebi-3312
- assessment_id: q-peptone
  area: quantity
  topic: ingredients[0].concentration
  outcome: supported
  summary: Peptone 5 g/L agrees with the 15% recipe 5 g per 1000 mL final medium and
    API. Preserve the source Difco qualifier, which is omitted from the target. The
    10% PDF has the same mass but a less explicit water denominator; its nominal g/L
    interpretation is supplied by MediaDive.
  target_ids:
  - CultureMech:000848
  evidence_ids:
  - record
  - dsmz1388
  - api1388
  - dsmz1339
  - api1339
  dimensions:
  - name: decision
    value: retain 15% main-medium amount; preserve manufacturer qualifier and distinguish
      10% denominator
    definition: Claim-level quantity decision for the stated field; source amount,
      preparation basis and any derivation are distinguished.
    evidence_ids:
    - record
    - dsmz1388
    - api1388
    - dsmz1339
    - api1339
- assessment_id: q-yeast
  area: quantity
  topic: ingredients[1].concentration
  outcome: supported
  summary: Yeast extract 1 g/L agrees with the 15% final-medium basis and API. This
    complex ingredient has no target ontology ID; a specific molecular composition
    is not implied. The 10% mass agrees, with its water-basis ambiguity retained separately.
  target_ids:
  - CultureMech:000848
  evidence_ids:
  - record
  - dsmz1388
  - api1388
  - dsmz1339
  - api1339
  dimensions:
  - name: decision
    value: retain main-medium amount with exact variant source
    definition: Claim-level quantity decision for the stated field; source amount,
      preparation basis and any derivation are distinguished.
    evidence_ids:
    - record
    - dsmz1388
    - api1388
    - dsmz1339
    - api1339
- assessment_id: q-agar
  area: quantity
  topic: ingredients[2].concentration
  outcome: supported
  summary: Agar 20 g/L is supported for the optional solid-medium variant. SOLID_AGAR
    together with the dose and conditional ingredient note explicitly selects that
    option. Retain the condition and do not infer that the source also requires agar
    for broth.
  target_ids:
  - CultureMech:000848
  evidence_ids:
  - record
  - dsmz1388
  - dsmz1339
  - chebi-2509
  dimensions:
  - name: decision
    value: retain conditional agar dose and make chosen variant explicit
    definition: Claim-level quantity decision for the stated field; source amount,
      preparation basis and any derivation are distinguished.
    evidence_ids:
    - record
    - dsmz1388
    - dsmz1339
    - chebi-2509
- assessment_id: q-salt-3
  area: quantity
  topic: ingredients[3].concentration
  outcome: concern
  summary: Target NaCl 240 g/L is the API stock concentration, not the final 15% medium
    value. Under API stock volume 1 L, multiply by 0.500 L stock / 1.000 L final medium
    to derive 120 g/L. Preserve the stock amount and dose separately; the PDF stock-water
    wording and magnesium formula conflict must not be erased.
  target_ids:
  - CultureMech:000848
  evidence_ids:
  - record
  - dsmz1388
  - api1388
  - chebi-26710
  dimensions:
  - name: decision
    value: restore stock boundary; any final concentration is conditional arithmetic
    definition: Claim-level quantity decision for the stated field; source amount,
      preparation basis and any derivation are distinguished.
    evidence_ids:
    - record
    - dsmz1388
    - api1388
    - chebi-26710
- assessment_id: q-salt-4
  area: quantity
  topic: ingredients[4].concentration
  outcome: concern
  summary: Target KCl 7 g/L is the API stock concentration, not the final 15% medium
    value. Under API stock volume 1 L, multiply by 0.500 L stock / 1.000 L final medium
    to derive 3.5 g/L. Preserve the stock amount and dose separately; the PDF stock-water
    wording and magnesium formula conflict must not be erased.
  target_ids:
  - CultureMech:000848
  evidence_ids:
  - record
  - dsmz1388
  - api1388
  - chebi-32588
  dimensions:
  - name: decision
    value: restore stock boundary; any final concentration is conditional arithmetic
    definition: Claim-level quantity decision for the stated field; source amount,
      preparation basis and any derivation are distinguished.
    evidence_ids:
    - record
    - dsmz1388
    - api1388
    - chebi-32588
- assessment_id: q-salt-5
  area: quantity
  topic: ingredients[5].concentration
  outcome: concern
  summary: Target MgCl2 hexahydrate 30 g/L is the API stock concentration, not the
    final 15% medium value. Under API stock volume 1 L, multiply by 0.500 L stock
    / 1.000 L final medium to derive 15 g/L. Preserve the stock amount and dose separately;
    the PDF stock-water wording and magnesium formula conflict must not be erased.
  target_ids:
  - CultureMech:000848
  evidence_ids:
  - record
  - dsmz1388
  - api1388
  - chebi-86345
  dimensions:
  - name: decision
    value: restore stock boundary; any final concentration is conditional arithmetic
    definition: Claim-level quantity decision for the stated field; source amount,
      preparation basis and any derivation are distinguished.
    evidence_ids:
    - record
    - dsmz1388
    - api1388
    - chebi-86345
- assessment_id: q-salt-6
  area: quantity
  topic: ingredients[6].concentration
  outcome: concern
  summary: Target MgSO4 heptahydrate 35 g/L is the API stock concentration, not the
    final 15% medium value. Under API stock volume 1 L, multiply by 0.500 L stock
    / 1.000 L final medium to derive 17.5 g/L. Preserve the stock amount and dose
    separately; the PDF stock-water wording and magnesium formula conflict must not
    be erased.
  target_ids:
  - CultureMech:000848
  evidence_ids:
  - record
  - dsmz1388
  - api1388
  - chebi-31795
  dimensions:
  - name: decision
    value: restore stock boundary; any final concentration is conditional arithmetic
    definition: Claim-level quantity decision for the stated field; source amount,
      preparation basis and any derivation are distinguished.
    evidence_ids:
    - record
    - dsmz1388
    - api1388
    - chebi-31795
- assessment_id: q-calcium
  area: quantity
  topic: ingredients[7].concentration
  outcome: concern
  summary: 'Target CaCl2 0.5549 g/L copies the API stock solute equivalent. Source
    addition is 5 mL of 1 M calcium stock: 0.005 L × 1 mol/L = 0.005 mol. With API
    salt-stock volume 1 L and the 500 mL main dose, final calcium is 2.5 mmol/L or
    about 0.27746 g/L CaCl2 equivalent using 110.984 g/mol. This is not a weighed
    0.5549 g final-medium ingredient or evidence for a particular starting hydrate.'
  target_ids:
  - CultureMech:000848
  evidence_ids:
  - record
  - dsmz1388
  - api1388
  - chebi-3312
  dimensions:
  - name: decision
    value: represent molar calcium stock addition, its parent stock and final dose
      without hydrate inference
    definition: Claim-level quantity decision for the stated field; source amount,
      preparation basis and any derivation are distinguished.
    evidence_ids:
    - record
    - dsmz1388
    - api1388
    - chebi-3312
- assessment_id: q-dose15
  area: quantity
  topic: solutions (missing stock addition)
  outcome: concern
  summary: 15% MGM requires 500 mL salt stock in the final 1000 mL medium. The target
    contains no solution descriptor or preparation-volume instruction encoding this
    dose. A direct ingredient list at stock strength cannot substitute for it.
  target_ids:
  - CultureMech:000848
  evidence_ids:
  - record
  - dsmz1388
  - api1388
  - bounded-search
  dimensions:
  - name: decision
    value: restore 500 mL stock addition and final-volume instruction
    definition: Claim-level quantity decision for the stated field; source amount,
      preparation basis and any derivation are distinguished.
    evidence_ids:
    - record
    - dsmz1388
    - api1388
    - bounded-search
- assessment_id: q-dose10
  area: quantity
  topic: parent_media and synonym formulation basis
  outcome: concern
  summary: 10% MGM requires 333.33 mL salt stock, rather than 500 mL. The API assigns
    final volume 1000 mL, implying a stock dilution factor 0.33333; the primary 10%
    PDF only lists 1000 mL water, so that exact denominator is not independently established
    by its wording. This uncertainty does not make the two prescribed stock doses
    equivalent.
  target_ids:
  - CultureMech:000848
  evidence_ids:
  - record
  - owner-0
  - dsmz1339
  - api1339
  dimensions:
  - name: decision
    value: keep distinct 10% formulation with explicit source-volume limitation
    definition: Claim-level quantity decision for the stated field; source amount,
      preparation basis and any derivation are distinguished.
    evidence_ids:
    - record
    - owner-0
    - dsmz1339
    - api1339
- assessment_id: q-water
  area: quantity
  topic: ingredients / solutions / preparation_steps water basis
  outcome: concern
  summary: 15% main-volume instruction is explicitly make up to 1000 mL. For the stock,
    the PDF 1000 mL water and API 995 mL water plus 5 mL calcium solution are inconsistent
    descriptions. No target water or preparation-volume field retains either basis.
    Preserve source statements; do not silently add all water volumes or assert a
    precise final stock volume from the PDF.
  target_ids:
  - CultureMech:000848
  evidence_ids:
  - record
  - dsmz1388
  - dsmz1339
  - api1388
  - api1339
  - bounded-search
  dimensions:
  - name: decision
    value: retain primary batch-volume wording and API normalization as separately
      attributed
    definition: Claim-level quantity decision for the stated field; source amount,
      preparation basis and any derivation are distinguished.
    evidence_ids:
    - record
    - dsmz1388
    - dsmz1339
    - api1388
    - api1339
    - bounded-search
- assessment_id: q-tris
  area: quantity
  topic: preparation_steps[0:2]
  outcome: concern
  summary: Neither source provides a volume of Tris titrant, only reagent molarity
    and pH endpoint. Main 15% medium uses 1 M Tris-base to pH 7.0; its PDF stock uses
    1 M Tris-HCl to pH 7.5. The target/API stock instead says 2 M Tris-base. The 10%
    PDF specifies 2 M Tris-base for both scoped adjustments. No titrant mass or final
    concentration can be calculated.
  target_ids:
  - CultureMech:000848
  evidence_ids:
  - record
  - dsmz1388
  - dsmz1339
  - api1388
  - api1339
  dimensions:
  - name: decision
    value: restore source-specific adjustment reagent and scope; keep amount unspecified
    definition: Claim-level quantity decision for the stated field; source amount,
      preparation basis and any derivation are distinguished.
    evidence_ids:
    - record
    - dsmz1388
    - dsmz1339
    - api1388
    - api1339
- assessment_id: grounding
  area: grounding
  topic: Every asserted CHEBI and MIM identifier
  outcome: supported
  summary: All six target CHEBI terms and six identical MIM CHEBI links match the
    encoded names/forms and resolve in official ChEBI; the pinned index contains all
    six. Magnesium hydrate identity is preserved, and calcium is anhydrous solute
    identity rather than a specified weighed solid. Peptone and yeast extract have
    no ontology assertions. Media/source and local parent IDs were independently resolved;
    no DOI, PMID, taxon or gene identifier is asserted.
  target_ids:
  - CultureMech:000848
  evidence_ids:
  - record
  - mim-index
  - chebi-2509
  - chebi-26710
  - chebi-32588
  - chebi-86345
  - chebi-31795
  - chebi-3312
  - api1388
  - api1339
  - owner-0
  - owner-1
- assessment_id: preparation
  area: consistency
  topic: Main medium versus stock preparation
  outcome: concern
  summary: pH 7.0 is supported for the main medium and pH 7.5 for the separate stock.
    Flattening both paragraphs into one sequential main-medium preparation obscures
    that distinction and appears to readjust the finished medium. Autoclaving is source-supported,
    but neither PDF states temperature or duration. The 15% stock reagent disagrees
    with the target and shared API stock.
  target_ids:
  - CultureMech:000848
  evidence_ids:
  - record
  - dsmz1339
  - dsmz1388
  - api1388
  - importer
- assessment_id: classification
  area: consistency
  topic: Complexity, optional physical state and high_metal
  outcome: supported
  summary: 'COMPLEX/UNDEFINED agree with peptone and yeast extract. SOLID_AGAR is
    supportable for an explicitly selected agar variant. high_metal is not disproved
    by dilution: under the API 1 L stock basis, NaCl alone gives 4106.78 mmol/L ×
    0.5 = 2053.39 mM sodium, above the schema threshold 1049.84 mM. This is qualified
    classification support, not a verified complete total or metal-toxicity claim;
    recompute after correcting source-volume representation.'
  target_ids:
  - CultureMech:000848
  evidence_ids:
  - record
  - dsmz1388
  - api1388
  - chebi-26710
  - high-metal-definition
- assessment_id: history
  area: provenance
  topic: Embedded history, maintained inputs and generator behavior
  outcome: concern
  summary: Both owners carry the same flattened stock amounts and retain different
    main-medium preparation text. The target August merge calls them duplicates, but
    that event is not scientific evidence. June MIM migration copied the ingredient
    CHEBI keys; current independent checks support those links only. Current formulation
    grouping rejects mismatching scientific fields, while legacy ingredient-set fingerprinting
    ignores doses. No historical cause beyond the observed stored data is asserted.
  target_ids:
  - CultureMech:000848
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - merge-owner
  - fingerprint
  - importer
findings:
- finding_id: f1
  issue_key: mgm10-15-false-duplicate
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Distinct 10% and 15% MGM formulations are merged as source duplicates
  description: DSMZ 1339 and 1388 use different salt-stock volumes and main adjustment
    reagents. The target presents 10% MGM as a synonym and parent SOURCE_DUPLICATE
    of 15% MGM. Shared ingredient signatures and copied stock concentrations do not
    establish formulation identity.
  target_ids:
  - CultureMech:000848
  field_paths:
  - merged_from
  - synonyms[0]
  - parent_media.relationship
  - variant_relationship
  - variant_modifications
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz1339
  - dsmz1388
  - api1339
  - api1388
  - fingerprint
  - merge-owner
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/10_mgm_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/15_mgm_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f2
  issue_key: mgm-stock-flattening
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Salt-stock concentrations are represented as final-medium amounts
  description: The five salt rows retain the undiluted stock values, while the 500
    mL stock dose, parent stock, water basis and calcium solution strength are absent
    from structured preparation. The generated formulation therefore encodes the wrong
    main-medium concentrations and cannot be reconstructed faithfully. Both maintained
    owners share this defect.
  target_ids:
  - CultureMech:000848
  field_paths:
  - ingredients[3].concentration
  - ingredients[4].concentration
  - ingredients[5].concentration
  - ingredients[6].concentration
  - ingredients[7].concentration
  - solutions
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz1388
  - api1388
  - dsmz1339
  - api1339
  - importer
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/10_mgm_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/15_mgm_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f3
  issue_key: mgm-stock-preparation-conflict
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Stock pH adjustment is both mis-scoped and inconsistent with DSMZ 1388
  description: The target applies the stock pH 7.5 paragraph as an unscoped second
    main preparation step and says 2 M Tris-base. The current DSMZ 1388 PDF specifies
    1 M Tris-HCl for the stock, unlike the shared API stock and DSMZ 1339. These distinctions
    affect both reagent identity and preparation.
  target_ids:
  - CultureMech:000848
  field_paths:
  - preparation_steps[0]
  - preparation_steps[1]
  - ph_value
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz1388
  - dsmz1339
  - api1388
  - importer
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/10_mgm_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/15_mgm_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f4
  issue_key: mgm-unrecorded-source-normalization
  category: provenance
  severity: major
  status: open
  certainty: confirmed
  title: Chemical spelling and water normalization conflicts are hidden
  description: The target cites the DSMZ PDF but silently follows API interpretations
    of MgSO2 as MgSO4 heptahydrate and CaCl as calcium chloride, plus API stock-volume
    normalization. The PDFs and API are not identical sources. Correct encoded CHEBI
    identities cannot resolve the primary transcription or denominator ambiguity.
  target_ids:
  - CultureMech:000848
  field_paths:
  - notes
  - ingredients[6]
  - ingredients[7]
  - references
  - solutions
  evidence_ids:
  - record
  - dsmz1388
  - dsmz1339
  - api1388
  - api1339
  - chebi-31795
  - chebi-3312
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/10_mgm_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/15_mgm_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Correct both normalized MGM owners and their variant relationships
    to preserve distinct formulations, then regenerate with formulation-aware grouping.
    Retain source identities and document a concentration variant relationship supported
    by the recipes rather than source-duplicate equivalence.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:000848
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/10_mgm_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/15_mgm_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - DSMZ 1339 and 1388 remain distinct with their respective 333.33 mL and 500 mL
    stock additions.
  - No synonym or SOURCE_DUPLICATE assertion conflates the two formulations.
  - Run documented target validators, relationship checks and the appropriate full
    regeneration/ID/product gates after authorized curation.
- action_id: a2
  description: Represent the Salt Water Solution separately from main ingredients,
    including its own composition and calcium-stock addition. Retain each variant
    dose and explicit source volume wording; derive final amounts only with a documented
    denominator. Update maintained owners before regeneration.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:000848
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/10_mgm_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/15_mgm_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - 15% main mixture includes 500 mL stock and make-up to 1000 mL; 10% retains its
    distinct dose and volume limitation.
  - Under the explicitly adopted API 1 L stock basis, derived 15% salt equivalents
    are 120, 3.5, 15, 17.5 and about 0.27746 g/L; these are derivations, not substitute
    primary-source weighings.
  - No undiluted stock dose is silently exported as a final-medium quantity; recompute
    derived classifications afterward.
- action_id: a3
  description: Scope each pH adjustment and autoclaving step to main medium or stock.
    Preserve the primary/API disagreement explicitly and support any chosen 15% stock
    instruction with its exact source; do not reuse the 10% instruction without qualification.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:000848
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/10_mgm_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/15_mgm_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - Main pH 7.0 and stock pH 7.5 belong to separate preparation objects.
  - The 15% stock 1 M Tris-HCl statement and conflicting API 2 M Tris-base statement
    remain traceable until resolved.
  - No titrant volume, autoclave duration or temperature is invented.
- action_id: a4
  description: Attach claim-level primary and API evidence to the corrected stock
    and document the spelling/volume interpretations and unresolved conflicts. Seek
    an unambiguous exact-source corroboration before treating a primary typo correction
    as verified; preserve original wording in provenance.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:000848
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/10_mgm_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/15_mgm_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - MgSO2 versus MgSO4, CaCl versus CaCl2 and 1000 mL versus 995 mL stock-water differences
    are explicitly attributed.
  - Neither a hydrate nor an exact stock denominator is silently inferred from ambiguous
    text.
  - Narrow evidence binds each retained amount and form to the source or documented
    arithmetic that supports it.
limitations:
- The PDFs visibly print MgSO2 x 7 H2O and CaCl 1M, while MediaDive interprets magnesium
  sulfate heptahydrate and 1 M calcium chloride. This review verifies that conflict
  without silently correcting the primary source.
- DSMZ 1339 lists 1000 mL water without explicitly saying final volume; DSMZ 1388
  explicitly makes the main mixture up to 1000 mL. Both PDFs list 1000 mL stock water,
  whereas the APIs give 995 mL water plus 5 mL calcium stock and a nominal 1000 mL
  stock volume. Derived concentrations below use the stated MediaDive basis and are
  not an assertion that every PDF water convention is resolved.
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
