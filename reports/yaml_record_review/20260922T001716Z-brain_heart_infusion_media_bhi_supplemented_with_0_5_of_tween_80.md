# YAML Record Review: Brain-heart-infusion media (BHI) supplemented with 0.5% of Tween 80

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/brain_heart_infusion_media_bhi_supplemented_with_0_5_of_tween_80.yaml
- Started UTC: 2026-09-22T00:17:16Z
- Finished UTC: 2026-09-22T00:18:40Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009424 |
| Label | Brain-heart-infusion media (BHI) supplemented with 0.5% of Tween 80 |
| Source accession | TOGO:M2889 |
| Merge source | data/normalized_yaml/bacterial/brain_heart_infusion_media_bhi_supplemented_with_0_5_of_tween_80.yaml |
| Generated status | Generated merge with one normalized owner |
| Merge fingerprint | 45e2878ba355564f97228e36dbd8810f20d8093cd4d9a4caeead7e4b931d14be |

The reviewed file is the generated TOGO M2889 BHI plus Tween 80 record. Future
fixes belong in the normalized owner named above or in the TOGO water-unit and
commercial-BHI expansion paths that populated it.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/brain_heart_infusion_media_bhi_supplemented_with_0_5_of_tween_80.yaml` | Passed |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/brain_heart_infusion_media_bhi_supplemented_with_0_5_of_tween_80.yaml --out /private/tmp/brain_heart_infusion_media_bhi_supplemented_with_0_5_of_tween_80.strict.tsv --workers 1 --quiet` | Passed with 0 error rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/brain_heart_infusion_media_bhi_supplemented_with_0_5_of_tween_80.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/brain_heart_infusion_media_bhi_supplemented_with_0_5_of_tween_80.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` gate validates standalone records under `history/`, not embedded `MediaRecipe.curation_history` entries in one merge file |

The direct `just validate-schema`, `just validate-strict`, and
`just validate-terms` recipes were not rerun for this record because project
environment creation currently stops while building `llvmlite==0.46.0` under
Python 3.13. The equivalent narrow validators above were run in a no-project
Python 3.11 tool environment.

## Identity and Grounding

- `TOGO:M2889` identifies HiMedia BHI medium supplemented with 0.5% Tween 80.
- TOGO M2889 lists 1000 ml distilled water, 0.5% Tween 80, and 37 g BHI from
  HiMedia.
- TOGO M2889 records pH `7.4+/-0.2`.
- The underlying Scientific Reports paper, DOI `10.1038/s41598-019-52695-4` /
  PMID 31705053, uses this liquid culture for Corynebacterium pseudotuberculosis
  strains at 37 C for 20 h under rotation.
- A gitignore-independent exact search for `TOGO:M2889`,
  `CultureMech:009424`, the merge fingerprint, and the normalized slug covered
  generated records, normalized records, local indexes, reports, source,
  scripts, `justfile`, and `.claude`; it found the single M2889 normalized
  owner and the single generated record.

The generated record identifies the M2889 source correctly and grounds Tween 80
to polysorbate 80. It does not preserve the HiMedia BHI base, water unit, pH,
or source-paper culture context.

## Evidence

TOGO M2889 supports 1000 ml distilled water and 37 g BHI from HiMedia. The
record changes the water volume to `1000 G_PER_L` and replaces the HiMedia BHI
row with inferred BD/Difco/MicrobeNotes constituents.

TOGO M2889 and the source paper support 0.5% Tween 80. They do not state the
percent basis; the record currently narrows it to `PERCENT_W_V` without a
source note preserving that ambiguity.

TOGO M2889 supports pH 7.4+/-0.2, and the paper supports C. pseudotuberculosis
liquid culture at 37 C for 20 h under rotation before genomic DNA extraction.
The record has no structured pH, source reference, target-organism scope, or
preparation/incubation condition.

## Completeness

- Consequential gap: source water is a 1000 ml volume but is stored as
  `1000 G_PER_L`.
- Consequential gap: the 37 g HiMedia BHI premix row is absent and replaced by
  a supplier-inconsistent BD/Difco expansion.
- Consequential gap: the source pH and 37 C / 20 h rotated growth condition are
  absent from structured fields.
- Consequential gap: the C. pseudotuberculosis source scope and DOI/PMID
  reference are absent.
- Minor gap: the bare `0.5%` Tween 80 source unit is asserted as w/v without
  preserving the original ambiguity.
- A gitignore-independent exact search under `reports/yaml_record_review` for
  the normalized slug and the M2889 merge fingerprint found no prior report for
  this target.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Distilled water has the wrong unit. | TOGO M2889 lists 1000 ml distilled water; the record stores `1000 G_PER_L`. | `data/normalized_yaml/bacterial/brain_heart_infusion_media_bhi_supplemented_with_0_5_of_tween_80.yaml`; likely also the TOGO milliliter unit importer |
| Major | The 37 g HiMedia BHI base is replaced by inferred BD/Difco constituents. | TOGO M2889 lists one `BHI (HiMedia)` row at 37 g; it does not assert the expanded calf-brain, beef-heart, proteose-peptone, dextrose, sodium-chloride, and disodium-phosphate rows, and it does not name BD/Difco as the supplier. | `data/normalized_yaml/bacterial/brain_heart_infusion_media_bhi_supplemented_with_0_5_of_tween_80.yaml`; likely also the BHI premix expansion importer |
| Major | Source pH, culture condition, organism scope, and primary citation are missing. | TOGO M2889 carries pH 7.4+/-0.2; Sousa et al. 2019 used this medium for C. pseudotuberculosis strains at 37 C for 20 h under rotation. | `data/normalized_yaml/bacterial/brain_heart_infusion_media_bhi_supplemented_with_0_5_of_tween_80.yaml` |
| Minor | The Tween 80 percent unit is over-specified. | TOGO M2889 and Sousa et al. state `0.5%` Tween 80 without specifying w/v versus v/v; the record stores `PERCENT_W_V`. | `data/normalized_yaml/bacterial/brain_heart_infusion_media_bhi_supplemented_with_0_5_of_tween_80.yaml` |

## Recommended Edits

1. Correct distilled water to a 1000 ml volume row.
2. Restore 37 g `BHI (HiMedia)` as an opaque premix row and remove the
   unsupported BD/Difco constituent expansion.
3. Add pH 7.4+/-0.2.
4. Add the Sousa et al. DOI/PMID/PMC reference and C. pseudotuberculosis growth
   scope.
5. Add the 37 C / 20 h rotation growth condition.
6. Preserve the Tween 80 unit ambiguity unless the source can disambiguate it.
7. Regenerate merged YAML after the normalized owner or importer is fixed.

## Follow-up Checks

- Rerun focused schema, strict, reference, and term validators on the corrected
  normalized M2889 owner.
- Rerun `just validate` after the project `llvmlite` build issue is resolved.
- Regenerate merges and verify the M2889 generated record preserves 1000 ml
  water, 37 g HiMedia BHI, and 0.5% Tween 80.
- Manually compare the regenerated record against the TOGO M2889 API payload
  and the methods section of Sousa et al. 2019.

## Additional Notes

- The full source was inspected through Europe PMC XML for PMCID PMC6841979.
