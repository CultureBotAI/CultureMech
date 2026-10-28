# Non-operational review: Chocolate agar

- Review: 20261028T084509Z-culturemech-008860-nonoperational-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T08:34:08.440835Z
- Finished UTC: 2026-10-28T08:45:09.930779Z
- Reviewer: Codex tsb_source_check (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Partial non-operational review of exact Chocolate agar identity, citation boundaries and structure. All recipe and culture assertions remain unchanged and unassessed.

## Scope And Provenance

Non-operational identity, bibliography, provenance and structure only.

Selection: Authoritative batch061 index08
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:008860 | data/merge_yaml/merged/CHOCOLATE_AGAR.yaml | generated | chocolate_agar |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Canonical schema | passed | True | CultureMech:008860 | Actual exit0; no formal validation/save by author. |
| Canonical strict | passed | True | CultureMech:008860 | Actual exit0; no formal validation/save by author. |
| Canonical terms | passed | True | CultureMech:008860 | Actual exit0; no formal validation/save by author. |
| Canonical references | passed | True | CultureMech:008860 | Actual exit0; no formal validation/save by author. |

## Scientific And Domain Assessments

### Record and citation identity

identity: supported. Targets: CultureMech:008860.

Stable selected and owner identities agree with exact TOGO M2274. Fresh metadata identifies the cited Slots1981 publication; no named-strain growth or full recipe equivalence is inferred.

### Current and prior source limits

provenance: concern. Targets: CultureMech:008860.

Current histories are preserved. Three historical reports were read only for header, identity and provenance; their operational conclusions are not adopted. Source comments contain distinct bibliographic leads not represented with claim-level scope in the current record.

### Non-operational boundary

scope: not_applicable. Targets: CultureMech:008860.

Specific clinical-source context limits this review to bibliography, identity, provenance and record structure. No culture, pathogenicity, infective-stage, toxin, formulation, supplied-form or preparation improvement is assessed or proposed.

### Unchanged private inventory

quantity: not_applicable. Targets: CultureMech:008860.

22 existing concentration fields are preserved unchanged in a private structural census, all not_assessed. No operational values or source-derived corrections are reproduced in the review.

### Existing identifier structure

grounding: unknown. Targets: CultureMech:008860.

Exact existing slots and current MIM membership/absence are inventoried only. No external chemical ontology or source-form evaluation was performed for this restricted record; native term success is not scientific chemical certification.

### Once-only canonical checks

schema: supported. Targets: CultureMech:008860.

All four original checks passed; strict has zero errors and references zero checks. These diagnostic outcomes are independent of excluded operational correctness.

## Findings

### f1: Imported record lacks explicit bibliographic and source-context boundaries

minor / open / confirmed; issue key: culturemech-008860-bibliographic-scope.

The current record retains the TOGO landing identity but not its citation-level provenance. Exact TOGO comments name A. aphrophilus, a PMID7026598 reference, and a separate Dogan1999 citation. Fresh ESummary identifies PMID7026598 as Slots1981, DOI10.1128/jcm.14.3.288-294.1981; it must not be conflated with the separately mentioned1999 work. This verifies bibliographic identity only and does not establish which whole formulation or operational passage belongs to either publication. Existing commercial-source notes also remain unverified provenance, not primary recipe authentication.

## Recommended Actions And Acceptance Checks

### a1

Add only verified bibliographic metadata with an explicit source-context limitation. Keep the two citation leads distinct and do not infer whole-recipe authentication or add operational growth/formulation assertions. Preserve all current recipe fields and historical events unchanged.

- PMID7026598, exact title/author/year/DOI and metadata-only scope agree with retained authority.
- No ingredient, concentration, stock, preparation, condition or cultivation correction is propagated; no blanket regeneration that transfers operational changes.
- Preserve historical events and append any independently authorized metadata change; recheck structure only.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| target | data/merge_yaml/merged/CHOCOLATE_AGAR.yaml; Complete exact file | context_only | Complete target read; scientific operational assertions excluded. |
| owner | data/normalized_yaml/bacterial/TOGO_M2274_Chocolate_agar.yaml; Complete exact file | context_only | Complete exact owner read; existing operational data unchanged. |
| quantities | REVIEW_WORK/batch061/record08/quantity-inventory.json; Complete exact file | context_only | Private structural or bibliographic provenance evidence only. |
| scalars | REVIEW_WORK/batch061/record08/field-census.json; Complete exact file | context_only | Private structural or bibliographic provenance evidence only. |
| numeric | REVIEW_WORK/batch061/record08/numeric-field-census.json; Complete exact file | context_only | Private structural or bibliographic provenance evidence only. |
| groundings | REVIEW_WORK/batch061/record08/grounding-inventory.json; Complete exact file | context_only | Private structural or bibliographic provenance evidence only. |
| history | REVIEW_WORK/batch061/record08/history-inventory.json; Complete exact file | context_only | Private structural or bibliographic provenance evidence only. |
| old-reports | REVIEW_WORK/batch061/record08/historical-report-scope.json; Complete exact file | context_only | Private structural or bibliographic provenance evidence only. |
| bibliography | REVIEW_WORK/batch061/record08/bibliographic-identity.json; Complete exact file | context_only | Private structural or bibliographic provenance evidence only. |
| mim | src/culturemech/data/mediaingredientmech/label_index.csv; Matching rows in grounding sidecar | context_only | Exact current identifier rows, not source-form verification. |
| mim-meta | src/culturemech/data/mediaingredientmech/label_index.metadata.json; Complete metadata | context_only | Exact packaged snapshot commit, checksum and9077 rows. |
| writer-merger | src/culturemech/merge/merger.py; merge_group | context_only | Current singleton merge copies maintained input. No blanket regeneration or operational change is authorized. |
| writer-formulation | src/culturemech/merge/formulation.py; Full scientific equality guards | context_only | Current conservative multi-record equality is not proof of source identity or historical execution. |
| togo2274 | https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2274; meta identity and comment citation/context only; operational contents excluded | context_only | Fresh exact TOGO record identifies chocolate agar and exposes named clinical-source context and separate citation leads. Retrieval occurred for identity screening; no operational content is endorsed. |
| pmid7026598 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&amp;id=7026598&amp;retmode=json; Bibliographic ESummary fields only | context_only | Fresh exact citation metadata only; no primary Methods or recipe equivalence assessed. |
| check-schema | REVIEW_WORK/batch061/record08/schema-result.json | supports | Original once-only canonical diagnostic, full argv/times/streams retained; reference zero checks does not authenticate scientific assertions. |
| check-strict | REVIEW_WORK/batch061/record08/strict-result.json | supports | Original once-only canonical diagnostic, full argv/times/streams retained; reference zero checks does not authenticate scientific assertions. |
| check-terms | REVIEW_WORK/batch061/record08/terms-result.json | supports | Original once-only canonical diagnostic, full argv/times/streams retained; reference zero checks does not authenticate scientific assertions. |
| check-references | REVIEW_WORK/batch061/record08/references-result.json | supports | Original once-only canonical diagnostic, full argv/times/streams retained; reference zero checks does not authenticate scientific assertions. |

## Limits And Additional Notes

- Explicitly partial review with scientific_review:false. All operational concentrations, supplied forms, stocks, culture conditions and preparation remain unassessed and unchanged.
- The exact TOGO payload was captured during identity screening before the named clinical context was recognized. Its operational content is not endorsed or used to propose corrections. No full cited article, Methods or additional operational source was acquired.
- PubMed ESummary supports bibliographic identity only; separate TOGO comment citations cannot be conflated or treated as whole-table evidence.
- Prior report operational tables and recommendations were deliberately excluded; historical native/source claims are not newly executed or recovered.
- Current packaged MIM snapshot 6643131b0f12ab40b66f98135245fca04027e0e9 is structural context only, not historical or live-catalog validity.
- No formal validation/save, source edits, STATE/Git changes or publication performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T084509Z-culturemech-008860-nonoperational-review
kind: record
repository: CultureBotAI/CultureMech
title: 'Non-operational review: Chocolate agar'
started_at: '2026-10-28T08:34:08.440835Z'
finished_at: '2026-10-28T08:45:09.930779Z'
reviewer:
  identity: Codex tsb_source_check
  kind: agent
  model: GPT-6
  independence: independent
  independence_basis: Independent current identity, bibliography, structural/provenance
    review; operational science excluded.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: false
summary: Partial non-operational review of exact Chocolate agar identity, citation
  boundaries and structure. All recipe and culture assertions remain unchanged and
  unassessed.
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
  - path: conf/oak_config.yaml
    sha256: c0ef0808662f57dc2f57ce9b405485830503653aceee1451c9e1dae42f9e7021
    role: context
  - path: conf/record_review.yaml
    sha256: a76531e51214e559c97ab748a4cba169f8a9598ce6e3664518489b43dfc9bf88
    role: context
  - path: data/culturemech_id_registry.tsv
    sha256: 0d059720f5c474b63daff8d5010fc56942a5a3ac30761ee75ce9e84801d555a5
    role: context
  - path: data/merge_yaml/merged/CHOCOLATE_AGAR.yaml
    sha256: 3d5d386586ad28f195451b786e779fa30649152b96b7121548948359a69df791
    role: target
  - path: data/normalized_yaml/bacterial/TOGO_M2274_Chocolate_agar.yaml
    sha256: 3855cab0818db5c1b0097d65040d38c660be44c28676285342483292d4ec7866
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
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/CHOCOLATE_AGAR.md
    sha256: 993c722adb84fe4e1109eb010835b12d6b098a43010e5520d5041218c40591e9
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/TOGO_M2274_Chocolate_agar.md
    sha256: 8e735453d956464e4c2a9251569b4eb9ac56fb16ff69fd9cde768c64e134fabb
    role: context
  - path: reports/yaml_record_review/20260922T072653Z-CHOCOLATE_AGAR.md
    sha256: 36df5a66cd552c5d9a7257b27e7ec90ae6de516ecbd360fecf6c2411762c6e3a
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/apply_cocktail_nesting.py
    sha256: a1914a040ca02c86633aae11ed8a52a0ea91ba157a8240da2232c4ae652d61ab
    role: context
  - path: scripts/apply_mim_groundings.py
    sha256: 3c6ab80c461a2abcfd8e68541ca0904d2f4e33f635976f76015b067ca137292f
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
  - path: scripts/enrich_with_chebi.py
    sha256: f18dd6e4317de76cb7379f6c9c6227f9af884c27a0761d7f64143aaf74d8e1dc
    role: context
  - path: scripts/enrich_with_kg_microbe_matches.py
    sha256: 61351f99ef2cb0cef03e74ad92d21dcf3b38df77a06602bdac814974e7728eeb
    role: context
  - path: scripts/enrich_with_mediaingredientmech.py
    sha256: 6357c9d621c3d6e32b28b2982afedfaed384830cea1602a775b0a5f0852c015e
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
  - path: scripts/migrate_mgso4_heptahydrate_term.py
    sha256: 6acb9d5164ad381c288f031fb34045036e3fd2283e559f1ad8ccd1a4687fb4ce
    role: context
  - path: scripts/migrate_ph_range.py
    sha256: 98b1ee128d70767e7409eeb8a331f1a31cfa016f0013225f508fd3fc89551fb1
    role: context
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
    role: context
  - path: scripts/normalize_media_names_to_snake_case.py
    sha256: 59bd842b1982b7d62af9db3fe280df576d8c4ae2e9ee411bf2e52523355f95de
    role: context
  - path: scripts/promote_komodo_volume_candidates.py
    sha256: 2423b7e2e04011b31d21eac939714a2db4380f033a69094325dc567e44929cd2
    role: context
  - path: scripts/refill_term_labels.py
    sha256: 8eee4532e4a71d120532db511733bde974ab1b179e50cb1ea51d66c3870f3cb9
    role: context
  - path: scripts/remove_invalid_chebi_ids.py
    sha256: a6c2f7577812081230fd5fe008182c09eace4ef7818857f8026ec8d5e0b760e0
    role: context
  - path: scripts/repair_ccap_instruction_rows.py
    sha256: eb1a4c8c46eb45dcdde6a5d2f0f6833792dd0802c45603eefa1b63a3ff96fca5
    role: context
  - path: scripts/repair_ccap_sources_score10.py
    sha256: f518688ae99e154f490af337dab30b9038657a814db72861e0b53658a2541ae6
    role: context
  - path: scripts/repair_mediadive_jcm_structure.py
    sha256: 5bff4c2d1900051bdea1b8e0f655049147c85cc9c61da4c348a6d60a8d0fd509
    role: context
  - path: scripts/repair_official_simple_score20.py
    sha256: 689ef1b008090eba5ce1ef4083ef25245565ba2f3ff8b9a34372c049590e75f1
    role: context
  - path: scripts/repair_togo_commercial_score20.py
    sha256: d5e34df82098bf7558fcdd103d24d00218513488ea860952881c73240596c822
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
    role: context
  - path: src/culturemech/import/ccap_importer.py
    sha256: c579c1d8fb62b96e739e5ee5c963453753ebca0bbf50996fb0f0d6eedd75c9ac
    role: context
  - path: src/culturemech/import/komodo_web_importer.py
    sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
    role: context
  - path: src/culturemech/import/mediadive_importer.py
    sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
    role: context
  - path: src/culturemech/import/togo_importer.py
    sha256: 5aead42443f27b0f7808fbe98f24a04c1e82261b37ca12c80fa4abef9dfc6b8a
    role: context
  - path: src/culturemech/match/kg_media_matcher.py
    sha256: 43f01f4b6e9285a60db437d7903646545ad6a6548e6b85f4478eb9b0e1b74e33
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
  - path: src/culturemech/validation/schema_defaulter.py
    sha256: 8b029526d93a39f1078c434e8dd0cf76cd19b2800fce765c9c390043eff38c53
    role: context
scope:
  description: Non-operational identity, bibliography, provenance and structure only.
  selection: Authoritative batch061 index08
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CultureMech:008860
targets:
- target_id: CultureMech:008860
  path: data/merge_yaml/merged/CHOCOLATE_AGAR.yaml
  label: chocolate_agar
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2274_Chocolate_agar.yaml
    role: maintained source
  ownership_note: Exact declared maintained contributors resolved against stable identity;
    stocks and other source variants remain scoped comparisons.
checks:
- check_id: schema
  name: Canonical schema
  status: passed
  required: true
  summary: Actual exit0; no formal validation/save by author.
  target_ids:
  - CultureMech:008860
  command: just validate-schema data/merge_yaml/merged/CHOCOLATE_AGAR.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-schema
- check_id: strict
  name: Canonical strict
  status: passed
  required: true
  summary: Actual exit0; no formal validation/save by author.
  target_ids:
  - CultureMech:008860
  command: just validate-strict data/merge_yaml/merged/CHOCOLATE_AGAR.yaml --out REVIEW_WORK/batch061/record08/strict.tsv
    --workers 1 --quiet
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-strict
- check_id: terms
  name: Canonical terms
  status: passed
  required: true
  summary: Actual exit0; no formal validation/save by author.
  target_ids:
  - CultureMech:008860
  command: just validate-terms data/merge_yaml/merged/CHOCOLATE_AGAR.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-terms
- check_id: references
  name: Canonical references
  status: passed
  required: true
  summary: Actual exit0; no formal validation/save by author.
  target_ids:
  - CultureMech:008860
  command: just validate-references data/merge_yaml/merged/CHOCOLATE_AGAR.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-references
evidence:
- evidence_id: target
  kind: record_content
  reference: data/merge_yaml/merged/CHOCOLATE_AGAR.yaml
  locator: Complete exact file
  accessed_at: '2026-10-28T08:45:09.928156Z'
  support: context_only
  summary: Complete target read; scientific operational assertions excluded.
  snapshot_sha256: 3d5d386586ad28f195451b786e779fa30649152b96b7121548948359a69df791
- evidence_id: owner
  kind: record_content
  reference: data/normalized_yaml/bacterial/TOGO_M2274_Chocolate_agar.yaml
  locator: Complete exact file
  accessed_at: '2026-10-28T08:45:09.928315Z'
  support: context_only
  summary: Complete exact owner read; existing operational data unchanged.
  snapshot_sha256: 3855cab0818db5c1b0097d65040d38c660be44c28676285342483292d4ec7866
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch061/record08/quantity-inventory.json
  locator: Complete exact file
  accessed_at: '2026-10-28T08:45:09.928341Z'
  support: context_only
  summary: Private structural or bibliographic provenance evidence only.
  snapshot_sha256: 704f50f316d991e7b2f895ce5b544ec11a54d631d05586ea8055c492684b2008
- evidence_id: scalars
  kind: record_content
  reference: REVIEW_WORK/batch061/record08/field-census.json
  locator: Complete exact file
  accessed_at: '2026-10-28T08:45:09.928365Z'
  support: context_only
  summary: Private structural or bibliographic provenance evidence only.
  snapshot_sha256: dd5b83a7cf5c0118274714dbb07b77aeaff20d4b9cebafc52bf16285f9b09c74
- evidence_id: numeric
  kind: record_content
  reference: REVIEW_WORK/batch061/record08/numeric-field-census.json
  locator: Complete exact file
  accessed_at: '2026-10-28T08:45:09.928406Z'
  support: context_only
  summary: Private structural or bibliographic provenance evidence only.
  snapshot_sha256: eaab3e87fb88053c20630170b328fdcdd52040e77add7eae676699edc4eca1f3
- evidence_id: groundings
  kind: record_content
  reference: REVIEW_WORK/batch061/record08/grounding-inventory.json
  locator: Complete exact file
  accessed_at: '2026-10-28T08:45:09.928434Z'
  support: context_only
  summary: Private structural or bibliographic provenance evidence only.
  snapshot_sha256: 319a6e3878c3cdf08c333511614bdba257aa12ac3e4dcdade8e4f5128472c61f
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch061/record08/history-inventory.json
  locator: Complete exact file
  accessed_at: '2026-10-28T08:45:09.928484Z'
  support: context_only
  summary: Private structural or bibliographic provenance evidence only.
  snapshot_sha256: a2866168df695fd953dc0eb0704d8810a6913a0a214a86ee65eda0a7fc009089
- evidence_id: old-reports
  kind: record_content
  reference: REVIEW_WORK/batch061/record08/historical-report-scope.json
  locator: Complete exact file
  accessed_at: '2026-10-28T08:45:09.928506Z'
  support: context_only
  summary: Private structural or bibliographic provenance evidence only.
  snapshot_sha256: f1e3e02e21b8c04690a5330e916851c052d20539d5506b05e0fe20621b54f5da
- evidence_id: bibliography
  kind: record_content
  reference: REVIEW_WORK/batch061/record08/bibliographic-identity.json
  locator: Complete exact file
  accessed_at: '2026-10-28T08:45:09.928525Z'
  support: context_only
  summary: Private structural or bibliographic provenance evidence only.
  snapshot_sha256: 30a752ad835ac1350162ba09fc33db781bfaaba3e796a2205cef2d78a0134405
- evidence_id: mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Matching rows in grounding sidecar
  accessed_at: '2026-10-28T08:45:09.928544Z'
  support: context_only
  summary: Exact current identifier rows, not source-form verification.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: mim-meta
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.metadata.json
  locator: Complete metadata
  accessed_at: '2026-10-28T08:45:09.928842Z'
  support: context_only
  summary: Exact packaged snapshot commit, checksum and9077 rows.
  snapshot_sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
- evidence_id: writer-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: merge_group
  accessed_at: '2026-10-28T08:45:09.928862Z'
  support: context_only
  summary: Current singleton merge copies maintained input. No blanket regeneration
    or operational change is authorized.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Full scientific equality guards
  accessed_at: '2026-10-28T08:45:09.928884Z'
  support: context_only
  summary: Current conservative multi-record equality is not proof of source identity
    or historical execution.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: togo2274
  kind: database
  reference: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2274
  locator: meta identity and comment citation/context only; operational contents excluded
  accessed_at: '2026-10-28T08:34:08.059478Z'
  support: context_only
  summary: Fresh exact TOGO record identifies chocolate agar and exposes named clinical-source
    context and separate citation leads. Retrieval occurred for identity screening;
    no operational content is endorsed.
  snapshot_sha256: 3475973197d9b47d081beb7d395964ba14924f35e1732362f869feba53e65484
- evidence_id: pmid7026598
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=7026598&retmode=json
  locator: Bibliographic ESummary fields only
  accessed_at: '2026-10-28T08:39:10.112108Z'
  support: context_only
  summary: Fresh exact citation metadata only; no primary Methods or recipe equivalence
    assessed.
  snapshot_sha256: 654851edfcc7f16b7f1f32a69fa480a2c3a50cf0d547d3182268da3cc8354262
- evidence_id: check-schema
  kind: validation
  reference: REVIEW_WORK/batch061/record08/schema-result.json
  accessed_at: '2026-10-28T08:34:10.474345Z'
  support: supports
  summary: Original once-only canonical diagnostic, full argv/times/streams retained;
    reference zero checks does not authenticate scientific assertions.
  snapshot_sha256: 628d0240c25ab7f5e2b5ab32fde4375046ce7296276f3f5205f06651a56ae589
- evidence_id: check-strict
  kind: validation
  reference: REVIEW_WORK/batch061/record08/strict-result.json
  accessed_at: '2026-10-28T08:34:12.136285Z'
  support: supports
  summary: Original once-only canonical diagnostic, full argv/times/streams retained;
    reference zero checks does not authenticate scientific assertions.
  snapshot_sha256: cba372c771ddb41604da0d7f5d145ae0e76cd0aca317e2cc3a53772fef480f92
- evidence_id: check-terms
  kind: validation
  reference: REVIEW_WORK/batch061/record08/terms-result.json
  accessed_at: '2026-10-28T08:34:14.389494Z'
  support: supports
  summary: Original once-only canonical diagnostic, full argv/times/streams retained;
    reference zero checks does not authenticate scientific assertions.
  snapshot_sha256: ed2c8063852628dc0a2e42c6ebc9750ac5c625c6b2ac506df016c443517d9040
- evidence_id: check-references
  kind: validation
  reference: REVIEW_WORK/batch061/record08/references-result.json
  accessed_at: '2026-10-28T08:34:15.646447Z'
  support: supports
  summary: Original once-only canonical diagnostic, full argv/times/streams retained;
    reference zero checks does not authenticate scientific assertions.
  snapshot_sha256: af506d5134ac2d6460c5cdba163e8827b17db5648081d06e47c534c8a3033419
assessments:
- assessment_id: identity
  area: identity
  topic: Record and citation identity
  outcome: supported
  summary: Stable selected and owner identities agree with exact TOGO M2274. Fresh
    metadata identifies the cited Slots1981 publication; no named-strain growth or
    full recipe equivalence is inferred.
  target_ids:
  - CultureMech:008860
  evidence_ids:
  - target
  - owner
  - togo2274
  - bibliography
- assessment_id: provenance
  area: provenance
  topic: Current and prior source limits
  outcome: concern
  summary: Current histories are preserved. Three historical reports were read only
    for header, identity and provenance; their operational conclusions are not adopted.
    Source comments contain distinct bibliographic leads not represented with claim-level
    scope in the current record.
  target_ids:
  - CultureMech:008860
  evidence_ids:
  - history
  - old-reports
  - togo2274
  - bibliography
- assessment_id: scope
  area: scope
  topic: Non-operational boundary
  outcome: not_applicable
  summary: Specific clinical-source context limits this review to bibliography, identity,
    provenance and record structure. No culture, pathogenicity, infective-stage, toxin,
    formulation, supplied-form or preparation improvement is assessed or proposed.
  target_ids:
  - CultureMech:008860
  evidence_ids:
  - target
  - togo2274
- assessment_id: quantity
  area: quantity
  topic: Unchanged private inventory
  outcome: not_applicable
  summary: 22 existing concentration fields are preserved unchanged in a private structural
    census, all not_assessed. No operational values or source-derived corrections
    are reproduced in the review.
  target_ids:
  - CultureMech:008860
  evidence_ids:
  - quantities
  - numeric
- assessment_id: grounding
  area: grounding
  topic: Existing identifier structure
  outcome: unknown
  summary: Exact existing slots and current MIM membership/absence are inventoried
    only. No external chemical ontology or source-form evaluation was performed for
    this restricted record; native term success is not scientific chemical certification.
  target_ids:
  - CultureMech:008860
  evidence_ids:
  - groundings
  - mim
  - mim-meta
  - check-terms
- assessment_id: schema
  area: schema
  topic: Once-only canonical checks
  outcome: supported
  summary: All four original checks passed; strict has zero errors and references
    zero checks. These diagnostic outcomes are independent of excluded operational
    correctness.
  target_ids:
  - CultureMech:008860
  evidence_ids:
  - check-schema
  - check-strict
  - check-terms
  - check-references
findings:
- finding_id: f1
  issue_key: culturemech-008860-bibliographic-scope
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Imported record lacks explicit bibliographic and source-context boundaries
  description: The current record retains the TOGO landing identity but not its citation-level
    provenance. Exact TOGO comments name A. aphrophilus, a PMID7026598 reference,
    and a separate Dogan1999 citation. Fresh ESummary identifies PMID7026598 as Slots1981,
    DOI10.1128/jcm.14.3.288-294.1981; it must not be conflated with the separately
    mentioned1999 work. This verifies bibliographic identity only and does not establish
    which whole formulation or operational passage belongs to either publication.
    Existing commercial-source notes also remain unverified provenance, not primary
    recipe authentication.
  target_ids:
  - CultureMech:008860
  field_paths:
  - notes
  - references
  evidence_ids:
  - target
  - owner
  - togo2274
  - pmid7026598
  - bibliography
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2274_Chocolate_agar.yaml
    role: maintained source
  rule_id: review-yaml-record/provenance
  native_severity: P3
  normalization_reason: Bounded citation/provenance completeness issue; no operational
    defect or culture improvement adjudicated.
actions:
- action_id: a1
  description: Add only verified bibliographic metadata with an explicit source-context
    limitation. Keep the two citation leads distinct and do not infer whole-recipe
    authentication or add operational growth/formulation assertions. Preserve all
    current recipe fields and historical events unchanged.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:008860
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/TOGO_M2274_Chocolate_agar.yaml
    role: maintained source
  acceptance_checks:
  - PMID7026598, exact title/author/year/DOI and metadata-only scope agree with retained
    authority.
  - No ingredient, concentration, stock, preparation, condition or cultivation correction
    is propagated; no blanket regeneration that transfers operational changes.
  - Preserve historical events and append any independently authorized metadata change;
    recheck structure only.
  generator: Explicit metadata-only curation
limitations:
- Explicitly partial review with scientific_review:false. All operational concentrations,
  supplied forms, stocks, culture conditions and preparation remain unassessed and
  unchanged.
- The exact TOGO payload was captured during identity screening before the named clinical
  context was recognized. Its operational content is not endorsed or used to propose
  corrections. No full cited article, Methods or additional operational source was
  acquired.
- PubMed ESummary supports bibliographic identity only; separate TOGO comment citations
  cannot be conflated or treated as whole-table evidence.
- Prior report operational tables and recommendations were deliberately excluded;
  historical native/source claims are not newly executed or recovered.
- Current packaged MIM snapshot 6643131b0f12ab40b66f98135245fca04027e0e9 is structural
  context only, not historical or live-catalog validity.
- No formal validation/save, source edits, STATE/Git changes or publication performed
  by this author.
```
