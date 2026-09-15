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
