---
name: curate-yaml-record
description: Review and curate one CultureMech medium or stock-solution YAML record for source identity, formulation accuracy, preparation detail, growth evidence, completeness, and resolvable gaps. Use when asked to audit, improve, complete, correct, or add evidence to one record; do not use for bulk ingestion, generated merge/page edits, or as permission to contact anyone or mutate GitHub.
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch, Edit, Write
metadata:
  category: curation
  requires_database: false
  requires_internet: true
  version: 2.0.0
---

# Curate one CultureMech YAML record

## Structured Review Output

For every new review or audit, follow
[docs/record-reviews.md](../../../docs/record-reviews.md) and
[the local profile](../../../docs/record-review-profile.md).
Capture exact targets and input hashes before judging, preserve this skill's
native rubric, rule IDs, scores and evidence requirements, then author the
structured assessment and run:

```bash
uv run python scripts/record_review.py inspect --targets /tmp/review-targets.yaml
uv run python scripts/record_review.py validate /tmp/completed-review.yaml
uv run python scripts/record_review.py save --content /tmp/completed-review.yaml
```

Choose session-unique temporary paths. Save authoritative YAML and derived
Markdown under `reviews/structured/<timestamp>-<slug>/`; link both in the
final response. This output contract supersedes prose-only report examples.
A single record uses `kind: record`; batches declare exact selection,
population, reviewed targets and limits. Categories also state boundary decisions.
Every reviewed target must have an assessment. Keep P1-P4 and other native
severity/rule information with a justified common severity, and metric definitions,
scales and denominators. Do not infer scientific approval from a native score.

Raw provider drafts and deterministic validator/scan reports are diagnostic
inputs, not completed scientific reviews. Use `scientific_review: false`
for deterministic-only or provenance-only assessments; mark required unavailable
checks and incomplete coverage explicitly. A valid bundle does not change native
status, clear release holds, authorize edits, or append curation history.
For audit-only requests, stop after assessment and persistence; any application
steps below require curation intent.

Produce a scientifically defensible medium or stock-solution record and an
explicit account of what is supported, corrected, still missing, and genuinely
unknown. Search results are leads; only inspected sources can support a claim.

## Shared Contract

<!-- canonical:begin the-contract -->
Produce a defensible record and an explicit account of four things: what is
**supported**, what was **corrected**, what is **still unresolved**, and what is
**genuinely unknown**. The last two are different — a gap you searched for and
could not close is a finding; a gap you did not look at is not.

**One target.** Resolve exactly one record before touching anything. If a label
matches several, or a request names a family rather than a member, stop and
disambiguate. Silently substituting a similar record is the error that no later
check catches, because everything downstream is then correct about the wrong
thing.

**Audit preserves scientific inputs. Curation authorises edits to the named
record only.** A review or audit request changes no scientific record, status,
or curation history. It does save a new timestamped structured review through
`docs/record-reviews.md` and the native rubric in `docs/record-review-profile.md`.
A curate, improve, complete, correct or add-evidence request authorises local edits to that record and the smallest
maintained path its provenance requires — not to neighbours, not to whatever
else looked wrong on the way.

**Search results are leads. Only an inspected source supports a claim.** A
search hit, a deep-research report, a rendered page, and a generated artifact are
each somewhere to look, and none is evidence. Evidence is text you read in the
source, attached to the narrowest assertion it actually supports.
<!-- canonical:end the-contract -->

## Shared Boundaries

<!-- canonical:begin boundaries -->
- **A generated artifact is never the fix.** Pages, merged products, exports and
  derived indexes are outputs. Correct the input or rule that owns the value and
  regenerate; patching the output makes it look right once and diverge on the
  next build.
- **No outbound action without explicit authorisation for that action.** Do not
  launch paid research, contact an author, or create or edit a GitHub issue, PR
  or comment because curation seemed to call for it. Authorisation to curate a
  record is not authorisation to spend or to speak.
- **Absence is not evidence of falsity, and coverage is not a goal.** Never
  infer that an unstated optional property is false. Never fill an optional
  slot to make the record look more complete. An empty field the source does
  not address is correct.
- **Search before declaring anything absent — and search past `.gitignore`.**
  Before treating a record, evidence source, decision row or overlay as missing,
  search for its identifier, label and slug with an ignore-independent tool
  (`rg --no-ignore --hidden`, `grep -r`, or `find`). Ordinary search skips
  ignored files, so an ordinary miss is a search over a subset, not a result.
