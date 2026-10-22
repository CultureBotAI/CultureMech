# Stage 1 Discovery Ledger — Run `mech-goal-sequence-20261019`, Cycle 2, Stage 1 (`add_records`)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `2`
- **Stage**: `1` (`add_records` / `discover_add`)
- **Revision**: `1`
- **Source Revision**: `98c2c080ee1b68ab3961fbba0bd50cef81d458ef` (`origin/main`)
- **Skill Sources**:
  - `.claude/skills/culturemech-evolve-workflow/SKILL.md`
  - `.claude/skills/create-recipe/SKILL.md`
  - `.claude/skills/manage-identifiers/SKILL.md`
  - `.claude/skills/scrape-jcm-media/SKILL.md`

---

## 1. Bounded Frontier Definition

The bounded discovery frontier for Cycle 2 Stage 1 is the live RIKEN Japan Collection of Microorganisms (JCM) Growth Medium Database (`https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=<N>`) over the range **`GRMD = 1..1600`** (expanded from the previous `--scan-max 1500` ceiling in `scripts/import_jcm_grmd.py` to cover the `1501..1600` range as well as any previously skipped multi-table records in `1..1500`).

### Frontier Partition Summary (`GRMD = 1..1600`)

| Partition | Count | Disposition | Notes |
|---|---:|---|---|
| Previously represented via `jcm.grmd:<N>`, `mediadive.medium:J<N>`, or `TOGO` JCM URLs | `1,391` | `already-present` | Verified by `scripts/import_jcm_grmd.py::ingested_grmd_numbers()` prior to this pass |
| Unassigned / empty JCM GRMD slots (`< 1,000` bytes, no `<FONT SIZE=3>` heading) | `195` | `rejected-with-evidence` | `14` in `1..1299` (`3, 4, 5, 6, 8, 9, 10, 36, 71, 132, 234, 353, 450, 810`), `82` in `1300..1500`, and `99` in `1501..1600` (`1501..1502`, `1504..1600`) |
| Named JCM GRMD pages already represented in `data/normalized_yaml/` under `TOGO` / `MediaDive` | `9` | `already-present` | `GRMD = 41, 663, 1338, 1370, 1408, 1428, 1446, 1453, 1461` (detailed in Section 2) |
| Newly added JCM growth-media recipes (including `10` embedded stock-solution recipes) | `5` | `added` | `GRMD = 1422, 1476, 1483, 1492, 1503` -> `CultureMech:015916`..`CultureMech:015920` (detailed in Section 3) |
| **Total Evaluated Across Bounded Frontier (`1..1600`)** | **`1,600`** | **100% accounted** | Repeated frontier scan confirms `0` remaining missing media |

---

## 2. Candidate Evaluation Table (All 14 Named Un-Ingested Candidates in `1..1600`)

