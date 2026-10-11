# KOMODO Concentration Evidence: Offsets 2000-2499

The guarded source pass is **applied locally**, not committed or published.
It produces [one report per selected exact path](records/) for all 500 records:
46 changed and 454 unchanged, with zero operational or schema-blocked records.
The all-record objective and unresolved findings within this cohort are not
finished.

The [applied plan](plan.json) adds 220 concentration-evidence entries, each with
an exact source excerpt and persistent recipe URL, plus 46 source-identity
mapping entries, 92 references and 46 append-only curation events. There are no
numeric, unit, ingredient-identity, stock, variant or growth-association changes.
Identity-mapping snippets do not support quantities. Source-duplicate records
are not independent scientific confirmations.

The evidence supports provider-declared main-recipe amounts only, not measured
final volume, stock composition or downstream dilutions. Unsupported amounts and
historical ontology mappings remain unchanged. No authors or publication years
were invented for the dataset records.

[Source captures](source-captures.json) verifies 500 exact tracked paths against
both the inventory and preceding coverage hashes. Their 272 mapped medium
endpoints comprise 251 accessible captured responses and 21 actual HTTP 404
responses, affecting 25 records. A missing API response does not prove that an
original PDF or variant formulation is unavailable. Mapping evidence establishes
source identity only, not ingredient amounts or variant equivalence.

The initial dry run proposed 375 claims across 69 candidate records. Complete
candidate/source inspection led to [23 source-pinned withholdings](withholdings.json)
removing 155 preliminary claims. [Preparation findings](preparation-findings.md)
explain the stock, supplement, extraction and source-conflict decisions. The final
plan has 220 applied `evidence_only`, 7,676 `conflict` and 11,475 `unsupported`
claim rows. These row counts include source-only rows, preparation and variant
context; they are not counts of independently resolved scientific facts.

For reproducibility, the frozen initial preview is
`/tmp/ingredient-media-20261007/komodo-2500-initial-preview.json`,
SHA256 `92f17f43b3335c67a020bee85e3e42d751a6e2ab0e7646cbf0f6c44cd432bfff`.
Do not overwrite either the initial preview or the applied plan. Reapplication
must use the applied plan and its frozen withholdings, not a fresh preview that
would treat this post-curation state as a new baseline.

## Verification

[Baseline checks](baseline.json) passed the independent preview audit, LinkML
schema validation for all 500 targets, full strict corpus validation, and 165
guard tests. The preview only inserted provenance text: 7,769 added lines, zero
removed lines and zero replacement blocks.

The [independent applied audit](diff-audit.json) rechecks all 500 hashes and every
accepted source row, exact quote, identity mapping, quantity, unit and arithmetic.
Inverting only the appended provenance reconstructs each complete original
object exactly. Read-back passed; rerunning the guarded apply changes zero
records. Post-edit schema validation passed for all 500 targets, all 246 selected
tests passed, and strict validation scanned all 15,910 records with zero errors.

The post-apply [validation journal](validation.json) is terminal: 12 of 15 commands
pass. Three separate merge gates fail. [Actual-group retention](merge-retention.json)
preserves 198/220 amount quotes and 184/220 complete evidence entries; see the
[adversarial review](adversarial-review.md) for exact affected records and the
merge-rule cause. The global verifier reports 1,247 name conflicts and 3,287
fingerprint issues. [Freshness](merge-freshness.json) compares 6,320 tracked with
6,494 freshly generated records: 3,720 only tracked, 3,894 only fresh, 1,683
changed and 917 unchanged. Temporary regeneration is not publication.

The separate [product/reference journal](reference-validation.json) is terminal.
Product validation passes with 91 non-blocking warnings (50 implausible labels,
41 hydrate/anhydrous warnings) and 96,044 no-adapter skips. The installed
deterministic URL-content matcher validates all 220 concentration and 46
identity snippets against retrieved/cached content. This is not proof of
uninterrupted live access or scientific claim scope.

The full reference CLI over all 46 edited records **fails** with 96 issues:
46 API URL-as-title fallback mismatches, 42 KOMODO title mismatches and eight
fetch errors; its log includes HTTP 403 mapping-source responses. The captured
mapping page independently confirms the literal HTML title, so the descriptive
mapping reference title needs a separate source-pinned correction. See the
[title handoff](reference-title-handoff.json); historical plans must not be
rewritten. Do not replace meaningful recipe titles with URLs merely to satisfy
the dataset-title fallback. The runtime is the partial locked Python 3.13
environment, not a full project environment or CI run. Generated merges/pages
are not hand-edited or published.

## Remaining Work

Resolve the 23 withheld formulations and all other unsupported or conflicted
claim rows. API 404 responses are source-access gaps, not evidence that original
recipes or genuine variants do not exist. Preserve separate variant review;
never transfer a parent recipe's concentrations merely because a duplicate link
or concentration-independent fingerprint exists.

[Initial preparation triage](preparation-triage.md) is retained as a historical
lead. The complete frozen [candidate context](inspected-candidate-context.json)
and subsequent findings supersede its incomplete inspection status.
