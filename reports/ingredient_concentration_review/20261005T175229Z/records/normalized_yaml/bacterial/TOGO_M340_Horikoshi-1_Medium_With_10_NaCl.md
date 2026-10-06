# Ingredient Concentration Review

- Record: data/normalized_yaml/bacterial/TOGO_M340_Horikoshi-1_Medium_With_10_NaCl.yaml
- ID: CultureMech:009719
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 298c06f9ecdd6c1035630e860ccf4bde9211106ba2a425b74fe8108166d618bd
- Layer: normalized
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/2
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/TOGO_M340_Horikoshi-1_Medium_With_10_NaCl.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / NaCl | {"value": "100", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[0].concentration / Horikoshi-I medium | {"value": "1000", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://togomedium.org/medium/M174
- https://togomedium.org/medium/M340
- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=181
- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=345

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
