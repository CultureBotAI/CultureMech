# CultureMech Recipe Validation Report

**Date:** 2026-03-16 20:59:38

## Summary Statistics

- **Total recipes:** 15,449
- **Valid recipes (no P1 errors):** 6,983 (45.2%)
- **P1 Critical Errors:** 18034 issues in 8466 recipes (54.8%)
- **P2 High Priority:** 1 issues in 1 recipes (0.0%)
- **P3 Medium Priority:** 38260 issues in 15449 recipes (100.0%)
- **P4 Low Priority:** 30603 issues in 15449 recipes (100.0%)

## MediaIngredientMech Coverage

- **Total ingredient instances:** 191,134
- **Linked instances:** 67
- **Overall coverage:** 0.0%

## By Category

| Category | Recipes | Valid | P1 | P2 | P3 | P4 | Avg Coverage |
|----------|---------|-------|----|----|----|----|-------------|
| algae | 242 | 242 | 0 | 0 | 242 | 242 | 0.0% |
| archaea | 63 | 52 | 11 | 0 | 63 | 63 | 0.0% |
| bacterial | 10,136 | 6,568 | 3568 | 1 | 10136 | 10136 | 0.0% |
| fungal | 119 | 47 | 72 | 0 | 119 | 119 | 0.0% |
| mediadive | 4,774 | 0 | 4774 | 0 | 4774 | 4774 | 0.0% |
| solutions | 10 | 0 | 10 | 0 | 10 | 10 | 88.3% |
| specialized | 105 | 74 | 31 | 0 | 105 | 105 | 4.4% |

## Most Frequent Issues

| Rule | Description | Count | Affected Recipes |
|------|-------------|-------|------------------|
| P3.5 | Sterilization not specified | 15,449 | 15,449 |
| P4.2 | Missing target organisms | 15,439 | 15,439 |
| P4.3 | Missing references | 15,164 | 15,164 |
| P3.2 | Low MediaIngredientMech coverage | 15,071 | 15,071 |
| P1.3 | Missing required fields | 14,352 | 4,784 |
| P3.4 | Missing preparation steps | 5,849 | 5,849 |
| P1.4 | Invalid enum values | 3,682 | 3,682 |
| P3.6 | pH not specified | 1,394 | 1,394 |
| P3.1 | Placeholder text | 497 | 99 |
| P2.1 | Invalid MediaIngredientMech ID | 1 | 1 |

## P1 Critical Errors (Must Fix)

### MEDIUM FOR HALOPHILIC ARCHAEA (CultureMech:000249)

**File:** `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CultureMech/data/normalized_yaml/archaea/DSMZ_1184_MEDIUM_FOR_HALOPHILIC_ARCHAEA.yaml`

- **P1.4:** Invalid physical_state: SOLID_AGAR

### HALOPHILIC MEDIUM (CultureMech:000252)

**File:** `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CultureMech/data/normalized_yaml/archaea/DSMZ_1399_HALOPHILIC_MEDIUM.yaml`

- **P1.4:** Invalid physical_state: SOLID_AGAR

### SALINIBACTER HALOPHILIC MEDIUM (CultureMech:000253)

**File:** `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CultureMech/data/normalized_yaml/archaea/DSMZ_1400_SALINIBACTER_HALOPHILIC_MEDIUM.yaml`

- **P1.4:** Invalid physical_state: SOLID_AGAR

### ALKALOPHILIC HALOPHILE MEDIUM (CultureMech:000255)

**File:** `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CultureMech/data/normalized_yaml/archaea/DSMZ_1431_ALKALOPHILIC_HALOPHILE_MEDIUM.yaml`

- **P1.4:** Invalid physical_state: SOLID_AGAR

### ACIDO-THERMOPHILE MEDIUM (CultureMech:000256)

**File:** `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CultureMech/data/normalized_yaml/archaea/DSMZ_1433_ACIDO-THERMOPHILE_MEDIUM.yaml`

- **P1.4:** Invalid physical_state: SOLID_AGAR

### HALOACTINOMYCES HALOPHILUS MEDIUM (CultureMech:000257)

**File:** `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CultureMech/data/normalized_yaml/archaea/DSMZ_1742_HALOACTINOMYCES_HALOPHILUS_MEDIUM.yaml`

- **P1.4:** Invalid physical_state: SOLID_AGAR

