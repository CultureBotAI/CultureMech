# YAML Record Review: HP 101 Halophile Medium
- Repository: CultureMech
- Record: data/merge_yaml/merged/hp_101_halophile_medium__94be48da.yaml
- Started UTC: 2026-09-23T12:39:24Z
- Finished UTC: 2026-09-23T12:40:29Z
- Verdict: needs curation

## Target

Reviewed the generated TOGO/JCM branch for TOGO Medium M465 and JCM Medium 464, `HP 101 Halophile Medium`, at `data/merge_yaml/merged/hp_101_halophile_medium__94be48da.yaml`. The maintained source is `data/normalized_yaml/bacterial/TOGO_M465_HP_101_Halophile_Medium.yaml`.

## Validation

- Open LinkML validation: passed for `MediaRecipe`.
- Strict validation: passed with zero error rows in `/private/tmp/hp_101_halophile_medium__94be48da.strict.tsv`.
- Reference validation: passed with zero checks.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone YAML files under `history/`, not embedded `MediaRecipe.curation_history` entries in generated merge artifacts.

## Identity and Grounding

The record ID, `TOGO:M465` source accession, and source URL all identify the TOGO mirror of JCM Medium 464, `HP 101 HALOPHILE MEDIUM`. The hash-suffixed generated filename appears because DSMZ and KOMODO HP 101 branches exist under the same normalized name, but this record's source identity is still one JCM/TOGO branch and is not conflated with those branches.

## Evidence

TOGO M465 reports original medium `JCM_M464`, links JCM `GRMD=464`, gives pH 7.2, and lists 1 L distilled water, 4.3 g MgSO4 hydrate, 1 g yeast extract, 100 g NaCl, 2 g NaNO3, 20 g agar, and 10 g peptone. The inspected JCM 464 page confirms the same formulation, the same pH adjustment to 7.2, and the JCM default sterilization condition of autoclaving at 121 C for 15 min unless otherwise stated.

The generated record carries the six non-water solute amounts faithfully and marks the medium as agar-solid. It imports the explicit 1 L distilled-water row as `1 G_PER_L`, and it loses both the pH 7.2 value and the pH-adjustment preparation instruction.

## Completeness

The NaCl, sodium nitrate, magnesium sulfate heptahydrate, yeast extract, agar, and peptone rows match the inspected upstream recipe. The consequential gaps are all procedural or unit-context gaps: source water volume, pH, pH adjustment, and the JCM default autoclave instruction.

No `target_organisms`, growth metrics, or strain-specific growth evidence are asserted, so there are no over-scoped organism claims to review.

## Findings

- **major**: The explicit 1 L distilled-water row from TOGO and JCM is represented as `1 G_PER_L` instead of 1000 ml of water.
- **major**: The source pH 7.2 is absent from the generated record.
- **major**: The JCM `Adjust pH to 7.2` preparation instruction is absent.
- **major**: The JCM default 121 C for 15 min autoclave instruction is absent.
- **minor**: The magnesium sulfate heptahydrate row is chemically grounded correctly, but the generated display string still uses the old middle-dot hydrate spelling that other repaired JCM/TOGO records have moved away from.

## Recommended Edits

- In `data/normalized_yaml/bacterial/TOGO_M465_HP_101_Halophile_Medium.yaml`, change the distilled-water concentration from `1 G_PER_L` to an explicit 1 L or 1000 ml water volume in the unit vocabulary used by repaired TOGO records.
- Add structured `ph_value: 7.2` and an `ADJUST_PH` preparation step backed by TOGO M465 and JCM 464.
- Add the default JCM autoclave instruction to `sterilization` and `preparation_steps`.
- Replace the magnesium sulfate display string with an ASCII `MgSO4 x 7 H2O` spelling while keeping the existing CHEBI:31795 heptahydrate grounding.
- Regenerate `data/merge_yaml/merged/hp_101_halophile_medium__94be48da.yaml` after the maintained source is corrected.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation after regeneration.
- Re-open TOGO M465 and JCM Medium 464 to confirm the regenerated record keeps the six supported solutes, 1 L water, pH 7.2, and the JCM default autoclave step.
- Run the repository's merge freshness audit to prove the generated TOGO branch no longer lags its normalized source.

## Additional Notes

The DSMZ 625 and KOMODO 625 HP 101 records use the same six solute masses and pH 7.2, but the reviewed file is the separate TOGO/JCM branch and should be corrected in its own normalized source first.
