# Media Growth Review: Corpus Scope and Current Evidence

Date: 2026-05-05

## Scope

The target media set is the repo's media YAML corpus, not a manually supplied organism/media list.

- Primary corpus: `data/normalized_yaml/**/*.yaml`
- Current YAML count: 15,827
- Primary media directories: `algae`, `archaea`, `bacterial`, `fungal`, `specialized`
- Supporting records: `data/normalized_yaml/solutions` should be used for stock solutions and formulation comparison, not as primary growable-media targets unless a record is clearly used as a growth medium.

Because this is a large corpus, review must be tracked in batches. The generated coverage manifest is:

- `reports/media_growth_review_manifest.tsv`
- `reports/media_growth_review_manifest.json`
- `reports/media_growth_review_manifest_summary.md`

The manifest currently shows:

- Total normalized YAML records: 15,827
- Primary target records: 15,827
- Supporting solution records: 0
- YAML load errors: 0
- Records with applied growth metrics in YAML: 31
- Records with supported applied growth evidence in YAML: 31
- Records with genome assembly IDs on target organisms: 10
- Records with modeled variants: 25
- Records with unapplied supported growth candidates: 0
- Records with review-only proposal candidates: 991
- Records reviewed with no candidates: 14,805
- Records not reviewed: 0

The existing local proposal artifacts currently cover 15,855 proposal YAML files:

- `workspace/reports/growth_evidence_proposals/**/*.yaml`: 15,850 files
- `workspace/reports/growth_evidence_proposals_backfill/*.yaml`: 5 files

Manifest-level coverage is 15,827 normalized YAML records with applied evidence, review-only candidates, or an explicit no-candidate search. These proposal files now cover the full normalized YAML corpus at the manifest level.

Algae directory coverage is complete at the manifest level:

- `applied_growth_evidence`: 9 records
- `has_review_candidates`: 93 records
- `reviewed_no_candidates`: 146 records
- `not_reviewed`: 0 records

Archaea directory coverage is complete at the manifest level:

- `applied_growth_evidence`: 0 records
- `has_review_candidates`: 0 records
- `reviewed_no_candidates`: 63 records
- `not_reviewed`: 0 records

Fungal directory coverage is complete at the manifest level:

- `applied_growth_evidence`: 0 records
- `has_review_candidates`: 10 records
- `reviewed_no_candidates`: 114 records
- `not_reviewed`: 0 records

Specialized directory coverage is complete at the manifest level:

- `applied_growth_evidence`: 2 records
- `has_review_candidates`: 51 records
- `reviewed_no_candidates`: 402 records
- `not_reviewed`: 0 records

Bacterial directory coverage is partial:

- `applied_growth_evidence`: 20 records
- `has_review_candidates`: 837 records
- `reviewed_no_candidates`: 14,080 records
- `not_reviewed`: 0 records

Implementation note:

- `scripts/propose_growth_evidence.py` now writes proposal files under category-preserving paths such as `workspace/reports/growth_evidence_proposals/algae/dm.yaml`. `scripts/build_media_growth_review_manifest.py` and `scripts/apply_growth_evidence.py` now read proposals recursively. This prevents cross-directory records with the same basename from overwriting each other.

## Existing Pipeline

The repo already contains a growth-evidence workflow:

- `python3 scripts/build_media_growth_review_manifest.py`: builds the corpus coverage manifest
- `just propose-growth`: runs `scripts/propose_growth_evidence.py`
- `just fetch-pubmed`: caches PubMed abstracts under `references_cache/`
- `just apply-growth`: applies curator-approved proposal YAMLs
- `just validate-growth`: verifies evidence snippets against cached abstracts

`scripts/propose_growth_evidence.py` now supports batch filters:

- `--category algae,bacterial`
- `--offset N`
- `--limit N`

Example batch command:

```bash
just propose-growth --category algae --offset 0 --limit 25 --retmax 3 --apply --write-empty
```

Current validation artifact:

- `workspace/reports/evidence_reference_validation.md`
- Last rerun command: `just validate-growth`
- Total evidence items checked: 128
- `OK`: 89
- `MISSING_CACHE`: 2
- `NO_EVIDENCE`: 37
- `SNIPPET_NOT_IN_ABSTRACT`: 0

File-level validation note:

- Most media records edited for applied growth evidence and/or variants pass
  `just validate <file>`.
- `m9.yaml` and `nutrient_broth.yaml` were normalized to satisfy schema while
  preserving provenance: `sources` was converted to `source_data`, category
  values were lowercased, and FOODON mappings for complex ingredients were
  preserved in notes instead of `term`.
- `data/normalized_yaml/bacterial/KOMODO_1078_FRIIS_medium.yaml` currently
  fails schema validation on pre-existing ingredient issues unrelated to the
  added growth evidence: UBERON/FOODON ingredient terms where the schema expects
  CHEBI, plus unexpected ingredient-level `synonyms` fields. The growth-evidence
  snippet itself passes `just validate-growth`.
- `data/normalized_yaml/bacterial/KOMODO_11_MRS_medium.yaml` passes
  `just validate`. Its PMID:38194015 and PMID:39353547 MRS growth-evidence
  snippets pass `just validate-growth`.
- `data/normalized_yaml/bacterial/KOMODO_429_COLUMBIA_BLOOD_AGAR.yaml`
  currently fails schema validation on pre-existing ingredient issues unrelated
  to the added growth evidence: UBERON/FOODON ingredient terms where the schema
  expects CHEBI, plus unexpected ingredient-level `synonyms` fields. The
  growth-evidence snippet itself passes `just validate-growth`.
- `data/normalized_yaml/bacterial/KOMODO_761_HALOTHERMOTHRIX_ORENII.yaml`
  passes `just validate`. Its PMID:7520742 evidence snippets pass
  `just validate-growth`; the NCBI BioProject URL is retained as genome
  identifier provenance and is reported as `NO_EVIDENCE` by the PMID/DOI
  snippet validator because it is a database URL rather than a cached literature
  abstract.
- `data/normalized_yaml/bacterial/TOGO_M1547_Marine_Agar_2216.yaml` passes
  `just validate`. Its PMID:18319453 colony-formation snippet passes
  `just validate-growth`; the NCBI/BacDive database provenance references are
  retained for genome/type-strain identifiers and are reported as `NO_EVIDENCE`
  by the PMID/DOI snippet validator.
- `data/normalized_yaml/bacterial/TOGO_M1663_Thermus_Medium.yaml` passes
  `just validate`. Its PMID:16233377 growth-kinetics snippet passes
  `just validate-growth`; the NCBI database provenance references are retained
  for genome identifiers and are reported as `NO_EVIDENCE` by the PMID/DOI
  snippet validator. A pre-existing curation-history `date` key in this record
  was normalized to `timestamp` to satisfy the schema.
- `data/normalized_yaml/bacterial/TOGO_M540_Brucella_Broth.yaml` passes
  `just validate`. Its PMID:10609610 Brucella broth / fetal-bovine-serum /
  H2O2 growth-evidence snippets pass `just validate-growth`; full-text review
  was used to resolve the primary strain as *Helicobacter pylori* OMU89-362
  and the OD620 value recorded in the growth metric.
- `data/normalized_yaml/bacterial/tryptic_soy_broth.yaml` currently fails
  schema validation on pre-existing ingredient issues unrelated to the added
  growth evidence: FOODON ingredient terms where the schema expects CHEBI, plus
  unexpected ingredient-level `synonyms` fields. Its PMID:15931519 snippets
  pass `just validate-growth`. The evidence was modeled as a TSB-without-
  dextrose starch/maltose variant for *Arthrobacter psychrolactophilus* B7 /
  ATCC 700733 with NCBITaxon:92442 and genome assembly GCA_003219795.

Genome enrichment dry run:

- Command: `just enrich-genomes`
- Recipes scanned: 15,827
- Organisms scanned: 36
- Already had `genome_assembly_id`: 1
- Newly resolved: 0
- Unresolved NCBITaxon-bearing organisms: 25
- Target organism entries without NCBITaxon terms: 10
- Cache: `workspace/cache/ncbi_genome_lookups.json`

Main proposal apply dry run:

- Command: `just apply-growth --proposal-dir workspace/reports/growth_evidence_proposals`
- Proposals checked: 5,713
- Already represented supported proposal applications detected: 5
- Review-only/no-support candidates skipped: 1,781
- New organisms/metrics/genomes that would be added: 0
- Interpretation: supported main proposals are already represented in YAML; remaining candidates are review-only or no-candidate searches.

Initial live PubMed batch checks:

- Command: `just propose-growth --category algae --offset 0 --limit 1 --retmax 1 --apply --write-empty`
- Reviewed record: `data/normalized_yaml/algae/1_1_dyiii_pea_gr_medium.yaml`
- Outcome: 0 candidates; negative-search proposal written to `workspace/reports/growth_evidence_proposals/1_1_dyiii_pea_gr_medium.yaml`
- Command: `just propose-growth --category algae --offset 1 --limit 5 --retmax 1 --apply --write-empty`
- Reviewed records: next 5 algae records
- Outcome: 0 candidates; negative-search proposal files written
- Command: `just propose-growth --category algae --offset 6 --limit 10 --retmax 1 --apply --write-empty`
- Reviewed records: next 10 algae records
- Outcome: 0 candidates; negative-search proposal files written
- Command: `just propose-growth --category algae --offset 41 --limit 15 --retmax 1 --apply --write-empty`
- Reviewed records: `CR1+_Diatom_Medium.yaml`, `CR1_Diatom_Medium.yaml`, `Combo_Diatom_Medium.yaml`, `Cyanidium_Medium.yaml`, `Cyanophycean_Medium.yaml`, `DYIII_Medium.yaml`, `DYV_Medium.yaml`, `Dasycladales_Seawater_Medium.yaml`, `Desmid_Medium.yaml`, `ES_10_Enriched_Seawater_Medium.yaml`, `ES_2_Enriched_Seawater_Medium.yaml`, `ES_4_Enriched_Seawater_Medium.yaml`, `Enriched_Seawater_Medium.yaml`, `Euglena_Medium.yaml`, and `F_2_Medium.yaml`
- Outcome: 13 no-candidate review records, 1 review-only candidate for `Enriched_Seawater_Medium.yaml`, and 1 supported F/2 evidence record applied to `F_2_Medium.yaml`
- Command: `just propose-growth --category algae --offset 56 --limit 15 --retmax 1 --apply --write-empty`
- Reviewed records: `HEPES_Medium.yaml`, `J_Medium.yaml`, `LDM_Medium.yaml`, `Malt_Medium.yaml`, `Modified_2X_CHEV_Medium.yaml`, `Modified_Artificial_Seawater_Medium.yaml`, `Modified_Bolds_3N_Medium.yaml`, `Modified_CHEV_Medium.yaml`, `Modified_COMBO_Medium.yaml`, `Modified_Desmidiacean_Medium.yaml`, `N_20_Medium.yaml`, `Ochromonas_Medium.yaml`, `P49_Medium.yaml`, `Polytomella_Medium.yaml`, and `Porphryridium_Medium.yaml`
- Outcome: 11 no-candidate review records and 4 records with review-only candidates. `HEPES_Medium.yaml`, `J_Medium.yaml`, and `Malt_Medium.yaml` candidates are likely false-positive literature matches outside the algae medium context. `Modified_Artificial_Seawater_Medium.yaml` matches PMID:33083143, already modeled as a variant under the `Artificial_Seawater_Medium.yaml` parent rather than duplicated as a separate applied record.
- Command: `just propose-growth --category algae --offset 71 --limit 15 --retmax 1 --apply --write-empty`
- Reviewed records: `Proteose_Medium.yaml`, `SS_Diatom_Medium.yaml`, `Snow_Algae_Medium.yaml`, `Soil_Extract_Medium.yaml`, `Soilwater_BAR_Medium.yaml`, `Soilwater_GR-_Medium.yaml`, `Soilwater_GR-_NH4_Medium.yaml`, `Soilwater_PEA_Medium.yaml`, `Soilwater_Peat_Medium.yaml`, `Soilwater_VT_Medium.yaml`, `Spirulina_Medium.yaml`, `TAP_Medium.yaml`, `Trebouxia_Medium.yaml`, `Volvocacean_Medium.yaml`, and `Volvox_Medium.yaml`
- Outcome: 12 no-candidate or review-only records plus applied evidence for `Spirulina_Medium.yaml` and `TAP_Medium.yaml`. `Soil_Extract_Medium.yaml` remains review-only because the strongest hit is genus-level Loxodes ciliate growth in liquid soil extract medium, not a strain- or species-resolved algae target.
- Command: `just propose-growth --category algae --offset 86 --limit 15 --retmax 1 --apply --write-empty`
- Reviewed records: `WC+_Medium.yaml`, `WC_Medium.yaml`, `Waris_Medium.yaml`, `a_medium.yaml`, `abm.yaml`, `ajs.yaml`, `ant.yaml`, `artificial_seawater.yaml`, `asw.yaml`, `asw_150_barley.yaml`, `asw_225_barley.yaml`, `asw_300_barley.yaml`, `asw_barley.yaml`, `asw_ses.yaml`, and `aswp.yaml`
- Outcome: 6 no-candidate review records and 9 records with review-only candidates. `artificial_seawater.yaml` included a strong Synechocystis PCC 6803 ASW hit, which was modeled under the existing `Artificial_Seawater_Medium.yaml` parent as a variant rather than duplicating evidence on the standalone SAG record. Other short-name candidates were left unapplied because they were false positives or did not directly tie growth to the target medium formulation.
- Command: `just propose-growth --category algae --offset 101 --limit 15 --retmax 1 --apply --write-empty`
- Reviewed records: `bacillariophycean.yaml`, `basal.yaml`, `bb.yaml`, `bb_merds.yaml`, `beggiatoa.yaml`, `bg.yaml`, `bg11.yaml`, `bg11_no_bicarb.yaml`, `bg11_nonitrogen.yaml`, `bg11_tes_no_bicarb.yaml`, `bg11c.yaml`, `bg11c_tes.yaml`, `bg11r.yaml`, `bg_11_0_36_nacl_medium.yaml`, and `bg_11_1_nacl_medium.yaml`
- Outcome: 10 no-candidate records, 4 records with review-only candidates, and 1 record with applied BG11 evidence. Most `basal`, `bb`, and `beggiatoa` candidates need manual review before application. `bg11.yaml` yielded supported Nostoc and Synechococcus growth evidence and was modeled as variants on the algae BG11 parent. The corpus also contains a bacterial BG11 parent, so the duplicate BG11 parent grouping should be reconciled in a later parent-medium normalization pass.
- Command: `just propose-growth --category algae --offset 116 --limit 15 --retmax 1 --apply --write-empty`
- Reviewed records: `bg_11_medium.yaml`, `bg_11_n_medium.yaml`, `bold_modified_basal.yaml`, `bold_modified_basal_tom.yaml`, `brackish_water_medium.yaml`, `bristol_nacl_medium.yaml`, `c_medium_modified.yaml`, `cgm.yaml`, `ch.yaml`, `chapman_andresens_modified_pringsheims_solution.yaml`, `chilomonas.yaml`, `chm.yaml`, `chus_medium.yaml`, `cma.yaml`, and `cr1_s_diatom_medium.yaml`
- Outcome: 9 no-candidate records, 6 records with review-only candidates, and one additional supported BG11 relationship applied to the existing algae `bg11.yaml` parent. The review-only `CGM`, `CH`, `CHM`, and `CMA` candidates are acronym false positives in the current proposal artifacts. `bg_11_medium.yaml` overlaps the BG11 parent group; the supported *Scenedesmus obliquus* ABC-009 hit from PMID:34584038 was modeled as a variant under `data/normalized_yaml/algae/bg11.yaml` rather than duplicated on `bg_11_medium.yaml`.
- Command: `just propose-growth --category algae --offset 131 --limit 15 --retmax 1 --apply --write-empty`
- Reviewed records: `cyanidium.yaml`, `desmidiacean.yaml`, `dm.yaml`, `dunaliella.yaml`, `dunaliella_acid.yaml`, `e26_biotin.yaml`, `e26_biotin_ant.yaml`, `e27.yaml`, `e31.yaml`, `e31_ant.yaml`, `ea.yaml`, `eg.yaml`, `eg_jm.yaml`, `enriched_seawater.yaml`, and `erdschreibers_medium.yaml`
- Outcome: 6 no-candidate records and 9 records with review-only candidates. `dm`, `e27`, `e31`, `ea`, and `eg` are dominated by acronym false positives. `dunaliella.yaml` includes real *Dunaliella tertiolecta* growth papers, but the abstracts do not directly tie the growth to the SAG Dunaliella Medium formulation, so no variant was applied. `enriched_seawater.yaml` includes a Provasoli Enriched Seawater seaweed cultivation hit, but the abstract does not name the six seaweed species, so it remains review-only pending full-text or source-level organism resolution.
- Command: `just propose-growth --category algae --offset 146 --limit 15 --retmax 1 --apply --write-empty`
- Reviewed records: `euglena.yaml`, `f_2.yaml`, `f_2_nh4_medium.yaml`, `f_2_si.yaml`, `f_2_si_for_heterotrophic_growth.yaml`, `fdmed.yaml`, `hsm.yaml`, `jm.yaml`, `jm_se.yaml`, `k35.yaml`, `k_medium.yaml`, `k_minimum.yaml`, `l1.yaml`, `lb.yaml`, and `maf6_se.yaml`
- Outcome: 6 no-candidate records and 7 records with review-only candidates newly counted in the manifest; `f_2_si.yaml` and `lb.yaml` proposals were refreshed from existing proposal files. The `f_2.yaml` hit from PMID:23562179 is real f/2 medium evidence but only genus-level in the abstract, so it was not applied as a specific organism-medium relationship. The `hsm.yaml` hit from PMID:38432540 reports engineered *Chlamydomonas reinhardtii* outdoor growth in modified high-salt medium with bicarbonate, but the formulation differs from the CCAP HSM parent and needs a full formulation comparison before any variant is applied. Remaining candidates are acronym or non-algal false positives.
- Command: `just propose-growth --category algae --offset 161 --limit 15 --retmax 1 --apply --write-empty`
- Reviewed records: `malt_peptone.yaml`, `masm.yaml`, `mbbm.yaml`, `mc.yaml`, `mc_ii.yaml`, `mch.yaml`, `mdy_v.yaml`, `merds.yaml`, `merds_my75s.yaml`, `mes_volvox_medium.yaml`, `met_44.yaml`, `mhy.yaml`, `modified_2x_chev_soil_medium.yaml`, `mp.yaml`, and `mw.yaml`
- Outcome: 5 no-candidate records and 10 records with review-only candidates. The only extracted growth metric came from a human tumor cell line paper matched to the short name `mch`, not from an algae medium. `malt_peptone.yaml` found a fungal medium-optimization hit, but the source does not support the SAG algae Malt Peptone medium as a parent or variant. The remaining candidates are short-name or acronym false positives, so no YAML evidence was applied.
- Command: `just propose-growth --category algae --offset 176 --limit 15 --retmax 1 --apply --write-empty`
- Reviewed records: `mwc.yaml`, `my75s.yaml`, `n75s.yaml`, `n75s_nsw.yaml`, `ncl.yaml`, `ncl75s.yaml`, `ncl_0_01_npa.yaml`, `ncl_mp.yaml`, `ncl_pj.yaml`, `ncl_pj_0_01_npa.yaml`, `nn.yaml`, `note_on_biphasic_soilwater_media_20081216.yaml`, `nss_low.yaml`, `ochromonas.yaml`, and `pas.yaml`
- Outcome: 9 no-candidate records and 6 records with review-only candidates. The `ochromonas.yaml` candidates include real *Ochromonas danica* growth evidence, including a 7.6 h doubling time in sonication-generated waste-activated-sludge supernatant, but that formulation is not the CultureMech Ochromonas medium parent or a small variant of it. `nn.yaml`, `pas.yaml`, `mwc.yaml`, and `ncl.yaml` are dominated by acronym or non-medium matches. No YAML evidence was applied.
- Command: `just propose-growth --category algae --offset 191 --limit 15 --retmax 1 --apply --write-empty`
- Reviewed records: `pc.yaml`, `pe.yaml`, `per.yaml`, `pes.yaml`, `pj.yaml`, `pj_nn.yaml`, `pm.yaml`, `polytoma.yaml`, `polytomella.yaml`, `porphyridium.yaml`, `pp.yaml`, `ppg.yaml`, `ppy.yaml`, `r75s.yaml`, and `r75s_nsw.yaml`
- Outcome: 3 no-candidate records and 12 records with review-only candidates. `porphyridium.yaml` has credible *Porphyridium* growth evidence in Pm, F/2, and Hemerick media, including biomass and doubling-time data from PMID:38131141, but the local SAG Porphyridium parent has incomplete composition and the evidence media cannot yet be confirmed as a parent match or small variant. `polytomella.yaml` and `polytoma.yaml` hits name the organisms but not the target medium formulation. The remaining records are short-name/acronym false positives. No YAML evidence was applied.
- Command: `just propose-growth --category algae --offset 206 --limit 15 --retmax 1 --apply --write-empty`
- Reviewed records: `rpl.yaml`, `rpl_0_01_rpa.yaml`, `rpl_mp.yaml`, `rpl_pj.yaml`, `rpl_pj_0_01_rpa.yaml`, `s77_vitamins.yaml`, `s88_vitamins.yaml`, `s_w.yaml`, `s_w_amp.yaml`, `s_w_ca.yaml`, `sbbm.yaml`, `se1.yaml`, `se2.yaml`, `seawater.yaml`, and `ses.yaml`
- Outcome: 8 no-candidate records and 7 records with review-only candidates. A transient PubMed connection reset was reported for PMID:27339032, but proposals were still written for all 15 records. `seawater.yaml` includes broad seawater cultivation and halophytic algae evidence, but not a specific CultureMech parent or small variant. `rpl`, `s_w`, `sbbm`, `se1`, `se2`, and `ses` candidates are short-code or non-medium false positives. No YAML evidence was applied.
- Command: `just propose-growth --category algae --offset 221 --limit 15 --retmax 1 --apply --write-empty`
- Reviewed records: `ses_mp.yaml`, `ses_pj.yaml`, `sna.yaml`, `sna_5.yaml`, `soil_extract_sodium_metasilicate_medium.yaml`, `soil_seawater_medium.yaml`, `soil_water_media.yaml`, `soilwater_gr_medium.yaml`, `soilwater_gr_nh4_medium.yaml`, `sp.yaml`, `spirulina.yaml`, `ucm.yaml`, `um.yaml`, `unicellular_green_algae.yaml`, and `volvocacean_3n_medium.yaml`
- Outcome: 8 no-candidate records and 6 records with review-only candidates newly counted in the manifest; `spirulina.yaml` proposal refreshed an existing file. `spirulina.yaml` overlaps the already modeled Spirulina/Arthrospira parent group, but the candidate abstracts do not establish a better formulation-specific variant. `unicellular_green_algae.yaml` names algae but not the target medium formulation. `sna`, `sna_5`, `sp`, `ucm`, and `um` are non-medium or short-code false positives. No YAML evidence was applied.
- Command: `just propose-growth --category algae --offset 236 --limit 25 --retmax 1 --apply --write-empty`
- Reviewed records: `volvox.yaml`, `volvox_dextrose_medium.yaml`, `walnes.yaml`, `waris_h.yaml`, `waris_soil_extract_medium.yaml`, `wees.yaml`, `wmy.yaml`, `woods_hole_mbl_medium.yaml`, `yel.yaml`, `ypd_agar.yaml`, `z_medium_for_cyanos.yaml`, and `zm_10.yaml`
- Outcome: 6 no-candidate records and 6 records with review-only candidates. `walnes.yaml` has broad microalgae/cyanobacteria growth-medium evidence, but the abstract does not resolve strain-level or formulation-specific relationships for this parent. `ypd_agar.yaml` matches yeast/fungal cultivation rather than an algae medium relationship. `volvox.yaml`, `wees.yaml`, `wmy.yaml`, and `yel.yaml` were not medium-specific. No YAML evidence was applied. This completed manifest-level coverage for all 248 records in `data/normalized_yaml/algae`.

