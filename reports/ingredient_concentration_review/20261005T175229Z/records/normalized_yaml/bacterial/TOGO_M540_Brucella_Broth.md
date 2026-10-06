# Ingredient Concentration Review

- Record: data/normalized_yaml/bacterial/TOGO_M540_Brucella_Broth.yaml
- ID: CultureMech:009933
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: f292dee86d67451cf7e1cc227e807733d9c3835a9b6b39ad191ef041b809dc10
- Layer: normalized
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/8
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/TOGO_M540_Brucella_Broth.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Distilled water | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Yeast extract | {"value": "2", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / NaCl | {"value": "5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Glucose | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / NaHSO3 | {"value": "0.1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / Pancreatic digest of casein | {"value": "10", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[6].concentration / Peptic digest of animal tissue | {"value": "10", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| variants[0].modifications / brucella_broth_fbs_h2o2_helicobacter_pylori | ["Supplement Brucella broth with 10% fetal bovine serum.", "Add hydrogen peroxide at sublethal concentrations, with maximum growth stimulation reported at 3.5 mM H2O2.", "Incubate microaerobically at 37 C with shaking; source measured OD620 and viable CFU after 24 h."] | incomplete_or_nonqualifying_attached_evidence; VARIANT_TEXT_REQUIRES_SOURCE_REVIEW | unsupported; not_performed | unknown | [{"reference": "PMID:10609610", "supports": "SUPPORT", "snippet": "enhanced the growth of Helicobacter pylori in Brucella broth supplemented with 10% fetal bovine serum (BB/FBS)", "explanation": "The source uses the same Brucella broth basal formulation, supplemented with fetal bovine serum and hydrogen peroxide, to measure Helicobacter pylori OMU89-362 growth."}] |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- PMID:10609610
- https://togomedium.org/medium/M540
- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=538

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
