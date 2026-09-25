# YAML Record Review: Chocolate agar

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/CHOCOLATE_AGAR.yaml
- Started UTC: 2026-09-22T07:25:38Z
- Finished UTC: 2026-09-22T07:27:02Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:008860 |
| Label | Chocolate agar |
| Generated record | data/merge_yaml/merged/CHOCOLATE_AGAR.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M2274_Chocolate_agar.yaml |
| Source | TOGO Medium M2274 |

The reviewed file is a generated one-source merge of TOGO M2274. Future fixes
belong in `data/normalized_yaml/bacterial/TOGO_M2274_Chocolate_agar.yaml`, the
TOGO unit-conversion importer, or the commercial-medium expansion overlay
rather than in `data/merge_yaml/merged/CHOCOLATE_AGAR.yaml`.

## Validation

| Check | Result |
| --- | --- |
| Open LinkML validation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe` | Passed |
| `scripts/validate_strict.py` on the generated record | Passed; 0 errors in `/private/tmp/CHOCOLATE_AGAR.strict.tsv` |
| `linkml-reference-validator validate data` on the generated record | Passed; 0 checks |
| `linkml-term-validator validate-data` on the generated record | Passed |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` objects in a merged YAML file |

The first TOGO API request failed on DNS resolution inside the sandbox and then
passed when retried directly. The term validator emitted only the expected
`eutils/pkg_resources is deprecated` warning before passing.

## Identity and Grounding

The identity is coherent: `CultureMech:008860`, `TOGO:M2274`, and the
normalized owner all denote TOGO Chocolate agar.

An ignored-independent `rg --no-ignore --hidden` search across
`data/normalized_yaml` and `data/merge_yaml/merged` for the CultureMech ID,
TOGO M2274 source ID, normalized owner stem, and merge fingerprint found this
generated record, its TOGO owner, and normalized index entries.

## Evidence

TOGO M2274 supports six source components: 1 L distilled water, 5 ug/mL hemin,
0.2 ug/mL menadione, 10% sheep blood, 40 g Trypticase soy agar from BBL, and a
5% carbon dioxide gas atmosphere.

Three supported quantities were imported with the wrong unit or magnitude.
Distilled water is recorded as `1 G_PER_L` even though the source amount is a
1 L volume. Hemin is recorded as 5 g/L but 5 ug/mL converts to 0.005 g/L.
Menadione is recorded as 0.2 g/L but 0.2 ug/mL converts to 0.0002 g/L.

The source asserts a single commercial component, 40 g/L `Trypticase soy agar
(BBL)`. The record instead removes that component and inserts a 45 g/L
constituent expansion from a generic TSB/TSA product note: 17 g/L pancreatic
digest of casein, 3 g/L soybean meal digest, 2.5 g/L glucose, 5 g/L sodium
chloride, 2.5 g/L dipotassium phosphate, and 15 g/L agar. TOGO does not supply
this expansion, the notes cite Wikipedia instead of a BBL Trypticase soy agar
specification, and the substituted totals no longer equal the source's 40 g/L
commercial ingredient.

The imported carbon dioxide row is less precise than TOGO M2274 because the
source gives a 5% atmosphere and the record preserves only `variable`.

## Completeness

The empty `target_organisms` and growth-observation fields are not defects for
this TOGO source record.

The formula is incomplete as source-faithful structured data until the volume,
microgram, and percentage units are preserved or converted correctly and the
source commercial TSA component is restored or decomposed from a directly
verified BBL product specification.

## Findings

| Severity | Finding |
| --- | --- |
| Major | The TOGO `L` and `ug/ml` quantities were imported as `G_PER_L`, making distilled water, hemin, and menadione materially wrong. **Owner:** the TOGO unit-conversion importer and `data/normalized_yaml/bacterial/TOGO_M2274_Chocolate_agar.yaml`. |
| Major | 40 g/L BBL Trypticase soy agar was replaced by an unsupported 45 g/L generic TSB/TSA constituent expansion. **Owner:** the commercial-medium expansion overlay and the TOGO M2274 normalized owner. |
| Minor | The 5% CO2 source atmosphere was downgraded to a variable concentration. **Owner:** the TOGO importer or the schema-defaulter step that supplied the default variable concentration. |

## Recommended Edits

1. Correct the TOGO import of `L` volume units so distilled water is represented
   as a 1 L or 1000 mL liquid volume rather than 1 g/L.
2. Convert hemin and menadione from `ug/ml` to 0.005 g/L and 0.0002 g/L, or
   preserve their original microgram-per-millilitre units if the schema allows.
3. Restore `Trypticase soy agar (BBL)` as the 40 g/L source ingredient unless a
   BBL source document directly supports a component-level expansion.
4. Preserve TOGO's 5% CO2 value on the gas-atmosphere assertion.
5. Regenerate merged YAML from the repaired normalized owner.

## Follow-up Checks

Run the narrow generated-record validators after regeneration:

1. Open LinkML validation against `MediaRecipe`.
2. `scripts/validate_strict.py` on the regenerated record.
3. `linkml-reference-validator validate data` on the regenerated record.
4. `linkml-term-validator validate-data` on the regenerated record.

Then manually compare the regenerated record against TOGO M2274 and confirm
that all six TOGO components are present at the source-supported quantities.

## Additional Notes

None found.
