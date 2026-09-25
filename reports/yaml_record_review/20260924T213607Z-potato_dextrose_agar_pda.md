# YAML Record Review: potato_dextrose_agar_pda

- Repository: CultureMech
- Record: data/merge_yaml/merged/potato_dextrose_agar_pda.yaml
- Started UTC: 2026-09-24T21:36:07Z
- Finished UTC: 2026-09-24T21:36:07Z
- Verdict: needs curation

## Target

- MediaRecipe ID: CultureMech:008210
- Name: potato_dextrose_agar_pda
- Source import: TOGO Medium M1653 / NBRC_M856
- Primary external ID: TOGO:M1653
- Maintained input: data/normalized_yaml/bacterial/potato_dextrose_agar_pda.yaml

This generated record represents Potato Dextrose Agar from NBRC 856, with TOGO M1870 and TOGO M1954 merged in as source duplicates.

## Validation

- Open LinkML validation: passed with no reported issues.
- Strict validation: passed for 1 file with 0 error rows; `/private/tmp/potato_dextrose_agar_pda.strict.tsv` is header-only.
- Reference validation: passed for 1 file with 0 reference checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

TOGO M1653 and NBRC 856 agree on the ordinary Potato Dextrose Agar identity: 200 g potato, 10 g glucose, 15 g agar, 1 L distilled water, adjustment to pH 5.4 - 5.6, autoclaving, and the commercial-PDA availability note.

The merged TOGO M1870 / NBRC 1115 source is not a pure source duplicate because it is the pH 3.0 variant: it has the same bulk potato/glucose/agar/water signature, but its preparation explicitly adjusts to pH 3.0.

The merged TOGO M1954 / NBRC 1232 source is not a pure source duplicate because it is PDA +Hygromycin medium: it adds 0.8 ml of Sodium hygromycin solution (50 mg/ml), instructs separate filtration for that antibiotic solution, and adds it after the agar medium has cooled to about 60C.

Exact ignored-file searches across `data/normalized_yaml` and `data/merge_yaml` for `TOGO:M1653`, `TOGO:M1870`, `TOGO:M1954`, `NBRC_M856`, `NBRC_M1115`, `NBRC_M1232`, `NO=856`, `NO=1115`, `NO=1232`, `pda_hygromycin_medium`, `pda_ph_3_0`, and `potato_dextrose_agar_pda` found one maintained normalized YAML for each TOGO/NBRC source and this merged record.

## Evidence

- TOGO M1653 / NBRC 856 list Potato Dextrose Agar with 200 g potato, 10 g glucose, 15 g agar, 1 L distilled water, and pH 5.4 - 5.6.
- TOGO M1870 / NBRC 1115 list the same core PDA composition, but the preparation directs adjustment to pH 3.0.
- TOGO M1954 / NBRC 1232 list the same core PDA composition plus 0.8 ml Sodium hygromycin solution (50 mg/ml), a separate filtration instruction, pH 5.4 - 5.6, and post-autoclave addition of the antibiotic solution.

## Completeness

The generated record is structurally valid but incomplete against all three NBRC sources. It converts the shared 1 L distilled water row to 1 G_PER_L, omits the M1653 pH 5.4 - 5.6 preparation and commercial-PDA note, flattens the M1870 pH 3.0 variant into a source duplicate, and drops the M1954 sodium hygromycin addition from the merged output.

## Findings

1. Major: The TOGO M1954 / NBRC 1232 recipe loses its 0.8 ml Sodium hygromycin solution (50 mg/ml) addition during normalization and merging; `data/normalized_yaml/bacterial/pda_hygromycin_medium.yaml` stores it as an empty `solutions` entry with concentration `0.8 G_PER_L`, and the generated merged record drops it entirely.
2. Major: The TOGO M1870 / NBRC 1115 pH 3.0 recipe is merged as a `SOURCE_DUPLICATE` of ordinary PDA, so the generated record hides a distinct low-pH variant and has no retained pH 3.0 preparation text.
3. Major: All three maintained normalized inputs import the source 1 L distilled-water row as `1 G_PER_L`; the generated merge preserves that unit error instead of representing 1 L of water per liter of prepared medium.
4. Minor: The ordinary TOGO M1653 / NBRC 856 source pH range, preparation steps, and commercial-PDA note are absent from the maintained normalized input and therefore absent from the generated record.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/pda_hygromycin_medium.yaml` so sodium hygromycin is represented as a real post-autoclave addition from a 50 mg/ml stock, with separate filtration and addition after cooling to about 60C.
- Repair `data/normalized_yaml/bacterial/pda_ph_3_0.yaml` so its pH 3.0 adjustment is represented and so it is no longer merged as a mere source duplicate of M1653 PDA.
- Repair `data/normalized_yaml/bacterial/potato_dextrose_agar_pda.yaml` and the related TOGO inputs so the 1 L distilled-water row is no longer emitted as `1 G_PER_L`.
- Regenerate `data/merge_yaml/merged/potato_dextrose_agar_pda.yaml` after normalized curation so M1653, M1870, and M1954 remain distinct where their pH and hygromycin differences are source-significant.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation on all repaired normalized inputs and regenerated merged outputs.
- Run exact ignored-file searches for `TOGO:M1653`, `TOGO:M1870`, `TOGO:M1954`, `NBRC_M856`, `NBRC_M1115`, and `NBRC_M1232` before adding or deleting any PDA records.
- Spot-check the regenerated records to ensure that ordinary PDA keeps pH 5.4 - 5.6, the pH 3.0 PDA variant keeps pH 3.0, and PDA +Hygromycin retains its antibiotic addition.

## Additional Notes

None found.
