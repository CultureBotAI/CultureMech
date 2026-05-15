# Media Variant Completion Audit

Date: 2026-05-13

## Objective Restated

Review the CultureMech media YAML corpus to assess ingredient validity,
concentration coverage, and possible media variations. Represent reviewed
media variations as child YAML records with explicit parent links, and add
child links on parent media records, across the current
`data/normalized_yaml/**/*.yaml` corpus.

## Prompt-To-Artifact Checklist

| Requirement | Evidence | Current status |
|---|---|---|
| Assess the current YAML media corpus | `reports/media_content_review_manifest.tsv`, `reports/media_content_review_manifest_summary.md`, `reports/media_ingredient_variant_state_assessment.md` | Covered for all 15,827 normalized YAML records. |
| Validate ingredient state | Manifest counts ingredient entries, CHEBI coverage, MediaIngredientMech coverage, non-CHEBI IDs, unexpected ingredient keys, and missing/blank terms | Partially covered. Review exists, but ingredient normalization is incomplete. |
| Validate concentration state | Manifest counts missing/malformed concentration objects, missing values/units, non-schema units, and `VARIABLE` concentrations | Partially covered. Syntactic coverage is high, but many semantic concentration issues remain. |
| Identify possible variation groups | `reports/media_variation_candidate_groups.tsv/json`, `reports/media_variant_link_proposals.tsv/json`, `reports/media_variant_parent_group_proposals.tsv/json` | Covered as candidate discovery; not all proposals are curated. |
| Add schema support for parent/child variant records | `src/culturemech/schema/culturemech.yaml`, regenerated dataclasses, `tests/test_media_variant_links.py` | Implemented and tested. |
| Represent variations as child YAML records | Applied parent/child links in normalized YAML records; latest validation counts 2,546 child links | Partially complete. Curated subset applied, not full corpus. |
| Parent media YAML contains links to each child | `variant_children` links validated by `scripts/validate_media_variant_links.py` | Partially complete for applied families. |
| Validate bidirectional links | `reports/media_variant_link_validation.md/tsv` | Covered for current corpus state: 15,827 records, 2,546 parent links, 2,546 child links, 0 errors, 0 warnings. |
| Avoid applying broad or ambiguous groups blindly | `reports/media_variant_algae_source_duplicate_review.md` | Covered for broad algae exact-signature groups; 103 algae proposals downgraded to review-required. |
| Apply a non-duplicate concentration-variant family | `reports/media_variant_zahorchak_grid_review.md`, Zahorchak YAML edits | Covered for two Zahorchak ATP/Mg2+ concentration-grid groups, 28 child links. |
| Apply a salinity-variant family | `reports/media_variant_m63_salinity_grid_review.md`, modified M63 YAML edits | Covered for three modified M63 salinity grids, 9 child links. |
| Apply another salinity-variant family | `reports/media_variant_802_salinity_grid_review.md`, 802 YAML edits | Covered for one TOGO/NBRC 802 NaCl grid, 3 child links. |
| Apply another salinity-variant family | `reports/media_variant_rdm_salinity_grid_review.md`, RDM YAML edits | Covered for one MediaDB RDM NaCl grid, 2 child links. |
| Apply another concentration-variant family | `reports/media_variant_defined_freshwater_cobalt_grid_review.md`, defined freshwater cobalt YAML edits | Covered for two MediaDB cobalt-source concentration grids, 6 child links. |
| Apply another concentration-variant family | `reports/media_variant_potato_carrot_agar_review.md`, Potato-Carrot Agar YAML edits | Covered for one JCM/DSMZ Potato-Carrot Agar concentration family, 2 child links. |
| Apply another concentration-variant family | `reports/media_variant_btt_medium_review.md`, BTT medium YAML edits | Covered for one JCM/DSMZ/KOMODO BTT concentration family, 2 child links. |
| Apply another concentration-variant family | `reports/media_variant_xed_agar_review.md`, XED Agar YAML edits | Covered for one JCM/DSMZ/KOMODO XED Agar concentration family, 2 child links. |
| Apply another concentration-variant family | `reports/media_variant_tcg_medium_review.md`, TCG medium YAML edits | Covered for one JCM/DSMZ/KOMODO TCG medium concentration family, 2 child links. |
| Apply another source-duplicate family | `reports/media_variant_ypg_medium_review.md`, YPG medium YAML edits | Covered for two DSMZ/KOMODO YPG source-duplicate pairs, 2 child links. |
| Apply another source-duplicate family | `reports/media_variant_dsmz_komodo_source_duplicate_review.md`, DSMZ/KOMODO YAML edits | Covered for six hundred fifty-two one-to-one DSMZ/KOMODO source-duplicate pairs, 652 child links. |
| Apply another salinity-variant family | `reports/media_variant_asw_barley_salinity_grid_review.md`, ASW barley YAML edits | Covered for one CCAP ASW barley salinity grid, 2 child links. |
| Apply another concentration-variant family | `reports/media_variant_m9_kazan_glucose_grid_review.md`, M9 Kazan YAML edits | Covered for one MediaDB M9 glucose concentration grid, 4 child links. |
| Apply another concentration-variant family | `reports/media_variant_m9_park_zinc_grid_review.md`, M9 Park YAML edits | Covered for four MediaDB M9 zinc concentration grids, 8 child links. |
| Apply another concentration-variant family | `reports/media_variant_mrs_fructose_grid_review.md`, MRS fructose YAML edits | Covered for one TOGO/NBRC MRS fructose concentration grid, 2 child links. |
| Apply another concentration-variant family | `reports/media_variant_hassan_limiting_grid_review.md`, Hassan minimal-media YAML edits | Covered for one MediaDB limiting-nutrient concentration grid, 3 child links. |
| Apply another concentration-variant family | `reports/media_variant_m40y_sucrose_grid_review.md`, M40Y/MY50G/M60Y YAML edits | Covered for one TOGO/JCM/NBRC M40Y sucrose concentration grid plus one source duplicate, 4 child links. |
| Apply another concentration-variant family | `reports/media_variant_802_glucose_grid_review.md`, 802 glucose YAML edits | Covered for one TOGO/NBRC 802 glucose concentration grid, 2 child links. |
| Apply another salinity-variant family | `reports/media_variant_desulfovibrio_brackish_salinity_review.md`, Desulfovibrio YAML edits | Covered for one KOMODO/DSMZ marine-to-brackish salinity family, 2 child links. |
| Apply another concentration-variant family | `reports/media_variant_fungal_mcafes_glucose_grid_review.md`, fungal mCAFEs YAML edits | Covered for one CultureBotHT fungal mCAFEs glucose concentration grid, 2 child links. |
| Apply another salinity-variant family | `reports/media_variant_mrs_nacl_salinity_review.md`, MRS NaCl YAML edits | Covered for two source-specific MRS NaCl salinity families, 4 child links. |
| Apply another concentration-variant family | `reports/media_variant_hmm_junlon_grid_review.md`, HMM Junlon YAML edits | Covered for one MediaDB HMM Junlon dose grid, 3 child links. |
| Apply another salinity-variant family | `reports/media_variant_reinforced_clostridial_sea_salt_review.md`, Reinforced Clostridial Medium sea-salt YAML edits | Covered for two source-specific 3% to 4% sea-salt pairs, 2 child links. |
| Apply another mixed concentration/salinity batch | `reports/media_variant_small_axis_batch_review.md`, small-axis YAML edits | Covered for nine one-axis variant links across MediaDB, JCM/MediaDive, and TOGO records. |
| Apply another concentration-variant batch | `reports/media_variant_inorganic_defined_freshwater_review.md`, inorganic and defined freshwater YAML edits | Covered for five one-axis concentration-variant links across MediaDB records. |
| Apply another mixed one-axis batch | `reports/media_variant_isolated_one_axis_review.md`, isolated bacterial/fungal/specialized YAML edits | Covered for six one-axis concentration/salinity links. |
| Apply another salinity-variant batch | `reports/media_variant_lb_salinity_review.md`, LB salinity YAML edits | Covered for three source-specific LB/Luria salt variant links. |
| Apply another salinity-variant batch | `reports/media_variant_horikoshi_salinity_review.md`, Horikoshi-I salinity YAML edits | Covered for one JCM/MediaDive 2% to 3.5/5/10% NaCl salinity grid, 3 child links. |
| Apply another salinity-variant batch | `reports/media_variant_source_local_salinity_review.md`, source-local salinity YAML edits | Covered for four JCM/MediaDive and TOGO salinity variant links. |
| Apply another mixed concentration/salinity batch | `reports/media_variant_halobacteria_review.md`, Halobacteria medium YAML edits | Covered for four source-local Halobacteria-style links. |
| Apply another salinity/condition batch | `reports/media_variant_salinity_ph_review.md`, salinity plus pH YAML edits | Covered for two salinity children with explicit pH conditions under existing parent groups. |
| Apply another concentration-variant batch | `reports/media_variant_strength_buffer_review.md`, strength and buffer YAML edits | Covered for three one-axis concentration links. |
| Apply another mixed one-axis batch | `reports/media_variant_mixed_one_axis_review.md`, mixed bacterial/specialized YAML edits | Covered for six one-axis concentration/salinity links. |
| Apply another mixed one-axis batch | `reports/media_variant_isp_cys_pfennig_methylobacterium_review.md`, ISP/CYS/Pfennig/Methylobacterium YAML edits | Covered for five one-axis salinity/concentration links. |
| Apply another mixed one-axis batch | `reports/media_variant_mmys_lb_nitrifier_salinispira_review.md`, MMYS/LB/nitrifier/Salinispira YAML edits | Covered for four one-axis salinity/concentration links. |
| Apply another concentration-variant batch | `reports/media_variant_togo_nbrc_agar_strength_review.md`, TOGO/NBRC agar strength YAML edits | Covered for two one-axis concentration links. |
| Apply another concentration-variant batch | `reports/media_variant_togo_nbrc_strength_review.md`, TOGO/NBRC strength YAML edits | Covered for four source-local concentration links. |
| Apply another concentration-variant batch | `reports/media_variant_togo_sw_cmye_gym_r2a_review.md`, TOGO SW/CM+YE/GYM/R2A YAML edits | Covered for six source-local concentration links. |
| Apply another concentration-variant batch | `reports/media_variant_specialized_strength_review.md`, specialized strength YAML edits | Covered for four concentration links. |
| Apply another concentration-variant batch | `reports/media_variant_dilution_named_strength_review.md`, dilution and named-strength YAML edits | Covered for seven concentration links. |
| Apply another concentration-variant batch | `reports/media_variant_r2a_nutrient_agar_dilution_review.md`, R2A and Nutrient Agar dilution YAML edits | Covered for three concentration links. |
| Apply another mixed strength/salinity batch | `reports/media_variant_misc_strength_salinity_review.md`, miscellaneous strength/salinity YAML edits | Covered for five concentration/salinity links. |
| Apply another salinity-variant batch | `reports/media_variant_tsb_gym_salinity_review.md`, TSB/GYM salinity YAML edits | Covered for three salinity links. |
| Apply another mixed concentration/salinity batch | `reports/media_variant_lb_r2a_cys_review.md`, LB/R2A/CYS YAML edits | Covered for three concentration/salinity links. |
| Apply another source-duplicate/concentration batch | `reports/media_variant_same_name_duplicate_agar_review.md`, same-name duplicate and agar YAML edits | Covered for two source-duplicate links and one concentration link. |
| Apply another salinity/pH batch | `reports/media_variant_togo_tsb_nacl_ph_review.md`, TOGO Trypticase Soy Broth Agar YAML edits | Covered for two salinity links and one pH link. |
| Apply another source-duplicate/concentration batch | `reports/media_variant_same_name_concentration_source_review.md`, same-name Nutrient Agar, Mixotrophic Nitrobacter, and Acidimicrobium YAML edits | Covered for one source-duplicate link and two concentration links. |
| Apply another concentration-variant batch | `reports/media_variant_defined_strength_concentration_review.md`, CDM, 3N-BBM+V, and Enriched Cytophaga Agar YAML edits | Covered for three concentration links. |
| Apply another concentration-variant batch | `reports/media_variant_ym_sw_k_concentration_review.md`, YM, SW-20, and K Medium YAML edits | Covered for four concentration links. |
| Apply another concentration-variant batch | `reports/media_variant_rhodobacter_halosimplex_acetobacter_review.md`, Rhodobacter, Halosimplex, and Acetobacter YAML edits | Covered for four concentration links. |
| Apply another concentration-variant batch | `reports/media_variant_haloalkaliphile_alkaliphilus_chitin_review.md`, Haloalkaliphile, Alkaliphilus, and Chitin medium YAML edits | Covered for four concentration links. |
| Apply another concentration-variant batch | `reports/media_variant_anaerobe_ml_concentration_review.md`, anaerobe and ML medium YAML edits | Covered for four concentration links. |
| Apply another mixed source/concentration batch | `reports/media_variant_nam_tsby_gauze_573c_review.md`, NAM, TSBY, Gauze, and 573C YAML edits | Covered for one source-duplicate link and three concentration links. |
| Apply another concentration-variant batch | `reports/media_variant_rhodobium_mj_asw_acetobacter_dc8a_review.md`, Rhodobium, MJ, ASW, Acetobacter, and DC-8A YAML edits | Covered for five concentration links. |
| Apply another concentration-variant batch | `reports/media_variant_acid_hypho_manning_marinitoga_review.md`, Acidimicrobium, Hyphomicrobium, Manning, and Marinitoga YAML edits | Covered for four concentration links. |
| Apply another concentration-variant batch | `reports/media_variant_anaerobe_halobacteria_l21_review.md`, anaerobe, Halobacteria, and L21 YAML edits | Covered for four concentration links. |
| Apply another source-duplicate batch | `reports/media_variant_nutrient_agar_source_duplicate_review.md`, Nutrient Agar YAML edits | Covered for one hundred fifty-one source-duplicate links. |
| Apply another source-duplicate batch | `reports/media_variant_gyp_source_duplicate_review.md`, GYP YAML edits | Covered for eight source-duplicate links. |
| Apply another source-duplicate batch | `reports/media_variant_medium_88_source_duplicate_review.md`, Medium 88 YAML edits | Covered for seven source-duplicate links. |
| Apply another source-duplicate batch | `reports/media_variant_phototrophic_source_duplicate_review.md`, phototrophic medium YAML edits | Covered for six source-duplicate links. |
| Apply another source-duplicate batch | `reports/media_variant_sulfurimonas_source_duplicate_review.md`, Sulfurimonas YAML edits | Covered for one source-duplicate link. |
| Apply another source-duplicate batch | `reports/media_variant_yps_source_duplicate_review.md`, YPS YAML edits | Covered for two source-duplicate links. |
| Validate changed YAML | Targeted schema validation loops for 30 Zahorchak files, 12 modified M63 files, 4 802 salinity files, 3 RDM files, 8 defined freshwater cobalt files, 3 Potato-Carrot Agar files, 3 BTT medium files, 3 XED Agar files, 3 TCG medium files, 4 YPG medium files, 1304 DSMZ/KOMODO source-duplicate files, 3 ASW barley files, 5 M9 Kazan files, 12 M9 Park zinc files, 3 MRS fructose files, 4 Hassan limiting-nutrient files, 5 M40Y sucrose-grid files, 3 802 glucose-grid files, 3 Desulfovibrio marine/brackish files, 3 fungal mCAFEs files, 6 MRS NaCl files, 4 HMM Junlon files, 4 Reinforced Clostridial Medium sea-salt files, 18 small-axis batch files, 10 inorganic/defined-freshwater files, 12 isolated one-axis files, 5 LB salinity files, 4 Horikoshi-I salinity files, 8 source-local salinity files, 7 Halobacteria files, 4 salinity/pH files, 6 strength/buffer files, 12 mixed one-axis files, 9 ISP/CYS/Pfennig/Methylobacterium files, 8 MMYS/LB/nitrifier/Salinispira files, 4 TOGO/NBRC agar strength files, 8 TOGO/NBRC strength files, 12 TOGO SW/CM+YE/GYM/R2A files, 6 specialized strength files, 13 dilution/named-strength files, 5 R2A/Nutrient Agar dilution files, 10 miscellaneous strength/salinity files, 5 TSB/GYM salinity files, 6 LB/R2A/CYS files, 6 same-name duplicate/agar files, 4 TOGO TSB NaCl/pH files, 6 same-name concentration/source files, 6 defined/source-local strength files, 7 YM/SW/K concentration files, 7 Rhodobacter/Halosimplex/Acetobacter concentration files, 8 Haloalkaliphile/Alkaliphilus/Chitin concentration files, 8 anaerobe/ML concentration files, 8 NAM/TSBY/Gauze/573C files, 10 Rhodobium/MJ/ASW/Acetobacter/DC-8A files, 8 Acidimicrobium/Hyphomicrobium/Manning/Marinitoga files, 8 anaerobe/Halobacteria/L21 files, nine 6-file Nutrient Agar subsets, ten 11-file Nutrient Agar subsets, one 7-file Nutrient Agar final subset, 9 GYP source-duplicate files, 8 Medium 88 source-duplicate files, 7 phototrophic source-duplicate files, 2 Sulfurimonas source-duplicate files, and 3 YPS source-duplicate files; link validator; focused tests | Covered for the latest batch. |

