# Ingredient release follow-up — 2026-11-13

This records the requested adversarial review of PR #684 and bounded progress
on release tracker #687 and variant-prose issue #683. It does not declare an
integrated mapping release.

## PR #684 review

Independent read-only review filed #688 (large lossless CSV fields) and #689
(fallible cleanup after acceptance). Both were fixed in
`22c46f13ee450d58120a538cb33e9ac74dfe9afb`; independent re-review of that exact
head found no additional material issue. The initial focused run passed 64
tests and exposed one overly large threshold in a new test fixture; correcting
the threshold and rerunning all five new regressions passed. Ruff/Black passed.
The real one-record canary produced 25 groups/occurrences and zero errors, with
successful pinned verification. Its manifest SHA256 is
`9b964d3c4e2bf3bb59a613b66cbf3835e8ab4506e1ce7b805f2f8f8a953f4525`.

The final-code full build and pinned verification passed on that clean head:
15,915 records, 2,506 ingredient groups, 209,330 occurrences and zero errors.
Final manifest SHA256:
`2603186e09d8af74028ff875ed8277ef5d2141a98964c6887134e504f8a61114`.
All five products are byte-identical to the earlier verified full bundle.
All nine final-head CI checks passed. The required GitHub merge queue then
created candidate `dda27db28f1e5f4f05da6d92fbd2cc1bd6e8add3`, whose Git tree
exactly equals the reviewed head's `d2cbe88aac1a530743ad50c2953bdfc8405045e1`.
All nine merge-queue checks passed, and PR #684 merged as that candidate at
2026-11-14 05:18:39 UTC.

Both accepted bundles, canaries and session logs were preserved outside the
retiring worktree in the main CultureMech checkout's
`.temp/ingredient-release-684-preserved/`. The final bundle is under
`output/ingredient-release-final-684/` there. Pinned verification passed again
after relocation. `pr684-producer.bundle` is a verified 23 KB Git recovery
bundle for the branch, requiring the retained base
`7b1d460ce57a66cb7fb10452ecc90e8bc48ee4f9`.

The merged worktree and local/remote
`feat/ingredient-release-bundle-20261113` refs were deleted. Fresh Git and
filesystem checks confirmed their absence; the ignored-file listing before
removal contained only Python/test/lint/coverage caches after evidence
preservation. The other worktrees were retained. Pre-removal `du -sk` reported
1,754,972 KiB for the retiring checkout; net free-space recovery was not measured.

The cleanup helper rechecked content equivalence to the fetched `origin/main`
before branch deletion. Its receipt is in the preserved directory under
`git-recovery/culturemech-variant-prose-683-20261113-211937-ca79b4e/MANIFEST.json`;
`cleanup.tsv` records the Git operations. The ref can be recovered with
`git branch feat/ingredient-release-bundle-20261113 22c46f13ee450d58120a538cb33e9ac74dfe9afb`.
The saved Git bundle supplies those commits if local objects later expire.
The surviving follow-up branch was merged forward from the new main without
conflicts so both inventory workflows are available together.
After removal, the preserved full bundle passed pinned verification from this
surviving checkout as well. The receipt is
`.temp/pr684-preserved-cross-checkout-verification.json`. Issue checks confirmed
#682, #685, #686, #688 and #689 closed; #683 and #687 remain open for the
scientific and downstream release work.

## Exact CultureMech source reconciliation

The helper `scripts/adhoc/compare_mim_culturemech_intake.py` compares declared
source paths and hashes in the native bundle and the frozen MIM intake. It
removes only the leading `data/normalized_yaml/` prefix and rejects duplicate
keys, duplicate normalized paths, malformed hashes and existing output paths.
It does not rehash source recipes or validate scientific dispositions.

The inspected M5 manifest is:

```text
MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5/input-manifest.json
```

Its SHA256 is
`663b95bac7d8bdda39352b50be27439a3b622a3f7c38fdb7c92de5b8a6869bc9`.
The already verified full bundle manifest is
`30c336713f5426c55b4756b298abd1fe959a773422ea1ec24fec05fe040bf4a3`,
produced by clean commit `d28c7c76036558b9352a3ca1b9b442a408d2b14d`.

Comparison found **15,915 matching paths and hashes**, zero missing paths in
either direction and zero differing source hashes. Repeating the comparison
produced a byte-identical receipt, SHA256
`87f6bb97037d91b7ca67dea1172d4f440e42691da080178d60ee5cb3214c1c76`.
The helper's 11 focused tests passed. The downloaded manifest and receipt are
preserved under `.temp/release687/` in this worktree.

The final `22c46f13ee` bundle was compared separately and also matched all
15,915 paths/hashes. Its comparison receipt is
`.temp/release687/final-culturemech-mim-intake-comparison.json`, SHA256
`884bc4168856f8496a767383a86b529324b1ab9d8993815da679657ca651441c`.

