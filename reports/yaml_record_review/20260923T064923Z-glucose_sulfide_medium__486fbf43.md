# YAML Record Review: glucose_sulfide_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/glucose_sulfide_medium__486fbf43.yaml
- Started UTC: 2026-09-23T06:47:53Z
- Finished UTC: 2026-09-23T06:49:19Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated status | Generated merge under `data/merge_yaml/merged/` |
| ID | `CultureMech:000911` |
| Name | `glucose_sulfide_medium` |
| Original name | `GLUCOSE SULFIDE MEDIUM` |
| Category | `bacterial` |
| Media term | `mediadive.medium:1448` |
| Maintained parent | `data/normalized_yaml/bacterial/glucose_sulfide_medium.yaml` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/glucose_sulfide_medium__486fbf43.yaml` | Passed; no issues found. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/glucose_sulfide_medium__486fbf43.yaml --out /private/tmp/glucose_sulfide_medium__486fbf43.strict.tsv --workers 1 --quiet` | Passed; 0 ERROR rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/glucose_sulfide_medium__486fbf43.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/glucose_sulfide_medium__486fbf43.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` rows. |

## Identity and Grounding

This record denotes DSMZ / MediaDive medium 1448, `GLUCOSE SULFIDE MEDIUM`. A gitignore-independent exact search for `mediadive.medium:1448` and `DSMZ_Medium1448.pdf` across `data/normalized_yaml/` and `data/merge_yaml/merged/` found only this maintained parent, this generated merge, and normalized index references.

A broader ignored-inclusive search for `glucose_sulfide_medium` also found other same-label records, including DSMZ 851, JCM 514, Togo M515, and a Richard et al. 1985 variant. Those are near misses with their own source accessions, not evidence for DSMZ 1448.

The main-medium compound groundings are exact for glucose, ammonium sulfate, magnesium sulfate heptahydrate, calcium carbonate, calcium nitrate, dipotassium hydrogen phosphate, potassium chloride, sodium sulfide nonahydrate, and agar. Co Carboxylase is grounded to thiamine diphosphate in `term`, but still carries a legacy `mediaingredientmech_term` instead of a CHEBI-keyed `mediaingredientmech_chebi_term`.

## Evidence

DSMZ 1448 has a main solution plus a separately filter-sterilized vitamin solution:

| Source row | DSMZ amount |
|---|---:|
| Glucose | 0.15 g |
| (NH4)2SO4 | 0.50 g |
| MgSO4 x 7 H2O | 0.05 g |
| CaCO3 | 0.10 g |
| Ca(NO3)2 | 0.10 g |
| K2HPO4 | 0.05 g |
| KCl | 0.05 g |
| Vitamin solution | 1 ml |
| Na2S x 9 H2O | 0.19 g |
| Agar | 15.00 g |
| Distilled water | 1000 ml |

The vitamin solution is a 1000 ml stock. DSMZ and MediaDive agree that the main medium receives only 1 ml of that stock after autoclaving.

The generated record flattens each vitamin at the stock g/l value as if it were a final-medium amount. Because the medium receives 1 ml of a 1000 ml stock, each generated vitamin concentration is 1000 times too high relative to its final-medium dilution.

The source preparation text is present but under-scoped. DSMZ adjusts the main solution to pH 7.3, autoclaves it for 20 min at 121 C, adds the vitamin solution after autoclaving, and filter sterilizes the vitamin stock. The generated record has no explicit vitamin-solution boundary, so `Filter-sterilized` is ambiguous.

## Completeness

The generated record is incomplete for source structure and final amounts: it omits the 1 ml vitamin-stock addition row, the vitamin-solution grouping, and both 1000 ml water rows. The main-medium non-vitamin quantities are otherwise supported.

Empty optional fields such as `target_organisms`, `references`, and `discussion` are not defects here.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The vitamin solution was flattened at stock strength, inflating all vitamin additions 1000-fold in the final medium. | DSMZ 1448 adds 1 ml of a 1000 ml vitamin solution; the generated record stores the vitamin stock g/l rows directly as final `ingredients`. | MediaDive import normalization for `data/normalized_yaml/bacterial/glucose_sulfide_medium.yaml`. |
| Major | The source solution boundary and water rows are missing. | DSMZ 1448 has a main solution with 1000 ml water, a 1 ml Vitamin solution row, and a 1000 ml vitamin stock; the generated record has no water or stock-addition rows. | MediaDive import normalization for DSMZ 1448. |
| Minor | One ingredient still uses a legacy MIM-keyed link. | `Co Carboxylase` has `mediaingredientmech_term: MediaIngredientMech:001083`, while the June 2026 migration history says legacy MediaIngredientMech IDs were replaced by CHEBI-keyed links. | MIM legacy migration output for `data/normalized_yaml/bacterial/glucose_sulfide_medium.yaml`. |
| Minor | Cyanocobalamin lost the source vitamin B12 attribute. | MediaDive stores `attribute: vitamin B12`; the generated row keeps only `preferred_term: Cyanocobalamin`. | MediaDive import normalization for DSMZ 1448 if attributes are in scope. |

## Recommended Edits

1. Recode DSMZ 1448's vitamin solution as a stock solution and the main medium's vitamin row as a 1 ml stock addition.
2. Preserve the two distilled-water rows in the appropriate solution scopes if water rows are represented for direct DSMZ records.
3. Scope `Filter-sterilized` to the vitamin solution rather than the main autoclaved medium.
4. Replace the lingering `mediaingredientmech_term` on Co Carboxylase with a CHEBI-keyed link or explicitly mark it unresolved if MIM has no CHEBI mapping.
5. Preserve the MediaDive `vitamin B12` attribute for Cyanocobalamin if ingredient attributes are in scope.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation after regenerating `data/merge_yaml/merged/glucose_sulfide_medium__486fbf43.yaml`.
- Compare the regenerated record against the DSMZ 1448 PDF or MediaDive 1448 REST payload and verify the main solution, 1 ml vitamin solution addition, vitamin stock, preparation steps, and water rows.
- Re-run the exact gitignore-independent search for `mediadive.medium:1448` and `DSMZ_Medium1448.pdf` across `data/normalized_yaml/` and `data/merge_yaml/merged/` to verify no extra DSMZ 1448 copies were introduced.

## Additional Notes

The DSMZ PDF text extraction renders the calcium nitrate row as `Ca(NO3)`, while the MediaDive JSON reports `Ca(NO3)2`. The generated `Ca(NO3)2` row follows MediaDive.
