# YAML Record Review: CLOSTRIDIUM SP. LA1 MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/clostridium_sp_la1_medium.yaml`
- Started UTC: `2026-09-22T09:34:25Z`
- Finished UTC: `2026-09-22T09:34:35Z`
- Verdict: pass with minor issues

## Target

Generated bacterial `MediaRecipe` record `CultureMech:000902` for MediaDive medium `143`, DSMZ Medium 143 `CLOSTRIDIUM SP. LA1 MEDIUM`. The generated record merges the MediaDive source with KOMODO duplicate `clostridium_medium.yaml` on merge fingerprint `54b6136ac7a9e4a81f3f7e6f3dd492f206e2f98e822258f35af329bb7f12b072`.

## Validation

- LinkML open schema validation: passed.
- Strict validation: passed with no errors in `/private/tmp/clostridium_sp_la1_medium.strict.tsv`.
- LinkML reference validation: passed; the validator reported 0 total checks.
- LinkML term validation: passed.
- Embedded `curation_history` entries: not checked by the standalone history validator.

## Identity and Grounding

The DSMZ/MediaDive identity is correct, and the direct KOMODO duplicate is merged rather than emitted as a second generated record.

The main label-plausibility defect from an older report is resolved in this generated record: `(NH4)2HPO4` is now grounded to `CHEBI:63051` / diammonium hydrogen phosphate rather than the earlier implausible polysaccharide CHEBI ID.

The remaining grounding issues are minor. `(NH4)2HPO4` still retains a legacy `mediaingredientmech_term`, and `(NH4)6Mo7O24 x 4 H2O` is linked only to generic ammonium molybdate without a CHEBI-keyed MediaIngredientMech link.

## Evidence

The DSMZ Medium 143 PDF supports every generated final concentration. Bulk gram additions are carried through directly, and 0.1% w/v aliquots have been correctly converted: 0.60 ml MgSO4 gives `0.0006 G_PER_L`, 0.40 ml MnSO4 and FeSO4 give `0.0004 G_PER_L`, 0.04 ml biotin gives `0.00004 G_PER_L`, 0.80 ml p-aminobenzoic acid gives `0.0008 G_PER_L`, and 0.50 ml sodium resazurin gives `0.0005 G_PER_L`.

The preparation step also matches the DSMZ source: potassium carbonate is withheld from the main autoclave, the parent medium is sparged and dispensed under 100% N2, the potassium carbonate stock is autoclaved under 80% N2 / 20% CO2, final pH is adjusted to 6.8-7.0, and sodium dithionite is optionally added before inoculation.

The ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml/merged`, `data/import_tracking`, and `reports` found only the direct DSMZ/MediaDive source and the KOMODO duplicate for exact DSMZ Medium 143 identifiers and URLs; ignored files were included.

## Completeness

The record carries the formula, pH range, anaerobic preparation, and optional sodium dithionite note.

Source vendor strings for `Tryptone (BD BBL)` and `Yeast extract (OXOID)` are not retained on the ingredient rows, but the ingredient identities and amounts are still present.

No target organism is listed.

## Findings

- Minor: `(NH4)2HPO4` keeps a deprecated `MediaIngredientMech:000385` link even though the primary CHEBI grounding is now correct.
- Minor: `(NH4)6Mo7O24 x 4 H2O` is grounded to generic ammonium molybdate and lacks a CHEBI-keyed MediaIngredientMech link.
- Minor: `parent_media` points to the KOMODO duplicate `clostridium_medium.yaml`, and that source still carries the inherited `Aerobic: Yes` note despite DSMZ's anoxic preparation.

## Recommended Edits

- Replace remaining legacy MediaIngredientMech IDs with CHEBI-keyed links when matching terms exist.
- Prefer the DSMZ/MediaDive source as the duplicate-group parent during merge metadata regeneration.
- Clean stale KOMODO aerobic annotations on anaerobic DSMZ-derived media.

## Follow-up Checks

- Validate the regenerated record with open schema, strict, reference, and term validators.
- Confirm the small 0.1% aliquots remain final-mass concentrations after any import refactor.
- Confirm the KOMODO duplicate remains merged and no second DSMZ Medium 143 generated record is emitted.

## Additional Notes

No formula-level curation issues were found. Empty optional fields are not defects, and the generated record is a faithful flat representation of the DSMZ one-page formula.
