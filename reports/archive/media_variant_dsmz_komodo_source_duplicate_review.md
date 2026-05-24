# DSMZ/KOMODO Source-Duplicate Variant Review

Date: 2026-05-13

## Decision

Applied parent/child `MediaRecipe` links for six hundred fifty-two one-to-one DSMZ/KOMODO
source-duplicate pairs:

| Parent path | Child path | Relationship |
|---|---|---|
| `data/normalized_yaml/bacterial/macromonas_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_847_MACROMONAS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/caldicoprobacter_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1233_CALDICOPROBACTER_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/lentibacillus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1449_LENTIBACILLUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/sporohalobacter_lortetii_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_319_SPOROHALOBACTER_LORTETII_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/thermus_ruber_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_256_THERMUS_RUBER_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/spirillum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_37_SPIRILLUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/amb_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_455_AMB_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/caminicella_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_964_CAMINICELLA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/mjanhox_no3_medium_with_supplement.yaml` | `data/normalized_yaml/bacterial/KOMODO_1000_MJANHOX-NO3_MEDIUM_WITH_SUPPLEMENT.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/basal_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1001_BASAL_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/ectothiorhodosynus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1002_ECTOTHIORHODOSYNUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/hydrogen_oxydizing_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1003_HYDROGEN-OXYDIZING_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/anaerolinea_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1004_ANAEROLINEA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/allisonella_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1006_ALLISONELLA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/mineral_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1007_MINERAL_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/ypga.yaml` | `data/normalized_yaml/bacterial/KOMODO_1015_YPGA.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/idiomarina_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1016_IDIOMARINA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/haloferax_sulfurifontis_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1018_HALOFERAX_SULFURIFONTIS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/nutrient_agar_or_broth_with_nacl.yaml` | `data/normalized_yaml/bacterial/KOMODO_101_NUTRIENT_AGAR_or_BROTH_WITH_NaCl.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/sodalis_glossinidius_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1021_SODALIS_GLOSSINIDIUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/maricaulis_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1025_MARICAULIS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/bbl_actinomyces_broth.yaml` | `data/normalized_yaml/bacterial/KOMODO_1029_BBL_ACTINOMYCES_BROTH.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/flavobacterium_aquatile_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_102_FLAVOBACTERIUM_AQUATILE_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/smithella_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1030_SMITHELLA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/medium_for_methylobacterium_podarium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1032_MEDIUM_FOR_METHYLOBACTERIUM_PODARIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/alkaliphilic_halomonas_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1034_ALKALIPHILIC_HALOMONAS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/collimonas_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1035_COLLIMONAS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/thiomonas_delicata_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1037_THIOMONAS_DELICATA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/acidicaldus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1038_ACIDICALDUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/vulcanibacillus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1042_VULCANIBACILLUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/ignisphaera_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1043_IGNISPHAERA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/gluconacetobacter_rhaeticus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1044_GLUCONACETOBACTER_RHAETICUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/anoxybacillus_amylolyticus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1046_ANOXYBACILLUS_AMYLOLYTICUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/difco_raka_ray_no_3_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1047_DIFCO_RAKA-RAY_NO.3_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/gauzes_synthetic_medium_no_1.yaml` | `data/normalized_yaml/bacterial/KOMODO_1048_GAUZE_S_SYNTHETIC_MEDIUM_NO.1.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/selenate_reducer_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1049_SELENATE_REDUCER_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/dextran_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1050_DEXTRAN_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/tepidanaerobacter_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1051_TEPIDANAEROBACTER_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/bosea_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1052_BOSEA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/a1_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1054_A1-MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/ethanoligenes_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1057_ETHANOLIGENES_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/geoalkalibacter_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1059_GEOALKALIBACTER_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/gluconobacter_oxydans_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_105_GLUCONOBACTER_OXYDANS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/modified_th_agar.yaml` | `data/normalized_yaml/bacterial/KOMODO_1061_MODIFIED_TH_AGAR.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/desulfitobacterium_pce_ii_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1062_DESULFITOBACTERIUM_PCE_II_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/brevibacillus_levickii_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1064_BREVIBACILLUS_LEVICKII_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/m1_nocardiopsis_arabia_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1065_M1-NOCARDIOPSIS_ARABIA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/marinobacter_lutaoensis_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1066_MARINOBACTER_LUTAOENSIS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/modified_biebl_and_pfennigs_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1069_MODIFIED_BIEBL_AND_PFENNIG_S_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/ym_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1070_YM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/py_broth.yaml` | `data/normalized_yaml/bacterial/KOMODO_1071_PY-BROTH.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/ppes_ii_agar_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1075_PPES-II_AGAR_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/sp4_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1076_SP4_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/friis_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1078_FRIIS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/horikoshi_1_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1081_HORIKOSHI-1_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/aminiphilus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1082_AMINIPHILUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/aciduliprofundum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1083_ACIDULIPROFUNDUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/howardella_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1085_HOWARDELLA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/desulfatirhabdium_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1086_DESULFATIRHABDIUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/haloquadratum_walsbyi_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1091_HALOQUADRATUM_WALSBYI_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/thermosulfidibacter_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1092_THERMOSULFIDIBACTER_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/natranaerobius_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1095_NATRANAEROBIUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/sulfurospirillum_mv_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1097_SULFUROSPIRILLUM_MV_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/desulfoluna_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1099_DESULFOLUNA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/rhodopseudomonas_sulfoviridis_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_109_RHODOPSEUDOMONAS_SULFOVIRIDIS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/zymomonas_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_10_ZYMOMONAS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/desulfonatronospira_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1101_DESULFONATRONOSPIRA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/dethiobacter_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1104_DETHIOBACTER_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/nitriliruptor_alkaliphilus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1105_NITRILIRUPTOR_ALKALIPHILUS_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/sporosalibacterium_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1106_SPOROSALIBACTERIUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/dialister_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1107_DIALISTER_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/chopped_meat_medium_with_carbohydrates.yaml` | `data/normalized_yaml/bacterial/KOMODO_110_CHOPPED_MEAT_medium_WITH_CARBOHYDRATES.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/carboxymethyl_cellulose_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1111_CARBOXYMETHYL_CELLULOSE_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/calditerrivibrio_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1112_CALDITERRIVIBRIO_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/thiofaba_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1114_THIOFABA_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/steroidobacter_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1116_STEROIDOBACTER_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/pys_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1117_PYS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/md1_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1118_MD1-MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/gnys_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1119_GNYS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/beijerinckia_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_111_BEIJERINCKIA_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/pyse_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1120_PYSE_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/yed_medium_salted.yaml` | `data/normalized_yaml/bacterial/KOMODO_1123_YED_medium_salted.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/hd_1_10_diluted.yaml` | `data/normalized_yaml/bacterial/KOMODO_1124_HD_1_10_diluted.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/tpt_18_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1127_TPT_18_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/rhodovulum_visakhum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1128_RHODOVULUM_VISAKHUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/re_101_102_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1130_RE-101_102_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/lc_2.yaml` | `data/normalized_yaml/bacterial/KOMODO_1132_LC_2.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/enriched_cytophaga_agar_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1133_ENRICHED_CYTOPHAGA_AGAR_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/rhodovulum_kholense_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1136_RHODOVULUM_KHOLENSE_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/rubritalea_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1137_RUBRITALEA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/halopiger_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1138_HALOPIGER_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/pyg_medium_b.yaml` | `data/normalized_yaml/bacterial/KOMODO_1139_PYG_medium_B.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/pyg_medium_e.yaml` | `data/normalized_yaml/bacterial/KOMODO_1140_PYG_medium_E.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/rhodoblastus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1142_RHODOBLASTUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/ty_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1143_TY_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/singulisphaera_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1144_SINGULISPHAERA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/ms_medium_modified.yaml` | `data/normalized_yaml/bacterial/KOMODO_1145_MS-MEDIUM_MODIFIED.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/venenivibrio_stagnispumantis_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1146_VENENIVIBRIO_STAGNISPUMANTIS_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/oceanithermus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1149_OCEANITHERMUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/paracoccus_halodenitrificans_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_114_PARACOCCUS_HALODENITRIFICANS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/r3_a_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1153_R3_A_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/pyem_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1157_PYEM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/gym_streptomyces_medium_10_nacl.yaml` | `data/normalized_yaml/bacterial/KOMODO_1159_GYM_STREPTOMYCES_medium_10_NACL.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/payne_seghal_gibbons_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1160_PAYNE_SEGHAL_GIBBONS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/dubos_salts_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1161_DUBOS_SALTS_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/thiophaeococcus_mangrovi_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1162_THIOPHAEOCOCCUS_MANGROVI_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/halomicrobium_katesii_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1164_HALOMICROBIUM_KATESII_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/spirochaeta_americana_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1165_SPIROCHAETA_AMERICANA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/nsy_medium_for_polynucleobacter.yaml` | `data/normalized_yaml/bacterial/KOMODO_1167_NSY-MEDIUM_FOR_POLYNUCLEOBACTER.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/yps_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1168_YPS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/seawater_ypg.yaml` | `data/normalized_yaml/bacterial/KOMODO_1169_SEAWATER_YPG.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/DSMZ_1170_METHYLONATRUM_MEDIUM.yaml` | `data/normalized_yaml/bacterial/KOMODO_1170_METHYLONATRUM_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/methylohalomonas_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1171_METHYLOHALOMONAS_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/modified_medium_514.yaml` | `data/normalized_yaml/bacterial/KOMODO_1173_MODIFIED_medium_514.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/alkaliflexus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1175_ALKALIFLEXUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/halovibrio_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1176_HALOVIBRIO_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/rubitelea_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1177_RUBITELEA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/aquincola_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1178_AQUINCOLA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/methylomicrobium_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1180_METHYLOMICROBIUM_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/methylocella_silverstris_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1181_METHYLOCELLA_SILVERSTRIS_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/aquisalimonas_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1182_AQUISALIMONAS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/roseicyclus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1183_ROSEICYCLUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/smb_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1185_SMB_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/granulibacter_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1186_GRANULIBACTER_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/anoyxnatronum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1187_ANOYXNATRONUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/aerobic_sulfolobales_medium_without_sulfur.yaml` | `data/normalized_yaml/bacterial/KOMODO_1189_AEROBIC_SULFOLOBALES_medium_WITHOUT_SULFUR.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/dap_nutrient_agar.yaml` | `data/normalized_yaml/bacterial/KOMODO_118_DAP-NUTRIENT_AGAR.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/eggc.yaml` | `data/normalized_yaml/bacterial/KOMODO_1191_EGGC.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/bm_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1192_BM_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/halorubrum_californiense_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1194_HALORUBRUM_CALIFORNIENSE_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/kushneria_aurantia_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1195_KUSHNERIA_AURANTIA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/zavarzinella_formosa_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1196_ZAVARZINELLA_FORMOSA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/rhodobacter_thiocapsa_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1197_RHODOBACTER_THIOCAPSA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/k7_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1199_K7_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/anaeromyxobacter_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1200_ANAEROMYXOBACTER-MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/alicyclobacillus_ferrooxydans_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1201_ALICYCLOBACILLUS_FERROOXYDANS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/fastidious_anaerobe_agar.yaml` | `data/normalized_yaml/bacterial/KOMODO_1203_FASTIDIOUS_ANAEROBE_AGAR.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/caldanaerovirga_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1206_CALDANAEROVIRGA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/tge.yaml` | `data/normalized_yaml/bacterial/KOMODO_1207_TGE.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/bacillus_alkalidiazotrophicus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1208_BACILLUS_ALKALIDIAZOTROPHICUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/alicycobacillus_pohliae_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1209_ALICYCOBACILLUS_POHLIAE_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/caldisericum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1211_CALDISERICUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/thalassobacillus_cyri_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1213_THALASSOBACILLUS_CYRI_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/halorubrum_choaviator_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1214_HALORUBRUM_CHOAVIATOR_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/beijerinckia_doebereinerae_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1215_BEIJERINCKIA_DOEBEREINERAE_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/salinisphaera_hydrothermalis_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1216_SALINISPHAERA_HYDROTHERMALIS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/roseococcus_suduntuyensis_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1217_ROSEOCOCCUS_SUDUNTUYENSIS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/roseinatronobacter_monicus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1218_ROSEINATRONOBACTER_MONICUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/methylovirgula_ligni_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1219_METHYLOVIRGULA_LIGNI_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/acidosoma_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1220_ACIDOSOMA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/salisaeta_longa_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1221_SALISAETA_LONGA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/rhodovulum_marinum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1222_RHODOVULUM_MARINUM_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/ectothiorhodospira_variabilis_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1224_ECTOTHIORHODOSPIRA_VARIABILIS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/thiohalocapsa_marina_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1226_THIOHALOCAPSA_MARINA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/rhodobaca_barguzinensis_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1227_RHODOBACA_BARGUZINENSIS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/thioalkalivibrio_thiocyanodenitrificans_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1228_THIOALKALIVIBRIO_THIOCYANODENITRIFICANS_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/haloplasma_contractile_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1231_HALOPLASMA_CONTRACTILE_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/xylan_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1235_XYLAN_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/woodsholea_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1238_WOODSHOLEA_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/desulfurispirillum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1239_DESULFURISPIRILLUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/starch_mineral_salt_agar_10_nacl.yaml` | `data/normalized_yaml/bacterial/KOMODO_1240_STARCH-MINERAL_SALT-AGAR_10_NACL.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/algoriphagus_alkaliphilus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1242_ALGORIPHAGUS_ALKALIPHILUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/schlesneria_paludicola_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1244_SCHLESNERIA_PALUDICOLA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/oteb_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1245_OTEB-MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/tyb.yaml` | `data/normalized_yaml/bacterial/KOMODO_1247_TYB.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/desulfosporosinus_acidophilus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1250_DESULFOSPOROSINUS_ACIDOPHILUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/caldinitratiruptor_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1251_CALDINITRATIRUPTOR_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/kistimonas_asteriae_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1252_KISTIMONAS_ASTERIAE_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/thermovenabulum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1255_THERMOVENABULUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/methanocella_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1257_METHANOCELLA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/methylobacterium_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_125_METHYLOBACTERIUM_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/spirochaeta_dissipatitropha_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1263_SPIROCHAETA_DISSIPATITROPHA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/spirochaeta_sp_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1264_SPIROCHAETA_SP._medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/bacteroides_galacturonicus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1265_BACTEROIDES_GALACTURONICUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/mycobacterium_intracellulare_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_126_MYCOBACTERIUM_INTRACELLULARE_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/b12_medium_guttman.yaml` | `data/normalized_yaml/bacterial/KOMODO_1270_B12_-_MEDIUM_GUTTMAN.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/thioalkalivibrio_jannaschi.yaml` | `data/normalized_yaml/bacterial/KOMODO_1272_THIOALKALIVIBRIO_JANNASCHI.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/methanospirillum_lacunae_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1273_METHANOSPIRILLUM_LACUNAE_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/georgfuchsia_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1275_GEORGFUCHSIA_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/micromonospora_megalomicea_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_127_MICROMONOSPORA_MEGALOMICEA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/sh_seawater_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1282_SH_SEAWATER_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/kr_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1283_KR_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/granulicella_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1284_GRANULICELLA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/rhizomicrobium_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1288_RHIZOMICROBIUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/alcanivorax_balericus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1289_ALCANIVORAX_BALERICUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/thermosipho_affectus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1299_THERMOSIPHO_AFFECTUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/soil_extract_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_12_SOIL_EXTRACT_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/tepidanaerobacter_acetatoxydans_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1301_TEPIDANAEROBACTER_ACETATOXYDANS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/yim_medium_10_nacl.yaml` | `data/normalized_yaml/bacterial/KOMODO_1302_YIM_medium_10_NaCl.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/sulfuritalea_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1304_SULFURITALEA_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/mmn.yaml` | `data/normalized_yaml/bacterial/KOMODO_1305_MMN.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/deinococcus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1306_DEINOCOCCUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/bacillus_mucilaginosus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1307_BACILLUS_MUCILAGINOSUS_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/py4s.yaml` | `data/normalized_yaml/bacterial/KOMODO_1308_PY4S.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/bacillus_locisalis_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1309_BACILLUS_LOCISALIS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/methanocella_conradii_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1318_METHANOCELLA_CONRADII_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/half_strength_r2a_medium_in_75_seawater.yaml` | `data/normalized_yaml/bacterial/KOMODO_1320_HALF_STRENGTH_R2A_MEDIUM_IN_75_SEAWATER.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/methylocapsa_aurea_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1323_METHYLOCAPSA_AUREA_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/modified_methylobacterium_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1324_MODIFIED_METHYLOBACTERIUM_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/paracoccus_bogoriensis_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1325_PARACOCCUS_BOGORIENSIS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/aurantimonas_manganoxydans_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1326_AURANTIMONAS_MANGANOXYDANS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/larkinella_arboricola_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1327_LARKINELLA_ARBORICOLA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/defluviitoga_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1328_DEFLUVIITOGA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/methanosaeta_pelagica_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1329_METHANOSAETA_PELAGICA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/asaia_gyp_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1330_ASAIA_GYP_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/algoriphagus_aquaeductus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1332_ALGORIPHAGUS_AQUAEDUCTUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/flb_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1333_FLB_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/modified_yma_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1334_MODIFIED_YMA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/min_e_methyloversatilis_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1341_MIN_E_-_METHYLOVERSATILIS_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/tistlia_consotensis_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1343_TISTLIA_CONSOTENSIS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/haliscomenobacter_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_134_HALISCOMENOBACTER_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/fuchsiella_alkaliacetigena_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1352_FUCHSIELLA_ALKALIACETIGENA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/mineral_lactate_medium_low_carbon_content.yaml` | `data/normalized_yaml/bacterial/KOMODO_137_MINERAL_LACTATE_MEDIUM_low_carbon_content.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/s_heliorestis_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1381_S_HELIORESTIS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/lindane_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_138_LINDANE_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/haloarchaeal_medium_mh_1.yaml` | `data/normalized_yaml/bacterial/KOMODO_1396_HALOARCHAEAL_medium_MH-1.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/1_10_pygv_medium_modified.yaml` | `data/normalized_yaml/bacterial/KOMODO_1398_1_10_PYGV_medium_modified.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/bacillus_acidocaldarius_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_13_BACILLUS_ACIDOCALDARIUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/methylorosula_medium_v_022.yaml` | `data/normalized_yaml/bacterial/KOMODO_1403_METHYLOROSULA_MEDIUM_V-022.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/methylocystis_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1409_METHYLOCYSTIS_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/mst_medium_autotrophic_growth.yaml` | `data/normalized_yaml/bacterial/KOMODO_1416_MST-MEDIUM_AUTOTROPHIC_GROWTH.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/sse_hd_1_10_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1426_SSE_HD_1_10_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/alkalispirillum_mobile_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1446_ALKALISPIRILLUM_MOBILE_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/deferrisoma_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1451_DEFERRISOMA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/alcalilimnicola_ehrlichii_mhle_1_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_1457_ALCALILIMNICOLA_EHRLICHII_MHLE-1_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/halococcus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_146_HALOCOCCUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/ruminobacter_amylophilus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_147_RUMINOBACTER_AMYLOPHILUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/nicotinic_acid_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_152_NICOTINIC_ACID_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/beggiatoa_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_155_BEGGIATOA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/cytophaga_hutchinsonii_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_160_CYTOPHAGA_HUTCHINSONII_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/hyphomicrobium_strain_x_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_166_HYPHOMICROBIUM_STRAIN_X_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/sporocytophaga_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_167_SPOROCYTOPHAGA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/selenomonas_ruminantium_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_181_SELENOMONAS_RUMINANTIUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/trichococcus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_183_TRICHOCOCCUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/medium_for_osmophilic_fungi_m_40_y.yaml` | `data/normalized_yaml/bacterial/KOMODO_187_medium_FOR_OSMOPHILIC_FUNGI_M_40_Y.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/chaetomium_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_188_CHAETOMIUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/oat_flake_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_189_OAT_FLAKE_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/ypss_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_190_YpSs_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/corn_meal_agar.yaml` | `data/normalized_yaml/bacterial/KOMODO_191_CORN_MEAL_AGAR.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/pilobolus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_192_PILOBOLUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/desulfonema_magnum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_202_DESULFONEMA_MAGNUM_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/eubacterium_lentum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_209_EUBACTERIUM_LENTUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/haloanaerobium_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_210_HALOANAEROBIUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/synthrophomonas_medium_sulfate_free.yaml` | `data/normalized_yaml/bacterial/KOMODO_213_SYNTHROPHOMONAS_medium_-SULFATE_FREE.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/gym_s_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_214_GYM_S_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/bhi_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_215_BHI_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/bhi_1_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_216_BHI_1_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/bhi_2_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_217_BHI_2_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/bhi_3_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_218_BHI_3_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/mycobacterium_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_219_MYCOBACTERIUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/sarcina_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_21_SARCINA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/azospirillum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_221_AZOSPIRILLUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/sp_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_222_SP_-_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/polyangium_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_223_POLYANGIUM_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/aureobacterium_terregens_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_226_AUREOBACTERIUM_TERREGENS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/corynebacterium_medium_with_salt.yaml` | `data/normalized_yaml/bacterial/KOMODO_229_CORYNEBACTERIUM_medium_WITH_SALT.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/pediococcus_damnosus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_231_PEDIOCOCCUS_DAMNOSUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/mrs_medium_with_cysteine.yaml` | `data/normalized_yaml/bacterial/KOMODO_232_MRS_medium_WITH_CYSTEINE.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/enb_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_237_ENB_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/streptomycin_nutrient_agar.yaml` | `data/normalized_yaml/bacterial/KOMODO_238_STREPTOMYCIN_NUTRIENT_AGAR.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/diethyl_phosphonate_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_239_DIETHYL_PHOSPHONATE_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/corynebacterium_medium_with_blood.yaml` | `data/normalized_yaml/bacterial/KOMODO_240_CORYNEBACTERIUM_medium_WITH_BLOOD.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/bmm_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_242_BMM_-_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/blood_agar_ii.yaml` | `data/normalized_yaml/bacterial/KOMODO_245_BLOOD_AGAR_II.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/sea_water_agar.yaml` | `data/normalized_yaml/bacterial/KOMODO_246_SEA_WATER_AGAR.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/peptone_meat_extract_glycerol_agar.yaml` | `data/normalized_yaml/bacterial/KOMODO_250_Peptone_MEAT_EXTRACT_GLYCEROL_AGAR.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/peptone_meat_extract_soil_extract_agar_pfe.yaml` | `data/normalized_yaml/bacterial/KOMODO_251_Peptone_-_MEAT_EXTRACT_-_SOIL_EXTRACT_AGAR_PFE.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/starch_mineral_salt_agar_stms.yaml` | `data/normalized_yaml/bacterial/KOMODO_252_STARCH_-_MINERAL_salt_-_AGAR_STMS.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/medium_for_ectothiorhodospira.yaml` | `data/normalized_yaml/bacterial/KOMODO_253_medium_FOR_ECTOTHIORHODOSPIRA.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/acetobacter_peroxydans_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_254_ACETOBACTER_PEROXYDANS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/rhodopseudomonas_globiformis_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_25_RHODOPSEUDOMONAS_GLOBIFORMIS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/bacillus_schlegelii_heterotrophic_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_260_BACILLUS_SCHLEGELII_HETEROTROPHIC_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/j_agar.yaml` | `data/normalized_yaml/bacterial/KOMODO_262_J_-_AGAR.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/tomato_juice_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_264_TOMATO_JUICE_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/thermofilum_pendens_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_265_THERMOFILUM_PENDENS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/thermococcus_celer_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_266_THERMOCOCCUS_CELER_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/ginger_beer_plant_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_267_GINGER_BEER_PLANT_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/tea_fungus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_268_TEA_FUNGUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/acid_rhodospirillaceae_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_26_ACID_RHODOSPIRILLACEAE_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/rhodospirillaceae_medium_modified.yaml` | `data/normalized_yaml/bacterial/KOMODO_27_RHODOSPIRILLACEAE_medium_modified.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/hyphomonas_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_281_HYPHOMONAS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/clostridium_aminobutyricum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_286_CLOSTRIDIUM_AMINOBUTYRICUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/acidaminobacter_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_292_ACIDAMINOBACTER_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/ruminococcus_pasteurii_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_300_RUMINOCOCCUS_PASTEURII_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/falcivibrio_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_301_FALCIVIBRIO_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/nutrient_broth_with_10_horse_serum.yaml` | `data/normalized_yaml/bacterial/KOMODO_302_NUTRIENT_BROTH_WITH_10_HORSE_SERUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/simonsiella_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_303_SIMONSIELLA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/bacillus_thermoglucosidasius_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_305_BACILLUS_THERMOGLUCOSIDASIUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/ny_agar.yaml` | `data/normalized_yaml/bacterial/KOMODO_306_NY-AGAR.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/vibrio_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_308_VIBRIO_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/neomycin_agar.yaml` | `data/normalized_yaml/bacterial/KOMODO_309_NEOMYCIN_AGAR.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/v_8_juice_agar.yaml` | `data/normalized_yaml/bacterial/KOMODO_310_V-8_JUICE_AGAR.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/scy_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_312_SCY_-_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/ilyobacter_polytropus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_314_ILYOBACTER_POLYTROPUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/bacteroides_cellulosolvens_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_315_BACTEROIDES_CELLULOSOLVENS_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/alkaline_nutrient_agar.yaml` | `data/normalized_yaml/bacterial/KOMODO_31_ALKALINE_NUTRIENT_AGAR.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/clostridium_cellulovorans_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_320_CLOSTRIDIUM_CELLULOVORANS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/pyg_medium_with_volatile_fatty_acids.yaml` | `data/normalized_yaml/bacterial/KOMODO_328_PYG_medium_WITH_VOLATILE_FATTY_ACIDS.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/rumen_bacteria_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_330_RUMEN_BACTERIA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/eubacterium_oxidoreducens_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_335_EUBACTERIUM_OXIDOREDUCENS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/syntrophococcus_sucromutans_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_337_SYNTROPHOCOCCUS_SUCROMUTANS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/campylobacter_rectus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_338_CAMPYLOBACTER_RECTUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/capnocytophaga_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_340_CAPNOCYTOPHAGA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/methanobacterium_alcaliphilum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_342_METHANOBACTERIUM_ALCALIPHILUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/caryophanon_latum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_34_CARYOPHANON_LATUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/rhodobacter_adriaticus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_351_RHODOBACTER_ADRIATICUS_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/azospirillum_amazonense_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_352_AZOSPIRILLUM_AMAZONENSE_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/l_wenstein_jensen_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_354_L_WENSTEIN-JENSEN_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/thiosphaera_pantotropha_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_356_THIOSPHAERA_PANTOTROPHA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/flexibacter_canadensis_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_357_FLEXIBACTER_CANADENSIS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/gfy_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_359_GFY_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/ypm_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_360_YPM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/flavobacterium_tirrenicum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_362_FLAVOBACTERIUM_TIRRENICUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/phenylobacterium_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_363_PHENYLOBACTERIUM_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/pyea_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_364_PYEA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/pseudomonas_indigofera_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_365_PSEUDOMONAS_INDIGOFERA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/kunkee_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_368_KUNKEE_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/bacillus_tusciae_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_369_BACILLUS_TUSCIAE_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/heliobacterium_chlorum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_370_HELIOBACTERIUM_CHLORUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/natronobacteria_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_371_NATRONOBACTERIA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/halobacteria_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_372_HALOBACTERIA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/methanospirillum_sk_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_374_METHANOSPIRILLUM_SK_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/methanohalobium_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_375_METHANOHALOBIUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/an1_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_376_AN1_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/arthrobacter_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_378_ARTHROBACTER_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/mineral_medium_m9_for_e_coli_jm_strains.yaml` | `data/normalized_yaml/bacterial/KOMODO_382_MINERAL_MEDIUM_M9_for_E._coli_JM_strains.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/dictyoglomus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_388_DICTYOGLOMUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/pyrobaculum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_390_PYROBACULUM_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/baf_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_392_BAF_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/ypd_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_393_YPD_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/chi_1776_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_394_CHI_1776_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/ferulate_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_397_FERULATE_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/archaeoglobus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_399_ARCHAEOGLOBUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/azotobacter_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_3_AZOTOBACTER_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/sp2_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_405_SP2_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/pfennigs_medium_ii_with_salt.yaml` | `data/normalized_yaml/bacterial/KOMODO_40_PFENNIG_S_MEDIUM_II_WITH_SALT.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/acetomicrobium_faecalis_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_412_ACETOMICROBIUM_FAECALIS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/btu_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_413_BTU_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/allantoin_mineral_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_6_ALLANTOIN_MINERAL_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/ancylobacter_spirosoma_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_7_ANCYLOBACTER_-_SPIROSOMA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/bacillus_racemilacticus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_8_BACILLUS_RACEMILACTICUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/tryptone_thioglycolate_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_48_TRYPTONE_THIOGLYCOLATE_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/c_10_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_49_C_10_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/sphaerotilus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_51_SPHAEROTILUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/corynebacterium_agar.yaml` | `data/normalized_yaml/bacterial/KOMODO_53_CORYNEBACTERIUM_AGAR.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/fructose_mineral_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_55_FRUCTOSE_MINERAL_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/trypticase_starch_agar.yaml` | `data/normalized_yaml/bacterial/KOMODO_56_TRYPTICASE_STARCH_AGAR.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/aam_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_57_AAM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/leuconostoc_oenos_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_59_LEUCONOSTOC_OENOS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/gym_streptomyces_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_65_GYM_STREPTOMYCES_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/cy_agar.yaml` | `data/normalized_yaml/bacterial/KOMODO_67_CY-AGAR.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/trypticase_phytone_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_75_TRYPTICASE_PHYTONE_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/leucothrix_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_79_LEUCOTHRIX_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/glycerol_soil_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_80_GLYCEROL-SOIL_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/bhi_glucose_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_82_BHI-GLUCOSE_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/rolled_oats_mineral_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_84_ROLLED_OATS_MINERAL_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/glucose_peptone_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_85_GLUCOSE_Peptone_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/castenholz_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_86_CASTENHOLZ_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/propionibacterium_agar.yaml` | `data/normalized_yaml/bacterial/KOMODO_91_PROPIONIBACTERIUM_AGAR.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/lactobacillus_medium_ii.yaml` | `data/normalized_yaml/bacterial/KOMODO_93_LACTOBACILLUS_medium_II.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/halobacterium_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_97_HALOBACTERIUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/rhizobium_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_98_RHIZOBIUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/acidaminococcus_fermentans_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_414_ACIDAMINOCOCCUS_FERMENTANS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/oxalobacter_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_419_OXALOBACTER_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/blood_agar_i.yaml` | `data/normalized_yaml/bacterial/KOMODO_420_BLOOD_AGAR_I.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/chromatium_salexigens_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_421_CHROMATIUM_SALEXIGENS_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/amoebobacter_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_422_AMOEBOBACTER_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/xenorhabdus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_423_XENORHABDUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/oatmeal_agar.yaml` | `data/normalized_yaml/bacterial/KOMODO_425_OATMEAL_AGAR.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/organic_medium_79.yaml` | `data/normalized_yaml/bacterial/KOMODO_426_ORGANIC_medium_79.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/mykorrhiza_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_427_MYKORRHIZA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/columbia_blood_agar.yaml` | `data/normalized_yaml/bacterial/KOMODO_429_COLUMBIA_BLOOD_AGAR.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/halobacteroides_acetoethylicus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_432_HALOBACTEROIDES_ACETOETHYLICUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/marinococcus_albus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_434_MARINOCOCCUS_ALBUS_-_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/kdm_2_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_435_KDM-2_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/ruminococcus_albus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_436_RUMINOCOCCUS_ALBUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/mitsuokella_dentalis_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_437_MITSUOKELLA_DENTALIS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/bordet_gengou_medium_difco.yaml` | `data/normalized_yaml/bacterial/KOMODO_438_BORDET-GENGOU-MEDIUM_DIFCO.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/casman_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_439_CASMAN-MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/m17_medium_for_lactic_streptococci.yaml` | `data/normalized_yaml/bacterial/KOMODO_449_M17_medium_FOR_LACTIC_STREPTOCOCCI.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/supplemented_arginine_m9_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_450_SUPPLEMENTED_ARGININE_M9_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/glucose_medium_nakayama.yaml` | `data/normalized_yaml/bacterial/KOMODO_452_GLUCOSE_medium_NAKAYAMA.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/standard_i_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_453_STANDARD_I_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/eba_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_454_EBA_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/kpl_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_456_KPL_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/sucrose_peptone_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_459_SUCROSE-Peptone-MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/nitrogen_free_medium_for_pseudomonas_stutzeri.yaml` | `data/normalized_yaml/bacterial/KOMODO_460_NITROGEN-FREE_medium_FOR_PSEUDOMONAS_STUTZERI.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/plate_count_agar.yaml` | `data/normalized_yaml/bacterial/KOMODO_464_PLATE_COUNT_AGAR.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/tsby_salt_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_466_TSBY_salt_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/ottow_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_467_OTTOW_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/exiguobacterium_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_468_EXIGUOBACTERIUM_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/ym_catalase_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_469_YM-CATALASE_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/pityrosporum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_472_PITYROSPORUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/medium_with_edta_as_carbon_source.yaml` | `data/normalized_yaml/bacterial/KOMODO_473_MEDIUM_WITH_EDTA_AS_CARBON_SOURCE.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/medium_with_polyhydroxybutyric_acid_as_carbon_source.yaml` | `data/normalized_yaml/bacterial/KOMODO_474_MEDIUM_WITH_POLYHYDROXYBUTYRIC_ACID_AS_CARBON_SOURCE.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/anaerobacter_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_482_ANAEROBACTER_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/acetohalobium_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_494_ACETOHALOBIUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/desulfohalobium_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_499_DESULFOHALOBIUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/fervidobacterium_islandicum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_501_FERVIDOBACTERIUM_ISLANDICUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/methanobacterium_espanolae_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_506_METHANOBACTERIUM_ESPANOLAE_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/pp_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_513_PP-MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/anaerocellum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_516_ANAEROCELLUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/archaeoglobus_profundus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_519_ARCHAEOGLOBUS_PROFUNDUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/desulfomonile_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_521_DESULFOMONILE_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/clostridium_chartatabidum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_523_CLOSTRIDIUM_CHARTATABIDUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/DSMZ_529_AMPHIBACILLUS_MEDIUM.yaml` | `data/normalized_yaml/bacterial/KOMODO_529_AMPHIBACILLUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/thioglycolate_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_530_THIOGLYCOLATE_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/sporulation_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_531_SPORULATION_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/trypticase_soy_broth_agar.yaml` | `data/normalized_yaml/bacterial/KOMODO_535_TRYPTICASE_SOY_BROTH_AGAR.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/herbaspirillum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_538_HERBASPIRILLUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/acetitomaculum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_540_ACETITOMACULUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/sulfurospirillum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_541_SULFUROSPIRILLUM_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/pennassay_g_thy_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_542_PENNASSAY_G-THY_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/nzcym_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_544_NZCYM-MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/lc_broth_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_546_LC_BROTH_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/isp_medium_4.yaml` | `data/normalized_yaml/bacterial/KOMODO_547_ISP_medium_4.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/cyc_medium_modified_following_cross_and_attwell_1973.yaml` | `data/normalized_yaml/bacterial/KOMODO_550_CYC-MEDIUM_modified_following_Cross_and_Attwell_1973.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/gphf_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_553_GPHF-MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/n_z_amine_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_554_N-Z-AMINE-MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/sporulation_agar_sa.yaml` | `data/normalized_yaml/bacterial/KOMODO_555_SPORULATION-AGAR_SA.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/tmbs4_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_559_TMBS4_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/z_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_563_Z_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/medium_125_with_methanol.yaml` | `data/normalized_yaml/bacterial/KOMODO_569_MEDIUM_125_WITH_METHANOL.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/DSMZ_572_GYE_-_MEDIUM.yaml` | `data/normalized_yaml/bacterial/KOMODO_572_GYE_-_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/thiothrix_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_573_THIOTHRIX_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/geobacter_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_579_GEOBACTER_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/glycerol_cornsteep_agar.yaml` | `data/normalized_yaml/bacterial/KOMODO_581_GLYCEROL_CORNSTEEP_AGAR.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/15_mh_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_582_15_MH_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/corynebacterium_medium_cii.yaml` | `data/normalized_yaml/bacterial/KOMODO_583_CORYNEBACTERIUM_medium_CII.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/thauera_aromatica_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_586_THAUERA_AROMATICA_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/xylophilus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_587_XYLOPHILUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/halobacteroides_halobius_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_588_HALOBACTEROIDES_HALOBIUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/halobacterium_lacusprofundii_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_589_HALOBACTERIUM_LACUSPROFUNDII_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/halobacteroides_haloincola_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_591_HALOBACTEROIDES_HALOINCOLA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/thermomicrobium_roseum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_592_THERMOMICROBIUM_ROSEUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/10_mh_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_593_10_MH_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/caulobacter_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_595_CAULOBACTER_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/blastococcus_aggregatus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_596_BLASTOCOCCUS_AGGREGATUS_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/salinivibrio_costicola_subsp_vallismortis_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_597_SALINIVIBRIO_COSTICOLA_SUBSP._VALLISMORTIS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/halovibrio_variabilis_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_598_HALOVIBRIO_VARIABILIS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/ancalomicrobium_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_603_ANCALOMICROBIUM_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/colby_and_zathman_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_606_COLBY_AND_ZATHMAN_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/bacillus_thermoalcalophilus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_610_BACILLUS_THERMOALCALOPHILUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/desulfovibrio_mg_1_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_615_DESULFOVIBRIO_MG-1_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/marinomonas_vaga_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_617_MARINOMONAS_VAGA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/tween_80a_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_618_TWEEN_80A_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/hyphomicrobium_methylovorum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_619_HYPHOMICROBIUM_METHYLOVORUM_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/2_mh_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_620_2_MH_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/thermococcus_litoralis_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_623_THERMOCOCCUS_LITORALIS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/mh_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_624_MH_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/seawater_lemco.yaml` | `data/normalized_yaml/bacterial/KOMODO_627_SEAWATER_LEMCO.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/DSMZ_628_MMB_MEDIUM.yaml` | `data/normalized_yaml/bacterial/KOMODO_628_MMB_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/staleys_maintenance_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_629_STALEY_S_MAINTENANCE_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/acetobacter_europaeus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_631_ACETOBACTER_EUROPAEUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/nms_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_632_NMS_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/isp_medium_2_with_5_nacl.yaml` | `data/normalized_yaml/bacterial/KOMODO_636_ISP_medium_2_WITH_5_NaCl.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/lactobacillus_medium_iii.yaml` | `data/normalized_yaml/bacterial/KOMODO_638_LACTOBACILLUS_medium_III.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/rabbit_blood_agar.yaml` | `data/normalized_yaml/bacterial/KOMODO_646_RABBIT_BLOOD_AGAR.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/clostridium_grantii_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_648_CLOSTRIDIUM_GRANTII_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/centenum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/r_8_a_h_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_651_R_8_A_H_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/peptone_succinate_agar.yaml` | `data/normalized_yaml/bacterial/KOMODO_653_Peptone-SUCCINATE_AGAR.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/spirillum_gracile_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_654_SPIRILLUM_GRACILE_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/pye_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_655_PYE_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/hickey_tresner_agar.yaml` | `data/normalized_yaml/bacterial/KOMODO_658_HICKEY-TRESNER-AGAR.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/m17_medium_modified.yaml` | `data/normalized_yaml/bacterial/KOMODO_659_M17_medium_modified.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/alcaligenes_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_660_ALCALIGENES_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/dp_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_661_DP_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/yepg_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_662_YEPG_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/sulfobacillus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_665_SULFOBACILLUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/succiniclasticum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_666_SUCCINICLASTICUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/DSMZ_668_FLEXIBACTER_MEDIUM.yaml` | `data/normalized_yaml/bacterial/KOMODO_668_FLEXIBACTER_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/cytophaga_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_669_CYTOPHAGA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/half_strength_nutrient_broth_or_agar.yaml` | `data/normalized_yaml/bacterial/KOMODO_672_HALF_STRENGTH_NUTRIENT_BROTH_OR_AGAR.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/thermococcus_profundus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_673_THERMOCOCCUS_PROFUNDUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/tga_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_681_TGA-MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/anaerobranca_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_685_ANAEROBRANCA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/ace_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_689_ACE_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/dma_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_690_DMA_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/credm1_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_691_CreDm1_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/columbia_blood_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_693_COLUMBIA_BLOOD_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/medium_e_2.yaml` | `data/normalized_yaml/bacterial/KOMODO_694_MEDIUM_E-2.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/medium_for_erythrobacter_longus.yaml` | `data/normalized_yaml/bacterial/KOMODO_695_medium_FOR_ERYTHROBACTER_LONGUS.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/streptococcus_suis_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_696_STREPTOCOCCUS_SUIS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/todd_hewitt_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_697_TODD-HEWITT_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/doepel_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_698_DOEPEL_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/triple_sugar_iron_medium_difco.yaml` | `data/normalized_yaml/bacterial/KOMODO_699_TRIPLE-SUGAR-IRON_medium_Difco.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/haloanaerobacter_chitinovorans_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_701_HALOANAEROBACTER_CHITINOVORANS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/halocella_cellulolytica_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_702_HALOCELLA_CELLULOLYTICA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/semisolid_brucella_broth.yaml` | `data/normalized_yaml/bacterial/KOMODO_703_SEMISOLID_BRUCELLA_BROTH.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/butyrivibrio_sp_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_704_BUTYRIVIBRIO_SP._medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/pseudobutyrivibrio_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_712_PSEUDOBUTYRIVIBRIO_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/columbia_agar.yaml` | `data/normalized_yaml/bacterial/KOMODO_715_COLUMBIA_AGAR.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/desulfitobacterium_pce_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_717_DESULFITOBACTERIUM_PCE_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/anaerofilum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_719_ANAEROFILUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/rhizomonas_suberifaciens_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_726_RHIZOMONAS_SUBERIFACIENS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/desulfobacca_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_728_DESULFOBACCA_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/myx_agar.yaml` | `data/normalized_yaml/bacterial/KOMODO_729_MYX_AGAR.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/sulfitobacter_pontiacus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_733_SULFITOBACTER_PONTIACUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/rich_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_736_RICH_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/dpm_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_737_DPM_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/bphd_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_738_BPHD_Medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/desulfonema_ishimotoi_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_739_DESULFONEMA_ISHIMOTOI_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/desulfonatronovibrio_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_742_DESULFONATRONOVIBRIO_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/rhodobium_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_745_RHODOBIUM_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/rhodovulum_strictum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_746_RHODOVULUM_STRICTUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/dsic_medium_modified.yaml` | `data/normalized_yaml/bacterial/KOMODO_747_DSIC_medium_modified.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/cens_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_748_CENS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/sc_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_751_SC_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/halomonas_pantelleriense.yaml` | `data/normalized_yaml/bacterial/KOMODO_752_HALOMONAS_PANTELLERIENSE.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/my_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_753_MY_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/halobacillus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_755_HALOBACILLUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/halothermothrix_orenii.yaml` | `data/normalized_yaml/bacterial/KOMODO_761_HALOTHERMOTHRIX_ORENII.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/halomonas_desiderata_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_762_HALOMONAS_DESIDERATA_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/bosea_thiooxidans_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_763_BOSEA_THIOOXIDANS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/haloanaerobium_lacusroseus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_764_HALOANAEROBIUM_LACUSROSEUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/thermococcus_chitinophagus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_766_THERMOCOCCUS_CHITINOPHAGUS_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/erythromicrobium_and_roseococcus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_767_ERYTHROMICROBIUM_AND_ROSEOCOCCUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/m17_medium_for_filomicrobium_fusiforme.yaml` | `data/normalized_yaml/bacterial/KOMODO_768_M17_MEDIUM_FOR_FILOMICROBIUM_FUSIFORME.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/clostridium_vincentii_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_769_CLOSTRIDIUM_VINCENTII_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/paracoccus_kocurii_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_773_PARACOCCUS_KOCURII_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/medium_for_paracoccus_aminophilus_and_p_aminovorans.yaml` | `data/normalized_yaml/bacterial/KOMODO_774_medium_FOR_PARACOCCUS_AMINOPHILUS_AND_P._AMINOVORANS.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/r_cw_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_775_R_-_CW_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/microlunatus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_776_MICROLUNATUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/capnocytophaga_ii_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_779_CAPNOCYTOPHAGA_II_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/middlebrook_medium_with_mycobactin.yaml` | `data/normalized_yaml/bacterial/KOMODO_780_MIDDLEBROOK_MEDIUM_WITH_MYCOBACTIN.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/dung_extract_agar.yaml` | `data/normalized_yaml/bacterial/KOMODO_781_DUNG_EXTRACT_AGAR.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/om_2_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_782_OM-2_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/natroniella_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_784_NATRONIELLA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/bogoriella_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_785_BOGORIELLA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/dilute_potato_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_789_DILUTE_POTATO_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/porphyrobacter_tepidarius_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_791_PORPHYROBACTER_TEPIDARIUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/moorella_glycerini_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_793_MOORELLA_GLYCERINI_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/modified_chopped_meat_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_797_MODIFIED_CHOPPED_MEAT_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/DSMZ_798_TINDALLIA_MEDIUM.yaml` | `data/normalized_yaml/bacterial/KOMODO_798_TINDALLIA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/sphaerotilus_leptothrix_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_803_SPHAEROTILUS-LEPTOTHRIX_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/haemophilus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_804_HAEMOPHILUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/methylobacterium_thiocyanatum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_805_METHYLOBACTERIUM_THIOCYANATUM_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/thermococcus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_806_THERMOCOCCUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/haloanaerobium_alcaliphilum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_807_HALOANAEROBIUM_ALCALIPHILUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/alcanivorax_borkumensis_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_809_ALCANIVORAX_BORKUMENSIS_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/skim_milk_glucose_agar.yaml` | `data/normalized_yaml/bacterial/KOMODO_810_SKIM_MILK_GLUCOSE_AGAR.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/methanobacterium_subterraneum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_814_METHANOBACTERIUM_SUBTERRANEUM_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/thermosphaera_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_817_THERMOSPHAERA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/chrysiogenes_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_818_CHRYSIOGENES_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/fundibacter_jadensis_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_821_FUNDIBACTER_JADENSIS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/halobaculum_gomorrense_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_823_HALOBACULUM_GOMORRENSE_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/nevskia_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_828_NEVSKIA_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/desulfurobacterium_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_829_DESULFUROBACTERIUM_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/pepton_corn_meal_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_831_PEPTON-CORN_MEAL_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/dehalospirillum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_833_DEHALOSPIRILLUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/coprothermobacter_platensis_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_834_COPROTHERMOBACTER_PLATENSIS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/desulfuromonas_palmitatis_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_837_DESULFUROMONAS_PALMITATIS_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/serpulina_murdochii_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_840_SERPULINA_MURDOCHII_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/msv_thiotrix_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_841_MSV-THIOTRIX-MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/haloanaerobacter_salinarius_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_842_HALOANAEROBACTER_SALINARIUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/rae_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_848_RAE_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/ae_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_849_AE_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/alternative_acetobacter_intermedius_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_850_ALTERNATIVE_ACETOBACTER_INTERMEDIUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/DSMZ_851_GLUCOSE_SULFIDE_MEDIUM.yaml` | `data/normalized_yaml/bacterial/KOMODO_851_GLUCOSE_SULFIDE_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/starch_nitrate_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_856_STARCH_NITRATE_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/lactobacillus_medium_iv.yaml` | `data/normalized_yaml/bacterial/KOMODO_859_LACTOBACILLUS_medium_IV.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/halothiobacillus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_864_HALOTHIOBACILLUS_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/rhodobacter_veldkampii_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_867_RHODOBACTER_VELDKAMPII_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/syntrophothermus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_870_SYNTROPHOTHERMUS_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/gym_seawater.yaml` | `data/normalized_yaml/bacterial/KOMODO_871_GYM_SEAWATER.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/papillibacter_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_872_PAPILLIBACTER_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/thermoanaerovibrio_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_873_THERMOANAEROVIBRIO_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/ferroplasma_acidiphilum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_874_FERROPLASMA_ACIDIPHILUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/desulfacinum_hydrothermale_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_875_DESULFACINUM_HYDROTHERMALE_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/luedemann_medium_luedemann_1968.yaml` | `data/normalized_yaml/bacterial/KOMODO_877_LUEDEMANN_medium_LUEDEMANN_1968.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/clostridium_ljungdahlii_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_879_CLOSTRIDIUM_LJUNGDAHLII_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/denitrovibrio_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_881_DENITROVIBRIO_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/tween_80_agar.yaml` | `data/normalized_yaml/bacterial/KOMODO_884_TWEEN_80-AGAR.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/phc_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_885_PHC_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/aquaspirillum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_888_AQUASPIRILLUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/methanocalculus_pumilus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_892_METHANOCALCULUS_PUMILUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/ts_agar.yaml` | `data/normalized_yaml/bacterial/KOMODO_893_TS_AGAR.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/bennetts_modified_medium_p_agrawal_unpublished.yaml` | `data/normalized_yaml/bacterial/KOMODO_894_BENNETT_S_MODIFIED_medium_P._AGRAWAL_UNPUBLISHED.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/anaerobranca_gottschalkii_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_895_ANAEROBRANCA_GOTTSCHALKII_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/acetobacterium_tundrae_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_900_ACETOBACTERIUM_TUNDRAE_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/acidolobus_aceticus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_901_ACIDOLOBUS_ACETICUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/pseudomonas_agar_f.yaml` | `data/normalized_yaml/bacterial/KOMODO_907_PSEUDOMONAS_AGAR_F.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/medium_for_chlorate_respirers.yaml` | `data/normalized_yaml/bacterial/KOMODO_908_MEDIUM_FOR_CHLORATE_RESPIRERS.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/treponema_denticola_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_909_TREPONEMA_DENTICOLA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/modified_cm_ye_medium_b.yaml` | `data/normalized_yaml/bacterial/KOMODO_910_MODIFIED_CM_YE_medium_B.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/middlebrock_7h11_agar.yaml` | `data/normalized_yaml/bacterial/KOMODO_911_MIDDLEBROCK_7H11_AGAR.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/thermotoga_petrophila_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_913_THERMOTOGA_PETROPHILA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/ptyg_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_914_PTYG-MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/modified_sea_water_agar.yaml` | `data/normalized_yaml/bacterial/KOMODO_917_MODIFIED_SEA_WATER_AGAR.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/thauera_mechernichi_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_918_THAUERA_MECHERNICHI_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/limnobacter_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_919_LIMNOBACTER_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/gluconacetobacter_johannae_and_g_azotocaptans_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_920_GLUCONACETOBACTER_JOHANNAE_AND_G._AZOTOCAPTANS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/methylosarcina_quisquillarum_and_m_fibrata_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_921_METHYLOSARCINA_QUISQUILLARUM_AND_M._FIBRATA_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/methylocapsa_acidophila_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_922_METHYLOCAPSA_ACIDOPHILA_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/alkalibacterium_olivapovliticus.yaml` | `data/normalized_yaml/bacterial/KOMODO_923_ALKALIBACTERIUM_OLIVAPOVLITICUS.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/alkaliphilic_sulphur_respiring_strains_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_925_ALKALIPHILIC_SULPHUR_RESPIRING_STRAINS_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/alkaliphilic_thermococcus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_926_ALKALIPHILIC_THERMOCOCCUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/roseinatronobacter_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_928_ROSEINATRONOBACTER_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/rhodovulum_iodosum_and_r_robiginosum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_929_RHODOVULUM_IODOSUM_AND_R._ROBIGINOSUM_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/natronincola_histidinovorans_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_930_NATRONINCOLA_HISTIDINOVORANS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/alcaliphilic_amphibacillus_strains_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_931_ALCALIPHILIC_AMPHIBACILLUS_STRAINS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/halonatronum_saccharophilum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_932_HALONATRONUM_SACCHAROPHILUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/haloanaerobium_congolense_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_933_HALOANAEROBIUM_CONGOLENSE_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/thermococcus_waiotapuense_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_934_THERMOCOCCUS_WAIOTAPUENSE_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/salinibacter_ruber_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_936_SALINIBACTER_RUBER_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/pyes_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_937_PYES_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/methylotrophic_arthrobacter_and_hyphomicrobium_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_939_METHYLOTROPHIC_ARTHROBACTER_AND_HYPHOMICROBIUM_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/horikoshi_alkaline.yaml` | `data/normalized_yaml/bacterial/KOMODO_940_HORIKOSHI_ALKALINE.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/medium_for_arhodomonas_and_marinobacter.yaml` | `data/normalized_yaml/bacterial/KOMODO_941_medium_FOR_ARHODOMONAS_AND_MARINOBACTER.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/pseudomonas_chlorotidismutans_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_944_PSEUDOMONAS_CHLOROTIDISMUTANS_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/nautilia_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_946_NAUTILIA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/oxoid_nutrient_broth.yaml` | `data/normalized_yaml/bacterial/KOMODO_948_OXOID_NUTRIENT_BROTH.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/methylophaga_sulfidovorans_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_951_METHYLOPHAGA_SULFIDOVORANS_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/1_10_nutrient_agar_no_2.yaml` | `data/normalized_yaml/bacterial/KOMODO_952_1_10_NUTRIENT_AGAR_NO.2.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/1_100_nutrient_agar_no_2.yaml` | `data/normalized_yaml/bacterial/KOMODO_953_1_100_NUTRIENT_AGAR_NO.2.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/medium_for_h_dombrowskii.yaml` | `data/normalized_yaml/bacterial/KOMODO_954_medium_FOR_H._DOMBROWSKII.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/ag_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_955_AG_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/medium_for_dsm_14457_and_14458.yaml` | `data/normalized_yaml/bacterial/KOMODO_956_MEDIUM_FOR_DSM_14457_AND_14458.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/microvirgula_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_957_MICROVIRGULA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/pelotomaculum_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_960_PELOTOMACULUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/thermovibrio_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_961_THERMOVIBRIO_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/thermoanaeromonas_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_963_THERMOANAEROMONAS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/r3_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_966_R3_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/marinobacter_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_970_MARINOBACTER_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/halomonas_magadiensis_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_971_HALOMONAS_MAGADIENSIS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/myct_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_972_MYCT_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/marinithermus_hydrothermalis_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_973_MARINITHERMUS_HYDROTHERMALIS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/1_2_ytss_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_974_1_2_YTSS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/oceanithermus_profundus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_975_OCEANITHERMUS_PROFUNDUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/methylophaga_alcalica_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_976_METHYLOPHAGA_ALCALICA_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/vulcanithermus_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_977_VULCANITHERMUS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/thermoactinomyces_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_978_THERMOACTINOMYCES_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/geothermobacter_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_981_GEOTHERMOBACTER_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/my10_12_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_982_MY10-12_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/DSMZ_983_ONR7a_MEDIUM.yaml` | `data/normalized_yaml/bacterial/KOMODO_983_ONR7a_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/acetic_acid_bacterium_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_989_ACETIC_ACID_BACTERIUM_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/DSMZ_990_YPS_MEDIUM.yaml` | `data/normalized_yaml/bacterial/KOMODO_990_YPS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/bacillus_filiformis_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_992_BACILLUS_FILIFORMIS_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/DSMZ_994_MINERAL_MEDIUM.yaml` | `data/normalized_yaml/bacterial/KOMODO_994_MINERAL_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/npb_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_995_NPB_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/medium_for_roseospira.yaml` | `data/normalized_yaml/bacterial/KOMODO_998_medium_FOR_ROSEOSPIRA.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/halorhodospira_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_999_HALORHODOSPIRA_medium.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/cys_medium_with_modified_nacl_concentration.yaml` | `data/normalized_yaml/bacterial/KOMODO_1108a_CYS_MEDIUM_WITH_MODIFIED_NACL_CONCENTRATION.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/phb_pyruvate_medium.yaml` | `data/normalized_yaml/bacterial/KOMODO_193a_PHB_PYRUVATE_MEDIUM.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/medium_for_chlorobium_ferrooxidans.yaml` | `data/normalized_yaml/bacterial/KOMODO_29a_MEDIUM_FOR_CHLOROBIUM_FERROOXIDANS.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/plates_with_fluoranthene.yaml` | `data/normalized_yaml/bacterial/KOMODO_462a_PLATES_WITH_FLUORANTHENE.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/reactivation_with_liquid_medium_464.yaml` | `data/normalized_yaml/bacterial/KOMODO_464a_REACTIVATION_WITH_LIQUID_medium_464.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/mineral_medium_with_2_hydroxybiphenyl.yaml` | `data/normalized_yaml/bacterial/KOMODO_465a_MINERAL_MEDIUM_WITH_2-HYDROXYBIPHENYL.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/bacterial/nutrient_agar_oxoid_cm3_with_phosphate.yaml` | `data/normalized_yaml/bacterial/KOMODO_605a_NUTRIENT_AGAR_OXOID_CM3_WITH_PHOSPHATE.yaml` | `SOURCE_DUPLICATE` |
| `data/normalized_yaml/fungal/potato_dextrose_agar.yaml` | `data/normalized_yaml/bacterial/KOMODO_129_POTATO_DEXTROSE_AGAR.yaml` | `SOURCE_DUPLICATE` |

