# YAML Record Review: GALENEA MJ MEDIUM (CO2)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/galenea_mj_medium_co2.yaml
- Started UTC: 2026-09-23T05:08:40Z
- Finished UTC: 2026-09-23T05:12:05Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:000431`, `galenea_mj_medium_co2`, category `bacterial`, for DSMZ Medium 1011d / MediaDive `mediadive.medium:1011d`.

The generated merge contains one source, `galenea_mj_medium_co2`, with merge fingerprint `18ef423f1d4ca66479dbea69bbca1884b8e2f4c8ac3fdc14fec4e1df9f81afc6`; the maintained source that owns future YAML edits is `data/normalized_yaml/bacterial/galenea_mj_medium_co2.yaml`.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/galenea_mj_medium_co2.yaml` | Passed with `No issues found`. |
| `python scripts/validate_strict.py data/merge_yaml/merged/galenea_mj_medium_co2.yaml --out /private/tmp/galenea_mj_medium_co2.strict.tsv --workers 1 --quiet` | Passed; the TSV had one header row and no error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/galenea_mj_medium_co2.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the reference validator reported zero checks. |
| `linkml-term-validator validate-data data/merge_yaml/merged/galenea_mj_medium_co2.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the repository documents `just validate-history` for standalone files under `history/`, not for generated `MediaRecipe.curation_history` entries. |

## Identity and Grounding

The record identity is correct: MediaDive REST resolves medium `1011d` to `GALENEA MJ MEDIUM (CO2)`, source `DSMZ`, pH 6.7, and the DSMZ Medium 1011d PDF URL that is already in the YAML notes. The DSMZ PDF also carries the title `1011d: GALENEA MJ MEDIUM (CO2)`.

An ignored-file-inclusive search over `data/normalized_yaml` and `data/merge_yaml/merged` for `mediadive.medium:1011d`, `CultureMech:000431`, and `galenea_mj_medium_co2` found this normalized bacterial record, this generated merge, and generated indexes only; it did not find a second merged record for the same source accession.

Most direct ingredient groundings match the supplied salts and vitamins, but the `NiCl2 x 6 H2O` row is under-grounded to anhydrous `CHEBI:34887` / `nickel dichloride`. DSMZ and MediaDive specifically name the hexahydrate form.

## Evidence

The top-level DSMZ formula contains NaCl, K2HPO4, CaCl2 x 2 H2O, MgSO4 x 7 H2O, MgCl2 x 6 H2O, KCl, NH4Cl, Fe(NH4)2(SO4)2 x 6 H2O, `10.00 ml` Modified Wolin's mineral solution, Na2CO3, Na2S2O3 x 5 H2O, `1.00 ml` Wolin's vitamin solution (10x), and `1000.00 ml` distilled water. MediaDive preserves that structure as main solution `2062`, stock solution `241`, and stock solution `5980`.

The generated `ingredients` list instead flattens the two nested stock solutions into the final medium. Every ingredient from Modified Wolin's mineral solution appears as a final-medium `G_PER_L` row at stock strength, even though DSMZ says to add only 10 ml of that stock. Every ingredient from the 10x Wolin vitamin solution also appears at stock strength, even though DSMZ says to add only 1 ml of that stock.

Three rows additionally prove cross-scope duplicate merging:

| Ingredient | Generated value | Supported DSMZ / MediaDive structure |
|---|---:|---|
| NaCl | 30.6736 g/L, with `Merged 2 duplicates: 29.6736, 1.0` | 30 g in the main medium plus 1 g/L in a 10 ml/L mineral stock. |
| CaCl2 x 2 H2O | 0.238477 g/L, with `Merged 2 duplicates: 0.138477, 0.1` | 0.14 g in the main medium plus 0.1 g/L in a 10 ml/L mineral stock. |
| MgSO4 x 7 H2O | 6.36301 g/L, with `Merged 2 duplicates: 3.36301, 3.0` | 3.4 g in the main medium plus 3 g/L in a 10 ml/L mineral stock. |

The importer also propagated MediaDive final-volume normalization into the main rows: for example, MediaDive stores main solution volume `1011` and converts the 30 g NaCl row to 29.6736 g/L. That calculated concentration is not wrong by itself, but the generated record loses the 10 ml and 1 ml solution-addition rows, omits the 1000 ml water row, and leaves no way to distinguish final-medium concentrations from stock concentrations.

## Completeness

The record captures pH 6.7 and the two main preparation steps from DSMZ 1011d. It also captured the Modified Wolin stock preparation text, but as a third top-level `ADJUST_PH` step rather than as a stock-specific instruction; this makes the generated main medium appear to require both final pH 6.7 and a separate final pH 7.0 adjustment.

Consequential gaps:

- `Modified Wolin's mineral solution` should be represented as a nested stock addition of 10 ml, not as its full one-liter formula on the main ingredient list.
- `Wolin's vitamin solution (10x)` should be represented as a nested stock addition of 1 ml, not as its full one-liter formula on the main ingredient list.
- The main-medium 1000 ml distilled water row is absent.
- The stock-solution 1000 ml distilled water rows and their provenance from DSMZ medium 141 and DSMZ medium 120 are absent.
- The normalized source carries the same defects as the generated merge, so regeneration alone will not repair this record.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | DSMZ stock solutions were flattened into the main GALENEA MJ recipe at stock strength. | DSMZ 1011d lists only 10 ml Modified Wolin's mineral solution and 1 ml Wolin's vitamin solution in the top-level medium; MediaDive keeps those as solution links, but the YAML expands every mineral and vitamin stock ingredient as a top-level `G_PER_L` row. | `data/normalized_yaml/bacterial/galenea_mj_medium_co2.yaml` and the MediaDive import that writes nested solutions. |
| Major | Duplicate merging combined main-medium salts with stock-solution salts. | NaCl, CaCl2 x 2 H2O, and MgSO4 x 7 H2O have generated duplicate-merge notes that sum the MediaDive main-solution g/L values with the Modified Wolin stock-solution g/L values. | `data/normalized_yaml/bacterial/galenea_mj_medium_co2.yaml` and duplicate merge logic. |
| Major | Source volumes and nested-solution provenance were lost. | DSMZ 1011d and MediaDive include 1000 ml distilled water in the main medium, 1000 ml water in each stock recipe, and solution-level references to DSMZ medium 141 and 120; the generated record has no water row or stock source boundary. | `data/normalized_yaml/bacterial/galenea_mj_medium_co2.yaml`. |
| Major | The Modified Wolin stock pH instruction is scoped as a top-level final-medium step. | The generated `ADJUST_PH` step says to dissolve nitrilotriacetic acid and adjust final pH to 7.0, while DSMZ places that text under the Modified Wolin's mineral solution subsection, not under the complete GALENEA MJ medium. | `data/normalized_yaml/bacterial/galenea_mj_medium_co2.yaml`. |
| Minor | `NiCl2 x 6 H2O` is grounded to a term that omits the hydrate. | The source ingredient is nickel chloride hexahydrate; the YAML uses `CHEBI:34887` / `nickel dichloride`. | `data/normalized_yaml/bacterial/galenea_mj_medium_co2.yaml`. |

