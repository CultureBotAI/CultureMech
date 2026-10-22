# Stage 1 Validation Report — Run `mech-goal-sequence-20261019`, Cycle 2, Stage 1 (`add_records`)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `2`
- **Stage**: `1` (`add_records` / `discover_add`)
- **Revision**: `1`
- **Source Revision**: `98c2c080ee1b68ab3961fbba0bd50cef81d458ef` (`origin/main`)

---

## 1. Summary of Changes Validated

1. **5 Newly Added JCM Growth-Media Recipes (`CultureMech:015916`–`CultureMech:015920`) and 10 Embedded Stock-Solution Recipes**:
   - `data/normalized_yaml/archaea/JCM_J1422_METHANOCORPUSCULUM_AGGREGANS_MEDIUM.yaml` + `data/merge_yaml/merged/methanocorpusculum_aggregans_medium_jcm_1422.yaml` (`CultureMech:015916`)
   - `data/normalized_yaml/bacterial/JCM_J1476_MODIFIED_UREAPLASMA_MEDIUM.yaml` + `data/merge_yaml/merged/modified_ureaplasma_medium.yaml` (`CultureMech:015917`)
   - `data/normalized_yaml/bacterial/JCM_J1483_AMMONIA_OXIDIZING_BACTERIA_MEDIUM.yaml` + `data/merge_yaml/merged/ammonia_oxidizing_bacteria_medium.yaml` (`CultureMech:015918`)
   - `data/normalized_yaml/bacterial/JCM_J1492_BAP_MEDIUM_FOR_FRANKIA.yaml` + `data/merge_yaml/merged/bap_medium_for_frankia_jcm_1492.yaml` (`CultureMech:015919`)
   - `data/normalized_yaml/bacterial/JCM_J1503_AUTOTROPHIC_NITROBACTER_MEDIUM.yaml` + `data/merge_yaml/merged/autotrophic_nitrobacter_medium_jcm_1503.yaml` (`CultureMech:015920`)
2. **Lifecycle Registry & Catalog**:
   - `data/culturemech_id_registry.tsv` (`15,910` -> `15,915` active rows)
   - `data/culturemech_recipe_catalog.tsv` (`15,915` -> `15,920` total rows: `15,915` active, `5` retired)
3. **JCM Importer & Unit Tests**:
   - `scripts/import_jcm_grmd.py`: expanded default `--scan-max` from `1500` to `1600`, added `source: TOGO M#### / JCM Medium <N>` provenance recognition in `ingested_grmd_numbers()`, and updated `SKIP_GRMDS` documentation for `GRMD=1483`.
   - `tests/test_import_jcm_grmd.py`: added test coverage for `source: TOGO M3010 / JCM Medium 1338` in `test_ingested_grmd_numbers_finds_source_records_without_auxiliary_refs`.
4. **Tracked Workflow Index**:
   - `reviews/workflow/latest.yaml` synchronized from `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/session-orchestration/20261019/culturemech/verified-evidence-index.json` (incorporating verified Cycle 1 Stage 6 closure PR `#655`).

---

## 2. Validation Commands and Results

### 2.1 Repeated Bounded-Frontier Scan (`scripts/import_jcm_grmd.py --detect-missing --scan-max 1600 --dry-run`)
```text
$ .venv/bin/python scripts/import_jcm_grmd.py --detect-missing --scan-max 1600 --delay 0.05 --dry-run
Scanning JCM 1..1600 for media missing from the corpus...
Found 0 real JCM media not yet ingested.

Done. written=0 skipped=0
```

### 2.2 Strict LinkML Schema Validation (`scripts/validate_strict.py`)
```text
$ .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
Validating 15915 files with 15 workers; layers=schema; schema=/Users/marcin/Documents/VIMSS/ontology/Mechs/CultureMech/src/culturemech/schema/culturemech.yaml
=== validate-strict summary ===
  files scanned:      15915
  layers:             schema
  files with ERROR:   0
  total ERROR rows:   0
  TSV:                /tmp/instance_validation_failures.tsv
```

### 2.3 ChEBI Consistency Audit (`scripts/audit_chebi_consistency.py`)
```text
$ .venv/bin/python scripts/audit_chebi_consistency.py --out /tmp/chebi_consistency.tsv --max-allowed 101
Signal A — same name, multiple CHEBI ids (reliable groundings): 70 names
Signal B — same CHEBI id, multiple distinct compounds: 251 ids
Low-confidence chebi_term layer (reported, not gated): 29 fields {'(none)': 29}
wrote /tmp/chebi_consistency.tsv (321 rows)
```

### 2.4 Concentration Plausibility Audit (`scripts/audit_concentration_plausibility.py`)
```text
$ .venv/bin/python scripts/audit_concentration_plausibility.py --out /tmp/conc_plausibility.tsv --max-allowed 9252 --max-cocktails 171
Implausible concentration rows: 9252 across 3261 records
  WATER_AS_VOLUME      492
  TRACE_SALT_AS_STOCK  4328
  INDICATOR_UNIT_SLIP  4432

Records holding a FLATTENED STOCK COCKTAIL: 171
  (>=3 flagged vitamin or trace rows and no `solutions:` block — the actionable subset)
```

### 2.5 Recipe ID Lifecycle Catalog & Media Variant Links (`scripts/build_recipe_id_catalog.py --check`, `scripts/validate_media_variant_links.py`)
```text
$ .venv/bin/python scripts/build_recipe_id_catalog.py --check
Recipe ID catalog is current: 15915 active, 5 retired.

$ .venv/bin/python scripts/validate_media_variant_links.py --reports-dir /tmp
Scanned 15915 YAML records
Parent-to-child links: 2992
Child-to-parent links: 2992
Errors: 0
Warnings: 0
```

### 2.6 Pytest Suite (`tests/test_import_jcm_grmd.py`, `tests/test_recipe_id_catalog.py`)
```text
$ .venv/bin/pytest --no-cov -o cache_dir=/tmp/pytest_cache tests/test_import_jcm_grmd.py tests/test_recipe_id_catalog.py
============================= test session starts ==============================
collected 24 items

tests/test_import_jcm_grmd.py ...                                        [ 12%]
tests/test_recipe_id_catalog.py .....................                    [100%]

============================= 24 passed in 51.54s ==============================
```
