# Checkpoint Update

The earlier medium-829 run is now terminal. Its
[validation receipt](../20261009-desulfurobacterium-family/validation.json)
records 11,748 fast-tier passes, 75 QA passes and fifteen explicit legacy
corpus-tier passes. Global merge verification/freshness still fail and remain
separate from the repaired legacy-test issue.

The OTEB `validation-preview.json` and its pinned documents remain immutable
pre-application snapshots. Their references to an in-progress medium-829 run
describe that earlier checkpoint; no such run needs to be restarted or polled.
No OTEB YAML has been applied. The next action is guarded six-record
application followed by actual readback/no-op, record/corpus/merge checks,
index refresh, inverse-audit registration and report reconciliation.

Do not count the 154 proposed evidence entries as applied. The full 15,910-record
objective and GitHub publication remain unfinished.
