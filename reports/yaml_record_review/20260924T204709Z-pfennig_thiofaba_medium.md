# YAML Record Review: PFENNIG THIOFABA MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/pfennig_thiofaba_medium.yaml
- Started UTC: 2026-09-24T20:47:09Z
- Finished UTC: 2026-09-24T20:47:09Z
- Verdict: pass with minor issues

## Target

| Field | Value |
| --- | --- |
| Record path | `data/merge_yaml/merged/pfennig_thiofaba_medium.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/JCM_J1393_PFENNIG_THIOFABA_MEDIUM.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:015851` |
| Name | `pfennig_thiofaba_medium` |
| Original name | `PFENNIG THIOFABA MEDIUM` |
| Media term | `jcm.grmd:1393` |
| Generated status | Generated merge output from `data/normalized_yaml/bacterial/JCM_J1393_PFENNIG_THIOFABA_MEDIUM.yaml` |

The target resolves to the direct JCM GRMD 1393 import. An ignored-inclusive
search over `data`, `src`, and `scripts` for `J1393`, `GRMD=1393`,
`jcm.grmd:1393`, `CultureMech:015851`, and `PFENNIG_THIOFABA` found only this
maintained owner and this generated merged YAML output.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/pfennig_thiofaba_medium.yaml` | Passed; no issues found. |
| Strict repository validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/pfennig_thiofaba_medium.yaml --out /private/tmp/pfennig_thiofaba_medium.strict.tsv --workers 1 --quiet` | Passed; the TSV had only its header line, so 0 errors. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/pfennig_thiofaba_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/pfennig_thiofaba_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not run. | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in one generated YAML file. |

## Identity and Grounding

The record's identity is correct. Live JCM GRMD 1393 is PFENNIG THIOFABA
MEDIUM, and the local `jcm.grmd:1393` media term matches that source.

The defined medium and defined composition classifications are supported by the
JCM formulation. The source uses salts, defined stock-solution aliquots, sodium
thiosulfate pentahydrate, sulfide, trace elements, and trace vitamins, with no
undefined complex nutrient.

The checked CHEBI groundings for the seven simple salts and water are
compatible with the JCM labels. The JCM cross-referenced stock additions are
captured as aliquots by name but are not explicitly linked to `jcm.grmd:899` or
`jcm.grmd:197`.

## Evidence

JCM 1393 supports the top-level ingredients and concentrations: 0.33 g/L each
of NH4Cl, KH2PO4, KCl, CaCl2 x 2 H2O, and MgCl2 x 6 H2O; 2.0 g/L Na2SO4;
2.0 g/L Na2S2O3 x 5 H2O; 1.0 ml/L Trace element solution from Medium No. 899;
10.0 ml/L Trace vitamins from Medium No. 197; and 1.0 L distilled water.

JCM also supports the preparation text: mix and adjust to pH 4.5, dispense into
culture vessels, seal and autoclave, replace the gas phase with O2-CO2 10:90 at
50 KPa overpressure, add 12.0 ml/L 5% Na2S x 9 H2O solution stored under N2,
and readjust to pH 4.3-4.5 if necessary.

## Completeness

The only source amount mismatch found is the water row: JCM lists 1.0 L
distilled water, but the generated record stores `value: 1.0` with
`unit: ML_PER_L`.

The two JCM cross-reference targets, Medium No. 899 and Medium No. 197, are
not modeled as explicit source CURIEs on the two referenced stock additions.

No empty optional field was material to this review.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Minor | Distilled water has the wrong unit. | JCM 1393 lists 1.0 L distilled water, while the generated row says `1.0 ML_PER_L`. | `data/normalized_yaml/bacterial/JCM_J1393_PFENNIG_THIOFABA_MEDIUM.yaml` |
| Minor | Referenced JCM stock media are captured only in text. | The source explicitly points Trace element solution to Medium No. 899 and Trace vitamins to Medium No. 197; the record preserves those phrases but does not link `jcm.grmd:899` or `jcm.grmd:197`. | `data/normalized_yaml/bacterial/JCM_J1393_PFENNIG_THIOFABA_MEDIUM.yaml` |

## Recommended Edits

1. Change the distilled water row to represent the source's 1.0 L volume rather
   than `1.0 ML_PER_L`.
2. Add explicit source references or solution links for JCM Medium 899 and JCM
   Medium 197 if the schema can represent cross-referenced stock media.

## Follow-up Checks

1. Regenerate the merged YAML and rerun the open schema, strict, reference, and
   term validators on the regenerated JCM 1393 output.
2. Manually compare the regenerated record against live JCM GRMD 1393 and
   verify that water, stock aliquots, pH values, gas handling, and sulfide
   addition instructions still match.

## Additional Notes

None found.
