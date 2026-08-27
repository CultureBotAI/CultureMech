# CultureMech quick start

Run all commands from the repository root.

## Install and inspect

```bash
uv sync --frozen --extra dev
just --list
```

The repository uses four data layers:

```text
data/raw/                source payloads
data/raw_yaml/           mechanical YAML conversions
data/normalized_yaml/    authoritative curated records
data/merge_yaml/merged/  deduplicated canonical records
```

Do not edit generated `app/data.js` or `pages/` output. See
[Data Layers](DATA_LAYERS.md) for ownership and regeneration rules.

## Inspect and validate a recipe

`data/normalized_yaml/bacterial/lb_medium.yaml` is a tracked example that is
present in a clean checkout.

```bash
sed -n '1,120p' data/normalized_yaml/bacterial/lb_medium.yaml
just validate-schema data/normalized_yaml/bacterial/lb_medium.yaml
```

Ontology and evidence checks are available when their external resources are
configured:

```bash
just validate-terms data/normalized_yaml/bacterial/lb_medium.yaml
just validate-references data/normalized_yaml/bacterial/lb_medium.yaml
```

## Render and browse

```bash
# One ad-hoc page beneath pages/single/
just gen-page data/normalized_yaml/bacterial/lb_medium.yaml

# Complete reproducible web outputs
just build-browser
just gen-pages
just gen-media-pages
just serve-browser
```

Open `http://localhost:8000/app/` after starting the server.

## Run checks

```bash
just test-fast
just test-corpus
just test-integration
just test              # full suite and coverage floor
just validate-strict
just assign-ids-check
just check-id-catalog
```

The fast tier avoids corpus parsing and is intended for immediate feedback. The
corpus tier checks all tracked recipe data. Integration tests cover optional
checkouts, services, and installed-package boundaries and may skip when those
dependencies are absent.

## Make a recipe change

1. Edit a record under `data/normalized_yaml/<category>/` with a round-trip YAML
   editor; do not mechanically reformat unrelated content.
2. Curate the current classification axes:
   `composition_type` (`DEFINED`, `UNDEFINED`, or `SEMI_DEFINED`), optional
   `nutritional_class`, and multivalued `functional_role`. Keep the compatibility
   `medium_type` derived from `composition_type`.
3. Append a `curation_history` entry describing the scientific change and its
   source. Do not rewrite prior history.
4. Run the single-file schema check, `just validate-strict`,
   `just assign-ids-check`, and the relevant test tier.
5. Review `git diff --check` and the YAML diff before committing.

Do not invent a `CultureMech:` identifier. For a new record, leave `id` absent,
run `just assign-ids --dry-run`, review the allocation, then run
`just assign-ids` to apply it.

Continue with the [Contributing Guide](CONTRIBUTING.md) for the record template,
curation rules, and pull-request checklist.
