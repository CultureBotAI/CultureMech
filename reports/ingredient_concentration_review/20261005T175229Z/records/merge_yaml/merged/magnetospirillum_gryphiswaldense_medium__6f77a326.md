# Ingredient Concentration Review

- Record: data/merge_yaml/merged/magnetospirillum_gryphiswaldense_medium__6f77a326.yaml
- ID: CultureMech:003006
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 7b2fa0b5ea9135392945f0031372656064367a2aa8655d148f29fbc8c53f792f
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/8
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/TOGO_M677_Magnetospirillum_Gryphiswaldense_Medium.yaml
- data/normalized_yaml/bacterial/TOGO_M678_Magnetospirillum_Gryphiswaldense_Medium.yaml
- data/normalized_yaml/bacterial/magnetospirillum_gryphiswaldense_medium.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / MgSO4 x 7 H2O | {"value": "0.1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / K2HPO4 | {"value": "0.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / Sodium acetate | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / NH4Cl | {"value": "0.1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / Yeast extract | {"value": "0.1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[5].concentration / Sodium thioglycolate | {"value": "0.5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[6].concentration / Ferric citrate | {"value": "0.006", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| variants[0].modifications / crvi_stress_magnetosome_deficient_b17316 | ["Use magnetosome-deficient strain B17316 derived from M. gryphiswaldense MSR-1.", "Add Cr(VI) at 10 mg/L."] | incomplete_or_nonqualifying_attached_evidence; VARIANT_TEXT_REQUIRES_SOURCE_REVIEW | unsupported; not_performed | unknown | [{"reference": "PMID:37088211", "supports": "SUPPORT", "snippet": "The addition of 10 mg L-1 Cr(VI) significantly inhibited cell growth, but the magnetosome-deficient strain, B17316, showed an average specific growth rate of 0.062 h-1 at the same dosage.", "explanation": "Literature evidence supports a Cr(VI)-stress variant for magnetosome-deficient Magnetospirillum gryphiswaldense strain B17316."}] |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=660

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
