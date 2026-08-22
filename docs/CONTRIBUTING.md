# Contributing to CultureMech

CultureMech accepts code, schema, documentation, and curated recipe changes.
Install the locked development environment first:

```bash
uv sync --frozen --extra dev
git switch -c <descriptive-branch>
```

## Know which files are authoritative

- `data/raw/` preserves upstream payloads.
- `data/raw_yaml/` is a mechanical conversion layer.
- `data/normalized_yaml/` is the authoritative curated corpus.
- `data/merge_yaml/merged/` is a reproducible deduplicated output.
- `app/data.js` and generated files under `pages/` are reproducible web assets.

Do not hand-edit or commit reproducible outputs. The full model is documented in
[Data Layers](DATA_LAYERS.md).

## Add or curate a recipe

Media records belong under one of these tracked paths:

- `data/normalized_yaml/algae/`
- `data/normalized_yaml/archaea/`
- `data/normalized_yaml/bacterial/`
- `data/normalized_yaml/fungal/`
- `data/normalized_yaml/specialized/`

Standalone stock-solution records use the schema's `record_kind: SOLUTION` and
are not interchangeable with growth media. Follow an existing record from the
same source/category rather than guessing its representation.

New records should omit `id`; the repository allocator owns the monotonic
`CultureMech:` namespace. Run `just assign-ids --dry-run`, review the proposed
allocation, and only then run `just assign-ids`.

### Current classification model

New curation uses three orthogonal axes:

- `composition_type`: `DEFINED`, `UNDEFINED`, or `SEMI_DEFINED`.
- `nutritional_class`: `MINIMAL`, `RICH`, or `GENERAL_PURPOSE` when supported.
- `functional_role`: a list such as `SELECTIVE`, `DIFFERENTIAL`, `ENRICHMENT`,
  `GENERAL_PURPOSE`, `TRANSPORT`, `ASSAY`, or `ENUMERATION`.

The published `medium_type` compatibility field remains required and derived
from `composition_type`: `DEFINED` maps to `DEFINED`; `UNDEFINED` and
`SEMI_DEFINED` map to `COMPLEX`. Do not put selective/differential/nutritional
claims only in `medium_type`.

### Minimal editing template

Use the schema and a nearby tracked record to determine all source-specific
fields. This excerpt shows the core shape, not a complete scientific recipe:

```yaml
name: example_medium
original_name: Example Medium
category: bacterial
medium_type: COMPLEX
composition_type: UNDEFINED
nutritional_class: RICH
functional_role:
  - GENERAL_PURPOSE
physical_state: LIQUID
ingredients:
  - preferred_term: Yeast extract
    concentration:
      value: "5"
      unit: G_PER_L
curation_history:
  - timestamp: "2026-08-21T00:00:00Z"
    curator: your-github-handle
    action: Added recipe from primary source
    notes: Source identifier or citation and a concise rationale
```

Use real source evidence and real ontology identifiers only. CHEBI labels must
refer to the intended chemical; NCBITaxon identifiers must match the organism.

### Preserve YAML and history

Curated YAML is reviewed as a scientific record. Use `ruamel.yaml` round-trip
loading in mutation scripts so comments, quoting, field order, and unrelated
formatting survive. Every substantive applied change must append a
`curation_history` event. Never rewrite or sort prior history entries.

Commands that can update many records must be report-only or `--dry-run` by
default and require explicit apply intent. Review the proposed paths and diff
before applying.

## Validate your change

For a recipe edit:

```bash
just validate-schema data/normalized_yaml/bacterial/example_medium.yaml
just validate-strict
just assign-ids-check
just test-corpus
```

Run term/reference validation when those parts changed and the external
validators are configured:

```bash
just validate-terms data/normalized_yaml/bacterial/example_medium.yaml
just validate-references data/normalized_yaml/bacterial/example_medium.yaml
```

For code or schema changes:

```bash
just test-fast
just test-corpus
just test-integration
just test
```

The full suite enforces a coverage floor. CI also runs Ruff and Black on changed
hand-written Python, type-checks the renderer boundary, builds the wheel, and
smoke-tests the installed CLI and renderer.

## Pull-request checklist

- The change targets the authoritative layer and contains no generated web output.
- Recipe claims cite an upstream database, primary source, or clearly described
  curator judgment.
- The three current classification axes and compatibility `medium_type` agree.
- IDs came from the allocator and `just assign-ids-check` passes.
- YAML round-trips cleanly and curation history was appended.
- Relevant validations and test tiers pass.
- Documentation links and commands are repository-relative and work from the root.

Open pull requests and issues at
[CultureBotAI/CultureMech](https://github.com/CultureBotAI/CultureMech).
