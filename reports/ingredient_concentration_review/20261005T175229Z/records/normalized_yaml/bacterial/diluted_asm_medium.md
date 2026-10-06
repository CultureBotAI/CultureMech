# Ingredient Concentration Review

- Record: data/normalized_yaml/bacterial/diluted_asm_medium.yaml
- ID: CultureMech:003160
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: c610f9bc44d69ca1ba4803fece2b6291d2b906f3ef7bc401d9562ef8cb8f8c46
- Layer: normalized
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/1
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/diluted_asm_medium.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| solutions[0].concentration / Acidic Diluted ASM Medium | {"value": "1000", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://togomedium.org/medium/M850
- https://togomedium.org/medium/M851
- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=815
- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=816

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
