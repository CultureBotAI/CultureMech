# ID↔Label correspondence

A cross-repo invariant for CultureMech, MIM, and CommunityMech.

## The invariant

> Every ontology **ID** must carry its **correct ontology label**, everywhere it
> appears — data **inputs**, **intermediates**, and **data products** (mappings,
> exports, results).

Checking that an ID *exists* in an ontology is **not** sufficient. The label
asserted next to the ID must be the **right label for that ID**. A wrong label
is often the visible symptom of a **wrong ID** — the more serious bug.

## Why this was needed

The previous term validation (`linkml-term-validator validate-data --labels`)
silently passed files with wrong labels, because `--labels` only fires for slots
that declare a LinkML **`binding`** — and no schema had bindings. Demonstration:
corrupting `ENVO:00002046`'s label to `ZZZ_not_sludge_wrong` still reported
"✅ Validation passed". Data products (SSSOM/CSV/KGX) were never label-checked at
all, since no LinkML tool reads them.

## Policy (Hybrid)

| Surface | Field | Required label |
|---|---|---|
| Schema YAML | `*_label` / `term.label` / `ontology_label` | the **canonical** OBO label |
| Products | SSSOM/CSV `*_label` columns | canonical **or** an exact/related synonym |

The schema `label` field holds the **canonical** ontology label. Human / project
/ surface names (abbreviations, formulas like `NaCl`, recipe names) live in
`preferred_term` (or `synonyms` / `notes`), never in the canonical `label` field.

## How it's enforced — two engines

**Engine A — LinkML-native gate (YAML data).** Each schema marks its label slot
`slot_uri: rdfs:label` and gives the term-bearing slot a **range-less**
`binding` (`binds_value_of: <id_field>`). A range-less binding triggers
`linkml-term-validator validate-data --labels` to compare the asserted label to
OAK's canonical label and **fail** on mismatch — without an enum-membership
check (which would require expensive per-ontology tree expansion). ID existence
is covered by Engine B's OAK lookup.

**Engine B — shared OAK validator (products + unified report).**
`scripts/validate_id_label_correspondence.py` is **vendored byte-identical**
across the three Mech repos (same convention as `_edison_capture.py`; verify
with `md5`). It reads `conf/id_label_targets.yaml`, resolves canonical label +
synonyms from the same OAK sqlite adapters the repos already use, and classifies
each `(id, label)` pair: `OK_CANONICAL`, `OK_SYNONYM`, `MISMATCH`,
`ID_NOT_FOUND`, `EMPTY_LABEL`, or `SKIPPED_NO_ADAPTER` (prefix with no adapter,
e.g. `cas:`, `kgmicrobe.compound:`). It runs in `--report` mode (non-failing
TSV) or enforce mode (exit 2).

## Rollout: report → baseline → enforce

Enforcement surfaces existing drift, so it lands in three steps:

1. **Report** — `just report-label-drift` writes `reports/label_drift.tsv`; the
   `label-correspondence` CI workflow runs this **non-blocking**.
2. **Baseline / triage** — fix each row: stale label → write the canonical
   label; wrong ID → re-map the ID.
3. **Enforce** — add `validate-terms-all` + `validate-products` to `qc` and flip
   the CI workflow to blocking.

## Per-repo recipes

| Repo | Engine A (YAML) | Engine B (products) | Report |
|---|---|---|---|
| MIM | `just validate-terms[-all]` | `just validate-products` | `just report-label-drift` |
| CultureMech | `just validate-terms <file>` | `just validate-products` | `just report-label-drift` |
| CommunityMech | `just validate-terms[-all]` | `just validate-products` | `just report-label-drift` |

Engine A and Engine B agree on canonical labels for YAML; Engine B additionally
tolerates synonyms on product surface labels.
