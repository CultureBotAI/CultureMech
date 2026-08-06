---
name: schema-gap-analysis
description: Lightweight linkml-validate-based check for CultureMech schema/data drift, classified along three axes (schema / instances / process). For the comprehensive audit (also scans pipeline/writers, emits TSV reports + re-runnable harness), use `audit-schema-gaps` instead.
category: quality
requires_database: false
requires_internet: false
version: 2.1.0
---

# Schema gap analysis (CultureMech)

The conceptual framework — why three axes, error-class heuristics, common anti-patterns — lives once at the cross-Mech version in claw:
https://github.com/CultureBotAI/culturebotai-claw/blob/main/.claude/skills/schema-gap-analysis/SKILL.md

This file is the CultureMech-specific operational version. Every command below runs as-is.

## When to use this skill vs. `audit-schema-gaps`

- **`schema-gap-analysis`** (this skill): quick `linkml-validate` pass + error histogram + three-axis classification. ~5–10 min start to finish. Good for "did my recent commit break something?" or onboarding.
- **`audit-schema-gaps`** (CultureMech's deeper skill): also scans `src/`/`scripts/` for writer/pipeline drift, produces five reports under `reports/`, emits a re-runnable `scripts/validate_strict.py` harness. ~30 min. Run when you suspect systemic drift or before a major release.

Same three-axis framework underneath; the deep version just covers more surface.

## Setup

CultureMech uses `uv`-managed `.venv/`:

```bash
# linkml-validate ships in .venv; smoke test:
.venv/bin/linkml-validate --help

# If you get `AttributeError: Format has no attribute 'JSON'` — pin runtime:
.venv/bin/python -m pip install "linkml-runtime>=1.9,<1.10"
```

## Procedure

### 1. Validate the canonical merged set

```bash
find data/merge_yaml/merged -name "*.yaml" -print0 \
  | xargs -0 .venv/bin/linkml-validate \
      -s src/culturemech/schema/culturemech.yaml \
      -C MediaRecipe \
      2>&1 | tee /tmp/cm_validate.out > /dev/null
grep -c "^\[ERROR\]" /tmp/cm_validate.out
```

### 2. (Optional) Validate the raw normalized layer

```bash
find data/normalized_yaml -name "*.yaml" -print0 \
  | xargs -0 .venv/bin/linkml-validate \
      -s src/culturemech/schema/culturemech.yaml \
      -C MediaRecipe \
      2>&1 | tee /tmp/cm_normalized_validate.out > /dev/null
grep -c "^\[ERROR\]" /tmp/cm_normalized_validate.out
```

### 3. Histogram the errors

```bash
grep -oE "Additional properties are not allowed \('[^']+'" /tmp/cm_validate.out \
  | sort | uniq -c | sort -rn

grep -oE "'[^']+' is a required property" /tmp/cm_validate.out \
  | sort | uniq -c | sort -rn

grep -oE "does not match '[^']+'" /tmp/cm_validate.out \
  | sort | uniq -c | sort -rn

grep -oE "is not a '[^']+'" /tmp/cm_validate.out \
  | sort | uniq -c | sort -rn
```

### 4. Cross-check generator drift (Axis 3)

```bash
# Naive datetimes
grep -rnE 'datetime\.now\(\)\.isoformat\b' \
  src/ scripts/ --include='*.py' | grep -v "timezone"

# yaml.dump that drops collection metadata (CultureMech keys: media/recipes)
grep -rnE 'yaml\.dump\(\s*\{\s*["\047](media|recipes)["\047]\s*:' \
  src/ scripts/ --include='*.py'

# Smoking-gun greps for known classes (see history table below)
grep -rn '"date":\|\bcuration_history\b.*[^a-z]date\b' \
  src/ scripts/ --include='*.py' | head -10
grep -rn '"instruction":' src/ scripts/ --include='*.py' | head -10
grep -rn '"reference_id":' src/ scripts/ --include='*.py' | head -10
```

### 5. Re-validate after fixes

```bash
find data/merge_yaml/merged -name "*.yaml" -print0 \
  | xargs -0 .venv/bin/linkml-validate \
      -s src/culturemech/schema/culturemech.yaml \
      -C MediaRecipe \
      2>&1 | grep -c "^\[ERROR\]"
# target: 0
```

## CultureMech-specific gap classes (current state, 2026-05-17 pass)

| Count | Error | Axis | Fix |
|---:|---|---|---|
| 1,195 | `Additional properties are not allowed ('date')` + `'timestamp' is a required property` in `curation_history[]` | Process | Rename emit: `date` → `timestamp`. Use `datetime.now(timezone.utc).isoformat()`. Then migrate the 1,195 records. |
| 126 | `Additional properties are not allowed ('instruction')` + `'description'` + `'action'` required in `preparation_steps[]` | Process | Rename emit: `instruction` → `description`. Ensure `action` is populated (likely `MIX`/`ADJUST_PH`/`AUTOCLAVE` enum default). |
| 119 | `'concentration' is a required property` in `ingredients[]` | Schema or instance — needs inspection | If solid-medium ingredients legitimately lack `concentration`, relax schema to `recommended`. If a writer drops it, fix the writer. |
| 28 | `Additional properties are not allowed ('reference_id')` + `'reference' is a required property` in `references[]` | Process | Rename emit: `reference_id` → `reference`. |

Total: 2,943 errors across 4,289 records (2026-05-17). Same data, deeper audit is in `reports/` (run `/audit-schema-gaps` for that).

## Pointers

- Schema: `src/culturemech/schema/culturemech.yaml`
- Custom validator (tolerant): `src/culturemech/validation/validator.py`
- Renderer (writes to `pages/`, not validated YAML): `src/culturemech/render_media_pages.py`
- Deeper audit skill: `.claude/skills/audit-schema-gaps/SKILL.md`
- Cross-Mech framework + new-Mech bootstrap template: [claw/.claude/skills/schema-gap-analysis](https://github.com/CultureBotAI/culturebotai-claw/blob/main/.claude/skills/schema-gap-analysis/SKILL.md)
