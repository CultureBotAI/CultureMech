# Halobacteria Variant Concentration Review

The sixteen-record successor is **applied locally**, not published or a claim
of full-corpus completion. Thirteen records receive ingredient/preparation
review; three parents receive reciprocal relationship updates only. Parent
ingredient arrays, including their 28 existing quantities, remain unchanged.

The guarded application, independent readback and repeat no-op account for
575 evidence-linked claims, 127 reviewed old quantity fields and 167 output
ingredient/stock nodes. This batch adds **335 evidence entries, 45 references
and sixteen append-only history events**. Every edited non-provenance field
has source-linked snippet evidence in the YAML. No taxa-media assertion is
added, and no chemical mapping or role is recertified by this amount review.
Only the sixteen intended normalized records changed.

## Evidence Decisions

- Six TOGO variants have twelve iron/manganese units corrected from g/L to
  mg/L. Their six false water mass concentrations are removed; water remains
  unquantified final-volume make-up, not an invented fixed input volume.
- J572's magnesium target is 2 g/L; J1008's specified formulation is 270 g/L
  NaCl and 15 g/L magnesium sulfate heptahydrate; J914's NaCl target is
  150 g/L. These are not the copied base amounts. JCM1008's supplemented
  wording has an unresolved operational ambiguity; no additive sum is inferred.
- J1132 and M1212 retain a 1 L prepared-base dose with the existing ingredients
  relocated into its composition. The subsequent pH-8 adjustment has no
  specified titrant identity, dose or independently established resulting
  volume. The provider's nominal 1000 ml volume field is not hidden, but it is
  not a separate final-volume preparation instruction. No carbonate reagent
  or final-medium dilution factor is invented.
- S3823 retains its nine supported base concentrations and gains unquantified
  water make-up. Only its false composition placeholder and corresponding
  incomplete-composition flag are removed. No universal working dose is added.
- True variants replace incorrect duplicate relationships. Exact reciprocal
  tracked paths are repaired. Conditional agar remains confined to the selected
  solid TOGO formulations; earlier preparation arrays and unrelated children
  remain unchanged.

## Sources And Limits

[context.json](context.json) freezes source captures, access metadata, record
baselines and the precise source gap. Sources are official JCM recipe pages,
TOGO datasets and the MediaDive J1132 provider export. The original JCM1132
page returned no recipe. Provider evidence is explicitly qualified, not
presented as a recovered original or a DOI-backed publication. Missing authors,
publication years and DOIs are not fabricated.

[plan.json](plan.json) is the immutable first proposal. The applied
[plan-v2.json](plan-v2.json) strengthens the relationship excerpts with their pH
instructions. [Preview reports](records-preview/) remain immutable and excluded
from applied coverage; the three parent reports include unchanged ingredient
rows separately from new metadata claims.

## Verification

- [Preview validation](validation-preview.json): 689 focused tests, 64
  baseline/proposal schema and strict commands, 417 supported reference checks,
  25 separately checked provider-dataset entries and two unchanged bibliography
  entries explicitly not reverified. This is not an unrestricted reference pass.
- [Application tests](focused.json): 725 passing tests, including write guards,
  concurrent edits, symlinks, altered plans/receipts/logs, readback and no-op.
- [Application](apply.json): sixteen changes, sixteen verified readbacks,
  zero repeat changes, independent source audit and a full-corpus hash check
  proving no other normalized YAML changed.
- [Post-edit validation](post.json): all 32 actual-written schema/strict
  commands and twelve supported reference CLI commands pass, with 417
  supported reference checks and the same explicitly qualified exclusions.
- [Corpus checks](corpus.json): strict validation covers 15,910 records;
  ID/product checks pass and variant-link validation has no findings. Product
  validation retains 91 warnings and 96,010 unsupported-adapter skips.
- [Applied ledgers](applied-ledgers.json): sixteen reports, nine prior
  canonical reports linked forward, 11,812 unique canonical paths and 4,098
  outside follow-up coverage. All 65 immutable previews are excluded. A
  [wording-only clarification](report-header-clarification.json) corrects the
  applied report headers' overbroad flag-preservation statement; S3823's removed
  incomplete-composition flag was already explicit in its claim rows. This
  receipt pins successor hashes and verifies every other report byte unchanged;
  the original ledger hashes and immutable previews remain preserved.
- Six indexes are refreshed for seven metadata records. All fifteen medium
  targets pass merge retention; S3823 is correctly excluded as a solution.
  All 699 final QA tests pass. The [terminal fast tier](fast.json) passes
  12,702 tests, with sixteen skipped, 3,374 deselected and two dependency
  warnings. The corpus hash is unchanged across that run.

The [final applied checkpoint](validation.json) pins the receipts, current
report headers, source/code hashes and next-batch schema investigation. The
isolated schema prototype is not a production schema change.

All results are local in the existing partial Python 3.13 environment, not
clean CI. Global merge verification still fails with 1,247 name conflicts and
3,287 fingerprint issues. Freshness fails with 6,320 tracked versus 10,781 fresh
outputs: 4,275 tracked-only, 8,736 fresh-only, 2,045 changed and zero unchanged.
Neither failure is waived. The all-record goal remains active.
