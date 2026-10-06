# Ingredient Concentration Review

- Record: data/merge_yaml/merged/nutrient_broth__3e8602c5.yaml
- ID: CultureMech:015471
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 9bcdadfdd1bd295aecb64f11f412a91e226c6f1ecd0463105099917bd4463ba3
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/5
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/TOGO_M2418_Nutrient_Broth.yaml
- data/normalized_yaml/bacterial/TOGO_M2783_Nutrient_broth.yaml
- data/normalized_yaml/bacterial/TOGO_M681_Nutrient_Broth.yaml
- data/normalized_yaml/bacterial/nutrient_broth.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Bacto Peptone | {"value": "15", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Yeast Extract | {"value": "3", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / D-Glucose | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Sodium Chloride | {"value": "6", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| variants[0].modifications / nutrient_broth_mycolicibacterium_cosmeticum_dm11_25c | ["Use Mycolicibacterium cosmeticum strain DM-11 as the target strain.", "Incubate at 25 C."] | incomplete_or_nonqualifying_attached_evidence; VARIANT_TEXT_REQUIRES_SOURCE_REVIEW | unsupported; not_performed | unknown | [{"reference": "PMID:16461697", "supports": "SUPPORT", "snippet": "The strain, designated strain DM-11, grew optimally at 25 degrees C and had a doubling time of 29.2 h.", "explanation": "Literature evidence supports a strain-specific 25 C growth condition variant under the parent Nutrient Broth record."}] |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://github.com/CultureBotAI/CultureBotHT

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
