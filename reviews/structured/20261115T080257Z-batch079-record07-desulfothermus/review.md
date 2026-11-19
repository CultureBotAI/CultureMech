# Recovered batch079 record07: DSMZ876 scientific assessment

- Review: 20261115T080257Z-batch079-record07-desulfothermus
- Repository: CultureBotAI/CultureMech
- Started UTC: 2026-11-15T07:56:56Z
- Finished UTC: 2026-11-15T08:02:57Z
- Reviewer: Codex recovery reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Completed bounded assessment of one generated record with both maintained owners as context. Source tables confirm stock/root representation defects, stale generated content, two chemical-form mismatches and unresolved preparation/source scope. Native diagnostic passes do not change this verdict. No scientific record was edited.

## Scope And Provenance

Record07 only: full generated target and its two maintained owners, every ingredient/stock entry, preparation, source provenance and chemical IDs.

Selection: Recovered batch079 selection identifies CultureMech:002034; exact paths and IDs checked.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base dda27db28f1e5f4f05da6d92fbd2cc1bd6e8add3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CultureMech:002034 | data/merge_yaml/merged/DESULFOTHERMUS_NAPHTHAE_MEDIUM.yaml | generated | DESULFOTHERMUS NAPHTHAE MEDIUM |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native schema | passed | True | CultureMech:002034 | Open-schema structure only. |
| Native strict schema | passed | True | CultureMech:002034 | One file, schema layer, zero errors; not a whole-repository QC sweep. |
| Native term validator | passed | True | CultureMech:002034 | Configured bound slots only; chemical term slots are not fully bound and this does not establish supplied-form identity. |
| Native reference validator | passed | True | CultureMech:002034 | ZERO evidence assertions checked; no evidence completeness or scientific approval implied. |
| Packaged MIM snapshot integrity | passed | True | CultureMech:002034 | Byte/hash/row/contract integrity only; no external chemical proof. |
| Native input inspection | passed | True | CultureMech:002034 | Native inspect captured every final local assessment input; original inputs rechecked without recipe changes. |
| Primary-source scientific assessment | failed | True | CultureMech:002034 | Assessment completed and found critical stock representation and exact-form defects; failed scientific acceptance is retained as needs_curation. |
| Read-only history and ownership review | passed | True | CultureMech:002034 | Historical provenance and maintained/generated boundaries read; no history edited or native scientific status promoted. Native validate-history targets separate session HistoryRecords, not these embedded event arrays. |
| Exact KOMODO recipe retrieval | unavailable | False | CultureMech:002034 | Exact servlet routes failed in bounded peer source review; no usable independent KOMODO formulation recovered. This is an unresolved source-identity finding, not an inferred equality. |

## Scientific And Domain Assessments

### Exact generated target and maintained sources

identity: concern. Targets: CultureMech:002034.

CultureMech:002034 explicitly denotes DSMZ876. KOMODO876/TD3 is a distinct maintained owner with unresolved source-equivalence and atmosphere claims; historical89%-of37 counterevidence is not a current identity measurement.

### All twelve basal component rates and volume basis

quantity: supported. Targets: CultureMech:002034.

The first twelve local rates match the structured main solution's explicit1005mL normalization. They are evidence_only decisions pending claim-level linkage, not instructions to replace them using1000mL water.

### Every direct and nested ingredient amount

quantity: concern. Targets: CultureMech:002034.

Reviewed37 generated root rows and41 rows in each owner, including10 existing nested components per owner. Correct stock placement before deriving final amounts; preserve distinct vitamin additions. No quantity or source field was changed.

data/merge_yaml/merged/DESULFOTHERMUS_NAPHTHAE_MEDIUM.yaml
ingredients[0]; Na2SO4; retained=3.9801 G_PER_L; evidence_only: main-rate supported on provider1005mL basis; source=1815:3.9801g/L-stock-or-main/1005mL-batch
ingredients[1]; KH2PO4; retained=0.199005 G_PER_L; evidence_only: main-rate supported on provider1005mL basis; source=1815:0.199005g/L-stock-or-main/1005mL-batch
ingredients[2]; NH4Cl; retained=0.248756 G_PER_L; evidence_only: main-rate supported on provider1005mL basis; source=1815:0.248756g/L-stock-or-main/1005mL-batch
ingredients[3]; NaCl; retained=19.9005 G_PER_L; evidence_only: main-rate supported on provider1005mL basis; source=1815:19.9005g/L-stock-or-main/1005mL-batch
ingredients[4]; MgCl2 x 6 H2O; retained=9.75124 G_PER_L; evidence_only: main-rate supported on provider1005mL basis; source=1815:9.75124g/L-stock-or-main/1005mL-batch
ingredients[5]; KCl; retained=0.497512 G_PER_L; evidence_only: main-rate supported on provider1005mL basis; source=1815:0.497512g/L-stock-or-main/1005mL-batch
ingredients[6]; CaCl2 x 2 H2O; retained=0.0995025 G_PER_L; evidence_only: main-rate supported on provider1005mL basis; source=1815:0.0995025g/L-stock-or-main/1005mL-batch
ingredients[7]; Sodium resazurin; retained=0.000497512 G_PER_L; evidence_only: main-rate supported on provider1005mL basis; source=1815:0.000497512g/L-stock-or-main/1005mL-batch
ingredients[8]; Na2CO3; retained=0.995025 G_PER_L; evidence_only: main-rate supported on provider1005mL basis; source=1815:0.995025g/L-stock-or-main/1005mL-batch
ingredients[9]; Na-caproate; retained=0.497512 G_PER_L; evidence_only: main-rate supported on provider1005mL basis; source=1815:0.497512g/L-stock-or-main/1005mL-batch
ingredients[10]; Na-butyrate; retained=0.298507 G_PER_L; evidence_only: main-rate supported on provider1005mL basis; source=1815:0.298507g/L-stock-or-main/1005mL-batch
ingredients[11]; Na2S x 9 H2O; retained=0.39801 G_PER_L; evidence_only: main-rate supported on provider1005mL basis; source=1815:0.39801g/L-stock-or-main/1005mL-batch
ingredients[12]; HCl; retained=2.5 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=595:2.5g/L-stock-or-main/1000mL-batch
ingredients[13]; FeCl2 x 4 H2O; retained=1.5 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=595:1.5g/L-stock-or-main/1000mL-batch
ingredients[14]; ZnCl2; retained=0.07 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=595:0.07g/L-stock-or-main/1000mL-batch
ingredients[15]; MnCl2 x 4 H2O; retained=0.1 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=595:0.1g/L-stock-or-main/1000mL-batch
ingredients[16]; H3BO3; retained=0.006 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=595:0.006g/L-stock-or-main/1000mL-batch
ingredients[17]; CoCl2 x 6 H2O; retained=0.19 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=595:0.19g/L-stock-or-main/1000mL-batch
ingredients[18]; CuCl2 x 2 H2O; retained=0.002 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=595:0.002g/L-stock-or-main/1000mL-batch
ingredients[19]; NiCl2 x 6 H2O; retained=0.024 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=595:0.024g/L-stock-or-main/1000mL-batch
ingredients[20]; Na2MoO4 x 2 H2O; retained=0.036 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=595:0.036g/L-stock-or-main/1000mL-batch
ingredients[21]; NaOH; retained=0.5 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=777:0.5g/L-stock-or-main/1000mL-batch
ingredients[22]; Na2SeO3 x 5 H2O; retained=0.003 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=777:0.003g/L-stock-or-main/1000mL-batch
ingredients[23]; Na2WO4 x 2 H2O; retained=0.004 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=777:0.004g/L-stock-or-main/1000mL-batch
ingredients[24]; Biotin; retained=0.02 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=5980:0.02g/L-stock-or-main/1000mL-batch
ingredients[25]; Folic acid; retained=0.02 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=5980:0.02g/L-stock-or-main/1000mL-batch
ingredients[26]; Pyridoxine hydrochloride; retained=0.4 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=5980:0.1g/L-stock-or-main/1000mL-batch, 1038:0.3g/L-stock-or-main/1000mL-batch
ingredients[27]; Thiamine HCl; retained=0.05 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=5980:0.05g/L-stock-or-main/1000mL-batch
ingredients[28]; Riboflavin; retained=0.05 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=5980:0.05g/L-stock-or-main/1000mL-batch
ingredients[29]; Nicotinic acid; retained=0.25 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=5980:0.05g/L-stock-or-main/1000mL-batch, 1038:0.2g/L-stock-or-main/1000mL-batch
ingredients[30]; Calcium D-(+)-pantothenate; retained=0.05 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=5980:0.05g/L-stock-or-main/1000mL-batch
ingredients[31]; Vitamin B12; retained=0.101 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=5980:0.001g/L-stock-or-main/1000mL-batch, 1038:0.1g/L-stock-or-main/1000mL-batch
ingredients[32]; p-Aminobenzoic acid; retained=0.13 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=5980:0.05g/L-stock-or-main/1000mL-batch, 1038:0.08g/L-stock-or-main/1000mL-batch
ingredients[33]; (DL)-alpha-Lipoic acid; retained=0.05 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=5980:0.05g/L-stock-or-main/1000mL-batch
ingredients[34]; D-(+)-biotin; retained=0.02 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=1038:0.02g/L-stock-or-main/1000mL-batch
ingredients[35]; Calcium pantothenate; retained=0.1 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=1038:0.1g/L-stock-or-main/1000mL-batch
ingredients[36]; Thiamine-HCl x 2 H2O; retained=0.2 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=1038:0.2g/L-stock-or-main/1000mL-batch
data/normalized_yaml/bacterial/desulfothermus_naphthae_medium.yaml
ingredients[0]; Na2SO4; retained=3.9801 G_PER_L; evidence_only: main-rate supported on provider1005mL basis; source=1815:3.9801g/L-stock-or-main/1005mL-batch
ingredients[1]; KH2PO4; retained=0.199005 G_PER_L; evidence_only: main-rate supported on provider1005mL basis; source=1815:0.199005g/L-stock-or-main/1005mL-batch
ingredients[2]; NH4Cl; retained=0.248756 G_PER_L; evidence_only: main-rate supported on provider1005mL basis; source=1815:0.248756g/L-stock-or-main/1005mL-batch
ingredients[3]; NaCl; retained=19.9005 G_PER_L; evidence_only: main-rate supported on provider1005mL basis; source=1815:19.9005g/L-stock-or-main/1005mL-batch
ingredients[4]; MgCl2 x 6 H2O; retained=9.75124 G_PER_L; evidence_only: main-rate supported on provider1005mL basis; source=1815:9.75124g/L-stock-or-main/1005mL-batch
ingredients[5]; KCl; retained=0.497512 G_PER_L; evidence_only: main-rate supported on provider1005mL basis; source=1815:0.497512g/L-stock-or-main/1005mL-batch
ingredients[6]; CaCl2 x 2 H2O; retained=0.0995025 G_PER_L; evidence_only: main-rate supported on provider1005mL basis; source=1815:0.0995025g/L-stock-or-main/1005mL-batch
ingredients[7]; Sodium resazurin; retained=0.000497512 G_PER_L; evidence_only: main-rate supported on provider1005mL basis; source=1815:0.000497512g/L-stock-or-main/1005mL-batch
ingredients[8]; Na2CO3; retained=0.995025 G_PER_L; evidence_only: main-rate supported on provider1005mL basis; source=1815:0.995025g/L-stock-or-main/1005mL-batch
ingredients[9]; Na-caproate; retained=0.497512 G_PER_L; evidence_only: main-rate supported on provider1005mL basis; source=1815:0.497512g/L-stock-or-main/1005mL-batch
ingredients[10]; Na-butyrate; retained=0.298507 G_PER_L; evidence_only: main-rate supported on provider1005mL basis; source=1815:0.298507g/L-stock-or-main/1005mL-batch
ingredients[11]; Na2S x 9 H2O; retained=0.39801 G_PER_L; evidence_only: main-rate supported on provider1005mL basis; source=1815:0.39801g/L-stock-or-main/1005mL-batch
ingredients[12]; HCl; retained=2.5 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=595:2.5g/L-stock-or-main/1000mL-batch
ingredients[13]; ZnCl2; retained=0.07 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=595:0.07g/L-stock-or-main/1000mL-batch
ingredients[14]; MnCl2 x 4 H2O; retained=0.1 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=595:0.1g/L-stock-or-main/1000mL-batch
ingredients[15]; H3BO3; retained=0.006 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=595:0.006g/L-stock-or-main/1000mL-batch
ingredients[16]; CoCl2 x 6 H2O; retained=0.19 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=595:0.19g/L-stock-or-main/1000mL-batch
ingredients[17]; CuCl2 x 2 H2O; retained=0.002 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=595:0.002g/L-stock-or-main/1000mL-batch
ingredients[18]; NiCl2 x 6 H2O; retained=0.024 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=595:0.024g/L-stock-or-main/1000mL-batch
ingredients[19]; Na2MoO4 x 2 H2O; retained=0.036 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=595:0.036g/L-stock-or-main/1000mL-batch
ingredients[20]; NaOH; retained=0.5 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=777:0.5g/L-stock-or-main/1000mL-batch
ingredients[21]; Na2SeO3 x 5 H2O; retained=0.003 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=777:0.003g/L-stock-or-main/1000mL-batch
ingredients[22]; Na2WO4 x 2 H2O; retained=0.004 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=777:0.004g/L-stock-or-main/1000mL-batch
ingredients[23]; Biotin; retained=0.02 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=5980:0.02g/L-stock-or-main/1000mL-batch
ingredients[24]; Folic acid; retained=0.02 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=5980:0.02g/L-stock-or-main/1000mL-batch
ingredients[25]; Thiamine HCl; retained=0.05 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=5980:0.05g/L-stock-or-main/1000mL-batch
ingredients[26]; Riboflavin; retained=0.05 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=5980:0.05g/L-stock-or-main/1000mL-batch
ingredients[27]; Calcium D-(+)-pantothenate; retained=0.05 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=5980:0.05g/L-stock-or-main/1000mL-batch
ingredients[28]; (DL)-alpha-Lipoic acid; retained=0.05 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=5980:0.05g/L-stock-or-main/1000mL-batch
ingredients[29]; D-(+)-biotin; retained=0.02 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=1038:0.02g/L-stock-or-main/1000mL-batch
ingredients[30]; Calcium pantothenate; retained=0.1 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=1038:0.1g/L-stock-or-main/1000mL-batch
solutions[0].composition[0]; FeCl2 x 4 H2O; retained=1.5 G_PER_L; evidence_only for named stock-strength component; stock completeness and receiving dose still concern; source=595:1.5g/L-stock-or-main/1000mL-batch
solutions[1].composition[0]; Thiamine-HCl x 2 H2O; retained=0.2 G_PER_L; evidence_only for named stock-strength component; stock completeness and receiving dose still concern; source=1038:0.2g/L-stock-or-main/1000mL-batch
solutions[1].composition[1]; Nicotinic acid; retained=0.2 G_PER_L; evidence_only for named stock-strength component; stock completeness and receiving dose still concern; source=5980:0.05g/L-stock-or-main/1000mL-batch, 1038:0.2g/L-stock-or-main/1000mL-batch
solutions[1].composition[2]; p-Aminobenzoic acid; retained=0.08 G_PER_L; evidence_only for named stock-strength component; stock completeness and receiving dose still concern; source=5980:0.05g/L-stock-or-main/1000mL-batch, 1038:0.08g/L-stock-or-main/1000mL-batch
solutions[1].composition[3]; Pyridoxine hydrochloride; retained=0.3 G_PER_L; evidence_only for named stock-strength component; stock completeness and receiving dose still concern; source=5980:0.1g/L-stock-or-main/1000mL-batch, 1038:0.3g/L-stock-or-main/1000mL-batch
solutions[1].composition[4]; Vitamin B12; retained=0.1 G_PER_L; evidence_only for named stock-strength component; stock completeness and receiving dose still concern; source=5980:0.001g/L-stock-or-main/1000mL-batch, 1038:0.1g/L-stock-or-main/1000mL-batch
solutions[2].composition[0]; Nicotinic acid; retained=0.05 G_PER_L; evidence_only for named stock-strength component; stock completeness and receiving dose still concern; source=5980:0.05g/L-stock-or-main/1000mL-batch, 1038:0.2g/L-stock-or-main/1000mL-batch
solutions[2].composition[1]; p-Aminobenzoic acid; retained=0.05 G_PER_L; evidence_only for named stock-strength component; stock completeness and receiving dose still concern; source=5980:0.05g/L-stock-or-main/1000mL-batch, 1038:0.08g/L-stock-or-main/1000mL-batch
solutions[2].composition[2]; Pyridoxine hydrochloride; retained=0.1 G_PER_L; evidence_only for named stock-strength component; stock completeness and receiving dose still concern; source=5980:0.1g/L-stock-or-main/1000mL-batch, 1038:0.3g/L-stock-or-main/1000mL-batch
solutions[2].composition[3]; Vitamin B12; retained=0.001 G_PER_L; evidence_only for named stock-strength component; stock completeness and receiving dose still concern; source=5980:0.001g/L-stock-or-main/1000mL-batch, 1038:0.1g/L-stock-or-main/1000mL-batch
data/normalized_yaml/bacterial/KOMODO_876_TD3-MEDIUM.yaml
ingredients[0]; Na2SO4; retained=3.9801 G_PER_L; evidence_only: main-rate supported on provider1005mL basis; source=1815:3.9801g/L-stock-or-main/1005mL-batch
ingredients[1]; KH2PO4; retained=0.199005 G_PER_L; evidence_only: main-rate supported on provider1005mL basis; source=1815:0.199005g/L-stock-or-main/1005mL-batch
ingredients[2]; NH4Cl; retained=0.248756 G_PER_L; evidence_only: main-rate supported on provider1005mL basis; source=1815:0.248756g/L-stock-or-main/1005mL-batch
ingredients[3]; NaCl; retained=19.9005 G_PER_L; evidence_only: main-rate supported on provider1005mL basis; source=1815:19.9005g/L-stock-or-main/1005mL-batch
ingredients[4]; MgCl2 x 6 H2O; retained=9.75124 G_PER_L; evidence_only: main-rate supported on provider1005mL basis; source=1815:9.75124g/L-stock-or-main/1005mL-batch
ingredients[5]; KCl; retained=0.497512 G_PER_L; evidence_only: main-rate supported on provider1005mL basis; source=1815:0.497512g/L-stock-or-main/1005mL-batch
ingredients[6]; CaCl2 x 2 H2O; retained=0.0995025 G_PER_L; evidence_only: main-rate supported on provider1005mL basis; source=1815:0.0995025g/L-stock-or-main/1005mL-batch
ingredients[7]; Sodium resazurin; retained=0.000497512 G_PER_L; evidence_only: main-rate supported on provider1005mL basis; source=1815:0.000497512g/L-stock-or-main/1005mL-batch
ingredients[8]; Na2CO3; retained=0.995025 G_PER_L; evidence_only: main-rate supported on provider1005mL basis; source=1815:0.995025g/L-stock-or-main/1005mL-batch
ingredients[9]; Na-caproate; retained=0.497512 G_PER_L; evidence_only: main-rate supported on provider1005mL basis; source=1815:0.497512g/L-stock-or-main/1005mL-batch
ingredients[10]; Na-butyrate; retained=0.298507 G_PER_L; evidence_only: main-rate supported on provider1005mL basis; source=1815:0.298507g/L-stock-or-main/1005mL-batch
ingredients[11]; Na2S x 9 H2O; retained=0.39801 G_PER_L; evidence_only: main-rate supported on provider1005mL basis; source=1815:0.39801g/L-stock-or-main/1005mL-batch
ingredients[12]; HCl; retained=2.5 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=595:2.5g/L-stock-or-main/1000mL-batch
ingredients[13]; ZnCl2; retained=0.07 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=595:0.07g/L-stock-or-main/1000mL-batch
ingredients[14]; MnCl2 x 4 H2O; retained=0.1 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=595:0.1g/L-stock-or-main/1000mL-batch
ingredients[15]; H3BO3; retained=0.006 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=595:0.006g/L-stock-or-main/1000mL-batch
ingredients[16]; CoCl2 x 6 H2O; retained=0.19 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=595:0.19g/L-stock-or-main/1000mL-batch
ingredients[17]; CuCl2 x 2 H2O; retained=0.002 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=595:0.002g/L-stock-or-main/1000mL-batch
ingredients[18]; NiCl2 x 6 H2O; retained=0.024 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=595:0.024g/L-stock-or-main/1000mL-batch
ingredients[19]; Na2MoO4 x 2 H2O; retained=0.036 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=595:0.036g/L-stock-or-main/1000mL-batch
ingredients[20]; NaOH; retained=0.5 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=777:0.5g/L-stock-or-main/1000mL-batch
ingredients[21]; Na2SeO3 x 5 H2O; retained=0.003 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=777:0.003g/L-stock-or-main/1000mL-batch
ingredients[22]; Na2WO4 x 2 H2O; retained=0.004 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=777:0.004g/L-stock-or-main/1000mL-batch
ingredients[23]; Biotin; retained=0.02 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=5980:0.02g/L-stock-or-main/1000mL-batch
ingredients[24]; Folic acid; retained=0.02 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=5980:0.02g/L-stock-or-main/1000mL-batch
ingredients[25]; Thiamine HCl; retained=0.05 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=5980:0.05g/L-stock-or-main/1000mL-batch
ingredients[26]; Riboflavin; retained=0.05 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=5980:0.05g/L-stock-or-main/1000mL-batch
ingredients[27]; Calcium D-(+)-pantothenate; retained=0.05 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=5980:0.05g/L-stock-or-main/1000mL-batch
ingredients[28]; (DL)-alpha-Lipoic acid; retained=0.05 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=5980:0.05g/L-stock-or-main/1000mL-batch
ingredients[29]; D-(+)-biotin; retained=0.02 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=1038:0.02g/L-stock-or-main/1000mL-batch
ingredients[30]; Calcium pantothenate; retained=0.1 G_PER_L; correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted; source=1038:0.1g/L-stock-or-main/1000mL-batch
solutions[0].composition[0]; FeCl2 x 4 H2O; retained=1.5 G_PER_L; evidence_only for named stock-strength component; stock completeness and receiving dose still concern; source=595:1.5g/L-stock-or-main/1000mL-batch
solutions[1].composition[0]; Thiamine-HCl x 2 H2O; retained=0.2 G_PER_L; evidence_only for named stock-strength component; stock completeness and receiving dose still concern; source=1038:0.2g/L-stock-or-main/1000mL-batch
solutions[1].composition[1]; Nicotinic acid; retained=0.2 G_PER_L; evidence_only for named stock-strength component; stock completeness and receiving dose still concern; source=5980:0.05g/L-stock-or-main/1000mL-batch, 1038:0.2g/L-stock-or-main/1000mL-batch
solutions[1].composition[2]; p-Aminobenzoic acid; retained=0.08 G_PER_L; evidence_only for named stock-strength component; stock completeness and receiving dose still concern; source=5980:0.05g/L-stock-or-main/1000mL-batch, 1038:0.08g/L-stock-or-main/1000mL-batch
solutions[1].composition[3]; Pyridoxine hydrochloride; retained=0.3 G_PER_L; evidence_only for named stock-strength component; stock completeness and receiving dose still concern; source=5980:0.1g/L-stock-or-main/1000mL-batch, 1038:0.3g/L-stock-or-main/1000mL-batch
solutions[1].composition[4]; Vitamin B12; retained=0.1 G_PER_L; evidence_only for named stock-strength component; stock completeness and receiving dose still concern; source=5980:0.001g/L-stock-or-main/1000mL-batch, 1038:0.1g/L-stock-or-main/1000mL-batch
solutions[2].composition[0]; Nicotinic acid; retained=0.05 G_PER_L; evidence_only for named stock-strength component; stock completeness and receiving dose still concern; source=5980:0.05g/L-stock-or-main/1000mL-batch, 1038:0.2g/L-stock-or-main/1000mL-batch
solutions[2].composition[1]; p-Aminobenzoic acid; retained=0.05 G_PER_L; evidence_only for named stock-strength component; stock completeness and receiving dose still concern; source=5980:0.05g/L-stock-or-main/1000mL-batch, 1038:0.08g/L-stock-or-main/1000mL-batch
solutions[2].composition[2]; Pyridoxine hydrochloride; retained=0.1 G_PER_L; evidence_only for named stock-strength component; stock completeness and receiving dose still concern; source=5980:0.1g/L-stock-or-main/1000mL-batch, 1038:0.3g/L-stock-or-main/1000mL-batch
solutions[2].composition[3]; Vitamin B12; retained=0.001 G_PER_L; evidence_only for named stock-strength component; stock completeness and receiving dose still concern; source=5980:0.001g/L-stock-or-main/1000mL-batch, 1038:0.1g/L-stock-or-main/1000mL-batch

