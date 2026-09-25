# YAML Record Review: BACTO PHOTOBACTERIUM BROTH

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/BACTO_PHOTOBACTERIUM_BROTH.yaml`
- Started UTC: 2026-09-21T18:28:10Z
- Finished UTC: 2026-09-21T18:29:34Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:015365` |
| Merged record | `data/merge_yaml/merged/BACTO_PHOTOBACTERIUM_BROTH.yaml` |
| Maintained owner | `data/normalized_yaml/specialized/bacto_photobacterium_broth.yaml` |
| Source identity | DSMZ Medium 608 / MediaDive `mediadive.medium:608` |
| Merge status | Generated from one normalized source, `bacto_photobacterium_broth` |

The reviewed record is the generated merge for DSMZ 608, "BACTO PHOTOBACTERIUM BROTH". A gitignore-independent search for `CultureMech:015365`, the record stem, `BACTO PHOTOBACTERIUM BROTH`, `DSMZ Medium 608`, and `DSMZ_Medium608` across `data`, `history`, `src`, `scripts`, `.claude`, and `reports` found one live maintained owner under `data/normalized_yaml/`, its generated merge, registry/index rows, import-tracking rows, and historical validation/report rows; no second live normalized owner was found. The same search included ignored files.

## Validation

| Check | Result |
| --- | --- |
| Open schema | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BACTO_PHOTOBACTERIUM_BROTH.yaml`. |
| Strict schema | Passed with `scripts/validate_strict.py`; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| Reference snippets | Passed with `linkml-reference-validator validate data ...`; 1 file validated, 0 snippet checks, all validations passed. |
| Term labels | Passed with `linkml-term-validator validate-data ... --labels -c conf/oak_config.yaml`. |
| Embedded curation history | Not checked: no documented focused validator exists for embedded `MediaRecipe.curation_history` on one generated merge record; `just validate-history` targets standalone history files. |

The direct `just` validators remain unavailable in this checkout because project `uv` tries to build `llvmlite==0.46.0` under Python 3.13 and exits inside `setuptools`. I used the no-project Python 3.11 validator workaround for the focused schema, strict, reference, and term checks above.

## Identity and Grounding

The record identity is correct. The ID, snake-case name, original DSMZ title, `mediadive.medium:608` source accession, `specialized` category, `COMPLEX` / `UNDEFINED` classification, `LIQUID` physical state, and pH 6.8-7.2 all agree with the single maintained MediaDive/DSMZ import and the DSMZ Medium 608 PDF.

The six simple salts that are grounded in the record also match exact rows in `src/culturemech/data/mediaingredientmech/label_index.csv`: `NH4Cl` to `CHEBI:31206`, `MgSO4` to `CHEBI:32599`, `FeCl2` to `CHEBI:30812`, `CaCO3` to `CHEBI:3311`, `KH2PO4` to `CHEBI:63036`, and `NaCl` to `CHEBI:26710`.

`Tryptone` and `Yeast extract` are ungrounded even though exact local MIM rows exist for the simplified labels: `Tryptone` maps to `MICRO:0000182`, and `Yeast extract` maps to `FOODON:03315426`. DSMZ gives the more specific source labels `Tryptone (Bacto)` and `Yeast extract (Bacto)`, so a future curation pass should decide whether to retain the Bacto qualifier in `preferred_term` while linking the base material, or leave a concrete unresolved flag for the qualifier.

An ignored-inclusive exact and near-exact search of the packaged MIM label index for `Na-glycerol phosphate`, `Sodium glycerophosphate`, `glycerol phosphate`, and `Glycerophosphate` found no exact `Na-glycerol phosphate` row. It did find nearby glycerophosphate salts, including `Sodium glycerophosphate` to `NCIT:C120561`; the present ungrounded value is therefore a defensible unresolved ingredient until an exact-form curator review maps or intentionally leaves DSMZ's `Na-glycerol phosphate`.

## Evidence

DSMZ Medium 608 directly supports the medium title, the 5 g/L `Tryptone (Bacto)`, 2.5 g/L `Yeast extract (Bacto)`, 0.3 g/L `NH4Cl`, 0.3 g/L `MgSO4`, 0.01 g/L `FeCl2`, 1 g/L `CaCO3`, 3 g/L `KH2PO4`, 23.5 g/L `Na-glycerol phosphate`, and 30 g/L `NaCl` rows, plus final adjustment to pH 7.0 +/- 0.2 at 25 C. The generated record preserves the nine solute amounts and the pH range.

The DSMZ source also specifies 1000 ml distilled water. That ingredient is absent from the generated and maintained records.

The record has no target-organism or growth-evidence claims, so no organism assertion is over-generalized from the DSMZ formulation.

## Completeness

The source formulation is materially incomplete because the solvent row is missing. Adding 1000 ml distilled water to the maintained normalized recipe and regenerating the merge would make the ingredient list faithful to the DSMZ formula.

`Na-glycerol phosphate` remains ungrounded, but the ignored-inclusive MIM index search found no exact row for that label. `Tryptone` and `Yeast extract` should be grounded with the exact local rows for their base materials, while preserving or explicitly deferring the DSMZ `Bacto` qualifier.

The pH adjustment is the only preparation instruction in the inspected DSMZ PDF. The absent target-organism, atmosphere, sterilization, and storage fields are optional and not automatically defects for this record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | DSMZ's 1000 ml `Distilled water` row is missing from the ingredient list. | The inspected DSMZ Medium 608 PDF lists 1000 ml distilled water after the 30 g NaCl row; the generated and normalized YAML contain only the nine solutes. | `data/normalized_yaml/specialized/bacto_photobacterium_broth.yaml` |
| Major | The two Bacto complex ingredients are simplified and ungrounded. | DSMZ names `Tryptone (Bacto)` and `Yeast extract (Bacto)`; the record stores `Tryptone` and `Yeast extract` without the Bacto qualifier and without `term` / `mediaingredientmech_chebi_term`, despite exact local rows for the simplified labels. | `data/normalized_yaml/specialized/bacto_photobacterium_broth.yaml` |

## Recommended Edits

1. In `data/normalized_yaml/specialized/bacto_photobacterium_broth.yaml`, add the DSMZ solvent row as 1000 ml distilled water and regenerate `data/merge_yaml/merged/`.
2. In `data/normalized_yaml/specialized/bacto_photobacterium_broth.yaml`, restore the source specificity of `Tryptone (Bacto)` and `Yeast extract (Bacto)` while linking the exact base labels to `MICRO:0000182` and `FOODON:03315426`, or add an explicit quality flag if the Bacto qualifier needs a narrower product record that is not yet available.

## Follow-up Checks

1. Re-run the focused schema, strict, term, and reference validators on `data/merge_yaml/merged/BACTO_PHOTOBACTERIUM_BROTH.yaml` after regeneration.
2. Re-fetch or re-open DSMZ Medium 608 and confirm the regenerated ingredient list contains all nine DSMZ solutes, 1000 ml distilled water, the source Bacto qualifiers, and pH 7.0 +/- 0.2 with no unsupported preparation fields.
3. Re-run an ignored-inclusive search of `src/culturemech/data/mediaingredientmech/label_index.csv` before grounding `Na-glycerol phosphate`; map it only if the source label resolves to an exact salt form.

## Additional Notes

The DSMZ source row is captured only in `notes` and import history, not a structured `source_data` or reference object. This is enough to recover the inspected PDF, but a future curation pass could make the imported DSMZ accession and retrieval path easier to validate automatically.
