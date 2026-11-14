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

The final-code full build, final-head CI and merge/cleanup receipts are recorded
on PR #684 and the release tracker once those operations complete. The previous
full build is retained as historical evidence at its original producer commit,
not relabeled as a build of the later fixes.

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

The subsequent read-only KG audit at 04:42:34 UTC used
`scripts/adhoc/audit_kg_snapshot_freshness.py`. All 95 files declared by the
frozen KG source manifest matched their stored hashes; all 68 declared upstream
snapshot files also matched the campaign KG worktree at `f10fb3909ed32898a54176ca77e509a950d16b84`.
The primary M5 KG checkout at `d6baf5b90003a2032747559d94c00f86a7a4c615`
had 32 matching, 22 different and 14 missing files at those exact paths.
Differences included MediaDive and MetaTraits/GTDB data, mapping tables and
source-finalization evidence. The missing paths were captured generation or
rebuild evidence; this is not a repository-wide absence claim.

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

This delivers a reproducible review queue for #683. Scientific disposition of
the prose, any resulting structured recipe edits and later explicit MIM intake
remain open. It is not an inventory of ingredient mentions in every other
notes or protocol field.
