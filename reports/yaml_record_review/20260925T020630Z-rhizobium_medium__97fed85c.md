# YAML Record Review: rhizobium_medium__97fed85c

- Repository: CultureMech
- Record: `data/merge_yaml/merged/rhizobium_medium__97fed85c.yaml`
- Started UTC: 2026-09-25T02:04:08Z
- Finished UTC: 2026-09-25T02:06:30Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:008938` for TOGO Medium M2353 / `TOGO:M2353`, generated from `data/normalized_yaml/bacterial/TOGO_M2353_Rhizobium_Medium.yaml`.

## Validation

- Open schema validation: passed with `No issues found`.
- Strict validation: passed; `scripts/validate_strict.py` reported 0 errors and wrote only the TSV header.
- Reference validation: passed; 0 checks.
- Term validation: passed with the known `eutils` / `pkg_resources` deprecation warning.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

TOGO M2353 imports DSMZ Medium 98 / Rhizobium Medium. Exact ignored-inclusive searches for `TOGO:M2353`, `DSMZ_Medium98.pdf`, and the M2353 API URL within the owner, generated target, and manifest found the expected M2353 owner and generated target; the DSMZ PDF search also found the direct DSMZ owner for `mediadive.medium:98`.

## Evidence

DSMZ Medium 98 and MediaDive 98 model the final medium as 1 g/L yeast extract, 10 g/L mannitol, 15 g/L agar, 200 ml/L soil extract, 800 ml/L distilled water, and pH 7.0. Soil extract is a 200 ml stock made from 80 g air-dried garden soil, 0.2 g Na2CO3, and 200 ml distilled water; that stock is autoclaved for 1 hour at 121 C, settled, centrifuged, and adjusted to pH 7.2 before 200 ml is used in the final medium.

## Completeness

The generated target keeps the source ingredient names but flattens the soil-extract stock into the final recipe and loses the distinction between main-medium water and stock water.

## Findings

- The generated target merges the main-medium 800 ml water and the soil-extract stock's 200 ml water into one `Distilled water` row of `1000 G_PER_L`. These are two different solution contexts and both source amounts are volumes, not grams.
- `Soil extract` is represented as `200 G_PER_L`, but the final DSMZ/MediaDive recipe uses 200 ml of that stock per liter.
- `Na2CO3` and `Air-dried garden soil` are emitted as top-level final-medium ingredients even though they belong inside the soil-extract stock. They should be nested under a `Soil extract` solution or omitted from the final flat ingredient list in favor of the 200 ml/L soil-extract stock.
- The generated target lacks the final pH 7.0, the soil-extract pH 7.2, and the DSMZ preparation instructions for autoclaving, settling, and centrifuging the soil extract.
- TOGO M2353 remains separate from the direct DSMZ Medium 98 owner even though both cite `DSMZ_Medium98.pdf`.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/TOGO_M2353_Rhizobium_Medium.yaml` to model soil extract as a subsolution with its own air-dried soil, Na2CO3, and water recipe.
- Represent the final recipe water as 800 ml/L and the soil-extract stock as 200 ml/L; do not sum water across stock and final recipe.
- Add pH/preparation evidence and a curation-history entry, source-link or source-merge the owner with the direct DSMZ 98 record, then regenerate `data/merge_yaml/merged`.

## Follow-up Checks

- Confirm the regenerated final Rhizobium Medium has yeast extract 1 g/L, mannitol 10 g/L, agar 15 g/L, soil extract 200 ml/L, and distilled water 800 ml/L.
- Confirm air-dried garden soil and Na2CO3 only appear in the soil-extract subsolution.
- Re-run open schema, strict, reference, and term validation for the regenerated target.

## Additional Notes

The direct DSMZ owner for the same source also flattens the soil-extract stock, but with stock concentrations of 400 g/L soil and 1 g/L Na2CO3. Both source families need the same stock/subsolution repair.
