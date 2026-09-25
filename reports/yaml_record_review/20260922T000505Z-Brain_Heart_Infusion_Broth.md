# YAML Record Review: Brain Heart Infusion Broth

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/Brain_Heart_Infusion_Broth.yaml
- Started UTC: 2026-09-22T00:05:05Z
- Finished UTC: 2026-09-22T00:06:29Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009009 |
| Label | Brain Heart Infusion Broth |
| Source accession | TOGO:M2426 |
| Merge source | data/normalized_yaml/bacterial/brain_heart_infusion_broth.yaml |
| Generated status | Generated merge with one normalized owner |
| Merge fingerprint | 2bdee35c250a2cb31edb8a41a11623dbfe2c19a37e57e947c11b534f12aed299 |

The reviewed file is the generated TOGO M2426 / ATCC Brain Heart Infusion Broth
record. Future fixes belong in the normalized owner named above or in the TOGO
commercial-BHI import/enrichment path that populated it.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/Brain_Heart_Infusion_Broth.yaml` | Passed |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/Brain_Heart_Infusion_Broth.yaml --out /private/tmp/Brain_Heart_Infusion_Broth.strict.tsv --workers 1 --quiet` | Passed with 0 error rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/Brain_Heart_Infusion_Broth.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/Brain_Heart_Infusion_Broth.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` gate validates standalone records under `history/`, not embedded `MediaRecipe.curation_history` entries in one merge file |

The direct `just validate-schema`, `just validate-strict`, and
`just validate-terms` recipes were not rerun for this record because project
environment creation currently stops while building `llvmlite==0.46.0` under
Python 3.13. The equivalent narrow validators above were run in a no-project
Python 3.11 tool environment.

## Identity and Grounding

- `TOGO:M2426` identifies the ATCC Brain Heart Infusion Broth recipe.
- TOGO M2426 lists 1000 ml DI water and 37 g Brain Heart Infusion Broth, BD
  237500.
- The linked ATCC PDF lists the same 37 g BD Brain Heart Infusion Broth plus
  1000 ml DI water broth recipe and a separate scratch `Brain Heart Infusion
  Composition` recipe.
- The ATCC scratch recipe lists calf-brain infusion, beef-heart infusion,
  proteose peptone, dextrose, NaCl, Na2HPO4, and DI water.
- A gitignore-independent exact search for `TOGO:M2426`,
  `CultureMech:009009`, the merge fingerprint, and the normalized/generated
  stems covered generated records, normalized records, local indexes, reports,
  source, scripts, `justfile`, and `.claude`; it found the single M2426
  normalized owner, the generated record, indexes for that owner, and broader
  BHI records that are not identity-equivalent to M2426.

The generated record identifies the TOGO M2426 source correctly, but it
substitutes an alternative scratch formulation for the explicit 37 g BD 237500
commercial row and then attributes those scratch rows to the commercial product.

## Evidence

TOGO M2426 and the ATCC source PDF support a Brain Heart Infusion Broth recipe
made with 1000 ml DI water and 37 g Brain Heart Infusion Broth, BD 237500. The
record changes the water to `1000 G_PER_L`, which is a mass unit instead of the
source volume unit.

The ATCC PDF also provides a scratch `Brain Heart Infusion Composition`
formulation. The calf-brain, beef-heart, proteose-peptone, dextrose, NaCl, and
Na2HPO4 rows in the record are therefore source-backed as an alternate scratch
recipe, but the record misrepresents them as constituents of BD 237500 from
MicrobeNotes rather than as ATCC scratch-formulation ingredients.

TOGO M2426 carries pH `7.2 - 7.6`, matching the ATCC final pH of `7.4 +/- 0.2`,
and both TOGO and ATCC state to autoclave the medium at 121 C. The record only
mentions final pH inside the disodium-phosphate ingredient note and has no
structured preparation step.

No inspected TOGO or ATCC evidence identified a target organism, strain, or
taxonomy scope, so the empty `target_organisms` field is not a defect for this
generic ATCC medium.

## Completeness

- Consequential gap: source water is a 1000 ml volume but is stored as
  `1000 G_PER_L`.
- Consequential gap: the explicit 37 g BD 237500 commercial BHI broth row is
  absent.
- Consequential gap: the ATCC scratch formulation is not preserved as an
  alternative recipe and is instead misattributed to the commercial product.
- Consequential gap: the source pH and autoclave instruction are absent from
  structured fields.
- A gitignore-independent exact search under `reports/yaml_record_review` for
  `Brain_Heart_Infusion_Broth.yaml`, the M2426 merge fingerprint,
  `CultureMech:009009`, and `TOGO:M2426` found no prior report for this target.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | DI water has the wrong unit. | TOGO M2426 and the ATCC PDF list 1000 ml DI water; the record stores `1000 G_PER_L`. | `data/normalized_yaml/bacterial/brain_heart_infusion_broth.yaml`; likely also the TOGO unit importer |
| Major | The explicit 37 g BD 237500 BHI broth row is missing. | TOGO M2426 and the ATCC PDF list `Brain Heart Infusion Broth (BD 237500)` as a 37 g ingredient, but the record replaces it with calf-brain, beef-heart, proteose-peptone, dextrose, sodium-chloride, and disodium-phosphate rows. | `data/normalized_yaml/bacterial/brain_heart_infusion_broth.yaml`; likely also the BHI premix expansion importer |
| Major | The scratch BHI formulation is mis-scoped and misattributed. | ATCC supports the expanded rows only as a separate scratch `Brain Heart Infusion Composition`; the record attaches BD 237500 supplier metadata and a MicrobeNotes product URL to each scratch row. | `data/normalized_yaml/bacterial/brain_heart_infusion_broth.yaml`; likely also the BHI premix expansion importer |
| Major | Source pH and preparation details are missing from structured fields. | TOGO M2426 and ATCC record final pH `7.4 +/- 0.2` / `7.2 - 7.6` and autoclaving at 121 C; the generated record has no structured pH or preparation step. | `data/normalized_yaml/bacterial/brain_heart_infusion_broth.yaml` |

## Recommended Edits

1. Restore the source commercial recipe as 37 g Brain Heart Infusion Broth (BD
   237500) plus 1000 ml DI water.
2. If the ATCC scratch formulation is retained, model it as an alternative
   ATCC-supported formulation, not as catalog-backed BD powder subcomponents.
3. Store the source pH as 7.4 +/- 0.2, equivalent to the TOGO range 7.2-7.6.
4. Add the source autoclave-at-121-C preparation instruction.
5. Regenerate merged YAML after the normalized owner or importer is fixed.

## Follow-up Checks

- Rerun focused schema, strict, reference, and term validators on the corrected
  normalized M2426 owner.
- Rerun `just validate` after the project `llvmlite` build issue is resolved.
- Regenerate merges and verify the M2426 record still has one owner and remains
  distinct from M2511, M2905, and the other BHI broth variants.
- Manually compare the regenerated record against the TOGO M2426 API payload
  and the ATCC PDF linked from it.

## Additional Notes

- Related BHI broth variants appeared during exact slug searches but were not
  identity matches for TOGO M2426.
