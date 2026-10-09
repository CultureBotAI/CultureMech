# Structured Record Reviews

CLAW owns `schema/record_review.yaml` and `scripts/record_review.py`. The schema
defines the common record; the helper enforces its semantic constraints and
saves an immutable pair:

```text
reviews/structured/<YYYYMMDDTHHMMSSZ>-<slug>/review.yaml
reviews/structured/<YYYYMMDDTHHMMSSZ>-<slug>/review.md
```

YAML is authoritative. Markdown is rendered from it, not a second editable
verdict. New reviews use this format; old reports remain historical evidence
and are not automatically converted. A valid report does not certify scientific
truth or authorize curation, Git publication, paid research, or status promotion.

Read `docs/record-review-profile.md` for this Mech's entrypoints, local rubrics,
input ownership, validators, and any native scientific-status gates. Preserve
those domain rules; this contract standardizes their output, not their science.

## Capture And Save

Use the repository's Python environment with LinkML, linkml-runtime, jsonschema,
and PyYAML installed. Missing dependencies are a blocked output step, not
permission to save unvalidated prose instead. From the repository root:

```bash
uv run python scripts/record_review.py inspect --targets /tmp/review-targets.yaml
uv run python scripts/record_review.py validate /tmp/completed-review.yaml
uv run python scripts/record_review.py save --content /tmp/completed-review.yaml
uv run python scripts/record_review.py check
```

The temporary input locations are illustrative; choose session-unique paths.
`inspect` takes a mapping with a nonempty `targets` list. Each target uses the
schema's `ReviewTarget` fields: stable `target_id`, repository-relative `path`,
`label`, `kind`, and `owner_paths` (repository/path/role) or an explicit
`ownership_note`. Include an exact `selector` for a frozen snapshot row. Add
`--input <path>` for each schema, overlay, source table, or other local input
whose bytes informed the review. Inspect before judging; retain the resulting
Git base and SHA-256 input hashes in `source`. Inspection is not a saved review.

Read the actual input bytes. For a generated record, identify the maintained
table, overlay, source transform, or seeder that owns a future fix. Include an
algorithm-labelled `semantic_digest` when the native Mech gate uses one; raw
file hashes and semantic hashes serve different purposes.

Author a complete document against `RecordReview` in the schema:

- Identity: `schema_version: 1.0.0`, timestamp-prefixed `review_id`, `kind`,
  repository, title, actual UTC start/finish, reviewer identity and independence
  basis, invoking skill, completion, verdict, scientific-review flag, summary.
- Scope: exact selected targets, selection rule, population denominator,
  actually reviewed target IDs, full/sampled/partial coverage, exclusions.
  Sampling requires its method and limitations; retain seed/strata where used.
- Checks: actual documented commands, actual exit codes, required status,
  result, targets, and evidence. Do not execute commands copied from an old
  report. Distinguish failed, skipped, unavailable, and not applicable.
- Evidence: stable local IDs, source reference, precise locator, actual access
  timestamp, support/refutation/context, and what was inspected. Record bounded
  search scope, including whether ignored files were searched, for absence
  findings. Search snippets and expression-module membership are not proof of
  experimental mechanism.
- Assessments: common area plus a domain-specific topic, outcome, targets,
  evidence, summary, optional detailed prose and metrics. Every reviewed target
  must be assessed. Scores need units, definitions, denominators where relevant,
  and scales; do not equate scores across Mechs just because both are percentages.
  Use evidence-linked `dimensions` (name, value, definition, evidence IDs) for
  structured domain context such as strain, criticality authority/edition,
  biomass state, source category, taxon rank or evidence tier. Prose details may
  remain flexible without losing these important triage coordinates.
- Findings: local ID, stable repository-scoped `issue_key`, category, severity,
  status, certainty, affected targets and field paths, evidence, owner paths,
  and description. Preserve local rule IDs and native severities with an
  explicit normalization rationale. Do not reuse an issue key for an unrelated
  defect. Use `related_findings` for similarities across repositories.
- Actions: affected findings and targets, maintained owners, concrete acceptance
  checks, optional generator, dependency IDs, and blocking finding references.
  These are proposed work, not a record that the fix was already performed.
- Category boundaries: explicit lump/split/retain/defer decisions, evidence,
  rationale and proposed membership. A split is a complete disjoint partition;
  a lump requires at least two targets. Similar names alone do not prove identity.
- Explicit limitations and optional notes, tags, links and related reviews.
  Empty `findings: []` means no findings in this scope, not a fleet-wide pass.

