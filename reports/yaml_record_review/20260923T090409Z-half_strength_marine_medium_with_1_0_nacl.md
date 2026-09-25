# YAML Record Review: half_strength_marine_medium_with_1_0_nacl

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/half_strength_marine_medium_with_1_0_nacl.yaml
- Started UTC: 2026-09-23T09:02:22Z
- Finished UTC: 2026-09-23T09:04:09Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:010197 |
| Name | half_strength_marine_medium_with_1_0_nacl |
| Original name | Half Strength Marine Medium With 1.0% NaCl |
| Category | bacterial |
| Generated path | data/merge_yaml/merged/half_strength_marine_medium_with_1_0_nacl.yaml |
| Maintained parent | data/normalized_yaml/bacterial/half_strength_marine_medium_with_1_0_nacl.yaml |
| Merge fingerprint | 9c7a498b629cda1c34b1f14392b9e5de8200611f299194e436551f9387a48ba9 |

This is the generated August 2026 merge product for Togo Medium M788, which
Togo imported from JCM `JCM_M762`. Future edits belong in the Togo normalized
parent, in the Togo importer/unit normalization, or in the source-equivalence
merge logic; `data/merge_yaml/merged/` should then be regenerated.

## Validation

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/half_strength_marine_medium_with_1_0_nacl.yaml` | Passed |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/half_strength_marine_medium_with_1_0_nacl.yaml --out /private/tmp/half_strength_marine_medium_with_1_0_nacl.strict.tsv --workers 1 --quiet` | Passed with 0 error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/half_strength_marine_medium_with_1_0_nacl.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/half_strength_marine_medium_with_1_0_nacl.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not checked | The repository's documented `just validate-history` check validates standalone files under `history/`; this generated MediaRecipe carries only embedded `curation_history` |

`just` validators were not used because this project currently resolves `llvmlite==0.46.0`
under Python 3.13 and fails inside setuptools before the record can be validated.

## Identity and Grounding

- The target `media_term` identifies Togo `M788`, labeled `Half Strength Marine
  Medium With 1.0% NaCl`.
- Togo M788 metadata reports `original_media_id: JCM_M762` and links back to
  the same JCM `GRMD=762` source named by this record.
- The live JCM `GRMD=762` page identifies medium 762 as `HALF STRENGTH MARINE
  MEDIUM WITH 1.0% NaCl` and lists 18.7 g Marine broth 2216 (BD-Difco), 10.0 g
  NaCl, and 1.0 L distilled water.
- MediaDive `J762` is a direct JCM import of the same recipe. It remains split
  into generated record
  `data/merge_yaml/merged/half_strength_marine_medium_with_1_0_nacl__70db091e.yaml`
  and maintained parent
  `data/normalized_yaml/specialized/half_strength_marine_medium_with_1_0_nacl.yaml`.
- The target record's NaCl CHEBI grounding is correct. Marine broth 2216
  remains ungrounded, which is acceptable for this complex BD-Difco product
  until an exact local term is available.

## Evidence

Supported by inspected sources:

- Togo M788 supports the target Togo accession, recipe label, original JCM
  source ID, and original JCM source URL.
- Togo M788 and JCM `GRMD=762` support the three-component recipe: distilled
  water, 10 g NaCl, and 18.7 g Marine broth 2216 (BD-Difco).
- JCM `GRMD=762` and MediaDive `J762` support the direct source-equivalent
  JCM recipe already present in
  `data/normalized_yaml/specialized/half_strength_marine_medium_with_1_0_nacl.yaml`.
- CHEBI `CHEBI:26710` is the correct grounding for the NaCl/sodium chloride
  ingredient; CHEBI `CHEBI:15377` is the correct grounding for distilled water.

Unsupported, stale, or incomplete in this generated record:

- `Distilled water` is encoded as `1 G_PER_L`, but Togo M788 and JCM `GRMD=762`
  specify 1 L water, not 1 g/L water.
