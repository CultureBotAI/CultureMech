---
name: review-yaml-record
description: "Review one CultureMech YAML record without editing it: verify identity, source support, evidence placement, completeness, and the exact changes a curator would need. Use when asked to audit, inspect, spot-check, or review a named record. Not for bulk sampling, curation edits, paid research, or GitHub mutation."
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch, Write
metadata:
  category: review
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Review one CultureMech YAML record

- Repository: `CultureBotAI/CultureMech`
- Records: `data/merge_yaml/merged/*.yaml`
- Schema: `src/culturemech/schema/culturemech.yaml`

## The Contract

<!-- canonical:begin the-contract -->
Produce a read-only judgement of one record: what is sound, what is unsupported
or internally inconsistent, what is materially incomplete, and what bounded
checks would resolve the remaining uncertainty.

Reviewing is not curation. A review request authorizes reads, validation
commands, one new Markdown report under the review-report path named below, and
a concise final summary; it does not authorize editing a record, regenerating
products, spending provider credits, contacting anyone, or creating or mutating
GitHub issues, pull requests, comments, labels, or settings.

Resolve exactly one target before judging anything. If a label, slug, or
identifier matches several records, stop and disambiguate; a thorough review of
the wrong record is still wrong.

Read the entire target file before making a finding. Projections, indexes,
rendered pages, and search snippets are useful leads, but they hide context and
cannot support a record-level verdict on their own.
<!-- canonical:end the-contract -->

## Scope

<!-- canonical:begin scope -->
Review only YAML records from this repository's curated record corpus. If a
record is generated from a maintained table, overlay, or source transform,
report the maintained upstream input that owns any future fix. Do not patch
generated artifacts, generated pages, cache files, reports, or cross-repository
outputs to make a reviewed record look correct, except for the new review
report this skill writes.

Use the write boundaries, generated-output warnings, and curation ownership
rules from `.claude/skills/curate-yaml-record/SKILL.md` to decide where a future
fix would belong. For this skill, report that path; do not make the change.

Use `.claude/skills/curate-yaml-record/references/review-checklist.md` as the
field-by-field rubric for this corpus. The checklist is deliberately local: the
shared review shape is the same across the fleet, but claim types and
completeness criteria are Mech-specific.
<!-- canonical:end scope -->

## Evidence Rules

<!-- canonical:begin evidence-rules -->
- Verify every stable identifier, DOI, PMID, ontology CURIE, source accession,
  and internal reference that the record relies on.
- Attach evidence to the narrowest claim it supports. A source that supports
  one definition, member, mechanism edge, ingredient, example, or organism does
  not automatically support the whole record.
- Treat search results, raw research reports, generated summaries, and rendered
  pages as leads. Only inspected source text can support a claim.
- Keep direct quotations short and exact. Interpretation belongs in notes or in
  the review report, not inside quoted snippets.
- Preserve scope. Evidence about one strain, protein, medium formulation,
  habitat, condition, or experiment is not evidence for a broader class unless
  the source makes that generalization.
- Preserve conflicts. If two inspected sources disagree, report the
  disagreement and its scope instead of choosing the convenient one.
- A near miss is not a match. Do not ground a record to a plausible broader or
  adjacent term; leave unsupported identity claims flagged as unresolved.
<!-- canonical:end evidence-rules -->

## Missing Things

<!-- canonical:begin missing-things -->
Before reporting that a record, source file, evidence object, decision row,
overlay, generated product, or referenced artifact is absent, search for the
identifier, label, and slug with a gitignore-independent search such as
`rg --no-ignore --hidden`, `rg -uu`, `grep -r`, or `find`.

Say what the exhaustive search covered. If you used an ordinary ignored-aware
search, call the miss provisional.
<!-- canonical:end missing-things -->

## Workflow