These were selected because each KOMODO record explicitly states that its
composition was copied from the corresponding DSMZ medium number, and each
DSMZ parent record has the same medium number and matching ingredient and
concentration signature.

## Evidence From Local Records

- Macromonas medium: DSMZ Medium 847 and KOMODO Medium 847 share the same
  pH range, physical state, ingredients, and concentrations.
- Caldicoprobacter medium: DSMZ Medium 1233 and KOMODO Medium 1233 share the
  same liquid formulation, pH range, ingredients, and concentrations.
- Lentibacillus medium: DSMZ Medium 1449 and KOMODO Medium 1449 share the same
  solid formulation at pH 7.2, including 100 g/L NaCl and 20 g/L agar.
- Sporohalobacter lortetii medium: DSMZ Medium 319 and KOMODO Medium 319 share
  the same liquid formulation at pH 6.5. The KOMODO child additionally records
  NaOH as a variable pH-adjuster extracted from notes; this is treated as a
  pH-adjustment annotation, not a separate formulation.
- Thermus ruber medium: DSMZ Medium 256 and KOMODO Medium 256 share the same
  solid formulation at pH 8.0.
- Spirillum medium: DSMZ Medium 37 and KOMODO Medium 37 share the same liquid
  formulation at pH 6.8.
- AMB medium: DSMZ Medium 455 and KOMODO Medium 455 share the same liquid
  anaerobic formulation at pH 6.9.
