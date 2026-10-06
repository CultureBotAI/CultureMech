# Ingredient Concentration Review

- Record: data/normalized_yaml/bacterial/TOGO_M1238_Inorganic_Salts-Starch_Agar_ISP-4_With_5_NaCl.yaml
- ID: CultureMech:007767
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 3e5bb3f9dc7b882e0980970e1012098c51957661535bc59ab945752a04469925
- Layer: normalized
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/2
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/TOGO_M1238_Inorganic_Salts-Starch_Agar_ISP-4_With_5_NaCl.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / NaCl | {"value": "50", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[0].concentration / Inorganic Salts-Starch Agar (ISP-4) | {"value": "1000", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://togomedium.org/medium/M1238
- https://togomedium.org/medium/M50
- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1156
- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=58

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
