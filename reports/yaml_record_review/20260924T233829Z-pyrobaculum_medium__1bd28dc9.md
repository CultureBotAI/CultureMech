# YAML Record Review: pyrobaculum_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/pyrobaculum_medium__1bd28dc9.yaml
- Started UTC: 2026-09-24T23:36:57Z
- Finished UTC: 2026-09-24T23:38:30Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/pyrobaculum_medium__1bd28dc9.yaml` as a generated `MediaRecipe` for `CultureMech:008346`, label `pyrobaculum_medium`, with `media_term` `TOGO:M177`.

The only normalized input is `data/normalized_yaml/archaea/TOGO_M177_Pyrobaculum_Medium.yaml`; the reviewed file is generated output and should be regenerated after that maintained TOGO owner is fixed.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/pyrobaculum_medium__1bd28dc9.yaml` | Passed; printed `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/pyrobaculum_medium__1bd28dc9.yaml --out /private/tmp/pyrobaculum_medium__1bd28dc9.strict.tsv --workers 1 --quiet` | Passed; 1 TSV line, header only, 0 error rows. |
| Internal references | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/pyrobaculum_medium__1bd28dc9.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks were configured for this record. |
| Term grounding | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/pyrobaculum_medium__1bd28dc9.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils/pkg_resources` warning. |
| Embedded history | `just validate-history` | Not checked: the available validator covers standalone `history/`, not embedded `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

TOGO M177 and JCM Medium 184 both identify `Pyrobaculum Medium`; the reviewed record denotes the right named medium and the correct source page. Its pH, submedium expansion, and direct-JCM deduplication are incomplete.

An ignored-file-inclusive exact search across `data/normalized_yaml`, `data/merge_yaml/merged`, and `reports/yaml_record_review` for `CultureMech:008346`, `TOGO:M177` with a numeric boundary, `togomedium.org/medium/M177` with a numeric boundary, `JCM_M184`, `GRMD=184`, `JCM_J184_PYROBACULUM_MEDIUM`, and the full `1bd28dc9fee776059f4685bd237ff83aca02a2fb76225ddf86d8a4a6d4c8c693` fingerprint found the maintained TOGO owner, the reviewed generated TOGO artifact, the direct JCM J184 normalized owner, and `data/merge_yaml/merged/PYROBACULUM_MEDIUM.yaml`, which already contains the direct JCM import.

TOGO M156 is the TOGO copy of JCM Medium 165, `SULFOLOBUS MEDIUM`. The live TOGO M156 payload and live JCM 165 page both define the `Modified Brock's salt base solution` referenced by JCM 184.

## Evidence

The live TOGO M177 payload and live JCM 184 page support the same top-level ingredient list: 1 L Modified Brock's salt base, 0.5 g Bacto peptone, 0.2 g yeast extract, 20 g sulfur powder, 0.5 g `Na2S x 9H2O`, and 1 mg resazurin. The reviewed record carries the peptone, yeast extract, sulfur, and sulfide gram amounts correctly, but records resazurin as `1 G_PER_L` instead of `0.001 G_PER_L`.

TOGO M177 represents the Modified Brock's salt base as `reference_media_id: M156`; JCM 184 links the same salt base through JCM Medium 165. Those sources support expansion through the M156/M165 salt-base composition: distilled water, `(NH4)2SO4`, `KH2PO4`, `MgSO4 x 7H2O`, `CaCl2 x 2H2O`, `FeCl3 x 6H2O`, `MnCl2 x 4H2O`, `Na2B4O7 x 10H2O`, `ZnSO4 x 7H2O`, `CuCl2 x 2H2O`, `Na2MoO4 x 2H2O`, `VOSO4 x nH2O`, and `CoSO4 x 7H2O`. The generated record instead has an empty `solutions` entry with a non-concentration placeholder of `1 G_PER_L`.

TOGO M177 also carries the JCM 184 preparation text: mix all ingredients except yeast extract, peptone, sulfur, and sodium sulfide; autoclave under N2; separately autoclave yeast extract, peptone, and sodium sulfide as anoxic stock solutions; steam sulfur for 3 hr on each of 3 successive days; add the sterile stocks and sulfur aseptically and anaerobically; then adjust to pH 5.5 with sterile 1 N sulfuric acid before inoculation. The reviewed YAML has no `ph_value` and no `preparation_steps`.

## Completeness

Empty optional fields are not defects.

Consequential omissions:

- `ph_value: 5.5` is missing.
- The referenced Modified Brock's salt base is present only as an empty solution shell.
- The main JCM/TOGO preparation instructions are absent.
- The record is not linked to the direct JCM J184 normalized record even though TOGO M177 cites exactly that JCM source.

