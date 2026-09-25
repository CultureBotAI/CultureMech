# YAML Record Review: peptone_meat_extract_soil_extract_agar_pfe

- Repository: CultureMech
- Record: data/merge_yaml/merged/peptone_meat_extract_soil_extract_agar_pfe.yaml
- Started UTC: 2026-09-24T20:27:16Z
- Finished UTC: 2026-09-24T20:27:16Z
- Verdict: needs curation

## Target

Generated bacterial MediaRecipe `CultureMech:004623`, `peptone_meat_extract_soil_extract_agar_pfe`, merged from `data/normalized_yaml/bacterial/KOMODO_251_Peptone_-_MEAT_EXTRACT_-_SOIL_EXTRACT_AGAR_PFE.yaml` and `data/normalized_yaml/bacterial/peptone_meat_extract_soil_extract_agar_pfe.yaml`.

The record represents KOMODO medium 251 as a source duplicate of DSMZ / MediaDive medium 251, PEPTONE - MEAT EXTRACT - SOIL EXTRACT AGAR (PFE). The generated recipe has 5 g/L Proteose peptone no. 3, 3 g/L meat extract, 20 g/L glycerol, 150 g/L soil extract, and 20 g/L agar, with pH 7.0.

## Validation

- Open LinkML validation: Passed with no issues.
- Strict validator: Passed; `/private/tmp/peptone_meat_extract_soil_extract_agar_pfe.strict.tsv` was header-only, so there were 0 strict errors.
- Reference validation: Passed; 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not embedded `MediaRecipe.curation_history`.

## Identity and Grounding

The duplicate relationship is sound. The KOMODO owner explicitly cites DSMZ Medium 251 / `mediadive.medium:251`, the direct MediaDive owner is DSMZ medium 251, and the two maintained owners have matching source identities and local ingredient signatures.

An exact ignored-inclusive search found only these two maintained source owners and their one generated merge for `komodo.medium:251`, `mediadive.medium:251`, and the two relevant CultureMech IDs.

## Evidence

The DSMZ medium 251 PDF supports 5.0 g Proteose peptone no. 3, 3.0 g meat extract, 20.0 g glycerol, 150.0 ml soil extract, 15.0 g agar, 850.0 ml distilled water, and pH adjustment to 7.0.

MediaDive medium 251 supports the DSMZ source identity, pH 7.0, 5 g Proteose peptone no. 3, 3 g meat extract, 20 g glycerol, 150 ml soil extract, and 850 ml distilled water. It disagrees with the linked DSMZ PDF on agar, listing 20 g agar where the PDF lists 15 g.

The September maintained owners correctly add local MICRO grounding for Proteose peptone no. 3 and Soil extract. The generated August merge is stale and still lacks those term links.

## Completeness

The merge preserves both duplicate source owners, pH 7.0, and the direct major components, but both maintained inputs omit the 850 ml distilled water row and carry the 150 ml soil extract volume as `150 G_PER_L`.

The generated record also loses the DSMZ preparation text that remains present in the direct DSMZ owner. That text includes both the pH adjustment and the soil-extract stock preparation.

## Findings

1. Needs curation: `Soil extract` is encoded as `150 G_PER_L` in both maintained owners and the generated record, but DSMZ and MediaDive specify a `150 ml` volume addition.
2. Needs curation: both maintained owners and the generated record omit the 850 ml `Distilled water` row from DSMZ / MediaDive medium 251.
3. Needs curation: `Agar` is encoded as `20 G_PER_L`, matching MediaDive REST, but the linked DSMZ PDF lists 15 g; the record needs a curated decision on which current DSMZ representation is authoritative.
4. Needs curation: the generated merge is stale relative to September maintained-owner repairs that ground Proteose peptone no. 3 and Soil extract to local MICRO terms.
5. Needs curation: the generated merge uses the KOMODO owner as canonical and drops the direct DSMZ owner's preparation step, including the pH adjustment and the soil-extract stock preparation details.

## Recommended Edits

1. Encode the soil extract addition as `150 ml` from the source recipe rather than as `150 G_PER_L` in both maintained owners.
2. Add the 850 ml distilled water component to both maintained owners.
3. Resolve the MediaDive-versus-DSMZ-PDF agar conflict; if the linked DSMZ PDF is treated as authoritative, change `Agar` to `15 G_PER_L`.
4. Preserve the DSMZ pH-adjustment and soil-extract stock preparation text after source-duplicate merging.
5. Regenerate merged YAML so the September MICRO grounding repairs are reflected in this generated record.

## Follow-up Checks

1. Re-run open, strict, reference, and term validation on the repaired maintained owners and regenerated merged record.
2. Re-fetch MediaDive medium 251 and the DSMZ medium 251 PDF when applying the edit to confirm the agar discrepancy has not been resolved upstream.
3. Repeat an exact ignored-inclusive search for `komodo.medium:251`, `mediadive.medium:251`, and the CultureMech IDs to confirm no additional duplicate medium 251 owner appears.

## Additional Notes

The exact ignored-inclusive duplicate search covered `data`, `src`, and `scripts` for `komodo.medium:251`, `mediadive.medium:251`, `DSMZ Medium: 251`, `DSMZ_Medium251`, `CultureMech:004623`, and `CultureMech:001350`.
