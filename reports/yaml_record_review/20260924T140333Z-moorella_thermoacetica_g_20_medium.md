# YAML Record Review: MOORELLA THERMOACETICA (G-20) MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/moorella_thermoacetica_g_20_medium.yaml
- Started UTC: 2026-09-24T14:02:22Z
- Finished UTC: 2026-09-24T14:03:33Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:001658 |
| Name | moorella_thermoacetica_g_20_medium |
| Original name | MOORELLA THERMOACETICA (G-20) MEDIUM |
| Primary source owner | data/normalized_yaml/bacterial/moorella_thermoacetica_g_20_medium.yaml |
| Merged source owner | data/normalized_yaml/bacterial/clostridium_thermoaceticum_ii_medium.yaml |
| Generated record | Yes; produced under data/merge_yaml/merged with merge_fingerprint 1b4a616d353438ca7219d6b50700f3c1d39b9a7be3cab3c54eb88360089dc131 |

## Validation

| Check | Result |
| --- | --- |
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/moorella_thermoacetica_g_20_medium.yaml` | Passed; `No issues found`. |
| `python scripts/validate_strict.py data/merge_yaml/merged/moorella_thermoacetica_g_20_medium.yaml --out /private/tmp/moorella_thermoacetica_g_20_medium.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors, 0 total error rows, and the TSV contained only the header. |
| `linkml-reference-validator validate data data/merge_yaml/merged/moorella_thermoacetica_g_20_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 references were checked. |
| `linkml-term-validator validate-data data/merge_yaml/merged/moorella_thermoacetica_g_20_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the expected `eutils` / `pkg_resources` warning. |
| Embedded `curation_history` | Not checked: the documented history validator targets the standalone `history/` corpus, not inline `MediaRecipe.curation_history`. |

## Identity and Grounding

The primary record denotes DSMZ / MediaDive medium 527, `MOORELLA THERMOACETICA (G-20) MEDIUM`, and keeps pH 6.9 from the MediaDive REST record. The merged KOMODO child also maps to DSMZ Medium 527 and says the DSMZ 527 ingredients were copied into it, so the KOMODO merge is a plausible source duplicate rather than a collision between distinct recipes.

An ignored-inclusive search over `data/normalized_yaml` and `data/merge_yaml` for exact `mediadive.medium:527`, `komodo.medium:527`, `DSMZ_Medium527.pdf`, the Moorella G-20 slug, and the Clostridium thermoaceticum II slug found only the expected MediaDive owner, KOMODO child owner, generated merged output, and index entries.

Most ontology groundings are appropriate. `NiCl2 x 6 H2O` is grounded to CHEBI:34887 `nickel dichloride`, which does not capture the hexahydrate in the source label.

## Evidence

MediaDive exposes medium 527 as a five-solution recipe. The main solution has a 1018 ml total built by adding 608 ml Solution A, 300 ml Solution B, 100 ml Solution C, 5 ml Solution D, and 5 ml Solution E, then adjusting the completed medium to pH 6.9 if necessary.

The generated record stores the concentrations of Solutions A through E as if they were final medium concentrations:

| Source claim | Generated representation | Assessment |
| --- | --- | --- |
| Solution A is a 608 ml stock containing 5 g yeast extract, 5 g tryptone peptone, 1.8 g Na-pyruvate, 1 g ammonium sulfate, salts, and water | Solution A concentrations are top-level rows, e.g. 8.22368 g/L yeast extract and 2.96053 g/L Na-pyruvate | These values are grams per liter of Solution A, not final medium values. |
| Solution B is a 300 ml stock with 16.8 g NaHCO3, 7 g K2HPO4, 5.5 g KH2PO4, and water | 56 g/L NaHCO3, 23.3333 g/L K2HPO4, and 18.3333 g/L KH2PO4 | These are Solution B stock strengths. |
| Solution C is 100 ml with 20 g D-glucose | 200 g/L D-glucose | This is the Solution C stock strength. |
| Solution D is 5 ml with 0.25 g L-Cysteine-HCl-H2O | 50 g/L L-Cysteine-HCl-H2O | This is the Solution D stock strength. |
| Solution E is 5 ml with 0.25 g Na2S x 9 H2O | 50 g/L Na2S x 9 H2O | This is the Solution E stock strength. |

