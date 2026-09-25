# YAML Record Review: half_strength_skim_milk_agar

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/half_strength_skim_milk_agar__878456b7.yaml
- Started UTC: 2026-09-23T09:11:44Z
- Finished UTC: 2026-09-23T09:14:05Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:002250 |
| Name | half_strength_skim_milk_agar |
| Original name | HALF STRENGTH SKIM MILK AGAR |
| Category | bacterial |
| Generated path | data/merge_yaml/merged/half_strength_skim_milk_agar__878456b7.yaml |
| Maintained parent | data/normalized_yaml/bacterial/half_strength_skim_milk_agar.yaml |
| Merge fingerprint | 878456b783b4eabecf41b53e2a51906fe58ab58d07c10ba0a400e59cea297bae |

This is the generated August 2026 merge product for MediaDive/JCM medium `J106`.
Future record edits belong in `data/normalized_yaml/bacterial/half_strength_skim_milk_agar.yaml`
or in the merge and external-match generation logic, then `data/merge_yaml/merged/`
should be regenerated.

## Validation

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/half_strength_skim_milk_agar__878456b7.yaml` | Passed |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/half_strength_skim_milk_agar__878456b7.yaml --out /private/tmp/half_strength_skim_milk_agar_878456b7.strict.tsv --workers 1 --quiet` | Passed with 0 error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/half_strength_skim_milk_agar__878456b7.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/half_strength_skim_milk_agar__878456b7.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not checked | The repository's documented `just validate-history` check validates standalone files under `history/`; this generated MediaRecipe carries only embedded `curation_history` |

`just` validators were not used because this project currently resolves `llvmlite==0.46.0`
under Python 3.13 and fails inside setuptools before the record can be validated.

## Identity and Grounding

- `media_term` is correctly grounded to `mediadive.medium:J106` labeled `HALF
  STRENGTH SKIM MILK AGAR`.
- MediaDive `J106` reports source `JCM` and links to JCM `GRMD=106`.
- The live JCM `GRMD=106` page identifies medium 106 as `HALF STRENGTH SKIM MILK
  AGAR`, with Solution A and Solution B mixed after separate autoclaving.
- Togo M98 is the same recipe by source identity: its API metadata reports
  `original_media_id: JCM_M106` and `src_url` equal to the same JCM `GRMD=106`
  URL. The Togo import is still split into
  `data/normalized_yaml/bacterial/TOGO_M98_Half_Strength_Skim_Milk_Agar.yaml`
  and generated `data/merge_yaml/merged/HALF_STRENGTH_SKIM_MILK_AGAR.yaml`.
- `kg_microbe_match: mediadive.medium:12` is a false cross-source match.
  MediaDive numeric medium `12` is DSMZ `SOIL EXTRACT MEDIUM`, not JCM `J106`.

## Evidence

Supported by inspected sources:

- JCM `GRMD=106`, MediaDive `J106`, and Togo M98 support the JCM 106 identity and
  two 500 ml sub-solutions.
- JCM and MediaDive support 25 g Skim milk (BD-Difco) plus 500 ml distilled
  water in Solution A.
- JCM and MediaDive support 20 g agar plus 500 ml distilled water in Solution B.
- JCM and MediaDive support adjusting Solution A to pH 7.0, autoclaving
  Solutions A and B separately, and mixing aseptically.
- CHEBI `CHEBI:2509` is the correct grounding for agar.

Unsupported, stale, or over-scoped in this generated record:

- The flat ingredient list gives the stock concentrations, 50 g/L skim milk and
  40 g/L agar, as if they were final-medium concentrations. After the two 500 ml
  solutions are mixed, the final 1 L medium contains 25 g/L skim milk and
  20 g/L agar.
- The generated record drops the two 500 ml distilled-water rows and loses the
  Solution A/Solution B boundaries that determine the dilution and separate
  sterilization.
- `Skim milk` has lost the source qualifier `(BD-Difco)` in this generated
  output.
- `kg_microbe_match: mediadive.medium:12` is unsupported because MediaDive 12 is
  DSMZ Soil Extract Medium.

## Completeness

- The maintained September parent correctly replaced the flattened ingredients
  with explicit nested `Solution A` and `Solution B` recipes, each added at
  500 ml/L.
