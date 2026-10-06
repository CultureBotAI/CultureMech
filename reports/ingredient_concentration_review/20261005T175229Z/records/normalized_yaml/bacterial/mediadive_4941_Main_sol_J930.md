# Ingredient Concentration Review

- Record: data/normalized_yaml/bacterial/mediadive_4941_Main_sol_J930.yaml
- ID: CultureMech:013867
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 9ed5513013c701e6405c9b78d2902e9f04a9c11b2366e8c2e72b3b952da2e8c5
- Layer: normalized
- Record kind: SOLUTION
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/3
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/mediadive_4941_Main_sol_J930.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| composition[0].concentration / Leibovitz's L-15 medium | {"value": "1.0", "unit": "L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| composition[1].concentration / Fetal bovine serum | {"value": "100.0", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| composition[2].concentration / NaCl | {"value": "15.0", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://mediadive.dsmz.de/medium/J930
- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=930

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
