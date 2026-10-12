# Isolate Resolver Tests From The Authoritative Corpus

Status: fixed locally; not posted to GitHub.

## Finding

During this batch, `just assign-ids-check` scanned all 15,910 records with IDs
but exited 2 after a temporary `zz_test_resolution_cache_probe.yaml` disappeared
between enumeration and read. The original failure is retained in `corpus.json`
and its referenced log, not overwritten by a retry.

The ignored-inclusive search located the writer in `tests/test_resolve_media_file.py`.
One test created/deleted its probe under the real `research_media.MEDIA_DIR`.
Another deleted a real YAML, then restored its saved text. Besides concurrent
scan failures, that pattern could overwrite a concurrent curator's edit.

## Resolution

Both mutation tests now use a function-scoped `tmp_path` corpus with
`MEDIA_DIR` monkeypatched and resolver caches cleared before/after. The deletion
test creates its own minimal temporary record instead of selecting a real one.
Read-only corpus-backed resolver tests are unchanged. No production resolver
behavior or authoritative recipe is modified by this fix.

All 11 resolver tests pass in the direct focused run. `id-recheck.json` records
the successful serial ID gate for all 15,910 records and resolver-only selection
through `just test-fast` (six passed, one skipped, 11,127 deselected), with exact
corpus inventories before/after and a hash of the changed test file.
See `validation.json` for terminal status. The full fast run passed 9,173 tests
before this test-only isolation change; its result is not represented as a full
rerun of the changed fixture.