The ignored-file-inclusive exact search described above found no duplicate TOGO M177 normalized owner and no newer generated artifact for fingerprint `1bd28dc9fee776059f4685bd237ff83aca02a2fb76225ddf86d8a4a6d4c8c693`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Resazurin is inflated 1000-fold. | TOGO M177 and JCM 184 specify 1 mg per liter; the generated TOGO import records `value: '1'`, `unit: G_PER_L`. The direct JCM J184 owner correctly uses `0.001 G_PER_L`. | `data/normalized_yaml/archaea/TOGO_M177_Pyrobaculum_Medium.yaml` |
| Major | The Modified Brock's salt base cross-reference is unresolved. | TOGO M177 points to TOGO M156 and JCM 184 points to JCM 165 for this 1 L salt-base solution. The YAML keeps `Modified Brock's salt base solution` as `composition: []` with `1 G_PER_L`, so water and 12 salts from the referenced base are absent. | `data/normalized_yaml/archaea/TOGO_M177_Pyrobaculum_Medium.yaml` |
| Major | pH and anaerobic/staged preparation are missing. | JCM 184/TOGO M177 require N2 autoclaving, separate anoxic stock autoclaving, sulfur steaming, aseptic anaerobic additions, and final adjustment to pH 5.5 with sterile 1 N sulfuric acid. The YAML has no `ph_value` and no `preparation_steps`. | `data/normalized_yaml/archaea/TOGO_M177_Pyrobaculum_Medium.yaml` |
| Major | The same JCM 184 source is stranded in two generated records. | The TOGO owner cites JCM M184, while `data/normalized_yaml/archaea/JCM_J184_PYROBACULUM_MEDIUM.yaml` is a direct import of the same JCM source and has the expanded base, pH, and preparation details. The merge did not link them because the TOGO record has an empty base solution and a wrong resazurin concentration. | `data/normalized_yaml/archaea/TOGO_M177_Pyrobaculum_Medium.yaml`; `data/normalized_yaml/archaea/JCM_J184_PYROBACULUM_MEDIUM.yaml`; merge regeneration |
| Minor | Sulfur still carries a legacy MediaIngredientMech identifier. | `Sulfur (powder)` has a primary CHEBI grounding to `CHEBI:33403`, but the ingredient keeps `mediaingredientmech_term: MediaIngredientMech:001072` instead of using the CHEBI-keyed `mediaingredientmech_chebi_term` slot. | `data/normalized_yaml/archaea/TOGO_M177_Pyrobaculum_Medium.yaml` |

## Recommended Edits

1. In `data/normalized_yaml/archaea/TOGO_M177_Pyrobaculum_Medium.yaml`, convert the 1 mg resazurin row to `0.001 G_PER_L`.

2. Expand `Modified Brock's salt base solution` from TOGO M156/JCM 165 into the maintained TOGO owner, preserving its 1 L water row and 12 salt rows at the source concentrations.

3. Add `ph_value: 5.5` and copy the JCM 184 anaerobic preparation into `preparation_steps`, including the separate yeast extract, peptone, sodium sulfide, and sulfur sterilization instructions.

4. Refresh sulfur's MediaIngredientMech link to the CHEBI-keyed slot after the primary `CHEBI:33403` grounding.

5. Regenerate `data/merge_yaml/merged` and verify that TOGO M177 reconciles with the direct JCM J184 owner. Keep the JCM J309 `pyrobaculum_arsenaticum_medium` record out of any source-duplicate merge because JCM 309 is a pH 6.8 variant of JCM 184 without sulfur and with thiosulfate supplementation.

## Follow-up Checks

- Re-run the focused schema, strict, reference, and term validators on the repaired TOGO owner and regenerated merged YAML.
- Re-run an ignored-file-inclusive exact search for `TOGO:M177`, `JCM_M184`, `GRMD=184`, `mediadive.medium:J184`, and `mediadive.medium:J309` to confirm the repaired TOGO owner reconciles with JCM 184 without collapsing JCM 309.
- Manually compare the regenerated YAML against live TOGO M177, live TOGO M156, JCM Medium 184, and JCM Medium 165 to confirm resazurin, the Modified Brock's salt base, pH 5.5, and the preparation text survived.

## Additional Notes

The live JCM 184 page links Modified Brock's salt base through JCM Medium 165, while TOGO M177 stores `reference_media_id: M156`; live TOGO M156 maps back to JCM M165. That identifier mismatch is not itself a formulation conflict.
