# Ingredient Concentration Review

- Record: data/normalized_yaml/bacterial/TOGO_M358_PY4SR_Agar.yaml
- ID: CultureMech:009738
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: a96edc8ab14cbdf046e4085d5d87561524d97fd41b61fad6d18f46c4e8dea5d4
- Layer: normalized
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/3
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/TOGO_M358_PY4SR_Agar.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| solutions[0].concentration / Plant residue extract | {"value": "50.0", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[0].composition[0].concentration / Rice straw | {"value": "variable", "unit": "VARIABLE"} | missing_attached_evidence; VARIABLE_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[0].composition[1].concentration / Distilled water | {"value": "variable", "unit": "VARIABLE"} | missing_attached_evidence; VARIABLE_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://togomedium.org/medium/M358
- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=363
- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=364

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