Archaea PubMed batch checks:

- Command: `just propose-growth --category archaea --offset 0 --limit 15 --retmax 1 --apply --write-empty`
- Reviewed records: first 15 sorted archaea records, from `DSMZ_1399_HALOPHILIC_MEDIUM.yaml` through `halophilic_methanotrophic_bacterium_medium.yaml`
- Outcome: 15 no-candidate proposal files written; no supported organism-medium relationships found by the configured search.
- Command: `just propose-growth --category archaea --offset 15 --limit 15 --retmax 1 --apply --write-empty`
- Reviewed records: next 15 sorted archaea records, from `halophilic_sob_medium.yaml` through `methanogenium_medium_h2_co2.yaml`
- Outcome: 15 no-candidate proposal files written; no supported organism-medium relationships found by the configured search.
- Command: `just propose-growth --category archaea --offset 30 --limit 15 --retmax 1 --apply --write-empty`
- Reviewed records: next 15 sorted archaea records, from `methanogens_saline_water_medium.yaml` through `modified_balchs_methanogen_medium_1_b.yaml`
- Outcome: 15 no-candidate proposal files written; no supported organism-medium relationships found by the configured search.
- Command: `just propose-growth --category archaea --offset 45 --limit 30 --retmax 1 --apply --write-empty`
- Reviewed records: final 18 sorted archaea records, from `modified_balchs_methanogens_medium.yaml` through `treponema_thermophilum_medium.yaml`
- Outcome: 18 no-candidate proposal files written; no supported organism-medium relationships found by the configured search. This completed manifest-level coverage for all 63 records in `data/normalized_yaml/archaea`.

Fungal PubMed batch checks:

