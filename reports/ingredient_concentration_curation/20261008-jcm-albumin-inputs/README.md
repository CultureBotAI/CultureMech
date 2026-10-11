# J201/J220 Albumin And Reagent Input Repairs

Applied locally to JCM J201 and J220. The all-record ingredient goal and the
requested publication workflow remain incomplete. No taxa-media associations
were added. Existing chemical annotations are preserved, not recertified.

## Evidence And Corrections

The four inspected source responses were refreshed and their hashes match the
pinned captures. Three provide formulation evidence: MediaDive J201, MediaDive
J220 and the original JCM220 page. The fourth, JCM201, currently returns no recipe.
Its response is retained as an access-status observation, never cited as recipe
support. J201 is explicitly provider-backed rather than original-page-corroborated.

All 38 reference checks pass: 35 attached evidence entries and three bibliography
entries. Each scientific change has a persistent source URL and exact snippet
in the YAML, with field and preparation-stage scope. Missing authors and publication
years remain absent; source type, discovery mode, access date and capture hash
are recorded in reference notes.

- J201: removed the three false LB supplier nodes and restored the source's
  50 g bovine albumin fraction V batch input. Corrected CMRL 1066 from 100 g/L
  to its 100 ml batch dose, restored 900 ml water, and represented the late
  200 ml gelatin-solution dose and sterile rabbit serum separately. The 7%
  gelatin and final 6% serum labels have unspecified percentage bases; no numeric
  strength, serum dose or final volume was guessed. The preparation action is
  FILTER, not the schema's 0.22-micrometer-specific FILTER_STERILIZE.
- J220: removed the false LB nodes and restored the 10 ml dose of source-labeled
  20% bovine serum albumin fraction V preparation. Separated hemin, glucose and
  cysteine stock doses from their unspecified percentage bases. Preserved
  hemin's 0.05 N NaOH solvent as a nested, unquantified preparation rather than
  converting normality to molarity or asserting a solvent dose. Only the three
  source-designated albumin/glucose/cysteine stocks receive filtration instructions.

The independent audit accounts for all 22 old quantity fields, all 20 API recipe
rows and 65 field claims. It verifies 35 new evidence entries, three references
and two append-only history events; 18 unsupported quantity withdrawals; four
stock-dose corrections; four newly represented numeric inputs; four node relocations;
and the separately scoped late preparations and solvent. The eight current numeric
fields are batch inputs, not final-medium concentrations. Source batch masses
remain in evidence-backed notes, not unsupported g/L fields.

## Verification

Baseline and applied schema/strict/reference checks, independent readback, no-op,
lint, formatting and diff checks pass. All 73 dedicated tests and the 819-test
focused selection pass. The fast tier passes 9,017 tests, with 16 skipped and
1,945 deselected. Strict schema and ID checks pass for all 15,910 records.
Product validation passes with 91 warnings and 96,081 no-adapter skips;
chemical groundings are not all recertified. Global merge verification fails
with 1,247 name conflicts and 3,287 fingerprint issues. Generated-data freshness
fails with 4,275 tracked-only paths, 8,732 fresh-only paths and 2,045 changed
shared paths. All intended checks are terminal in [validation.json](validation.json).
The environment is the existing partial locked Python 3.13 runtime,
not a clean CI run, and the full test suite was not rerun for this localized batch.

Full-corpus routing produces 10,777 groups from 15,910 normalized inputs. The
two repaired records retain their claims in separate closed-schema-valid runtime
outputs. No tracked merged YAML was written. Three generated metadata indexes
were refreshed; their only semantic changes are these records' ingredient and
solution counts.

The cumulative audit verifies 5,159 edited records, 32,733 added evidence entries,
5,609 references and 5,363 appended history events. Coverage remains 11,781 of
15,910 exact paths, with 4,129 outside follow-up reports. Both targets already
had canonical reports; the new `records/` files use `- Follow-up target:` and
do not rewrite or duplicate historical `- Record:` lines. Coverage is not proof
that all ingredient claims in a record are resolved.

## Artifacts

- `context.json`, `plan.json`: pinned baselines, source responses and guarded changes.
- `application.json`, `applied-audit.json`: actual application, readback and no-op.
- `records/`: one supplemental result per exact repaired path.
- `live.json`: three available recipe sources, one unavailable original and reference results.
- `cumulative-audit.json`, `followup-coverage.json`, `reconciliation.json`: current accounting.
- `index-refresh-plan.json`, `index-refresh-application.json`: generated metadata changes.
- `merge-retention.json`: recomputed target retention, not a global freshness pass.
- `validation.json`: terminal results, corpus/source hashes and remaining failures.
- `adversarial-review.md`, `next-work.md`: addressed risks and remaining scope.

The next source captures are preparation for later work, not edits to M194,
M213, M244 or J252 and not new report coverage. Publication and all-record
completion remain unproven.
