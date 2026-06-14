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

## 2. Page renderer skip logic ignores template/code changes

`render_media_pages.py` skips a page when its HTML output is newer than the
**source YAML** (mtime-based). It does NOT account for changes to the Jinja
template or the renderer itself, so a template edit silently no-ops under
`just gen-pages` — you must pass `--force` to actually re-render (discovered
2026-06-14 fixing the wall-clock footer).

- Improve: fold a hash of the template + renderer version into the skip decision
  (re-render when either changes), or document the `--force` requirement
  prominently so future template edits don't ship half-applied.

## 3. Cross-Mech validator pin guard covers only the .py (cross-repo)

The `verify-validator-pin` guard pins the validator **script** byte-for-byte
across the Mechs, but NOT the vendored test files or the conf structure, so those
can silently drift. Tracked in culturebotai-claw#6. Coordinate any fix across
CultureMech / MIM / CommunityMech together (and decide whether TraitMech joins
the trio — see TraitMech `NEXT_TASKS.md` item 2).
