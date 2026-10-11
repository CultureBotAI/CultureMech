# Five Organic-Medium Concentration Previews

Historical preview. The v3 proposal is now [applied locally](../20261010-utex-organic-five/README.md).
The status below records the preview state; only the applied successor reports
count toward canonical follow-up coverage.

Reviewed the current Malt, Euglena, Polytomella, Ochromonas and Trebouxia records
against their exact UTEX recipes on 2026-10-10. The linked Liver Extract Infusion
recipe was also retrieved and inspected. **No authoritative records are edited.**

The current [v3 proposal](mutation-preview-v3/plan.json) corrects four
extraction-generated water-formula snippets without changing quantities, units
or volume bases. Its [twenty CLI/source checks](mutation-preview-v3/validation.json)
and [78 guard tests plus dry run](mutation-preview-v3/guard-preview/validation.json)
pass. Updated reports, rendering and live reference checks are in the
[combined v2 preview](../20261010-next-utex-integration-preview/v2/README.md).
The v1/v2 discussion below is historical.

[Five preview reports](records/) cover all 22 existing concentration claims and
four proposed agar-variant claims. Each has exactly one exact tracked Record
line and an explicit Preview state. The [coverage check](reports.json) confirms
they add zero canonical coverage: 11,946 / 15,910 remain covered, with 3,964
outside canonical follow-up coverage.

## Proposed Changes

- Retain seventeen numeric quantities. Twenty-six source-URL/snippet evidence
  entries and six enriched bibliography entries support the proposed assertions.
- Qualify Malt's 67.2 g/L as mass per liter of starting water. The recipe adds
  33.6 g to 500 mL water; its heading does not resolve the final-volume ambiguity.
- Qualify Ochromonas's 50 g/L liver-extract stock as a preparation input before
  heating and filtration. No recovered filtrate strength is inferred.
- Remove four unsupported 1000 mL/L water fractions. Preserve initial water and
  makeup instructions without inventing the combined water dose.
- Remove Trebouxia's 825 mL/L total Bristol Medium dose: the source starts with
  approximately 825 mL and uses additional reserved Bristol Medium for makeup.
- Preserve four optional agar formulations as inline variants, without adding
  agar to any liquid parent or calculating a new final-volume concentration.

## Verification And Limits

The [current v2 proposal](mutation-preview-v2/plan.json) retains original/proposed
YAML, exact excerpts, source captures, table coordinates, hashes and arithmetic.
[Independent checks](mutation-preview-v2/validation.json) pass all twenty baseline
and proposed schema/strict commands. Seventeen retained amounts match the source
projection; 82 deliberately altered values, units, bases, removed slots, agar
doses, snippets, identities, history entries or unrelated claims are rejected.

The [isolated guard](mutation-preview-v2/guard-preview/validation.json) passes
78 adversarial tests, Ruff, Black and patch application checking. Its real-schema
dry run reports five pending records, zero changed and zero already applied.
The guard is not installed; application/readback/no-op and rollback are exercised
only in temporary fixture repositories. Cumulative-audit integration and actual
application remain outstanding.

[Rendered proposal checks](render-preview-v2.json) preserve all seventeen quantity
cells, both qualified volume bases and all four optional variants. These are
HTML DOM/content checks, not visual browser inspection; composition graphs remain
unavailable and the renderer marks the output as degraded.

V2 corrects one audit-history issue: preview-only state belongs in reports, not
in prospective applied history. The [revision check](mutation-preview-v2/history-revision.json)
proves all scientific content is unchanged. The original v1 proposal, guard,
reports and receipts remain historical; [v2 reports](records-v2/) and their
[receipt](reports-v2.json) pin the corrected proposal. Both versions are unapplied.

The inverse comparison preserves unrelated fields and existing history. No
authoritative application or post-edit check is claimed. Printed molarities remain
source assertions, not independent molecular-weight calculations. Existing
ontology mappings, role/growth claims and linked-medium compositions are not
newly certified. Authors, publication year and DOI remain unknown; source URLs,
titles, source type, discovery mode and access date are recorded. Linked PDFs
were not inspected. No taxa-media association is added.
