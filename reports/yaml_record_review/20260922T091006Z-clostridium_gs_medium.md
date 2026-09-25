# YAML Record Review: clostridium_gs_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/clostridium_gs_medium.yaml
- Started UTC: 2026-09-22T09:08:00Z
- Finished UTC: 2026-09-22T09:10:06Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/clostridium_gs_medium.yaml`, a generated `MediaRecipe` for `CultureMech:001354` / `clostridium_gs_medium`.

The record is a generated merge of four maintained source duplicates: `data/normalized_yaml/bacterial/clostridium_gs_medium.yaml`, `KOMODO_255_GS_medium.yaml`, `medium_255_modified_for_dsm_14427.yaml`, and `medium_255_modified_for_dsm_8532.yaml`. Its merge fingerprint is `a95122e6dde67d17873f3f53ac3c4ccf1c5efa72f88541a4823debb92b4a4d37`.

The retained source identity is `mediadive.medium:255`, DSMZ Medium 255, labelled `CLOSTRIDIUM (GS) MEDIUM`.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/clostridium_gs_medium.yaml` | Pass |
| `python scripts/validate_strict.py data/merge_yaml/merged/clostridium_gs_medium.yaml --out /private/tmp/clostridium_gs_medium.strict.tsv --workers 1 --quiet` | Pass; TSV contained only the header row |
| `linkml-reference-validator validate data data/merge_yaml/merged/clostridium_gs_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass; 0 reference checks |
| `linkml-term-validator validate-data data/merge_yaml/merged/clostridium_gs_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass; emitted only the expected NCBI E-utilities deprecation warning |
| Embedded curation-history validation | Not checked: the documented `just validate-history` target validates standalone `history/` records, not embedded `MediaRecipe.curation_history` nodes in generated YAML |

`just` wrapper validators were not used because the project environment attempts to build `llvmlite==0.46.0` under Python 3.13 and fails inside setuptools. The equivalent focused LinkML, strict, reference, and term validators were run under `/usr/local/bin/python3.11` with offline cached packages.

## Identity and Grounding

The record identity matches DSMZ Medium 255. The downloaded `DSMZ_Medium255.pdf` identifies Medium 255 as `CLOSTRIDIUM (GS) MEDIUM`, with the same parent formula and 100% N2 anaerobic preparation.

The generated merge correctly collapsed four identical DSMZ/KOMODO source copies into one generated record, including the generic KOMODO 255 record and two KOMODO records labelled as Medium 255 modified for DSM 14427 and DSM 8532.

Two identity-level issues remain:

- `K2HPO4 x 3 H2O` is grounded to generic dipotassium hydrogen phosphate, losing the trihydrate named by DSMZ.
- `TOGO:M2741`, another import of the same DSMZ PDF, is still a separate generated recipe at `data/merge_yaml/merged/clostridium_gs_medium__51cf6d40.yaml`.

An ignored-inclusive search of `data/normalized_yaml`, `data/merge_yaml/merged`, `data/import_tracking`, and `reports` for `CultureMech:001354`, `mediadive.medium:255`, `DSMZ Medium 255`, `komodo.medium:255`, `komodo.medium:255_14427`, `komodo.medium:255_8532`, the merge fingerprint, `clostridium_gs_medium.yaml`, and the exact DSMZ label found the intended four merged owners and no fifth owner in that exact DSMZ/KOMODO source set. A second ignored-inclusive search for `DSMZ_Medium255`, `TOGO:M2741`, and `TOGO_M2741_Clostridium_GS_Medium` found the unmerged TOGO branch for the same DSMZ PDF.

## Evidence

The DSMZ PDF supports the presence of KH2PO4, K2HPO4 x 3 H2O, urea, MgCl2 x 6 H2O, CaCl2 x 2 H2O, the FeSO4 x 7 H2O acid stock, morpholinopropane sulfonic acid, sodium resazurin stock, yeast extract, L-Cysteine HCl x H2O, cellobiose, and 1000 ml distilled water.

