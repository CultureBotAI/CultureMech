# Ingredient Concentration Review

- Record: data/normalized_yaml/algae/note_on_biphasic_soilwater_media_20081216.yaml
- ID: CultureMech:000205
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: db18fa1b24797fe74abd86b80428b070e625408e9476e8c95420d6529242155d
- Layer: normalized
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/2
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/algae/note_on_biphasic_soilwater_media_20081216.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Garden soil | {"value": "1", "unit": "VARIABLE"} | missing_attached_evidence; VARIABLE_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Deionized or distilled water | {"value": "1", "unit": "VARIABLE"} | missing_attached_evidence; VARIABLE_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- http://sagdb.uni-goettingen.de/culture_media/Note_on_biphasic_soilwater_media_20081216.pdf
- https://sagdb.uni-goettingen.de/culture_media/Note_on_biphasic_soilwater_media_20081216.pdf

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
