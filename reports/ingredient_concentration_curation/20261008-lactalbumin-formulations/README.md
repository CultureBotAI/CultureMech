# Source-Specific Hydrolysate Formulations

Four authoritative normalized records are repaired locally: DSMZ 1021, KOMODO
1021, KOMODO 1021_16929 and TOGO M2287. The guarded application adds **77
evidence entries, nine references and four append-only curation events**.
Every changed scientific claim has an exact supporting excerpt and persistent
source URL in YAML. These are ingredient/formulation claims, not newly added
taxa-media associations. The all-record goal and publication remain incomplete.

## Corrections

- Remove the falsely substituted LB constituents while retaining genuine yeast
  extract and sodium chloride. Preserve original IDs, history, unrelated
  chemical annotations and explicitly superseded historical provenance.
- DSMZ 1021: restore lactalbumin hydrolysate at the API-reported stock rate of
  9 g/L, corresponding to the original 8.10 g Solution A batch input. Restore
  separate A/B preparations, their water inputs and provider-reported basal
  addition volumes. Keep the later 4:1 base/serum ratio as text, not an assumed
  percent basis or fixed serum dose. Move pH 8.0 to Solution A. Preserve the
  source-explicit casein substitution as an alternative, not an extra ingredient.
- KOMODO 1021 and 1021_16929: use each actual detail page's casein hydrolysate
  and reported final-medium mass rates, replacing copied DSMZ stock values.
  Preserve displayed precision rather than substituting calculated values.
  Serum's generic Gram/Mol columns do not establish density or molarity;
  preserve the linked preparation ratio without a numeric serum concentration.
  Null water/gas quantities remain unknown, not zero.
- The DSM 16929 variant retains its own unquantified O2, N2 and CO2 rows and
  no longer inherits a final pH absent from its source. Correct reciprocal
  exact-duplicate links to source derivation and strain-specific variation.
  Source-named strain variation is not a newly curated growth association.
- TOGO M2287: restore 6.5 g/L lactalbumin hydrolysate in the basal recipe,
  correct water from 1 g/L to a 1 L input, and separate the basal concentrations
  from later serum supplementation. Preserve 5% heat-inactivated fetal bovine
  serum as text because its percentage basis is unspecified.

The linked DSMZ protocol retains separate A/B sterilization at 121 C for
20 min, cooling to 50 C, combination and later sterile serum addition. Its
liquid alternative specifies filtration, but neither a pore size nor a separate
quantified agar change; those remain explicitly unknown.

## Evidence And Checks

All five source responses refreshed identically before and after application.
The original DSMZ PDF page image and both KOMODO tables were inspected.
The independent audit covers all **49 old quantity slots**, all **50 source
ingredient rows** and all **201 claim excerpts**. Readback and a no-op rerun
pass. Baseline schema/strict checks pass for all four records. Both focused
selections pass **344 tests**, with lint and formatting checks passing.

Historical reference validation was not fully passing. The initial live check passed 49
of 86 checks; 37 KOMODO checks failed during HTTP fetching. Sandboxed post-edit
CLI attempts encountered DNS restrictions. An approved applied-record retry
then passed 55 checks, with 31 KOMODO table/pH quotations failing in the generic
text extractor. The source captures remain byte-identical, and all literal
excerpts pass the independent table-aware audit. See
[`issue-komodo-reference-validation.md`](issue-komodo-reference-validation.md).

The subsequent [KOMODO parser repair](../20261008-komodo-reference-validation/README.md)
now passes all 86 unchanged reference checks and all four reference CLI commands.
All five sources were refreshed with identical bytes; the two KOMODO responses
required explicit separate public capture after the requests refresh returned
HTTP 403. That failed transport attempt remains recorded, not claimed fixed.

Cumulative accounting is **5,174 edited records and 33,094 added evidence
entries**. Follow-up coverage is **11,786 of 15,910** exact normalized paths,
with **4,124** outside these reports. Covered records may still have unresolved
claims. Only these four normalized records changed relative to this batch's
baseline. Five generated metadata indexes were refreshed; three records have
metadata changes, while the fourth's source identity/ingredient count is stable.
All four repaired formulations retain their claims in distinct, schema-valid
runtime merges. Derived merged YAML was not hand-edited.

Strict schema and serial ID checks pass for all 15,910 normalized records.
Product validation passes with 91 warnings and 96,066 no-adapter skips; this
does not recertify every chemical mapping. This batch's fast tier passes 9,541
tests, with 16 skipped and 1,945 deselected; it predates the later parser repair.
Global merge verification fails with 1,247 name conflicts and 3,287 fingerprint
issues. Freshness fails: 6,320 tracked versus 10,777 fresh outputs, with 4,275
tracked-only, 8,732 fresh-only and 2,045 changed common paths. All batch checks
are terminal in [validation.json](validation.json).
This uses the existing partial locked Python 3.13
environment, not clean CI. Passing narrow checks does not resolve outstanding
global merge/freshness failures.

## Artifacts And Limits

- `context.json`, `plan.json`: immutable inspected sources, baselines and decisions.
- `preview-audit.json`, `applied-audit.json`, `application.json`: independent
  source/amount accounting, guarded application, readback and no-op.
- `records/`: one new M2287 follow-up report and supplements to the three
  existing canonical reports. Older full-corpus audits remain unchanged.
- `live.json`, `applied-live.json`: actual reference results, including failures.
- `next-work.md`: unchanged remaining queues and unresolved source claims.
- `adversarial-review.md`: local self-review, not independent PR approval.
- `next-middlebrook-context.json`: 24 unchanged candidates and 28 source
  captures, not completed record reviews or applied edits.

The initial dry-run stopped on an uninitialized variant list before writing a
plan or any YAML. The list initialization and lint findings were corrected
before the successful preview and tests. No failed data application occurred.

No DOI, source author, publication year, density, unknown dose, gas fraction,
percentage basis or chemical identifier was invented. The unverified
parenthetical Beard et al. citation in TOGO is not promoted to article evidence.
No commit, push, GitHub issue, PR, merge or branch deletion occurred in this batch.
