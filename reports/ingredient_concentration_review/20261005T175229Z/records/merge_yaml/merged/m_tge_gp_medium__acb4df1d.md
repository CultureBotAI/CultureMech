# Ingredient Concentration Review

- Record: data/merge_yaml/merged/m_tge_gp_medium__acb4df1d.yaml
- ID: CultureMech:003197
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: bbfe9f1fc9bc3beda6c662935e8a96e7d246d866bbe2868c34a1702f5cf5896c
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/1
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/TOGO_M828_m_TGE_Broth_Medium.yaml
- data/normalized_yaml/bacterial/TOGO_M829_m_TGE_Broth_Medium.yaml
- data/normalized_yaml/bacterial/TOGO_M887_m_TGE-GP_Medium.yaml
- data/normalized_yaml/bacterial/m_tge_broth_medium.yaml
- data/normalized_yaml/bacterial/m_tge_gp_medium.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Bacto m TGE broth | {"value": "18", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=851

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