| Candidate (`GRMD`) | Source URL | Upstream Title | Classification | Existing / New `CultureMech` ID | Target File / Evidence |
|---:|---|---|---|---|---|
| `41` | `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=41` | `MARINE BROTH 2216` | `already-present` | `CultureMech:009718` / `CultureMech:008094` | Already represented by `data/normalized_yaml/bacterial/TOGO_M33_Marine_Broth_2216.yaml` and `JCM J193` (`Marine Broth 2216`, BD-Difco `37.4 g/L`). |
| `663` | `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=663` | `NUTRIENT BROTH` | `already-present` | `CultureMech:010086` | Already represented by `data/normalized_yaml/bacterial/TOGO_M681_Nutrient_Broth.yaml` (`Beef extract 3.0 g/L`, `Peptone 5.0 g/L`, pH `7.0`). |
| `1338` | `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1338` | `PYG MEDIUM (K)` | `already-present` | `CultureMech:009528` | Already represented by `data/normalized_yaml/bacterial/pyg_medium_k.yaml` (`TOGO M3010 / JCM Medium 1338`, citing `GRMD=1338`). |
| `1370` | `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1370` | `MODIFIED GAM AGAR WITH 5% HORSE BLOOD` | `already-present` | `CultureMech:009536` | Already represented by `data/normalized_yaml/bacterial/modified_gam_agar_with_5_horse_blood.yaml` (`TOGO M3025 / JCM Medium 1370`, citing `GRMD=1370`). |
| `1408` | `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1408` | `TMBS4 MEDIUM` | `already-present` | `CultureMech:009690` | Already represented by `data/normalized_yaml/bacterial/TOGO_M3270_Tmbs4_Medium.yaml` (`TOGO M3270 / JCM Medium 1408`, citing `GRMD=1408`). |
| `1422` | `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1422` | `METHANOCORPUSCULUM AGGREGANS MEDIUM` | `added` | `CultureMech:015916` | Added `data/normalized_yaml/archaea/JCM_J1422_METHANOCORPUSCULUM_AGGREGANS_MEDIUM.yaml` and `data/merge_yaml/merged/methanocorpusculum_aggregans_medium_jcm_1422.yaml`. |
| `1428` | `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1428` | `ALKALINE DILUTED AMS MEDIUM` | `already-present` | `CultureMech:009693` | Already represented by `data/normalized_yaml/bacterial/alkaline_diluted_ams_medium.yaml` (`TOGO M3279 / JCM Medium 1428`, citing `GRMD=1428`). |
| `1446` | `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1446` | `RCM BROTH` | `already-present` | `CultureMech:009696` | Already represented by `data/normalized_yaml/bacterial/rcm_broth.yaml` (`TOGO M3282 / JCM Medium 1446`, citing `GRMD=1446`). |
| `1453` | `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1453` | `PECTIN MEDIUM` | `already-present` | `CultureMech:009697` | Already represented by `data/normalized_yaml/bacterial/TOGO_M3283_Pectin_Medium.yaml` (`TOGO M3283 / JCM Medium 1453`, citing `GRMD=1453`). |
| `1461` | `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1461` | `MODIFIED GAM BROTH` | `already-present` | `CultureMech:009699` | Already represented by `data/normalized_yaml/bacterial/modified_gam_broth.yaml` (`TOGO M3285 / JCM Medium 1461`, citing `GRMD=1461`). |
| `1476` | `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1476` | `MODIFIED UREAPLASMA MEDIUM` | `added` | `CultureMech:015917` | Added `data/normalized_yaml/bacterial/JCM_J1476_MODIFIED_UREAPLASMA_MEDIUM.yaml` and `data/merge_yaml/merged/modified_ureaplasma_medium.yaml`. |
| `1483` | `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1483` | `AMMONIA OXIDIZING BACTERIA MEDIUM` | `added` | `CultureMech:015918` | Added `data/normalized_yaml/bacterial/JCM_J1483_AMMONIA_OXIDIZING_BACTERIA_MEDIUM.yaml` and `data/merge_yaml/merged/ammonia_oxidizing_bacteria_medium.yaml`. |
| `1492` | `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1492` | `BAP+ MEDIUM FOR FRANKIA` | `added` | `CultureMech:015919` | Added `data/normalized_yaml/bacterial/JCM_J1492_BAP_MEDIUM_FOR_FRANKIA.yaml` and `data/merge_yaml/merged/bap_medium_for_frankia_jcm_1492.yaml`. |
| `1503` | `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1503` | `AUTOTROPHIC NITROBACTER MEDIUM` | `added` | `CultureMech:015920` | Added `data/normalized_yaml/bacterial/JCM_J1503_AUTOTROPHIC_NITROBACTER_MEDIUM.yaml` and `data/merge_yaml/merged/autotrophic_nitrobacter_medium_jcm_1503.yaml`. |

---

## 3. Newly Added Growth-Media and Stock-Solution Records (`CultureMech:015916`–`CultureMech:015920`)

