# Ingredient Concentration Review

- Record: data/merge_yaml/merged/Distilled_Water.yaml
- ID: CultureMech:010087
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: cf378e1685dee4435332eb1852c19b5914954696827b2dcbe9d61d43a2b617ca
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/1
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/TOGO_M682_Distilled_Water.yaml
- data/normalized_yaml/bacterial/distilled_water.yaml
- data/normalized_yaml/bacterial/togo_medium_m1444.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Distilled water | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://togomedium.org/medium/M682
- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=664

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
