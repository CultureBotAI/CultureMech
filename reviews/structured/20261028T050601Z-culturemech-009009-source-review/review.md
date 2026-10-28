# Brain Heart Infusion Broth: source and representation review

- Review: 20261028T050601Z-culturemech-009009-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T04:33:06.642859Z
- Finished UTC: 2026-10-28T05:06:01.964386Z
- Reviewer: OpenAI Codex (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Identity and six canonical term labels are corroborated, and all four native checks pass. Four major findings concern water units, commercial/scratch scope, batch amount basis and structured source conditions; one minor finding concerns claim evidence. Manufacturer dry-composition evidence remains unavailable.

## Scope And Provenance

One entire generated record, exact maintained owner, every direct quantity and related condition, source identity, grounding, roles, histories and provenance.

Selection: Batch 055 item 10 of the first ten Python-sorted paths uncovered by successful native list union. Coverage at selection: 473 of 6325 merged corpus paths. Fresh origin/main base 9ea7ff33d354e37b791df96a880005153e446ce3.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:009009 | data/merge_yaml/merged/Brain_Heart_Infusion_Broth.yaml | generated | Brain Heart Infusion Broth |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:009009 | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | passed | True | CultureMech:009009 | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch055/record10/strict.tsv |
| validate-terms | passed | True | CultureMech:009009 | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | passed | True | CultureMech:009009 | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| Embedded history comparison | passed | False | CultureMech:009009 | Both full embedded histories were read and compared. No separate focused embedded-history command is exposed; no invented validator was run. |
| Structured expression-module adapter applicability | not_applicable | False | CultureMech:009009 | No gene, regulator, pathway or transcriptomic dataset claim is present; expression membership cannot establish this formulation. |

## Scientific And Domain Assessments

### Accession, owner and formulation identity

identity: supported. Targets: CultureMech:009009.

The selected target is the M2426 BHI broth record, maintained by the exact normalized owner; ATCC44 corroborates the commercial broth identity.

The agar sibling and other BHI accessions are not interchangeable owners. Commercial-product identity is established independently of the unresolved detailed dry composition.

### All direct amounts, tissue notes and source-only conditions

quantity: concern. Targets: CultureMech:009009.

All fourteen local concentration fields and related tissue, pH and preparation claims were assessed. Water uses the wrong quantity kind; commercial and scratch claims need separate representation.

No nested stock or solution exists in either record. No final volume, density, hydrate, infusion yield or unverified manufacturer formula is assumed. Source batch masses are not summed into a commercial dose.

### Primary terms, exact material forms and MIM linkage

grounding: concern. Targets: CultureMech:009009.

The six existing term IDs have exact current canonical labels, but organ terms denote source anatomy and do not establish prepared-infusion or commercial-powder equivalence.

The notes explicitly identify tissue origins, which is useful context. Preserve that scope when representing extracted ingredients. MICRO proteose peptone matches the stated digest; glucose and salt IDs resolve correctly. No hydrate is added. A FOODON candidate is not promoted without exact material verification.

### Recipe-level pH, preparation and product context

completeness: concern. Targets: CultureMech:009009.

The existing phosphate pH note is supported, but structured recipe pH and the source commercial-broth sterilization instruction are missing.

The nominal pH 7.4 and range 7.2–7.6 agree. No sterilization duration, incubation, atmosphere, growth yield or organism scope is inferred. The optional storage range refers to the finished product.

### Complexity, phase and ingredient roles

representation: supported. Targets: CultureMech:009009.

COMPLEX, UNDEFINED and LIQUID are consistent with a broth containing biological infusions and digest material.

The generic notes about peptone nutrients, dextrose energy, salt osmotic contribution, phosphate buffering and water solvent role are bounded ingredient descriptions, not evidence of strain-specific essentiality or optimality.

### Claim placement, history and generated ownership

provenance: concern. Targets: CultureMech:009009.

Supplier product URLs point to a secondary agar article, and the unqualified researched-product-specification claim lacks a retrievable manufacturer formula.

Both local layers currently agree on the substantive recipe. No generated-staleness defect is claimed. Preserve the append-only history; add a future curation event only if separately authorized. Historical reports are leads, not current source verification.

### Growth assertions and structured adapter applicability

scope: supported. Targets: CultureMech:009009.

The record makes no organism-specific growth assertion; no organism or strain is inferred from the generic medium name.

Secondary pathogen-specific applications, supplements and incubation claims are excluded. No new DOI, PMID or taxonomy ID is invented.

### Native deterministic checks

schema: supported. Targets: CultureMech:009009.

All four required commands passed; strict validation scanned one file with zero errors.

The reference gate checked zero references. These results establish structural acceptance, not scientific source correspondence; separate OLS and source checks supply the scientific review.

## Findings

### F1: Input water volume is represented as mass concentration

major / open / confirmed; issue key: CM009009-water-volume.

Both records encode 1000 G_PER_L water, while TOGO and ATCC explicitly list 1000 ml water. Represent the input volume without assuming final mixed volume or density.

### F2: Commercial premix and scratch formulation are conflated

major / open / confirmed; issue key: CM009009-commercial-scratch-scope.

The commercial broth requires an explicitly named 37 g BD237500 product. Local records omit that addition and attach its SKU to separate scratch-style constituents, including anatomical tissue inputs. The inspected ATCC source labels its scratch route separately; the cited agar article does not authenticate this broth product decomposition. Preserve alternatives and provenance without double counting or replacing the formula silently.

### F3: Component rates claim an unresolved final-volume basis

major / open / confirmed; issue key: CM009009-batch-amount-basis.

The tissue notes and four component concentration rows reuse scratch batch digits with g/L units. ATCC lists the input amounts with 1000 ml water, without an explicit final mixed-volume instruction. The secondary agar rates do not establish exact broth-SKU equivalence. Preserve source batch quantity and stage; do not fabricate conversion factors, tissue yield or commercial powder masses.

### F4: Source conditions are not represented at recipe level

major / open / confirmed; issue key: CM009009-source-conditions.

The phosphate note already preserves final pH 7.4 ± 0.2, which must be credited. Recipe-level pH fields and preparation steps remain absent, so the explicit commercial-broth autoclaving temperature is lost to structured consumers. Preserve nominal pH and range; do not invent a duration.

### F5: Source support and supplier scope are not attached to individual claims

minor / open / confirmed; issue key: CM009009-claim-evidence.

The notes retain source URLs, but ingredient/preparation evidence and reference collections do not identify the exact claim scope. A secondary agar page is used as the supplier product URL and the broad product-specification assertion exceeds the inspected evidence. Add exact primary-source support while keeping unresolved manufacturer composition explicit.

## Recommended Actions And Acceptance Checks

### A1

Correct the maintained water quantity to the explicit input volume and cite its source.

- Use schema-supported volume semantics; retain 1000 ml = 1 L as input volume, with no density conversion or final-volume claim.
- Run the four native recipe validators on the corrected owner.

### A2

Represent the source commercial broth identity and batch dose separately from the scratch route; resolve the mass/volume representation before changing scalar rates.

- The 37 g commercial batch input, two tissue extraction inputs and four scratch masses remain separately sourced, with no double counting.
- A manufacturer formulation must be inspected before claiming exact SKU constituent equivalence; unknown dry infusion masses remain unknown.
- Preserve batch masses in preparation/evidence when the current enum cannot express them. Any schema extension requires its separately governed implementation and generated products.
- Recheck all direct amount and tissue-note claims and run the four native recipe validators.

### A3

Expose supported pH and commercial-broth preparation conditions in the normalized owner.

- Credit the existing pH note, retain nominal value and supported range, and distinguish preparation from incubation.
- Capture only the source-explicit sterilization temperature; leave unreported duration unspecified.

### A4

Attach exact source excerpts at the narrowest claim and correct supplier-reference scope.

- Distinguish collection recipe, scratch formulation, secondary agar discussion and authenticated manufacturer specification.
- Keep source access limits visible; append a curation event only with actual authorized curation, preserving earlier entries.

### A5

Regenerate the target after maintained-owner curation and compare the resulting formulation to its sources.

- Run just verify-merges and just audit-merge-freshness, then the four native validators; inspect commercial/scratch boundaries in the generated record.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| target | data/merge_yaml/merged/Brain_Heart_Infusion_Broth.yaml; entire file | context_only | Full generated record reread: seven direct ingredients, no nested stocks or solutions, six primary terms, no MIM links, no structured pH or preparation, source and supplier notes, four history events. |
| owner | data/normalized_yaml/bacterial/brain_heart_infusion_broth.yaml; entire file | context_only | Full maintained owner reread: identical seven ingredients, classifications and source notes; three history events. The generated record adds its merge event. No later scientific owner repair is concealed by the selected target. |
| schema | src/culturemech/schema/culturemech.yaml; ConcentrationUnitEnum; MediaRecipe pH and preparation slots | context_only | ConcentrationUnitEnum includes volume-only L and concentration units, but no plain batch-mass G. Preserve source batch masses in evidence/preparation or resolve a representation gap; do not invent a final-volume denominator. |
| importer | src/culturemech/import/togo_importer.py; _parse_unit; _extract_ph; medium conversion | context_only | Current parser maps g to G_PER_L, ml to ML_PER_L and l to L. A unit conversion alone does not establish final mixture volume. The pH reader expects medium.ph while current source API puts ph in meta; trace the actual loader before attributing a historical omission. |
| generator | src/culturemech/merge/merger.py; merge_group single-source branch | context_only | Single-source merge preserves owner content and adds merge metadata; maintain the normalized owner and regenerate the derived target. |
| registry | data/culturemech_id_registry.tsv; CultureMech:009009 | context_only | Exact identifier and normalized path corroborate the selected owner. Similarly named BHI records, including TOGO M2511, are not substitute owners. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Exact label and preferred-term rows for all seven ingredients | context_only | Exact label/preferred-term projections inspected. Proteose peptone, D-glucose, NaCl and disodium hydrogenphosphate have mapped matches; the rejected Dextrose preferred entry does not invalidate its mapped D-glucose synonym. Beef heart FOODON and calf-brain unresolved rows are leads, not automatically verified replacements. No fuzzy resolver or sibling checkout was used. |
| mim-metadata | src/culturemech/data/mediaingredientmech/label_index.metadata.json; entire file | context_only | Packaged snapshot pins 9,077 rows, source commit 6643131b0f12ab40b66f98135245fca04027e0e9 and CSV digest; this is linkage context, not formula certification. |
| history-record | reports/yaml_record_review/20260922T000505Z-Brain_Heart_Infusion_Broth.md; entire file | context_only | Entire historical report read. September findings are leads and have been reassessed against current sources; October concentration reports explicitly source-check zero of seven amounts and do not establish formula accuracy. |
| history-target | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Brain_Heart_Infusion_Broth.md; entire file | context_only | Entire historical report read. September findings are leads and have been reassessed against current sources; October concentration reports explicitly source-check zero of seven amounts and do not establish formula accuracy. |
| history-owner | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/brain_heart_infusion_broth.md; entire file | context_only | Entire historical report read. September findings are leads and have been reassessed against current sources; October concentration reports explicitly source-check zero of seven amounts and do not establish formula accuracy. |
| togo | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2426; meta; components[0].items; comments | partial | Full current M2426 response identifies BHI broth BD237500, 37 g with 1000 ml DI water, pH range 7.2–7.6 and autoclaving at 121 degrees C. No strain, duration or measured final volume is stated. |
| atcc | https://www.atcc.org/~/media/45E208A3191F4C7EA9B7E1063EB55303.ashx; page 1; Broth Medium; Brain Heart Infusion Composition; Final Product Description | partial | Full extracted one-page ATCC44 source read. Commercial agar, commercial broth and the separate scratch formulation are distinguished. Broth uses BD237500 37 g with 1000 ml water. Scratch tissue input masses are not dry infusion solids. Final pH, sterilization temperature and storage are bounded source conditions. |
| secondary | https://microbenotes.com/brain-heart-infusion-bhi-agar/; Composition of Brain Heart Infusion (BHI) Agar; Principle; References | partial | Only the cited article composition/principles/reference context informs this review. The agar table uses HM infusion powder 12.5 g/L and BHI powder 5 g/L plus peptone, dextrose, salts and agar. It does not authenticate the exact composition of broth SKU237500 or the 200/250 g tissue inputs. Organism-specific applications and supplements are excluded. |
| uberon0000955 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?iri=http://purl.obolibrary.org/obo/UBERON_0000955; _embedded.terms[0] | supports | Current OLS exact term: UBERON:0000955 — brain; obsolete=False. Definition, synonyms and available formula/charge inspected. Anatomical organ terms do not quantify an extracted infusion or identify its dry commercial equivalent. |
| uberon0000948 | https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?iri=http://purl.obolibrary.org/obo/UBERON_0000948; _embedded.terms[0] | supports | Current OLS exact term: UBERON:0000948 — heart; obsolete=False. Definition, synonyms and available formula/charge inspected. Anatomical organ terms do not quantify an extracted infusion or identify its dry commercial equivalent. |
| micro0000180 | https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http://purl.obolibrary.org/obo/MICRO_0000180; _embedded.terms[0] | supports | Current OLS exact term: MICRO:0000180 — proteose peptone; obsolete=False. Definition, synonyms and available formula/charge inspected. Anatomical organ terms do not quantify an extracted infusion or identify its dry commercial equivalent. |
| chebi17634 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17634; _embedded.terms[0] | supports | Current OLS exact term: CHEBI:17634 — D-glucose; obsolete=False. Definition, synonyms and available formula/charge inspected. Anatomical organ terms do not quantify an extracted infusion or identify its dry commercial equivalent. |
| chebi26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_26710; _embedded.terms[0] | supports | Current OLS exact term: CHEBI:26710 — sodium chloride; obsolete=False. Definition, synonyms and available formula/charge inspected. Anatomical organ terms do not quantify an extracted infusion or identify its dry commercial equivalent. |
| chebi34683 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_34683; _embedded.terms[0] | supports | Current OLS exact term: CHEBI:34683 — disodium hydrogenphosphate; obsolete=False. Definition, synonyms and available formula/charge inspected. Anatomical organ terms do not quantify an extracted infusion or identify its dry commercial equivalent. |
| bd237500 | https://www.bd.com/en-us/products-and-solutions/products/product-page.237500; captured request outcome | unknown | Official product URL returned HTTP403 in direct capture. Exact dry constituent masses for the SKU remain unverified; search snippets are not adopted. |
| bdifu237500 | https://legacy.bd.com/europe/regulatory/Assets/IFU/Difco_BBL/237500.pdf; captured request outcome | unknown | Legacy IFU host failed DNS resolution; no PDF obtained. Exact dry constituent masses for the SKU remain unverified; search snippets are not adopted. |
| bdmanual404 | https://static.bd.com/assets/product/Documents/Integrated%20Diagnostic%20Solutions%20%28IDS%29/DS_CM_Difco-and-BBL-culture-media-manual_UG_EN.pdf; captured request outcome | unknown | Indexed official culture-media manual returned HTTP404. Exact dry constituent masses for the SKU remain unverified; search snippets are not adopted. |
| bdmanual_citeseer | https://citeseerx.ist.psu.edu/document?doi=b9e564323726b77dd578f90be1f447da053c25f4&amp;repid=rep1&amp;type=pdf; captured request outcome | unknown | Indexed mirror redirected to a Wayback HTML page, not the manufacturer PDF. Exact dry constituent masses for the SKU remain unverified; search snippets are not adopted. |
| bdmanual_trios | https://www.trios.cz/wp-content/uploads/sites/149/2016/08/DIFCO-A-BBL-MANUAL-2.pdf; captured request outcome | unknown | Python TLS certificate verification failed; no source content obtained. Exact dry constituent masses for the SKU remain unverified; search snippets are not adopted. |
| bdmanual_trios_curl | https://www.trios.cz/wp-content/uploads/sites/149/2016/08/DIFCO-A-BBL-MANUAL-2.pdf; captured request outcome | unknown | System curl with normal TLS reached HTTP404 HTML, not the manual. Transport exit0 is not a source-content success. Exact dry constituent masses for the SKU remain unverified; search snippets are not adopted. |
| validate-schema | just validate-schema data/merge_yaml/merged/Brain_Heart_Infusion_Broth.yaml; full stdout and stderr | context_only | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed |
| validate-strict | just validate-strict data/merge_yaml/merged/Brain_Heart_Infusion_Broth.yaml --out REVIEW_WORK/batch055/record10/strict.tsv --workers 1; full stdout and stderr | context_only | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch055/record10/strict.tsv |
| validate-terms | just validate-terms data/merge_yaml/merged/Brain_Heart_Infusion_Broth.yaml; full stdout and stderr | context_only | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed |
| validate-references | just validate-references data/merge_yaml/merged/Brain_Heart_Infusion_Broth.yaml; full stdout and stderr | context_only | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed |
| q-water | https://www.atcc.org/~/media/45E208A3191F4C7EA9B7E1063EB55303.ashx; page 1; Broth Medium water row | partial | Source input is 1000 ml water, equivalent to 1 L input volume using schema L; 1000 G_PER_L is not supported. Do not infer final mixed volume or convert via density. |
| q-infusion-1 | https://www.atcc.org/~/media/45E208A3191F4C7EA9B7E1063EB55303.ashx; page 1; scratch formulation tissue row | partial | VARIABLE is acceptable for an unmeasured calf brain infusion-solids concentration. The source tissue input mass is not the mass of extracted dry solids or the authenticated commercial powder fraction. |
| q-tissue-input-1 | https://www.atcc.org/~/media/45E208A3191F4C7EA9B7E1063EB55303.ashx; page 1; scratch formulation tissue row | partial | Preserve 200 g as a scratch-recipe tissue extraction input with stage and source. The local g/L note asserts a denominator not explicitly established by the listed 1000 ml water; do not assign the tissue mass to the dry commercial product. |
| q-infusion-2 | https://www.atcc.org/~/media/45E208A3191F4C7EA9B7E1063EB55303.ashx; page 1; scratch formulation tissue row | partial | VARIABLE is acceptable for an unmeasured beef heart infusion-solids concentration. The source tissue input mass is not the mass of extracted dry solids or the authenticated commercial powder fraction. |
| q-tissue-input-2 | https://www.atcc.org/~/media/45E208A3191F4C7EA9B7E1063EB55303.ashx; page 1; scratch formulation tissue row | partial | Preserve 250 g as a scratch-recipe tissue extraction input with stage and source. The local g/L note asserts a denominator not explicitly established by the listed 1000 ml water; do not assign the tissue mass to the dry commercial product. |
| q-mass-3 | https://www.atcc.org/~/media/45E208A3191F4C7EA9B7E1063EB55303.ashx; page 1; scratch formulation component row | partial | Numerical mass agrees with the ATCC scratch batch. Its explicit final mixed-volume basis and equivalence to the named commercial SKU have not been established. The secondary agar g/L table cannot certify this broth SKU. Retain exact source mass and formulation scope; do not fabricate a new concentration. |
| q-mass-4 | https://www.atcc.org/~/media/45E208A3191F4C7EA9B7E1063EB55303.ashx; page 1; scratch formulation component row | partial | Numerical mass agrees with the ATCC scratch batch. Its explicit final mixed-volume basis and equivalence to the named commercial SKU have not been established. The secondary agar g/L table cannot certify this broth SKU. Retain exact source mass and formulation scope; do not fabricate a new concentration. |
| q-mass-5 | https://www.atcc.org/~/media/45E208A3191F4C7EA9B7E1063EB55303.ashx; page 1; scratch formulation component row | partial | Numerical mass agrees with the ATCC scratch batch. Its explicit final mixed-volume basis and equivalence to the named commercial SKU have not been established. The secondary agar g/L table cannot certify this broth SKU. Retain exact source mass and formulation scope; do not fabricate a new concentration. |
| q-mass-6 | https://www.atcc.org/~/media/45E208A3191F4C7EA9B7E1063EB55303.ashx; page 1; scratch formulation component row | partial | Numerical mass agrees with the ATCC scratch batch. Its explicit final mixed-volume basis and equivalence to the named commercial SKU have not been established. The secondary agar g/L table cannot certify this broth SKU. Retain exact source mass and formulation scope; do not fabricate a new concentration. |
| q-premix | https://www.atcc.org/~/media/45E208A3191F4C7EA9B7E1063EB55303.ashx; page 1; Broth Medium premix row | partial | Recover the source commercial-product identity and 37 g batch amount separately from scratch-component metadata. Do not count both premix and its constituents as independent additions. Plain batch G is not supported by the current concentration enum; preserve exact mass in preparation/evidence pending a suitable representation. |
| q-ph | https://www.atcc.org/~/media/45E208A3191F4C7EA9B7E1063EB55303.ashx; page 1; final pH | partial | Credit the existing phosphate note and expose the same supported nominal pH/range in recipe-level fields; TOGO 7.2–7.6 is arithmetically consistent. Do not silently discard the range. |
| q-sterilization | https://www.atcc.org/~/media/45E208A3191F4C7EA9B7E1063EB55303.ashx; page 1; Broth Medium | partial | Add only the source commercial-broth autoclaving temperature; neither primary source supplies a duration. This is preparation, not incubation. |
| q-storage | https://www.atcc.org/~/media/45E208A3191F4C7EA9B7E1063EB55303.ashx; page 1; Final Product Description | partial | ATCC44 supplies a generic product storage range. It can be captured with exact finished-product scope; absence is not a separate major finding, and no storage duration or organism growth condition is inferred. |

## Limits And Additional Notes

- No retrievable manufacturer manual or IFU verified the detailed dry formula for BD237500. Official endpoints were blocked/unavailable and mirrors did not yield the document; search snippets were not adopted.
- No final mixed volume, tissue extraction yield, density, hydration state beyond the literal source or sterilization duration was established. No conversion requiring these values was performed.
- The primary page was read as complete extracted text; the independent peer checked its visual layout. This review does not establish organism-specific growth or experimental optimality.
- The standalone history-tree validator is not a focused embedded-history check; histories were read and compared without modification.
- Ignored-inclusive searches covered selected identifiers/slugs in normalized records and historical reports, plus supplier/composition writer strings in scripts and src. The ownership finding does not claim a global absence outside those bounds.
- Source captures retain URLs, actual UTC access times and SHA256 hashes in the durable batch work area. The quantity inventory has 13 decisions covering all fourteen local concentration fields and related claims.
- Current substantive owner/target agreement is credited. No recipe, source history or generated product was edited.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T050601Z-culturemech-009009-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Brain Heart Infusion Broth: source and representation review'
started_at: '2026-10-28T04:33:06.642859Z'
finished_at: '2026-10-28T05:06:01.964386Z'
reviewer:
  identity: OpenAI Codex
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author or modify the assessed scientific records.
    Independent source and exact-input review, not experimental validation.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: true
summary: Identity and six canonical term labels are corroborated, and all four native
  checks pass. Four major findings concern water units, commercial/scratch scope,
  batch amount basis and structured source conditions; one minor finding concerns
  claim evidence. Manufacturer dry-composition evidence remains unavailable.
source:
  git_revision: 9ea7ff33d354e37b791df96a880005153e446ce3
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
  - path: AGENTS.md
    sha256: 72737a531548de8636bcf70b972e71a7630a0e579215b6ded392d88d1b51a4fc
    role: context
  - path: CLAUDE.md
    sha256: b5c5bb1c2293ba5f6c49cda8cb40bf36e021c0a2b9fe2d9497cf0a2fe19a1ac4
    role: context
  - path: conf/oak_config.yaml
    sha256: c0ef0808662f57dc2f57ce9b405485830503653aceee1451c9e1dae42f9e7021
    role: context
  - path: conf/record_review.yaml
    sha256: a76531e51214e559c97ab748a4cba169f8a9598ce6e3664518489b43dfc9bf88
    role: context
  - path: data/culturemech_id_registry.tsv
    sha256: 0d059720f5c474b63daff8d5010fc56942a5a3ac30761ee75ce9e84801d555a5
    role: context
  - path: data/merge_yaml/merged/Brain_Heart_Infusion_Broth.yaml
    sha256: fa61fe80dfed7c4dc0b82a39ee01d3719f8d3c8070711edaefd629e67665e75e
    role: target
  - path: data/normalized_yaml/bacterial/brain_heart_infusion_broth.yaml
    sha256: 8abf1e31a460674cb4009a5f6b07e4d9bfac302b1592236f0b46aaa9f3fcfdaf
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Brain_Heart_Infusion_Broth.md
    sha256: a7d6468cedf83b6f6718118a282f988c682a0d823793d3acb0d302a25451d846
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/brain_heart_infusion_broth.md
    sha256: d541855a3370b3766a449e3678f106abb464f7584435e5848fbfec90f29e5356
    role: context
  - path: reports/yaml_record_review/20260922T000505Z-Brain_Heart_Infusion_Broth.md
    sha256: 25b6142013510a7bf800e49c2ac89d3661588c6bd18ab34bbe03a5c9ed24b798
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_mim_groundings.py
    sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
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
  - path: src/culturemech/import/togo_importer.py
    sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
    role: context
  - path: src/culturemech/merge/fingerprint.py
    sha256: 9bc62b7f462b26775e7dff15bb91beb653ba8f1642b247466dba1c0366ed8a9e
    role: context
  - path: src/culturemech/merge/merge_recipes.py
    sha256: ce00a4b4e0bc2fa9a63e8b33f4a591cb20984569e125d395af40f5b7e84766a7
    role: context
  - path: src/culturemech/merge/merger.py
    sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
    role: context
  - path: src/culturemech/schema/culturemech.yaml
    sha256: 8551fa65e4e96f36847368641282948cffd393356648fd9fb6947831ab985fae
    role: context
  - path: src/culturemech/validation/schema_defaulter.py
    sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
    role: context
scope:
  description: One entire generated record, exact maintained owner, every direct quantity
    and related condition, source identity, grounding, roles, histories and provenance.
  selection: 'Batch 055 item 10 of the first ten Python-sorted paths uncovered by
    successful native list union. Coverage at selection: 473 of 6325 merged corpus
    paths. Fresh origin/main base 9ea7ff33d354e37b791df96a880005153e446ce3.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:009009
  exclusions:
  - target: Agar and other BHI variants; organism-specific applications
    reason: Different formulation or unsupported scope; no growth, supplement or incubation
      claims are transferred.
targets:
- target_id: CultureMech:009009
  path: data/merge_yaml/merged/Brain_Heart_Infusion_Broth.yaml
  label: Brain Heart Infusion Broth
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_broth.yaml
    role: maintained normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merger.py
    role: generated merge implementation
checks:
- check_id: validate-schema
  name: validate-schema
  command: just validate-schema data/merge_yaml/merged/Brain_Heart_Infusion_Broth.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  target_ids:
  - CultureMech:009009
  evidence_ids:
  - validate-schema
- check_id: validate-strict
  name: validate-strict
  command: just validate-strict data/merge_yaml/merged/Brain_Heart_Infusion_Broth.yaml
    --out REVIEW_WORK/batch055/record10/strict.tsv --workers 1
  exit_code: 0
  required: true
  status: passed
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch055/record10/strict.tsv"
  target_ids:
  - CultureMech:009009
  evidence_ids:
  - validate-strict
- check_id: validate-terms
  name: validate-terms
  command: just validate-terms data/merge_yaml/merged/Brain_Heart_Infusion_Broth.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  target_ids:
  - CultureMech:009009
  evidence_ids:
  - validate-terms
- check_id: validate-references
  name: validate-references
  command: just validate-references data/merge_yaml/merged/Brain_Heart_Infusion_Broth.yaml
  exit_code: 0
  required: true
  status: passed
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  target_ids:
  - CultureMech:009009
  evidence_ids:
  - validate-references
- check_id: history
  name: Embedded history comparison
  required: false
  status: passed
  summary: Both full embedded histories were read and compared. No separate focused
    embedded-history command is exposed; no invented validator was run.
  target_ids:
  - CultureMech:009009
  evidence_ids:
  - target
  - owner
- check_id: imodulondb
  name: Structured expression-module adapter applicability
  required: false
  status: not_applicable
  summary: No gene, regulator, pathway or transcriptomic dataset claim is present;
    expression membership cannot establish this formulation.
  target_ids:
  - CultureMech:009009
evidence:
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/Brain_Heart_Infusion_Broth.yaml
  accessed_at: '2026-10-28T04:48:37.116606Z'
  support: context_only
  summary: 'Full generated record reread: seven direct ingredients, no nested stocks
    or solutions, six primary terms, no MIM links, no structured pH or preparation,
    source and supplier notes, four history events.'
  locator: entire file
  snapshot_sha256: fa61fe80dfed7c4dc0b82a39ee01d3719f8d3c8070711edaefd629e67665e75e
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/brain_heart_infusion_broth.yaml
  accessed_at: '2026-10-28T04:48:37.116778Z'
  support: context_only
  summary: 'Full maintained owner reread: identical seven ingredients, classifications
    and source notes; three history events. The generated record adds its merge event.
    No later scientific owner repair is concealed by the selected target.'
  locator: entire file
  snapshot_sha256: 8abf1e31a460674cb4009a5f6b07e4d9bfac302b1592236f0b46aaa9f3fcfdaf
- evidence_id: schema
  kind: record_content
  reference: src/culturemech/schema/culturemech.yaml
  accessed_at: '2026-10-28T04:48:37.116781Z'
  support: context_only
  summary: ConcentrationUnitEnum includes volume-only L and concentration units, but
    no plain batch-mass G. Preserve source batch masses in evidence/preparation or
    resolve a representation gap; do not invent a final-volume denominator.
  locator: ConcentrationUnitEnum; MediaRecipe pH and preparation slots
  snapshot_sha256: 8551fa65e4e96f36847368641282948cffd393356648fd9fb6947831ab985fae
- evidence_id: importer
  kind: record_content
  reference: src/culturemech/import/togo_importer.py
  accessed_at: '2026-10-28T04:48:37.116782Z'
  support: context_only
  summary: Current parser maps g to G_PER_L, ml to ML_PER_L and l to L. A unit conversion
    alone does not establish final mixture volume. The pH reader expects medium.ph
    while current source API puts ph in meta; trace the actual loader before attributing
    a historical omission.
  locator: _parse_unit; _extract_ph; medium conversion
  snapshot_sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
- evidence_id: generator
  kind: record_content
  reference: src/culturemech/merge/merger.py
  accessed_at: '2026-10-28T04:48:37.116784Z'
  support: context_only
  summary: Single-source merge preserves owner content and adds merge metadata; maintain
    the normalized owner and regenerate the derived target.
  locator: merge_group single-source branch
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: registry
  kind: record_content
  reference: data/culturemech_id_registry.tsv
  accessed_at: '2026-10-28T04:48:37.116785Z'
  support: context_only
  summary: Exact identifier and normalized path corroborate the selected owner. Similarly
    named BHI records, including TOGO M2511, are not substitute owners.
  locator: CultureMech:009009
  snapshot_sha256: 0d059720f5c474b63daff8d5010fc56942a5a3ac30761ee75ce9e84801d555a5
- evidence_id: mim
  kind: database
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  accessed_at: '2026-10-28T04:48:37.116786Z'
  support: context_only
  summary: Exact label/preferred-term projections inspected. Proteose peptone, D-glucose,
    NaCl and disodium hydrogenphosphate have mapped matches; the rejected Dextrose
    preferred entry does not invalidate its mapped D-glucose synonym. Beef heart FOODON
    and calf-brain unresolved rows are leads, not automatically verified replacements.
    No fuzzy resolver or sibling checkout was used.
  locator: Exact label and preferred-term rows for all seven ingredients
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-metadata
  kind: database
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  accessed_at: '2026-10-28T04:48:37.116787Z'
  support: context_only
  summary: Packaged snapshot pins 9,077 rows, source commit 6643131b0f12ab40b66f98135245fca04027e0e9
    and CSV digest; this is linkage context, not formula certification.
  locator: entire file
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: history-record
  kind: prior_review
  reference: reports/yaml_record_review/20260922T000505Z-Brain_Heart_Infusion_Broth.md
  accessed_at: '2026-10-28T04:48:37.116789Z'
  support: context_only
  summary: Entire historical report read. September findings are leads and have been
    reassessed against current sources; October concentration reports explicitly source-check
    zero of seven amounts and do not establish formula accuracy.
  locator: entire file
  snapshot_sha256: 25b6142013510a7bf800e49c2ac89d3661588c6bd18ab34bbe03a5c9ed24b798
- evidence_id: history-target
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/Brain_Heart_Infusion_Broth.md
  accessed_at: '2026-10-28T04:48:37.116790Z'
  support: context_only
  summary: Entire historical report read. September findings are leads and have been
    reassessed against current sources; October concentration reports explicitly source-check
    zero of seven amounts and do not establish formula accuracy.
  locator: entire file
  snapshot_sha256: a7d6468cedf83b6f6718118a282f988c682a0d823793d3acb0d302a25451d846
- evidence_id: history-owner
  kind: prior_review
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/brain_heart_infusion_broth.md
  accessed_at: '2026-10-28T04:48:37.116791Z'
  support: context_only
  summary: Entire historical report read. September findings are leads and have been
    reassessed against current sources; October concentration reports explicitly source-check
    zero of seven amounts and do not establish formula accuracy.
  locator: entire file
  snapshot_sha256: d541855a3370b3766a449e3678f106abb464f7584435e5848fbfec90f29e5356
- evidence_id: togo
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2426
  accessed_at: '2026-10-28T04:34:37.699919Z'
  support: partial
  summary: Full current M2426 response identifies BHI broth BD237500, 37 g with 1000
    ml DI water, pH range 7.2–7.6 and autoclaving at 121 degrees C. No strain, duration
    or measured final volume is stated.
  locator: meta; components[0].items; comments
  snapshot_sha256: df29e5a6635a11ebc4ab98be1f7fdc2989c2374ee3f7e7e2e947eb15ced4b826
- evidence_id: atcc
  kind: primary_source
  reference: https://www.atcc.org/~/media/45E208A3191F4C7EA9B7E1063EB55303.ashx
  accessed_at: '2026-10-28T04:32:41.260557Z'
  support: partial
  summary: Full extracted one-page ATCC44 source read. Commercial agar, commercial
    broth and the separate scratch formulation are distinguished. Broth uses BD237500
    37 g with 1000 ml water. Scratch tissue input masses are not dry infusion solids.
    Final pH, sterilization temperature and storage are bounded source conditions.
  locator: page 1; Broth Medium; Brain Heart Infusion Composition; Final Product Description
  snapshot_sha256: 0d494bdb3bf7f1a710b2f0dce26e183df8b4c67e9d5b316bf4a9113bc4a2607a
- evidence_id: secondary
  kind: authority
  reference: https://microbenotes.com/brain-heart-infusion-bhi-agar/
  accessed_at: '2026-10-28T04:32:42.000923Z'
  support: partial
  summary: Only the cited article composition/principles/reference context informs
    this review. The agar table uses HM infusion powder 12.5 g/L and BHI powder 5
    g/L plus peptone, dextrose, salts and agar. It does not authenticate the exact
    composition of broth SKU237500 or the 200/250 g tissue inputs. Organism-specific
    applications and supplements are excluded.
  locator: Composition of Brain Heart Infusion (BHI) Agar; Principle; References
  snapshot_sha256: 39873c93291f575a5337e3a92e910ccd2da27845bf74e1419288088d9e3a2634
- evidence_id: uberon0000955
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?iri=http://purl.obolibrary.org/obo/UBERON_0000955
  accessed_at: '2026-10-28T04:34:37.691634Z'
  support: supports
  summary: 'Current OLS exact term: UBERON:0000955 — brain; obsolete=False. Definition,
    synonyms and available formula/charge inspected. Anatomical organ terms do not
    quantify an extracted infusion or identify its dry commercial equivalent.'
  locator: _embedded.terms[0]
  snapshot_sha256: 3a8c7e03094fbc40ba464ce7eff7b8e96d0da80ff69810a0be88721a6230bef8
- evidence_id: uberon0000948
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/uberon/terms?iri=http://purl.obolibrary.org/obo/UBERON_0000948
  accessed_at: '2026-10-28T04:34:37.708239Z'
  support: supports
  summary: 'Current OLS exact term: UBERON:0000948 — heart; obsolete=False. Definition,
    synonyms and available formula/charge inspected. Anatomical organ terms do not
    quantify an extracted infusion or identify its dry commercial equivalent.'
  locator: _embedded.terms[0]
  snapshot_sha256: 3f12566876de04720b1d477973f570c60ab1af7a33021ddad1c7ce168e46cf1a
- evidence_id: micro0000180
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http://purl.obolibrary.org/obo/MICRO_0000180
  accessed_at: '2026-10-28T04:34:37.672400Z'
  support: supports
  summary: 'Current OLS exact term: MICRO:0000180 — proteose peptone; obsolete=False.
    Definition, synonyms and available formula/charge inspected. Anatomical organ
    terms do not quantify an extracted infusion or identify its dry commercial equivalent.'
  locator: _embedded.terms[0]
  snapshot_sha256: 8cc05dbdb24058b9c2eb0c959eb5c9aaf59ee72752f012aebb5ece4e69cdbc6c
- evidence_id: chebi17634
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_17634
  accessed_at: '2026-10-28T04:34:37.672589Z'
  support: supports
  summary: 'Current OLS exact term: CHEBI:17634 — D-glucose; obsolete=False. Definition,
    synonyms and available formula/charge inspected. Anatomical organ terms do not
    quantify an extracted infusion or identify its dry commercial equivalent.'
  locator: _embedded.terms[0]
  snapshot_sha256: 6e02f3cee82012b7f630c04f122676c0029753074a4421cb005301b8bf24cedb
- evidence_id: chebi26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_26710
  accessed_at: '2026-10-28T04:34:37.743646Z'
  support: supports
  summary: 'Current OLS exact term: CHEBI:26710 — sodium chloride; obsolete=False.
    Definition, synonyms and available formula/charge inspected. Anatomical organ
    terms do not quantify an extracted infusion or identify its dry commercial equivalent.'
  locator: _embedded.terms[0]
  snapshot_sha256: b145f4ff9b90ebb993ff576d9ab35a6c10b7c42a3b99e18feffcc8d75c0e1e50
- evidence_id: chebi34683
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_34683
  accessed_at: '2026-10-28T04:34:38.277100Z'
  support: supports
  summary: 'Current OLS exact term: CHEBI:34683 — disodium hydrogenphosphate; obsolete=False.
    Definition, synonyms and available formula/charge inspected. Anatomical organ
    terms do not quantify an extracted infusion or identify its dry commercial equivalent.'
  locator: _embedded.terms[0]
  snapshot_sha256: b8fc153769cf791f5e08680678fe7df66be98486bbfbb734518f3de625596efe
- evidence_id: bd237500
  kind: search
  reference: https://www.bd.com/en-us/products-and-solutions/products/product-page.237500
  accessed_at: '2026-10-28T04:34:37.102613Z'
  support: unknown
  summary: Official product URL returned HTTP403 in direct capture. Exact dry constituent
    masses for the SKU remain unverified; search snippets are not adopted.
  locator: captured request outcome
  snapshot_sha256: 271df6538873f915561c99fcb45d3d3b85433553f785fd4f72a0a6722ebb714b
  search_scope: Bounded inspection of the captured public retrieval outcome for the
    exact reference URL. Request metadata and response bytes, when available, are
    retained in record10/sources/bd237500.json and .raw. This outcome does not establish
    exhaustive manufacturer-document availability; no unavailable content or search-result
    snippet is treated as formula evidence.
- evidence_id: bdifu237500
  kind: search
  reference: https://legacy.bd.com/europe/regulatory/Assets/IFU/Difco_BBL/237500.pdf
  accessed_at: '2026-10-28T04:34:37.061486Z'
  support: unknown
  summary: Legacy IFU host failed DNS resolution; no PDF obtained. Exact dry constituent
    masses for the SKU remain unverified; search snippets are not adopted.
  locator: captured request outcome
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  search_scope: Bounded inspection of the captured public retrieval outcome for the
    exact reference URL. Request metadata and response bytes, when available, are
    retained in record10/sources/bdifu237500.json and .raw. This outcome does not
    establish exhaustive manufacturer-document availability; no unavailable content
    or search-result snippet is treated as formula evidence.
- evidence_id: bdmanual404
  kind: search
  reference: https://static.bd.com/assets/product/Documents/Integrated%20Diagnostic%20Solutions%20%28IDS%29/DS_CM_Difco-and-BBL-culture-media-manual_UG_EN.pdf
  accessed_at: '2026-10-28T04:38:07.616770Z'
  support: unknown
  summary: Indexed official culture-media manual returned HTTP404. Exact dry constituent
    masses for the SKU remain unverified; search snippets are not adopted.
  locator: captured request outcome
  snapshot_sha256: 493fda53120050f85836032324409be6c6484f90a0755ae0c6a673ba7626818b
  search_scope: Bounded inspection of the captured public retrieval outcome for the
    exact reference URL. Request metadata and response bytes, when available, are
    retained in record10/sources/bdmanual404.json and .raw. This outcome does not
    establish exhaustive manufacturer-document availability; no unavailable content
    or search-result snippet is treated as formula evidence.
- evidence_id: bdmanual_citeseer
  kind: search
  reference: https://citeseerx.ist.psu.edu/document?doi=b9e564323726b77dd578f90be1f447da053c25f4&repid=rep1&type=pdf
  accessed_at: '2026-10-28T04:38:08.680375Z'
  support: unknown
  summary: Indexed mirror redirected to a Wayback HTML page, not the manufacturer
    PDF. Exact dry constituent masses for the SKU remain unverified; search snippets
    are not adopted.
  locator: captured request outcome
  snapshot_sha256: 6716ebe5aefafa979ce448ed664ba71b411b221695063754823caae3dc254477
  search_scope: Bounded inspection of the captured public retrieval outcome for the
    exact reference URL. Request metadata and response bytes, when available, are
    retained in record10/sources/bdmanual_citeseer.json and .raw. This outcome does
    not establish exhaustive manufacturer-document availability; no unavailable content
    or search-result snippet is treated as formula evidence.
- evidence_id: bdmanual_trios
  kind: search
  reference: https://www.trios.cz/wp-content/uploads/sites/149/2016/08/DIFCO-A-BBL-MANUAL-2.pdf
  accessed_at: '2026-10-28T04:38:07.802495Z'
  support: unknown
  summary: Python TLS certificate verification failed; no source content obtained.
    Exact dry constituent masses for the SKU remain unverified; search snippets are
    not adopted.
  locator: captured request outcome
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  search_scope: Bounded inspection of the captured public retrieval outcome for the
    exact reference URL. Request metadata and response bytes, when available, are
    retained in record10/sources/bdmanual_trios.json and .raw. This outcome does not
    establish exhaustive manufacturer-document availability; no unavailable content
    or search-result snippet is treated as formula evidence.
- evidence_id: bdmanual_trios_curl
  kind: search
  reference: https://www.trios.cz/wp-content/uploads/sites/149/2016/08/DIFCO-A-BBL-MANUAL-2.pdf
  accessed_at: '2026-10-28T04:40:02.065456Z'
  support: unknown
  summary: System curl with normal TLS reached HTTP404 HTML, not the manual. Transport
    exit0 is not a source-content success. Exact dry constituent masses for the SKU
    remain unverified; search snippets are not adopted.
  locator: captured request outcome
  snapshot_sha256: 759944f18701fa1516693f1974c8a4c237af239a4c1243268ea1bb956a788691
  search_scope: Bounded inspection of the captured public retrieval outcome for the
    exact reference URL. Request metadata and response bytes, when available, are
    retained in record10/sources/bdmanual_trios_curl.json and .raw. This outcome does
    not establish exhaustive manufacturer-document availability; no unavailable content
    or search-result snippet is treated as formula evidence.
- evidence_id: validate-schema
  kind: validation
  reference: just validate-schema data/merge_yaml/merged/Brain_Heart_Infusion_Broth.yaml
  accessed_at: '2026-10-28T04:33:08.199185Z'
  support: context_only
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed'
  locator: full stdout and stderr
  snapshot_sha256: cbc975416938a03c34fa8cc6f43b30dd539afe069d53ed198fd8293ae9265392
- evidence_id: validate-strict
  kind: validation
  reference: just validate-strict data/merge_yaml/merged/Brain_Heart_Infusion_Broth.yaml
    --out REVIEW_WORK/batch055/record10/strict.tsv --workers 1
  accessed_at: '2026-10-28T04:33:09.478649Z'
  support: context_only
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch055/record10/strict.tsv"
  locator: full stdout and stderr
  snapshot_sha256: 354185d66fa203635092c50e097d4d2577c6f91a9e959733fceb36c840695f83
- evidence_id: validate-terms
  kind: validation
  reference: just validate-terms data/merge_yaml/merged/Brain_Heart_Infusion_Broth.yaml
  accessed_at: '2026-10-28T04:33:11.244288Z'
  support: context_only
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed'
  locator: full stdout and stderr
  snapshot_sha256: f414604bb69be1489c05c8df02b1886a35dc93119e060a8094b43741f23a0c34
- evidence_id: validate-references
  kind: validation
  reference: just validate-references data/merge_yaml/merged/Brain_Heart_Infusion_Broth.yaml
  accessed_at: '2026-10-28T04:33:12.257921Z'
  support: context_only
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed'
  locator: full stdout and stderr
  snapshot_sha256: a737402251ba3612e7b4efd8e05d2eb4beab9aaa52a11e4f173429b80b03681d
- evidence_id: q-water
  kind: primary_source
  reference: https://www.atcc.org/~/media/45E208A3191F4C7EA9B7E1063EB55303.ashx
  accessed_at: '2026-10-28T04:32:41.260557Z'
  snapshot_sha256: 0d494bdb3bf7f1a710b2f0dce26e183df8b4c67e9d5b316bf4a9113bc4a2607a
  support: partial
  summary: Source input is 1000 ml water, equivalent to 1 L input volume using schema
    L; 1000 G_PER_L is not supported. Do not infer final mixed volume or convert via
    density.
  quote: DI Water…………………………………………………….1000 ml
  locator: page 1; Broth Medium water row
- evidence_id: q-infusion-1
  kind: primary_source
  reference: https://www.atcc.org/~/media/45E208A3191F4C7EA9B7E1063EB55303.ashx
  accessed_at: '2026-10-28T04:32:41.260557Z'
  snapshot_sha256: 0d494bdb3bf7f1a710b2f0dce26e183df8b4c67e9d5b316bf4a9113bc4a2607a
  support: partial
  summary: VARIABLE is acceptable for an unmeasured calf brain infusion-solids concentration.
    The source tissue input mass is not the mass of extracted dry solids or the authenticated
    commercial powder fraction.
  quote: Calf Brains, infusion from…………………………………..200 g
  locator: page 1; scratch formulation tissue row
- evidence_id: q-tissue-input-1
  kind: primary_source
  reference: https://www.atcc.org/~/media/45E208A3191F4C7EA9B7E1063EB55303.ashx
  accessed_at: '2026-10-28T04:32:41.260557Z'
  snapshot_sha256: 0d494bdb3bf7f1a710b2f0dce26e183df8b4c67e9d5b316bf4a9113bc4a2607a
  support: partial
  summary: Preserve 200 g as a scratch-recipe tissue extraction input with stage and
    source. The local g/L note asserts a denominator not explicitly established by
    the listed 1000 ml water; do not assign the tissue mass to the dry commercial
    product.
  quote: Calf Brains, infusion from…………………………………..200 g
  locator: page 1; scratch formulation tissue row
- evidence_id: q-infusion-2
  kind: primary_source
  reference: https://www.atcc.org/~/media/45E208A3191F4C7EA9B7E1063EB55303.ashx
  accessed_at: '2026-10-28T04:32:41.260557Z'
  snapshot_sha256: 0d494bdb3bf7f1a710b2f0dce26e183df8b4c67e9d5b316bf4a9113bc4a2607a
  support: partial
  summary: VARIABLE is acceptable for an unmeasured beef heart infusion-solids concentration.
    The source tissue input mass is not the mass of extracted dry solids or the authenticated
    commercial powder fraction.
  quote: Beef Hearts, infusion from………………………………….250 g
  locator: page 1; scratch formulation tissue row
- evidence_id: q-tissue-input-2
  kind: primary_source
  reference: https://www.atcc.org/~/media/45E208A3191F4C7EA9B7E1063EB55303.ashx
  accessed_at: '2026-10-28T04:32:41.260557Z'
  snapshot_sha256: 0d494bdb3bf7f1a710b2f0dce26e183df8b4c67e9d5b316bf4a9113bc4a2607a
  support: partial
  summary: Preserve 250 g as a scratch-recipe tissue extraction input with stage and
    source. The local g/L note asserts a denominator not explicitly established by
    the listed 1000 ml water; do not assign the tissue mass to the dry commercial
    product.
  quote: Beef Hearts, infusion from………………………………….250 g
  locator: page 1; scratch formulation tissue row
- evidence_id: q-mass-3
  kind: primary_source
  reference: https://www.atcc.org/~/media/45E208A3191F4C7EA9B7E1063EB55303.ashx
  accessed_at: '2026-10-28T04:32:41.260557Z'
  snapshot_sha256: 0d494bdb3bf7f1a710b2f0dce26e183df8b4c67e9d5b316bf4a9113bc4a2607a
  support: partial
  summary: Numerical mass agrees with the ATCC scratch batch. Its explicit final mixed-volume
    basis and equivalence to the named commercial SKU have not been established. The
    secondary agar g/L table cannot certify this broth SKU. Retain exact source mass
    and formulation scope; do not fabricate a new concentration.
  quote: Proteose Peptone…………………………………...………10.0 g
  locator: page 1; scratch formulation component row
- evidence_id: q-mass-4
  kind: primary_source
  reference: https://www.atcc.org/~/media/45E208A3191F4C7EA9B7E1063EB55303.ashx
  accessed_at: '2026-10-28T04:32:41.260557Z'
  snapshot_sha256: 0d494bdb3bf7f1a710b2f0dce26e183df8b4c67e9d5b316bf4a9113bc4a2607a
  support: partial
  summary: Numerical mass agrees with the ATCC scratch batch. Its explicit final mixed-volume
    basis and equivalence to the named commercial SKU have not been established. The
    secondary agar g/L table cannot certify this broth SKU. Retain exact source mass
    and formulation scope; do not fabricate a new concentration.
  quote: Dextrose……………………………………………..………..2.0 g
  locator: page 1; scratch formulation component row
- evidence_id: q-mass-5
  kind: primary_source
  reference: https://www.atcc.org/~/media/45E208A3191F4C7EA9B7E1063EB55303.ashx
  accessed_at: '2026-10-28T04:32:41.260557Z'
  snapshot_sha256: 0d494bdb3bf7f1a710b2f0dce26e183df8b4c67e9d5b316bf4a9113bc4a2607a
  support: partial
  summary: Numerical mass agrees with the ATCC scratch batch. Its explicit final mixed-volume
    basis and equivalence to the named commercial SKU have not been established. The
    secondary agar g/L table cannot certify this broth SKU. Retain exact source mass
    and formulation scope; do not fabricate a new concentration.
  quote: NaCl…………………………………………………...………5.0 g
  locator: page 1; scratch formulation component row
- evidence_id: q-mass-6
  kind: primary_source
  reference: https://www.atcc.org/~/media/45E208A3191F4C7EA9B7E1063EB55303.ashx
  accessed_at: '2026-10-28T04:32:41.260557Z'
  snapshot_sha256: 0d494bdb3bf7f1a710b2f0dce26e183df8b4c67e9d5b316bf4a9113bc4a2607a
  support: partial
  summary: Numerical mass agrees with the ATCC scratch batch. Its explicit final mixed-volume
    basis and equivalence to the named commercial SKU have not been established. The
    secondary agar g/L table cannot certify this broth SKU. Retain exact source mass
    and formulation scope; do not fabricate a new concentration.
  quote: Na2HPO4…………………………………………...………...2.5 g
  locator: page 1; scratch formulation component row
- evidence_id: q-premix
  kind: primary_source
  reference: https://www.atcc.org/~/media/45E208A3191F4C7EA9B7E1063EB55303.ashx
  accessed_at: '2026-10-28T04:32:41.260557Z'
  snapshot_sha256: 0d494bdb3bf7f1a710b2f0dce26e183df8b4c67e9d5b316bf4a9113bc4a2607a
  support: partial
  summary: Recover the source commercial-product identity and 37 g batch amount separately
    from scratch-component metadata. Do not count both premix and its constituents
    as independent additions. Plain batch G is not supported by the current concentration
    enum; preserve exact mass in preparation/evidence pending a suitable representation.
  quote: Brain Heart Infusion Broth (BD 237500)…………..…….37.0g
  locator: page 1; Broth Medium premix row
- evidence_id: q-ph
  kind: primary_source
  reference: https://www.atcc.org/~/media/45E208A3191F4C7EA9B7E1063EB55303.ashx
  accessed_at: '2026-10-28T04:32:41.260557Z'
  snapshot_sha256: 0d494bdb3bf7f1a710b2f0dce26e183df8b4c67e9d5b316bf4a9113bc4a2607a
  support: partial
  summary: Credit the existing phosphate note and expose the same supported nominal
    pH/range in recipe-level fields; TOGO 7.2–7.6 is arithmetically consistent. Do
    not silently discard the range.
  quote: Final pH 7.4 +/- 0.2
  locator: page 1; final pH
- evidence_id: q-sterilization
  kind: primary_source
  reference: https://www.atcc.org/~/media/45E208A3191F4C7EA9B7E1063EB55303.ashx
  accessed_at: '2026-10-28T04:32:41.260557Z'
  snapshot_sha256: 0d494bdb3bf7f1a710b2f0dce26e183df8b4c67e9d5b316bf4a9113bc4a2607a
  support: partial
  summary: Add only the source commercial-broth autoclaving temperature; neither primary
    source supplies a duration. This is preparation, not incubation.
  quote: Autoclave at 121ºC.
  locator: page 1; Broth Medium
- evidence_id: q-storage
  kind: primary_source
  reference: https://www.atcc.org/~/media/45E208A3191F4C7EA9B7E1063EB55303.ashx
  accessed_at: '2026-10-28T04:32:41.260557Z'
  snapshot_sha256: 0d494bdb3bf7f1a710b2f0dce26e183df8b4c67e9d5b316bf4a9113bc4a2607a
  support: partial
  summary: ATCC44 supplies a generic product storage range. It can be captured with
    exact finished-product scope; absence is not a separate major finding, and no
    storage duration or organism growth condition is inferred.
  quote: 'Recommended storage temperature: 2-8ºC.'
  locator: page 1; Final Product Description
assessments:
- assessment_id: identity
  area: identity
  topic: Accession, owner and formulation identity
  outcome: supported
  summary: The selected target is the M2426 BHI broth record, maintained by the exact
    normalized owner; ATCC44 corroborates the commercial broth identity.
  target_ids:
  - CultureMech:009009
  evidence_ids:
  - target
  - owner
  - registry
  - togo
  - atcc
  - generator
  details: The agar sibling and other BHI accessions are not interchangeable owners.
    Commercial-product identity is established independently of the unresolved detailed
    dry composition.
- assessment_id: quantities
  area: quantity
  topic: All direct amounts, tissue notes and source-only conditions
  outcome: concern
  summary: All fourteen local concentration fields and related tissue, pH and preparation
    claims were assessed. Water uses the wrong quantity kind; commercial and scratch
    claims need separate representation.
  target_ids:
  - CultureMech:009009
  evidence_ids:
  - target
  - owner
  - atcc
  - togo
  - secondary
  - schema
  dimensions:
  - name: water
    value: correct
    definition: 'data/merge_yaml/merged/Brain_Heart_Infusion_Broth.yaml::ingredients[0].concentration;
      data/normalized_yaml/bacterial/brain_heart_infusion_broth.yaml::ingredients[0].concentration;
      existing {"value": "1000", "unit": "G_PER_L"}. Source input is 1000 ml water,
      equivalent to 1 L input volume using schema L; 1000 G_PER_L is not supported.
      Do not infer final mixed volume or convert via density.'
    evidence_ids:
    - q-water
  - name: infusion-1
    value: not_quantified
    definition: 'data/merge_yaml/merged/Brain_Heart_Infusion_Broth.yaml::ingredients[1].concentration;
      data/normalized_yaml/bacterial/brain_heart_infusion_broth.yaml::ingredients[1].concentration;
      existing {"value": "variable", "unit": "VARIABLE"}. VARIABLE is acceptable for
      an unmeasured calf brain infusion-solids concentration. The source tissue input
      mass is not the mass of extracted dry solids or the authenticated commercial
      powder fraction.'
    evidence_ids:
    - q-infusion-1
  - name: tissue-input-1
    value: correct
    definition: data/merge_yaml/merged/Brain_Heart_Infusion_Broth.yaml::ingredients[1].notes;
      data/normalized_yaml/bacterial/brain_heart_infusion_broth.yaml::ingredients[1].notes;
      existing "infusion from 200 g/L; Tissue infusion - source material is calf brain
      tissue; Constituent of Brain Heart Infusion commercial product". Preserve 200
      g as a scratch-recipe tissue extraction input with stage and source. The local
      g/L note asserts a denominator not explicitly established by the listed 1000
      ml water; do not assign the tissue mass to the dry commercial product.
    evidence_ids:
    - q-tissue-input-1
  - name: infusion-2
    value: not_quantified
    definition: 'data/merge_yaml/merged/Brain_Heart_Infusion_Broth.yaml::ingredients[2].concentration;
      data/normalized_yaml/bacterial/brain_heart_infusion_broth.yaml::ingredients[2].concentration;
      existing {"value": "variable", "unit": "VARIABLE"}. VARIABLE is acceptable for
      an unmeasured beef heart infusion-solids concentration. The source tissue input
      mass is not the mass of extracted dry solids or the authenticated commercial
      powder fraction.'
    evidence_ids:
    - q-infusion-2
  - name: tissue-input-2
    value: correct
    definition: data/merge_yaml/merged/Brain_Heart_Infusion_Broth.yaml::ingredients[2].notes;
      data/normalized_yaml/bacterial/brain_heart_infusion_broth.yaml::ingredients[2].notes;
      existing "infusion from 250 g/L; Tissue infusion - source material is beef/ox
      heart tissue; Constituent of Brain Heart Infusion commercial product". Preserve
      250 g as a scratch-recipe tissue extraction input with stage and source. The
      local g/L note asserts a denominator not explicitly established by the listed
      1000 ml water; do not assign the tissue mass to the dry commercial product.
    evidence_ids:
    - q-tissue-input-2
  - name: mass-3
    value: unsupported
    definition: 'data/merge_yaml/merged/Brain_Heart_Infusion_Broth.yaml::ingredients[3].concentration;
      data/normalized_yaml/bacterial/brain_heart_infusion_broth.yaml::ingredients[3].concentration;
      existing {"value": "10.0", "unit": "G_PER_L"}. Numerical mass agrees with the
      ATCC scratch batch. Its explicit final mixed-volume basis and equivalence to
      the named commercial SKU have not been established. The secondary agar g/L table
      cannot certify this broth SKU. Retain exact source mass and formulation scope;
      do not fabricate a new concentration.'
    evidence_ids:
    - q-mass-3
  - name: mass-4
    value: unsupported
    definition: 'data/merge_yaml/merged/Brain_Heart_Infusion_Broth.yaml::ingredients[4].concentration;
      data/normalized_yaml/bacterial/brain_heart_infusion_broth.yaml::ingredients[4].concentration;
      existing {"value": "2.0", "unit": "G_PER_L"}. Numerical mass agrees with the
      ATCC scratch batch. Its explicit final mixed-volume basis and equivalence to
      the named commercial SKU have not been established. The secondary agar g/L table
      cannot certify this broth SKU. Retain exact source mass and formulation scope;
      do not fabricate a new concentration.'
    evidence_ids:
    - q-mass-4
  - name: mass-5
    value: unsupported
    definition: 'data/merge_yaml/merged/Brain_Heart_Infusion_Broth.yaml::ingredients[5].concentration;
      data/normalized_yaml/bacterial/brain_heart_infusion_broth.yaml::ingredients[5].concentration;
      existing {"value": "5.0", "unit": "G_PER_L"}. Numerical mass agrees with the
      ATCC scratch batch. Its explicit final mixed-volume basis and equivalence to
      the named commercial SKU have not been established. The secondary agar g/L table
      cannot certify this broth SKU. Retain exact source mass and formulation scope;
      do not fabricate a new concentration.'
    evidence_ids:
    - q-mass-5
  - name: mass-6
    value: unsupported
    definition: 'data/merge_yaml/merged/Brain_Heart_Infusion_Broth.yaml::ingredients[6].concentration;
      data/normalized_yaml/bacterial/brain_heart_infusion_broth.yaml::ingredients[6].concentration;
      existing {"value": "2.5", "unit": "G_PER_L"}. Numerical mass agrees with the
      ATCC scratch batch. Its explicit final mixed-volume basis and equivalence to
      the named commercial SKU have not been established. The secondary agar g/L table
      cannot certify this broth SKU. Retain exact source mass and formulation scope;
      do not fabricate a new concentration.'
    evidence_ids:
    - q-mass-6
  - name: premix
    value: add
    definition: data/merge_yaml/merged/Brain_Heart_Infusion_Broth.yaml::ingredients
      (missing commercial premix); data/normalized_yaml/bacterial/brain_heart_infusion_broth.yaml::ingredients
      (missing commercial premix); existing "absent". Recover the source commercial-product
      identity and 37 g batch amount separately from scratch-component metadata. Do
      not count both premix and its constituents as independent additions. Plain batch
      G is not supported by the current concentration enum; preserve exact mass in
      preparation/evidence pending a suitable representation.
    evidence_ids:
    - q-premix
  - name: ph
    value: evidence_only
    definition: data/merge_yaml/merged/Brain_Heart_Infusion_Broth.yaml::ingredients[6].notes;
      data/normalized_yaml/bacterial/brain_heart_infusion_broth.yaml::ingredients[6].notes;
      data/merge_yaml/merged/Brain_Heart_Infusion_Broth.yaml::ph_value; ph_range;
      data/normalized_yaml/bacterial/brain_heart_infusion_broth.yaml::ph_value; ph_range;
      existing "existing final pH 7.4 ± 0.2 note; no structured pH". Credit the existing
      phosphate note and expose the same supported nominal pH/range in recipe-level
      fields; TOGO 7.2–7.6 is arithmetically consistent. Do not silently discard the
      range.
    evidence_ids:
    - q-ph
  - name: sterilization
    value: add
    definition: data/merge_yaml/merged/Brain_Heart_Infusion_Broth.yaml::preparation_steps;
      data/normalized_yaml/bacterial/brain_heart_infusion_broth.yaml::preparation_steps;
      existing "absent". Add only the source commercial-broth autoclaving temperature;
      neither primary source supplies a duration. This is preparation, not incubation.
    evidence_ids:
    - q-sterilization
  - name: storage
    value: evidence_only
    definition: data/merge_yaml/merged/Brain_Heart_Infusion_Broth.yaml::storage_conditions;
      data/normalized_yaml/bacterial/brain_heart_infusion_broth.yaml::storage_conditions;
      existing "absent". ATCC44 supplies a generic product storage range. It can be
      captured with exact finished-product scope; absence is not a separate major
      finding, and no storage duration or organism growth condition is inferred.
    evidence_ids:
    - q-storage
  details: No nested stock or solution exists in either record. No final volume, density,
    hydrate, infusion yield or unverified manufacturer formula is assumed. Source
    batch masses are not summed into a commercial dose.
- assessment_id: grounding
  area: grounding
  topic: Primary terms, exact material forms and MIM linkage
  outcome: concern
  summary: The six existing term IDs have exact current canonical labels, but organ
    terms denote source anatomy and do not establish prepared-infusion or commercial-powder
    equivalence.
  target_ids:
  - CultureMech:009009
  evidence_ids:
  - target
  - owner
  - mim
  - mim-metadata
  - atcc
  - secondary
  - uberon0000955
  - uberon0000948
  - micro0000180
  - chebi17634
  - chebi26710
  - chebi34683
  metrics:
  - name: Primary term linkage
    value: 85.71428571428571
    unit: percent
    definition: Six of seven generated direct ingredient instances carry term.id;
      two anatomical, one MICRO and three CHEBI. Linkage is not accuracy.
    denominator: 7
    minimum: 0
    maximum: 100
  - name: MIM ingredient linkage
    value: 0
    unit: percent
    definition: Zero of seven generated direct ingredient instances carry a MIM ingredient
      identifier.
    denominator: 7
    minimum: 0
    maximum: 100
  details: The notes explicitly identify tissue origins, which is useful context.
    Preserve that scope when representing extracted ingredients. MICRO proteose peptone
    matches the stated digest; glucose and salt IDs resolve correctly. No hydrate
    is added. A FOODON candidate is not promoted without exact material verification.
- assessment_id: preparation
  area: completeness
  topic: Recipe-level pH, preparation and product context
  outcome: concern
  summary: The existing phosphate pH note is supported, but structured recipe pH and
    the source commercial-broth sterilization instruction are missing.
  target_ids:
  - CultureMech:009009
  evidence_ids:
  - target
  - owner
  - togo
  - atcc
  - q-ph
  - q-sterilization
  - q-storage
  details: The nominal pH 7.4 and range 7.2–7.6 agree. No sterilization duration,
    incubation, atmosphere, growth yield or organism scope is inferred. The optional
    storage range refers to the finished product.
- assessment_id: classification
  area: representation
  topic: Complexity, phase and ingredient roles
  outcome: supported
  summary: COMPLEX, UNDEFINED and LIQUID are consistent with a broth containing biological
    infusions and digest material.
  target_ids:
  - CultureMech:009009
  evidence_ids:
  - target
  - owner
  - atcc
  - secondary
  - micro0000180
  details: The generic notes about peptone nutrients, dextrose energy, salt osmotic
    contribution, phosphate buffering and water solvent role are bounded ingredient
    descriptions, not evidence of strain-specific essentiality or optimality.
- assessment_id: provenance
  area: provenance
  topic: Claim placement, history and generated ownership
  outcome: concern
  summary: Supplier product URLs point to a secondary agar article, and the unqualified
    researched-product-specification claim lacks a retrievable manufacturer formula.
  target_ids:
  - CultureMech:009009
  evidence_ids:
  - target
  - owner
  - secondary
  - atcc
  - history-record
  - history-target
  - history-owner
  - importer
  - generator
  - bd237500
  - bdifu237500
  - bdmanual404
  - bdmanual_citeseer
  - bdmanual_trios
  - bdmanual_trios_curl
  details: Both local layers currently agree on the substantive recipe. No generated-staleness
    defect is claimed. Preserve the append-only history; add a future curation event
    only if separately authorized. Historical reports are leads, not current source
    verification.
- assessment_id: scope
  area: scope
  topic: Growth assertions and structured adapter applicability
  outcome: supported
  summary: The record makes no organism-specific growth assertion; no organism or
    strain is inferred from the generic medium name.
  target_ids:
  - CultureMech:009009
  evidence_ids:
  - target
  - owner
  - togo
  - atcc
  details: Secondary pathogen-specific applications, supplements and incubation claims
    are excluded. No new DOI, PMID or taxonomy ID is invented.
- assessment_id: validation
  area: schema
  topic: Native deterministic checks
  outcome: supported
  summary: All four required commands passed; strict validation scanned one file with
    zero errors.
  target_ids:
  - CultureMech:009009
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
  details: The reference gate checked zero references. These results establish structural
    acceptance, not scientific source correspondence; separate OLS and source checks
    supply the scientific review.
findings:
- finding_id: F1
  issue_key: CM009009-water-volume
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Input water volume is represented as mass concentration
  description: Both records encode 1000 G_PER_L water, while TOGO and ATCC explicitly
    list 1000 ml water. Represent the input volume without assuming final mixed volume
    or density.
  target_ids:
  - CultureMech:009009
  field_paths:
  - ingredients[0].concentration
  evidence_ids:
  - target
  - owner
  - q-water
  - schema
  - importer
  rule_id: concentration-evidence-contract
  native_severity: major
  normalization_reason: Material source or representation defect affecting interpretation
    of the formulation.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_broth.yaml
    role: maintained normalized source
- finding_id: F2
  issue_key: CM009009-commercial-scratch-scope
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Commercial premix and scratch formulation are conflated
  description: The commercial broth requires an explicitly named 37 g BD237500 product.
    Local records omit that addition and attach its SKU to separate scratch-style
    constituents, including anatomical tissue inputs. The inspected ATCC source labels
    its scratch route separately; the cited agar article does not authenticate this
    broth product decomposition. Preserve alternatives and provenance without double
    counting or replacing the formula silently.
  target_ids:
  - CultureMech:009009
  field_paths:
  - ingredients
  - ingredients[*].supplier_catalog
  - ingredients[1].notes
  - ingredients[2].notes
  - notes
  evidence_ids:
  - target
  - owner
  - atcc
  - togo
  - secondary
  - q-premix
  - q-tissue-input-1
  - q-tissue-input-2
  rule_id: concentration-evidence-contract
  native_severity: major
  normalization_reason: Material source or representation defect affecting interpretation
    of the formulation.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_broth.yaml
    role: maintained normalized source
- finding_id: F3
  issue_key: CM009009-batch-amount-basis
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Component rates claim an unresolved final-volume basis
  description: The tissue notes and four component concentration rows reuse scratch
    batch digits with g/L units. ATCC lists the input amounts with 1000 ml water,
    without an explicit final mixed-volume instruction. The secondary agar rates do
    not establish exact broth-SKU equivalence. Preserve source batch quantity and
    stage; do not fabricate conversion factors, tissue yield or commercial powder
    masses.
  target_ids:
  - CultureMech:009009
  field_paths:
  - ingredients[1].notes
  - ingredients[2].notes
  - ingredients[3:7].concentration
  evidence_ids:
  - atcc
  - secondary
  - schema
  - q-mass-3
  - q-mass-4
  - q-mass-5
  - q-mass-6
  rule_id: concentration-evidence-contract
  native_severity: major
  normalization_reason: Material source or representation defect affecting interpretation
    of the formulation.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_broth.yaml
    role: maintained normalized source
- finding_id: F4
  issue_key: CM009009-source-conditions
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Source conditions are not represented at recipe level
  description: The phosphate note already preserves final pH 7.4 ± 0.2, which must
    be credited. Recipe-level pH fields and preparation steps remain absent, so the
    explicit commercial-broth autoclaving temperature is lost to structured consumers.
    Preserve nominal pH and range; do not invent a duration.
  target_ids:
  - CultureMech:009009
  field_paths:
  - ph_value
  - ph_range
  - preparation_steps
  - ingredients[6].notes
  evidence_ids:
  - target
  - owner
  - q-ph
  - q-sterilization
  rule_id: P3.4/P3.6
  native_severity: P3
  normalization_reason: Escalated from native P3 to major because source-explicit
    preparation is absent and the recipe conditions are unavailable to structured
    consumers; the existing pH note is acknowledged.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_broth.yaml
    role: maintained normalized source
- finding_id: F5
  issue_key: CM009009-claim-evidence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Source support and supplier scope are not attached to individual claims
  description: The notes retain source URLs, but ingredient/preparation evidence and
    reference collections do not identify the exact claim scope. A secondary agar
    page is used as the supplier product URL and the broad product-specification assertion
    exceeds the inspected evidence. Add exact primary-source support while keeping
    unresolved manufacturer composition explicit.
  target_ids:
  - CultureMech:009009
  field_paths:
  - ingredients[*].evidence
  - ingredients[*].supplier_catalog.product_url
  - evidence
  - references
  - notes
  evidence_ids:
  - target
  - owner
  - atcc
  - secondary
  - validate-references
  rule_id: P4.3
  native_severity: P4
  normalization_reason: Recoverable provenance gap that does not independently alter
    the formulation.
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_broth.yaml
    role: maintained normalized source
actions:
- action_id: A1
  description: Correct the maintained water quantity to the explicit input volume
    and cite its source.
  finding_ids:
  - F1
  target_ids:
  - CultureMech:009009
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_broth.yaml
    role: maintained normalized source
  acceptance_checks:
  - Use schema-supported volume semantics; retain 1000 ml = 1 L as input volume, with
    no density conversion or final-volume claim.
  - Run the four native recipe validators on the corrected owner.
- action_id: A2
  description: Represent the source commercial broth identity and batch dose separately
    from the scratch route; resolve the mass/volume representation before changing
    scalar rates.
  finding_ids:
  - F2
  - F3
  target_ids:
  - CultureMech:009009
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_broth.yaml
    role: maintained normalized source
  acceptance_checks:
  - The 37 g commercial batch input, two tissue extraction inputs and four scratch
    masses remain separately sourced, with no double counting.
  - A manufacturer formulation must be inspected before claiming exact SKU constituent
    equivalence; unknown dry infusion masses remain unknown.
  - Preserve batch masses in preparation/evidence when the current enum cannot express
    them. Any schema extension requires its separately governed implementation and
    generated products.
  - Recheck all direct amount and tissue-note claims and run the four native recipe
    validators.
- action_id: A3
  description: Expose supported pH and commercial-broth preparation conditions in
    the normalized owner.
  finding_ids:
  - F4
  target_ids:
  - CultureMech:009009
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_broth.yaml
    role: maintained normalized source
  acceptance_checks:
  - Credit the existing pH note, retain nominal value and supported range, and distinguish
    preparation from incubation.
  - Capture only the source-explicit sterilization temperature; leave unreported duration
    unspecified.
- action_id: A4
  description: Attach exact source excerpts at the narrowest claim and correct supplier-reference
    scope.
  finding_ids:
  - F5
  target_ids:
  - CultureMech:009009
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_broth.yaml
    role: maintained normalized source
  acceptance_checks:
  - Distinguish collection recipe, scratch formulation, secondary agar discussion
    and authenticated manufacturer specification.
  - Keep source access limits visible; append a curation event only with actual authorized
    curation, preserving earlier entries.
- action_id: A5
  description: Regenerate the target after maintained-owner curation and compare the
    resulting formulation to its sources.
  finding_ids:
  - F1
  - F2
  - F3
  - F4
  - F5
  target_ids:
  - CultureMech:009009
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/brain_heart_infusion_broth.yaml
    role: maintained normalized source
  - repository: CultureBotAI/CultureMech
    path: src/culturemech/merge/merger.py
    role: generated merge implementation
  acceptance_checks:
  - Run just verify-merges and just audit-merge-freshness, then the four native validators;
    inspect commercial/scratch boundaries in the generated record.
  depends_on:
  - A1
  - A2
  - A3
  - A4
  generator: src/culturemech/merge/merge_recipes.py
limitations:
- No retrievable manufacturer manual or IFU verified the detailed dry formula for
  BD237500. Official endpoints were blocked/unavailable and mirrors did not yield
  the document; search snippets were not adopted.
- No final mixed volume, tissue extraction yield, density, hydration state beyond
  the literal source or sterilization duration was established. No conversion requiring
  these values was performed.
- The primary page was read as complete extracted text; the independent peer checked
  its visual layout. This review does not establish organism-specific growth or experimental
  optimality.
- The standalone history-tree validator is not a focused embedded-history check; histories
  were read and compared without modification.
notes:
- Ignored-inclusive searches covered selected identifiers/slugs in normalized records
  and historical reports, plus supplier/composition writer strings in scripts and
  src. The ownership finding does not claim a global absence outside those bounds.
- Source captures retain URLs, actual UTC access times and SHA256 hashes in the durable
  batch work area. The quantity inventory has 13 decisions covering all fourteen local
  concentration fields and related claims.
- Current substantive owner/target agreement is credited. No recipe, source history
  or generated product was edited.
tags:
- source-review
- generated-record
- togo
- bhi
- batch-055
```