### Stock-addition basis and conversion limits

quantity: concern. Targets: CultureMech:002034.

DSM owner asserts three1mL/L additions; provider describes1mL per1005mL batch, with2mL selenium/tungsten stock. HCl2.5g/L is provider stock data, not independently derivable from an unspecified25% basis. Retain exact batch and stock context; no density assumption or averaged vitamin total.

### Every asserted chemical identifier and supplied form

grounding: concern. Targets: CultureMech:002034.

35 unique asserted ChEBI IDs across232 primary/secondary slots are active. Two exact-form mismatches remain: nickel hexahydrate and sodium resazurin.29 named identities are compatible; B12 breadth, lipoic stereochemistry, HCl solution context and generic calcium-pantothenate specificity retain explicit limits.

CHEBI:114126; Na-caproate; compatible_named_chemical; Current active ChEBI label/synonyms and formula/InChI/SMILES agree with the named chemical, including explicitly supplied counterion/hydrate counts where present. This is identity support only, not support for concentration, stock placement, purity or growth.
CHEBI:131361; Na2SeO3 x 5 H2O; compatible_named_chemical; Current active ChEBI label/synonyms and formula/InChI/SMILES agree with the named chemical, including explicitly supplied counterion/hydrate counts where present. This is identity support only, not support for concentration, stock placement, purity or growth.
CHEBI:132751; Thiamine-HCl x 2 H2O; compatible_named_chemical; Current active ChEBI label/synonyms and formula/InChI/SMILES agree with the named chemical, including explicitly supplied counterion/hydrate counts where present. This is identity support only, not support for concentration, stock placement, purity or growth.
CHEBI:15940; Nicotinic acid; compatible_named_chemical; Current active ChEBI label/synonyms and formula/InChI/SMILES agree with the named chemical, including explicitly supplied counterion/hydrate counts where present. This is identity support only, not support for concentration, stock placement, purity or growth.
CHEBI:15956; Biotin, D-(+)-biotin; compatible_named_chemical; Current active ChEBI label/synonyms and formula/InChI/SMILES agree with the named chemical, including explicitly supplied counterion/hydrate counts where present. This is identity support only, not support for concentration, stock placement, purity or growth.
CHEBI:16494; (DL)-alpha-Lipoic acid; compatible_broad_identity; Lipoic-acid connectivity matches, but the ontology InChI and SMILES contain no stereo specification and do not establish the explicit DL/racemic supplied material. Retain the source DL label; do not infer pure R/S identity or claim exact racemate proof.
CHEBI:17015; Riboflavin; compatible_named_chemical; Current active ChEBI label/synonyms and formula/InChI/SMILES agree with the named chemical, including explicitly supplied counterion/hydrate counts where present. This is identity support only, not support for concentration, stock placement, purity or growth.
CHEBI:176843; Vitamin B12; compatible_broad_identity; Active vitamin B12 vitamer class matches the source generic label. No molecular formula/mass/structure is supplied for the class, so no specific vitamer, counterion or mass-to-molar conversion is established. This broad match is not itself an incorrect ID.
CHEBI:17883; HCl; matched_constituent_not_solution; HCl constituent identity matches. The term does not encode the separately supplied aqueous25% stock, percentage basis or receiving-medium dilution. Preserve stock attribute/dose; the identity match does not validate provider-derived concentration arithmetic.
CHEBI:26710; NaCl; compatible_named_chemical; Current active ChEBI label/synonyms and formula/InChI/SMILES agree with the named chemical, including explicitly supplied counterion/hydrate counts where present. This is identity support only, not support for concentration, stock placement, purity or growth.
CHEBI:27470; Folic acid; compatible_named_chemical; Current active ChEBI label/synonyms and formula/InChI/SMILES agree with the named chemical, including explicitly supplied counterion/hydrate counts where present. This is identity support only, not support for concentration, stock placement, purity or growth.
CHEBI:29377; Na2CO3; compatible_named_chemical; Current active ChEBI label/synonyms and formula/InChI/SMILES agree with the named chemical, including explicitly supplied counterion/hydrate counts where present. This is identity support only, not support for concentration, stock placement, purity or growth.
CHEBI:30753; p-Aminobenzoic acid; compatible_named_chemical; Current active ChEBI label/synonyms and formula/InChI/SMILES agree with the named chemical, including explicitly supplied counterion/hydrate counts where present. This is identity support only, not support for concentration, stock placement, purity or growth.
CHEBI:30961; Pyridoxine hydrochloride; compatible_named_chemical; Current active ChEBI label/synonyms and formula/InChI/SMILES agree with the named chemical, including explicitly supplied counterion/hydrate counts where present. This is identity support only, not support for concentration, stock placement, purity or growth.
CHEBI:31206; NH4Cl; compatible_named_chemical; Current active ChEBI label/synonyms and formula/InChI/SMILES agree with the named chemical, including explicitly supplied counterion/hydrate counts where present. This is identity support only, not support for concentration, stock placement, purity or growth.
CHEBI:31345; Calcium D-(+)-pantothenate, Calcium pantothenate; matched_with_source_specificity_limit; Formula 2C9H16NO5.Ca and explicit D stereochemistry support Calcium D-(+)-pantothenate. For the separately named generic Calcium pantothenate source component, unspecified stereochemistry is not independently fixed by the source name alone. Do not reject the D-labelled match or infer generic-source stereo solely from MIM synonyms. No molecular-weight conversion is made.
CHEBI:32145; NaOH; compatible_named_chemical; Current active ChEBI label/synonyms and formula/InChI/SMILES agree with the named chemical, including explicitly supplied counterion/hydrate counts where present. This is identity support only, not support for concentration, stock placement, purity or growth.
CHEBI:32149; Na2SO4; compatible_named_chemical; Current active ChEBI label/synonyms and formula/InChI/SMILES agree with the named chemical, including explicitly supplied counterion/hydrate counts where present. This is identity support only, not support for concentration, stock placement, purity or growth.
CHEBI:32588; KCl; compatible_named_chemical; Current active ChEBI label/synonyms and formula/InChI/SMILES agree with the named chemical, including explicitly supplied counterion/hydrate counts where present. This is identity support only, not support for concentration, stock placement, purity or growth.
CHEBI:33118; H3BO3; compatible_named_chemical; Current active ChEBI label/synonyms and formula/InChI/SMILES agree with the named chemical, including explicitly supplied counterion/hydrate counts where present. This is identity support only, not support for concentration, stock placement, purity or growth.
CHEBI:34887; NiCl2 x 6 H2O; exact_form_mismatch; Local NiCl2 x 6 H2O requires six waters; asserted Cl2Ni has none. Candidate CHEBI:53542 explicitly represents 2Cl.6H2O.Ni. Correct both primary and secondary mappings in maintained owners, preserving amount/stage; regenerate derived target. Exact MIM preferred row is REJECTED while its synonym row is MAPPED; both identify53542.
CHEBI:49105; Thiamine HCl; compatible_named_chemical; Current active ChEBI label/synonyms and formula/InChI/SMILES agree with the named chemical, including explicitly supplied counterion/hydrate counts where present. This is identity support only, not support for concentration, stock placement, purity or growth.
CHEBI:49976; ZnCl2; compatible_named_chemical; Current active ChEBI label/synonyms and formula/InChI/SMILES agree with the named chemical, including explicitly supplied counterion/hydrate counts where present. This is identity support only, not support for concentration, stock placement, purity or growth.
CHEBI:53503; CoCl2 x 6 H2O; compatible_named_chemical; Current active ChEBI label/synonyms and formula/InChI/SMILES agree with the named chemical, including explicitly supplied counterion/hydrate counts where present. This is identity support only, not support for concentration, stock placement, purity or growth.
CHEBI:63036; KH2PO4; compatible_named_chemical; Current active ChEBI label/synonyms and formula/InChI/SMILES agree with the named chemical, including explicitly supplied counterion/hydrate counts where present. This is identity support only, not support for concentration, stock placement, purity or growth.
CHEBI:63939; Na2WO4 x 2 H2O; compatible_named_chemical; Current active ChEBI label/synonyms and formula/InChI/SMILES agree with the named chemical, including explicitly supplied counterion/hydrate counts where present. This is identity support only, not support for concentration, stock placement, purity or growth.
CHEBI:64103; Na-butyrate; compatible_named_chemical; Current active ChEBI label/synonyms and formula/InChI/SMILES agree with the named chemical, including explicitly supplied counterion/hydrate counts where present. This is identity support only, not support for concentration, stock placement, purity or growth.
CHEBI:75213; Na2MoO4 x 2 H2O; compatible_named_chemical; Current active ChEBI label/synonyms and formula/InChI/SMILES agree with the named chemical, including explicitly supplied counterion/hydrate counts where present. This is identity support only, not support for concentration, stock placement, purity or growth.
CHEBI:76209; Na2S x 9 H2O; compatible_named_chemical; Current active ChEBI label/synonyms and formula/InChI/SMILES agree with the named chemical, including explicitly supplied counterion/hydrate counts where present. This is identity support only, not support for concentration, stock placement, purity or growth.
CHEBI:86158; CaCl2 x 2 H2O; compatible_named_chemical; Current active ChEBI label/synonyms and formula/InChI/SMILES agree with the named chemical, including explicitly supplied counterion/hydrate counts where present. This is identity support only, not support for concentration, stock placement, purity or growth.
CHEBI:86249; FeCl2 x 4 H2O; compatible_named_chemical; Current active ChEBI label/synonyms and formula/InChI/SMILES agree with the named chemical, including explicitly supplied counterion/hydrate counts where present. This is identity support only, not support for concentration, stock placement, purity or growth.
CHEBI:86318; CuCl2 x 2 H2O; compatible_named_chemical; Current active ChEBI label/synonyms and formula/InChI/SMILES agree with the named chemical, including explicitly supplied counterion/hydrate counts where present. This is identity support only, not support for concentration, stock placement, purity or growth.
CHEBI:86345; MgCl2 x 6 H2O; compatible_named_chemical; Current active ChEBI label/synonyms and formula/InChI/SMILES agree with the named chemical, including explicitly supplied counterion/hydrate counts where present. This is identity support only, not support for concentration, stock placement, purity or growth.
CHEBI:86368; MnCl2 x 4 H2O; compatible_named_chemical; Current active ChEBI label/synonyms and formula/InChI/SMILES agree with the named chemical, including explicitly supplied counterion/hydrate counts where present. This is identity support only, not support for concentration, stock placement, purity or growth.
CHEBI:8806; Sodium resazurin; exact_form_mismatch; Local and primary-source material is Sodium resazurin; asserted C12H7NO4/229.191 contains no sodium. MIM exact Sodium resazurin synonym maps to8806 and therefore reproduces, rather than resolves, the supplied-salt conflict. Resolve authoritative sodium-salt identity before any replacement or mass/molar conversion; no replacement ID is asserted by this audit.

