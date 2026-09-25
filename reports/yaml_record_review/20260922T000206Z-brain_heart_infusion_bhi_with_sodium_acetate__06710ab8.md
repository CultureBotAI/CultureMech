# YAML Record Review: Brain Heart Infusion (BHI) with Sodium Acetate

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/brain_heart_infusion_bhi_with_sodium_acetate__06710ab8.yaml
- Started UTC: 2026-09-22T00:02:06Z
- Finished UTC: 2026-09-22T00:03:22Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009557 |
| Label | Brain Heart Infusion (BHI) with Sodium Acetate |
| Source accession | TOGO:M3044 / NBRC_M1574-1 |
| Merge source | data/normalized_yaml/bacterial/brain_heart_infusion_bhi_with_sodium_acetate.yaml |
| Generated status | Generated merge with one normalized owner |
| Merge fingerprint | 06710ab8454c46c9663813d099b8aec7ef5ce8af2bf045e7c12d24fe81fd5245 |

The reviewed file is the agar-plate NBRC 1574-1 / TOGO M3044 BHI
sodium-acetate variant. Future fixes belong in the normalized owner named above
or in the TOGO solution/unit import path that populated it.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/brain_heart_infusion_bhi_with_sodium_acetate__06710ab8.yaml` | Passed |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/brain_heart_infusion_bhi_with_sodium_acetate__06710ab8.yaml --out /private/tmp/brain_heart_infusion_bhi_with_sodium_acetate__06710ab8.strict.tsv --workers 1 --quiet` | Passed with 0 error rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/brain_heart_infusion_bhi_with_sodium_acetate__06710ab8.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/brain_heart_infusion_bhi_with_sodium_acetate__06710ab8.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` gate validates standalone records under `history/`, not embedded `MediaRecipe.curation_history` entries in one merge file |

The direct `just validate-schema`, `just validate-strict`, and
`just validate-terms` recipes were not rerun for this record because project
environment creation currently stops while building `llvmlite==0.46.0` under
Python 3.13. The equivalent narrow validators above were run in a no-project
Python 3.11 tool environment.

## Identity and Grounding

- `TOGO:M3044` identifies the agar-plate NBRC_M1574-1 BHI sodium-acetate
  recipe.
- `TOGO:M3045` is the related NBRC_M1574-2 liquid sibling; it lacks agar and
  has N2 only in its liquid-medium autoclave instruction.
- TOGO M3044 lists 1 L distilled water, 2.7 g sodium acetate, 15 g agar, 37 g
  Bacto Brain Heart Infusion, and 2.5 ml of the liquid-only antifoam solution.
- TOGO M3044 also defines the antifoam stock as 9 ml distilled water plus 1 ml
  Antifoam SI (Wako).
- A gitignore-independent exact search for `TOGO:M3044`, `TOGO:M3045`,
  `NBRC_M1574`, `CultureMech:009557`, `CultureMech:009558`, both merge
  fingerprints, and the normalized slugs covered generated records, normalized
  records, local indexes, reports, source, scripts, `justfile`, and `.claude`;
  it found the agar M3044 owner, the liquid M3045 sibling, and their generated
  records/index entries.

The generated record identifies the agar M3044 source correctly. It also
correctly remains separate from the no-agar M3045 liquid sibling, but its
ingredient list conflates final-medium rows and antifoam-stock rows.

## Evidence

TOGO M3044 supports a 1 L agar BHI sodium-acetate medium with 2.7 g sodium
acetate, 15 g agar, and 37 g Bacto Brain Heart Infusion. It does not support
summing the final 1 L distilled water with 9 ml antifoam-stock water into one
`10.0 G_PER_L` row.

The TOGO M3044 final-ingredient list includes 2.5 ml antifoam solution, and the
TOGO label for that row says the solution is only for liquid medium. The record
does not preserve that conflict as a reviewable condition; it stores the stock
as an empty `Unknown solution` at `2.5 G_PER_L` and also leaves `Antifoam SI
(Wako)` as a top-level `1 G_PER_L` final ingredient.

TOGO M3044 has no N2 row, and the generated agar record likewise has no N2 row.

As with other BHI imports, the 37 g Bacto Brain Heart Infusion row is replaced
by inferred BD/Difco constituents from MicrobeNotes. The inspected TOGO payload
does not list calf-brain, beef-heart, proteose-peptone, dextrose,
sodium-chloride, or disodium-phosphate rows separately.

## Completeness

- Consequential gap: final-medium water and antifoam-stock water have been
  summed and assigned a mass unit.
- Consequential gap: the antifoam stock is both labeled liquid-only in a solid
  agar recipe and malformed into an empty solution plus a flattened final
  `Antifoam SI (Wako)` row.
- Consequential gap: the 37 g Bacto BHI premix row is absent.
- Consequential gap: the source's `pH unadjusted` note and agar-plate
  sterilization, cooling, and dispensing instructions are absent from structured
  fields.
- A gitignore-independent exact search under `reports/yaml_record_review` for
  the normalized slug and the M3044 merge fingerprint found no prior report for
  this target.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The record sums water from two different recipe boundaries and stores the result as `10.0 G_PER_L`. | TOGO M3044 has 1 L distilled water in the final medium and 9 ml distilled water inside the antifoam stock; these should not be added. | `data/normalized_yaml/bacterial/brain_heart_infusion_bhi_with_sodium_acetate.yaml`; likely also the duplicate-row merge and TOGO unit importer |
| Major | The liquid-only antifoam stock is malformed and its source conflict is not preserved. | TOGO M3044 adds 2.5 ml antifoam solution to the final agar recipe, labels that solution as liquid-only, and defines the stock as 9 ml water plus 1 ml Antifoam SI; the record has an empty `Unknown solution` at `2.5 G_PER_L` plus top-level `1 G_PER_L` Antifoam SI. | `data/normalized_yaml/bacterial/brain_heart_infusion_bhi_with_sodium_acetate.yaml`; likely also the solution migrator/importer |
| Major | The 37 g Bacto Brain Heart Infusion row is replaced by inferred constituents. | TOGO M3044 lists one Bacto Brain Heart Infusion row; it does not directly assert the expanded calf-brain, beef-heart, proteose-peptone, dextrose, sodium-chloride, and disodium-phosphate rows. | `data/normalized_yaml/bacterial/brain_heart_infusion_bhi_with_sodium_acetate.yaml`; likely also the BHI premix expansion importer |
| Major | Source pH and preparation details are missing. | TOGO M3044 records `pH unadjusted` and agar-medium sterilization, cooling, and plate-dispensing instructions. | `data/normalized_yaml/bacterial/brain_heart_infusion_bhi_with_sodium_acetate.yaml` |

## Recommended Edits

1. Split final-medium ingredients from the antifoam stock: keep 1 L final
   distilled water, preserve the 2.5 ml final antifoam-solution row with its
   liquid-only qualifier until checked against the NBRC source, and store a
   stock recipe of 9 ml distilled water plus 1 ml Antifoam SI.
2. Restore 37 g Bacto Brain Heart Infusion (BD Difco) as an opaque premix row
   and remove the unsupported MicrobeNotes expansion.
3. Add the source pH note that the pH is unadjusted.
4. Add the agar-plate preparation instruction for 121 C / 15 min sterilization,
   cooling to about 50 C, and plate dispensing.
5. Regenerate merged YAML after the normalized owner or importer is fixed.

## Follow-up Checks

- Rerun focused schema, strict, reference, and term validators on the corrected
  normalized M3044 owner.
- Rerun `just validate` after the project `llvmlite` build issue is resolved.
- Regenerate merges and verify M3044 remains the agar variant while M3045
  remains the separate no-agar liquid variant.
- Manually compare the regenerated M3044 record against the TOGO M3044 API
  payload and the upstream NBRC 1574-1 record.

## Additional Notes

- The M3045 liquid sibling was inspected as context and reviewed separately.
