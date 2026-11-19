# Integration checkpoint — 2026-11-19

This is a bounded source/consumer handoff, not a completed mapping release.
Main baseline: `13c710defa9eddf17dab531f40b915e449f68663`.
Isolated branch: `integration/handoff-687-20261119`.
Durable checkout: `~/agent-work/CultureMech/integration-687-20261119`.
Runtime evidence below is relative to `.temp/integration-687-20261119/` there.
The original main checkout and all accepted packages remain unchanged.

The exact accepted pins, coverage and pending gates are in [README.md](README.md).
The coverage artifact SHA256 is
`65bcfbd9caf9746925f27046825d1e3546819d92d9f407a6964bb9415a2ac763`.
No source inventory was rebuilt and no active MIM input was replaced.

## Environment and archived replays

`uv sync --frozen --extra dev --python 3.13` exited 0 in the isolated checkout.
Python is 3.13.2. Sync stdout is empty; stderr SHA256 is
`312fdb595f5eabba0ce84f4a44c5d9429e586df54635b02a64017fbe5af1723e`.
The accepted producer records Python 3.13.12. Replay used 3.13.2 and the exact
archived source: this is an explicit patch-version difference, not a claim of
identical runtime. The verifier uses only the standard library on this path.

Set `CM_V3` and `MIM_PACKAGE` as described in README, and `CM_PYTHON` /
`MIM_PYTHON` to the verified Python 3.13 interpreters. Actual absolute argv,
working directory, runtime and stream hashes are retained in each request and
receipt. Portable equivalents of the successful native checks are:

```bash
"$CM_PYTHON" -I -B "$CM_V3/producer/scripts/ingredient_release_bundle.py" verify \
  --bundle-dir "$CM_V3/bundle" \
  --expected-manifest-sha256 ede822e6424433644ae25f363cb5bfb88b154b453c1e954185ecc2c6cb3c829f

# Run with cwd "$MIM_PACKAGE/consumer"; archived src supplies the implementation.
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=src "$MIM_PYTHON" -B \
  scripts/adhoc/package_culturemech_intake_1453.py verify --package .. \
  --expected-package-sha256 cf7e1f1434ab2dfc61922a47ae785f474c06cf4f88fbfd76d09e6b55993f70c8
```

| Check | Exit | Durable receipt | Receipt SHA256 |
|---|---:|---|---|
| Producer Git/archive/extracted preflight | 0 | `20261119T085335638922Z-producer-archive-preflight/receipt.json` | `76b053af7b574415fdddc53c8921a480a89799ac85e89aa973b3b38ec3534d78` |
| Archived producer native verify | 0 | `20261119T085407747334Z-archived-producer-verify/receipt.json` | `fc92fdba3d4711d2453d065c33e4a2377c52156bffc75b115edd7d9a12e0ba06` |
| Archived consumer native verify | 0 | `20261119T085234648802Z-mim-consumer-native-verify/receipt.json` | `2bc545a3e99637858091189abb12f9fbecb0f6cc916c4ed4a34cfa4738f60a73` |
| Final coverage accounting | 0 | `20261119T085336820065Z-coverage-accounting-final/receipt.json` | `80c018b1b6a71462676e01d5204c9bcc4f497396e9f411dd232ed143513470c9` |

Preflight matched all 64,995 archived entries against the exact Git producer,
including extracted bytes/modes. Native producer output SHA256 is
`c8911b0c67eaa8ccf3cbed0a9817783dd9e5ad0e305a8f859afe410193912bb4`,
byte-identical to the retained prior M5 result. Native consumer replay verified
all 14,803 package members before and after, returned
`VERIFIED_REVIEWED_SOURCE_INTAKE` and retained 623 supported / 4,384 withheld.
Both native stderr streams are empty. Native consumer temporary rebuilds occur
only in its separate verification package, not the running campaign.

The producer summary is `archived-producer-replay-report.json`, SHA256
`329d79a2b9bea6b46f60059a61c7dbba90881773edd05c26dedc9bb48315db16`.
The independent consumer/coverage review is
`independent-coverage-consumer-review.json`, SHA256
`d14e6e311e25e7b362111a39fcca71d97195daa4282a2c7f85fbf316e3a67db3`.
These are reproducibility/accounting checks, not new scientific approvals.

