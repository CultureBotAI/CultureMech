# YAML Record Review: Brain Heart Infusion (BHI) with Sodium Acetate

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/brain_heart_infusion_bhi_with_sodium_acetate.yaml
- Started UTC: 2026-09-21T23:59:11Z
- Finished UTC: 2026-09-22T00:00:14Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009558 |
| Label | Brain Heart Infusion (BHI) with Sodium Acetate |
| Source accession | TOGO:M3045 / NBRC_M1574-2 |
| Merge source | data/normalized_yaml/bacterial/TOGO_M3045_Brain_Heart_Infusion_BHI_with_Sodium_Acetate.yaml |
| Generated status | Generated merge with one normalized owner |
| Merge fingerprint | 01d8d23a32cc5f85ea251ed17cadbe923d78da4a1861ce9b3a3877dafdc9a514 |

The reviewed file is the liquid NBRC 1574-2 / TOGO M3045 BHI sodium-acetate
variant. Future fixes belong in the normalized owner named above or in the TOGO
solution/unit import path that populated it.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/brain_heart_infusion_bhi_with_sodium_acetate.yaml` | Passed |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/brain_heart_infusion_bhi_with_sodium_acetate.yaml --out /private/tmp/brain_heart_infusion_bhi_with_sodium_acetate.strict.tsv --workers 1 --quiet` | Passed with 0 error rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/brain_heart_infusion_bhi_with_sodium_acetate.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/brain_heart_infusion_bhi_with_sodium_acetate.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` gate validates standalone records under `history/`, not embedded `MediaRecipe.curation_history` entries in one merge file |

The direct `just validate-schema`, `just validate-strict`, and
`just validate-terms` recipes were not rerun for this record because project
environment creation currently stops while building `llvmlite==0.46.0` under
Python 3.13. The equivalent narrow validators above were run in a no-project
Python 3.11 tool environment.

## Identity and Grounding

- `TOGO:M3045` identifies the liquid NBRC_M1574-2 BHI sodium-acetate recipe.
- `TOGO:M3044` is the related NBRC_M1574-1 agar-plate sibling; it has 15 g agar
  and no N2 ingredient.
- TOGO M3045 lists 1 L distilled water, 2.7 g sodium acetate, 37 g Bacto Brain
  Heart Infusion (BD Difco), 2.5 ml of the liquid-only antifoam solution, and
  an N2 autoclave atmosphere.
- TOGO M3045 also defines the antifoam stock as 9 ml distilled water plus 1 ml
  Antifoam SI (Wako).
- A gitignore-independent exact search for `TOGO:M3045`, `TOGO:M3044`,
  `NBRC_M1574`, `CultureMech:009558`, `CultureMech:009557`, both merge
  fingerprints, and the normalized slugs covered generated records, normalized
  records, local indexes, reports, source, scripts, `justfile`, and `.claude`;
  it found the liquid M3045 owner, the agar M3044 sibling, and their generated
  records/index entries.

The generated record identifies the liquid M3045 source correctly, but its
ingredient list conflates final-medium rows, antifoam-stock rows, and N2
sterilization atmosphere.

## Evidence

TOGO M3045 supports a 1 L liquid BHI sodium-acetate medium with 2.7 g sodium
acetate, 37 g Bacto Brain Heart Infusion, and 2.5 ml antifoam solution. It does
not support summing the final 1 L distilled water with 9 ml antifoam-stock water
into one `10.0 G_PER_L` row.

The antifoam solution is a stock made from 9 ml distilled water plus 1 ml
Antifoam SI. The final medium receives 2.5 ml of that stock. The record stores
the stock as an empty `Unknown solution` at `2.5 G_PER_L` and also leaves
`Antifoam SI (Wako)` as a top-level `1 G_PER_L` final ingredient.

The N2 assertion belongs to the liquid preparation step: dispense to vessels and
autoclave under N2 at 121 C for 15 min. The record stores N2 as a variable
medium ingredient.

As with other BHI imports, the 37 g Bacto Brain Heart Infusion row is replaced
by inferred BD/Difco constituents from MicrobeNotes. The inspected TOGO payload
does not list calf-brain, beef-heart, proteose-peptone, dextrose,
sodium-chloride, or disodium-phosphate rows separately.

## Completeness

- Consequential gap: final-medium water and antifoam-stock water have been
  summed and assigned a mass unit.
- Consequential gap: the antifoam stock recipe is empty and is also flattened
  into the final medium.
- Consequential gap: the 37 g Bacto BHI premix row is absent.
- Consequential gap: N2 is modeled as an ingredient instead of preparation
  atmosphere.
- Consequential gap: the source's `pH unadjusted` note and liquid-medium
  sterilization instruction are absent from structured fields.
- A gitignore-independent exact search under `reports/yaml_record_review` for
  the normalized slug and the M3045 merge fingerprint found no prior report for
  this target.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The record sums water from two different recipe boundaries and stores the result as `10.0 G_PER_L`. | TOGO M3045 has 1 L distilled water in the final medium and 9 ml distilled water inside the antifoam stock; these should not be added. | `data/normalized_yaml/bacterial/TOGO_M3045_Brain_Heart_Infusion_BHI_with_Sodium_Acetate.yaml`; likely also the duplicate-row merge and TOGO unit importer |
| Major | The liquid-only antifoam stock is malformed. | TOGO M3045 adds 2.5 ml antifoam solution to the final medium and defines the stock as 9 ml water plus 1 ml Antifoam SI; the record has an empty `Unknown solution` at `2.5 G_PER_L` plus top-level `1 G_PER_L` Antifoam SI. | `data/normalized_yaml/bacterial/TOGO_M3045_Brain_Heart_Infusion_BHI_with_Sodium_Acetate.yaml`; likely also the solution migrator/importer |
| Major | N2 is modeled as a medium ingredient. | TOGO M3045 mentions N2 only in the liquid-medium autoclave instruction; the record stores it as an ingredient with `VARIABLE` concentration. | `data/normalized_yaml/bacterial/TOGO_M3045_Brain_Heart_Infusion_BHI_with_Sodium_Acetate.yaml` |
| Major | The 37 g Bacto Brain Heart Infusion row is replaced by inferred constituents. | TOGO M3045 lists one Bacto Brain Heart Infusion row; it does not directly assert the expanded calf-brain, beef-heart, proteose-peptone, dextrose, sodium-chloride, and disodium-phosphate rows. | `data/normalized_yaml/bacterial/TOGO_M3045_Brain_Heart_Infusion_BHI_with_Sodium_Acetate.yaml`; likely also the BHI premix expansion importer |
| Major | Source pH and preparation details are missing. | TOGO M3045 records `pH unadjusted` and the N2 autoclave instruction for the liquid medium. | `data/normalized_yaml/bacterial/TOGO_M3045_Brain_Heart_Infusion_BHI_with_Sodium_Acetate.yaml` |

## Recommended Edits

1. Split final-medium ingredients from the antifoam stock: keep 1 L final
   distilled water, 2.5 ml final antifoam solution, and a stock recipe of 9 ml
   distilled water plus 1 ml Antifoam SI.
2. Restore 37 g Bacto Brain Heart Infusion (BD Difco) as an opaque premix row
   and remove the unsupported MicrobeNotes expansion.
3. Move N2 from ingredients to the liquid autoclave/preparation instruction.
4. Add the source pH note that the pH is unadjusted.
5. Regenerate merged YAML after the normalized owner or importer is fixed.

## Follow-up Checks

- Rerun focused schema, strict, reference, and term validators on the corrected
  normalized M3045 owner.
- Rerun `just validate` after the project `llvmlite` build issue is resolved.
- Regenerate merges and verify M3045 remains the liquid no-agar variant while
  M3044 remains the separate agar variant.
- Manually compare the regenerated M3045 record against the TOGO M3045 API
  payload.

## Additional Notes

- The M3044 agar sibling was inspected as context but is a separate generated
  record and was not curated or reviewed in this report.
