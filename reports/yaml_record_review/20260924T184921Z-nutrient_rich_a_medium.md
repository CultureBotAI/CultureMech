# YAML Record Review: nutrient_rich_a_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/nutrient_rich_a_medium.yaml`
- Started UTC: 2026-09-24T18:49:21Z
- Finished UTC: 2026-09-24T18:49:55Z
- Verdict: needs curation

## Target

Generated bacterial record `CultureMech:009479`, `nutrient_rich_a_medium`, a one-source TOGO M2952 import.

## Validation

Open LinkML validation passed with `No issues found`.

Strict validation passed; `/private/tmp/nutrient_rich_a_medium.strict.tsv` contained only the header row.

Reference validation passed with 0 checks.

Term validation passed.

Embedded `curation_history` was not checked: the history validator operates over standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The reviewed record is grounded to TOGO M2952, `nutrient-rich A medium`, and the generated merge contains only the single expected `nutrient_rich_a_medium` source.

An exact ignored-inclusive, hidden-inclusive search for `TOGO:M2952`, `GMDB:M2952`, `M2952`, `nutrient_rich_a_medium`, and `nutrient-rich A medium` found only the normalized owner, this generated merge, source indexes, and the TOGO M2952 deep-research row.

## Evidence

TOGO M2952 lists the same 16 top-level rows as the CultureMech record: Distilled water; MgSO4 x 7H2O; yeast extract; KH2PO4; K2HPO4; FeSO4 x 7H2O; biotin; (NH4)2SO4; MnSO4 x H2O; thiamine; optional chloramphenicol; optional kanamycin; glucose; optional gentamicin; casamino acid; and (NH2)2CO.

The generated record preserves the source g/L, mg/L, and 4% glucose amounts for the base A medium.

TOGO M2952 lists optional C. glutamicum antibiotic concentrations of 5 ug/ml chloramphenicol, 50 ug/ml kanamycin, and 50 ug/ml gentamicin. These are 5, 50, and 50 mg/L, respectively.

## Completeness

The generated record omits the TOGO source comment that scopes the recipe to C. glutamicum A medium with 4% glucose and optional antibiotics for genetic manipulations.

No source organism, DOI, PMID, or growth measurement is present in the TOGO M2952 API response, so target-organism and growth-metric slots are correctly empty for now.

## Findings

Needs curation:

- `Distilled water` is encoded as `1 G_PER_L`; TOGO M2952 lists 1 L Distilled water.
- Optional `chloramphenicol`, `kanamycin`, and `gentamicin` are encoded as 5, 50, and 50 g/L, but the TOGO M2952 source lists 5, 50, and 50 ug/ml.
- The free-text source comment that mentions C. glutamicum A medium with 4% glucose and optional antibiotics is not represented.
- The `thiamine` row still has a legacy `mediaingredientmech_term` link alongside its CHEBI term instead of a refreshed `mediaingredientmech_chebi_term` link.

## Recommended Edits

Repair `data/normalized_yaml/bacterial/nutrient_rich_a_medium.yaml` before regenerating this artifact:

- Convert `Distilled water` to `1000 ML_PER_L`.
- Convert the optional antibiotic rows to `MG_PER_L` with the same numeric values, because 1 ug/ml equals 1 mg/L.
- Preserve the TOGO M2952 source comment in a notes or evidence field so the optional-antibiotic context is not lost.
- Refresh the `thiamine` MediaIngredientMech link to the current CHEBI-keyed slot.

## Follow-up Checks

After repair, rerun open schema, strict, reference, and term validation on the normalized owner and regenerated merged YAML. Re-fetch TOGO M2952 and confirm the base A-medium values, 4% glucose, optional antibiotic units, and water volume all match the source JSON.

## Additional Notes

None found.
