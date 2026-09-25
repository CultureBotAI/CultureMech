# YAML Record Review: PFENNIG THERMODESULFOBIUM MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/pfennig_thermodesulfobium_medium.yaml
- Started UTC: 2026-09-24T20:46:11Z
- Finished UTC: 2026-09-24T20:46:11Z
- Verdict: pass with minor issues

## Target

| Field | Value |
| --- | --- |
| Record path | `data/merge_yaml/merged/pfennig_thermodesulfobium_medium.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/JCM_J1395_PFENNIG_THERMODESULFOBIUM_MEDIUM.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:015852` |
| Name | `pfennig_thermodesulfobium_medium` |
| Original name | `PFENNIG THERMODESULFOBIUM MEDIUM` |
| Media term | `jcm.grmd:1395` |
| Generated status | Generated merge output from `data/normalized_yaml/bacterial/JCM_J1395_PFENNIG_THERMODESULFOBIUM_MEDIUM.yaml` |

The target resolves to the direct JCM GRMD 1395 import. An ignored-inclusive
search over `data`, `src`, and `scripts` for `J1395`, `GRMD=1395`,
`jcm.grmd:1395`, `CultureMech:015852`, and
`PFENNIG_THERMODESULFOBIUM` found only this maintained owner and this generated
merged YAML output.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/pfennig_thermodesulfobium_medium.yaml` | Passed; no issues found. |
| Strict repository validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/pfennig_thermodesulfobium_medium.yaml --out /private/tmp/pfennig_thermodesulfobium_medium.strict.tsv --workers 1 --quiet` | Passed; the TSV had only its header line, so 0 errors. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/pfennig_thermodesulfobium_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/pfennig_thermodesulfobium_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not run. | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in one generated YAML file. |

## Identity and Grounding

The record's identity is correct. Live JCM GRMD 1395 is PFENNIG
THERMODESULFOBIUM MEDIUM, and the local `jcm.grmd:1395` media term matches that
source.

The defined medium and defined composition classifications are supported by the
JCM formulation. The source uses salts, defined stock-solution aliquots,
resazurin, sodium thiosulfate, sulfide, trace elements, and trace vitamins, with
no undefined complex nutrient.

The checked CHEBI groundings for the six simple salts, resazurin, and water are
compatible with the JCM labels. The JCM cross-referenced stock additions are
captured as aliquots by name but are not explicitly linked to `jcm.grmd:899` or
`jcm.grmd:197`.

## Evidence

JCM 1395 supports the top-level ingredients and concentrations: 0.33 g/L each
of NH4Cl, KH2PO4, KCl, CaCl2 x 2 H2O, and MgCl2 x 6 H2O; 2.0 g/L Na2SO4; 1.0
ml/L Trace element solution from Medium No. 899; 1.0 mg/L resazurin; and 1.0 L
distilled water.

JCM also supports the post-autoclave additions: 10.0 ml/L Trace vitamins from
Medium No. 197, 10.0 ml/L 1.0 M sodium thiosulfate solution, and 10.0 ml/L 5%
Na2S x 9 H2O solution.

The preparation text is preserved in substance: mix and adjust to pH 6.0,
dispense under an N2-CO2 80:20 gas mixture, seal and autoclave, replace the gas
phase with H2-CO2 70:30 at 50 KPa overpressure, aseptically and anaerobically
add the post-autoclave solutions, and readjust to pH 6.0-6.2 if necessary.

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
| Minor | Distilled water has the wrong unit. | JCM 1395 lists 1.0 L distilled water, while the generated row says `1.0 ML_PER_L`. | `data/normalized_yaml/bacterial/JCM_J1395_PFENNIG_THERMODESULFOBIUM_MEDIUM.yaml` |
| Minor | Referenced JCM stock media are captured only in text. | The source explicitly points Trace element solution to Medium No. 899 and Trace vitamins to Medium No. 197; the record preserves those phrases but does not link `jcm.grmd:899` or `jcm.grmd:197`. | `data/normalized_yaml/bacterial/JCM_J1395_PFENNIG_THERMODESULFOBIUM_MEDIUM.yaml` |

## Recommended Edits

1. Change the distilled water row to represent the source's 1.0 L volume rather
   than `1.0 ML_PER_L`.
2. Add explicit source references or solution links for JCM Medium 899 and JCM
   Medium 197 if the schema can represent cross-referenced stock media.

## Follow-up Checks

1. Regenerate the merged YAML and rerun the open schema, strict, reference, and
   term validators on the regenerated JCM 1395 output.
2. Manually compare the regenerated record against live JCM GRMD 1395 and
   verify that water, stock aliquots, pH values, and gas handling instructions
   still match.

## Additional Notes

None found.