## Recommended Edits

1. Repair the MediaDive-normalized representation in `data/normalized_yaml/bacterial/galenea_mj_medium_co2.yaml` so DSMZ 1011d has main-solution rows, explicit 10 ml and 1 ml nested-solution additions, and separate `SolutionRecipe` entries for Modified Wolin's mineral solution and Wolin's vitamin solution (10x).
2. Preserve the three 1000 ml distilled-water rows in the right main or stock solution scope, rather than dropping water entirely.
3. Keep the Modified Wolin mineral-solution pH 6.5 and 7.0 instructions attached to that stock recipe; keep the final pH 6.7 adjustment attached to the complete GALENEA MJ medium.
4. Prevent duplicate-ingredient consolidation across main and stock-solution scopes when regenerating `data/merge_yaml/merged/galenea_mj_medium_co2.yaml`.
5. Ground `NiCl2 x 6 H2O` to an exact nickel chloride hexahydrate term if one is available in the accepted CHEBI release; otherwise leave its exact supplied form explicit and unresolved instead of mapping it to an anhydrous salt.

## Follow-up Checks

After curation, rerun focused schema, strict, reference, and term validation on `data/merge_yaml/merged/galenea_mj_medium_co2.yaml`.

Manually compare the regenerated record with:

- MediaDive REST `https://mediadive.dsmz.de/rest/medium/1011d`
- DSMZ `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1011d.pdf`

Check that NaCl, CaCl2 x 2 H2O, and MgSO4 x 7 H2O are no longer marked as merged duplicates across stock boundaries.

## Additional Notes

The record is generated from a single normalized source; no separate direct-vs-snapshot conflict was found in the ignored-file-inclusive search described above.