- Caminicella medium: DSMZ Medium 964 and KOMODO Medium 964 share the same
  liquid formulation at pH 7.5.
- The ten additional DSMZ/KOMODO pairs for media 1000, 1001, 1002, 1003,
  1004, 1006, 1007, 1015, 1016, and 1018 were selected by exact local
  ingredient/concentration signature matching, a single matching DSMZ parent
  record, and KOMODO provenance notes that state the composition was copied
  from the corresponding DSMZ medium number.
- The twenty additional DSMZ/KOMODO pairs for media 101, 102, and 1021-1051
  were selected using the same exact local signature and provenance criteria.
- The twenty additional DSMZ/KOMODO pairs for media 105, 1052-1059, and
  1061-1085 were selected using the same exact local signature and provenance
  criteria.
- The twenty additional DSMZ/KOMODO pairs for media 10, 109, 110, and
  1086-1118 were selected using the same exact local signature and provenance
  criteria.
- The twenty additional DSMZ/KOMODO pairs for media 111, 1119-1120,
  1123-1124, 1127-1128, 1130, 1132-1133, 1136-1140, and 1142-1146 were
  selected using the same exact local signature and provenance criteria.
- The twenty additional DSMZ/KOMODO pairs for media 114, 1149, 1153,
  1157, 1159-1162, 1164-1171, 1173, and 1175-1178 were selected using
  the same exact local signature and provenance criteria.
