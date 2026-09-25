# YAML Record Review: half_strength_marine_medium_with_1_0_nacl

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/half_strength_marine_medium_with_1_0_nacl__70db091e.yaml
- Started UTC: 2026-09-23T09:05:22Z
- Finished UTC: 2026-09-23T09:06:03Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:015420 |
| Name | half_strength_marine_medium_with_1_0_nacl |
| Original name | HALF STRENGTH MARINE MEDIUM WITH 1.0% NaCl |
| Category | specialized |
| Generated path | data/merge_yaml/merged/half_strength_marine_medium_with_1_0_nacl__70db091e.yaml |
| Maintained parent | data/normalized_yaml/specialized/half_strength_marine_medium_with_1_0_nacl.yaml |
| Merge fingerprint | 70db091ef6ebae7d5dfa3ba5485060678fc282c3509672fc20c7829e570e0fde |

This is the generated August 2026 merge product for MediaDive/JCM medium `J762`.
Future record edits belong in `data/normalized_yaml/specialized/half_strength_marine_medium_with_1_0_nacl.yaml`
or in the merge and external-match generation logic, then `data/merge_yaml/merged/`
should be regenerated.

## Validation

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/half_strength_marine_medium_with_1_0_nacl__70db091e.yaml` | Passed |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/half_strength_marine_medium_with_1_0_nacl__70db091e.yaml --out /private/tmp/half_strength_marine_medium_with_1_0_nacl_70db091e.strict.tsv --workers 1 --quiet` | Passed with 0 error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/half_strength_marine_medium_with_1_0_nacl__70db091e.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/half_strength_marine_medium_with_1_0_nacl__70db091e.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not checked | The repository's documented `just validate-history` check validates standalone files under `history/`; this generated MediaRecipe carries only embedded `curation_history` |

`just` validators were not used because this project currently resolves `llvmlite==0.46.0`
under Python 3.13 and fails inside setuptools before the record can be validated.

## Identity and Grounding

- `media_term` is correctly grounded to `mediadive.medium:J762` labeled `HALF
  STRENGTH MARINE MEDIUM WITH 1.0% NaCl`.
- MediaDive `J762` reports source `JCM` and links to JCM `GRMD=762`.
- The live JCM `GRMD=762` page identifies medium 762 as `HALF STRENGTH MARINE
  MEDIUM WITH 1.0% NaCl` and gives the same three components as the maintained
  normalized parent: `Marine broth 2216 (BD-Difco)` 18.7 g, `NaCl` 10.0 g, and
  `Distilled water` 1.0 L.
- Togo M788 is the same recipe by source identity: its API metadata reports
  `original_media_id: JCM_M762` and `src_url` equal to the same JCM `GRMD=762`
  URL. The Togo import is still split into
  `data/normalized_yaml/bacterial/half_strength_marine_medium_with_1_0_nacl.yaml`
  and generated `data/merge_yaml/merged/half_strength_marine_medium_with_1_0_nacl.yaml`.
- `kg_microbe_match: mediadive.medium:74` is a false cross-source match.
  MediaDive numeric medium `74` is DSMZ `THERMUS THERMOPHILUS MEDIUM`, not JCM
  `J762`.

## Evidence

Supported by inspected sources:

- JCM `GRMD=762` and MediaDive `J762` support the ID, label, JCM source link,
  complex medium classification, and liquid state.
- MediaDive `J762` supports 18.7 g/L Marine broth 2216 with the `BD-Difco`
  attribute, 10 g/L NaCl, and 1000 ml distilled water per liter.
- JCM `GRMD=762` supports 18.7 g Marine broth 2216 (BD-Difco), 10.0 g NaCl, and
  1.0 L distilled water.
- The JCM page states its default sterilization rule is autoclaving media at
  121 C for 15 min unless otherwise stated; this supports the normalized
  parent's autoclave step.
- Togo M788 supports the same 1 L water, 10 g NaCl, and 18.7 g Marine broth
  2216 (BD-Difco) recipe, but through the Togo projection of JCM M762.
- CHEBI `CHEBI:26710` is the correct grounding for the NaCl/sodium chloride
  ingredient.

Unsupported, stale, or over-scoped in this generated record:

- The generated ingredient list omits the 1.0 L distilled water component that
  JCM, MediaDive, Togo, and the September maintained parent all carry.
- `Marine broth 2216` has lost the source qualifier `(BD-Difco)` in this
  generated output.
