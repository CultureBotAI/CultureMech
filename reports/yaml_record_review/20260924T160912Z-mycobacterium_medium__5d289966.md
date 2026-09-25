# YAML Record Review: mycobacterium_medium__5d289966

- Repository: CultureMech
- Record: data/merge_yaml/merged/mycobacterium_medium__5d289966.yaml
- Started UTC: 2026-09-24T16:08:58Z
- Finished UTC: 2026-09-24T16:09:12Z
- Verdict: needs curation

## Target

Reviewed the generated MediaRecipe `CultureMech:004429` for `mycobacterium_medium`.
The canonical generated record is the KOMODO import for `komodo.medium:219` and
is merged with the direct DSMZ owner `CultureMech:001321` as a
`SOURCE_DUPLICATE`.

## Validation

Focused validation passed:

- LinkML `MediaRecipe` validation: passed; no issues found.
- Strict validation: passed with zero error rows in `/private/tmp/mycobacterium_medium__5d289966.strict.tsv`.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The duplicate identity is credible. The generated canonical record is grounded
to KOMODO Medium 219, its notes explicitly cite DSMZ Medium 219, and the
curated DSMZ parent is linked as the same `mediadive.medium:219` recipe.

The active KOMODO and DSMZ owners share the same incomplete ingredient
signature: both retain the ten non-water MediaDive rows. The maintained DSMZ
owner additionally has the source pH-adjustment step, but the generated
canonical record inherits from the KOMODO child and drops that preparation
detail.

## Evidence

The MediaDive REST record for medium 219 gives `MYCOBACTERIUM MEDIUM`, source
DSMZ, pH 7, and a 1000 ml `Main sol. 219` containing eleven source rows:

- Yeast extract, 2 g
- Proteose peptone no. 3, 2 g
- Casein peptone, tryptic digested, 2 g
- Na2HPO4 x 12 H2O, 2.5 g
- KH2PO4, 1 g
- Sodium citrate, 1.5 g
- MgSO4 x 7H2O, 0.6 g
- Glycerol, 50 ml
- Tween, 0.5 g
- Agar, 20 g
- Distilled water, 1000 ml

MediaDive also supplies the preparation step `Adjust pH to 7.0.`

## Completeness

The generated recipe has ten ingredient rows and is missing the source
`Distilled water` row. It also records pH only as `ph_value: 7.0`; the explicit
DSMZ pH-adjustment step is absent after the merge selected the KOMODO child as
canonical.

Most dry quantities are transcribed in the expected g/L units for a 1 L main
solution. `Glycerol` is not: MediaDive lists 50 ml, while the generated row has
`50 G_PER_L`.

## Findings

1. Source water is missing from both normalized owners and therefore from the
   generated duplicate recipe. MediaDive 219 includes `Distilled water` at
   1000 ml in `Main sol. 219`.

2. `Glycerol` has a source quantity of 50 ml, but the generated record casts it
   as `50 G_PER_L`. That changes a liquid volume addition into a mass
   concentration.

3. The generated canonical record omits DSMZ's source preparation step,
   `Adjust pH to 7.0.`, even though the linked direct DSMZ owner already
   preserves it.

4. The KOMODO owner carries malformed embedded history timestamp
   `2026-01-27T01:15:02.fZ`.

5. The `Na2HPO4 x 12 H2O` row is grounded to anhydrous disodium
   hydrogenphosphate, `CHEBI:34683`; that is broader than the dodecahydrate
   named by the DSMZ source.

## Recommended Edits

Repair the normalized owners before regenerating `data/merge_yaml/merged`:

- Add the 1000 ml `Distilled water` ingredient to the DSMZ owner
  `data/normalized_yaml/bacterial/mycobacterium_medium.yaml` and the KOMODO
  duplicate `data/normalized_yaml/bacterial/KOMODO_219_MYCOBACTERIUM_medium.yaml`.
- Preserve MediaDive's liquid quantity for `Glycerol` as 50 ml instead of
  converting it to 50 g/L.
- Ensure the generated source duplicate keeps the DSMZ pH-adjustment
  preparation step regardless of whether the KOMODO child or direct DSMZ owner
  is selected as canonical.
- Normalize the malformed KOMODO import timestamp.
- Revisit the `Na2HPO4 x 12 H2O` grounding and either use a hydrate-specific
  term when available or leave the source hydrate ungrounded instead of
  silently broadening it to anhydrous `CHEBI:34683`.

## Follow-up Checks

- Regenerate the merged YAML and confirm the `mycobacterium_medium__5d289966`
  duplicate recipe has eleven ingredients and the pH-adjustment preparation
  step.
- Re-run LinkML, strict, reference, and term validation on the regenerated
  record.
- Run a focused comparison against MediaDive medium 219 to verify that no
  source row is dropped.

## Additional Notes

None found.
