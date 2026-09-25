# YAML Record Review: Brain heart infusion (BHI) broth (Oxoid)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/brain_heart_infusion_bhi_broth_oxoid.yaml
- Started UTC: 2026-09-21T23:53:32Z
- Finished UTC: 2026-09-21T23:54:17Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:008801 |
| Label | Brain heart infusion (BHI) broth (Oxoid) |
| Source accession | TOGO:M2211 |
| Merge source | data/normalized_yaml/bacterial/brain_heart_infusion_bhi_broth_oxoid.yaml |
| Generated status | Generated merge with one normalized owner |
| Merge fingerprint | 8f99b26a68e31b046057353cc2656981a3bf6edb8f7a383f34357dbb8b9dabef |

The reviewed file is generated, and the generated content currently matches its
single normalized owner. Future fixes belong in
`data/normalized_yaml/bacterial/brain_heart_infusion_bhi_broth_oxoid.yaml`
or in the TOGO import and BHI-premix paths that populated it.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/brain_heart_infusion_bhi_broth_oxoid.yaml` | Passed |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/brain_heart_infusion_bhi_broth_oxoid.yaml --out /private/tmp/brain_heart_infusion_bhi_broth_oxoid.strict.tsv --workers 1 --quiet` | Passed with 0 error rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/brain_heart_infusion_bhi_broth_oxoid.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/brain_heart_infusion_bhi_broth_oxoid.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` gate validates standalone records under `history/`, not embedded `MediaRecipe.curation_history` entries in one merge file |

The direct `just validate-schema`, `just validate-strict`, and
`just validate-terms` recipes were not rerun for this record because project
environment creation currently stops while building `llvmlite==0.46.0` under
Python 3.13. The equivalent narrow validators above were run in a no-project
Python 3.11 tool environment.

## Identity and Grounding

- `TOGO:M2211` identifies Brain heart infusion broth (Oxoid).
- TOGO M2211 lists the final medium as 37 g Brain heart infusion broth (Oxoid)
  powder dissolved in 1 L distilled water.
- TOGO also records the Oxoid powder subcomposition: 5 g sodium chloride, 2.5 g
  disodium phosphate, 2 g glucose, 10 g proteose peptone, 5 g beef-heart
  infusion solids, and 12.5 g brain-infusion solids per 37 g powder.
- A gitignore-independent exact search for `TOGO:M2211`,
  `CultureMech:008801`, the merge fingerprint, and the normalized slug covered
  generated records, normalized records, local indexes, reports, source,
  scripts, `justfile`, and `.claude`; it found only this normalized owner and
  this generated merge for the M2211 source accession.

The top-level TOGO identity is correct, but the record flattened an Oxoid
premix, added an unrelated BD/Difco expansion, and converted the liter of water
to grams per liter.

## Evidence

The inspected TOGO M2211 payload supports two top-level rows: 1 L distilled
water and 37 g Brain heart infusion broth (Oxoid). It also supports pH
7.4 +/- 0.2 at 25 C and a preparation step to dissolve 37 g in 1 L distilled
water, mix, distribute, and autoclave at 121 C for 15 min.

The 1 L water row is present but stored as `1 G_PER_L`. The 37 g Oxoid BHI
powder row is absent from the flattened record.

The Oxoid powder subcomposition was copied into final-medium ingredients, and
then generic BD/Difco BHI rows from MicrobeNotes were added on top. That leaves
duplicated sodium chloride, phosphate, glucose/dextrose, proteose peptone, and
heart/brain infusion material, with BD/Difco catalog metadata attached to an
Oxoid medium.

## Completeness

- Consequential gap: the required 37 g Oxoid BHI broth powder row is absent.
- Consequential gap: 1 L distilled water is stored as a mass concentration.
- Consequential gap: the Oxoid powder subcomposition is not kept separate from
  the final medium, so the generated record cannot be followed literally.
- Consequential gap: the pH and sterilization instructions captured by TOGO are
  absent from structured fields.
- A gitignore-independent exact search under `reports/yaml_record_review` for
  the normalized slug and the merge fingerprint found no prior report for this
  target.
- Empty target-organism and growth-evidence slots are acceptable for this
  product-formulation record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The 37 g Brain heart infusion broth (Oxoid) powder row is missing. | TOGO M2211 lists 37 g Oxoid BHI powder in the final liter; the generated and normalized records flatten the powder but omit the actual 37 g row. | `data/normalized_yaml/bacterial/brain_heart_infusion_bhi_broth_oxoid.yaml`; likely also the TOGO subcomponent importer |
| Major | One liter of distilled water was imported as `1 G_PER_L`. | TOGO M2211 lists `Distilled water`, `volume: 1`, `unit: L`; the record stores `value: '1'`, `unit: G_PER_L`. | `data/normalized_yaml/bacterial/brain_heart_infusion_bhi_broth_oxoid.yaml`; likely also the TOGO unit importer |
| Major | Oxoid powder subcomponents and unrelated BD/Difco BHI constituents are both represented as final-medium ingredients. | TOGO provides the internal Oxoid powder composition as a subcomponent; the record also adds BD/Difco calf-brain, beef-heart, proteose-peptone, dextrose, sodium-chloride, and disodium-phosphate rows from MicrobeNotes. | `data/normalized_yaml/bacterial/brain_heart_infusion_bhi_broth_oxoid.yaml`; likely also the BHI premix expansion importer |
| Major | TOGO's pH and sterilization instructions are missing. | The TOGO payload records pH 7.4 +/- 0.2 at 25 C and directs dissolving 37 g in 1 L distilled water, mixing, distributing, and autoclaving at 121 C for 15 min. | `data/normalized_yaml/bacterial/brain_heart_infusion_bhi_broth_oxoid.yaml` |

## Recommended Edits

1. Restore the final formulation as 37 g Brain heart infusion broth (Oxoid) plus
   1 L distilled water.
2. Keep the Oxoid powder composition as a nested/subcomponent description, or
   move it to a linked stock/premix record if the schema cannot represent it
   safely inline.
3. Remove the unsupported BD/Difco MicrobeNotes expansion from this Oxoid
   record.
4. Correct the distilled-water unit to 1 L.
5. Add the TOGO pH and preparation instructions.
6. Regenerate merged YAML after the normalized owner or importer is fixed.

## Follow-up Checks

- Rerun focused schema, strict, reference, and term validators on the corrected
  normalized owner.
- Rerun `just validate` after the project `llvmlite` build issue is resolved.
- Regenerate merges and confirm the final M2211 record has 37 g Oxoid powder
  and 1 L water rather than duplicated final sodium-chloride, phosphate,
  glucose, and proteose-peptone rows.
- Manually compare the regenerated record against the TOGO M2211 API payload.

## Additional Notes

- TOGO M2211 has no upstream `src_url`; an exact web search located an Oxoid
  manual PDF, but its extracted text was too noisy to use as the reviewed
  source for this report.