### Preparation, pH, gas and optional supplement

scope: concern. Targets: CultureMech:002034.

Main anoxic protocol, vitamin filtration and pH6.7–6.9 are source-supported. SL-10 makeup text belongs to the stock, while KOMODO aerobic wording conflicts with DSMZ. Optional1%v/v fatty-acid-mixture prose is correctly scoped to medium119's mixture only.

### Composition and physical-state classification

identity: supported. Targets: CultureMech:002034.

Source describes a defined liquid formulation; existing DEFINED/DEFINED/LIQUID classification is supported. Empty optional growth/storage fields are not filled by inference.

### Organism and cultivation claims

evidence: supported. Targets: CultureMech:002034.

No strain-specific structured growth claim is asserted by this target. Generic cultivation context and optional stimulation note are recipe-source statements only; no optimality, species-wide growth or medium119 organism claim is inferred.

### Evidence linkage, history and generated freshness

provenance: concern. Targets: CultureMech:002034.

Each complete YAML lacks evidence entries; source URLs/history remain provenance leads. Existing nesting repairs are credited. GeneratedAugust6 content predates theirAugust7/15 nesting events, and current exact-formulation merge rules require source-boundary decisions before regeneration.

## Findings

### F-stock: Stock formulations appear as basal ingredients

blocker / open / confirmed; issue key: batch079-record07-f-stock.

Both owners leave trace, selenium/tungsten and vitamin components at root stock strengths. SL-10/vitamin nesting is incomplete and no selenium/tungsten container exists within these fully read files. This changes the formulation a reader would prepare; maintain separate stocks, supplied forms, addition amounts and source basis.

### F-stale: Generated target drops existing normalized nesting repairs

blocker / open / confirmed; issue key: batch079-record07-f-stale.

The generated target retains37 root ingredients and no solutions, including summed pyridoxine0.4, nicotinic acid0.25, B120.101 and PABA0.13G_PER_L. Each current owner has31 root plus10 nested components. Do not overwrite owners with this stale product or force differing formulations into one current merge group.

### F-nickel: Hexahydrate supplied as anhydrous nickel chloride

major / open / confirmed; issue key: batch079-record07-f-nickel.

Generated ingredients[19] and both owners' ingredients[18] use34887 in primary and secondary term slots.53542 explicitly represents six waters. Exact MIM rows have different mapped/rejected roles; preserve resolver policy and attach chemical evidence through authoritative inputs.

### F-resazurin: Sodium resazurin uses an identifier without sodium

major / open / confirmed; issue key: batch079-record07-f-resazurin.

All three files' ingredients[7].term map the explicitly supplied sodium salt to8806, whose formula has no sodium. A repeated MIM synonym mapping is not independent chemical verification. Replacement identity remains unresolved; no substitute ID is invented.

### F-preparation: Conflicting atmosphere and misplaced stock preparation

major / open / confirmed; issue key: batch079-record07-f-preparation.

KOMODO notes assert aerobic conditions while the associated DSMZ formulation is anoxic. Exact KOMODO equivalence is not established. Separately, DSM and generated preparation_steps[2] contain SL-10 makeup text at main-medium scope. Preserve distinctions among main80%N2/20%CO2, selected100%N2 stocks and vitamin filtration.

### F-linkage: Formulation support lacks narrow evidence links

minor / open / confirmed; issue key: batch079-record07-f-linkage.

The complete three YAML files contain no evidence entries. Native references consequently inspect zero assertions. Attach evidence to each corrected claim, retaining source/version/stock basis and existing history; no missing optional property is inferred false.

## Recommended Actions And Acceptance Checks

### ACT-owners

Resolve source equivalence, stock boundaries/doses, preparation scoping and narrow evidence in the two maintained owners; keep exact quantities unsupported by sources unresolved. Current observations are retained as follow-up rather than a forced repair.

- Compare every direct and nested component with primary stock tables, preserving1005mL provider basis and independent stock strengths.
- Use round-trip source edits with closed-schema validation and append-only substantive curation events.
- Rerun native schema, strict, term and reference checks on changed owners; manually verify PURL/table claims.

### ACT-grounding

Correct only exact verified chemical forms in authoritative inputs after checking packaged resolver behavior; resolve or explicitly withhold sodium-resazurin replacement and narrower stereochemical claims.

- Recheck ChEBI formula/hydration/charge/stereochemistry against exact supplied source forms.
- Keep MIM snapshot immutable and use its maintained resolver; do not bypass rejected/ambiguous decisions.
- Validate changed owner terms and source-linked evidence without claiming configured term validation covers all chemical slots.

### ACT-regenerate

After owner decisions, regenerate only the defensible scoped target group through maintained merge code, preserving IDs and all historical receipts. If owners split under exact-formulation rules, review the ID/lifecycle impact rather than forcing the historical merge.

- Preview grouping/names/IDs; never use --limit as a target selector.
- Run native output validation, verify-merges and audit-merge-freshness at their documented scopes; record pre-existing corpus drift separately.
- Independent scientific review confirms stock/preparation/identity preservation before considering a passing assessment.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| E-record | data/merge_yaml/merged/DESULFOTHERMUS_NAPHTHAE_MEDIUM.yaml | context_only | Complete generated YAML and both complete maintained owners read; input hashes verified. Generated37 root ingredients/no solutions; each owner31 root ingredients and10 nested components. |
| E-primary | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium876.pdf; Pages1–2: basal recipe, preparation and four separate stock tables | partial | Official formulation distinguishes basal ingredients, SL-10, selenite/tungstate and two vitamin stocks; supports anoxic preparation, pH and optional fatty-acid supplementation. |
| E-structured | https://mediadive.dsmz.de/download/medium/876/json; solutions1815,595,777,5980,1038; full separate recipe tables | partial | Provider records1005mL main volume and1000mL stocks. Twelve main rates match local values; stock rates must retain their separate solution context. Provider conversion is not independent proof of percentage basis or chemical grounding. |
| E-flattened | https://mediadive.dsmz.de/download/composition/876/json; Pyridoxine hydrochloride row compared with both primary vitamin stocks | refutes | Flattened pyridoxine0.000298507g/L captures only the0.3g/L stock contribution at1mL/1005mL, although the other stock also supplies0.1g/L at1mL/1005mL. This endpoint is not an authoritative total oracle. |
| E-119 | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium119.pdf; Fatty acid mixture subsection, pages2–3 only | supports | The referenced mixture is a separate preparation. Existing optional1%v/v prose correctly transfers this mixture only; no medium119 basal recipe, organism claims or gas conditions are transferred. |
| E-mim | src/culturemech/data/mediaingredientmech/label_index.csv; Pinned metadata; exact label rows retained in input snapshot | context_only | Snapshot6643131b0f12ab40b66f98135245fca04027e0e9 passes native integrity check. Nickel exact-label rows include a rejected preferred row and mapped synonym, both53542; sodium-resazurin synonym maps8806. Resolver policy and chemical truth are separate. |
| E-peer | .temp/batch079-scientific-20261114/peer-review-record07.md | context_only | Independent source peer supplied by coordinating root; current input and primary citations rechecked by the author before adopting findings. |
| E-generator | src/culturemech/merge/formulation.py | context_only | Current generator requires exact formulation assertions, including stocks, notes and conditions. Historical ingredient-set grouping is not permission to force the two differing owners into one regenerated target. |
| E-CHEBI-114126 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_114126; CHEBI:114126: exact active OLS/ChEBI term | context_only | sodium hexanoate; formula=['C6H11O2.Na']; active=True |
| E-CHEBI-131361 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361; CHEBI:131361: exact active OLS/ChEBI term | context_only | disodium selenite pentahydrate; formula=['5H2O.2Na.O3Se']; active=True |
| E-CHEBI-132751 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_132751; CHEBI:132751: exact active OLS/ChEBI term | context_only | thiamine hydrochloride dihydrate; formula=['C12H18N4OS.2Cl.2H2O']; active=True |
| E-CHEBI-15940 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940; CHEBI:15940: exact active OLS/ChEBI term | context_only | nicotinic acid; formula=['C6H5NO2']; active=True |
| E-CHEBI-15956 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956; CHEBI:15956: exact active OLS/ChEBI term | context_only | biotin; formula=['C10H16N2O3S']; active=True |
| E-CHEBI-16494 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494; CHEBI:16494: exact active OLS/ChEBI term | context_only | lipoic acid; formula=['C8H14O2S2']; active=True |
| E-CHEBI-17015 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015; CHEBI:17015: exact active OLS/ChEBI term | context_only | riboflavin; formula=['C17H20N4O6']; active=True |
| E-CHEBI-176843 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843; CHEBI:176843: exact active OLS/ChEBI term | context_only | vitamin B12; formula=None; active=True |
| E-CHEBI-17883 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883; CHEBI:17883: exact active OLS/ChEBI term | context_only | hydrogen chloride; formula=['HCl']; active=True |
| E-CHEBI-26710 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710; CHEBI:26710: exact active OLS/ChEBI term | context_only | sodium chloride; formula=['Cl.Na']; active=True |
| E-CHEBI-27470 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470; CHEBI:27470: exact active OLS/ChEBI term | context_only | folic acid; formula=['C19H19N7O6']; active=True |
| E-CHEBI-29377 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377; CHEBI:29377: exact active OLS/ChEBI term | context_only | sodium carbonate; formula=['CO3.2Na']; active=True |
| E-CHEBI-30753 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753; CHEBI:30753: exact active OLS/ChEBI term | context_only | 4-aminobenzoic acid; formula=['C7H7NO2']; active=True |
| E-CHEBI-30961 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961; CHEBI:30961: exact active OLS/ChEBI term | context_only | pyridoxine hydrochloride; formula=['C8H11NO3.HCl']; active=True |
| E-CHEBI-31206 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206; CHEBI:31206: exact active OLS/ChEBI term | context_only | ammonium chloride; formula=['Cl.H4N']; active=True |
| E-CHEBI-31345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345; CHEBI:31345: exact active OLS/ChEBI term | context_only | Calcium pantothenate; formula=['2C9H16NO5.Ca']; active=True |
| E-CHEBI-32145 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145; CHEBI:32145: exact active OLS/ChEBI term | context_only | sodium hydroxide; formula=['HO.Na']; active=True |
| E-CHEBI-32149 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149; CHEBI:32149: exact active OLS/ChEBI term | context_only | sodium sulfate; formula=['2Na.O4S']; active=True |
| E-CHEBI-32588 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588; CHEBI:32588: exact active OLS/ChEBI term | context_only | potassium chloride; formula=['Cl.K']; active=True |
| E-CHEBI-33118 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118; CHEBI:33118: exact active OLS/ChEBI term | context_only | boric acid; formula=['H3BO3']; active=True |
| E-CHEBI-34887 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887; CHEBI:34887: exact active OLS/ChEBI term | context_only | nickel dichloride; formula=['Cl2Ni']; active=True |
| E-CHEBI-49105 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105; CHEBI:49105: exact active OLS/ChEBI term | context_only | thiamine hydrochloride; formula=['C12H17N4OS.Cl.HCl']; active=True |
| E-CHEBI-49976 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976; CHEBI:49976: exact active OLS/ChEBI term | context_only | zinc dichloride; formula=['2Cl.Zn']; active=True |
| E-CHEBI-53503 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503; CHEBI:53503: exact active OLS/ChEBI term | context_only | cobalt chloride hexahydrate; formula=['2Cl.Co.6H2O']; active=True |
| E-CHEBI-53542 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542; CHEBI:53542: exact active OLS/ChEBI term | context_only | nickel chloride hexahydrate; formula=['2Cl.6H2O.Ni']; active=True |
| E-CHEBI-63036 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036; CHEBI:63036: exact active OLS/ChEBI term | context_only | potassium dihydrogen phosphate; formula=['H2O4P.K']; active=True |
| E-CHEBI-63939 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939; CHEBI:63939: exact active OLS/ChEBI term | context_only | sodium tungstate dihydrate; formula=['2H2O.2Na.O4W']; active=True |
| E-CHEBI-64103 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64103; CHEBI:64103: exact active OLS/ChEBI term | context_only | sodium butyrate; formula=['C4H7O2.Na']; active=True |
| E-CHEBI-75213 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213; CHEBI:75213: exact active OLS/ChEBI term | context_only | sodium molybdate dihydrate; formula=['2H2O.MoO4.2Na']; active=True |
| E-CHEBI-76209 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209; CHEBI:76209: exact active OLS/ChEBI term | context_only | sodium sulfide nonahydrate; formula=['9H2O.2Na.S']; active=True |
| E-CHEBI-86158 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158; CHEBI:86158: exact active OLS/ChEBI term | context_only | calcium chloride dihydrate; formula=['Ca.2Cl.2H2O']; active=True |
| E-CHEBI-86249 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249; CHEBI:86249: exact active OLS/ChEBI term | context_only | iron dichloride tetrahydrate; formula=['Cl2Fe.4H2O']; active=True |
| E-CHEBI-86318 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318; CHEBI:86318: exact active OLS/ChEBI term | context_only | copper(II) chloride dihydrate; formula=['Cl2Cu.2H2O']; active=True |
| E-CHEBI-86345 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345; CHEBI:86345: exact active OLS/ChEBI term | context_only | magnesium dichloride hexahydrate; formula=['2Cl.6H2O.Mg']; active=True |
| E-CHEBI-86368 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368; CHEBI:86368: exact active OLS/ChEBI term | context_only | manganese(II) chloride tetrahydrate; formula=['Cl2Mn.4H2O']; active=True |
| E-CHEBI-8806 | https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806; CHEBI:8806: exact active OLS/ChEBI term | context_only | Resazurin; formula=['C12H7NO4']; active=True |

## Limits And Additional Notes

- Completed assessment means the declared record was reviewed, not scientifically approved: two blocker and three major findings remain open.
- Exact KOMODO source formulation is inaccessible in the bounded search. DSM association and historical copied composition do not prove source equivalence.
- No scientific inputs were corrected or regenerated. Source-equivalence, dose basis and current formulation grouping require a separately verified correction; follow-up is filed in issue749.
- Native references checked zero evidence assertions; configured term checks do not independently validate every chemical supplied form.
- B12 is a broad class; lipoic stereochemistry and generic calcium-pantothenate specificity are not made more precise than their sources. HCl percentage basis/density is not invented.
- Raw primary captures, runtime logs and peer records are retained under ignored .temp with input hashes, not published as reusable source corpora. Working-tree hashes attest examined bytes; Git base remains dda27db.
- The broader history/ID/product/corpus and merge-freshness gates are not claimed executed by this read-only scientific assessment; no source/ID/product mutation required those gates in this canary.
- Initial native inspect failed because a metadata filename was mistyped; the failed receipt is preserved and the corrected/final native inspections succeeded.
- The original approval rejections were superseded by direct user continuation approval before environment setup; no bypass was used.
- Optional medium119 supplementation is retained as supported prose, not a missing mandatory component.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261115T080257Z-batch079-record07-desulfothermus
kind: record
repository: CultureBotAI/CultureMech
title: 'Recovered batch079 record07: DSMZ876 scientific assessment'
started_at: '2026-11-15T07:56:56Z'
finished_at: '2026-11-15T08:02:57Z'
reviewer:
  identity: Codex recovery reviewer
  kind: agent
  independence: independent
  independence_basis: Reviewer did not author or alter the existing scientific inputs.
    Independent source and chemical peer contributions were checked against current
    bytes and inspected authorities. This is not human approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Completed bounded assessment of one generated record with both maintained
  owners as context. Source tables confirm stock/root representation defects, stale
  generated content, two chemical-form mismatches and unresolved preparation/source
  scope. Native diagnostic passes do not change this verdict. No scientific record
  was edited.
