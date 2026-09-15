# Common semantic text map inputs

Includes canonical normalized media and solution records, using stable CultureMech
IDs and their published normalized pages. Text includes names, descriptions,
medium/physical types, recipe components with concentrations and roles, growth
conditions, target organisms with variant scope, applications and preparation
instructions. History, citations, supplier identifiers, ontology IDs and raw
curation notes are excluded. The existing graph map remains a separate view.

Export with `just text-map-inputs --output data/text_map/inputs.jsonl`. Without `--output`, the command validates a preview. `--record` (repeatable repository-relative YAML path) and `--limit` explicitly select canary subsets; ordinary exports cover every eligible record.

Each JSONL row has exactly `identifier`, `label`, `category`, `page`, `source_path`, `text`, `text_sha256`, and `adapter_version`. The text digest is SHA-256 over the exact UTF-8 text. Input order and text are deterministic; duplicate IDs and unreadable records fail. This adapter makes no model call. Common model/projection generation and publication require the fleet pipeline and full-input checks.

Changing provenance-only fields leaves semantic text unchanged. Editing a selected semantic field changes its digest. This text view supplements the existing graph view; it does not alter graph aggregation or its scientific interpretation.

The `page` field is relative to the directory containing the published map
folder: from `text-map/index.html`, the shared renderer uses `../` plus `page`.
This repository publishes the bundle at `pages/text-map/`, so record links omit
the deployment wrapper `pages/` and resolve to its sibling record directories.

## Verified site publication

`conf/text_map.yaml` enables the verified complete input-bound common bundle
selected by `data/text_map/current.json`. `just stage-text-map` validates fresh
full normalized YAML inputs,
the pinned BGE profile and 512-token window, actual PaCMAP and the exact preflight
generation before staging `pages/text-map/`. Invalid enabled prerequisites fail
before site writes; a pointer or manifest replacement is refused before promotion.
`just gen-media-pages` runs this guard first, as does the Pages workflow before
browser data and both normalized/merged page rendering.

The map belongs directly under `pages/`, whose record links are
`normalized/<CultureMech ID>.html`; it must not be placed under
`pages/normalized/text-map/`. The static `app/index.html` card links to
`../pages/text-map/` and stays hidden until successful staging writes the generated
`app/text_map_status.json` status. Disabling the setting clears this status.
Existing derived/direct graph PaCMAP and graph-layout views remain separate.
The shared semantic text map is the primary text view; the retained specialty
graph views keep their own source and projection provenance.

The [locked runtime guide](../conf/embedding-runtime/README.md) documents the
installed Python 3.13 environment and the explicit export, inspect, embed,
project and check commands. Semantic curation requires a matching local
cache-backed map refresh before enabled site checks can pass: export the full
current corpus, update its verified vector cache, rebuild the bundle and run
its freshness check before rendering. Unchanged records reuse matching cache
entries. Model inference is not run automatically in CI, and historical caches
without matching provenance are not silently reused.