Use `kind: record` for one record, `category` for a coherent cohort with a
boundary decision, `batch` for an explicit sample/batch, and `repository` for a
bounded repository-level inspection. Unresolved identity or an ambiguous target
needs clarification before a report is created. Once a target is resolved,
retain a partial/blocked review when required checks cannot run. A process crash
or provider failure without assessed content is not a completed review.

Use current UTC times, not a historical filename's timestamp. On an ID collision,
choose a new suffix; never overwrite an earlier review. Saving verifies origin,
Git base, hashes, path safety and Git visibility. If inputs changed, inspect and
reassess the changed content; do not merely replace the old hashes. A deliberately
historical review can use `source.state: git_commit` with exact tracked bytes.
It must say it assesses that revision, not the current working tree.
On ingestion, the base commit must still be available. A `git_commit` review's
hashes are checked against that historical tree, not today's files. A
`working_tree` review preserves the reviewer's input-byte attestation; it is not
proof that those bytes were committed. Invalid or unverifiable provenance is
reported as an error and cannot retire a previous finding.

The saver publishes YAML only after Markdown and input rechecks succeed. It
does not stage or commit either file. `check` includes hidden/ignored existing
bundles and fails on mismatched, malformed or incomplete pairs. No saved reviews
is reported as missing coverage; `check --require-reviews` makes that an error.

`check --base <revision>` also rejects deletion or byte changes to previously
committed bundles. The default is `RECORD_REVIEW_BASE` when configured, otherwise
`HEAD`. CI must set that variable to the trusted pull-request, merge-group or
push event base and fetch that revision; checking against an already changed
HEAD cannot detect a committed rewrite. Unknown bases fail rather than silently
skipping the check. The canonical consumer test uses the same base. Correct a
review by adding a new linked observation, never by rewriting its history.

## Verdict And Severity

Use `pass`, `pass_with_limitations`, `needs_curation`, `seed_only`, `blocked`,
or `not_assessed`. Preserve a Mech-specific verdict in `native_verdict` if needed.
`completion` is separate from the scientific verdict. Deterministic validation
and seed metadata use `scientific_review: false`. Provenance-only inspection
must explicitly say literature support was not reassessed.

- Blocker: wrong identity, invalid representation, broken critical references,
  or a defect that makes the record denote the wrong thing.
- Major: materially unsupported claims, wrong grounding, scope inflation,
  missing required representation, or systemic source/generator errors.
- Minor: bounded, non-blocking wording, redundancy or provenance problems.
- Informational: a scoped observation that does not require a corrective edit.

Passing verdicts cannot conceal unresolved major/blocker findings or failed
required checks. Unavailable required checks preclude completed status. Report
limitations instead of silently dropping checks or broadening sample results.
Every passing target needs a positive, evidence-linked assessment. An unknown
or concerning assessment precludes plain `pass`; a qualified pass must state
its limitations and still positively assess each actually reviewed target.
Do not promote native record status or append curation/history events merely
because the review document validates.

## Triage And Follow-Up

Each review is a new observation. To change a finding's disposition, retain its
`issue_key` and cite exact repository/review/finding identities in
`previous_occurrences`. Resolved, rejected and accepted-risk findings require
that history, inspected evidence, and a disposition reason. A newer clean
review does not close an older issue. Multiple conflicting heads stay visible
until a new observation explicitly reconciles all relevant predecessors.
Every successor, including an open or deferred update, must retain all affected
targets of each predecessor it supersedes. A failed review cannot make a
terminal disposition. A partial review can resolve a scoped finding only when
its affected targets were actually reviewed and assessed against evidence.

From a configured CLAW checkout, aggregate without modifying Mechs:

```bash
kg-microbe-reviews fleet --all --format markdown --output /tmp/review-triage.md
kg-microbe-reviews fleet --all --status open --severity major --format tsv
```

The default reads each local cached `origin/main` commit, not uncommitted reports,
and never fetches. Use the normal fleet refresh workflow separately when remote
freshness is required. `--working-tree` includes local reports, including ignored
ones. Every manifest target remains in the inventory, even if unavailable or
without structured output. JSON retains all evidence and action history; the
Markdown/TSV views are summaries. Filters never bypass validation or hide lineage
errors. Current input hashes indicate whether the observed source surface still
matches, changed, or could not be established, not whether the science is true.
Currentness remains visible for closed findings as well as open ones. Action
plans come from unresolved finding heads and their prerequisite closure; they
are proposed work with execution status not established, not completed tasks.

Link the saved Markdown and YAML in the final response. Summarize the declared
scope, verdict, finding counts, and unavailable checks. Do not create GitHub
issues or curate records unless separately requested.
