# Corpus Ingredient Concentration Review

**Status: full-corpus structural/evidence-gap audit complete; scientific source-by-source review incomplete.**

All records in the local tracked corpus were parsed and inventoried. Every exact
path has its own report, including records with no structured composition. This
is not a claim that every concentration has been scientifically verified.
No recipe YAML, merged product, schema, or existing review report was changed.

## Scope

- Reviewed checkout: `ea4fad40114940af87daf1d56c9cad56beec8cca`.
- Upstream main observed during this run: `70a34fef7032a8c024fa2bbf721156d94f19f3c0`.
  The review is pinned to the local checkout; it does not certify later upstream changes.
- Inventory started: 2026-10-05T17:57:47Z; finished: 2026-10-05T17:59:15Z.
- Selection: exact `git ls-files` YAML paths under normalized and merged record directories.
- Normalized records are authoritative. Merged records are derived and counted
  separately, not as additional independent recipes or scientific confirmations.
- Normalized scope includes 10,832 media and 5,078 stock/base solution records,
  using the repository's maintained record-kind classifier.

| Coverage | Normalized | Merged |
| --- | ---: | ---: |
| Tracked records / per-record reports | 15,910 | 6,320 |
| Structured ingredient/stock concentration entries | 220,957 | 105,321 |
| Separate inline-variant text contexts | 53 | 34 |
| Records with no structured ingredient/stock/variant rows | 261 | 0 |
| Closed-schema errors | 0 | 0 |
| Claim rows with an inspected source during this run | 12 | 0 |
| Records with at least one such source check | 4 | 0 |
| Records whose listed concentration claims were all source-checked | 1 | 0 |

The structured-entry counts include missing and source-variable quantities;
they are not counts of asserted numeric concentrations. Free-text notes and
preparation steps were not exhaustively converted into individual quantity
claims. Inline variants remain text contexts pending detailed source review.

## Evidence Coverage

At baseline, **no structured concentration entry had an explicitly scoped
DOI/URL, nonempty snippet, SUPPORT classification, and explanation together**.
This is a structural evidence finding, not proof that every amount is wrong.
Recipe-level bibliographies, import notes, and growth snippets do not establish
an ingredient concentration by themselves.

| Baseline structured concentration evidence | Normalized | Merged |
| --- | ---: | ---: |
| No scoped evidence entry attached | 220,913 | 105,281 |
| Ingredient evidence exists but lacks the required DOI/PURL/snippet combination | 7 | 7 |
| Recipe-level evidence requires scope review | 37 | 33 |
| Structurally complete scoped DOI/URL-plus-snippet candidate | 0 | 0 |

The eight normalized records with root/source-data evidence were inspected:
those excerpts describe growth, community membership, or study context rather
than the individual ingredient amounts. Seven ingredient evidence entries are
all in TOGO M1308; they use `DSMZ:J1219` and lack snippets. Their source was
inspected in this run; see the findings below.

Nine normalized variant contexts and their nine derived copies contain
DOI-plus-snippet candidates. Full-text retrieval for their ten cited DOI
identifiers failed; candidates were not promoted to verified evidence.
For three references, PubMed identified the corresponding paper, but paper
identity is not verification of its concentration quote. PMC pages returned
browser-check pages, Europe PMC retrieval was unavailable, and an independent
open-access XML request for PMC3008241 returned HTTP 500.

## Triage Findings

These are screening flags, not confirmed errors or permission to change values.
The existing plausibility detector only checks selected direct `G_PER_L`
ingredient patterns in media, excluding stock-solution records.

| Finding | Normalized entries | Normalized records |
| --- | ---: | ---: |
| Missing concentration object | 212 | 97 |
| Explicit VARIABLE value needing source interpretation | 8,976 | 6,725 |
| Range/nonnumeric value under another unit | 38 | 33 |
| Unasserted stock-concentration candidates | 128 | 66 |
| Potential indicator/vitamin unit slip | 4,502 | 1,910 |
| Potential trace-stock flattening | 4,435 | 2,246 |
| Water quantity represented as mass concentration | 518 | 515 |

There are 9,455 plausibility-flagged entries across 3,375 normalized records.
The merged layer has 8,808 such entries across 2,627 records. These layers
overlap scientifically and must not be summed as independent findings.
Some absent or VARIABLE concentrations are legitimate titration, gas, or
preparation quantities; do not fill them with conventional numbers.

## Source-Checked Findings

All following findings are report-only. [Source checks](source_checks.json)
contain exact snippets, field paths, old-value assertions, source locators,
calculations, and proposed changes where support is sufficient.
[Source metadata](source_documents.json) records source type, discovery mode,
access date, and unavailable bibliographic fields without inventing them.

1. **DSMZ 962a: stock components are flattened into direct ingredients.**
   Nitrilotriacetic acid is represented at its stock amount; calcium explicitly
   sums a stock quantity with a medium quantity without preserving dilution.
   Restore the stock boundary before calculating final concentrations. Do not
   assume final volume from the water amount alone.
   [Record report](records/normalized_yaml/bacterial/DSMZ_962a_THERMOVENABULUM_MEDIUM.md).
   [Inspected DSMZ recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium962a.pdf).

