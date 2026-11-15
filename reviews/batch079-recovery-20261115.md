# Bounded batch079 recovery checkpoint

The completed scientific assessments cover exactly recovered records 07, 08 and 10. All three immutable pairs were independently cleared within their **needs_curation** scopes. The findings remain open; neither native validation nor this publication makes the recipes scientifically acceptable for export or release.

| Record | Target | Saved review | Open findings | Follow-up |
|---|---|---|---|---|
| 07 | CultureMech:002034 | [YAML](structured/20261115T080257Z-batch079-record07-desulfothermus/review.yaml), [Markdown](structured/20261115T080257Z-batch079-record07-desulfothermus/review.md) | 2 blocker, 3 major, 1 minor | [#749](https://github.com/CultureBotAI/CultureMech/issues/749) |
| 08 | CultureMech:001490 | [YAML](structured/20261115T081711Z-batch079-record08-desulfotignum/review.yaml), [Markdown](structured/20261115T081711Z-batch079-record08-desulfotignum/review.md) | 2 blocker, 2 major, 2 minor | [#750](https://github.com/CultureBotAI/CultureMech/issues/750) |
| 10 | CultureMech:009942 | [YAML](structured/20261115T082226Z-batch079-record10-desulfotomaculum/review.yaml), [Markdown](structured/20261115T082226Z-batch079-record10-desulfotomaculum/review.md) | 3 major, 1 minor | [#751](https://github.com/CultureBotAI/CultureMech/issues/751) |

The recovery source baseline is `dda27db28f1e5f4f05da6d92fbd2cc1bd6e8add3`, including merged #684. Work remains isolated on `recovery/batch079-native-20261114`; canonical main and scientific YAML files were not edited. Record 10's lowercase J547 counterpart is context only, not an additional merge owner.

## Current publication policy and issue #752

The owner's later instruction supersedes the earlier bundle-only plan. This PR includes the review-producing and check-capture helpers, superseded source versions, provenance documentation and this checkpoint. The earlier plan remains in immutable record 08 notes and historical authoring-script strings as an accurate record of draft-time intent. Those statements are not current publication policy. This reconciliation addresses [#752](https://github.com/CultureBotAI/CultureMech/issues/752); no prior review is restamped or rewritten.

Commit `71d94151e0090b8f99cb828cb94e36ee53ed0156` preserves the eight retained helper files before publication formatting. Earlier executed versions were recovered from literal creation/edit commands in the retained session transcript, with deterministic transformations explicitly distinguished from literal copies. The [provenance manifest and README](../scripts/batch079_provenance/README.md) map exact historical hashes, runtime paths, execution evidence and current versions. Historical source-text archives are immutable data; current executable Python helpers receive the changed-Python Ruff/Black checks. Import ordering, unused-import removal, two equivalent set comprehensions and one owner-variable rename do not change scientific decisions. Original helper bytes remain available in Git history and the source archives. The later top-of-file provenance headers identify purpose, required inputs, outputs, date and issue/task context for all nine current executable helpers. These documentation-only successors passed module-docstring-excluded AST comparison, Ruff and Black after the successful required fast run; the existing portability-guard module also passed all 1,017 cases. No further full fast suite was run. Original execution hashes and saved reviews are not restamped. The pre-header manifest is retained at `.temp/batch079-scientific-20261114/helpers-pre-provenance-headers/manifest.json` (SHA256 `f04d3e02897ba735114ff0237a4acc7a48ba989ef47b25c166e2d73536c10fd5`).

These are task-specific provenance artifacts, not reusable scientific-review APIs. They contain frozen decisions, source hashes and run-specific paths. Re-running an authoring helper is not a fresh source assessment. A new independent checkout can inspect the published code, exact historical source text, immutable reports and input hashes. Reproducing authoring also requires the retained raw captures, original streams, peer artifacts and matching environment under ignored `.temp/batch079-scientific-20261114/`. Source captures and complete private session transcripts are not published. The manifest contains only the scoped extracted code and transcript provenance references.

## Environment and validation

The checkout-local environment uses Python 3.13.2, established with `uv sync --frozen --extra dev --python 3.13`; interpreter/import origins and unchanged lock bytes were verified. The lock SHA256 is `9848d8c59d7162ee7a1e3a29b6318768ed613a8920e196b2e976a89ba9a11f55`. Runtime receipts are `environment-sync.json` and `20261115T075601984823Z-environment-origins.json` under the ignored run directory.

Each selected generated target passed the documented schema, strict-schema, term and reference checks. Strict validation scanned one file at the schema layer. **Every reference check inspected zero evidence assertions.** Record 07 was verified before 08, and 08 was saved and its persisted check verified before 10. The final persisted check reports 45 valid reviews in their declared scopes, and the native review-contract test reports 4 passed. No validator was waived.

The initial `just test-fast` run was interrupted: exit 2, 4,130 passed, one failed, seven skipped and 3,599 deselected. Its observed failure expected a temporary tree outside Git, but this task's durable `TMPDIR` was inside the checkout. That exact test passed separately with a unique durable `--basetemp` outside Git (one test, exit 0); [#753](https://github.com/CultureBotAI/CultureMech/issues/753) records the configuration finding. No test assertion was weakened.

The first complete required fast selection used the same `pytest tests/ -m fast --no-cov -q` arguments with an outside-Git basetemp. It finished with exit 1: **15,960 passed, one failed, 150 setup errors, 23 skipped and 3,599 deselected**. The failure identified a workstation path in the new record10 helper ([#754](https://github.com/CultureBotAI/CultureMech/issues/754)). Its current executable successor requires `--original-native-dir`; the exact original builder and all saved review attestations are preserved. This is a functional path-configuration repair in addition to the earlier formatting changes.

All 150 setup errors came from four fixture modules reading historical commit `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`, which was absent from this shallow clone at that run. An exact-object fetch with `--no-tags --no-write-fetch-head` restored the required history without moving a branch or editing scientific files. The four affected fixture modules plus the complete portability-guard module then passed: **1,182 passed, exit 0**. The subsequently authorized corrected required fast selection completed successfully: **16,111 passed, 23 skipped, 3,599 deselected, two warnings, exit 0** in 318.93 seconds. It retained the documented `pytest tests/ -m fast --no-cov -q` selection and used a new outside-Git basetemp. All earlier failed/interrupted attempts and their actual streams remain retained. No full `just test`, scientific-validator repeat or unrelated recipe repair is claimed.

The [machine-readable checkpoint](batch079-recovery-20261115.json) pins the canonical native receipts, review pairs, helper versions and source archives. Full command/exit/stream histories and current publication state are in the append-only ignored checkpoint files, selected by `.temp/batch079-scientific-20261114/CURRENT.md`. Final frozen-head diff review is a separate publication check; scientific review of the three pairs has already cleared.

## Remaining scientific and source limits

Record 07 still needs stock/dose representation, chemical-form and preparation/source-equivalence curation; its exact KOMODO source remains unavailable. Record 08 still needs the 383/383a output boundary, stock stages and grounding corrected, with a qualified variant rationale and re-evaluated metal total. Record 10 still needs generated volume/preparation freshness and source-supported percentage basis; current direct TOGO corroboration timed out and peptone-specific origin/processing remains unconfirmed. The primary JCM source supports the 121°C/15-minute default. API-derived 990-mL concentrations were not adopted.

Existing historical 01–06 and09 receipts and all prior committed reviews are preserved; 26 historical artifact pins were independently rechecked. Failed attempts, alias-producing drafts, shallow-clone diagnostics, unsupported list-flag output, and source timeouts remain available. There is no full-batch completion claim.

PR #692 remains a separate draft: last independently verified head `02e005db42246b8a04ece9df4b5657e036fa5697`, containing684 and nine green checks. Its scientific/source/export/KG-Microbe admission gates were not waived or changed. The historical Documents EPERM is separate from completed authorized SSH technical checks and the usable agent-work checkout. No permissions change, merge, force push, cleanup, paid research, historical batch publication or catalog-loop continuation occurred.


## PR755 CI follow-up: issue756

The full corpus job at 61d501fd9eff12a387a2e013a7f983801d9a9809 failed only
the existing corpus-writer width guard: 19,732 passed, 25 skipped and one failure.
The three offending calls write review drafts, not corpus records. Removing
their explicit width keywords leaves the broad guard intact. The original
[failed job](https://github.com/CultureBotAI/CultureMech/actions/runs/43696509390/job/132758127461)
remains failed; [issue756](https://github.com/CultureBotAI/CultureMech/issues/756)
records this bounded correction.

The saved read-only verifier confirmed that each builder's only AST change is
removing its width keyword and that old/default serialization of the saved
review payload yields equal parsed content. It also verified that saved reviews,
historical archives and manifest, scientific data and the corpus guard are
unchanged from the failed candidate. The complete record-IO, review-contract and
portability modules passed 1,032 tests in 22.89 seconds. Native saved-review
validation reports 45 valid reviews in declared scopes; Ruff and Black passed.
The machine-readable checkpoint separately pins all five new check receipts,
their streams and the 10 current helpers. Historical review assertions are not
restamped. Full local suites were not repeated; full CI on the new head remains
required, and no merge is authorized by these checks.
