# UTEX Soil/Seawater Ingredient Preview

Historical preview. The v2 proposal is now [applied locally](../20261010-utex-soil-seawater/README.md).
The status below records the preview state; only the applied successor reports
count toward canonical follow-up coverage.

Status: **unapplied source-backed proposal for seven exact records**. No canonical
coverage or edited-record totals are incremented by this preview.

The current [v2 proposal](mutation-preview-v2/plan.json) corrects one source
snippet's chemical/optional-label spacing, with no numeric or volume-basis change.
Its [28 CLI/source checks](mutation-preview-v2/validation.json) and
[106 guard tests plus real-schema dry run](mutation-preview-v2/guard-preview/validation.json)
pass. Updated reports and live reference checks are linked from the
[combined v2 preview](../20261010-next-utex-integration-preview/v2/README.md).
V1 links below retain the historical review trail.

[Source triage](source-triage.json) covers 29 existing concentration assertions.
The seven UTEX source accessions were searched throughout normalized YAML with
ignored files included; they select exactly the seven paths in this ledger.
Eight official HTML sources, including Supplemented Seawater, are captured and
hashed. No PDF inspection is claimed for this cohort.

## Proposed Changes

The [YAML proposal](mutation-preview-v1/plan.json) adds 35 scoped evidence entries:

- Five fixed teaspoon soil doses move out of misleading `VARIABLE` concentrations
  into literal notes and evidence. No teaspoon size, density or mass is guessed.
- Five optional calcium carbonate doses move out of mandatory parent composition
  into inline variants. The original descriptors remain in append-only history.
  Calcium carbonate remains mandatory in the distinct 2X source formulation.
- Ten retained doses get explicit input-volume bases. Four unsupported carrier
  fractions are removed while preserving the literal input amounts.
- The one-third formulation retains the source's 67/133 mL inputs, not exact
  one-third/two-thirds fractions. Corresponding parent/child notes are qualified.
- Preparation excerpts support the heat ramp and gradual cooling, the one-fifth
  formulation's 10 C refrigeration, and the agar recipe's do-not-mix instruction.

The proposal retains fifteen structured concentration fields and five optional
carbonate dose descriptions. Source-printed molarities remain explicitly source
assertions; unknown final volumes and publication metadata are not invented.

## Verification And Limits

Fourteen in-process baseline/proposed schema checks pass. The separate
[CLI/source validation](mutation-preview-v1/validation.json) passes all 28 commands.
It checks fifteen retained concentration fields and five optional dose descriptions,
rejecting fifteen altered amounts, fifteen altered units, thirty wrong/missing
volume bases and five altered optional doses.

The [isolated application guard](mutation-preview-v1/guard-preview/validation.json)
now passes 106 adversarial tests, Ruff and Black. Its inverse diff check reconciles
all permitted changes, preserves the original optional carbonate descriptors in
history, and rejects forged plans, source/record drift, links and unsafe rollback.
A real-schema dry run reports seven pending records and zero writes. The saved
patch passes `git apply --check` but remains uninstalled while the J/DAS full-suite
run pins repository code and YAML. Cumulative-audit integration, guarded application,
post-edit checks and publication gates remain outstanding.

[Per-record reports](records/) and the plan retain field paths, old/proposed
amounts, source URLs, exact excerpts, locators and calculations. These are preview
reports, not completed general scientific reviews. Culture conditions, organism
growth, ingredient roles and unrelated salinity claims are not certified here.

The [volume-basis consumer fix](../20261010-volume-basis-consumers/README.md) is
applied locally with focused and installed-wheel checks; full tests are pending.
The original `source-triage-v1.json` is retained; the current ledger corrects the
agar source locator from a table row to the recipe directions.
