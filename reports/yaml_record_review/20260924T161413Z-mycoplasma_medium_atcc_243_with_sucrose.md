# YAML Record Review: mycoplasma_medium_atcc_243_with_sucrose

- Repository: CultureMech
- Record: data/merge_yaml/merged/mycoplasma_medium_atcc_243_with_sucrose.yaml
- Started UTC: 2026-09-24T16:13:20Z
- Finished UTC: 2026-09-24T16:14:13Z
- Verdict: needs curation

## Target

Reviewed the generated MediaRecipe `CultureMech:008815` for
`mycoplasma_medium_atcc_243_with_sucrose`, a TOGO import grounded to
`TOGO:M2227`.

## Validation

Focused validation passed:

- LinkML `MediaRecipe` validation: passed; no issues found.
- Strict validation: passed with zero error rows in `/private/tmp/mycoplasma_medium_atcc_243_with_sucrose.strict.tsv`.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The TOGO grounding is correct. `TOGO:M2227` is `Mycoplasma medium (ATCC 243)
with sucrose` and cites the ATCC Medium 1161 source.

The generated record is stale relative to
`data/normalized_yaml/bacterial/mycoplasma_medium_atcc_243_with_sucrose.yaml`,
which was repaired on 2026-09-12. The repaired owner now models the ATCC
sucrose and yeast-extract additions as explicit stock solutions instead of the
empty generated `Unknown solution` stub.

The generated record also retains `kg_microbe_match: mediadive.medium:263`.
MediaDive 263 is DSMZ `TIBI MEDIUM`, a sucrose, fig, lemon, and tap-water
recipe unrelated to ATCC Mycoplasma medium.

## Evidence

The TOGO `M2227` API reports pH 7.4 +/- 0.2 and six component rows:

- 150 ml `Yeast extract solution (15%)`
- 650 ml `Distilled deionized water`
- 40 g sucrose
- 200 ml horse serum
- 10 g Agar, Noble (BD 214230)
- 17.5 g Heart Infusion Broth (BD 238400)

TOGO also preserves the ATCC preparation comments: combine heart infusion and
450 ml water, autoclave at 121 C for 15 minutes, dissolve sucrose in 200 ml
water and filter-sterilize it, aseptically add horse serum, yeast extract, and
sterile sucrose to the cooled heart-infusion solution, heat-inactivate horse
serum at 56 C for 30 minutes, and cool/warm components to 50-55 C before
combining for solid medium.

## Completeness

The generated recipe preserves the target identity and the five named
top-level TOGO rows, but it does not preserve the preparation structure. The
single 650 g/L water row should be split into basal water and sucrose-solution
water, horse serum is a 200 ml/L addition, and 150 ml of 15% yeast extract
solution should be represented as a real stock solution instead of an empty
stub at `150 G_PER_L`.

The generated recipe also omits pH 7.4 +/- 0.2 and the ATCC preparation
operations that distinguish autoclaved basal agar, filter-sterilized sucrose,
heat-inactivated horse serum, and aseptic addition after cooling.

## Findings

1. The generated record is stale relative to the 2026-09-12 repaired owner and
   still contains the pre-repair empty `Yeast extract solution (15%)` stub.

2. `Distilled deionized water` is modeled as `650 G_PER_L`; the repaired owner
   splits the water into 450 ml/L basal water plus 200 ml/L water inside the
   sucrose stock solution.

3. `Horse serum` is modeled as `200 G_PER_L` instead of a 200 ml/L liquid
   addition.

4. `Sucrose` is modeled as a direct 40 g/L ingredient instead of a 40 g
   filtered stock in 200 ml distilled deionized water.

5. The source pH range and preparation operations are missing from the
   generated record.

6. `kg_microbe_match: mediadive.medium:263` points to DSMZ `TIBI MEDIUM`, an
   unrelated recipe.

## Recommended Edits

Finish propagating the normalized repair:

- Remove the stale `kg_microbe_match: mediadive.medium:263` from the normalized
  TOGO owner.
- Regenerate `data/merge_yaml/merged` from the repaired owner.
- Confirm the regenerated record has 450 ml/L basal water, a 200 ml/L sucrose
  stock containing 40 g sucrose, a 150 ml/L 15% Yeast Extract Solution with
  yeast extract composition, and 200 ml/L horse serum.
- Confirm the regenerated record preserves pH 7.2-7.6 and the autoclave,
  filter-sterilization, heat-inactivation, and aseptic-addition steps.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation on the regenerated
  record.
- Run an exact ignored-inclusive search for `mediadive.medium:263` to confirm
  this unrelated Tibi Medium link no longer appears on
  `mycoplasma_medium_atcc_243_with_sucrose`.

## Additional Notes

None found.
