# YAML Record Review: modified_cm_ye_medium_b

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_cm_ye_medium_b.yaml
- Started UTC: 2026-09-24T10:40:57Z
- Finished UTC: 2026-09-24T10:42:12Z
- Verdict: needs curation

## Target

Generated record `CultureMech:002632` for JCM/MediaDive medium `J275`, `MODIFIED CM+YE MEDIUM (B)`.

The generated record is a canonical merge of eight maintained recipes: JCM `J275`, JCM `J59`, DSMZ 910 and its KOMODO duplicate, DSMZ 1262, JCM `J1233`, JCM `J115`, and a KOMODO 910 variant for DSM 44618. The review compared the generated YAML with those exact owners, MediaDive media `J275`, `J59`, `J115`, `J1233`, `910`, and `1262`, and the corresponding JCM pages for 59, 115, 275, and 1233.

## Validation

- Open LinkML validation: passed with no issues found.
- Strict validation: passed; `/private/tmp/modified_cm_ye_medium_b.strict.tsv` contained only the header row.
- Reference validation: passed with 0 reference checks.
- Term validation: passed.
- Embedded `curation_history`: Not checked: the available history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The top-level identity points at JCM `J275`, which is the 100 g NaCl `MODIFIED CM+YE MEDIUM (B)` variant.

The merged provenance is too broad for that identity. JCM 275/DSMZ 910 are 100 g NaCl B media, JCM 115 is the 150 g NaCl A medium, JCM 59 is the 200 g NaCl base CM+YE medium, DSMZ 1262 carries 200 g NaCl plus an extra 100 g NaCl row, and JCM 1233 is the JCM 59 base adjusted to pH 9.0 with sterilized 10% `Na2CO3` after autoclaving. Collapsing those records under the JCM 275 identifier hides distinct salinity and pH variants.

## Evidence

JCM 275 lists 7.5 g Casamino acids, 10 g yeast extract, 10 g `MgSO4 x 7 H2O`, 3 g trisodium citrate dihydrate, 2 g KCl, 100 g NaCl, 1 ml `Fe2+ solution`, 15 g agar, and 1 L distilled water, followed by pH adjustment to 7.4. Its Fe2+ stock is 4.98 g `FeSO4 x 7 H2O` in 100 ml distilled water.

The generated record keeps JCM 275's 100 g NaCl, 10 g magnesium sulfate, 15 g agar, and pH 7.4 values, but promotes the Fe2+ stock content into a 49.8 g/L final-medium `FeSO4 x 7 H2O` row and drops both the 1 L main water row and the 100 ml Fe2+ stock water row.

The merged siblings disagree with JCM 275. JCM 59 and its pH-9 derivative use 200 g NaCl and 20 g magnesium sulfate, JCM 115 uses 150 g NaCl and 20 g magnesium sulfate, DSMZ 1262 adds a second 100 g NaCl row to the 200 g base, and DSMZ 910 uses 100 g NaCl but 20 g agar rather than the 15 g used by JCM 275.

## Completeness

The generated record preserves a recognizable JCM 275 scalar formula, pH 7.4, and the 49.8 g/L strength of the Fe2+ stock.

It is incomplete for stock boundaries and source identity. The Fe2+ stock is flattened, water rows are absent, vendor qualifiers on Casamino acids and yeast extract are incomplete, and variant media with distinct NaCl, magnesium sulfate, agar, and pH values are represented only as synonyms of a 100 g NaCl B record.

## Findings

- High: JCM/DSMZ CM+YE variants with different salinities and pH values were merged into one JCM 275 record.
- High: The 1 ml Fe2+ solution addition was flattened into a 49.8 g/L top-level `FeSO4 x 7 H2O` final-medium row.
- Medium: The 1 L main distilled-water row and 100 ml Fe2+ stock distilled-water row are missing.
- Medium: DSMZ 910 and JCM 275 are not exact duplicates because the agar amount differs: 20 g in DSMZ 910 versus 15 g in JCM 275.
- Low: The BD-Difco/Difco attributes on Casamino acids and yeast extract are only partially retained.

## Recommended Edits

- Revisit the 2026-08-06 duplicate merge and split JCM 115, JCM 275, JCM 59, JCM 1233, DSMZ 1262, and DSMZ/KOMODO 910 variants unless a source-specific variant model can preserve their different NaCl, magnesium sulfate, agar, and pH values.
- Keep only true exact duplicates as `variant_children`; the maintained DSMZ 910 owner already limits its duplicate child to `KOMODO_910_MODIFIED_CM_YE_medium_B.yaml`.
- Restore Fe2+ solution as a nested 1 ml addition with 4.98 g `FeSO4 x 7 H2O` in 100 ml distilled water.
- Restore the JCM 275 1 L main distilled-water row.
- Preserve source-specific Casamino acids and yeast-extract attributes from JCM or DSMZ.
- Regenerate `data/merge_yaml/merged/modified_cm_ye_medium_b.yaml` after the merge grouping or owners are repaired.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated YAML.
- Confirm that JCM 275 no longer lists JCM 59, JCM 115, JCM 1233, or DSMZ 1262 in `merged_from` or as synonyms.
- Compare the regenerated JCM 275 formula against the JCM 275 page to verify 100 g NaCl, 10 g magnesium sulfate, 15 g agar, pH 7.4, and a nested 1 ml Fe2+ solution.

## Additional Notes

The exact owners were found with `find`, which included ignored files.