source:
  git_revision: dda27db28f1e5f4f05da6d92fbd2cc1bd6e8add3
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: 846db73710b3134ef5267ce486d151e297295282dc5e9249658592432f8d6a7a
    role: context
  - path: .claude/skills/review-ingredient-concentrations/references/evidence-contract.md
    sha256: 5eb4783f02a0567b45b462dfb5e8c0393fb34daf842a3ce23ff7946652f157d1
    role: context
  - path: .claude/skills/review-recipes/reference/validation-rules.md
    sha256: 3b8666d58fc0c9deb02981053a50760a937675e6e22a6ecd53e92678e8d422f0
    role: context
  - path: .temp/batch079-scientific-20261114/peer-review-record07.md
    sha256: 2dea97a18d835d50c9a2f92175e746b1426a7279b2c617d813be9ab4c85ea53c
    role: context
  - path: .temp/batch079-scientific-20261114/record07/DSMZ_Medium876.pdf
    sha256: 0f220aeeeed3e75c95b9a1a18743407822c467004c76226a5588cd6709dd335e
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/CHEBI_114126.json
    sha256: 53e3e60061626a0ea56edd9bac24718ceedce02758d8738235a148e9ab61d95f
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/CHEBI_131361.json
    sha256: 643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/CHEBI_132751.json
    sha256: 509a9cc0fafffbbccf4801dc30121b1cf3d5d176746d0003356be395faf625e9
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/CHEBI_15940.json
    sha256: ba646eb565dda766d0398c467e4c55effd4376b5d30134b22773e694ae6186f7
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/CHEBI_15956.json
    sha256: 70707d310306fa19de0c6a9d43a7a2abeb3b59161f295e5e1bf888c4a347cd20
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/CHEBI_16494.json
    sha256: aa3c1003d6266cc48f19a4d1d9527edd6844b96094a911e9a3c4f6a8851444e1
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/CHEBI_17015.json
    sha256: cd0f9bb993f17848e326fb7580ed311820332c5850a77122e2a12c47c72e6022
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/CHEBI_176843.json
    sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/CHEBI_17883.json
    sha256: 1c4c2e8e3474319ab5fb79041b19cabfae42f4360729a7569f8a943a503d2f6a
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/CHEBI_26710.json
    sha256: 263497ec2251a5547afabcfd16c9c4c90a8906f0b09e79bb1d6d5f36211b17e8
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/CHEBI_27470.json
    sha256: b10d7468d09b64b3175ed33f6da7b91930c4a06f58de48c41e8ff558fdf64400
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/CHEBI_29377.json
    sha256: d762286083196442ea72280ad6e8cbdfd43d355fe40a80cee5562a57bf1ae3a3
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/CHEBI_30753.json
    sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/CHEBI_30961.json
    sha256: 3ddda602b527dd6fe27be17939aa67b919cd7c14ff127e459f6b0aaaa362cbd3
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/CHEBI_31206.json
    sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/CHEBI_31345.json
    sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/CHEBI_32145.json
    sha256: 2373bbcef187826c692b5378554daa4d799085002aa8616ff418e067655027b7
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/CHEBI_32149.json
    sha256: 969ae214c947d944eb086715a9f43a67e02b889258f6c61a64eb2a17b882b9a0
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/CHEBI_32588.json
    sha256: 216d4ddec877706842671317d1fba8c29a6c66f46a811f1661471222b4652f3f
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/CHEBI_33118.json
    sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/CHEBI_34887.json
    sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/CHEBI_49105.json
    sha256: e389d4e22c1155379a117cd26c5e997bbafce3ad00deea5aee9231de2f35a067
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/CHEBI_49976.json
    sha256: 7b8e2fc9cccc968d43ee39996916da9f300a4d411d7ca0ce7d9ce477e8c2236b
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/CHEBI_53503.json
    sha256: c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/CHEBI_53542.json
    sha256: 423c21fd3715257bbccc1ad83ef3b8e438ffe20f02418e2b202886237c4ea112
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/CHEBI_63036.json
    sha256: 52c051eb66c85e0955858b2780078900c6e37d77d4824af7eb8595a19f9168f4
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/CHEBI_63939.json
    sha256: 987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/CHEBI_64103.json
    sha256: ba9facc4882668ea0efa5236ed77c4ac9c53376c613bece8c0f744b3c93f3e9f
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/CHEBI_75213.json
    sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/CHEBI_76209.json
    sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/CHEBI_86158.json
    sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/CHEBI_86249.json
    sha256: 63bb84e7a947d2a3db0e5f23cf6a533bda2eee137020d7bbe2590477131c5683
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/CHEBI_86318.json
    sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/CHEBI_86345.json
    sha256: cdf62749dcbfbfaa3b7d424c018306977fd107a3387f104f7f1a1bfa00b9adf7
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/CHEBI_86368.json
    sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/CHEBI_8806.json
    sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/chemical-identity-assessment.json
    sha256: 67e924d2e47594e4581f556556a2b1731cbdb65437ed125b6d162d827ec2a695
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/direct-pin-receipt.json
    sha256: 0ba47c2aa94a3032bed649e5156a83c2363d0c96737ca376e0570ac5d900d123
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/input-slots.json
    sha256: 96191e7f49d9dc27ba87a08d8f3c755f3bb684bc983cf95904468589f5c8bc7a
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/mim-exact-label-rows.json
    sha256: ed1949cdb4ecdd927c062429a2fb1e939a76df7535a9f22c01dfb254bbf9f844
    role: context
  - path: .temp/batch079-scientific-20261114/record07/chemical-identity-tsb-20261115T075834261194Z/ols-capture-catalog.json
    sha256: 7676cab706bad3e3fb6878c23687b3ab61d2d3c83fb0b365a55db7c778b5a774
    role: context
  - path: .temp/batch079-scientific-20261114/record07/claim-inventory.json
    sha256: 6b5899923b5c21b46a1369013e38a792b6a6e114214700054f9db83a55f17023
    role: context
  - path: .temp/batch079-scientific-20261114/record07/composition876.json
    sha256: b0e61952ab6a0247d4f123cff0d833006e106f64d582ef669e62745b4df4b451
    role: context
  - path: .temp/batch079-scientific-20261114/record07/medium876.json
    sha256: 015433bc7d2e5e0569eeab5fceb8715eb323c089cf8a2f45b1e9d35d910f7a5a
    role: context
  - path: AGENTS.md
    sha256: 61991a89af8cb8d55b19dbb4a512656a438087b9f712174de99234b43183c3e5
    role: context
  - path: data/merge_yaml/merged/DESULFOTHERMUS_NAPHTHAE_MEDIUM.yaml
    sha256: 63fdec4987631ed6b6c79ca7ca860a7fb97d6f2c8a564590e9cf2d0859777d32
    role: target
  - path: data/normalized_yaml/bacterial/KOMODO_876_TD3-MEDIUM.yaml
    sha256: 5b5126bf5f64c5014d0bb5dcde23d0c316183cdb0b7704075a92ab55c53fddf5
    role: context
  - path: data/normalized_yaml/bacterial/desulfothermus_naphthae_medium.yaml
    sha256: 01491b228a53280acffbce625fd56bff926613b37e4d5e0153f61ce0d9a10c60
    role: context
  - path: docs/record-review-profile.md
    sha256: 99eebe27f0079cb816c974f58ee457148da5a3c346ec9c30ff853b95dade9127
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: pyproject.toml
    sha256: b79f4f49058ed840aa1060e278575e5100102817cbc091d4ae205d1b72b4e246
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/batch079_record07_inventory.py
    sha256: 79c29544e484721dfb586ed306ba876af7a4b3ff4e54fdc1e9e1902e9f9d9fce
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.csv
    sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
    role: context
  - path: src/culturemech/data/mediaingredientmech/label_index.metadata.json
    sha256: 67547827490f422d33e6c06c607caad685e9a49225f76d716c0bc2736d4acff3
    role: context
  - path: src/culturemech/ingredients/mim_label_index.py
    sha256: e07eb72fe91743859451d1998dfeafe58a40dad43baa82d710a740c47dc4bf61
    role: context
  - path: src/culturemech/merge/formulation.py
    sha256: 985289c6afd0fa07296b784b159ef023096b8c7ab72a1cbbed0eb397dedea9ab
    role: context
  - path: src/culturemech/merge/matcher.py
    sha256: 5ac2cbf1aba823a53b2d22877270246e19fdad21c1881dc3047054a3bf5b6885
    role: context
  - path: src/culturemech/merge/merge_recipes.py
    sha256: ce00a4b4e0bc2fa9a63e8b33f4a591cb20984569e125d395af40f5b7e84766a7
    role: context
  - path: src/culturemech/merge/merger.py
    sha256: b81b498bd0da08c774b5412add4044fa962a8d9bea681d2a7f4e45f4639b7ff6
    role: context
  - path: src/culturemech/schema/culturemech.yaml
    sha256: 43725a6b518253da59235a20fa684f0332f2fd83ef852b2463c9e4d0cf1be9d5
    role: context
  - path: uv.lock
    sha256: 9848d8c59d7162ee7a1e3a29b6318768ed613a8920e196b2e976a89ba9a11f55
    role: context
scope:
  description: 'Record07 only: full generated target and its two maintained owners,
    every ingredient/stock entry, preparation, source provenance and chemical IDs.'
  selection: Recovered batch079 selection identifies CultureMech:002034; exact paths
    and IDs checked.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CultureMech:002034
  exclusions:
  - target: batch079 records01–06 and09
    reason: Historical receipts preserved, not reassessed or claimed complete.
  - target: batch079 records08 and10
    reason: Deferred until this canary is validated, saved and verified.
  - target: PR692, variant queue, catalog-wide repair and KG-Microbe workflow work
    reason: Separate scopes; this report makes no release/admission decision.
targets:
- target_id: CultureMech:002034
  path: data/merge_yaml/merged/DESULFOTHERMUS_NAPHTHAE_MEDIUM.yaml
  label: DESULFOTHERMUS NAPHTHAE MEDIUM
  record_class: MediaRecipe
  kind: generated
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_876_TD3-MEDIUM.yaml
    role: normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfothermus_naphthae_medium.yaml
    role: normalized source
checks:
- check_id: C-record07-schema
  name: Native schema
  status: passed
  required: true
  target_ids:
  - CultureMech:002034
  exit_code: 0
  command: just validate-schema data/merge_yaml/merged/DESULFOTHERMUS_NAPHTHAE_MEDIUM.yaml
  summary: Open-schema structure only.
  scope_note: Actual output, timing and exit retained at .temp/batch079-scientific-20261114/20261115T075705104393Z-record07-schema.json
- check_id: C-record07-strict
  name: Native strict schema
  status: passed
  required: true
  target_ids:
  - CultureMech:002034
  exit_code: 0
  command: just validate-strict data/merge_yaml/merged/DESULFOTHERMUS_NAPHTHAE_MEDIUM.yaml
    --out .temp/batch079-scientific-20261114/record07/strict.tsv --workers 1 --quiet
  summary: One file, schema layer, zero errors; not a whole-repository QC sweep.
  scope_note: Actual output, timing and exit retained at .temp/batch079-scientific-20261114/20261115T075705924125Z-record07-strict.json
- check_id: C-record07-terms
  name: Native term validator
  status: passed
  required: true
  target_ids:
  - CultureMech:002034
  exit_code: 0
  command: just validate-terms data/merge_yaml/merged/DESULFOTHERMUS_NAPHTHAE_MEDIUM.yaml
  summary: Configured bound slots only; chemical term slots are not fully bound and
    this does not establish supplied-form identity.
  scope_note: Actual output, timing and exit retained at .temp/batch079-scientific-20261114/20261115T075713230348Z-record07-terms.json
- check_id: C-record07-references
  name: Native reference validator
  status: passed
  required: true
  target_ids:
  - CultureMech:002034
  exit_code: 0
  command: just validate-references data/merge_yaml/merged/DESULFOTHERMUS_NAPHTHAE_MEDIUM.yaml
  summary: ZERO evidence assertions checked; no evidence completeness or scientific
    approval implied.
  scope_note: Actual output, timing and exit retained at .temp/batch079-scientific-20261114/20261115T075714381035Z-record07-references.json
- check_id: C-mim-index
  name: Packaged MIM snapshot integrity
  status: passed
  required: true
  target_ids:
  - CultureMech:002034
  exit_code: 0
  command: just check-mim-label-index
  summary: Byte/hash/row/contract integrity only; no external chemical proof.
  scope_note: Actual output, timing and exit retained at .temp/batch079-scientific-20261114/20261115T075806642481Z-mim-index.json
- check_id: C-inspect
  name: Native input inspection
  status: passed
  required: true
  exit_code: 0
  target_ids:
  - CultureMech:002034
  summary: Native inspect captured every final local assessment input; original inputs
    rechecked without recipe changes.
  scope_note: .temp/batch079-scientific-20261114/20261115T080039435860Z-record07-inspect-final.json
- check_id: C-science
  name: Primary-source scientific assessment
  status: failed
  required: true
  target_ids:
  - CultureMech:002034
  summary: Assessment completed and found critical stock representation and exact-form
    defects; failed scientific acceptance is retained as needs_curation.
  evidence_ids:
  - E-record
  - E-primary
  - E-structured
  - E-CHEBI-34887
  - E-CHEBI-53542
  - E-CHEBI-8806
- check_id: C-history
  name: Read-only history and ownership review
  status: passed
  required: true
  target_ids:
  - CultureMech:002034
  summary: Historical provenance and maintained/generated boundaries read; no history
    edited or native scientific status promoted. Native validate-history targets separate
    session HistoryRecords, not these embedded event arrays.
  evidence_ids:
  - E-record
  - E-generator
- check_id: C-komodo
  name: Exact KOMODO recipe retrieval
  status: unavailable
  required: false
  target_ids:
  - CultureMech:002034
  summary: Exact servlet routes failed in bounded peer source review; no usable independent
    KOMODO formulation recovered. This is an unresolved source-identity finding, not
    an inferred equality.
  scope_note: DSMZ876 and the imported-owner history establish the conflict; unverified
    KOMODO equivalence remains an explicit limitation.
evidence:
- evidence_id: E-record
  kind: record_content
  reference: data/merge_yaml/merged/DESULFOTHERMUS_NAPHTHAE_MEDIUM.yaml
  accessed_at: '2026-11-15T08:02:57Z'
  support: context_only
  summary: Complete generated YAML and both complete maintained owners read; input
    hashes verified. Generated37 root ingredients/no solutions; each owner31 root
    ingredients and10 nested components.
  snapshot_sha256: 63fdec4987631ed6b6c79ca7ca860a7fb97d6f2c8a564590e9cf2d0859777d32
- evidence_id: E-primary
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium876.pdf
  locator: 'Pages1–2: basal recipe, preparation and four separate stock tables'
  accessed_at: '2026-11-15T07:58:11Z'
  support: partial
  summary: Official formulation distinguishes basal ingredients, SL-10, selenite/tungstate
    and two vitamin stocks; supports anoxic preparation, pH and optional fatty-acid
    supplementation.
  snapshot_sha256: 0f220aeeeed3e75c95b9a1a18743407822c467004c76226a5588cd6709dd335e
- evidence_id: E-structured
  kind: database
  reference: https://mediadive.dsmz.de/download/medium/876/json
  locator: solutions1815,595,777,5980,1038; full separate recipe tables
  accessed_at: '2026-11-15T07:58:08Z'
  support: partial
  summary: Provider records1005mL main volume and1000mL stocks. Twelve main rates
    match local values; stock rates must retain their separate solution context. Provider
    conversion is not independent proof of percentage basis or chemical grounding.
  snapshot_sha256: 015433bc7d2e5e0569eeab5fceb8715eb323c089cf8a2f45b1e9d35d910f7a5a
- evidence_id: E-flattened
  kind: database
  reference: https://mediadive.dsmz.de/download/composition/876/json
  locator: Pyridoxine hydrochloride row compared with both primary vitamin stocks
  accessed_at: '2026-11-15T07:58:08Z'
  support: refutes
  summary: Flattened pyridoxine0.000298507g/L captures only the0.3g/L stock contribution
    at1mL/1005mL, although the other stock also supplies0.1g/L at1mL/1005mL. This
    endpoint is not an authoritative total oracle.
  snapshot_sha256: b0e61952ab6a0247d4f123cff0d833006e106f64d582ef669e62745b4df4b451