### MEDIUM FOR THERMOPHILIC ACTINOMYCETES (AGRE 1964) (CultureMech:000273)

**File:** `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CultureMech/data/normalized_yaml/archaea/DSMZ_570_MEDIUM_FOR_THERMOPHILIC_ACTINOMYCETES_AGRE_1964.yaml`

- **P1.4:** Invalid physical_state: SOLID_AGAR

### DICHOTOMICROBIUM THERMOHALOPHILUM MEDIUM (CultureMech:000274)

**File:** `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CultureMech/data/normalized_yaml/archaea/DSMZ_590_DICHOTOMICROBIUM_THERMOHALOPHILUM_MEDIUM.yaml`

- **P1.4:** Invalid physical_state: SOLID_AGAR

### HP 101 HALOPHILE MEDIUM (CultureMech:000275)

**File:** `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CultureMech/data/normalized_yaml/archaea/DSMZ_625_HP_101_HALOPHILE_MEDIUM.yaml`

- **P1.4:** Invalid physical_state: SOLID_AGAR

### MEDIUM FOR ACIDURIC, THERMOPHILIC BACILLUS STRAINS (CultureMech:000277)

**File:** `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CultureMech/data/normalized_yaml/archaea/DSMZ_674_MEDIUM_FOR_ACIDURIC_THERMOPHILIC_BACILLUS_STRAINS.yaml`

- **P1.4:** Invalid physical_state: SOLID_AGAR

### HP 101 HALOPHILE MEDIUM (CultureMech:000299)

**File:** `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CultureMech/data/normalized_yaml/archaea/JCM_J464_HP_101_HALOPHILE_MEDIUM.yaml`

- **P1.4:** Invalid physical_state: SOLID_AGAR

### ZM/10 (CultureMech:000315)

**File:** `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CultureMech/data/normalized_yaml/bacterial/CCAP_C108_ZM_10.yaml`

- **P1.4:** Invalid physical_state: SOLID_AGAR

### ASW:BG (CultureMech:000316)

**File:** `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CultureMech/data/normalized_yaml/bacterial/CCAP_C10_ASW_BG.yaml`

- **P1.4:** Invalid physical_state: SOLID_AGAR

### ASN-III (CultureMech:000317)

**File:** `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CultureMech/data/normalized_yaml/bacterial/CCAP_C110_ASN-III.yaml`

- **P1.4:** Invalid physical_state: SOLID_AGAR

### 3N-BBM+V (CultureMech:000321)

**File:** `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CultureMech/data/normalized_yaml/bacterial/CCAP_C14_3N-BBM_V.yaml`

- **P1.4:** Invalid physical_state: SOLID_AGAR

### 3N-BBM+V recipe for customer orders (CultureMech:000322)

**File:** `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CultureMech/data/normalized_yaml/bacterial/CCAP_C15_3N-BBM_V_recipe_for_customer_orders.yaml`

- **P1.4:** Invalid physical_state: SOLID_AGAR

### BG11 (CultureMech:000324)

**File:** `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CultureMech/data/normalized_yaml/bacterial/CCAP_C17_BG11.yaml`

- **P1.4:** Invalid physical_state: SOLID_AGAR

### C Medium, Modified (CultureMech:000328)

**File:** `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CultureMech/data/normalized_yaml/bacterial/CCAP_C20_C_Medium_Modified.yaml`

- **P1.4:** Invalid physical_state: SOLID_AGAR

### CGM (CultureMech:000329)

**File:** `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CultureMech/data/normalized_yaml/bacterial/CCAP_C21_CGM.yaml`

- **P1.4:** Invalid physical_state: SOLID_AGAR

### CMA (CultureMech:000332)

**File:** `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CultureMech/data/normalized_yaml/bacterial/CCAP_C24_CMA.yaml`

- **P1.4:** Invalid physical_state: SOLID_AGAR


*...and 8446 more recipes with P1 errors*

## Recommendations

1. **CRITICAL:** Fix 18034 P1 errors in 8466 recipes before KG export
2. **HIGH PRIORITY:** Review 1 P2 issues in 1 recipes
3. **MEDIUM PRIORITY:** Auto-fix or review 38260 P3 issues
   - Run: `just fix-all-data-quality` to auto-correct safe issues
4. **Coverage:** Improve MediaIngredientMech coverage from 0.0% to >80%
   - Run: `PYTHONPATH=src python scripts/enrich_with_mediaingredientmech.py`
