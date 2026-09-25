# YAML Record Review: clostridium_aminovalericum_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/clostridium_aminovalericum_medium.yaml
- Started UTC: 2026-09-22T09:05:00Z
- Finished UTC: 2026-09-22T09:07:34Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/clostridium_aminovalericum_medium.yaml`, a generated `MediaRecipe` for `CultureMech:005889` / `clostridium_aminovalericum_medium`.

The record is generated from the single maintained source `data/normalized_yaml/bacterial/clostridium_aminovalericum_medium.yaml` with merge fingerprint `8587eb46259efc852f57896ab64318073457e226175d8a15cb1d2e315a2fde08`.

The retained source identity is KOMODO ModelSEED medium 526, while the ingredients were copied from DSMZ/MediaDive Medium 526.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/clostridium_aminovalericum_medium.yaml` | Pass |
| `python scripts/validate_strict.py data/merge_yaml/merged/clostridium_aminovalericum_medium.yaml --out /private/tmp/clostridium_aminovalericum_medium.strict.tsv --workers 1 --quiet` | Pass; TSV contained only the header row |
| `linkml-reference-validator validate data data/merge_yaml/merged/clostridium_aminovalericum_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass; 0 reference checks |
| `linkml-term-validator validate-data data/merge_yaml/merged/clostridium_aminovalericum_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass; emitted only the expected NCBI E-utilities deprecation warning |
| Embedded curation-history validation | Not checked: the documented `just validate-history` target validates standalone `history/` records, not embedded `MediaRecipe.curation_history` nodes in generated YAML |

`just` wrapper validators were not used because the project environment attempts to build `llvmlite==0.46.0` under Python 3.13 and fails inside setuptools. The equivalent focused LinkML, strict, reference, and term validators were run under `/usr/local/bin/python3.11` with offline cached packages.

## Identity and Grounding

The generated record is source-mixed. It is labelled as `komodo.medium:526` / `CLOSTRIDIUM AMINOVALERICUM medium`, but its history says `dsmz-resolver-v1.0` copied ingredients from DSMZ Medium 526. DSMZ Medium 526 is represented locally by `data/normalized_yaml/bacterial/clostridium_viride_medium.yaml` as `CultureMech:001657` / `mediadive.medium:526` / `CLOSTRIDIUM VIRIDE MEDIUM`.

An ignored-inclusive search of `data/normalized_yaml`, `data/merge_yaml/merged`, `data/import_tracking`, and `reports` for `CultureMech:005889`, `komodo.medium:526`, `KOMODO Medium 526`, `DSMZ Medium: 526`, `mediadive.medium:526`, the merge fingerprint, `clostridium_aminovalericum_medium.yaml`, and the exact KOMODO label found only one KOMODO owner but also found the direct DSMZ 526 Clostridium viride owner. The two sources are not merged because the KOMODO-enriched record has an extra variable `Na2CO3` ingredient.

Most source chemical groundings match their labels, but `NiCl2 x 6 H2O` is grounded to generic nickel dichloride (`CHEBI:34887`), losing the hexahydrate form specified by the DSMZ PDF.

## Evidence

The fetched DSMZ Medium 526 PDF supports the parent formula for 5-aminovaleric acid, K2HPO4, yeast extract, 0.5 ml of 0.1% w/v sodium resazurin, NaHCO3, L-Cysteine HCl x H2O, and 1000 ml distilled water.

The same PDF does not support the final 11 trace salts as top-level parent ingredients. It defines `Trace elements solution VR` as a separate one-liter stock containing NTA, MgSO4 x 7 H2O, CaCl2 x 2 H2O, FeSO4 x 7 H2O, NiCl2 x 6 H2O, ZnSO4 x 7 H2O, MnSO4 x H2O, CoCl2 x 6 H2O, VOSO4 x 5 H2O, Na2MoO4 x 2 H2O, and CuSO4 x 5 H2O, then uses only 4 ml of that stock per parent liter.

The DSMZ direct owner contains two preparation steps copied from that PDF: anaerobic sparging with an 80% N2 / 20% CO2 gas mixture, bicarbonate/cysteine addition, Hungate or serum-vial dispensing, autoclaving, final pH adjustment to 7.6-7.8 with sterile anoxic 5% Na2CO3, and the separate Trace elements solution VR preparation. The reviewed KOMODO owner copied the ingredient list but lost both preparation steps.

## Completeness

The generated record has the supported pH range and the major substrate masses, and it correctly normalizes 0.5 ml of a 0.1% sodium resazurin stock to 0.0005 g/L.

