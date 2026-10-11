# JCM Acid Identity And Preparation Repairs

Applied locally to J266, J675 and J1203. The all-record objective and publication
workflow remain incomplete. These are ingredient/preparation repairs, not new
taxa-media associations or complete chemical-grounding reviews.

## Evidence And Changes

Eight pinned responses cover the three exact MediaDive accessions and original
JCM266, JCM675, JCM1203, JCM151 and JCM197 pages. Fresh responses match the
inspected captures. All 175 automated reference checks pass: 167 attached
evidence entries and eight bibliography entries. Authors and publication years
are not supplied; they were not invented. Each scientific change has a persistent
source URL and a literal excerpt attached in the YAML, with its preparation scope.

- J266: removed only the three false LB supplier nodes and restored
  alpha-methylbutyric acid in the fatty-acid stock. Separated rumen preparation,
  trace minerals, vitamins, fatty acids and reducing-agent preparations. Split
  four collapsed main/trace ingredients. Corrected root pH from stock pH 7.5
  to source-explicit medium pH 6.5, retaining the metadata conflict explicitly.
- J675: retained genuine Tryptone and yeast extract, removed the false LB nodes,
  and restored 2-methylbutyric acid in its liquid stock. Restored the 1 ml stock
  dose and late sodium carbonate/cysteine inputs from original preparation prose.
- J1203: restored DL-2-methylbutyric acid and corrected liquid inputs previously
  represented as g/L. Separated the 1 ml resazurin-solution dose from its ambiguous
  0.05% strength, and glucose's receiving-batch contribution from its separately
  filtered stock of unspecified strength and dose.

The independent audit accounts for all 73 old quantity slots and 85 API recipe
rows. It checks 213 field claims, including original-prose-only additions.
The changes add 167 evidence entries, eight references and three history events;
withdraw 38 unsupported quantity slots; correct six quantities and two stock-dose
bases; rebase 27 source-declared stock rates; add 22 numeric fields; and relocate
34 existing nodes into their proper stock scopes.

Water remains a batch input, not a measured final volume. Source-declared stock
rates remain explicitly attributed to the provider, not independently measured
stock volumes or final-medium rates. No density, percentage basis, hydrate,
normality conversion, molecular identity or dissolved-gas amount is guessed.

## Verification

Baseline and applied schema/strict checks, applied reference checks, independent
readback, no-op rerun, lint, formatting, diff checks and the 746-test focused
selection pass. The dedicated repair suite contains 93 passing tests.
The fast tier passes 8,943 tests (16 skipped, 1,945 deselected, two deprecation
warnings). Strict schema and identifier checks pass for all 15,910 records.
Product validation exits successfully with 91 non-blocking warnings (50
implausible-label and 41 hydrate findings) and 96,083 no-adapter skips. It does
not recertify every chemical grounding. All intended checks are terminal in
`validation.json`. Checks used the existing partial locked Python 3.13 runtime,
not a clean CI environment; the full test suite was not rerun for this local batch.

Global merge verification fails with 1,247 name conflicts and 3,287 fingerprint
issues. Freshness also fails: 6,320 tracked outputs versus 10,777 fresh outputs,
with 4,275 tracked-only paths, 8,732 fresh-only paths, 2,045 changed shared paths
and zero unchanged shared paths. These match the preceding batch's failure
counts; target retention does not resolve these global gates.

Full-corpus routing computes 10,777 groups from 15,910 inputs. The three repaired
records each retain their claims in a separate, closed-schema-valid runtime
output. No tracked merged YAML was written. Four generated metadata indexes
were refreshed, with semantic changes limited to these records' ingredient and
solution counts. The source index is MediaDive, not unknown.

The cumulative independent audit verifies 5,157 edited records, 32,698 new evidence
entries, 5,606 references and 5,361 appended history events. Coverage remains
11,781 of 15,910 exact normalized paths, with 4,129 outside follow-up reports.
All three targets already had canonical reports: these new reports use
`- Follow-up target:` and do not duplicate or rewrite historical `- Record:` lines.
Report coverage is not proof that all scientific claims are resolved.

## Artifacts

- `context.json`: pinned source responses and exact baseline records.
- `plan.json`, `application.json`, `applied-audit.json`: guarded changes/readback.
- `records/`: one supplemental result for each repaired path.
- `cumulative-audit.json`, `followup-coverage.json`, `reconciliation.json`: current accounting.
- `index-refresh-plan.json`, `index-refresh-application.json`: generated metadata changes.
- `merge-retention.json`: actual recomputed output retention, not a freshness claim.
- `validation.json`: terminal results, current corpus hash and artifact/code hashes.
- `adversarial-review.md`: local self-review and mutation-test coverage.
- `next-work.md`: remaining scope, unchanged baselines and source-access gaps.

The superseded preview with the shorter pH quote is retained only as historical
debugging evidence; it was never applied. The final plan includes the literal
sentence-ending period required by the reference matcher.
