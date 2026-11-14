# C/10 medium: supported base quantities, unresolved DSM 435 variant and stale generated evidence

- Review: 20261028T133015Z-batch068-record09-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T13:13:47.586807Z
- Finished UTC: 2026-10-28T13:30:15.612057Z
- Reviewer: Codex independent source reviewer (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The DSMZ 49 base recipe supports the three existing ingredient rates, calcium-chloride dihydrate form, solid state and pH. Two maintained base owners already carry authenticated quantity evidence, which the generated merge lacks. The separately named KOMODO 49_435 variant has no verified formulation; its copied amounts and SOURCE_DUPLICATE relationship remain unsupported. Water input and ordered preparation are incomplete. Exact KOMODO routes returned 403, so completion is partial.

## Scope And Provenance

Full selected record and exact maintained contributors; explicitly scoped dependency and external-source limits retained.

Selection: Actual batch068 native selection index 09.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:005633 | data/merge_yaml/merged/C_10_MEDIUM.yaml | generated | c_10_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:005633 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-strict | passed | True | CultureMech:005633 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-terms | passed | True | CultureMech:005633 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-references | passed | True | CultureMech:005633 | Native reference checker performed zero reference checks; this is not claim authentication. |

## Scientific And Domain Assessments

### Base accessions and separately named variant

identity: concern. Targets: CultureMech:005633.

Exact declared merged_from stems resolve three unique owners. DSMZ 49 base identity is directly verified; KOMODO 49 cross-reference is present in local evidence and historical mapping reports, but current mapping retrieval returned 403. KOMODO 49_435 is a distinct accession and name with imported base composition; the local SOURCE_DUPLICATE label is not formulation evidence. DSM 435 identifies Myxococcus xanthus only and adds no growth claim.

### Earlier evidence gaps versus current repairs

evidence: concern. Targets: CultureMech:005633.

The September review and October 5 reports precede the October 7 evidence-only owner repairs. Both base-owner current byte hashes equal the reported resulting hashes; six quantity snippets now match fresh source bytes and exact rows. The generated target retains none of these quantity snippets or source references. Current quantity writers conservatively withhold mismatched/variant claims, and the current merge implementation unions evidence only across equal formulation content. This is an existing generated artifact gap; no claim that current code would reproduce it.

### Quantity scope and inventory

quantity: concern. Targets: CultureMech:005633.

Every selected target/owner concentration field has an explicit disposition; scoped dependency fields and source-only preparation are separate from receiving-medium rates.

[{"quantity_id": "q1", "topic": "Casitone base rate versus unresolved variant", "source": {"evidence_id": "api49", "reference": "https://mediadive.dsmz.de/rest/medium/49", "raw_path": "REVIEW_WORK/batch068/source09/api49.bin", "raw_sha256": "5e702b51e94e3e9df5b8ca11855ae622be07093d77b4c957ecc3b0faad56a943", "locator": "$.data.solutions[0].recipe[0] and .volume", "accessed_at": "2026-10-28T13:13:57.316817Z", "source_object": {"recipe_order": 1, "compound": "Casitone", "compound_id": 84, "amount": 3, "unit": "g", "g_l": 3, "optional": 0}, "provider_volume_ml": 1000}, "decision": "mixed", "rationale": "Exact API reports 3 g and g_l=3; 3 g / (1000 ml / 1000 ml per L) = 3 g/L on its declared provider basis. PDF agrees with absolute batch input. This is not independently measured final volume; no rate is extended to 49_435.", "layer_assessments": [{"path": "data/merge_yaml/merged/C_10_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "3", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact DSMZ 49 base rate and form agree with the stored scalar; retain provider scope and attach/preserve claim-level evidence."}, {"path": "data/normalized_yaml/bacterial/KOMODO_49_C_10_medium.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "3", "unit": "G_PER_L"}, "decision": "verified", "rationale": "Existing attached ingredient evidence is verified at the exact source row against fresh original API bytes, literal snippet and stored whole-response digest. Preserve this existing base-owner repair and its provider-volume scope."}, {"path": "data/normalized_yaml/bacterial/c_10_medium.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "3", "unit": "G_PER_L"}, "decision": "verified", "rationale": "Existing attached ingredient evidence is verified at the exact source row against fresh original API bytes, literal snippet and stored whole-response digest. Preserve this existing base-owner repair and its provider-volume scope."}, {"path": "data/normalized_yaml/bacterial/medium_49_modified_for_dsm_435.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "3", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Base recipe import and local duplicate annotation do not authenticate this separately named variant; no replacement amount proposed."}]}, {"quantity_id": "q2", "topic": "CaCl2 x 2 H2O base rate versus unresolved variant", "source": {"evidence_id": "api49", "reference": "https://mediadive.dsmz.de/rest/medium/49", "raw_path": "REVIEW_WORK/batch068/source09/api49.bin", "raw_sha256": "5e702b51e94e3e9df5b8ca11855ae622be07093d77b4c957ecc3b0faad56a943", "locator": "$.data.solutions[0].recipe[1] and .volume", "accessed_at": "2026-10-28T13:13:57.316817Z", "source_object": {"recipe_order": 2, "compound": "CaCl2 x 2 H2O", "compound_id": 7, "amount": 1.36, "unit": "g", "g_l": 1.36, "mmol_l": 9.25076, "optional": 0}, "provider_volume_ml": 1000}, "decision": "mixed", "rationale": "Exact API reports 1.36 g and g_l=1.36; 1.36 g / (1000 ml / 1000 ml per L) = 1.36 g/L on its declared provider basis. PDF agrees with absolute batch input. This is not independently measured final volume; no rate is extended to 49_435.", "layer_assessments": [{"path": "data/merge_yaml/merged/C_10_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "1.36", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact DSMZ 49 base rate and form agree with the stored scalar; retain provider scope and attach/preserve claim-level evidence."}, {"path": "data/normalized_yaml/bacterial/KOMODO_49_C_10_medium.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "1.36", "unit": "G_PER_L"}, "decision": "verified", "rationale": "Existing attached ingredient evidence is verified at the exact source row against fresh original API bytes, literal snippet and stored whole-response digest. Preserve this existing base-owner repair and its provider-volume scope."}, {"path": "data/normalized_yaml/bacterial/c_10_medium.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "1.36", "unit": "G_PER_L"}, "decision": "verified", "rationale": "Existing attached ingredient evidence is verified at the exact source row against fresh original API bytes, literal snippet and stored whole-response digest. Preserve this existing base-owner repair and its provider-volume scope."}, {"path": "data/normalized_yaml/bacterial/medium_49_modified_for_dsm_435.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "1.36", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Base recipe import and local duplicate annotation do not authenticate this separately named variant; no replacement amount proposed."}]}, {"quantity_id": "q3", "topic": "Agar base rate versus unresolved variant", "source": {"evidence_id": "api49", "reference": "https://mediadive.dsmz.de/rest/medium/49", "raw_path": "REVIEW_WORK/batch068/source09/api49.bin", "raw_sha256": "5e702b51e94e3e9df5b8ca11855ae622be07093d77b4c957ecc3b0faad56a943", "locator": "$.data.solutions[0].recipe[2] and .volume", "accessed_at": "2026-10-28T13:13:57.316817Z", "source_object": {"recipe_order": 3, "compound": "Agar", "compound_id": 3, "amount": 15, "unit": "g", "g_l": 15, "mmol_l": 44.5991, "optional": 0}, "provider_volume_ml": 1000}, "decision": "mixed", "rationale": "Exact API reports 15 g and g_l=15; 15 g / (1000 ml / 1000 ml per L) = 15 g/L on its declared provider basis. PDF agrees with absolute batch input. This is not independently measured final volume; no rate is extended to 49_435.", "layer_assessments": [{"path": "data/merge_yaml/merged/C_10_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "15", "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact DSMZ 49 base rate and form agree with the stored scalar; retain provider scope and attach/preserve claim-level evidence."}, {"path": "data/normalized_yaml/bacterial/KOMODO_49_C_10_medium.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "15", "unit": "G_PER_L"}, "decision": "verified", "rationale": "Existing attached ingredient evidence is verified at the exact source row against fresh original API bytes, literal snippet and stored whole-response digest. Preserve this existing base-owner repair and its provider-volume scope."}, {"path": "data/normalized_yaml/bacterial/c_10_medium.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "15", "unit": "G_PER_L"}, "decision": "verified", "rationale": "Existing attached ingredient evidence is verified at the exact source row against fresh original API bytes, literal snippet and stored whole-response digest. Preserve this existing base-owner repair and its provider-volume scope."}, {"path": "data/normalized_yaml/bacterial/medium_49_modified_for_dsm_435.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "15", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Base recipe import and local duplicate annotation do not authenticate this separately named variant; no replacement amount proposed."}]}, {"quantity_id": "q4", "topic": "Base pH", "source": {"evidence_id": "api49", "reference": "https://mediadive.dsmz.de/rest/medium/49", "raw_path": "REVIEW_WORK/batch068/source09/api49.bin", "raw_sha256": "5e702b51e94e3e9df5b8ca11855ae622be07093d77b4c957ecc3b0faad56a943", "locator": "$.data.medium and $.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T13:13:57.316817Z"}, "decision": "mixed", "rationale": "The exact base formulation supports this field; the variant remains separately unresolved.", "layer_assessments": [{"path": "data/merge_yaml/merged/C_10_MEDIUM.yaml", "field_path": "ph_value", "stored_value": 7.2, "decision": "evidence_only", "rationale": "Base source explicitly supports pH 7.2 and nonoptional agar; retain the current base descriptor."}, {"path": "data/normalized_yaml/bacterial/KOMODO_49_C_10_medium.yaml", "field_path": "ph_value", "stored_value": 7.2, "decision": "evidence_only", "rationale": "Base source explicitly supports pH 7.2 and nonoptional agar; retain the current base descriptor."}, {"path": "data/normalized_yaml/bacterial/c_10_medium.yaml", "field_path": "ph_value", "stored_value": 7.2, "decision": "evidence_only", "rationale": "Base source explicitly supports pH 7.2 and nonoptional agar; retain the current base descriptor."}, {"path": "data/normalized_yaml/bacterial/medium_49_modified_for_dsm_435.yaml", "field_path": "ph_value", "stored_value": 7.2, "decision": "unsupported", "rationale": "No exact variant formulation; copied base pH/state does not establish the variant."}]}, {"quantity_id": "q5", "topic": "Base solid state", "source": {"evidence_id": "api49", "reference": "https://mediadive.dsmz.de/rest/medium/49", "raw_path": "REVIEW_WORK/batch068/source09/api49.bin", "raw_sha256": "5e702b51e94e3e9df5b8ca11855ae622be07093d77b4c957ecc3b0faad56a943", "locator": "$.data.medium and $.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T13:13:57.316817Z"}, "decision": "mixed", "rationale": "The exact base formulation supports this field; the variant remains separately unresolved.", "layer_assessments": [{"path": "data/merge_yaml/merged/C_10_MEDIUM.yaml", "field_path": "physical_state", "stored_value": "SOLID_AGAR", "decision": "evidence_only", "rationale": "Base source explicitly supports pH 7.2 and nonoptional agar; retain the current base descriptor."}, {"path": "data/normalized_yaml/bacterial/KOMODO_49_C_10_medium.yaml", "field_path": "physical_state", "stored_value": "SOLID_AGAR", "decision": "evidence_only", "rationale": "Base source explicitly supports pH 7.2 and nonoptional agar; retain the current base descriptor."}, {"path": "data/normalized_yaml/bacterial/c_10_medium.yaml", "field_path": "physical_state", "stored_value": "SOLID_AGAR", "decision": "evidence_only", "rationale": "Base source explicitly supports pH 7.2 and nonoptional agar; retain the current base descriptor."}, {"path": "data/normalized_yaml/bacterial/medium_49_modified_for_dsm_435.yaml", "field_path": "physical_state", "stored_value": "SOLID_AGAR", "decision": "unsupported", "rationale": "No exact variant formulation; copied base pH/state does not establish the variant."}]}, {"quantity_id": "q6", "topic": "Source water input and provider volume", "source": {"evidence_id": "api49", "reference": "https://mediadive.dsmz.de/rest/medium/49", "raw_path": "REVIEW_WORK/batch068/source09/api49.bin", "raw_sha256": "5e702b51e94e3e9df5b8ca11855ae622be07093d77b4c957ecc3b0faad56a943", "locator": "$.data.solutions[0].recipe[3] and .volume", "accessed_at": "2026-10-28T13:13:57.316817Z"}, "decision": "mixed", "rationale": "All four complete local documents lack a water row or explicit water-input quantity. API names 1000 ml distilled water and provider volume 1000; PDF supplies water input only. Curate base solvent/batch scope; no water-to-final-volume assumption.", "layer_assessments": [{"path": "data/merge_yaml/merged/C_10_MEDIUM.yaml", "field_path": "source_water_input", "stored_value": null, "decision": "add", "rationale": "Record the exact 1000 ml distilled-water input at its preparation stage without inventing a measured final volume.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_49_C_10_medium.yaml", "field_path": "source_water_input", "stored_value": null, "decision": "add", "rationale": "Record the exact 1000 ml distilled-water input at its preparation stage without inventing a measured final volume.", "missing": true}, {"path": "data/normalized_yaml/bacterial/c_10_medium.yaml", "field_path": "source_water_input", "stored_value": null, "decision": "add", "rationale": "Record the exact 1000 ml distilled-water input at its preparation stage without inventing a measured final volume.", "missing": true}, {"path": "data/normalized_yaml/bacterial/medium_49_modified_for_dsm_435.yaml", "field_path": "source_water_input", "stored_value": null, "decision": "unsupported", "rationale": "No exact variant formulation; do not add a base water amount.", "missing": true}]}, {"quantity_id": "q7", "topic": "Ordered pH preparation", "source": {"evidence_id": "api49", "reference": "https://mediadive.dsmz.de/rest/medium/49", "raw_path": "REVIEW_WORK/batch068/source09/api49.bin", "raw_sha256": "5e702b51e94e3e9df5b8ca11855ae622be07093d77b4c957ecc3b0faad56a943", "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T13:13:57.316817Z", "quote": "Adjust pH to 7.2 before adding agar."}, "decision": "mixed", "rationale": "A scalar pH does not preserve the stated order before agar. Current resolver copies composition/pH/state, not this ordered preparation; the present merger is conservative and does not authorize forcing these owners together.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/c_10_medium.yaml", "field_path": "preparation_steps[0].description", "stored_value": "Adjust pH to 7.2 before adding agar.", "decision": "evidence_only", "rationale": "Exact instruction already retained by the direct owner; preserve it."}, {"path": "data/merge_yaml/merged/C_10_MEDIUM.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "The base preparation sequence is missing; restore from the exact source through the owner and compatible regeneration.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_49_C_10_medium.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale": "The base preparation sequence is missing; restore from the exact source through the owner and compatible regeneration.", "missing": true}, {"path": "data/normalized_yaml/bacterial/medium_49_modified_for_dsm_435.yaml", "field_path": "preparation_steps", "stored_value": null, "decision": "unsupported", "rationale": "Variant-specific preparation not retrieved; do not borrow the base instruction.", "missing": true}]}, {"quantity_id": "q8", "topic": "KOMODO atmosphere annotation", "source": {"evidence_id": "komodo49exact", "reference": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=49", "raw_path": "REVIEW_WORK/batch068/source09-exact-route/komodo49exact.bin", "raw_sha256": "b561a0beb87ccb8eb1d31690e78d800923fc46a9c000f3dbe849c746b8f9b37a", "accessed_at": "2026-10-28T13:28:38.681378Z", "scope": "Exact historical /komodo/servlet/ route returned 403; original alternate-path attempts also preserved. No atmosphere authenticated."}, "decision": "unsupported", "rationale": "The DSMZ 49 recipe does not state an atmosphere. The accessible DSM 435 catalogue concerns other media and cannot authenticate or correct this C/10 annotation.", "layer_assessments": [{"path": "data/merge_yaml/merged/C_10_MEDIUM.yaml", "field_path": "notes", "stored_value": "Source: KOMODO ModelSEED &#124; ID: 49 &#124; DSMZ Medium: 49 (mediadive.medium:49) &#124; Aerobic: No", "decision": "unsupported", "rationale": "Aerobic: No is a source metadata assertion without authenticated current support; do not infer an incubation atmosphere or flip it from organism taxonomy."}, {"path": "data/normalized_yaml/bacterial/KOMODO_49_C_10_medium.yaml", "field_path": "notes", "stored_value": "Source: KOMODO ModelSEED &#124; ID: 49 &#124; DSMZ Medium: 49 (mediadive.medium:49) &#124; Aerobic: No", "decision": "unsupported", "rationale": "Aerobic: No is a source metadata assertion without authenticated current support; do not infer an incubation atmosphere or flip it from organism taxonomy."}, {"path": "data/normalized_yaml/bacterial/medium_49_modified_for_dsm_435.yaml", "field_path": "notes", "stored_value": "Source: KOMODO ModelSEED &#124; ID: 49_435 &#124; DSMZ Medium: 49 (mediadive.medium:49) &#124; Aerobic: No", "decision": "unsupported", "rationale": "Aerobic: No is a source metadata assertion without authenticated current support; do not infer an incubation atmosphere or flip it from organism taxonomy."}]}]

### Current ontology and MIM correspondence

grounding: supported. Targets: CultureMech:005633.

Every asserted primary and secondary chemical slot carries CHEBI:86158/calcium chloride dihydrate or CHEBI:2509/agar. Fresh OLS preferred labels, nonobsolete flags, calcium dihydrate formula/mass/CAS and agar mixture definition agree. Exact current MIM joins retain MAPPED preferred rows and the separate REJECTED CaCl22H2O row; that rejected alias does not invalidate the asserted calcium-chloride-dihydrate ID. Casitone remains an undefined ungrounded source component; no unsupported pure-compound identity is proposed. Identifier correspondence does not authenticate variant quantities.

### History and evidence scope

provenance: concern. Targets: CultureMech:005633.

Complete four local histories, references and evidence were inventoried. Six base-owner quantity snippets are authenticated against exact current raw bytes and their stored source hash; historical KOMODO mapping bytes were not retrieved. October 7 repairs remain intact, while the generated history predates them. Current import, resolver, quantity writers and compatible merger were read separately from historical claims. Malformed/naive timestamps remain explicit uncertainty.

### Growth and taxonomic evidence

scope: unknown. Targets: CultureMech:005633.

Generic cultivation applications and bacterial filing are not strain-level growth evidence. No organism-specific growth, temperature or atmosphere is inferred from names or source catalog identifiers.

### Canonical diagnostics

schema: supported. Targets: CultureMech:005633.

All four original canonical diagnostics passed. Reference checks were zero; structural and term diagnostics do not establish formulation accuracy.

## Findings

### f1: Variant equivalence is not established

major / open / confirmed; issue key: culturemech-005633-variant-equivalence-is-not-established.

KOMODO 49_435 is explicitly named as a DSM 435 modification, but it has only copied base composition and a SOURCE_DUPLICATE parent relation. Exact source retrieval failed 403. Preserve its accession and resolve its own formulation before endorsing copied quantities or consolidating it with the base. The base recipe and strain catalogue do not fill that evidence gap.

### f2: Base water input and preparation order are incomplete

major / open / confirmed; issue key: culturemech-005633-base-water-input-and-preparation-order-are-incomplete.

The base PDF/API include distilled-water input and an instruction placing pH adjustment before agar. All local layers omit the water-input quantity; the direct DSMZ owner already preserves the ordered instruction while the KOMODO base owner and generated target omit it. Keep provider volume distinct from water input and do not transfer these details to the unresolved variant.

### f3: Generated base claims omit repaired owner evidence

minor / open / confirmed; issue key: culturemech-005633-generated-base-claims-omit-repaired-owner-evidence.

Both maintained base owners already carry three exact quantity excerpts and source references; six claims authenticate against the freshly retrieved unchanged raw API response. The generated target has no claim-level excerpts or structured source references. Preserve these repairs and resolve grouping before regeneration; do not reapply obsolete all-owner missing-evidence findings.

### f4: KOMODO import history contains a malformed timestamp

minor / open / confirmed; issue key: culturemech-005633-komodo-import-history-contains-a-malformed-timestamp.

The selected target and two KOMODO contributors retain the literal timestamp 2026-01-27T01:15:02.fZ. Current importer uses time.strftime with a microsecond token and the resolver emits naive local timestamps; this identifies current metadata-generation weaknesses without proving past execution. Preserve original events and append a documented correction only when original time evidence exists.

## Recommended Actions And Acceptance Checks

### action1

Retrieve an exact authoritative 49_435 formulation or explicit no-change provenance. Resolve the variant relationship in maintained contributors, retaining unresolved identity until evidence supports equivalence; regenerate compatible groups only.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action2

Preserve the direct owner preparation, add source-backed base water-input/batch metadata and missing base preparation to the relevant owner, then regenerate without forcing unequal formulations or assigning base details to 49_435.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action3

Regenerate after contributor identity and preparation reconciliation, preserving exact evidence scope and base references. Confirm the resulting artifact retains these claims; leave unsupported variant claims unendorsed.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action4

Maintain append-only history: document the malformed timestamp and its uncertainty; repair the writer formatting separately without inventing a historic fractional time or timezone.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local-target | data/merge_yaml/merged/C_10_MEDIUM.yaml; Complete document | context_only | Complete selected generated record; no changes made. |
| owner-1 | data/normalized_yaml/bacterial/KOMODO_49_C_10_medium.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| owner-2 | data/normalized_yaml/bacterial/c_10_medium.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| owner-3 | data/normalized_yaml/bacterial/medium_49_modified_for_dsm_435.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| identity-search | REVIEW_WORK/batch068/record09/identity-search.json | supports | Exact generated lineage resolves every maintained contributor; no filename-only transfer from neighboring variants. |
| api49 | https://mediadive.dsmz.de/rest/medium/49; $.data.medium and $.data.solutions[0] | supports | Exact DSMZ 49 provider response; current SHA256 equals the hash stored by both repaired base owners. Main recipe lists three mass inputs with explicit g_l and provider volume, one water input and one ordered pH instruction. |
| dsm49 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium49.pdf; Page1 title, full ingredient table and final instruction | supports | Exact DSMZ 49 primary PDF read completely: three non-water inputs, distilled-water input and pH-before-agar instruction. The water input alone is not a measured final-volume claim. |
| dsm435_identity | https://www.dsmz.de/collection/catalogue/details/culture/DSM-435; Name; DSM No.; strain designation; isolation; risk group | context_only | DSM 435 catalogue identifies Myxococcus xanthus, strain Mx x1, soil with roots, Liberia, risk group 1. Used for organism-identity scope only; this page does not establish C/10 or KOMODO 49_435 growth. |
| komodo_list | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList; HTTP status and retained response | context_only | Exact MediaList request returned 403; block-page bytes retained, no live mapping authenticated. |
| komodo49 | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=49; HTTP status and retained response | context_only | Initial alternate /servlet/ MediaInfo route returned 403. Its original attempt is preserved; the exact historical /komodo/servlet/ route was subsequently captured separately, also 403. Neither block page authenticates formulation or atmosphere. |
| komodo49_435 | https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=49_435; HTTP status and retained response | context_only | Initial alternate /servlet/ MediaInfo route returned 403. Its original attempt is preserved; the exact historical /komodo/servlet/ route was subsequently captured separately, also 403. Neither block page authenticates formulation or atmosphere. |
| report1 | reports/archive/media_variant_dsmz_komodo_source_duplicate_review.md; Header and exact DSMZ 49/KOMODO 49 row | context_only | Historical context only. Exact target/owner report read completely, except the broad source-duplicate archive where only the header and exact C/10 row were assessed. Later owner repairs supersede earlier missing-evidence claims; no report substitutes for source authentication. |
| report2 | reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/KOMODO_49_C_10_medium.yaml.md; Complete exact target/owner report | context_only | Historical context only. Exact target/owner report read completely, except the broad source-duplicate archive where only the header and exact C/10 row were assessed. Later owner repairs supersede earlier missing-evidence claims; no report substitutes for source authentication. |
| report3 | reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/medium_49_modified_for_dsm_435.yaml.md; Complete exact target/owner report | context_only | Historical context only. Exact target/owner report read completely, except the broad source-duplicate archive where only the header and exact C/10 row were assessed. Later owner repairs supersede earlier missing-evidence claims; no report substitutes for source authentication. |
| report4 | reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/c_10_medium.yaml.md; Complete exact target/owner report | context_only | Historical context only. Exact target/owner report read completely, except the broad source-duplicate archive where only the header and exact C/10 row were assessed. Later owner repairs supersede earlier missing-evidence claims; no report substitutes for source authentication. |
| report5 | reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/C_10_MEDIUM.md; Complete exact target/owner report | context_only | Historical context only. Exact target/owner report read completely, except the broad source-duplicate archive where only the header and exact C/10 row were assessed. Later owner repairs supersede earlier missing-evidence claims; no report substitutes for source authentication. |
| report6 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_49_C_10_medium.md; Complete exact target/owner report | context_only | Historical context only. Exact target/owner report read completely, except the broad source-duplicate archive where only the header and exact C/10 row were assessed. Later owner repairs supersede earlier missing-evidence claims; no report substitutes for source authentication. |
| report7 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/c_10_medium.md; Complete exact target/owner report | context_only | Historical context only. Exact target/owner report read completely, except the broad source-duplicate archive where only the header and exact C/10 row were assessed. Later owner repairs supersede earlier missing-evidence claims; no report substitutes for source authentication. |
| report8 | reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/medium_49_modified_for_dsm_435.md; Complete exact target/owner report | context_only | Historical context only. Exact target/owner report read completely, except the broad source-duplicate archive where only the header and exact C/10 row were assessed. Later owner repairs supersede earlier missing-evidence claims; no report substitutes for source authentication. |
| report9 | reports/yaml_record_review/20260922T013503Z-C_10_MEDIUM.md; Complete exact target/owner report | context_only | Historical context only. Exact target/owner report read completely, except the broad source-duplicate archive where only the header and exact C/10 row were assessed. Later owner repairs supersede earlier missing-evidence claims; no report substitutes for source authentication. |
| current-formulation | src/culturemech/merge/formulation.py; Complete projection and compatible-evidence merge implementation | context_only | Current writer behavior read in the exact inspected checkout; this is not proof that current code produced any historic record. |
| current-merger | src/culturemech/merge/merger.py; merge_group and canonical-selection behavior | context_only | Current writer behavior read in the exact inspected checkout; this is not proof that current code produced any historic record. |
| komodo-import | src/culturemech/import/komodo_web_importer.py; _convert_to_culturemech | context_only | Current writer behavior read in the exact inspected checkout; this is not proof that current code produced any historic record. |
| dsm-resolver | src/culturemech/enrich/dsmz_resolver.py; extract_dsmz_id; merge_composition; _add_enrichment_metadata; resolve_recipe | context_only | Current writer behavior read in the exact inspected checkout; this is not proof that current code produced any historic record. |
| quantity-writer | scripts/review_medium_concentration_evidence.py; identity_problem; decide; review | context_only | Current writer behavior read in the exact inspected checkout; this is not proof that current code produced any historic record. |
| mapping-writer | scripts/review_komodo_concentration_evidence.py; identity_problem; mapping_evidence; review | context_only | Current writer behavior read in the exact inspected checkout; this is not proof that current code produced any historic record. |
| source-audit | REVIEW_WORK/batch068/record09/source-and-lineage-audit.json | supports | Six exact owner quantity claims match literal fresh raw source bytes, parsed source rows and stored source hash. Current owner formulation keys differ; mapping authentication remains unavailable. |
| chebi86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86158; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_2509; _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation chemical properties | supports | Exact OLS accession, current preferred label, obsolete flag, definition, chemical formula, mass and CAS annotations examined. The full object is retained; unrelated literature links are not asserted verified. Supports identifier correspondence only, not recipe amounts or growth. |
| quantities | REVIEW_WORK/batch068/record09/quantity-inventory.json | context_only | Complete local concentration and source-stage decision inventory; includes exact local paths and source failure limits. |
| grounding | REVIEW_WORK/batch068/record09/grounding-inventory.json | context_only | All recursive asserted identifier/label slots, exact current OLS objects and current packaged MIM preferred-row joins. |
| history | REVIEW_WORK/batch068/record09/history-and-evidence-inventory.json | context_only | Complete current history, references and attached evidence; source-specific claims are assessed without authenticating historical execution from code. |
| scalars | REVIEW_WORK/batch068/record09/scalar-census.json | context_only | Lossless scalar census of the selected target and all maintained contributors. |
| validate-schema | REVIEW_WORK/batch068/record09/validate-schema.json | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed<br> |
| validate-strict | REVIEW_WORK/batch068/record09/validate-strict.json | supports | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch068/record09/strict.tsv<br> |
| validate-terms | REVIEW_WORK/batch068/record09/validate-terms.json | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed<br> |
| validate-references | REVIEW_WORK/batch068/record09/validate-references.json | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed<br> |
| komodo49exact | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=49; Exact historical /komodo/servlet/ MediaInfo route; HTTP status and retained response metadata | context_only | Exact historical route returned 403. Block-page bytes and original access metadata are retained; no source formulation or atmosphere is authenticated. Earlier alternate-path attempts remain preserved separately. |
| komodo49_435exact | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=49_435; Exact historical /komodo/servlet/ MediaInfo route; HTTP status and retained response metadata | context_only | Exact historical route returned 403. Block-page bytes and original access metadata are retained; no source formulation or atmosphere is authenticated. Earlier alternate-path attempts remain preserved separately. |

## Limits And Additional Notes

- Exact KOMODO list, base and 49_435 routes returned 403. Their historical mapping excerpts are local context, not authenticated current full responses; the variant formulation and atmosphere remain unresolved. Obtain exact accessible authoritative source evidence before endorsing variant quantities or equivalence.
- DSM 435 catalogue was used for identity scope only. No strain-specific growth on C/10, growth conditions, or taxonomy grounding has been added. The PDF water input is not an independent final-volume measurement. Keep future organism growth and final-volume claims scoped to direct evidence.
- Fresh review; historical lost snapshots were not reconstructed. All inspected source files remain unchanged.
- This draft authoring step performed no formal review validation/save, Git mutation or publication.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T133015Z-batch068-record09-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'C/10 medium: supported base quantities, unresolved DSM 435 variant and stale
  generated evidence'
started_at: '2026-10-28T13:13:47.586807Z'
finished_at: '2026-10-28T13:30:15.612057Z'
reviewer:
  identity: Codex independent source reviewer
  kind: agent
  independence: independent
  independence_basis: Fresh assessment of the inspected checkout and newly captured
    primary/provider/ontology evidence; no reconstruction of lost reviews and no record
    edits.
skill: .claude/skills/review-yaml-record/SKILL.md; .claude/skills/review-ingredient-concentrations/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: The DSMZ 49 base recipe supports the three existing ingredient rates, calcium-chloride
  dihydrate form, solid state and pH. Two maintained base owners already carry authenticated
  quantity evidence, which the generated merge lacks. The separately named KOMODO
  49_435 variant has no verified formulation; its copied amounts and SOURCE_DUPLICATE
  relationship remain unsupported. Water input and ordered preparation are incomplete.
  Exact KOMODO routes returned 403, so completion is partial.
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
  - path: data/culturemech_id_registry.tsv
    sha256: 0d059720f5c474b63daff8d5010fc56942a5a3ac30761ee75ce9e84801d555a5
    role: context
  - path: data/merge_yaml/merged/C_10_MEDIUM.yaml
    sha256: 988db26a29005c39c3a546b7565d048c5ececdc2968c631c7c2db3a9c69ea24b
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_49_C_10_medium.yaml
    sha256: acff23ec468fb4f8eac822580d03e4de1a3ca6489d9a1e00411fb71a764dbf0e
    role: context
  - path: data/normalized_yaml/bacterial/c_10_medium.yaml
    sha256: 66e16a8f82cdb33caed7cc56a6e477d91babea01dab8a303ecbb9439b3d59886
    role: context
  - path: data/normalized_yaml/bacterial/medium_49_modified_for_dsm_435.yaml
    sha256: b6954bce257f9b255539c9604d3afe6dba429372cbcadfe1c2448ce3642f7e7b
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
  - path: reports/archive/media_variant_dsmz_komodo_source_duplicate_review.md
    sha256: a723d4b7950bf4ac296a8a7fe4890d4d0881199a5d17c12a5fe39c2afbc40a10
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/KOMODO_49_C_10_medium.yaml.md
    sha256: 91c12f48ea6a721e0b21ae8299e41fbc650ce250fc54e1633796504269a846bc
    role: context
  - path: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/medium_49_modified_for_dsm_435.yaml.md
    sha256: 78d1e6fcc5572c17b6b3de1bed28de6beb95d2595b3721d3db3841ebc1afc936
    role: context
  - path: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/c_10_medium.yaml.md
    sha256: 43b2b31491128842a0fa67a3a1800a56386d0219e0837877155b4897fa2233ad
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/C_10_MEDIUM.md
    sha256: a25b25e41177aef4a0042cd858a83d1951627a7e52eadc0879940a9ea8dd77e4
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_49_C_10_medium.md
    sha256: 10d8e75d5be0227406ed29f7bf9b29cf5a10031929c96f76ab0a1e0ae7554b4d
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/c_10_medium.md
    sha256: d1ce3322bdee71c10ac934a61b60abaaa3409c206d6daf0d89049d9970e5f418
    role: context
  - path: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/medium_49_modified_for_dsm_435.md
    sha256: af0d52bf6e59608326fb6db1ff578cf61c863846ccfc8b489275398bcb756329
    role: context
  - path: reports/yaml_record_review/20260922T013503Z-C_10_MEDIUM.md
    sha256: 5f61636e1fb46328033cdf75b06add40eb396fdb662ab71c0ab00c42ca6670de
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
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
  - path: scripts/migrate_chebi_regrounding.py
    sha256: bb174120fd6fcd1d3ed56092000fe54e6660fea4aabae7fece43a122dbd8d544
    role: context
  - path: scripts/migrate_legacy_mim_to_chebi.py
    sha256: 439ed5cb36fb9f619762c71db89266cf990e1783f5c10041fd35efec4b2ba5db
    role: context
  - path: scripts/migrate_solutions_from_ingredients.py
    sha256: 6d6c026e4542c6ddc1092604b44e4968d4ae575632b7c25460219ef68ff9f709
    role: context
  - path: scripts/normalize_media_names_to_snake_case.py
    sha256: 59bd842b1982b7d62af9db3fe280df576d8c4ae2e9ee411bf2e52523355f95de
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/record_target_class.py
    sha256: 468fcbfd2362ca08b7066d6f21adf85c04f21ab40f80e60995522b4edc0f6349
    role: context
  - path: scripts/repair_merged_duplicates.py
    sha256: a6f8af9fa5599f4e1bd22bbe3d79293e7798dce940efc354d9c63d3f1dc051c4
    role: context
  - path: scripts/review_komodo_concentration_evidence.py
    sha256: 4470019965d068a53587be3668c3872daedc1505dab1bc6e2d1ed937ba409658
    role: context
  - path: scripts/review_medium_concentration_evidence.py
    sha256: ccb5fb9b3c56dc1a57afb1d3bf1a76312a5ca7720bc71272ddfec5e333039f3a
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
  - path: src/culturemech/enrich/dsmz_resolver.py
    sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
    role: context
  - path: src/culturemech/import/komodo_web_importer.py
    sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
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
  selection: Actual batch068 native selection index 09.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:005633
targets:
- target_id: CultureMech:005633
  path: data/merge_yaml/merged/C_10_MEDIUM.yaml
  label: c_10_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_49_C_10_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/c_10_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_49_modified_for_dsm_435.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:005633
  command: just validate-schema data/merge_yaml/merged/C_10_MEDIUM.yaml
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
  - CultureMech:005633
  command: just validate-strict data/merge_yaml/merged/C_10_MEDIUM.yaml --out REVIEW_WORK/batch068/record09/strict.tsv
    --workers 1 --quiet
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
  - CultureMech:005633
  command: just validate-terms data/merge_yaml/merged/C_10_MEDIUM.yaml
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
  - CultureMech:005633
  command: just validate-references data/merge_yaml/merged/C_10_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
  scope_note: Exact selected target; scientific source and owner assessments are separate.
evidence:
- evidence_id: local-target
  kind: record_content
  reference: data/merge_yaml/merged/C_10_MEDIUM.yaml
  locator: Complete document
  accessed_at: '2026-10-28T13:17:57.807018Z'
  support: context_only
  summary: Complete selected generated record; no changes made.
  snapshot_sha256: 988db26a29005c39c3a546b7565d048c5ececdc2968c631c7c2db3a9c69ea24b
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_49_C_10_medium.yaml
  locator: Complete document
  accessed_at: '2026-10-28T13:17:57.807018Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: acff23ec468fb4f8eac822580d03e4de1a3ca6489d9a1e00411fb71a764dbf0e
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/c_10_medium.yaml
  locator: Complete document
  accessed_at: '2026-10-28T13:17:57.807018Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: 66e16a8f82cdb33caed7cc56a6e477d91babea01dab8a303ecbb9439b3d59886
- evidence_id: owner-3
  kind: record_content
  reference: data/normalized_yaml/bacterial/medium_49_modified_for_dsm_435.yaml
  locator: Complete document
  accessed_at: '2026-10-28T13:17:57.807018Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: b6954bce257f9b255539c9604d3afe6dba429372cbcadfe1c2448ce3642f7e7b
- evidence_id: identity-search
  kind: search
  reference: REVIEW_WORK/batch068/record09/identity-search.json
  accessed_at: '2026-10-28T13:17:57.857187Z'
  support: supports
  summary: Exact generated lineage resolves every maintained contributor; no filename-only
    transfer from neighboring variants.
  search_scope: Complete recursive normalized YAML filename census including ignored
    and hidden paths; exact merged_from stems and stable identity resolve the owner;
    excluded namesakes are retained in the census. Similar names and source accessions
    are not promoted to owners.
  snapshot_sha256: fe9ead8d3ce4e15cae6ddd60cce63d4573f2f2df33e3d5434f125327c5297bac
- evidence_id: api49
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/49
  locator: $.data.medium and $.data.solutions[0]
  accessed_at: '2026-10-28T13:13:57.316817Z'
  support: supports
  summary: Exact DSMZ 49 provider response; current SHA256 equals the hash stored
    by both repaired base owners. Main recipe lists three mass inputs with explicit
    g_l and provider volume, one water input and one ordered pH instruction.
  snapshot_sha256: 5e702b51e94e3e9df5b8ca11855ae622be07093d77b4c957ecc3b0faad56a943
- evidence_id: dsm49
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium49.pdf
  locator: Page1 title, full ingredient table and final instruction
  accessed_at: '2026-10-28T13:13:57.693648Z'
  support: supports
  summary: 'Exact DSMZ 49 primary PDF read completely: three non-water inputs, distilled-water
    input and pH-before-agar instruction. The water input alone is not a measured
    final-volume claim.'
  snapshot_sha256: c23ec6413149cc4fdb7b850788b246d604ba99d6a98ecfad029de4688a4493c7
- evidence_id: dsm435_identity
  kind: primary_source
  reference: https://www.dsmz.de/collection/catalogue/details/culture/DSM-435
  locator: Name; DSM No.; strain designation; isolation; risk group
  accessed_at: '2026-10-28T13:13:58.348630Z'
  support: context_only
  summary: DSM 435 catalogue identifies Myxococcus xanthus, strain Mx x1, soil with
    roots, Liberia, risk group 1. Used for organism-identity scope only; this page
    does not establish C/10 or KOMODO 49_435 growth.
  snapshot_sha256: bc84786c9e09a8e6bcefdfd8e203fa53528da99eb387706eee659d9259e0a9c6
- evidence_id: komodo_list
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList
  locator: HTTP status and retained response
  accessed_at: '2026-10-28T13:13:56.921674Z'
  support: context_only
  summary: Exact MediaList request returned 403; block-page bytes retained, no live
    mapping authenticated.
  snapshot_sha256: 7c95b7719b65e11185610efba5007a973ba34aa2426d0838e28dc3d004a553eb
- evidence_id: komodo49
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=49
  locator: HTTP status and retained response
  accessed_at: '2026-10-28T13:13:56.861388Z'
  support: context_only
  summary: Initial alternate /servlet/ MediaInfo route returned 403. Its original
    attempt is preserved; the exact historical /komodo/servlet/ route was subsequently
    captured separately, also 403. Neither block page authenticates formulation or
    atmosphere.
  snapshot_sha256: a723933187baf0d9b890cb542c49d98b42687a9fcf5dc2d7dc47d054d17b15e3
- evidence_id: komodo49_435
  kind: database
  reference: https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=49_435
  locator: HTTP status and retained response
  accessed_at: '2026-10-28T13:13:56.924304Z'
  support: context_only
  summary: Initial alternate /servlet/ MediaInfo route returned 403. Its original
    attempt is preserved; the exact historical /komodo/servlet/ route was subsequently
    captured separately, also 403. Neither block page authenticates formulation or
    atmosphere.
  snapshot_sha256: 1ea876c1444b74502fa39a3f21983bb0232c3c0d1e950a6ac23656a299241041
- evidence_id: report1
  kind: record_content
  reference: reports/archive/media_variant_dsmz_komodo_source_duplicate_review.md
  locator: Header and exact DSMZ 49/KOMODO 49 row
  accessed_at: '2026-10-28T13:17:57.807018Z'
  support: context_only
  summary: Historical context only. Exact target/owner report read completely, except
    the broad source-duplicate archive where only the header and exact C/10 row were
    assessed. Later owner repairs supersede earlier missing-evidence claims; no report
    substitutes for source authentication.
  snapshot_sha256: a723d4b7950bf4ac296a8a7fe4890d4d0881199a5d17c12a5fe39c2afbc40a10
- evidence_id: report2
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/KOMODO_49_C_10_medium.yaml.md
  locator: Complete exact target/owner report
  accessed_at: '2026-10-28T13:17:57.807018Z'
  support: context_only
  summary: Historical context only. Exact target/owner report read completely, except
    the broad source-duplicate archive where only the header and exact C/10 row were
    assessed. Later owner repairs supersede earlier missing-evidence claims; no report
    substitutes for source authentication.
  snapshot_sha256: 91c12f48ea6a721e0b21ae8299e41fbc650ce250fc54e1633796504269a846bc
- evidence_id: report3
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-komodo-media-0000-0500/records/bacterial/medium_49_modified_for_dsm_435.yaml.md
  locator: Complete exact target/owner report
  accessed_at: '2026-10-28T13:17:57.807018Z'
  support: context_only
  summary: Historical context only. Exact target/owner report read completely, except
    the broad source-duplicate archive where only the header and exact C/10 row were
    assessed. Later owner repairs supersede earlier missing-evidence claims; no report
    substitutes for source authentication.
  snapshot_sha256: 78d1e6fcc5572c17b6b3de1bed28de6beb95d2595b3721d3db3841ebc1afc936
- evidence_id: report4
  kind: record_content
  reference: reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/records/bacterial/c_10_medium.yaml.md
  locator: Complete exact target/owner report
  accessed_at: '2026-10-28T13:17:57.807018Z'
  support: context_only
  summary: Historical context only. Exact target/owner report read completely, except
    the broad source-duplicate archive where only the header and exact C/10 row were
    assessed. Later owner repairs supersede earlier missing-evidence claims; no report
    substitutes for source authentication.
  snapshot_sha256: 43b2b31491128842a0fa67a3a1800a56386d0219e0837877155b4897fa2233ad
- evidence_id: report5
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/merge_yaml/merged/C_10_MEDIUM.md
  locator: Complete exact target/owner report
  accessed_at: '2026-10-28T13:17:57.807018Z'
  support: context_only
  summary: Historical context only. Exact target/owner report read completely, except
    the broad source-duplicate archive where only the header and exact C/10 row were
    assessed. Later owner repairs supersede earlier missing-evidence claims; no report
    substitutes for source authentication.
  snapshot_sha256: a25b25e41177aef4a0042cd858a83d1951627a7e52eadc0879940a9ea8dd77e4
- evidence_id: report6
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/KOMODO_49_C_10_medium.md
  locator: Complete exact target/owner report
  accessed_at: '2026-10-28T13:17:57.807018Z'
  support: context_only
  summary: Historical context only. Exact target/owner report read completely, except
    the broad source-duplicate archive where only the header and exact C/10 row were
    assessed. Later owner repairs supersede earlier missing-evidence claims; no report
    substitutes for source authentication.
  snapshot_sha256: 10d8e75d5be0227406ed29f7bf9b29cf5a10031929c96f76ab0a1e0ae7554b4d
- evidence_id: report7
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/c_10_medium.md
  locator: Complete exact target/owner report
  accessed_at: '2026-10-28T13:17:57.807018Z'
  support: context_only
  summary: Historical context only. Exact target/owner report read completely, except
    the broad source-duplicate archive where only the header and exact C/10 row were
    assessed. Later owner repairs supersede earlier missing-evidence claims; no report
    substitutes for source authentication.
  snapshot_sha256: d1ce3322bdee71c10ac934a61b60abaaa3409c206d6daf0d89049d9970e5f418
- evidence_id: report8
  kind: record_content
  reference: reports/ingredient_concentration_review/20261005T175229Z/records/normalized_yaml/bacterial/medium_49_modified_for_dsm_435.md
  locator: Complete exact target/owner report
  accessed_at: '2026-10-28T13:17:57.807018Z'
  support: context_only
  summary: Historical context only. Exact target/owner report read completely, except
    the broad source-duplicate archive where only the header and exact C/10 row were
    assessed. Later owner repairs supersede earlier missing-evidence claims; no report
    substitutes for source authentication.
  snapshot_sha256: af0d52bf6e59608326fb6db1ff578cf61c863846ccfc8b489275398bcb756329
- evidence_id: report9
  kind: record_content
  reference: reports/yaml_record_review/20260922T013503Z-C_10_MEDIUM.md
  locator: Complete exact target/owner report
  accessed_at: '2026-10-28T13:17:57.807018Z'
  support: context_only
  summary: Historical context only. Exact target/owner report read completely, except
    the broad source-duplicate archive where only the header and exact C/10 row were
    assessed. Later owner repairs supersede earlier missing-evidence claims; no report
    substitutes for source authentication.
  snapshot_sha256: 5f61636e1fb46328033cdf75b06add40eb396fdb662ab71c0ab00c42ca6670de
- evidence_id: current-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: Complete projection and compatible-evidence merge implementation
  accessed_at: '2026-10-28T13:17:57.807018Z'
  support: context_only
  summary: Current writer behavior read in the exact inspected checkout; this is not
    proof that current code produced any historic record.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: current-merger
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: merge_group and canonical-selection behavior
  accessed_at: '2026-10-28T13:17:57.807018Z'
  support: context_only
  summary: Current writer behavior read in the exact inspected checkout; this is not
    proof that current code produced any historic record.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: komodo-import
  kind: record_content
  reference: src/culturemech/import/komodo_web_importer.py
  locator: _convert_to_culturemech
  accessed_at: '2026-10-28T13:17:57.807018Z'
  support: context_only
  summary: Current writer behavior read in the exact inspected checkout; this is not
    proof that current code produced any historic record.
  snapshot_sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
- evidence_id: dsm-resolver
  kind: record_content
  reference: src/culturemech/enrich/dsmz_resolver.py
  locator: extract_dsmz_id; merge_composition; _add_enrichment_metadata; resolve_recipe
  accessed_at: '2026-10-28T13:17:57.807018Z'
  support: context_only
  summary: Current writer behavior read in the exact inspected checkout; this is not
    proof that current code produced any historic record.
  snapshot_sha256: 5a15106efbd34b6fe074186968dfeb030b8f350ed1ba4a1ca66560093dceaa77
- evidence_id: quantity-writer
  kind: record_content
  reference: scripts/review_medium_concentration_evidence.py
  locator: identity_problem; decide; review
  accessed_at: '2026-10-28T13:17:57.807018Z'
  support: context_only
  summary: Current writer behavior read in the exact inspected checkout; this is not
    proof that current code produced any historic record.
  snapshot_sha256: ccb5fb9b3c56dc1a57afb1d3bf1a76312a5ca7720bc71272ddfec5e333039f3a
- evidence_id: mapping-writer
  kind: record_content
  reference: scripts/review_komodo_concentration_evidence.py
  locator: identity_problem; mapping_evidence; review
  accessed_at: '2026-10-28T13:17:57.807018Z'
  support: context_only
  summary: Current writer behavior read in the exact inspected checkout; this is not
    proof that current code produced any historic record.
  snapshot_sha256: 4470019965d068a53587be3668c3872daedc1505dab1bc6e2d1ed937ba409658
- evidence_id: source-audit
  kind: record_content
  reference: REVIEW_WORK/batch068/record09/source-and-lineage-audit.json
  accessed_at: '2026-10-28T13:17:57.861864Z'
  support: supports
  summary: Six exact owner quantity claims match literal fresh raw source bytes, parsed
    source rows and stored source hash. Current owner formulation keys differ; mapping
    authentication remains unavailable.
  snapshot_sha256: b68c750c1ecec70ceff532429c9bc4b3c3d95cfa331d0a6f33651bc49a184f16
- evidence_id: chebi86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_86158
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T13:13:57.924029Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: df8f702eb5b9d3e50209bfa2b0c4b6f1db30c116e56a58e348cbd4bf3bc0ebc1
- evidence_id: chebi2509
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_2509
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/annotation
    chemical properties
  accessed_at: '2026-10-28T13:14:01.440635Z'
  support: supports
  summary: Exact OLS accession, current preferred label, obsolete flag, definition,
    chemical formula, mass and CAS annotations examined. The full object is retained;
    unrelated literature links are not asserted verified. Supports identifier correspondence
    only, not recipe amounts or growth.
  snapshot_sha256: 348b20478bba221cc21e285237104281145111be6ea3aa30d381d6eae19c0a90
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch068/record09/quantity-inventory.json
  accessed_at: '2026-10-28T13:30:15.611876Z'
  support: context_only
  summary: Complete local concentration and source-stage decision inventory; includes
    exact local paths and source failure limits.
  snapshot_sha256: 711cc92782befc68f311d56b60c932bc6403afd61483682a040ae019dcb66e4d
- evidence_id: grounding
  kind: record_content
  reference: REVIEW_WORK/batch068/record09/grounding-inventory.json
  accessed_at: '2026-10-28T13:17:57.867320Z'
  support: context_only
  summary: All recursive asserted identifier/label slots, exact current OLS objects
    and current packaged MIM preferred-row joins.
  snapshot_sha256: 9c90ad265cccdfb22f9c15846a975166c69a857925311dafbfb81114f48c4a63
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch068/record09/history-and-evidence-inventory.json
  accessed_at: '2026-10-28T13:17:57.867352Z'
  support: context_only
  summary: Complete current history, references and attached evidence; source-specific
    claims are assessed without authenticating historical execution from code.
  snapshot_sha256: 83e1898c44b2b0115219a7b8f799cceda9906a61f6ad9f86acc54727a89e4d5d
- evidence_id: scalars
  kind: record_content
  reference: REVIEW_WORK/batch068/record09/scalar-census.json
  accessed_at: '2026-10-28T13:17:57.867376Z'
  support: context_only
  summary: Lossless scalar census of the selected target and all maintained contributors.
  snapshot_sha256: 18b80cf9ff82d39552fbf0bfcda205a499f0714aa2bc718fd7563e3018876709
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch068/record09/validate-schema.json
  accessed_at: '2026-10-28T13:13:48.638749Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed

    '
  snapshot_sha256: 1fbfaee6837af0f819099aa162193ba83232cfb693711b42f7cee72c8b970a64
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch068/record09/validate-strict.json
  accessed_at: '2026-10-28T13:13:49.553463Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch068/record09/strict.tsv\n"
  snapshot_sha256: 3e3e3cad31ae5140b06e9c71895b591ea4d9067219e68f5a48424a0a697e41b5
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch068/record09/validate-terms.json
  accessed_at: '2026-10-28T13:13:50.561250Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed

    '
  snapshot_sha256: 1e1f399b508be05b56f98c4dea790ac8475987e46b74027fa8a5382161f47cc9
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch068/record09/validate-references.json
  accessed_at: '2026-10-28T13:13:51.210812Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed

    '
  snapshot_sha256: 5089fd2102e89fe879f62f1600b4d15e05653674e3655f72ea618a0813ab7af0
- evidence_id: komodo49exact
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=49
  locator: Exact historical /komodo/servlet/ MediaInfo route; HTTP status and retained
    response metadata
  accessed_at: '2026-10-28T13:28:38.681378Z'
  support: context_only
  summary: Exact historical route returned 403. Block-page bytes and original access
    metadata are retained; no source formulation or atmosphere is authenticated. Earlier
    alternate-path attempts remain preserved separately.
  snapshot_sha256: b561a0beb87ccb8eb1d31690e78d800923fc46a9c000f3dbe849c746b8f9b37a
- evidence_id: komodo49_435exact
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=49_435
  locator: Exact historical /komodo/servlet/ MediaInfo route; HTTP status and retained
    response metadata
  accessed_at: '2026-10-28T13:28:38.672679Z'
  support: context_only
  summary: Exact historical route returned 403. Block-page bytes and original access
    metadata are retained; no source formulation or atmosphere is authenticated. Earlier
    alternate-path attempts remain preserved separately.
  snapshot_sha256: e6b9b3d76e13a3b70a9b3c36b7c8499249141b640d9af1a226aa43b8ac0abebf
assessments:
- assessment_id: a1
  area: identity
  topic: Base accessions and separately named variant
  outcome: concern
  summary: Exact declared merged_from stems resolve three unique owners. DSMZ 49 base
    identity is directly verified; KOMODO 49 cross-reference is present in local evidence
    and historical mapping reports, but current mapping retrieval returned 403. KOMODO
    49_435 is a distinct accession and name with imported base composition; the local
    SOURCE_DUPLICATE label is not formulation evidence. DSM 435 identifies Myxococcus
    xanthus only and adds no growth claim.
  target_ids:
  - CultureMech:005633
  evidence_ids:
  - identity-search
  - api49
  - komodo49_435exact
  - dsm435_identity
  - source-audit
- assessment_id: a2
  area: evidence
  topic: Earlier evidence gaps versus current repairs
  outcome: concern
  summary: The September review and October 5 reports precede the October 7 evidence-only
    owner repairs. Both base-owner current byte hashes equal the reported resulting
    hashes; six quantity snippets now match fresh source bytes and exact rows. The
    generated target retains none of these quantity snippets or source references.
    Current quantity writers conservatively withhold mismatched/variant claims, and
    the current merge implementation unions evidence only across equal formulation
    content. This is an existing generated artifact gap; no claim that current code
    would reproduce it.
  target_ids:
  - CultureMech:005633
  evidence_ids:
  - source-audit
  - quantity-writer
  - mapping-writer
  - current-formulation
  - current-merger
- assessment_id: a3
  area: quantity
  topic: Quantity scope and inventory
  outcome: concern
  summary: Every selected target/owner concentration field has an explicit disposition;
    scoped dependency fields and source-only preparation are separate from receiving-medium
    rates.
  target_ids:
  - CultureMech:005633
  evidence_ids:
  - quantities
  details: '[{"quantity_id": "q1", "topic": "Casitone base rate versus unresolved
    variant", "source": {"evidence_id": "api49", "reference": "https://mediadive.dsmz.de/rest/medium/49",
    "raw_path": "REVIEW_WORK/batch068/source09/api49.bin", "raw_sha256": "5e702b51e94e3e9df5b8ca11855ae622be07093d77b4c957ecc3b0faad56a943",
    "locator": "$.data.solutions[0].recipe[0] and .volume", "accessed_at": "2026-10-28T13:13:57.316817Z",
    "source_object": {"recipe_order": 1, "compound": "Casitone", "compound_id": 84,
    "amount": 3, "unit": "g", "g_l": 3, "optional": 0}, "provider_volume_ml": 1000},
    "decision": "mixed", "rationale": "Exact API reports 3 g and g_l=3; 3 g / (1000
    ml / 1000 ml per L) = 3 g/L on its declared provider basis. PDF agrees with absolute
    batch input. This is not independently measured final volume; no rate is extended
    to 49_435.", "layer_assessments": [{"path": "data/merge_yaml/merged/C_10_MEDIUM.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "3", "unit":
    "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact DSMZ 49 base rate
    and form agree with the stored scalar; retain provider scope and attach/preserve
    claim-level evidence."}, {"path": "data/normalized_yaml/bacterial/KOMODO_49_C_10_medium.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "3", "unit":
    "G_PER_L"}, "decision": "verified", "rationale": "Existing attached ingredient
    evidence is verified at the exact source row against fresh original API bytes,
    literal snippet and stored whole-response digest. Preserve this existing base-owner
    repair and its provider-volume scope."}, {"path": "data/normalized_yaml/bacterial/c_10_medium.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "3", "unit":
    "G_PER_L"}, "decision": "verified", "rationale": "Existing attached ingredient
    evidence is verified at the exact source row against fresh original API bytes,
    literal snippet and stored whole-response digest. Preserve this existing base-owner
    repair and its provider-volume scope."}, {"path": "data/normalized_yaml/bacterial/medium_49_modified_for_dsm_435.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "3", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "Base recipe import and local
    duplicate annotation do not authenticate this separately named variant; no replacement
    amount proposed."}]}, {"quantity_id": "q2", "topic": "CaCl2 x 2 H2O base rate
    versus unresolved variant", "source": {"evidence_id": "api49", "reference": "https://mediadive.dsmz.de/rest/medium/49",
    "raw_path": "REVIEW_WORK/batch068/source09/api49.bin", "raw_sha256": "5e702b51e94e3e9df5b8ca11855ae622be07093d77b4c957ecc3b0faad56a943",
    "locator": "$.data.solutions[0].recipe[1] and .volume", "accessed_at": "2026-10-28T13:13:57.316817Z",
    "source_object": {"recipe_order": 2, "compound": "CaCl2 x 2 H2O", "compound_id":
    7, "amount": 1.36, "unit": "g", "g_l": 1.36, "mmol_l": 9.25076, "optional": 0},
    "provider_volume_ml": 1000}, "decision": "mixed", "rationale": "Exact API reports
    1.36 g and g_l=1.36; 1.36 g / (1000 ml / 1000 ml per L) = 1.36 g/L on its declared
    provider basis. PDF agrees with absolute batch input. This is not independently
    measured final volume; no rate is extended to 49_435.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/C_10_MEDIUM.yaml", "field_path": "ingredients[1].concentration",
    "stored_value": {"value": "1.36", "unit": "G_PER_L"}, "decision": "evidence_only",
    "rationale": "Exact DSMZ 49 base rate and form agree with the stored scalar; retain
    provider scope and attach/preserve claim-level evidence."}, {"path": "data/normalized_yaml/bacterial/KOMODO_49_C_10_medium.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "1.36",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "Existing attached ingredient
    evidence is verified at the exact source row against fresh original API bytes,
    literal snippet and stored whole-response digest. Preserve this existing base-owner
    repair and its provider-volume scope."}, {"path": "data/normalized_yaml/bacterial/c_10_medium.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "1.36",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "Existing attached ingredient
    evidence is verified at the exact source row against fresh original API bytes,
    literal snippet and stored whole-response digest. Preserve this existing base-owner
    repair and its provider-volume scope."}, {"path": "data/normalized_yaml/bacterial/medium_49_modified_for_dsm_435.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "1.36",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Base recipe import
    and local duplicate annotation do not authenticate this separately named variant;
    no replacement amount proposed."}]}, {"quantity_id": "q3", "topic": "Agar base
    rate versus unresolved variant", "source": {"evidence_id": "api49", "reference":
    "https://mediadive.dsmz.de/rest/medium/49", "raw_path": "REVIEW_WORK/batch068/source09/api49.bin",
    "raw_sha256": "5e702b51e94e3e9df5b8ca11855ae622be07093d77b4c957ecc3b0faad56a943",
    "locator": "$.data.solutions[0].recipe[2] and .volume", "accessed_at": "2026-10-28T13:13:57.316817Z",
    "source_object": {"recipe_order": 3, "compound": "Agar", "compound_id": 3, "amount":
    15, "unit": "g", "g_l": 15, "mmol_l": 44.5991, "optional": 0}, "provider_volume_ml":
    1000}, "decision": "mixed", "rationale": "Exact API reports 15 g and g_l=15; 15
    g / (1000 ml / 1000 ml per L) = 15 g/L on its declared provider basis. PDF agrees
    with absolute batch input. This is not independently measured final volume; no
    rate is extended to 49_435.", "layer_assessments": [{"path": "data/merge_yaml/merged/C_10_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "15",
    "unit": "G_PER_L"}, "decision": "evidence_only", "rationale": "Exact DSMZ 49 base
    rate and form agree with the stored scalar; retain provider scope and attach/preserve
    claim-level evidence."}, {"path": "data/normalized_yaml/bacterial/KOMODO_49_C_10_medium.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "15",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "Existing attached ingredient
    evidence is verified at the exact source row against fresh original API bytes,
    literal snippet and stored whole-response digest. Preserve this existing base-owner
    repair and its provider-volume scope."}, {"path": "data/normalized_yaml/bacterial/c_10_medium.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "15",
    "unit": "G_PER_L"}, "decision": "verified", "rationale": "Existing attached ingredient
    evidence is verified at the exact source row against fresh original API bytes,
    literal snippet and stored whole-response digest. Preserve this existing base-owner
    repair and its provider-volume scope."}, {"path": "data/normalized_yaml/bacterial/medium_49_modified_for_dsm_435.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "15",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Base recipe import
    and local duplicate annotation do not authenticate this separately named variant;
    no replacement amount proposed."}]}, {"quantity_id": "q4", "topic": "Base pH",
    "source": {"evidence_id": "api49", "reference": "https://mediadive.dsmz.de/rest/medium/49",
    "raw_path": "REVIEW_WORK/batch068/source09/api49.bin", "raw_sha256": "5e702b51e94e3e9df5b8ca11855ae622be07093d77b4c957ecc3b0faad56a943",
    "locator": "$.data.medium and $.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T13:13:57.316817Z"},
    "decision": "mixed", "rationale": "The exact base formulation supports this field;
    the variant remains separately unresolved.", "layer_assessments": [{"path": "data/merge_yaml/merged/C_10_MEDIUM.yaml",
    "field_path": "ph_value", "stored_value": 7.2, "decision": "evidence_only", "rationale":
    "Base source explicitly supports pH 7.2 and nonoptional agar; retain the current
    base descriptor."}, {"path": "data/normalized_yaml/bacterial/KOMODO_49_C_10_medium.yaml",
    "field_path": "ph_value", "stored_value": 7.2, "decision": "evidence_only", "rationale":
    "Base source explicitly supports pH 7.2 and nonoptional agar; retain the current
    base descriptor."}, {"path": "data/normalized_yaml/bacterial/c_10_medium.yaml",
    "field_path": "ph_value", "stored_value": 7.2, "decision": "evidence_only", "rationale":
    "Base source explicitly supports pH 7.2 and nonoptional agar; retain the current
    base descriptor."}, {"path": "data/normalized_yaml/bacterial/medium_49_modified_for_dsm_435.yaml",
    "field_path": "ph_value", "stored_value": 7.2, "decision": "unsupported", "rationale":
    "No exact variant formulation; copied base pH/state does not establish the variant."}]},
    {"quantity_id": "q5", "topic": "Base solid state", "source": {"evidence_id": "api49",
    "reference": "https://mediadive.dsmz.de/rest/medium/49", "raw_path": "REVIEW_WORK/batch068/source09/api49.bin",
    "raw_sha256": "5e702b51e94e3e9df5b8ca11855ae622be07093d77b4c957ecc3b0faad56a943",
    "locator": "$.data.medium and $.data.solutions[0].recipe[2]", "accessed_at": "2026-10-28T13:13:57.316817Z"},
    "decision": "mixed", "rationale": "The exact base formulation supports this field;
    the variant remains separately unresolved.", "layer_assessments": [{"path": "data/merge_yaml/merged/C_10_MEDIUM.yaml",
    "field_path": "physical_state", "stored_value": "SOLID_AGAR", "decision": "evidence_only",
    "rationale": "Base source explicitly supports pH 7.2 and nonoptional agar; retain
    the current base descriptor."}, {"path": "data/normalized_yaml/bacterial/KOMODO_49_C_10_medium.yaml",
    "field_path": "physical_state", "stored_value": "SOLID_AGAR", "decision": "evidence_only",
    "rationale": "Base source explicitly supports pH 7.2 and nonoptional agar; retain
    the current base descriptor."}, {"path": "data/normalized_yaml/bacterial/c_10_medium.yaml",
    "field_path": "physical_state", "stored_value": "SOLID_AGAR", "decision": "evidence_only",
    "rationale": "Base source explicitly supports pH 7.2 and nonoptional agar; retain
    the current base descriptor."}, {"path": "data/normalized_yaml/bacterial/medium_49_modified_for_dsm_435.yaml",
    "field_path": "physical_state", "stored_value": "SOLID_AGAR", "decision": "unsupported",
    "rationale": "No exact variant formulation; copied base pH/state does not establish
    the variant."}]}, {"quantity_id": "q6", "topic": "Source water input and provider
    volume", "source": {"evidence_id": "api49", "reference": "https://mediadive.dsmz.de/rest/medium/49",
    "raw_path": "REVIEW_WORK/batch068/source09/api49.bin", "raw_sha256": "5e702b51e94e3e9df5b8ca11855ae622be07093d77b4c957ecc3b0faad56a943",
    "locator": "$.data.solutions[0].recipe[3] and .volume", "accessed_at": "2026-10-28T13:13:57.316817Z"},
    "decision": "mixed", "rationale": "All four complete local documents lack a water
    row or explicit water-input quantity. API names 1000 ml distilled water and provider
    volume 1000; PDF supplies water input only. Curate base solvent/batch scope; no
    water-to-final-volume assumption.", "layer_assessments": [{"path": "data/merge_yaml/merged/C_10_MEDIUM.yaml",
    "field_path": "source_water_input", "stored_value": null, "decision": "add", "rationale":
    "Record the exact 1000 ml distilled-water input at its preparation stage without
    inventing a measured final volume.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_49_C_10_medium.yaml",
    "field_path": "source_water_input", "stored_value": null, "decision": "add", "rationale":
    "Record the exact 1000 ml distilled-water input at its preparation stage without
    inventing a measured final volume.", "missing": true}, {"path": "data/normalized_yaml/bacterial/c_10_medium.yaml",
    "field_path": "source_water_input", "stored_value": null, "decision": "add", "rationale":
    "Record the exact 1000 ml distilled-water input at its preparation stage without
    inventing a measured final volume.", "missing": true}, {"path": "data/normalized_yaml/bacterial/medium_49_modified_for_dsm_435.yaml",
    "field_path": "source_water_input", "stored_value": null, "decision": "unsupported",
    "rationale": "No exact variant formulation; do not add a base water amount.",
    "missing": true}]}, {"quantity_id": "q7", "topic": "Ordered pH preparation", "source":
    {"evidence_id": "api49", "reference": "https://mediadive.dsmz.de/rest/medium/49",
    "raw_path": "REVIEW_WORK/batch068/source09/api49.bin", "raw_sha256": "5e702b51e94e3e9df5b8ca11855ae622be07093d77b4c957ecc3b0faad56a943",
    "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T13:13:57.316817Z",
    "quote": "Adjust pH to 7.2 before adding agar."}, "decision": "mixed", "rationale":
    "A scalar pH does not preserve the stated order before agar. Current resolver
    copies composition/pH/state, not this ordered preparation; the present merger
    is conservative and does not authorize forcing these owners together.", "layer_assessments":
    [{"path": "data/normalized_yaml/bacterial/c_10_medium.yaml", "field_path": "preparation_steps[0].description",
    "stored_value": "Adjust pH to 7.2 before adding agar.", "decision": "evidence_only",
    "rationale": "Exact instruction already retained by the direct owner; preserve
    it."}, {"path": "data/merge_yaml/merged/C_10_MEDIUM.yaml", "field_path": "preparation_steps",
    "stored_value": null, "decision": "add", "rationale": "The base preparation sequence
    is missing; restore from the exact source through the owner and compatible regeneration.",
    "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_49_C_10_medium.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "add", "rationale":
    "The base preparation sequence is missing; restore from the exact source through
    the owner and compatible regeneration.", "missing": true}, {"path": "data/normalized_yaml/bacterial/medium_49_modified_for_dsm_435.yaml",
    "field_path": "preparation_steps", "stored_value": null, "decision": "unsupported",
    "rationale": "Variant-specific preparation not retrieved; do not borrow the base
    instruction.", "missing": true}]}, {"quantity_id": "q8", "topic": "KOMODO atmosphere
    annotation", "source": {"evidence_id": "komodo49exact", "reference": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=49",
    "raw_path": "REVIEW_WORK/batch068/source09-exact-route/komodo49exact.bin", "raw_sha256":
    "b561a0beb87ccb8eb1d31690e78d800923fc46a9c000f3dbe849c746b8f9b37a", "accessed_at":
    "2026-10-28T13:28:38.681378Z", "scope": "Exact historical /komodo/servlet/ route
    returned 403; original alternate-path attempts also preserved. No atmosphere authenticated."},
    "decision": "unsupported", "rationale": "The DSMZ 49 recipe does not state an
    atmosphere. The accessible DSM 435 catalogue concerns other media and cannot authenticate
    or correct this C/10 annotation.", "layer_assessments": [{"path": "data/merge_yaml/merged/C_10_MEDIUM.yaml",
    "field_path": "notes", "stored_value": "Source: KOMODO ModelSEED | ID: 49 | DSMZ
    Medium: 49 (mediadive.medium:49) | Aerobic: No", "decision": "unsupported", "rationale":
    "Aerobic: No is a source metadata assertion without authenticated current support;
    do not infer an incubation atmosphere or flip it from organism taxonomy."}, {"path":
    "data/normalized_yaml/bacterial/KOMODO_49_C_10_medium.yaml", "field_path": "notes",
    "stored_value": "Source: KOMODO ModelSEED | ID: 49 | DSMZ Medium: 49 (mediadive.medium:49)
    | Aerobic: No", "decision": "unsupported", "rationale": "Aerobic: No is a source
    metadata assertion without authenticated current support; do not infer an incubation
    atmosphere or flip it from organism taxonomy."}, {"path": "data/normalized_yaml/bacterial/medium_49_modified_for_dsm_435.yaml",
    "field_path": "notes", "stored_value": "Source: KOMODO ModelSEED | ID: 49_435
    | DSMZ Medium: 49 (mediadive.medium:49) | Aerobic: No", "decision": "unsupported",
    "rationale": "Aerobic: No is a source metadata assertion without authenticated
    current support; do not infer an incubation atmosphere or flip it from organism
    taxonomy."}]}]'
- assessment_id: a4
  area: grounding
  topic: Current ontology and MIM correspondence
  outcome: supported
  summary: Every asserted primary and secondary chemical slot carries CHEBI:86158/calcium
    chloride dihydrate or CHEBI:2509/agar. Fresh OLS preferred labels, nonobsolete
    flags, calcium dihydrate formula/mass/CAS and agar mixture definition agree. Exact
    current MIM joins retain MAPPED preferred rows and the separate REJECTED CaCl22H2O
    row; that rejected alias does not invalidate the asserted calcium-chloride-dihydrate
    ID. Casitone remains an undefined ungrounded source component; no unsupported
    pure-compound identity is proposed. Identifier correspondence does not authenticate
    variant quantities.
  target_ids:
  - CultureMech:005633
  evidence_ids:
  - grounding
- assessment_id: a5
  area: provenance
  topic: History and evidence scope
  outcome: concern
  summary: Complete four local histories, references and evidence were inventoried.
    Six base-owner quantity snippets are authenticated against exact current raw bytes
    and their stored source hash; historical KOMODO mapping bytes were not retrieved.
    October 7 repairs remain intact, while the generated history predates them. Current
    import, resolver, quantity writers and compatible merger were read separately
    from historical claims. Malformed/naive timestamps remain explicit uncertainty.
  target_ids:
  - CultureMech:005633
  evidence_ids:
  - history
  - scalars
- assessment_id: a6
  area: scope
  topic: Growth and taxonomic evidence
  outcome: unknown
  summary: Generic cultivation applications and bacterial filing are not strain-level
    growth evidence. No organism-specific growth, temperature or atmosphere is inferred
    from names or source catalog identifiers.
  target_ids:
  - CultureMech:005633
  evidence_ids:
  - local-target
- assessment_id: a7
  area: schema
  topic: Canonical diagnostics
  outcome: supported
  summary: All four original canonical diagnostics passed. Reference checks were zero;
    structural and term diagnostics do not establish formulation accuracy.
  target_ids:
  - CultureMech:005633
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-005633-variant-equivalence-is-not-established
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Variant equivalence is not established
  description: KOMODO 49_435 is explicitly named as a DSM 435 modification, but it
    has only copied base composition and a SOURCE_DUPLICATE parent relation. Exact
    source retrieval failed 403. Preserve its accession and resolve its own formulation
    before endorsing copied quantities or consolidating it with the base. The base
    recipe and strain catalogue do not fill that evidence gap.
  target_ids:
  - CultureMech:005633
  field_paths:
  - merged_from
  - synonyms
  - variant_relationship
  - parent_media
  - variant_children
  - ingredients
  evidence_ids:
  - identity-search
  - komodo49_435exact
  - source-audit
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_49_modified_for_dsm_435.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_49_C_10_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/c_10_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f2
  issue_key: culturemech-005633-base-water-input-and-preparation-order-are-incomplete
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Base water input and preparation order are incomplete
  description: The base PDF/API include distilled-water input and an instruction placing
    pH adjustment before agar. All local layers omit the water-input quantity; the
    direct DSMZ owner already preserves the ordered instruction while the KOMODO base
    owner and generated target omit it. Keep provider volume distinct from water input
    and do not transfer these details to the unresolved variant.
  target_ids:
  - CultureMech:005633
  field_paths:
  - ingredients
  - preparation_steps
  - ph_value
  evidence_ids:
  - api49
  - dsm49
  - owner-1
  - owner-2
  - dsm-resolver
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_49_C_10_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/c_10_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f3
  issue_key: culturemech-005633-generated-base-claims-omit-repaired-owner-evidence
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Generated base claims omit repaired owner evidence
  description: Both maintained base owners already carry three exact quantity excerpts
    and source references; six claims authenticate against the freshly retrieved unchanged
    raw API response. The generated target has no claim-level excerpts or structured
    source references. Preserve these repairs and resolve grouping before regeneration;
    do not reapply obsolete all-owner missing-evidence findings.
  target_ids:
  - CultureMech:005633
  field_paths:
  - ingredients[].evidence
  - references
  - evidence
  - curation_history
  evidence_ids:
  - source-audit
  - local-target
  - owner-1
  - owner-2
  - current-formulation
  - current-merger
  rule_id: source-stage-or-identity
  native_severity: P3
  normalization_reason: 'Minor: bounded metadata or traceability defect without establishing
    a new formulation.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_49_C_10_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/c_10_medium.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f4
  issue_key: culturemech-005633-komodo-import-history-contains-a-malformed-timestamp
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: KOMODO import history contains a malformed timestamp
  description: The selected target and two KOMODO contributors retain the literal
    timestamp 2026-01-27T01:15:02.fZ. Current importer uses time.strftime with a microsecond
    token and the resolver emits naive local timestamps; this identifies current metadata-generation
    weaknesses without proving past execution. Preserve original events and append
    a documented correction only when original time evidence exists.
  target_ids:
  - CultureMech:005633
  field_paths:
  - curation_history[0].timestamp
  - curation_history
  evidence_ids:
  - komodo-import
  - dsm-resolver
  - local-target
  - owner-1
  - owner-3
  rule_id: source-stage-or-identity
  native_severity: P3
  normalization_reason: 'Minor: bounded metadata or traceability defect without establishing
    a new formulation.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_49_C_10_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_49_modified_for_dsm_435.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
actions:
- action_id: action1
  description: Retrieve an exact authoritative 49_435 formulation or explicit no-change
    provenance. Resolve the variant relationship in maintained contributors, retaining
    unresolved identity until evidence supports equivalence; regenerate compatible
    groups only.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:005633
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_49_modified_for_dsm_435.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_49_C_10_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/c_10_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action2
  description: Preserve the direct owner preparation, add source-backed base water-input/batch
    metadata and missing base preparation to the relevant owner, then regenerate without
    forcing unequal formulations or assigning base details to 49_435.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:005633
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_49_C_10_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/c_10_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action3
  description: Regenerate after contributor identity and preparation reconciliation,
    preserving exact evidence scope and base references. Confirm the resulting artifact
    retains these claims; leave unsupported variant claims unendorsed.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:005633
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_49_C_10_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/c_10_medium.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action4
  description: 'Maintain append-only history: document the malformed timestamp and
    its uncertainty; repair the writer formatting separately without inventing a historic
    fractional time or timezone.'
  finding_ids:
  - f4
  target_ids:
  - CultureMech:005633
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_49_C_10_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_49_modified_for_dsm_435.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
limitations:
- Exact KOMODO list, base and 49_435 routes returned 403. Their historical mapping
  excerpts are local context, not authenticated current full responses; the variant
  formulation and atmosphere remain unresolved. Obtain exact accessible authoritative
  source evidence before endorsing variant quantities or equivalence.
- DSM 435 catalogue was used for identity scope only. No strain-specific growth on
  C/10, growth conditions, or taxonomy grounding has been added. The PDF water input
  is not an independent final-volume measurement. Keep future organism growth and
  final-volume claims scoped to direct evidence.
notes:
- Fresh review; historical lost snapshots were not reconstructed. All inspected source
  files remain unchanged.
- This draft authoring step performed no formal review validation/save, Git mutation
  or publication.
```