The long preparation instruction is supported by the MediaDive REST step: Solution A is sparged with 100% CO2, Solution B is autoclaved under 80% N2 / 20% CO2, Solutions C through E are autoclaved under 100% N2, and solutions B through E are added to sterile Solution A in sequence.

The DSMZ PDF link embedded in the record no longer served the medium PDF during review; it downloaded a TYPO3 404 page. MediaDive REST remained available and carried the structured recipe.

## Completeness

No empty optional scalar fields are present, and the absent target organism list is not a schema defect for this provider recipe.

The record is incomplete because all five named solutions and their water rows were discarded. Without Solution A through E as structured stocks, the 608 ml / 300 ml / 100 ml / 5 ml / 5 ml assembly cannot be represented, and all numeric `G_PER_L` values for the stock ingredients are ambiguous or misleading as final-medium concentrations.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Solution A through E were flattened into top-level final ingredients. | MediaDive medium 527 has a main recipe that combines 608 ml A, 300 ml B, 100 ml C, 5 ml D, and 5 ml E; the YAML has no `solutions` array and stores every stock ingredient as a final ingredient. | `data/normalized_yaml/bacterial/moorella_thermoacetica_g_20_medium.yaml` and the DSMZ/MediaDive import path. |
| Major | Several high-strength stock concentrations are materially over-scoped as final medium concentrations. | 56 g/L NaHCO3, 200 g/L D-glucose, 50 g/L L-Cysteine-HCl-H2O, and 50 g/L Na2S x 9 H2O are the concentrations of Solutions B through E, not of the completed 1018 ml medium. | `data/normalized_yaml/bacterial/moorella_thermoacetica_g_20_medium.yaml`; the KOMODO child inherits the same copied values. |
| Major | Required solution-local water rows are absent. | MediaDive lists 600 ml water in Solution A, 300 ml in Solution B, 100 ml in Solution C, 5 ml in Solution D, and 5 ml in Solution E; none are present in the generated YAML. | The DSMZ/MediaDive solution importer. |
| Major | NiCl2 x 6 H2O has the wrong CHEBI grounding. | The ingredient label is nickel chloride hexahydrate, but the term is CHEBI:34887 `nickel dichloride`. | CHEBI enrichment over the MediaDive owner and any KOMODO copy. |
| Minor | The DSMZ PDF URL is stale. | Fetching `DSMZ_Medium527.pdf` returned a TYPO3 404 page, while the same medium was still available through MediaDive REST ID 527. | Source metadata in `data/normalized_yaml/bacterial/moorella_thermoacetica_g_20_medium.yaml`. |

## Recommended Edits

1. Rebuild DSMZ / MediaDive medium 527 with Solution A, B, C, D, and E as structured stocks and a main solution that adds 608, 300, 100, 5, and 5 ml respectively.
2. Keep stock-specific `G_PER_L` concentrations inside their source solution objects or convert them to final concentrations only after preserving the assembly semantics.
3. Include the water rows for all five stocks so each solution recipe is complete.
4. Keep the KOMODO 527 child as a source duplicate only if it continues to resolve to DSMZ Medium 527; do not let it fork an independent flat copy of the same solution-local values.
5. Correct the NiCl2 x 6 H2O CHEBI grounding to a hexahydrate term after the maintained owners are updated.
6. Replace the stale DSMZ PDF URL with a live source URL if DSMZ publishes a new PDF location, and retain MediaDive REST 527 as the structured source identity.

## Follow-up Checks

- Rerun `linkml-validate`, `scripts/validate_strict.py`, `linkml-reference-validator`, and `linkml-term-validator` on the regenerated Moorella G-20 record.
- Manually compare the regenerated record against MediaDive REST medium 527 and verify the 608/300/100/5/5 ml main assembly plus pH 6.9.
- Run an ignored-inclusive search for `mediadive.medium:527`, `komodo.medium:527`, `moorella_thermoacetica_g_20_medium`, and `clostridium_thermoaceticum_ii_medium` across `data/normalized_yaml` and `data/merge_yaml` to confirm there is still a single generated DSMZ 527 recipe with a KOMODO source alias or child.

## Additional Notes

The source merge itself is sounder than the formula import: both normalized owners point to medium 527, but both owners carry the same flat stock-concentration projection.
