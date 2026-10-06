# Ingredient Concentration Review

- Record: data/merge_yaml/merged/acidiphilium_medium__9ab0ce72.yaml
- ID: CultureMech:001368
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: d34dbe257de80551784663080af2ceaf02d79be805ce924caa46b21310a46075
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/7
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/JCM_J129_ACIDIPHILIUM_MEDIUM.yaml
- data/normalized_yaml/bacterial/KOMODO_269_ACIDIPHILIUM_medium.yaml
- data/normalized_yaml/bacterial/TOGO_M2997_Acidiphilium_Medium.yaml
- data/normalized_yaml/bacterial/TOGO_M2998_Acidiphilium_Medium.yaml
- data/normalized_yaml/bacterial/acidiphilium_medium.yaml
- data/normalized_yaml/bacterial/medium_269_modified_for_dsm_11237.yaml
- data/normalized_yaml/bacterial/medium_269_modified_for_dsm_11244.yaml
- data/normalized_yaml/bacterial/medium_269_modified_for_dsm_11245.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / (NH4)2SO4 | {"value": "2", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / KCl | {"value": "0.1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / K2HPO4 | {"value": "0.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / MgSO4 x 7 H2O | {"value": "0.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / Yeast extract | {"value": "0.3", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / D-Glucose | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| variants[0].modifications / aluminum_sulfate_stress_acidiphilium_cryptum | ["Maintain pH 3.0.", "Add aluminum sulfate at the stress concentration reported by the source study.", "Use Acidiphilium cryptum as the target organism."] | incomplete_or_nonqualifying_attached_evidence; VARIANT_TEXT_REQUIRES_SOURCE_REVIEW | unsupported; not_performed | unknown | [{"reference": "PMID:12420179", "supports": "SUPPORT", "snippet": "with a doubling time of 7.6 h, as compared to 5.2 h of growth without aluminum", "explanation": "Literature evidence supports modeling the aluminum sulfate growth condition as a variant of the parent Acidiphilium Medium record."}] |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium269.pdf

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