The selected MIM campaign has 1,330 CultureMech cases / 2,911 occurrences.
Those are a subset of the full inventory's 2,506 groups / 209,330 occurrences;
source-inventory equality does not imply new mappings for every group.

## MIM checkpoint

At the read-only 2026-11-14 04:28 UTC readiness checkpoint, native stable-ID
adoption had completed (818 operations, 65 retired source paths). Administrative
accounting recorded 412 new IDs, 3,368 total, all 2,956 previous IDs retained,
922 alias associations added and 155 withheld owners left uninstalled. Original
producer verification was still awaiting a terminal result. Scientific review,
final export and validation remained pending.

The existing SSSOM and companion manifest under the stable campaign adoption
worktree were dated Nov 9, predating adoption. They are not evidence of the new
completed campaign export. The recorded KG input revision was
`f10fb3909ed32898a54176ca77e509a950d16b84`, captured Nov 8; its freshness is a
separate release gate. No agent-session input or campaign mutation was made.

The 04:51 UTC refresh supersedes the earlier pending-original-verification
status. Session 11838 exited zero at 04:41:08 with
`COMPLETE_CURRENT_CANDIDATE`, explicitly without adding scientific approval.
The 04:43:43 checkpoint committed the 818 reviewed data paths at
`303a1597c19d2aea978400ff0a1b9ee101ea7f4d` (parent
`4f57a1f3a9ed6b20d2c103c4e7f46d14c6b571f5`); 3,372 maintained outputs matched
and 428 unrelated artifacts were preserved. Postcommit verification session
38419 was active at 04:51:07. The existing export timestamps remained Nov 9.

The original verifier result
`preflight/full-adoption-original-verify-v1/RESULT.json` has SHA256
`9b2d281a57bd582337cd005d3ec523cb2b36e6cd57f85b0b59f6584d1d356d7b`;
`metadata/ledger-history/native-adoption-committed-20261114-v1/checkpoint.json`
has SHA256 `2efca4285043e765e2dbc69d00fad403b42aabca98983455d123930774ae24a3`.
These paths are beneath the same MIM campaign root. The recorded next gates
are successful postcommit verification, ordinary branch push, independently
accepted input-bound bootstrap, scientific correction review and full export
validation. The adoption commit is not a final SSSOM release pin.

The subsequent read-only refresh at 05:08:49 UTC still found verifier 38419 active
at the same HEAD, without a terminal receipt. Terminal 2445 reported expected
warnings and continuing work; scientific review and exports remained queued.
Export timestamps were still Nov 9. Local copies of the two completed receipts
above were checked against their recorded SHA256 values.

At the final 05:22:52 UTC observation, MIM had advanced: verifier 38419 passed
at 05:17:36 with exit zero and `COMPLETE_CURRENT_CANDIDATE`. Commit `303a1597…`
was pushed to `campaign/stable-full-adoption-20261112`, and its remote value
was verified. The 05:20:40 checkpoint is
`FULL_ADOPTION_COMMITTED_NATIVE_VERIFIED_AND_PUSHED`. A separate reviewed
workspace was being prepared; scientific corrections/review, final exports and
validation remained pending. Existing export timestamps were still Nov 9.

The copied postcommit result has SHA256
`756934ddcb1c0df0343d8ec9a845987b6c8d4da0230c728528478af8576f6049`;
the copied `adoption-verified-pushed-20261114-v1/checkpoint.json` has SHA256
`46f6c44b2533c39b60a0dc55ddac4123ab52f7a9a1f2df5ff3c2a83e3f8b5ca1`.
They are retained under `.temp/release687/` beside the earlier receipts.

The subsequent read-only KG audit at 04:42:34 UTC used
`scripts/adhoc/audit_kg_snapshot_freshness.py`. All 95 files declared by the
frozen KG source manifest matched their stored hashes; all 68 declared upstream
snapshot files also matched the campaign KG worktree at `f10fb3909ed32898a54176ca77e509a950d16b84`.
The primary M5 KG checkout at `d6baf5b90003a2032747559d94c00f86a7a4c615`
had 32 matching, 22 different and 14 missing files at those exact paths.
Differences included MediaDive and MetaTraits/GTDB data, mapping tables and
source-finalization evidence. Missing paths included captured generation
artifacts and rebuild evidence, `mappings/mediadive_unknown_dispositions.json`,
and the active pointer `data/raw/mediadive/current.json`. This is not a
repository-wide absence claim. Final PR review filed #693 before correcting
the earlier description, which had called all missing paths evidence files.

