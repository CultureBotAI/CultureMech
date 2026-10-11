# Remaining Ingredient Review Work

Scope remains all 15,910 normalized YAML records, not only this batch. The
sixteen-record guarded application and post-application reconciliation are
complete; the terminal fast test tier passes 12,702 tests. Follow-up reports cover 11,812
exact paths, with 4,098 outside coverage and 65 previews excluded. A report is
not proof that every amount is verified.

## Source Limits

- JCM1008's operational supplemented wording remains ambiguous despite its
  explicit modified formulation and matching TOGO values. Do not infer sums.
- JCM1132 remains an original-source access gap. The captured MediaDive export
  supports the prepared-base stage but not a newly identified titrant or an
  independently measured post-adjustment volume.
- Two existing M1212 bibliography entries were preserved without reverification.
  Existing chemical mappings/roles and high-metal flags were not recertified.

## Next Records

The [medium323 adjudication](../20261009-synthrophomonas-family/next-323-adjudication.json)
still covers four unchanged candidates, not an applied repair. Recheck exact
record and source hashes before constructing its guarded proposal. Preserve
its nine prior evidence entries and distinguish KOMODO's own formulation from
the DSMZ/MediaDive formulation. The [follow-up inspection](next-323-review-notes.md)
records the freshly checked source differences and remaining physical-state
and identity decisions.

The [S599 schema gap](next-323-schema-gap.json) is now explicit: the source gives
a 1.4 ml nested-stock dose, but no legitimate in-record evidence container is
available for that claim. Address the formulation-evidence schema contract and
its generated artifacts/tests before asserting that dose. This does not block
source review or supported work on the other three medium323 records.

An [isolated schema prototype](next-solution-evidence-prototype-v2.json) adds
only an optional `SolutionRecipe.evidence` field in a temporary schema. Four
baseline records remain valid, generated dataclasses round-trip the new claim,
and three malformed-field probes still fail. All eleven captured-source checks
pass after an in-memory correction of S599's bibliography title to the provider's
`Main sol. 323`. The [first attempt](next-solution-evidence-prototype.json)
failed on that existing title mismatch and remains preserved with its
[diagnostic](next-schema-prototype-reference-diagnostic.json). Neither the
schema proposal nor the title correction is applied to production. This is not
a corpus-wide compatibility result or permission to bypass the current contract.

That adjudication supports the existing resazurin solute rate with explicit
stock strength, dose and final volume; it is not a numerical error. S599's
water value needs a ml/L unit rather than percent. S6552's unsupported percent
entries need source-scoped batch-dose handling without discarding its valid
provider-reported mass rates or inventing density. Conditional agar bases,
required physical state and existing identity discrepancies need explicit
decisions, not silent copying or averaging.

The preceding [31-record acid-name queue](../20261009-halobacteria-family/next-lb-identity-context.json)
and [71-record queue](../20261009-halobacteria-family/remaining-queue.json)
have no target-path overlap with this applied batch. Their source/identity
reviews remain open. All other incomplete corpus records remain in scope.

## Publication Limits

Global merge verification and generated-data freshness are mandatory unresolved
gates. The latest verification still reports 1,247 name conflicts and 3,287
fingerprint issues. No generated merged YAML has been hand-edited and no
GitHub issue, PR, push or merge is claimed for this checkpoint. Local results
use the existing partial Python 3.13 environment, not clean CI.
