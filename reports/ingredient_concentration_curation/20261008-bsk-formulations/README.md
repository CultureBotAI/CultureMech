# Three Source-Specific BSK Formulations

Applied locally to TOGO M2410, DSMZ 1829 and JCM 173. This adds 69 evidence
entries, five references and three append-only curation events. Every changed
scientific claim has a persistent source URL and exact snippet in its YAML.
These are ingredient/formulation claims, not new taxa-media associations.
The all-record goal and publication workflow remain incomplete.

## Corrections

- All three: remove the false LB constituent expansion and restore the exact
  source's bovine serum albumin input. Keep genuine yeast extract, prior history,
  stable IDs and unrelated chemical annotations. Preserve the superseded LB
  provenance as historical, not current formulation evidence.
- DSMZ 1829: its original PDF specifies a final 100 ml volume. Albumin is
  0.85 g / 0.1 L = 8.5 g/L; rabbit serum is 8.56 ml / 0.1 L = 85.6 mL/L,
  not 8.56 g/L. Nine existing mass rates retain source support. Deionized water
  is makeup, not a fixed 100 ml input. Keep 1 M NaOH at titrant-stock scope and
  final pH 7.3. No titrant dose, filter pore size or separate makeup-versus-pH
  adjustment order is invented.
- JCM 173: restore separate Solutions A/B, their water inputs and provider-
  reported stock rates. Do not treat those rates or water volumes as final-
  medium concentrations or fixed parent doses. The original corroborates
  **2.5 mg**, not grams, of Neopeptone. Keep CMRL with glutamate, Wako fraction V
  albumin, 1 N NaOH, 0.22 micrometer filtration, separate B autoclaving and a
  40 ml dose of sterile serum heat-inactivated at 56 C for 45 min. Withdraw the
  unsupported final combined-medium pH assertion; preserve the earlier pH
  adjustment instruction instead. The page's general autoclave default remains
  explicitly qualified and applies only to the separately autoclaved B.
- TOGO M2410: restore 50 g albumin as a batch amount, the 900 ml water input,
  100 ml of 10X CMRL without glutamine, 1 N titrant and a 200 ml gelatin-stock
  dose. Preserve dry batch masses without assuming final g/L. Gelatin's 7
  percent and serum's final 6 percent lack a stated percentage basis; retain
  them as qualified text. Preserve unheated serum, 0.2 micrometer filtration,
  preparation timing, storage, incubation and container-fill context.

## Evidence And Checks

The five refreshed official sources match the pinned captures exactly. All
74 complete reference checks pass (M2410: 14, D1829: 29, J173: 31). The original
DSMZ page image was inspected. All 139 claim excerpts match their captures;
these include additional excerpts scoped inside evidence explanations, beyond
the primary snippets checked by the reference CLI.

All 373 pre-application focused tests, lint and formatting checks pass, as do
baseline and applied schema/strict/reference checks. The independent audit
accounts for all 40 old quantity slots and all 37 source ingredient rows.
Readback and a no-op rerun pass. The final focused selection also passes 373
tests after registration in the cumulative audit. Five generated metadata
indexes were refreshed through the maintained generator. Full-corpus routing
keeps all three repaired formulations separate and retains their claims in
schema-valid runtime merges; generated merged YAML was not hand-edited.

Cumulative accounting is **5,170 edited records and 33,017 added evidence
entries**. Follow-up report coverage is **11,785 of 15,910** exact normalized
paths, with **4,125** outside these reports. M2410 contributes one new follow-up
path; earlier historical audit reports are distinct and were preserved. Report
presence is not scientific completion. Strict schema and serial ID checks pass
for all 15,910 normalized records. Product validation passes with 91 warnings
and 96,070 no-adapter skips; this does not recertify every chemical mapping.
Global merge verification still fails with 1,247 name conflicts and 3,287
fingerprint issues. Freshness also fails: 6,320 tracked versus 10,777 freshly
generated outputs, 4,275 tracked-only, 8,732 fresh-only, 2,045 changed and zero
unchanged. Those fresh merges were temporary audit outputs, not applied files.
The fast tier passes **9,443 tests**, with 16 skipped, 1,945 deselected and two
warnings (868.99 seconds). All intended checks are terminal in
[`validation.json`](validation.json), including the two failing global gates.
The runtime is the existing partial locked Python 3.13 environment, not clean
CI, and this is not the complete test suite.

## Artifacts And Limits

- `context.json`: immutable three-record baseline and five inspected sources.
- `plan.json`, `preview-audit.json`, `applied-audit.json`, `application.json`:
  guarded decisions, independent audits, application, readback and no-op.
- `baseline.json`, `live.json`, `preapply-focused.json`: successful pre-edit gates.
- `validation.json`: reconciled terminal checks, immutable corpus/code hashes,
  actual cumulative counts and explicit remaining/publication limits.
- `records/`: one new M2410 follow-up report and two supplements; earlier audit
  and canonical curation reports are preserved.
- `initial-preview/`: preserved first preview/source check. A final manual read
  caught and removed an implied makeup-before-titration order before application.
- `next-work.md`, `issue-m2410-addition-order.md`: remaining scientific work.
- `adversarial-review.md`: local self-review, not independent PR approval.

M2410's API array is not accepted as the dry-ingredient addition order. The
Barbour article lead remains text-accessible but without a successful binary
capture/inspectable table image; it is not cited as verified amount evidence.
Unknown source bibliographic authors/year and percentage bases stay unknown.
Unchanged chemical groundings are not recertified merely by amount review.

No commit, push, GitHub issue, PR, merge or branch deletion occurred in this batch.