- evidence_id: E-119
  kind: primary_source
  reference: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium119.pdf
  locator: Fatty acid mixture subsection, pages2–3 only
  accessed_at: '2026-11-15T08:02:57Z'
  support: supports
  summary: The referenced mixture is a separate preparation. Existing optional1%v/v
    prose correctly transfers this mixture only; no medium119 basal recipe, organism
    claims or gas conditions are transferred.
- evidence_id: E-mim
  kind: record_content
  reference: src/culturemech/data/mediaingredientmech/label_index.csv
  locator: Pinned metadata; exact label rows retained in input snapshot
  accessed_at: '2026-11-15T08:02:57Z'
  support: context_only
  summary: Snapshot6643131b0f12ab40b66f98135245fca04027e0e9 passes native integrity
    check. Nickel exact-label rows include a rejected preferred row and mapped synonym,
    both53542; sodium-resazurin synonym maps8806. Resolver policy and chemical truth
    are separate.
  snapshot_sha256: 4765c45d026f7f8e83e056043efb16f8f736e1a871eb168b151092ca2c934ae5
- evidence_id: E-peer
  kind: prior_review
  reference: .temp/batch079-scientific-20261114/peer-review-record07.md
  accessed_at: '2026-11-15T08:02:57Z'
  support: context_only
  summary: Independent source peer supplied by coordinating root; current input and
    primary citations rechecked by the author before adopting findings.
  snapshot_sha256: 2dea97a18d835d50c9a2f92175e746b1426a7279b2c617d813be9ab4c85ea53c
- evidence_id: E-generator
  kind: record_content
  reference: src/culturemech/merge/formulation.py
  accessed_at: '2026-11-15T08:02:57Z'
  support: context_only
  summary: Current generator requires exact formulation assertions, including stocks,
    notes and conditions. Historical ingredient-set grouping is not permission to
    force the two differing owners into one regenerated target.
- evidence_id: E-CHEBI-114126
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_114126
  locator: 'CHEBI:114126: exact active OLS/ChEBI term'
  accessed_at: '2026-11-15T07:58:34.319925Z'
  support: context_only
  summary: sodium hexanoate; formula=['C6H11O2.Na']; active=True
  snapshot_sha256: 53e3e60061626a0ea56edd9bac24718ceedce02758d8738235a148e9ab61d95f
- evidence_id: E-CHEBI-131361
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_131361
  locator: 'CHEBI:131361: exact active OLS/ChEBI term'
  accessed_at: '2026-11-15T07:58:34.320003Z'
  support: context_only
  summary: disodium selenite pentahydrate; formula=['5H2O.2Na.O3Se']; active=True
  snapshot_sha256: 643fefa89a2c0afeb2a00a0dd6149dbbf86cc4824369c58bde1c6ea6d4316d10
- evidence_id: E-CHEBI-132751
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_132751
  locator: 'CHEBI:132751: exact active OLS/ChEBI term'
  accessed_at: '2026-11-15T07:58:34.320072Z'
  support: context_only
  summary: thiamine hydrochloride dihydrate; formula=['C12H18N4OS.2Cl.2H2O']; active=True
  snapshot_sha256: 509a9cc0fafffbbccf4801dc30121b1cf3d5d176746d0003356be395faf625e9
- evidence_id: E-CHEBI-15940
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15940
  locator: 'CHEBI:15940: exact active OLS/ChEBI term'
  accessed_at: '2026-11-15T07:58:34.320122Z'
  support: context_only
  summary: nicotinic acid; formula=['C6H5NO2']; active=True
  snapshot_sha256: ba646eb565dda766d0398c467e4c55effd4376b5d30134b22773e694ae6186f7
- evidence_id: E-CHEBI-15956
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_15956
  locator: 'CHEBI:15956: exact active OLS/ChEBI term'
  accessed_at: '2026-11-15T07:58:35.013257Z'
  support: context_only
  summary: biotin; formula=['C10H16N2O3S']; active=True
  snapshot_sha256: 70707d310306fa19de0c6a9d43a7a2abeb3b59161f295e5e1bf888c4a347cd20
- evidence_id: E-CHEBI-16494
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_16494
  locator: 'CHEBI:16494: exact active OLS/ChEBI term'
  accessed_at: '2026-11-15T07:58:35.016299Z'
  support: context_only
  summary: lipoic acid; formula=['C8H14O2S2']; active=True
  snapshot_sha256: aa3c1003d6266cc48f19a4d1d9527edd6844b96094a911e9a3c4f6a8851444e1
- evidence_id: E-CHEBI-17015
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17015
  locator: 'CHEBI:17015: exact active OLS/ChEBI term'
  accessed_at: '2026-11-15T07:58:35.016526Z'
  support: context_only
  summary: riboflavin; formula=['C17H20N4O6']; active=True
  snapshot_sha256: cd0f9bb993f17848e326fb7580ed311820332c5850a77122e2a12c47c72e6022
- evidence_id: E-CHEBI-176843
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_176843
  locator: 'CHEBI:176843: exact active OLS/ChEBI term'
  accessed_at: '2026-11-15T07:58:35.240788Z'
  support: context_only
  summary: vitamin B12; formula=None; active=True
  snapshot_sha256: b535c3de88f47e93aed8909c58ff4e2d054a6845dea3bc9a048c18df12b371a9
- evidence_id: E-CHEBI-17883
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_17883
  locator: 'CHEBI:17883: exact active OLS/ChEBI term'
  accessed_at: '2026-11-15T07:58:35.656872Z'
  support: context_only
  summary: hydrogen chloride; formula=['HCl']; active=True
  snapshot_sha256: 1c4c2e8e3474319ab5fb79041b19cabfae42f4360729a7569f8a943a503d2f6a
- evidence_id: E-CHEBI-26710
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_26710
  locator: 'CHEBI:26710: exact active OLS/ChEBI term'
  accessed_at: '2026-11-15T07:58:35.761355Z'
  support: context_only
  summary: sodium chloride; formula=['Cl.Na']; active=True
  snapshot_sha256: 263497ec2251a5547afabcfd16c9c4c90a8906f0b09e79bb1d6d5f36211b17e8
- evidence_id: E-CHEBI-27470
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_27470
  locator: 'CHEBI:27470: exact active OLS/ChEBI term'
  accessed_at: '2026-11-15T07:58:35.830611Z'
  support: context_only
  summary: folic acid; formula=['C19H19N7O6']; active=True
  snapshot_sha256: b10d7468d09b64b3175ed33f6da7b91930c4a06f58de48c41e8ff558fdf64400
- evidence_id: E-CHEBI-29377
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_29377
  locator: 'CHEBI:29377: exact active OLS/ChEBI term'
  accessed_at: '2026-11-15T07:58:36.184144Z'
  support: context_only
  summary: sodium carbonate; formula=['CO3.2Na']; active=True
  snapshot_sha256: d762286083196442ea72280ad6e8cbdfd43d355fe40a80cee5562a57bf1ae3a3
- evidence_id: E-CHEBI-30753
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30753
  locator: 'CHEBI:30753: exact active OLS/ChEBI term'
  accessed_at: '2026-11-15T07:58:36.300144Z'
  support: context_only
  summary: 4-aminobenzoic acid; formula=['C7H7NO2']; active=True
  snapshot_sha256: 97ea54b8020d3bcda2478182be115d2bc632249ee22b197b0575a4a9fd5fe21a
- evidence_id: E-CHEBI-30961
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_30961
  locator: 'CHEBI:30961: exact active OLS/ChEBI term'
  accessed_at: '2026-11-15T07:58:36.570682Z'
  support: context_only
  summary: pyridoxine hydrochloride; formula=['C8H11NO3.HCl']; active=True
  snapshot_sha256: 3ddda602b527dd6fe27be17939aa67b919cd7c14ff127e459f6b0aaaa362cbd3
- evidence_id: E-CHEBI-31206
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31206
  locator: 'CHEBI:31206: exact active OLS/ChEBI term'
  accessed_at: '2026-11-15T07:58:36.575306Z'
  support: context_only
  summary: ammonium chloride; formula=['Cl.H4N']; active=True
  snapshot_sha256: ee305afe3bf4a52b81b433055fe3908296a177700fcb477572e51c08e2b81c76
- evidence_id: E-CHEBI-31345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_31345
  locator: 'CHEBI:31345: exact active OLS/ChEBI term'
  accessed_at: '2026-11-15T07:58:36.800236Z'
  support: context_only
  summary: Calcium pantothenate; formula=['2C9H16NO5.Ca']; active=True
  snapshot_sha256: 56fc4b33c78d82faf317e131ae936f2e00eab0c369b2a9d8be86eddff6fd616d
- evidence_id: E-CHEBI-32145
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32145
  locator: 'CHEBI:32145: exact active OLS/ChEBI term'
  accessed_at: '2026-11-15T07:58:36.955511Z'
  support: context_only
  summary: sodium hydroxide; formula=['HO.Na']; active=True
  snapshot_sha256: 2373bbcef187826c692b5378554daa4d799085002aa8616ff418e067655027b7
- evidence_id: E-CHEBI-32149
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32149
  locator: 'CHEBI:32149: exact active OLS/ChEBI term'
  accessed_at: '2026-11-15T07:58:37.171101Z'
  support: context_only
  summary: sodium sulfate; formula=['2Na.O4S']; active=True
  snapshot_sha256: 969ae214c947d944eb086715a9f43a67e02b889258f6c61a64eb2a17b882b9a0
- evidence_id: E-CHEBI-32588
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_32588
  locator: 'CHEBI:32588: exact active OLS/ChEBI term'
  accessed_at: '2026-11-15T07:58:37.244659Z'
  support: context_only
  summary: potassium chloride; formula=['Cl.K']; active=True
  snapshot_sha256: 216d4ddec877706842671317d1fba8c29a6c66f46a811f1661471222b4652f3f
- evidence_id: E-CHEBI-33118
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_33118
  locator: 'CHEBI:33118: exact active OLS/ChEBI term'
  accessed_at: '2026-11-15T07:58:37.420959Z'
  support: context_only
  summary: boric acid; formula=['H3BO3']; active=True
  snapshot_sha256: f1ed0fa3a5355bbef1d9200ab8b7c46ce02b96fbf5d86b931208709e57b83f87
- evidence_id: E-CHEBI-34887
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_34887
  locator: 'CHEBI:34887: exact active OLS/ChEBI term'
  accessed_at: '2026-11-15T07:58:37.559915Z'
  support: context_only
  summary: nickel dichloride; formula=['Cl2Ni']; active=True
  snapshot_sha256: f42ee4bb41f919ba75269a1e5d5a023a3e4bd67b7acabd1439a2ecb5e3ac9ddc
- evidence_id: E-CHEBI-49105
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49105
  locator: 'CHEBI:49105: exact active OLS/ChEBI term'
  accessed_at: '2026-11-15T07:58:37.798012Z'
  support: context_only
  summary: thiamine hydrochloride; formula=['C12H17N4OS.Cl.HCl']; active=True
  snapshot_sha256: e389d4e22c1155379a117cd26c5e997bbafce3ad00deea5aee9231de2f35a067
- evidence_id: E-CHEBI-49976
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_49976
  locator: 'CHEBI:49976: exact active OLS/ChEBI term'
  accessed_at: '2026-11-15T07:58:37.981722Z'
  support: context_only
  summary: zinc dichloride; formula=['2Cl.Zn']; active=True
  snapshot_sha256: 7b8e2fc9cccc968d43ee39996916da9f300a4d411d7ca0ce7d9ce477e8c2236b
- evidence_id: E-CHEBI-53503
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53503
  locator: 'CHEBI:53503: exact active OLS/ChEBI term'
  accessed_at: '2026-11-15T07:58:38.048871Z'
  support: context_only
  summary: cobalt chloride hexahydrate; formula=['2Cl.Co.6H2O']; active=True
  snapshot_sha256: c33e304a0a565068c592ba0970e501052981599ef69cd2cb901e88f27931389d
- evidence_id: E-CHEBI-53542
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_53542
  locator: 'CHEBI:53542: exact active OLS/ChEBI term'
  accessed_at: '2026-11-15T07:58:38.164168Z'
  support: context_only
  summary: nickel chloride hexahydrate; formula=['2Cl.6H2O.Ni']; active=True
  snapshot_sha256: 423c21fd3715257bbccc1ad83ef3b8e438ffe20f02418e2b202886237c4ea112
- evidence_id: E-CHEBI-63036
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63036
  locator: 'CHEBI:63036: exact active OLS/ChEBI term'
  accessed_at: '2026-11-15T07:58:38.440569Z'
  support: context_only
  summary: potassium dihydrogen phosphate; formula=['H2O4P.K']; active=True
  snapshot_sha256: 52c051eb66c85e0955858b2780078900c6e37d77d4824af7eb8595a19f9168f4
- evidence_id: E-CHEBI-63939
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_63939
  locator: 'CHEBI:63939: exact active OLS/ChEBI term'
  accessed_at: '2026-11-15T07:58:38.626864Z'
  support: context_only
  summary: sodium tungstate dihydrate; formula=['2H2O.2Na.O4W']; active=True
  snapshot_sha256: 987144fa0342502834f116860a4b4f71696f62c18e7b701301667c15e588562a
- evidence_id: E-CHEBI-64103
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_64103
  locator: 'CHEBI:64103: exact active OLS/ChEBI term'
  accessed_at: '2026-11-15T07:58:38.661324Z'
  support: context_only
  summary: sodium butyrate; formula=['C4H7O2.Na']; active=True
  snapshot_sha256: ba9facc4882668ea0efa5236ed77c4ac9c53376c613bece8c0f744b3c93f3e9f
- evidence_id: E-CHEBI-75213
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_75213
  locator: 'CHEBI:75213: exact active OLS/ChEBI term'
  accessed_at: '2026-11-15T07:58:38.758547Z'
  support: context_only
  summary: sodium molybdate dihydrate; formula=['2H2O.MoO4.2Na']; active=True
  snapshot_sha256: b550cc83b4a37e7b1710a3221c77e7899e27a6bd0696df85cdd84a03b99b8083
- evidence_id: E-CHEBI-76209
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_76209
  locator: 'CHEBI:76209: exact active OLS/ChEBI term'
  accessed_at: '2026-11-15T07:58:39.257099Z'
  support: context_only
  summary: sodium sulfide nonahydrate; formula=['9H2O.2Na.S']; active=True
  snapshot_sha256: f74d2c85574a4e28bdf71a78e4263f7e4c211036cd6d63b1f8282aca1d255e5c
- evidence_id: E-CHEBI-86158
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86158
  locator: 'CHEBI:86158: exact active OLS/ChEBI term'
  accessed_at: '2026-11-15T07:58:39.265158Z'
  support: context_only
  summary: calcium chloride dihydrate; formula=['Ca.2Cl.2H2O']; active=True
  snapshot_sha256: b9c4f7706b41224c9f9db6fbb6cb2b6e6ebc73466e115325a646b0122757eb61
- evidence_id: E-CHEBI-86249
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86249
  locator: 'CHEBI:86249: exact active OLS/ChEBI term'
  accessed_at: '2026-11-15T07:58:39.293444Z'
  support: context_only
  summary: iron dichloride tetrahydrate; formula=['Cl2Fe.4H2O']; active=True
  snapshot_sha256: 63bb84e7a947d2a3db0e5f23cf6a533bda2eee137020d7bbe2590477131c5683
- evidence_id: E-CHEBI-86318
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86318
  locator: 'CHEBI:86318: exact active OLS/ChEBI term'
  accessed_at: '2026-11-15T07:58:39.354169Z'
  support: context_only
  summary: copper(II) chloride dihydrate; formula=['Cl2Cu.2H2O']; active=True
  snapshot_sha256: 9bbecfe37d67d923ee070067aebdf1abf21048cdb2cbdff9de0e3d21f68ea1ae
- evidence_id: E-CHEBI-86345
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86345
  locator: 'CHEBI:86345: exact active OLS/ChEBI term'
  accessed_at: '2026-11-15T07:58:39.854061Z'
  support: context_only
  summary: magnesium dichloride hexahydrate; formula=['2Cl.6H2O.Mg']; active=True
  snapshot_sha256: cdf62749dcbfbfaa3b7d424c018306977fd107a3387f104f7f1a1bfa00b9adf7
- evidence_id: E-CHEBI-86368
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_86368
  locator: 'CHEBI:86368: exact active OLS/ChEBI term'
  accessed_at: '2026-11-15T07:58:39.863236Z'
  support: context_only
  summary: manganese(II) chloride tetrahydrate; formula=['Cl2Mn.4H2O']; active=True
  snapshot_sha256: 286a549d903f559a3f24698a85fa4ffcf67bf32032116beaa74088dc9c84a15f