## Current Verified State

- YAML records scanned: 15,827
- Total component entries in assessment: 170,715
- Records with complete concentration object/value/unit coverage: 15,453
- Records where every component has a CHEBI `term.id`: 1,822
- Candidate ingredient-identity variation groups: 1,451
- Candidate parent-child links: 9,145
- Current parent-to-child links: 2,546
- Current child-to-parent links: 2,546
- Current link validation errors: 0
- Current link validation warnings: 0

## Completed Batches

- Schema/dataclass/test support for explicit parent/child media variant links.
- Validator and proposal/apply scripts for parent/child links.
- Multiple curated `SOURCE_DUPLICATE` family batches.
- Remaining broad algae exact-signature groups downgraded to
  `REVIEW_REQUIRED`.
- Zahorchak et al. ATP/Mg2+ concentration-grid batch applied as
  `CONCENTRATION_VARIANT`.
- Modified M63 ectoine/glucose/hydroxyectoine salinity-grid batch applied as
  `SALINITY_VARIANT`.
- TOGO/NBRC 802 NaCl salinity-grid batch applied as `SALINITY_VARIANT`.
- MediaDB RDM NaCl salinity-grid batch applied as `SALINITY_VARIANT`.
- MediaDB defined freshwater CoSO4/CoCl2 concentration-grid batch applied as
  `CONCENTRATION_VARIANT`.
