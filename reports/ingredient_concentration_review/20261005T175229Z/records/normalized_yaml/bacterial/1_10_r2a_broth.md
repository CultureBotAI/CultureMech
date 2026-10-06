# Ingredient Concentration Review

- Record: data/normalized_yaml/bacterial/1_10_r2a_broth.yaml
- ID: CultureMech:003150
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 6ac0bb531f3881cf99448c0f9b5cb72cdb39dd926bc4a86257d013380ccdc9cf
- Layer: normalized
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 2/2
- Verdict: all listed claims source-checked; evidence not applied
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/1_10_r2a_broth.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / R2A broth (DAIGO) (Nihon Pharm. Co.) | {"value": "0.32", "unit": "G_PER_L"} | missing_attached_evidence;  | evidence_only; inspected_amount_and_basis | {"value": "0.32", "unit": "G_PER_L"} | [{"reference": "https://www.bacmedia.dsmz.de/pdf/J805", "snippet": "R2A Broth (DAIGO) (Nihon Pharm. Co.) 0.32 g", "locator": "Page 1, broth row and final-volume heading", "calculation": "0.32 g / 1 L = 0.32 g/L.", "explanation": "Existing amount is supported; attach ingredient-level reference and snippet rather than changing the number. Additional exact excerpt: Final volume: 1000 ml"}] |
| ingredients[1].concentration / Distilled water | {"value": "1.0", "unit": "L"} | missing_attached_evidence;  | evidence_only; inspected_amount_and_basis | {"value": "1.0", "unit": "L"} | [{"reference": "https://www.bacmedia.dsmz.de/pdf/J805", "snippet": "Distilled water 1000.00 ml", "locator": "Page 1, water row", "calculation": "1000 ml / 1000 = 1 L; retain volume unit L, not mass concentration.", "explanation": "Amount and volume representation are supported. Ingredient-level reference and snippet are missing; no numeric correction is needed."}] |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=805
- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=839

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