- The JCM source's default autoclave-at-121-C-for-15-min instruction is missing
  from the Togo-derived record.
- This Togo record is not merged with the direct MediaDive/JCM `J762` record,
  even though both cite the same original JCM medium.

## Completeness

- The target has the source label, TOGO accession, original JCM accession, JCM
  source URL, and all three ingredient names.
- The target is not complete enough to execute as written because the water row
  has a mass concentration unit rather than the source volume and because the
  JCM sterilization instruction is absent.
- The source-equivalent MediaDive/JCM `J762` record has already been repaired
  in `data/normalized_yaml/specialized/half_strength_marine_medium_with_1_0_nacl.yaml`
  with 1000 ml/L water, source-level ingredient notes, the JCM reference,
  preparation steps, sterilization, and data-quality flags.
- An exact `rg --no-ignore --hidden` search for
  `JCM_M762\b|GRMD=762\b|TOGO:M788\b` across `data/merge_yaml` and
  `data/normalized_yaml` found this Togo record and the direct JCM/MediaDive
  sibling only; the two source-equivalent parents remain split.
- Empty organism-specific growth slots are acceptable; this source recipe does
  not assert a narrow strain growth observation.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Distilled water is imported with the wrong unit. | Togo M788 reports `Distilled water` with `volume: 1` and `unit: L`, while the generated YAML writes `value: '1'` and `unit: G_PER_L`. | `data/normalized_yaml/bacterial/half_strength_marine_medium_with_1_0_nacl.yaml` or the Togo import/unit-normalization transform. |
| Major | The Togo-derived record is missing the JCM default sterilization step. | The JCM `GRMD=762` page states the default 121 C for 15 min autoclave instruction; this generated record has no `preparation_steps` or `sterilization`. | Add the step in the maintained Togo parent or merge this record into the already repaired JCM/MediaDive parent, then regenerate. |
| Major | Togo M788 and MediaDive/JCM J762 remain split into separate generated records. | Togo M788 has `original_media_id: JCM_M762` and JCM `GRMD=762`; MediaDive `J762` links to the same JCM page and has the same ingredient list. | Add a source-equivalence or merge-key repair so Togo M788 and MediaDive/JCM J762 collapse into one generated record, then regenerate. |

## Recommended Edits

1. Fix the Togo M788 parent so `Distilled water` is represented as 1 L per
   liter, not 1 g/L.
2. Add the JCM default autoclave instruction for the Togo-derived parent, or
   merge this source with the already repaired direct JCM/MediaDive `J762`
   normalized record.
3. Add a source-identity merge rule or equivalence overlay for Togo M788 and
   MediaDive/JCM J762.
4. Regenerate `data/merge_yaml/merged/` and confirm only one
   `half_strength_marine_medium_with_1_0_nacl` generated recipe remains for
   JCM `GRMD=762`.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation on the regenerated
  output.
- Inspect the regenerated YAML and confirm it carries 18.7 g/L Marine broth
  2216 (BD-Difco), 10 g/L NaCl, 1000 ml/L distilled water, and the default JCM
  autoclave instruction.
- Search `data/merge_yaml/merged` for exact `JCM_M762`, `GRMD=762`, Togo
  `M788`, and `mediadive.medium:J762` tokens with `rg --no-ignore --hidden`;
  after equivalence repair they should identify one merged source recipe group.
- Re-fetch Togo M788, JCM `GRMD=762`, and MediaDive `J762` to confirm the
  regenerated ingredients still match the live source records.

## Additional Notes

- The direct JCM/MediaDive generated sibling
  `data/merge_yaml/merged/half_strength_marine_medium_with_1_0_nacl__70db091e.yaml`
  has a stale `kg_microbe_match: mediadive.medium:74`; MediaDive numeric medium
  74 is DSMZ `THERMUS THERMOPHILUS MEDIUM`, not JCM `J762`.
- The maintained direct JCM/MediaDive parent has the same stale
  `kg_microbe_match`. That generated external match should be recomputed before
  or during source-equivalence merge.
