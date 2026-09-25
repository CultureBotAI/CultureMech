# YAML Record Review: deferrisoma_paleochrorii_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/DEFERRISOMA_PALEOCHRORII_MEDIUM.yaml
- Started UTC: 2026-09-22T14:28:37Z
- Finished UTC: 2026-09-22T14:28:37Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:007641`, label
`deferrisoma_paleochrorii_medium`, original name
`Deferrisoma Paleochrorii Medium`, under `data/merge_yaml/merged/`.

The record is generated from the maintained TOGO mirror:

- `data/normalized_yaml/bacterial/TOGO_M1120_Deferrisoma_Paleochrorii_Medium.yaml`

The same JCM GRMD 1053 source also has a separately maintained, repaired direct
JCM owner:

- `data/normalized_yaml/bacterial/deferrisoma_paleochrorii_medium.yaml`

## Validation

| Check | Result |
| --- | --- |
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/DEFERRISOMA_PALEOCHRORII_MEDIUM.yaml` | Pass |
| `python scripts/validate_strict.py data/merge_yaml/merged/DEFERRISOMA_PALEOCHRORII_MEDIUM.yaml --out /private/tmp/DEFERRISOMA_PALEOCHRORII_MEDIUM.strict.tsv --workers 1 --quiet` | Pass |
| `linkml-reference-validator validate data data/merge_yaml/merged/DEFERRISOMA_PALEOCHRORII_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass; 0 reference checks |
| `linkml-term-validator validate-data data/merge_yaml/merged/DEFERRISOMA_PALEOCHRORII_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass |
| `just validate-history` | Not checked: the documented validator targets standalone files under `history/`; this generated record stores embedded `curation_history`. |

Term validation emitted only the known `eutils` `pkg_resources` deprecation
warning before `Validation passed`.

## Identity and Grounding

TOGO M1120 and JCM GRMD 1053 both identify the source as
`DEFERRISOMA PALEOCHRORII MEDIUM`. The generated TOGO identity is therefore a
real mirror of JCM 1053, but it is stale relative to the repaired direct JCM
owner. The direct JCM record has already restored the eight source-asserted
stock additions as `ML_PER_L` rows, while this TOGO mirror still carries raw
milliliter volumes as `G_PER_L` solution rows with empty compositions.

The exact ignored-file search
`rg --no-ignore --hidden -n "M1120|GRMD=1053|JCM_M1053|Deferrisoma Paleochrorii Medium|deferrisoma_paleochrorii_medium" data/normalized_yaml data/merge_yaml`
covered normalized records, generated merged records, and generated indexes. It
found this TOGO M1120 owner, the repaired direct JCM 1053 owner, this generated
TOGO record, and a generated `GEOTHERMOBACTER_MEDIUM.yaml` cluster that already
contains `deferrisoma_paleochrorii_medium` as a merge source. These JCM 1053
representations need reconciliation.

## Evidence

JCM 1053 supports the first solution as NaCl 15 g, MgCl2 x 6H2O 4 g, KCl
0.33 g, CaCl2 x 2H2O 0.33 g, (NH4)2SO4 0.5 g, FeCl2 solution 1 ml, Trace
element solution 1 ml, Selenite-tungstate solution 0.5 ml, and distilled water
860 ml. After autoclaving under an H2-CO2 4:1 gas mixture, it aseptically and
anaerobically adds 10 ml 3.3% KH2PO4 solution, 10 ml trace vitamins, 10 ml 8%
NaHCO3 solution, 10 ml 20% MES pH 6.0 solution, and 100 ml Iron(III)citrate
solution. The final pH is readjusted to 6.0-6.3 if necessary.

The generated TOGO record loses that structure. The 860 ml water row is
`860 G_PER_L`, every JCM milliliter solution addition is stored as `G_PER_L`,
and the eight solutions have empty `composition` arrays. The record also lacks
the pH 6.0-6.3 range and all JCM preparation text. A variable 1 N HCl solution,
hydrogen gas, and carbon dioxide gas were promoted into top-level ingredients
even though HCl adjusts pH and H2/CO2 is the autoclave atmosphere.