## Demonstrated fixes and validation

The original verifier accepted 15 malformed-header controls and seven
post-hash product mutations. All 22 expected-rejection regressions failed
before repair; the failed run is retained, not relabeled green.

- Red receipt `gate-regressions-before-fix.json`, exit 1, SHA256
  `684ac49291394e9a0c44d44e400bb30200ea71ef46c1278d0f1053ad0d5abd48`.
- After fixing #801/#802, 85 focused bundle/variant tests passed.
  `gate-focused-after-fix.json`, exit 0, SHA256
  `3525d5553efec208a48d07bc4306cd7b4c5bf2869cb2e34e35c90c491ededae2`.
- Coverage helper tests: nine passed, exit 0; `coverage-report-tests.*`.
  The initial Ruff run found four literal-dict style findings in its new tests;
  those were fixed before final checks and the required fast selection.
- Final five-file Ruff receipt
  `20261119T085542962318Z-final-python-quality/receipt.json`, exit 0, SHA256
  `a71130e62f9aa1e1289000a85a3da1d8aa0180f2404963c95d1821b8e1d9e6ca`.
- Final five-file Black receipt
  `20261119T085543054544Z-final-black-check/receipt.json`, exit 0, SHA256
  `98e6d6dbc6abf7525d9a8ba82b46083154129f49c4a41666a1e7a2c50b6c9675`.

Required `just test-fast` uses the unchanged recipe
`uv run --extra dev pytest tests/ -m fast --no-cov -q`, with `PYTEST_ADDOPTS`
setting an outside-Git basetemp under `~/agent-work/CultureMech/`.
The first run and its corrected successor are recorded below with their actual terminal results.
No test assertion or validator was waived.

## Provenance and remaining work

Exact executed predecessors are preserved under
`scripts/integration_handoff_provenance/` as `.py.txt` data. The initial runner
SHA `6c091c4a0e0c19b8ca85d1dd30d318117b443dd30cc102f4c1cf1722d5233f74`
maps to the current `7219693fcb0918d46d4aa640770c80becf7fd8f329c529c0bc7d6dd0ff8faf1c`
by removal of one unused import. The first accounting helper is SHA
`d6813a65b1a432233bddb440040055ea7325052f10b8d480849a586d2bd4b3cd`;
its final SHA `bcbee74fd008cf83f9cb1e3a3800cf046ff0fe64701c1414c3c924f542a985c4`
adds explicit #1879/non-presence gates and corrects an empty-action summary
label. Both reports and their byte-bound receipts remain intact. The preflight
source SHA is `96f09c050aaa83eb39f48b483ee7fe3e633dc25767c9f15e088a8c03ca8589fa`.
Historical receipt hashes have not been restamped to these successors.

A read-only process observation at 08:56:15 UTC still found PID 47190 running
the native MIM successor application. Receipt
`20261119T085615526351Z-campaign-process-observation/receipt.json`, SHA256
`850bff2827cc51a98daabbd61f5d7a3fec7fccb2de86bb16ba90f9bc20606cd9`.
This observation is not certification of its eventual result. No process was
signalled and no campaign input was mutated or duplicated.

