# Next Tasks — CultureMech backlog

Deferred work, each entry with enough context to pick up cold. **Maintenance:**
update this file as work is started/finished — move done items out, add new
deferrals here instead of letting them live only in your head or a closed PR.
Keep the cross-Mech items in sync with the sibling repos' `NEXT_TASKS.md`
(MIM / CommunityMech / TraitMech).

Last reconciled: 2026-06-14.

## 1. Phase-2 id↔label enforcement rollout (report-only → blocking) — DONE

**Done** (2026-06-14): the drift backlog was triaged to zero and the gate flipped
to blocking. The `label-correspondence` CI job now builds the SSSOM product, then
runs `just validate-products` (Engine B) as a **blocking** step; `qc` does the
same locally. Recipe id↔label is clean (0 MISMATCH / ID_NOT_FOUND / EMPTY_LABEL;
`jcm.grmd` ignored), and `generate_sssom_mappings.py` emits canonical object
labels so the product is drift-free by construction.

Note: Engine B (single-process) is the gate. `validate-terms-all` (per-file
linkml-term-validator, Engine A) is **deliberately NOT in CI/qc** — it reloads
the schema+OAK per file (~hours over the full corpus) and re-checks the same
canonical-label surface Engine B already enforces in one pass; keep it as a
targeted dev tool (`just validate-terms <file>`).

## 2. Page renderer skip logic ignores template/code changes — DONE

**Done** (2026-06-14): `render_media_pages.py` now folds a build signature
(sha256 of `media.html.j2` + the renderer source, 12 hex chars) into the skip
decision and embeds it in each page (`<!-- culturemech-build-sig: … -->`). A
page is skipped only when it is fresher than its source YAML AND carries the
current signature; editing the template or the renderer changes the signature
and forces a re-render under `just gen-pages` — no `--force` needed. Verified:
edit template → all pages re-render.

## 3. Cross-Mech validator pin guard covers only the .py — DONE (CultureMech + MIM)

**Done** (2026-06-14, culturebotai-claw#6 Option 1): `verify-validator-pin` /
`refresh-validator-pin` now pin the full vendored set via a `VENDORED_IDLABEL_FILES`
manifest — the validator `.py` **plus** the two byte-identical shared tests
(`tests/test_id_label_empty_adapter.py`, `tests/test_id_label_unknown_prefix.py`).
The pinned hashes are byte-identical across CultureMech (PR #64) and MIM
(MIM PR #64), so the two guards jointly enforce the cross-repo invariant; editing
a vendored test now fails CI. `conf/id_label_targets.yaml` is left **unpinned** —
it is intentionally per-repo (different adapters/targets/exceptions).

Remaining (lower priority): CommunityMech's checkout does not currently vendor the
validator + tests (so it's a 2-repo invariant today); fold it (and decide on
TraitMech) into the next coordinated sync if/when it adopts the validator.
