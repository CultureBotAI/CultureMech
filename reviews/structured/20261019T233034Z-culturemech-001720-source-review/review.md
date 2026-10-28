# Source and formulation review: 10_mh_medium (CultureMech:001720)

- Review: 20261019T233034Z-culturemech-001720-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-19T07:31:38Z
- Finished UTC: 2026-10-19T23:30:34Z
- Reviewer: OpenAI Codex with delegated source and validator checks (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

DSMZ 593 identity, all 11 stated ingredient amounts, chemical forms, pH, and solid-medium preparation are supported. The generated record omits nine verified concentration evidence entries already present in its maintained source, and omits the source water amount needed to reproduce the batch instruction.

## Scope And Provenance

One complete generated MediaRecipe, including source identity, every listed amount, chemical forms, stocks, conditions, preparation, classifications, provenance, and maintained-input correspondence.

Selection: Record 7 of the first ten uncovered paths in Python lexicographic repository-relative path order. Initial scripts/record_review.py list validated 34 existing bundles, whose targets covered 0 of 6320 merged records. This bundle selects only the named record; no sampling or fleet-wide scientific claim.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7c568537897ee4bba1b8e97f8172133c1572aec0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:001720 | data/merge_yaml/merged/10_mh_medium.yaml | generated | 10_mh_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:001720 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:001720 | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work/007/strict.tsv |
| validate-terms | passed | True | CultureMech:001720 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:001720 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| iModulonDB applicability | not_applicable | False | CultureMech:001720 | The reviewed medium asserts no gene, locus, regulator, pathway or transcriptomic dataset requiring an iModulonDB cross-check; expression-module membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Documented deterministic checks

schema: supported. Targets: CultureMech:001720.

The four documented recipes completed; interpret the scope of each separately.

### Source accession, medium variant, and reciprocal child

identity: supported. Targets: CultureMech:001720.

The target denotes the solid preparation of DSMZ 593. The local SOURCE_DUPLICATE child resolves as CultureMech:006075 and reciprocates parent CultureMech:001720; all 11 ingredient names, concentrations, primary terms, and MIM links agree.

### Every asserted chemical identity and exact supplied form

grounding: supported. Targets: CultureMech:001720.

All 9 unique target CHEBI IDs resolve. Primary mappings cover 9/11 direct ingredient instances; MIM links cover 9/11. These unweighted linkage counts do not measure scientific accuracy.

&#124; Field &#124; Supplied component &#124; Primary CHEBI; official label/form &#124; MIM link &#124; Decision &#124;
&#124;---&#124;---&#124;---&#124;---&#124;---&#124;
&#124; ingredients[0] &#124; NaCl &#124; CHEBI:26710; sodium chloride; Cl.Na &#124; CHEBI:26710 &#124; Matches supplied form and official label &#124;
&#124; ingredients[1] &#124; MgCl2 &#124; CHEBI:6636; magnesium dichloride; 2Cl.Mg &#124; CHEBI:6636 &#124; Matches supplied form and official label &#124;
&#124; ingredients[2] &#124; MgSO4 &#124; CHEBI:32599; magnesium sulfate; Mg.O4S &#124; CHEBI:32599 &#124; Matches supplied form and official label &#124;
&#124; ingredients[3] &#124; CaCl2 &#124; CHEBI:3312; calcium dichloride; Ca.2Cl &#124; CHEBI:3312 &#124; Matches supplied form and official label &#124;
&#124; ingredients[4] &#124; KCl &#124; CHEBI:32588; potassium chloride; Cl.K &#124; CHEBI:32588 &#124; Matches supplied form and official label &#124;
&#124; ingredients[5] &#124; NaHCO3 &#124; CHEBI:32139; sodium hydrogencarbonate; CHO3.Na &#124; CHEBI:32139 &#124; Matches supplied form and official label &#124;
&#124; ingredients[6] &#124; NaBr &#124; CHEBI:63004; sodium bromide; Br.Na &#124; CHEBI:63004 &#124; Matches supplied form and official label &#124;
&#124; ingredients[7] &#124; Proteose peptone no. 3 &#124; absent &#124; absent &#124; Undefined mixture; no forced single-chemical assignment &#124;
&#124; ingredients[8] &#124; Yeast extract &#124; absent &#124; absent &#124; Undefined mixture; no forced single-chemical assignment &#124;
&#124; ingredients[9] &#124; Glucose &#124; CHEBI:17234; glucose; C6H12O6 &#124; CHEBI:17234 &#124; Matches supplied form and official label &#124;
&#124; ingredients[10] &#124; Agar &#124; CHEBI:2509; agar; mixture; no discrete formula &#124; CHEBI:2509 &#124; Matches supplied form and official label &#124;

### Every ingredient concentration and batch boundary

quantity: supported. Targets: CultureMech:001720.

All 11 stated ingredient concentrations match explicit source g_l values; none requires correction on the inspected evidence. The source-only water instruction is separately incomplete. No stock strength or measured final-volume conversion is inferred.

&#124; Target claim &#124; Encoded value &#124; Inspected source value and stage &#124; Decision &#124;
&#124;---&#124;---&#124;---&#124;---&#124;
&#124; ingredients[0].concentration; NaCl &#124; 81 G_PER_L &#124; REST recipe[0].g_l=81; main recipe &#124; verified &#124;
&#124; ingredients[1].concentration; MgCl2 &#124; 7 G_PER_L &#124; REST recipe[1].g_l=7; main recipe &#124; verified &#124;
&#124; ingredients[2].concentration; MgSO4 &#124; 9.6 G_PER_L &#124; REST recipe[2].g_l=9.6; main recipe &#124; verified &#124;
&#124; ingredients[3].concentration; CaCl2 &#124; 0.36 G_PER_L &#124; REST recipe[3].g_l=0.36; main recipe &#124; verified &#124;
&#124; ingredients[4].concentration; KCl &#124; 2 G_PER_L &#124; REST recipe[4].g_l=2; main recipe &#124; verified &#124;
&#124; ingredients[5].concentration; NaHCO3 &#124; 0.06 G_PER_L &#124; REST recipe[5].g_l=0.06; main recipe &#124; verified &#124;
&#124; ingredients[6].concentration; NaBr &#124; 0.026 G_PER_L &#124; REST recipe[6].g_l=0.026; main recipe &#124; verified &#124;
&#124; ingredients[7].concentration; Proteose peptone no. 3 &#124; 5 G_PER_L &#124; REST recipe[7].g_l=5; main recipe &#124; verified &#124;
&#124; ingredients[8].concentration; Yeast extract &#124; 10 G_PER_L &#124; REST recipe[8].g_l=10; main recipe &#124; verified &#124;
&#124; ingredients[9].concentration; Glucose &#124; 1 G_PER_L &#124; REST recipe[9].g_l=1; main recipe &#124; verified &#124;
&#124; ingredients[10].concentration; Agar &#124; 15 G_PER_L &#124; REST recipe[11].g_l=15; main recipe; solid-medium condition &#124; verified &#124;
&#124; Source-only water instruction &#124; absent &#124; REST recipe[10] and DSMZPDF: distilled water 1000 mL added to batch &#124; add source instruction; do not describe as measured final volume &#124;

### Source-supported conditions, classification, and growth scope

completeness: supported. Targets: CultureMech:001720.

pH 7.5 and cooling before adding sterilized bicarbonate stock match the source. COMPLEX/UNDEFINED is consistent with peptone and yeast extract, and SOLID_AGAR matches the source solid option. The general cultivation application does not establish species-specific growth. No target-organism or growth evidence assertion is present. The importer action MIX attached to the final-pH statement is not a source-specified mixing operation and is not independently validated by this assessment.

The source names Difco preparations for proteose peptone no.3 and yeast extract, while the target retains the material names without supplier annotation. Supplier equivalence was not tested. Neither source supplies a main-medium autoclave cycle or stock strength; no protocol was invented. Empty optional organism/experimental fields are not classified as defects.

### Generated-target evidence freshness and maintained owners

provenance: concern. Targets: CultureMech:001720.

The normalized parent contains nine concentration evidence entries and a root reference added 2026-10-07; the generated target has none of those entries and retains an August merge event. The current REST response hash equals the normalized evidence hash. This is bounded provenance loss despite supported quantities.

Nine supported normalized ingredient evidence paths are ingredients[0..6,9,10].evidence. The parent and child maintain a coherent reciprocal SOURCE_DUPLICATE relationship. Historical provenance was read, but neither source-import dates nor append-only history across all earlier Git revisions were independently reconstructed.

## Findings

### f1: Generated record omits verified maintained-source evidence

minor / open / confirmed; issue key: CultureMech-001720-generated-concentration-evidence-omission.

Nine ingredient evidence entries and the root source reference present in the normalized parent are absent from this generated target. All corresponding quantities are supported by the current source, so this is bounded loss of claim-level traceability rather than unsupported concentration values.

### f2: Source water addition is omitted

minor / open / confirmed; issue key: CultureMech-001720-source-water-batch-instruction-omitted.

The source recipe includes 1000 mL distilled water, but neither target ingredients nor preparation carries that batch addition. Explicit g_l values still support the recorded ingredient rates; do not reinterpret the source water quantity as measured final volume.

## Recommended Actions And Acceptance Checks

### a1

Regenerate from the current normalized owner and confirm the merger preserves existing evidence and bibliographic context; fix merge preservation if regeneration still drops it.

- just validate-schema data/merge_yaml/merged/10_mh_medium.yaml
- just validate-strict data/merge_yaml/merged/10_mh_medium.yaml
- just validate-terms data/merge_yaml/merged/10_mh_medium.yaml
- just validate-references data/merge_yaml/merged/10_mh_medium.yaml
- Reinspect primary-source formulation and claim-level evidence after authorized owner curation; regenerate merged records and run just verify-merges and just audit-merge-freshness.
- Generated nine ingredient evidence entries retain exact current source snippets and matching reference metadata.

### a2

In a separately authorized curation, retain the source water/batch instruction on the normalized parent with a volume unit or preparation wording supported by the schema, then regenerate.

- just validate-schema data/merge_yaml/merged/10_mh_medium.yaml
- just validate-strict data/merge_yaml/merged/10_mh_medium.yaml
- just validate-terms data/merge_yaml/merged/10_mh_medium.yaml
- just validate-references data/merge_yaml/merged/10_mh_medium.yaml
- Reinspect primary-source formulation and claim-level evidence after authorized owner curation; regenerate merged records and run just verify-merges and just audit-merge-freshness.
- The source water addition is represented without density conversion, invented final-volume evidence, or double counting.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/merge_yaml/merged/10_mh_medium.yaml; Entire YAML; exact source hash captured in source.inputs | context_only | Complete generated record read, including all ingredients, notes, preparation, annotations, and history. |
| owner-0 | data/normalized_yaml/bacterial/10_mh_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| owner-1 | data/normalized_yaml/bacterial/KOMODO_593_10_MH_medium.yaml; Entire maintained YAML | context_only | Maintained owner read in full and compared with generated target; ownership is traced from the merge event source and merged_from. |
| validate-schema | just validate-schema data/merge_yaml/merged/10_mh_medium.yaml; Actual command output | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/10_mh_medium.yaml --workers 1 --out /private/tmp/culturemech-review-work/007/strict.tsv; Actual command output | supports | Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019/src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/culturemech-review-work/007/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/10_mh_medium.yaml; Actual command output | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/10_mh_medium.yaml; Actual command output | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| dsmz593 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium593.pdf; PDF page1; formulation table and final preparation paragraph | supports | Official DSMZ 593 identifies the medium, component batch amounts, pH 7.5, late bicarbonate-stock addition, and conditional agar for solid medium. |
| mediadive593 | https://mediadive.dsmz.de/rest/medium/593; $.data.medium; $.data.solutions[0].recipe[0..11] and steps | supports | Official REST medium 593 identifies the same medium and provides explicit g_l values for every recorded direct ingredient. Current response hash matches the hash recorded by the normalized parent evidence. |
| chebi-17234 | https://www.ebi.ac.uk/chebi/CHEBI:17234; ChEBI ID, ChEBI Name, Formula, definition and ontology form | supports | HTTP 200; CHEBI:17234 is glucose; formula C6H12O6. Identity and supplied form inspected; this does not establish a recipe amount or role. |
| chebi-2509 | https://www.ebi.ac.uk/chebi/CHEBI:2509; ChEBI ID, ChEBI Name, Formula, definition and ontology form | supports | HTTP 200; CHEBI:2509 is agar; formula mixture; no discrete formula. Identity and supplied form inspected; this does not establish a recipe amount or role. |
| chebi-26710 | https://www.ebi.ac.uk/chebi/CHEBI:26710; ChEBI ID, ChEBI Name, Formula, definition and ontology form | supports | HTTP 200; CHEBI:26710 is sodium chloride; formula Cl.Na. Identity and supplied form inspected; this does not establish a recipe amount or role. |
| chebi-32139 | https://www.ebi.ac.uk/chebi/CHEBI:32139; ChEBI ID, ChEBI Name, Formula, definition and ontology form | supports | HTTP 200; CHEBI:32139 is sodium hydrogencarbonate; formula CHO3.Na. Identity and supplied form inspected; this does not establish a recipe amount or role. |
| chebi-32588 | https://www.ebi.ac.uk/chebi/CHEBI:32588; ChEBI ID, ChEBI Name, Formula, definition and ontology form | supports | HTTP 200; CHEBI:32588 is potassium chloride; formula Cl.K. Identity and supplied form inspected; this does not establish a recipe amount or role. |
| chebi-32599 | https://www.ebi.ac.uk/chebi/CHEBI:32599; ChEBI ID, ChEBI Name, Formula, definition and ontology form | supports | HTTP 200; CHEBI:32599 is magnesium sulfate; formula Mg.O4S. Identity and supplied form inspected; this does not establish a recipe amount or role. |
| chebi-3312 | https://www.ebi.ac.uk/chebi/CHEBI:3312; ChEBI ID, ChEBI Name, Formula, definition and ontology form | supports | HTTP 200; CHEBI:3312 is calcium dichloride; formula Ca.2Cl. Identity and supplied form inspected; this does not establish a recipe amount or role. |
| chebi-63004 | https://www.ebi.ac.uk/chebi/CHEBI:63004; ChEBI ID, ChEBI Name, Formula, definition and ontology form | supports | HTTP 200; CHEBI:63004 is sodium bromide; formula Br.Na. Identity and supplied form inspected; this does not establish a recipe amount or role. |
| chebi-6636 | https://www.ebi.ac.uk/chebi/CHEBI:6636; ChEBI ID, ChEBI Name, Formula, definition and ontology form | supports | HTTP 200; CHEBI:6636 is magnesium dichloride; formula 2Cl.Mg. Identity and supplied form inspected; this does not establish a recipe amount or role. |
| mim-index | src/culturemech/data/mediaingredientmech/label_index.csv; All asserted mediaingredientmech_chebi_term IDs; metadata source commit 6643131b0f12ab40b66f98135245fca04027e0e9 | supports | Every asserted MIM CHEBI ID occurs in the packaged index. Index membership is a linkage check, not proof of correct hydrate identity. |
| mim-metadata | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Source commit and SHA256 | context_only | Pinned source commit and label-index SHA256 correspond to the input captured by inspection. |

## Limits And Additional Notes

- The KOMODO child was verified locally by stable ID, reciprocal parent relationship, declared DSMZ 593 provenance, and all 11 matching ingredient signatures; no independent live KOMODO accession page was inspected. Owner-only aerobic or historical import claims are not certified.
- The DSMZ PDF specifies added distilled-water volume, not an independently measured final volume. Concentration support uses the explicit MediaDive g_l values; no density, stock concentration, or final-volume assumption was introduced.
- Culture conditions or organisms absent from this record were not inferred. The source does not specify the main-medium sterilization cycle or bicarbonate-stock strength; these remain source limits.
- A schema/term pass does not establish chemical identity, correct source quantities, or growth. The reference recipe performed zero excerpt checks for this target; direct source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No new experiment or exhaustive literature review was performed. Full-corpus regeneration, ID/product/merge gates are acceptance checks for follow-up changes, not executed by this read-only single-record review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T233034Z-culturemech-001720-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Source and formulation review: 10_mh_medium (CultureMech:001720)'
started_at: '2026-10-19T07:31:38Z'
finished_at: '2026-10-19T23:30:34Z'
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
summary: DSMZ 593 identity, all 11 stated ingredient amounts, chemical forms, pH,
  and solid-medium preparation are supported. The generated record omits nine verified
  concentration evidence entries already present in its maintained source, and omits
  the source water amount needed to reproduce the batch instruction.
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
  - path: data/merge_yaml/merged/10_mh_medium.yaml
    sha256: eca28a35bbc45f0bbb4c74ffd7463660a2fa11daf64f82cdb0ca1b76efca4ebf
    role: target
  - path: data/normalized_yaml/bacterial/10_mh_medium.yaml
    sha256: 322e0e2ea54319d0a64bc6beb6508561d58e707ef6d63032ddc77a0b6e9174d8
    role: context
  - path: data/normalized_yaml/bacterial/KOMODO_593_10_MH_medium.yaml
    sha256: 03d88e73f8f93a338f64d5e7887ab7e5de258c1640a8904a3fbd42a720c7ff69
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
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
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
  selection: Record 7 of the first ten uncovered paths in Python lexicographic repository-relative
    path order. Initial scripts/record_review.py list validated 34 existing bundles,
    whose targets covered 0 of 6320 merged records. This bundle selects only the named
    record; no sampling or fleet-wide scientific claim.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:001720
targets:
- target_id: CultureMech:001720
  path: data/merge_yaml/merged/10_mh_medium.yaml
  label: 10_mh_medium
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/10_mh_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_593_10_MH_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/10_mh_medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:001720
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/10_mh_medium.yaml --workers
    1 --out /private/tmp/culturemech-review-work/007/strict.tsv
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work/007/strict.tsv"
  target_ids:
  - CultureMech:001720
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/10_mh_medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:001720
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/10_mh_medium.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:001720
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
  - CultureMech:001720
evidence:
- evidence_id: record
  kind: record_content
  reference: data/merge_yaml/merged/10_mh_medium.yaml
  locator: Entire YAML; exact source hash captured in source.inputs
  accessed_at: '2026-10-19T07:40:27Z'
  support: context_only
  summary: Complete generated record read, including all ingredients, notes, preparation,
    annotations, and history.
- evidence_id: owner-0
  kind: record_content
  reference: data/normalized_yaml/bacterial/10_mh_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-19T07:40:27Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_593_10_MH_medium.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-19T07:40:27Z'
  support: context_only
  summary: Maintained owner read in full and compared with generated target; ownership
    is traced from the merge event source and merged_from.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/10_mh_medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-19T07:33:47.475473Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/10_mh_medium.yaml --workers
    1 --out /private/tmp/culturemech-review-work/007/strict.tsv
  locator: Actual command output
  accessed_at: '2026-10-19T07:33:49.676313Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=/private/tmp/culturemech-record-review-20261019/src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         /private/tmp/culturemech-review-work/007/strict.tsv"
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/10_mh_medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-19T07:33:52.530870Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/10_mh_medium.yaml
  locator: Actual command output
  accessed_at: '2026-10-19T07:33:54.112150Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
- evidence_id: dsmz593
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium593.pdf
  locator: PDF page1; formulation table and final preparation paragraph
  accessed_at: '2026-10-19T07:32:40Z'
  support: supports
  summary: Official DSMZ 593 identifies the medium, component batch amounts, pH 7.5,
    late bicarbonate-stock addition, and conditional agar for solid medium.
  snapshot_sha256: f0c82b02a9f56dde8405f949732d7bde165f4f1ca8406b81d187a09fe6e6a4e7
- evidence_id: mediadive593
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/593
  locator: $.data.medium; $.data.solutions[0].recipe[0..11] and steps
  accessed_at: '2026-10-19T07:34:05Z'
  support: supports
  summary: Official REST medium 593 identifies the same medium and provides explicit
    g_l values for every recorded direct ingredient. Current response hash matches
    the hash recorded by the normalized parent evidence.
  snapshot_sha256: 8740ef227f4afc896558da1efec81b061ef315e531cc5a96eb9056b30dc89227
- evidence_id: chebi-17234
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:17234
  locator: ChEBI ID, ChEBI Name, Formula, definition and ontology form
  accessed_at: '2026-10-19T07:35:31.337539Z'
  support: supports
  summary: HTTP 200; CHEBI:17234 is glucose; formula C6H12O6. Identity and supplied
    form inspected; this does not establish a recipe amount or role.
  snapshot_sha256: 79006ae44d9d794815f34092ca6407adc60ba22b5a269fbc4f69dce945aef797
- evidence_id: chebi-2509
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:2509
  locator: ChEBI ID, ChEBI Name, Formula, definition and ontology form
  accessed_at: '2026-10-19T07:35:33.096698Z'
  support: supports
  summary: HTTP 200; CHEBI:2509 is agar; formula mixture; no discrete formula. Identity
    and supplied form inspected; this does not establish a recipe amount or role.
  snapshot_sha256: fdf12a8280861ef7a97ff6940adfaeba3e1bbe69671dbc1e4ee58869fc4f6bd3
- evidence_id: chebi-26710
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:26710
  locator: ChEBI ID, ChEBI Name, Formula, definition and ontology form
  accessed_at: '2026-10-19T07:35:35.012347Z'
  support: supports
  summary: HTTP 200; CHEBI:26710 is sodium chloride; formula Cl.Na. Identity and supplied
    form inspected; this does not establish a recipe amount or role.
  snapshot_sha256: 20d037f64aa7b26b83d04556c47a29bc5d4808bbdf7d25027e18ad22a5c5f02f
- evidence_id: chebi-32139
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:32139
  locator: ChEBI ID, ChEBI Name, Formula, definition and ontology form
  accessed_at: '2026-10-19T07:35:41.058859Z'
  support: supports
  summary: HTTP 200; CHEBI:32139 is sodium hydrogencarbonate; formula CHO3.Na. Identity
    and supplied form inspected; this does not establish a recipe amount or role.
  snapshot_sha256: 9c890ba478b78dfc699a10ead1ae2e71a5596286046d1ae6994b23aad7f69929
- evidence_id: chebi-32588
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:32588
  locator: ChEBI ID, ChEBI Name, Formula, definition and ontology form
  accessed_at: '2026-10-19T07:35:45.264277Z'
  support: supports
  summary: HTTP 200; CHEBI:32588 is potassium chloride; formula Cl.K. Identity and
    supplied form inspected; this does not establish a recipe amount or role.
  snapshot_sha256: 135d8318fe8cde9dc1b0ead7c50c12650a3d09d69cf4aa8541a1da01fc7abdce
- evidence_id: chebi-32599
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:32599
  locator: ChEBI ID, ChEBI Name, Formula, definition and ontology form
  accessed_at: '2026-10-19T07:35:47.353697Z'
  support: supports
  summary: HTTP 200; CHEBI:32599 is magnesium sulfate; formula Mg.O4S. Identity and
    supplied form inspected; this does not establish a recipe amount or role.
  snapshot_sha256: 3b05d10bdc37fe5074d0e91a3396d1c6f73224ed144ef845b501deaced552da2
- evidence_id: chebi-3312
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:3312
  locator: ChEBI ID, ChEBI Name, Formula, definition and ontology form
  accessed_at: '2026-10-19T07:35:53.053804Z'
  support: supports
  summary: HTTP 200; CHEBI:3312 is calcium dichloride; formula Ca.2Cl. Identity and
    supplied form inspected; this does not establish a recipe amount or role.
  snapshot_sha256: 44c71301c55f2a281eb5df66c3a53c281d48cf770d3b553e24cafd42a7b2f99f
- evidence_id: chebi-63004
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:63004
  locator: ChEBI ID, ChEBI Name, Formula, definition and ontology form
  accessed_at: '2026-10-19T07:35:56.710059Z'
  support: supports
  summary: HTTP 200; CHEBI:63004 is sodium bromide; formula Br.Na. Identity and supplied
    form inspected; this does not establish a recipe amount or role.
  snapshot_sha256: f7012f2d912509a901c06cc99442b4cf0e23a61065ecf429e8cb79ef4afba498
- evidence_id: chebi-6636
  kind: authority
  reference: https://www.ebi.ac.uk/chebi/CHEBI:6636
  locator: ChEBI ID, ChEBI Name, Formula, definition and ontology form
  accessed_at: '2026-10-19T07:36:00.250949Z'
  support: supports
  summary: HTTP 200; CHEBI:6636 is magnesium dichloride; formula 2Cl.Mg. Identity
    and supplied form inspected; this does not establish a recipe amount or role.
  snapshot_sha256: a1764bd688049cd029c31189e9bdd0afcf268103cdfd9fec5ded83eb4b93c54a
- evidence_id: mim-index
  kind: database
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: All asserted mediaingredientmech_chebi_term IDs; metadata source commit
    6643131b0f12ab40b66f98135245fca04027e0e9
  accessed_at: '2026-10-19T07:40:27Z'
  support: supports
  summary: Every asserted MIM CHEBI ID occurs in the packaged index. Index membership
    is a linkage check, not proof of correct hydrate identity.
- evidence_id: mim-metadata
  kind: database
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Source commit and SHA256
  accessed_at: '2026-10-19T07:40:27Z'
  support: context_only
  summary: Pinned source commit and label-index SHA256 correspond to the input captured
    by inspection.
assessments:
- assessment_id: schema
  area: schema
  topic: Documented deterministic checks
  outcome: supported
  summary: The four documented recipes completed; interpret the scope of each separately.
  target_ids:
  - CultureMech:001720
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
- assessment_id: identity
  area: identity
  topic: Source accession, medium variant, and reciprocal child
  outcome: supported
  summary: The target denotes the solid preparation of DSMZ 593. The local SOURCE_DUPLICATE
    child resolves as CultureMech:006075 and reciprocates parent CultureMech:001720;
    all 11 ingredient names, concentrations, primary terms, and MIM links agree.
  target_ids:
  - CultureMech:001720
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - dsmz593
  - mediadive593
  dimensions:
  - name: record_kind
    value: generated MediaRecipe
    definition: Derived from two maintained normalized inputs.
    evidence_ids:
    - record
    - owner-0
    - owner-1
  - name: source_accession
    value: DSMZ 593; MediaDive medium 593
    definition: Live primary formulation accession; KOMODO 593 is local duplicate
      provenance only.
    evidence_ids:
    - dsmz593
    - mediadive593
    - owner-1
  - name: source_variant
    value: solid agar preparation
    definition: Agar 15 g/L is conditional on preparing the solid medium; target SOLID_AGAR
      retains this distinction.
    evidence_ids:
    - record
    - dsmz593
    - mediadive593
- assessment_id: chemistry
  area: grounding
  topic: Every asserted chemical identity and exact supplied form
  outcome: supported
  summary: All 9 unique target CHEBI IDs resolve. Primary mappings cover 9/11 direct
    ingredient instances; MIM links cover 9/11. These unweighted linkage counts do
    not measure scientific accuracy.
  target_ids:
  - CultureMech:001720
  evidence_ids:
  - record
  - mim-index
  - mim-metadata
  - chebi-17234
  - chebi-2509
  - chebi-26710
  - chebi-32139
  - chebi-32588
  - chebi-32599
  - chebi-3312
  - chebi-63004
  - chebi-6636
  details: '| Field | Supplied component | Primary CHEBI; official label/form | MIM
    link | Decision |

    |---|---|---|---|---|

    | ingredients[0] | NaCl | CHEBI:26710; sodium chloride; Cl.Na | CHEBI:26710 |
    Matches supplied form and official label |

    | ingredients[1] | MgCl2 | CHEBI:6636; magnesium dichloride; 2Cl.Mg | CHEBI:6636
    | Matches supplied form and official label |

    | ingredients[2] | MgSO4 | CHEBI:32599; magnesium sulfate; Mg.O4S | CHEBI:32599
    | Matches supplied form and official label |

    | ingredients[3] | CaCl2 | CHEBI:3312; calcium dichloride; Ca.2Cl | CHEBI:3312
    | Matches supplied form and official label |

    | ingredients[4] | KCl | CHEBI:32588; potassium chloride; Cl.K | CHEBI:32588 |
    Matches supplied form and official label |

    | ingredients[5] | NaHCO3 | CHEBI:32139; sodium hydrogencarbonate; CHO3.Na | CHEBI:32139
    | Matches supplied form and official label |

    | ingredients[6] | NaBr | CHEBI:63004; sodium bromide; Br.Na | CHEBI:63004 | Matches
    supplied form and official label |

    | ingredients[7] | Proteose peptone no. 3 | absent | absent | Undefined mixture;
    no forced single-chemical assignment |

    | ingredients[8] | Yeast extract | absent | absent | Undefined mixture; no forced
    single-chemical assignment |

    | ingredients[9] | Glucose | CHEBI:17234; glucose; C6H12O6 | CHEBI:17234 | Matches
    supplied form and official label |

    | ingredients[10] | Agar | CHEBI:2509; agar; mixture; no discrete formula | CHEBI:2509
    | Matches supplied form and official label |'
  dimensions:
  - name: chemical_form_scope
    value: Exact salt, hydrate, and stoichiometry
    definition: Every primary and secondary CHEBI assertion in the generated target;
      source concentration support assessed separately.
    evidence_ids:
    - record
    - mim-index
    - mim-metadata
    - chebi-17234
    - chebi-2509
    - chebi-26710
    - chebi-32139
    - chebi-32588
    - chebi-32599
    - chebi-3312
    - chebi-63004
    - chebi-6636
- assessment_id: amounts
  area: quantity
  topic: Every ingredient concentration and batch boundary
  outcome: supported
  summary: All 11 stated ingredient concentrations match explicit source g_l values;
    none requires correction on the inspected evidence. The source-only water instruction
    is separately incomplete. No stock strength or measured final-volume conversion
    is inferred.
  target_ids:
  - CultureMech:001720
  evidence_ids:
  - record
  - owner-0
  - dsmz593
  - mediadive593
  details: '| Target claim | Encoded value | Inspected source value and stage | Decision
    |

    |---|---|---|---|

    | ingredients[0].concentration; NaCl | 81 G_PER_L | REST recipe[0].g_l=81; main
    recipe | verified |

    | ingredients[1].concentration; MgCl2 | 7 G_PER_L | REST recipe[1].g_l=7; main
    recipe | verified |

    | ingredients[2].concentration; MgSO4 | 9.6 G_PER_L | REST recipe[2].g_l=9.6;
    main recipe | verified |

    | ingredients[3].concentration; CaCl2 | 0.36 G_PER_L | REST recipe[3].g_l=0.36;
    main recipe | verified |

    | ingredients[4].concentration; KCl | 2 G_PER_L | REST recipe[4].g_l=2; main recipe
    | verified |

    | ingredients[5].concentration; NaHCO3 | 0.06 G_PER_L | REST recipe[5].g_l=0.06;
    main recipe | verified |

    | ingredients[6].concentration; NaBr | 0.026 G_PER_L | REST recipe[6].g_l=0.026;
    main recipe | verified |

    | ingredients[7].concentration; Proteose peptone no. 3 | 5 G_PER_L | REST recipe[7].g_l=5;
    main recipe | verified |

    | ingredients[8].concentration; Yeast extract | 10 G_PER_L | REST recipe[8].g_l=10;
    main recipe | verified |

    | ingredients[9].concentration; Glucose | 1 G_PER_L | REST recipe[9].g_l=1; main
    recipe | verified |

    | ingredients[10].concentration; Agar | 15 G_PER_L | REST recipe[11].g_l=15; main
    recipe; solid-medium condition | verified |

    | Source-only water instruction | absent | REST recipe[10] and DSMZPDF: distilled
    water 1000 mL added to batch | add source instruction; do not describe as measured
    final volume |'
  dimensions:
  - name: concentration_decision
    value: 'verified: all 11 stated ingredient amounts'
    definition: Each direct amount was compared to its exact source recipe row, preserving
      the solid-agar condition.
    evidence_ids:
    - mediadive593
    - dsmz593
  - name: volume_basis
    value: Provider-declared g_l; 1000 mL source water addition
    definition: Water addition and final-volume measurement are distinct claims.
    evidence_ids:
    - mediadive593
    - dsmz593
- assessment_id: conditions
  area: completeness
  topic: Source-supported conditions, classification, and growth scope
  outcome: supported
  summary: pH 7.5 and cooling before adding sterilized bicarbonate stock match the
    source. COMPLEX/UNDEFINED is consistent with peptone and yeast extract, and SOLID_AGAR
    matches the source solid option. The general cultivation application does not
    establish species-specific growth. No target-organism or growth evidence assertion
    is present. The importer action MIX attached to the final-pH statement is not
    a source-specified mixing operation and is not independently validated by this
    assessment.
  target_ids:
  - CultureMech:001720
  evidence_ids:
  - record
  - dsmz593
  - mediadive593
  details: The source names Difco preparations for proteose peptone no.3 and yeast
    extract, while the target retains the material names without supplier annotation.
    Supplier equivalence was not tested. Neither source supplies a main-medium autoclave
    cycle or stock strength; no protocol was invented. Empty optional organism/experimental
    fields are not classified as defects.
- assessment_id: provenance
  area: provenance
  topic: Generated-target evidence freshness and maintained owners
  outcome: concern
  summary: The normalized parent contains nine concentration evidence entries and
    a root reference added 2026-10-07; the generated target has none of those entries
    and retains an August merge event. The current REST response hash equals the normalized
    evidence hash. This is bounded provenance loss despite supported quantities.
  target_ids:
  - CultureMech:001720
  evidence_ids:
  - record
  - owner-0
  - owner-1
  - mediadive593
  details: Nine supported normalized ingredient evidence paths are ingredients[0..6,9,10].evidence.
    The parent and child maintain a coherent reciprocal SOURCE_DUPLICATE relationship.
    Historical provenance was read, but neither source-import dates nor append-only
    history across all earlier Git revisions were independently reconstructed.
findings:
- finding_id: f1
  issue_key: CultureMech-001720-generated-concentration-evidence-omission
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Generated record omits verified maintained-source evidence
  description: Nine ingredient evidence entries and the root source reference present
    in the normalized parent are absent from this generated target. All corresponding
    quantities are supported by the current source, so this is bounded loss of claim-level
    traceability rather than unsupported concentration values.
  target_ids:
  - CultureMech:001720
  field_paths:
  - ingredients[0].evidence
  - ingredients[1].evidence
  - ingredients[2].evidence
  - ingredients[3].evidence
  - ingredients[4].evidence
  - ingredients[5].evidence
  - ingredients[6].evidence
  - ingredients[9].evidence
  - ingredients[10].evidence
  - references
  - curation_history
  evidence_ids:
  - record
  - owner-0
  - mediadive593
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/10_mh_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_593_10_MH_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
- finding_id: f2
  issue_key: CultureMech-001720-source-water-batch-instruction-omitted
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Source water addition is omitted
  description: The source recipe includes 1000 mL distilled water, but neither target
    ingredients nor preparation carries that batch addition. Explicit g_l values still
    support the recorded ingredient rates; do not reinterpret the source water quantity
    as measured final volume.
  target_ids:
  - CultureMech:001720
  field_paths:
  - ingredients
  - preparation_steps
  evidence_ids:
  - record
  - owner-0
  - dsmz593
  - mediadive593
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/10_mh_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_593_10_MH_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
actions:
- action_id: a1
  description: Regenerate from the current normalized owner and confirm the merger
    preserves existing evidence and bibliographic context; fix merge preservation
    if regeneration still drops it.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:001720
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/10_mh_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_593_10_MH_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - just validate-schema data/merge_yaml/merged/10_mh_medium.yaml
  - just validate-strict data/merge_yaml/merged/10_mh_medium.yaml
  - just validate-terms data/merge_yaml/merged/10_mh_medium.yaml
  - just validate-references data/merge_yaml/merged/10_mh_medium.yaml
  - Reinspect primary-source formulation and claim-level evidence after authorized
    owner curation; regenerate merged records and run just verify-merges and just
    audit-merge-freshness.
  - Generated nine ingredient evidence entries retain exact current source snippets
    and matching reference metadata.
- action_id: a2
  description: In a separately authorized curation, retain the source water/batch
    instruction on the normalized parent with a volume unit or preparation wording
    supported by the schema, then regenerate.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:001720
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/10_mh_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_593_10_MH_medium.yaml
    role: authoritative normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merge_recipes.py
    role: derived record generator
  generator: python -m culturemech.merge.merge_recipes (only after owner verification,
    necessary corrections and separately authorized regeneration)
  acceptance_checks:
  - just validate-schema data/merge_yaml/merged/10_mh_medium.yaml
  - just validate-strict data/merge_yaml/merged/10_mh_medium.yaml
  - just validate-terms data/merge_yaml/merged/10_mh_medium.yaml
  - just validate-references data/merge_yaml/merged/10_mh_medium.yaml
  - Reinspect primary-source formulation and claim-level evidence after authorized
    owner curation; regenerate merged records and run just verify-merges and just
    audit-merge-freshness.
  - The source water addition is represented without density conversion, invented
    final-volume evidence, or double counting.
limitations:
- The KOMODO child was verified locally by stable ID, reciprocal parent relationship,
  declared DSMZ 593 provenance, and all 11 matching ingredient signatures; no independent
  live KOMODO accession page was inspected. Owner-only aerobic or historical import
  claims are not certified.
- The DSMZ PDF specifies added distilled-water volume, not an independently measured
  final volume. Concentration support uses the explicit MediaDive g_l values; no density,
  stock concentration, or final-volume assumption was introduced.
- Culture conditions or organisms absent from this record were not inferred. The source
  does not specify the main-medium sterilization cycle or bicarbonate-stock strength;
  these remain source limits.
- A schema/term pass does not establish chemical identity, correct source quantities,
  or growth. The reference recipe performed zero excerpt checks for this target; direct
  source comparisons are separately documented.
- No record, curation history, merge output, or scientific status was changed. No
  new experiment or exhaustive literature review was performed. Full-corpus regeneration,
  ID/product/merge gates are acceptance checks for follow-up changes, not executed
  by this read-only single-record review.
tags:
- unreviewed-records
- batch-001
- generated-medium
```