- **Preserve unrelated work.** Use a branch, and a separate worktree when the
  checkout is dirty or occupied by something else.
<!-- canonical:end boundaries -->

## Shared Evidence Standard

<!-- canonical:begin evidence-standard -->
- Each claim is its own object. A definition, an example, a relation and a
  mechanism edge are separate assertions; attach a source to the narrowest one
  it supports, never to the record as a whole.
- Resolve every DOI, PMID and CURIE, and read enough of the source to establish
  support for the *exact* claim and scope. A matching string from the wrong
  paper, or an unrelated sentence from the right one, is not support.
- A snippet is short verbatim text from the source. Interpretation belongs in a
  notes field, never inside the quotation.
- **The kind of source is part of the citation.** A database assertion, a
  primary experiment, a review, a prediction and a search snippet are different
  strengths of support. Cite each as what it is; never present a database row
  or a review as if it were the primary study.
- Association and prediction do not establish mechanism or causality. Do not
  let a co-occurrence or a computed score become a mechanism edge.
- **A near-miss is not a match.** Never ground to a CURIE or canonical label
  because it looks plausible, and never use a broader or related term as an
  exact identity. Unresolved stays unresolved, recorded as such, until a source
  resolves it.
- **Evidence about one thing supports a claim about that thing.** Do not
  generalise one organism, strain, protein instance, construct or experiment
  into a family-wide, universal or "optimal" claim. Scope inflation is the most
  common way a true observation becomes a false record.
- Keep conflicts. When sources disagree, record both and the disagreement; do
  not resolve it by omission.
- A bounded search that found nothing is a result. Report it as "not found,
  searched X" rather than leaving the field silently empty.
<!-- canonical:end evidence-standard -->

## Shared Write Contract

<!-- canonical:begin writing-back -->
**Write only through the path that preserves formatting and records history.**
Never hand-edit a curated YAML with a text editor or a generic dump: canonical
key order, quoting and derived metadata are what make the corpus diffable, and a
dump destroys them in one save.

Repositories in this fleet do this in three different, equally correct ways, and
which one applies is a property of the corpus:

- **Direct guarded write** — a narrowly scoped mutator loads the record, asserts
  its identity, changes only the reviewed nodes, appends a curation event, and
  writes through the repository's validated writer.
- **Registered editor** — no generic writer exists on purpose; in-place changes
  use text-preserving operations through an editor that is registered and
  behaviourally tested, and the writer audit rejects anything else.
- **Regenerate from inputs** — the record is a build product. The fix goes into
  the decision row, term request, overlay or source inventory that owns the
  value, and the record is regenerated; the YAML is never edited directly.

The section below says which one this repository uses and names the exact
functions or files. Do not guess from a sibling.

Inspect the diff before committing. Whole-file presentation churn — reordered
keys, requoted strings, a hundred lines changed to alter one value — means the
write path was bypassed; abandon and repair rather than commit it.
<!-- canonical:end writing-back -->

## Shared History And Attribution

<!-- canonical:begin history-and-attribution -->
- Use `curator="claude"` when no curator identity was supplied. **Never
  attribute an agent's judgement to the user.** The history entry is a record
  of who decided, and it will be read when the decision is questioned.
- Mark LLM assistance where the schema records it.
- **Do not append a history event when nothing substantive changed.** A
  no-op event is noise that makes real events harder to find.
- The history entry describes the actual diff. If the corpus derives status or
  history from inputs, never set them directly — change the input.
- A REVIEWED status means a human reviewed it. Do not invent one, and do not
  promote to it on the strength of an agent pass.
<!-- canonical:end history-and-attribution -->

## Boundaries

- Resolve one authoritative target under `data/normalized_yaml/`. Distinguish
  `MediaRecipe` from `SolutionRecipe`; do not silently substitute a similarly
  named medium, variant, or stock solution.
- Audit/review preserves scientific inputs and saves a new structured review.
  Curate, improve, complete, correct,
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

For concentration review or additions, use
[review-ingredient-concentrations](../review-ingredient-concentrations/SKILL.md).
Every added/corrected concentration needs a verified DOI or persistent URL and
an exact supporting snippet linked to that claim, with conversion arithmetic
kept separate from the quotation.

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
