# JCM261 Variant Repair

Applied locally on 2026-10-08 at baseline
`f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`.
This is a four-record follow-up, not completion of the all-record objective.

## Source Decisions

- JCM261 and TOGO M253 explicitly replace the parent's yeast extract and
  peptone amounts with final 2.0 g/L each, add sodium thiosulfate pentahydrate
  at 1.0 g/L, omit elemental sulfur, and set receiving-medium pH to 7.0.
- J261's copied parent formulation was incorrect. It now has the three
  explicit final rates, separately scoped salt-base and trace-mineral stocks,
  and separately prepared sulfide. The omitted sulfur node, including its
  old annotations, is archived in the appended curation event.
- M253's 1 mg resazurin and 5 mg citric acid batch inputs are not 1 and
  5 g/L. Unsupported final concentrations are withdrawn; batch amounts remain
  in evidence-backed notes. Its stock additions are 1 L and 0.01 L per batch,
  not mass concentrations or doses per final liter.
- M253's inherited preparation paragraph conflicts with its later explicit
  variant instruction. The effective procedure applies the latter's sulfur
  omission and pH 7.0 override. The inherited text remains cited context, not
  a second operational sulfur-addition instruction.
- Reciprocal J261/J151 and M253/M142 links now use `DERIVED_FROM` for the
  combined modifications. J261's parent path is corrected to the exact
  tracked archaea path. Both parent formulations remain unchanged.
- No percentage basis, stock addition volume for the 5% sulfide preparation,
  measured final volume, new chemical grounding, or organism-growth evidence
  is inferred. The legacy M253 gas quantity placeholder remains unsupported.

Frozen primary sources and original baseline YAML are in
[`next-j261-context.json`](../20261008-jcm-stock-preparations/next-j261-context.json),
SHA256 `da25a5f492f0fcc0bf1fdeca5f4cb0c80a261b7387c2c9acb83efdcc7b31b53c`.
Source URLs include [JCM261](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=261),
[MediaDive J261](https://mediadive.dsmz.de/rest/medium/J261),
[TOGO M253](https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M253),
and the explicitly referenced J151/M142 stock definitions. Unknown authors
and publication years are not manufactured; source/discovery/access metadata
and capture hashes accompany the references.

## Accounting

The independent [applied audit](applied-audit.json) accounts for all 36 old
child quantity fields and unchanged parent scientific claims. It records:

- 193 new evidence entries, 10 references, and four appended events.
- Two final-rate corrections and one missing final-rate ingredient added.
- Seven stock-rate rebases and two stock-dose unit corrections.
- Seven unsupported quantity assertions withdrawn; one elemental-sulfur
  node omitted explicitly, separately counted from quantity withdrawals.
- 25 old ingredient-node placements restored to stock scope, including
  multiple stock-specific placements of previously collapsed salts.

[Cumulative accounting](../20261008-diff-audit-after-j261.json): 5,127 distinct
edited records, 30,962 evidence entries, 5,477 references, 5,329 events and
1,397 quantity corrections. Evidence totals include batch, preparation and
relationship support, not just independently verified final concentrations.
[Coverage](../20261008-followup-coverage-after-j261.json): 11,754 of 15,910
normalized paths have follow-up reports; 4,156 remain outside this coverage.
Covered records can still contain unresolved claims.

## Validation

Baseline and post-apply schema/strict checks pass for all four records.
Preview, applied independent audit, readback and no-op apply pass. The initial
53 repair tests and 225 repair/shared/variant/I-O tests pass. All 15,910
normalized records pass strict schema; IDs and reciprocal variant links pass.
The fast tier passes 8,036 tests, with 16 skipped and 1,943 deselected.
Products exit 0 with 91 warnings and 96,081 no-adapter skips. All broad
checks in [validation.json](validation.json) are terminal; these use the
partial locked Python 3.13 runtime, not full CI.

The [final reconciliation](final-checks.json) verifies all four current record
hashes, the complete normalized source inventory, five regenerated metadata
artifacts, one canonical report per target, code hashes and final lint/format,
diff and repair/index/manifest tests. No required validation session is left
running. Passing local checks do not override the failed publication gates.

The [reference gate](reference-validation.json) remains failed for all four
records. All 193 new primary snippets match their frozen sources literally;
the installed matcher accepts 97 and rejects 96 because of JCM chemical
subscript rendering and TOGO bracket processing. Across prior and new entries,
260 primary snippets match literally and 164 pass the installed matcher.
API bibliographic titles also mismatch the validator's URL fallback. No
automated pass is claimed and no quote is rewritten to conceal a failure.
Additional excerpts in evidence explanations are checked by the independent
claim audit against their pinned source text.

[Merge retention](merge-retention.json) routes all 15,910 normalized inputs
and confirms all claims/provenance survive for these four records in separate,
schema-valid formulation groups. It does not recertify every other output.
No tracked merged YAML is regenerated. Global merge verification fails with
1,247 name conflicts and 3,287 fingerprint issues. The freshness gate also
fails: 6,320 tracked versus 10,777 fresh outputs, with 4,275 tracked-only,
8,732 fresh-only and 2,045 changed shared paths; none of the shared outputs
is unchanged. These failed gates still prevent publication readiness.

Five generated metadata artifacts were refreshed from the maintained index
generator. Its direct-ingredient-only hierarchy detection loses J261's index
flag when KI moves into a stock, although the actual KI annotation is preserved;
the statistics change from 1,476 to 1,475 reflects that existing generator
limitation, not annotation deletion.

No commit, push, PR, GitHub issue, merge, or branch deletion was performed in
this cohort. Publication and the whole-corpus objective remain unfinished.

## Next Cohort

The [next M142-dependent queue](next-m142-handoff.md) pins 98 pending records,
their official TOGO source tables, and 96 original JCM pages. Sixteen original
pages contain no recipe; preparation stages, subrecipe identifiers and source
amount conflicts remain explicit. No next-cohort record has been edited or
counted as reviewed. The captured sources support a larger source-mapped
follow-up without assuming that every M142 reference is a root batch dose.
