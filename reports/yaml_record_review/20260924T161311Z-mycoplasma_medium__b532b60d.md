# YAML Record Review: mycoplasma_medium__b532b60d

- Repository: CultureMech
- Record: data/merge_yaml/merged/mycoplasma_medium__b532b60d.yaml
- Started UTC: 2026-09-24T16:12:00Z
- Finished UTC: 2026-09-24T16:13:11Z
- Verdict: needs curation

## Target

Reviewed the generated MediaRecipe `CultureMech:003105` for
`mycoplasma_medium`, a JCM `MYCOPLASMA MEDIUM` record grounded to
`mediadive.medium:J761`.

## Validation

Focused validation passed:

- LinkML `MediaRecipe` validation: passed; no issues found.
- Strict validation: passed with zero error rows in `/private/tmp/mycoplasma_medium__b532b60d.strict.tsv`.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The direct JCM identity is sound, but the generated file is stale relative to
the maintained normalized owner. `data/normalized_yaml/bacterial/mycoplasma_medium.yaml`
was repaired on 2026-09-11 and now links the equivalent TOGO M787 import,
`CultureMech:010196`, as a `SOURCE_DUPLICATE`.

The generated JCM file still reflects the older flattened owner state and has
no source-duplicate link to the TOGO child. The generated TOGO file,
`data/merge_yaml/merged/MYCOPLASMA_MEDIUM.yaml`, is also stale and still shows
the old empty `25% Yeast Extract Solution` stub.

The target record also retains `kg_microbe_match: mediadive.medium:12`. That is
DSMZ `SOIL EXTRACT MEDIUM`, not JCM `MYCOPLASMA MEDIUM`, so this cross-link is
unrelated to the record under review.

## Evidence

The repaired normalized JCM owner says MediaDive J761 and TOGO M787 describe
the same 1 L solid agar recipe:

- 700 ml distilled water
- 17.5 g Heart Infusion Broth
- 10 g Bacto agar
- 200 ml heat-inactivated horse serum
- 100 ml 25% Yeast Extract Solution

The live TOGO `M787` API agrees on JCM `M761`, pH 7.2-7.6, 700 ml water,
17.5 g Heart infusion broth, 10 g Bacto agar, 100 ml 25% Yeast Extract
Solution, and 200 ml heat-inactivated horse serum. TOGO also carries two
preparation comments: autoclave the basal medium at 121 C for 15 min before
adding the filter-sterilized solutions, then warm the serum and yeast extract
solution to 55 C and adjust the final pH to 7.4+-0.2.

The live JCM `GRMD=761` URL currently returns `Nothing found`, so the repaired
local owner and live TOGO mirror are the available source checks for the old
JCM page.

## Completeness

The generated record is missing the 700 ml distilled water ingredient and
converts two liquid additions, horse serum and 25% Yeast Extract Solution, into
top-level mass concentrations. It also lacks the normalized owner's structured
`25% Yeast Extract Solution` composition and the duplicate relationship to
TOGO M787.

The generated pH is stale as well. It has `ph_value: 7.4`, while both the
repaired owner and TOGO source represent this as the range 7.2-7.6.

## Findings

1. The generated JCM record is stale relative to the repaired normalized owner
   and omits the 2026-09-11 restoration of distilled water, liquid additions,
   the structured 25% Yeast Extract Solution, pH range, sterilization details,
   and TOGO M787 source-duplicate link.

2. `Horse serum` is still modeled as `200 G_PER_L` even though the source and
   repaired owner represent 200 ml/L heat-inactivated horse serum.

3. `Yeast extract` is still modeled as `100 G_PER_L` even though the source and
   repaired owner represent 100 ml/L of a 25% Yeast Extract Solution.

4. `kg_microbe_match: mediadive.medium:12` points to DSMZ `SOIL EXTRACT
   MEDIUM`, an unrelated recipe.

5. The equivalent TOGO M787 owner is active and repaired, but generated
   `MYCOPLASMA_MEDIUM.yaml` remains a separate stale record.

## Recommended Edits

Finish propagating the normalized repair:

- Remove the stale `kg_microbe_match: mediadive.medium:12` from
  `data/normalized_yaml/bacterial/mycoplasma_medium.yaml`.
- Regenerate `data/merge_yaml/merged` from the repaired JCM and TOGO owners.
- Confirm the regenerated generated record includes 700 ml water, 200 ml horse
  serum, 100 ml of the nested 25% Yeast Extract Solution, pH range 7.2-7.6, and
  the JCM/TOGO source-duplicate relationship.
- Confirm `MYCOPLASMA_MEDIUM.yaml` is eliminated or merged after regeneration,
  rather than remaining as an independent stale TOGO projection.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation on the regenerated JCM
  and TOGO records.
- Run an exact ignored-inclusive search for `mediadive.medium:12` to confirm
  this unrelated Soil Extract Medium link no longer appears on either
  Mycoplasma Medium owner.

## Additional Notes

None found.