- JCM/DSMZ Potato-Carrot Agar concentration-variant batch applied as
  `CONCENTRATION_VARIANT`.
- JCM/DSMZ/KOMODO BTT medium concentration-variant batch applied as
  `CONCENTRATION_VARIANT`.
- JCM/DSMZ/KOMODO XED Agar concentration-variant batch applied as
  `CONCENTRATION_VARIANT`.
- JCM/DSMZ/KOMODO TCG medium concentration-variant batch applied as
  `CONCENTRATION_VARIANT`.
- DSMZ/KOMODO YPG medium source-duplicate batch applied as
  `SOURCE_DUPLICATE`.
- Six hundred fifty-two one-to-one DSMZ/KOMODO source-duplicate pairs applied as
  `SOURCE_DUPLICATE`.
- CCAP ASW barley salinity-grid batch applied as `SALINITY_VARIANT`.
- MediaDB M9 Kazan glucose-grid batch applied as `CONCENTRATION_VARIANT`.
- MediaDB M9 Park zinc-grid batch applied as `CONCENTRATION_VARIANT`.
- TOGO/NBRC MRS fructose-grid batch applied as `CONCENTRATION_VARIANT`.
- MediaDB Hassan limiting-nutrient batch applied as `CONCENTRATION_VARIANT`.
- TOGO/JCM/NBRC M40Y sucrose-grid batch applied as `CONCENTRATION_VARIANT` plus
  one `SOURCE_DUPLICATE`.
