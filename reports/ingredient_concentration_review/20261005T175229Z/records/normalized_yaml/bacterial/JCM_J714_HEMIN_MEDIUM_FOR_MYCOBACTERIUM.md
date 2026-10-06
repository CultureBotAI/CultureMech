# Ingredient Concentration Review

- Record: data/normalized_yaml/bacterial/JCM_J714_HEMIN_MEDIUM_FOR_MYCOBACTERIUM.yaml
- ID: CultureMech:003061
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: c5e9f35cc71349e809a675d003ac1427d568b4e220232349515f9bb4e06f1e2d
- Layer: normalized
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/5
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/JCM_J714_HEMIN_MEDIUM_FOR_MYCOBACTERIUM.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Middlebrook 7H10 agar (BD-Difco) | {"value": "19", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Glycerol | {"value": "5", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Distilled water | {"value": "895", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Middlebrook OADC Enrichment (BD-BBL) | {"value": "100", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / Hemin | {"value": "60", "unit": "MICROMOLAR"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=386
- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=714

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
