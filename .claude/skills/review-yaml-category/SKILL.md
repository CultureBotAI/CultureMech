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
validation commands, structured YAML/Markdown review bundles described below,
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
Review records from this repository's declared corpus, including an exact frozen
snapshot row when the local profile uses that surface. Read
`docs/record-review-profile.md` for the active native review entrypoints, local
rubrics, validators, and maintained input ownership. A curation skill is not a
prerequisite for reviewing a record.

For a generated record, identify the maintained table, overlay, source transform
or seeder that owns a future fix. Do not patch records, generated artifacts,
pages, caches, or cross-repository outputs. Only the new review bundle is written.

Preserve local claim types, priority rules, scoring definitions, and scientific
status/history gates. The shared shape standardizes observations; it does not
replace the Mech's field-by-field rubric or authorize status promotion.

Use the local record-review rubric for individual members. Add explicit cohort
membership, lump/split/retain/defer decisions and systemic findings.
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

## Structured Source Cross-Checks

<!-- canonical:begin structured-source-cross-checks -->
Use structured source adapters before open-ended web search when the cohort
boundary depends on genes, locus tags, UniProt accessions, regulators, pathways,
stress responses, traits, or transcriptomics datasets that may already be
represented in a shared database.

For iModulonDB candidates, first resolve the runner. In the commands below,
`<kg-microbe-sources>` means either an installed `kg-microbe-sources` console
script or `uv run --project <claw-root> kg-microbe-sources` from a local
`culturebotai-claw` checkout. If neither runner is available, record the
structured adapter as unavailable and fall back to inspected iModulonDB source
pages or open web search.

- Run `<kg-microbe-sources> imodulondb datasets` to find covered
  organism/dataset keys.
- Run `<kg-microbe-sources> imodulondb search --organism <organism> --dataset
  <dataset> --query <term>` for member genes, loci, regulators, protein names,
  stress-response terms, or iModulon names that match covered organisms.
- Run `<kg-microbe-sources> imodulondb summarize --organism <organism>
  --dataset <dataset> --k <component>` for iModulon hits that explain a
  repeated evidence or membership pattern.
- Record useful `organism/dataset/component` and `organism/dataset/gene` keys
  under **Evidence Patterns** or **Additional Notes**, and keep any copied
  summary tables small enough to justify why the cohort boundary is or is not
  supported.

iModulon membership is computational expression-module evidence. It can support
a bounded transcriptomic context finding for a covered strain, gene, regulator,
or protein, but it is not direct proof of a phenotype, MIC, natural-product
identity, cell-structure localization, habitat assertion, medium recipe, or
medium-ingredient identity. If no covered organism/dataset matches the cohort,
write that iModulonDB was not applicable; absence from iModulonDB is not
negative evidence.
<!-- canonical:end structured-source-cross-checks -->

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
   `CLAUDE.md`, `justfile`, `docs/record-review-profile.md`, its local rubrics,
   and `docs/record-reviews.md` for the shared output contract.
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
Save one immutable structured review bundle per reviewed cohort
using the CLAW-governed contract in `docs/record-reviews.md` and
`schema/record_review.yaml`. Preserve the local rubric identified by
`docs/record-review-profile.md`.

- Capture actual UTC start/finish, reviewer identity and independence, exact
  target IDs/locators, Git base, input hashes, and generated-input owners.
- Retain every check and its real result, domain assessments, inspected evidence,
  normalized findings, native rules/severity rationale, proposed actions with
  acceptance checks, and explicit limitations. Do not equate a deterministic
  check with scientific review.
- Use `kind: category`; enumerate reviewed members, population and selection,
  and record explicit lump/split/retain/defer decisions with evidence. Sampled
  coverage must retain its method and uninspected remainder.
- Invoke `uv run python scripts/record_review.py inspect --targets <targets.yaml>`
  before assessment, then `validate <completed-review.yaml>` and
  `save --content <completed-review.yaml>` with the same script. Recheck changed
  inputs instead of silently refreshing their hashes.
- The saver writes
  `reviews/structured/<YYYYMMDDTHHMMSSZ>-<slug>/review.yaml` plus `review.md`.
  YAML is authoritative; do not hand-edit the rendered Markdown or overwrite an
  earlier bundle. Run `uv run python scripts/record_review.py check` afterward.
- If required checks are unavailable after the target is resolved, save an honest
  partial/blocked observation. If the shared saver itself cannot run, report
  that persistence is blocked; session-only prose is not a saved review.
- Retain stable issue keys and exact `previous_occurrences` when reassessing a
  finding. A later clean report does not close earlier unresolved findings.
- Do not append curation/history events or promote native scientific status.
  Those require a separately authorized curation change and native gates.

Do not create a report for an unresolved ambiguous target. In the final response,
link both saved files and summarize scope, verdict, findings by severity, and
unavailable checks. Existing ad hoc Markdown is historical, not the output format
for new reviews.
<!-- canonical:end output -->