- TOGO/NBRC 802 glucose-grid batch applied as `CONCENTRATION_VARIANT`.
- KOMODO/DSMZ Desulfovibrio marine/brackish salinity batch applied as
  `SALINITY_VARIANT`.
- CultureBotHT fungal mCAFEs glucose-grid batch applied as
  `CONCENTRATION_VARIANT`.
- JCM/MediaDive and TOGO MRS NaCl salinity batches applied as
  `SALINITY_VARIANT`.
- MediaDB HMM Junlon PW 110 dose-grid batch applied as
  `CONCENTRATION_VARIANT`.
- JCM/MediaDive and TOGO Reinforced Clostridial Medium sea-salt batches applied
  as `SALINITY_VARIANT`.
- Nine one-axis concentration/salinity variant links applied across modified
  M1 lactate, RDM ammonium chloride, P2 butanol challenge, nutrient broth NaCl,
  Marine 2216 NaCl, R2A NaCl, 1/2 ISP 2 NaCl, and MRS NaCl pairs.
- Five inorganic and defined freshwater concentration-variant links applied
  across ferrous sulfate, toluene, and nitrate concentration axes.
- Six isolated one-axis variant links applied across malt-extract, glycerol,
  ethanol, Marine AOB NaCl, and Varel Bryant low-cysteine variants.
