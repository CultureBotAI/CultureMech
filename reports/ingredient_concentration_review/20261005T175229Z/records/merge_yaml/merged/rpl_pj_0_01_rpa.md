# Ingredient Concentration Review

- Record: data/merge_yaml/merged/rpl_pj_0_01_rpa.yaml
- ID: CultureMech:000124
- Reviewed commit: ea4fad40114940af87daf1d56c9cad56beec8cca
- Record SHA256: 3264ed47c3c5a071582324f2fd37e72f05a9a57a8423b6663dc1b979a535bea5
- Layer: merged
- Record kind: MEDIUM
- Mode: read-only; no recipe edits
- Source-checked claim rows: 0/1
- Verdict: source review incomplete
- Validation: 0 closed-schema errors

## Ownership

Candidate authoritative input paths (ID/name linkage; not proof of source equivalence):
- data/normalized_yaml/algae/mch.yaml
- data/normalized_yaml/algae/ncl.yaml
- data/normalized_yaml/algae/ncl_0_01_npa.yaml
- data/normalized_yaml/algae/ncl_mp.yaml
- data/normalized_yaml/algae/ncl_pj.yaml
- data/normalized_yaml/algae/ncl_pj_0_01_npa.yaml
- data/normalized_yaml/algae/pj.yaml
- data/normalized_yaml/algae/pj_nn.yaml
- data/normalized_yaml/algae/rpl.yaml
- data/normalized_yaml/algae/rpl_0_01_rpa.yaml
- data/normalized_yaml/algae/rpl_mp.yaml
- data/normalized_yaml/algae/rpl_pj.yaml
- data/normalized_yaml/algae/rpl_pj_0_01_rpa.yaml
- data/normalized_yaml/bacterial/mch.yaml
- data/normalized_yaml/bacterial/ncl.yaml
- data/normalized_yaml/bacterial/ncl_0_01_npa.yaml
- data/normalized_yaml/bacterial/ncl_mp.yaml
- data/normalized_yaml/bacterial/ncl_pj.yaml
- data/normalized_yaml/bacterial/ncl_pj_0_01_npa.yaml
- data/normalized_yaml/bacterial/pj.yaml
- data/normalized_yaml/bacterial/pj_nn.yaml
- data/normalized_yaml/bacterial/rpl.yaml
- data/normalized_yaml/bacterial/rpl_0_01_rpa.yaml
- data/normalized_yaml/bacterial/rpl_mp.yaml
- data/normalized_yaml/bacterial/rpl_pj.yaml
- data/normalized_yaml/bacterial/rpl_pj_0_01_rpa.yaml

## Concentration Claims

Missing means absent from inspected YAML, not absent from the scientific literature. Plausibility flags are triage leads, not proven errors.

| Field / ingredient | Existing amount | Evidence state / flags | Decision / source check | Proposed amount | Evidence and calculation |
| --- | --- | --- | --- | --- | --- |
| ingredients[0].concentration / KCl | {"value": "0.2", "unit": "G_PER_L"} | missing_attached_evidence;  | unsupported; not_performed | unknown | No scoped concentration evidence attached; source lookup pending |

## Source Leads

These references have not been fetched unless explicitly source-checked above.

- https://www.ccap.ac.uk/wp-content/uploads/MR_RPL_PJ_0_01_RPA.pdf

## Follow-up

Inspect the exact source formulation, quote amount/unit/basis, document any calculation, and resolve flags before proposing edits. Stock quantities must remain distinct from final-medium amounts. No findings were applied.
