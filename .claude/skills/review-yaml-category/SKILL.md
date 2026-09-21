---
name: review-yaml-category
description: "Review one coherent CultureMech YAML record category or cohort without editing records: resolve membership, lump synonymous sets, split over-broad sets into reviewable cohorts, audit boundary/identity/evidence/completeness patterns, and report exact curation follow-up. Use when asked to audit or review a folder, category, source slice, ontology family, or record set. Not for one named record, curation edits, bulk ingestion, paid research, or GitHub mutation."
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch, Write
metadata:
  category: review
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Review one CultureMech YAML record category

- Repository: `CultureBotAI/CultureMech`
- Records: `data/merge_yaml/merged/*.yaml`
- Schema: `src/culturemech/schema/culturemech.yaml`

## The Contract

<!-- canonical:begin the-contract -->
Produce a read-only judgement of a coherent record category: which records
belong together, which are synonyms or aliases that should be lumped, which
mix unrelated concepts and should be split, which patterns are well supported,
and which future curation changes would make the category sound.

Reviewing a category is not curation. A review request authorizes reads,
validation commands, Markdown reports under the review-report path named below,
and a concise final summary; it does not authorize editing records,
regenerating products, spending provider credits, contacting anyone, or
creating or mutating GitHub issues, pull requests, comments, labels, or
settings.

Resolve at least one bounded, coherent target category before judging anything.
Use the user's words as a starting point, not as an unquestioned file glob: a
category can be a directory, class, enum value, source slice, identifier
namespace, ontology neighborhood, shared prefix, generated batch, or any other
set whose members have the same review question. If the request names a
mixture, split it into coherent cohorts and review each cohort separately. If
different labels, source names, or folders denote the same intended cohort,
lump them before reviewing so duplicates are judged together.
<!-- canonical:end the-contract -->

## Scope

<!-- canonical:begin scope -->
Review only YAML records from this repository's curated record corpus. If a
record is generated from a maintained table, overlay, or source transform,
report the maintained upstream input that owns any future fix. Do not patch
generated artifacts, generated pages, cache files, reports, or cross-repository
outputs to make a reviewed category look correct, except for new review
reports this skill writes.

Use the write boundaries, generated-output warnings, and curation ownership
rules from `.claude/skills/curate-yaml-record/SKILL.md` to decide where future
fixes would belong. For this skill, report those paths; do not make the
changes.

Use `.claude/skills/review-yaml-record/SKILL.md` for the per-record review
rubric and `.claude/skills/curate-yaml-record/references/review-checklist.md`
for repository-specific field expectations. The category review adds a boundary
layer: membership, lumping, splitting, and systemic patterns across the member
records.
<!-- canonical:end scope -->

## Evidence Rules

<!-- canonical:begin evidence-rules -->
- Verify every stable identifier, DOI, PMID, ontology CURIE, source accession,
  and internal reference that a boundary or lump/split finding relies on.
- Attach evidence to the narrowest claim it supports. Evidence that two records
  share a string, directory, or source accession is a lead for equivalence, not
  proof that the biological or chemical thing is the same.
- Treat search results, raw research reports, generated summaries, rendered
  pages, and generated indexes as leads. Only inspected source text can support
  a claim.
- Keep direct quotations short and exact. Interpretation belongs in notes or in
  the review report, not inside quoted snippets.
- Preserve scope. Evidence about one strain, protein, medium formulation,
  habitat, condition, source row, or experiment is not evidence for a broader
  category unless the source makes that generalization.
- Preserve legitimate variants. Hydration states, strains, habitats, media
  variants, source classes, ontology children, and taxon ranks may be separate
  records on purpose; lump only records that evidence shows have the same
  intended identity in this corpus.
- Preserve conflicts. If two inspected sources disagree, report the
  disagreement and its scope instead of choosing the convenient one.
<!-- canonical:end evidence-rules -->

## Missing Things

<!-- canonical:begin missing-things -->
Before reporting that a sibling category, synonym set, record, source file,
evidence object, decision row, overlay, generated product, or referenced
artifact is absent, search for the identifier, label, slug, and any plausible
folder or source alias with a gitignore-independent search such as
`rg --no-ignore --hidden`, `rg -uu`, `grep -r`, or `find`.

Say what the exhaustive search covered. If you used an ordinary ignored-aware
search, call the miss provisional.
<!-- canonical:end missing-things -->

## Workflow

<!-- canonical:begin workflow -->
1. Read the local guidance that names exact validators and write boundaries:
   `CLAUDE.md`, `justfile`,
   `.claude/skills/review-yaml-record/SKILL.md`,
   `.claude/skills/curate-yaml-record/SKILL.md`, and
   `.claude/skills/curate-yaml-record/references/review-checklist.md`.
2. Resolve the requested category into one or more bounded cohorts under the
   curated record globs named above. Record the selection rule for each cohort,
   then enumerate its candidate members from the filesystem. Do not write a
   report for an ambiguous or unbounded set.
