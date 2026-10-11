# Adversarial Review: Marine Stock Pair

This is a local self-review plus an independent source-row auditor, not an
external PR approval. The reviewed plan is `plan.json`; applied files are checked
against it by byte hash, source membership, annotations, quantities and history.
The 87 new mutation/guard tests pass. Wider terminal results belong in
`validation.json`, not inferences from this scoped review.

## Findings Addressed

1. Main water and local-stock water were collapsed across units and preparation
   stages. M208's 866 g/L becomes distinct 865 ml main and 1 L stock inputs;
   M209's 971 g/L becomes distinct 970 ml main and 1 L stock inputs. The prior
   duplicate annotation is preserved and explicitly superseded in both scopes.
   The auditor counts each old water slot once and each newly separated slot
   once, while retaining both old-to-new lineage links.
2. Local stock solids were flattened into the receiving medium. Only the named
   marine stock tables are restored; only M142's trace-mineral table and M190's
   vitamin table are inherited. Tests reject flattened, missing, extra or
   substituted stock rows, including a vitamin/trace-mineral mix-up.
3. Masses stated in milligrams were imported as g/L. Exact original JCM table
   excerpts corroborate TOGO's form, amount and unit. Original-table ambiguity,
   different amounts and changed forms all block preview. The repair keeps
   batch masses in notes without inventing final volume or g/L.
4. Prepared-stock additions were represented as mass rates. They are now batch
   volumes: M208's marine stock is 0.125 L and the other four inputs are 0.01 L.
   Tests reject mass units or per-liter dose assumptions. Summed liquid inputs
   are not a final-volume statement.
5. M209 requires a separately autoclaved sulfide preparation. Its 0.5 g mass
   is the receiving-batch contribution, not a stock-batch recipe. The 5% basis,
   solvent volume and addition volume remain unspecified. M208 does not inherit
   sulfide preparation. Tests reject invented strength, dose and cross-recipe
   inheritance.
6. Source-specific preparation must survive curation. M208 retains 1 N acid,
   filtration, dispensing, the 80:20:1 gas ratio and post-inoculation pressure.
   M209 retains pH 6.0 before filtration and pH 6.5 at later sulfide addition.
   Neither a pore size nor normality-to-molarity conversion is asserted.
7. M208's original and TOGO sources both print `NaWO4` for the hydrated tungstate
   ingredient. The apparent formula/legacy-grounding discrepancy is explicitly
   unresolved; neither the formula nor mapping is silently normalized. M209's
   legacy phosphate grounding, KNO3 link and `high_metal` flag are preserved,
   not recertified.

## Guards And Limitations

All targets are checked before any write; tests cover concurrent edits,
symlinks, forged plans, readback and no-op application. Each old quantity and
each source row has a claim decision. Every evidence entry and extra excerpt
is checked for literal support and field attachment; duplicate references,
missing claims, invented years and changed history are rejected.

The index generator still checks hierarchy enrichment only at the top level.
Moving M209's existing KNO3 link to its correct stock scope changes the generated
flag and aggregate count without deleting the annotation. The guarded index
refresh permits only the reviewed records' expected metadata and this one
documented aggregate change.

Unstated final volumes and chemical-grounding questions remain unresolved.
The report does not certify growth associations, all corpus records, global
merge correctness, clean CI, or publication readiness.
