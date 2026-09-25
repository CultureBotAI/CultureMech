# YAML Record Review: clostridial_growth_medium_cgm

- Repository: CultureMech
- Record: data/merge_yaml/merged/clostridial_growth_medium_cgm.yaml
- Started UTC: 2026-09-22T08:54:00Z
- Finished UTC: 2026-09-22T08:59:13Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/clostridial_growth_medium_cgm.yaml`, a generated `MediaRecipe` for `CultureMech:009327` / `clostridial_growth_medium_cgm`.

The record is generated from the single maintained source `data/normalized_yaml/bacterial/clostridial_growth_medium_cgm.yaml` with merge fingerprint `66d02591439a02df2e6b046ecb3bab9630977b744523c51e68c85db278734151`.

The source identity is `TOGO:M2779`, labelled `Clostridial Growth Medium (CGM)`.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/clostridial_growth_medium_cgm.yaml` | Pass |
| `python scripts/validate_strict.py data/merge_yaml/merged/clostridial_growth_medium_cgm.yaml --out /private/tmp/clostridial_growth_medium_cgm.strict.tsv --workers 1 --quiet` | Pass; TSV contained only the header row |
| `linkml-reference-validator validate data data/merge_yaml/merged/clostridial_growth_medium_cgm.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass; 0 reference checks |
| `linkml-term-validator validate-data data/merge_yaml/merged/clostridial_growth_medium_cgm.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass; emitted only the expected NCBI E-utilities deprecation warning |
| Embedded curation-history validation | Not checked: the documented `just validate-history` target validates standalone `history/` records, not embedded `MediaRecipe.curation_history` nodes in generated YAML |

`just` wrapper validators were not used because the project environment attempts to build `llvmlite==0.46.0` under Python 3.13 and fails inside setuptools. The equivalent focused LinkML, strict, reference, and term validators were run under `/usr/local/bin/python3.11` with offline cached packages.

## Identity and Grounding

The generated record denotes the intended TOGO M2779 Clostridial Growth Medium. The TOGO API payload for `gm_id=M2779` reports `gm` `http://togomedium.org/medium/M2779`, name `Clostridial Growth Medium (CGM)`, no upstream `src_url`, and one component table headed by M2779.

The structured TOGO ingredient table supports all 14 imported ingredient names and the scalar values for the non-water gram quantities. The June `mgso4-heptahydrate-term-fix-v1.0` event also corrected the primary `MgSO4 . 7H2O` grounding to `CHEBI:31795`, so the heptahydrate form is preserved in this record.

The formula still contains a unit defect: TOGO stores `Distilled water` as 1 L, while the YAML stores it as `1` `G_PER_L`.

An ignored-inclusive search of `data/normalized_yaml`, `data/merge_yaml/merged`, `data/import_tracking`, and `reports` for `CultureMech:009327`, `TOGO:M2779`, `M2779`, the merge fingerprint, `clostridial_growth_medium_cgm.yaml`, and the exact label found the normalized owner, its generated merge, derived indexes/import reports, historical validation snapshots, and no alternate CultureMech owner with the same TOGO identity or merge fingerprint.

## Evidence

The TOGO M2779 structured payload supports the gram-per-liter formulation for MgSO4 . 7H2O, yeast extract, KH2PO4, K2HPO4, FeSO4 . 7H2O, ZnSO4 . 7H2O, `(NH4)2SO4`, CaCl2, MnSO4 . H2O, Na2SeO3, CoCl2, glucose, and tryptone.

TOGO paragraph 1 cites `PMID:4332793` for CBM and `PMID:16346566` for CGM in a comment about culturing `Clostridium spp.` at 37 C under anaerobic-cabinet conditions. NCBI E-utilities resolves `PMID:16346566` to Hartmanis and Gatenbeck 1984, DOI `10.1128/aem.47.6.1277-1283.1984`, with PMC accession `PMC240219`; that article's scanned page 1277 confirms the same CGM formula and its `Clostridium acetobutylicum` ATCC 824 culture context.

The YAML has no `references`, no `source_data`, and no evidence entries linking the formula to TOGO or to Hartmanis and Gatenbeck. Its only provenance is the free-text note `Source: https://togomedium.org/medium/M2779`, which is not enough to recover the PMID/DOI if TOGO changes its comment text.

