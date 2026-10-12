# Checkpoint Update

The earlier medium-829 run is now terminal. Its
[validation receipt](../20261009-desulfurobacterium-family/validation.json)
records 11,748 fast-tier passes, 75 QA passes and fifteen explicit legacy
corpus-tier passes. Global merge verification/freshness still fail and remain
separate from the repaired legacy-test issue.

The OTEB `validation-preview.json` and its pinned documents remain immutable
pre-application snapshots. Their references to an in-progress medium-829 run
describe that earlier checkpoint; no such run needs to be restarted or polled.
OTEB is now applied locally. Guarded application, readback/no-op, per-record and
corpus checks, index refresh, inverse-audit registration and report
reconciliation are complete. Its fast tier finished with 11,972 passes and
16 skips; all 91 QA tests passed. `validation.json` is terminal and pins the
completed receipts. No old OTEB process needs polling or restarting. Global
merge verification and freshness remain failing.

The 154 OTEB evidence entries are now included in the cumulative applied total
of 35,282. The full 15,910-record objective and GitHub publication remain
unfinished. Medium-436 preparation is read-only and adds nothing to those
counts; its access failure and source conflicts remain explicit.
