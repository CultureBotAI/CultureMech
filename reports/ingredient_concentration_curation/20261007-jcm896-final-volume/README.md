# JCM 896 Original-Source Concentration Repair

Applied locally to `data/normalized_yaml/bacterial/modified_bsk_medium.yaml`,
stable ID `CultureMech:003244`. This is one repaired record, not completion of
the all-record objective. Baseline commit:
`f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`.

## Evidence And Changes

The complete original [JCM 896 recipe](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=896)
was inspected and captured on 2026-10-07. Its preparation explicitly makes the
complete medium to 584 ml. The API-derived mass concentrations instead divided
by 40 ml, the serum dose, and the serum was incorrectly encoded as mass per
liter. The original table and final-volume statement, not another local record
or the faulty API calculation, support this repair.

- Corrected all ten mass concentrations using original batch grams / 0.584 L.
- Corrected serum using 40.0 ml / 0.584 L, with `ML_PER_L` and no density assumption.
- Replaced generic yeast extract with the source-specific TC Yeastolate product.
- Restored the original micrometer symbol in the filtration instruction.
- Added 12 evidence entries for 13 scoped changes, one bibliography entry, and
  one append-only agent-authored curation event.
- Preserved IDs, prior history, other labels, chemical mappings, pH, stocks,
  variants, and growth fields. Ontology mappings are not verified by amount evidence.

Every changed quantity has its exact rendered source row in ingredient evidence,
plus a separately quoted final-volume statement, source locator, and arithmetic.
HTML entities and whitespace are normalized without splitting inline chemical
digits. Six-significant-digit storage is computational rounding, not increased
experimental precision; the original stated inputs remain in the source quotes.
Unknown individual authors and publication year are not invented.

Original capture SHA256:
`c6e814a8bff1580ddd42179b7d401a204ae19469786fdafd140408d1522f03c8`.
The ignored local capture is `/tmp/ingredient-media-20261007/JCM_GRMD896.html`.

## Replay And Review

[plan.json](plan.json) freezes before/after text, hashes, source hash, and all
13 claims. The guarded repair verifies the exact tracked target, complete
baseline context, original source bytes, source title/table/preparation, and
whole-record schema before writing. Readback passed; reapplication changed zero
records. [J896.md](J896.md) lists every correction and its evidence.

The [sixth cohort's original review](../20261007-mediadive-media-2500-3000/records/bacterial/modified_bsk_medium.yaml.md)
withheld all six mechanically eligible claims and made no changes to this target.
That historical report, plan, inventory, and handoff remain unchanged. This
successor is explicitly linked into readback, coverage, and semantic-diff checks;
its report does not add a duplicate `- Record:` marker for the same exact path.

An adversarial fixture exposed a title-prefix check accepting a variant suffix.
The check now requires the exact heading immediately before the first table row.
Tests also reject changed amounts, units, hydration, final volume, preparation,
source hashes, local context, plans, symlinks, and non-exact tracked paths.
Readback remains valid after an unrelated commit; provenance retains the
original reviewed commit rather than rewriting history.

## Validation

[validation.json](validation.json) records actual commands, exit codes, and logs.
All 24 post-apply jobs and both baseline jobs are terminal. **588 focused tests**
pass, including 35 repair tests. Both strict corpus scans cover 15,910 records
with zero errors. Open-schema, canonical-ID, guarded apply/readback/no-op, all
six earlier medium readbacks, KOMODO 12 readback, independent semantic-diff,
and exact-path coverage checks pass. The sixth readback explicitly follows this
successor; its old report and frozen source plan were not overwritten.

The runtime is isolated Python 3.11, not maintained Python 3.13 or CI. Product
validation fails because `oaklib` is missing, reference validation lacks its
executable, and full tests fail on missing coverage support or dependency imports.
No dependency pins or existing environment were altered. Black, Ruff, and
`git diff --check` pass for the changed code and tracked diff.

The product-label correction may change fingerprint membership intentionally.
[check_retention.py](check_retention.py) checks this record's actual merge group
for complete formulation, preparation, and evidence retention. No generated
merge is copied into the worktree and no evidence is propagated to another
formulation merely because its ingredient fingerprint is similar.

[Actual-group retention](merge-retention.json) passes: the corrected record is
in a singleton group, and every checked ingredient/evidence, stock, preparation,
physical-state, pH, root evidence, and bibliography field survives unchanged.
This does not resolve evidence loss in other groups. Global merge verification
still fails with 1,247 name conflicts and 3,287 fingerprint issues.
[Freshness](merge-freshness.json) fails with 6,320 tracked and 6,491 fresh records:
3,719 only tracked, 3,890 only fresh, 1,624 changed, and 977 unchanged. The
regeneration was temporary, not published.

The [current independent corpus diff](../20261007-diff-audit-after-jcm896.json)
counts 4,808 edited records, 27,832 new evidence entries, and 1,159 quantity/unit
corrections. [Coverage](../20261007-followup-coverage-after-jcm896.json) remains
7,780 unique reported paths and 8,130 outside this follow-up; this correction
resolves an already reported path rather than increasing review coverage.
