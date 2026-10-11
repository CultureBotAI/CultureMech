# Albumin Counterpart Repairs

Applied locally to TOGO M194, M213, M244 and MediaDive J252. The all-record
ingredient goal and publication workflow remain incomplete. No taxa-media
associations were added, and existing chemical groundings are not recertified.

## Evidence And Corrections

All nine source responses were refreshed and hash-matched before application.
JCM201 still returns no recipe; it is an access-status observation, not cited
formulation evidence. M194 is explicitly TOGO-provider-backed. M213, M244 and
J252 have available original-page corroboration. All 108 reference checks pass:
101 attached evidence entries and seven bibliography entries. Missing authors
and publication years remain absent rather than inferred from access dates.

- M194: restore the 50 g fraction V batch input, retain one 200 ml dose of
  percentage-labeled gelatin, correct the 100 ml CMRL product dose and 900 ml
  water input, and withdraw the invented serum VARIABLE placeholder. The serum
  source says final 6%, without a basis or fixed dose; gelatin 7% is also
  basis-unspecified. Preserve source ordering and the serum-after-filtration step.
- M213: restore the 10 ml albumin-stock dose and separate glucose, cysteine,
  hemin and the nested 0.05 N NaOH solvent. Unspecified percentage bases are not
  converted to numeric strengths. Only the three source-named stocks receive
  separate filtration instructions. Add source-backed pH 6.6.
- M244/J252: restore bovine serum albumin and preserve genuine yeast extract.
  Represent yeast, albumin and neutralized sulfide as separate preparations.
  Albumin is explicitly 10% w/v; its 1 g receiving-batch contribution implies a
  calculated 10 ml stock dose. Every conversion input and the arithmetic are
  attached in YAML, outside the exact quotations. Yeast 10% and sulfide 5%
  remain basis-unspecified, without guessed strengths or doses. Retain the
  pH 7.6 preparation context at 80-90 C and separate filtration/autoclaving.
- M244's milligram inputs no longer remain as same-number g/L assertions.
  Withdraw its unsupported `high_metal` flag without setting it false. Its
  schema-defined molar threshold cannot be established from these batch inputs
  and unknown final volume. J252's previously scaled gram values also lack a
  verified final-volume denominator; exact batch amounts remain in notes.

The independent audit accounts for all 60 old quantity fields, 53 provider recipe
rows and 180 field claims. It verifies 52 unsupported quantity withdrawals, three
water-input corrections, five stock-dose corrections, six new numeric fields,
ten relocated existing nodes, nine added stock descriptors, and four append-only
history events. No final-medium concentration is inferred from a water input.

## Verification

Baseline and applied schema/strict/reference checks, independent readback,
no-op application, lint, formatting and diff checks pass. All 155 dedicated
mutation/guard tests and 498 focused regression tests pass. Fast-tier and full
corpus checks are terminal: the fast tier passed 9,173 tests (16 skipped) before
the subsequent test-only resolver isolation fix. After that fix, all 11 direct
resolver tests pass; the resolver-only fast selection passes six tests with one
skip. This is not a full fast-tier rerun after the fixture change.

Strict schema validation passes for all 15,910 records. The initial corpus ID
check failed because resolver tests temporarily mutated the live corpus; that
failed receipt is preserved. Both mutation tests now use temporary corpora, and
the serial ID recheck passes for all 15,910 records. Product validation passes
with 91 warnings and 96,077 no-adapter skips, not complete chemical recertification.
Global merge verification still fails with 1,247 name conflicts and 3,287
fingerprint issues. Freshness fails with 4,275 tracked-only, 8,732 fresh-only and
2,045 changed shared paths. See the [validation receipt](validation.json).

Full-corpus routing produces 10,777 groups from 15,910 normalized inputs. All
four repaired outputs retain their claims in separate schema-valid runtime merge
groups. No tracked merged YAML was written. Five generated indexes were refreshed;
the only semantic changes are these four records' ingredient and solution counts.

Cumulative accounting is 5,163 edited records, 32,834 added evidence entries,
5,616 references and 5,367 appended history events. Follow-up coverage is 11,784
of 15,910 exact normalized paths, leaving 4,126 outside follow-up reports.
Coverage is not proof that all concentration claims are resolved. M194/M213/M244
have new canonical reports with exactly one `- Record:` line each; J252 retains
its historical canonical report and gains a `- Follow-up target:` supplement.

## Artifacts

- `context.json`, `plan.json`: inspected sources, baselines and guarded decisions.
- `initial-preview.json`: superseded, unapplied first preview; never use for application.
- `application.json`, `applied-audit.json`: readback, all-field audit and no-op results.
- `records/`: per-record evidence and decision tables.
- `live.json`: refreshed-source and reference checks, including the unavailable original.
- `cumulative-audit.json`, `followup-coverage.json`, `reconciliation.json`: actual accounting.
- `index-refresh-plan.json`, `index-refresh-application.json`: guarded generator refresh.
- `merge-retention.json`: target retention, not a global freshness pass.
- `validation.json`: terminal check results, artifact hashes and remaining failures.
- `corpus.json`, `id-recheck.json`: original ID failure and successful serial retry.
- `adversarial-review.md`, `next-work.md`: addressed findings and remaining scope.

The next DSMZ/KOMODO source capture is preparation only, not another four edits or
four completed reviews. Publication and all-record completion remain unproven.
