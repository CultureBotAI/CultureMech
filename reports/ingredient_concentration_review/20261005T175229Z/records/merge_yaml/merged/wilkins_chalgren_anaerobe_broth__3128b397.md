# Ingredient Concentration Review

- Record: data/merge_yaml/merged/wilkins_chalgren_anaerobe_broth__3128b397.yaml
- ID: CultureMech:001439
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: fdd014b3c984d643b6c13025deb326458c68f2ddb240aecff964d3a82497a090
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/3
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/TOGO_M2586_Wilkins-Chalgren_Anaerobe_Broth.yaml
- data/normalized_yaml/bacterial/for_dsm_14204_dsm_14205_dsm_14206_dsm_14207_dsm_14924_dsm_15176_dsm_15243_dsm_15248_dsm_15480_dsm_15481_dsm_15498_dsm_15567_dsm_15692_dsm_17763_and_dsm_22608.yaml
- data/normalized_yaml/bacterial/for_dsm_14428.yaml
- data/normalized_yaml/bacterial/for_dsm_23669.yaml
- data/normalized_yaml/bacterial/medium_339_modified_for_dsm_12679.yaml
- data/normalized_yaml/bacterial/medium_339_modified_for_dsm_12858.yaml
- data/normalized_yaml/bacterial/medium_339_modified_for_dsm_19450.yaml
- data/normalized_yaml/bacterial/medium_339_modified_for_dsm_22006.yaml
- data/normalized_yaml/bacterial/medium_339_modified_for_dsm_5676.yaml
- data/normalized_yaml/bacterial/medium_339_modified_for_dsm_6011.yaml
- data/normalized_yaml/bacterial/medium_339_modified_for_dsm_6400.yaml
- data/normalized_yaml/bacterial/wilkins_chalgren_anaerobe_broth.yaml
- data/normalized_yaml/bacterial/wilkins_chalgren_anaerobe_broth_oxoid_cm_643.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / dehydrated Wilkins-Chalgren medium | {"value": "33", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Sodium resazurin | {"value": "0.0005", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / L-Cysteine HCl | {"value": "0.3", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium339.pdf

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
