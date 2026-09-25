# YAML Record Review: brain heart infusion (BHI) medium (supplemented with antibiotics)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/brain_heart_infusion_bhi_medium_supplemented_with_antibiotics.yaml
- Started UTC: 2026-09-21T23:57:21Z
- Finished UTC: 2026-09-21T23:58:14Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009493 |
| Label | brain heart infusion (BHI) medium (supplemented with antibiotics) |
| Source accession | TOGO:M2970 |
| Merge source | data/normalized_yaml/bacterial/brain_heart_infusion_bhi_medium_supplemented_with_antibiotics.yaml |
| Generated status | Stale generated merge with one normalized owner |
| Merge fingerprint | 435adfdeb90615c08d4d777b2ebd020a7b8933ac06da0981da3160e71d2ce9ae |

The reviewed file is generated from one normalized owner. Future fixes belong in
`data/normalized_yaml/bacterial/brain_heart_infusion_bhi_medium_supplemented_with_antibiotics.yaml`
or in the TOGO import and BHI-premix paths that populated it.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/brain_heart_infusion_bhi_medium_supplemented_with_antibiotics.yaml` | Passed |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/brain_heart_infusion_bhi_medium_supplemented_with_antibiotics.yaml --out /private/tmp/brain_heart_infusion_bhi_medium_supplemented_with_antibiotics.strict.tsv --workers 1 --quiet` | Passed with 0 error rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/brain_heart_infusion_bhi_medium_supplemented_with_antibiotics.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/brain_heart_infusion_bhi_medium_supplemented_with_antibiotics.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` gate validates standalone records under `history/`, not embedded `MediaRecipe.curation_history` entries in one merge file |

The direct `just validate-schema`, `just validate-strict`, and
`just validate-terms` recipes were not rerun for this record because project
environment creation currently stops while building `llvmlite==0.46.0` under
Python 3.13. The equivalent narrow validators above were run in a no-project
Python 3.11 tool environment.

## Identity and Grounding

- `TOGO:M2970` identifies BHI medium supplemented with antibiotics.
- The inspected TOGO M2970 payload lists a 1 L Oxoid BHI medium base and stock
  solutions of kanamycin, ampicillin, erythromycin, and chloramphenicol.
- TOGO M2970 has no `src_url`. Its comments state that L. monocytogenes was
  cultured in Oxoid BHI and that stock solutions of the four antibiotics were
  added to the medium, where appropriate, at required levels; an exact web
  search did not recover a primary source with the same 50/50/30/50 mg/ml stock
  strengths.
- A gitignore-independent exact search for `TOGO:M2970`,
  `CultureMech:009493`, the merge fingerprint, and the normalized slug covered
  generated records, normalized records, local indexes, reports, source,
  scripts, `justfile`, and `.claude`; it found only this normalized owner and
  this generated merge for the M2970 source accession.

The source identity is correct, but the generated record is stale and conflates
stock-solution strengths with final-medium ingredient concentrations.

## Evidence

TOGO M2970 supports four antibiotic stock solutions: kanamycin 50 mg/ml,
ampicillin 50 mg/ml, erythromycin 30 mg/ml, and chloramphenicol 50 mg/ml. These
values describe stock solutions that were added as needed at required final
levels, not the final grams-per-liter concentrations in the BHI medium.

The TOGO BHI base is an Oxoid complex component at 1 L. The normalized record
replaces it with inferred BD/Difco BHI constituents from a MicrobeNotes page,
which is the wrong supplier and the wrong formulation boundary for this source.

The generated target was built on 2026-08-06. Its normalized owner was updated
on 2026-08-20 by `apply_mim_groundings.py`, which added CHEBI terms for
kanamycin and chloramphenicol. The generated target still lacks those two
groundings.

## Completeness

- Consequential gap: antibiotic stock strengths are represented as final
  medium concentrations.
- Consequential gap: the 1 L Oxoid BHI base is not represented.
- Consequential gap: the generated record is stale relative to August
  normalized owner grounding changes.
- Consequential gap: the L. monocytogenes growth scope from the TOGO comment is
  not represented in target-organism or growth-evidence fields.
- A gitignore-independent exact search under `reports/yaml_record_review` for
  the normalized slug and the merge fingerprint found no prior report for this
  target.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Antibiotic stock concentrations are modeled as final-medium grams-per-liter rows. | The TOGO M2970 comment says antibiotic stock solutions were added, where appropriate, at required levels; the payload lists 50/50/30/50 mg/ml stock strengths, while the record stores those numbers as final `G_PER_L` concentrations. | `data/normalized_yaml/bacterial/brain_heart_infusion_bhi_medium_supplemented_with_antibiotics.yaml`; likely also the TOGO stock-solution importer |
| Major | The 1 L Oxoid BHI medium base was expanded into unsupported BD/Difco constituents. | TOGO M2970 lists `brain heart infusion (BHI) medium (Oxoid, Hampshire, England)`, 1 L; the record stores BD/Difco calf-brain, beef-heart, proteose-peptone, dextrose, sodium-chloride, and disodium-phosphate rows from MicrobeNotes. | `data/normalized_yaml/bacterial/brain_heart_infusion_bhi_medium_supplemented_with_antibiotics.yaml`; likely also the BHI premix expansion importer |
| Major | The generated record is stale. | The normalized owner gained kanamycin and chloramphenicol CHEBI groundings on 2026-08-20, after this merge was generated on 2026-08-06. | Regenerated `data/merge_yaml/merged/brain_heart_infusion_bhi_medium_supplemented_with_antibiotics.yaml` |
| Major | Primary source and L. monocytogenes growth metadata are absent. | TOGO M2970 has only local comments, no `src_url`; those comments scope the BHI medium to L. monocytogenes culture, but the record keeps only the TOGO accession and no target-organism entry. | `data/normalized_yaml/bacterial/brain_heart_infusion_bhi_medium_supplemented_with_antibiotics.yaml` |

## Recommended Edits

1. Remodel kanamycin, ampicillin, erythromycin, and chloramphenicol as stock
   solutions, or as conditional additions with unresolved final amounts, instead
   of final 50/50/30/50 g/L medium ingredients.
2. Restore the 1 L BHI medium as an opaque Oxoid base and remove the
   unsupported BD/Difco MicrobeNotes expansion.
3. Add the narrow L. monocytogenes scope from the TOGO comment and attach a
   primary source if one is recovered.
4. Regenerate the merged YAML so kanamycin and chloramphenicol groundings from
   the normalized owner reach the generated record.

## Follow-up Checks

- Rerun focused schema, strict, reference, and term validators on the corrected
  normalized owner.
- Rerun `just validate` after the project `llvmlite` build issue is resolved.
- Regenerate merges and rerun `just audit-merge-freshness`.
- Manually compare the regenerated record against TOGO M2970 and confirm stock
  strengths are no longer treated as final medium concentrations.

## Additional Notes

- The inspected TOGO text does not specify final antibiotic levels, so the
  review does not infer them from the stock strengths.