- This generated record is stale relative to
  `data/normalized_yaml/bacterial/half_strength_skim_milk_agar.yaml` and must be
  regenerated before the nested-solution repair, JCM reference, sterilization
  block, source-scoped notes, and data-quality flags are published.
- The source-equivalent Togo M98 record is still split from this MediaDive/JCM
  record; an exact `rg --no-ignore --hidden` search for
  `JCM_M106\b|GRMD=106\b|mediadive\.medium:J106\b` across `data/merge_yaml` and
  `data/normalized_yaml` found only the direct MediaDive/JCM parent plus the
  Togo M98 normalized and generated records.
- The Togo M98 parent also needs repair before equivalence merging because its
  two solution references are encoded as `500 G_PER_L` instead of 500 ml/L.
- Empty organism-specific growth slots are acceptable; this source recipe does
  not assert a narrow strain growth observation.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated recipe doubles the final skim milk and agar concentrations by flattening sub-solution concentrations. | JCM 106 uses 25 g skim milk in 500 ml Solution A and 20 g agar in 500 ml Solution B, mixed to 1 L final volume; the generated record lists 50 g/L skim milk and 40 g/L agar as final ingredients. | Regenerate `data/merge_yaml/merged/` from the repaired nested-solution parent `data/normalized_yaml/bacterial/half_strength_skim_milk_agar.yaml`. |
| Major | The generated record omits the Solution A/Solution B boundaries and water rows required to execute the protocol. | JCM, MediaDive, and Togo all carry two 500 ml solutions; the generated record has no `solutions` array and no distilled-water entries. | Regenerate from the September repaired parent, which models the two nested solutions explicitly. |
| Major | `kg_microbe_match` points to a different medium. | The record says `kg_microbe_match: mediadive.medium:12`; MediaDive numeric medium 12 is DSMZ `SOIL EXTRACT MEDIUM`, while this record is JCM/MediaDive `J106` `HALF STRENGTH SKIM MILK AGAR`. | Refresh or repair the external match generation that writes `kg_microbe_match`, then regenerate `data/merge_yaml/merged/`. |
| Major | The Togo M98 source-equivalent record remains split under a separate CultureMech ID and merge fingerprint. | `data/normalized_yaml/bacterial/TOGO_M98_Half_Strength_Skim_Milk_Agar.yaml` names Togo `M98`, `Original source: JCM - JCM_M106`, and the same JCM `GRMD=106` URL; the Togo API confirms `original_media_id: JCM_M106`. | Add a source equivalence or merge-key repair so Togo M98 and MediaDive/JCM J106 collapse into one generated record, then regenerate. |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/` so this output uses the maintained
   September nested-solution representation from
   `data/normalized_yaml/bacterial/half_strength_skim_milk_agar.yaml`.
2. Remove or recompute the stale `kg_microbe_match: mediadive.medium:12` value
   in the match-generation input or overlay that owns generated
   `kg_microbe_match` values.
3. Add a source-identity merge rule or equivalence overlay for Togo M98 and
   MediaDive/JCM J106.
4. Repair the Togo M98 parent so the two solution references are 500 ml/L
   additions instead of `500 G_PER_L` before it participates in the
   source-equivalence merge.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation on the regenerated
  `half_strength_skim_milk_agar` output.
- Inspect the regenerated YAML and confirm it has nested 500 ml/L Solution A and
  Solution B entries, final-medium pH 7.0, the separate autoclave instruction,
  no flat 50 g/L skim milk or 40 g/L agar rows, and no `kg_microbe_match` to
  `mediadive.medium:12`.
- Search `data/merge_yaml/merged` for exact `JCM_M106`, `GRMD=106`, Togo `M98`,
  and `mediadive.medium:J106` tokens with `rg --no-ignore --hidden`; after
  equivalence repair they should identify one merged source recipe group.
- Re-fetch MediaDive `J106`, the JCM `GRMD=106` page, and Togo M98 to confirm
  the regenerated nested solutions still match the live source records.

## Additional Notes

- The JCM `GRMD=106` live page was reachable and agreed with MediaDive `J106`.
- Keeping Skim milk (BD-Difco) opaque and unmapped is appropriate; this is a
  complex BD-Difco product, and the maintained parent records
  `has_unmapped_ingredients`.