- The twenty additional DSMZ/KOMODO pairs for media 118, 1180-1183,
  1185-1187, 1189, 1191-1192, 1194-1197, 1199-1201, 1203, and 1206
  were selected using the same exact local signature and provenance criteria.
- The twenty additional DSMZ/KOMODO pairs for media 1207-1209, 1211,
  1213-1222, 1224, 1226-1228, 1231, and 1235 were selected using the same
  exact local signature and provenance criteria.
- The twenty additional DSMZ/KOMODO pairs for media 125-126, 1238-1240,
  1242, 1244-1245, 1247, 1250-1252, 1255, 1257, 1263-1265, 1270, and
  1272-1273 were selected using the same exact local signature and provenance
  criteria.
- The twenty additional DSMZ/KOMODO pairs for media 12, 127, 1275,
  1282-1284, 1288-1289, 1299, 1301-1309, 1318, 1320, and 1323 were selected
  using the same exact local signature and provenance criteria.
- The twenty additional DSMZ/KOMODO pairs for media 13, 134, 137-138,
  1324-1330, 1332-1334, 1341, 1343, 1352, 1381, 1396, and 1398 were selected
  using the same exact local signature and provenance criteria.
- The twenty additional DSMZ/KOMODO pairs for media 146-147, 152, 155,
  160, 166-167, 181, 183, 187-190, 1403, 1409, 1416, 1426, 1446, 1451,
  and 1457 were selected using the same exact local signature and provenance
  criteria.
