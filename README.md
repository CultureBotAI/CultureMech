# CultureMech

CultureMech is a versioned knowledge base of microbial culture-media recipes.
It combines LinkML validation, ontology grounding, provenance, deduplication,
browser exports, and static recipe pages.

[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10--3.14-blue.svg)](pyproject.toml)

## Corpus snapshot

<!-- BEGIN GENERATED CORPUS STATS -->
The tracked corpus currently contains **15,877 normalized records** and **6,286 merged records**.

| Normalized category | Records |
| --- | ---: |
| algae | 249 |
| archaea | 743 |
| bacterial | 14,304 |
| fungal | 126 |
| solutions | 0 |
| specialized | 455 |
| **Total normalized** | **15,877** |
| **Total merged** | **6,286** |
<!-- END GENERATED CORPUS STATS -->

These are different layers, not competing recipe totals. Normalized records
preserve source-specific formulations; merged records are deduplicated canonical
outputs. Run `just update-readme-stats` after corpus changes. CI runs
`just check-readme-stats` to prevent this block from drifting.

## Install

CultureMech supports Python 3.10 through 3.14 and uses
[uv](https://docs.astral.sh/uv/) plus [just](https://just.systems/).

```bash
git clone https://github.com/CultureBotAI/CultureMech.git
cd CultureMech
uv sync --frozen --extra dev
just --list
```

## Data architecture

CultureMech has four data layers:

1. `data/raw/` — immutable source payloads.
2. `data/raw_yaml/` — mechanical, source-shaped YAML conversions.
3. `data/normalized_yaml/` — authoritative curated and validated records.
4. `data/merge_yaml/merged/` — reproducible deduplicated records.

The normalized layer is authoritative for source-specific curation and browser
data. The merged layer is authoritative for canonical recipe pages. Generated
`app/data.js` and `pages/` outputs must be rebuilt, not hand-edited or committed.
See [Data Layers](docs/DATA_LAYERS.md) for provenance and regeneration details.

## Common workflows

Validate one tracked record:

```bash
just validate-schema data/normalized_yaml/bacterial/lb_medium.yaml
```

Run repository checks:

```bash
just test-fast          # isolated unit and smoke tests
just test-corpus        # tracked-corpus invariants
just test-integration   # optional checkout/service boundaries
just test               # full suite with coverage floor
just validate-strict
just assign-ids-check
```

Build the browser and recipe pages:

```bash
just build-browser
just gen-pages
just gen-media-pages
just serve-browser
```

Render one recipe while editing:

```bash
just gen-page data/normalized_yaml/bacterial/lb_medium.yaml
```

The output is written beneath `pages/single/`. The renderer is also available as
`culturemech render --file ...` after installation.

## Contributing

Start with the [Quick Start](docs/QUICK_START.md), then read the
[Contributing Guide](docs/CONTRIBUTING.md). New curation uses the orthogonal
`composition_type`, `nutritional_class`, and `functional_role` axes while keeping
the compatibility `medium_type` consistent with `composition_type`. Preserve
round-trip YAML formatting and append a curation-history event for substantive
record changes.

Useful references:

- [Schema](src/culturemech/schema/culturemech.yaml)
- [Quick Reference](docs/QUICK_REFERENCE.md)
- [Data Layers](docs/DATA_LAYERS.md)
- [Unmapped Ingredients Guide](docs/unmapped_ingredients_guide.md)
- [Archived project-status snapshot](docs/archive/PROJECT_STATUS_SUMMARY.md)
- [Archived gas-mapping snapshot](docs/archive/GAS_MAPPING_SUMMARY.md)

Archived documents describe completed work at a point in time; they are not the
current corpus status.

## Ownership, citation, and license

The canonical repository is
[CultureBotAI/CultureMech](https://github.com/CultureBotAI/CultureMech). Use
[GitHub Issues](https://github.com/CultureBotAI/CultureMech/issues) for bugs and
[GitHub Discussions](https://github.com/CultureBotAI/CultureMech/discussions)
for broader questions.

Citation metadata is provided in [CITATION.cff](CITATION.cff). CultureMech is
dedicated to the public domain under [CC0 1.0 Universal](LICENSE).
