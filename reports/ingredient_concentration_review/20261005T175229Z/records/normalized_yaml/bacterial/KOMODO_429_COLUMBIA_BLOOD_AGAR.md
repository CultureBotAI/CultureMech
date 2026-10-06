# Ingredient Concentration Review

- Record: data/normalized_yaml/bacterial/KOMODO_429_COLUMBIA_BLOOD_AGAR.yaml
- ID: CultureMech:005268
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 83725a42c8a74ff8eff0b5710926f709ff1d68e9b859224ba81db186704d08cc
- Layer: normalized
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/16
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/KOMODO_429_COLUMBIA_BLOOD_AGAR.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Columbia agar base | {"value": "1000", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Horse blood | {"value": "40", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Casein peptone | {"value": "17", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Soy peptone | {"value": "3", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / D(+)-Glucose | {"value": "2.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / NaCl | {"value": "5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[6].concentration / K2HPO4 | {"value": "2.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[7].concentration / Calf brains | {"value": "variable", "unit": "VARIABLE"} | missing_attached_evidence; VARIABLE_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[8].concentration / Beef heart | {"value": "variable", "unit": "VARIABLE"} | missing_attached_evidence; VARIABLE_REQUIRES_SOURCE | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[9].concentration / Proteose peptone | {"value": "10.0", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[10].concentration / Dextrose | {"value": "2.0", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[11].concentration / Sodium chloride | {"value": "5.0", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[12].concentration / Disodium phosphate | {"value": "2.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[13].concentration / Peptone | {"value": "5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[14].concentration / Meat extract | {"value": "3", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| variants[0].modifications / columbia_blood_agar_staphylococcus_saccharolyticus_anaerobic | ["BacDive DSMZ Medium 693 specifies Columbia agar base with 50 g/L defibrinated sheep blood; the local parent record contains a Columbia blood agar base with horse blood at 40 g/L.", "Incubate anaerobically or under reduced oxygen at 37 C for this anaerobic organism."] | incomplete_or_nonqualifying_attached_evidence; VARIANT_TEXT_REQUIRES_SOURCE_REVIEW | unsupported; not_performed | unknown | [{"reference": "PMID:7077295", "supports": "SUPPORT", "snippet": "The highest bacterial counts were obtained on Columbia blood agar incubated anaerobically.", "explanation": "The primary literature reports quantitative culture of Peptococcus saccharolyticus strains, now Staphylococcus saccharolyticus, on Columbia blood agar under anaerobic incubation."}, {"reference": "https://bacdive.dsmz.de/strain/14567", "supports": "SUPPORT", "explanation": "BacDive identifies Staphylococcus saccharolyticus S1 as the type strain with DSM 20359, ATCC 14953, JCM 1768, and NCTC 11807 aliases; its cultivation data list Columbia Blood Medium with positive growth at 37 C."}] |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://microbenotes.com/brain-heart-infusion-bhi-agar/

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
