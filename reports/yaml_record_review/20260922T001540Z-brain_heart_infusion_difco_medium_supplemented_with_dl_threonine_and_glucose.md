# YAML Record Review: Brain heart infusion (Difco) medium supplemented with DL-threonine and glucose

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/brain_heart_infusion_difco_medium_supplemented_with_dl_threonine_and_glucose.yaml
- Started UTC: 2026-09-22T00:15:40Z
- Finished UTC: 2026-09-22T00:16:30Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009442 |
| Label | Brain heart infusion (Difco) medium supplemented with DL-threonine and glucose |
| Source accession | TOGO:M2904 |
| Merge source | data/normalized_yaml/bacterial/brain_heart_infusion_difco_medium_supplemented_with_dl_threonine_and_glucose.yaml |
| Generated status | Generated merge with one normalized owner |
| Merge fingerprint | f5a82cfd5a13677e0c8c370d34df9012420ab5089a339618f53e52b9eefc603d |

The reviewed file is the generated TOGO M2904 BHI / DL-threonine / glucose
record. Future fixes belong in the normalized owner named above or in the
commercial-BHI expansion path that populated it.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/brain_heart_infusion_difco_medium_supplemented_with_dl_threonine_and_glucose.yaml` | Passed |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/brain_heart_infusion_difco_medium_supplemented_with_dl_threonine_and_glucose.yaml --out /private/tmp/brain_heart_infusion_difco_medium_supplemented_with_dl_threonine_and_glucose.strict.tsv --workers 1 --quiet` | Passed with 0 error rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/brain_heart_infusion_difco_medium_supplemented_with_dl_threonine_and_glucose.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/brain_heart_infusion_difco_medium_supplemented_with_dl_threonine_and_glucose.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` gate validates standalone records under `history/`, not embedded `MediaRecipe.curation_history` entries in one merge file |

The direct `just validate-schema`, `just validate-strict`, and
`just validate-terms` recipes were not rerun for this record because project
environment creation currently stops while building `llvmlite==0.46.0` under
Python 3.13. The equivalent narrow validators above were run in a no-project
Python 3.11 tool environment.

## Identity and Grounding

- `TOGO:M2904` identifies Brain Heart Infusion (Difco) medium supplemented with
  DL-threonine and glucose.
- TOGO M2904 lists 20 mM DL-threonine, 10 mM glucose, and 1 L Brain Heart
  Infusion (Difco) medium.
- A gitignore-independent exact search for `TOGO:M2904`,
  `CultureMech:009442`, the merge fingerprint, and the normalized slug covered
  generated records, normalized records, local indexes, reports, source,
  scripts, `justfile`, and `.claude`; it found the single M2904 normalized
  owner and the single generated record.

The generated record identifies the TOGO M2904 source correctly, and the
DL-threonine and glucose concentrations are source-supported. The 1 L BHI base
is not preserved as a source component.

## Evidence

TOGO M2904 supports 20 mM DL-threonine and 10 mM glucose as simple final
supplements.

TOGO M2904 lists 1 L Brain Heart Infusion (Difco) medium as the complex base.
It does not list calf-brain, beef-heart, proteose-peptone, dextrose,
sodium-chloride, or disodium-phosphate rows with MicrobeNotes/BD catalog
metadata.

The TOGO comment mentions erythromycin only for transformants; erythromycin is
conditional and correctly absent from the baseline BHI / DL-threonine / glucose
formulation.

## Completeness

- Consequential gap: the 1 L BHI base is absent and replaced by an unsupported
  expansion.
- Consequential gap: the record has no reference to the primary publication
  behind the TOGO excerpt.
- Follow-up gap: DL-threonine is mapped to the generic `CHEBI:26986` threonine
  term; confirm whether a more stereochemically precise DL-threonine CHEBI term
  exists before changing the grounding.
- A gitignore-independent exact search under `reports/yaml_record_review` for
  the normalized slug and the M2904 merge fingerprint found no prior report for
  this target.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The 1 L BHI base is replaced by inferred constituents. | TOGO M2904 lists one 1 L Brain Heart Infusion (Difco) medium row; it does not directly assert the expanded calf-brain, beef-heart, proteose-peptone, dextrose, sodium-chloride, and disodium-phosphate rows. | `data/normalized_yaml/bacterial/brain_heart_infusion_difco_medium_supplemented_with_dl_threonine_and_glucose.yaml`; likely also the BHI premix expansion importer |
| Minor | The source paper behind the TOGO excerpt is missing. | TOGO M2904 stores a methods excerpt but no `src_url`; the record has no primary-paper DOI, PMID, or URL in `references`. | `data/normalized_yaml/bacterial/brain_heart_infusion_difco_medium_supplemented_with_dl_threonine_and_glucose.yaml` |

## Recommended Edits

1. Restore the 1 L Brain Heart Infusion (Difco) medium base as an opaque row and
   remove the unsupported MicrobeNotes/BD constituent expansion.
2. Search for the paper behind the TOGO M2904 methods excerpt and add a narrow
   reference if it can be identified.
3. Verify whether DL-threonine can be grounded more precisely than generic
   threonine.
4. Regenerate merged YAML after the normalized owner or importer is fixed.

## Follow-up Checks

- Rerun focused schema, strict, reference, and term validators on the corrected
  normalized M2904 owner.
- Rerun `just validate` after the project `llvmlite` build issue is resolved.
- Regenerate merges and verify the M2904 generated record preserves the 20 mM
  DL-threonine, 10 mM glucose, and opaque 1 L BHI base rows.
- Manually compare the regenerated record against the TOGO M2904 API payload.

## Additional Notes

- The organism identity behind "Wild-type 57.I" and "Emr transformants" was not
  resolved from the TOGO payload alone.
