# YAML Record Review: M17 medium (modified)

- Repository: CultureMech
- Record: `data/merge_yaml/merged/m17_medium_modified.yaml`
- Started UTC: 2026-09-23T20:56:35Z
- Finished UTC: 2026-09-23T20:57:24Z
- Verdict: needs curation

## Target

- Generated record: `data/merge_yaml/merged/m17_medium_modified.yaml`
- Canonical maintained owner: `data/normalized_yaml/bacterial/KOMODO_659_M17_medium_modified.yaml`
- Duplicate maintained owner: `data/normalized_yaml/bacterial/m17_medium_modified.yaml`
- CultureMech ID: `CultureMech:006236`
- Media term: `komodo.medium:659`
- Merge fingerprint: `705bb79f89fe3eca50938b971835b25daec40dd28708d7221fafa5957d1ac079`
- Merge sources: `KOMODO_659_M17_medium_modified`, `m17_medium_modified`
- Ignored-inclusive search over `data/normalized_yaml`, `data/merge_yaml`, and `reports/archive` found the KOMODO owner, the direct DSMZ/MediaDive owner, the generated two-source merge, a historical source-duplicate review row, generated indexes, and historical validation rows.

## Validation

- Open LinkML validation against `MediaRecipe`: passed.
- Strict validation with `scripts/validate_strict.py`: passed with 0 error rows in `/private/tmp/m17_medium_modified.strict.tsv`.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded `curation_history` entries were not checked as standalone history records.

## Identity and Grounding

The generated record represents DSMZ Medium 659, `M17 MEDIUM (modified)`, through the KOMODO copy `komodo.medium:659`. MediaDive REST for DSMZ `659` confirms the base composition: 5 g/L each of casein peptone, soy peptone, and meat peptone; 2.5 g/L yeast extract; 0.5 g/L ascorbic acid; 0.25 g/L MgSO4 x 7 H2O; 9.5 g/L Na2-beta-glycerolphosphate; lactose to 8.0 g/L after autoclaving; and a 1.2 ml addition of 1 M CaCl2 x 2 H2O. It also confirms pH 7.1-7.2.

The KOMODO and MediaDive owners are legitimate source duplicates for the same DSMZ formula, but the merged canonical inherited the KOMODO version, which lacks the preparation step present in the direct MediaDive owner.

## Evidence

- MediaDive REST for `659` confirms the exact peptone, yeast extract, ascorbic acid, MgSO4 x 7 H2O, sodium beta-glycerophosphate, lactose, and pH values used in the YAML.
- MediaDive encodes lactose as 8 g/L with `sterilized by filtration`.
- MediaDive encodes the final calcium chloride addition as `1.2 ml 1M CaCl2 x 2 H2O`, not as 1.2 g/L.
- `reports/archive/media_variant_dsmz_komodo_source_duplicate_review.md` had already classified the DSMZ and KOMODO owners as `SOURCE_DUPLICATE`.

## Completeness

The ingredient list is mostly complete relative to MediaDive/DSMZ 659, but it drops DSMZ preparation semantics during the duplicate merge and misrepresents the 1.2 ml 1 M CaCl2 x 2 H2O addition as 1.2 g/L.

The record also lacks structured source references and target-organism grounding.

## Findings

1. The CaCl2 x 2 H2O addition is quantitatively wrong. DSMZ adds 1.2 ml of a 1 M CaCl2 x 2 H2O solution to 1 L; the YAML records `1.2 G_PER_L`, which treats a molar stock-volume addition as a dry mass. If flattened to final mass, 1.2 mmol/L calcium chloride dihydrate is approximately 0.176 g/L, not 1.2 g/L.

2. The generated merge lost the source-backed preparation step. The direct DSMZ owner says to add a filter-sterilized lactose solution after autoclaving, add the 1 M CaCl2 x 2 H2O solution, and adjust pH to 7.15 +/- 0.05. The KOMODO owner has no `preparation_steps`, and the generated canonical inherited that omission.

3. Source references are not structured. The generated record carries KOMODO and DSMZ identity only in `media_term` and a free-text note, so DSMZ Medium 659 is not traversable through a `references` entry.

## Recommended Edits

- Correct the CaCl2 x 2 H2O addition in both maintained owners by representing it as 1.2 ml of 1 M solution, or by storing the calculated final concentration with notes that preserve the original DSMZ volume.
- Preserve the DSMZ post-autoclave preparation instruction when KOMODO 659 and MediaDive 659 are merged.
- Add structured references for both KOMODO 659 and the DSMZ Medium 659 source URL.
- Regenerate merged YAML and rerun open schema, strict, reference, and term validation.

## Follow-up Checks

- Confirm how the schema should represent molar stock additions before converting `1.2 ml 1M CaCl2 x 2 H2O` to a final concentration.
- Re-run an ignored-inclusive exact search for `komodo.medium:659` and `mediadive.medium:659` after regeneration to ensure the duplicate relationship remains one KOMODO owner plus one DSMZ owner.

## Additional Notes

The source name contains `beta`-glycerolphosphate. Reports use ASCII spelling to avoid carrying a non-ASCII beta character into the review artifact.
