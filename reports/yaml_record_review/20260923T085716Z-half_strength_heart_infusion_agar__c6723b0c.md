# YAML Record Review: HALF STRENGTH HEART INFUSION AGAR

- Repository: CultureMech
- Record: data/merge_yaml/merged/half_strength_heart_infusion_agar__c6723b0c.yaml
- Started UTC: 2026-09-23T08:55:53Z
- Finished UTC: 2026-09-23T08:57:16Z
- Verdict: needs curation

## Target

- Reviewed generated YAML for `HALF STRENGTH HEART INFUSION AGAR`.
- Stable ID: `CultureMech:002240`.
- Primary source in generated record: direct JCM/MediaDive `mediadive.medium:J105`.
- Merge fingerprint: `c6723b0c3a46a74c219ffa81ab7fd5236e10f2840954bcc7be9d80b47892e6a5`.

## Validation

- LinkML validation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe`: pass.
- Strict validation with `scripts/validate_strict.py`: pass; the validator exited 0 after its startup line, and `/private/tmp/half_strength_heart_infusion_agar_c6723b0c.strict.tsv` has 1 line, the header only.
- LinkML reference validation: pass, 0 checked references.
- LinkML term validation with `conf/oak_config.yaml`: pass.
- Embedded `curation_history`: Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

- The generated record is the direct JCM/MediaDive import for JCM medium 105.
- An exact `rg --no-ignore --hidden` search for `JCM_M105`, `GRMD=105`, `TOGO:M97`, and `mediadive.medium:J105` found the direct JCM/MediaDive source and a source-equivalent Togo `M97` / `JCM_M105` import in `data/merge_yaml` and `data/normalized_yaml`.
- The generated record carries `kg_microbe_match: mediadive.medium:12`, which resolves to DSMZ `SOIL EXTRACT MEDIUM`, not to Half Strength Heart Infusion Agar.

## Evidence

- MediaDive `J105` lists Heart Infusion Broth 12.5 g, agar 15 g, and distilled water 1000 ml.
- Togo `M97` is a snapshot of JCM `M105` and lists the same 1 L distilled water, 15 g agar, and 12.5 g Heart infusion broth from BD-Difco.
- The live JCM `GRMD=105` endpoint currently returns `Nothing found`; MediaDive and Togo were the available cross-checks for this JCM recipe.
- MediaDive DSMZ 12 is Soil Extract Medium, with 400 g air-dried garden soil, 1000 ml tap water, and 15 g agar, so it is not an appropriate `kg_microbe_match` for this JCM 105 formula.

## Completeness

- The generated record has the correct Heart Infusion Broth 12.5 g/L and agar 15 g/L formula.
- The generated record is stale relative to `data/normalized_yaml/bacterial/half_strength_heart_infusion_agar.yaml`, which now has the 1000 ml water row, the BD-Difco Heart infusion broth product qualifier, a Togo M97 reference, and `ingredients_curated` / `has_ontology_mappings` / `has_unmapped_ingredients` flags.
- `Heart Infusion Broth` is ungrounded in the generated record.

## Findings

- Major: `kg_microbe_match` points to unrelated DSMZ Medium 12, Soil Extract Medium.
- Minor: The source-equivalent Togo `M97` / `JCM_M105` import remains split from the direct JCM/MediaDive `J105` import.
- Minor: The generated output is stale relative to the September 2026 normalized-parent repair.

## Recommended Edits

- Remove the false `kg_microbe_match: mediadive.medium:12` assignment from this JCM 105 record.
- Regenerate `data/merge_yaml/merged/half_strength_heart_infusion_agar__c6723b0c.yaml` so it carries the curated September 2026 normalized-parent data.
- Add source-equivalence handling so `TOGO:M97` / `JCM_M105` merges with direct `mediadive.medium:J105`.

## Follow-up Checks

- After regeneration, verify that JCM 105 retains 12.5 g/L Heart infusion broth, 15 g/L agar, the Togo M97 reference, and no DSMZ 12 match.

## Additional Notes

- None found.