1. **`CultureMech:015916` (`jcm.grmd:1422` — `METHANOCORPUSCULUM AGGREGANS MEDIUM`)**
   - **Normalized YAML**: `data/normalized_yaml/archaea/JCM_J1422_METHANOCORPUSCULUM_AGGREGANS_MEDIUM.yaml`
   - **Merged YAML**: `data/merge_yaml/merged/methanocorpusculum_aggregans_medium_jcm_1422.yaml`
   - **Category / Type / State / pH**: `archaea`, `COMPLEX`, `LIQUID`, `pH 7.0`
   - **Formulation**: 14 basal and post-autoclave anaerobic components (`KH2PO4`, `MgSO4·7H2O`, `NaCl`, `NH4Cl`, `CaCl2·2H2O`, `Sodium acetate`, `Sodium formate`, `Yeast extract`, `Trypticase peptone (BD-BBL)`, `Resazurin`, `Distilled water`, `8% NaHCO3 solution`, `5% L-Cysteine·HCl·H2O solution`, `5% Na2S·9H2O solution`) plus 1 referenced stock solution (`Trace mineral solution (see Medium No. 1303)`, `mediadive.solution:5312`, `1.0 ML_PER_L`).

2. **`CultureMech:015917` (`jcm.grmd:1476` — `MODIFIED UREAPLASMA MEDIUM`)**
   - **Normalized YAML**: `data/normalized_yaml/bacterial/JCM_J1476_MODIFIED_UREAPLASMA_MEDIUM.yaml`
   - **Merged YAML**: `data/merge_yaml/merged/modified_ureaplasma_medium.yaml`
   - **Category / Type / State / pH**: `bacterial`, `COMPLEX`, `LIQUID`, `pH 6.0`
   - **Formulation**: Basal broth (`PPLO broth without crystal violet (BD-Difco) 21.0 g/L`, `Distilled water 700.0 ml/L`, heat-inactivated `Fetal bovine serum 200.0 ml/L`) supplemented with 3 filter-sterilized stock solutions modeled in `solutions`:
     - `25% (w/v) Fresh yeast extract solution` (`100.0 ML_PER_L`)
     - `10% (w/v) Urea solution` (`5.0 ML_PER_L`)
     - `0.2% (w/v) Phenol red solution` (`10.0 ML_PER_L`)

3. **`CultureMech:015918` (`jcm.grmd:1483` — `AMMONIA OXIDIZING BACTERIA MEDIUM`)**
   - **Normalized YAML**: `data/normalized_yaml/bacterial/JCM_J1483_AMMONIA_OXIDIZING_BACTERIA_MEDIUM.yaml`
   - **Merged YAML**: `data/merge_yaml/merged/ammonia_oxidizing_bacteria_medium.yaml`
   - **Category / Type / State / pH**: `bacterial`, `DEFINED`, `LIQUID`, `pH 7.8`
   - **Formulation**: Multi-table JCM medium previously held in `SKIP_GRMDS` in `scripts/import_jcm_grmd.py` because the single-table scraper would have emitted only Solution A. Curated with full basal salts from Solution A (`800 ml`) + Solution B (`200 ml`) (`(NH4)2SO4 2.0 g/L`, `NaCl 0.5 g/L`, `MgSO4·7H2O 0.05 g/L`, `CaCl2·2H2O 0.02 g/L`, `KH2PO4 0.5 g/L`) and 3 filter-sterilized stock solutions in `solutions`:
     - `Solution C (Fe-EDTA solution)` (`0.5 ML_PER_L`: `EDTA·2Na`, `FeSO4·7H2O`, `Conc. H2SO4`, `Distilled water`)
     - `Solution D (Trace element solution)` (`1.0 ML_PER_L`: `H3BO3`, `CuCl2·2H2O`, `MnCl2·4H2O`, `Na2MoO4·2H2O`, `ZnCl2`, `CoCl2·6H2O`, `NiCl2·6H2O`, `Distilled water`)
     - `0.05% (w/v) Phenol red solution` (`2.5 ML_PER_L`: `Phenol red`, `Distilled water`)

