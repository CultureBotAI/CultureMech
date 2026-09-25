# YAML Record Review: nutrient_medium_glucose

- Repository: CultureMech
- Record: `data/merge_yaml/merged/nutrient_medium_glucose.yaml`
- Started UTC: 2026-09-24T18:37:40Z
- Finished UTC: 2026-09-24T18:39:22Z
- Verdict: needs curation

## Target

Generated bacterial record `CultureMech:007169`, `nutrient_medium_glucose`, a one-source merge from MediaDB Medium 26.

## Validation

Open LinkML validation passed with `No issues found`.

Strict validation passed; `/private/tmp/nutrient_medium_glucose.strict.tsv` contained only the header row.

Reference validation passed with 0 checks.

Term validation passed.

Embedded `curation_history` was not checked: the history validator operates over standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The generated record is correctly grounded to MediaDB Medium 26, `Nutrient medium + glucose`, and the merge contains only the single expected `nutrient_medium_glucose` source.

An exact ignored-inclusive, hidden-inclusive search for `MEDIADB:26`, `media/26/`, `media_text/26/`, `growthdata/26/`, `nutrient_medium_glucose`, and `Nutrient medium + glucose` found only the normalized owner, this generated merge, generated source indexes, and the MediaDB Medium 26 deep-research row.

## Evidence

The live MediaDB Medium 26 page and tab-delimited export list 7 compounds, all matching the generated YAML labels and mM amounts:

- D-Glucose 10.0 mM
- Calcium chloride anhydrous 0.034 mM
- Potassium dibasic phosphate 8.8 mM
- Dibasic sodium phosphate 10.0 mM
- Magnesium sulfate 0.8 mM
- Ammonium chloride 9.3 mM
- Ferrous sulfate 0.033 mM

MediaDB Medium 26 links source 7, `Trautwein et al, 2001`, and four 30.0 C growth-data rows: Acinetobacter baylyi ADP1, ADP197, ADP331, and ADPU331 on Nutrient medium + glucose. Those growth-data rows report `None` for growth rate and pH.

The MediaDB Medium 26 page and tab-delimited export did not expose pH-adjustment or 0.22 um filter-sterilization preparation instructions.

## Completeness

The formula table is complete relative to MediaDB 26, but source-specific provenance is incomplete. The YAML has no `references`, no MediaDB source 7 or growth-data links, no scoped target organisms for the four Acinetobacter baylyi strains, and a curation-history import note naming the generic Mazumdar 2014 MediaDB paper rather than the medium-specific Trautwein 2001 source.

`Magnesium sulfate` is grounded to generic `CHEBI:32599`; the MediaDB export gives ChEBI `31795`, which the local ChEBI index labels as magnesium sulfate heptahydrate.

## Findings

Needs curation:

- MediaDB's medium-specific primary source and four growth-data contexts are missing from the record.
- The generic MediaDB importer inserted `DISSOLVE`, conditional `ADJUST_PH`, and 0.22 um `FILTER_STERILIZE` steps that are not asserted on the inspected MediaDB Medium 26 page or tab-delimited export.
- `Magnesium sulfate` is overbroadly grounded to `CHEBI:32599` instead of MediaDB's exported `CHEBI:31795`.
- The curation history names the umbrella Mazumdar 2014 MediaDB paper instead of the medium-specific `Trautwein et al, 2001` source linked from MediaDB.

## Recommended Edits

Repair `data/normalized_yaml/bacterial/nutrient_medium_glucose.yaml` before regenerating this generated artifact:

- Add source-scoped references for MediaDB Medium 26, MediaDB Source 7, and Growth Data 54, 67, 61, and 73.
- Add four scoped Acinetobacter baylyi growth contexts for ADP1, ADP197, ADP331, and ADPU331 on this glucose medium, retaining the 30.0 C temperature and the explicit `None` pH and growth-rate values as MediaDB evidence notes if the schema cannot represent them directly.
- Remove the three generic preparation steps unless Trautwein 2001 or a checked MediaDB page supports those instructions.
- Re-ground `Magnesium sulfate` from `CHEBI:32599` to `CHEBI:31795`.
- Preserve all seven current component labels and mM values.

## Follow-up Checks

After repair, rerun open schema, strict, reference, and term validation on the normalized owner and regenerated merged YAML. Re-fetch MediaDB `/defined_media/media/26/`, `/defined_media/media_text/26/`, `/defined_media/sources/7/`, and `/defined_media/growthdata/{54,61,67,73}/` and compare the component table, source, organisms, temperature, pH, and growth-rate values.

## Additional Notes

None found.
