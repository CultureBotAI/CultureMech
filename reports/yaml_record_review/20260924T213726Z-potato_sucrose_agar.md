# YAML Record Review: potato_sucrose_agar

- Repository: CultureMech
- Record: data/merge_yaml/merged/potato_sucrose_agar.yaml
- Started UTC: 2026-09-24T21:37:26Z
- Finished UTC: 2026-09-24T21:37:26Z
- Verdict: needs curation

## Target

- MediaRecipe ID: CultureMech:002692
- Name: potato_sucrose_agar
- Source import: JCM Medium J333
- Primary external ID: mediadive.medium:J333
- Maintained input: data/normalized_yaml/bacterial/potato_sucrose_agar.yaml

This generated record represents a direct JCM import of JCM Medium 333, POTATO-SUCROSE AGAR.

## Validation

- Open LinkML validation: passed with no reported issues.
- Strict validation: passed for 1 file with 0 error rows; `/private/tmp/potato_sucrose_agar.strict.tsv` is header-only.
- Reference validation: passed for 1 file with 0 reference checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

JCM 333 is the cited source and lists Potato 200 g, Sucrose 20 g, Agar 20 g, and Distilled water 1.0 L, with pH adjustment to 5.6 and a potato-extract preparation step.

The generated record keeps the JCM name, pH 5.6, potato, sucrose, agar, and preparation text, but it omits the 1.0 L distilled-water ingredient from the JCM composition table.

The generated record also records `kg_microbe_match: mediadive.medium:187`, but MediaDive medium 187 is DSMZ MEDIUM FOR OSMOPHILIC FUNGI (M 40 Y), a distinct sucrose/malt-extract/yeast-extract/agar medium at pH 5.4.

Exact ignored-file searches across `data/normalized_yaml` and `data/merge_yaml` for `GRMD=333`, `JCM Medium J333`, `mediadive.medium:J333`, `mediadive.medium:187`, and `potato_sucrose_agar` found this direct JCM import, a separate TOGO M328 normalized record that cites the same JCM `GRMD=333` URL, a separate `potato_sucrose_agar_psa` generated merge, and several unrelated `kg_microbe_match: mediadive.medium:187` occurrences.

## Evidence

- The JCM 333 page lists 200.0 g Potato, 20.0 g Sucrose, 20.0 g Agar, and 1.0 L Distilled water.
- The JCM 333 page instructs pH adjustment to 5.6 and preparation by boiling 200 g potato cubes in 1.0 L distilled water for 20 min, adding agar and sucrose, making up to 1.0 L, adjusting pH, and autoclaving.
- TOGO M328 imports the same JCM_M333 source and the same `GRMD=333` URL, but it lives in `data/normalized_yaml/bacterial/TOGO_M328_Potato-Sucrose_Agar.yaml` and is merged into `data/merge_yaml/merged/potato_sucrose_agar_psa.yaml`.
- MediaDive medium 187 resolves to DSMZ Medium 187, not JCM Medium 333.

## Completeness

The generated record is incomplete relative to JCM 333 because it omits the source 1.0 L distilled water row. It is also not globally deduplicated: the same JCM 333 source exists in the TOGO M328 import under the separate `potato_sucrose_agar_psa` generated record.

## Findings

1. Major: `data/normalized_yaml/bacterial/potato_sucrose_agar.yaml` and this generated output omit the JCM 333 1.0 L Distilled water row.
2. Major: JCM 333 is split across two generated outputs; the direct JCM import remains in `potato_sucrose_agar.yaml`, while TOGO M328 for the same JCM source is merged into `potato_sucrose_agar_psa.yaml`.
3. Major: `kg_microbe_match: mediadive.medium:187` is a false external match to DSMZ MEDIUM FOR OSMOPHILIC FUNGI (M 40 Y), not Potato-Sucrose Agar.
4. Minor: `media_term.term.id` uses `mediadive.medium:J333`, which preserves a JCM local number in a MediaDive CURIE namespace instead of a resolvable JCM or numeric MediaDive identifier.

## Recommended Edits

- Add the missing 1.0 L Distilled water component to `data/normalized_yaml/bacterial/potato_sucrose_agar.yaml`.
- Remove the false `mediadive.medium:187` KG-Microbe match from the maintained normalized record.
- Reconcile the direct JCM 333 and TOGO M328 imports so the same JCM source is not emitted under two generated potato-sucrose-agar records.
- Replace `mediadive.medium:J333` with a source identifier that reflects JCM 333 rather than a nonnumeric MediaDive CURIE.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation after normalized curation and regeneration.
- Run exact ignored-file searches for `GRMD=333`, `TOGO:M328`, `JCM_M333`, and `mediadive.medium:187` after deduplication to confirm only the intended Potato-Sucrose Agar records remain.
- Spot-check that the regenerated JCM 333 record contains 200 g potato, 20 g sucrose, 20 g agar, 1 L distilled water, and pH 5.6.

## Additional Notes

None found.
