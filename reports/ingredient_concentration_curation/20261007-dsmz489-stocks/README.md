# Medium 489 Stock Repair

The [frozen plan](plan.json) repairs the DSMZ and exact mapped KOMODO copies
of medium 489, plus standalone MediaDive solution 995. It is a source-specific
follow-up within the unfinished all-record objective, not a new formulation.
All three records are applied locally. Readback matches all three result hashes,
reapplication changes zero records, and the [applied audit](diff-audit.json)
passes complete-record inversion. [Validation](validation.json) is terminal;
the successful checks, unavailable validators and failing merge gates are
distinguished below. No all-gates pass is claimed.

The [independent preflight](preflight.json) checks the evidence and
inverts all three records to recover their complete original contents. It
counts 23 new evidence entries, five references and three curation events;
nine stock-node moves, three resazurin stock-stage concentration corrections,
six unsupported reducing-stock rate removals, one water-unit correction and
five added volume slots. These are separate count categories.

## Scientific Decisions

- The original [DSMZ 489 recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium489.pdf)
  specifies sodium resazurin as a 0.1% w/v stock with a 0.50 ml batch addition.
  The repair represents stock strength separately from the 0.0005 L dose;
  it does not treat the imported 0.0005 g/L rate as a stock strength.
- Cysteine hydrochloride monohydrate and sodium sulfide nonahydrate are added
  after sterilization from sterile anoxic stocks prepared under 100% nitrogen.
  Their 0.15 g batch requirements remain in notes. No stock strength, stock
  volume, dose volume or solvent identity is invented.
- Distilled water is a 1000 ml input, represented as 1 L. The standalone copy's
  1000 percent value is corrected; the two media gain the missing input. Water
  input does not establish a measured final volume after stock additions.
- Eight basal g/L values remain explicitly provider-nominal recipe rates.
  Existing cysteine/sulfide endorsements are superseded at their new preparation
  stage with explicit claim resolutions; old snippets and explanations remain.
- The KOMODO aerobic annotation remains historical import provenance, with an
  explicit warning that it is not verified incubation or growth evidence.
  The original recipe establishes anoxic preparation, not a new growth claim.

Both complete API payloads, original one-page PDF, and exact KOMODO source
mapping were inspected. Byte hashes, retrieval dates and locators are pinned
in the plan. Mapping evidence establishes source identity, not concentrations.
Individual authors/year remain unknown; the PDF copyright date is not used
as publication year. Existing ontology mappings, IDs, variant relationships,
legacy placeholders/quality flags and prior curation history are preserved.
In particular, the resazurin CHEBI mapping has not been validated as a sodium-salt
identifier; no replacement is guessed.

## Verification

The local guarded mutator requires the exact tracked paths, original hashes,
source identifiers, chemical forms, source rows and preparation text. It
validates both schema targets, rejects plan/source/concurrent edits, and keeps
reruns idempotent. Tests additionally tamper with stock strength, dose, water,
ontology, old history, evidence snippets and unrelated growth fields.

`baseline.json` and `validation.json` record command exit statuses and runtimes;
they are not CI. Per-record supplements preserve earlier reports rather than
creating duplicate canonical `- Record:` entries. No generated merge, PR,
GitHub issue or branch cleanup is part of this local repair.

Per-record supplements: [DSMZ](dsmz-followup.md), [KOMODO](komodo-followup.md),
and [standalone solution](solution-followup.md). The [adversarial review](adversarial-review.md)
records remaining uncertainty separately from applied corrections.

The [actual-group retention check](merge-retention.json) fails. Both media
belong to the same two-record group; the standalone solution is correctly
excluded. The DSMZ copy retains 14/14 scoped snippets but not its complete
ingredient fields. The KOMODO copy retains 14/15 scoped snippets and loses
complete stock/procedure/context/provenance fields. Thus 28/29 record-scoped
snippets survive, which is not full evidence retention. No generated merge is
published, and the scientific inputs are not changed to accommodate this loss.

Global merge verification exits 1 with 1,247 name conflicts and 3,287 fingerprint
issues. [Freshness](merge-freshness.json) exits 1: 6,320 tracked outputs versus
6,494 temporary regenerated outputs; 3,720 only tracked, 3,894 only fresh,
1,668 changed and 932 unchanged. The tracked merge files remain unchanged.

Post-edit strict validation passes for all 15,910 normalized records, as do the
three schema checks, ID and variant-link gates, source readback of the affected
500-record medium and solution batches and the 500-record KOMODO batch, Ruff,
Black and whitespace. The cached Python 3.13 selection passes 238 tests. The
initial Python 3.11 selection passed 314 and failed the historical 489 test,
which had loaded its old successor list before the update. Its identical final
rerun passes all 315 tests; the initial failure is preserved. The repository
fast gate is recorded separately. Product/reference validators are unavailable (`oaklib` and
`linkml-reference-validator`); they are not passes. This is isolated local
validation, not maintained-project CI.

`just test-fast` was attempted in the cached Python 3.13 environment with
dependency installation disabled. It stopped at collection with four missing
modules: `dotenv`, `rapidfuzz`, `pandas` and `bs4` (one skipped, 1,616 deselected,
four collection errors). It did not execute a successful fast tier. The journal
contains 27 checks; excluding the superseded initial test failure leaves 20
passes, three unavailable checks and three failed merge gates.

All changes remain local and uncommitted. The read-only inventory of 2,710
remaining standalone water candidates is a next-work lead, not an applied
batch or a reduction of the 5,800 paths outside follow-up coverage.

The [medium 187 handoff](next-medium187-handoff.json) captures a separate,
read-only source check: three unchanged records, two API payloads and the
original PDF's limited support. Its pH disagreement remains unresolved; this
handoff is not an applied plan or additional reviewed-path coverage.