- Three source-specific LB/Luria broth salinity variant links applied.
- JCM/MediaDive Horikoshi-I 2/3.5/5/10% NaCl salinity grid applied as
  `SALINITY_VARIANT`.
- Four source-local TSB agar, fungal ISP-2 agar, and CM+YE salinity variant
  links applied as `SALINITY_VARIANT`.
- Four source-local Halobacteria-style salinity/concentration variant links
  applied.
- Two salinity child records with explicit pH conditions added under existing
  TSB agar and fungal ISP-2 parent groups.
- Three strength and buffer concentration variant links applied across Marine
  Broth 2216, YM agar, and BL medium.
- Six mixed one-axis concentration/salinity variant links applied across TOGO,
  DSMZ, and FEBA records.
- Five ISP/CYS/Pfennig/Methylobacterium one-axis variant links applied.
- Four MMYS/LB/nitrifier/Salinispira one-axis variant links applied.
- Two TOGO/NBRC agar strength concentration-variant links applied.
- Four TOGO/NBRC strength concentration-variant links applied.
- Six TOGO SW/CM+YE/GYM/R2A concentration-variant links applied.
- Four specialized strength concentration-variant links applied.
- Seven dilution and named-strength concentration-variant links applied.
- Three R2A and Nutrient Agar dilution concentration-variant links applied.
- Five miscellaneous strength and salinity variant links applied.
- Three TSB and GYM salinity variant links applied.
- Three LB/R2A/CYS concentration and salinity variant links applied.
- Two same-name source-duplicate links and one Sucrose-Bennett agar
  concentration-variant link applied.