- `kg_microbe_match: mediadive.medium:74` is unsupported because MediaDive 74 is
  DSMZ Thermus Thermophilus Medium.
- The record does not include the JCM reference, ingredient-level source notes,
  preparation steps, sterilization block, or `data_quality_flags` now present in
  its maintained parent.

## Completeness

- The direct JCM/MediaDive recipe is nearly complete in the maintained
  September parent, including the 1 L water row, BD-Difco qualifier, JCM source
  URL, preparation steps, sterilization, and data quality flags.
- This generated record is stale relative to
  `data/normalized_yaml/specialized/half_strength_marine_medium_with_1_0_nacl.yaml`
  and must be regenerated before it can publish those maintained corrections.
- The source-equivalent Togo M788 record is still split from this MediaDive/JCM
  record; an exact `rg --no-ignore --hidden` search for
  `JCM_M762\b|GRMD=762\b|TOGO:M788\b` across `data/merge_yaml` and
  `data/normalized_yaml` found only the direct MediaDive/JCM parent plus the
  Togo M788 normalized and generated records.
- Empty organism-specific growth slots are acceptable; this source recipe does
  not assert a narrow strain growth observation.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated recipe is stale and omits supported water, provenance, preparation, sterilization, and data-quality content already curated in the maintained parent. | The generated August record lists only Marine broth 2216 and NaCl, while the September parent includes 1000 ml/L distilled water, ingredient source notes, `references`, two `preparation_steps`, `sterilization`, and `data_quality_flags`; JCM `GRMD=762` and MediaDive `J762` both support the missing water row. | Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/specialized/half_strength_marine_medium_with_1_0_nacl.yaml`. |
| Major | `kg_microbe_match` points to a different medium. | The record says `kg_microbe_match: mediadive.medium:74`; MediaDive numeric medium 74 is DSMZ `THERMUS THERMOPHILUS MEDIUM`, while this record is JCM/MediaDive `J762` `HALF STRENGTH MARINE MEDIUM WITH 1.0% NaCl`. | Refresh or repair the external match generation that writes `kg_microbe_match`, then regenerate `data/merge_yaml/merged/`. |
| Major | The Togo M788 source-equivalent record remains split under a separate CultureMech ID and merge fingerprint. | `data/normalized_yaml/bacterial/half_strength_marine_medium_with_1_0_nacl.yaml` names Togo `M788`, `Original source: JCM - JCM_M762`, and the same JCM `GRMD=762` URL; the Togo API confirms `original_media_id: JCM_M762`. | Add a source equivalence or merge-key repair so Togo M788 and MediaDive/JCM J762 collapse into one generated record, then regenerate. |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/` so this output includes the maintained
   September repair from
   `data/normalized_yaml/specialized/half_strength_marine_medium_with_1_0_nacl.yaml`:
   distilled water, BD-Difco qualifier, JCM reference, ingredient source notes,
   preparation steps, sterilization, and data quality flags.
2. Remove or recompute the stale `kg_microbe_match: mediadive.medium:74` value
   in the match-generation input or overlay that owns generated
   `kg_microbe_match` values.
3. Add a source-identity merge rule or equivalence overlay for Togo M788 and
   MediaDive/JCM J762 so the Togo M788 import no longer emits as the separate
   unmerged product.
4. Fix the Togo M788 parent water quantity from `1 G_PER_L` to `1000 ML_PER_L`
   or the repository's canonical 1 L/L representation before it participates
   in the source-equivalence merge.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation on the regenerated
  `half_strength_marine_medium_with_1_0_nacl` output.
- Inspect the regenerated YAML and confirm it contains `Distilled water` at the
  JCM-supported final-medium amount, `Marine broth 2216 (BD-Difco)`, the JCM
  `GRMD=762` reference, preparation steps, and no `kg_microbe_match` to
  `mediadive.medium:74`.
- Search `data/merge_yaml/merged` for exact `JCM_M762`, `GRMD=762`, Togo
  `M788`, and `mediadive.medium:J762` tokens with `rg --no-ignore --hidden`;
  after equivalence repair they should identify one merged source recipe group.
- Re-fetch MediaDive `J762`, the JCM `GRMD=762` page, and Togo M788 to confirm
  the regenerated ingredients and source equivalence still match the live
  source records.

## Additional Notes

- The JCM `GRMD=762` live page was reachable and agreed with MediaDive `J762`.
- Marine broth 2216 remains intentionally unmapped in the maintained parent,
  which is acceptable as long as `has_unmapped_ingredients` survives
  regeneration.
