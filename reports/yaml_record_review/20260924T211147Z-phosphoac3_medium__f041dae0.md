# YAML Record Review: phosphoac3_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/phosphoac3_medium__f041dae0.yaml
- Started UTC: 2026-09-24T21:11:47Z
- Finished UTC: 2026-09-24T21:11:47Z
- Verdict: needs curation

## Target

- MediaRecipe ID: CultureMech:003222
- Name: phosphoac3_medium
- Source import: phosphoac3_medium, ird_mesotoga_medium
- Primary external ID: mediadive.medium:J875
- Source URL: `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=875`

This generated record represents direct JCM Medium 875, PHOSPHOAC3 MEDIUM, merged with JCM Medium 926, IRD MESOTOGA MEDIUM.

## Validation

- Open LinkML validation: passed with no reported issues.
- Strict validation: passed for 1 file with 0 error rows; `/private/tmp/phosphoac3_medium__f041dae0.strict.tsv` is header-only.
- Reference validation: passed for 1 file with 0 reference checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

The `phosphoac3_medium` identity is correct for JCM 875, but the merged `ird_mesotoga_medium` identity is not a plain duplicate. The live JCM 926 page defines IRD Mesotoga Medium as Medium 875 with the 20 ml/L 1 M L-sodium lactate solution replaced by 20 ml/L 1 M fructose solution. The current merged record keeps the JCM 875 lactate row and only stores `ird_mesotoga_medium` as a synonym, so the JCM 926 child-specific replacement is lost.

Exact ignored-file searches across `data/merge_yaml/merged` and `data/normalized_yaml` also found a TOGO M914 / TOGO M972 sibling at `data/merge_yaml/merged/PHOSPHOAC3_MEDIUM.yaml`. That sibling has the same parent/child merge problem and should be normalized together with the direct JCM branches.

Several stock-level rows are grounded as if they were top-level final ingredients. Most visibly, Trace minerals from JCM Medium 151 and the NaHCO3, lactate, and Na2S stock additions were copied into the final ingredient table with `G_PER_L` units.

## Evidence

- The live JCM 875 page lists a base one-liter PHOSPHOAC3 recipe with 10 ml Trace minerals from Medium 151 and three post-autoclave additions per liter: 25 ml 8% NaHCO3 solution, 20 ml 1 M L-sodium lactate solution, and 8 ml 5% Na2S x 9H2O solution.
- JCM 875 instructs anaerobic autoclaving under N2-CO2 and sulfur steaming/distribution, so those gases are preparation atmosphere, not ingredients.
- The live JCM 926 page says to use Medium 875 while replacing the L-sodium lactate solution with 20 ml/L 1 M fructose solution.
- The TOGO M914 / M972 sibling confirms that TOGO imported the same JCM parent and derivative as separate source records.

## Completeness

The generated record is not complete as either JCM 875 or JCM 926:

- 8% NaHCO3, 1 M L-sodium lactate, and 5% Na2S x 9H2O are source solution additions but are stored as 25, 20, and 8 G_PER_L.
- Trace minerals from Medium 151 are expanded into final top-level ingredients; their stock values are not converted through the 10 ml addition.
- Base Medium 875 masses were rescaled to fractional values, for example 0.3 g KH2PO4 to 0.28222 G_PER_L, while source-facing curation should keep the one-liter base recipe and separate solution additions.
- NaCl and CaCl2 were summed across base and trace-mineral contexts.
- The JCM 926 fructose replacement is absent, so the IRD Mesotoga variant is chemically indistinguishable from the lactate-containing parent.

## Findings

1. JCM 875 and the derivative JCM 926 were merged as duplicates even though JCM 926 replaces lactate with fructose.
2. Three post-autoclave solution additions are dimensionally wrong because milliliter aliquots are represented as grams per liter.
3. Trace minerals from JCM Medium 151 were flattened into the main recipe and then partially summed with base-medium salts.
4. The copied stock rows make the record look like a high-metal final medium even though those values are stock concentrations.
5. The TOGO M914 / M972 imports are still a separate uppercase generated record for the same parent and child source family.

## Recommended Edits

- Keep JCM 875 PHOSPHOAC3 Medium as the parent recipe.
- Model JCM 926 IRD Mesotoga Medium as a variant of JCM 875 that replaces the 1 M L-sodium lactate addition with a 1 M fructose addition.
- Preserve Trace minerals from Medium 151 as a 10 ml referenced stock instead of copying its components into the final medium.
- Preserve the 8% NaHCO3, 1 M lactate, 5% Na2S, and JCM 926 1 M fructose additions as volume-aware stocks.
- Keep N2-CO2 gassing as preparation metadata rather than chemical ingredients.
- Normalize the direct MediaDive and TOGO branches together so parent and child variants merge only with their true counterparts.

## Follow-up Checks

- Regenerate merged YAML and verify that JCM 875 and JCM 926 are distinct parent/variant records, not one duplicate.
- Re-run open schema, strict, term, and reference validation after regeneration.
- Run exact ignored-file searches for `GRMD=875`, `GRMD=926`, `mediadive.medium:J875`, `mediadive.medium:J926`, `TOGO:M914`, and `TOGO:M972` with ignored files included to confirm no stale split remains.
- Spot-check the rendered pages to ensure JCM 926 visibly contains fructose in place of lactate.

## Additional Notes

None found.