2. **DSMZ 1255: undiluted SL-10 iron appears as a direct ingredient.**
   The stored iron amount belongs to the stock solution, not the receiving
   medium. Preserve stock composition and addition dose separately before
   assigning a final concentration.
   [Record report](records/normalized_yaml/bacterial/thermovenabulum_medium.md).
   [Inspected DSMZ recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1255.pdf).

3. **TOGO M1308 / JCM 1219: water and methanol volume units were lost.**
   The water row should retain preparation volume rather than `G_PER_L`.
   Methanol is specified as a batch volume, so its stored mass concentration
   is unsupported; replacing the unit alone would still assume final volume.
   KOH is explicitly titrated to pH, so a fixed amount must not be invented.
   Four salt/buffer batch amounts were inspected, but their precise final-volume
   denominator remains unresolved after the additional liquids.
   [Record report](records/normalized_yaml/bacterial/TOGO_M1308_Methylotroph_Medium.md).
   [Inspected JCM recipe](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1219).

4. **JCM 805: existing broth and water amounts are supported; ingredient evidence is missing.**
   Both listed quantities agree with the inspected JCM-attributed PDF, including
   its explicit final-volume heading. Add scoped evidence rather than changing
   those amounts.
   [Record report](records/normalized_yaml/bacterial/1_10_r2a_broth.md).
   [Inspected JCM recipe hosted by DSMZ](https://www.bacmedia.dsmz.de/pdf/J805).

Across these four normalized records: five correction findings, two
evidence-only findings, one legitimate nonquantified dose, and four unresolved
final-volume interpretations. The reviewed quotations and conclusions were not
automatically propagated to derived records or similarly named variants.

## Validation and Coverage

- The existing closed-schema validator scanned all 22,230 paths with zero
  error rows. The narrower open-schema pass was not run separately.
- The validator ran in an isolated Python 3.11 environment with LinkML and
  PyYAML, not the repository's default Python 3.13 environment.
- Corpus-wide term/reference validators were not run. Four source documents
  were manually inspected; DOI resolver failures are not validator passes.
- Inventory-driver self-checks cover missing versus zero, negative values,
  PMID-only evidence rejection, nested stocks, and the rule that syntactic
  evidence candidates must not become verified claims.
- Coverage verification found 22,230 Markdown reports, 22,230 unique exact
  targets, and exactly one `- Record:` line per report. Missing, duplicate,
  and stale targets: zero.
- Every record's SHA256 still matches the inventory snapshot. No corpus file
  changed during this review.

See [validation details](validation_complete.json),
[strict validation output](strict_validation.tsv), and
[coverage verification](coverage_verification.json).

## Local Source Search

Gitignore-independent searches included hidden/ignored files under `data/raw`,
the expected raw-YAML/research locations, repository concentration tooling, and
existing review reports. The raw directory had fourteen files, largely README
files plus mapping tables and one sample PDF; `data/raw_yaml` and `research`
were absent in this checkout. Prior JCM 805 reports were found and used as
leads, not as independent concentration evidence. These search results do not
establish absence of evidence in the literature or elsewhere on the machine.

## Outputs and Remaining Work

- [Record manifest](manifest.tsv): one row per exact tracked path, report path,
  record hash, validation, and source-check coverage.
- `records/`: one Markdown result per record, preserving layer and exact path.
- `claims.tsv.gz`: all 326,365 claim/context rows, including pending work.
- `inventory.jsonl.gz`: the machine-readable inventory used to generate reports.
- [Summary counts](summary.json) and [run scope](run.json).
- [Unverified source leads](source_queue.json): discovery queue, not proof of
  recipe identity or concentration support.
- [Unavailable DOI references](unavailable_references.json): retrieval failures
  specific to this run, not declarations that these publications do not exist.
- `review_driver.py` and `verify_coverage.py`: retained report-generation and
  verification drivers; run from the repository root. They do not modify recipes.

### Publication Review

Adversarial self-review for [PR #563](https://github.com/CultureBotAI/CultureMech/pull/563)
reproduced and addressed three tooling defects:

- [#564](https://github.com/CultureBotAI/CultureMech/issues/564): validation now
  requires successful status, complete record coverage, and matching inventory,
  schema, and validation-report hashes. Missing validation remains pending;
  inconsistent results fail before reports are written. Coverage checks remain
  active under optimized Python.
- [#565](https://github.com/CultureBotAI/CultureMech/issues/565): each manual
  source check is bound to the reviewed record ID/hash, ingredient name/identity,
  and old concentration. Duplicate, unmatched, or incomplete checks fail before
  output writes. Existing source conclusions and quotations are unchanged.
- [#566](https://github.com/CultureBotAI/CultureMech/issues/566): failed scans
  retain diagnostic rows but exit nonzero. Render rejects failed or incomplete
  inventories; new scans observe the local `origin/main` ref instead of reusing
  this run's historical SHA.

The regression fixtures are in `tests/test_concentration_review_reports.py`.
The retained drivers reproduce this snapshot; they are not a source-research
engine. Replaying a validated snapshot against a different schema or corpus must
fail rather than silently relabel its historical results as current.

**Remaining:** source-by-source research for nearly the entire corpus. Only
twelve structured concentration entries were source-inspected in this run;
326,266 other structured entries remain without a completed source check,
alongside the 87 inline-variant contexts. Prioritize stock/unit mistakes and
missing quantities, inspect original source amounts and denominators, retain
legitimate nonnumeric doses, then propose changes with exact evidence. Applying
any correction still requires an explicit curation request.