<!-- canonical:begin workflow -->
1. Read the local guidance that names exact validators and write boundaries:
   `CLAUDE.md`, `justfile`,
   `.claude/skills/curate-yaml-record/SKILL.md`, and
   `.claude/skills/curate-yaml-record/references/review-checklist.md`.
2. Resolve one YAML file under the curated record globs named above. Confirm
   its class, identifier, label, source provenance, grounding status, evidence
   entries, discussion or quality flags, generated status, and curation history
   shape.
3. Run the schema, strict, term, reference, and history validators documented
   for this record in this repository. Do not invent a focused validator for a
   category the repository exposes only as a full-corpus check; run the
   narrowest documented validator and report any full-corpus-only, missing
   dependency, cache, network, or skipped check.
4. Verify identity first: confirm the file denotes the requested biological or
   chemical thing, not a sibling, example, variant, source artifact, generated
   copy, or similarly named class.
5. Apply the local checklist claim by claim. For every material assertion, say
   whether the nearest cited source supports exactly that claim.
6. Classify findings by severity:
   **blocker** for wrong identity, invalid YAML, broken references, or a claim
   that makes the record denote the wrong thing;
   **major** for unsupported evidence, wrong ontology grounding, scope
   inflation, a missing required representation, or a systemic curation bug;
   **minor** for style, weak wording, redundant evidence, or non-blocking
   provenance gaps.
7. Report the exact follow-up: which maintained input should change, which
   generator should be rerun, which validator would prove the fix, and which
   uncertainty remains genuinely unresolved.
<!-- canonical:end workflow -->

## Output

<!-- canonical:begin output -->
After resolving exactly one target and completing a review, write exactly one
timestamped Markdown report before the final response:

- Name it `reports/yaml_record_review/<YYYYMMDDTHHMMSSZ>-<record-stem>.md`.
  Use `date -u +%Y%m%dT%H%M%SZ` for the UTC timestamp. Preserve the target
  file stem when it is already filename-safe; otherwise slugify the stem to
  lower-case ASCII words joined with `-`.
- Create `reports/yaml_record_review/` if it does not exist.
- Do not overwrite or append to a prior review. If a filename already exists,
  regenerate the timestamp.
- Keep this section order so review reports are easy to diff across the fleet:

```markdown
# YAML Record Review: <record label>

- Repository:
- Record:
- Started UTC:
- Finished UTC:
- Verdict:

## Target
## Validation
## Identity and Grounding
## Evidence
## Completeness
## Findings
## Recommended Edits
## Follow-up Checks
## Additional Notes
```

Use tables, bullets, or prose inside those headings as the record demands. Put
repo-specific diagnostics, edge cases, and low-signal observations under
**Additional Notes** instead of inventing new top-level sections.

The report must cover:

- **Verdict**: pass, pass with minor issues, or needs curation.
- **Target**: the record reviewed, its path, class, ID, label, and generated or
  maintained status.
- **Validation**: each command run and its result, including unavailable checks.
- **Identity and Grounding**: whether the record's ID, label, category, source
  identity, and ontology grounding agree.
- **Evidence**: supported claims, unsupported or over-scoped claims, and any
  citation or snippet mismatch.
- **Completeness**: consequential gaps, empty optional slots correctly left
  empty, and bounded searches that found nothing.
- **Findings**: blocker, major, and minor findings, each with evidence and a
  maintained owner path for any fix.
- **Recommended Edits**: concrete future curation actions, ordered by severity,
  with the maintained path that owns each fix.
- **Follow-up Checks**: the narrowest validators or manual checks that would
  prove each recommended edit.

Use `None found` or `Not checked: <reason>` when a section has no findings or a
check cannot run; do not delete required headings.

Do not append a curation event, promote a review status, or write a history
entry from this read-only review. Those belong to a later curation change.
If the request needs disambiguation before one target is resolved, ask for it
without creating a report.

In the final response, link the report path and summarize only the verdict,
finding counts by severity, and any skipped validators or unresolved blockers.
<!-- canonical:end output -->
