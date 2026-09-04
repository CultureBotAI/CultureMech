# Claude Code task: one CultureMech deep-research curation

Work from the CultureMech repository root. Read `CLAUDE.md`, any applicable
`AGENTS.md`, the LinkML schema, and the existing target record before editing.

## Mission

Select exactly one high-value, unanswered culturing-media question, research it
with the `claude_code` deep-research provider, and curate only supported findings
into one schema-compliant `MediaRecipe` YAML record.

The provider's Markdown report is a raw, auditable research artifact. It is not
the schema-compliant result. The accepted findings must also be represented in
the canonical YAML record and pass all relevant validation.

## Non-negotiable constraints

- Use only the `claude_code` provider. Do not run Falcon/Edison, OpenScientist,
  Cyberian, or another provider, and do not fall back to one if Claude Code is
  unavailable. This prevents separate provider-credit spending.
- Run at most one new deep-research job. Before starting it, confirm there is no
  existing Claude Code report for the selected medium. If one exists, select a
  different target rather than paying for a duplicate run.
- Do not expose, print, alter, or commit API keys or `.env` contents.
- Do not modify the LinkML schema to accommodate research output.
- Do not infer growth from recipe composition, a collection accession, strain
  availability, or taxonomic plausibility. A source must explicitly connect the
  organism or strain to growth/cultivation on the named medium or a clearly
  identified variant.
- Prefer primary publications and authoritative culture-collection records.
  Record strain-level evidence when the source is strain-specific.
- Preserve uncertainty. Never invent identifiers, ontology CURIEs, citations,
  quotations, concentrations, conditions, or organism-medium relationships.

## 1. Pick and record the question

Inspect:

- `data/import_tracking/reports/deep_research_priority_top100.json`
- `data/import_tracking/reports/deep_research_priority.json`
- `data/import_tracking/researched_media.json`
- the candidate files under `data/normalized_yaml/`
- existing `research/media/**/*claude_code*` reports, if present

Choose the highest-priority existing recipe that has a meaningful growth-evidence
gap, is absent from the researched manifest for equivalent work, and has no
Claude Code report. State the exact target path and a single answerable question
before calling the provider. Use this form:

> Which explicitly documented organisms or strains grow on **<medium>**, under
> what conditions, and does each source support this exact recipe, the parent
> medium, or a named variant?

Do not edit anything during question selection.

## 2. Confirm provider fit without starting research

Run:

```bash
just deep-research-provider claude_code growth_evidence
```

This is an availability/capability check, not a research job. If it reports that
Claude Code is unavailable, stop and report the blocker. Do not switch providers.

## 3. Run exactly one deep-research job

Run:

```bash
just research-media claude_code <target-yaml-path>
```

Wait for completion. Do not launch a second job. Record the report and citations
paths printed by the runner. Confirm that the report is non-empty and contains
traceable sources. If the runner fails or returns no usable evidence, keep any
diagnostic artifact, make no speculative YAML assertions, and stop with a clear
status.

## 4. Curate the report into the MediaRecipe schema

Compare every candidate finding against the source and the existing record.
Accept only findings with explicit evidence. Use the existing schema and nearby
curated records as the structural authority.

In particular:

- Put supported organisms in `target_organisms` using the narrowest defensible
  taxon/strain identity.
- Distinguish the exact recipe from a parent medium and from `media_variants`.
  If a paper changed composition or conditions materially, model or link the
  variant; do not silently attach its evidence to the parent recipe.
- Attach source identifiers and evidence snippets in the schema's evidence
  objects. Snippets must be short, verbatim, and actually present in the cited
  cached/source text.
- Add growth conditions or metrics only when directly reported and supported.
- Preserve existing correct data and formatting. Make the smallest useful edit.
- Follow the repository's provenance/curation-history convention for an
  LLM-assisted deep-research edit.

The raw report stays under `research/`; the curated result stays under
`data/normalized_yaml/`. Do not add report-only prose as new YAML fields.

## 5. Validate the saved result

Run all of the following against the edited file:

```bash
just validate <target-yaml-path>
just validate-strict <target-yaml-path>
just validate-growth --file <target-yaml-path>
```

If variant links changed, also run:

```bash
just validate-media-variant-links
```

Fix data errors, not the schema or validators. Do not run another research job to
fix validation failures. Inspect `git diff --check` and the focused diff before
finishing.

## Completion report

Report:

1. the research question and why this target was selected;
2. the provider-fit command and the single research command run;
3. raw report/citations paths;
4. canonical YAML path and exactly which claims were accepted or rejected;
5. validation commands and outcomes;
6. any unresolved evidence or identifier uncertainty.

