# Yeast Mineral Ingredient Review Decisions

## Source Findings

1. Correct para-aminobenzoic acid amount and identity together. Both primary
   papers specify 0.2 mg/L final vitamin concentration. Current records contain
   0.1458 mM with CHEBI:17836, the conjugate base. CHEBI:30753 is the verified
   acid candidate. Do not describe this change merely as unit normalization.
2. Preserve the 1992 molybdate formula ambiguity. The page image, not just OCR,
   prints `NaMoO4.2H2O`. Do not assign the later paper's disodium identifier or
   concentration as though it appeared here. The hydrate suffix is also
   inconsistent with the current anhydrous grounding.
3. Keep final-volume boundaries explicit. Thirteen mineral quantities in each
   1996 record are water-input amounts, not verified final-medium molarities.
   Seven vitamin concentrations and the initial batch carbon concentration
   have separate explicit final/initial concentration statements.
4. Supply the missing antifoam with formulation-specific evidence: quantified
   0.025 mL/L for 1992; unquantified final concentration with the 0.05 mL water-
   input amount recorded in notes for 1996. Do not infer density or a final
   volume.
5. Repair filtration-only preparation when applying the ingredient changes.
   Both papers heat-sterilize the medium at 120 C, then add filter-sterilized
   vitamins. Neither inspected passage states the imported 0.22 micrometer
   pore size. Avoid inventing sterilization time or carbon-stock handling.
6. Qualify both ends of the ethanol variant relationship. Similar stored
   ingredient lists do not prove the two source formulations differ only in
   ethanol dose: antifoam input and experimental stages differ too. Preserve
   distinct records and IDs; this review does not authorize merging them.

## Application Requirements

These are the historical preview requirements. Guard installation and actual
application/readback/repeat no-op are now completed in the
[applied successor](../20261010-yeast-mineral-ingredients/README.md); its receipts
track the remaining post-edit checks.

- The preferred `mutation-preview-v2` contains supporting snippets in the
  proposed YAML for every amount, identity, antifoam, preparation and
  relationship-description edit. Eight proposed schema/strict checks pass.
  The independent semantic audit checks all 84 claims and rejects forty altered
  previews. The separate guard draft passes 68 tests and a real-schema dry run.
  All application tests use temporary repositories, not authoritative recipes.
- Install and apply the tested guard after the preceding frozen fast-tier run
  terminates and its checkpoint is pinned. The guard rejects source drift and
  forged or reordered plans before recipe writes. Schema validity alone does
  not constitute scientific verification.
- Preserve original evidence, history and unrelated claims. Append a precise
  curation event; make repeat application a no-op and preflight all records
  before writing any of them.
- Keep 56 supported amount proposals separate from 26 unresolved amounts and
  two conflicted amounts. Retaining an amount with an uncertainty note is not
  primary-source verification.
- Run actual application/readback/repeat no-op and post-edit schema/reference
  checks, and verify source-content retention through runtime merging. Reconcile
  cumulative counts only after application. Guard-draft tests already cover drift,
  forged-plan rejection and partial-failure behavior; no crash-atomic multi-file
  guarantee is claimed.
- Preserve this preview as historical evidence. It must not create duplicate
  canonical reports or inflate completed follow-up coverage.

## Preview Defects Resolved

- Restored printed trailing-zero precision in ten proposed vitamin values and
  four held mineral inputs; the precision receipt pins the before/after source
  preview hashes. No normalized concentration changed.
- Superseded the first YAML preview with concise append-only history,
  source-specific discovery modes, static antifoam context and exact carbon-dose
  excerpts for both ethanol relationship sources. Retained imported cross-
  references are explicitly historical database annotations, not new evidence.
- Fixed a shadowed-variable reference in the preview generator's new-ingredient
  history summary before generating the second preview. The semantic audit
  checks that the event identifies the actual added antifoam node and rejects
  altered history. Neither preview applies recipes.
- The first temporary test collection wandered outside its intended test root
  and failed on an unrelated inaccessible temporary directory. An explicit
  collection root/confcutdir scoped the run correctly; all 68 saved guard tests
  then passed. No broader filesystem permission was requested.

No GitHub issue or PR mutation is claimed by this local ledger. No paid source
access or author contact was attempted.
