# Halobacteria Variant Adversarial Review

These are local findings and dispositions, not created GitHub issues or a PR
review. The independent auditor reparses the captured sources rather than
accepting the proposal's generated values as scientific truth.

1. **P1: Thousandfold trace-metal unit errors. Fixed locally.** M1065, M576,
   M959, M960, M371 and M372 had milligram source amounts encoded as g/L.
   Exact TOGO rows and the JCM one-liter recipes support mg/L, without density
   or molecular-weight assumptions. M1212's already-correct gram equivalents
   are preserved in the prepared-base stage.
2. **P1: Copied base values erase variant formulations. Fixed with a limit.**
   J572, J1008 and J914 now retain the specific Mg/NaCl formulation in the
   source. J1008's operational ambiguity remains visible: adding Mg to an
   unchanged 20 g/L base cannot lower it to 15 g/L. The independent TOGO row
   explicitly gives 15 g/L; neither 35 nor 470 g/L is inferred by summation.
3. **P1: Flattened ingredients overclaim the pH-8 final medium. Fixed locally.**
   J1132 and M1212 now distinguish the prepared J168/M159 base from the final
   adjustment. A 1000 ml input is encoded as a 1 L dose, not 1000 ml/L. Base
   make-up, pH and agar instructions stay at base scope. No later pH-7 step,
   invented carbonate dose, duplicate flat ingredients or assumed dilution
   factor is introduced.
4. **P1: Unsupported water and stock placeholders. Fixed locally.** Six
   false 1 g/L water quantities are removed. JCM make-up water is unquantified.
   S3823's complete nine-component source replaces only the false placeholder
   and incomplete-composition flag; its optional agar instruction remains.
5. **P2: Evidence and relationship scope. Fixed locally.** Wrong duplicate
   classifications, stale exact paths and M1065's wrong NBRC attribution are
   replaced with specific source-backed relationships. The successor proposal
   includes the pH text in J572/J1008 relationship excerpts. Parent ingredient
   arrays and prior evidence/history are unchanged.
6. **P2: Mutation tests could stop at byte equality before testing science.
   Fixed in the application tests.** Negative tests now assert a known current
   state, then audit the candidate at the frozen baseline. This makes altered
   amounts/snippets/history reach the semantic checks. Written-state equality
   and the parent successor chain are tested separately; no hash exemption is
   given to arbitrary later changes.
7. **P2: Table extraction whitespace obscured hydrate formulas. Fixed before
   application.** The first independent HTML-table test attempt failed because
   a separator was inserted at subscript boundaries. The corrected parser
   normalizes text whitespace without splitting chemical formulas. The later
   689-test preview and 725-test application runs pass; the failed attempt is
   not treated as validation.
8. **P3: Applied report boilerplate overstates flag preservation. Fixed locally.**
   The headers now acknowledge S3823's explicitly documented removal of its
   false incomplete-composition flag. The claim rows already reported that
   change. A separate hash-pinned clarification receipt proves that only the
   header wording changed in the sixteen applied reports; original ledgers and
   preview reports remain preserved. No YAML or scientific claim changes.

## Qualified Checks

Every edited claim has a literal captured-source excerpt, a precise field
mapping and matching in-record evidence. Numeric water, quantity/unit changes,
invented snippets, changed identities/roles, flattened stocks, duplicate links,
misordered pH, unrelated flags and rewritten history are rejected by tests.
Whole-batch preflight rejects any changed or symlinked target before writing.

The MediaDive J1132 export lacks a production reference adapter. Its 25 evidence
and bibliography entries are checked against the pinned raw dataset separately.
Two existing M1212 bibliography entries are retained without reverification.
JCM1132 remains an original-source access gap, not a verified original recipe.

The application/readback/no-op is terminal and passes. All 32 actual-written
schema/strict commands and 417 supported reference checks pass. Corpus strict,
ID/product and variant-link checks, presentation preservation, report/index
reconciliation and all fifteen target merge-retention checks pass. All 699
final QA tests pass. The terminal fast test tier passes 12,702 tests, with
sixteen skipped, 3,374 deselected and two dependency warnings. Global
merge/freshness defects and unreviewed corpus concentrations are not waived
or marked complete.