3. Search outside the initial candidate list for aliases, duplicate labels,
   adjacent folders, source rows, or ontology siblings that might need to be
   lumped into the review or split out of it. Include ignored and hidden files
   before declaring no sibling exists.
4. Read every member record when the cohort is bounded and tractable. If the
   cohort is too large for full manual inspection, split it into smaller
   coherent cohorts. Use deterministic, explicitly documented strata only when
   the user's question really is a sample or a full read would not change a
   boundary verdict; report the uninspected remainder.
5. Run the schema, strict, term, reference, and history validators documented
   for these records in this repository. Do not invent a focused validator for
   a category the repository exposes only as a full-corpus check; run the
   narrowest documented validator and report any full-corpus-only, missing
   dependency, cache, network, or skipped check.
6. Judge the set before judging individual records:
   membership, duplicates, over-split singleton groups, over-broad groups,
   source artifacts, ontology-parent drift, generated-copy drift, and records
   whose identifiers, labels, classes, or evidence put them outside the
   resolved boundary.
7. Apply the per-record checklist to the members that drive the category
   verdict. Promote repeated per-record findings into systemic findings when
   the same generator, source transform, routing table, or schema pattern owns
   them.
8. Classify findings by severity:
   **blocker** for a category boundary that denotes the wrong kind of record,
   a merge/split error that makes records incorrect, invalid YAML, or broken
   references;
   **major** for unsupported category membership, wrong ontology grounding,
   scope inflation, missing required representations, generated systemic
   errors, or duplicate records with the same intended identity;
   **minor** for style, weak wording, redundant evidence, or non-blocking
   provenance gaps.
9. Report the exact follow-up: which maintained input should change, which
   generator should be rerun, which validator would prove the fix, and which
   uncertainty remains genuinely unresolved.
<!-- canonical:end workflow -->

## Output

<!-- canonical:begin output -->
After resolving at least one coherent target category and completing a review,
write one timestamped Markdown report per reviewed cohort before the final
response:

- Name each report
  `reports/yaml_category_review/<YYYYMMDDTHHMMSSZ>-<category-slug>.md`. Use
  `date -u +%Y%m%dT%H%M%SZ` for the UTC timestamp. Preserve the category slug
  when it is already filename-safe; otherwise slugify it to lower-case ASCII
  words joined with `-`.
- Create `reports/yaml_category_review/` if it does not exist.
- Do not overwrite or append to a prior review. If a filename already exists,
  regenerate the timestamp.
- Keep this section order so review reports are easy to diff across the fleet:

```markdown
# YAML Category Review: <category label>

- Repository:
- Category:
- Selection Rule:
- Started UTC:
- Finished UTC:
- Verdict:

## Target Category
## Selection and Membership
## Validation
## Lump and Split Review
## Identity and Grounding
## Evidence Patterns
## Completeness Patterns
## Findings
## Recommended Edits
## Follow-up Checks
## Additional Notes
```

Use tables, bullets, or prose inside those headings as the category demands.
Put repo-specific diagnostics, edge cases, and low-signal observations under
**Additional Notes** instead of inventing new top-level sections.

The report must cover:

- **Verdict**: pass, pass with minor issues, or needs curation.
- **Target Category**: the resolved cohort label, source request, selection
  rule, member count, and whether coverage was full, split into subcohorts, or
  sampled.
- **Selection and Membership**: every included record path and every excluded
  near miss that explains the boundary.
- **Validation**: each command run and its result, including unavailable checks.
- **Lump and Split Review**: synonyms, duplicate identities, over-split
  variants, over-broad groups, singleton smells, and legitimate siblings that
  should remain separate.
- **Identity and Grounding**: whether the members agree on class, identifier
  policy, label shape, source identity, ontology grounding, and internal
  references.
- **Evidence Patterns**: supported category-level patterns, unsupported or
  over-scoped source usage, and citation or snippet mismatches that recur.
- **Completeness Patterns**: consequential gaps, empty optional slots correctly
  left empty, and bounded searches that found nothing.
- **Findings**: blocker, major, and minor findings, each with evidence,
  affected paths, and a maintained owner path for any fix.
- **Recommended Edits**: concrete future curation actions, ordered by severity,
  with the maintained path that owns each fix.
- **Follow-up Checks**: the narrowest validators or manual checks that would
  prove each recommended edit.

Use `None found` or `Not checked: <reason>` when a section has no findings or a
check cannot run; do not delete required headings. If only a sample was read,
the verdict must say `sampled` and must not claim full-category coverage.

Do not append a curation event, promote a review status, or write a history
entry from this read-only review. Those belong to a later curation change.
If the request needs disambiguation before a coherent category is resolved, ask
for it without creating a report.

In the final response, link every report path and summarize only each verdict,
finding counts by severity, and any skipped validators or unresolved blockers.
<!-- canonical:end output -->
