# Ingredient Concentration Review

- Record: data/merge_yaml/merged/Brucella_albimi_Broth.yaml
- ID: CultureMech:008874
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: e716595f72c7260b503bb01fd6633926a636a0f4fc1c9b417ab78b4a7c17fcaa
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/2
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/brucella_albimi_broth.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / DI Water | {"value": "1000", "unit": "G_PER_L"} | missing_attached_evidence; PLAUSIBILITY_WATER_AS_VOLUME | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Brucella Broth (BD 211088) | {"value": "28", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://togomedium.org/medium/M2288
- https://www.atcc.org/~/media/F163104383194581BB0A1890306A732B.ashx

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
