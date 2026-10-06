# Ingredient Concentration Review

- Record: data/normalized_yaml/bacterial/TOGO_M957_R2A_Agar_With_1_NaCl.yaml
- ID: CultureMech:010381
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: d951f776572dee5fd661bd43cad7f6367ab73b8a7a4778f155857f9c5cfebe0f
- Layer: normalized
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/3
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/TOGO_M957_R2A_Agar_With_1_NaCl.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Distilled water | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / NaCl | {"value": "10", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / R2A agar (DB-Difco) | {"value": "18.2", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://togomedium.org/medium/M957
- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=912

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
