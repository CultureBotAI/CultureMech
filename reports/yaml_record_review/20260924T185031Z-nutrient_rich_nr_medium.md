# YAML Record Review: nutrient_rich_nr_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/nutrient_rich_nr_medium.yaml`
- Started UTC: 2026-09-24T18:50:31Z
- Finished UTC: 2026-09-24T18:51:06Z
- Verdict: needs curation

## Target

Generated bacterial record `CultureMech:009647`, `nutrient_rich_nr_medium`, a one-source TOGO M3207 import.

## Validation

Open LinkML validation passed with `No issues found`.

Strict validation passed; `/private/tmp/nutrient_rich_nr_medium.strict.tsv` contained only the header row.

Reference validation passed with 0 checks.

Term validation passed.

Embedded `curation_history` was not checked: the history validator operates over standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The reviewed record is grounded to TOGO M3207, `Nutrient rich (NR) medium`, and the generated merge contains only the single expected `nutrient_rich_nr_medium` source.

An exact ignored-inclusive, hidden-inclusive search for `TOGO:M3207`, `GMDB:M3207`, `M3207`, `nutrient_rich_nr_medium`, and `Nutrient rich (NR) medium` found only the maintained normalized owner, this generated merge, generated source indexes, and the TOGO M3207 deep-research row.

## Evidence

TOGO M3207 lists 10 g meat extract, 10 g Peptone, 2 g Yeast extract, and 1 L Distilled water. Its source comment says C. necator PHB-4 was cultivated in nutrient rich medium containing 10 g/L meat extract, 10 g/L peptone, and 2 g/L yeast extract at 30 C.

The generated record preserves the three non-water ingredient amounts.

## Completeness

The generated record is stale relative to the maintained normalized owner. `data/normalized_yaml/bacterial/nutrient_rich_nr_medium.yaml` already stores source-scoped ingredient notes, Peptone and Yeast extract ontology mappings, temperature 30.0, a TOGO M3207 reference, and `ingredients_curated`, `has_ontology_mappings`, and `has_unmapped_ingredients` data-quality flags.

No DOI, PMID, or quantitative growth metric is present in the TOGO M3207 API response; those slots are correctly empty.

## Findings

Needs curation:

- `Distilled water` is encoded as `1 G_PER_L`; TOGO M3207 lists 1 L Distilled water.
- The generated record lost the source-supported 30 C cultivation temperature.
- The generated record is stale relative to the September 2026 normalized repair and is missing source annotations, ontology mappings for Peptone and Yeast extract, data-quality flags, and the structured TOGO M3207 reference.

## Recommended Edits

Regenerate `data/merge_yaml/merged/nutrient_rich_nr_medium.yaml` from `data/normalized_yaml/bacterial/nutrient_rich_nr_medium.yaml` so the generated artifact carries the repaired water unit, 30 C temperature, source notes, ontology mappings, quality flags, and reference.

Do not hand-edit the generated YAML unless the merge pipeline cannot be rerun; the authoritative repair is already in the normalized source record.

## Follow-up Checks

After regeneration, rerun open schema, strict, reference, and term validation on the generated YAML. Re-fetch TOGO M3207 and confirm the generated record has 10 g/L meat extract, 10 g/L Peptone, 2 g/L Yeast extract, a 1 L or 1000 ml/L Distilled water row, and temperature 30.0.

## Additional Notes

None found.