The frozen source-manifest SHA256 is
`e2f4252a44aabaffaad7d3d3ca27ac0fb96e50b58939747e095e2ca1b9e3b48e`.
The detailed audit receipt is `.temp/release687/kg-snapshot-freshness.json`,
SHA256 `7ac82fbde5691beff0d4ed7a8103b16b7af3c9df8cd3bcd01e085c98419c33ed`.
Per-file stability and before/after Git HEAD checks observed no concurrent
changes. The audit covers only declared paths, not new upstream sources or
an atomic filesystem snapshot. Therefore the running campaign's frozen KG
input cannot be described as identical to the current primary checkout.
#687 must reconcile that delta before claiming a release includes current KG
unmatched inputs; it must not silently replace the active campaign's intake.

A CSV-aware row comparison at 04:45:39 UTC narrowed the two changed unmapped
tables: MetaTraits has 197 frozen versus 193 current rows; MetaTraits GTDB has
121 versus 117. Each current table removes four rows and adds none. Every
retained row, including `majority_label` and `num_observations`, is unchanged.
The removed trait texts are `builds acid from: maltose hydrate`,
`carbon source: maltose hydrate`, `fermentation: maltose hydrate`, and
`growth: maltose hydrate`. Literal `(trait_name, tax_name)` pairs are unique
within each compared file. This comparison does not establish why those rows
disappeared or whether a reviewed mapping resolved them.

The helper is `scripts/adhoc/compare_unmapped_tsv_snapshots.py`; its receipt is
`.temp/release687/metatraits-unmapped-row-delta.json`, SHA256
`8500d8fc283a3e38e2c5a1d08d0d04bb37f54017dab36d1766f09d0373b5f201`.
Input hashes match the preceding audit. The remaining release decision is to
account for these removals and the other source/mapping/evidence differences,
not to assume these two tables contain newly added unmapped cases.

## Variant prose inventory

`scripts/inventory_variant_prose.py` produces an `UNREVIEWED` queue with one row
per modification and one context-only row for variants without modifications.
It preserves exact modification text, source coordinates/hashes, full variant
context/evidence and record references. It does not infer chemical identities.
The guide and existing `list-ingredients` skill describe the same reusable CLI.

Independent read-only review filed #690 (output within authoritative inputs)
and #691 (manifest read after acceptance) before fixes. The implementation
rejects resolved equal/nested destinations and computes the return receipt
before publishing the acceptance manifest. Full-catalog receipts are recorded
with the follow-up PR after a fresh actual-record canary passes.

The corrected inventory passed 36 focused tests, Ruff and Black. Combined with
the intake comparison, all 47 focused tests passed in the isolated Python 3.13
test environment. Both skill validators and the Just command expansion passed.
The fresh Bold Basal Medium canary retained one variant and all four original
modification texts, including their surrounding evidence and experimental
context. Pinned verification passed against manifest SHA256
`291c69d05b622dc0e2dbf04bd221784a8b1e55ba4dc74368c1344bd2f90103e8`.

The full-catalog plan and build agreed: 15,915 records scanned, 104 records with
152 variants and 396 modification/review rows; no context-only variants occur
in this snapshot. The remaining 15,811 records contribute no variant rows but
remain bound in the input manifest. The queue is 2,976,192 bytes, SHA256
`dd5faea741da0a11e8eb86cad2976e8bf51d42884c601e96973eba61748330ca`.
Bundle `output/variant683-full-catalog/` has manifest SHA256
`fb2c1cbe0e5d165ef2e3366f54098f7bc469e2c5df1a5686a5524e519b582442`;
the implementation is committed at
`ca79b4e99a58bd2b0c54c450a92f6285856a7176`. The source hashes, rather than the
informational checkout revision alone, bind the exact inputs and producer.
Full source-derived verification passed against the independently recorded
manifest digest with `externally_pinned_manifest` assurance.

All nine CI checks passed for follow-up implementation commit `ca79b4e99a`,
including the required `just test-fast` and full corpus/integration suite.
The duplicate local broad run was then interrupted deliberately, retaining
its log: 8,021 passed, 21 skipped, 3,599 deselected and one environment import
failure before interruption. A subprocess removes `PYTHONPATH`; the isolated
test interpreter had not installed the source directory into its site path.
Adding that directory to the isolated `.pth` file fixed the setup; all 254
tests in the affected `test_hajjaj_ingredients.py` module then passed. No
production-code change or failure suppression was used. The completed broad
validation is CI; the interrupted local run is not reported as a full pass.

Only the ignored test environment changed. Its prior site-path configuration
is beside the file as `culturemech-validation.pth.bak-local-source-20261113`;
restoring that backup over `.temp/test-venv/lib/python3.13/site-packages/culturemech-validation.pth`
undoes the environment change. The shared development environment was untouched.

This delivers a reproducible review queue for #683. Scientific disposition of
the prose, any resulting structured recipe edits and later explicit MIM intake
remain open. It is not an inventory of ingredient mentions in every other
notes or protocol field.
