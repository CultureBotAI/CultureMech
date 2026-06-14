# Next Tasks — CultureMech backlog

Deferred work, each entry with enough context to pick up cold. **Maintenance:**
update this file as work is started/finished — move done items out, add new
deferrals here instead of letting them live only in your head or a closed PR.
Keep the cross-Mech items in sync with the sibling repos' `NEXT_TASKS.md`
(MIM / CommunityMech / TraitMech).

Last reconciled: 2026-06-14.

## 1. Phase-2 id↔label enforcement rollout (report-only → blocking)

The id↔label correspondence validator (`scripts/validate_id_label_correspondence.py`,
byte-identical across the Mechs) is live but **report-only**. `validate-terms-all`
and `validate-products` exist in `project.justfile` but are deliberately NOT in
the `qc` gate, and CI only runs the non-blocking drift report.

- Triage first: `just report-label-drift` → `reports/label_drift.tsv`, resolve
  real MISMATCH/ID_NOT_FOUND rows (curate or add justified `exceptions`).
- Then add `validate-terms-all` + `validate-products` to the `qc` recipe and
  flip the CI step to blocking.
- Don't flip the gate while drift rows remain — it will red-wall every PR.

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
