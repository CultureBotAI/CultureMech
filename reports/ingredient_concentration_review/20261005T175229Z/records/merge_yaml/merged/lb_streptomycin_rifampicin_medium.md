# Ingredient Concentration Review

- Record: data/merge_yaml/merged/lb_streptomycin_rifampicin_medium.yaml
- ID: CultureMech:008554
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 8e4fa271b94b7cd5d20e4c14f917259462cd9cdfcfb3f1effdfcef2e06169ff3
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/7
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/lb_ampicilin_hygromycin_medium.yaml
- data/normalized_yaml/bacterial/lb_ampicillin_cefpodoxime_kanamycin_medium.yaml
- data/normalized_yaml/bacterial/lb_ampicillin_kanamycin_medium.yaml
- data/normalized_yaml/bacterial/lb_chloramphenicol_medium.yaml
- data/normalized_yaml/bacterial/lb_kanamycin_hygromycin_medium.yaml
- data/normalized_yaml/bacterial/lb_nalidixic_acid_ciprofloxacin_medium.yaml
- data/normalized_yaml/bacterial/lb_rifampicin_medium.yaml
- data/normalized_yaml/bacterial/lb_streptomycin_medium.yaml
- data/normalized_yaml/bacterial/lb_streptomycin_rifampicin_medium.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Distilled water | {"value": "1", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / Yeast extract | {"value": "5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[2].concentration / NaCl | {"value": "5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[3].concentration / Agar (if needed) | {"value": "15", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[4].concentration / Bacto Tryptone (Difco) | {"value": "10", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[0].concentration / Rifampicin solution (50 mg/ml)* | {"value": "5", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| solutions[1].concentration / Streptomycin solution (50 mg/ml)* | {"value": "10", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://togomedium.org/medium/M1972
- https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1250

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
