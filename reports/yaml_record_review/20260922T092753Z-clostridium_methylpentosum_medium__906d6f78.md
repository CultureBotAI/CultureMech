# YAML Record Review: CLOSTRIDIUM METHYLPENTOSUM MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/clostridium_methylpentosum_medium__906d6f78.yaml`
- Started UTC: `2026-09-22T09:27:53Z`
- Finished UTC: `2026-09-22T09:28:04Z`
- Verdict: needs curation

## Target

Generated bacterial `MediaRecipe` record `CultureMech:001620` for MediaDive medium `492`, DSMZ Medium 492 `CLOSTRIDIUM METHYLPENTOSUM MEDIUM`. The generated record was produced from `data/normalized_yaml/bacterial/clostridium_methylpentosum_medium.yaml` on merge fingerprint `906d6f78ec219d4181be7949d6c415aa533bedabc7d8328d050b9e9e54c22e9b`.

## Validation

- LinkML open schema validation: passed.
- Strict validation: passed with no errors in `/private/tmp/clostridium_methylpentosum_medium__906d6f78.strict.tsv`.
- LinkML reference validation: passed; the validator reported 0 total checks.
- LinkML term validation: passed.
- Embedded `curation_history` entries: not checked by the standalone history validator.

## Identity and Grounding

The main MediaDive identity is correct for DSMZ Medium 492, and the pH range 6.8-7.0 is preserved.

The same DSMZ 492 medium is emitted separately from the KOMODO import as `data/merge_yaml/merged/CLOSTRIDIUM_METHYLPENTOSUM_MEDIUM.yaml`. The KOMODO branch carries a variable-concentration KOH ingredient and `Aerobic: Yes` in notes; those are import artifacts for a pH adjuster and an anoxic DSMZ medium, not a distinct formula that should prevent reconciliation.

Ingredient grounding is mostly usable. `CuSO4 x H2O` is grounded to generic copper(II) sulfate rather than a monohydrate-specific term, if one is available, and `Calcium D-(+)-pantothenate` has no CHEBI-keyed MediaIngredientMech link.

## Evidence

The DSMZ Medium 492 PDF defines the completed medium as 954 ml Solution A, 20 ml Solution B, 10 ml Solution C, 1 ml Solution D, and 20 ml Solution E. Solution A contains the salts, trace metal aliquots, sodium resazurin, and 940 ml distilled water; Solution B is 1 g NaHCO3 in 20 ml water; Solution C is 2 g L-rhamnose in 10 ml water; Solution D is 1 ml Wolin's vitamin solution (10x); Solution E is 1 g L-Cysteine HCl x H2O in 20 ml water.

The DSMZ PDF supports the anoxic handling copied into `preparation_steps`: Solution A under 100% N2, Solution B under 80% N2 / 20% CO2, Solutions C and D filter-sterilized under 100% N2, Solution E autoclaved under 100% N2, and final pH 6.8-7.0.

The ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml/merged`, `data/import_tracking`, and `reports` found this exact MediaDive branch and the separate KOMODO `CLOSTRIDIUM_METHYLPENTOSUM_MEDIUM.yaml` branch for DSMZ Medium 492.

## Completeness

The record preserves the pH and preparation prose but not the source solution structure:

- Solution A through Solution E are absent as explicit solutions.
- Wolin's vitamin solution (10x) is absent as a stock solution.
- Solution A metal solution aliquots are flattened into Solution A concentrations.
- The KOH adjustment belongs in the Solution A preparation, not as a final ingredient.

## Findings

- Solution B, Solution C, and Solution E are stored at stock strength as final ingredients: `NaHCO3` `50 G_PER_L`, `L-Rhamnose` `200 G_PER_L`, and `L-Cysteine HCl x H2O` `50 G_PER_L`. These values come directly from 1 g/20 ml, 2 g/10 ml, and 1 g/20 ml stocks, not from completed final-medium concentrations.
- Solution A salts are represented as Solution A concentrations rather than completed-medium concentrations. For example, 0.90 g NH4Cl, KH2PO4, and NaCl in 954 ml Solution A become `0.943396 G_PER_L`.
- The CoCl2, FeSO4, ZnSO4, CuSO4, and resazurin rows are derived from milliliter additions to Solution A and lose the fact that their source chemicals were supplied as 0.1% w/v stocks.
- Wolin vitamin stock internals are flattened into the final ingredient list at one-liter stock concentrations, including `Biotin` `0.02 G_PER_L`, `Pyridoxine hydrochloride` `0.1 G_PER_L`, and `Vitamin B12` `0.001 G_PER_L`.
- The KOMODO duplicate branch remains separate even though it was copied from the same DSMZ Medium 492 source and differs mainly by an imported variable KOH pH-buffer row.

## Recommended Edits

- Fix `data/normalized_yaml/bacterial/clostridium_methylpentosum_medium.yaml`, `data/normalized_yaml/bacterial/KOMODO_492_CLOSTRIDIUM_METHYLPENTOSUM_MEDIUM.yaml`, or the DSMZ MediaDive/KOMODO solution import logic, then regenerate; generated `data/merge_yaml/merged/*.yaml` outputs are derived.
- Represent Solution A through Solution E explicitly with their aliquot volumes.
- Represent Wolin's vitamin solution as the source 10x stock dosed at 1 ml through Solution D.
- Preserve the 0.1% CoCl2, FeSO4, ZnSO4, CuSO4, and resazurin additions as aliquots to Solution A or correctly diluted final concentrations.
- Treat KOH as a Solution A pH adjuster instead of a final variable-concentration ingredient.
- Reconcile the MediaDive and KOMODO generated branches after their solution representation matches.

## Follow-up Checks

- Validate the regenerated record with open schema, strict, reference, and term validators.
- Confirm no Solution B, C, or E stock-strength row remains as a top-level final ingredient.
- Confirm the 1 ml Wolin vitamin aliquot is not expanded as undiluted stock ingredients in the final formula.
- Confirm the KOMODO branch merges with, or is intentionally linked to, the MediaDive DSMZ 492 branch.
- Confirm the defined final formula remains fully grounded after `CuSO4 x H2O` and calcium pantothenate are revisited.

## Additional Notes

Empty optional fields are not defects. The key defect is concentration context: the source is a five-solution assembly, but the generated record currently reads like a single final medium with several 20 ml or 10 ml stocks at full strength.
