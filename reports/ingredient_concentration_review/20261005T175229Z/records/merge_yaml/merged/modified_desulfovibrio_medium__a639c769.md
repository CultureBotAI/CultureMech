# Ingredient Concentration Review

- Record: data/merge_yaml/merged/modified_desulfovibrio_medium__a639c769.yaml
- ID: CultureMech:010288
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: dac0b315366907ff7b0a4ae42717a6e50a0e939240180e1f3a9608cd57b7939d
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/2
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/TOGO_M870_Modified_Desulfovibrio_Medium.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Beef extract (BD-Difco) | {"value": "3", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[0].concentration / DESULFOVIBRIO MEDIUM (see Medium [M384]) | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://togomedium.org/medium/M870
- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=834

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
