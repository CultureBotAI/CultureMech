# YAML Record Review: peptone_meat_extract_glycerol_agar__14f6bae7

- Repository: CultureMech
- Record: data/merge_yaml/merged/peptone_meat_extract_glycerol_agar__14f6bae7.yaml
- Started UTC: 2026-09-24T20:24:26Z
- Finished UTC: 2026-09-24T20:24:26Z
- Verdict: needs curation

## Target

Generated bacterial MediaRecipe `CultureMech:004622`, `peptone_meat_extract_glycerol_agar`, merged from `data/normalized_yaml/bacterial/KOMODO_250_Peptone_MEAT_EXTRACT_GLYCEROL_AGAR.yaml` and `data/normalized_yaml/bacterial/peptone_meat_extract_glycerol_agar.yaml`.

The record represents KOMODO medium 250 as a source duplicate of DSMZ / MediaDive medium 250, PEPTONE MEAT EXTRACT GLYCEROL AGAR. The generated recipe has 5 g/L Proteose peptone no. 3, 3 g/L meat extract, 20 g/L glycerol, and 20 g/L agar, with pH 7.0.

## Validation

- Open LinkML validation: Passed with no issues.
- Strict validator: Passed; `/private/tmp/peptone_meat_extract_glycerol_agar__14f6bae7.strict.tsv` was header-only, so there were 0 strict errors.
- Reference validation: Passed; 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not embedded `MediaRecipe.curation_history`.

## Identity and Grounding

The duplicate relationship is sound. The KOMODO owner explicitly cites DSMZ Medium 250 / `mediadive.medium:250`, the direct MediaDive owner is DSMZ medium 250, and the two maintained owners have matching local ingredient and pH signatures.

An exact ignored-inclusive search found only these two maintained source owners and their one generated merge for `komodo.medium:250`, `mediadive.medium:250`, and the two relevant CultureMech IDs.

## Evidence

The DSMZ medium 250 PDF supports 5.0 g Proteose peptone no. 3, 3.0 g meat extract, 20.0 ml glycerol, 15.0 g agar, 1000.0 ml distilled water, and pH adjustment to 7.0.

MediaDive medium 250 supports the DSMZ source identity, pH 7.0, 5 g Proteose peptone no. 3, 3 g meat extract, 20 ml glycerol, and 1000 ml distilled water. It disagrees with the linked DSMZ PDF on agar, listing 20 g agar where the PDF lists 15 g.

Glycerol is a liquid volume addition in both source mirrors, not a 20 g/L weighed ingredient. Proteose peptone no. 3 and meat extract are appropriately left ungrounded as complex undefined ingredients; glycerol and agar use the expected CHEBI terms.

## Completeness

The merge preserves both duplicate source owners, pH 7.0, and the shared non-water rows, but both maintained inputs omit the 1000 ml distilled water row and carry a volume of glycerol as `20 G_PER_L`.

There is also an unresolved source conflict for agar: CultureMech follows the MediaDive REST value of 20 g/L, while the linked DSMZ PDF lists 15 g per liter.

## Findings

1. Needs curation: `Glycerol` is encoded as `20 G_PER_L` in both maintained owners and the generated record, but DSMZ medium 250 and MediaDive medium 250 both specify `20 ml`.
2. Needs curation: both maintained owners and the generated record omit the 1000 ml `Distilled water` row from DSMZ / MediaDive medium 250.
3. Needs curation: `Agar` is encoded as `20 G_PER_L`, matching MediaDive REST, but the linked DSMZ PDF lists 15 g. The medium needs a curated decision on which current DSMZ representation is authoritative.

## Recommended Edits

1. Encode the glycerol addition as a volume from the source recipe rather than as `20 G_PER_L` in both maintained owners.
2. Add the 1000 ml distilled water component to both maintained owners.
3. Resolve the MediaDive-versus-DSMZ-PDF agar conflict; if the linked DSMZ PDF is treated as authoritative, change `Agar` to `15 G_PER_L`.
4. Regenerate merged YAML and verify the KOMODO 250 owner still merges with the direct DSMZ / MediaDive 250 owner as a source duplicate.

## Follow-up Checks

1. Re-run open, strict, reference, and term validation on the repaired maintained owners and regenerated merged record.
2. Re-fetch MediaDive medium 250 and the DSMZ medium 250 PDF when applying the edit to confirm the agar discrepancy has not been resolved upstream.
3. Repeat an exact ignored-inclusive search for `komodo.medium:250`, `mediadive.medium:250`, and the CultureMech IDs to confirm no additional duplicate medium 250 owner appears.

## Additional Notes

The exact ignored-inclusive duplicate search covered `data`, `src`, and `scripts` for `komodo.medium:250`, `mediadive.medium:250`, `DSMZ Medium: 250`, `CultureMech:004622`, and `CultureMech:001349`.