## Completeness

Consequential gaps:

- The TOGO mirror is unrepaired and should be reconciled with the repaired
  direct JCM 1053 owner.
- 860 ml distilled water is represented with a mass-per-liter unit.
- Eight JCM stock additions are represented as `G_PER_L` placeholders instead of
  `ML_PER_L` solution rows with cross-reference provenance.
- The pH 6.0-6.3 range is missing.
- HCl, H2, and CO2 are top-level variable ingredients rather than preparation
  and atmosphere metadata.
- The H2-CO2 4:1 autoclaving step, anaerobic post-autoclave additions, and final
  pH readjustment are missing.

No target-organism or growth-rate rows are supplied by TOGO M1120 or JCM 1053.

## Findings

| Severity | Finding | Evidence | Future owner |
| --- | --- | --- | --- |
| Major | The TOGO M1120 mirror is stale relative to the repaired JCM 1053 owner. | `deferrisoma_paleochrorii_medium.yaml` has a 2026-08-25 `RESTORED_STOCK_SOLUTION_BOUNDARIES` event with eight `ML_PER_L` solution rows; `TOGO_M1120_Deferrisoma_Paleochrorii_Medium.yaml` still has empty `G_PER_L` solution rows. | `data/normalized_yaml/bacterial/TOGO_M1120_Deferrisoma_Paleochrorii_Medium.yaml`; source reconciliation |
| Major | Source volumes use mass units. | JCM 1053 specifies 860 ml water and eight ml stock additions; the generated TOGO record stores them as `G_PER_L`. | TOGO unit normalization |
| Major | Preparation and pH support are lost. | JCM 1053 gives pH 6.0-6.3, H2-CO2 4:1 autoclaving, anaerobic additions, and final pH readjustment; the generated record has no `ph_range` or `preparation_steps`. | TOGO comment importer |
| Major | Atmosphere and pH-adjustment terms leak into `ingredients`. | JCM 1053 uses 1 N HCl only to adjust pH and H2/CO2 as a gas mixture for autoclaving; generated output stores HCl, carbon dioxide gas, and hydrogen gas as variable final-medium ingredients. | TOGO prose importer |
| Major | The JCM 1053 duplicate set remains fragmented. | The exhaustive ignored search found the repaired direct JCM 1053 owner separately from TOGO M1120, and the direct owner is already merged into `GEOTHERMOBACTER_MEDIUM.yaml`. | duplicate merge and JCM/TOGO reconciliation |

## Recommended Edits

- Reconcile `TOGO_M1120_Deferrisoma_Paleochrorii_Medium.yaml` with the repaired
  direct `deferrisoma_paleochrorii_medium.yaml` owner and keep JCM 1053 in one
  canonical generated cluster.
- Convert the 860 ml water row and all JCM solution additions to `ML_PER_L`
  rather than `G_PER_L`.
- Preserve JCM cross-references to the FeCl2, trace-element, selenite-tungstate,
  trace-vitamin, and iron(III) citrate solutions.
- Add pH 6.0-6.3 and preparation steps for 1 N HCl pH adjustment, H2-CO2
  autoclaving, anaerobic post-autoclave solution additions, and final pH
  readjustment.
- Move HCl, hydrogen, and carbon dioxide out of top-level ingredients.
- Regenerate merged YAML after the maintained TOGO owner and duplicate mapping
  are repaired.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the regenerated JCM
  1053/TOGO M1120 record.
- Search ignored files for `M1120`, `GRMD=1053`, `JCM_M1053`, and
  `deferrisoma_paleochrorii_medium` to confirm only the intended canonical JCM
  1053 cluster remains.
- Manually compare the regenerated stock volumes, pH, and preparation metadata
  against JCM GRMD 1053.

## Additional Notes

- The exact stale-duplicate search included ignored and hidden files.
- `linkml-reference-validator` reported zero reference checks, so its pass does
  not exercise TOGO, JCM, or MediaDive source identifiers.
