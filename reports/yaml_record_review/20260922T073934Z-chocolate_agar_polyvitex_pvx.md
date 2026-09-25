# YAML Record Review: Chocolate agar + PolyViteX (PVX)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/chocolate_agar_polyvitex_pvx.yaml
- Started UTC: 2026-09-22T07:38:11Z
- Finished UTC: 2026-09-22T07:39:37Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:008743 |
| Label | Chocolate agar + PolyViteX (PVX) |
| Generated record | data/merge_yaml/merged/chocolate_agar_polyvitex_pvx.yaml |
| Maintained owner | data/normalized_yaml/bacterial/chocolate_agar_polyvitex_pvx.yaml |
| Source | TOGO Medium M2149, NBRC M1503 |

The reviewed file is a generated one-source merge of the NBRC M1503 import via
TOGO M2149. Future fixes belong in
`data/normalized_yaml/bacterial/chocolate_agar_polyvitex_pvx.yaml` or the
TOGO/NBRC unit-conversion importer rather than in
`data/merge_yaml/merged/chocolate_agar_polyvitex_pvx.yaml`.

## Validation

| Check | Result |
| --- | --- |
| Open LinkML validation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe` | Passed |
| `scripts/validate_strict.py` on the generated record | Passed; 0 errors in `/private/tmp/chocolate_agar_polyvitex_pvx.strict.tsv` |
| `linkml-reference-validator validate data` on the generated record | Passed; 0 checks |
| `linkml-term-validator validate-data` on the generated record | Passed |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` objects in a merged YAML file |

The first TOGO and NBRC requests failed on DNS resolution inside the sandbox and
then passed when retried directly. The term validator emitted only the expected
`eutils/pkg_resources is deprecated` warning before passing.

## Identity and Grounding

The source identity is coherent: `CultureMech:008743`, `TOGO:M2149`, NBRC
M1503, and the generated merge fingerprint all denote Chocolate agar +
PolyViteX (PVX).

An ignored-independent `rg --no-ignore --hidden` search across
`data/normalized_yaml` and `data/merge_yaml/merged` for the CultureMech ID,
TOGO M2149 source ID, NBRC M1503 identifiers, normalized owner stem, and merge
fingerprint found this generated record, its maintained owner, and normalized
index entries.

## Evidence

The NBRC M1503 page and TOGO M2149 support the eight weighed or measured medium
constituents imported here: 7.5 g casein peptone, 7.5 g peptone, 1.0 g corn
starch, 5.0 g NaCl, 10.0 g hemoglobin, 4.0 g dipotassium phosphate, 10.0 g
agar, and 10.0 mL PolyViteX, with distilled water to 1.0 L. The source also
states pH 7.3, and its comment states that 5% CO2 incubation is required for
Haemophilus strains.

Most mass ingredients are imported at the supported values, but two liquid
amounts have the wrong unit. `Distilled water` is recorded as `1 G_PER_L`
instead of water to 1.0 L, and `PolyViteX` is recorded as 10 g/L instead of
10 mL/L. The pH 7.3 assertion is absent. CO2 is present only as a defaulted
variable-concentration ingredient even though the inspected source states a 5%
incubation atmosphere for Haemophilus strains.

## Completeness

The empty `target_organisms` and growth-observation fields are not defects for
this NBRC/TOGO source record.

The recipe is incomplete until the 1 L water volume, 10 mL PolyViteX volume, pH
7.3, and 5% CO2 incubation condition are represented with source-faithful units
and scope.

## Findings

| Severity | Finding |
| --- | --- |
| Major | Liquid units are imported as `G_PER_L`: distilled water should make the recipe up to 1.0 L and PolyViteX should be 10 mL/L. **Owner:** the TOGO/NBRC unit-conversion importer and `data/normalized_yaml/bacterial/chocolate_agar_polyvitex_pvx.yaml`. |
| Major | Source pH 7.3 is missing. **Owner:** the TOGO/NBRC importer or normalized owner. |
| Minor | The source 5% CO2 incubation condition is downgraded to a variable CO2 ingredient. **Owner:** the schema defaulter or TOGO/NBRC importer. |

## Recommended Edits

1. Convert the distilled-water and PolyViteX volume rows to source-faithful
   liquid units.
2. Add pH 7.3 from NBRC M1503/TOGO M2149.
3. Replace the default variable CO2 ingredient with a scoped 5% incubation
   atmosphere for Haemophilus strains, or preserve it as a source note if
   strain-specific atmosphere is outside the current recipe model.
4. Regenerate merged YAML after repairing the maintained owner or importer.

## Follow-up Checks

Run the narrow generated-record validators after regeneration:

1. Open LinkML validation against `MediaRecipe`.
2. `scripts/validate_strict.py` on the regenerated record.
3. `linkml-reference-validator validate data` on the regenerated record.
4. `linkml-term-validator validate-data` on the regenerated record.

Then manually compare the regenerated record against NBRC M1503 and TOGO M2149
to confirm all masses, liquid volumes, pH, and the CO2 condition are
source-faithful.

## Additional Notes

None found.