4. **`CultureMech:015919` (`jcm.grmd:1492` — `BAP+ MEDIUM FOR FRANKIA`)**
   - **Normalized YAML**: `data/normalized_yaml/bacterial/JCM_J1492_BAP_MEDIUM_FOR_FRANKIA.yaml`
   - **Merged YAML**: `data/merge_yaml/merged/bap_medium_for_frankia_jcm_1492.yaml`
   - **Category / Type / State / pH**: `bacterial`, `COMPLEX`, `LIQUID`, `pH 6.7`
   - **Formulation**: 6 basal components (`MgSO4·7H2O`, `CaCl2·2H2O`, `NH4Cl`, `Sodium propionate`, `Yeast extract`, `Distilled water`) plus 4 structured stock solutions in `solutions`:
     - `Phosphate buffer stock solution` (`10.0 ML_PER_L`: `KH2PO4 95.0 g/L`, `K2HPO4 52.0 g/L`, `Distilled water 1000.0 ml/L`, pH 6.7)
     - `Fe-EDTA stock solution` (`1.0 ML_PER_L`: `Sodium citrate·2H2O 20.0 g/L`, `Iron(III) citrate 4.0 g/L`, `Distilled water 100.0 ml/L`)
     - `Trace element solution` (`1.0 ML_PER_L`: `H3BO3`, `MnCl2·4H2O`, `ZnSO4·7H2O`, `CuSO4·5H2O`, `Na2MoO4·2H2O`, `CoSO4·7H2O`, `Distilled water`)
     - `Vitamin solution` (`1.0 ML_PER_L`: `Thiamine·HCl`, `Nicotinic acid`, `Pyridoxine·HCl`, `Distilled water`)

5. **`CultureMech:015920` (`jcm.grmd:1503` — `AUTOTROPHIC NITROBACTER MEDIUM`)**
   - **Normalized YAML**: `data/normalized_yaml/bacterial/JCM_J1503_AUTOTROPHIC_NITROBACTER_MEDIUM.yaml`
   - **Merged YAML**: `data/merge_yaml/merged/autotrophic_nitrobacter_medium_jcm_1503.yaml`
   - **Category / Type / State / pH**: `bacterial`, `DEFINED`, `LIQUID`, `pH 6.3`
   - **Formulation**: MES-buffered pH 6.3 autotrophic *Nitrobacter* medium (`NaNO2 0.2 g/L`, `MES 2.0 g/L`, `Distilled water 900.0 ml/L`) plus 2 structured stock solutions in `solutions`:
     - `Stock solution` (`100.0 ML_PER_L`: `NaCl 5.0 g/L`, `KH2PO4 1.5 g/L`, `MgSO4·7H2O 0.5 g/L`, `CaCl2·2H2O 0.07 g/L`, `Distilled water 1000.0 ml/L`)
     - `Trace element solution` (`1.0 ML_PER_L`: `MnSO4·xH2O 33.8 mg/L`, `H3BO3 49.4 mg/L`, `ZnSO4·7H2O 43.1 mg/L`, `(NH4)6Mo7O24 37.1 mg/L`, `FeSO4·7H2O 97.3 mg/L`, `CuSO4·5H2O 25.0 mg/L`, `Distilled water 1000.0 ml/L`)

---

## 4. Repeated Search of the Bounded Frontier & Preserved Search Limits

- **Importer Enhancement**: Updated `scripts/import_jcm_grmd.py` so `ingested_grmd_numbers()` recognizes `source: TOGO M#### / JCM Medium <N>` ingredient provenance and raised `--scan-max` default from `1500` to `1600` (with unit-test coverage in `tests/test_import_jcm_grmd.py`).
- **Repeated Frontier Scan**: Re-ran `.venv/bin/python scripts/import_jcm_grmd.py --detect-missing --scan-max 1600 --delay 0.05 --dry-run`:
  ```text
  Scanning JCM 1..1600 for media missing from the corpus...
  Found 0 real JCM media not yet ingested.

  Done. written=0 skipped=0
  ```
- **Preserved Search Limits & Future Frontier**:
  - `GRMD = 1504..1600` (and `1501..1502`) are currently unassigned ~843-byte empty slots in the upstream RIKEN JCM database; future cycles should re-scan `1501..1650` as RIKEN JCM publishes new media above `GRMD=1503`.
  - `GRMD = 1483` remains listed in `SKIP_GRMDS` as a safeguard so the single-table scraper never overwrites the manually curated multi-solution record `JCM_J1483_AMMONIA_OXIDIZING_BACTERIA_MEDIUM.yaml`.
