# YAML Record Review: mycoplasma_medium_cip_medium_89

- Repository: CultureMech
- Record: data/merge_yaml/merged/mycoplasma_medium_cip_medium_89.yaml
- Started UTC: 2026-09-24T16:14:22Z
- Finished UTC: 2026-09-24T16:15:14Z
- Verdict: needs curation

## Target

Reviewed the generated MediaRecipe `CultureMech:000514` for
`mycoplasma_medium_cip_medium_89`, a single-source DSMZ record grounded to
`mediadive.medium:1080`.

## Validation

Focused validation passed:

- LinkML `MediaRecipe` validation: passed; no issues found.
- Strict validation: passed with zero error rows in `/private/tmp/mycoplasma_medium_cip_medium_89.strict.tsv`.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The identity is direct and unambiguous. MediaDive medium 1080 is DSMZ
`MYCOPLASMA MEDIUM (CIP MEDIUM 89)`, and the generated record is a
single-source merge from the corresponding normalized DSMZ owner.

An exact ignored-inclusive search across `data/normalized_yaml`,
`data/merge_yaml/merged`, and top-level `data/*.tsv` files found this owner,
its generated YAML, and its MediaDive indexes; it did not find another active
recipe carrying `mediadive.medium:1080`.

## Evidence

MediaDive 1080 defines a 1000 ml main solution with:

- 17 g PPLO broth
- 100 ml 25% yeast extract stock, pH 7.0, autoclaved
- 20 ml 1% phenol red stock, pH 7.0, autoclaved
- 670 ml distilled water
- 210 ml sterile supplement

The 210 ml sterile supplement contains:

- 10 ml Arginine solution 50%(w/v)
- 200 ml horse serum
- 1 g ampicillin

The 100 ml Arginine solution 50%(w/v) contains:

- 50 g L-Arginine x HCl
- distilled water to make up 100 ml

DSMZ also gives pH 7.0-7.4. Its main-solution step says to add all components
except sterile supplement, adjust pH to 7.2 + 0.2, autoclave at 121 C for 15
minutes, and aseptically add sterile supplement. The sterile supplement is
autoclaved at 121 C for 15 minutes, and the arginine stock is prepared from
50 g L-Arginine hydrochloride plus water to 100 ml.

## Completeness

The generated record preserves the base DSMZ identity, pH range, six flattened
non-water/non-solution ingredients, and all three free-text preparation
instructions. It is not complete as a layered recipe because it drops the
670 ml water row, the 210 ml sterile-supplement addition, the 10 ml arginine
stock addition, and the arginine stock water.

The flattened top-level quantities are a mixture of final-medium quantities and
local stock concentrations. `L-Arginine x HCl` is modeled as the 500 g/L stock
concentration, and `Ampicillin` is modeled as its 4.7619 g/L concentration
within the 210 ml supplement.

## Findings

1. `Distilled water`, 670 ml, is missing from the main solution.

2. The 210 ml `Sterile supplement` addition is missing and its children were
   flattened into top-level ingredients.

3. The 10 ml `Arginine solution 50%(w/v)` addition is missing and its contents
   were flattened as top-level `500 G_PER_L` L-Arginine x HCl.

4. The arginine stock's 100 ml water quantity is missing.

5. `Horse serum` was converted from a 200 ml sterile-supplement ingredient to
   `200 G_PER_L`.

6. `Ampicillin` carries its 210 ml supplement-local concentration instead of a
   final 1 L dose.

## Recommended Edits

Repair the normalized DSMZ owner before regenerating the merged record:

- Preserve the 1000 ml main solution with 670 ml distilled water and 210 ml
  sterile supplement.
- Preserve the sterile supplement as a 210 ml stock with 10 ml Arginine
  solution 50%(w/v), 200 ml horse serum, and 1 g ampicillin.
- Preserve the arginine stock as 50 g L-Arginine x HCl plus water to 100 ml.
- Keep the yeast extract, phenol red, ampicillin, and arginine quantities in
  their source stock context rather than flattening stock-local concentrations
  into the final medium.

## Follow-up Checks

- Regenerate the merged YAML and confirm DSMZ 1080 retains the main solution,
  sterile supplement, and arginine solution as distinct layers.
- Re-run LinkML, strict, reference, and term validation on the regenerated
  record.
- Compare the regenerated ingredient tree against MediaDive medium 1080 to
  ensure no water or solution rows are dropped.

## Additional Notes

None found.
