# JCM Ingredient Curation: First Applied Batch

Status: **partial progress toward corpus-wide curation, not completion**.

Follow-up: the initial counts below are historical. The later
[M1308 stock review](../20261007-m1308-stock-followup/README.md) adds twelve
evidence-only stock claims, leaving six main-medium concentration gaps and both
variants unresolved. It revisits an already counted record; cumulative totals
are in the [current status](../README.md).

Baseline commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`.
The checkout was clean and `origin/main` was fetched before this batch.
Authoritative normalized YAML was edited; the earlier full-corpus audit remains
an immutable historical snapshot. No growth/taxa-media associations were added.

## Applied Results

| Exact record | Claims inspected | Corrections applied | Evidence-only claims | Unresolved claims |
| --- | ---: | ---: | ---: | ---: |
| [TOGO M1308](TOGO_M1308_Methylotroph_Medium.md) | 38 | 7 | 13 | 18 |
| [JCM 805](1_10_r2a_broth.md) | 2 | 0 | 2 | 0 |
| [TOGO M840](TOGO_M840_1_10_R2A_Broth.md) | 2 | 0 | 2 | 0 |
| Total record-local claims | 42 | 7 | 17 | 18 |

The two R2A records are source duplicates, not independent scientific
confirmations. Twenty new evidence entries cover 24 supported record-local
claims; the five stock-addition claims share one scoped recipe-level entry.
Every changed quantity has an official source URL, exact snippet, locator, and
conversion explanation in the YAML. The other additions support existing
quantities or the source-explicit variable KOH dose. Three append-only curation
events record the changes with `curator: codex`.

M1308's water, methanol, and five stock doses are now volume-only `L` values per
prepared batch, rather than unsupported `G_PER_L` values. Stock concentrations
are kept separate from stock doses. No density or final-medium volume is assumed.
Ten trace-element concentrations are supported by the source's explicit stock
final-volume instruction. Six main-medium masses and twelve Se/W or vitamin
stock masses retain their previous values without claiming a verified final
concentration. Both inline variants remain unchanged and incompletely reviewed.

## Inspected Sources

- [JCM 1219](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1219):
  main composition, titration, and post-autoclave addition tables.
- [JCM 284](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=284):
  linked trace-element and Se/W stock recipes; only the trace-element stock has
  an explicit make-up-to-volume instruction in the inspected section.
- [JCM 197](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=197):
  linked vitamin stock; amount cells inspected, final-volume basis unresolved.
- [JCM 805 PDF hosted by DSMZ](https://www.bacmedia.dsmz.de/pdf/J805):
  broth and water amounts, explicit final-volume heading; downloaded, extracted,
  rendered, and visually inspected. The original JCM 805 CGI URL and TOGO pages
  were unavailable through the web tool. The TOGO record's existing JCM 805
  lineage and exact two-ingredient formulation identify the source duplicate.

Discovery modes are existing-record-reference and cross-reference. Source type
is culture-collection recipe/page. Titles, organization, access date, and
locators are recorded in the new bibliography entries; individual authors and
publication year are not stated by these sources. Copyright dates are not
treated as publication years. No DOI was invented for these institutional URLs.

## Verification

- Three-file closed-schema baseline and post-edit checks: zero errors.
- `just validate-schema` passed for all three records in the isolated runtime.
- Write-time closed-schema validation ran before any recipe write.
- Guarded application pinned exact git paths, record IDs, baseline SHA256s,
  ingredient identities, and old quantities. The whole batch was validated
  before writes; concurrent differences were refused. A second apply was a
  recipe no-op, without duplicate evidence or curation events.
- Existing YAML presentation and historical events were preserved; only the
  seven intended quantity objects changed. Previous evidence was retained.
- Focused tests plus concentration-plausibility regressions: 83 passed,
  including 15 new concentration-evidence tests.
- Merge/runtime regression selection: 37 passed (includes the same 15 new
  curation tests; do not add the two totals as unique tests).
- `git diff --check`: passed.
- Project Python 3.13 setup failed building the unrelated `llvmlite==0.46.0`
  dependency on this macOS machine. Validation/tests used an isolated Python
  3.11 environment with the repo source and current schema.
- `just validate-references` could not run because the isolated environment
  lacks `linkml-reference-validator`. Source and snippet checks above are manual,
  not an automated reference-validation pass.
- `just verify-merges`: failed with 1,247 duplicate canonical-name conflicts
  and 3,286 fingerprint issues in the untouched merged corpus. Its stored
  statistics also predate the current inventory. All three edited records retain
  their baseline ingredient-identity fingerprints; no record identity, name,
  ingredient membership, or derived merge file was changed by this batch.
- The initial pure-Python parsing runs were explicitly terminated after the
  performance bottleneck was confirmed, not counted as passes. The complete
  checks were rerun with PyYAML's native `CSafeLoader`, preserving the same
  command, corpus scope, merge rules, and Python YAML emitter. Both safe parsers
  agree on all three edited records in both their before and after states.
- `just audit-merge-freshness --json`: completed with exit 1 (drift). It found
  6,320 tracked versus 6,461 freshly generated files: 3,723 filenames only in
  tracked output, 3,864 only in fresh output, 1,469 shared filenames with changed
  content, and 1,128 unchanged files. These are filename/content comparisons,
  not counts of independently missing scientific recipes. Timestamps were
  normalized by the maintained comparison routine. No blanket regeneration was
  copied into the worktree in this small curation batch.
- The affected freshly generated groups were inspected before temporary-output
  cleanup: M1308 preserves its full ingredients, solutions, evidence, and
  references; the merged JCM 805/TOGO M840 group preserves the curated ingredients
  and source references. This proves the maintained generator carries these
  changes, not that the tracked derived corpus is current.

## Additional Source Context

After applying this batch, a direct HTTPS download of
[MediaDive J1219 JSON](https://mediadive.dsmz.de/rest/medium/J1219) succeeded even
though retrieval through the web tool failed. The response identifies JCM 1219
and links the same original recipe. Its SHA256 was
`ec7bff0980d24724c1052f1e90796ca659808e61f3206a93b61376d2e1dbac67`.

The response declares main solution 5347 with `"volume": 1005` and explicit
`g_l` values. Its linked stock solutions 3980, 3981, and 3861 have
`"volume": 1000` and ingredient `g_l` values. This is useful evidence for a
follow-up, but its main-volume convention must be distinguished from the
original JCM page: the seven listed liquid additions total 1004.81 ml before
accounting for titration. This batch did not replace M1308's remaining amounts
with API-derived concentrations or assert that the API volume is a measured
final volume. The API's stock definitions can be reviewed independently to
  resolve the twelve pending Se/W and vitamin concentration claims.

The standalone endpoint `/rest/solution/5347` was also retrieved successfully.
It explicitly supplies the upstream compound identifiers, optional/conditional
markers, stock-strength attributes, and original amount units, which should be
checked before matching record fields. Inspection of
`scripts/import_mediadive_solutions.py` found that its current conversion labels
per-liter `ml` quantities as `PERCENT_V_V`. That conversion does not divide by
ten to produce a percentage; it explains the solution record's impossible water
percentage. Do not rerun that importer as a correction step before repairing and
testing its unit handling. No importer change or corpus reimport was performed
in this batch.

Retrieved source hashes for reproducibility:

- JCM 805 PDF:
  `9dc08d379ecf378ddad57ad7129c115df68779031af2ef68289a51b0e6496956`.
- DSMZ 1255 PDF (next-batch source, not yet applied):
  `633e2f20abda714f98b37c85183ccf8ef01624757c459ffaf161cf62b92c7097`.

## Remaining Work

The all-record objective remains active. These three records do not stand in for
the normalized corpus, derived merges, or all concentration claims.

1. Restore source-supported stock boundaries for DSMZ 962a and 1255, starting
   from the prior audit's flattened mineral/SL-10 findings. Their official PDFs
   were retrieved again on 2026-10-07; no correction was applied to those records
   in this batch.
2. Review `methylotroph_medium.yaml` and `mediadive_5347_Main_sol_J1219.yaml`
   independently. Inspection found flattened stock quantities and liquid doses
   represented as mass concentrations or volume percentages. Do not propagate
   M1308's corrected doses by name alone.
3. Resolve the 18 denominator gaps and two variants reported for M1308 using
   additional primary-source context, or retain explicit unresolved decisions.
4. Continue source-by-source review of every other authoritative record, with
   evidence on every applied edit and per-record results. Reconcile derived
   products through the maintained pipeline, not hand-edited merged YAML.
