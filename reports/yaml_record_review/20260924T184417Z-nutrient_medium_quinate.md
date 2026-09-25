# YAML Record Review: nutrient_medium_quinate

- Repository: CultureMech
- Record: `data/merge_yaml/merged/nutrient_medium_quinate.yaml`
- Started UTC: 2026-09-24T18:44:17Z
- Finished UTC: 2026-09-24T18:45:08Z
- Verdict: needs curation

## Target

Generated bacterial record `CultureMech:007201`, `nutrient_medium_quinate`, a one-source merge from MediaDB Medium 29.

## Validation

Open LinkML validation passed with `No issues found`.

Strict validation passed; `/private/tmp/nutrient_medium_quinate.strict.tsv` contained only the header row.

Reference validation passed with 0 checks.

Term validation passed.

Embedded `curation_history` was not checked: the history validator operates over standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The generated record is correctly grounded to MediaDB Medium 29, `Nutrient medium + quinate`, and the merge contains only the single expected `nutrient_medium_quinate` source.

An exact ignored-inclusive, hidden-inclusive search for `MEDIADB:29`, `media/29/`, `media_text/29/`, `growthdata/29/`, `nutrient_medium_quinate`, and `Nutrient medium + quinate` found only the normalized owner, this generated merge, generated source indexes, and the MediaDB Medium 29 deep-research row.

## Evidence

The live MediaDB Medium 29 page and tab-delimited export list 7 compounds, all matching the generated YAML labels and mM amounts:

- Quinate 5.0 mM
- Calcium chloride anhydrous 0.034 mM
- Potassium dibasic phosphate 8.8 mM
- Dibasic sodium phosphate 10.0 mM
- Magnesium sulfate 0.8 mM
- Ammonium chloride 9.3 mM
- Ferrous sulfate 0.033 mM

MediaDB Medium 29 links source 7, `Trautwein et al, 2001`, and four 30.0 C growth-data rows: Acinetobacter baylyi ADP1, ADP197, ADP331, and ADPU331 on Nutrient medium + quinate. The ADP1 and ADP197 rows report growth rates of 0.805905 and 0.5342 1/h; all four rows report `None` for pH.

The MediaDB Medium 29 page and tab-delimited export did not expose pH-adjustment or 0.22 um filter-sterilization preparation instructions.

## Completeness

The formula table is complete relative to MediaDB 29, but the generated record is stale relative to the maintained normalized source. `data/normalized_yaml/bacterial/nutrient_medium_quinate.yaml` has an August 2026 MIM-derived `CHEBI:26490` Quinate grounding that is absent from this generated merge.

Source-specific provenance is also incomplete. The YAML has no `references`, no MediaDB source 7 or growth-data links, no scoped target organisms for the four Acinetobacter baylyi strains, and a curation-history import note naming the generic Mazumdar 2014 MediaDB paper rather than the medium-specific Trautwein 2001 source.

`Magnesium sulfate` is grounded to generic `CHEBI:32599`; the MediaDB export gives ChEBI `31795`, which the local ChEBI index labels as magnesium sulfate heptahydrate. The Quinate row also needs source-aware review because MediaDB exports `CHEBI:17521` and `CHEBI:29751`, while the repaired normalized owner uses the broader `CHEBI:26490` term from MIM.

## Findings

Needs curation:

- The generated YAML is stale and lacks the normalized owner's Quinate grounding.
- MediaDB's medium-specific primary source and four growth-data contexts are missing from the record.
- The generic MediaDB importer inserted `DISSOLVE`, conditional `ADJUST_PH`, and 0.22 um `FILTER_STERILIZE` steps that are not asserted on the inspected MediaDB Medium 29 page or tab-delimited export.
- `Magnesium sulfate` is overbroadly grounded to `CHEBI:32599` instead of MediaDB's exported `CHEBI:31795`.
- The curation history names the umbrella Mazumdar 2014 MediaDB paper instead of the medium-specific `Trautwein et al, 2001` source linked from MediaDB.

## Recommended Edits

Repair `data/normalized_yaml/bacterial/nutrient_medium_quinate.yaml` before regenerating this generated artifact:

- Add source-scoped references for MediaDB Medium 29, MediaDB Source 7, and Growth Data 57, 64, 70, and 76.
- Add four scoped Acinetobacter baylyi growth contexts for ADP1, ADP197, ADP331, and ADPU331 on this quinate medium, retaining 30.0 C for every row and growth rates for ADP1 and ADP197.
- Remove the three generic preparation steps unless Trautwein 2001 or a checked MediaDB page supports those instructions.
- Re-ground `Magnesium sulfate` from `CHEBI:32599` to `CHEBI:31795`.
- Reconcile the MIM `Quinate` grounding against MediaDB's exported quinate ChEBI IDs.
- Preserve all seven current component labels and mM values.

## Follow-up Checks

After repair, rerun open schema, strict, reference, and term validation on the normalized owner and regenerated merged YAML. Re-fetch MediaDB `/defined_media/media/29/`, `/defined_media/media_text/29/`, `/defined_media/sources/7/`, and `/defined_media/growthdata/{57,64,70,76}/` and compare the component table, source, organisms, temperature, pH, and growth-rate values.

## Additional Notes

None found.