- The twenty additional DSMZ/KOMODO pairs for media 21, 191-192, 202,
  209-210, 213-219, 221-223, 226, 229, and 231-232 were selected using the
  same exact local signature and provenance criteria.
- The twenty additional DSMZ/KOMODO pairs for media 25, 237-240, 242,
  245-246, 250-254, 260, 262, and 264-268 were selected using the same exact
  local signature and provenance criteria.
- The twenty additional DSMZ/KOMODO pairs for media 26-27, 31, 281, 286,
  292, 300-303, 305-306, 308-310, 312, 314-315, 320, and 328 were selected
  using the same exact local signature and provenance criteria.
- The twenty additional DSMZ/KOMODO pairs for media 34, 330, 335, 337-338,
  340, 342, 351-352, 354, 356-357, 359-365, and 368-369 were selected using
  the same exact local signature and provenance criteria.
- The twenty additional DSMZ/KOMODO pairs for media 3, 40, 370-372,
  374-376, 378, 382, 388, 390, 392-394, 397, 399, 405, and 412-413 were
  selected using the same exact local signature and provenance criteria.
- The twenty additional same-category DSMZ/KOMODO pairs for media 6-8,
  48-49, 51, 53, 55-57, 59, 65, 67, 75, 79-80, 82, and 84-86 were selected
  using the same exact local signature and provenance criteria. A matching
  cross-category potato dextrose agar pair was left for separate review.
