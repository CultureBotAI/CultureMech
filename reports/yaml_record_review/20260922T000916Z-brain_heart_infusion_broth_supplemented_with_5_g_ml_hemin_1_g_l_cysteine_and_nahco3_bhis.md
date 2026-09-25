# YAML Record Review: Brain heart infusion broth supplemented with 5 ug/ml hemin, 1 g/L-cysteine, and NaHCO3 (BHIS)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/brain_heart_infusion_broth_supplemented_with_5_g_ml_hemin_1_g_l_cysteine_and_nahco3_bhis.yaml
- Started UTC: 2026-09-22T00:09:16Z
- Finished UTC: 2026-09-22T00:10:49Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009360 |
| Label | Brain heart infusion broth supplemented with 5 ug/ml hemin, 1 g/L-cysteine, and NaHCO3 (BHIS) |
| Source accession | TOGO:M2812 |
| Merge source | data/normalized_yaml/bacterial/brain_heart_infusion_broth_supplemented_with_5_g_ml_hemin_1_g_l_cysteine_and_nahco3_bhis.yaml |
| Generated status | Generated merge with one normalized owner |
| Merge fingerprint | d98f33d8cade629bbfad6b8fe4cb0207e08aa38f791b49c04116463298cf80bb |

The reviewed file is the generated TOGO M2812 BHIS record. Future fixes belong
in the normalized owner named above or in the TOGO unit and BHI-base enrichment
paths that populated it.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/brain_heart_infusion_broth_supplemented_with_5_g_ml_hemin_1_g_l_cysteine_and_nahco3_bhis.yaml` | Passed |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/brain_heart_infusion_broth_supplemented_with_5_g_ml_hemin_1_g_l_cysteine_and_nahco3_bhis.yaml --out /private/tmp/brain_heart_infusion_broth_supplemented_with_5_g_ml_hemin_1_g_l_cysteine_and_nahco3_bhis.strict.tsv --workers 1 --quiet` | Passed with 0 error rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/brain_heart_infusion_broth_supplemented_with_5_g_ml_hemin_1_g_l_cysteine_and_nahco3_bhis.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/brain_heart_infusion_broth_supplemented_with_5_g_ml_hemin_1_g_l_cysteine_and_nahco3_bhis.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` gate validates standalone records under `history/`, not embedded `MediaRecipe.curation_history` entries in one merge file |

The direct `just validate-schema`, `just validate-strict`, and
`just validate-terms` recipes were not rerun for this record because project
environment creation currently stops while building `llvmlite==0.46.0` under
Python 3.13. The equivalent narrow validators above were run in a no-project
Python 3.11 tool environment.

## Identity and Grounding

- `TOGO:M2812` identifies BHIS medium from Rocha and Krykunivsky 2017, PMID
  28397401, DOI `10.1002/mbo3.479`.
- TOGO M2812 lists 1 g/L NaHCO3, 5 ug/ml hemin, 1 g/L cysteine, and 1 L brain
  heart infusion broth.
- The source paper uses BHIS for routine anaerobic growth of Bacteroides
  strains and lists the studied Bacteroides strains in its Table 1.
- A gitignore-independent exact search for `TOGO:M2812`,
  `CultureMech:009360`, the merge fingerprint, and the normalized slug covered
  generated records, normalized records, local indexes, reports, source,
  scripts, `justfile`, and `.claude`; it found the single M2812 normalized
  owner and the single generated record.

The generated record identifies the TOGO M2812 BHIS source correctly and the
NaHCO3 and cysteine source concentrations are preserved. Hemin's unit, the BHI
base, and the original paper's anaerobic Bacteroides scope are not preserved.

## Evidence

TOGO M2812 supports 5 ug/ml hemin, not `5 G_PER_L`. That import error changes
the final hemin concentration by a factor of 1000.

TOGO M2812 lists 1 L prepared brain heart infusion broth as the base. It does
not list the calf-brain, beef-heart, proteose-peptone, dextrose,
sodium-chloride, or disodium-phosphate rows now attached to the record with
MicrobeNotes/BD catalog metadata.

The Rocha and Krykunivsky paper supports anaerobic BHIS cultivation of
Bacteroides strains. The record has no structured preparation or incubation
condition, no Bacteroides target-organism scope, and no DOI, PMID, or PMC
reference to the paper behind the TOGO excerpt.

## Completeness

- Consequential gap: source hemin is a 5 ug/ml supplement but is stored as
  `5 G_PER_L`.
- Consequential gap: the 1 L BHI broth base is absent and replaced by an
  unsupported expansion.
- Consequential gap: the original Rocha and Krykunivsky paper is absent from
  `references`.
- Consequential gap: routine anaerobic Bacteroides growth context from the
  source paper is not represented in target organisms or preparation fields.
- A gitignore-independent exact search under `reports/yaml_record_review` for
  the normalized slug and the M2812 merge fingerprint found no prior report for
  this target.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Hemin is imported with a mass unit that is 1000-fold too high. | TOGO M2812 lists hemin at 5 ug/ml; the record stores `5 G_PER_L` instead of 5 mg/L or an equivalent representation. | `data/normalized_yaml/bacterial/brain_heart_infusion_broth_supplemented_with_5_g_ml_hemin_1_g_l_cysteine_and_nahco3_bhis.yaml`; likely also the TOGO microgram-per-milliliter unit importer |
| Major | The 1 L BHI broth base is replaced by inferred constituents. | TOGO M2812 lists one 1 L brain-heart-infusion-broth base row; it does not directly assert the expanded calf-brain, beef-heart, proteose-peptone, dextrose, sodium-chloride, and disodium-phosphate rows. | `data/normalized_yaml/bacterial/brain_heart_infusion_broth_supplemented_with_5_g_ml_hemin_1_g_l_cysteine_and_nahco3_bhis.yaml`; likely also the BHI premix expansion importer |
| Major | The record omits the source paper and its anaerobic Bacteroides scope. | The full text behind the TOGO excerpt is Rocha and Krykunivsky 2017, DOI `10.1002/mbo3.479` / PMID 28397401, which used BHIS for anaerobic growth of Bacteroides strains; the record has no reference or corresponding growth scope. | `data/normalized_yaml/bacterial/brain_heart_infusion_broth_supplemented_with_5_g_ml_hemin_1_g_l_cysteine_and_nahco3_bhis.yaml` |

## Recommended Edits

1. Correct the hemin concentration to 5 ug/ml or the equivalent 5 mg/L.
2. Restore the 1 L prepared brain heart infusion broth base and remove the
   unsupported MicrobeNotes/BD constituent expansion.
3. Add the Rocha and Krykunivsky 2017 DOI/PMID/PMC reference identified from
   the TOGO source excerpt.
4. Add Bacteroides anaerobic growth context from the source paper at the
   narrowest strain or taxon scope supported by Table 1.
5. Regenerate merged YAML after the normalized owner or importer is fixed.

## Follow-up Checks

- Rerun focused schema, strict, reference, and term validators on the corrected
  normalized M2812 owner.
- Rerun `just validate` after the project `llvmlite` build issue is resolved.
- Regenerate merges and verify the BHIS generated record preserves the corrected
  hemin concentration, the 1 L BHI base, and the Rocha/Krykunivsky reference.
- Manually compare the regenerated record against the TOGO M2812 API payload
  and the Materials and methods section of Rocha and Krykunivsky 2017.

## Additional Notes

- The source uses antibiotics when required; those conditional rows are not part
  of the baseline BHIS formulation and are correctly absent here.
