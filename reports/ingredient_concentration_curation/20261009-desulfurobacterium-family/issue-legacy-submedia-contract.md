# Legacy Submedium Contract Regression

Resolved locally; no GitHub issue was created. The first full fast-tier run is
preserved in `fast.json` and `fast-0.log`: **one failure, 11,758 passes and
16 skips**. The failed test was
`test_target_records_match_komodo_dsmz_submedia_repair_contract` in
`tests/test_repair_komodo_dsmz_submedia_score15.py`.

## Cause

The historical three-record migration test required each current ingredient to
have an explicit concentration matching an old imported/final signature. The
source-reviewed K2027 successor legitimately leaves H2O and NaOH unquantified,
as their exact KOMODO table entries are null. The old signature function raised
`ValueError: ingredient 'H2O' lacks concentration` before checking the signature.
Adding a guessed quantity or VARIABLE merely to satisfy that test would weaken
the scientific result.

## Scoped Fix

The production migration and its strict input guard remain unchanged. The live
record regression test now looks up registered applied source-review chains,
independently audits each successor, and then checks the historical ingredient
signature against the verified pre-repair record. ID and source accession are
checked before and after that inversion. Unregistered or disconnected changes
remain failures; a rehashed record is not a scientific-audit exemption.

Three negative tests rehash deliberately wrong water quantity, evidence snippet
and historical notes, and require independent rejection. A fourth test confirms
that the old mutator rejects the current source-curated record without modifying
it. Existing synthetic migration tests remain intact.

No recipe, source capture or scientific decision was changed to address this
test failure. The original failed receipt is immutable. The successor
`qa-v2.json` passes 75 targeted tests, including all fifteen tests in this module.
The successor `fast-v2.json` passes 11,748 tests, with sixteen skipped.

The repository's unchanged `pytest_collection_modifyitems` assigns an entire
module to the corpus tier when its text contains `data/normalized_yaml`.
Adding the explicit real-record path triggered that rule: the eleven original
tests plus four new tests are now corpus-classified. Thus the fast-tier total
decreased; its green result alone does not prove this regression is fixed.
`legacy-corpus.json` independently confirms all fifteen are collected under
`-m corpus` and **all fifteen pass**. No test was skipped or deleted to close
this issue, and no tier-classifier code was changed.

The separate global merge/freshness failures and all-record work remain open.
