---
name: curate-yaml-record
description: Review and curate one CultureMech medium or stock-solution YAML record for source identity, formulation accuracy, preparation detail, growth evidence, completeness, and resolvable gaps. Use when asked to audit, improve, complete, correct, or add evidence to one record; do not use for bulk ingestion, generated merge/page edits, or as permission to contact anyone or mutate GitHub.
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch, Edit, Write
metadata:
  category: curation
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Curate one CultureMech YAML record

Produce a scientifically defensible medium or stock-solution record and an
explicit account of what is supported, corrected, still missing, and genuinely
unknown. Search results are leads; only inspected sources can support a claim.

## Boundaries

- Resolve one authoritative target under `data/normalized_yaml/`. Distinguish
  `MediaRecipe` from `SolutionRecipe`; do not silently substitute a similarly
  named medium, variant, or stock solution.
- An audit or review request is read-only. Curate, improve, complete, correct,
  or add-evidence requests authorize local edits to the named record and the
  smallest necessary repository-owned provenance path.
- Never edit `data/raw_yaml/`, `data/merge_yaml/merged/`, `app/data.js`, or
  generated `pages/` as the source of a correction. Fix the normalized record,
  source-specific input, or maintained rule that owns the value.
- Never create or edit a GitHub issue, PR, comment, email, form, or message
  without explicit authorization for that outbound action.
- Preserve unrelated work. Follow `CLAUDE.md`; use a branch and a separate
  worktree when the checkout is dirty or occupied.
- Never infer that an absent optional property is false and never add a value
  merely to improve coverage.

## Read before judging the record

Read the complete target plus:

- `CLAUDE.md`;
- `docs/CONTRIBUTING.md` and `docs/QUICK_START.md`;
- the relevant `MediaRecipe`, `SolutionRecipe`, ingredient, evidence, and
  curation-event classes in `src/culturemech/schema/culturemech.yaml`;
- [references/review-checklist.md](references/review-checklist.md).

Consult `docs/DATA_LAYERS.md` when ownership of a field or generated artifact
is unclear. Check related variants, solutions, and source records; a rendered
page or merged recipe is not independent evidence.

## Workflow

### 1. Establish the baseline

Read the whole YAML. Record its ID, lineage token, name, record kind, source
metadata, references, variants, composition, existing evidence, quality flags,
and curation history. Run:

```bash
just validate-schema <record-path>
just validate-strict <record-path>
```

Use `just validate-terms <record-path>` and `just validate-references
<record-path>` when their caches or network dependencies are available. A green
schema gate proves shape, not scientific correctness.

### 2. Verify record and source identity first

Confirm that the record denotes the intended medium or stock solution and that
its source name, source accession, category, `record_kind`, parent/variant
relations, and stable ID agree. IDs are permanent; never hand-pick or reuse one.

For ingredients, use the packaged MediaIngredientMech label index and respect
exact chemical form. Hydration, stereochemistry, salts, digits, formula
punctuation, and stock-versus-final concentration can change identity or amount.
Do not replace unresolved material with a plausible ChEBI term.

### 3. Review every scientific and procedural claim

Check each ingredient, solution reference, amount/unit, pH, temperature,
salinity, atmosphere, physical state, sterilization step, preparation step,
storage condition, target-organism assertion, application, and growth-evidence
claim against the cited source. Distinguish an upstream recipe, primary growth
study, database assertion, secondary review, and search-result snippet.

Preserve the source's stated formulation. Do not silently convert a stock
recipe to final-medium amounts, fill an unspecified quantity, or upgrade
reported growth to an optimal or exclusive medium claim. Keep exact quotations
short and attached to the narrowest supported assertion.

### 4. Assess completeness and resolve supported gaps

Apply the checklist and use bounded, targeted searches for consequential gaps.
Prioritize:

1. wrong medium/solution identity or source;
2. missing, duplicated, or chemically misresolved ingredients;
3. incorrect quantity, unit, stock dilution, or final-volume arithmetic;
4. missing or contradictory preparation, sterilization, pH, temperature, or
   atmosphere details;
5. unsupported growth, application, organism, or variant claims.

Do not add generic discussion text for every empty optional slot. Record a
discussion or quality flag only for a concrete conflict or consequential task,
including what was checked and what evidence would resolve it.

### 5. Write through the guarded path

Use a narrowly scoped temporary or checked-in Python mutator that loads the
existing YAML, asserts the expected ID/path, changes only reviewed nodes,
appends an event with
`culturemech.curate.curation_event.record_curation_event`, and writes with
`culturemech.validation.write_validated.write_validated_recipe`.

Use `curator="claude"` when no curator identity was supplied. Do not attribute
an agent's judgement to the user. Do not append an event when no substantive
change was made. Inspect the object and text diff; abandon or repair any
whole-file presentation churn before proceeding.

If the correction is source-owned or generated, fix its authoritative input or
rule and regenerate. Never patch the derived merge to make it look correct.

### 6. Verify and report

After an edit, run the focused checks again and then the proportional wider
gates:

```bash
just validate-strict <record-path>
just validate-products
just verify-merges
git diff --check
git diff -- <record-path> src scripts history
```

Run `just qc` when the change or available environment warrants the full gate.
Read the emitted YAML again and ensure every citation supports its nearest
claim and the history entry describes the actual diff.

Report corrections/additions and their sources, retained claims checked,
remaining gaps and unsuccessful bounded searches, data-layer ownership of each
change, and every validation result. CultureMech has no record-level REVIEWED
status; never invent one.
