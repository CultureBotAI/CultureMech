# Integration handoff provenance

These `.py.txt` files preserve exact historical helper source as data for
CultureMech issue #687. They are not executable entry points and must not be
reformatted. The current command runner is `scripts/integration_handoff_run.py`.
Runtime requests, streams and receipts remain in the checkout's ignored
`.temp/integration-687-20261119/` directory.

## Archived producer preflight — 2026-11-19

`producer_archive_preflight.py.txt` preserves the exact source executed from
`.temp/integration-687-20261119/producer_archive_preflight.py`.
SHA256: `96f09c050aaa83eb39f48b483ee7fe3e633dc25767c9f15e088a8c03ca8589fa`.
It reads an explicit Git checkout, archive and extracted producer. It compares
archive/extracted bytes and file modes with the selected Git tree, checks the
independently supplied manifest/archive digests, and records runtime metadata.
It does not import or execute archived producer code or modify its inputs.

The exact command and runtime paths are retained in the request and receipt
under `20261119T085335638922Z-producer-archive-preflight/`.
Receipt SHA256: `76b053af7b574415fdddc53c8921a480a89799ac85e89aa973b3b38ec3534d78`.
Output SHA256: `bce0c96ec5d85129e12491e2932368325aea357fffec9c2582a09f9ebaa85608`.
Exit status was 0. All 64,995 Git/archive/extracted files matched; no missing,
extra, content or extracted-mode differences were found.

The subsequent native verification used the unchanged archived
`scripts/ingredient_release_bundle.py` from producer
`6f1b1d18a5528532fa239400bd73c1a040fb78a0`, with the manifest pin obtained
independently from live issue #687:
`ede822e6424433644ae25f363cb5bfb88b154b453c1e954185ecc2c6cb3c829f`.
Its receipt is under `20261119T085407747334Z-archived-producer-verify/`,
SHA256 `fc92fdba3d4711d2453d065c33e4a2377c52156bffc75b115edd7d9a12e0ba06`.
Verification exited 0 with empty stderr. Its output SHA256
`c8911b0c67eaa8ccf3cbed0a9817783dd9e5ad0e305a8f859afe410193912bb4`
exactly matches the separately recorded original M5 native verification.

The producer manifest records Python 3.13.12; replay used Python 3.13.2 with
`-I -B`. All four manifest-listed package versions matched. The verified command
path uses only Python's standard library; aggregation and its local imports were
not run. This is an explicit runtime patch difference, not a claim of identical
runtimes. Verification authenticates this preserved source candidate; it does
not approve scientific mappings or complete the integrated MIM/KGM release.

Two additional executed predecessors are retained exactly as source data:

- `integration_handoff_run.initial.py.txt`: runner used for the initial coverage
  and MIM runtime/native checks. The current executable differs only by removal
  of an unused `sys` import. Historical receipt hashes still bind the old bytes.
- `report_integration_handoff.executed-v1.py.txt`: first accounting report
  producer. Its successor renames the empty-action bucket from `BASE_DIRECT`
  to `NO_CHANGE_ACTION` and explicitly records KGM #1879, native
  `manifest.inputs` binding and the absence of presence/release authorization.
  Counts and partition logic are unchanged. Both output reports and their
  original command receipts remain in ignored durable storage.

These files are historical data, not new operational commands. Do not reformat
or replay them. Current portable commands live directly under `scripts/`.
