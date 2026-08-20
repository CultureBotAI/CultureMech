# Deep-research artifact contract

What each file a research run leaves behind *means*, and which ones may be cited
as evidence. Introduced by #289, which found that the Mechs disagreed about
citation artifacts and about how a runner is invoked.

## The entity-runner contract

```
just research-entity <provider> <target> [focus] [-- extra args]
```

- **provider** — `claude_code`, `openscientist`, `falcon`, `cborg`, … Aliases
  (`edison` → `falcon`) resolve in `scripts/deep_research_provider.py`.
- **target** — a media YAML path, filename slug, `CultureMech:NNNNNN` id, or
  record `name`. Resolution is the domain-specific part; see
  `resolve_media_file`.
- **focus** — one of the focuses below. Selects the prompt template *and* the
  output label. Defaults to `growth_evidence`.

`focus` is positional here, so **flags must come after it**:

```
just research-entity claude_code ko2_no3 formulation --dry-run
```

`just research-media <provider> <target> [flags]` is the compatibility alias.
Its signature is deliberately *not* the same: it takes **no positional focus**,
because adding one would bind `--dry-run` in
`just research-media claude_code ko2_no3 --dry-run` to the focus. Existing
callers keep working; pass `--focus formulation` through its flags if you need a
non-default focus, or use `research-entity`.

`just research-focuses` prints the table below from the code.

### Passing options to deep-research-client

Client flags go after a `--` separator:

```
just research-entity claude_code ko2_no3 formulation --dry-run -- --max-cost 1
just research-media  claude_code ko2_no3 --dry-run -- --max-cost 1
```

Without the separator, argparse claims the flag as one of the runner's own and
rejects it (`unrecognized arguments: --max-cost`). That is #297, and until it was
fixed no client flag was reachable through the runner at all — the unit tests
missed it because they call `build_command` directly, where passthrough always
worked. The separator itself is stripped before the command is built, so the
child never sees a bare `--`.

### Focuses

| focus | template | question it asks |
|---|---|---|
| `growth_evidence` (default) | `templates/media_growth_research.md` | which organisms are reported to grow on this medium |
| `formulation` | `templates/media_recipe_validation.md` | is this record's formulation right, against authoritative sources |

The names match the focuses in `conf/deep_research_provider.yaml`, which ranks
providers per focus. Before #289 that ranking was disconnected from dispatch, so
`--focus formulation` could rank providers for formulation work and then render
the growth prompt anyway.

Prompts that are steps in a named workflow rather than standing focuses —
`media_stock_solution_research.md` (the #150 cocktail repair),
`media_axis_classification.md`, `medium_organism_recipe_extraction.md` (phase 2)
— are deliberately not focuses. Reach them with an explicit `--template`, which
overrides the focus's template.

### Output paths

```
research/media/<category>/<slug>-deep-research-<focus>-<provider>.md
```

The focus appears even for the default, so a caller can predict the path from
(slug, focus, provider) alone without knowing which focus is default. Two
focuses therefore never collide on one filename.

## Citation artifacts

**One rule: cite from the report's own References section. Nothing else is
evidence.**

| artifact | status | notes |
|---|---|---|
| References section inside the report `.md` | **authoritative** | maps PaperQA keys to DOIs; what a curator reads |
| `deep-research-client --separate-citations` sidecar | **disabled** | not requested; see below |
| `<stem>-citations.md` (Edison path) | **derived** | local best-effort parse of the report, for skimming |

### Why the client's separate-citations sidecar is disabled

It is a regex over the report prose, not structured output from the provider.
CultureMech produced exactly one before this was turned off —
`research/media/algae/2asw-deep-research-falcon.md.citations.md` — and it shows
the failure modes plainly:

- it re-emits the entire ~55-line rendered prompt as "Query", which the report
  already carries as template variables;
- entry 12 of 27 is the bare string `Na+`;
- `10.1101/2024.06.09.598106` is listed three times over, as entries 16, 17 and
  24, differing only in a trailing `.` or `,`.

TraitMech reached the same verdict over a far larger sample (their #249: 353
sidecars, 194 broken markdown-link tails, 2,770 stray trailing commas, and 332 of
353 duplicating a reference two or three times).

It drops a broken duplicate, not a source. Re-enable it only if the upstream
parser is fixed — and re-check against a fresh sample before trusting it.

That one pre-existing sidecar is left on disk as the evidence for this decision.
It must not be read as a citation list.

### Why `<stem>-citations.md` is kept but marked derived

It comes from our own `parse_citations` in `scripts/_edison_capture.py`, not from
the client, and it is regenerated from the report. It is genuinely useful for
skimming a long answer, and an empty file is meaningful — it distinguishes "we
parsed and found nothing" from "we never tried". But it is a parse, so a claim
should always be traced back to the report.

## Provenance artifacts

`<stem>-meta.yaml` records what the run itself produced. Its `sidecar_files`
block reports the sidecars **this invocation wrote**, not whatever happens to sit
in the directory — Edison stems are deterministic, so a rerun lands beside the
previous run's files (#288). A `false` there means this task did not produce that
file, even if a same-named file from an earlier task is present.

## Scope

This documents CultureMech. #289 proposes the same contract fleet-wide; the
other Mechs are tracked in their own repositories.
