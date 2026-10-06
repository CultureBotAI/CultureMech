# Ingredient Concentration Review

- Record: data/merge_yaml/merged/horikoshi_i_medium_with_5_nacl.yaml
- ID: CultureMech:002762
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: a3359114292778fadc33fd7f16b97c5f1e68970906b51438bce5d660c8edc342
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/2
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/bacterial/TOGO_M1092_Horikoshi-I_Medium_With_3.5_NaCl.yaml
- data/normalized_yaml/bacterial/TOGO_M404_Horikoshi-I_Medium_With_5_NaCl.yaml
- data/normalized_yaml/bacterial/TOGO_M407_Horikoshi-I_Medium_With_2_NaCl.yaml
- data/normalized_yaml/bacterial/horikoshi_i_medium_with_2_nacl.yaml
- data/normalized_yaml/bacterial/horikoshi_i_medium_with_3_5_nacl.yaml
- data/normalized_yaml/bacterial/horikoshi_i_medium_with_5_nacl.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / Horikoshi-I medium | {"value": "1000", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |
| ingredients[1].concentration / NaCl | {"value": "100", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=406

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
