# Ingredient Concentration Review

- Record: data/normalized_yaml/bacterial/tryptic_soy_broth.yaml
- ID: CultureMech:008226
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 569018dc43baf552de065e7fbb7a547f5c10dcc0a308a0d9cb49f0a0a5a34040
- Layer: normalized
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/8
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/tryptic_soy_broth.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Distilled water | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Pancreatic digest of casein | {"value": "17.0", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Peptic digest of soybean meal | {"value": "3.0", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Glucose | {"value": "2.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / Sodium chloride | {"value": "5.0", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / Dipotassium phosphate | {"value": "2.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[6].concentration / Agar | {"value": "15.0", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| variants[0].modifications / tsb_without_dextrose_plus_starch_or_maltose | ["Omit dextrose/glucose from the parent Tryptic Soy Broth formulation.", "Add 0.5% or 1.0% (w/v) soluble starch or maltose."] | incomplete_or_nonqualifying_attached_evidence; VARIANT_TEXT_REQUIRES_SOURCE_REVIEW | unsupported; not_performed | unknown | [{"reference": "PMID:15931519", "supports": "SUPPORT", "snippet": "tryptic soy broth without dextrose (TSBWD) containing 0.5% or 1.0%", "explanation": "Smith and Zahnley report the study-specific TSBWD variant and the starch/maltose supplement levels used for Arthrobacter psychrolactophilus ATCC 700733 growth."}] |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- PMID:15931519
- https://en.wikipedia.org/wiki/Tryptic_soy_broth
- https://togomedium.org/medium/M1668
- https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=871

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
