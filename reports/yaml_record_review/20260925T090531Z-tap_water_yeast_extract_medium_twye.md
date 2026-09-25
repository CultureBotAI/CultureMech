# YAML Record Review: tap_water_yeast_extract_medium_twye

- Repository: CultureMech
- Record: `data/merge_yaml/merged/tap_water_yeast_extract_medium_twye.yaml`
- Started UTC: 2026-09-25T09:04:55Z
- Finished UTC: 2026-09-25T09:05:31Z
- Verdict: pass with minor issues

## Target

Generated merged record `CultureMech:010456` for
`tap_water_yeast_extract_medium_twye`, with `mediadive.medium:1625`, fingerprint
`df3524f7e64a690f557ce73d12484aac128eb309cdde0dec4b4e476e0dedca1b`, and one
merged source, `tap_water_yeast_extract_medium_twye`.

## Validation

- LinkML schema: passed; exited 0 with no diagnostics.
- Strict validator: passed with 0 ERROR rows.
- Reference validator: passed with 0 checks.
- Term validator: passed.
- Embedded `curation_history`: Not checked: the available history validator checks
  standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The record is correctly grounded to DSMZ/MediaDive medium 1625, `TAP WATER YEAST
EXTRACT MEDIUM (TWYE)`.

## Evidence

MediaDive 1625 and the current DSMZ 1625 PDF agree on the four-line recipe:
0.25 g yeast extract, 0.5 g K2HPO4, 18 g agar, and 1000 ml tap water.

The generated record represents the three mass ingredients at the same grams per
liter values and grounds K2HPO4 and agar to CHEBI.

## Completeness

The core DSMZ 1625 ingredient set is complete. DSMZ 1625 does not state a pH,
temperature, special preparation step, or target organism on the fetched PDF.

The only minor modeling issue is the solvent row: the source measures tap water
as `1000 ml`, while the generated record stores it as `1000 G_PER_L` and grounds
it to generic water. That preserves the presence of water but loses the
source-specific tap-water wording and volume context.

## Findings

- Minor: `Tap water` is volume-based in DSMZ/MediaDive but is encoded as
  `1000 G_PER_L` in the generated YAML.

## Recommended Edits

- Represent `Tap water` as a solvent volume or preparation context rather than a
  grams-per-liter concentration if the schema supports it.
- If the row must remain a flat ingredient, preserve a note that DSMZ specifies
  tap water rather than deionised or distilled water.

## Follow-up Checks

- Re-fetch DSMZ/MediaDive medium 1625 after any solvent modeling change and
  confirm the mass ingredients remain 0.25 g/l yeast extract, 0.5 g/l K2HPO4,
  and 18 g/l agar.

## Additional Notes

None found