- Command: `just propose-growth --category fungal --offset 0 --limit 25 --retmax 1 --apply --write-empty`
- Reviewed records: first 25 sorted fungal records, from `1_10_r2a_medium_modified_yeast_extract.yaml` through `czapek_solution_agar_b.yaml`
- Outcome: 21 no-candidate records and 4 review candidates across `2_malt_agar.yaml` and `czapek_dox_agar.yaml`; no YAML evidence applied.
- Command: `just propose-growth --category fungal --offset 25 --limit 25 --retmax 1 --apply --write-empty`
- Reviewed records: next 25 sorted fungal records, from `czapek_yeast_extract_agar_cya.yaml` through `malt_extract_agar_with_15_nacl.yaml`
- Outcome: 20 no-candidate records and 5 review candidates across `glucose_yeast_extract_medium.yaml` and `malt_extract_agar.yaml`; the extracted *Salinivibrio costicola* doubling-time candidate is not an exact match to the DSMZ 54 solid/agar-capable formulation and remains review-only.
- Command: `just propose-growth --category fungal --offset 50 --limit 25 --retmax 1 --apply --write-empty`
- Reviewed records: next 25 sorted fungal records, from `malt_extract_glucose_agar.yaml` through `saline_tryptone_yeast_extract_broth.yaml`
- Outcome: 21 no-candidate records and 4 review candidates across `potato_dextrose_agar.yaml` and `sabouraud_glucose_medium.yaml`; candidates were plausible cultivation leads but lacked strain/genome resolution or usable abstract snippets for applied evidence.
- Command: `just propose-growth --category fungal --offset 75 --limit 25 --retmax 1 --apply --write-empty`
- Reviewed records: next 25 sorted fungal records, from `sea_salts_yeast_extract_glucose_medium.yaml` through `yeast_extract_malt_extract_agar_isp_2_with_2_nacl.yaml`
- Outcome: 21 no-candidate records and 4 review candidates across trypticase/tryptone yeast extract records; candidates were bacterial or mixed antimicrobial-assay contexts and were not applied.
- Command: `just propose-growth --category fungal --offset 100 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: final 24 sorted fungal records, from `yeast_extract_malt_extract_agar_isp_2_with_5_nacl.yaml` through `yeastextrakt_mannitol_medium.yaml`
- Outcome: 23 no-candidate records and 1 review candidate for `yeast_extract_mannitol_agar_medium.yaml`; the candidate was rhizobial, lacked a usable evidence snippet, and was not applied. This completed manifest-level coverage for all 124 records in `data/normalized_yaml/fungal`.

Specialized PubMed batch checks:

- Command: `just propose-growth --category specialized --offset 0 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: first 50 sorted specialized records, from `1_2_tryptic_soy_broth_anaerobic.yaml` through `bhis_k3_noglucose.yaml`
- Outcome: 43 no-candidate records, 6 review-candidate records, and one applied BHIS evidence record. Most candidates were broad short-name matches (`7h9`, `abb`, `acy`, `bhi`) or lacked usable snippets. `bhis.yaml` had strain-specific quantitative evidence for *Brachyspira pilosicoli* P43/6/78T growth in BHIS broth and was manually curated as a variant plus target-organism growth metric.
- Command: `just propose-growth --category specialized --offset 50 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted specialized records, from `bhis_pipes.yaml` through `ird_marine_desulfovibrio_medium_2.yaml`
- Outcome: 43 no-candidate records and 7 records with review candidates. The only extracted metric was a Brucella OD phase from a Brucella biology/genome-structure paper, not evidence that the local Brucella broth formulation supports a named strain under defined conditions, so no YAML evidence was applied.
- Command: `just propose-growth --category specialized --offset 100 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted specialized records, from `ird_marine_desulfovibrio_medium_3.yaml` through `marine_medium_with_thiosulfate.yaml`
- Outcome: 42 no-candidate records and 8 records with review candidates. Metric-bearing short-code candidates were false positives or already covered by existing M9 evidence; no YAML evidence was applied.
- Command: `just propose-growth --category specialized --offset 150 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted specialized records, from `marine_methanobacterium_medium.yaml` through `mhii_biocarbonate_serum.yaml`
- Outcome: 44 no-candidate records and 6 records with review candidates. The only extracted metric was a *Chlorella* acetate-growth false positive matched to short code `MGL`, not the MGL medium; no YAML evidence was applied.
- Command: `just propose-growth --category specialized --offset 200 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted specialized records, from `mhii_biocarbonate_serum_chelated.yaml` through `mrs_recovery.yaml`
- Outcome: 47 no-candidate records and 3 records with review candidates. No candidates had extracted growth metrics or genome IDs; no YAML evidence was applied.
- Command: `just propose-growth --category specialized --offset 250 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted specialized records, from `ms_basal_salts_robin.yaml` through `propionigenium_modestum_medium_marine.yaml`
- Outcome: 39 no-candidate records and 11 records with review candidates. The metric-bearing `NFM` candidate was neuronal cell growth, not nitrogen-fixing medium evidence; no YAML evidence was applied.
- Command: `just propose-growth --category specialized --offset 300 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted specialized records, from `pye.yaml` through `rpmi.yaml`
- Outcome: 46 no-candidate records and 4 records with review candidates. No candidates had extracted growth metrics or genome IDs; no YAML evidence was applied.
- Command: `just propose-growth --category specialized --offset 350 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted specialized records, from `rpmi_with_fetal_bovine_serum.yaml` through `varel_bryant_medium_glucose_homopipes.yaml`
- Outcome: 45 no-candidate records and 5 records with review candidates. The Terrific Broth growth-rate hit did not tie the metric to the formulation with sufficient strain/formulation detail, so no YAML evidence was applied.
- Command: `just propose-growth --category specialized --offset 400 --limit 100 --retmax 1 --apply --write-empty`
- Reviewed records: final 55 sorted specialized records, from `varel_bryant_medium_glucose_lowcys_nonitrogen.yaml` through `zmb_nofolicacid.yaml`
- Outcome: 50 no-candidate records and 5 records with review candidates. No candidates had extracted growth metrics or genome IDs. This completed manifest-level coverage for all 455 records in `data/normalized_yaml/specialized`.

Bacterial PubMed batch checks:

- Command: `just propose-growth --category bacterial --offset 0 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: first 50 sorted bacterial records, from `0_01_lb_seawater_medium.yaml` through `1_3_lb.yaml`
- Outcome: 49 no-candidate records and 1 record with a review-only false-positive candidate. `1_3_lb.yaml` matched PMID:6368150, a diabetes follow-up paper retrieved by the text string `1/3 LB`; it does not provide microbial growth evidence, organism identifiers, growth metrics, or genome IDs. No YAML evidence was applied.
- Command: `just propose-growth --category bacterial --offset 50 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `1_3_lb_agar.yaml` through `5_x_r2a_agar.yaml`
- Outcome: 43 no-candidate records and 7 records with review-only candidates. Candidates were not applied because they lacked strain/formulation support or were out-of-scope matches: `1_ogawa_medium.yaml` was broad AFB culture-method evidence without resolved organism or strain; `25_glucose_medium.yaml`, `2_malt_agar.yaml`, and `2_malt_extract_agar.yaml` were fungal or non-bacterial context hits; `2asw.yaml` was diatom evidence; and `2_x_yt_medium.yaml`/`2yt_medium.yaml` mentioned engineered *E. coli* but lacked enough strain and formulation detail in the proposal evidence to model a supported variant.
- Command: `just propose-growth --category bacterial --offset 100 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `6_b_medium.yaml` through `DSMZ_969_SULFOBACILLUS_MEDIUM.yaml`
- Outcome: 40 no-candidate records and 10 records with review-only candidates. No candidate had extracted growth metrics or genome assembly IDs. `CCAP_C18_BG11₀.yaml` produced BG11/BG110 candidates already represented or better handled under the existing BG11 parent reconciliation work. `DSMZ_1753_SEAWATER_MEDIUM.yaml` produced a plausible PRT1 seawater-medium lead with a 36 h doubling-time snippet, but the proposal does not establish that the reported formulation matches DSMZ Medium 1753, so it remains review-only. The remaining candidates were short-name, clinical, fungal, plant/cell-culture, or broad cultivation-method matches and were not applied.
- Command: `just propose-growth --category bacterial --offset 150 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `DSMZ_983_ONR7a_MEDIUM.yaml` through `JCM_J19_BIFIDOBACTERIUM_MEDIUM.yaml`
- Outcome: 42 no-candidate records and 8 records with review-only candidates. One metric-bearing candidate on `DSMZ_994_MINERAL_MEDIUM.yaml` matched the already represented *Acidiphilium cryptum* glucose-mineral medium evidence, not a supported exact match to the generic DSMZ mineral medium parent. `JCM_J119_BCYE_AGAR.yaml` found a broad Legionella handling source without strain/genome detail. Corn meal agar and oatmeal agar candidates were fungal or oomycete contexts, and the remaining candidates lacked formulation-specific growth support. No YAML evidence was applied.
- Command: `just propose-growth --category bacterial --offset 200 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `JCM_J201_BSK_MEDIUM.yaml` through `JCM_J467_BHI_2_MEDIUM.yaml`
- Outcome: 45 no-candidate records and 5 records with review-only candidates. `JCM_J201_BSK_MEDIUM.yaml` found Borrelia BSK/modified-BSK leads but no strain/genome or exact formulation support in the proposal. `JCM_J220_SC_MEDIUM.yaml` and `JCM_J404_YPG_MEDIUM.yaml` were yeast/fungal medium-name matches, `JCM_J40_GLUCOSE-ASPARAGINE_AGAR.yaml` lacked usable organism/formulation support, and `JCM_J466_MYCOBACTERIUM_MEDIUM.yaml` was a clinical Histoplasma recovery context rather than a supported Mycobacterium-medium growth relationship. No YAML evidence was applied.
- Command: `just propose-growth --category bacterial --offset 250 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `JCM_J468_VEILLONELLA_MEDIUM.yaml` through `JCM_J876_DESULFONEMA_MAGNUM_MEDIUM.yaml`
- Outcome: 42 no-candidate records and 8 records with review-only candidates. A transient NCBI HTTP 500 occurred, but proposal files were still written for all 50 records. Candidate-bearing records lacked actionable strain/formulation support: `JCM_J510_NMS_MEDIUM.yaml` and `JCM_J74_NUTRIENT_AGAR.yaml` had broad growth snippets without exact parent support; `JCM_J54_POTATO-CARROT_AGAR.yaml` was fungal; `JCM_J806_GS_MEDIUM.yaml` was tissue-preservation context; and `JCM_J840_YPM_MEDIUM.yaml` mixed bacterial/yeast leads without a safe parent match. No YAML evidence was applied.
- Command: `just propose-growth --category bacterial --offset 300 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `JCM_J881_KNH_MEDIUM.yaml` through `KOMODO_1044_GLUCONACETOBACTER_RHAETICUS_medium.yaml`
- Outcome: 43 no-candidate records and 7 records with review-only candidates. One metric-bearing `KOMODO_1007_MINERAL_MEDIUM.yaml` candidate matched the already modeled *Acidiphilium cryptum* glucose-mineral medium evidence rather than a safe exact match to the KOMODO mineral parent. `KOMODO_1010_Artificial_SEAWATER_MEDIUM.yaml` duplicated an artificial-seawater relationship already modeled under the algae artificial seawater parent. The remaining candidates were broad basal/mineral medium hits, yeast/fungal YPG/YPGA hits, or formulation-uncertain Thermus/YMA matches. No YAML evidence was applied.
- Command: `just propose-growth --category bacterial --offset 350 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `KOMODO_1046_ANOXYBACILLUS_AMYLOLYTICUS_medium.yaml` through `KOMODO_1107_DIALISTER_medium.yaml`
- Outcome: 42 no-candidate records and 8 records with review candidates. Most candidates were weak text matches (`DEXTRAN medium`, `A1-MEDIUM`, `YM medium`, `PY-BROTH`, `SP4 MEDIUM`) or lacked enough strain/formulation support. `KOMODO_1078_FRIIS_medium.yaml` had direct Mycoplasma hyopneumoniae growth-kinetics evidence in modified Friis medium, so a Friis parent variant and target-organism growth metric were added for the seven named isolates.
- Command: `just propose-growth --category bacterial --offset 400 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `KOMODO_1108_CYS_MEDIUM.yaml` through `KOMODO_1162_THIOPHAEOCOCCUS_MANGROVI_medium.yaml`
- Outcome: 42 no-candidate records and 8 review-only candidates. A transient NCBI HTTP 502 occurred but proposal files were written for all 50 records. Candidate records were short-code or broad medium-name matches (`CARBOXYMETHYL CELLULOSE medium`, `MEDIUM K`, `LC 2`, `TY medium`), several were non-microbial cell-culture hits, and none had extracted genome IDs or actionable formulation-specific growth metrics. No YAML evidence was applied.
- Command: `just propose-growth --category bacterial --offset 450 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `KOMODO_1164_HALOMICROBIUM_KATESII_medium.yaml` through `KOMODO_1218_ROSEINATRONOBACTER_MONICUS_medium.yaml`
- Outcome: 37 no-candidate records and 13 records with review candidates. Most candidates were yeast/fungal YPS/YPG hits, plant or cell-culture false positives, or broad medium-name matches. `KOMODO_11_MRS_medium.yaml` had direct strain-specific MRS growth-kinetics evidence for *Heyndrickxia coagulans* ATCC 7050 and *Lactiplantibacillus plantarum* ATCC 10012, so an MRS oxygen-condition variant and two target-organism growth metrics were added. No other YAML evidence was applied.
- Command: `just propose-growth --category bacterial --offset 500 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `KOMODO_1219_METHYLOVIRGULA_LIGNI_medium.yaml` through `KOMODO_1289_ALCANIVORAX_BALERICUS_medium.yaml`
- Outcome: 45 no-candidate records and 5 review-only candidates. `KOMODO_1235_XYLAN_medium.yaml` had organism and growth-context leads, but no exact parent-medium/formulation support or usable growth metrics; `KOMODO_1247_TYB.yaml`, `KOMODO_1278_HYL_medium.yaml`, and `KOMODO_1283_KR_medium.yaml` were short-code, historical-method, or broad isolation-medium matches. No YAML evidence was applied.
- Command: `just propose-growth --category bacterial --offset 550 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `KOMODO_1294_DESULFURISPIRILLUM_INDICUM_MEDIUM.yaml` through `KOMODO_144_THERMOANAEROBIUM_medium.yaml`
- Outcome: 41 no-candidate records and 9 review-only candidates. Potato dextrose agar hits were fungal or yeast contexts, soil-extract candidates lacked strain/formulation support for the local parent, and MMN/M2 candidates were plant, animal, or fungal false positives. No candidates had extracted growth metrics or genome IDs. No YAML evidence was applied.
- Command: `just propose-growth --category bacterial --offset 600 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `KOMODO_1451_DEFERRISOMA_medium.yaml` through `KOMODO_218_BHI_3_medium.yaml`
- Outcome: 41 no-candidate records and 9 review-only candidates. YpSs and corn meal agar candidates were fungal contexts; nutrient agar candidates were broad methods or non-parent formulation evidence; the BHI candidate described modified-BHI/Akkermansia work but lacked strain, exact formulation, and metric detail needed for a safe parent/variant application. No YAML evidence was applied.
- Command: `just propose-growth --category bacterial --offset 650 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `KOMODO_219_MYCOBACTERIUM_medium.yaml` through `KOMODO_292_ACIDAMINOBACTER_medium.yaml`
- Outcome: 42 no-candidate records and 8 review-only candidates. Candidate records included Histoplasma recovery in radiometric Mycobacterium medium, Bacillus lipase/SP-medium optimization, Pichia/fungal BMM context, plant-based seawater microbiome medium, Optisol GS corneal preservation, Mycobacterium avium paratuberculosis medium optimization without exact J-agar strain/metric support, and fungal tomato-juice context. No candidates had extracted growth metrics or genome IDs. No YAML evidence was applied.
- Command: `just propose-growth --category bacterial --offset 700 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `KOMODO_294_PELOBACTER_ACIDIGALLICI_MEDIUM.yaml` through `KOMODO_360_YPM_medium.yaml`
- Outcome: 43 no-candidate records and 7 records with review-only candidates. Candidate records included chromogenic Vibrio detection medium, Clostridium difficile selective neomycin agar, fungal/oomycete V-8 juice agar contexts, Fastidious Anaerobe Agar disk-diffusion and anaerobe-cultivation studies, a Sporohalobacter salinus species-description lead without exact parent support, a Löwenstein-Jensen tuberculosis diagnostic context, and YPM medium leads from yeast, Micrococcus degradation, and cacao-mucilage medium studies. No candidates had extracted growth metrics or genome IDs. No YAML evidence was applied.
- Command: `just propose-growth --category bacterial --offset 750 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `KOMODO_362_FLAVOBACTERIUM_TIRRENICUM_medium.yaml` through `KOMODO_429a_COLUMBIA_BLOOD_AGAR_WITH_CHARCOAL.yaml`
- Outcome: 46 no-candidate records and 4 records with review candidates. YPD candidates were yeast growth studies, oatmeal agar candidates were fungal growth studies, and BSK candidates were Borrelia modified-BSK leads without enough local-parent formulation resolution for automated application. `KOMODO_429_COLUMBIA_BLOOD_AGAR.yaml` had primary-literature and BacDive support for *Staphylococcus saccharolyticus* ATCC 14953 / DSM 20359 / NCTC 11807 growth on Columbia blood medium, so a variant, target organism, qualitative growth metric, and genome/BioSample identifiers were added. No other YAML evidence was applied.
- Command: `just propose-growth --category bacterial --offset 800 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `KOMODO_429b_CHOCOLATE_AGAR.yaml` through `KOMODO_469_YM-CATALASE_medium.yaml`
- Outcome: 46 no-candidate records and 4 records with review-only candidates. Chocolate agar candidates were broad methods or Brucella review contexts, sucrose-peptone was a fungal EPS cultivation hit, EDTA medium mixed an EDTA-degrading bacterium lead with a non-microbial false positive, and plate count agar candidates were bioburden/plant-growth contexts. No candidates had extracted growth metrics or genome IDs. No YAML evidence was applied.
- Command: `just propose-growth --category bacterial --offset 850 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `KOMODO_471_ALCALIGENES_XYLOSOXYDANS_MEDIUM_WITH_BENZOATE.yaml` through `KOMODO_547_ISP_medium_4.yaml`
- Outcome: 45 no-candidate records and 5 records with review-only candidates. Thioglycolate matched a Trichomonas diagnostic medium, trypticase soy broth agar matched a plant-pathology isolation context, TSB hits lacked strain/formulation support, and ISP medium 4 matched a Streptomyces species-description lead without enough local-parent support. `KOMODO_531_SPORULATION_medium.yaml` had a real *Bacillus subtilis* doubling-time hit in a single chemically defined sporulation medium, but the local parent is a complex solid KOMODO/DSMZ sporulation medium, so it was not applied as a parent or variant. No YAML evidence was applied.
- Command: `just propose-growth --category bacterial --offset 900 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `KOMODO_548_BENNETT_S_AGAR.yaml` through `KOMODO_621a_EKHO_LAKE_STRAINS_medium.yaml`
- Outcome: 46 no-candidate records and 4 records with review-only candidates. `KOMODO_563_Z_medium.yaml` matched ambiguous fungal/algal Z-medium contexts, `KOMODO_585_BCYE_AGAR.yaml` matched a Legionella culture-handling chapter without extracted strain-specific evidence, `KOMODO_58_BIFIDOBACTERIUM_medium.yaml` matched fecal bifidobacteria selective-plating evidence without strain IDs, and `KOMODO_595_CAULOBACTER_medium.yaml` matched a Gemmata/Caulobacter-medium method lead without extracted identifiers. No candidates had extracted growth metrics or genome IDs. No YAML evidence was applied.
- Command: `just propose-growth --category bacterial --offset 950 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `KOMODO_623_THERMOCOCCUS_LITORALIS_medium.yaml` through `KOMODO_696_STREPTOCOCCUS_SUIS_medium.yaml`
- Outcome: 42 no-candidate records and 8 records with review-only candidates. NMS medium matched methanotroph enrichment evidence but lacked strain/genome specificity in the cached abstract; RCM candidates were mixed stool-microflora and periodontal antimicrobial contexts; rabbit blood agar candidates lacked resolved strain/formulation evidence; PYE matched *Deinococcus indicus* DR1 and an amoeba cultivation context without enough formulation detail; DP and YEPG candidates were cyanobacterial/fungal or yeast contexts; MS-medium hits were plant tissue-culture or transformation contexts. No candidates had extracted growth metrics or genome IDs. No YAML evidence was applied.
- Command: `just propose-growth --category bacterial --offset 1000 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `KOMODO_697_TODD-HEWITT_medium.yaml` through `KOMODO_762_HALOMONAS_DESIDERATA_MEDIUM.yaml`
- Outcome: 44 no-candidate records, 5 records with review-only candidates, and 1 record with manually applied evidence. Todd-Hewitt, Columbia agar, rich medium, SC medium, and Halomonas pantelleriense candidates lacked enough cached-abstract strain/formulation support for application. `KOMODO_761_HALOTHERMOTHRIX_ORENII.yaml` had primary-literature strain H168 growth evidence at 60 C in 100 g/L NaCl medium, and NCBI BioProject PRJNA16377 provided `GCA_000020485.1` and `SAMN00623047`; a high-salt strict-anaerobic variant and target organism entry were added. No automated proposal writes remained after dry-run application.
- Command: `just propose-growth --category bacterial --offset 1050 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml` through `KOMODO_818_CHRYSIOGENES_MEDIUM.yaml`
- Outcome: 50 no-candidate records. No review candidates, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied.
- Command: `just propose-growth --category bacterial --offset 1100 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `KOMODO_81_MINERAL_MEDIUM_FOR_CHEMOLITHOTROPHIC_GROWTH_H-3.yaml` through `KOMODO_882_LEPTOSPIRILLUM_HH_MEDIUM.yaml`
- Outcome: 46 no-candidate records and 4 records with review-only candidates. R2A candidates were broad recovery/cultivation-method evidence, AE medium candidates were oral-streptococci selective-medium and bacterial-cellulose contexts, starch nitrate medium was marine actinomycete enumeration without strain-level support, and glucose-peptone candidates were unrelated cow-milk/yeast contexts. No candidates had extracted growth metrics or genome IDs. No YAML evidence was applied.
- Command: `just propose-growth --category bacterial --offset 1150 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `KOMODO_883_CALDIVIRGA_medium.yaml` through `KOMODO_934_THERMOCOCCUS_WAIOTAPUENSE_medium.yaml`
- Outcome: 45 no-candidate records and 5 records with review-only candidates. Tween 80 agar matched Candida identification context, OS medium matched human cell-culture work, TS agar matched Listeria resuscitation work without strain/formulation support, Pseudomonas agar F matched selective-agent screening without strain IDs, and the Alkalibacterium candidate was taxonomy/growth-range context without medium formulation support. No candidates had extracted growth metrics or genome IDs. No YAML evidence was applied.
- Command: `just propose-growth --category bacterial --offset 1200 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `KOMODO_935_DEFERRIBACTER_medium.yaml` through `KOMODO_993b_MODIFIED_ISP5_medium.yaml`
- Outcome: 48 no-candidate records and 2 records with review-only candidates. `KOMODO_955_AG_medium.yaml` was a non-microbial *Caenorhabditis elegans* false match. `KOMODO_990_YPS_medium.yaml` matched a yeast extract-peptone-sucrose study for *Saccharomyces cerevisiae* PE-2, but the CultureMech parent is a seawater/sulfur YPS formulation without sucrose, so it was not modeled as a variant of this parent. No candidates had extracted genome IDs. No YAML evidence was applied.
- Command: `just propose-growth --category bacterial --offset 1250 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `KOMODO_993c_MODIFIED_ISP5_MEDIUM_WITH_SODIUM_CHLORIDE.yaml` through `MEDIADB_455_Defined_freshwater_medium_CoCl2.yaml`
- Outcome: 49 no-candidate records and 1 record with review-only candidates. `KOMODO_994_MINERAL_MEDIUM.yaml` had four broad mineral-medium candidates; the Acidiphilium doubling-time hit is already represented under an acidophilic pH 3 glucose-mineral medium parent, not this pH 6.8 DSMZ/KOMODO mineral medium, and the Listeria defined-mineral-medium hit lacked enough cached formulation detail to attach safely as a variant. No YAML evidence was applied.
- Command: `just propose-growth --category bacterial --offset 1300 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `MEDIADB_456_Defined_freshwater_medium_CoCl2.yaml` through `NBRC_1311.yaml`
- Outcome: 26 no-candidate records and 24 records with review-only candidates. Most candidate-bearing records were numeric NBRC media names whose searches matched unrelated numerical strings in articles, strain IDs, OD values, page identifiers, or concentrations. The only extracted doubling-time hit was for an anaerobic rumen fungus on glucose/xylose and did not match the NBRC 1210 parent formulation. No candidates had extracted genome IDs. No YAML evidence was applied.
- Command: `just propose-growth --category bacterial --offset 1350 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `NBRC_1323.yaml` through `TOGO_M1006_Desulfohalobium_Utahense_Medium.yaml`
- Outcome: 9 no-candidate records and 41 records with review-only candidates. This batch was dominated by numeric NBRC media names whose searches matched unrelated numerical strings; representative checks showed non-microbial cancer/doubling-time false positives, plant-growth Bacillus formulation work without a parent match, and review-only cultivation contexts. `NBRC_NUTRIENT_AGAR.yaml` had broad method/cultivation hits without strain-specific medium evidence, and `NBRC_YPG_MEDIUM.yaml` had fungal/yeast contexts outside the bacterial parent target. No candidates had extracted growth metrics or genome IDs. No YAML evidence was applied.
- Command: `just propose-growth --category bacterial --offset 1400 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `TOGO_M1007_Sea_Salts_TYG_Medium.yaml` through `TOGO_M1059_Acidic_HB-1_Medium.yaml`
- Outcome: 46 no-candidate records and 4 records with review-only candidates. `TOGO_M1016_PA_Medium.yaml` and the two M30 records matched non-microbial or unrelated false positives. `TOGO_M1022_Artificial_Seawater_Medium.yaml` matched the Hemiaulus-Richelia artificial-seawater evidence already represented under the algae artificial-seawater parent, so it was not duplicated on the bacterial TOGO artificial-seawater record. No candidates had extracted growth metrics or genome IDs. No YAML evidence was applied.
- Command: `just propose-growth --category bacterial --offset 1450 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `TOGO_M105_R_Agar_With_3_NaCl.yaml` through `TOGO_M1118_Endomicrobium_Proavitum_RSA_Medium.yaml`
- Outcome: 50 no-candidate records. No review candidates, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied.
- Command: `just propose-growth --category bacterial --offset 1500 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `TOGO_M1119_573C_Medium.yaml` through `TOGO_M116_Myxococcus_Flavescens_Medium.yaml`
- Outcome: 44 no-candidate records and 6 records with review-only candidates. `TOGO_M111_BCYE_Agar.yaml` matched a broad Legionella culture-handling chapter without extracted strain/genome or metric evidence. `TOGO_M113_Benzoate_Medium.yaml` had a benzoate-medium doubling-time snippet for an unnamed subset of environmental isolates, but no named organism or strain support. `TOGO_M1165_Bicarbonate_Buffered_Medium.yaml` through `TOGO_M1168_Bicarbonate_Buffered_Medium.yaml` matched bovine oocyte in vitro culture work, not microbial growth-medium evidence. No candidates had extracted growth metrics or genome IDs, and no YAML evidence was applied.
- Command: `just propose-growth --category bacterial --offset 1550 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `TOGO_M1170_Seawater_Pyruvate_Thiosulfate_Medium.yaml` through `TOGO_M1226_Abyssisolibacter_Medium.yaml`
- Outcome: 49 no-candidate records and 1 record with a review-only candidate. `TOGO_M1210_YCFA_Medium.yaml` matched a gut microbial interaction/pairwise cultivation paper, but the proposal did not extract a named organism, strain, metric, genome ID, or evidence snippet tying a specific organism to the CultureMech YCFA parent. No YAML evidence was applied.
- Command: `just propose-growth --category bacterial --offset 1600 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `TOGO_M1227_Modified_Roseospira_Medium.yaml` through `TOGO_M1281_Acidihalobacter_Medium.yaml`
- Outcome: 45 no-candidate records and 5 records with review-only candidates. `TOGO_M1236_K_Medium.yaml` and `TOGO_M1263_M_Medium.yaml` were short-name false positives from clinical, plant, or animal studies. `TOGO_M1245_Modified_Baar_s_Medium.yaml` named biofilm/corrosion organisms but lacked strain, metric, or snippet support. `TOGO_M1252_A7_Medium.yaml` was genital mycoplasma culture-method evidence without strain-level support. `TOGO_M124_Medium_10.yaml` included a real *Streptococcus bovis* / *Streptococcus equinus* characterization lead from PMID:15355536, but the abstract only states that doubling time was determined in basal medium 10 with glucose and does not provide values, full culture conditions, or a clear match to the local solid-agar parent; it remains review-only pending full-text/source-formulation comparison. No YAML evidence was applied.
- Command: `just propose-growth --category bacterial --offset 1650 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `TOGO_M1282_Acidihalobacter_Prosperus_F5_Medium.yaml` through `TOGO_M1342_Mineral_Salts_Medium_With_TCE.yaml`
- Outcome: 48 no-candidate records and 2 records with review-only candidates, one of which was already represented by applied YAML evidence. `TOGO_M12_Bifidobacterium_Medium.yaml` matched human-feces selective-plating work without strain/formulation support. `TOGO_M1308_Methylotroph_Medium.yaml` produced an additional *Methylovorus mays* enzyme-characterization paper, but the supported methylotroph growth relationships for *Methylosinus* sp. Ce-a6 and *Methylovorus mays* are already represented in the YAML/report. No new YAML evidence was applied.
- Command: `just propose-growth --category bacterial --offset 1700 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `TOGO_M1343_TYG-Acetate_Medium.yaml` through `TOGO_M1399_Sea_Salts_YTG_Medium.yaml`
- Outcome: 50 no-candidate records. No review candidates, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied.
- Command: `just propose-growth --category bacterial --offset 1750 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `TOGO_M139_Oatmeal_Agar.yaml` through `TOGO_M1579_PE_Medium.yaml`
- Outcome: 35 no-candidate records, 14 records with review-only candidates, and 1 record with manually applied exact-parent evidence. Fungal/yeast or broad clinical-method candidates from oatmeal agar, corn meal agar, YM/YPD, blood agar, Trypticase soy agar, Todd-Hewitt, GAM, Caulobacter, and Bifidobacterium records were not applied because they lacked strain/formulation support or represented non-bacterial contexts. `TOGO_M1523_MRS_Medium.yaml` reproduced the already applied ATCC 7050 / ATCC 10012 MRS evidence under the existing KOMODO MRS parent and was not duplicated. `TOGO_M1547_Marine_Agar_2216.yaml` had direct species-description evidence for *Sneathiella glossodoripedis* MKT133T colony formation on Marine Agar 2216 at 30 C after 4-5 days; exact-parent target-organism evidence and GCA/GCF genome identifiers were added to that YAML record.
- Command: `just propose-growth --category bacterial --offset 1800 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `TOGO_M1580_NPB_Medium.yaml` through `TOGO_M169_Acidianus_Brierleyi_Medium.yaml`
- Outcome: 42 no-candidate records, 7 records with review-only candidates, and 1 record with manually applied exact-parent evidence. Thioglycolate, R agar, SP medium, R2A, and reinforced clostridial candidates lacked microbial strain/formulation support or represented non-target contexts. `TOGO_M1664_Thermus_Medium.yaml` duplicated the same Thermus literature hit on a gelrite-containing related record and was not separately applied. `TOGO_M1663_Thermus_Medium.yaml` had direct growth-kinetics evidence for *Thermus thermophilus* HB27 in rich Thermus medium at 65 C; the liquid parent record was updated with growth rate, doubling time, and GCA/GCF genome identifiers.
- Command: `just propose-growth --category bacterial --offset 1850 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `TOGO_M1691_Bone_Ash_Medium.yaml` through `TOGO_M1868_Sporulation_Medium.yaml`
- Outcome: 42 no-candidate records and 8 records with review-only candidates. `TOGO_M1704_GS_medium.yaml` matched Optisol GS corneal donor tissue preservation rather than microbial growth-medium evidence. `TOGO_M1721_Potato_Dextrose_Agar.yaml` matched fungal/yeast PDA records outside the bacterial parent target. `TOGO_M172_Medium_10_Broth.yaml` found a plausible enriched Medium 10 broth lead for *Treponema socranskii*, but the abstract does not provide strain identifiers and the source formulation has substantially higher yeast extract and glucose than the local parent, so it remains review-only pending full formulation review. `TOGO_M1762_Thermus_Medium.yaml` and `TOGO_M1860_Thermus_medium.yaml` duplicated the already applied *T. thermophilus* HB27 Thermus-medium evidence under `TOGO_M1663_Thermus_Medium.yaml`. `TOGO_M1868_Sporulation_Medium.yaml` found a real *Bacillus subtilis* chemically defined sporulation-medium doubling-time lead, but that formulation does not match the local complex NBRC/KOMODO sporulation parent. No YAML evidence was applied.
- Command: `just propose-growth --category bacterial --offset 1900 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `TOGO_M1873_Thermotoga_medium.yaml` through `TOGO_M203_Modified_Medium_10.yaml`
- Outcome: 35 no-candidate records and 15 records with review-only candidates. Thermus-medium hits repeated PMID:16233377 and remain represented only on the stronger liquid parent `TOGO_M1663_Thermus_Medium.yaml`. `TOGO_M1948_BG11.yaml` overlapped the existing algae/bacterial BG11 parent evidence and should be handled during BG11 parent reconciliation, not duplicated on this TOGO record. `TOGO_M1_MRS_Medium.yaml` repeated the applied ATCC 7050 / ATCC 10012 MRS evidence under the existing KOMODO MRS parent, while other MRS leads were optimization or non-parent variant contexts without genome IDs. BSK, benzoate, R agar, SL, M98-5, GV, YM agar, and modified Medium 10 candidates lacked strain/formulation support, had empty snippets, or represented diagnostic/fungal/non-target contexts. No YAML evidence was applied.
- Command: `just propose-growth --category bacterial --offset 1950 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `TOGO_M2049_RAE_Medium.yaml` through `TOGO_M226_Picrophilus_Medium.yaml`
- Outcome: 41 no-candidate records and 9 records with review-only candidates. `TOGO_M2228_Friis_medium.yaml` repeated the already applied *Mycoplasma hyopneumoniae* Friis-medium growth-kinetics evidence under the KOMODO Friis parent. BCYE agar, YMA, SC medium, PYG, trypticase soy yeast extract, brain-heart infusion agar, and PPLO broth candidates either lacked strain/formulation support in the cached abstracts, had empty snippets, or represented fungal, diagnostic, stress-response, or non-parent contexts. No YAML evidence was applied.
- Command: `just propose-growth --category bacterial --offset 2000 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `TOGO_M2274_Chocolate_agar.yaml` through `TOGO_M2351_Autotrophic_Nitrobacter_Medium.yaml`
- Outcome: 40 no-candidate records, 9 records with review-only candidates, and 1 record with manually applied exact-parent evidence. Chocolate agar, OS medium, R2A, trypticase soy broth/yeast extract, nutrient agar, and J-agar candidates lacked actionable strain/formulation support or represented diagnostic, stress-response, or non-parent contexts. `TOGO_M2298_Thermus_Medium.yaml` duplicated the already applied *T. thermophilus* HB27 Thermus-medium evidence under `TOGO_M1663_Thermus_Medium.yaml`. `TOGO_M2314_LB_medium.yaml` had direct strain-specific evidence from PMID:16628448 for *Escherichia coli* K-12 MG1655 growth on LB medium; this was added as exact-parent evidence with NCBI taxon, GCA/GCF assembly IDs, and BioSample provenance from NCBI. Pre-existing ingredient-level FOODON/synonym fields in that LB record were normalized into notes so the edited file passes schema validation.
- Command: `just propose-growth --category bacterial --offset 2050 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `TOGO_M2352_CASO_Agar_Merck_105458.yaml` through `TOGO_M2459_Alkaliphilic_Sulphur_Respiring_Strains_Medium.yaml`
- Outcome: 39 no-candidate records and 11 records with review-only candidates. A transient PubMed HTTP 502 occurred, but proposal files were written for all 50 records. `TOGO_M2362_Columbia_Blood_Agar.yaml` duplicated the already applied *Staphylococcus saccharolyticus* Columbia blood agar evidence under the KOMODO Columbia blood agar parent. `TOGO_M2439_MRS_Medium.yaml` duplicated the applied ATCC 7050 / ATCC 10012 MRS evidence under the KOMODO MRS parent. Caulobacter, BHI, BSK, Todd-Hewitt, potato dextrose agar, Leptospira, nutrient agar/broth, and brain-heart infusion agar candidates lacked strain/formulation support, had empty snippets, or represented fungal, diagnostic, stress-response, or non-parent contexts. No YAML evidence was applied.
- Command: `just propose-growth --category bacterial --offset 2100 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `TOGO_M2460_Pyrobaculum_Ferrireducens_Medium.yaml` through `TOGO_M2561_Methanocella_Conradii_Medium.yaml`
- Outcome: 39 no-candidate records, 10 records with review-only candidates, and one manually applied MRS variant/evidence addition on the existing parent `KOMODO_11_MRS_medium.yaml`. `TOGO_M2481_Marine_Broth_2216.yaml`, `TOGO_M2511_brain_heart_infusion_broth.yaml`, `TOGO_M2515_tryptic_soy_broth.yaml`, `TOGO_M2516_tryptic_soy_agar.yaml`, and `TOGO_M2520_R2A_Medium.yaml` lacked actionable strain/formulation support. `TOGO_M2497_LB_medium.yaml`, `TOGO_M2499_BG11.yaml`, and `TOGO_M2545_Columbia_Blood_Agar.yaml` duplicated evidence already represented under stronger LB, BG11, or Columbia blood parent records. `TOGO_M2489_MRS_broth.yaml` and `TOGO_M2494_MRS_broth.yaml` produced direct *Lactiplantibacillus plantarum* BG24 MRS optimization evidence; because that evidence belongs to the existing MRS parent group, it was modeled as the variant `mrs_broth_bg24_ph_yeast_extract_optimization` under `KOMODO_11_MRS_medium.yaml` rather than duplicated on the TOGO MRS broth records.
- Command: `just propose-growth --category bacterial --offset 2150 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `TOGO_M2564_Desulfurococcus_Medium.yaml` through `TOGO_M2664_Archaeoglobus_Medium.yaml`
- Outcome: 47 no-candidate records and 3 records with review-only candidates; no extracted growth metrics or genome assembly IDs, and no YAML evidence was applied. `TOGO_M2567_YPS_medium.yaml` matched *Saccharomyces cerevisiae* PE-2 growth in yeast extract-peptone-sucrose medium, which is a yeast/fungal context and not a supported bacterial parent match. `TOGO_M2592_R2A_Medium.yaml` found broad R2A recovery/cultivation leads without strain-specific formulation evidence or usable snippets. `TOGO_M261_MS_Medium.yaml` candidates were Murashige-Skoog plant/callus culture or Agrobacterium infection-method contexts rather than growth of a named organism on the bacterial MS parent medium.
- Command: `just propose-growth --category bacterial --offset 2200 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `TOGO_M2666_Ferroglobus_Placidus_Medium.yaml` through `TOGO_M2747_Thermoanaerobacter_Kivui_Medium.yaml`
- Outcome: 48 no-candidate records and 2 records with review-only candidates; no extracted growth metrics or genome assembly IDs, and no YAML evidence was applied. `TOGO_M2708_PYE_Medium.yaml` matched *Deinococcus indicus* DR1 and *Entamoeba histolytica* leads, but the proposal had no usable evidence snippets tying strain-specific growth to the local PYE parent formulation. `TOGO_M2726_Clostridium_medium.yaml` matched a *Clostridium sartagoforme* isolation lead without strain, formulation, or metric support sufficient for a parent or variant application.
- Command: `just propose-growth --category bacterial --offset 2250 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `TOGO_M2749_Acetobacterium_medium.yaml` through `TOGO_M294_RC_Medium.yaml`
- Outcome: 31 no-candidate records and 19 records with review-only candidates; no genome assembly IDs were extracted, and no YAML evidence was applied. The batch included two metric-bearing candidates, but neither was safe to apply: the tryptic-soy-agar hit reports late-exponential *Listeria monocytogenes* cells without strain/genome or a supported match to the local agar parent, and the LB hit reports modified M9 growth rather than LB evidence. MRS and LB candidates duplicated relationships already represented under stronger parent records (`KOMODO_11_MRS_medium.yaml` and `TOGO_M2314_LB_medium.yaml`) or lacked strain/formulation support. Other candidate records were broad basal, TPGY, nutrient broth, chocolate agar, BCYE, TY/YPG, modified BHI/MRS, and RC medium leads with weak snippets, non-bacterial contexts, or insufficient parent/variant formulation support.
- Command: `just propose-growth --category bacterial --offset 2300 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `TOGO_M295_Petrotoga_Medium.yaml` through `TOGO_M3141_Chloroflexus_Medium_modified.yaml`
- Outcome: 41 no-candidate records and 9 records with review-only candidates; no extracted growth metrics or genome assembly IDs, and no YAML evidence was applied. Candidate-bearing records were BHI agar, chocolate agar, Mueller-Hinton broth, PPM, corn meal agar, HGAM, nutrient agar, BG11 medium, and alkaline agar. The strongest-looking hits either lacked strain/formulation support, were antimicrobial testing or recovery-method contexts, were non-bacterial/fungal/plant contexts, or duplicated existing BG11 parent evidence that should be handled in a parent-reconciliation pass rather than duplicated on this TOGO record.
- Command: `just propose-growth --category bacterial --offset 2350 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `TOGO_M3142_Chloroflexus_medium.yaml` through `TOGO_M342_SME_Medium.yaml`
- Outcome: 30 no-candidate records and 20 records with review-only candidates; 7 metric-bearing candidates were extracted, but no genome assembly IDs were found and no YAML evidence was applied. Defined/minimal-medium metrics either reported growth in nutrient-rich LB or did not match the generic local parents. The Bacillus chemically defined sporulation-medium hit remains review-only because it does not safely match these defined-medium records as a parent or small variant. Other candidates included LC, 2xYT, LB, nutrient agar, seed/minimal media, 9K, MB, pectin, potato-sucrose agar, glucose-asparagine agar, Marine Broth 2216, and R2A agar leads that were duplicates, broad methods, non-bacterial contexts, or lacked strain/formulation support.
- Command: `just propose-growth --category bacterial --offset 2400 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `TOGO_M344_Ancylobacter-Spirosoma_Medium.yaml` through `TOGO_M395_Desulfovibrio_Magneticus_Medium.yaml`
- Outcome: 49 no-candidate records and 1 record with a review-only candidate; no extracted growth metrics or genome assembly IDs, and no YAML evidence was applied. `TOGO_M366_TH_Agar.yaml` matched a *Streptococcus sanguinis* twitching-motility paper, but the proposal had no usable snippet, strain, genome, or formulation support tying growth to the local TH agar parent.
- Command: `just propose-growth --category bacterial --offset 2450 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `TOGO_M396_Desulfovibrio_Piger_Medium.yaml` through `TOGO_M447_Mjtso_Medium.yaml`
- Outcome: 47 no-candidate records and 3 records with review-only candidates; no extracted growth metrics or genome assembly IDs, and no YAML evidence was applied. `TOGO_M402_YPG_Medium.yaml` matched yeast/fungal YPG contexts, `TOGO_M426_Beer_Medium.yaml` matched yeast fermentation and acetic-acid-bacterium beer-context work without local-parent support, and `TOGO_M428_PY_Medium.yaml` matched protozoa parasite RPMI-PY medium rather than a bacterial PY parent.
- Command: `just propose-growth --category bacterial --offset 2500 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `TOGO_M448_Methanobacterium_Adherens_Medium.yaml` through `TOGO_M498_Modified_Eichler_And_Pfennig_s_Medium.yaml`
- Outcome: 45 no-candidate records and 5 records with review-only candidates; no extracted growth metrics or genome assembly IDs, and no YAML evidence was applied. Candidate-bearing records were `TOGO_M458_B_Medium.yaml`, `TOGO_M460_Fluid_Thioglycollate_Medium.yaml`, `TOGO_M467_Mycobacterium_Medium.yaml`, `TOGO_M46_Potato-Carrot_Agar.yaml`, and `TOGO_M476_Trypticase_Soy_Broth_Agar.yaml`. The hits were cell-culture, fungal/non-bacterial, broad recovery-method, or no-snippet leads without strain-specific formulation support for a parent or variant application.
- Command: `just propose-growth --category bacterial --offset 2550 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `TOGO_M49_Yeast-Krainsky_s_Agar.yaml` through `TOGO_M550_Geosporobacter_Subterreneus_Medium.yaml`
- Outcome: 45 no-candidate records, 4 records with review-only candidates, and 1 record with manually applied variant evidence. `TOGO_M511_NMS_Medium.yaml`, `TOGO_M513_A1_Medium.yaml`, and the paired `TOGO_M530_Thioglycollate_Medium.yaml` / `TOGO_M531_Thioglycollate_Medium.yaml` hits lacked strain/formulation support or were non-microbial cell-culture false positives. `TOGO_M540_Brucella_Broth.yaml` had direct *Helicobacter pylori* Brucella broth growth evidence in PMID:10609610; full-text review resolved the primary strain as OMU89-362 and the BB/FBS/H2O2 condition was modeled as a variant under the Brucella broth parent.
- Command: `just propose-growth --category bacterial --offset 2600 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `TOGO_M551_Desulfovibrio_As36_Medium.yaml` through `TOGO_M5_Nutrient_Broth_With_0.5_NaCl.yaml`
- Outcome: 48 no-candidate records and 2 records with review-only candidates; no extracted growth metrics or genome assembly IDs, and no YAML evidence was applied. `TOGO_M57_Cellulose_Agar.yaml` matched a broad immobilized-microorganism review and a fungal cellulose-agar soil study, while `TOGO_M58_V8_Juice_Agar.yaml` matched oomycete/fungal culture-media papers. These do not support a bacterial parent or variant application.
- Command: `just propose-growth --category bacterial --offset 2650 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `TOGO_M600_Alicycliphilus_Denitrificans_Medium.yaml` through `TOGO_M653_Cellulosilyticum_Ruminicola_Medium.yaml`
- Outcome: 43 no-candidate records and 7 records with review-only candidates; no extracted growth metrics or genome assembly IDs, and no YAML evidence was applied. Glucose agar, mannitol agar, cooked meat medium, reinforced clostridial medium, blood agar, HYL medium, and HM medium candidates were broad medium-name hits, diagnostic or optimization contexts, fungal/oomycete or non-target contexts, or lacked enough formulation support for a parent/variant application. The *E. coli* JM109 HM-medium lead was not applied because the source abstract describes yeast-extract-containing HM medium while the local HM parent is a high-salt solid agar formulation.
- Command: `just propose-growth --category bacterial --offset 2700 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `TOGO_M654_Clostridium_SW_Medium.yaml` through `TOGO_M701_Methanofollis_Ethanolicus_Medium.yaml`
- Outcome: 44 no-candidate records and 6 records with review-only candidates; no extracted growth metrics or genome assembly IDs, and no YAML evidence was applied. Nutrient agar, trypticase soy agar, MBG-20, nutrient broth, distilled water, and YM broth candidates were broad method papers, antimicrobial/diagnostic contexts, non-medium false positives, or lacked unambiguous organism-strain-formulation support. The YM broth bradyrhizobium lead remains review-only because isolate-level doubling times were not unambiguously linked to a species/genome in the abstract.
- Command: `just propose-growth --category bacterial --offset 2750 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `TOGO_M702_FRR_Medium.yaml` through `TOGO_M75_GAM_Semisolid.yaml`
- Outcome: 47 no-candidate records and 3 records with review-only candidates; one metric-bearing candidate was extracted, but no genome assembly IDs were found and no YAML evidence was applied. `TOGO_M729_Lactate_Sulfate_Medium.yaml` and `TOGO_M733_AG_Medium.yaml` lacked strain/formulation support or were non-target contexts. `TOGO_M735_Lowenstein-Jensen_Medium.yaml` repeated the already applied *Mycobacterium* sp. DM-11 nutrient-broth doubling-time paper; the metric is not evidence for growth on the local Lowenstein-Jensen parent.
- Command: `just propose-growth --category bacterial --offset 2800 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `TOGO_M760_MY_Medium.yaml` through `TOGO_M807_MH1_Medium_For_Saliarchaeum_Acidophilum.yaml`
- Outcome: 45 no-candidate records and 5 records with review-only candidates; no extracted growth metrics or genome assembly IDs, and no YAML evidence was applied. `TOGO_M77_25_Glucose_Medium.yaml` matched a fungal glucose-medium paper, `TOGO_M787_Mycoplasma_Medium.yaml` contained plausible Mycoplasma/Spiroplasma review leads without enough local-parent formulation support, `TOGO_M79_1_Ogawa_Medium.yaml` was broad AFB culture-method evidence, `TOGO_M7_EG_Medium.yaml` was a Salmonella acid-tolerance context without a supported EG parent match, and `TOGO_M802_Rumen_Fluid_Medium.yaml` lacked strain/genome-formulation support for a variant.
- Command: `just propose-growth --category bacterial --offset 2850 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `TOGO_M808_Thermoanaeromonas_Medium.yaml` through `TOGO_M855_Methanotroph_1A_Medium.yaml`
- Outcome: 47 no-candidate records and 3 records with review-only candidates; no extracted growth metrics or genome assembly IDs, and no YAML evidence was applied. `TOGO_M80_SM_Medium.yaml` and `TOGO_M841_GS_Medium.yaml` were false-positive or context-mismatched hits. `TOGO_M84_9K_Medium.yaml` produced plausible *Acidithiobacillus ferrooxidans* 9K-medium review leads, but the proposal lacked strain/genome identifiers or a usable formulation-specific evidence snippet.
- Command: `just propose-growth --category bacterial --offset 2900 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `TOGO_M857_Fermentative_Cellulolytic_Anaerobes_Medium.yaml` through `TOGO_M903_Desulfotomaculum_BS_Medium.yaml`
- Outcome: 46 no-candidate records and 4 records with review-only candidates; one metric-bearing candidate was extracted, but no genome assembly IDs were found and no YAML evidence was applied. `TOGO_M875_R2A_Broth.yaml` had a *Sphingopyxis* R2A-broth lead without usable snippet/formulation support and a yeast false positive. `TOGO_M876_YPM_Medium.yaml` mixed broad medium, yeast, and actinobacteria leads without local-parent support. `TOGO_M8_Tomato_Juice_Agar.yaml` was a Candida differentiation/non-bacterial context. `TOGO_M901_ML_Medium.yaml` included a metric-bearing *Pseudomonas* MPDS degradation lead, but the proposal did not establish that the source medium matches the local ML parent.
- Command: `just propose-growth --category bacterial --offset 2950 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `TOGO_M904_Bs_107_Medium.yaml` through `TOGO_M94_Nutrient_Agar_With_25_Soil_Extract.yaml`
- Outcome: 45 no-candidate records and 5 records with review-only candidates; no extracted growth metrics or genome assembly IDs, and no YAML evidence was applied. `TOGO_M908_YP_Medium.yaml` and `TOGO_M909_YP_Medium.yaml` were yeast or broad mixed-context YP-medium hits without usable snippets or strain/formulation support. `TOGO_M926_Phosphate-Buffered_Saline_pH_7.4.yaml` and `TOGO_M949_MK_Medium.yaml` were non-microbial cell/tissue contexts. `TOGO_M937_Modified_BSK_Medium.yaml` was a plausible Borrelia modified-BSK cultivation lead, but the proposal lacked strain/genome identifiers, growth metrics, and formulation detail needed for a parent/variant application.
- Command: `just propose-growth --category bacterial --offset 3000 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `TOGO_M950_MK_Medium.yaml` through `a2_medium.yaml`
- Outcome: 45 no-candidate records and 5 records with review-only candidates; no extracted growth metrics or genome assembly IDs, and no YAML evidence was applied. `TOGO_M950_MK_Medium.yaml` repeated non-microbial McCarey-Kaufman corneal/tissue contexts. `TOGO_M958_Modified_Marine_Agar_2216.yaml` had a possible *Flavobacterium cerinum* species-description lead, but the proposal lacked a usable snippet, genome ID, or formulation-level match. `TOGO_M993_Korthof_s_Medium.yaml` was a leptospire vaccine/culture lead without enough strain/formulation detail for application. `TOGO_M999_Alginate_Medium.yaml` was plant-cell culture, and `a1_medium.yaml` was an OSMAC actinobacteria lead without sufficient strain/genome/formulation support.
- Command: `just propose-growth --category bacterial --offset 3050 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `a3.yaml` through `acidianus_brierleyi_medium.yaml`
- Outcome: 45 no-candidate records and 5 records with review-only candidates; no extracted growth metrics or genome assembly IDs, and no YAML evidence was applied. The `a3.yaml`, `a_medium.yaml`, `aam.yaml`, and `abm.yaml` candidates were dominated by acronym or non-microbial false positives, including cancer, plant, hydrogel, and tissue-scaffold contexts. `a7_medium.yaml` had genital mycoplasma culture-method leads, but the proposal lacked strain/genome identifiers and formulation-level support. The `a_medium.yaml` methanogen unified-medium lead remains review-only because it does not establish that the local `A medium` parent is the source formulation.
- Command: `just propose-growth --category bacterial --offset 3100 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `acidianus_infernus_medium.yaml` through `acm_medium_for_verminephrobacter.yaml`
- Outcome: 49 no-candidate records and 1 review-only candidate on an already evidence-bearing parent; no extracted growth metrics or genome assembly IDs, and no YAML evidence was applied. `acidiphilium_medium.yaml` found a real *Acidiphilium cryptum* DSM 2389 glycerol/PHB production lead from PMID:37847335, but the available proposal and PubMed evidence do not establish that the source formulation is the local DSMZ Medium 269 parent or a small variant; this remains review-only pending full formulation comparison.
- Command: `just propose-growth --category bacterial --offset 3150 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `actinobacteria_medium.yaml` through `alkaline_lb_agar.yaml`
- Outcome: 43 no-candidate records and 7 records with review-only candidates; no extracted growth metrics or genome assembly IDs, and no YAML evidence was applied. `ae_medium.yaml`, `af6.yaml`, `ag_medium.yaml`, `ajs.yaml`, and `alginate_medium.yaml` were acronym or non-microbial false-positive contexts, with one algae AF6 candidate outside the bacterial parent target. `alkalibacterium_olivapovliticus.yaml` was a broad species-description/related-organism lead without strain or formulation support. `alkaline_agar.yaml` had plausible alkaline pectinolytic screening-method context, but lacked strain/genome identifiers and local-parent formulation support.
- Command: `just propose-growth --category bacterial --offset 3200 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `alkaline_malt_extract_agar.yaml` through `aminiphilus_medium.yaml`
- Outcome: 50 no-candidate records; no review candidates, extracted growth metrics, genome assembly IDs, or YAML evidence applications were found.
- Command: `just propose-growth --category bacterial --offset 3250 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `aminithiophilus_medium.yaml` through `anaerocellum_medium.yaml`
- Outcome: 49 no-candidate records and 1 record with a review-only candidate; no extracted growth metrics or genome assembly IDs, and no YAML evidence was applied. `anaerobic_brain_heart_infusion_broth.yaml` matched a cattle rumen fermentation context from PMID:27695807, but the proposal did not identify a specific organism/strain or support a formulation-level match to the local anaerobic BHI parent.
- Command: `just propose-growth --category bacterial --offset 3300 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `anaerocolumna_medium.yaml` through `artficial_marine_water_medium.yaml`
- Outcome: 49 no-candidate records and 1 record with review-only candidates; no extracted growth metrics or genome assembly IDs, and no YAML evidence was applied. `ant.yaml` was a short-name false-positive record: candidates were ant/plant growth, probiotic-assay acronym, and fungus-ant agriculture contexts rather than evidence for the local bacterial medium.
- Command: `just propose-growth --category bacterial --offset 3350 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `arthrobacter_medium.yaml` through `aurantimonas_medium.yaml`
- Outcome: 45 no-candidate records and 5 records with review-only candidates; no extracted growth metrics or genome assembly IDs, and no YAML evidence was applied. `artificial_seawater_medium.yaml` repeated the Hemiaulus-Richelia artificial-seawater evidence already modeled under the algae artificial-seawater parent and had an additional algae cultivation context. `asn_iii.yaml`, `asw.yaml`, and `aswp.yaml` were algae or acronym/clinical false positives. `asp2.yaml` was unrelated receptor/plant transcriptomics context.
- Command: `just propose-growth --category bacterial --offset 3400 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `aureobacterium_terregens_medium.yaml` through `basal_medium_acetaldehyde.yaml`
- Outcome: 46 no-candidate records and 4 records with review-only candidates; one non-microbial metric-bearing candidate was extracted, no genome assembly IDs were found, and no YAML evidence was applied. `b12_medium.yaml` matched a gut-microbiota B12/Macfarlane-medium context without a local-parent match. `b2_medium.yaml` included a plausible *Bordetella pertussis* B2-medium lead from PMID:31013007 but lacked usable metric values, genome IDs, and formulation support; its metric-bearing sheep ovarian-cell candidate was a non-microbial false positive. `b_medium.yaml` was cell-culture/plant-context noise. `basal_medium.yaml` included broad *Clostridium perfringens*, *Nitrobacter winogradskyi*, and *Corynebacterium glutamicum* basal-medium leads, but no strain/genome/formulation support for applying a local parent or variant.
- Command: `just propose-growth --category bacterial --offset 3450 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `basal_medium_benzaldehyde.yaml` through `bhi_glucose_medium.yaml`
- Outcome: 36 no-candidate records and 14 records with review candidates; no extracted growth metrics or genome assembly IDs were found, and no YAML evidence was applied. Manifest coverage increased by 49 records because `bg11.yaml` already had applied BG11 evidence before this batch. Basal/mineral-medium candidates were broad biodegradation, fermentation, plant, or no-abstract leads without strain/genome/formulation support. `bb.yaml` and `bgdm.yaml` were short-name false positives. `bcye_agar.yaml` and `bcye_alpha_agar.yaml` had broad Legionella culture leads without usable strain-specific support. `beer_medium.yaml`, `benzoate_medium.yaml`, `bhi_agar.yaml`, and `bhi_broth.yaml` had plausible cultivation contexts but lacked strain/genome identifiers and local-parent formulation evidence. `bg11_medium.yaml`, `bg_11.yaml`, and `bg11.yaml` overlapped existing BG11 evidence and parent-reconciliation work, so no duplicate variant was applied.
- Command: `just propose-growth --category bacterial --offset 3500 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `bhi_liquid_supplemented_with_haemin_and_nad.yaml` through `bordet_gengou_agar_base.yaml`
- Outcome: 41 no-candidate records and 9 records with review candidates; no extracted growth metrics or genome assembly IDs were found, and no YAML evidence was applied. The `bhis.yaml` P43/6/78T doubling-time hit is already modeled on the specialized `bhis.yaml` parent, so it was not duplicated onto the bacterial duplicate. `bhi_medium.yaml`, `bifidobacterium_medium.yaml`, `bl_medium.yaml`, `blood_agar.yaml`, and `blood_agar_medium.yaml` had plausible organism or strain leads but lacked sufficient local-parent formulation support, genome identifiers, or applied-evidence snippets. `bicarbonate_buffered_medium.yaml`, `bm_medium.yaml`, and `bmm_medium.yaml` were non-microbial, plant, or yeast/fungal expression contexts rather than supported bacterial medium-growth relationships.
- Command: `just propose-growth --category bacterial --offset 3550 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `bordet_gengou_agar_medium.yaml` through `brucella_blood_agar_with_hemin_menadione.yaml`
- Outcome: 44 no-candidate records and 6 records with review candidates; no extracted growth metrics or genome assembly IDs were found, and no YAML evidence was applied. The BHI candidates included *Francisella tularensis*, *Listeria monocytogenes* 10403S, *Burkholderia pseudomallei*, *Bacillus weihenstephanensis* KBAB4, *Staphylococcus aureus*, *Salmonella Typhimurium*, and mixed biofilm/gut-bacteria contexts, but the proposal snippets did not establish strain-specific parent-medium growth with enough formulation support for a variant. `brucella_agar.yaml` found broad anaerobe and *Campylobacter jejuni* cultivation leads, but no strain/genome identifiers or applied-evidence snippet suitable for a local Brucella agar parent or variant.
- Command: `just propose-growth --category bacterial --offset 3600 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `brucella_broth.yaml` through `caloramator_medium.yaml`
- Outcome: 42 no-candidate records and 8 records with review candidates; no extracted growth metrics or genome assembly IDs were found, and no YAML evidence was applied. `brucella_broth.yaml` repeated PMID:10609610 *Helicobacter pylori* Brucella-broth evidence already applied to `data/normalized_yaml/bacterial/TOGO_M540_Brucella_Broth.yaml`, so it was not duplicated on the JCM duplicate parent. `bsk_ii_medium.yaml` and `bsk_medium.yaml` found Borrelia BSK/modified-BSK cultivation leads, but without strain/genome identifiers or enough formulation support for a local variant. `buffered_charcoal_yeast_extract_bcye_agar.yaml` found broad Legionella BCYE leads without strain-specific support. `bs_medium.yaml`, `bsm_medium.yaml`, `bt_medium.yaml`, and `by_medium.yaml` were algae, yeast, plant, or broad optimization contexts rather than supported bacterial medium-growth relationships.
- Command: `just propose-growth --category bacterial --offset 3650 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `caloramator_proteoclasticus_medium.yaml` through `cellulolytic_natronoarchaea_medium.yaml`
- Outcome: 45 no-candidate records and 5 records with review candidates; no extracted growth metrics or genome assembly IDs were found, and no YAML evidence was applied. `camm.yaml` and `cc.yaml` were acronym or non-medium false-positive matches, including cell-culture, COVID/epidemic, and human organoid contexts. `carboxymethyl_cellulose_medium.yaml` had a broad *Pseudomonas* cellulose-medium lead without strain/genome identifiers or usable formulation evidence. `cdm_lp.yaml` matched Leishmania CDM/LP, not a bacterial medium relationship. `cdmm.yaml` included a possible *Clostridioides difficile* CDMM lead, but lacked strain/genome identifiers and local-parent formulation support, plus a non-microbial lung-cancer false positive.
- Command: `just propose-growth --category bacterial --offset 3700 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `cellulomonas_fermentans_medium.yaml` through `chloroflexus_medium_modified.yaml`
- Outcome: 45 no-candidate records and 5 records with review candidates; no extracted growth metrics or genome assembly IDs were found, and no YAML evidence was applied. `cellulose_agar.yaml` had broad cellulose-agar hits, including fungi from soil and an immobilized-microorganism overview, but no bacterial strain/genome support or local JCM J65 formulation match. `cgm.yaml` included an ABE-fermentation *Clostridium acetobutylicum* lead plus non-microbial CGM false positives, but lacked parent-formulation support for applying the local CGM record. `ch.yaml` was dominated by acronym false positives, including clinical and environmental CH/CH4 contexts. `chemically_defined_medium.yaml` matched unrelated defined-media contexts, including Trypanosoma, stem-cell, archaeal, and Bacillus Pafoba-medium papers, but not the local anaerobic chemically defined parent formulation. `chitin_agar.yaml` contained a real rumen chitinolytic *Clostridium* sp. ChK5 chitin-agar lead from PMID:8862026, but the abstract/cache did not establish a DSMZ Medium 1794 formulation match or provide genome identifiers, so it remains review-only.
- Command: `just propose-growth --category bacterial --offset 3750 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `chm.yaml` through `clostridium_chartatabidum_medium.yaml`
- Outcome: 47 no-candidate records and 3 records with review candidates; no extracted growth metrics or genome assembly IDs were found, and no YAML evidence was applied. `chm.yaml` was acronym noise from broiler-feed, cell-culture, and Chinese-herbal-medicine contexts. `chocolate_agar.yaml` included broad productivity and Brucella-cultivation evidence; PMID:37175672 compares conventional chocolate agar with blood-powder variants and reports comparable CFU counts for broad genera including *Neisseria*, *Haemophilus*, *Campylobacter*, *Streptococcus*, *Moraxella*, *Staphylococcus*, *Enterococcus*, *Klebsiella*, and *Pseudomonas*, but it does not provide strain/genome identifiers or a clear match to the local DSMZ 429b parent formulation, so it remains review-only. `clostridial_medium.yaml` included real reinforced-clostridial-medium contexts for *Lactobacillus delbrueckii* ssp. *bulgaricus* and *Clostridium botulinum*, but the papers use RCM/mRCM contexts rather than the local TOGO M2781 parent formulation and lack strain/genome support for applying a variant.
- Command: `just propose-growth --category bacterial --offset 3800 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `clostridium_ck_medium.yaml` through `clostridium_viride_medium.yaml`
- Outcome: 48 no-candidate records and 2 records with review candidates; no extracted growth metrics or genome assembly IDs were found, and no YAML evidence was applied. `clostridium_medium.yaml` matched PMID:34780527, which reports *Clostridium sartagoforme* XN-T4 isolated from rabbit feces using reinforced clostridium medium, but the source does not match the local DSMZ/KOMODO Clostridium medium formulation. `clostridium_thermolacticum_medium_replace_cellobiose_with_sucrose.yaml` matched PMID:16508746 for *Clostridium thermolacticum* continuous culture on lactose, which does not support the local sucrose-replacement medium variant. Both remain review-only.
- Command: `just propose-growth --category bacterial --offset 3850 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `clostridum_g4_medium.yaml` through `corn_and_fish_meal_agar.yaml`
- Outcome: 41 no-candidate records and 9 records with review candidates; no extracted growth metrics or genome assembly IDs were found, and no YAML evidence was applied. `cm_medium.yaml`, `cma.yaml`, and `cmm.yaml` were acronym or non-bacterial false positives. `columbia_agar.yaml`, `columbia_agar_base.yaml`, and `columbia_blood_agar.yaml` included broad Columbia-based agar or blood-agar evidence; PMID:7077295 is already modeled on `data/normalized_yaml/bacterial/KOMODO_429_COLUMBIA_BLOOD_AGAR.yaml`, and the other Columbia candidates lacked strain/genome support or a clear local-parent formulation match. `complete_chemically_defined_medium.yaml` and `complete_medium.yaml` matched unrelated chemically defined, TTU complete, semi-defined, stem-cell, or fungal complete-medium contexts rather than the local parent formulations. `cooked_meat_medium.yaml` included *Clostridium botulinum* and *Clostridium sporogenes* cooked-meat-medium leads, but the sources use improved cooked meat, egg meat replacement, soil extract, or manganese sulfate variants and do not provide strain/genome support for applying the local JCM J605 parent.
- Command: `just propose-growth --category bacterial --offset 3900 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `corn_meal_agar.yaml` through `czapek_solution_agar_a.yaml`
- Outcome: 46 no-candidate records and 4 records with review candidates; no extracted growth metrics or genome assembly IDs were found, and no YAML evidence was applied. `corn_meal_agar.yaml` and `cornmeal_agar.yaml` matched fungal plant-pathology or clinical-fungal contexts, not bacterial growth evidence. `cp_medium.yaml` included diet/acronym noise and a *Streptomyces diastatochromogenes* protoplast-method lead without parent-formulation support. `czapek_dox_agar.yaml` matched fungal *Penicillium rubens* and generic dip-slide cultivation contexts rather than a supported bacterial medium-growth relationship.
- Command: `just propose-growth --category bacterial --offset 3950 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `czapek_solution_agar_b.yaml` through `desulfitobacterium_aromaticivorans_medium.yaml`
- Outcome: 48 no-candidate records and 2 records with review candidates; one extracted growth metric was found, no genome assembly IDs were found, and no YAML evidence was applied. `defined_medium.yaml` included a non-microbial NS0-cell hit, an archaeal *Sulfolobus acidocaldarius* defined-medium hit, and PMID:6148336 for a generic chemically defined *Bacillus subtilis* sporulation medium with about 40 min doubling time, but none matched the local defined-medium parent formulation closely enough to apply. `defined_minimal_medium.yaml` included a real *Gluconobacter oxydans* defined-minimal-medium lead and an *Acinetobacter johnsonii* growth-rate paper, but the extracted doubling-time snippet was for LB and the defined-minimal-medium formulations did not match the local TOGO M3197 parent.
- Command: `just propose-growth --category bacterial --offset 4000 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `desulfitobacterium_dehalogenans_medium.yaml` through `desulfohimalaya_medium.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was dominated by Desulfitobacterium, Desulfobacter, Desulfobacterium, Desulfobulbus, and related sulfate-reducing or dehalogenating media names where the current PubMed query pass did not find direct medium-growth support.
- Command: `just propose-growth --category bacterial --offset 4050 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `desulfoluna_medium.yaml` through `desulfotomaculum_pbe_medium.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch continued the sulfate-reducing/desulfo- prefixed media block, including Desulfoluna, Desulfomicrobium, Desulfonatronum, Desulfonema, Desulfosporosinus, Desulfotalea, Desulfothermus, Desulfotignum, and Desulfotomaculum media names, where the current PubMed query pass did not find direct medium-growth support.
- Command: `just propose-growth --category bacterial --offset 4100 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `desulfotomaculum_sapomandens_medium.yaml` through `desulfurella_ii_medium.yaml`
- Outcome: 49 no-candidate records and 1 review-only candidate; no new genome assembly IDs were found, and no YAML evidence was applied. The single candidate was the existing PMID:10380647 *Desulfovibrio intestinalis* KMS2 doubling-time hit for `desulfovibrio_medium.yaml`, which is already represented in the target YAML and in the supported-evidence table, so it was not duplicated. The remaining Desulfotomaculum, Desulfovectis, Desulfovermiculus, Desulfovibrio-specific variant, Desulfovigra, Desulfovirga, and Desulfurella records had no candidate abstracts in this pass.
- Command: `just propose-growth --category bacterial --offset 4150 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `desulfurella_k_119_medium.yaml` through `dinomm_l_lactatecarbon_highnutrient_novitamin.yaml`
- Outcome: 49 no-candidate records and 1 review-only candidate; no extracted growth metrics or genome assembly IDs were found, and no YAML evidence was applied. The only candidate was `dextran_medium.yaml`, where PMID:35019457 is a DNA-nanotube macromolecular-crowding paper and does not support organism growth on DSMZ Medium 1050. The remaining Desulfurella, Desulfuribacillus, Desulfurispirillum, Desulfurobacterium, Desulfurococcus, Desulfuromonas, Desulfuromusa, Dethiobacter, Dethiosulfovibrio, DG18, Dialister, Diazotrophic, Dictyoglomus, diluted-medium, and DINoMM records had no usable candidate abstracts in this pass.
- Command: `just propose-growth --category bacterial --offset 4200 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `dinomm_nocarbon_highnutrient.yaml` through `e2_medium_with_octanoate.yaml`
- Outcome: 43 no-candidate records and 7 records with review-only candidates; no extracted growth metrics or genome assembly IDs were found, and no YAML evidence was applied. `distilled_water.yaml` had broad *Pseudomonas aeruginosa*, *Streptococcus mutans*, methanogen, and irrigation-water hits without strain/formulation support for the local parent. `dm.yaml` and `e27.yaml` were acronym false positives from animal, plant, cancer, fungal-model, and ecology contexts. `dp_medium.yaml` matched a Microcystis potassium-salt inhibition paper rather than the local bacterial parent. Numeric DSM records (`dsm_14919.yaml`, `dsm_16658.yaml`, and `dsm_24515.yaml`) named plausible type strains, but the cached proposal evidence did not establish growth on the local recipe formulation, so they remain review-only.
- Command: `just propose-growth --category bacterial --offset 4250 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `e31.yaml` through `eubacterium_oxidoreducens_medium.yaml`
- Outcome: 44 no-candidate records and 6 records with review-only candidates; no extracted growth metrics or genome assembly IDs were found, and no YAML evidence was applied. `e31.yaml`, `ea.yaml`, `eg.yaml`, and `eggc.yaml` were dominated by acronym or non-medium false positives from clinical, animal-cell, plant, cancer, fungal-model, and neurobiology contexts. `eg_medium.yaml` found a Salmonella acid-resistance lead but did not establish the local EG parent formulation. `edta_medium.yaml` found an EDTA-degrading bacterium lead, but the cached proposal had no strain/genome identifiers, growth metric, or formulation evidence sufficient to model a variant under DSMZ Medium 463a.
- Command: `just propose-growth --category bacterial --offset 4300 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `ex_lm_medium.yaml` through `fermentation_medium_methanol_nh4cl.yaml`
- Outcome: 45 no-candidate records and 5 records with review-only candidates; no extracted growth metrics or genome assembly IDs were found, and no YAML evidence was applied. `f_10.yaml` and `f_2.yaml` were dominated by cell-culture, fungal, thyroid, plant, or algae contexts; the broad algae f/2 lead remains better handled under algae F/2 parent review and lacks strain/genome support here. `f_2_si.yaml` found diatom/dinoflagellate cultivation contexts rather than bacterial parent evidence. `fastidious_anaerobe_agar.yaml` and `fastidious_anaerobe_broth.yaml` found broad anaerobe method or nutritive-capacity studies without strain/genome identifiers or enough local formulation support to model variants.
- Command: `just propose-growth --category bacterial --offset 4350 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `fermentation_medium_oleic_acid_nh4cl.yaml` through `for_dsm_1085_chemoorganotrophic_growth.yaml`
- Outcome: 47 no-candidate records and 3 records with review-only candidates; no extracted growth metrics or genome assembly IDs were found, and no YAML evidence was applied. `flour_medium.yaml` found a *Bacillus velezensis* endospore-production lead and a fungal wheat-flour cultivation lead, but neither supported the local bacterial parent formulation. `fluid_thioglycolate_medium.yaml` and `fluid_thioglycollate_medium.yaml` found broad diagnostic, transport, or cultivation-method hits without strain/genome identifiers or enough local formulation detail to add organism evidence or variants.
- Command: `just propose-growth --category bacterial --offset 4400 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `for_dsm_11046.yaml` through `for_dsm_14283.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was dominated by DSM-number-specific media or growth-condition records, where the current PubMed query pass did not find direct organism-medium growth support.
- Command: `just propose-growth --category bacterial --offset 4450 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `for_dsm_14290.yaml` through `for_dsm_15841_and_dsm_16925.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch continued the DSM-number-specific media or growth-condition block, with no direct organism-medium support found by the current PubMed query pass.
- Command: `just propose-growth --category bacterial --offset 4500 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `for_dsm_15941.yaml` through `for_dsm_18632.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch continued the DSM-number-specific media or growth-condition block, with no direct organism-medium support found by the current PubMed query pass.
- Command: `just propose-growth --category bacterial --offset 4550 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `for_dsm_18709.yaml` through `for_dsm_21940.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch continued the DSM-number-specific media or growth-condition block, with no direct organism-medium support found by the current PubMed query pass.
- Command: `just propose-growth --category bacterial --offset 4600 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `for_dsm_22050.yaml` through `for_dsm_4661.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch continued the DSM-number-specific media or growth-condition block, with no direct organism-medium support found by the current PubMed query pass.
- Command: `just propose-growth --category bacterial --offset 4650 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `for_dsm_5219.yaml` through `for_growth_on_nitrogen_free_medium.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch completed the current DSM-number-specific block and ended with two non-DSM `for_...` growth-condition records; the current PubMed query pass did not find direct organism-medium support.
- Command: `just propose-growth --category bacterial --offset 4700 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `for_haemophilus_spp.yaml` through `fumarate_medium.yaml`
- Outcome: 45 no-candidate records and 5 records with review-only candidates; no extracted growth metrics or genome assembly IDs were found, and no YAML evidence was applied. `friis_medium.yaml` repeated PMID:20851152 evidence already modeled under the KOMODO Friis parent, so it was not duplicated. `frey_broth.yaml` had a plausible *Mycoplasma synoviae* Frey-broth lead but no cached evidence snippet or formulation support strong enough to apply. `formate_medium.yaml`, `fresh_water_media.yaml`, and `fumarate_medium.yaml` had broad organism or algal/fumarate/formate leads without enough strain, genome, or local parent-medium support.
- Command: `just propose-growth --category bacterial --offset 4750 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `fundibacter_jadensis_medium.yaml` through `geoglobus_medium.yaml`
- Outcome: 47 no-candidate records, 2 new review-only candidate records, and 1 candidate on an already-applied evidence record; no new extracted growth metrics or genome assembly IDs were found, and no YAML evidence was applied. `fw_medium.yaml` was a plant cell-culture false positive. `gam_medium.yaml` had a plausible *Clostridium sporogenes* lead but lacked usable snippet and local-formulation support. `geobacter_sulfurreducens_medium.yaml` found a broad Geobacter protein-nanowire review, while the stronger PMID:35960254 growth evidence is already applied under the same parent.
- Command: `just propose-growth --category bacterial --offset 4800 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `geomonas_saccharovorans_medium.yaml` through `gotz_minimal_medium_with_malate.yaml`
- Outcome: 42 no-candidate records and 8 records with review-only candidates; one extracted growth metric was found, no genome assembly IDs were found, and no YAML evidence was applied. `glucose_yeast_extract_medium.yaml` repeated the *Salinivibrio costicola* DVT glucose/yeast-extract doubling-time lead, but this remains review-only because the cached evidence does not establish an exact local DSMZ parent formulation match. `glucose_agar.yaml` had a *Clostridium thermohydrosulfuricum* doubling-time snippet, but not enough support for the local glucose agar parent. `gluconobacter_oxydans_medium.yaml`, `glucose_asparagine_agar.yaml`, `glucose_nutrient_agar.yaml`, `glucose_peptone_medium.yaml`, `glutamine_medium.yaml`, and `gm17.yaml` were broad glucose-media, fungal/plant, mammalian-cell, or production/induction contexts without strain/genome or local-parent formulation support.
- Command: `just propose-growth --category bacterial --offset 4850 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `gotz_minimal_medium_with_mannitol.yaml` through `halanaerobacter_jeridensis_medium.yaml`
- Outcome: 45 no-candidate records and 5 net review-only candidate records in the manifest; no extracted growth metrics or genome assembly IDs were found, and no YAML evidence was applied. `gpy_medium.yaml`, `gv_medium.yaml`, and `gya.yaml` were fungal or plant-culture contexts rather than supported bacterial growth on the local parents. `graces_insect_medium.yaml` was dominated by insect-cell and Leishmania cultivation contexts, and `gs_medium.yaml` was Optisol GS corneal-preservation noise. The remaining GPY/GYP/GYM/GYS, green-sulfur, growth-factor, Haemophilus, and halanaerobe records had no usable candidate abstracts in this pass.
- Command: `just propose-growth --category bacterial --offset 4900 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `halanaerobaculum_tunisiense_medium.yaml` through `halobacteria_mh4_2_medium.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was dominated by halanaerobe, half-strength medium, haloalkaliphile, haloanaerobe, haloarchaeal, and halobacteria records where the current PubMed query pass did not find direct organism-medium support.
- Command: `just propose-growth --category bacterial --offset 4950 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `halobacteria_starch_medium.yaml` through `halophilic_medium.yaml`
- Outcome: 48 no-candidate records and 2 review-only candidate records; no extracted growth metrics or genome assembly IDs were found, and no YAML evidence was applied. `halomonas_pantelleriense.yaml` matched PMID:11822668, which discusses salinity, temperature, pH, and medium-composition effects on *Halomonas pantelleriense* osmoprotectants and lipids, but the cached abstract does not provide a strain/genome ID or local DSMZ Medium 752 formulation match. `halomonas_subglaciescola.yaml` matched PMID:15459644 for *H. subglaciescola* DH-1 saline-growth physiology, but the cached evidence does not establish the local DSMZ Medium 602 formulation or variant composition. The command encountered one transient PubMed HTTP 429 but completed and wrote all 50 proposal files.
- Command: `just propose-growth --category bacterial --offset 5000 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `halophilic_methanotrophic_bacterium_medium.yaml` through `herbaspirillum_medium.yaml`
- Outcome: 44 no-candidate records and 6 review-only candidate records; no extracted growth metrics or genome assembly IDs were found, and no YAML evidence was applied. `halothermothrix_orenii.yaml` repeated PMID:7520742 evidence already modeled on `KOMODO_761_HALOTHERMOTHRIX_ORENII.yaml`, while a second candidate was non-growth enzyme-use context. `hayflick_medium.yaml` had a *Mycoplasma pneumoniae* comparison lead without strain/genome or local-formulation support. `heart_infusion_agar.yaml`, `heart_infusion_blood_agar.yaml`, and `heart_infusion_broth.yaml` had broad anaerobe, *Francisella*, *Burkholderia*, *Helicobacter*, *Listeria*, and mutans-streptococci leads, but no exact local-parent formulation support. `hepes_medium.yaml` was non-bacterial embryo/cell-culture context.
- Command: `just propose-growth --category bacterial --offset 5050 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `hesp1_medium.yaml` through `hutners_salts_medium_590.yaml`
- Outcome: 47 no-candidate records and 3 review-only candidate records; no extracted growth metrics or genome assembly IDs were found, and no YAML evidence was applied. `hgam.yaml` was orthodontic acronym noise. `hm_medium.yaml` had a recombinant *E. coli* JM109 HM-medium growth-rate lead, but no strain/genome or local formulation support sufficient to apply a variant. `hsm.yaml` returned human organoid and algal *Chlamydomonas* contexts rather than supported bacterial growth. The command encountered two transient PubMed HTTP 500 errors but completed and wrote all 50 proposal files.
- Command: `just propose-growth --category bacterial --offset 5100 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `hydrogen_oxidizing_bacteria_medium.yaml` through `iodide_oxidizing_bacterium_medium.yaml`
- Outcome: 47 no-candidate records and 3 review-only candidate records in the manifest; one extracted growth metric was found, no genome assembly IDs were found, and no YAML evidence was applied. `hyl_medium.yaml` was a clinical *Neisseria gonorrhoeae* solid-medium comparison without local HYL formulation support. `hypertonic_medium.yaml` was non-bacterial cell and virus context. `inorganic_medium.yaml` had broad inorganic-medium leads, including a methane-culture doubling-time snippet and supplemented *Halomonas* and *Clostridium pasteurianum* contexts, but none established the local parent formulation or a supported variant.
- Command: `just propose-growth --category bacterial --offset 5150 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `ip3_3_medium.yaml` through `jcm_medium_no_188.yaml`
- Outcome: 44 no-candidate records and 5 net review-only candidate records in the manifest; one extracted growth metric was found, no genome assembly IDs were found, and no YAML evidence was applied. `isolation_medium.yaml` had broad exoelectrogenic, sponge-associated, and methanogen isolation leads, including a rumen-fluid-supplemented complex-medium doubling-time snippet, but no local formulation support. `isovitalex.yaml` was supplement evidence for chocolate agar or *H. pylori* media rather than a standalone parent. `isp2_medium.yaml`, `isp_2_medium.yaml`, and `isp_medium_4.yaml` had actinomycete/ISP leads but lacked strain/genome and parent-formulation support. `j_agar.yaml` was a *Mycobacterium avium* subsp. *paratuberculosis* medium-optimization lead without enough detail to model the local J agar parent.
- Command: `just propose-growth --category bacterial --offset 5200 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `jcm_medium_no_189.yaml` through `kdm_2_medium.yaml`
- Outcome: 47 no-candidate records and 3 review-only candidate records in the manifest; no extracted growth metrics or genome assembly IDs were found, and no YAML evidence was applied. Most JCM-numbered medium records had no candidates. `jm.yaml` was dominated by acronym, transformation, tumor, and organoid contexts. `k35.yaml` matched *Pediococcus inopinatus* strain K35 and plant-context hits rather than the local K35 medium. `k_medium.yaml` matched M-K preservation medium and plant tissue-culture context. The command encountered several transient PubMed HTTP 429 rate-limit errors but completed and wrote all 50 proposal files.
- Command: `just propose-growth --category bacterial --offset 5250 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `kim_medium.yaml` through `lb_1_tween_80.yaml`
- Outcome: 38 no-candidate records and 11 net review-only candidate records in the manifest; one extracted growth metric was found, no genome assembly IDs were found, and no YAML evidence was applied. `king_b.yaml`, `kings_b_medium.yaml`, `kr_medium.yaml`, `l1.yaml`, and `l_medium.yaml` were acronym, broad, plant/algal, cell-culture, or unrelated contexts. `korthofs_medium.yaml` had Leptospira/Korthof leads but no strain/genome or local formulation support. `l_wenstein_jensen_medium.yaml` included *Mycobacterium* growth leads and the already-used DM-11 doubling-time source, but did not support a new local Lowenstein-Jensen variant. `lactate_sulfate_medium.yaml` had broad *Desulfovibrio* microcalorimetry evidence without strain/genome support. `lactobacilli_mrs_agar.yaml`, `lactobacilli_mrs_broth.yaml`, `lactobacillus_kefiranofaciens.yaml`, and `lb.yaml` were broad MRS/LB or organism-name leads, with stronger LB and MRS evidence already modeled on canonical parent records. The command was heavily rate-limited by PubMed HTTP 429 responses but completed and wrote all 50 proposal files.
- Command: `just propose-growth --category bacterial --offset 5300 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `lb_50_ug_ml_kanamycin_medium.yaml` through `leeming_amp_notman_agar_lna_leeming_amp_notman_1987_in_the_yeasts_a_taxonomic_study_5th_edn.yaml`
- Outcome: 40 no-candidate records and 10 net review-only candidate records in the manifest; one extracted growth metric was found, no genome assembly IDs were found, and no YAML evidence was applied. The LB-family candidates were either duplicate themes already represented by stronger MG1655 evidence on `TOGO_M2314_LB_medium.yaml`, unrelated Leishmania/cell-line contexts, or lacked strain/genome and parent-formulation support. `lbs_medium.yaml`, `lc_2.yaml`, `lc_medium.yaml`, and `lca.yaml` were broad Vibrio, methanotroph, defined-medium, cell-line, or bile-acid contexts that did not support local parent records. The command encountered several transient PubMed HTTP 429 rate-limit errors but completed and wrote all 50 proposal files.
- Command: `just propose-growth --category bacterial --offset 5350 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `leeming_amp_notman_agar_modified_mlna.yaml` through `low_salt_methanotrophic_medium.yaml`
- Outcome: 46 no-candidate records and 4 review-only candidate records in the manifest; no extracted growth metrics or genome assembly IDs were found, and no YAML evidence was applied. `lennox.yaml` was clinical Lennox-Gastaut/cannabidiol noise rather than LB Lennox evidence. `leptospira_medium.yaml` had Leptospira and Bartonella leads without local formulation, strain, or genome support. `lg_medium.yaml` matched protozoan or stem-cell context. `liquid_fermentation_medium.yaml` had broad Streptomyces and fungal fermentation-optimization leads, not a supported local parent formulation. The command encountered transient PubMed HTTP 500 and 429 errors but completed and wrote all 50 proposal files.
- Command: `just propose-growth --category bacterial --offset 5400 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `low_strength_artificial_seawater_medium.yaml` through `m39_methylomonas_medium.yaml`
- Outcome: 41 no-candidate records and 9 review-only candidate records in the manifest; one extracted growth metric was found, no genome assembly IDs were found, and no YAML evidence was applied. `lowenstein_jensen_medium.yaml` and `lowenstein_jenson_medium.yaml` had *Mycobacterium* leads, including the already-used DM-11 doubling-time source, but did not establish a new local parent or variant. `luria_broth.yaml` and `luria_broth_lb.yaml` were broad LB/Luria broth contexts or duplicate themes already represented by stronger LB parent evidence. `m1_medium.yaml`, `m1d_medium.yaml`, `m2_medium.yaml`, `m2gsc_medium.yaml`, and `m30.yaml` were fungal, animal, human-tumor, plant, or broad gut-microbe contexts without local parent support. The command encountered one transient PubMed HTTP 429 rate-limit error but completed and wrote all 50 proposal files.
- Command: `just propose-growth --category bacterial --offset 5450 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `m408_medium.yaml` through `m9_with_0_67_zinc_acetate_park_et_al.yaml`
- Outcome: 46 no-candidate records and 4 review-only candidate records in the manifest; no extracted growth metrics or genome assembly IDs were found, and no YAML evidence was applied. `m63.yaml` had plausible *E. coli* and *Pseudomonas* M63 leads, but lacked genome IDs and local parent-formulation support. `m98_5.yaml` was broad anaerobic fecal-isolation medium context. `m9_medium.yaml` and `m9_minimal_media.yaml` had plausible M9 growth leads, but either duplicated existing specialized M9 evidence, lacked strain/genome support, or needed deeper variant formulation review. The command was heavily rate-limited by PubMed HTTP 429 responses; it completed and wrote all 50 proposal files, but no-candidate outputs from this batch should be treated cautiously.
- Command: `just propose-growth --category bacterial --offset 5500 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `m9_with_0_67_zinc_sulfate_and_05_cysteine_hcl_park_et_al.yaml` through `maize_meal_sardine_agar.yaml`
- Outcome: 42 no-candidate records, 7 review-only candidate records, and 1 candidate on an already-applied evidence record in the manifest; one extracted growth metric was found, no genome assembly IDs were found, and no YAML evidence was applied. `m_05.yaml`, `m_medium.yaml`, `ma2.yaml`, `ma4.yaml`, and `mab_medium.yaml` were plant, animal, fungal, or cell-culture contexts. `ma.yaml` had a plausible *Lactiplantibacillus plantarum* QS7T inulin-medium OD600 lead but did not support the local `ma` parent formulation. `mac.yaml` was dominated by macrophage or Mycobacterium avium complex acronym context. `magnetospirillum_gryphiswaldense_medium.yaml` found a weaker magnetosome-membrane lead, while the stronger PMID:37088211 growth evidence is already applied under the same parent.
- Command: `just propose-growth --category bacterial --offset 5550 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `maleate_liquid_medium.yaml` through `marine_broth_2216_with_pyruvate.yaml`
- Outcome: 45 no-candidate records, 4 review-only candidate records, and 1 candidate on an already-applied evidence record in the manifest; no extracted growth metrics or genome assembly IDs were found, and no YAML evidence was applied. `malt_extract_agar.yaml` was fungal/mushroom context, and `mannitol_agar.yaml` had a broad rhizobial glyphosate lead without local formulation or identifiers. `marine_agar.yaml` and `marine_broth_2216.yaml` had broad marine-isolation or strain leads without enough formulation/genome support. `marine_agar_2216.yaml` repeated PMID:18319453 *Sneathiella glossodoripedis* evidence already applied under `TOGO_M1547_Marine_Agar_2216.yaml`, so it was not duplicated.
- Command: `just propose-growth --category bacterial --offset 5600 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `marine_broth_mb_2216.yaml` through `mbbs_medium_for_hydrogenobacter.yaml`
- Outcome: 46 no-candidate records and 4 review-only candidate records in the manifest; no extracted growth metrics or genome assembly IDs were found, and no YAML evidence was applied. Most marine broth, marine methanogen, marine sulfate reducer, Marinobacter, Marinifilum, Marinitoga, and related records had no candidates in this pass. `marinospirillum_celere.yaml` was a taxonomic comparison lead rather than direct growth on the local parent. `masm.yaml` and `mbbm.yaml` were acronym false positives, and `mb_medium.yaml` matched broad phytoplasma or mycobacterial diagnostic media without local formulation or strain/genome support.
- Command: `just propose-growth --category bacterial --offset 5650 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mbg_20.yaml` through `mediadive_1070_Solution_F.yaml`
- Outcome: 42 no-candidate records and 8 review-only candidate records in the manifest; one extracted growth metric was found, no genome assembly IDs were found, and no YAML evidence was applied. `mbg_20.yaml`, `mc.yaml`, `mc_medium.yaml`, `mcd_medium.yaml`, `mch.yaml`, `mda.yaml`, and `mdm.yaml` were dominated by human/cancer/cell-culture, plant/fungal, or acronym contexts. `mc_ii.yaml` had a broad bioremediation consortium lead without local formulation or strain/genome support. The MediaDive solution records in this batch had no candidates and should remain supporting solution-like records rather than primary growable-media targets.
- Command: `just propose-growth --category bacterial --offset 5700 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_1072_Solution_A.yaml` through `mediadive_1141_Main_sol_514f.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive solution or main-solution records, including trace-element, vitamin, main-solution, and Bacto Marine Broth supporting components; these should remain supporting formulation records rather than primary growable-media targets unless a record is explicitly used as a growth medium.
- Command: `just propose-growth --category bacterial --offset 5750 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_1142_Main_sol_514g.yaml` through `mediadive_1194_Main_sol_540.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution, solution, trace-element, vitamin, or other formulation-component records, except for `mediadive_1185_545_TRYPTONE_SOYA_BROTH_TSB.yaml`, which did not yield direct organism-growth evidence in this pass. These records should continue to be treated as supporting formulation records unless a source explicitly uses the record as a growth medium.
- Command: `just propose-growth --category bacterial --offset 5800 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_1196_Solution_A.yaml` through `mediadive_1244_Main_sol_579.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive solution, main-solution, trace-salt, trace-element, vitamin, or small stock-solution records such as syringate solution, so these should remain supporting formulation records rather than primary growable-media targets unless a source explicitly documents organism growth on the record as a complete medium.
- Command: `just propose-growth --category bacterial --offset 5850 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_1246_Main_sol_581.yaml` through `mediadive_129_Main_sol_78b.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution, solution, vitamin, trace-element, amino-acid, artificial-seawater, Hutner salts, Metals 44, phosphate, haemin, or Vitamin K1 stock records, so these should remain supporting formulation records rather than primary growable-media targets unless a source explicitly documents organism growth on the record as a complete medium.
- Command: `just propose-growth --category bacterial --offset 5900 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_12_Main_sol_11.yaml` through `mediadive_1356_Main_sol_635.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution, solution, trace-element, vitamin, mineral salt, phosphate buffer, synthetic seawater, and related supporting stock records, so these should remain supporting formulation records rather than primary growable-media targets unless a source explicitly documents organism growth on the record as a complete medium.
- Command: `just propose-growth --category bacterial --offset 5950 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_1357_Main_sol_636.yaml` through `mediadive_1405_Solution_A.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was mostly MediaDive main-solution, solution, trace-element, and vitamin stock records, with `mediadive_1370_Bacto_Middlebrook_7H10_agar.yaml` and `mediadive_1371_Bacto_Middlebrook_OADC_enrichment.yaml` also returning no direct supported growth evidence in this pass. The command encountered one transient PubMed HTTP 429 rate-limit warning but completed and wrote all 50 proposal files.
- Command: `just propose-growth --category bacterial --offset 6000 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_1406_Solution_B.yaml` through `mediadive_1467_Main_sol_716.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was almost entirely MediaDive solution, main-solution, vitamin, trace-element, and supporting formulation records, with `mediadive_1435_Columbia_Blood_Agar_Base.yaml` also returning no direct supported growth evidence in this pass.
- Command: `just propose-growth --category bacterial --offset 6050 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_1468_Main_sol_717.yaml` through `mediadive_1521_Main_sol_743.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution, solution, trace-element, chelated iron, and supporting formulation records. The command encountered one transient PubMed HTTP 429 rate-limit warning but completed and wrote all 50 proposal files.
- Command: `just propose-growth --category bacterial --offset 6100 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_1522_Main_sol_744.yaml` through `mediadive_1581_Main_sol_778.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution, solution, trace-element, chelated iron, inorganic salt, stock, vitamin, and artificial sea-water supporting records.
- Command: `just propose-growth --category bacterial --offset 6150 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_1582_Main_sol_778a.yaml` through `mediadive_1632_Main_sol_802.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution, solution, vitamin, mineral, trace-element, artificial sea-water, haemin, Vitamin K1, and related supporting stock records.
- Command: `just propose-growth --category bacterial --offset 6200 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_1633_Trace_metals_solution.yaml` through `mediadive_1682_Main_sol_829b.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive trace-metal, solution, main-solution, ferric EDTA, concentrated seawater, growth-stimulating-factor, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 6250 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_1683_Main_sol_829c.yaml` through `mediadive_1738_Main_sol_850.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution, trace-element, solution, vitamin, artificial-seawater, sulfide, selenite-tungstate, phosphate, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 6300 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_1739_Main_sol_851.yaml` through `mediadive_1811_Solution_C.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution, salt-solution, enrichment, solution, trace-element, basal-salt, cysteine, seawater, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 6350 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_1813_Solution_E.yaml` through `mediadive_1867_Solution_E_Vitamins.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive solution, main-solution, trace-element, vitamin, and related supporting stock records.
- Command: `just propose-growth --category bacterial --offset 6400 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_1869_Solution_A.yaml` through `mediadive_192_Solution_A.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive solution, main-solution, trace-element, phosphate-buffer, ferrous-chloride, volatile-fatty-acid, vitamin, selenite-tungstate, meat-filtrate, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 6450 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_1931_Solution_A.yaml` through `mediadive_1988_Main_sol_964.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive solution, main-solution, trace-element, selenite-tungstate-molybdate, vitamin, sea-water-salts, synthetic-seawater, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 6500 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_1989_Main_sol_965.yaml` through `mediadive_2036_Trace_element_solution_SL12.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution, solution, trace-element, vitamin, synthetic-seawater, mineral, FeSO4, MnCl2, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 6550 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_2037_Main_sol_999.yaml` through `mediadive_208_Sludge_fluid.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution, trace-mineral, mineral-mixture, concentrated solution, trace-element, PYE, sludge-fluid, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 6600 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_2091_Main_sol_1031.yaml` through `mediadive_2141_Main_sol_1058c.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution, solution, trace-element, fatty-acid-mixture, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 6650 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_2143_Main_sol_1058d.yaml` through `mediadive_2198_Main_sol_1091.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution, solution, trace-element, vitamin, artificial-seawater, Hank's BSS, sterile supplement, arginine solution, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 6700 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_2199_Main_sol_1092.yaml` through `mediadive_2250_Trace_element_solution_SL8.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution, solution, trace-element, sodium-thiosulfate, Dialister medium, Vitamin K1, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 6750 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_2251_Main_sol_1120.yaml` through `mediadive_2306_Trace_element_solution_mg_per_200_ml.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution, trace-mineral, micronutrient, phosphate-buffer, potato-infusion, salt-solution, Hutner basal salts, MS buffer, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 6800 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_2307_Main_sol_1149.yaml` through `mediadive_2361_Main_sol_1183.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution, trace-element, vitamin, micronutrient, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 6850 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_2362_Vitamin_solution.yaml` through `mediadive_2410_Main_sol_1210.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive vitamin, trace-element, main-solution, salt-base, heterotrophic basal salts, phosphate, redox mix, electron acceptor, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 6900 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_2411_Amorphous_Fe_OH_3.yaml` through `mediadive_246_Main_sol_142.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive amorphous iron, main-solution, modified Wolin mineral/vitamin, trace-element, artificial-seawater, mineral-solution, and related supporting formulation records. The command encountered two transient PubMed HTTP 429 rate-limit warnings but completed and wrote all 50 proposal files.
- Command: `just propose-growth --category bacterial --offset 6950 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_2474_Main_sol_1245.yaml` through `mediadive_2547_Solution_B.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution, hemin, cysteine, trace-element, liquid/solid media component records, salt and vitamin solutions, ferrous sulfide sludge, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 7000 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_2548_Solution_C.yaml` through `mediadive_2602_Main_sol_1302.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive solution, vitamin, trace-element, salt-solution, and main-solution supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 7050 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_2604_Solution_A.yaml` through `mediadive_2668_220_CASO_AGAR_Merck_105458_-_without_Agar.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive solution, main-solution, artificial-seawater, cultivation, freshwater, phosphate, acetate, selenite-tungstate, trace-element, FeEDTA, Metals 44, Columbia Blood Agar Base, CASO Agar component, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 7100 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_2669_Main_sol_1332.yaml` through `mediadive_272_Main_sol_157.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution, trace-element, vitamin, Wolfe mineral, carbonate salts, salt-water stock, MIN_E base, phosphate buffer, Zeikus trace elements, sulfide, bicarbonate, mineral salts, artificial-seawater, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 7150 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_2731_Mineral_Salts_Solution.yaml` through `mediadive_2801_Main_sol_1381.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive mineral-salts, main-solution, trace-element, vitamin, phosphate-buffer, micronutrient, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 7200 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_2802_Main_sol_1382.yaml` through `mediadive_2868_Trace_Element_Solution.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution, selenite-tungstate, mineral-salts, trace-element, vitamin, total salts, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 7250 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_286_Main_sol_166.yaml` through `mediadive_2936_Vitamin_B12_solution_0_001_g_L.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution, mineral-salts, trace-element, vitamin, modified Hutner basal salts, Metals 44, sulfide, SSE concentrate, mineral salt solution, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 7300 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_2937_Main_sol_1435.yaml` through `mediadive_3008_Main_sol_1465.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution, solution, vitamin, artificial-seawater, mineral-salts, trace-element, bicarbonate, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 7350 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_300_Solution_E.yaml` through `mediadive_3066_Solution_B.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive solution, main-solution, Nitsch element solution, trace-element, resazurin, vitamin mix, mineral solution, FeEDTA, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 7400 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_3067_Solution_C.yaml` through `mediadive_311_Main_sol_185.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive solution, supplement, trace-element, vitamin, mineral salts, basal salts, phosphate, Trypticase Soy Broth with yeast extract, PYG, sucrose-phosphate-glutamate buffer, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 7450 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_3121_Main_sol_1511.yaml` through `mediadive_3187_Main_sol_1538.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution, solution, trace-element, sodium chloride, selenite-tungstate, vitamin, chelated iron, marine salts, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 7500 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_3189_Vitamin_solution.yaml` through `mediadive_3256_Phosphate_buffer.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive vitamin, main-solution, solution, Pfennig heterotrophic salts, artificial-seawater, mineral salts, Metals 44, trace-element, and phosphate-buffer supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 7550 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_3257_Main_sol_1571.yaml` through `mediadive_3333_Phosphate_buffer.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution, trace-element, cresol red, vitamin B12, NMS salts, phosphate buffer, and related solution/supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 7600 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_3335_Main_sol_1599.yaml` through `mediadive_3399_Main_sol_1636.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution, trace-mineral, vitamin, volatile fatty acid, salt, HEPES buffer, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 7650 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_33_Trace_element_solution_SL-12_B.yaml` through `mediadive_3464_Main_sol_1669.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive trace-element, main-solution, selenium/tungsten, acetate, bicarbonate, vitamin, phosphate buffer, basal stock, cellobiose, CM mix, Vitamin K1, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 7700 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_3465_Main_sol_1670.yaml` through `mediadive_3536_Trace_element_solution.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution, trace-element, salt water, MGM, vitamin, borate-copper, neutralized sulfide, artificial seawater, Wolfe mineral, iron citrate, trace metal, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 7750 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_3537_Vitamin_solution.yaml` through `mediadive_3602_Solution_B.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive vitamin, main-solution, solution, bicarbonate, ascorbate, benzoate, synthetic seawater, trace-element, NaHCO3, Vitamin B12, Wolfe mineral, and iron citrate supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 7800 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_3603_Solution_D_Alkaline_Trace_Elements_Solution.yaml` through `mediadive_3658_Main_sol_J35.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive alkaline trace elements, main-solution J-series records, mineral salts, sucrose, trace-element, and related solution/supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 7850 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_3659_Main_sol_J37.yaml` through `mediadive_3707_Main_sol_J80.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution J-series records, trace salts, Fe2 solution, and related solution/supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 7900 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_3708_Main_sol_J81.yaml` through `mediadive_3762_Solution_B.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution J-series records, trace-metal solution, solution pairs, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 7950 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_3763_Main_sol_J123.yaml` through `mediadive_3810_Main_sol_J157.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution J-series records, trace-element, VFA, salt, standard mineral base, Hutner vitamin-free mineral base, Metals 44, salt-base, trace-mineral, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 8000 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_3811_Main_sol_J158.yaml` through `mediadive_3867_Main_sol_J202.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution J-series records, modified Brock salt base, trace-element, vitamin, FeCl2, trace vitamins, trace minerals, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 8050 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_3868_Main_sol_J203.yaml` through `mediadive_3924_Trace_element_solution.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution J-series records, marine medium synthetic seawater mix, marine trace elements, Wolfe mineral, reducing solution, Czapek concentrate, general salts, trace minerals, vitamin B, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 8100 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_3925_Main_sol_J244.yaml` through `mediadive_3982_Main_sol_J285.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution J-series records, synthetic seawater, Ni-Se-W, artificial seawater, Wolfe mineral, fatty acid mixture, Castenholz basal salt, Nitsch trace elements, trace vitamins, trace-element, Se/W, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 8150 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_3984_Main_sol_J287.yaml` through `mediadive_4035_Main_sol_J318.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution J-series records, maltose-hemin, hemin, trace-metal, vitamin, FeCl3, growth-stimulating factors, basal salts, phosphate, mineral salt, artificial seawater, trace elements, Se/W, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 8200 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_4036_Main_sol_J319.yaml` through `mediadive_4094_Main_sol_J371.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution J-series records, trace-mineral, trace-element SL-4, vitamin VA, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 8250 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_4095_Main_sol_J372.yaml` through `mediadive_4158_Main_sol_J423.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution J-series records, seawater, trace-element, trace-metal, Fe(III)-quinate, vitamin, thiamine, Vitamin B12, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 8300 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_4161_Main_sol_J425.yaml` through `mediadive_4215_Main_sol_J467.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution J-series records, acetate, APM salts, basal medium, trace-element, selenite-tungstate, vitamin, trace-mineral, and riboflavin solution supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 8350 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_4216_Main_sol_J468.yaml` through `mediadive_4280_Main_sol_J505.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution J-series records, Wolfe mineral elixir, microelement, vitamin, trace-mineral, modified MJ synthetic seawater, trace-element SL-12, and related solution/supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 8400 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_4281_Main_sol_J506.yaml` through `mediadive_4335_Basal_solution.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution J-series records, trace elements, FeCl3, phosphate, DL minerals/vitamins, APM salts, sulfide, galactose, vitamin, mineral medium, reducing agent, FeSO4, micronutrient, basal solution, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 8450 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_4336_SL-7_trace_element_solution.yaml` through `mediadive_439_Main_sol_206.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive trace-element, vitamin, cofactor, solution, main-solution J-series records, SL10 elements, Se/W, Mg/Ca, benzoate, FeSO4/EDTA, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 8500 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_43_Solution_F.yaml` through `mediadive_4459_Solution_C.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive solution, main-solution J-series records, MDS salt water, phosphate buffer, vitamin, substrate, trace metal, salts, starch, synthetic seawater, thioglycolate-ascorbate, acid/alkaline trace-element, and related supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 8550 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_4460_Vitamin_solution.yaml` through `mediadive_451_Solution_F.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive vitamin, main-solution J-series records, metal, phosphate, trace-element, artificial seawater, ferric quinate, mineral/fatty-acid mixtures, and related solution/supporting formulation records.
- Command: `just propose-growth --category bacterial --offset 8600 --limit 50 --retmax 1 --apply --write-empty`
- Reviewed records: next 50 sorted bacterial records, from `mediadive_4521_Main_sol_J641.yaml` through `mediadive_4571_Fatty_acid_mixture.yaml`
- Outcome: 50 no-candidate records; no candidate abstracts, extracted growth metrics, or genome assembly IDs were found, and no YAML evidence was applied. This batch was entirely MediaDive main-solution J-series records, trace-element, artificial seawater, vitamin, ferric quinate, sulfur solutions, mineral solution, and fatty-acid mixture supporting formulation records.

## Supported Growth Evidence Found Locally

The table below summarizes supported growth evidence found in local YAML records and proposal files. Some entries have already been applied to `target_organisms[].growth_metrics`; others remain proposal candidates for curator review. These records do not by themselves prove full corpus completion.

| Parent medium record | Organism / strain | Identifier | Growth evidence | Status | Medium / variant assessment | Source |
|---|---|---:|---|---|---|---|
| `data/normalized_yaml/bacterial/TOGO_M1308_Methylotroph_Medium.yaml` | *Methylosinus* sp. Ce-a6; JCM 32771 | `NCBITaxon:2172005`; `GCA_009811655`; `GCF_009811655` | Positive methanol-culture growth in Ca-free basal medium with lanthanides | Applied | Variant already present: `ca_free_lanthanide_test_basal_medium` | DOI:10.1264/jsme2.ME19128 |
| `data/normalized_yaml/bacterial/TOGO_M1308_Methylotroph_Medium.yaml` | *Methylovorus mays* | `NCBITaxon:184077` | Doubling time 2 h; optimum 35-40 C and pH 7.0-7.5 | Applied | Likely parent match if TOGO methylotroph formulation matches source; formulation still needs comparison | PMID:11315676 |
| `data/normalized_yaml/bacterial/desulfovibrio_medium.yaml` | *Desulfovibrio intestinalis* strain KMS2 | `NCBITaxon:58621` | Fastest reported doubling time 12.5 h at 37 C | Applied | Likely parent match for Desulfovibrio medium; strain-specific record can be added | PMID:10380647 |
| `data/normalized_yaml/bacterial/acidiphilium_medium.yaml` | *Acidiphilium cryptum* | `NCBITaxon:524` | Growth in glucose-mineral medium at pH 3; 7.6 h doubling with aluminum, 5.2 h without aluminum | Applied | Variant added: `aluminum_sulfate_stress_acidiphilium_cryptum` | PMID:12420179 |
| `data/normalized_yaml/bacterial/bg11.yaml` | *Synechocystis* sp. PCC 6803 | `NCBITaxon:1148` | Growth rate 0.16 h-1; 4.3 h doubling time under optimized BG11 conditions | Applied | Variant added: `optimized_bg11_synechocystis_pcc6803` | PMID:29577667 |
| `data/normalized_yaml/bacterial/bg11.yaml` | *Synechococcus elongatus* PCC 11801 | `NCBITaxon:2219813` | Doubling time 2.3 h under ambient CO2 conditions | Applied | Variant added: `ambient_co2_bg11_synechococcus_pcc11801` | PMID:30413737 |
| `data/normalized_yaml/bacterial/bg11.yaml` | *Synechococcus elongatus* PCC 11802 | `NCBITaxon:2283154` | Doubling time 2.8 h at 1% CO2 and high light | Applied | Variant added: `high_co2_high_light_bg11_synechococcus_pcc11802` | PMID:31932622 |
| `data/normalized_yaml/bacterial/geobacter_sulfurreducens_medium.yaml` | *Geobacter sulfurreducens* | `NCBITaxon:35554` | Doubling time 5 h with acetate donor and fumarate acceptor | Applied | Variant added: `acetate_fumarate_geobacter_sulfurreducens_growth` | PMID:35960254 |
| `data/normalized_yaml/bacterial/KOMODO_1078_FRIIS_medium.yaml` | *Mycoplasma hyopneumoniae* isolates F1.12A, F5.6A, F6.12D, F7.2C, F12.6A, 13.7B, and Mp143 | `NCBITaxon:2099` | Modified Friis medium supported growth-curve measurement; doubling times ranged from 4.8 to 7.8 h in slowly shaken cultures | Applied | Variant added: `friis_medium_mycoplasma_hyopneumoniae_isolate_growth`; parent record has pre-existing ingredient schema issues | PMID:20851152 |
| `data/normalized_yaml/bacterial/KOMODO_11_MRS_medium.yaml` | *Heyndrickxia coagulans* ATCC 7050 / DSM 1; *Lactiplantibacillus plantarum* ATCC 10012 / DSM 20246 | `NCBITaxon:1121088`; `GCA_000832905.1`; `GCF_000832905.1`; `NCBITaxon:337330` | MRS medium supported strain-specific fermentation/growth-kinetics work; minimum doubling times were 79.8 min for *H. coagulans* ATCC 7050 under anaerobic conditions and 85.5 min for *L. plantarum* ATCC 10012 under microaerophilic conditions | Applied | Variant added: `mrs_bsh_oxygen_condition_atcc7050_atcc10012`; no NCBI GCA/GCF found for ATCC 10012 in this pass | PMID:39353547; DOI:10.1016/j.mimet.2024.107050 |
| `data/normalized_yaml/bacterial/KOMODO_11_MRS_medium.yaml` | *Lactiplantibacillus plantarum* BG24 | `NCBITaxon:337330` | Static MRS broth reached OD600 6.60; original MRS broth pH 5.7 had growth rate 0.416 h-1 and doubling time 1.67 h, while MRS broth pH 6.5 enriched with 5 g/L yeast extract had growth rate 0.483 h-1 and doubling time 1.43 h | Applied | Variant added: `mrs_broth_bg24_ph_yeast_extract_optimization`; no genome assembly/BioSample ID resolved in this pass | PMID:38194015 |
| `data/normalized_yaml/bacterial/KOMODO_429_COLUMBIA_BLOOD_AGAR.yaml` | *Staphylococcus saccharolyticus* ATCC 14953 / DSM 20359 / JCM 1768 / NCTC 11807 / VPI 5661 / S1, formerly *Peptococcus saccharolyticus* | `NCBITaxon:33028`; `GCA_003968885.1`; `SAMN05977977` | Columbia blood agar supported anaerobic qualitative growth/count evidence; BacDive lists positive growth on Columbia Blood Medium at 37 C for the type strain | Applied | Variant added: `columbia_blood_agar_staphylococcus_saccharolyticus_anaerobic`; parent record has pre-existing ingredient schema issues and a blood-source/concentration difference relative to DSMZ Medium 693 | PMID:7077295; BacDive:14567 |
| `data/normalized_yaml/bacterial/KOMODO_761_HALOTHERMOTHRIX_ORENII.yaml` | *Halothermothrix orenii* H168 / DSM 9562 / OCM 544 | `NCBITaxon:373903`; `GCA_000020485.1`; `SAMN00623047` | Strain H168 was isolated/grown at 60 C in medium containing 100 g/L NaCl; optimum growth occurred across 50-100 g/L NaCl | Applied | Variant added: `strict_anaerobic_halothermothrix_orenii_h168_growth`; parent high-salt formulation is a close match with about 101 g/L NaCl | PMID:7520742; NCBI BioProject PRJNA16377 |
| `data/normalized_yaml/bacterial/TOGO_M1547_Marine_Agar_2216.yaml` | *Sneathiella glossodoripedis* MKT133T / IAM 15419T / KCTC 12842T / JCM 23214T | `NCBITaxon:1236958`; `GCA_000616095`; `GCF_000616095.1` | Colony formation on Marine Agar 2216 after 4-5 days at 30 C; colonies less than 1 mm diameter | Applied | Exact parent medium match; no formulation variant needed | PMID:18319453; NCBI:GCF_000616095.1; BacDive:134304 |
| `data/normalized_yaml/bacterial/TOGO_M1663_Thermus_Medium.yaml` | *Thermus thermophilus* HB27 | `NCBITaxon:262724`; `GCA_000008125.1`; `GCF_000008125.1` | Growth in rich Thermus medium at 65 C in 3 L batch fermentors; maximum growth rate 0.27 h-1, doubling time 2.67 h, and dry cell weight 3 g/L | Applied | Exact liquid parent medium match; culture-operation differences captured in measurement conditions rather than a new variant | PMID:16233377; NCBI:GCF_000008125.1 |
| `data/normalized_yaml/bacterial/TOGO_M2314_LB_medium.yaml` | *Escherichia coli* K-12 MG1655 | `NCBITaxon:511145`; `GCA_000005845.2`; `GCF_000005845.2`; `SAMN02604091` | Growth of *E. coli* MG1655 on LB medium; source monitored nutrient utilization during the culture growth-rate phase | Applied | Exact LB Miller liquid parent match; no formulation variant needed | PMID:16628448; NCBI:GCF_000005845.2 |
| `data/normalized_yaml/bacterial/TOGO_M540_Brucella_Broth.yaml` | *Helicobacter pylori* OMU89-362 | `NCBITaxon:210` | Brucella broth supplemented with 10% fetal bovine serum supported *H. pylori* growth; H2O2 detoxification of bisulfite-containing Brucella broth enhanced growth, with full text reporting OD620 0.724 in the BLBB/FBS comparison condition | Applied | Variant added: `brucella_broth_fbs_h2o2_helicobacter_pylori`; no genome assembly/BioSample ID resolved in this pass | PMID:10609610 |
| `data/normalized_yaml/bacterial/nutrient_broth.yaml` | *Mycolicibacterium cosmeticum* strain DM-11 | `NCBITaxon:258533` | Optimal growth at 25 C; doubling time 29.2 h | Applied | Variant added: `nutrient_broth_mycolicibacterium_cosmeticum_dm11_25c`; genome ID still needed | PMID:16461697 |
| `data/normalized_yaml/specialized/m9.yaml` | *Escherichia coli* | `NCBITaxon:562` | Modified M9 supported high-density growth to OD600 up to 10 | Applied | Variant added: `modified_m9_high_density_e_coli_expression` | PMID:27709314 |
| `data/normalized_yaml/specialized/bhis.yaml` | *Brachyspira pilosicoli* strain P43/6/78T / ATCC 51139 | `NCBITaxon:1042417`; `GCA_000325665.1`; `GCF_000325665.1` | BHIS broth supported 1 to 2 h doubling time and maximum cell density of 2 x 10(9) cells per ml at 37 to 42 C | Applied | Variant added: `bhis_brachyspira_pilosicoli_p43_growth` | PMID:8573497; genome support PMID:23469345 |
| `data/normalized_yaml/bacterial/methanosarcina_medium.yaml` | *Methanosarcina acetivorans* | `NCBITaxon:2214` | Slow-growth phase doubling time 49 h; fast growth also noted at 6 h | Applied | Variant added: `slow_growth_phase_methanosarcina_acetivorans` | PMID:21097629 |
| `data/normalized_yaml/bacterial/caulobacter_medium.yaml` | *Caulobacter* sp. K31 | `NCBITaxon:366602` | Growth at 4 C with 40 h doubling time | Applied | Variant added: `cold_growth_caulobacter_k31` | PMID:25274120 |
| `data/normalized_yaml/bacterial/magnetospirillum_gryphiswaldense_medium.yaml` | *Magnetospirillum gryphiswaldense* MSR-1 / B17316 | `NCBITaxon:55518` | Magnetosome-deficient B17316 had growth rate 0.062 h-1 with Cr(VI) | Applied | Variant added: `crvi_stress_magnetosome_deficient_b17316` | PMID:37088211 |
| `data/normalized_yaml/bacterial/pyrococcus_medium.yaml` | *Pyrococcus furiosus* | `NCBITaxon:2261` | Serial adaptation enabled growth on CF11 cellulose; 64 min doubling | Applied | Variant added: `cf11_cellulose_adapted_pyrococcus_furiosus` | PMID:21421788 |
| `data/normalized_yaml/bacterial/rhodobacter_sphaeroides_medium.yaml` | *Rhodobacter sphaeroides* OU5 | `NCBITaxon:1063` | Phototrophic growth on L-phenylalanine as sole nitrogen source; 18 h doubling | Applied | Variant added: `phototrophic_l_phenylalanine_sole_nitrogen_ou5` | PMID:19826864 |
| `data/normalized_yaml/algae/Artificial_Seawater_Medium.yaml` | *Hemiaulus hauckii* with *Richelia intracellularis* symbiont | `NCBITaxon:426650`; `NCBITaxon:98443` | Successful isolation/growth in modified artificial seawater medium; maximum growth rates 0.74-0.93 div d-1 in N-free medium with N2 as sole N source | Applied | Variant added: `modified_artificial_seawater_hemiaulus_richelia_symbiosis` | PMID:33083143 |
| `data/normalized_yaml/algae/Artificial_Seawater_Medium.yaml` | *Synechocystis* sp. PCC 6803 | `NCBITaxon:1148` | Wild-type strain grew well in artificial seawater medium supplemented with nitrogen and phosphorus; HEPES improved growth overall | Applied | Variant added: `np_supplemented_asw_synechocystis_pcc6803` | PMID:25954257 |
| `data/normalized_yaml/algae/Bristol_Medium.yaml` | *Chlorella pyrenoidosa* | `NCBITaxon:3077` | Qualitative growth in commercial Bristol medium as comparator; algal production comparable to or higher than Bristol medium in wastewater treatments | Applied | Parent medium match; no variant needed | PMID:15092268 |
| `data/normalized_yaml/algae/F_2_Medium.yaml` | *Tetraselmis marina* | `NCBITaxon:41888` | Cells were grown in F/2-medium for seven days; nitrogen-replete second stage reached 1900 mg/L biomass | Applied | Parent medium match for first stage; variant added: `n_replete_second_stage_tetraselmis_marina` | PMID:28456040 |
| `data/normalized_yaml/algae/Spirulina_Medium.yaml` | *Arthrospira platensis* | `NCBITaxon:118562` | Conventional Spirulina medium supported biomass production to late exponential phase in comparison with biogas effluent medium | Applied | Parent medium evidence plus variant added: `biogas_effluent_based_arthrospira_platensis` | PMID:28025700 |
| `data/normalized_yaml/algae/TAP_Medium.yaml` | *Chlorella vulgaris* | `NCBITaxon:3077` | TAP medium used for Chlorella vulgaris growth in Delftia co-culture interaction experiment | Applied | Variant added: `tap_delftia_chlorella_vulgaris_coculture` | PMID:39168352 |
| `data/normalized_yaml/algae/TAP_Medium.yaml` | *Chlorella sorokiniana* | `NCBITaxon:3076` | TAP used as comparator for fed-batch and semicontinuous cultures; TAP-derived Ab-WSF variant reached 4.5 g/L biomass | Applied | Variant added: `ab_wsf_tap_derived_chlorella_sorokiniana` | PMID:40484141 |
| `data/normalized_yaml/algae/bg11.yaml` | *Nostoc linckia* | `NCBITaxon:92942` | BG11 produced higher biomass than BG110 after 240 h: 1.65 +/- 0.06 g L-1 dry weight versus 0.92 +/- 0.01 g L-1 | Applied | Variant added: `nitrate_replete_bg11_nostoc_linckia` | PMID:36550226 |
| `data/normalized_yaml/algae/bg11.yaml` | *Synechococcus* sp. UCP002 | `NCBITaxon:2885151` | Cultured in BG-11; specific growth rate 0.086 +/- 0.008 h-1 and doubling time 8.08 +/- 0.78 h. Complete genome reported, but no GCA/GCF/SAMN accession resolved from NCBI assembly/nuccore search. | Applied | Variant added: `bg11_synechococcus_ucp002` | PMID:36437912 |
| `data/normalized_yaml/algae/bg11.yaml` | *Tetradesmus obliquus* strain ABC-009, reported as *Scenedesmus obliquus* ABC-009 | `NCBITaxon:3088`; GenBank marker accession `MG971386.1` | Photoautotrophic BG-11 cultivation with air or 2% CO2; BG-11 plus CO2 cultures had cell concentrations largely similar to YM medium | Applied | Variant added: `bg11_scenedesmus_obliquus_abc009_photoautotrophic` | PMID:34584038 |

Genome assembly IDs are currently present for *Methylosinus* sp. Ce-a6, *Brachyspira pilosicoli* P43/6/78T, *Heyndrickxia coagulans* ATCC 7050 / DSM 1, *Staphylococcus saccharolyticus* ATCC 14953 / DSM 20359 / NCTC 11807, *Halothermothrix orenii* H168, *Sneathiella glossodoripedis* MKT133T / JCM 23214, *Thermus thermophilus* HB27, and *Escherichia coli* K-12 MG1655. *Tetradesmus obliquus* ABC-009 has a strain-level GenBank marker accession (`MG971386.1`), but not a GCA/GCF/SAMN genome assembly or BioSample in the applied YAML. *Helicobacter pylori* OMU89-362 has strain-level growth evidence but no genome assembly/BioSample ID resolved in this pass. Genome/BioSample enrichment remains required for the rest of the strain-level evidence.

## Proposed YAML Change Table

| Parent record | Proposed change | Variant needed? | Status |
|---|---|---:|---|
| `TOGO_M1308_Methylotroph_Medium.yaml` | *Methylosinus* sp. Ce-a6 evidence and lanthanide-test variant already present; *Methylovorus mays* growth metric already present | Partly present | Applied; review formulation details |
| `desulfovibrio_medium.yaml` | *D. intestinalis* KMS2 growth metric already present; strain field/genome ID still needed if source supports it | Maybe | Applied; enrich identifiers |
| `acidiphilium_medium.yaml` | *A. cryptum* aluminum-stress growth evidence and variant now present | Yes | Applied |
| `bg11.yaml` | PCC 6803, PCC 11801, and PCC 11802 evidence and condition variants now present | Yes | Applied |
| `geobacter_sulfurreducens_medium.yaml` | Acetate/fumarate growth metric and variant now present | Yes | Applied |
| `KOMODO_1078_FRIIS_medium.yaml` | *M. hyopneumoniae* isolate growth-kinetics evidence and modified Friis medium variant now present; genome IDs still needed if available for these isolates | Yes | Applied; parent record has unrelated ingredient schema blockers |
| `KOMODO_11_MRS_medium.yaml` | *H. coagulans* ATCC 7050 and *L. plantarum* ATCC 10012 MRS oxygen-condition growth metrics and variant now present; *L. plantarum* BG24 static/shaking and pH/yeast-extract optimization growth metrics and variant now present; H. coagulans GCA/GCF IDs added | Yes | Applied |
| `KOMODO_429_COLUMBIA_BLOOD_AGAR.yaml` | *S. saccharolyticus* ATCC 14953 / DSM 20359 / NCTC 11807 Columbia blood agar qualitative growth evidence, variant, NCBI taxon, and GCA/SAMN identifiers now present | Yes | Applied; parent record has unrelated ingredient schema blockers |
| `KOMODO_761_HALOTHERMOTHRIX_ORENII.yaml` | *H. orenii* H168 high-salt strict-anaerobic growth evidence, variant, NCBI strain taxon, GCA assembly, and BioSample identifiers now present | Yes | Applied |
| `TOGO_M1547_Marine_Agar_2216.yaml` | *S. glossodoripedis* MKT133T colony-formation evidence on Marine Agar 2216 and GCA/GCF genome assembly identifiers now present | No | Applied |
| `TOGO_M1663_Thermus_Medium.yaml` | *T. thermophilus* HB27 growth-kinetics evidence in liquid rich Thermus medium and GCA/GCF genome assembly identifiers now present | No | Applied |
| `TOGO_M2314_LB_medium.yaml` | *E. coli* K-12 MG1655 exact-parent LB growth evidence, NCBI strain taxon, GCA/GCF assembly IDs, and BioSample provenance now present; pre-existing FOODON/synonym ingredient schema issues were normalized into notes | No | Applied |
| `TOGO_M540_Brucella_Broth.yaml` | *H. pylori* OMU89-362 Brucella broth / FBS / H2O2 growth evidence, NCBI species taxon, OD620 metric, and Brucella broth detoxification variant now present; genome/BioSample ID still needed | Yes | Applied |
| `nutrient_broth.yaml` | *M. cosmeticum* DM-11 growth metric and 25 C variant now present; genome ID still needed | Yes | Applied; enrich identifiers |
| `m9.yaml` | Modified M9 high-density expression evidence and variant now present for *E. coli* | Yes | Applied |
| `bhis.yaml` | *Brachyspira pilosicoli* P43/6/78T BHIS broth growth metric, NCBI strain taxon, and GCA/GCF genome assembly IDs now present | Yes | Applied |
| `methanosarcina_medium.yaml` | Growth-phase-specific doubling-time evidence and variant now present | Yes | Applied |
| `caulobacter_medium.yaml` | Cold-growth variant for K31 at 4 C now present | Yes | Applied |
| `magnetospirillum_gryphiswaldense_medium.yaml` | Cr(VI)/magnetosome-deficient strain variant now present | Yes | Applied |
| `pyrococcus_medium.yaml` | Cellulose-adapted growth variant now present | Yes | Applied |
| `rhodobacter_sphaeroides_medium.yaml` | Phototrophic L-phenylalanine sole-N variant now present | Yes | Applied |
| `Artificial_Seawater_Medium.yaml` | Modified artificial seawater variant for the Hemiaulus-Richelia symbiosis and N/P-supplemented ASW variant for Synechocystis PCC 6803 now present | Yes | Applied |
| `Bristol_Medium.yaml` | *Chlorella pyrenoidosa* qualitative Bristol Medium growth evidence now present | No | Applied |
| `F_2_Medium.yaml` | *Tetraselmis marina* F/2 growth evidence and nitrogen-replete second-stage variant now present | Yes | Applied |
| `Enriched_Seawater_Medium.yaml` | Candidate PMID:38942244 describes Sargassum species maintained in 1% Provasoli-enriched seawater medium for 14 d, but the abstract does not directly report growth on the UTEX Enriched Seawater parent formulation | Maybe | Review only; not applied |
| `Modified_Artificial_Seawater_Medium.yaml` | Candidate PMID:33083143 is already represented as `modified_artificial_seawater_hemiaulus_richelia_symbiosis` under the `Artificial_Seawater_Medium.yaml` parent | Yes | Review only on standalone record; parent variant applied |
| `Spirulina_Medium.yaml` | *Arthrospira platensis* conventional Spirulina medium growth evidence and biogas-effluent variant now present | Yes | Applied |
| `TAP_Medium.yaml` | *Chlorella vulgaris* TAP co-culture evidence and *Chlorella sorokiniana* TAP/Ab-WSF evidence now present | Yes | Applied |
| `algae/bg11.yaml` | *Nostoc linckia* BG11/BG110 biomass evidence, *Synechococcus* sp. UCP002 BG-11 growth-rate evidence, and *Tetradesmus obliquus* ABC-009 BG-11 photoautotrophic evidence now present; duplicate bacterial and UTEX BG11 parents should be reconciled later | Yes | Applied |

## Corpus-Wide Next Step

For full-corpus execution, run `just propose-growth` in batches and write a manifest recording every reviewed YAML path. A report should not claim full repo coverage until that manifest covers all primary media YAML records under `data/normalized_yaml/algae`, `archaea`, `bacterial`, `fungal`, and `specialized`.

Recommended batch policy:

1. Exclude `data/normalized_yaml/solutions` from primary target enumeration.
2. Group likely parent/variant records before external research.
3. Run PubMed proposal generation on one directory or filename cluster at a time.
4. Curate proposal candidates from `REVIEW` to `SUPPORT` only when the source names the organism and directly supports growth on the medium or variant.
5. Add variants to the parent `MediaRecipe` rather than creating duplicate media records for small changes.
6. Validate evidence snippets with `just validate-growth` after applying changes.

## Bacterial MediaDive Solution Batch

Date: 2026-05-09

After Falcon returned HTTP `402 Payment Required`, review continued with the
repo-local PubMed proposal pipeline. Two adjacent bacterial batches were run
over the next unreviewed MediaDive solution/main-solution records:

```bash
just propose-growth --category bacterial --offset 8650 --limit 50 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 8700 --limit 50 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 8750 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 8850 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 8950 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 9050 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 9150 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 9250 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 9350 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 9450 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 9550 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 9650 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 9750 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 9850 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 9950 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 10050 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 10150 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 10250 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 10350 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 10450 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 10550 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 10650 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 10750 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 10850 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 10950 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 11050 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 11150 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 11250 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 11350 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 11450 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 11550 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 11650 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 11750 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 11850 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 11950 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 12050 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 12150 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 12250 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 12350 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 12450 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 12550 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 12650 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 12750 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 12850 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 12950 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 13050 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 13150 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 13250 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 13350 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 13450 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 13550 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 13650 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 13750 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 13850 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 13950 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 14050 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 14150 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 14250 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 14350 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 14450 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 14550 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 14650 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 14750 --limit 100 --retmax 1 --apply --write-empty
just propose-growth --category bacterial --offset 14850 --limit 100 --retmax 1 --apply --write-empty
```

Outcome:

- Records processed: 6287
- Proposal files written: 6287
- Candidates found: 476 raw candidates. Manifest review-only candidates include
  newly counted records from recent batches; `methylovirgula_ligni_medium`
  already had a prior review proposal, and `methanosarcina_medium.yaml` is
  already counted as applied growth evidence from backfill.
- Growth metrics found: 3 raw extracted metrics; not applied
- Genome assembly IDs found: 0

These records are mostly MediaDive component solutions, trace/mineral/vitamin
solutions, salt/base solutions, and main-solution fragments. They now have
explicit no-candidate proposal files so the manifest marks them as reviewed
rather than unreviewed. One additional record, `medium_10.yaml`, now has
review-only candidates from broad "medium 10" PubMed hits; none currently
supports an apply-ready organism-medium growth claim. `medium_10_broth.yaml`
also has a review-only *Treponema socranskii* enriched Medium 10 broth lead
(PMID:8941771), but the local JCM record has unavailable composition and this
requires formulation review before any YAML evidence can be applied.
`medium_d.yaml` now has two review-only candidates: one non-microbial
psychology false positive and one algal *Desmochloris edaphica* `Medium D`
lead that does not directly support the bacterial `medium_d.yaml` record
without formulation review. `medium_h.yaml`, `medium_k.yaml`, and
`medium_s.yaml` now have short-name review-only candidates dominated by
non-bacterial systems, non-medium phrase matches, or different media such as
H-2 medium. `methanosarcina_medium.yaml` has a plausible
*Methanosarcina acetivorans* pyruvate-growth lead (PMID:38305193), but it does
not identify the CultureMech formulation or strain/genome in the snippet and
the record is already counted as applied growth evidence via backfill. The
latest batch added review-only candidates for records including
`mg_medium.yaml`, `mh_agar.yaml`, `mh_medium.yaml`, `mhy.yaml`,
`middlebrook_7h10_agar.yaml`, `middlebrook_7h11_agar.yaml`,
`middlebrook_medium.yaml`, and `mineral_medium.yaml`; these need source and
formulation review before any evidence or variants can be applied. The latest
batch added review-only candidates for `mineral_salts_medium.yaml`,
`minimal_media.yaml`, `minimal_mineral_medium.yaml`, and
`minimum_essential_medium_mem.yaml`; these include generic mineral/minimal
medium leads and mammalian MEM false positives, so no YAML evidence was
applied. The latest batch added review-only candidates for `mk_medium.yaml`,
`ml_medium.yaml`, `mm3.yaml`, `mmn.yaml`, `modified_9k_medium.yaml`, and
`modified_baars_medium.yaml`; the `ml_medium.yaml` Pseudomonas PAH-degradation
hit contains an OD600 lead, but the local ML formulation match is unresolved.
The latest batch added review-only candidates for `modified_basal_medium.yaml`,
`modified_bhi.yaml`, `modified_bsk_medium.yaml`, `modified_lb.yaml`,
`modified_lb_medium.yaml`, `modified_m9_medium.yaml`,
`modified_marine_agar_2216.yaml`, `modified_mb.yaml`, and
`modified_medium_10.yaml`; these include plausible modified BHI, BSK, M9, and
marine agar leads but still need formulation and strain/genome review before
YAML evidence can be applied. The latest batch added review-only candidates for
`modified_mrs.yaml`, `modified_mrs_medium.yaml`,
`modified_nutrient_agar.yaml`, `modified_tryptone_soya_broth.yaml`,
`mops_medium.yaml`, `mp.yaml`, `mp_medium.yaml`, and `mpa_medium.yaml`; the
modified MRS hits are plausible but require formulation comparison, while
several `mp` hits are acronym or non-bacterial false positives. The batch moved
the manifest from 6,276 to 2,078 unreviewed records. The latest batch added
review-only candidates for MRS, Mueller-Hinton, Mycoplasma/Mycobacterium, and
short-name records including `mrs_agar.yaml`, `mrs_broth.yaml`,
`mrs_medium.yaml`, `mueller_hinton.yaml`, `mueller_hinton_broth.yaml`,
`mycoplasma_medium.yaml`, and `n75s.yaml`; none was applied because exact
CultureMech formulation/variant and strain or genome linkage still require
manual review. The latest batch added review-only candidates for `na_medium.yaml`,
`nag_medium.yaml`, `nav_medium.yaml`, `nby.yaml`, `ncl.yaml`,
`neomycin_agar.yaml`, `nitrospira_moscoviensis.yaml`, `nms_medium.yaml`,
`nn.yaml`, and `npa.yaml`; the *Nitrospira moscoviensis* doubling-time lead is
real but still needs parent/variant formulation review before applying YAML
evidence. The latest batch added review-only candidates for `nsw.yaml`,
`nutrient_agar.yaml`, `nutrient_agar_slant.yaml`, `oatmeal_agar.yaml`,
`omy.yaml`, `os_medium.yaml`, `p_medium.yaml`, and `pa_medium.yaml`; nutrient
agar and PA medium include plausible organism leads, but exact local
formulation and strain/genome support remain unresolved. The latest batch added
review-only candidates for `pas.yaml`, `pc.yaml`, `pe.yaml`,
`pectin_medium.yaml`, `peptone_broth.yaml`, `per.yaml`, `ph_medium.yaml`,
`phosphate_buffer_ph_7_2.yaml`, and `phosphate_buffered_saline_ph_7_4.yaml`;
`pectin_medium.yaml` includes plausible pectin-medium coculture and oral
treponeme leads, but formulation/parent review is still needed before applying
YAML evidence, while the remaining records are dominated by clinical,
oncology, buffer, or short-name false positives. The batch moved the manifest
to 1,681 unreviewed records. The latest batch added review-only candidates for
`phototrophic_medium.yaml`, `pj.yaml`, `plate_count_agar.yaml`, `pm.yaml`,
`pm_medium.yaml`, `potato_carrot_agar.yaml`, `potato_dextrose_agar.yaml`,
`potato_dextrose_agar_pda.yaml`, `potato_sucrose_agar.yaml`, `pp.yaml`,
`ppg.yaml`, `pplo_broth.yaml`, `ppm.yaml`, `ppy.yaml`, `psa_medium.yaml`, and
`pseudomonas_agar_f.yaml`; PPLO broth, PSA medium, and Pseudomonas Agar F are
plausible follow-up leads, but the cached proposals do not yet establish
strain/genome-resolved local formulation support, while PM/PDA/potato agar
records are mostly algal/fungal contexts and `PJ`/`PP`/`PPG`/`PPM`/`PPY`
records are short-name or non-medium false positives. The next unreviewed
bacterial record was `data/normalized_yaml/bacterial/py4s.yaml` at offset
13,350. The latest batch added review-only candidates for `py_broth.yaml`,
`py_medium.yaml`, `pye_medium.yaml`, `pyg_agar.yaml`, `pyg_medium.yaml`,
`pyrococcus_medium.yaml`, `r2_broth.yaml`, `r2a.yaml`, `r2a_agar.yaml`,
`r2a_broth.yaml`, `r2a_medium.yaml`, `r8_medium.yaml`, and `r_agar.yaml`;
`pyg_medium.yaml` has a plausible *Prevotella copri* DSM 18205T PYG lead with
OD620 cell-density evidence, and R2A records include plausible type-strain or
water-culture leads, but the cached proposals do not yet establish exact
NBRC/TOGO/JCM parent formulation support or genome identifiers. The next
unreviewed bacterial record is
`data/normalized_yaml/bacterial/r_agar_ph_9_0.yaml` at offset 13,450, and the
manifest now has 1,482 unreviewed records. The latest batch added review-only
candidates for `r_medium.yaml`, `rabbit_blood_agar.yaml`, `rc_medium.yaml`,
`rcm_medium.yaml`, `rdm.yaml`, `reinforced_clostridial_medium.yaml`,
`rhodobacter_sphaeroides_medium.yaml`, `rich_medium.yaml`,
`rich_organic_medium.yaml`, and `rm_medium.yaml`; `rcm_medium.yaml` has a
plausible *Clostridium tyrobutyricum* RCM/copper OD550 lead that should be
reviewed as a copper-supplemented RCM variant under the appropriate RCM parent,
but duplicate RCM parent/formulation handling and missing strain/genome
identifiers need manual review before applying YAML evidence. The command also
reported one transient PubMed HTTP 429 warning but completed and wrote all 100
proposal files. The next unreviewed bacterial record is
`data/normalized_yaml/bacterial/roseinatronobacter_medium.yaml` at offset
13,550, and the manifest now has 1,383 unreviewed records.
The latest batch added review-only candidates for `rpl.yaml`,
`rumen_fluid_medium.yaml`, `s_medium.yaml`, `s_w.yaml`, `sa_medium.yaml`,
`sabouraud_glucose_medium.yaml`, `sabourauds_agar.yaml`, `salt_medium.yaml`,
`sbbm.yaml`, `sc_medium.yaml`, `se1.yaml`, and `se2.yaml`; `salt_medium.yaml`
contains a real minimal-salt-medium growth-rate/doubling-time lead, but it does
not establish the local Salt Medium formulation, and the remaining records are
mostly short-name false positives or fungal/algal Sabouraud/SC/S-medium
contexts. The command reported one transient PubMed HTTP 429 warning but
completed and wrote all 100 proposal files. The next unreviewed bacterial
record is `data/normalized_yaml/bacterial/sea_salts_tyg_medium.yaml` at offset
13,650, and the manifest now has 1,283 unreviewed records.
The latest batch added review-only candidates for `sea_water_agar.yaml`,
`seawater_medium.yaml`, `seed_medium.yaml`, `ses.yaml`,
`sheep_blood_agar.yaml`, `si_medium.yaml`, `skirrows_selective_medium.yaml`,
`sl_medium.yaml`, `sm_medium.yaml`, `smc_medium.yaml`, `sna.yaml`,
`sna_5.yaml`, `soil_extract_medium.yaml`, `solid_medium.yaml`,
`sot_medium.yaml`, `soybean_casein_digest_agar.yaml`,
`soybean_casein_digest_broth.yaml`, `sp.yaml`, `sp4_medium.yaml`,
`sp_4_medium.yaml`, and `sp_medium.yaml`; seawater medium, sheep blood agar,
Skirrow's selective medium, and SP-4/SP4 records include plausible follow-up
leads, but the cached abstracts lack strain/genome IDs or exact local
parent/variant formulation support. The next unreviewed bacterial record is
`data/normalized_yaml/bacterial/sphaerochaeta_medium.yaml` at offset 13,750,
and the manifest now has 1,183 unreviewed records.
The latest batch added review-only candidates for `sporulation_medium.yaml`,
`starch_nitrate_medium.yaml`, `sterile_human_urine.yaml`, and
`sucrose_asparagine_medium.yaml`; the defined *Bacillus subtilis*
sporulation-medium lead contains a doubling-time snippet, but exact local
parent or variant formulation support remains unresolved, while sterile human
urine and sucrose-asparagine leads need strain/formulation review. The next
unreviewed bacterial record is
`data/normalized_yaml/bacterial/sucrose_peptone_medium.yaml` at offset 13,850,
and the manifest now has 1,083 unreviewed records.
The latest batch added review-only candidates for
`sucrose_peptone_medium.yaml` and `synthetic_medium.yaml`;
`sucrose_peptone_medium.yaml` is a fungal cultivation hit, and
`synthetic_medium.yaml` is too generic across unrelated synthetic-media
contexts to support the local parent without source/formulation review. The
next unreviewed bacterial record is
`data/normalized_yaml/bacterial/syntrophospora_medium.yaml` at offset 13,950,
and the manifest now has 984 unreviewed records.
The latest batch added review-only candidates for `t5.yaml`, `tge.yaml`, and
`th_agar.yaml`; `T5` and `TGE` are non-medium/short-name false positives, while
`TH agar` lacks enough formulation and strain detail in the cached proposal to
support a local parent or variant update. The next unreviewed bacterial record
is `data/normalized_yaml/bacterial/thermococcales_rich_medium.yaml` at offset
14,050, and the manifest now has 884 unreviewed records.
The latest batch refreshed `thermus_medium.yaml` with a review-only candidate
matching PMID:16233377; this Thermus growth-kinetics evidence is already
represented on `data/normalized_yaml/bacterial/TOGO_M1663_Thermus_Medium.yaml`,
so it was not duplicated on the short-name record. The next unreviewed
bacterial record is
`data/normalized_yaml/bacterial/thioalkalivibrio_jannaschi.yaml` at offset
14,150, and the manifest now has 785 unreviewed records.
The latest batch added review-only candidates for
`thiobacillus_novellus_medium.yaml`, `thioglycolate_medium.yaml`,
`thioglycollate_medium.yaml`, `todd_hewitt_agar.yaml`,
`todd_hewitt_broth.yaml`, and `todd_hewitt_medium.yaml`; the thioglycollate
doubling-time metric is a mouse peritoneal-cell false positive, and the
Thiobacillus/Todd-Hewitt hits lack strain/genome and exact local formulation
support in cached abstracts. The next unreviewed bacterial record is
`data/normalized_yaml/bacterial/togo_medium_m1428.yaml` at offset 14,250, and
the manifest now has 686 unreviewed records.
The latest batch covered TOGO-numbered records from `togo_medium_m1428.yaml`
through `togo_medium_m1613.yaml`; it found zero PubMed candidates and wrote
explicit no-candidate proposal files for all 100 records. The next unreviewed
bacterial record is `data/normalized_yaml/bacterial/togo_medium_m1619.yaml` at
offset 14,350, and the manifest now has 586 unreviewed records.
The latest batch covered TOGO-numbered records from `togo_medium_m1619.yaml`
through `togo_medium_m967.yaml`, plus `tomato_agar_ta.yaml`; it found zero
PubMed candidates and wrote explicit no-candidate proposal files for all 100
records. The next unreviewed bacterial record is
`data/normalized_yaml/bacterial/tomato_juice_agar.yaml` at offset 14,450, and
the manifest now has 486 unreviewed records.
The latest batch added review-only candidates for `tomato_juice_agar.yaml`,
`tomato_juice_medium.yaml`, and `tpgy_broth.yaml`; tomato-juice hits are
fungal/Candida identification contexts, and the TPGY broth hit is broad
Bacillus food-testing evidence without strain/genome or formulation support.
The command reported one transient PubMed HTTP 500 warning but completed and
wrote all 100 proposal files. The next unreviewed bacterial record is
`data/normalized_yaml/bacterial/trebonia_medium.yaml` at offset 14,550, and the
manifest now has 386 unreviewed records.
The latest batch added review-only candidates for `treponema_medium.yaml`,
`tryptic_soy_agar.yaml`, `trypticase_soy_agar.yaml`,
`trypticase_soy_blood_agar.yaml`, `trypticase_soy_broth_agar.yaml`,
`trypticase_soy_broth_tsb.yaml`, `trypticase_soy_yeast_extract_medium.yaml`,
`tryptone_soya_broth_tsb.yaml`, `tryptone_yeast_extract_agar.yaml`,
`tryptose_blood_agar_base.yaml`, `tryptose_phosphate_agar.yaml`,
`ts_agar.yaml`, and `tsb.yaml`; these were left as review-only because the
cached abstracts lacked strain/genome identifiers, exact local formulation
support, or were diagnostic/broad-method contexts. One candidate from
`tryptic_soy_broth.yaml` was applied manually: PMID:15931519 explicitly reports
*Arthrobacter psychrolactophilus* ATCC 700733 growth in tryptic soy broth
without dextrose supplemented with 0.5% or 1.0% soluble starch or maltose, with
a 1.5-2.3 h doubling-time range at 22 degrees C. This was modeled as the
`tsb_without_dextrose_plus_starch_or_maltose` variant under the existing
`tryptic_soy_broth.yaml` parent, with NCBITaxon:92442 and genome assembly
GCA_003219795 from BacDive/NCBI-linked strain metadata. The next unreviewed
bacterial record is `data/normalized_yaml/bacterial/tsb_k3.yaml` at offset
14,961, and the manifest now has 287 unreviewed records.
The latest batch added review-only candidates for `ttl.yaml`,
`tween_80_agar.yaml`, `ty_medium.yaml`, `tyb.yaml`, `tyg_medium.yaml`,
`um.yaml`, `v8_juice_agar.yaml`, `v_8_juice_agar.yaml`, and
`vibrio_medium.yaml`; none was applied. `TTL`, `TYB`, and `UM` were dominated
by non-medium acronym matches or non-bacterial systems; Tween 80 agar and V8
juice agar hits were fungal/oomycete contexts; `TY` and `TYG` hits lacked exact
local formulation support or were protozoal/Clostridium contexts without
strain/genome support; and the Vibrio chromogenic-medium hit did not provide an
apply-ready local formulation or strain-specific growth relationship. The next
unreviewed bacterial record is
`data/normalized_yaml/bacterial/vitamin_solution_medium_663.yaml` at offset
14,750, and the manifest now has 187 unreviewed records.
The latest batch added review-only candidates for `vitox.yaml`,
`vogel_bonner_medium.yaml`, `walnes.yaml`, `waris_h.yaml`,
`xylan_medium.yaml`, `ycfa_medium.yaml`, and
`yeast_extract_mannitol_agar_medium.yaml`; no YAML evidence was applied. The
Vitox and Vogel-Bonner hits were broad supplement/assay contexts without exact
local formulation support, Walne's and Waris H were algal/plant contexts,
xylan medium and YCFA had plausible bacterial leads but lacked enough
formulation and identifier support in cached abstracts, and yeast extract
mannitol agar hits lacked strain/genome-resolved growth support. The next
unreviewed bacterial record is
`data/normalized_yaml/bacterial/yeast_extract_starch_agar_50_marine_water.yaml`
at offset 14,850, and the manifest now has 87 unreviewed records.
The final bacterial batch added review-only candidates for `yel.yaml`,
`yepg_medium.yaml`, `ym_agar.yaml`, `ym_broth.yaml`, `ym_medium.yaml`,
`yma_medium.yaml`, `yp_medium.yaml`, `ypad_medium.yaml`,
`ypd_liquid_medium.yaml`, `ypd_medium.yaml`, `ypg_medium.yaml`, `ypga.yaml`,
`ypm_medium.yaml`, `yps_medium.yaml`, `ypss_medium.yaml`, `ysg_medium.yaml`,
and `z_medium.yaml`; no YAML evidence was applied. The batch was dominated by
yeast/fungal, algal, plant, or short-name contexts. The lone extracted metric
from `ypd_medium.yaml` captured the SD-medium OD600 value from the abstract
rather than an apply-ready YPD growth metric, and the remaining YP/YM/YSG/Z
hits lacked strain/genome-resolved local formulation support. The final
manifest rebuild reports zero `not_reviewed` records across the normalized YAML
corpus.

## Falcon-Assisted ASW/F/2 Curation Batch

Date: 2026-05-09

This batch used a completed FutureHouse/Edison Falcon report for
`data/normalized_yaml/algae/2asw.yaml`, followed by manual source review of
CCAP, NCBI, PubMed, and UTEX pages. A subsequent Falcon call for
`data/normalized_yaml/algae/F_2_Medium.yaml` failed with HTTP `402 Payment
Required`, so F/2 updates were curated from the completed 2ASW report and
public source metadata rather than from a second Falcon report.

### Applied YAML Changes

| Parent medium path | Variant name | Affected organism/strain | Evidence source | Applied? | Notes |
|---|---|---|---|---|---|
| `data/normalized_yaml/algae/2asw.yaml` | none | *Dunaliella salina* CCAP 19/18 | CCAP strain page; NCBI BioProject PRJNA32771 | yes | Direct 2ASW parent-medium match. Added NCBITaxon:3046 plus BioProject/BioSample/WGS/assembly identifiers in evidence notes. |
| `data/normalized_yaml/algae/2asw.yaml` | `f_2asw` | *Phaeodactylum tricornutum* UTEX 642 | Matsui et al. 2018, DOI:10.1104/pp.18.00453 / PMID:30076224 | yes | Modeled as F/2 nutrient-supplemented artificial seawater variant under the 2ASW parent. |
| `data/normalized_yaml/algae/2asw.yaml` | `f_2asw` | *Thalassiosira pseudonana* CCMP1335 | Matsui et al. 2018, DOI:10.1104/pp.18.00453 / PMID:30076224 | yes | Modeled as F/2 nutrient-supplemented artificial seawater variant under the 2ASW parent. |
| `data/normalized_yaml/algae/2asw.yaml` | `modified_f_2asw_sodium_response` | *Chaetoceros gracilis* UTEX LB2658 | Tsuji et al. 2021, DOI:10.1007/s10126-021-10037-4 / PMID:34109463; UTEX LB 2658 strain page | yes | Modeled as a sodium/CO2 response variant, not a separate parent medium. |
| `data/normalized_yaml/algae/F_2_Medium.yaml` | `f_2asw_diatom_culture` | *Phaeodactylum tricornutum* UTEX 642 | Matsui et al. 2018, DOI:10.1104/pp.18.00453 / PMID:30076224 | yes | Applied to the F/2 parent as a F/2ASW implementation variant with OD730 harvest ranges in `growth_metrics`. |
| `data/normalized_yaml/algae/F_2_Medium.yaml` | `f_2asw_diatom_culture` | *Thalassiosira pseudonana* CCMP1335 | Matsui et al. 2018, DOI:10.1104/pp.18.00453 / PMID:30076224 | yes | Applied to the F/2 parent as a F/2ASW implementation variant with OD730 harvest ranges in `growth_metrics`. |
| `data/normalized_yaml/algae/F_2_Medium.yaml` | `modified_f_2asw_sodium_response` | *Chaetoceros gracilis* UTEX LB2658 | Tsuji et al. 2021, DOI:10.1007/s10126-021-10037-4 / PMID:34109463; UTEX LB 2658 strain page | yes | Applied as an experimental modified F/2ASW sodium-response variant. |

### Evidence And Identifier Notes

- CCAP lists *Dunaliella salina* CCAP 19/18 with medium `2ASW`, axenic serial
  subculture, and maintenance at 20-35 deg C. NCBI BioProject PRJNA32771 links
  the same strain to Taxonomy ID 3046, BioSample SAMN02746051, WGS
  NSFN00000000, and assembly GCA_002284615.2.
- PubMed record PMID:30076224 identifies Matsui et al. 2018
  (`DOI:10.1104/pp.18.00453`). The Falcon report extracted method-level
  evidence that *Phaeodactylum tricornutum* UTEX 642 and
  *Thalassiosira pseudonana* CCMP1335 were cultured in F/2ASW at 20 deg C,
  continuous light, and ambient-air or CO2 aeration.
- Tsuji et al. 2021 (`DOI:10.1007/s10126-021-10037-4`; PMID:34109463)
  supports *Chaetoceros gracilis* UTEX LB2658 growth experiments in modified
  F/2ASW with sodium selenite, sodium metasilicate, NaCl-based sodium
  manipulation, and varied CO2 availability. The UTEX LB 2658 page confirms the
  strain identity and general liquid-culture maintenance metadata.

### Validation

- `data/normalized_yaml/algae/F_2_Medium.yaml` passes
  `just validate data/normalized_yaml/algae/F_2_Medium.yaml`.
- `data/normalized_yaml/algae/2asw.yaml` passes
  `just validate data/normalized_yaml/algae/2asw.yaml` after normalizing legacy
  category, reference, curation-history, ingredient provenance, and
  `data_quality_flags` fields.
- `just validate-growth` completed successfully after the ASW/F/2 edits: 124
  evidence items checked; 87 `OK`, 2 `MISSING_CACHE`, and 35 `NO_EVIDENCE`.
  The remaining `MISSING_CACHE` entries are unrelated existing evidence items;
  database/catalog provenance is reported as `NO_EVIDENCE` by the PubMed/DOI
  snippet validator when no snippet is supplied.
