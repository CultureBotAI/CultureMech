# Ingredient Concentration Review

- Record: data/normalized_yaml/bacterial/TOGO_M523_Xylanobacter_Medium.yaml
- ID: CultureMech:009915
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 330224842fe64147ef2c9291c6e8f1e574d72cb00a0002e309331423817ebc23
- Layer: normalized
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/1
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/TOGO_M523_Xylanobacter_Medium.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| solutions[0].concentration / PY4S Agar | {"value": "1000", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://togomedium.org/medium/M357
- https://togomedium.org/medium/M523
- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=363
- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=522

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