- evidence_id: E-CHEBI-8806
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FCHEBI_8806
  locator: 'CHEBI:8806: exact active OLS/ChEBI term'
  accessed_at: '2026-11-15T07:58:39.939720Z'
  support: context_only
  summary: Resazurin; formula=['C12H7NO4']; active=True
  snapshot_sha256: e4b3829e3ecc9bf2e831f740a736843a425952bd34a410e5c1f8989b3fd62de5
assessments:
- assessment_id: A-identity
  area: identity
  topic: Exact generated target and maintained sources
  outcome: concern
  summary: CultureMech:002034 explicitly denotes DSMZ876. KOMODO876/TD3 is a distinct
    maintained owner with unresolved source-equivalence and atmosphere claims; historical89%-of37
    counterevidence is not a current identity measurement.
  target_ids:
  - CultureMech:002034
  evidence_ids:
  - E-record
  - E-primary
  - E-structured
  - E-generator
- assessment_id: A-main
  area: quantity
  topic: All twelve basal component rates and volume basis
  outcome: supported
  summary: The first twelve local rates match the structured main solution's explicit1005mL
    normalization. They are evidence_only decisions pending claim-level linkage, not
    instructions to replace them using1000mL water.
  target_ids:
  - CultureMech:002034
  evidence_ids:
  - E-record
  - E-structured
- assessment_id: A-amounts
  area: quantity
  topic: Every direct and nested ingredient amount
  outcome: concern
  summary: Reviewed37 generated root rows and41 rows in each owner, including10 existing
    nested components per owner. Correct stock placement before deriving final amounts;
    preserve distinct vitamin additions. No quantity or source field was changed.
  target_ids:
  - CultureMech:002034
  evidence_ids:
  - E-record
  - E-primary
  - E-structured
  - E-flattened
  details: 'data/merge_yaml/merged/DESULFOTHERMUS_NAPHTHAE_MEDIUM.yaml

    ingredients[0]; Na2SO4; retained=3.9801 G_PER_L; evidence_only: main-rate supported
    on provider1005mL basis; source=1815:3.9801g/L-stock-or-main/1005mL-batch

    ingredients[1]; KH2PO4; retained=0.199005 G_PER_L; evidence_only: main-rate supported
    on provider1005mL basis; source=1815:0.199005g/L-stock-or-main/1005mL-batch

    ingredients[2]; NH4Cl; retained=0.248756 G_PER_L; evidence_only: main-rate supported
    on provider1005mL basis; source=1815:0.248756g/L-stock-or-main/1005mL-batch

    ingredients[3]; NaCl; retained=19.9005 G_PER_L; evidence_only: main-rate supported
    on provider1005mL basis; source=1815:19.9005g/L-stock-or-main/1005mL-batch

    ingredients[4]; MgCl2 x 6 H2O; retained=9.75124 G_PER_L; evidence_only: main-rate
    supported on provider1005mL basis; source=1815:9.75124g/L-stock-or-main/1005mL-batch

    ingredients[5]; KCl; retained=0.497512 G_PER_L; evidence_only: main-rate supported
    on provider1005mL basis; source=1815:0.497512g/L-stock-or-main/1005mL-batch

    ingredients[6]; CaCl2 x 2 H2O; retained=0.0995025 G_PER_L; evidence_only: main-rate
    supported on provider1005mL basis; source=1815:0.0995025g/L-stock-or-main/1005mL-batch

    ingredients[7]; Sodium resazurin; retained=0.000497512 G_PER_L; evidence_only:
    main-rate supported on provider1005mL basis; source=1815:0.000497512g/L-stock-or-main/1005mL-batch

    ingredients[8]; Na2CO3; retained=0.995025 G_PER_L; evidence_only: main-rate supported
    on provider1005mL basis; source=1815:0.995025g/L-stock-or-main/1005mL-batch

    ingredients[9]; Na-caproate; retained=0.497512 G_PER_L; evidence_only: main-rate
    supported on provider1005mL basis; source=1815:0.497512g/L-stock-or-main/1005mL-batch

    ingredients[10]; Na-butyrate; retained=0.298507 G_PER_L; evidence_only: main-rate
    supported on provider1005mL basis; source=1815:0.298507g/L-stock-or-main/1005mL-batch

    ingredients[11]; Na2S x 9 H2O; retained=0.39801 G_PER_L; evidence_only: main-rate
    supported on provider1005mL basis; source=1815:0.39801g/L-stock-or-main/1005mL-batch

    ingredients[12]; HCl; retained=2.5 G_PER_L; correct representation: stock-strength/root
    placement or summed separate stocks; no new final concentration asserted; source=595:2.5g/L-stock-or-main/1000mL-batch

    ingredients[13]; FeCl2 x 4 H2O; retained=1.5 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=595:1.5g/L-stock-or-main/1000mL-batch

    ingredients[14]; ZnCl2; retained=0.07 G_PER_L; correct representation: stock-strength/root
    placement or summed separate stocks; no new final concentration asserted; source=595:0.07g/L-stock-or-main/1000mL-batch

    ingredients[15]; MnCl2 x 4 H2O; retained=0.1 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=595:0.1g/L-stock-or-main/1000mL-batch

    ingredients[16]; H3BO3; retained=0.006 G_PER_L; correct representation: stock-strength/root
    placement or summed separate stocks; no new final concentration asserted; source=595:0.006g/L-stock-or-main/1000mL-batch

    ingredients[17]; CoCl2 x 6 H2O; retained=0.19 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=595:0.19g/L-stock-or-main/1000mL-batch

    ingredients[18]; CuCl2 x 2 H2O; retained=0.002 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=595:0.002g/L-stock-or-main/1000mL-batch

    ingredients[19]; NiCl2 x 6 H2O; retained=0.024 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=595:0.024g/L-stock-or-main/1000mL-batch

    ingredients[20]; Na2MoO4 x 2 H2O; retained=0.036 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=595:0.036g/L-stock-or-main/1000mL-batch

    ingredients[21]; NaOH; retained=0.5 G_PER_L; correct representation: stock-strength/root
    placement or summed separate stocks; no new final concentration asserted; source=777:0.5g/L-stock-or-main/1000mL-batch

    ingredients[22]; Na2SeO3 x 5 H2O; retained=0.003 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=777:0.003g/L-stock-or-main/1000mL-batch

    ingredients[23]; Na2WO4 x 2 H2O; retained=0.004 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=777:0.004g/L-stock-or-main/1000mL-batch

    ingredients[24]; Biotin; retained=0.02 G_PER_L; correct representation: stock-strength/root
    placement or summed separate stocks; no new final concentration asserted; source=5980:0.02g/L-stock-or-main/1000mL-batch

    ingredients[25]; Folic acid; retained=0.02 G_PER_L; correct representation: stock-strength/root
    placement or summed separate stocks; no new final concentration asserted; source=5980:0.02g/L-stock-or-main/1000mL-batch

    ingredients[26]; Pyridoxine hydrochloride; retained=0.4 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=5980:0.1g/L-stock-or-main/1000mL-batch, 1038:0.3g/L-stock-or-main/1000mL-batch

    ingredients[27]; Thiamine HCl; retained=0.05 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=5980:0.05g/L-stock-or-main/1000mL-batch

    ingredients[28]; Riboflavin; retained=0.05 G_PER_L; correct representation: stock-strength/root
    placement or summed separate stocks; no new final concentration asserted; source=5980:0.05g/L-stock-or-main/1000mL-batch

    ingredients[29]; Nicotinic acid; retained=0.25 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=5980:0.05g/L-stock-or-main/1000mL-batch, 1038:0.2g/L-stock-or-main/1000mL-batch

    ingredients[30]; Calcium D-(+)-pantothenate; retained=0.05 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=5980:0.05g/L-stock-or-main/1000mL-batch

    ingredients[31]; Vitamin B12; retained=0.101 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=5980:0.001g/L-stock-or-main/1000mL-batch, 1038:0.1g/L-stock-or-main/1000mL-batch

    ingredients[32]; p-Aminobenzoic acid; retained=0.13 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=5980:0.05g/L-stock-or-main/1000mL-batch, 1038:0.08g/L-stock-or-main/1000mL-batch

    ingredients[33]; (DL)-alpha-Lipoic acid; retained=0.05 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=5980:0.05g/L-stock-or-main/1000mL-batch

    ingredients[34]; D-(+)-biotin; retained=0.02 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=1038:0.02g/L-stock-or-main/1000mL-batch

    ingredients[35]; Calcium pantothenate; retained=0.1 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=1038:0.1g/L-stock-or-main/1000mL-batch

    ingredients[36]; Thiamine-HCl x 2 H2O; retained=0.2 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=1038:0.2g/L-stock-or-main/1000mL-batch

    data/normalized_yaml/bacterial/desulfothermus_naphthae_medium.yaml

    ingredients[0]; Na2SO4; retained=3.9801 G_PER_L; evidence_only: main-rate supported
    on provider1005mL basis; source=1815:3.9801g/L-stock-or-main/1005mL-batch

    ingredients[1]; KH2PO4; retained=0.199005 G_PER_L; evidence_only: main-rate supported
    on provider1005mL basis; source=1815:0.199005g/L-stock-or-main/1005mL-batch

    ingredients[2]; NH4Cl; retained=0.248756 G_PER_L; evidence_only: main-rate supported
    on provider1005mL basis; source=1815:0.248756g/L-stock-or-main/1005mL-batch

    ingredients[3]; NaCl; retained=19.9005 G_PER_L; evidence_only: main-rate supported
    on provider1005mL basis; source=1815:19.9005g/L-stock-or-main/1005mL-batch

    ingredients[4]; MgCl2 x 6 H2O; retained=9.75124 G_PER_L; evidence_only: main-rate
    supported on provider1005mL basis; source=1815:9.75124g/L-stock-or-main/1005mL-batch

    ingredients[5]; KCl; retained=0.497512 G_PER_L; evidence_only: main-rate supported
    on provider1005mL basis; source=1815:0.497512g/L-stock-or-main/1005mL-batch

    ingredients[6]; CaCl2 x 2 H2O; retained=0.0995025 G_PER_L; evidence_only: main-rate
    supported on provider1005mL basis; source=1815:0.0995025g/L-stock-or-main/1005mL-batch

    ingredients[7]; Sodium resazurin; retained=0.000497512 G_PER_L; evidence_only:
    main-rate supported on provider1005mL basis; source=1815:0.000497512g/L-stock-or-main/1005mL-batch

    ingredients[8]; Na2CO3; retained=0.995025 G_PER_L; evidence_only: main-rate supported
    on provider1005mL basis; source=1815:0.995025g/L-stock-or-main/1005mL-batch

    ingredients[9]; Na-caproate; retained=0.497512 G_PER_L; evidence_only: main-rate
    supported on provider1005mL basis; source=1815:0.497512g/L-stock-or-main/1005mL-batch

    ingredients[10]; Na-butyrate; retained=0.298507 G_PER_L; evidence_only: main-rate
    supported on provider1005mL basis; source=1815:0.298507g/L-stock-or-main/1005mL-batch

    ingredients[11]; Na2S x 9 H2O; retained=0.39801 G_PER_L; evidence_only: main-rate
    supported on provider1005mL basis; source=1815:0.39801g/L-stock-or-main/1005mL-batch

    ingredients[12]; HCl; retained=2.5 G_PER_L; correct representation: stock-strength/root
    placement or summed separate stocks; no new final concentration asserted; source=595:2.5g/L-stock-or-main/1000mL-batch

    ingredients[13]; ZnCl2; retained=0.07 G_PER_L; correct representation: stock-strength/root
    placement or summed separate stocks; no new final concentration asserted; source=595:0.07g/L-stock-or-main/1000mL-batch

    ingredients[14]; MnCl2 x 4 H2O; retained=0.1 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=595:0.1g/L-stock-or-main/1000mL-batch

    ingredients[15]; H3BO3; retained=0.006 G_PER_L; correct representation: stock-strength/root
    placement or summed separate stocks; no new final concentration asserted; source=595:0.006g/L-stock-or-main/1000mL-batch

    ingredients[16]; CoCl2 x 6 H2O; retained=0.19 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=595:0.19g/L-stock-or-main/1000mL-batch

    ingredients[17]; CuCl2 x 2 H2O; retained=0.002 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=595:0.002g/L-stock-or-main/1000mL-batch

    ingredients[18]; NiCl2 x 6 H2O; retained=0.024 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=595:0.024g/L-stock-or-main/1000mL-batch

    ingredients[19]; Na2MoO4 x 2 H2O; retained=0.036 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=595:0.036g/L-stock-or-main/1000mL-batch

    ingredients[20]; NaOH; retained=0.5 G_PER_L; correct representation: stock-strength/root
    placement or summed separate stocks; no new final concentration asserted; source=777:0.5g/L-stock-or-main/1000mL-batch

    ingredients[21]; Na2SeO3 x 5 H2O; retained=0.003 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=777:0.003g/L-stock-or-main/1000mL-batch

    ingredients[22]; Na2WO4 x 2 H2O; retained=0.004 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=777:0.004g/L-stock-or-main/1000mL-batch

    ingredients[23]; Biotin; retained=0.02 G_PER_L; correct representation: stock-strength/root
    placement or summed separate stocks; no new final concentration asserted; source=5980:0.02g/L-stock-or-main/1000mL-batch

    ingredients[24]; Folic acid; retained=0.02 G_PER_L; correct representation: stock-strength/root
    placement or summed separate stocks; no new final concentration asserted; source=5980:0.02g/L-stock-or-main/1000mL-batch

    ingredients[25]; Thiamine HCl; retained=0.05 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=5980:0.05g/L-stock-or-main/1000mL-batch

    ingredients[26]; Riboflavin; retained=0.05 G_PER_L; correct representation: stock-strength/root
    placement or summed separate stocks; no new final concentration asserted; source=5980:0.05g/L-stock-or-main/1000mL-batch

    ingredients[27]; Calcium D-(+)-pantothenate; retained=0.05 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=5980:0.05g/L-stock-or-main/1000mL-batch

    ingredients[28]; (DL)-alpha-Lipoic acid; retained=0.05 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=5980:0.05g/L-stock-or-main/1000mL-batch

    ingredients[29]; D-(+)-biotin; retained=0.02 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=1038:0.02g/L-stock-or-main/1000mL-batch

    ingredients[30]; Calcium pantothenate; retained=0.1 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=1038:0.1g/L-stock-or-main/1000mL-batch

    solutions[0].composition[0]; FeCl2 x 4 H2O; retained=1.5 G_PER_L; evidence_only
    for named stock-strength component; stock completeness and receiving dose still
    concern; source=595:1.5g/L-stock-or-main/1000mL-batch

    solutions[1].composition[0]; Thiamine-HCl x 2 H2O; retained=0.2 G_PER_L; evidence_only
    for named stock-strength component; stock completeness and receiving dose still
    concern; source=1038:0.2g/L-stock-or-main/1000mL-batch

    solutions[1].composition[1]; Nicotinic acid; retained=0.2 G_PER_L; evidence_only
    for named stock-strength component; stock completeness and receiving dose still
    concern; source=5980:0.05g/L-stock-or-main/1000mL-batch, 1038:0.2g/L-stock-or-main/1000mL-batch

    solutions[1].composition[2]; p-Aminobenzoic acid; retained=0.08 G_PER_L; evidence_only
    for named stock-strength component; stock completeness and receiving dose still
    concern; source=5980:0.05g/L-stock-or-main/1000mL-batch, 1038:0.08g/L-stock-or-main/1000mL-batch

    solutions[1].composition[3]; Pyridoxine hydrochloride; retained=0.3 G_PER_L; evidence_only
    for named stock-strength component; stock completeness and receiving dose still
    concern; source=5980:0.1g/L-stock-or-main/1000mL-batch, 1038:0.3g/L-stock-or-main/1000mL-batch

    solutions[1].composition[4]; Vitamin B12; retained=0.1 G_PER_L; evidence_only
    for named stock-strength component; stock completeness and receiving dose still
    concern; source=5980:0.001g/L-stock-or-main/1000mL-batch, 1038:0.1g/L-stock-or-main/1000mL-batch

    solutions[2].composition[0]; Nicotinic acid; retained=0.05 G_PER_L; evidence_only
    for named stock-strength component; stock completeness and receiving dose still
    concern; source=5980:0.05g/L-stock-or-main/1000mL-batch, 1038:0.2g/L-stock-or-main/1000mL-batch

    solutions[2].composition[1]; p-Aminobenzoic acid; retained=0.05 G_PER_L; evidence_only
    for named stock-strength component; stock completeness and receiving dose still
    concern; source=5980:0.05g/L-stock-or-main/1000mL-batch, 1038:0.08g/L-stock-or-main/1000mL-batch

    solutions[2].composition[2]; Pyridoxine hydrochloride; retained=0.1 G_PER_L; evidence_only
    for named stock-strength component; stock completeness and receiving dose still
    concern; source=5980:0.1g/L-stock-or-main/1000mL-batch, 1038:0.3g/L-stock-or-main/1000mL-batch

    solutions[2].composition[3]; Vitamin B12; retained=0.001 G_PER_L; evidence_only
    for named stock-strength component; stock completeness and receiving dose still
    concern; source=5980:0.001g/L-stock-or-main/1000mL-batch, 1038:0.1g/L-stock-or-main/1000mL-batch

    data/normalized_yaml/bacterial/KOMODO_876_TD3-MEDIUM.yaml

    ingredients[0]; Na2SO4; retained=3.9801 G_PER_L; evidence_only: main-rate supported
    on provider1005mL basis; source=1815:3.9801g/L-stock-or-main/1005mL-batch

    ingredients[1]; KH2PO4; retained=0.199005 G_PER_L; evidence_only: main-rate supported
    on provider1005mL basis; source=1815:0.199005g/L-stock-or-main/1005mL-batch

    ingredients[2]; NH4Cl; retained=0.248756 G_PER_L; evidence_only: main-rate supported
    on provider1005mL basis; source=1815:0.248756g/L-stock-or-main/1005mL-batch

    ingredients[3]; NaCl; retained=19.9005 G_PER_L; evidence_only: main-rate supported
    on provider1005mL basis; source=1815:19.9005g/L-stock-or-main/1005mL-batch

    ingredients[4]; MgCl2 x 6 H2O; retained=9.75124 G_PER_L; evidence_only: main-rate
    supported on provider1005mL basis; source=1815:9.75124g/L-stock-or-main/1005mL-batch

    ingredients[5]; KCl; retained=0.497512 G_PER_L; evidence_only: main-rate supported
    on provider1005mL basis; source=1815:0.497512g/L-stock-or-main/1005mL-batch

    ingredients[6]; CaCl2 x 2 H2O; retained=0.0995025 G_PER_L; evidence_only: main-rate
    supported on provider1005mL basis; source=1815:0.0995025g/L-stock-or-main/1005mL-batch

    ingredients[7]; Sodium resazurin; retained=0.000497512 G_PER_L; evidence_only:
    main-rate supported on provider1005mL basis; source=1815:0.000497512g/L-stock-or-main/1005mL-batch

    ingredients[8]; Na2CO3; retained=0.995025 G_PER_L; evidence_only: main-rate supported
    on provider1005mL basis; source=1815:0.995025g/L-stock-or-main/1005mL-batch

    ingredients[9]; Na-caproate; retained=0.497512 G_PER_L; evidence_only: main-rate
    supported on provider1005mL basis; source=1815:0.497512g/L-stock-or-main/1005mL-batch

    ingredients[10]; Na-butyrate; retained=0.298507 G_PER_L; evidence_only: main-rate
    supported on provider1005mL basis; source=1815:0.298507g/L-stock-or-main/1005mL-batch

    ingredients[11]; Na2S x 9 H2O; retained=0.39801 G_PER_L; evidence_only: main-rate
    supported on provider1005mL basis; source=1815:0.39801g/L-stock-or-main/1005mL-batch

    ingredients[12]; HCl; retained=2.5 G_PER_L; correct representation: stock-strength/root
    placement or summed separate stocks; no new final concentration asserted; source=595:2.5g/L-stock-or-main/1000mL-batch

    ingredients[13]; ZnCl2; retained=0.07 G_PER_L; correct representation: stock-strength/root
    placement or summed separate stocks; no new final concentration asserted; source=595:0.07g/L-stock-or-main/1000mL-batch

    ingredients[14]; MnCl2 x 4 H2O; retained=0.1 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=595:0.1g/L-stock-or-main/1000mL-batch

    ingredients[15]; H3BO3; retained=0.006 G_PER_L; correct representation: stock-strength/root
    placement or summed separate stocks; no new final concentration asserted; source=595:0.006g/L-stock-or-main/1000mL-batch

    ingredients[16]; CoCl2 x 6 H2O; retained=0.19 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=595:0.19g/L-stock-or-main/1000mL-batch

    ingredients[17]; CuCl2 x 2 H2O; retained=0.002 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=595:0.002g/L-stock-or-main/1000mL-batch

    ingredients[18]; NiCl2 x 6 H2O; retained=0.024 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=595:0.024g/L-stock-or-main/1000mL-batch

    ingredients[19]; Na2MoO4 x 2 H2O; retained=0.036 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=595:0.036g/L-stock-or-main/1000mL-batch

    ingredients[20]; NaOH; retained=0.5 G_PER_L; correct representation: stock-strength/root
    placement or summed separate stocks; no new final concentration asserted; source=777:0.5g/L-stock-or-main/1000mL-batch

    ingredients[21]; Na2SeO3 x 5 H2O; retained=0.003 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=777:0.003g/L-stock-or-main/1000mL-batch

    ingredients[22]; Na2WO4 x 2 H2O; retained=0.004 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=777:0.004g/L-stock-or-main/1000mL-batch

    ingredients[23]; Biotin; retained=0.02 G_PER_L; correct representation: stock-strength/root
    placement or summed separate stocks; no new final concentration asserted; source=5980:0.02g/L-stock-or-main/1000mL-batch

    ingredients[24]; Folic acid; retained=0.02 G_PER_L; correct representation: stock-strength/root
    placement or summed separate stocks; no new final concentration asserted; source=5980:0.02g/L-stock-or-main/1000mL-batch

    ingredients[25]; Thiamine HCl; retained=0.05 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=5980:0.05g/L-stock-or-main/1000mL-batch

    ingredients[26]; Riboflavin; retained=0.05 G_PER_L; correct representation: stock-strength/root
    placement or summed separate stocks; no new final concentration asserted; source=5980:0.05g/L-stock-or-main/1000mL-batch

    ingredients[27]; Calcium D-(+)-pantothenate; retained=0.05 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=5980:0.05g/L-stock-or-main/1000mL-batch

    ingredients[28]; (DL)-alpha-Lipoic acid; retained=0.05 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=5980:0.05g/L-stock-or-main/1000mL-batch

    ingredients[29]; D-(+)-biotin; retained=0.02 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=1038:0.02g/L-stock-or-main/1000mL-batch

    ingredients[30]; Calcium pantothenate; retained=0.1 G_PER_L; correct representation:
    stock-strength/root placement or summed separate stocks; no new final concentration
    asserted; source=1038:0.1g/L-stock-or-main/1000mL-batch

    solutions[0].composition[0]; FeCl2 x 4 H2O; retained=1.5 G_PER_L; evidence_only
    for named stock-strength component; stock completeness and receiving dose still
    concern; source=595:1.5g/L-stock-or-main/1000mL-batch

    solutions[1].composition[0]; Thiamine-HCl x 2 H2O; retained=0.2 G_PER_L; evidence_only
    for named stock-strength component; stock completeness and receiving dose still
    concern; source=1038:0.2g/L-stock-or-main/1000mL-batch

    solutions[1].composition[1]; Nicotinic acid; retained=0.2 G_PER_L; evidence_only
    for named stock-strength component; stock completeness and receiving dose still
    concern; source=5980:0.05g/L-stock-or-main/1000mL-batch, 1038:0.2g/L-stock-or-main/1000mL-batch

    solutions[1].composition[2]; p-Aminobenzoic acid; retained=0.08 G_PER_L; evidence_only
    for named stock-strength component; stock completeness and receiving dose still
    concern; source=5980:0.05g/L-stock-or-main/1000mL-batch, 1038:0.08g/L-stock-or-main/1000mL-batch

    solutions[1].composition[3]; Pyridoxine hydrochloride; retained=0.3 G_PER_L; evidence_only
    for named stock-strength component; stock completeness and receiving dose still
    concern; source=5980:0.1g/L-stock-or-main/1000mL-batch, 1038:0.3g/L-stock-or-main/1000mL-batch

    solutions[1].composition[4]; Vitamin B12; retained=0.1 G_PER_L; evidence_only
    for named stock-strength component; stock completeness and receiving dose still
    concern; source=5980:0.001g/L-stock-or-main/1000mL-batch, 1038:0.1g/L-stock-or-main/1000mL-batch

    solutions[2].composition[0]; Nicotinic acid; retained=0.05 G_PER_L; evidence_only
    for named stock-strength component; stock completeness and receiving dose still
    concern; source=5980:0.05g/L-stock-or-main/1000mL-batch, 1038:0.2g/L-stock-or-main/1000mL-batch

    solutions[2].composition[1]; p-Aminobenzoic acid; retained=0.05 G_PER_L; evidence_only
    for named stock-strength component; stock completeness and receiving dose still
    concern; source=5980:0.05g/L-stock-or-main/1000mL-batch, 1038:0.08g/L-stock-or-main/1000mL-batch

    solutions[2].composition[2]; Pyridoxine hydrochloride; retained=0.1 G_PER_L; evidence_only
    for named stock-strength component; stock completeness and receiving dose still
    concern; source=5980:0.1g/L-stock-or-main/1000mL-batch, 1038:0.3g/L-stock-or-main/1000mL-batch

    solutions[2].composition[3]; Vitamin B12; retained=0.001 G_PER_L; evidence_only
    for named stock-strength component; stock completeness and receiving dose still
    concern; source=5980:0.001g/L-stock-or-main/1000mL-batch, 1038:0.1g/L-stock-or-main/1000mL-batch'
