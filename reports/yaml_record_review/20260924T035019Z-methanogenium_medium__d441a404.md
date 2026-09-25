# YAML Record Review: methanogenium_medium__d441a404
- Repository: CultureMech
- Record: data/merge_yaml/merged/methanogenium_medium__d441a404.yaml
- Started UTC: 2026-09-24T03:48:30Z
- Finished UTC: 2026-09-24T03:50:19Z
- Verdict: needs curation

## Target
- ID: CultureMech:009148
- Name: methanogenium_medium
- Label: Methanogenium Medium
- Category: archaea
- Source: TOGO M257, imported from JCM_M265
- Merge fingerprint: d441a404508afc09a04afc718e42d212f5c8b44feed78044fbf0e934952f2c56
- Merged from: TOGO_M257_Methanogenium_Medium
- Maintained owner: data/normalized_yaml/archaea/TOGO_M257_Methanogenium_Medium.yaml

## Validation
- Open schema validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed; 1 file scanned and 0 error rows.
- LinkML reference validation: Passed; exited 0 with no diagnostics.
- Term validation: Passed.
- Embedded curation history: Not checked: the history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding
- The record identity matches TOGO M257 and JCM 265, METHANOGENIUM MEDIUM.
- An exhaustive hidden and ignored search for `TOGO:M257`, `CultureMech:009148`, `JCM_M265`, and `TOGO_M257_Methanogenium_Medium` found one maintained normalized owner plus expected generated indexes and the merged output.
- NiCl2 x 6H2O is grounded to generic nickel dichloride even though the Wolfe's mineral solution source specifies the hexahydrate.

## Evidence
- JCM 265 defines a main medium with 980 ml water, salts, 10 ml Wolfe's mineral solution, 10 ml Trace vitamins from JCM 197, 2 mg Fe(NH4)2(SO4)2 x 6H2O, NaHCO3, sodium acetate, yeast extract, Trypticase peptone, and 1 mg Resazurin.
- The same source instructs users to add 10 ml 5% L-Cysteine HCl x H2O solution and 10 ml 5% Na2S x 9H2O solution aseptically and anaerobically after autoclaving.
- JCM 265 defines Wolfe's mineral solution locally as 1 L Trace minerals from JCM 151 plus NiCl2 x 6H2O, Na2SeO3, and Na2WO4 x 2H2O.
- The YAML has five empty `Unknown solution` stubs: Wolfe's mineral solution, Trace vitamins, the two 5% reducing-agent stocks, and Trace minerals.
- The Wolfe-local NiCl2 x 6H2O, Na2SeO3, and Na2WO4 x 2H2O rows are promoted to top-level final-medium ingredients rather than scoped to Wolfe's mineral solution.
- The 10 ml final solution additions and the 1 L Trace minerals addition are encoded as `G_PER_L`.
- The TOGO comments that preserve H2-CO2 cooling and dispensing, overnight standing, anaerobic additions, and 200 kPa H2:CO2 pressurization are absent from `preparation_steps`.

## Completeness
- The main JCM 265 ingredients and Wolfe-specific mineral rows are present in flattened form.
- Wolfe's mineral solution, Trace vitamins, Trace minerals, and both 5% reducing-agent solution formulas are unresolved.
- Preparation and pressure conditions are absent.
- Empty optional fields are acceptable, but these empty solution stubs stand in for required source subrecipes.

## Findings
- Major: `data/normalized_yaml/archaea/TOGO_M257_Methanogenium_Medium.yaml` leaves Wolfe's mineral solution, Trace vitamins, Trace minerals, and the two 5% reducing-agent stocks as empty `Unknown solution` placeholders.
- Major: The Wolfe-local NiCl2 x 6H2O, Na2SeO3, and Na2WO4 x 2H2O rows are top-level final-medium ingredients instead of children of Wolfe's mineral solution.
- Major: Milliliter and liter source solution additions are represented with `G_PER_L` units.
- Major: Milligram Fe(NH4)2(SO4)2 x 6H2O and Resazurin source rows are inflated to `2 G_PER_L` and `1 G_PER_L`.
- Major: The H2-CO2 gas handling, overnight standing, anaerobic reducing-agent additions, and 200 kPa inoculation pressure are missing from preparation.
- Minor: NiCl2 x 6H2O needs hydrate-specific grounding if a suitable CHEBI term is available.

## Recommended Edits
- Re-curate `data/normalized_yaml/archaea/TOGO_M257_Methanogenium_Medium.yaml` from JCM 265 and the TOGO/JCM stock references M190 and M142.
- Model 10 ml Wolfe's mineral solution and 10 ml Trace vitamins as final-medium solution additions.
- Model Trace minerals as a 1 L component of Wolfe's mineral solution, not as a final-medium amount.
- Model the 5% L-Cysteine HCl x H2O and 5% Na2S x 9H2O post-autoclave additions as 10 ml solution additions.
- Convert Fe(NH4)2(SO4)2 x 6H2O and Resazurin from milligrams to correct gram-scale concentrations.
- Restore JCM preparation notes for H2-CO2 handling, standing overnight, anaerobic stock addition, and 200 kPa pressurization.

## Follow-up Checks
- Regenerate `data/merge_yaml/merged/methanogenium_medium__d441a404.yaml`.
- Confirm that `Unknown solution` is gone from the TOGO M257 owner.
- Confirm that Wolfe's mineral solution contains Trace minerals plus NiCl2 x 6H2O, Na2SeO3, and Na2WO4 x 2H2O.
- Confirm that Trace vitamins, 5% cysteine, and 5% sulfide are not represented as `G_PER_L` rows.
- Rerun open schema, strict, reference, and term validation.

## Additional Notes
- None found.
