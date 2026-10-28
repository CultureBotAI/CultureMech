# Source and formulation review: 15_mh_medium (CultureMech:001708)

- Review: 20261020T032925Z-culturemech-001708-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-19T23:40:50Z
- Finished UTC: 2026-10-20T03:29:25Z
- Reviewer: OpenAI Codex with delegated source and validator checks (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The selected liquid DSMZ 582 formulation is supported: all ten ingredient concentrations match the provider-declared main-recipe values, pH and bicarbonate handling agree, and all eight asserted chemical identities resolve. One minor provenance finding concerns maintained ingredient evidence omitted from this older generated record. No material formulation or grounding error was established.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Record 21 in Python lexicographic repository-relative path order of the initially uncovered merged corpus; Batch 003 selects ordinals 21-30 after the first two reserved batches; saved bundles are published locally in path order. On fresh origin/main at this batch base, scripts/record_review.py list validated 34 existing bundles and none listed this target path or ID. This bundle selects only the named record; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7c568537897ee4bba1b8e97f8172133c1572aec0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001708 | data/merge_yaml/merged/15_mh_medium.yaml | generated | 15_mh_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:001708 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:001708 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-003/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch003/021/strict.tsv |
| validate-terms | passed | True | CultureMech:001708 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:001708 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:001708 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:001708.

The four documented recipes completed; interpret the scope of each separately.

### One DSMZ medium and locally copied source duplicate

identity: supported. Targets: CultureMech:001708.

CultureMech:001708 identifies DSMZ 582, 15% MH MEDIUM. The linked CultureMech:006053 path resolves and its recorded DSMZ-copy relationship agrees with the actual ingredient inventory. Similar JCM formulations are not substituted.

### Every direct amount and source-only preparation quantity

quantity: supported. Targets: CultureMech:001708.

All 10/10 direct concentrations agree with explicit provider g_l values and source batch amounts. Optional agar and unquantified bicarbonate stock remain scoped separately.

ingredients[0].concentration (NaCl): verified 121.5 G_PER_L against MediaDive $.data.solutions[0].recipe[0].g_l=121.5; PDF batch amount 121.5 g. Provider volume=1000 mL; arithmetic 121.5 g/(1000/1000 L)=121.5 g/L. This is provider normalization, not a measured final-volume claim.
ingredients[1].concentration (MgCl2): verified 10.5 G_PER_L against MediaDive $.data.solutions[0].recipe[1].g_l=10.5; PDF batch amount 10.5 g. Provider volume=1000 mL; arithmetic 10.5 g/(1000/1000 L)=10.5 g/L. This is provider normalization, not a measured final-volume claim.
ingredients[2].concentration (MgSO4): verified 14.4 G_PER_L against MediaDive $.data.solutions[0].recipe[2].g_l=14.4; PDF batch amount 14.4 g. Provider volume=1000 mL; arithmetic 14.4 g/(1000/1000 L)=14.4 g/L. This is provider normalization, not a measured final-volume claim.
ingredients[3].concentration (CaCl2): verified 0.54 G_PER_L against MediaDive $.data.solutions[0].recipe[3].g_l=0.54; PDF batch amount 0.54 g. Provider volume=1000 mL; arithmetic 0.54 g/(1000/1000 L)=0.54 g/L. This is provider normalization, not a measured final-volume claim.
ingredients[4].concentration (KCl): verified 3 G_PER_L against MediaDive $.data.solutions[0].recipe[4].g_l=3; PDF batch amount 3 g. Provider volume=1000 mL; arithmetic 3 g/(1000/1000 L)=3 g/L. This is provider normalization, not a measured final-volume claim.
ingredients[5].concentration (NaHCO3): verified 0.09 G_PER_L against MediaDive $.data.solutions[0].recipe[5].g_l=0.09; PDF batch amount 0.09 g. Provider volume=1000 mL; arithmetic 0.09 g/(1000/1000 L)=0.09 g/L. This is provider normalization, not a measured final-volume claim.
ingredients[6].concentration (NaBr): verified 0.039 G_PER_L against MediaDive $.data.solutions[0].recipe[6].g_l=0.039; PDF batch amount 0.039 g. Provider volume=1000 mL; arithmetic 0.039 g/(1000/1000 L)=0.039 g/L. This is provider normalization, not a measured final-volume claim.
ingredients[7].concentration (Proteose peptone no. 3): verified 5 G_PER_L against MediaDive $.data.solutions[0].recipe[7].g_l=5; PDF batch amount 5 g. Provider volume=1000 mL; arithmetic 5 g/(1000/1000 L)=5 g/L. This is provider normalization, not a measured final-volume claim.
ingredients[8].concentration (Yeast extract): verified 10 G_PER_L against MediaDive $.data.solutions[0].recipe[8].g_l=10; PDF batch amount 10 g. Provider volume=1000 mL; arithmetic 10 g/(1000/1000 L)=10 g/L. This is provider normalization, not a measured final-volume claim.
ingredients[9].concentration (Glucose): verified 1 G_PER_L against MediaDive $.data.solutions[0].recipe[9].g_l=1; PDF batch amount 1 g. Provider volume=1000 mL; arithmetic 1 g/(1000/1000 L)=1 g/L. This is provider normalization, not a measured final-volume claim.
Source-only water: PDF and API specify 1000 mL distilled water. The generated solute list omits water and does not state batch volume. Preserve source water addition and its distinction from a final-volume instruction in future curation; the existing solute g/L values are independently supported by API, not refuted by this omission.
Bicarbonate stock: not_quantified for stock strength and addition volume; source specifies only the 0.09 g solute amount and addition after cooling. No structured solution reference or dose is asserted, so no broken-reference or missing dilution-factor finding is justified.
Optional solid branch: verified 20 g/L agar in source and preparation description. The selected LIQUID formulation validly excludes agar from ingredients. No mandatory agar addition or solid-state mismatch is inferred.

### Every asserted primary and MIM chemical identifier

grounding: supported. Targets: CultureMech:001708.

Eight primary CHEBI IDs and eight matching MIM CHEBI links resolve. MgCl2, MgSO4 and CaCl2 are represented without waters of crystallization, matching this DSMZ source wording. Glucose remains stereochemically unspecified. Proteose peptone and yeast extract are ungrounded mixtures, not falsely assigned pure-compound identities. Primary linkage coverage=8/10 ingredient instances (80%); MIM CHEBI linkage coverage=8/10 (80%); neither metric measures scientific accuracy.

### Preparation and physical state

representation: supported. Targets: CultureMech:001708.

pH 7.5 and cooled-medium addition of sterilized bicarbonate stock are retained. The first action MIX is a broad tag on a pH statement, not evidence for a separate mixing protocol. Source agar is conditional; LIQUID is supported. Sterilization temperature/time and bicarbonate stock concentration are not supplied by the inspected DSMZ source.

### Complex medium and growth scope

scope: supported. Targets: CultureMech:001708.

Peptone and yeast extract support COMPLEX/UNDEFINED. Microbial cultivation is a generic application, not a strain-growth claim. The record asserts no organism, incubation temperature, salinity class, yield or experimentally verified growth outcome; no organism inference is added from source database membership.

### Maintained evidence versus generated snapshot

provenance: concern. Targets: CultureMech:001708.

Generated ingredient rows and references omit eight claim-level evidence entries, their dataset citation and the October curation event present in the maintained DSMZ owner. The generated notes retain the authoritative PDF link, and all ten amounts were independently confirmed, so the gap is non-blocking provenance loss rather than unsupported chemistry.

### Native history and future edit ownership

ownership: supported. Targets: CultureMech:001708.

Target identity and merge history are coherent with the two named normalized sources. Target has no record-level REVIEWED status and no status promotion is proposed. Future edits belong in normalized sources; generated bundles must come through the merge pipeline. Ingredient quantities and IDs need no correction based on this review.

## Findings

### f1: Generated recipe omits maintained concentration evidence

minor / open / confirmed; issue key: culturemech-001708-generated-concentration-evidence-gap.

The normalized DSMZ owner has eight ingredient-level MediaDive excerpts, a dataset reference and an October evidence-curation event, while the target contains none of these additions and records an August merge. All ten amounts remain source-supported and the PDF link is retained; this is a bounded evidence-currentness gap. The comparison does not establish that current merge code would discard the evidence.

## Recommended Actions And Acceptance Checks

### a1

Retain the validated owner evidence and, in separately authorized curation, regenerate this target through the current merge pipeline. Inspect the output for the eight correctly scoped excerpts and dataset reference; fix a generator only if regeneration demonstrates evidence loss. Do not change the supported ingredient amounts.

- Compare regenerated target with the maintained owner: eight ingredient evidence entries and dataset citation retained at the original claim scope.
- Re-run the four documented target validation recipes; reference validation should examine the newly present excerpts.
- Run the documented merge-freshness and merge-verification gates after authorized regeneration; preserve immutable review bundles.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/15_mh_medium.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/15_mh_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/KOMODO_582_15_MH_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/15_mh_medium.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/15_mh_medium.yaml --workers 1 --out /private/tmp/culturemech-review-work-batch003/021/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-003/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work-batch003/021/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/15_mh_medium.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/15_mh_medium.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| dsmz | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium582.pdf; Page 1, complete recipe and preparation paragraph | supports | DSMZ medium 582 gives ten solutes, distilled water 1000 mL, pH 7.5, bicarbonate addition from a sterilized stock after cooling, and an optional solid variant with 20 g/L agar. It does not name hydrated magnesium/calcium salts. |
| api | https://mediadive.dsmz.de/rest/medium/582; $.data.medium and $.data.solutions[0] | supports | Medium accession 582, name and source link resolve. Main solution 1247 reports volume 1000 mL, ten explicit g_l values, a water row and two preparation steps. Its response SHA256 matches the October 7 capture cited by the maintained owner. |
| komodo | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; HTML table row with first-cell accession 582 | supports | Inspected row identifies 582 as 15% MH medium, pH 7.5, and links DSMZ_Medium582.pdf. Supports source accession correspondence; table flags are not evidence of strain growth or a chemically independent formulation. |
| chebi-17234 | https://www.ebi.ac.uk/chebi/CHEBI:17234; ChEBI ID, Name, Formula and chemical structure/form | supports | Inspected CHEBI:17234: glucose; formula C6H12O6. Supports the stored ID/label and supplied formula scope; unrelated ontology roles are not transferred to this medium. |
| chebi-26710 | https://www.ebi.ac.uk/chebi/CHEBI:26710; ChEBI ID, Name, Formula and chemical structure/form | supports | Inspected CHEBI:26710: sodium chloride; formula Cl.Na. Supports the stored ID/label and supplied formula scope; unrelated ontology roles are not transferred to this medium. |
| chebi-32139 | https://www.ebi.ac.uk/chebi/CHEBI:32139; ChEBI ID, Name, Formula and chemical structure/form | supports | Inspected CHEBI:32139: sodium hydrogencarbonate; formula CHO3.Na. Supports the stored ID/label and supplied formula scope; unrelated ontology roles are not transferred to this medium. |
| chebi-32588 | https://www.ebi.ac.uk/chebi/CHEBI:32588; ChEBI ID, Name, Formula and chemical structure/form | supports | Inspected CHEBI:32588: potassium chloride; formula Cl.K. Supports the stored ID/label and supplied formula scope; unrelated ontology roles are not transferred to this medium. |
| chebi-32599 | https://www.ebi.ac.uk/chebi/CHEBI:32599; ChEBI ID, Name, Formula and chemical structure/form | supports | Inspected CHEBI:32599: magnesium sulfate; formula Mg.O4S. Supports the stored ID/label and supplied formula scope; unrelated ontology roles are not transferred to this medium. |
| chebi-3312 | https://www.ebi.ac.uk/chebi/CHEBI:3312; ChEBI ID, Name, Formula and chemical structure/form | supports | Inspected CHEBI:3312: calcium dichloride; formula Ca.2Cl. Supports the stored ID/label and supplied formula scope; unrelated ontology roles are not transferred to this medium. |
| chebi-63004 | https://www.ebi.ac.uk/chebi/CHEBI:63004; ChEBI ID, Name, Formula and chemical structure/form | supports | Inspected CHEBI:63004: sodium bromide; formula Br.Na. Supports the stored ID/label and supplied formula scope; unrelated ontology roles are not transferred to this medium. |
| chebi-6636 | https://www.ebi.ac.uk/chebi/CHEBI:6636; ChEBI ID, Name, Formula and chemical structure/form | supports | Inspected CHEBI:6636: magnesium dichloride; formula 2Cl.Mg. Supports the stored ID/label and supplied formula scope; unrelated ontology roles are not transferred to this medium. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Exact source labels and eight asserted CHEBI keys; companion label_index.metadata.json | supports | All eight asserted MIM CHEBI keys have matching MAPPED rows for the exact ingredient label (MgSO4 is a synonym of Magnesium sulfate). Packaged snapshot source commit 6643131b0f12ab40b66f98135245fca04027e0e9, CSV SHA256 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5; metadata byte count and digest checked. Labels elsewhere in the index are not assumed chemically valid. |
| internal | data/normalized_yaml/bacterial/KOMODO_582_15_MH_medium.yaml; id, parent_media, ingredients and curation_history | supports | Full owner read confirms CultureMech:006053, reciprocal parent CultureMech:001708, identical ten ingredient identities and amounts, and an explicit DSMZ-copy history. Whole-checkout dependency discovery included ignored and hidden files. The child has an old malformed timestamp; it is not a timestamp asserted in the generated target and is not made a target defect. |
| merge | src/culturemech/merge/merger.py; merge_recipes canonical selection and merge_formulation_evidence call; formulation.py lines 92-126 | context_only | Current merge code delegates evidence preservation to merge_formulation_evidence. The generated record has August merge timestamps while its owner has October concentration-evidence curation. The byte difference is established; an execution trace proving a current generator defect was not performed. |

## Limits And Additional Notes

- The DSMZ PDF states 1000 mL distilled water, not a measured final volume; G_PER_L values are verified against the explicit MediaDive volume and g_l declarations, not inferred from water alone.
- The source does not specify bicarbonate stock strength, dose volume, sterilization cycle, incubation conditions or strain growth; no such details were invented.
- KOMODO accession identity is confirmed from its captured MediaList row and local duplicate lineage. This does not independently verify an external KOMODO ingredient inventory or its historical aerobic flag.
- A schema/term pass does not establish chemical identity, correct source quantities, or growth. Reference-check coverage must be read from its actual output; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T032925Z-culturemech-001708-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 15_mh_medium (CultureMech:001708)'
started_at: '2026-10-19T23:40:50Z'
finished_at: '2026-10-20T03:29:25Z'
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
summary: 'The selected liquid DSMZ 582 formulation is supported: all ten ingredient
  concentrations match the provider-declared main-recipe values, pH and bicarbonate
  handling agree, and all eight asserted chemical identities resolve. One minor provenance
  finding concerns maintained ingredient evidence omitted from this older generated
  record. No material formulation or grounding error was established.'
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
  - path: data/merge_yaml/merged/15_mh_medium.yaml
    sha256: 849e073209b96189a07a9ef4fd5d7c530e4a2791dd020c9a5d7b4e86b99bc55b
    role: target
  - path: data/normalized_yaml/bacterial/15_mh_medium.yaml
    sha256: 2242aae26037b0db2869f2fd6978ac4e65954e5499431e882c3c6b99407a500b
    role: context
  - path: data/normalized_yaml/bacterial/KOMODO_582_15_MH_medium.yaml
    sha256: 9ca9bd4420163df6d7dcc49e0ea8bbe0c2c9c78f471e868b8d258d16501e767d
    role: context
  - path: data/normalized_yaml/bacterial/mediadive_1247_Main_sol_582.yaml
    sha256: c5a7b2e876468103adb44c0d89530863c1f66487b914e5594ffc9229696e6dbd
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
  - path: scripts/apply_cocktail_nesting.py
    sha256: a1914a040ca02c86633aae11ed8a52a0ea91ba157a8240da2232c4ae652d61ab
    role: context
  - path: scripts/apply_mim_groundings.py
    sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
    role: context
  - path: scripts/fetch_mediadive_solution_volumes.py
    sha256: 408cdfa3f5c446e8f9c32ac98d7ea8a3a36553b23c032f3b7551f6a1661fd39a
    role: context
  - path: scripts/import_mediadive_solutions.py
    sha256: f97db7607d76c46b75d2d2428e8a425a5735e52beb3a9c28fd0af03ab5b31aa8
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
  - path: src/culturemech/convert/komodo_web_raw_yaml.py
    sha256: a1a37015b4e6bac657e49f375b39a319815cc6b02a02135674a858a8b6eab03a
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
  - path: src/culturemech/enrich/dsmz_resolver.py
    sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
    role: context
  - path: src/culturemech/fetch/komodo_web_fetcher.py
    sha256: 89c510caa08d989b7ec6cee9ac17cc2f0faab606fe8a29ca435df476e52ff004
    role: context
  - path: src/culturemech/fetch/mediadive_api_fetcher.py
    sha256: 60b15f231d96099bd76ff10bb215de2d0ca9ad71de5d7977b0054d1b7b622c5e
    role: context
  - path: src/culturemech/import/komodo_web_importer.py
    sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
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
  selection: Record 21 in Python lexicographic repository-relative path order of the
    initially uncovered merged corpus; Batch 003 selects ordinals 21-30 after the
    first two reserved batches; saved bundles are published locally in path order.
    On fresh origin/main at this batch base, scripts/record_review.py list validated
    34 existing bundles and none listed this target path or ID. This bundle selects
    only the named record; no sampling or fleet-wide scientific claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:001708
targets:
- target_id: CultureMech:001708
  path: data/merge_yaml/merged/15_mh_medium.yaml
  label: 15_mh_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/15_mh_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_582_15_MH_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/15_mh_medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:001708
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/15_mh_medium.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch003/021/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-003/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch003/021/strict.tsv"
  target_ids:
  - CultureMech:001708
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/15_mh_medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:001708
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/15_mh_medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:001708
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
  - CultureMech:001708
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/15_mh_medium.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-20T03:29:25Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/15_mh_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-20T03:29:25Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_582_15_MH_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-20T03:29:25Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/15_mh_medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-19T23:41:05.105230Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/15_mh_medium.yaml --workers
    1 --out /private/tmp/culturemech-review-work-batch003/021/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-19T23:41:09.676117Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019-batch-003/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work-batch003/021/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/15_mh_medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-19T23:41:14.597354Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/15_mh_medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-19T23:41:17.233565Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: dsmz
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium582.pdf
  locator: Page 1, complete recipe and preparation paragraph
  accessed_at: '2026-10-19T23:37:48.982194Z'
  support: supports
  summary: DSMZ medium 582 gives ten solutes, distilled water 1000 mL, pH 7.5, bicarbonate
    addition from a sterilized stock after cooling, and an optional solid variant
    with 20 g/L agar. It does not name hydrated magnesium/calcium salts.
  quote: Distilled water 1000.000 ml
  snapshot_sha256: 4cd11891f96451ec295499ab10bf261d44f07de0379c8f22c989c107f4940f8c
- evidence_id: api
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/582
  locator: $.data.medium and $.data.solutions[0]
  accessed_at: '2026-10-19T23:37:48.646702Z'
  support: supports
  summary: Medium accession 582, name and source link resolve. Main solution 1247
    reports volume 1000 mL, ten explicit g_l values, a water row and two preparation
    steps. Its response SHA256 matches the October 7 capture cited by the maintained
    owner.
  snapshot_sha256: 31f2b2c713e28b748dd847ae26f5a52fac186abd27616218f9eb9ed5b67fcbe7
- evidence_id: komodo
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: HTML table row with first-cell accession 582
  accessed_at: '2026-10-19T23:42:38.189631Z'
  support: supports
  summary: Inspected row identifies 582 as 15% MH medium, pH 7.5, and links DSMZ_Medium582.pdf.
    Supports source accession correspondence; table flags are not evidence of strain
    growth or a chemically independent formulation.
  snapshot_sha256: d8259d98e6dbffdf6961a1ab92bc86f3567d5d96de352bfa079edb2a91e9580a
- evidence_id: chebi-17234
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:17234
  locator: ChEBI ID, Name, Formula and chemical structure/form
  accessed_at: '2026-10-19T07:35:31.337539Z'
  support: supports
  summary: 'Inspected CHEBI:17234: glucose; formula C6H12O6. Supports the stored ID/label
    and supplied formula scope; unrelated ontology roles are not transferred to this
    medium.'
  snapshot_sha256: 79006ae44d9d794815f34092ca6407adc60ba22b5a269fbc4f69dce945aef797
- evidence_id: chebi-26710
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:26710
  locator: ChEBI ID, Name, Formula and chemical structure/form
  accessed_at: '2026-10-19T23:32:12.913708Z'
  support: supports
  summary: 'Inspected CHEBI:26710: sodium chloride; formula Cl.Na. Supports the stored
    ID/label and supplied formula scope; unrelated ontology roles are not transferred
    to this medium.'
  snapshot_sha256: 20d037f64aa7b26b83d04556c47a29bc5d4808bbdf7d25027e18ad22a5c5f02f
- evidence_id: chebi-32139
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:32139
  locator: ChEBI ID, Name, Formula and chemical structure/form
  accessed_at: '2026-10-19T07:35:41.058859Z'
  support: supports
  summary: 'Inspected CHEBI:32139: sodium hydrogencarbonate; formula CHO3.Na. Supports
    the stored ID/label and supplied formula scope; unrelated ontology roles are not
    transferred to this medium.'
  snapshot_sha256: 9c890ba478b78dfc699a10ead1ae2e71a5596286046d1ae6994b23aad7f69929
- evidence_id: chebi-32588
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:32588
  locator: ChEBI ID, Name, Formula and chemical structure/form
  accessed_at: '2026-10-19T23:32:12.858281Z'
  support: supports
  summary: 'Inspected CHEBI:32588: potassium chloride; formula Cl.K. Supports the
    stored ID/label and supplied formula scope; unrelated ontology roles are not transferred
    to this medium.'
  snapshot_sha256: 135d8318fe8cde9dc1b0ead7c50c12650a3d09d69cf4aa8541a1da01fc7abdce
- evidence_id: chebi-32599
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:32599
  locator: ChEBI ID, Name, Formula and chemical structure/form
  accessed_at: '2026-10-19T07:35:47.353697Z'
  support: supports
  summary: 'Inspected CHEBI:32599: magnesium sulfate; formula Mg.O4S. Supports the
    stored ID/label and supplied formula scope; unrelated ontology roles are not transferred
    to this medium.'
  snapshot_sha256: 3b05d10bdc37fe5074d0e91a3396d1c6f73224ed144ef845b501deaced552da2
- evidence_id: chebi-3312
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:3312
  locator: ChEBI ID, Name, Formula and chemical structure/form
  accessed_at: '2026-10-19T23:32:19.179614Z'
  support: supports
  summary: 'Inspected CHEBI:3312: calcium dichloride; formula Ca.2Cl. Supports the
    stored ID/label and supplied formula scope; unrelated ontology roles are not transferred
    to this medium.'
  snapshot_sha256: 44c71301c55f2a281eb5df66c3a53c281d48cf770d3b553e24cafd42a7b2f99f
- evidence_id: chebi-63004
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:63004
  locator: ChEBI ID, Name, Formula and chemical structure/form
  accessed_at: '2026-10-19T07:35:56.710059Z'
  support: supports
  summary: 'Inspected CHEBI:63004: sodium bromide; formula Br.Na. Supports the stored
    ID/label and supplied formula scope; unrelated ontology roles are not transferred
    to this medium.'
  snapshot_sha256: f7012f2d912509a901c06cc99442b4cf0e23a61065ecf429e8cb79ef4afba498
- evidence_id: chebi-6636
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:6636
  locator: ChEBI ID, Name, Formula and chemical structure/form
  accessed_at: '2026-10-19T07:36:00.250949Z'
  support: supports
  summary: 'Inspected CHEBI:6636: magnesium dichloride; formula 2Cl.Mg. Supports the
    stored ID/label and supplied formula scope; unrelated ontology roles are not transferred
    to this medium.'
  snapshot_sha256: a1764bd688049cd029c31189e9bdd0afcf268103cdfd9fec5ded83eb4b93c54a
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Exact source labels and eight asserted CHEBI keys; companion label_index.metadata.json
  accessed_at: '2026-10-20T03:29:25Z'
  support: supports
  summary: All eight asserted MIM CHEBI keys have matching MAPPED rows for the exact
    ingredient label (MgSO4 is a synonym of Magnesium sulfate). Packaged snapshot
    source commit 6643131b0f12ab40b66f98135245fca04027e0e9, CSV SHA256 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5;
    metadata byte count and digest checked. Labels elsewhere in the index are not
    assumed chemically valid.
- evidence_id: internal
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_582_15_MH_medium.yaml
  locator: id, parent_media, ingredients and curation_history
  accessed_at: '2026-10-20T03:29:25Z'
  support: supports
  summary: Full owner read confirms CultureMech:006053, reciprocal parent CultureMech:001708,
    identical ten ingredient identities and amounts, and an explicit DSMZ-copy history.
    Whole-checkout dependency discovery included ignored and hidden files. The child
    has an old malformed timestamp; it is not a timestamp asserted in the generated
    target and is not made a target defect.
- evidence_id: merge
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: merge_recipes canonical selection and merge_formulation_evidence call;
    formulation.py lines 92-126
  accessed_at: '2026-10-20T03:29:25Z'
  support: context_only
  summary: Current merge code delegates evidence preservation to merge_formulation_evidence.
    The generated record has August merge timestamps while its owner has October concentration-evidence
    curation. The byte difference is established; an execution trace proving a current
    generator defect was not performed.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:001708
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: One DSMZ medium and locally copied source duplicate
  outcome: supported
  summary: CultureMech:001708 identifies DSMZ 582, 15% MH MEDIUM. The linked CultureMech:006053
    path resolves and its recorded DSMZ-copy relationship agrees with the actual ingredient
    inventory. Similar JCM formulations are not substituted.
  target_ids:
  - CultureMech:001708
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz
  - api
  - komodo
  - internal
- assessment_id: amounts
  area: quantity
  topic: Every direct amount and source-only preparation quantity
  outcome: supported
  summary: All 10/10 direct concentrations agree with explicit provider g_l values
    and source batch amounts. Optional agar and unquantified bicarbonate stock remain
    scoped separately.
  target_ids:
  - CultureMech:001708
  evidence_ids:
  - record
  - dsmz
  - api
  details: 'ingredients[0].concentration (NaCl): verified 121.5 G_PER_L against MediaDive
    $.data.solutions[0].recipe[0].g_l=121.5; PDF batch amount 121.5 g. Provider volume=1000
    mL; arithmetic 121.5 g/(1000/1000 L)=121.5 g/L. This is provider normalization,
    not a measured final-volume claim.

    ingredients[1].concentration (MgCl2): verified 10.5 G_PER_L against MediaDive
    $.data.solutions[0].recipe[1].g_l=10.5; PDF batch amount 10.5 g. Provider volume=1000
    mL; arithmetic 10.5 g/(1000/1000 L)=10.5 g/L. This is provider normalization,
    not a measured final-volume claim.

    ingredients[2].concentration (MgSO4): verified 14.4 G_PER_L against MediaDive
    $.data.solutions[0].recipe[2].g_l=14.4; PDF batch amount 14.4 g. Provider volume=1000
    mL; arithmetic 14.4 g/(1000/1000 L)=14.4 g/L. This is provider normalization,
    not a measured final-volume claim.

    ingredients[3].concentration (CaCl2): verified 0.54 G_PER_L against MediaDive
    $.data.solutions[0].recipe[3].g_l=0.54; PDF batch amount 0.54 g. Provider volume=1000
    mL; arithmetic 0.54 g/(1000/1000 L)=0.54 g/L. This is provider normalization,
    not a measured final-volume claim.

    ingredients[4].concentration (KCl): verified 3 G_PER_L against MediaDive $.data.solutions[0].recipe[4].g_l=3;
    PDF batch amount 3 g. Provider volume=1000 mL; arithmetic 3 g/(1000/1000 L)=3
    g/L. This is provider normalization, not a measured final-volume claim.

    ingredients[5].concentration (NaHCO3): verified 0.09 G_PER_L against MediaDive
    $.data.solutions[0].recipe[5].g_l=0.09; PDF batch amount 0.09 g. Provider volume=1000
    mL; arithmetic 0.09 g/(1000/1000 L)=0.09 g/L. This is provider normalization,
    not a measured final-volume claim.

    ingredients[6].concentration (NaBr): verified 0.039 G_PER_L against MediaDive
    $.data.solutions[0].recipe[6].g_l=0.039; PDF batch amount 0.039 g. Provider volume=1000
    mL; arithmetic 0.039 g/(1000/1000 L)=0.039 g/L. This is provider normalization,
    not a measured final-volume claim.

    ingredients[7].concentration (Proteose peptone no. 3): verified 5 G_PER_L against
    MediaDive $.data.solutions[0].recipe[7].g_l=5; PDF batch amount 5 g. Provider
    volume=1000 mL; arithmetic 5 g/(1000/1000 L)=5 g/L. This is provider normalization,
    not a measured final-volume claim.

    ingredients[8].concentration (Yeast extract): verified 10 G_PER_L against MediaDive
    $.data.solutions[0].recipe[8].g_l=10; PDF batch amount 10 g. Provider volume=1000
    mL; arithmetic 10 g/(1000/1000 L)=10 g/L. This is provider normalization, not
    a measured final-volume claim.

    ingredients[9].concentration (Glucose): verified 1 G_PER_L against MediaDive $.data.solutions[0].recipe[9].g_l=1;
    PDF batch amount 1 g. Provider volume=1000 mL; arithmetic 1 g/(1000/1000 L)=1
    g/L. This is provider normalization, not a measured final-volume claim.

    Source-only water: PDF and API specify 1000 mL distilled water. The generated
    solute list omits water and does not state batch volume. Preserve source water
    addition and its distinction from a final-volume instruction in future curation;
    the existing solute g/L values are independently supported by API, not refuted
    by this omission.

    Bicarbonate stock: not_quantified for stock strength and addition volume; source
    specifies only the 0.09 g solute amount and addition after cooling. No structured
    solution reference or dose is asserted, so no broken-reference or missing dilution-factor
    finding is justified.

    Optional solid branch: verified 20 g/L agar in source and preparation description.
    The selected LIQUID formulation validly excludes agar from ingredients. No mandatory
    agar addition or solid-state mismatch is inferred.'
- assessment_id: grounding
  area: grounding
  topic: Every asserted primary and MIM chemical identifier
  outcome: supported
  summary: Eight primary CHEBI IDs and eight matching MIM CHEBI links resolve. MgCl2,
    MgSO4 and CaCl2 are represented without waters of crystallization, matching this
    DSMZ source wording. Glucose remains stereochemically unspecified. Proteose peptone
    and yeast extract are ungrounded mixtures, not falsely assigned pure-compound
    identities. Primary linkage coverage=8/10 ingredient instances (80%); MIM CHEBI
    linkage coverage=8/10 (80%); neither metric measures scientific accuracy.
  target_ids:
  - CultureMech:001708
  evidence_ids:
  - record
  - mim
  - dsmz
  - chebi-17234
  - chebi-26710
  - chebi-32139
  - chebi-32588
  - chebi-32599
  - chebi-3312
  - chebi-63004
  - chebi-6636
- assessment_id: conditions
  area: representation
  topic: Preparation and physical state
  outcome: supported
  summary: pH 7.5 and cooled-medium addition of sterilized bicarbonate stock are retained.
    The first action MIX is a broad tag on a pH statement, not evidence for a separate
    mixing protocol. Source agar is conditional; LIQUID is supported. Sterilization
    temperature/time and bicarbonate stock concentration are not supplied by the inspected
    DSMZ source.
  target_ids:
  - CultureMech:001708
  evidence_ids:
  - record
  - dsmz
  - api
- assessment_id: classification
  area: scope
  topic: Complex medium and growth scope
  outcome: supported
  summary: Peptone and yeast extract support COMPLEX/UNDEFINED. Microbial cultivation
    is a generic application, not a strain-growth claim. The record asserts no organism,
    incubation temperature, salinity class, yield or experimentally verified growth
    outcome; no organism inference is added from source database membership.
  target_ids:
  - CultureMech:001708
  evidence_ids:
  - record
  - dsmz
  - api
- assessment_id: provenance
  area: provenance
  topic: Maintained evidence versus generated snapshot
  outcome: concern
  summary: Generated ingredient rows and references omit eight claim-level evidence
    entries, their dataset citation and the October curation event present in the
    maintained DSMZ owner. The generated notes retain the authoritative PDF link,
    and all ten amounts were independently confirmed, so the gap is non-blocking provenance
    loss rather than unsupported chemistry.
  target_ids:
  - CultureMech:001708
  evidence_ids:
  - record
  - owner-0
  - api
  - merge
- assessment_id: history
  area: ownership
  topic: Native history and future edit ownership
  outcome: supported
  summary: Target identity and merge history are coherent with the two named normalized
    sources. Target has no record-level REVIEWED status and no status promotion is
    proposed. Future edits belong in normalized sources; generated bundles must come
    through the merge pipeline. Ingredient quantities and IDs need no correction based
    on this review.
  target_ids:
  - CultureMech:001708
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - internal
  - merge
findings:
- finding_id: f1
  issue_key: culturemech-001708-generated-concentration-evidence-gap
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Generated recipe omits maintained concentration evidence
  description: The normalized DSMZ owner has eight ingredient-level MediaDive excerpts,
    a dataset reference and an October evidence-curation event, while the target contains
    none of these additions and records an August merge. All ten amounts remain source-supported
    and the PDF link is retained; this is a bounded evidence-currentness gap. The
    comparison does not establish that current merge code would discard the evidence.
  target_ids:
  - CultureMech:001708
  field_paths:
  - ingredients[0].evidence
  - ingredients[1].evidence
  - ingredients[2].evidence
  - ingredients[3].evidence
  - ingredients[4].evidence
  - ingredients[5].evidence
  - ingredients[6].evidence
  - ingredients[9].evidence
  - references
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - api
  - merge
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/15_mh_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_582_15_MH_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Retain the validated owner evidence and, in separately authorized curation,
    regenerate this target through the current merge pipeline. Inspect the output
    for the eight correctly scoped excerpts and dataset reference; fix a generator
    only if regeneration demonstrates evidence loss. Do not change the supported ingredient
    amounts.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001708
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/15_mh_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_582_15_MH_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - 'Compare regenerated target with the maintained owner: eight ingredient evidence
    entries and dataset citation retained at the original claim scope.'
  - Re-run the four documented target validation recipes; reference validation should
    examine the newly present excerpts.
  - Run the documented merge-freshness and merge-verification gates after authorized
    regeneration; preserve immutable review bundles.
limitations:
- The DSMZ PDF states 1000 mL distilled water, not a measured final volume; G_PER_L
  values are verified against the explicit MediaDive volume and g_l declarations,
  not inferred from water alone.
- The source does not specify bicarbonate stock strength, dose volume, sterilization
  cycle, incubation conditions or strain growth; no such details were invented.
- KOMODO accession identity is confirmed from its captured MediaList row and local
  duplicate lineage. This does not independently verify an external KOMODO ingredient
  inventory or its historical aerobic flag.
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
