---
name: id-label-correspondence
description: Validate that every ontology ID carries its correct ontology LABEL across CultureMech recipe YAMLs and SSSOM mapping products. Uses LinkML schema bindings + linkml-term-validator for term.{id,label} (canonical label) and a shared OAK validator for products. Run report-then-enforce; triage drift as wrong-label vs wrong-id.
category: research
requires_database: false
requires_internet: true
version: 1.0.0
---

# ID↔Label correspondence (CultureMech)

## The invariant

Every ontology **ID** must carry its **correct ontology label**, everywhere —
recipe YAML inputs and the SSSOM mapping products. Checking that an ID *exists*
is not enough; the **label must be the right label for that ID**. A wrong label
often signals a **wrong ID** (the more serious bug).

Policy (**Hybrid**):
- **`Term.label`** (under every grounding slot: ingredient `term`/`chebi_term`,
  organism `term`, environment `term`, cofactor/precursor/substrate terms) must
  equal the **canonical** OBO label (e.g. `CHEBI:32599` → `magnesium sulfate`).
  The source/recipe name lives in the sibling `preferred_term`, not in
  `term.label`.
- **SSSOM `*_label` columns** accept canonical OR an exact/related synonym.

See `docs/ID_LABEL_CORRESPONDENCE.md` for the cross-repo rationale.

## How it's enforced

**Engine A — LinkML-native (YAML).** The schema marks `Term.label`
`slot_uri: rdfs:label` and gives every descriptor term slot a range-less
`binding` (`binds_value_of: id`). `linkml-term-validator validate-data --labels`
then verifies `term.label` against OAK's canonical label and **fails** on drift.

```bash
just validate-terms data/normalized_yaml/bacterial/<file>.yaml   # one file
just validate-terms-all                                          # all recipes
```

(The 3-layer `just validate <file>` recipe already runs this term layer.)

**Engine B — shared OAK validator (products).**
`scripts/validate_id_label_correspondence.py` (vendored byte-identical across
the Mech repos) checks `output/*.sssom.tsv` (`subject_*`/`object_*`) per
`conf/id_label_targets.yaml`.

```bash
just validate-products       # enforce (exit 2 on mismatch / unknown id)
just report-label-drift      # baseline: reports/label_drift.tsv, never fails
```

## Rollout: report → baseline → enforce

The CI gate is **report-only** first (`label-correspondence.yaml` uploads
`reports/label_drift.tsv`, non-blocking) — enforcing surfaces existing drift,
including the many recipe terms with empty `label: ''`.

1. `just report-label-drift` → open `reports/label_drift.tsv`.
2. **Triage** each row (below).
3. Once cleared, add `validate-terms-all` + `validate-products` to a blocking
   CI job (Phase 2).

## Triage: wrong label vs wrong ID

- **Empty/stale label, right ID** → set `term.label` to the canonical OBO label
  (use `scripts/enrich_sssom_with_ols.py` / OLS to fetch it).
- **Wrong ID** → the label names a *different* term; fix the **ID**.
- **`ID_NOT_FOUND`** → obsolete/removed CURIE; re-map (see
  `scripts/remove_invalid_chebi_ids.py`, `scripts/trace_invalid_chebi_sources.py`).

## Surfaces (`conf/id_label_targets.yaml`)

- `data/normalized_yaml/**/*.yaml` (`term.{id,label}`) — canonical
- `output/*.sssom.tsv` (`subject_*`/`object_*`) — canonical-or-synonym

Prefixes without an OAK adapter (`mediadive.compound`, `komodo.medium`, `DSMZ`,
`TOGO`, `ATCC`, `MediaIngredientMech:`, `CultureMech:`, `GTDB`) are reported
`SKIPPED_NO_ADAPTER`.

## Related

- `conf/oak_config.yaml` (OAK adapter map for the term validator),
  `scripts/enrich_sssom_with_ols.py` (OLS label fetch),
  `scripts/remove_invalid_chebi_ids.py`.
