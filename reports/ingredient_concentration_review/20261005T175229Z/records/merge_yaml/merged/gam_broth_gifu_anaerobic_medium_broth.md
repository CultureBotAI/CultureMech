# Ingredient Concentration Review

- Record: data/merge_yaml/merged/gam_broth_gifu_anaerobic_medium_broth.yaml
- ID: CultureMech:015347
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: baa206fd923c05085820013ddec891965ce44578e588a98b057626d6c9d1716c
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/1
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/specialized/gam_broth_gifu_anaerobic_medium_broth.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / GAM Broth powder | {"value": "59", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1713.pdf

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
