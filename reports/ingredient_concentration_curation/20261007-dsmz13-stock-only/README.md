# DSMZ 13 Stock-Only Follow-Up

This is one additional local stock-boundary repair, not completion of the full
ingredient-curation objective or a new unique reviewed path. The original
first-pass report remains historical and links to [the scoped follow-up](13.md).

## Source And Correction

The exact [MediaDive medium 13 capture](https://mediadive.dsmz.de/rest/medium/13)
identifies Main solution 16, with explicit additions of 500 ml each of solution
17 (A) and solution 18 (B). The original
[DSMZ 13 PDF](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium13.pdf)
was visually inspected in full: five non-water ingredients belong to A, glucose
and agar belong to B, and each solution uses 500 ml water. The pH adjustment
belongs to A, before separate sterilization and combination.

The authoritative record now has an explicit empty direct ingredient list and
two stocks. Seven existing ingredient nodes were moved with amounts, chemical
identifiers, and unrelated metadata preserved. Four explicit 0.5 L fields were
added: two stock doses and two preparation-water amounts. One preparation text
was relocated. No final-medium dilution, final volume, or final pH is inferred.
The original remaining main procedure is unchanged.

Twelve scoped changes carry ten new evidence entries: nine ingredient/water
entries and one root entry covering both stock doses and the preparation move.
Each claim has an exact API excerpt, locator, persistent URL, scope, and any
conversion arithmetic. Two bibliography entries and one curation event were
appended. No duplicate reference IDs or fictitious URL fragments are used.
Publication year and individual authors were not established; institutional
source, discovery mode, access date, and capture hashes are recorded instead.

- API SHA256: `a66f5d5dfa8b26790d08b54af1e72f22e8a0b3704a19723c66a06eac5547874a`
- PDF SHA256: `5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95`
- Record baseline SHA256: `8c6539615bfbef574f50497f952c88236d198ec56ad22e885ba4db0a4dd0078d`

The existing guarded runner accepts this separately pinned cohort via
`--cohort dsmz13`. Its default seven-record cohort and frozen plan are unchanged.
Preview is the default; `--apply` is required to write. Whole-record hashes,
source captures, exact identities, source graph, inventory, quantities, and
preparation texts are checked before applying.

## Fingerprinting Repair

The maintained fingerprinter previously rejected empty direct-ingredient lists
before inspecting stocks. It also claimed to traverse nested stocks while
actually examining only their first level. It now collects real compositions
through nested stocks, allowing stock-only media when valid constituents exist.
Name-only unresolved stocks and empty/placeholder-only compositions still do
not provide a fingerprint. Missing/invalid direct lists, malformed collections,
and stock cycles fail; shared noncyclic YAML aliases remain valid.

This remains an **ingredient-set** fingerprint. It does not prove equal
concentrations, stock doses, preparation conditions, or formulation identity,
and it does not fix the separate mixed-source merging defect.

The [full-corpus before-curation comparison](fingerprint-impact-before-curation.json)
checked all 15,910 exact tracked normalized paths with unchanged input hashes.
It found 111 empty-direct records with stock references and 14 records with
nested stocks. The code change makes 32 previously skipped records
fingerprintable and changes six existing fingerprints to include previously
omitted nested constituents. No previously fingerprintable record lost its
fingerprint. Other records' fingerprint outcomes are unchanged. These 38 code
effects are not 38 scientific record reviews or evidence additions.

## Verification

Both baseline schema gates passed. The independent cumulative diff audit
inverts this repair and verifies all original nodes, the new volume amounts,
the exact preparation move, and preservation of unrelated data. The current
cumulative audit records 4,304 edited records and 25,022 added evidence entries.
Post-edit open/closed validation and the full 15,910-record strict-schema gate
passed. The focused regression selection passed 398 tests, including stock-only,
nested, cyclic/shared-alias, malformed-input, batch, and merge tests. Ruff passes
for the other edited Python files; the fingerprint module retains exactly its
12 pre-existing findings with no new ones, recorded in
[the baseline comparison](ruff-baseline-comparison.json).

The repaired record's [actual maintained merge group](merge-retention.json)
contains only DSMZ 13 and retains its empty direct list, both stocks, preparation,
references, and evidence. This is a real corpus-group check, not merely a
synthetic single-record test. No generated merge recipes were copied into the
worktree. Current command outcomes are in [validation.json](validation.json).

Final read-back verified the record hash and all twelve scoped claims; reapplying
changed zero records. The preceding seven-record batch still verifies all 105
claims. Global merge checks remain failing: 1,247 name conflicts and 3,287
fingerprint issues. The temporary freshness build has 6,491 records versus
6,320 tracked, with 3,718 only tracked, 3,889 only fresh, 1,494 changed, and
1,108 unchanged. Product/reference checks are unavailable because the OAK
adapters and reference-validator executable are missing, respectively.

Full-suite validation is not green: `just test` cannot load pytest-cov, and a
full run with coverage disabled stops at collection because dotenv, rapidfuzz,
pandas, and bs4 are unavailable in the isolated Python 3.11 runtime. Focused
tests and source read-back are separate checks, not a passing 3.13/CI claim.

## Remaining Scope

The full all-record curation goal remains active. The legacy source-duplicate
link from this record to KOMODO 13 has not been updated or treated as proof of
equivalent formulation structure. Secondary chemical mappings are preserved,
not revalidated. The DSMZ 261/369 mixed-source merge, conditional agar in DSMZ
464a, importer unit handling, other flattened stocks, variants, and records
outside source follow-up reports remain unresolved. Changes are local and
uncommitted; no new taxa-media associations were created.
