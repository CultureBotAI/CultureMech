# Ingredient Concentration Review

- Record: data/normalized_yaml/bacterial/TOGO_M407_Horikoshi-I_Medium_With_2_NaCl.yaml
- ID: CultureMech:009791
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: af5ef516de75f52f3a33a114312a0e3ffb3f436af6a1aff39c1c92094c22e3f0
- Layer: normalized
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/2
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/TOGO_M407_Horikoshi-I_Medium_With_2_NaCl.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / NaCl | {"value": "20", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[0].concentration / Horikoshi-I medium | {"value": "1000", "unit": "ML_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://togomedium.org/medium/M174
- https://togomedium.org/medium/M407
- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=181
- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=409

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
