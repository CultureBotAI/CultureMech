# Ingredient Concentration Review

- Record: data/merge_yaml/merged/columbia_agar_with_sheep_blood__5abbf9e3.yaml
- ID: CultureMech:008653
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: a5b17de70741cfb730b76be8dfa367f13f86f535ecff8ada05f265439795a94b
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/1
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/TOGO_M2508_Columbia_agar_with_sheep_blood.yaml
- data/normalized_yaml/bacterial/columbia_agar_with_sheep_blood.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Columbia Agar with 5% Sheep Blood (BD-BBL) | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://togomedium.org/medium/M2062
- https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1365

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
