# YAML Record Review: clostridia_growth_medium_cgm

- Repository: CultureMech
- Record: data/merge_yaml/merged/clostridia_growth_medium_cgm.yaml
- Started UTC: 2026-09-22T08:51:00Z
- Finished UTC: 2026-09-22T08:53:52Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/clostridia_growth_medium_cgm.yaml`, a generated `MediaRecipe` for `CultureMech:009356` / `clostridia_growth_medium_cgm`.

The generated record is a one-source merge from the maintained owner `data/normalized_yaml/bacterial/clostridia_growth_medium_cgm.yaml` with merge fingerprint `fab3311456e642e0c5c51ff53149414a5e92085a8e37537d7df143e05869a0f7`.

The source identity is `TOGO:M2808`, labelled `Clostridia growth medium (CGM)`.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/clostridia_growth_medium_cgm.yaml` | Pass |
| `python scripts/validate_strict.py data/merge_yaml/merged/clostridia_growth_medium_cgm.yaml --out /private/tmp/clostridia_growth_medium_cgm.strict.tsv --workers 1 --quiet` | Pass; TSV contained only the header row |
| `linkml-reference-validator validate data data/merge_yaml/merged/clostridia_growth_medium_cgm.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass; 0 reference checks |
| `linkml-term-validator validate-data data/merge_yaml/merged/clostridia_growth_medium_cgm.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass; emitted only the expected NCBI E-utilities deprecation warning |
| Embedded curation-history validation | Not checked: the documented `just validate-history` target validates standalone `history/` records, not embedded `MediaRecipe.curation_history` nodes in generated YAML |

`just` wrapper validators were not used because the project environment attempts to build `llvmlite==0.46.0` under Python 3.13 and fails inside setuptools. The equivalent focused LinkML, strict, reference, and term validators were run under `/usr/local/bin/python3.11` with offline cached packages.

## Identity and Grounding

The record identity matches TOGO M2808. The TOGO API payload for `gm_id=M2808` reports `gm` `http://togomedium.org/medium/M2808`, name `Clostridia growth medium (CGM)`, no `src_url`, and an ingredient table headed by the same CGM source.

The formula identity is mostly the same as TOGO M2808 and Wiesenborn et al. 1988, PMID:16347774, DOI `10.1128/aem.54.11.2717-2722.1988`: water, yeast extract, NaCl, KH2PO4, K2HPO4, FeSO4 . 7H2O, `(NH4)2SO4`, MnSO4 . H2O, asparagine, MgSO4 . H2O, glucose, and Antifoam C are the expected components.

Two exact grounding or unit issues change the scientific representation:

- TOGO reports 1 L distilled water and 0.2 ml Antifoam C; the YAML stores both as `G_PER_L`.
- TOGO and the primary article specify `MgSO4 . H2O`, while the YAML's primary `term` is generic magnesium sulfate (`CHEBI:32599`) rather than a monohydrate-specific identifier or an unresolved exact hydrate.

An ignored-inclusive search of `data/normalized_yaml`, `data/merge_yaml/merged`, `data/import_tracking`, and `reports` for `CultureMech:009356`, `TOGO:M2808`, `M2808`, the merge fingerprint, `clostridia_growth_medium_cgm.yaml`, and the exact label found the single normalized owner, its generated merge, derived indexes/import reports, historical validation snapshots, and no alternate record with the same TOGO identity or fingerprint.

## Evidence

The fetched TOGO M2808 JSON supports the ingredient names and scalar quantities for the 12 imported rows, but it does not support the YAML's normalized units for the 1 L water row or the 0.2 ml Antifoam C row.

NCBI E-utilities resolved the PMID embedded in the TOGO comments to Wiesenborn, Rudolph, and Papoutsakis, 1988, and the PMC HTML for `PMC204361` exposes scanned page images for the article. Visual inspection of page 2718 confirmed that the paper gives the same per-liter CGM composition, including `MgSO4 . H2O`, `Antifoam C` as a volume, and glucose at 50 g.

The YAML has no `references`, no structured `source_data`, no DOI/PMID/PMC provenance, and no narrow evidence entries. Its only recoverable provenance is the notes string `Source: https://togomedium.org/medium/M2808`, even though the TOGO payload includes the PMID lead and the primary article is public.

An ignored-inclusive search of `data/normalized_yaml`, `data/merge_yaml/merged`, `data/import_tracking`, and `reports` for `16347774` found nothing, confirming that the PubMed ID from the TOGO comment has not already been captured in the searched CultureMech records or import reports.

## Completeness

The generated record preserves the basic medium category, undefined complex composition, liquid physical state, and microbial-cultivation application well enough for the TOGO import.

Consequential missing fields remain:

