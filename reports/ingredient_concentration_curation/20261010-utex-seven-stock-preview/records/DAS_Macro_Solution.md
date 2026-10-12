# UTEX Stock Source Triage

- Record: data/normalized_yaml/bacterial/DAS_Macro_Solution.yaml
- ID: CultureMech:015444
- Reviewed commit: f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f
- Record SHA256: 2dd1cff4bf6100645cea83a4f409fc6fd9ad6d1ada7de09ea1acd8462734bbb7
- State: preview; no authoritative edits applied

Source: [DAS Macro Solution Recipe](https://utex.org/products/das-macro-solution). HTTP-200 capture pinned in the source ledger; unknown bibliographic fields are not invented.

| Claim / ingredient | Existing amount | Status | Source and decision |
| --- | --- | --- | --- |
| composition[0].concentration / Sodium nitrate (0.70 M stock) | {"value": "25.0", "unit": "PERCENT_V_V"} | conflict | {"reference": "https://utex.org/products/das-macro-solution", "snippet": "10 mL/3 L", "basis_snippet": "For 40 mL total", "source_component": "NaNO3*autoclave before adding*(Fisher BP360)", "locator": "formulation table row 1; Amount column and volume heading", "calculation": "10 mL / 40 mL * 100 = 25.0% prepared-stock volume fraction; not pure-solute percent and not final DAS concentration.", "reason": "The quantity describes a prepared 0.70 M stock volume fraction, not pure sodium nitrate volume percent. Review composition-to-stock representation before approval.", "action_taken": "none; read-only source triage"} |
| composition[1].concentration / Disodium phosphate heptahydrate (0.02 M stock) | {"value": "75.0", "unit": "PERCENT_V_V"} | conflict | {"reference": "https://utex.org/products/das-macro-solution", "snippet": "30 mL/3 L", "basis_snippet": "For 40 mL total", "source_component": "Na2HPO4\u20227H2O*autoclave before adding*(Sigma S 9390)", "locator": "formulation table row 2; Amount column and volume heading", "calculation": "30 mL / 40 mL * 100 = 75.0% prepared-stock volume fraction; not pure-solute percent and not final DAS concentration.", "reason": "The quantity describes a prepared 0.02 M heptahydrate stock volume fraction, not pure phosphate volume percent. The current anhydrous grounding also requires supplied-form review.", "action_taken": "none; read-only source triage"} |

## Remaining Work

- Keep the 40 mL combined-stock preparation separate from each component stock strength and the 3 L receiving DAS medium.
- Source explicitly says autoclave the two component stocks before addition. No final-medium concentration is added by this triage.

Identity/role/growth/classification claims are not generally certified by this concentration triage. The baseline checks are in the batch validation receipt. No canonical follow-up coverage increment is counted.
