---
name: stats-report
description: Generate reproducible corpus, source, ingredient-mapping, and data-quality statistics from the current CultureMech normalized corpus.
category: reporting
requires_database: false
requires_internet: false
version: 1.1.0
---

# Statistics report

Use this skill for current repository counts, README statistics, publication
summaries, or before/after measurements for an import or enrichment.

## Commands

```bash
just stats-terminal
just stats-report
just stats-json
just stats-markdown
```

The underlying command is `uv run python scripts/generate_stats.py`. It reads
`data/normalized_yaml/` in one pass. Never copy a record count from this skill:
derive it at run time because the corpus changes continuously.

`just stats-report` writes JSON and Markdown beneath `output/stats/` by default.
These reports are reproducible outputs and are not authoritative recipe data.
Use `just update-readme-stats` for the README-managed statistics block.

## Prerequisites

Basic recipe counts need only the locked project environment. Ingredient
mapping coverage also uses tracked or locally fetched inputs under
`data/raw/microbe-media-param/` and `data/raw/mediadive/`; report missing
optional inputs rather than substituting workstation paths.

## Verification

- Confirm normalized and merged counts are labeled separately.
- Record the exact command and commit used for published figures.
- Do not hand-edit generated JSON/Markdown and present it as a fresh run.
- If updating documentation, run the README freshness and local-link checks.
