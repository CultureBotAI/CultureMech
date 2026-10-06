# Ingredient Concentration Review

- Record: data/normalized_yaml/bacterial/marine_agar_2216_with_5_nacl.yaml
- ID: CultureMech:010161
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: cc0a29f67d00833bdf150c04226768ab9d7caac2b594126f4c1a6a3195e256cb
- Layer: normalized
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/2
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/marine_agar_2216_with_5_nacl.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / NaCl | {"value": "50", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[0].concentration / Marine agar 2216 | {"value": "1000", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://togomedium.org/medium/M110
- https://togomedium.org/medium/M755
- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=118
- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=732

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
