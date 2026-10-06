# Ingredient Concentration Review

- Record: data/merge_yaml/merged/columbia_blood_agar_with_5_sheep_blood.yaml
- ID: CultureMech:009063
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: f3b7af5c97270a4b1ea560a88c40f3c66799e2a036fe50c66d71cf249223122b
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/2
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/TOGO_M248_Columbia_Blood_Agar_With_5_Sheep_Blood.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Columbia blood agar base (Oxoid CM331) | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / sterile defibrinated sheep blood | {"value": "variable", "unit": "VARIABLE"} | missing_attached_evidence; VARIABLE_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://togomedium.org/medium/M248
- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=256

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