An ignored-inclusive search of `data/normalized_yaml`, `data/merge_yaml/merged`, `data/import_tracking`, and `reports` for `16346566` and `4332793` found no local YAML, import-tracking, or report hits, so neither TOGO comment PMID is represented in the searched CultureMech corpus.

## Completeness

The basic M2779 formula is substantially complete after the MgSO4 . 7H2O fix: all 13 dry ingredients from TOGO and Hartmanis page 1277 are present, with the right scalar values and exact hydrate labels.

Consequential gaps remain:

- Water has been imported as an ordinary `G_PER_L` ingredient instead of a one-liter final volume.
- Hartmanis page 1277 specifies `Clostridium acetobutylicum` ATCC 824, 37 C anaerobic growth, heat shocking of the stock culture in growth medium, and separate autoclaving of glucose; none are represented in target-organism, temperature, preparation, or sterilization fields.
- The same page gives an initial fermentation pH of 6.5, nitrogen sparging before inoculation, and a 37 C fermentation temperature. Those should be represented only if curated as Hartmanis-specific growth or fermentation context, not as unconditional global CGM instructions.
- The public TOGO payload has no upstream `src_url`, and the maintained record has no quality note explaining that the primary CGM paper was recovered through the TOGO comments rather than through TOGO source metadata.

Empty variant, solution, salinity, light, and storage fields are acceptable for the inspected sources.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | The one-liter final-volume row was imported as `Distilled water` at `1` `G_PER_L`, which is dimensionally wrong and loses TOGO's 1 L volume. | `data/normalized_yaml/bacterial/clostridial_growth_medium_cgm.yaml`; check the TOGO importer for the systemic `L` to `G_PER_L` conversion |
| Major | Primary CGM provenance is recoverable but absent: TOGO's CGM comment cites `PMID:16346566`, NCBI resolves it to DOI `10.1128/aem.47.6.1277-1283.1984` and PMC `PMC240219`, but the YAML has no reference or source-data entry for that paper. | `data/normalized_yaml/bacterial/clostridial_growth_medium_cgm.yaml` |
| Major | Source-supported culture and preparation context from Hartmanis page 1277 is missing, including `Clostridium acetobutylicum` ATCC 824, 37 C anaerobic growth, stock-culture heat shocking in growth medium, and separate autoclaving of glucose. | `data/normalized_yaml/bacterial/clostridial_growth_medium_cgm.yaml` |

No blocker findings were found. The record's identity is correct, its non-water quantities match the structured TOGO table, and its exact MgSO4 . 7H2O, FeSO4 . 7H2O, ZnSO4 . 7H2O, and MnSO4 . H2O labels are preserved.

## Recommended Edits

1. Fix the authoritative M2779 owner or the TOGO importer so 1 L distilled water is represented as final volume or solvent volume instead of `1` `G_PER_L`, then regenerate the merged YAML.
2. Add structured provenance for Hartmanis and Gatenbeck 1984 using `PMID:16346566`, DOI `10.1128/aem.47.6.1277-1283.1984`, and `PMC240219`.
3. Add Hartmanis-scoped target-organism and preparation details: `Clostridium acetobutylicum` ATCC 824, 37 C anaerobic growth, heat shock of the stock culture, and separate glucose autoclaving.
4. Keep the O'Brien and Morris `PMID:4332793` CBM citation out of CGM-specific evidence unless a later curator inspects it and creates a separate CBM record or evidence note.

## Follow-up Checks

- Rerun the focused schema, strict, term, and reference validators on `data/normalized_yaml/bacterial/clostridial_growth_medium_cgm.yaml`.
- Regenerate `data/merge_yaml/merged/clostridial_growth_medium_cgm.yaml` and rerun the same focused validators on the generated record.
- Manually compare the regenerated ingredient block to TOGO M2779 and Hartmanis page 1277, with special attention to the one-liter volume row and the exact hydrate labels.
- Verify that new evidence objects scope the 1984 paper to this CGM formula and `Clostridium acetobutylicum` ATCC 824 rather than generalizing it to all clostridia.

## Additional Notes

TOGO paragraph 2 appears to OCR Hartmanis page 1277 and contains textual artifacts such as `CaCI2` and `Na,SeO3`; the structured TOGO component table has the expected `CaCl2` and `Na2SeO3` labels.

The public TOGO `/medium/M2779` page is an SPA shell; the inspected source payload was fetched from `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2779`.