- assessment_id: A-dose
  area: quantity
  topic: Stock-addition basis and conversion limits
  outcome: concern
  summary: DSM owner asserts three1mL/L additions; provider describes1mL per1005mL
    batch, with2mL selenium/tungsten stock. HCl2.5g/L is provider stock data, not
    independently derivable from an unspecified25% basis. Retain exact batch and stock
    context; no density assumption or averaged vitamin total.
  target_ids:
  - CultureMech:002034
  evidence_ids:
  - E-record
  - E-primary
  - E-structured
  - E-flattened
- assessment_id: A-chemistry
  area: grounding
  topic: Every asserted chemical identifier and supplied form
  outcome: concern
  summary: '35 unique asserted ChEBI IDs across232 primary/secondary slots are active.
    Two exact-form mismatches remain: nickel hexahydrate and sodium resazurin.29 named
    identities are compatible; B12 breadth, lipoic stereochemistry, HCl solution context
    and generic calcium-pantothenate specificity retain explicit limits.'
  target_ids:
  - CultureMech:002034
  evidence_ids:
  - E-mim
  - E-CHEBI-114126
  - E-CHEBI-131361
  - E-CHEBI-132751
  - E-CHEBI-15940
  - E-CHEBI-15956
  - E-CHEBI-16494
  - E-CHEBI-17015
  - E-CHEBI-176843
  - E-CHEBI-17883
  - E-CHEBI-26710
  - E-CHEBI-27470
  - E-CHEBI-29377
  - E-CHEBI-30753
  - E-CHEBI-30961
  - E-CHEBI-31206
  - E-CHEBI-31345
  - E-CHEBI-32145
  - E-CHEBI-32149
  - E-CHEBI-32588
  - E-CHEBI-33118
  - E-CHEBI-34887
  - E-CHEBI-49105
  - E-CHEBI-49976
  - E-CHEBI-53503
  - E-CHEBI-53542
  - E-CHEBI-63036
  - E-CHEBI-63939
  - E-CHEBI-64103
  - E-CHEBI-75213
  - E-CHEBI-76209
  - E-CHEBI-86158
  - E-CHEBI-86249
  - E-CHEBI-86318
  - E-CHEBI-86345
  - E-CHEBI-86368
  - E-CHEBI-8806
  details: 'CHEBI:114126; Na-caproate; compatible_named_chemical; Current active ChEBI
    label/synonyms and formula/InChI/SMILES agree with the named chemical, including
    explicitly supplied counterion/hydrate counts where present. This is identity
    support only, not support for concentration, stock placement, purity or growth.

    CHEBI:131361; Na2SeO3 x 5 H2O; compatible_named_chemical; Current active ChEBI
    label/synonyms and formula/InChI/SMILES agree with the named chemical, including
    explicitly supplied counterion/hydrate counts where present. This is identity
    support only, not support for concentration, stock placement, purity or growth.

    CHEBI:132751; Thiamine-HCl x 2 H2O; compatible_named_chemical; Current active
    ChEBI label/synonyms and formula/InChI/SMILES agree with the named chemical, including
    explicitly supplied counterion/hydrate counts where present. This is identity
    support only, not support for concentration, stock placement, purity or growth.

    CHEBI:15940; Nicotinic acid; compatible_named_chemical; Current active ChEBI label/synonyms
    and formula/InChI/SMILES agree with the named chemical, including explicitly supplied
    counterion/hydrate counts where present. This is identity support only, not support
    for concentration, stock placement, purity or growth.

    CHEBI:15956; Biotin, D-(+)-biotin; compatible_named_chemical; Current active ChEBI
    label/synonyms and formula/InChI/SMILES agree with the named chemical, including
    explicitly supplied counterion/hydrate counts where present. This is identity
    support only, not support for concentration, stock placement, purity or growth.

    CHEBI:16494; (DL)-alpha-Lipoic acid; compatible_broad_identity; Lipoic-acid connectivity
    matches, but the ontology InChI and SMILES contain no stereo specification and
    do not establish the explicit DL/racemic supplied material. Retain the source
    DL label; do not infer pure R/S identity or claim exact racemate proof.

    CHEBI:17015; Riboflavin; compatible_named_chemical; Current active ChEBI label/synonyms
    and formula/InChI/SMILES agree with the named chemical, including explicitly supplied
    counterion/hydrate counts where present. This is identity support only, not support
    for concentration, stock placement, purity or growth.

    CHEBI:176843; Vitamin B12; compatible_broad_identity; Active vitamin B12 vitamer
    class matches the source generic label. No molecular formula/mass/structure is
    supplied for the class, so no specific vitamer, counterion or mass-to-molar conversion
    is established. This broad match is not itself an incorrect ID.

    CHEBI:17883; HCl; matched_constituent_not_solution; HCl constituent identity matches.
    The term does not encode the separately supplied aqueous25% stock, percentage
    basis or receiving-medium dilution. Preserve stock attribute/dose; the identity
    match does not validate provider-derived concentration arithmetic.

    CHEBI:26710; NaCl; compatible_named_chemical; Current active ChEBI label/synonyms
    and formula/InChI/SMILES agree with the named chemical, including explicitly supplied
    counterion/hydrate counts where present. This is identity support only, not support
    for concentration, stock placement, purity or growth.

    CHEBI:27470; Folic acid; compatible_named_chemical; Current active ChEBI label/synonyms
    and formula/InChI/SMILES agree with the named chemical, including explicitly supplied
    counterion/hydrate counts where present. This is identity support only, not support
    for concentration, stock placement, purity or growth.

    CHEBI:29377; Na2CO3; compatible_named_chemical; Current active ChEBI label/synonyms
    and formula/InChI/SMILES agree with the named chemical, including explicitly supplied
    counterion/hydrate counts where present. This is identity support only, not support
    for concentration, stock placement, purity or growth.

    CHEBI:30753; p-Aminobenzoic acid; compatible_named_chemical; Current active ChEBI
    label/synonyms and formula/InChI/SMILES agree with the named chemical, including
    explicitly supplied counterion/hydrate counts where present. This is identity
    support only, not support for concentration, stock placement, purity or growth.

    CHEBI:30961; Pyridoxine hydrochloride; compatible_named_chemical; Current active
    ChEBI label/synonyms and formula/InChI/SMILES agree with the named chemical, including
    explicitly supplied counterion/hydrate counts where present. This is identity
    support only, not support for concentration, stock placement, purity or growth.

    CHEBI:31206; NH4Cl; compatible_named_chemical; Current active ChEBI label/synonyms
    and formula/InChI/SMILES agree with the named chemical, including explicitly supplied
    counterion/hydrate counts where present. This is identity support only, not support
    for concentration, stock placement, purity or growth.

    CHEBI:31345; Calcium D-(+)-pantothenate, Calcium pantothenate; matched_with_source_specificity_limit;
    Formula 2C9H16NO5.Ca and explicit D stereochemistry support Calcium D-(+)-pantothenate.
    For the separately named generic Calcium pantothenate source component, unspecified
    stereochemistry is not independently fixed by the source name alone. Do not reject
    the D-labelled match or infer generic-source stereo solely from MIM synonyms.
    No molecular-weight conversion is made.

    CHEBI:32145; NaOH; compatible_named_chemical; Current active ChEBI label/synonyms
    and formula/InChI/SMILES agree with the named chemical, including explicitly supplied
    counterion/hydrate counts where present. This is identity support only, not support
    for concentration, stock placement, purity or growth.

    CHEBI:32149; Na2SO4; compatible_named_chemical; Current active ChEBI label/synonyms
    and formula/InChI/SMILES agree with the named chemical, including explicitly supplied
    counterion/hydrate counts where present. This is identity support only, not support
    for concentration, stock placement, purity or growth.

    CHEBI:32588; KCl; compatible_named_chemical; Current active ChEBI label/synonyms
    and formula/InChI/SMILES agree with the named chemical, including explicitly supplied
    counterion/hydrate counts where present. This is identity support only, not support
    for concentration, stock placement, purity or growth.

    CHEBI:33118; H3BO3; compatible_named_chemical; Current active ChEBI label/synonyms
    and formula/InChI/SMILES agree with the named chemical, including explicitly supplied
    counterion/hydrate counts where present. This is identity support only, not support
    for concentration, stock placement, purity or growth.

    CHEBI:34887; NiCl2 x 6 H2O; exact_form_mismatch; Local NiCl2 x 6 H2O requires
    six waters; asserted Cl2Ni has none. Candidate CHEBI:53542 explicitly represents
    2Cl.6H2O.Ni. Correct both primary and secondary mappings in maintained owners,
    preserving amount/stage; regenerate derived target. Exact MIM preferred row is
    REJECTED while its synonym row is MAPPED; both identify53542.

    CHEBI:49105; Thiamine HCl; compatible_named_chemical; Current active ChEBI label/synonyms
    and formula/InChI/SMILES agree with the named chemical, including explicitly supplied
    counterion/hydrate counts where present. This is identity support only, not support
    for concentration, stock placement, purity or growth.

    CHEBI:49976; ZnCl2; compatible_named_chemical; Current active ChEBI label/synonyms
    and formula/InChI/SMILES agree with the named chemical, including explicitly supplied
    counterion/hydrate counts where present. This is identity support only, not support
    for concentration, stock placement, purity or growth.

    CHEBI:53503; CoCl2 x 6 H2O; compatible_named_chemical; Current active ChEBI label/synonyms
    and formula/InChI/SMILES agree with the named chemical, including explicitly supplied
    counterion/hydrate counts where present. This is identity support only, not support
    for concentration, stock placement, purity or growth.

    CHEBI:63036; KH2PO4; compatible_named_chemical; Current active ChEBI label/synonyms
    and formula/InChI/SMILES agree with the named chemical, including explicitly supplied
    counterion/hydrate counts where present. This is identity support only, not support
    for concentration, stock placement, purity or growth.

    CHEBI:63939; Na2WO4 x 2 H2O; compatible_named_chemical; Current active ChEBI label/synonyms
    and formula/InChI/SMILES agree with the named chemical, including explicitly supplied
    counterion/hydrate counts where present. This is identity support only, not support
    for concentration, stock placement, purity or growth.

    CHEBI:64103; Na-butyrate; compatible_named_chemical; Current active ChEBI label/synonyms
    and formula/InChI/SMILES agree with the named chemical, including explicitly supplied
    counterion/hydrate counts where present. This is identity support only, not support
    for concentration, stock placement, purity or growth.

    CHEBI:75213; Na2MoO4 x 2 H2O; compatible_named_chemical; Current active ChEBI
    label/synonyms and formula/InChI/SMILES agree with the named chemical, including
    explicitly supplied counterion/hydrate counts where present. This is identity
    support only, not support for concentration, stock placement, purity or growth.

    CHEBI:76209; Na2S x 9 H2O; compatible_named_chemical; Current active ChEBI label/synonyms
    and formula/InChI/SMILES agree with the named chemical, including explicitly supplied
    counterion/hydrate counts where present. This is identity support only, not support
    for concentration, stock placement, purity or growth.

    CHEBI:86158; CaCl2 x 2 H2O; compatible_named_chemical; Current active ChEBI label/synonyms
    and formula/InChI/SMILES agree with the named chemical, including explicitly supplied
    counterion/hydrate counts where present. This is identity support only, not support
    for concentration, stock placement, purity or growth.

    CHEBI:86249; FeCl2 x 4 H2O; compatible_named_chemical; Current active ChEBI label/synonyms
    and formula/InChI/SMILES agree with the named chemical, including explicitly supplied
    counterion/hydrate counts where present. This is identity support only, not support
    for concentration, stock placement, purity or growth.

    CHEBI:86318; CuCl2 x 2 H2O; compatible_named_chemical; Current active ChEBI label/synonyms
    and formula/InChI/SMILES agree with the named chemical, including explicitly supplied
    counterion/hydrate counts where present. This is identity support only, not support
    for concentration, stock placement, purity or growth.

    CHEBI:86345; MgCl2 x 6 H2O; compatible_named_chemical; Current active ChEBI label/synonyms
    and formula/InChI/SMILES agree with the named chemical, including explicitly supplied
    counterion/hydrate counts where present. This is identity support only, not support
    for concentration, stock placement, purity or growth.

    CHEBI:86368; MnCl2 x 4 H2O; compatible_named_chemical; Current active ChEBI label/synonyms
    and formula/InChI/SMILES agree with the named chemical, including explicitly supplied
    counterion/hydrate counts where present. This is identity support only, not support
    for concentration, stock placement, purity or growth.

    CHEBI:8806; Sodium resazurin; exact_form_mismatch; Local and primary-source material
    is Sodium resazurin; asserted C12H7NO4/229.191 contains no sodium. MIM exact Sodium
    resazurin synonym maps to8806 and therefore reproduces, rather than resolves,
    the supplied-salt conflict. Resolve authoritative sodium-salt identity before
    any replacement or mass/molar conversion; no replacement ID is asserted by this
    audit.'