- The primary paper gives culture context for `Clostridium acetobutylicum` ATCC 824, including a 37 C incubation, pH 6.0, nitrogen/carbon monoxide sparging, 14 L fermenter growth, and heat shocking. None of those target-organism, temperature, pH, atmosphere, or preparation claims are represented.
- The public TOGO record has an empty upstream `src_url`; the maintained record should carry an explicit provenance gap or curator-added primary source instead of relying only on the TOGO URL string.
- The Antifoam C commercial ingredient is intentionally literal but ungrounded; the maintained record should either add an exact product identifier if one exists or add a quality note documenting that no exact CHEBI/MediaIngredientMech term was found.

Empty solution, variant, storage, salinity, and light fields are acceptable for this source; the inspected TOGO payload and first two Wiesenborn scanned pages did not require those fields.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | Final-volume and milliliter units were flattened to `G_PER_L`: `Distilled water` is 1 L in TOGO but 1 `G_PER_L` in YAML, and Antifoam C is 0.2 ml in TOGO and Wiesenborn but 0.2 `G_PER_L` in YAML. | `data/normalized_yaml/bacterial/clostridia_growth_medium_cgm.yaml`; check the TOGO importer if other records imported `L` or `ml` rows the same way |
| Major | `MgSO4 . H2O` was grounded only to generic magnesium sulfate, losing the monohydrate specified by both TOGO and the primary paper. | `data/normalized_yaml/bacterial/clostridia_growth_medium_cgm.yaml` |
| Major | The record omits recoverable primary provenance. TOGO has no `src_url` but embeds `PMID:16347774`; NCBI resolves that PMID to Wiesenborn et al. 1988 with DOI `10.1128/aem.54.11.2717-2722.1988` and PMC `PMC204361`. | `data/normalized_yaml/bacterial/clostridia_growth_medium_cgm.yaml` |
| Major | Available pH, temperature, gas, fermenter, heat-shock, and `Clostridium acetobutylicum` ATCC 824 growth context from Wiesenborn page 2718 is absent, leaving the record as an ingredient list rather than a reusable culture protocol. | `data/normalized_yaml/bacterial/clostridia_growth_medium_cgm.yaml` |
| Minor | Antifoam C is explicitly present but unresolved in `data/import_tracking/reports/ungrounded_ingredients.tsv`; the YAML has no discussion item preserving the unresolved commercial-product grounding decision. | `data/normalized_yaml/bacterial/clostridia_growth_medium_cgm.yaml` |

No blocker findings were found. The record denotes the intended TOGO M2808 medium and passes the focused schema, strict, term, and reference validators.

## Recommended Edits

1. Fix the TOGO M2808 import or normalized owner so water keeps its final-volume role and Antifoam C remains a 0.2 ml component, then regenerate `data/merge_yaml/merged/clostridia_growth_medium_cgm.yaml`.
2. Replace the primary `term` for `MgSO4 . H2O` with an exact magnesium sulfate monohydrate term if the packaged chemical indexes provide one; otherwise leave the exact label ungrounded and add a quality note explaining that no exact monohydrate term was found.
3. Add structured primary-source provenance for PMID:16347774, DOI `10.1128/aem.54.11.2717-2722.1988`, and `PMC204361`, scoped to the CGM formula and Wiesenborn culture conditions rather than to all future uses of CGM.
4. Curate the recoverable preparation and growth context for `Clostridium acetobutylicum` ATCC 824 from Wiesenborn page 2718: incubation at 37 C, pH 6.0, nitrogen/carbon monoxide sparging, 14 L fermenter growth, heat-shocking context, and any source-supported target-organism entry.
5. Add a discussion or quality flag for Antifoam C if no exact CHEBI/MediaIngredientMech product grounding exists after a bounded exact search.

## Follow-up Checks

- Rerun the focused schema, strict, term, and reference validators on `data/normalized_yaml/bacterial/clostridia_growth_medium_cgm.yaml`.
- Regenerate merges and rerun the same validators on `data/merge_yaml/merged/clostridia_growth_medium_cgm.yaml`.
- Rerun the ungrounded-ingredient report or its owning import-tracking gate to confirm that any retained Antifoam C gap is intentional and documented.
- Manually compare the regenerated CGM ingredient block against TOGO M2808 and Wiesenborn page 2718 to verify the two non-mass quantities, exact MgSO4 hydrate, and source-scoped growth conditions.

## Additional Notes

The scanned PMC PDF endpoint returned a proof-of-work interstitial, so this pass inspected the PMC HTML and the first two CDN page images directly. Those images were sufficient for the culture-methods paragraph and the CGM formula on page 2718.

The public TOGO `/medium/M2808` page is an SPA shell; the inspected source payload was fetched from `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2808`.
