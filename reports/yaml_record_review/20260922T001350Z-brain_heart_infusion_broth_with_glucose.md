# YAML Record Review: brain-heart infusion broth (with glucose)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/brain_heart_infusion_broth_with_glucose.yaml
- Started UTC: 2026-09-22T00:13:50Z
- Finished UTC: 2026-09-22T00:14:55Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009375 |
| Label | brain-heart infusion broth (with glucose) |
| Source accession | TOGO:M2830 |
| Merge source | data/normalized_yaml/bacterial/brain_heart_infusion_broth_with_glucose.yaml |
| Generated status | Generated merge with one normalized owner; stale relative to its owner |
| Merge fingerprint | 543a2ea20e3883010a99fc469f7cd3903eafa69565aa198e4f4ea1ccad472b87 |

The reviewed file is the generated TOGO M2830 BHI-glucose record. Its
normalized owner already contains a later formulation repair, but the owner
still carries an unrelated `kg_microbe_match` that future curation should remove
before regenerating derived YAML.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/brain_heart_infusion_broth_with_glucose.yaml` | Passed |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/brain_heart_infusion_broth_with_glucose.yaml --out /private/tmp/brain_heart_infusion_broth_with_glucose.strict.tsv --workers 1 --quiet` | Passed with 0 error rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/brain_heart_infusion_broth_with_glucose.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/brain_heart_infusion_broth_with_glucose.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` gate validates standalone records under `history/`, not embedded `MediaRecipe.curation_history` entries in one merge file |

The direct `just validate-schema`, `just validate-strict`, and
`just validate-terms` recipes were not rerun for this record because project
environment creation currently stops while building `llvmlite==0.46.0` under
Python 3.13. The equivalent narrow validators above were run in a no-project
Python 3.11 tool environment.

## Identity and Grounding

- `TOGO:M2830` identifies BHI broth from Difco with glucose added to 0.1% and
  shaken cultivation for 18-20 h at 36 C.
- TOGO M2830 lists 0.1% glucose and 1 L brain-heart infusion broth from Difco.
- The local `repair_togo_m17_bhi_score20.py` script rewrote the normalized owner
  on 2026-09-10 to store the BHI base as `1000 ML_PER_L`, preserve source
  notes, record 36 C cultivation, and add a TOGO reference.
- The generated record was emitted on 2026-08-06, before that repair, and still
  stores the 1 L BHI base as `1 G_PER_L`.
- The generated record and its normalized owner both still carry
  `kg_microbe_match: mediadive.medium:21`, which resolves to DSMZ Medium 21 /
  SARCINA MEDIUM, not to TOGO M2830.
- A gitignore-independent exact search for `TOGO:M2830`,
  `CultureMech:009375`, `mediadive.medium:21`, the merge fingerprint, and the
  normalized slug covered generated records, normalized records, local indexes,
  reports, source, scripts, `justfile`, and `.claude`; it found the single M2830
  normalized owner, the stale generated record, the focused repair script, and
  the maintained Sarcina record for MediaDive 21.

The record's TOGO identity is correct, but the generated artifact is stale
relative to its corrected owner and the remaining `kg_microbe_match` links it
to an unrelated DSMZ formulation.

## Evidence

TOGO M2830 supports 0.1% glucose and 1 L brain-heart infusion broth from Difco.
The generated record preserves the glucose row but stores the BHI base as
`1 G_PER_L`; the normalized owner has already corrected that row to
`1000 ML_PER_L`.

The TOGO comment supports shaking the culture for 18-20 h at 36 C. The
normalized owner records that temperature and two preparation steps, but the
generated merge lacks them because it predates the 2026-09-10 owner repair.

MediaDive medium 21 is SARCINA MEDIUM with glucose, peptone, yeast extract, pH
6.0, and no BHI base. The M2830 `kg_microbe_match: mediadive.medium:21` is
therefore an unrelated cross-source link.

## Completeness

- Consequential gap: the generated 1 L BHI base is stored as `1 G_PER_L`.
- Consequential gap: the generated record lacks the owner record's TOGO
  reference, source notes, 36 C temperature, preparation steps, and quality
  flags.
- Consequential gap: the generated record and normalized owner still link TOGO
  M2830 to unrelated DSMZ Medium 21.
- A gitignore-independent exact search under `reports/yaml_record_review` for
  the normalized slug and the M2830 merge fingerprint found no prior report for
  this target.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated merge is stale relative to the maintained owner. | The generated record was emitted on 2026-08-06 and stores the TOGO 1 L BHI component as `1 G_PER_L`; the owner has a 2026-09-10 `RESOLVED_TOGO_M17_BHI_SCORE20` event and stores that row as `1000 ML_PER_L` with TOGO source notes and preparation steps. | Merge generator / generated `data/merge_yaml/merged` outputs after `data/normalized_yaml/bacterial/brain_heart_infusion_broth_with_glucose.yaml` is corrected |
| Major | The record is linked to unrelated DSMZ Medium 21. | The `kg_microbe_match` points to `mediadive.medium:21`, which is SARCINA MEDIUM with glucose, peptone, yeast extract, and pH 6.0 rather than BHI broth plus 0.1% glucose. | `data/normalized_yaml/bacterial/brain_heart_infusion_broth_with_glucose.yaml` |

## Recommended Edits

1. Remove `kg_microbe_match: mediadive.medium:21` from
   `data/normalized_yaml/bacterial/brain_heart_infusion_broth_with_glucose.yaml`.
2. Preserve the existing normalized-owner representation of the TOGO 1 L BHI
   base as `1000 ML_PER_L`.
3. Regenerate `data/merge_yaml/merged/brain_heart_infusion_broth_with_glucose.yaml`
   from the corrected normalized owner.
4. Preserve the owner record's TOGO reference, source notes, 36 C temperature,
   BHI-glucose preparation steps, data-quality flags, and
   `RESOLVED_TOGO_M17_BHI_SCORE20` history event in the regenerated merge.

## Follow-up Checks

- Rerun focused schema, strict, reference, and term validators on the corrected
  normalized M2830 owner.
- Rerun `just validate` after the project `llvmlite` build issue is resolved.
- Regenerate merges and verify the M2830 generated record has no
  `kg_microbe_match`.
- Manually compare the regenerated file against the TOGO M2830 API payload.

## Additional Notes

- The TOGO source comment has spelling and punctuation artifacts in the word
  glucose and in `0.1%`; the structured TOGO component table confirms the
  intended glucose concentration.