Remaining gates: native-bound accepted-v3/current-KGM reconciliation (#1879),
certified supported/withheld SSSOM and companions, independently pinned KGM
candidate/quarantine, final-artifact canary, paired installation review,
transforms/source receipts/fingerprints/graph validation, and separate owner
merge/publication approval. NTA #792 and other source holds remain separate;
neither this report nor CI converts them to supported scientific assertions.

Independent code/accounting review passed with no material findings:
`independent-code-and-handoff-review-publish-20261119-v2.json`, SHA256
`a8ba7f79812be36b6361d3fc7a8e7863d8f6965c309fcd9ea854c95b63f19889`.
The prior revision is retained. This review explicitly awaited the required
fast result and is not retroactively described as having verified that result.
[CM #803](https://github.com/CultureBotAI/CultureMech/issues/803) records an
inherited broken navigation-link finding; both links now use KGM's verified
`master` branch. Navigation links remain separate from immutable release pins.

The producer replay report retains the provenance README's original SHA256
`8ffd2496407cc0e2d500bfea3f5679e8cede95405eb2209fad64bf81c2726642`.
The current README adds the two subsequently archived predecessors. Its exact
original prefix is preserved at `provenance-readme-before-addendum.md` in the
runtime directory; both independent inspection and SHA256 verify the recovered
prefix. The sealed replay report remains unchanged and is interpreted through
this explicit historical-path relocation.

First required full fast selection exited 1:
**1 failed, 16,357 passed, 23 skipped, 3,700 deselected, two warnings** in
408.72 seconds. Receipt
`20261119T085353491205Z-required-test-fast/receipt.json`, SHA256
`9a6e645b189a4bb17b9a9fc33ff374593723e5c06b8cd109b7d4296fe5778630`.
The only failure was `test_every_saved_structured_bundle_is_valid`: the
historical stage-5 review references Git source commit
`71153bc25dfe85bf0ac858d786aadc52f92d69e2`, absent in the local object database.
This is retained as a failed complete run. The correction restores required Git
objects without changing immutable review bytes, test assertions or scientific
sources; focused review-contract and corrected full-selection receipts follow.

Exact historical-object restoration exited 0:
`git fetch --no-tags --no-write-fetch-head origin 71153bc25dfe85bf0ac858d786aadc52f92d69e2`.
Receipt `20261119T090216316102Z-fetch-missing-review-provenance-71153bc/receipt.json`,
SHA256 `4746aeb1a895dd0fa914fae3fca5d474e1c1a55184bff9a4e018440c9efbc621`.
The post-fetch audit verifies seven required commits and 46 declared committed
blobs; all 56 review YAML hashes, HEAD, refs and FETCH_HEAD are unchanged.
Post-fetch receipt SHA256:
`abf07600b0243845789f9d0934299012bd095e38525527170b4b23cdf261b903`.
The focused review contract then passed all four tests in 11.07 seconds:
`20261119T090246480824Z-record-review-contract-after-history-fetch/receipt.json`,
SHA256 `df7eb951a4f801c8ecf729f3a032213c6f06642c85970e644147bc3ba1e00fb6`.
No source, review or assertion was edited to obtain this result.


The corrected required full fast selection exited **0**:
**16,358 passed, 23 skipped, 3,700 deselected, two warnings** in 387.86 seconds.
Receipt `20261119T090312592121Z-corrected-required-test-fast/receipt.json`,
SHA256 `4deb647eea9c1bf7b28e4a9b76a649c7d8ac18a0204d0f9f94a951bcf3406c85`.
It used the same `just test-fast` recipe and a fresh outside-Git basetemp;
restoring the exact missing Git object was the only intervening environment
repair. No Python implementation, scientific input or test assertion changed
between the complete failed and successful selections. Both deprecation
warnings concern Typer's imports from Click.

The recovery handoff is `review-provenance-recovery-handoff-20261119.json`,
SHA256 `62845d9f447ab320efd21f18ec6fd024970f5c181a6c9f813a36aeaed9d871ff`.
Post-fetch verification is at
`20261119T090235512024Z-review-provenance-after-fetch/receipt.json`.
The independent content/runner review is `independent-final-content-review.json`,
SHA256 `1443e4654a9b85a684f4813cd2eaff1d6d3e31759a1142878c5815ed2c85fb80`.
Its earlier checkpoint subject is preserved byte-for-byte as
`checkpoint-reviewed-before-full-result.md` (SHA256
`e4b4e4b930d477a3f088bed25031306f77ce5f278414abe2b16223698464f92e`).
The earlier code review's guide subject is preserved as
`ingredient-release-guide-before-navigation-fix.md` (SHA256
`40c8821cdc3c5e46f42939edb66c566c774e99068047aac8a0194a6a6adbc8cd`).
Those sealed reviews retain their original pending-test limits. A final frozen
head review and remote PR readback will be recorded separately in durable
runtime evidence and the PR, rather than rewriting earlier attestations.