- The twenty additional same-category DSMZ/KOMODO pairs for media 91, 93,
  97-98, 414, 419-423, 425-427, 429, 432, and 434-438 were selected using the
  same exact local signature and provenance criteria.
- The forty additional same-category DSMZ/KOMODO pairs for media 439, 449-450,
  452-454, 456, 459-460, 464, 466-469, 472-474, 482, 494, 499, 501, 506,
  513, 516, 519, 521, 523, 529-531, 535, 538, 540-542, 544, 546-547,
  550, and 553 were selected using the same exact local signature and
  provenance criteria.
- The forty additional same-category DSMZ/KOMODO pairs for media 554-555,
  559, 563, 569, 572-573, 579, 581-583, 586-589, 591-593, 595-598, 603,
  606, 610, 615, 617-620, 623-624, 627-629, 631-632, 636, 638, and 646 were
  selected using the same exact local signature and provenance criteria.
- The forty additional same-category DSMZ/KOMODO pairs for media 648, 650-655,
  658-662, 665-666, 668-669, 672-673, 675, 681, 685, 689-699, 701-704,
  712, 715, 717, 719, 726, and 728 were selected using the same exact local
  signature and provenance criteria.
- The forty additional same-category DSMZ/KOMODO pairs for media 729, 733,
  736-739, 742, 745-748, 751-753, 755, 761-764, 766-769, 773-776, 779-782,
  784-785, 789, 791, 793, 797-798, and 803-804 were selected using the same
  exact local signature and provenance criteria.