It is materially incomplete for actual use:

- `Trace elements solution VR` is flattened into parent ingredients at full stock strength instead of being represented as a 4 ml stock addition.
- DSMZ's 1000 ml distilled-water row is missing.
- The anaerobic preparation, autoclaving sequence, 80% N2 / 20% CO2 atmosphere, and Trace elements solution VR preparation steps are missing.
- `Na2CO3` was converted from a sterile anoxic pH-adjustment stock into a variable top-level ingredient.
- The notes field says `Aerobic: Yes`, contradicting DSMZ's anoxic preparation.

Empty target-organism, storage, salinity, and light fields are acceptable for the inspected DSMZ PDF. The PDF names the recipe but does not name a strain or those additional conditions.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | `Trace elements solution VR` was flattened into the parent at full one-liter stock concentrations; DSMZ Medium 526 adds only 4 ml of that stock per liter of parent medium. | `data/normalized_yaml/bacterial/clostridium_aminovalericum_medium.yaml`; upstream DSMZ copy/enrichment logic likely copied the already-flattened `clostridium_viride_medium.yaml` owner |
| Major | DSMZ preparation steps were not copied with the DSMZ ingredients, so the KOMODO owner lacks the 80% N2 / 20% CO2 sparging, bicarbonate/cysteine addition, Hungate or serum-vial dispensing, autoclaving, final Na2CO3 pH adjustment, and trace-solution preparation details. | `data/normalized_yaml/bacterial/clostridium_aminovalericum_medium.yaml` |
| Major | `Na2CO3` was extracted as a variable-concentration top-level ingredient even though DSMZ uses sterile anoxic 5% w/v Na2CO3 only to adjust the final pH after autoclaving. | `data/normalized_yaml/bacterial/clostridium_aminovalericum_medium.yaml` |
| Major | The record advertises `Aerobic: Yes` in `notes` while the copied DSMZ 526 preparation is explicitly anaerobic/anoxic. | `data/normalized_yaml/bacterial/clostridium_aminovalericum_medium.yaml` |
| Major | The source identity is unresolved: KOMODO 526 has a Clostridium aminovalericum label, but the imported DSMZ 526 recipe is the local DSMZ Clostridium viride medium and remains a separate generated record. | KOMODO to DSMZ resolver and merge logic for `komodo.medium:526` and `mediadive.medium:526` |
| Minor | `NiCl2 x 6 H2O` is grounded to generic nickel dichloride rather than an exact nickel chloride hexahydrate term or an explicit unresolved hydrate. | `data/normalized_yaml/bacterial/clostridium_aminovalericum_medium.yaml` and `data/normalized_yaml/bacterial/clostridium_viride_medium.yaml` |

No blocker findings were found. The YAML is valid and the ingredient list is traceable to the named DSMZ 526 formula even though the stock boundary, preparation details, and source identity need curation.

## Recommended Edits

1. Model `Trace elements solution VR` as a nested 4 ml stock addition and stop publishing its one-liter stock ingredients as parent-medium concentrations.
2. Copy or link the DSMZ 526 preparation steps when copying the DSMZ 526 ingredient block into the KOMODO 526 owner.
3. Remove `Na2CO3` as a variable ingredient and represent it only in the final pH-adjustment step.
4. Correct the `Aerobic: Yes` note to reflect the DSMZ anoxic preparation or remove the unsupported KOMODO aerobic flag.
5. Resolve whether KOMODO 526 should be a variant of, alias of, or separate record from DSMZ/MediaDive 526; then make source identity and generated merging match that decision.
6. Replace the NiCl2 x 6 H2O grounding with an exact hexahydrate term if available, or leave the exact ingredient label ungrounded with a quality note.

## Follow-up Checks

- Rerun the focused schema, strict, term, and reference validators on the maintained KOMODO owner and any new Trace elements solution VR owner.
- Regenerate the merged records and verify that DSMZ 526 stock ingredients no longer appear as parent-level ingredients in the KOMODO 526 output.
- Inspect an ignored-inclusive exact search for `komodo.medium:526`, `mediadive.medium:526`, `DSMZ_Medium526.pdf`, and both Clostridium labels to verify the intended identity or variant relationship is represented once.
- Manually compare the regenerated parent recipe and trace stock against the DSMZ Medium 526 PDF.

## Additional Notes

The downloaded DSMZ PDF extracted cleanly with `mutool draw -F txt` from `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium526.pdf`.