- Two TOGO Trypticase Soy Broth Agar salinity-variant links and one pH-variant
  link applied.
- One Nutrient Agar source-duplicate link plus two same-name concentration-
  variant links for Mixotrophic Nitrobacter and Acidimicrobium media applied.
- Three defined/source-local strength concentration-variant links applied for
  CDM, 3N-BBM+V, and Enriched Cytophaga Agar records.
- Four YM/SW-20/K Medium concentration-variant links applied.
- Four Rhodobacter/Halosimplex/Acetobacter concentration-variant links applied.
- Four Haloalkaliphile/Alkaliphilus/Chitin concentration-variant links applied.
- Four anaerobe/ML concentration-variant links applied.
- One NAM source-duplicate link plus three TSBY/Gauze/573C concentration-
  variant links applied.
- Five Rhodobium/MJ/ASW/Acetobacter/DC-8A concentration-variant links applied.
- Four Acidimicrobium/Hyphomicrobium/Manning/Marinitoga concentration-variant
  links applied.
- Four anaerobe/Halobacteria/L21 concentration-variant links applied.
- One hundred fifty-one Nutrient Agar source-duplicate links applied.
- Eight GYP source-duplicate links applied.
- Seven Medium 88 source-duplicate links applied.
- Six phototrophic medium source-duplicate links applied.
- One Sulfurimonas medium source-duplicate link applied.
- Two YPS source-duplicate links applied.

## Remaining Gaps

- The full 15k-record corpus has not been fully migrated into parent/child
  variant structure.
- Most non-duplicate proposals still need source/formulation review before
  links should be applied.
- Ingredient normalization remains incomplete:
  - only 1,822 records currently have CHEBI IDs on every component
  - 1,872 component entries use non-CHEBI `term.id` values
  - some entries have blank ingredient names, including exogenous-ATP
    components in the Zahorchak grid
- Concentration normalization remains incomplete:
  - 533 non-schema concentration units
  - 6,649 records using `VARIABLE` concentration units
- Current proposal counts include already-applied links; future status reports
  should distinguish proposed, applied, and deferred relationships explicitly.

## Completion Judgment

The objective is not complete. The repo now has corpus-wide assessment,
schema/model support, validation tooling, curated batches, and clean
bidirectional links for 2,546 relationships, but many candidate variations and
ingredient/concentration normalization issues remain unresolved.