- The forty additional same-category DSMZ/KOMODO pairs for media 805-807,
  809-810, 814, 817-818, 821, 823, 828-829, 831, 833-834, 837, 840-842,
  848-851, 856, 859, 864, 867, 870-875, 877, 879, 881, 884-885, 888, and
  892 were selected using the same exact local signature and provenance
  criteria.
- The forty additional same-category DSMZ/KOMODO pairs for media 893-895,
  900-901, 907-914, 917-923, 925-926, 928-934, 936-937, 939-941, 944, 946,
  948, and 951-954 were selected using the same exact local signature and
  provenance criteria.
- The final thirty-three same-category DSMZ/KOMODO pairs for media 955-957,
  960-961, 963, 966, 970-978, 981-983, 989-990, 992, 994-995, 998-999,
  1108a, 193a, 29a, 462a, 464a-465a, and 605a were selected using the same
  exact local signature and provenance criteria. A follow-up exact-signature
  scan found zero remaining unlinked same-category DSMZ/KOMODO candidates.
- The one cross-category exact DSMZ/KOMODO pair for medium 129 was selected
  after separate review: the DSMZ parent is categorized as `fungal`, the
  KOMODO child is categorized as `bacterial`, and the two records have the
  same DSMZ medium number, explicit KOMODO DSMZ provenance, and exact local
  formulation signature. A follow-up exact-signature scan found zero remaining
  unlinked DSMZ/KOMODO candidates under the single-parent exact-signature rule.

Broad `medium_*_modified_for_dsm_*` groups and multi-parent DSMZ source groups
were left unmodified in this batch because they require separate
source/formulation review.

## Validation

- Applied actions:
  - `add_variant_child`: 652
  - `add_parent_media`: 652
  - `set_variant_relationship`: 652
  - `add_variant_modification`: 652
- Targeted schema validation: 1304/1304 touched YAML files passed after normalizing
  one pre-existing `curation_history` key from `date` to `timestamp` in
  `KOMODO_319_SPOROHALOBACTER_LORTETII_medium.yaml`.
- Global parent/child link validation:
  - YAML records scanned: 15,827
  - Parent-to-child links: 2,197
  - Child-to-parent links: 2,197
  - Errors: 0
  - Warnings: 0
