# JCM Stock Preparation Follow-up

Applied locally to J151, J187, J197, TOGO M142, M180 and M190. This is not
completion of whole-corpus concentration review or publication approval.

## Source And Scope

- Reviewed commit: `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`.
- Frozen input and nine HTTP-200 captures:
  [next-stock-source-context.json](../20261008-methanogen-boundaries/next-stock-source-context.json).
  SHA256: `291cb565a506c5d89690780c758275f68b42dc1895fb629bd5875ec3bbb45752`.
- Source APIs are MediaDive J151/J187/J197 and TOGO M142/M180/M190;
  original collection pages are JCM 151/187/197. The original pages were
  re-opened during this follow-up. Dataset versions are not treated as identical.
- All six current input hashes matched the frozen inputs before editing.
  `baseline-source-hashes.json` covers all 15,910 tracked normalized inputs.
- `plan.json` is the applied decision plan. `preview-initial.json` is an
  earlier, unapplied draft with less explicit preparation context.

## Applied Changes

The independent audit accounts for all 185 original quantity slots and 267
claims. It verifies 217 new evidence entries, 11 source references, and six
append-only curation events. No taxon-medium association was added.

- Restore separate salt-base, mineral, vitamin and acid preparations rather
  than summing their ingredients into the receiving medium.
- Preserve all original ingredient annotations and history, including copies
  split back into separate source-supported stocks. Former duplicate-collapse
  notes remain historical, not current quantity claims.
- Withdraw 111 unsupported quantity assertions. Source batch masses remain
  in evidence-backed notes; none are silently converted to final g/L.
- Keep MediaDive stock rates explicitly provider-qualified. They do not prove
  measured stock final volumes or receiving-medium concentrations.
- Store explicit water and stock-addition volumes in liters per batch;
  distinguish 7.7 M HCl reagent strength from its 10 ml FeCl2-stock addition.
- Restore separately sterilized percentage-labelled reagents. Unknown percent
  bases and addition volumes are not inferred. Their component notes specify
  receiving-batch contributions, not recipes for an unspecified stock volume.
- Restore pH 6.8 for J197/M190 and 6.2-6.4 for J187/M180. Trace-stock pH 7.0
  stays at stock scope. J151 main preparation uses filtration, not an
  unqualified autoclave action; no filter pore size is guessed.
- Expand M180's explicitly referenced M190 vitamin preparation with M190
  source evidence, without asserting that the complete media are duplicates.

## Verification

- `baseline.json`: all twelve per-record schema/strict checks passed.
- `preview-audit.json` and `applied-audit.json`: independent source-row,
  unit, preparation-scope, annotation, source-quote and history checks.
- Focused repair and shared-helper suite: 147 passed. Combined repair,
  record-I/O and concentration-plausibility suite: 186 passed.
- Fast tier: 8,035 passed, 16 skipped, 1,890 deselected in 517.65 seconds.
  This used the partial locked Python 3.13 environment, not full CI.
- `validation.json`: terminal statuses/log paths for per-record and corpus
  gates, readback, no-op apply, broad tests, IDs, products and merge gates.
  All 15,910 strict-schema checks and the ID gate pass. Products exit 0 with
  91 non-blocking warnings and 96,077 no-adapter skips. Legacy merge verification
  exits 1 with 1,247 name conflicts and 3,287 fingerprint issues. Freshness
  exits 1: 6,320 tracked versus 10,777 fresh outputs, 4,275 tracked-only,
  8,732 fresh-only, 2,045 changed shared paths and zero unchanged shared paths.
- `reference-validation.json`: 217/217 stored primary snippets match frozen
  source text literally; installed matcher passes 213 and rejects four JCM
  table snippets. All six installed reference commands exit 1, also reporting
  synthetic API-title versus URL-fallback mismatches. This is not an automated
  reference-validation pass. Additional excerpts/locators are checked by the
  independent audit, not counted as separate evidence entries.
- `merge-retention.json`: all 15,910 inputs routed, 10,777 formulation groups;
  the six targets are singleton groups and their runtime outputs preserve all
  reviewed assertions and pass schema checks. This is not a fresh semantic
  audit of every other output. No tracked merged YAML was regenerated here.
- `index-refresh-plan.json` and `index-refresh-application.json`: guarded
  publication of generator output for five indexes plus recipe statistics.
- `final-checks.json`: final hashes, report uniqueness, terminal gates and
  source inventory reconciliation. Broad validation is terminal; publication
  readiness is false because the reference and merge gates remain unresolved.
  The final repair/shared-helper/index/manifest selection passes 186 tests;
  lint, formatting and diff checks pass. Only the six planned normalized
  records changed relative to the complete baseline hash inventory.

## Remaining Issues

1. JCM197's ingredient table spells the sulfide differently from its
   preparation. J197/M190 retain this explicit disagreement without a numeric
   sulfide concentration or recertification of existing chemical annotations.
2. No percent basis or missing stock dose was established for the separately
   prepared reagents. Normality remains text, not inferred molarity. Five
   legacy gas VARIABLE placeholders remain unchanged and unsupported.
3. M180's existing `high_metal` flag and coarse chemical groundings were not
   recertified. J151's pre-existing J261 SOURCE_DUPLICATE candidate link is
   retained pending an independent review; this cohort does not validate it.
4. J187/M180 preparation text mentions bicarbonate both in the initial mix
   context and as a separately filter-sterilized addition. The original
   instruction is retained, not silently rewritten to resolve that ambiguity.
5. The maintained index generator examines only direct ingredients for legacy
   MIM hierarchy links. Moving J151's KI into its proper stock removes that
   generated flag (1477 to 1476), although the annotation survives unchanged.
   Nested-aware indexing needs a separately tested cross-corpus change.
6. API title handling, HTML-table snippet normalization, legacy merge integrity
   and freshness gates remain publication work. These checks are not bypassed.

Canonical J151/J187/J197 curation reports link to this follow-up; their old
tables remain historical. M142/M180/M190 each have one new canonical report
within `ingredient_concentration_curation`. Reports do not imply every
concentration is verified. The current coverage audit reports 11,753/15,910
follow-up paths, with 4,157 outside that coverage.

The cumulative semantic diff audit records 5,125 edited normalized records,
30,769 new evidence entries, 5,467 references and 5,325 curation events.
These are cumulative changes, not quantities all added in this cohort.
Commit/push, GitHub issue/PR review, merge and branch cleanup remain pending.

The [next J261/M253 handoff](next-j261-handoff.md) records newly inspected
variant evidence, a wrong exact parent path and a copied-formulation defect.
Those next-cohort records remain unchanged; their capture is not counted as
additional completed coverage.

`m142-dependent-stock-candidates.json` inventories 103 exact tracked records
with 107 named M142 stock-reference nodes; 99 records are outside current
follow-up coverage. The search included ignored/hidden files. This is a
candidate inventory, not verification of their stock identities or doses, and
does not increase reviewed coverage.
