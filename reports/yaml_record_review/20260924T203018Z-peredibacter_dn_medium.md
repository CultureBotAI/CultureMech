# YAML Record Review: peredibacter_dn_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/peredibacter_dn_medium.yaml
- Started UTC: 2026-09-24T20:30:18Z
- Finished UTC: 2026-09-24T20:30:18Z
- Verdict: pass with minor issues

## Target

Generated bacterial MediaRecipe `CultureMech:000432`, `peredibacter_dn_medium`, from the maintained direct DSMZ/MediaDive owner `data/normalized_yaml/bacterial/peredibacter_dn_medium.yaml`.

The record represents DSMZ / MediaDive medium 1012, PEREDIBACTER (DN) MEDIUM. It has 0.8 g/L Nutrient broth, 0.5 g/L Casamino acids, 0.1 g/L Yeast extract, 0.3 g/L CaCl2 x 2 H2O, 0.6 g/L MgCl2 x 6 H2O, pH 7.2, and prey-cell preparation instructions.

## Validation

- Open LinkML validation: Passed with no issues.
- Strict validator: Passed; `/private/tmp/peredibacter_dn_medium.strict.tsv` was header-only, so there were 0 strict errors.
- Reference validation: Passed; 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not embedded `MediaRecipe.curation_history`.

## Identity and Grounding

The DSMZ/MediaDive identity is internally consistent: `mediadive.medium:1012` names PEREDIBACTER (DN) MEDIUM and links to the same DSMZ medium 1012 PDF named by the maintained owner.

An exact ignored-inclusive search found a separate `dn_broth` record whose notes mention `DSMZ Medium: 1012 (mediadive.medium:1012)`, but that record's HEPES/MgCl2/CaCl2/NaOH composition does not match DSMZ medium 1012. It should not be merged with this Peredibacter record as-is.

## Evidence

MediaDive medium 1012 and the linked DSMZ medium 1012 PDF support the five non-water ingredients, pH 7.2, a 1000 ml distilled water row, and both preparation steps in the generated record.

The instructions to dissolve ingredients except calcium and magnesium chloride, adjust pH with NaOH, add calcium and magnesium after autoclaving from sterile stocks, and prepare the prey-cell suspension are captured in the generated `preparation_steps`.

The calcium chloride dihydrate and magnesium chloride hexahydrate CHEBI groundings are chemically specific and appropriate. Casamino acids, Yeast extract, and Nutrient broth are complex ingredients; the maintained owner now grounds the first two to local FoodOn terms, but the August generated merge predates that repair.

## Completeness

The generated record preserves source identity, pH, non-water ingredients, and preparation text. It omits only the 1000 ml distilled water row from DSMZ / MediaDive medium 1012.

The generated record is also stale relative to the maintained owner's September repair that grounded Casamino acids and Yeast extract to local FoodOn terms.

## Findings

1. Minor issue: the maintained owner and generated record omit the 1000 ml `Distilled water` row from DSMZ / MediaDive medium 1012.
2. Minor issue: the generated record is stale relative to the September maintained-owner repair that added local FoodOn term links for Casamino acids and Yeast extract.

## Recommended Edits

1. Add the 1000 ml distilled water row to `data/normalized_yaml/bacterial/peredibacter_dn_medium.yaml`.
2. Regenerate merged YAML so the maintained owner's Casamino acids and Yeast extract term links are reflected in `data/merge_yaml/merged/peredibacter_dn_medium.yaml`.

## Follow-up Checks

1. Re-run open, strict, reference, and term validation on the repaired maintained owner and regenerated merged record.
2. Repeat an exact ignored-inclusive search for `mediadive.medium:1012`, `DSMZ_Medium1012`, `CultureMech:000432`, and `dn_broth` to ensure the unrelated DN BROTH record remains separate.

## Additional Notes

The exact ignored-inclusive duplicate search covered `data`, `src`, and `scripts` for `mediadive.medium:1012`, `DSMZ_Medium1012`, `CultureMech:000432`, and `peredibacter_dn_medium`.
