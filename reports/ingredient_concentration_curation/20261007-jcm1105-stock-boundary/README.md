# JCM 1105 Original-Source Stock-Boundary Repair

Applied locally to `data/normalized_yaml/bacterial/virgibacillus_merv_medium.yaml`,
ID `CultureMech:002283`, against baseline commit
`f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`. The all-record objective remains
unfinished, and the curation changes remain uncommitted.

## Evidence And Changes

The complete original [JCM 1105 recipe](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1105)
was inspected and captured on 2026-10-07. It explicitly prepares a one-liter
base, then adds 10 ml of separately autoclaved 10% sodium carbonate solution.
The prior extraction used that stock dose as the base concentration denominator.

- Corrected five base concentrations to 10, 3, 1, 3, and 100 g/L respectively.
- Preserved the source's citrate trihydrate and other ingredient identities.
- Relocated the five base ingredients and carbonate into two inline solutions.
- Removed the unsupported carbonate mass concentration; retained the source's
  10% notation without assigning an unspecified percentage basis.
- Added explicit one-liter base and 0.010-liter stock batch amounts. Neither
  is asserted as a final-medium concentration or measured receiving volume.
- Assigned preparation text to the correct stage. Optional agar was not added
  to the existing liquid formulation.
- Added seven evidence entries supporting eleven scoped claims, one reference,
  and one append-only agent-authored curation event. No growth claim was added.

Every scientific change has a literal source snippet and source URL in the
YAML. Unknown authors and publication year were not invented. Original capture
SHA256: `2c7d8a4ae523578495afb0f7de58f4185a15a9cd5a489e938f46602d714356f8`.
The local capture is `/tmp/ingredient-media-20261007/JCM_GRMD1105-scope.html`.

## Replay And Review

[plan.json](plan.json) freezes the complete before/after records, source hash,
and claims. [J1105.md](J1105.md) contains the per-field evidence and decisions.
The guarded repair checks exact tracked path, baseline context, source bytes,
table boundaries, intervening preparation, and schema before writing.
Readback passed and a second apply changed zero records.

The [seventh cohort's original report](../20261007-mediadive-media-3000-3319/records/bacterial/virgibacillus_merv_medium.yaml.md)
withheld five preliminary claims and left this record unchanged. Its report and
frozen plan remain intact. This successor is linked into readback, coverage,
and the independent semantic diff, without adding a duplicate `- Record:` line.

The 47 repair tests include source changes with recomputed fixture hashes,
removed table boundaries, dose/concentration confusion, percentage ambiguity,
chemical form, preparation order, optional agar, pH, concurrent edits,
non-exact paths, symlinks, and independently inverted after-state tampering.

## Validation

[validation.json](validation.json) records actual commands, terminal exit codes,
and logs. All 26 post-apply jobs and both baseline jobs are terminal.
The focused selection passes **636 tests**. Baseline and post-edit
strict scans cover 15,910 normalized records without schema errors. Target
schema, canonical IDs, guarded apply/readback/no-op, all seven medium readbacks,
JCM 896 and KOMODO 12 readbacks, independent diff, and coverage checks pass.
Black, Ruff, and `git diff --check` pass for the changed code and tracked diff.

These are isolated Python 3.11 results, not maintained Python 3.13 or CI passes.
Product validation lacks `oaklib`; reference validation lacks its executable;
the full suite cannot run because coverage support and other imports are
missing. No environment or dependency pins were changed.

[Actual-group retention](merge-retention.json) passes for the corrected record's
singleton group, preserving all checked ingredients, solutions, preparation,
physical state, pH, evidence, and references. This does not resolve losses in
other groups. Global merge verification fails with 1,247 name conflicts and
3,287 fingerprint issues. [Freshness](merge-freshness.json) fails: 6,320 tracked
and 6,491 fresh records, with 3,719 only tracked, 3,890 only fresh, 1,645 changed,
and 956 unchanged. Regeneration was temporary; no generated merge was published.

The [current corpus diff](../20261007-diff-audit-after-jcm1105.json) confirms
4,846 edited records, 28,031 new evidence entries, and 1,164 quantity/unit
corrections. [Coverage](../20261007-followup-coverage-after-jcm1105.json) remains
8,099 reported paths and 7,811 outside these follow-up reports. Report presence
does not mean every claim is scientifically verified.
