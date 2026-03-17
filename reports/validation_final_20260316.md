# CultureMech Recipe Validation Report

**Date:** 2026-03-16 23:12:47

## Summary Statistics

- **Total recipes:** 15,449
- **Valid recipes (no P1 errors):** 15,449 (100.0%)
- **P1 Critical Errors:** 0 issues in 0 recipes (0.0%)
- **P2 High Priority:** 0 issues in 0 recipes (0.0%)
- **P3 Medium Priority:** 33477 issues in 15441 recipes (99.9%)
- **P4 Low Priority:** 21045 issues in 10665 recipes (69.0%)

## MediaIngredientMech Coverage

- **Total ingredient instances:** 186,360
- **Linked instances:** 66
- **Overall coverage:** 0.0%

## By Category

| Category | Recipes | Valid | P1 | P2 | P3 | P4 | Avg Coverage |
|----------|---------|-------|----|----|----|----|-------------|
| algae | 242 | 242 | 0 | 0 | 242 | 242 | 0.0% |
| archaea | 63 | 63 | 0 | 0 | 63 | 63 | 0.0% |
| bacterial | 10,136 | 10,136 | 0 | 0 | 10136 | 10136 | 0.0% |
| fungal | 119 | 119 | 0 | 0 | 119 | 119 | 0.0% |
| solution | 4,784 | 4,784 | 0 | 0 | 4776 | 0 | 0.2% |
| specialized | 105 | 105 | 0 | 0 | 105 | 105 | 4.4% |

## Most Frequent Issues

| Rule | Description | Count | Affected Recipes |
|------|-------------|-------|------------------|
| P3.2 | Low MediaIngredientMech coverage | 15,072 | 15,072 |
| P3.5 | Sterilization not specified | 10,665 | 10,665 |
| P4.2 | Missing target organisms | 10,655 | 10,655 |
| P4.3 | Missing references | 10,390 | 10,390 |
| P3.4 | Missing preparation steps | 5,849 | 5,849 |
| P3.6 | pH not specified | 1,394 | 1,394 |
| P3.1 | Placeholder text | 497 | 99 |

## Recommendations

1. ✅ No P1 critical errors - ready for KG export
3. **MEDIUM PRIORITY:** Auto-fix or review 33477 P3 issues
   - Run: `just fix-all-data-quality` to auto-correct safe issues
4. **Coverage:** Improve MediaIngredientMech coverage from 0.0% to >80%
   - Run: `PYTHONPATH=src python scripts/enrich_with_mediaingredientmech.py`