The generated record preserves the pH 7.2 and the key anaerobic procedure: sparging with 100% N2 for 30-45 min, adding cysteine before autoclaving, dispensing under the same gas, and adding filtered anoxic cellobiose stock before inoculation.

MediaDive has normalized DSMZ's displayed one-liter masses by an inferred 1001.75 ml volume, so rows listed as 0.50 g, 1.00 g, 2.00 g, 10.00 g, 6.00 g, 1.00 g, and 5.00 g in the PDF appear as 0.499002, 0.998004, 1.99601, 9.98004, 5.98802, 0.998004, and 4.99002 `G_PER_L`. The same small dilution is applied to the 1.25 ml FeSO4 stock and 0.50 ml resazurin stock calculations.

## Completeness

The generated record is mostly complete for the base DSMZ 255 formula and preparation; no stock boundary is being flattened as a full one-liter stock.

Consequential gaps are limited to the missing distilled-water row, the small inferred-volume rescaling away from DSMZ's printed per-liter quantities, the K2HPO4 trihydrate grounding, and the separate TOGO M2741 representation.

The DSMZ PDF also lists three strain-specific modifications: replace cellobiose with D-glucose for DSM 2360, DSM 103556, and DSM 111537; use 1% cellobiose for DSM 29353; and add a cellulose lens-cleaning tissue strip for DSM 101079. Empty variant fields in this base record are acceptable because those modifications are variants that should be modeled separately.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | `K2HPO4 x 3 H2O` is grounded to generic dipotassium hydrogen phosphate instead of an exact trihydrate term or an unresolved exact hydrate. | `data/normalized_yaml/bacterial/clostridium_gs_medium.yaml` and the KOMODO 255 duplicate owners |
| Major | TOGO M2741 points to the same DSMZ Medium 255 PDF but was not merged with the direct DSMZ/KOMODO duplicate group. | MediaDive/TOGO merge logic; owner `data/normalized_yaml/bacterial/TOGO_M2741_Clostridium_GS_Medium.yaml` |
| Minor | DSMZ's printed masses were divided by an inferred 1001.75 ml volume, producing values like 0.499002 g/L for a 0.50 g row. That should either be documented as deliberate final-volume normalization or regenerated to preserve the source's displayed one-liter recipe. | MediaDive import arithmetic for `data/normalized_yaml/bacterial/clostridium_gs_medium.yaml` |
| Minor | The generated canonical DSMZ record has `parent_media` pointing at a source-duplicate KOMODO owner, which makes the duplicate relationship look like a biological parent/child relationship. | `data/normalized_yaml/bacterial/clostridium_gs_medium.yaml` and merge metadata generation |

No blocker findings were found. The base DSMZ formula and 100% N2 anaerobic preparation are recoverable and the exact duplicate merge among the direct DSMZ and KOMODO records is largely correct.

## Recommended Edits

1. Replace the K2HPO4 x 3 H2O grounding with an exact trihydrate term if one exists; otherwise leave the exact label ungrounded with a quality note.
2. Deduplicate TOGO M2741 into the DSMZ/KOMODO 255 merge group so the DSMZ PDF publishes as one base record.
3. Decide whether MediaDive imports should preserve DSMZ displayed masses or normalize by small stock volumes; then document or regenerate the affected 1001.75 ml arithmetic consistently.
4. Remove `parent_media`/variant metadata from source-duplicate merge products unless a true formulation parent is being asserted.

## Follow-up Checks

- Rerun the focused schema, strict, term, and reference validators on the edited DSMZ and KOMODO 255 owners.
- Regenerate the GS merge and verify the four current source duplicates plus TOGO M2741 publish under one generated DSMZ Medium 255 record.
- Manually compare the regenerated record against `DSMZ_Medium255.pdf`, including the two milliliter stock additions and the strain-specific variant notes.

## Additional Notes

The DSMZ PDF extracted cleanly with `mutool draw -F txt` from `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium255.pdf`.
