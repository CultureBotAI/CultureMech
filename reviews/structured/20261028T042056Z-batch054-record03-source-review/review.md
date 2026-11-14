# BTU medium: flattened stock stages and conflicting source versions

- Review: 20261028T042056Z-batch054-record03-source-review
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-10-28T03:58:39.394929Z
- Finished UTC: 2026-10-28T04:20:56.855805Z
- Reviewer: Codex independent source reviewer (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

The selected BTU merge and five contributors flatten basal ingredients, separate stocks, optional supplements and solvent amounts into one ingredient list. Current provider objects explain many stored numbers but do not support their use as universal receiving-medium concentrations. Embedded DSM413, standalone DSM78 and current provider records conflict in cysteine form and vitamin details; exact KOMODO variants remain inaccessible. Existing DSM preparation and current stock-separation/no-summing guards are credited.

## Scope And Provenance

Full selected record and exact maintained contributors; external source limits explicitly retained.

Selection: Actual batch054 native selection index 03.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9ea7ff33d354e37b791df96a880005153e446ce3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:005240 | data/merge_yaml/merged/BTU_MEDIUM.yaml | generated | btu_medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate-schema | passed | True | CultureMech:005240 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-strict | passed | True | CultureMech:005240 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-terms | passed | True | CultureMech:005240 | Original once-only canonical command exited 0; full stdout/stderr retained and read. |
| validate-references | passed | True | CultureMech:005240 | Native reference checker performed zero reference checks; this is not claim authentication. |

## Scientific And Domain Assessments

### Provider correspondence versus primary version conflict

evidence: concern. Targets: CultureMech:005240.

The current API explains local numerical provenance, including 1025 mL-based rates and nested stock strengths. Embedded 413 and standalone 78 are not identical; their literal conflicting cysteine/vitamin statements are retained. Exact current KOMODO variants returned 403.

### Complete quantity and numeric preparation audit

quantity: concern. Targets: CultureMech:005240.

Every local concentration field has an explicit disposition; source-only doses, batch volumes and conditional preparation are separate from receiving-medium rates.

[{"quantity_id": "q1", "topic": "Sodium formate stock", "source": {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256": "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator": "$.data.solutions[1].recipe[0]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"}, "decision": "correct", "rationale": "The provider 60 g/L belongs to the Formiate/Fumarate stock. DSM413 gives 6 g formate and 6 g fumarate with 100 mL water, then 30µL stock per 1 mL basal medium. Retain stock correspondence but remove the unconditional final-ingredient interpretation; do not substitute 6 g/L or 60 g/L as final BTU.", "layer_assessments": [{"path": "data/merge_yaml/merged/BTU_MEDIUM.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "60", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The provider 60 g/L belongs to the Formiate/Fumarate stock. DSM413 gives 6 g formate and 6 g fumarate with 100 mL water, then 30µL stock per 1 mL basal medium. Retain stock correspondence but remove the unconditional final-ingredient interpretation; do not substitute 6 g/L or 60 g/L as final BTU."}, {"path": "data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "60", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The provider 60 g/L belongs to the Formiate/Fumarate stock. DSM413 gives 6 g formate and 6 g fumarate with 100 mL water, then 30µL stock per 1 mL basal medium. Retain stock correspondence but remove the unconditional final-ingredient interpretation; do not substitute 6 g/L or 60 g/L as final BTU."}, {"path": "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "60", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The provider 60 g/L belongs to the Formiate/Fumarate stock. DSM413 gives 6 g formate and 6 g fumarate with 100 mL water, then 30µL stock per 1 mL basal medium. Retain stock correspondence but remove the unconditional final-ingredient interpretation; do not substitute 6 g/L or 60 g/L as final BTU."}, {"path": "data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "60", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The provider 60 g/L belongs to the Formiate/Fumarate stock. DSM413 gives 6 g formate and 6 g fumarate with 100 mL water, then 30µL stock per 1 mL basal medium. Retain stock correspondence but remove the unconditional final-ingredient interpretation; do not substitute 6 g/L or 60 g/L as final BTU. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "60", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The provider 60 g/L belongs to the Formiate/Fumarate stock. DSM413 gives 6 g formate and 6 g fumarate with 100 mL water, then 30µL stock per 1 mL basal medium. Retain stock correspondence but remove the unconditional final-ingredient interpretation; do not substitute 6 g/L or 60 g/L as final BTU. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml", "field_path": "ingredients[0].concentration", "stored_value": {"value": "60", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The provider 60 g/L belongs to the Formiate/Fumarate stock. DSM413 gives 6 g formate and 6 g fumarate with 100 mL water, then 30µL stock per 1 mL basal medium. Retain stock correspondence but remove the unconditional final-ingredient interpretation; do not substitute 6 g/L or 60 g/L as final BTU. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}]}, {"quantity_id": "q2", "topic": "Disodium fumarate stock", "source": {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256": "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator": "$.data.solutions[1].recipe[1]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"}, "decision": "correct", "rationale": "The provider 60 g/L is the second component of the same both-salt stock, not a final-medium dose. The exact DSM413 table contains BOTH salts. The named KOMODO replacement remains independently unresolved.", "layer_assessments": [{"path": "data/merge_yaml/merged/BTU_MEDIUM.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "60", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The provider 60 g/L is the second component of the same both-salt stock, not a final-medium dose. The exact DSM413 table contains BOTH salts. The named KOMODO replacement remains independently unresolved."}, {"path": "data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "60", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The provider 60 g/L is the second component of the same both-salt stock, not a final-medium dose. The exact DSM413 table contains BOTH salts. The named KOMODO replacement remains independently unresolved."}, {"path": "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "60", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The provider 60 g/L is the second component of the same both-salt stock, not a final-medium dose. The exact DSM413 table contains BOTH salts. The named KOMODO replacement remains independently unresolved."}, {"path": "data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "60", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The provider 60 g/L is the second component of the same both-salt stock, not a final-medium dose. The exact DSM413 table contains BOTH salts. The named KOMODO replacement remains independently unresolved. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "60", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The provider 60 g/L is the second component of the same both-salt stock, not a final-medium dose. The exact DSM413 table contains BOTH salts. The named KOMODO replacement remains independently unresolved. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml", "field_path": "ingredients[1].concentration", "stored_value": {"value": "60", "unit": "G_PER_L"}, "decision": "correct", "rationale": "The provider 60 g/L is the second component of the same both-salt stock, not a final-medium dose. The exact DSM413 table contains BOTH salts. The named KOMODO replacement remains independently unresolved. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}]}, {"quantity_id": "q3", "topic": "Beef extraction precursor", "source": {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256": "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator": "$.data.solutions[2].recipe[0]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"}, "decision": "unsupported", "rationale": "Current provider explicitly reports 487.805 g/L on its 1025 mL Main sol.78 object, matching local digits. Primary source instead describes 500 g extraction precursor, removal/retention of meat and filtrate, and filtrate makeup to 1000 mL. Neither retained solids nor finished BTU beef concentration is thereby established.", "layer_assessments": [{"path": "data/merge_yaml/merged/BTU_MEDIUM.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "487.805", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Current provider explicitly reports 487.805 g/L on its 1025 mL Main sol.78 object, matching local digits. Primary source instead describes 500 g extraction precursor, removal/retention of meat and filtrate, and filtrate makeup to 1000 mL. Neither retained solids nor finished BTU beef concentration is thereby established."}, {"path": "data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "487.805", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Current provider explicitly reports 487.805 g/L on its 1025 mL Main sol.78 object, matching local digits. Primary source instead describes 500 g extraction precursor, removal/retention of meat and filtrate, and filtrate makeup to 1000 mL. Neither retained solids nor finished BTU beef concentration is thereby established."}, {"path": "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "487.805", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Current provider explicitly reports 487.805 g/L on its 1025 mL Main sol.78 object, matching local digits. Primary source instead describes 500 g extraction precursor, removal/retention of meat and filtrate, and filtrate makeup to 1000 mL. Neither retained solids nor finished BTU beef concentration is thereby established."}, {"path": "data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "487.805", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Current provider explicitly reports 487.805 g/L on its 1025 mL Main sol.78 object, matching local digits. Primary source instead describes 500 g extraction precursor, removal/retention of meat and filtrate, and filtrate makeup to 1000 mL. Neither retained solids nor finished BTU beef concentration is thereby established. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "487.805", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Current provider explicitly reports 487.805 g/L on its 1025 mL Main sol.78 object, matching local digits. Primary source instead describes 500 g extraction precursor, removal/retention of meat and filtrate, and filtrate makeup to 1000 mL. Neither retained solids nor finished BTU beef concentration is thereby established. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml", "field_path": "ingredients[2].concentration", "stored_value": {"value": "487.805", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Current provider explicitly reports 487.805 g/L on its 1025 mL Main sol.78 object, matching local digits. Primary source instead describes 500 g extraction precursor, removal/retention of meat and filtrate, and filtrate makeup to 1000 mL. Neither retained solids nor finished BTU beef concentration is thereby established. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}]}, {"quantity_id": "q4", "topic": "NaOH solution dimensions and stages", "source": {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256": "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator": "$.data.solutions[2].recipe[2]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"}, "decision": "correct", "rationale": "Local 26 G_PER_L sums 25 mL1N NaOH in the extraction stage and 1 mL1N NaOH in the separate hemin stock. These are solution volumes with a stated normality, not two masses with a common denominator. Keep the two stages separate; no density/normality conversion or sum is justified.", "layer_assessments": [{"path": "data/merge_yaml/merged/BTU_MEDIUM.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "26.0", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 26 G_PER_L sums 25 mL1N NaOH in the extraction stage and 1 mL1N NaOH in the separate hemin stock. These are solution volumes with a stated normality, not two masses with a common denominator. Keep the two stages separate; no density/normality conversion or sum is justified."}, {"path": "data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "26.0", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 26 G_PER_L sums 25 mL1N NaOH in the extraction stage and 1 mL1N NaOH in the separate hemin stock. These are solution volumes with a stated normality, not two masses with a common denominator. Keep the two stages separate; no density/normality conversion or sum is justified."}, {"path": "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "26.0", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 26 G_PER_L sums 25 mL1N NaOH in the extraction stage and 1 mL1N NaOH in the separate hemin stock. These are solution volumes with a stated normality, not two masses with a common denominator. Keep the two stages separate; no density/normality conversion or sum is justified."}, {"path": "data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "26.0", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 26 G_PER_L sums 25 mL1N NaOH in the extraction stage and 1 mL1N NaOH in the separate hemin stock. These are solution volumes with a stated normality, not two masses with a common denominator. Keep the two stages separate; no density/normality conversion or sum is justified. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "26.0", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 26 G_PER_L sums 25 mL1N NaOH in the extraction stage and 1 mL1N NaOH in the separate hemin stock. These are solution volumes with a stated normality, not two masses with a common denominator. Keep the two stages separate; no density/normality conversion or sum is justified. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml", "field_path": "ingredients[3].concentration", "stored_value": {"value": "26.0", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 26 G_PER_L sums 25 mL1N NaOH in the extraction stage and 1 mL1N NaOH in the separate hemin stock. These are solution volumes with a stated normality, not two masses with a common denominator. Keep the two stages separate; no density/normality conversion or sum is justified. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}]}, {"quantity_id": "q5", "topic": "Casitone after filtrate makeup", "source": {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256": "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator": "$.data.solutions[2].recipe[3]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"}, "decision": "unsupported", "rationale": "Provider 29.2683 g/L is an exact declared value on its 1025 mL object. Primary source places 30 g after filtrate makeup to 1000 mL. Preserve the 30 g batch addition and provider disagreement; do not silently assert an independently measured final BTU denominator.", "layer_assessments": [{"path": "data/merge_yaml/merged/BTU_MEDIUM.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "29.2683", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 29.2683 g/L is an exact declared value on its 1025 mL object. Primary source places 30 g after filtrate makeup to 1000 mL. Preserve the 30 g batch addition and provider disagreement; do not silently assert an independently measured final BTU denominator."}, {"path": "data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "29.2683", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 29.2683 g/L is an exact declared value on its 1025 mL object. Primary source places 30 g after filtrate makeup to 1000 mL. Preserve the 30 g batch addition and provider disagreement; do not silently assert an independently measured final BTU denominator."}, {"path": "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "29.2683", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 29.2683 g/L is an exact declared value on its 1025 mL object. Primary source places 30 g after filtrate makeup to 1000 mL. Preserve the 30 g batch addition and provider disagreement; do not silently assert an independently measured final BTU denominator."}, {"path": "data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "29.2683", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 29.2683 g/L is an exact declared value on its 1025 mL object. Primary source places 30 g after filtrate makeup to 1000 mL. Preserve the 30 g batch addition and provider disagreement; do not silently assert an independently measured final BTU denominator. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "29.2683", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 29.2683 g/L is an exact declared value on its 1025 mL object. Primary source places 30 g after filtrate makeup to 1000 mL. Preserve the 30 g batch addition and provider disagreement; do not silently assert an independently measured final BTU denominator. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml", "field_path": "ingredients[4].concentration", "stored_value": {"value": "29.2683", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 29.2683 g/L is an exact declared value on its 1025 mL object. Primary source places 30 g after filtrate makeup to 1000 mL. Preserve the 30 g batch addition and provider disagreement; do not silently assert an independently measured final BTU denominator. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}]}, {"quantity_id": "q6", "topic": "Yeast extract after filtrate makeup", "source": {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256": "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator": "$.data.solutions[2].recipe[4]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"}, "decision": "unsupported", "rationale": "Provider 4.87805 g/L is an exact declared value on its 1025 mL object. Primary source specifies 5 g after filtrate makeup. Preserve batch mass and denominator/stage conflict; no universal final rate is authenticated.", "layer_assessments": [{"path": "data/merge_yaml/merged/BTU_MEDIUM.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "4.87805", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 4.87805 g/L is an exact declared value on its 1025 mL object. Primary source specifies 5 g after filtrate makeup. Preserve batch mass and denominator/stage conflict; no universal final rate is authenticated."}, {"path": "data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "4.87805", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 4.87805 g/L is an exact declared value on its 1025 mL object. Primary source specifies 5 g after filtrate makeup. Preserve batch mass and denominator/stage conflict; no universal final rate is authenticated."}, {"path": "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "4.87805", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 4.87805 g/L is an exact declared value on its 1025 mL object. Primary source specifies 5 g after filtrate makeup. Preserve batch mass and denominator/stage conflict; no universal final rate is authenticated."}, {"path": "data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "4.87805", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 4.87805 g/L is an exact declared value on its 1025 mL object. Primary source specifies 5 g after filtrate makeup. Preserve batch mass and denominator/stage conflict; no universal final rate is authenticated. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "4.87805", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 4.87805 g/L is an exact declared value on its 1025 mL object. Primary source specifies 5 g after filtrate makeup. Preserve batch mass and denominator/stage conflict; no universal final rate is authenticated. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml", "field_path": "ingredients[5].concentration", "stored_value": {"value": "4.87805", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 4.87805 g/L is an exact declared value on its 1025 mL object. Primary source specifies 5 g after filtrate makeup. Preserve batch mass and denominator/stage conflict; no universal final rate is authenticated. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}]}, {"quantity_id": "q7", "topic": "Dipotassium hydrogen phosphate", "source": {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256": "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator": "$.data.solutions[2].recipe[5]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"}, "decision": "unsupported", "rationale": "Provider 4.87805 g/L matches local digits, but primary source specifies 5 g after filtrate makeup to 1000 mL. K2HPO4 identity is supported; do not choose a hydrate or final-medium denominator from this correspondence.", "layer_assessments": [{"path": "data/merge_yaml/merged/BTU_MEDIUM.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "4.87805", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 4.87805 g/L matches local digits, but primary source specifies 5 g after filtrate makeup to 1000 mL. K2HPO4 identity is supported; do not choose a hydrate or final-medium denominator from this correspondence."}, {"path": "data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "4.87805", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 4.87805 g/L matches local digits, but primary source specifies 5 g after filtrate makeup to 1000 mL. K2HPO4 identity is supported; do not choose a hydrate or final-medium denominator from this correspondence."}, {"path": "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "4.87805", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 4.87805 g/L matches local digits, but primary source specifies 5 g after filtrate makeup to 1000 mL. K2HPO4 identity is supported; do not choose a hydrate or final-medium denominator from this correspondence."}, {"path": "data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "4.87805", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 4.87805 g/L matches local digits, but primary source specifies 5 g after filtrate makeup to 1000 mL. K2HPO4 identity is supported; do not choose a hydrate or final-medium denominator from this correspondence. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "4.87805", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 4.87805 g/L matches local digits, but primary source specifies 5 g after filtrate makeup to 1000 mL. K2HPO4 identity is supported; do not choose a hydrate or final-medium denominator from this correspondence. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml", "field_path": "ingredients[6].concentration", "stored_value": {"value": "4.87805", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 4.87805 g/L matches local digits, but primary source specifies 5 g after filtrate makeup to 1000 mL. K2HPO4 identity is supported; do not choose a hydrate or final-medium denominator from this correspondence. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}]}, {"quantity_id": "q8", "topic": "Resazurin amount", "source": {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256": "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator": "$.data.solutions[2].recipe[6]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"}, "decision": "unsupported", "rationale": "Provider 0.00097561 g/L matches local digits; primary source specifies 1 mg batch addition after filtrate makeup.1 mg=0.001 g is a mass conversion only, not proof of final BTU volume. No sodium-salt substitution is inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/BTU_MEDIUM.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.00097561", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 0.00097561 g/L matches local digits; primary source specifies 1 mg batch addition after filtrate makeup.1 mg=0.001 g is a mass conversion only, not proof of final BTU volume. No sodium-salt substitution is inferred."}, {"path": "data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.00097561", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 0.00097561 g/L matches local digits; primary source specifies 1 mg batch addition after filtrate makeup.1 mg=0.001 g is a mass conversion only, not proof of final BTU volume. No sodium-salt substitution is inferred."}, {"path": "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.00097561", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 0.00097561 g/L matches local digits; primary source specifies 1 mg batch addition after filtrate makeup.1 mg=0.001 g is a mass conversion only, not proof of final BTU volume. No sodium-salt substitution is inferred."}, {"path": "data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.00097561", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 0.00097561 g/L matches local digits; primary source specifies 1 mg batch addition after filtrate makeup.1 mg=0.001 g is a mass conversion only, not proof of final BTU volume. No sodium-salt substitution is inferred. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.00097561", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 0.00097561 g/L matches local digits; primary source specifies 1 mg batch addition after filtrate makeup.1 mg=0.001 g is a mass conversion only, not proof of final BTU volume. No sodium-salt substitution is inferred. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml", "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.00097561", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 0.00097561 g/L matches local digits; primary source specifies 1 mg batch addition after filtrate makeup.1 mg=0.001 g is a mass conversion only, not proof of final BTU volume. No sodium-salt substitution is inferred. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}]}, {"quantity_id": "q9", "topic": "Cysteine identity/version", "source": {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256": "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator": "$.data.solutions[2].recipe[7]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"}, "decision": "unsupported", "rationale": "Local 0.487805 g/L L-cysteine hydrochloride matches provider Main sol.78 but conflicts with its own instruction 0.5 g/L L-cysteine hydrochloride. Embedded DSM413 says 0.5 g/L cysteine without HCl; standalone 78 explicitly says L-cysteine hydrochloride. Retain this source/version conflict rather than retroactively using newer 78 to authenticate embedded 413.", "layer_assessments": [{"path": "data/merge_yaml/merged/BTU_MEDIUM.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.487805", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Local 0.487805 g/L L-cysteine hydrochloride matches provider Main sol.78 but conflicts with its own instruction 0.5 g/L L-cysteine hydrochloride. Embedded DSM413 says 0.5 g/L cysteine without HCl; standalone 78 explicitly says L-cysteine hydrochloride. Retain this source/version conflict rather than retroactively using newer 78 to authenticate embedded 413."}, {"path": "data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.487805", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Local 0.487805 g/L L-cysteine hydrochloride matches provider Main sol.78 but conflicts with its own instruction 0.5 g/L L-cysteine hydrochloride. Embedded DSM413 says 0.5 g/L cysteine without HCl; standalone 78 explicitly says L-cysteine hydrochloride. Retain this source/version conflict rather than retroactively using newer 78 to authenticate embedded 413."}, {"path": "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.487805", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Local 0.487805 g/L L-cysteine hydrochloride matches provider Main sol.78 but conflicts with its own instruction 0.5 g/L L-cysteine hydrochloride. Embedded DSM413 says 0.5 g/L cysteine without HCl; standalone 78 explicitly says L-cysteine hydrochloride. Retain this source/version conflict rather than retroactively using newer 78 to authenticate embedded 413."}, {"path": "data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.487805", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Local 0.487805 g/L L-cysteine hydrochloride matches provider Main sol.78 but conflicts with its own instruction 0.5 g/L L-cysteine hydrochloride. Embedded DSM413 says 0.5 g/L cysteine without HCl; standalone 78 explicitly says L-cysteine hydrochloride. Retain this source/version conflict rather than retroactively using newer 78 to authenticate embedded 413. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.487805", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Local 0.487805 g/L L-cysteine hydrochloride matches provider Main sol.78 but conflicts with its own instruction 0.5 g/L L-cysteine hydrochloride. Embedded DSM413 says 0.5 g/L cysteine without HCl; standalone 78 explicitly says L-cysteine hydrochloride. Retain this source/version conflict rather than retroactively using newer 78 to authenticate embedded 413. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml", "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.487805", "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Local 0.487805 g/L L-cysteine hydrochloride matches provider Main sol.78 but conflicts with its own instruction 0.5 g/L L-cysteine hydrochloride. Embedded DSM413 says 0.5 g/L cysteine without HCl; standalone 78 explicitly says L-cysteine hydrochloride. Retain this source/version conflict rather than retroactively using newer 78 to authenticate embedded 413. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}]}, {"quantity_id": "q10", "topic": "Conditional agar", "source": {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256": "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator": "$.data.solutions[2].recipe[8]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"}, "decision": "correct", "rationale": "Provider 14.6341 g/L belongs to its 1025 mL object and is conditional for solid medium. Primary source explicitly gives 15 g agar per 1000 mL medium for slants. Preserve that conditional 15 g/L basis, not unconditional solid growth for all variants.", "layer_assessments": [{"path": "data/merge_yaml/merged/BTU_MEDIUM.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "14.6341", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Provider 14.6341 g/L belongs to its 1025 mL object and is conditional for solid medium. Primary source explicitly gives 15 g agar per 1000 mL medium for slants. Preserve that conditional 15 g/L basis, not unconditional solid growth for all variants."}, {"path": "data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "14.6341", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Provider 14.6341 g/L belongs to its 1025 mL object and is conditional for solid medium. Primary source explicitly gives 15 g agar per 1000 mL medium for slants. Preserve that conditional 15 g/L basis, not unconditional solid growth for all variants."}, {"path": "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "14.6341", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Provider 14.6341 g/L belongs to its 1025 mL object and is conditional for solid medium. Primary source explicitly gives 15 g agar per 1000 mL medium for slants. Preserve that conditional 15 g/L basis, not unconditional solid growth for all variants."}, {"path": "data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "14.6341", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Provider 14.6341 g/L belongs to its 1025 mL object and is conditional for solid medium. Primary source explicitly gives 15 g agar per 1000 mL medium for slants. Preserve that conditional 15 g/L basis, not unconditional solid growth for all variants. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "14.6341", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Provider 14.6341 g/L belongs to its 1025 mL object and is conditional for solid medium. Primary source explicitly gives 15 g agar per 1000 mL medium for slants. Preserve that conditional 15 g/L basis, not unconditional solid growth for all variants. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml", "field_path": "ingredients[9].concentration", "stored_value": {"value": "14.6341", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Provider 14.6341 g/L belongs to its 1025 mL object and is conditional for solid medium. Primary source explicitly gives 15 g agar per 1000 mL medium for slants. Preserve that conditional 15 g/L basis, not unconditional solid growth for all variants. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}]}, {"quantity_id": "q11", "topic": "Hemin stock", "source": {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256": "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator": "$.data.solutions[3].recipe[0]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"}, "decision": "correct", "rationale": "Local 0.5 g/L is numerically supported as 50 mg made up to 100 mL in the hemin stock. It is not the receiving-medium concentration. The stock is a conditional 10 mL addition per 1000 mL basal medium.", "layer_assessments": [{"path": "data/merge_yaml/merged/BTU_MEDIUM.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 0.5 g/L is numerically supported as 50 mg made up to 100 mL in the hemin stock. It is not the receiving-medium concentration. The stock is a conditional 10 mL addition per 1000 mL basal medium."}, {"path": "data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 0.5 g/L is numerically supported as 50 mg made up to 100 mL in the hemin stock. It is not the receiving-medium concentration. The stock is a conditional 10 mL addition per 1000 mL basal medium."}, {"path": "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 0.5 g/L is numerically supported as 50 mg made up to 100 mL in the hemin stock. It is not the receiving-medium concentration. The stock is a conditional 10 mL addition per 1000 mL basal medium."}, {"path": "data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 0.5 g/L is numerically supported as 50 mg made up to 100 mL in the hemin stock. It is not the receiving-medium concentration. The stock is a conditional 10 mL addition per 1000 mL basal medium. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 0.5 g/L is numerically supported as 50 mg made up to 100 mL in the hemin stock. It is not the receiving-medium concentration. The stock is a conditional 10 mL addition per 1000 mL basal medium. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml", "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 0.5 g/L is numerically supported as 50 mg made up to 100 mL in the hemin stock. It is not the receiving-medium concentration. The stock is a conditional 10 mL addition per 1000 mL basal medium. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}]}, {"quantity_id": "q12", "topic": "Vitamin K3 stock/version", "source": {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256": "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator": "$.data.solutions[4].recipe[0]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"}, "decision": "correct", "rationale": "Local 0.05 g/L equals 0.05 mg/mL, the diluted stock strength in standalone 78 and the current provider. Credit that exact numerical equality. Embedded DSM413 instead specifies 5 mg/mL K3 in 10 mL95%ethanol. Neither stock strength is a universal final-medium concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/BTU_MEDIUM.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 0.05 g/L equals 0.05 mg/mL, the diluted stock strength in standalone 78 and the current provider. Credit that exact numerical equality. Embedded DSM413 instead specifies 5 mg/mL K3 in 10 mL95%ethanol. Neither stock strength is a universal final-medium concentration."}, {"path": "data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 0.05 g/L equals 0.05 mg/mL, the diluted stock strength in standalone 78 and the current provider. Credit that exact numerical equality. Embedded DSM413 instead specifies 5 mg/mL K3 in 10 mL95%ethanol. Neither stock strength is a universal final-medium concentration."}, {"path": "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 0.05 g/L equals 0.05 mg/mL, the diluted stock strength in standalone 78 and the current provider. Credit that exact numerical equality. Embedded DSM413 instead specifies 5 mg/mL K3 in 10 mL95%ethanol. Neither stock strength is a universal final-medium concentration."}, {"path": "data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 0.05 g/L equals 0.05 mg/mL, the diluted stock strength in standalone 78 and the current provider. Credit that exact numerical equality. Embedded DSM413 instead specifies 5 mg/mL K3 in 10 mL95%ethanol. Neither stock strength is a universal final-medium concentration. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 0.05 g/L equals 0.05 mg/mL, the diluted stock strength in standalone 78 and the current provider. Credit that exact numerical equality. Embedded DSM413 instead specifies 5 mg/mL K3 in 10 mL95%ethanol. Neither stock strength is a universal final-medium concentration. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml", "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 0.05 g/L equals 0.05 mg/mL, the diluted stock strength in standalone 78 and the current provider. Credit that exact numerical equality. Embedded DSM413 instead specifies 5 mg/mL K3 in 10 mL95%ethanol. Neither stock strength is a universal final-medium concentration. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}]}, {"quantity_id": "q13", "topic": "Ethanol stock solvent", "source": {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256": "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator": "$.data.solutions[5].recipe[1]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"}, "decision": "correct", "rationale": "Local 959.5 g/L combines provider 9.5 and 950 values from different K3/K1 stocks. The primary sources describe 95%ethanol solution volumes, without an explicit percentage basis here. Keep source-specific stock solvents and exclude an unsupported mass sum.", "layer_assessments": [{"path": "data/merge_yaml/merged/BTU_MEDIUM.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "959.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 959.5 g/L combines provider 9.5 and 950 values from different K3/K1 stocks. The primary sources describe 95%ethanol solution volumes, without an explicit percentage basis here. Keep source-specific stock solvents and exclude an unsupported mass sum."}, {"path": "data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "959.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 959.5 g/L combines provider 9.5 and 950 values from different K3/K1 stocks. The primary sources describe 95%ethanol solution volumes, without an explicit percentage basis here. Keep source-specific stock solvents and exclude an unsupported mass sum."}, {"path": "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "959.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 959.5 g/L combines provider 9.5 and 950 values from different K3/K1 stocks. The primary sources describe 95%ethanol solution volumes, without an explicit percentage basis here. Keep source-specific stock solvents and exclude an unsupported mass sum."}, {"path": "data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "959.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 959.5 g/L combines provider 9.5 and 950 values from different K3/K1 stocks. The primary sources describe 95%ethanol solution volumes, without an explicit percentage basis here. Keep source-specific stock solvents and exclude an unsupported mass sum. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "959.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 959.5 g/L combines provider 9.5 and 950 values from different K3/K1 stocks. The primary sources describe 95%ethanol solution volumes, without an explicit percentage basis here. Keep source-specific stock solvents and exclude an unsupported mass sum. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml", "field_path": "ingredients[12].concentration", "stored_value": {"value": "959.5", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 959.5 g/L combines provider 9.5 and 950 values from different K3/K1 stocks. The primary sources describe 95%ethanol solution volumes, without an explicit percentage basis here. Keep source-specific stock solvents and exclude an unsupported mass sum. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}]}, {"quantity_id": "q14", "topic": "Vitamin K1 liquid amount", "source": {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256": "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator": "$.data.solutions[5].recipe[0]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"}, "decision": "correct", "rationale": "Primary and provider specify 0.1 mL vitamin K1 in 20 mL95%ethanol. Local 0.1 G_PER_L treats a volume as a mass rate without density or a receiving-medium basis. Embedded 413 K1/K3 wording remains a literal source anomaly, not silently repaired.", "layer_assessments": [{"path": "data/merge_yaml/merged/BTU_MEDIUM.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Primary and provider specify 0.1 mL vitamin K1 in 20 mL95%ethanol. Local 0.1 G_PER_L treats a volume as a mass rate without density or a receiving-medium basis. Embedded 413 K1/K3 wording remains a literal source anomaly, not silently repaired."}, {"path": "data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Primary and provider specify 0.1 mL vitamin K1 in 20 mL95%ethanol. Local 0.1 G_PER_L treats a volume as a mass rate without density or a receiving-medium basis. Embedded 413 K1/K3 wording remains a literal source anomaly, not silently repaired."}, {"path": "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Primary and provider specify 0.1 mL vitamin K1 in 20 mL95%ethanol. Local 0.1 G_PER_L treats a volume as a mass rate without density or a receiving-medium basis. Embedded 413 K1/K3 wording remains a literal source anomaly, not silently repaired."}, {"path": "data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Primary and provider specify 0.1 mL vitamin K1 in 20 mL95%ethanol. Local 0.1 G_PER_L treats a volume as a mass rate without density or a receiving-medium basis. Embedded 413 K1/K3 wording remains a literal source anomaly, not silently repaired. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Primary and provider specify 0.1 mL vitamin K1 in 20 mL95%ethanol. Local 0.1 G_PER_L treats a volume as a mass rate without density or a receiving-medium basis. Embedded 413 K1/K3 wording remains a literal source anomaly, not silently repaired. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml", "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.1", "unit": "G_PER_L"}, "decision": "correct", "rationale": "Primary and provider specify 0.1 mL vitamin K1 in 20 mL95%ethanol. Local 0.1 G_PER_L treats a volume as a mass rate without density or a receiving-medium basis. Embedded 413 K1/K3 wording remains a literal source anomaly, not silently repaired. Exact KOMODO variant access failed; current copied numbers do not authorize importing the generic DSM recipe as this variant."}]}, {"quantity_id": "q15", "topic": "pH 7 and source scope", "source": {"evidence_id": "dsm413", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium413.pdf", "raw_path": "REVIEW_WORK/batch054/source01-03/dsm413.bin", "raw_sha256": "2dc547e81e376a04e46659d3d0b800d9c9ec5dbedd1abe9ffcaaa59d9bfbd27f", "locator": "Page1 embedded78 preparation", "accessed_at": "2026-10-28T03:59:21.850645+00:00", "quote": "pH to 7.0."}, "decision": "mixed", "rationale": "The standalone 78 DSM21650 pH 8.5 exception is excluded from BTU and its unverified strain variants.", "layer_assessments": [{"path": "data/merge_yaml/merged/BTU_MEDIUM.yaml", "field_path": "ph_value", "stored_value": 7.0, "decision": "evidence_only", "rationale": "Retain pH 7 correspondence to the generic primary and current provider."}, {"path": "data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml", "field_path": "ph_value", "stored_value": 7.0, "decision": "evidence_only", "rationale": "Retain pH 7 correspondence to the generic primary and current provider."}, {"path": "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path": "ph_value", "stored_value": 7.0, "decision": "evidence_only", "rationale": "Retain pH 7 correspondence to the generic primary and current provider."}, {"path": "data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml", "field_path": "ph_value", "stored_value": 7.0, "decision": "unsupported", "rationale": "DSM413 supports pH 7 for the generic formulation; exact inaccessible variants are not thereby authenticated."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml", "field_path": "ph_value", "stored_value": 7.0, "decision": "unsupported", "rationale": "DSM413 supports pH 7 for the generic formulation; exact inaccessible variants are not thereby authenticated."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml", "field_path": "ph_value", "stored_value": 7.0, "decision": "unsupported", "rationale": "DSM413 supports pH 7 for the generic formulation; exact inaccessible variants are not thereby authenticated."}]}, {"quantity_id": "q16", "topic": "Existing DSM preparation step 1", "source": {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256": "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator": "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"}, "decision": "evidence_only", "rationale": "Existing DSM owner already preserves 30µL/mL addition before inoculation; equivalent provider assembly row is 30 mL stock with 1000 mL basal medium. Preserve dose versus total-volume distinction.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path": "preparation_steps[0].description", "stored_value": "Add 30 µl Formiate/Fumarate Solution per ml of medium 78 before inoculation.", "decision": "evidence_only", "rationale": "Existing DSM owner already preserves 30µL/mL addition before inoculation; equivalent provider assembly row is 30 mL stock with 1000 mL basal medium. Preserve dose versus total-volume distinction."}]}, {"quantity_id": "q17", "topic": "Existing DSM preparation step 2", "source": {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256": "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator": "$.data.solutions[1].steps[0]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"}, "decision": "evidence_only", "rationale": "Existing filter-sterilization instruction belongs to the Formiate/Fumarate stock.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path": "preparation_steps[1].description", "stored_value": "Filter sterilize.", "decision": "evidence_only", "rationale": "Existing filter-sterilization instruction belongs to the Formiate/Fumarate stock."}]}, {"quantity_id": "q18", "topic": "Existing DSM preparation step 3", "source": {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256": "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator": "$.data.solutions[2].steps[0]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"}, "decision": "evidence_only", "rationale": "Existing prose retains 100% N2, 0.5 g/L L-cysteine hydrochloride, pH 7, 7 mL, tube meat:fluid 1:4 or 5, 121°C/30 min and conditional 15 g/1000 mL agar. These match current provider/standalone 78 context; embedded 413 cysteine form differs. Do not delete supported existing prose or call it missing.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path": "preparation_steps[2].description", "stored_value": "To make medium anoxic bring it to a boil, cool under 100% N2 gas atmosphere, add 0.5 g/l L-cysteine hydrochloride and adjust pH to 7.0. Dispense under 100% N2 gas atmosphere by filling 7 ml medium into anoxic Hungate-type tubes (for strains demanding meat particles put those first into the tube (use 1 part meat particles to 4 or 5 parts fluid)). Autoclave at 121°C for 30 min. For agar slants use 15.0 g agar per 1000.0 ml medium.", "decision": "evidence_only", "rationale": "Existing prose retains 100% N2, 0.5 g/L L-cysteine hydrochloride, pH 7, 7 mL, tube meat:fluid 1:4 or 5, 121°C/30 min and conditional 15 g/1000 mL agar. These match current provider/standalone 78 context; embedded 413 cysteine form differs. Do not delete supported existing prose or call it missing."}]}, {"quantity_id": "q19", "topic": "Existing DSM preparation step 4", "source": {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256": "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator": "$.data.solutions[2].steps[1]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"}, "decision": "evidence_only", "rationale": "Existing conditional post-autoclave supplement instruction names 1000 mL medium but omits actual supplement doses. Preserve it; structured, version-qualified doses remain to be added.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path": "preparation_steps[3].description", "stored_value": "In some cases (as indicated in the catalogue) the addition of Haemin and Vitamin K1 or Vitamin K3 is necessary. Add to 1000 ml of medium after autoclaving:", "decision": "evidence_only", "rationale": "Existing conditional post-autoclave supplement instruction names 1000 mL medium but omits actual supplement doses. Preserve it; structured, version-qualified doses remain to be added."}]}, {"quantity_id": "q20", "topic": "Existing DSM preparation step 5", "source": {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256": "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator": "$.data.solutions[2].steps[2]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"}, "decision": "evidence_only", "rationale": "Existing extraction prose already retains 15 min boiling, separate retained meat/filtrate and explicit final 1000 mL filtrate makeup. This is an intermediate stage, not measured final BTU volume.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path": "preparation_steps[4].description", "stored_value": "Use lean beef or horse meat. Remove fat and connective tissue before grinding. Mix\r\nmeat, water and NaOH, then boil for 15 min with stirring. Cool to room temperature,\r\nskim fat off surface, and filter, retaining both meat particles and filtrate. To the filtrate\r\nadd water to a final volume of 1000 ml, and then add:", "decision": "evidence_only", "rationale": "Existing extraction prose already retains 15 min boiling, separate retained meat/filtrate and explicit final 1000 mL filtrate makeup. This is an intermediate stage, not measured final BTU volume."}]}, {"quantity_id": "q21", "topic": "Existing DSM preparation step 6", "source": {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256": "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator": "$.data.solutions[3].steps[0]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"}, "decision": "evidence_only", "rationale": "Existing hemin preparation already retains 50 mg,1 mL1N NaOH and makeup 100 mL; this supports stock 0.5 g/L only.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path": "preparation_steps[5].description", "stored_value": "Dissolve 50 mg haemin in 1 ml 1 N NaOH; make up to 100 ml with distilled water and filter sterilize. Store refrigerated.", "decision": "evidence_only", "rationale": "Existing hemin preparation already retains 50 mg,1 mL1N NaOH and makeup 100 mL; this supports stock 0.5 g/L only."}]}, {"quantity_id": "q22", "topic": "Existing DSM preparation step 7", "source": {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256": "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator": "$.data.solutions[4].steps[0]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"}, "decision": "evidence_only", "rationale": "Existing K3 prose exactly matches current provider 5 mg in 1 mL95%ethanol diluted 0.05 mg/mL. Preserve current provider attribution; embedded 413 differs and standalone 78 states initial 5 mg/mL rather than a required 1 mL batch.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path": "preparation_steps[6].description", "stored_value": "Dissolve 5 mg vitamin K3 in 1 ml 95% ethanol, dilute to 0.05 mg/ml in water and filter sterilize. Store refrigerated in a brown bottle.", "decision": "evidence_only", "rationale": "Existing K3 prose exactly matches current provider 5 mg in 1 mL95%ethanol diluted 0.05 mg/mL. Preserve current provider attribution; embedded 413 differs and standalone 78 states initial 5 mg/mL rather than a required 1 mL batch."}]}, {"quantity_id": "q23", "topic": "Existing DSM preparation step 8", "source": {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256": "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator": "$.data.solutions[5].steps[0]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"}, "decision": "evidence_only", "rationale": "Existing K1 prose has 0.1 mL in 20 mL95%ethanol and matches provider/standalone 78. Embedded 413 literally labels K1/K3, retained as an unresolved source anomaly.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path": "preparation_steps[7].description", "stored_value": "Dissolve 0.1 ml of vitamin K1 in 20 ml 95% ethanol and filter sterilize. Store refrigerated in a brown bottle.", "decision": "evidence_only", "rationale": "Existing K1 prose has 0.1 mL in 20 mL95%ethanol and matches provider/standalone 78. Embedded 413 literally labels K1/K3, retained as an unresolved source anomaly."}]}, {"quantity_id": "q24", "topic": "Basal assembly and both-salt stock", "source": {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256": "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator": "$.data.solutions[0:2]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"}, "decision": "mixed", "rationale": "Primary medium 413 adds a separately defined stock to medium 78. Current API gives 1000 mL basal and 30 mL stock; stock contains 6 g of each salt and 100 mL water with declared 100 mL volume. Do not treat provider primary volume 1000 as proof that the additive final volume is 1000 mL.", "layer_assessments": [{"path": "data/merge_yaml/merged/BTU_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale": "Generated/copy or exact KOMODO variant cannot receive this generic source topology as an authenticated variant before accession/version reconciliation. Primary medium 413 adds a separately defined stock to medium 78. Current API gives 1000 mL basal and 30 mL stock; stock contains 6 g of each salt and 100 mL water with declared 100 mL volume. Do not treat provider primary volume 1000 as proof that the additive final volume is 1000 mL.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale": "Generated/copy or exact KOMODO variant cannot receive this generic source topology as an authenticated variant before accession/version reconciliation. Primary medium 413 adds a separately defined stock to medium 78. Current API gives 1000 mL basal and 30 mL stock; stock contains 6 g of each salt and 100 mL water with declared 100 mL volume. Do not treat provider primary volume 1000 as proof that the additive final volume is 1000 mL.", "missing": true}, {"path": "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Create source/version-scoped stock topology while preserving existing preparation prose. Primary medium 413 adds a separately defined stock to medium 78. Current API gives 1000 mL basal and 30 mL stock; stock contains 6 g of each salt and 100 mL water with declared 100 mL volume. Do not treat provider primary volume 1000 as proof that the additive final volume is 1000 mL.", "missing": true}, {"path": "data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml", "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale": "Generated/copy or exact KOMODO variant cannot receive this generic source topology as an authenticated variant before accession/version reconciliation. Primary medium 413 adds a separately defined stock to medium 78. Current API gives 1000 mL basal and 30 mL stock; stock contains 6 g of each salt and 100 mL water with declared 100 mL volume. Do not treat provider primary volume 1000 as proof that the additive final volume is 1000 mL.", "missing": true}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml", "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale": "Generated/copy or exact KOMODO variant cannot receive this generic source topology as an authenticated variant before accession/version reconciliation. Primary medium 413 adds a separately defined stock to medium 78. Current API gives 1000 mL basal and 30 mL stock; stock contains 6 g of each salt and 100 mL water with declared 100 mL volume. Do not treat provider primary volume 1000 as proof that the additive final volume is 1000 mL.", "missing": true}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml", "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale": "Generated/copy or exact KOMODO variant cannot receive this generic source topology as an authenticated variant before accession/version reconciliation. Primary medium 413 adds a separately defined stock to medium 78. Current API gives 1000 mL basal and 30 mL stock; stock contains 6 g of each salt and 100 mL water with declared 100 mL volume. Do not treat provider primary volume 1000 as proof that the additive final volume is 1000 mL.", "missing": true}]}, {"quantity_id": "q25", "topic": "Hemin conditional stock and dose", "source": {"evidence_id": "dsm413", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium413.pdf", "raw_path": "REVIEW_WORK/batch054/source01-03/dsm413.bin", "raw_sha256": "2dc547e81e376a04e46659d3d0b800d9c9ec5dbedd1abe9ffcaaa59d9bfbd27f", "locator": "Page1 conditional additions and Haemin solution", "accessed_at": "2026-10-28T03:59:21.850645+00:00"}, "decision": "mixed", "rationale": "Hemin 50 mg,1 mL1NNaOH,makeup 100 mL; conditional 10 mL stock per 1000 mL medium after autoclaving. All are distinct from final hemin concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/BTU_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale": "Generated/copy or exact KOMODO variant cannot receive this generic source topology as an authenticated variant before accession/version reconciliation. Hemin 50 mg,1 mL1NNaOH,makeup 100 mL; conditional 10 mL stock per 1000 mL medium after autoclaving. All are distinct from final hemin concentration.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale": "Generated/copy or exact KOMODO variant cannot receive this generic source topology as an authenticated variant before accession/version reconciliation. Hemin 50 mg,1 mL1NNaOH,makeup 100 mL; conditional 10 mL stock per 1000 mL medium after autoclaving. All are distinct from final hemin concentration.", "missing": true}, {"path": "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Create source/version-scoped stock topology while preserving existing preparation prose. Hemin 50 mg,1 mL1NNaOH,makeup 100 mL; conditional 10 mL stock per 1000 mL medium after autoclaving. All are distinct from final hemin concentration.", "missing": true}, {"path": "data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml", "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale": "Generated/copy or exact KOMODO variant cannot receive this generic source topology as an authenticated variant before accession/version reconciliation. Hemin 50 mg,1 mL1NNaOH,makeup 100 mL; conditional 10 mL stock per 1000 mL medium after autoclaving. All are distinct from final hemin concentration.", "missing": true}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml", "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale": "Generated/copy or exact KOMODO variant cannot receive this generic source topology as an authenticated variant before accession/version reconciliation. Hemin 50 mg,1 mL1NNaOH,makeup 100 mL; conditional 10 mL stock per 1000 mL medium after autoclaving. All are distinct from final hemin concentration.", "missing": true}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml", "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale": "Generated/copy or exact KOMODO variant cannot receive this generic source topology as an authenticated variant before accession/version reconciliation. Hemin 50 mg,1 mL1NNaOH,makeup 100 mL; conditional 10 mL stock per 1000 mL medium after autoclaving. All are distinct from final hemin concentration.", "missing": true}]}, {"quantity_id": "q26", "topic": "Vitamin alternatives and incompatible doses", "source": {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256": "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator": "$.data.solutions[2].recipe[10:12], solutions[4:6]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"}, "decision": "mixed", "rationale": "Embedded DSM413 adds 0.2 mL of K1 OR K3 stock per 1000 mL. Standalone 78 adds 10 mL of either; current API separately saysK1=0.2 mL andK3=10 mL. Keep all versioned evidence and alternative status; no universal winning dose is selected.", "layer_assessments": [{"path": "data/merge_yaml/merged/BTU_MEDIUM.yaml", "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale": "Generated/copy or exact KOMODO variant cannot receive this generic source topology as an authenticated variant before accession/version reconciliation. Embedded DSM413 adds 0.2 mL of K1 OR K3 stock per 1000 mL. Standalone 78 adds 10 mL of either; current API separately saysK1=0.2 mL andK3=10 mL. Keep all versioned evidence and alternative status; no universal winning dose is selected.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale": "Generated/copy or exact KOMODO variant cannot receive this generic source topology as an authenticated variant before accession/version reconciliation. Embedded DSM413 adds 0.2 mL of K1 OR K3 stock per 1000 mL. Standalone 78 adds 10 mL of either; current API separately saysK1=0.2 mL andK3=10 mL. Keep all versioned evidence and alternative status; no universal winning dose is selected.", "missing": true}, {"path": "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path": "solutions", "stored_value": null, "decision": "add", "rationale": "Create source/version-scoped stock topology while preserving existing preparation prose. Embedded DSM413 adds 0.2 mL of K1 OR K3 stock per 1000 mL. Standalone 78 adds 10 mL of either; current API separately saysK1=0.2 mL andK3=10 mL. Keep all versioned evidence and alternative status; no universal winning dose is selected.", "missing": true}, {"path": "data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml", "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale": "Generated/copy or exact KOMODO variant cannot receive this generic source topology as an authenticated variant before accession/version reconciliation. Embedded DSM413 adds 0.2 mL of K1 OR K3 stock per 1000 mL. Standalone 78 adds 10 mL of either; current API separately saysK1=0.2 mL andK3=10 mL. Keep all versioned evidence and alternative status; no universal winning dose is selected.", "missing": true}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml", "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale": "Generated/copy or exact KOMODO variant cannot receive this generic source topology as an authenticated variant before accession/version reconciliation. Embedded DSM413 adds 0.2 mL of K1 OR K3 stock per 1000 mL. Standalone 78 adds 10 mL of either; current API separately saysK1=0.2 mL andK3=10 mL. Keep all versioned evidence and alternative status; no universal winning dose is selected.", "missing": true}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml", "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale": "Generated/copy or exact KOMODO variant cannot receive this generic source topology as an authenticated variant before accession/version reconciliation. Embedded DSM413 adds 0.2 mL of K1 OR K3 stock per 1000 mL. Standalone 78 adds 10 mL of either; current API separately saysK1=0.2 mL andK3=10 mL. Keep all versioned evidence and alternative status; no universal winning dose is selected.", "missing": true}]}, {"quantity_id": "q27", "topic": "Embedded 413 vitamin stock anomalies", "source": {"evidence_id": "dsm413", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium413.pdf", "raw_path": "REVIEW_WORK/batch054/source01-03/dsm413.bin", "raw_sha256": "2dc547e81e376a04e46659d3d0b800d9c9ec5dbedd1abe9ffcaaa59d9bfbd27f", "locator": "Page1 Vitamin K1 and Vitamin K3 subsections", "accessed_at": "2026-10-28T03:59:21.850645+00:00"}, "decision": "unsupported", "rationale": "Literal K1 subsection names 0.1 mL K1/K3 in 20 mL95%ethanol. Literal K3 subsection specifies 5 mg/mL in 10 mL95%ethanol. These differ from current provider diluted K3 and do not establish a universal receiving-medium dose. No percentage basis or density is invented.", "layer_assessments": []}, {"quantity_id": "q28", "topic": "Standalone 78 strain-specific exclusion", "source": {"evidence_id": "dsm78", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf", "raw_path": "REVIEW_WORK/batch054/source01-03/dsm78.bin", "raw_sha256": "4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0", "locator": "Final DSM21650 exception", "accessed_at": "2026-10-28T03:59:21.867329+00:00"}, "decision": "evidence_only", "rationale": "pH 8.5 is stated only for DSM21650 in standalone 78; this is excluded context and not transferred to the selected BTU formulation or DSM20703/6644 variants.", "layer_assessments": []}]

### Current ontology and MIM correspondence

grounding: supported. Targets: CultureMech:005240.

The grounding inventory enumerates every asserted identifier and exact preferred label. Current catalog joins establish present correspondence only; unmapped mixtures are not assigned invented chemical identities.

### History and evidence scope

provenance: supported. Targets: CultureMech:005240.

Complete owner and target histories were read. Current source bytes and inspected code are independent evidence; historical timestamps remain historical claims unless an exact cited raw digest is recovered.

### Growth and taxonomic evidence

scope: unknown. Targets: CultureMech:005240.

Generic cultivation applications and bacterial filing are not strain-level growth evidence. No organism-specific growth, temperature or atmosphere is inferred from names or source catalog identifiers.

### Canonical diagnostics

schema: supported. Targets: CultureMech:005240.

All four original canonical diagnostics passed. Reference checks were zero; structural and term diagnostics do not establish formulation accuracy.

## Findings

### f1: Stock compositions and final-medium quantities are flattened

major / open / confirmed; issue key: culturemech-005240-stock-compositions-and-final-medium-quantities-are-flattened.

All six local records contain the same fourteen direct concentrations, combining basal precursor amounts, two 60 g/L stock salts,0.5 g/L hemin stock and 0.05 g/L diluted K3 stock. No solutions topology is present. Current API/primary evidence separates these stages; current importer already implements stock separation.

### f2: Liquid units and incompatible stock values were combined

major / open / confirmed; issue key: culturemech-005240-liquid-units-and-incompatible-stock-values-were-combined.

NaOH26 G_PER_L comes from 25 mL and 1 mL1N solution inputs at different stages. Ethanol 959.5 G_PER_L combines 9.5 and 950 provider values from two stocks; K1 0.1 G_PER_L uses a source 0.1 mL amount as a mass rate. Numeric equality to provider fields does not repair these dimensions or stage joins.

### f3: Basal denominator and conditional solids need source reconciliation

major / open / confirmed; issue key: culturemech-005240-basal-denominator-and-conditional-solids-need-source-reconciliation.

Primary 413 uses 500 g beef as an extraction precursor and makes filtrate up to 1000 mL before adding 30 g Casitone,5 g yeast extract,5 g phosphate and 1 mg resazurin. Provider 1025 mL rates match local digits but are not an independently authenticated final BTU basis. Primary agar is explicitly 15 g per 1000 mL for slants; local 14.6341 derives from the other denominator.

### f4: Embedded 413 and standalone 78 vitamin/cysteine versions conflict

major / open / confirmed; issue key: culturemech-005240-embedded413-and-standalone78-vitamin-cysteine-versions-conflict.

Embedded 413 says 0.5 g/L cysteine and 0.2 mL of either vitamin stock. Standalone 78 names L-cysteine hydrochloride and 10 mL of either vitamin; current API combines K1 0.2 mL withK3 10 mL and a diluted K3 stock. Local 0.05 g/L equals the newer 0.05 mg/mL stock, but is not universal final concentration. Embedded K1/K3 wording and 5 mg/mL K3 in 10 mL ethanol are literal anomalies.

### f5: Copied signatures do not authenticate named KOMODO variants

major / open / confirmed; issue key: culturemech-005240-copied-signatures-do-not-authenticate-named-komodo-variants.

The merged record includes a named formate-to-fumarate replacement and DSM20703/6644 modified media. Histories say DSM413 ingredients were copied into them, and identical local signatures underpin duplicate links. Exact variant endpoints returned 403. DSM413 both-salt formulation cannot establish a replacement variant or strain-specific growth.

### f6: Legacy cysteine identifier lacks a current catalog row

minor / open / confirmed; issue key: culturemech-005240-legacy-cysteine-identifier-lacks-a-current-catalog-row.

The asserted MediaIngredientMech:000223 is absent from the current packaged label index. CHEBI:91247 currently denotes L-cysteine hydrochloride, but that does not resolve the embedded 413 form ambiguity or establish historical invalidity of the legacy identifier.

### f7: Malformed import timestamps and stale generated preparation obscure provenance

minor / open / confirmed; issue key: culturemech-005240-malformed-import-timestamps-and-stale-generated-preparation-obscure-provenance.

KOMODO import history retains an .fZ timestamp. The maintained DSM owner already carries eight preparation steps, while generated/other contributors do not. Preserve that existing work and qualify its version; absence from generated output is not evidence that no owner preparation was ever curated.

## Recommended Actions And Acceptance Checks

### action1

Curate explicit stock/assembly topology in the DSM owner with source version and conditional doses retained. Reconcile exact KOMODO variants before transferring any recipe. Regenerate compatible outputs and retain current importer guards; do not patch generated YAML directly.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action2

Restore separate liquid input dimensions and stock scopes from exact source records. Preserve old summed values as history; do not sum across stock denominators or invent ethanol density/percentage basis.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action3

Preserve precursor, filtrate makeup and subsequent batch additions separately. Resolve the provider/primary denominator conflict and conditional agar stage before assigning final-medium rates or universal physical-state claims.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action4

Represent or explicitly document the exact source versions without choosing the convenient dose/form. Keep existing DSM preparation prose and attach versioned source support; resolve missing structured dose alternatives separately.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action5

Keep exact source accessions and existing history, but qualify or defer source-duplicate claims until each variant is authenticated. Do not collapse variants solely because copied local signatures match.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action6

Document the current legacy-link limit and reconcile source form first. Do not guess a replacement MIM identifier or claim the historical identifier never existed.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

### action7

Preserve original history with a valid-time provenance qualification and regenerate only after source/version reconciliation. Retain the DSM owner preparation rather than redundantly adding it as entirely missing.

- Exact owner/source scopes and all quantity decisions are reconciled.
- Regenerated target retains claim-level evidence and passes the four canonical diagnostics.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| local-target | data/merge_yaml/merged/BTU_MEDIUM.yaml; Complete document | context_only | Complete selected generated record; no changes made. |
| owner-1 | data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| owner-2 | data/normalized_yaml/bacterial/btu_medium.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| owner-3 | data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| owner-4 | data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| owner-5 | data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml; Complete document | context_only | Complete maintained contributor including current curation history, evidence, quantities and preparation; no changes made. |
| dsm413 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium413.pdf; Exact source identity and scoped formulation/preparation | supports | Exact two-page BTU primary PDF, visually inspected: BOTH6 g sodium salts in a 100 mL-water stock; explicit 30µL/mL addition. Embedded 78 recipe and conditional vitamin details are version-specific. |
| dsm78 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf; Exact source identity and scoped formulation/preparation | context_only | Standalone 78 primary PDF is a distinct version: L-cysteine hydrochloride,10 mL vitamin addition and K3 dilution to 0.05 mg/mL. Not silently substituted for embedded 413. |
| api413 | https://mediadive.dsmz.de/rest/medium/413; Exact source identity and scoped formulation/preparation | supports | Exact current provider medium 413 with six nested solutions. Stored g_l values correspond to particular basal/stock objects; they are not all final BTU rates. Provider vitamin variant is retained separately. |
| komodo413 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=413; Exact source identity and scoped formulation/preparation | unknown | Exact KOMODO413 source returned 403; source-specific content unavailable. |
| komodo413fumarate | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=413_replace_Formiate_with_Fumarate; Exact source identity and scoped formulation/preparation | unknown | Exact replacement-variant endpoint returned 403; do not infer replacement amounts from its name or transfer both-salt DSM recipe as verified variant. |
| komodo41320703 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=413_20703; Exact source identity and scoped formulation/preparation | unknown | Exact strain-variant endpoint returned 403; no strain-specific recipe/growth conditions verified. |
| komodo4136644 | https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=413_6644; Exact source identity and scoped formulation/preparation | unknown | Exact strain-variant endpoint returned 403; no strain-specific recipe/growth conditions verified. |
| provider-stage-census | REVIEW_WORK/batch054/record03/provider-stage-census.json | context_only | Every provider solution volume and recipe row, including amount/unit/g_l/mmol_l/optional/condition. Identifiers and derived rates remain in their exact source stage. |
| dsm413-visual-1 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium413.pdf; PDF page1; render REVIEW_WORK/batch054/record03/dsm413-page-1.png | supports | Visual inspection confirms table/preparation text, including both salts and the printed vitamin anomalies; source PDF raw hash is separately pinned. |
| dsm413-visual-2 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium413.pdf; PDF page2; render REVIEW_WORK/batch054/record03/dsm413-page-2.png | supports | Visual inspection confirms table/preparation text, including both salts and the printed vitamin anomalies; source PDF raw hash is separately pinned. |
| writer-mediadive | src/culturemech/import/mediadive_importer.py; _parse_api_composition/_parse_api_solutions | context_only | Current _parse_api_composition reads only the primary solution, skips stock additions and pure-water edges; _parse_api_solutions preserves referenced stocks separately. Existing guards are credited; no claim of current flattening causality. |
| writer-cleanup | scripts/cleanup_recipe_ingredients.py; merge_ingredient_group | context_only | Current merge_ingredient_group keeps the first concentration and flags differing values; it does not sum the old NaOH or ethanol numbers. Historical summed notes are not proof that this current code produced them. |
| writer-merge | src/culturemech/merge/merger.py; merge_group | context_only | Current merge_group passes multiple inputs to merge_formulation_evidence. It does not authenticate source variants from copied matching ingredient sets. |
| writer-formulation | src/culturemech/merge/formulation.py; merge_formulation_evidence | context_only | Current compatibility guard requires equal formulation content before evidence union; ingredient-only similarity is insufficient. |
| chebi62965 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_62965; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi115156 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_115156; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32145; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi131527 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_131527; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_8806; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi91247 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_91247; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi2509 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_2509; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi50385 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_50385; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi28869 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_28869; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi16236 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_16236; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| chebi18067 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_18067; _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms | supports | Exact OLS term object: accession, current preferred label, obsolete flag, definition and synonyms. Supports identifier correspondence only, not recipe amounts or growth. |
| quantities | REVIEW_WORK/batch054/record03/quantity-inventory.json | context_only | Complete local concentration and source-stage decision inventory; includes exact local paths and source failure limits. |
| grounding | REVIEW_WORK/batch054/record03/grounding-inventory.json | context_only | All recursive asserted identifier/label slots, exact current OLS objects and current packaged MIM preferred-row joins. |
| history | REVIEW_WORK/batch054/record03/history-and-evidence-inventory.json | context_only | Complete current history, references and attached evidence; source-specific claims are assessed without authenticating historical execution from code. |
| scalars | REVIEW_WORK/batch054/record03/scalar-census.json | context_only | Lossless scalar census of the selected target and all maintained contributors. |
| validate-schema | REVIEW_WORK/batch054/record03/validate-schema.json | supports | Validating schema structure (MediaRecipe)...<br>No issues found<br>✓ Schema validation passed<br> |
| validate-strict | REVIEW_WORK/batch054/record03/validate-strict.json | supports | Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  layers:             schema<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                REVIEW_WORK/batch054/record03/strict.tsv<br> |
| validate-terms | REVIEW_WORK/batch054/record03/validate-terms.json | supports | Validating ontology terms (MediaRecipe)...<br>✅ Validation passed<br>✓ Term validation passed<br> |
| validate-references | REVIEW_WORK/batch054/record03/validate-references.json | supports | Validating evidence references (MediaRecipe)...<br>Reference checks: 0; issues: 0<br>✓ Reference validation passed<br> |

## Limits And Additional Notes

- All four exact KOMODO endpoints returned HTTP403. Generic DSM evidence does not authenticate the replacement or strain-specific variants.
- Current provider values are directly verified, but they conflict with primary source stage/volume statements. No final BTU rate is guessed where the source basis is unresolved.
- No taxonomy or strain growth claim is inferred from DSM accessions, generic applications, anaerobic notes or conditional source instructions.
- Current code inspection establishes existing safeguards only; it does not reconstruct which historical code executed. Current MIM absence is not proof of historical identifier invalidity.
- Fresh review; historical lost snapshots were not reconstructed. All inspected source files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this author.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261028T042056Z-batch054-record03-source-review
kind: record
repository: CultureBotAI/CultureMech
title: 'BTU medium: flattened stock stages and conflicting source versions'
started_at: '2026-10-28T03:58:39.394929Z'
finished_at: '2026-10-28T04:20:56.855805Z'
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
summary: The selected BTU merge and five contributors flatten basal ingredients, separate
  stocks, optional supplements and solvent amounts into one ingredient list. Current
  provider objects explain many stored numbers but do not support their use as universal
  receiving-medium concentrations. Embedded DSM413, standalone DSM78 and current provider
  records conflict in cysteine form and vitamin details; exact KOMODO variants remain
  inaccessible. Existing DSM preparation and current stock-separation/no-summing guards
  are credited.
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
  - path: data/merge_yaml/merged/BTU_MEDIUM.yaml
    sha256: 4bd8d47d4103963ccd00a106f5d74135724e7f9f5f57f0ea61b30675f090501a
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml
    sha256: 799900ae76c67b8e7b532c909574ee417226adde20123cd0ee0b25d675c46c60
    role: context
  - path: data/normalized_yaml/bacterial/btu_medium.yaml
    sha256: 3ea204ca831d4ba617bed08a653c7cd3278d10ce664671a6d0f3ab8115f53e21
    role: context
  - path: data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml
    sha256: 3a7fd1b962295b82b0b03b4a7e5ed6f1b41733d07c3f3468796a36f4c933e39a
    role: context
  - path: data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml
    sha256: 95ed0cd6878a589ddfaa134fb25c34a4815654e400a1c7cfc7a539745486addf
    role: context
  - path: data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml
    sha256: cbac7b1c4d82a76dd5508a1cb2ea4d7e70c247e8429530fee6fe805eaf734172
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
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/cleanup_recipe_ingredients.py
    sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: scripts/record_target_class.py
    sha256: 468fcbfd2362ca08b7066d6f21adf85c04f21ab40f80e60995522b4edc0f6349
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
  - path: src/culturemech/import/komodo_web_importer.py
    sha256: d99f08918b45eb7ecf9fcd871d6686153c97be5f5fb5da435d67c1c5fadee106
    role: context
  - path: src/culturemech/import/mediadive_importer.py
    sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
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
  description: Full selected record and exact maintained contributors; external source
    limits explicitly retained.
  selection: Actual batch054 native selection index 03.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:005240
targets:
- target_id: CultureMech:005240
  path: data/merge_yaml/merged/BTU_MEDIUM.yaml
  label: btu_medium
  kind: generated
  record_class: MediaRecipe
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/btu_medium.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml
    role: maintained normalized contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml
    role: maintained normalized contributor
checks:
- check_id: validate-schema
  name: validate-schema
  status: passed
  required: true
  summary: Original once-only canonical command exited 0; full stdout/stderr retained
    and read.
  target_ids:
  - CultureMech:005240
  command: just validate-schema data/merge_yaml/merged/BTU_MEDIUM.yaml
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
  - CultureMech:005240
  command: just validate-strict data/merge_yaml/merged/BTU_MEDIUM.yaml --out REVIEW_WORK/batch054/record03/strict.tsv
    --workers 1
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
  - CultureMech:005240
  command: just validate-terms data/merge_yaml/merged/BTU_MEDIUM.yaml
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
  - CultureMech:005240
  command: just validate-references data/merge_yaml/merged/BTU_MEDIUM.yaml
  exit_code: 0
  evidence_ids:
  - validate-references
  scope_note: Exact selected target; scientific source and owner assessments are separate.
evidence:
- evidence_id: local-target
  kind: record_content
  reference: data/merge_yaml/merged/BTU_MEDIUM.yaml
  locator: Complete document
  accessed_at: '2026-10-28T04:14:07.731744Z'
  support: context_only
  summary: Complete selected generated record; no changes made.
  snapshot_sha256: 4bd8d47d4103963ccd00a106f5d74135724e7f9f5f57f0ea61b30675f090501a
- evidence_id: owner-1
  kind: record_content
  reference: data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml
  locator: Complete document
  accessed_at: '2026-10-28T04:14:07.731744Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: 799900ae76c67b8e7b532c909574ee417226adde20123cd0ee0b25d675c46c60
- evidence_id: owner-2
  kind: record_content
  reference: data/normalized_yaml/bacterial/btu_medium.yaml
  locator: Complete document
  accessed_at: '2026-10-28T04:14:07.731744Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: 3ea204ca831d4ba617bed08a653c7cd3278d10ce664671a6d0f3ab8115f53e21
- evidence_id: owner-3
  kind: record_content
  reference: data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml
  locator: Complete document
  accessed_at: '2026-10-28T04:14:07.731744Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: 3a7fd1b962295b82b0b03b4a7e5ed6f1b41733d07c3f3468796a36f4c933e39a
- evidence_id: owner-4
  kind: record_content
  reference: data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml
  locator: Complete document
  accessed_at: '2026-10-28T04:14:07.731744Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: 95ed0cd6878a589ddfaa134fb25c34a4815654e400a1c7cfc7a539745486addf
- evidence_id: owner-5
  kind: record_content
  reference: data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml
  locator: Complete document
  accessed_at: '2026-10-28T04:14:07.731744Z'
  support: context_only
  summary: Complete maintained contributor including current curation history, evidence,
    quantities and preparation; no changes made.
  snapshot_sha256: cbac7b1c4d82a76dd5508a1cb2ea4d7e70c247e8429530fee6fe805eaf734172
- evidence_id: dsm413
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium413.pdf
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T03:59:21.850645Z'
  support: supports
  summary: 'Exact two-page BTU primary PDF, visually inspected: BOTH6 g sodium salts
    in a 100 mL-water stock; explicit 30µL/mL addition. Embedded 78 recipe and conditional
    vitamin details are version-specific.'
  snapshot_sha256: 2dc547e81e376a04e46659d3d0b800d9c9ec5dbedd1abe9ffcaaa59d9bfbd27f
- evidence_id: dsm78
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T03:59:21.867329Z'
  support: context_only
  summary: 'Standalone 78 primary PDF is a distinct version: L-cysteine hydrochloride,10
    mL vitamin addition and K3 dilution to 0.05 mg/mL. Not silently substituted for
    embedded 413.'
  snapshot_sha256: 4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0
- evidence_id: api413
  kind: database
  reference: https://mediadive.dsmz.de/rest/medium/413
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T04:02:49.107482Z'
  support: supports
  summary: Exact current provider medium 413 with six nested solutions. Stored g_l
    values correspond to particular basal/stock objects; they are not all final BTU
    rates. Provider vitamin variant is retained separately.
  snapshot_sha256: 50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c
- evidence_id: komodo413
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=413
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T03:59:21.474126Z'
  support: unknown
  summary: Exact KOMODO413 source returned 403; source-specific content unavailable.
  snapshot_sha256: a8086fb0fa7beb48ec5805da8af4c2f7a84cee1f9e0c5e70c321d4546af8228d
- evidence_id: komodo413fumarate
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=413_replace_Formiate_with_Fumarate
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T03:59:21.525736Z'
  support: unknown
  summary: Exact replacement-variant endpoint returned 403; do not infer replacement
    amounts from its name or transfer both-salt DSM recipe as verified variant.
  snapshot_sha256: 8d00ee1b940d9059d9e0b0b8e3db84a9c2c9c5eed6163e8fc1f44d7c22ffd74e
- evidence_id: komodo41320703
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=413_20703
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T03:59:21.653364Z'
  support: unknown
  summary: Exact strain-variant endpoint returned 403; no strain-specific recipe/growth
    conditions verified.
  snapshot_sha256: eb21d6a514a695f8d6c769e259e7cf60427a85852c7b60a4152e7624bf4b387a
- evidence_id: komodo4136644
  kind: database
  reference: https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=413_6644
  locator: Exact source identity and scoped formulation/preparation
  accessed_at: '2026-10-28T03:59:21.683501Z'
  support: unknown
  summary: Exact strain-variant endpoint returned 403; no strain-specific recipe/growth
    conditions verified.
  snapshot_sha256: fff8fe5e356f90b92bf68e3a863e103656c84b22e51f7dfdaafb939785e173dd
- evidence_id: provider-stage-census
  kind: record_content
  reference: REVIEW_WORK/batch054/record03/provider-stage-census.json
  accessed_at: '2026-10-28T04:14:07.765859Z'
  support: context_only
  summary: Every provider solution volume and recipe row, including amount/unit/g_l/mmol_l/optional/condition.
    Identifiers and derived rates remain in their exact source stage.
  snapshot_sha256: ff6f87bb13c2c6f275382c7e41bc527f2171f2cf0b2d3da0241518e6c3e675d7
- evidence_id: dsm413-visual-1
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium413.pdf
  locator: PDF page1; render REVIEW_WORK/batch054/record03/dsm413-page-1.png
  accessed_at: '2026-10-28T04:14:07.766277Z'
  support: supports
  summary: Visual inspection confirms table/preparation text, including both salts
    and the printed vitamin anomalies; source PDF raw hash is separately pinned.
  snapshot_sha256: 252825186a33ea076537f4aac7fb54b18d9a7508be7d27174dc2c537b006a17c
- evidence_id: dsm413-visual-2
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium413.pdf
  locator: PDF page2; render REVIEW_WORK/batch054/record03/dsm413-page-2.png
  accessed_at: '2026-10-28T04:14:07.766701Z'
  support: supports
  summary: Visual inspection confirms table/preparation text, including both salts
    and the printed vitamin anomalies; source PDF raw hash is separately pinned.
  snapshot_sha256: efeb33fea7ed790b3c7d87e07cb03087fc1c3f6befe8b2497ead63efa0bd46f9
- evidence_id: writer-mediadive
  kind: record_content
  reference: src/culturemech/import/mediadive_importer.py
  locator: _parse_api_composition/_parse_api_solutions
  accessed_at: '2026-10-28T04:14:07.731744Z'
  support: context_only
  summary: Current _parse_api_composition reads only the primary solution, skips stock
    additions and pure-water edges; _parse_api_solutions preserves referenced stocks
    separately. Existing guards are credited; no claim of current flattening causality.
  snapshot_sha256: fc76a182689720e8c3da65f2fe2209924ced59a6973554a0e8bcc152289eed69
- evidence_id: writer-cleanup
  kind: record_content
  reference: scripts/cleanup_recipe_ingredients.py
  locator: merge_ingredient_group
  accessed_at: '2026-10-28T04:14:07.731744Z'
  support: context_only
  summary: Current merge_ingredient_group keeps the first concentration and flags
    differing values; it does not sum the old NaOH or ethanol numbers. Historical
    summed notes are not proof that this current code produced them.
  snapshot_sha256: 5b95ca4155fb8b165b260748c59a30add520cf8747f15b8c08731b2bf48c7ff0
- evidence_id: writer-merge
  kind: record_content
  reference: src/culturemech/merge/merger.py
  locator: merge_group
  accessed_at: '2026-10-28T04:14:07.731744Z'
  support: context_only
  summary: Current merge_group passes multiple inputs to merge_formulation_evidence.
    It does not authenticate source variants from copied matching ingredient sets.
  snapshot_sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
- evidence_id: writer-formulation
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  locator: merge_formulation_evidence
  accessed_at: '2026-10-28T04:14:07.731744Z'
  support: context_only
  summary: Current compatibility guard requires equal formulation content before evidence
    union; ingredient-only similarity is insufficient.
  snapshot_sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
- evidence_id: chebi62965
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_62965
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T03:59:23.661775Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: faa44fb7ad16d3c11aae50472c3f1c5919c56f49d42400897a2fccf2e4861763
- evidence_id: chebi115156
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_115156
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T03:59:22.274459Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 105609ad4e58959de05de4772b043ed1082d7cb1b7342d8555d15df11710eee7
- evidence_id: chebi32145
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_32145
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T03:59:23.319720Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 1f39a220b091088af20782dd27577fb7ca89e037d2b0ea83e76075fb8d77b797
- evidence_id: chebi131527
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_131527
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T03:59:22.310791Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 97e9c2b05f3937c5beeebb4e6338aa6730f9e422ee0e7570a6c622dda8d97a86
- evidence_id: chebi8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_8806
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T03:59:23.817448Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: ceb05e9dd7fba3802d28b34c50bbb604ded87951e4ea3a812739824a84648d72
- evidence_id: chebi91247
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_91247
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T03:59:23.945717Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: a79f2c5fed98052a84e073ebca292320d9aaedae22ca95a1da756aa4d6cacef3
- evidence_id: chebi2509
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_2509
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T03:59:22.926393Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 348b20478bba221cc21e285237104281145111be6ea3aa30d381d6eae19c0a90
- evidence_id: chebi50385
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_50385
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T03:59:23.542736Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 9531274295a20e5b89ae5c0a87c0772ec355c40948c99661eacec8d887712a8a
- evidence_id: chebi28869
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_28869
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T03:59:23.182326Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 4715ccbed9d157f51f1faec46f5f0a552319f187925f9119582a93b84e8c829b
- evidence_id: chebi16236
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_16236
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T03:59:22.647991Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 13f540b5f7d1da3048cb39c5d42fc708b9165abff06f1209414ef248c5975547
- evidence_id: chebi18067
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http://purl.obolibrary.org/obo/CHEBI_18067
  locator: _embedded.terms matching exact obo_id; label/is_obsolete/description/synonyms
  accessed_at: '2026-10-28T03:59:22.932410Z'
  support: supports
  summary: 'Exact OLS term object: accession, current preferred label, obsolete flag,
    definition and synonyms. Supports identifier correspondence only, not recipe amounts
    or growth.'
  snapshot_sha256: 960fe2f954fbe8a045212ffcb213552818fefcbf75d452afc961807ef7cdbb48
- evidence_id: quantities
  kind: record_content
  reference: REVIEW_WORK/batch054/record03/quantity-inventory.json
  accessed_at: '2026-10-28T04:14:07.805802Z'
  support: context_only
  summary: Complete local concentration and source-stage decision inventory; includes
    exact local paths and source failure limits.
  snapshot_sha256: 3551fab37f68f38a9b706052d6d944c2212223774b87504cf3f032f0d5886df1
- evidence_id: grounding
  kind: record_content
  reference: REVIEW_WORK/batch054/record03/grounding-inventory.json
  accessed_at: '2026-10-28T04:14:07.805875Z'
  support: context_only
  summary: All recursive asserted identifier/label slots, exact current OLS objects
    and current packaged MIM preferred-row joins.
  snapshot_sha256: a0ad242ef16ed0a00c04936b692956bd73ee3a8ef8a06af4c994678000533152
- evidence_id: history
  kind: record_content
  reference: REVIEW_WORK/batch054/record03/history-and-evidence-inventory.json
  accessed_at: '2026-10-28T04:14:07.805969Z'
  support: context_only
  summary: Complete current history, references and attached evidence; source-specific
    claims are assessed without authenticating historical execution from code.
  snapshot_sha256: cd2cd77f1634d94773b0dc942db82da5aeb5a377ede29f96a82c4026ee757a56
- evidence_id: scalars
  kind: record_content
  reference: REVIEW_WORK/batch054/record03/scalar-census.json
  accessed_at: '2026-10-28T04:14:07.805997Z'
  support: context_only
  summary: Lossless scalar census of the selected target and all maintained contributors.
  snapshot_sha256: 6b69a221cd4683bda1cdc8cbcd03dcb70d6d79fba05b200dc80e100af72d9738
- evidence_id: validate-schema
  kind: validation
  reference: REVIEW_WORK/batch054/record03/validate-schema.json
  accessed_at: '2026-10-28T03:58:40.611104Z'
  support: supports
  summary: 'Validating schema structure (MediaRecipe)...

    No issues found

    ✓ Schema validation passed

    '
  snapshot_sha256: f3ef7f751c402262f86b9b34121c6e98c9189f97ab03963947132b7b590aa845
- evidence_id: validate-strict
  kind: validation
  reference: REVIEW_WORK/batch054/record03/validate-strict.json
  accessed_at: '2026-10-28T03:58:41.740747Z'
  support: supports
  summary: "Validating 1 files with 1 workers; layers=schema; schema=src/culturemech/schema/culturemech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  layers:        \
    \     schema\n  files with ERROR:   0\n  total ERROR rows:   0\n  TSV:       \
    \         REVIEW_WORK/batch054/record03/strict.tsv\n"
  snapshot_sha256: 307811ffeb066b5bc11f527f2ed0191b2a9f5e19c22290a45a2c8f165d07a576
- evidence_id: validate-terms
  kind: validation
  reference: REVIEW_WORK/batch054/record03/validate-terms.json
  accessed_at: '2026-10-28T03:58:44.146416Z'
  support: supports
  summary: 'Validating ontology terms (MediaRecipe)...

    ✅ Validation passed

    ✓ Term validation passed

    '
  snapshot_sha256: fd0c1a1279841180499212a58a227644e37a8611175bd9fbbd6378d5d5afa934
- evidence_id: validate-references
  kind: validation
  reference: REVIEW_WORK/batch054/record03/validate-references.json
  accessed_at: '2026-10-28T03:58:45.287391Z'
  support: supports
  summary: 'Validating evidence references (MediaRecipe)...

    Reference checks: 0; issues: 0

    ✓ Reference validation passed

    '
  snapshot_sha256: 4c55e0045a4475af5ad90d9ab7c84738f48afa345767c82df407e0e286b49220
assessments:
- assessment_id: a1
  area: evidence
  topic: Provider correspondence versus primary version conflict
  outcome: concern
  summary: The current API explains local numerical provenance, including 1025 mL-based
    rates and nested stock strengths. Embedded 413 and standalone 78 are not identical;
    their literal conflicting cysteine/vitamin statements are retained. Exact current
    KOMODO variants returned 403.
  target_ids:
  - CultureMech:005240
  evidence_ids:
  - api413
  - dsm413
  - dsm78
  - komodo413fumarate
  - provider-stage-census
- assessment_id: a2
  area: quantity
  topic: Complete quantity and numeric preparation audit
  outcome: concern
  summary: Every local concentration field has an explicit disposition; source-only
    doses, batch volumes and conditional preparation are separate from receiving-medium
    rates.
  target_ids:
  - CultureMech:005240
  evidence_ids:
  - quantities
  details: '[{"quantity_id": "q1", "topic": "Sodium formate stock", "source": {"evidence_id":
    "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413", "raw_path":
    "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256": "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c",
    "locator": "$.data.solutions[1].recipe[0]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"},
    "decision": "correct", "rationale": "The provider 60 g/L belongs to the Formiate/Fumarate
    stock. DSM413 gives 6 g formate and 6 g fumarate with 100 mL water, then 30µL
    stock per 1 mL basal medium. Retain stock correspondence but remove the unconditional
    final-ingredient interpretation; do not substitute 6 g/L or 60 g/L as final BTU.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/BTU_MEDIUM.yaml", "field_path":
    "ingredients[0].concentration", "stored_value": {"value": "60", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The provider 60 g/L belongs to the Formiate/Fumarate
    stock. DSM413 gives 6 g formate and 6 g fumarate with 100 mL water, then 30µL
    stock per 1 mL basal medium. Retain stock correspondence but remove the unconditional
    final-ingredient interpretation; do not substitute 6 g/L or 60 g/L as final BTU."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml", "field_path":
    "ingredients[0].concentration", "stored_value": {"value": "60", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The provider 60 g/L belongs to the Formiate/Fumarate
    stock. DSM413 gives 6 g formate and 6 g fumarate with 100 mL water, then 30µL
    stock per 1 mL basal medium. Retain stock correspondence but remove the unconditional
    final-ingredient interpretation; do not substitute 6 g/L or 60 g/L as final BTU."},
    {"path": "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path": "ingredients[0].concentration",
    "stored_value": {"value": "60", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "The provider 60 g/L belongs to the Formiate/Fumarate stock. DSM413 gives 6 g
    formate and 6 g fumarate with 100 mL water, then 30µL stock per 1 mL basal medium.
    Retain stock correspondence but remove the unconditional final-ingredient interpretation;
    do not substitute 6 g/L or 60 g/L as final BTU."}, {"path": "data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "60",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The provider 60 g/L belongs
    to the Formiate/Fumarate stock. DSM413 gives 6 g formate and 6 g fumarate with
    100 mL water, then 30µL stock per 1 mL basal medium. Retain stock correspondence
    but remove the unconditional final-ingredient interpretation; do not substitute
    6 g/L or 60 g/L as final BTU. Exact KOMODO variant access failed; current copied
    numbers do not authorize importing the generic DSM recipe as this variant."},
    {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "60",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The provider 60 g/L belongs
    to the Formiate/Fumarate stock. DSM413 gives 6 g formate and 6 g fumarate with
    100 mL water, then 30µL stock per 1 mL basal medium. Retain stock correspondence
    but remove the unconditional final-ingredient interpretation; do not substitute
    6 g/L or 60 g/L as final BTU. Exact KOMODO variant access failed; current copied
    numbers do not authorize importing the generic DSM recipe as this variant."},
    {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml",
    "field_path": "ingredients[0].concentration", "stored_value": {"value": "60",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The provider 60 g/L belongs
    to the Formiate/Fumarate stock. DSM413 gives 6 g formate and 6 g fumarate with
    100 mL water, then 30µL stock per 1 mL basal medium. Retain stock correspondence
    but remove the unconditional final-ingredient interpretation; do not substitute
    6 g/L or 60 g/L as final BTU. Exact KOMODO variant access failed; current copied
    numbers do not authorize importing the generic DSM recipe as this variant."}]},
    {"quantity_id": "q2", "topic": "Disodium fumarate stock", "source": {"evidence_id":
    "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413", "raw_path":
    "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256": "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c",
    "locator": "$.data.solutions[1].recipe[1]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"},
    "decision": "correct", "rationale": "The provider 60 g/L is the second component
    of the same both-salt stock, not a final-medium dose. The exact DSM413 table contains
    BOTH salts. The named KOMODO replacement remains independently unresolved.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/BTU_MEDIUM.yaml", "field_path": "ingredients[1].concentration",
    "stored_value": {"value": "60", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "The provider 60 g/L is the second component of the same both-salt stock, not
    a final-medium dose. The exact DSM413 table contains BOTH salts. The named KOMODO
    replacement remains independently unresolved."}, {"path": "data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "60",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The provider 60 g/L is
    the second component of the same both-salt stock, not a final-medium dose. The
    exact DSM413 table contains BOTH salts. The named KOMODO replacement remains independently
    unresolved."}, {"path": "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path":
    "ingredients[1].concentration", "stored_value": {"value": "60", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "The provider 60 g/L is the second component
    of the same both-salt stock, not a final-medium dose. The exact DSM413 table contains
    BOTH salts. The named KOMODO replacement remains independently unresolved."},
    {"path": "data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "60",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The provider 60 g/L is
    the second component of the same both-salt stock, not a final-medium dose. The
    exact DSM413 table contains BOTH salts. The named KOMODO replacement remains independently
    unresolved. Exact KOMODO variant access failed; current copied numbers do not
    authorize importing the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "60",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The provider 60 g/L is
    the second component of the same both-salt stock, not a final-medium dose. The
    exact DSM413 table contains BOTH salts. The named KOMODO replacement remains independently
    unresolved. Exact KOMODO variant access failed; current copied numbers do not
    authorize importing the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml",
    "field_path": "ingredients[1].concentration", "stored_value": {"value": "60",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "The provider 60 g/L is
    the second component of the same both-salt stock, not a final-medium dose. The
    exact DSM413 table contains BOTH salts. The named KOMODO replacement remains independently
    unresolved. Exact KOMODO variant access failed; current copied numbers do not
    authorize importing the generic DSM recipe as this variant."}]}, {"quantity_id":
    "q3", "topic": "Beef extraction precursor", "source": {"evidence_id": "api413",
    "reference": "https://mediadive.dsmz.de/rest/medium/413", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin",
    "raw_sha256": "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c",
    "locator": "$.data.solutions[2].recipe[0]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"},
    "decision": "unsupported", "rationale": "Current provider explicitly reports 487.805
    g/L on its 1025 mL Main sol.78 object, matching local digits. Primary source instead
    describes 500 g extraction precursor, removal/retention of meat and filtrate,
    and filtrate makeup to 1000 mL. Neither retained solids nor finished BTU beef
    concentration is thereby established.", "layer_assessments": [{"path": "data/merge_yaml/merged/BTU_MEDIUM.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "487.805",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Current provider
    explicitly reports 487.805 g/L on its 1025 mL Main sol.78 object, matching local
    digits. Primary source instead describes 500 g extraction precursor, removal/retention
    of meat and filtrate, and filtrate makeup to 1000 mL. Neither retained solids
    nor finished BTU beef concentration is thereby established."}, {"path": "data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "487.805",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Current provider
    explicitly reports 487.805 g/L on its 1025 mL Main sol.78 object, matching local
    digits. Primary source instead describes 500 g extraction precursor, removal/retention
    of meat and filtrate, and filtrate makeup to 1000 mL. Neither retained solids
    nor finished BTU beef concentration is thereby established."}, {"path": "data/normalized_yaml/bacterial/btu_medium.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "487.805",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Current provider
    explicitly reports 487.805 g/L on its 1025 mL Main sol.78 object, matching local
    digits. Primary source instead describes 500 g extraction precursor, removal/retention
    of meat and filtrate, and filtrate makeup to 1000 mL. Neither retained solids
    nor finished BTU beef concentration is thereby established."}, {"path": "data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "487.805",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Current provider
    explicitly reports 487.805 g/L on its 1025 mL Main sol.78 object, matching local
    digits. Primary source instead describes 500 g extraction precursor, removal/retention
    of meat and filtrate, and filtrate makeup to 1000 mL. Neither retained solids
    nor finished BTU beef concentration is thereby established. Exact KOMODO variant
    access failed; current copied numbers do not authorize importing the generic DSM
    recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "487.805",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Current provider
    explicitly reports 487.805 g/L on its 1025 mL Main sol.78 object, matching local
    digits. Primary source instead describes 500 g extraction precursor, removal/retention
    of meat and filtrate, and filtrate makeup to 1000 mL. Neither retained solids
    nor finished BTU beef concentration is thereby established. Exact KOMODO variant
    access failed; current copied numbers do not authorize importing the generic DSM
    recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml",
    "field_path": "ingredients[2].concentration", "stored_value": {"value": "487.805",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Current provider
    explicitly reports 487.805 g/L on its 1025 mL Main sol.78 object, matching local
    digits. Primary source instead describes 500 g extraction precursor, removal/retention
    of meat and filtrate, and filtrate makeup to 1000 mL. Neither retained solids
    nor finished BTU beef concentration is thereby established. Exact KOMODO variant
    access failed; current copied numbers do not authorize importing the generic DSM
    recipe as this variant."}]}, {"quantity_id": "q4", "topic": "NaOH solution dimensions
    and stages", "source": {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413",
    "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256":
    "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator":
    "$.data.solutions[2].recipe[2]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"},
    "decision": "correct", "rationale": "Local 26 G_PER_L sums 25 mL1N NaOH in the
    extraction stage and 1 mL1N NaOH in the separate hemin stock. These are solution
    volumes with a stated normality, not two masses with a common denominator. Keep
    the two stages separate; no density/normality conversion or sum is justified.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/BTU_MEDIUM.yaml", "field_path":
    "ingredients[3].concentration", "stored_value": {"value": "26.0", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "Local 26 G_PER_L sums 25 mL1N NaOH in the
    extraction stage and 1 mL1N NaOH in the separate hemin stock. These are solution
    volumes with a stated normality, not two masses with a common denominator. Keep
    the two stages separate; no density/normality conversion or sum is justified."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml", "field_path":
    "ingredients[3].concentration", "stored_value": {"value": "26.0", "unit": "G_PER_L"},
    "decision": "correct", "rationale": "Local 26 G_PER_L sums 25 mL1N NaOH in the
    extraction stage and 1 mL1N NaOH in the separate hemin stock. These are solution
    volumes with a stated normality, not two masses with a common denominator. Keep
    the two stages separate; no density/normality conversion or sum is justified."},
    {"path": "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path": "ingredients[3].concentration",
    "stored_value": {"value": "26.0", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "Local 26 G_PER_L sums 25 mL1N NaOH in the extraction stage and 1 mL1N NaOH in
    the separate hemin stock. These are solution volumes with a stated normality,
    not two masses with a common denominator. Keep the two stages separate; no density/normality
    conversion or sum is justified."}, {"path": "data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "26.0",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 26 G_PER_L sums
    25 mL1N NaOH in the extraction stage and 1 mL1N NaOH in the separate hemin stock.
    These are solution volumes with a stated normality, not two masses with a common
    denominator. Keep the two stages separate; no density/normality conversion or
    sum is justified. Exact KOMODO variant access failed; current copied numbers do
    not authorize importing the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "26.0",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 26 G_PER_L sums
    25 mL1N NaOH in the extraction stage and 1 mL1N NaOH in the separate hemin stock.
    These are solution volumes with a stated normality, not two masses with a common
    denominator. Keep the two stages separate; no density/normality conversion or
    sum is justified. Exact KOMODO variant access failed; current copied numbers do
    not authorize importing the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml",
    "field_path": "ingredients[3].concentration", "stored_value": {"value": "26.0",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 26 G_PER_L sums
    25 mL1N NaOH in the extraction stage and 1 mL1N NaOH in the separate hemin stock.
    These are solution volumes with a stated normality, not two masses with a common
    denominator. Keep the two stages separate; no density/normality conversion or
    sum is justified. Exact KOMODO variant access failed; current copied numbers do
    not authorize importing the generic DSM recipe as this variant."}]}, {"quantity_id":
    "q5", "topic": "Casitone after filtrate makeup", "source": {"evidence_id": "api413",
    "reference": "https://mediadive.dsmz.de/rest/medium/413", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin",
    "raw_sha256": "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c",
    "locator": "$.data.solutions[2].recipe[3]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"},
    "decision": "unsupported", "rationale": "Provider 29.2683 g/L is an exact declared
    value on its 1025 mL object. Primary source places 30 g after filtrate makeup
    to 1000 mL. Preserve the 30 g batch addition and provider disagreement; do not
    silently assert an independently measured final BTU denominator.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/BTU_MEDIUM.yaml", "field_path": "ingredients[4].concentration",
    "stored_value": {"value": "29.2683", "unit": "G_PER_L"}, "decision": "unsupported",
    "rationale": "Provider 29.2683 g/L is an exact declared value on its 1025 mL object.
    Primary source places 30 g after filtrate makeup to 1000 mL. Preserve the 30 g
    batch addition and provider disagreement; do not silently assert an independently
    measured final BTU denominator."}, {"path": "data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "29.2683",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 29.2683
    g/L is an exact declared value on its 1025 mL object. Primary source places 30
    g after filtrate makeup to 1000 mL. Preserve the 30 g batch addition and provider
    disagreement; do not silently assert an independently measured final BTU denominator."},
    {"path": "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path": "ingredients[4].concentration",
    "stored_value": {"value": "29.2683", "unit": "G_PER_L"}, "decision": "unsupported",
    "rationale": "Provider 29.2683 g/L is an exact declared value on its 1025 mL object.
    Primary source places 30 g after filtrate makeup to 1000 mL. Preserve the 30 g
    batch addition and provider disagreement; do not silently assert an independently
    measured final BTU denominator."}, {"path": "data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "29.2683",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 29.2683
    g/L is an exact declared value on its 1025 mL object. Primary source places 30
    g after filtrate makeup to 1000 mL. Preserve the 30 g batch addition and provider
    disagreement; do not silently assert an independently measured final BTU denominator.
    Exact KOMODO variant access failed; current copied numbers do not authorize importing
    the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "29.2683",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 29.2683
    g/L is an exact declared value on its 1025 mL object. Primary source places 30
    g after filtrate makeup to 1000 mL. Preserve the 30 g batch addition and provider
    disagreement; do not silently assert an independently measured final BTU denominator.
    Exact KOMODO variant access failed; current copied numbers do not authorize importing
    the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml",
    "field_path": "ingredients[4].concentration", "stored_value": {"value": "29.2683",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 29.2683
    g/L is an exact declared value on its 1025 mL object. Primary source places 30
    g after filtrate makeup to 1000 mL. Preserve the 30 g batch addition and provider
    disagreement; do not silently assert an independently measured final BTU denominator.
    Exact KOMODO variant access failed; current copied numbers do not authorize importing
    the generic DSM recipe as this variant."}]}, {"quantity_id": "q6", "topic": "Yeast
    extract after filtrate makeup", "source": {"evidence_id": "api413", "reference":
    "https://mediadive.dsmz.de/rest/medium/413", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin",
    "raw_sha256": "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c",
    "locator": "$.data.solutions[2].recipe[4]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"},
    "decision": "unsupported", "rationale": "Provider 4.87805 g/L is an exact declared
    value on its 1025 mL object. Primary source specifies 5 g after filtrate makeup.
    Preserve batch mass and denominator/stage conflict; no universal final rate is
    authenticated.", "layer_assessments": [{"path": "data/merge_yaml/merged/BTU_MEDIUM.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "4.87805",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 4.87805
    g/L is an exact declared value on its 1025 mL object. Primary source specifies
    5 g after filtrate makeup. Preserve batch mass and denominator/stage conflict;
    no universal final rate is authenticated."}, {"path": "data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "4.87805",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 4.87805
    g/L is an exact declared value on its 1025 mL object. Primary source specifies
    5 g after filtrate makeup. Preserve batch mass and denominator/stage conflict;
    no universal final rate is authenticated."}, {"path": "data/normalized_yaml/bacterial/btu_medium.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "4.87805",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 4.87805
    g/L is an exact declared value on its 1025 mL object. Primary source specifies
    5 g after filtrate makeup. Preserve batch mass and denominator/stage conflict;
    no universal final rate is authenticated."}, {"path": "data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "4.87805",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 4.87805
    g/L is an exact declared value on its 1025 mL object. Primary source specifies
    5 g after filtrate makeup. Preserve batch mass and denominator/stage conflict;
    no universal final rate is authenticated. Exact KOMODO variant access failed;
    current copied numbers do not authorize importing the generic DSM recipe as this
    variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "4.87805",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 4.87805
    g/L is an exact declared value on its 1025 mL object. Primary source specifies
    5 g after filtrate makeup. Preserve batch mass and denominator/stage conflict;
    no universal final rate is authenticated. Exact KOMODO variant access failed;
    current copied numbers do not authorize importing the generic DSM recipe as this
    variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml",
    "field_path": "ingredients[5].concentration", "stored_value": {"value": "4.87805",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 4.87805
    g/L is an exact declared value on its 1025 mL object. Primary source specifies
    5 g after filtrate makeup. Preserve batch mass and denominator/stage conflict;
    no universal final rate is authenticated. Exact KOMODO variant access failed;
    current copied numbers do not authorize importing the generic DSM recipe as this
    variant."}]}, {"quantity_id": "q7", "topic": "Dipotassium hydrogen phosphate",
    "source": {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413",
    "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256":
    "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator":
    "$.data.solutions[2].recipe[5]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"},
    "decision": "unsupported", "rationale": "Provider 4.87805 g/L matches local digits,
    but primary source specifies 5 g after filtrate makeup to 1000 mL. K2HPO4 identity
    is supported; do not choose a hydrate or final-medium denominator from this correspondence.",
    "layer_assessments": [{"path": "data/merge_yaml/merged/BTU_MEDIUM.yaml", "field_path":
    "ingredients[6].concentration", "stored_value": {"value": "4.87805", "unit": "G_PER_L"},
    "decision": "unsupported", "rationale": "Provider 4.87805 g/L matches local digits,
    but primary source specifies 5 g after filtrate makeup to 1000 mL. K2HPO4 identity
    is supported; do not choose a hydrate or final-medium denominator from this correspondence."},
    {"path": "data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml", "field_path":
    "ingredients[6].concentration", "stored_value": {"value": "4.87805", "unit": "G_PER_L"},
    "decision": "unsupported", "rationale": "Provider 4.87805 g/L matches local digits,
    but primary source specifies 5 g after filtrate makeup to 1000 mL. K2HPO4 identity
    is supported; do not choose a hydrate or final-medium denominator from this correspondence."},
    {"path": "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path": "ingredients[6].concentration",
    "stored_value": {"value": "4.87805", "unit": "G_PER_L"}, "decision": "unsupported",
    "rationale": "Provider 4.87805 g/L matches local digits, but primary source specifies
    5 g after filtrate makeup to 1000 mL. K2HPO4 identity is supported; do not choose
    a hydrate or final-medium denominator from this correspondence."}, {"path": "data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "4.87805",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 4.87805
    g/L matches local digits, but primary source specifies 5 g after filtrate makeup
    to 1000 mL. K2HPO4 identity is supported; do not choose a hydrate or final-medium
    denominator from this correspondence. Exact KOMODO variant access failed; current
    copied numbers do not authorize importing the generic DSM recipe as this variant."},
    {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "4.87805",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 4.87805
    g/L matches local digits, but primary source specifies 5 g after filtrate makeup
    to 1000 mL. K2HPO4 identity is supported; do not choose a hydrate or final-medium
    denominator from this correspondence. Exact KOMODO variant access failed; current
    copied numbers do not authorize importing the generic DSM recipe as this variant."},
    {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml",
    "field_path": "ingredients[6].concentration", "stored_value": {"value": "4.87805",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 4.87805
    g/L matches local digits, but primary source specifies 5 g after filtrate makeup
    to 1000 mL. K2HPO4 identity is supported; do not choose a hydrate or final-medium
    denominator from this correspondence. Exact KOMODO variant access failed; current
    copied numbers do not authorize importing the generic DSM recipe as this variant."}]},
    {"quantity_id": "q8", "topic": "Resazurin amount", "source": {"evidence_id": "api413",
    "reference": "https://mediadive.dsmz.de/rest/medium/413", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin",
    "raw_sha256": "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c",
    "locator": "$.data.solutions[2].recipe[6]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"},
    "decision": "unsupported", "rationale": "Provider 0.00097561 g/L matches local
    digits; primary source specifies 1 mg batch addition after filtrate makeup.1 mg=0.001
    g is a mass conversion only, not proof of final BTU volume. No sodium-salt substitution
    is inferred.", "layer_assessments": [{"path": "data/merge_yaml/merged/BTU_MEDIUM.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.00097561",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 0.00097561
    g/L matches local digits; primary source specifies 1 mg batch addition after filtrate
    makeup.1 mg=0.001 g is a mass conversion only, not proof of final BTU volume.
    No sodium-salt substitution is inferred."}, {"path": "data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.00097561",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 0.00097561
    g/L matches local digits; primary source specifies 1 mg batch addition after filtrate
    makeup.1 mg=0.001 g is a mass conversion only, not proof of final BTU volume.
    No sodium-salt substitution is inferred."}, {"path": "data/normalized_yaml/bacterial/btu_medium.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.00097561",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 0.00097561
    g/L matches local digits; primary source specifies 1 mg batch addition after filtrate
    makeup.1 mg=0.001 g is a mass conversion only, not proof of final BTU volume.
    No sodium-salt substitution is inferred."}, {"path": "data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.00097561",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 0.00097561
    g/L matches local digits; primary source specifies 1 mg batch addition after filtrate
    makeup.1 mg=0.001 g is a mass conversion only, not proof of final BTU volume.
    No sodium-salt substitution is inferred. Exact KOMODO variant access failed; current
    copied numbers do not authorize importing the generic DSM recipe as this variant."},
    {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.00097561",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 0.00097561
    g/L matches local digits; primary source specifies 1 mg batch addition after filtrate
    makeup.1 mg=0.001 g is a mass conversion only, not proof of final BTU volume.
    No sodium-salt substitution is inferred. Exact KOMODO variant access failed; current
    copied numbers do not authorize importing the generic DSM recipe as this variant."},
    {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml",
    "field_path": "ingredients[7].concentration", "stored_value": {"value": "0.00097561",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Provider 0.00097561
    g/L matches local digits; primary source specifies 1 mg batch addition after filtrate
    makeup.1 mg=0.001 g is a mass conversion only, not proof of final BTU volume.
    No sodium-salt substitution is inferred. Exact KOMODO variant access failed; current
    copied numbers do not authorize importing the generic DSM recipe as this variant."}]},
    {"quantity_id": "q9", "topic": "Cysteine identity/version", "source": {"evidence_id":
    "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413", "raw_path":
    "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256": "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c",
    "locator": "$.data.solutions[2].recipe[7]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"},
    "decision": "unsupported", "rationale": "Local 0.487805 g/L L-cysteine hydrochloride
    matches provider Main sol.78 but conflicts with its own instruction 0.5 g/L L-cysteine
    hydrochloride. Embedded DSM413 says 0.5 g/L cysteine without HCl; standalone 78
    explicitly says L-cysteine hydrochloride. Retain this source/version conflict
    rather than retroactively using newer 78 to authenticate embedded 413.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/BTU_MEDIUM.yaml", "field_path": "ingredients[8].concentration",
    "stored_value": {"value": "0.487805", "unit": "G_PER_L"}, "decision": "unsupported",
    "rationale": "Local 0.487805 g/L L-cysteine hydrochloride matches provider Main
    sol.78 but conflicts with its own instruction 0.5 g/L L-cysteine hydrochloride.
    Embedded DSM413 says 0.5 g/L cysteine without HCl; standalone 78 explicitly says
    L-cysteine hydrochloride. Retain this source/version conflict rather than retroactively
    using newer 78 to authenticate embedded 413."}, {"path": "data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.487805",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Local 0.487805 g/L
    L-cysteine hydrochloride matches provider Main sol.78 but conflicts with its own
    instruction 0.5 g/L L-cysteine hydrochloride. Embedded DSM413 says 0.5 g/L cysteine
    without HCl; standalone 78 explicitly says L-cysteine hydrochloride. Retain this
    source/version conflict rather than retroactively using newer 78 to authenticate
    embedded 413."}, {"path": "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path":
    "ingredients[8].concentration", "stored_value": {"value": "0.487805", "unit":
    "G_PER_L"}, "decision": "unsupported", "rationale": "Local 0.487805 g/L L-cysteine
    hydrochloride matches provider Main sol.78 but conflicts with its own instruction
    0.5 g/L L-cysteine hydrochloride. Embedded DSM413 says 0.5 g/L cysteine without
    HCl; standalone 78 explicitly says L-cysteine hydrochloride. Retain this source/version
    conflict rather than retroactively using newer 78 to authenticate embedded 413."},
    {"path": "data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.487805",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Local 0.487805 g/L
    L-cysteine hydrochloride matches provider Main sol.78 but conflicts with its own
    instruction 0.5 g/L L-cysteine hydrochloride. Embedded DSM413 says 0.5 g/L cysteine
    without HCl; standalone 78 explicitly says L-cysteine hydrochloride. Retain this
    source/version conflict rather than retroactively using newer 78 to authenticate
    embedded 413. Exact KOMODO variant access failed; current copied numbers do not
    authorize importing the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.487805",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Local 0.487805 g/L
    L-cysteine hydrochloride matches provider Main sol.78 but conflicts with its own
    instruction 0.5 g/L L-cysteine hydrochloride. Embedded DSM413 says 0.5 g/L cysteine
    without HCl; standalone 78 explicitly says L-cysteine hydrochloride. Retain this
    source/version conflict rather than retroactively using newer 78 to authenticate
    embedded 413. Exact KOMODO variant access failed; current copied numbers do not
    authorize importing the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml",
    "field_path": "ingredients[8].concentration", "stored_value": {"value": "0.487805",
    "unit": "G_PER_L"}, "decision": "unsupported", "rationale": "Local 0.487805 g/L
    L-cysteine hydrochloride matches provider Main sol.78 but conflicts with its own
    instruction 0.5 g/L L-cysteine hydrochloride. Embedded DSM413 says 0.5 g/L cysteine
    without HCl; standalone 78 explicitly says L-cysteine hydrochloride. Retain this
    source/version conflict rather than retroactively using newer 78 to authenticate
    embedded 413. Exact KOMODO variant access failed; current copied numbers do not
    authorize importing the generic DSM recipe as this variant."}]}, {"quantity_id":
    "q10", "topic": "Conditional agar", "source": {"evidence_id": "api413", "reference":
    "https://mediadive.dsmz.de/rest/medium/413", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin",
    "raw_sha256": "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c",
    "locator": "$.data.solutions[2].recipe[8]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"},
    "decision": "correct", "rationale": "Provider 14.6341 g/L belongs to its 1025
    mL object and is conditional for solid medium. Primary source explicitly gives
    15 g agar per 1000 mL medium for slants. Preserve that conditional 15 g/L basis,
    not unconditional solid growth for all variants.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/BTU_MEDIUM.yaml", "field_path": "ingredients[9].concentration",
    "stored_value": {"value": "14.6341", "unit": "G_PER_L"}, "decision": "correct",
    "rationale": "Provider 14.6341 g/L belongs to its 1025 mL object and is conditional
    for solid medium. Primary source explicitly gives 15 g agar per 1000 mL medium
    for slants. Preserve that conditional 15 g/L basis, not unconditional solid growth
    for all variants."}, {"path": "data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "14.6341",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Provider 14.6341 g/L
    belongs to its 1025 mL object and is conditional for solid medium. Primary source
    explicitly gives 15 g agar per 1000 mL medium for slants. Preserve that conditional
    15 g/L basis, not unconditional solid growth for all variants."}, {"path": "data/normalized_yaml/bacterial/btu_medium.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "14.6341",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Provider 14.6341 g/L
    belongs to its 1025 mL object and is conditional for solid medium. Primary source
    explicitly gives 15 g agar per 1000 mL medium for slants. Preserve that conditional
    15 g/L basis, not unconditional solid growth for all variants."}, {"path": "data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "14.6341",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Provider 14.6341 g/L
    belongs to its 1025 mL object and is conditional for solid medium. Primary source
    explicitly gives 15 g agar per 1000 mL medium for slants. Preserve that conditional
    15 g/L basis, not unconditional solid growth for all variants. Exact KOMODO variant
    access failed; current copied numbers do not authorize importing the generic DSM
    recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "14.6341",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Provider 14.6341 g/L
    belongs to its 1025 mL object and is conditional for solid medium. Primary source
    explicitly gives 15 g agar per 1000 mL medium for slants. Preserve that conditional
    15 g/L basis, not unconditional solid growth for all variants. Exact KOMODO variant
    access failed; current copied numbers do not authorize importing the generic DSM
    recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml",
    "field_path": "ingredients[9].concentration", "stored_value": {"value": "14.6341",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Provider 14.6341 g/L
    belongs to its 1025 mL object and is conditional for solid medium. Primary source
    explicitly gives 15 g agar per 1000 mL medium for slants. Preserve that conditional
    15 g/L basis, not unconditional solid growth for all variants. Exact KOMODO variant
    access failed; current copied numbers do not authorize importing the generic DSM
    recipe as this variant."}]}, {"quantity_id": "q11", "topic": "Hemin stock", "source":
    {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413",
    "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256":
    "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator":
    "$.data.solutions[3].recipe[0]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"},
    "decision": "correct", "rationale": "Local 0.5 g/L is numerically supported as
    50 mg made up to 100 mL in the hemin stock. It is not the receiving-medium concentration.
    The stock is a conditional 10 mL addition per 1000 mL basal medium.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/BTU_MEDIUM.yaml", "field_path": "ingredients[10].concentration",
    "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "Local 0.5 g/L is numerically supported as 50 mg made up to 100 mL in the hemin
    stock. It is not the receiving-medium concentration. The stock is a conditional
    10 mL addition per 1000 mL basal medium."}, {"path": "data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 0.5 g/L is numerically
    supported as 50 mg made up to 100 mL in the hemin stock. It is not the receiving-medium
    concentration. The stock is a conditional 10 mL addition per 1000 mL basal medium."},
    {"path": "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path": "ingredients[10].concentration",
    "stored_value": {"value": "0.5", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "Local 0.5 g/L is numerically supported as 50 mg made up to 100 mL in the hemin
    stock. It is not the receiving-medium concentration. The stock is a conditional
    10 mL addition per 1000 mL basal medium."}, {"path": "data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 0.5 g/L is numerically
    supported as 50 mg made up to 100 mL in the hemin stock. It is not the receiving-medium
    concentration. The stock is a conditional 10 mL addition per 1000 mL basal medium.
    Exact KOMODO variant access failed; current copied numbers do not authorize importing
    the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 0.5 g/L is numerically
    supported as 50 mg made up to 100 mL in the hemin stock. It is not the receiving-medium
    concentration. The stock is a conditional 10 mL addition per 1000 mL basal medium.
    Exact KOMODO variant access failed; current copied numbers do not authorize importing
    the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml",
    "field_path": "ingredients[10].concentration", "stored_value": {"value": "0.5",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 0.5 g/L is numerically
    supported as 50 mg made up to 100 mL in the hemin stock. It is not the receiving-medium
    concentration. The stock is a conditional 10 mL addition per 1000 mL basal medium.
    Exact KOMODO variant access failed; current copied numbers do not authorize importing
    the generic DSM recipe as this variant."}]}, {"quantity_id": "q12", "topic": "Vitamin
    K3 stock/version", "source": {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413",
    "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256":
    "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator":
    "$.data.solutions[4].recipe[0]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"},
    "decision": "correct", "rationale": "Local 0.05 g/L equals 0.05 mg/mL, the diluted
    stock strength in standalone 78 and the current provider. Credit that exact numerical
    equality. Embedded DSM413 instead specifies 5 mg/mL K3 in 10 mL95%ethanol. Neither
    stock strength is a universal final-medium concentration.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/BTU_MEDIUM.yaml", "field_path": "ingredients[11].concentration",
    "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "Local 0.05 g/L equals 0.05 mg/mL, the diluted stock strength in standalone 78
    and the current provider. Credit that exact numerical equality. Embedded DSM413
    instead specifies 5 mg/mL K3 in 10 mL95%ethanol. Neither stock strength is a universal
    final-medium concentration."}, {"path": "data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 0.05 g/L equals
    0.05 mg/mL, the diluted stock strength in standalone 78 and the current provider.
    Credit that exact numerical equality. Embedded DSM413 instead specifies 5 mg/mL
    K3 in 10 mL95%ethanol. Neither stock strength is a universal final-medium concentration."},
    {"path": "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path": "ingredients[11].concentration",
    "stored_value": {"value": "0.05", "unit": "G_PER_L"}, "decision": "correct", "rationale":
    "Local 0.05 g/L equals 0.05 mg/mL, the diluted stock strength in standalone 78
    and the current provider. Credit that exact numerical equality. Embedded DSM413
    instead specifies 5 mg/mL K3 in 10 mL95%ethanol. Neither stock strength is a universal
    final-medium concentration."}, {"path": "data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 0.05 g/L equals
    0.05 mg/mL, the diluted stock strength in standalone 78 and the current provider.
    Credit that exact numerical equality. Embedded DSM413 instead specifies 5 mg/mL
    K3 in 10 mL95%ethanol. Neither stock strength is a universal final-medium concentration.
    Exact KOMODO variant access failed; current copied numbers do not authorize importing
    the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 0.05 g/L equals
    0.05 mg/mL, the diluted stock strength in standalone 78 and the current provider.
    Credit that exact numerical equality. Embedded DSM413 instead specifies 5 mg/mL
    K3 in 10 mL95%ethanol. Neither stock strength is a universal final-medium concentration.
    Exact KOMODO variant access failed; current copied numbers do not authorize importing
    the generic DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml",
    "field_path": "ingredients[11].concentration", "stored_value": {"value": "0.05",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 0.05 g/L equals
    0.05 mg/mL, the diluted stock strength in standalone 78 and the current provider.
    Credit that exact numerical equality. Embedded DSM413 instead specifies 5 mg/mL
    K3 in 10 mL95%ethanol. Neither stock strength is a universal final-medium concentration.
    Exact KOMODO variant access failed; current copied numbers do not authorize importing
    the generic DSM recipe as this variant."}]}, {"quantity_id": "q13", "topic": "Ethanol
    stock solvent", "source": {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413",
    "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256":
    "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator":
    "$.data.solutions[5].recipe[1]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"},
    "decision": "correct", "rationale": "Local 959.5 g/L combines provider 9.5 and
    950 values from different K3/K1 stocks. The primary sources describe 95%ethanol
    solution volumes, without an explicit percentage basis here. Keep source-specific
    stock solvents and exclude an unsupported mass sum.", "layer_assessments": [{"path":
    "data/merge_yaml/merged/BTU_MEDIUM.yaml", "field_path": "ingredients[12].concentration",
    "stored_value": {"value": "959.5", "unit": "G_PER_L"}, "decision": "correct",
    "rationale": "Local 959.5 g/L combines provider 9.5 and 950 values from different
    K3/K1 stocks. The primary sources describe 95%ethanol solution volumes, without
    an explicit percentage basis here. Keep source-specific stock solvents and exclude
    an unsupported mass sum."}, {"path": "data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "959.5",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 959.5 g/L combines
    provider 9.5 and 950 values from different K3/K1 stocks. The primary sources describe
    95%ethanol solution volumes, without an explicit percentage basis here. Keep source-specific
    stock solvents and exclude an unsupported mass sum."}, {"path": "data/normalized_yaml/bacterial/btu_medium.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "959.5",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 959.5 g/L combines
    provider 9.5 and 950 values from different K3/K1 stocks. The primary sources describe
    95%ethanol solution volumes, without an explicit percentage basis here. Keep source-specific
    stock solvents and exclude an unsupported mass sum."}, {"path": "data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "959.5",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 959.5 g/L combines
    provider 9.5 and 950 values from different K3/K1 stocks. The primary sources describe
    95%ethanol solution volumes, without an explicit percentage basis here. Keep source-specific
    stock solvents and exclude an unsupported mass sum. Exact KOMODO variant access
    failed; current copied numbers do not authorize importing the generic DSM recipe
    as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "959.5",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 959.5 g/L combines
    provider 9.5 and 950 values from different K3/K1 stocks. The primary sources describe
    95%ethanol solution volumes, without an explicit percentage basis here. Keep source-specific
    stock solvents and exclude an unsupported mass sum. Exact KOMODO variant access
    failed; current copied numbers do not authorize importing the generic DSM recipe
    as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml",
    "field_path": "ingredients[12].concentration", "stored_value": {"value": "959.5",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Local 959.5 g/L combines
    provider 9.5 and 950 values from different K3/K1 stocks. The primary sources describe
    95%ethanol solution volumes, without an explicit percentage basis here. Keep source-specific
    stock solvents and exclude an unsupported mass sum. Exact KOMODO variant access
    failed; current copied numbers do not authorize importing the generic DSM recipe
    as this variant."}]}, {"quantity_id": "q14", "topic": "Vitamin K1 liquid amount",
    "source": {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413",
    "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256":
    "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator":
    "$.data.solutions[5].recipe[0]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"},
    "decision": "correct", "rationale": "Primary and provider specify 0.1 mL vitamin
    K1 in 20 mL95%ethanol. Local 0.1 G_PER_L treats a volume as a mass rate without
    density or a receiving-medium basis. Embedded 413 K1/K3 wording remains a literal
    source anomaly, not silently repaired.", "layer_assessments": [{"path": "data/merge_yaml/merged/BTU_MEDIUM.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Primary and provider
    specify 0.1 mL vitamin K1 in 20 mL95%ethanol. Local 0.1 G_PER_L treats a volume
    as a mass rate without density or a receiving-medium basis. Embedded 413 K1/K3
    wording remains a literal source anomaly, not silently repaired."}, {"path": "data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Primary and provider
    specify 0.1 mL vitamin K1 in 20 mL95%ethanol. Local 0.1 G_PER_L treats a volume
    as a mass rate without density or a receiving-medium basis. Embedded 413 K1/K3
    wording remains a literal source anomaly, not silently repaired."}, {"path": "data/normalized_yaml/bacterial/btu_medium.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Primary and provider
    specify 0.1 mL vitamin K1 in 20 mL95%ethanol. Local 0.1 G_PER_L treats a volume
    as a mass rate without density or a receiving-medium basis. Embedded 413 K1/K3
    wording remains a literal source anomaly, not silently repaired."}, {"path": "data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Primary and provider
    specify 0.1 mL vitamin K1 in 20 mL95%ethanol. Local 0.1 G_PER_L treats a volume
    as a mass rate without density or a receiving-medium basis. Embedded 413 K1/K3
    wording remains a literal source anomaly, not silently repaired. Exact KOMODO
    variant access failed; current copied numbers do not authorize importing the generic
    DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Primary and provider
    specify 0.1 mL vitamin K1 in 20 mL95%ethanol. Local 0.1 G_PER_L treats a volume
    as a mass rate without density or a receiving-medium basis. Embedded 413 K1/K3
    wording remains a literal source anomaly, not silently repaired. Exact KOMODO
    variant access failed; current copied numbers do not authorize importing the generic
    DSM recipe as this variant."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml",
    "field_path": "ingredients[13].concentration", "stored_value": {"value": "0.1",
    "unit": "G_PER_L"}, "decision": "correct", "rationale": "Primary and provider
    specify 0.1 mL vitamin K1 in 20 mL95%ethanol. Local 0.1 G_PER_L treats a volume
    as a mass rate without density or a receiving-medium basis. Embedded 413 K1/K3
    wording remains a literal source anomaly, not silently repaired. Exact KOMODO
    variant access failed; current copied numbers do not authorize importing the generic
    DSM recipe as this variant."}]}, {"quantity_id": "q15", "topic": "pH 7 and source
    scope", "source": {"evidence_id": "dsm413", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium413.pdf",
    "raw_path": "REVIEW_WORK/batch054/source01-03/dsm413.bin", "raw_sha256": "2dc547e81e376a04e46659d3d0b800d9c9ec5dbedd1abe9ffcaaa59d9bfbd27f",
    "locator": "Page1 embedded78 preparation", "accessed_at": "2026-10-28T03:59:21.850645+00:00",
    "quote": "pH to 7.0."}, "decision": "mixed", "rationale": "The standalone 78 DSM21650
    pH 8.5 exception is excluded from BTU and its unverified strain variants.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/BTU_MEDIUM.yaml", "field_path": "ph_value",
    "stored_value": 7.0, "decision": "evidence_only", "rationale": "Retain pH 7 correspondence
    to the generic primary and current provider."}, {"path": "data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml",
    "field_path": "ph_value", "stored_value": 7.0, "decision": "evidence_only", "rationale":
    "Retain pH 7 correspondence to the generic primary and current provider."}, {"path":
    "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path": "ph_value", "stored_value":
    7.0, "decision": "evidence_only", "rationale": "Retain pH 7 correspondence to
    the generic primary and current provider."}, {"path": "data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml",
    "field_path": "ph_value", "stored_value": 7.0, "decision": "unsupported", "rationale":
    "DSM413 supports pH 7 for the generic formulation; exact inaccessible variants
    are not thereby authenticated."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml",
    "field_path": "ph_value", "stored_value": 7.0, "decision": "unsupported", "rationale":
    "DSM413 supports pH 7 for the generic formulation; exact inaccessible variants
    are not thereby authenticated."}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml",
    "field_path": "ph_value", "stored_value": 7.0, "decision": "unsupported", "rationale":
    "DSM413 supports pH 7 for the generic formulation; exact inaccessible variants
    are not thereby authenticated."}]}, {"quantity_id": "q16", "topic": "Existing
    DSM preparation step 1", "source": {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413",
    "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256":
    "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator":
    "$.data.solutions[0].steps[0]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"},
    "decision": "evidence_only", "rationale": "Existing DSM owner already preserves
    30µL/mL addition before inoculation; equivalent provider assembly row is 30 mL
    stock with 1000 mL basal medium. Preserve dose versus total-volume distinction.",
    "layer_assessments": [{"path": "data/normalized_yaml/bacterial/btu_medium.yaml",
    "field_path": "preparation_steps[0].description", "stored_value": "Add 30 µl Formiate/Fumarate
    Solution per ml of medium 78 before inoculation.", "decision": "evidence_only",
    "rationale": "Existing DSM owner already preserves 30µL/mL addition before inoculation;
    equivalent provider assembly row is 30 mL stock with 1000 mL basal medium. Preserve
    dose versus total-volume distinction."}]}, {"quantity_id": "q17", "topic": "Existing
    DSM preparation step 2", "source": {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413",
    "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256":
    "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator":
    "$.data.solutions[1].steps[0]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"},
    "decision": "evidence_only", "rationale": "Existing filter-sterilization instruction
    belongs to the Formiate/Fumarate stock.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/btu_medium.yaml",
    "field_path": "preparation_steps[1].description", "stored_value": "Filter sterilize.",
    "decision": "evidence_only", "rationale": "Existing filter-sterilization instruction
    belongs to the Formiate/Fumarate stock."}]}, {"quantity_id": "q18", "topic": "Existing
    DSM preparation step 3", "source": {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413",
    "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256":
    "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator":
    "$.data.solutions[2].steps[0]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"},
    "decision": "evidence_only", "rationale": "Existing prose retains 100% N2, 0.5
    g/L L-cysteine hydrochloride, pH 7, 7 mL, tube meat:fluid 1:4 or 5, 121°C/30 min
    and conditional 15 g/1000 mL agar. These match current provider/standalone 78
    context; embedded 413 cysteine form differs. Do not delete supported existing
    prose or call it missing.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/btu_medium.yaml",
    "field_path": "preparation_steps[2].description", "stored_value": "To make medium
    anoxic bring it to a boil, cool under 100% N2 gas atmosphere, add 0.5 g/l L-cysteine
    hydrochloride and adjust pH to 7.0. Dispense under 100% N2 gas atmosphere by filling
    7 ml medium into anoxic Hungate-type tubes (for strains demanding meat particles
    put those first into the tube (use 1 part meat particles to 4 or 5 parts fluid)).
    Autoclave at 121°C for 30 min. For agar slants use 15.0 g agar per 1000.0 ml medium.",
    "decision": "evidence_only", "rationale": "Existing prose retains 100% N2, 0.5
    g/L L-cysteine hydrochloride, pH 7, 7 mL, tube meat:fluid 1:4 or 5, 121°C/30 min
    and conditional 15 g/1000 mL agar. These match current provider/standalone 78
    context; embedded 413 cysteine form differs. Do not delete supported existing
    prose or call it missing."}]}, {"quantity_id": "q19", "topic": "Existing DSM preparation
    step 4", "source": {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413",
    "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256":
    "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator":
    "$.data.solutions[2].steps[1]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"},
    "decision": "evidence_only", "rationale": "Existing conditional post-autoclave
    supplement instruction names 1000 mL medium but omits actual supplement doses.
    Preserve it; structured, version-qualified doses remain to be added.", "layer_assessments":
    [{"path": "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path": "preparation_steps[3].description",
    "stored_value": "In some cases (as indicated in the catalogue) the addition of
    Haemin and Vitamin K1 or Vitamin K3 is necessary. Add to 1000 ml of medium after
    autoclaving:", "decision": "evidence_only", "rationale": "Existing conditional
    post-autoclave supplement instruction names 1000 mL medium but omits actual supplement
    doses. Preserve it; structured, version-qualified doses remain to be added."}]},
    {"quantity_id": "q20", "topic": "Existing DSM preparation step 5", "source": {"evidence_id":
    "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413", "raw_path":
    "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256": "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c",
    "locator": "$.data.solutions[2].steps[2]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"},
    "decision": "evidence_only", "rationale": "Existing extraction prose already retains
    15 min boiling, separate retained meat/filtrate and explicit final 1000 mL filtrate
    makeup. This is an intermediate stage, not measured final BTU volume.", "layer_assessments":
    [{"path": "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path": "preparation_steps[4].description",
    "stored_value": "Use lean beef or horse meat. Remove fat and connective tissue
    before grinding. Mix\r\nmeat, water and NaOH, then boil for 15 min with stirring.
    Cool to room temperature,\r\nskim fat off surface, and filter, retaining both
    meat particles and filtrate. To the filtrate\r\nadd water to a final volume of
    1000 ml, and then add:", "decision": "evidence_only", "rationale": "Existing extraction
    prose already retains 15 min boiling, separate retained meat/filtrate and explicit
    final 1000 mL filtrate makeup. This is an intermediate stage, not measured final
    BTU volume."}]}, {"quantity_id": "q21", "topic": "Existing DSM preparation step
    6", "source": {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413",
    "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256":
    "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator":
    "$.data.solutions[3].steps[0]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"},
    "decision": "evidence_only", "rationale": "Existing hemin preparation already
    retains 50 mg,1 mL1N NaOH and makeup 100 mL; this supports stock 0.5 g/L only.",
    "layer_assessments": [{"path": "data/normalized_yaml/bacterial/btu_medium.yaml",
    "field_path": "preparation_steps[5].description", "stored_value": "Dissolve 50
    mg haemin in 1 ml 1 N NaOH; make up to 100 ml with distilled water and filter
    sterilize. Store refrigerated.", "decision": "evidence_only", "rationale": "Existing
    hemin preparation already retains 50 mg,1 mL1N NaOH and makeup 100 mL; this supports
    stock 0.5 g/L only."}]}, {"quantity_id": "q22", "topic": "Existing DSM preparation
    step 7", "source": {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413",
    "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256":
    "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator":
    "$.data.solutions[4].steps[0]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"},
    "decision": "evidence_only", "rationale": "Existing K3 prose exactly matches current
    provider 5 mg in 1 mL95%ethanol diluted 0.05 mg/mL. Preserve current provider
    attribution; embedded 413 differs and standalone 78 states initial 5 mg/mL rather
    than a required 1 mL batch.", "layer_assessments": [{"path": "data/normalized_yaml/bacterial/btu_medium.yaml",
    "field_path": "preparation_steps[6].description", "stored_value": "Dissolve 5
    mg vitamin K3 in 1 ml 95% ethanol, dilute to 0.05 mg/ml in water and filter sterilize.
    Store refrigerated in a brown bottle.", "decision": "evidence_only", "rationale":
    "Existing K3 prose exactly matches current provider 5 mg in 1 mL95%ethanol diluted
    0.05 mg/mL. Preserve current provider attribution; embedded 413 differs and standalone
    78 states initial 5 mg/mL rather than a required 1 mL batch."}]}, {"quantity_id":
    "q23", "topic": "Existing DSM preparation step 8", "source": {"evidence_id": "api413",
    "reference": "https://mediadive.dsmz.de/rest/medium/413", "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin",
    "raw_sha256": "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c",
    "locator": "$.data.solutions[5].steps[0]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"},
    "decision": "evidence_only", "rationale": "Existing K1 prose has 0.1 mL in 20
    mL95%ethanol and matches provider/standalone 78. Embedded 413 literally labels
    K1/K3, retained as an unresolved source anomaly.", "layer_assessments": [{"path":
    "data/normalized_yaml/bacterial/btu_medium.yaml", "field_path": "preparation_steps[7].description",
    "stored_value": "Dissolve 0.1 ml of vitamin K1 in 20 ml 95% ethanol and filter
    sterilize. Store refrigerated in a brown bottle.", "decision": "evidence_only",
    "rationale": "Existing K1 prose has 0.1 mL in 20 mL95%ethanol and matches provider/standalone
    78. Embedded 413 literally labels K1/K3, retained as an unresolved source anomaly."}]},
    {"quantity_id": "q24", "topic": "Basal assembly and both-salt stock", "source":
    {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413",
    "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256":
    "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator":
    "$.data.solutions[0:2]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"}, "decision":
    "mixed", "rationale": "Primary medium 413 adds a separately defined stock to medium
    78. Current API gives 1000 mL basal and 30 mL stock; stock contains 6 g of each
    salt and 100 mL water with declared 100 mL volume. Do not treat provider primary
    volume 1000 as proof that the additive final volume is 1000 mL.", "layer_assessments":
    [{"path": "data/merge_yaml/merged/BTU_MEDIUM.yaml", "field_path": "solutions",
    "stored_value": null, "decision": "unsupported", "rationale": "Generated/copy
    or exact KOMODO variant cannot receive this generic source topology as an authenticated
    variant before accession/version reconciliation. Primary medium 413 adds a separately
    defined stock to medium 78. Current API gives 1000 mL basal and 30 mL stock; stock
    contains 6 g of each salt and 100 mL water with declared 100 mL volume. Do not
    treat provider primary volume 1000 as proof that the additive final volume is
    1000 mL.", "missing": true}, {"path": "data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale":
    "Generated/copy or exact KOMODO variant cannot receive this generic source topology
    as an authenticated variant before accession/version reconciliation. Primary medium
    413 adds a separately defined stock to medium 78. Current API gives 1000 mL basal
    and 30 mL stock; stock contains 6 g of each salt and 100 mL water with declared
    100 mL volume. Do not treat provider primary volume 1000 as proof that the additive
    final volume is 1000 mL.", "missing": true}, {"path": "data/normalized_yaml/bacterial/btu_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Create source/version-scoped stock topology while preserving existing preparation
    prose. Primary medium 413 adds a separately defined stock to medium 78. Current
    API gives 1000 mL basal and 30 mL stock; stock contains 6 g of each salt and 100
    mL water with declared 100 mL volume. Do not treat provider primary volume 1000
    as proof that the additive final volume is 1000 mL.", "missing": true}, {"path":
    "data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale":
    "Generated/copy or exact KOMODO variant cannot receive this generic source topology
    as an authenticated variant before accession/version reconciliation. Primary medium
    413 adds a separately defined stock to medium 78. Current API gives 1000 mL basal
    and 30 mL stock; stock contains 6 g of each salt and 100 mL water with declared
    100 mL volume. Do not treat provider primary volume 1000 as proof that the additive
    final volume is 1000 mL.", "missing": true}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale":
    "Generated/copy or exact KOMODO variant cannot receive this generic source topology
    as an authenticated variant before accession/version reconciliation. Primary medium
    413 adds a separately defined stock to medium 78. Current API gives 1000 mL basal
    and 30 mL stock; stock contains 6 g of each salt and 100 mL water with declared
    100 mL volume. Do not treat provider primary volume 1000 as proof that the additive
    final volume is 1000 mL.", "missing": true}, {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale":
    "Generated/copy or exact KOMODO variant cannot receive this generic source topology
    as an authenticated variant before accession/version reconciliation. Primary medium
    413 adds a separately defined stock to medium 78. Current API gives 1000 mL basal
    and 30 mL stock; stock contains 6 g of each salt and 100 mL water with declared
    100 mL volume. Do not treat provider primary volume 1000 as proof that the additive
    final volume is 1000 mL.", "missing": true}]}, {"quantity_id": "q25", "topic":
    "Hemin conditional stock and dose", "source": {"evidence_id": "dsm413", "reference":
    "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium413.pdf", "raw_path":
    "REVIEW_WORK/batch054/source01-03/dsm413.bin", "raw_sha256": "2dc547e81e376a04e46659d3d0b800d9c9ec5dbedd1abe9ffcaaa59d9bfbd27f",
    "locator": "Page1 conditional additions and Haemin solution", "accessed_at": "2026-10-28T03:59:21.850645+00:00"},
    "decision": "mixed", "rationale": "Hemin 50 mg,1 mL1NNaOH,makeup 100 mL; conditional
    10 mL stock per 1000 mL medium after autoclaving. All are distinct from final
    hemin concentration.", "layer_assessments": [{"path": "data/merge_yaml/merged/BTU_MEDIUM.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale":
    "Generated/copy or exact KOMODO variant cannot receive this generic source topology
    as an authenticated variant before accession/version reconciliation. Hemin 50
    mg,1 mL1NNaOH,makeup 100 mL; conditional 10 mL stock per 1000 mL medium after
    autoclaving. All are distinct from final hemin concentration.", "missing": true},
    {"path": "data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml", "field_path":
    "solutions", "stored_value": null, "decision": "unsupported", "rationale": "Generated/copy
    or exact KOMODO variant cannot receive this generic source topology as an authenticated
    variant before accession/version reconciliation. Hemin 50 mg,1 mL1NNaOH,makeup
    100 mL; conditional 10 mL stock per 1000 mL medium after autoclaving. All are
    distinct from final hemin concentration.", "missing": true}, {"path": "data/normalized_yaml/bacterial/btu_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Create source/version-scoped stock topology while preserving existing preparation
    prose. Hemin 50 mg,1 mL1NNaOH,makeup 100 mL; conditional 10 mL stock per 1000
    mL medium after autoclaving. All are distinct from final hemin concentration.",
    "missing": true}, {"path": "data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale":
    "Generated/copy or exact KOMODO variant cannot receive this generic source topology
    as an authenticated variant before accession/version reconciliation. Hemin 50
    mg,1 mL1NNaOH,makeup 100 mL; conditional 10 mL stock per 1000 mL medium after
    autoclaving. All are distinct from final hemin concentration.", "missing": true},
    {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale":
    "Generated/copy or exact KOMODO variant cannot receive this generic source topology
    as an authenticated variant before accession/version reconciliation. Hemin 50
    mg,1 mL1NNaOH,makeup 100 mL; conditional 10 mL stock per 1000 mL medium after
    autoclaving. All are distinct from final hemin concentration.", "missing": true},
    {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale":
    "Generated/copy or exact KOMODO variant cannot receive this generic source topology
    as an authenticated variant before accession/version reconciliation. Hemin 50
    mg,1 mL1NNaOH,makeup 100 mL; conditional 10 mL stock per 1000 mL medium after
    autoclaving. All are distinct from final hemin concentration.", "missing": true}]},
    {"quantity_id": "q26", "topic": "Vitamin alternatives and incompatible doses",
    "source": {"evidence_id": "api413", "reference": "https://mediadive.dsmz.de/rest/medium/413",
    "raw_path": "REVIEW_WORK/batch054/source01-03-extra/api413.bin", "raw_sha256":
    "50c5f8ecb692fe639c52521e6b0ab405c40b4a228545b246ca551649f372690c", "locator":
    "$.data.solutions[2].recipe[10:12], solutions[4:6]", "accessed_at": "2026-10-28T04:02:49.107482+00:00"},
    "decision": "mixed", "rationale": "Embedded DSM413 adds 0.2 mL of K1 OR K3 stock
    per 1000 mL. Standalone 78 adds 10 mL of either; current API separately saysK1=0.2
    mL andK3=10 mL. Keep all versioned evidence and alternative status; no universal
    winning dose is selected.", "layer_assessments": [{"path": "data/merge_yaml/merged/BTU_MEDIUM.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale":
    "Generated/copy or exact KOMODO variant cannot receive this generic source topology
    as an authenticated variant before accession/version reconciliation. Embedded
    DSM413 adds 0.2 mL of K1 OR K3 stock per 1000 mL. Standalone 78 adds 10 mL of
    either; current API separately saysK1=0.2 mL andK3=10 mL. Keep all versioned evidence
    and alternative status; no universal winning dose is selected.", "missing": true},
    {"path": "data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml", "field_path":
    "solutions", "stored_value": null, "decision": "unsupported", "rationale": "Generated/copy
    or exact KOMODO variant cannot receive this generic source topology as an authenticated
    variant before accession/version reconciliation. Embedded DSM413 adds 0.2 mL of
    K1 OR K3 stock per 1000 mL. Standalone 78 adds 10 mL of either; current API separately
    saysK1=0.2 mL andK3=10 mL. Keep all versioned evidence and alternative status;
    no universal winning dose is selected.", "missing": true}, {"path": "data/normalized_yaml/bacterial/btu_medium.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "add", "rationale":
    "Create source/version-scoped stock topology while preserving existing preparation
    prose. Embedded DSM413 adds 0.2 mL of K1 OR K3 stock per 1000 mL. Standalone 78
    adds 10 mL of either; current API separately saysK1=0.2 mL andK3=10 mL. Keep all
    versioned evidence and alternative status; no universal winning dose is selected.",
    "missing": true}, {"path": "data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale":
    "Generated/copy or exact KOMODO variant cannot receive this generic source topology
    as an authenticated variant before accession/version reconciliation. Embedded
    DSM413 adds 0.2 mL of K1 OR K3 stock per 1000 mL. Standalone 78 adds 10 mL of
    either; current API separately saysK1=0.2 mL andK3=10 mL. Keep all versioned evidence
    and alternative status; no universal winning dose is selected.", "missing": true},
    {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale":
    "Generated/copy or exact KOMODO variant cannot receive this generic source topology
    as an authenticated variant before accession/version reconciliation. Embedded
    DSM413 adds 0.2 mL of K1 OR K3 stock per 1000 mL. Standalone 78 adds 10 mL of
    either; current API separately saysK1=0.2 mL andK3=10 mL. Keep all versioned evidence
    and alternative status; no universal winning dose is selected.", "missing": true},
    {"path": "data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml",
    "field_path": "solutions", "stored_value": null, "decision": "unsupported", "rationale":
    "Generated/copy or exact KOMODO variant cannot receive this generic source topology
    as an authenticated variant before accession/version reconciliation. Embedded
    DSM413 adds 0.2 mL of K1 OR K3 stock per 1000 mL. Standalone 78 adds 10 mL of
    either; current API separately saysK1=0.2 mL andK3=10 mL. Keep all versioned evidence
    and alternative status; no universal winning dose is selected.", "missing": true}]},
    {"quantity_id": "q27", "topic": "Embedded 413 vitamin stock anomalies", "source":
    {"evidence_id": "dsm413", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium413.pdf",
    "raw_path": "REVIEW_WORK/batch054/source01-03/dsm413.bin", "raw_sha256": "2dc547e81e376a04e46659d3d0b800d9c9ec5dbedd1abe9ffcaaa59d9bfbd27f",
    "locator": "Page1 Vitamin K1 and Vitamin K3 subsections", "accessed_at": "2026-10-28T03:59:21.850645+00:00"},
    "decision": "unsupported", "rationale": "Literal K1 subsection names 0.1 mL K1/K3
    in 20 mL95%ethanol. Literal K3 subsection specifies 5 mg/mL in 10 mL95%ethanol.
    These differ from current provider diluted K3 and do not establish a universal
    receiving-medium dose. No percentage basis or density is invented.", "layer_assessments":
    []}, {"quantity_id": "q28", "topic": "Standalone 78 strain-specific exclusion",
    "source": {"evidence_id": "dsm78", "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78.pdf",
    "raw_path": "REVIEW_WORK/batch054/source01-03/dsm78.bin", "raw_sha256": "4c39b6d8f2e8b62597bca6c6411fac0a850264a2f0410d8e2f83613fe400b4a0",
    "locator": "Final DSM21650 exception", "accessed_at": "2026-10-28T03:59:21.867329+00:00"},
    "decision": "evidence_only", "rationale": "pH 8.5 is stated only for DSM21650
    in standalone 78; this is excluded context and not transferred to the selected
    BTU formulation or DSM20703/6644 variants.", "layer_assessments": []}]'
- assessment_id: a3
  area: grounding
  topic: Current ontology and MIM correspondence
  outcome: supported
  summary: The grounding inventory enumerates every asserted identifier and exact
    preferred label. Current catalog joins establish present correspondence only;
    unmapped mixtures are not assigned invented chemical identities.
  target_ids:
  - CultureMech:005240
  evidence_ids:
  - grounding
- assessment_id: a4
  area: provenance
  topic: History and evidence scope
  outcome: supported
  summary: Complete owner and target histories were read. Current source bytes and
    inspected code are independent evidence; historical timestamps remain historical
    claims unless an exact cited raw digest is recovered.
  target_ids:
  - CultureMech:005240
  evidence_ids:
  - history
  - scalars
- assessment_id: a5
  area: scope
  topic: Growth and taxonomic evidence
  outcome: unknown
  summary: Generic cultivation applications and bacterial filing are not strain-level
    growth evidence. No organism-specific growth, temperature or atmosphere is inferred
    from names or source catalog identifiers.
  target_ids:
  - CultureMech:005240
  evidence_ids:
  - local-target
- assessment_id: a6
  area: schema
  topic: Canonical diagnostics
  outcome: supported
  summary: All four original canonical diagnostics passed. Reference checks were zero;
    structural and term diagnostics do not establish formulation accuracy.
  target_ids:
  - CultureMech:005240
  evidence_ids:
  - validate-schema
  - validate-strict
  - validate-terms
  - validate-references
findings:
- finding_id: f1
  issue_key: culturemech-005240-stock-compositions-and-final-medium-quantities-are-flattened
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: Stock compositions and final-medium quantities are flattened
  description: All six local records contain the same fourteen direct concentrations,
    combining basal precursor amounts, two 60 g/L stock salts,0.5 g/L hemin stock
    and 0.05 g/L diluted K3 stock. No solutions topology is present. Current API/primary
    evidence separates these stages; current importer already implements stock separation.
  target_ids:
  - CultureMech:005240
  field_paths:
  - ingredients
  evidence_ids:
  - local-target
  - owner-2
  - api413
  - dsm413
  - writer-mediadive
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/btu_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f2
  issue_key: culturemech-005240-liquid-units-and-incompatible-stock-values-were-combined
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Liquid units and incompatible stock values were combined
  description: NaOH26 G_PER_L comes from 25 mL and 1 mL1N solution inputs at different
    stages. Ethanol 959.5 G_PER_L combines 9.5 and 950 provider values from two stocks;
    K1 0.1 G_PER_L uses a source 0.1 mL amount as a mass rate. Numeric equality to
    provider fields does not repair these dimensions or stage joins.
  target_ids:
  - CultureMech:005240
  field_paths:
  - ingredients[3].concentration
  - ingredients[12].concentration
  - ingredients[13].concentration
  evidence_ids:
  - api413
  - dsm413
  - writer-cleanup
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/btu_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f3
  issue_key: culturemech-005240-basal-denominator-and-conditional-solids-need-source-reconciliation
  category: quantity
  severity: major
  status: open
  certainty: confirmed
  title: Basal denominator and conditional solids need source reconciliation
  description: Primary 413 uses 500 g beef as an extraction precursor and makes filtrate
    up to 1000 mL before adding 30 g Casitone,5 g yeast extract,5 g phosphate and
    1 mg resazurin. Provider 1025 mL rates match local digits but are not an independently
    authenticated final BTU basis. Primary agar is explicitly 15 g per 1000 mL for
    slants; local 14.6341 derives from the other denominator.
  target_ids:
  - CultureMech:005240
  field_paths:
  - ingredients[2].concentration
  - ingredients[4].concentration
  - ingredients[5].concentration
  - ingredients[6].concentration
  - ingredients[7].concentration
  - ingredients[9].concentration
  - physical_state
  evidence_ids:
  - api413
  - dsm413
  - dsm413-visual-1
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/btu_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f4
  issue_key: culturemech-005240-embedded413-and-standalone78-vitamin-cysteine-versions-conflict
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Embedded 413 and standalone 78 vitamin/cysteine versions conflict
  description: Embedded 413 says 0.5 g/L cysteine and 0.2 mL of either vitamin stock.
    Standalone 78 names L-cysteine hydrochloride and 10 mL of either vitamin; current
    API combines K1 0.2 mL withK3 10 mL and a diluted K3 stock. Local 0.05 g/L equals
    the newer 0.05 mg/mL stock, but is not universal final concentration. Embedded
    K1/K3 wording and 5 mg/mL K3 in 10 mL ethanol are literal anomalies.
  target_ids:
  - CultureMech:005240
  field_paths:
  - ingredients[8]
  - ingredients[11]
  - ingredients[13]
  evidence_ids:
  - dsm413
  - dsm78
  - api413
  - dsm413-visual-1
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/btu_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f5
  issue_key: culturemech-005240-copied-signatures-do-not-authenticate-named-komodo-variants
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Copied signatures do not authenticate named KOMODO variants
  description: The merged record includes a named formate-to-fumarate replacement
    and DSM20703/6644 modified media. Histories say DSM413 ingredients were copied
    into them, and identical local signatures underpin duplicate links. Exact variant
    endpoints returned 403. DSM413 both-salt formulation cannot establish a replacement
    variant or strain-specific growth.
  target_ids:
  - CultureMech:005240
  field_paths:
  - merged_from
  - synonyms
  - variant_children
  - parent_media
  - variant_modifications
  evidence_ids:
  - local-target
  - owner-3
  - owner-4
  - owner-5
  - dsm413
  - komodo413fumarate
  - komodo41320703
  - komodo4136644
  - writer-formulation
  rule_id: source-stage-or-identity
  native_severity: P2
  normalization_reason: 'Major: alters source identity, quantitative interpretation
    or usable source support; canonical schema success cannot authenticate these claims.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/btu_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f6
  issue_key: culturemech-005240-legacy-cysteine-identifier-lacks-a-current-catalog-row
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Legacy cysteine identifier lacks a current catalog row
  description: The asserted MediaIngredientMech:000223 is absent from the current
    packaged label index. CHEBI:91247 currently denotes L-cysteine hydrochloride,
    but that does not resolve the embedded 413 form ambiguity or establish historical
    invalidity of the legacy identifier.
  target_ids:
  - CultureMech:005240
  field_paths:
  - ingredients[8].mediaingredientmech_term
  evidence_ids:
  - local-target
  - grounding
  - chebi91247
  rule_id: current-legacy-catalog-scope
  native_severity: P3
  normalization_reason: 'Minor: bounded metadata or traceability defect without establishing
    a new formulation.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/btu_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
- finding_id: f7
  issue_key: culturemech-005240-malformed-import-timestamps-and-stale-generated-preparation-obscure-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Malformed import timestamps and stale generated preparation obscure provenance
  description: KOMODO import history retains an .fZ timestamp. The maintained DSM
    owner already carries eight preparation steps, while generated/other contributors
    do not. Preserve that existing work and qualify its version; absence from generated
    output is not evidence that no owner preparation was ever curated.
  target_ids:
  - CultureMech:005240
  field_paths:
  - curation_history
  evidence_ids:
  - local-target
  - owner-1
  - owner-2
  - history
  rule_id: source-stage-or-identity
  native_severity: P3
  normalization_reason: 'Minor: bounded metadata or traceability defect without establishing
    a new formulation.'
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/btu_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml
    role: maintained contributor
  ownership_note: The selected merge is generated. Curate the maintained contributor
    where still needed, then regenerate with the current compatible-formulation workflow.
actions:
- action_id: action1
  description: Curate explicit stock/assembly topology in the DSM owner with source
    version and conditional doses retained. Reconcile exact KOMODO variants before
    transferring any recipe. Regenerate compatible outputs and retain current importer
    guards; do not patch generated YAML directly.
  finding_ids:
  - f1
  target_ids:
  - CultureMech:005240
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/btu_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action2
  description: Restore separate liquid input dimensions and stock scopes from exact
    source records. Preserve old summed values as history; do not sum across stock
    denominators or invent ethanol density/percentage basis.
  finding_ids:
  - f2
  target_ids:
  - CultureMech:005240
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/btu_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action3
  description: Preserve precursor, filtrate makeup and subsequent batch additions
    separately. Resolve the provider/primary denominator conflict and conditional
    agar stage before assigning final-medium rates or universal physical-state claims.
  finding_ids:
  - f3
  target_ids:
  - CultureMech:005240
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/btu_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action4
  description: Represent or explicitly document the exact source versions without
    choosing the convenient dose/form. Keep existing DSM preparation prose and attach
    versioned source support; resolve missing structured dose alternatives separately.
  finding_ids:
  - f4
  target_ids:
  - CultureMech:005240
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/btu_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action5
  description: Keep exact source accessions and existing history, but qualify or defer
    source-duplicate claims until each variant is authenticated. Do not collapse variants
    solely because copied local signatures match.
  finding_ids:
  - f5
  target_ids:
  - CultureMech:005240
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/btu_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action6
  description: Document the current legacy-link limit and reconcile source form first.
    Do not guess a replacement MIM identifier or claim the historical identifier never
    existed.
  finding_ids:
  - f6
  target_ids:
  - CultureMech:005240
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/btu_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
- action_id: action7
  description: Preserve original history with a valid-time provenance qualification
    and regenerate only after source/version reconciliation. Retain the DSM owner
    preparation rather than redundantly adding it as entirely missing.
  finding_ids:
  - f7
  target_ids:
  - CultureMech:005240
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/btu_medium.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/btu_medium_replace_formiate_with_fumarate.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_413_modified_for_dsm_20703.yaml
    role: maintained contributor
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/medium_413_modified_for_dsm_6644.yaml
    role: maintained contributor
  ownership_note: Preserve source-specific variants and existing owner repairs; do
    not directly edit the generated record.
  acceptance_checks:
  - Exact owner/source scopes and all quantity decisions are reconciled.
  - Regenerated target retains claim-level evidence and passes the four canonical
    diagnostics.
  generator: src/culturemech/merge/merger.py
limitations:
- All four exact KOMODO endpoints returned HTTP403. Generic DSM evidence does not
  authenticate the replacement or strain-specific variants.
- Current provider values are directly verified, but they conflict with primary source
  stage/volume statements. No final BTU rate is guessed where the source basis is
  unresolved.
- No taxonomy or strain growth claim is inferred from DSM accessions, generic applications,
  anaerobic notes or conditional source instructions.
- Current code inspection establishes existing safeguards only; it does not reconstruct
  which historical code executed. Current MIM absence is not proof of historical identifier
  invalidity.
notes:
- Fresh review; historical lost snapshots were not reconstructed. All inspected source
  files remain unchanged.
- No formal review validation/save, Git mutation or publication was performed by this
  author.
```