- assessment_id: A-preparation
  area: scope
  topic: Preparation, pH, gas and optional supplement
  outcome: concern
  summary: Main anoxic protocol, vitamin filtration and pH6.7–6.9 are source-supported.
    SL-10 makeup text belongs to the stock, while KOMODO aerobic wording conflicts
    with DSMZ. Optional1%v/v fatty-acid-mixture prose is correctly scoped to medium119's
    mixture only.
  target_ids:
  - CultureMech:002034
  evidence_ids:
  - E-record
  - E-primary
  - E-119
- assessment_id: A-classification
  area: identity
  topic: Composition and physical-state classification
  outcome: supported
  summary: Source describes a defined liquid formulation; existing DEFINED/DEFINED/LIQUID
    classification is supported. Empty optional growth/storage fields are not filled
    by inference.
  target_ids:
  - CultureMech:002034
  evidence_ids:
  - E-record
  - E-structured
- assessment_id: A-growth
  area: evidence
  topic: Organism and cultivation claims
  outcome: supported
  summary: No strain-specific structured growth claim is asserted by this target.
    Generic cultivation context and optional stimulation note are recipe-source statements
    only; no optimality, species-wide growth or medium119 organism claim is inferred.
  target_ids:
  - CultureMech:002034
  evidence_ids:
  - E-record
  - E-primary
  - E-119
- assessment_id: A-provenance
  area: provenance
  topic: Evidence linkage, history and generated freshness
  outcome: concern
  summary: Each complete YAML lacks evidence entries; source URLs/history remain provenance
    leads. Existing nesting repairs are credited. GeneratedAugust6 content predates
    theirAugust7/15 nesting events, and current exact-formulation merge rules require
    source-boundary decisions before regeneration.
  target_ids:
  - CultureMech:002034
  evidence_ids:
  - E-record
  - E-primary
  - E-generator
findings:
- finding_id: F-stock
  issue_key: batch079-record07-f-stock
  category: representation
  severity: blocker
  status: open
  certainty: confirmed
  title: Stock formulations appear as basal ingredients
  description: Both owners leave trace, selenium/tungsten and vitamin components at
    root stock strengths. SL-10/vitamin nesting is incomplete and no selenium/tungsten
    container exists within these fully read files. This changes the formulation a
    reader would prepare; maintain separate stocks, supplied forms, addition amounts
    and source basis.
  target_ids:
  - CultureMech:002034
  field_paths:
  - ingredients
  - solutions
  evidence_ids:
  - E-record
  - E-primary
  - E-structured
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_876_TD3-MEDIUM.yaml
    role: normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfothermus_naphthae_medium.yaml
    role: normalized source
  rule_id: CultureMech.single-record-checklist.representation
  native_severity: blocker
  normalization_reason: Severity follows concrete scientific impact, not a linkage
    percentage or validator score.
  external_issues:
  - https://github.com/CultureBotAI/CultureMech/issues/749
- finding_id: F-stale
  issue_key: batch079-record07-f-stale
  category: ownership
  severity: blocker
  status: open
  certainty: confirmed
  title: Generated target drops existing normalized nesting repairs
  description: The generated target retains37 root ingredients and no solutions, including
    summed pyridoxine0.4, nicotinic acid0.25, B120.101 and PABA0.13G_PER_L. Each current
    owner has31 root plus10 nested components. Do not overwrite owners with this stale
    product or force differing formulations into one current merge group.
  target_ids:
  - CultureMech:002034
  field_paths:
  - ingredients
  - solutions
  - merged_from
  - curation_history
  evidence_ids:
  - E-record
  - E-generator
  - E-primary
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_876_TD3-MEDIUM.yaml
    role: normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfothermus_naphthae_medium.yaml
    role: normalized source
  rule_id: CultureMech.single-record-checklist.ownership
  native_severity: blocker
  normalization_reason: Severity follows concrete scientific impact, not a linkage
    percentage or validator score.
  external_issues:
  - https://github.com/CultureBotAI/CultureMech/issues/749
- finding_id: F-nickel
  issue_key: batch079-record07-f-nickel
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Hexahydrate supplied as anhydrous nickel chloride
  description: Generated ingredients[19] and both owners' ingredients[18] use34887
    in primary and secondary term slots.53542 explicitly represents six waters. Exact
    MIM rows have different mapped/rejected roles; preserve resolver policy and attach
    chemical evidence through authoritative inputs.
  target_ids:
  - CultureMech:002034
  field_paths:
  - ingredients[19].term
  - ingredients[19].mediaingredientmech_chebi_term
  evidence_ids:
  - E-record
  - E-CHEBI-34887
  - E-CHEBI-53542
  - E-mim
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_876_TD3-MEDIUM.yaml
    role: normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfothermus_naphthae_medium.yaml
    role: normalized source
  rule_id: CultureMech.single-record-checklist.grounding
  native_severity: major
  normalization_reason: Severity follows concrete scientific impact, not a linkage
    percentage or validator score.
  external_issues:
  - https://github.com/CultureBotAI/CultureMech/issues/749
- finding_id: F-resazurin
  issue_key: batch079-record07-f-resazurin
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Sodium resazurin uses an identifier without sodium
  description: All three files' ingredients[7].term map the explicitly supplied sodium
    salt to8806, whose formula has no sodium. A repeated MIM synonym mapping is not
    independent chemical verification. Replacement identity remains unresolved; no
    substitute ID is invented.
  target_ids:
  - CultureMech:002034
  field_paths:
  - ingredients[7].term
  evidence_ids:
  - E-record
  - E-primary
  - E-CHEBI-8806
  - E-mim
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_876_TD3-MEDIUM.yaml
    role: normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfothermus_naphthae_medium.yaml
    role: normalized source
  rule_id: CultureMech.single-record-checklist.grounding
  native_severity: major
  normalization_reason: Severity follows concrete scientific impact, not a linkage
    percentage or validator score.
  external_issues:
  - https://github.com/CultureBotAI/CultureMech/issues/749
- finding_id: F-preparation
  issue_key: batch079-record07-f-preparation
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Conflicting atmosphere and misplaced stock preparation
  description: KOMODO notes assert aerobic conditions while the associated DSMZ formulation
    is anoxic. Exact KOMODO equivalence is not established. Separately, DSM and generated
    preparation_steps[2] contain SL-10 makeup text at main-medium scope. Preserve
    distinctions among main80%N2/20%CO2, selected100%N2 stocks and vitamin filtration.
  target_ids:
  - CultureMech:002034
  field_paths:
  - preparation_steps[2]
  - parent_media
  - merged_from
  evidence_ids:
  - E-record
  - E-primary
  - E-structured
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_876_TD3-MEDIUM.yaml
    role: normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfothermus_naphthae_medium.yaml
    role: normalized source
  rule_id: CultureMech.single-record-checklist.scope
  native_severity: major
  normalization_reason: Severity follows concrete scientific impact, not a linkage
    percentage or validator score.
  external_issues:
  - https://github.com/CultureBotAI/CultureMech/issues/749
- finding_id: F-linkage
  issue_key: batch079-record07-f-linkage
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Formulation support lacks narrow evidence links
  description: The complete three YAML files contain no evidence entries. Native references
    consequently inspect zero assertions. Attach evidence to each corrected claim,
    retaining source/version/stock basis and existing history; no missing optional
    property is inferred false.
  target_ids:
  - CultureMech:002034
  field_paths:
  - evidence
  - ingredients
  - solutions
  evidence_ids:
  - E-record
  - E-primary
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_876_TD3-MEDIUM.yaml
    role: normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfothermus_naphthae_medium.yaml
    role: normalized source
  rule_id: CultureMech.single-record-checklist.evidence
  native_severity: minor
  normalization_reason: Severity follows concrete scientific impact, not a linkage
    percentage or validator score.
  external_issues:
  - https://github.com/CultureBotAI/CultureMech/issues/749
actions:
- action_id: ACT-owners
  description: Resolve source equivalence, stock boundaries/doses, preparation scoping
    and narrow evidence in the two maintained owners; keep exact quantities unsupported
    by sources unresolved. Current observations are retained as follow-up rather than
    a forced repair.
  finding_ids:
  - F-stock
  - F-preparation
  - F-linkage
  target_ids:
  - CultureMech:002034
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_876_TD3-MEDIUM.yaml
    role: normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfothermus_naphthae_medium.yaml
    role: normalized source
  acceptance_checks:
  - Compare every direct and nested component with primary stock tables, preserving1005mL
    provider basis and independent stock strengths.
  - Use round-trip source edits with closed-schema validation and append-only substantive
    curation events.
  - Rerun native schema, strict, term and reference checks on changed owners; manually
    verify PURL/table claims.
- action_id: ACT-grounding
  description: Correct only exact verified chemical forms in authoritative inputs
    after checking packaged resolver behavior; resolve or explicitly withhold sodium-resazurin
    replacement and narrower stereochemical claims.
  finding_ids:
  - F-nickel
  - F-resazurin
  target_ids:
  - CultureMech:002034
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_876_TD3-MEDIUM.yaml
    role: normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfothermus_naphthae_medium.yaml
    role: normalized source
  acceptance_checks:
  - Recheck ChEBI formula/hydration/charge/stereochemistry against exact supplied
    source forms.
  - Keep MIM snapshot immutable and use its maintained resolver; do not bypass rejected/ambiguous
    decisions.
  - Validate changed owner terms and source-linked evidence without claiming configured
    term validation covers all chemical slots.
- action_id: ACT-regenerate
  description: After owner decisions, regenerate only the defensible scoped target
    group through maintained merge code, preserving IDs and all historical receipts.
    If owners split under exact-formulation rules, review the ID/lifecycle impact
    rather than forcing the historical merge.
  finding_ids:
  - F-stale
  target_ids:
  - CultureMech:002034
  owner_paths:
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/KOMODO_876_TD3-MEDIUM.yaml
    role: normalized source
  - repository: CultureBotAI/CultureMech
    path: data/normalized_yaml/bacterial/desulfothermus_naphthae_medium.yaml
    role: normalized source
  depends_on:
  - ACT-owners
  - ACT-grounding
  generator: python -m culturemech.merge.merge_recipes with explicitly staged owner
    set
  acceptance_checks:
  - Preview grouping/names/IDs; never use --limit as a target selector.
  - Run native output validation, verify-merges and audit-merge-freshness at their
    documented scopes; record pre-existing corpus drift separately.
  - Independent scientific review confirms stock/preparation/identity preservation
    before considering a passing assessment.
limitations:
- 'Completed assessment means the declared record was reviewed, not scientifically
  approved: two blocker and three major findings remain open.'
- Exact KOMODO source formulation is inaccessible in the bounded search. DSM association
  and historical copied composition do not prove source equivalence.
- No scientific inputs were corrected or regenerated. Source-equivalence, dose basis
  and current formulation grouping require a separately verified correction; follow-up
  is filed in issue749.
- Native references checked zero evidence assertions; configured term checks do not
  independently validate every chemical supplied form.
- B12 is a broad class; lipoic stereochemistry and generic calcium-pantothenate specificity
  are not made more precise than their sources. HCl percentage basis/density is not
  invented.
- Raw primary captures, runtime logs and peer records are retained under ignored .temp
  with input hashes, not published as reusable source corpora. Working-tree hashes
  attest examined bytes; Git base remains dda27db.
- The broader history/ID/product/corpus and merge-freshness gates are not claimed
  executed by this read-only scientific assessment; no source/ID/product mutation
  required those gates in this canary.
notes:
- Initial native inspect failed because a metadata filename was mistyped; the failed
  receipt is preserved and the corrected/final native inspections succeeded.
- The original approval rejections were superseded by direct user continuation approval
  before environment setup; no bypass was used.
- Optional medium119 supplementation is retained as supported prose, not a missing
  mandatory component.
links:
- https://github.com/CultureBotAI/CultureMech/issues/749
- https://github.com/CultureBotAI/CultureMech/issues/150
- https://github.com/CultureBotAI/CultureMech/issues/278
tags:
- batch079
- record07
- needs_curation
- source_review
```
