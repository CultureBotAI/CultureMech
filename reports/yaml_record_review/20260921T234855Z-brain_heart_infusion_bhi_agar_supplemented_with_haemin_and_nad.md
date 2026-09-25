# YAML Record Review: Brain-heart infusion (BHI) agar supplemented with haemin and NAD

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/brain_heart_infusion_bhi_agar_supplemented_with_haemin_and_nad.yaml
- Started UTC: 2026-09-21T23:48:55Z
- Finished UTC: 2026-09-21T23:49:36Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009460 |
| Label | Brain-heart infusion (BHI) agar supplemented with haemin and NAD |
| Source accession | TOGO:M2924 |
| Merge source | data/normalized_yaml/bacterial/brain_heart_infusion_bhi_agar_supplemented_with_haemin_and_nad.yaml |
| Generated status | Generated merge with one normalized owner |
| Merge fingerprint | ae64278abfc5e270a0c28911ec0b5bc3c57c7b4f0eb907e2790b711bb4d90b63 |

The reviewed file is generated, and the generated content currently matches its
single normalized owner. Future fixes belong in
`data/normalized_yaml/bacterial/brain_heart_infusion_bhi_agar_supplemented_with_haemin_and_nad.yaml`
or in the TOGO import/unit-normalization path that populated it.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/brain_heart_infusion_bhi_agar_supplemented_with_haemin_and_nad.yaml` | Passed |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/brain_heart_infusion_bhi_agar_supplemented_with_haemin_and_nad.yaml --out /private/tmp/brain_heart_infusion_bhi_agar_supplemented_with_haemin_and_nad.strict.tsv --workers 1 --quiet` | Passed with 0 error rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/brain_heart_infusion_bhi_agar_supplemented_with_haemin_and_nad.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/brain_heart_infusion_bhi_agar_supplemented_with_haemin_and_nad.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` gate validates standalone records under `history/`, not embedded `MediaRecipe.curation_history` entries in one merge file |

The direct `just validate-schema`, `just validate-strict`, and
`just validate-terms` recipes were not rerun for this record because project
environment creation currently stops while building `llvmlite==0.46.0` under
Python 3.13. The equivalent narrow validators above were run in a no-project
Python 3.11 tool environment.

## Identity and Grounding

- `TOGO:M2924` identifies Brain-heart infusion agar supplemented with haemin
  and NAD.
- The TOGO M2924 API payload has no `src_url`, but its captured
  H. influenzae growth-condition sentence resolves by exact phrase search to
  Hood et al. 1999, PMID 10447878, DOI `10.1046/j.1365-2958.1999.01509.x`.
- TOGO M2924 lists haemin at 10 ug/ml, NAD at 2 ug/ml, agar at 1% w/v, and
  Brain-heart infusion agar as a 1 L base.
- A gitignore-independent exact search for `TOGO:M2924`,
  `CultureMech:009460`, the merge fingerprint, and the normalized slug covered
  generated records, normalized records, local indexes, reports, source,
  scripts, `justfile`, and `.claude`; it found only this normalized owner and
  this generated merge for the M2924 source accession.

The record identity is correct, but several source units were imported into the
wrong slot unit and the 1 L BHI agar base was replaced by inferred BHI
constituents.

## Evidence

The inspected TOGO payload, backed by Hood et al. 1999, supports a BHI agar
formulation for H. influenzae grown at 37 C with 10 ug/ml haemin and 2 ug/ml NAD.
The same source frames neuraminic acid, CMP-Neu5Ac, and kanamycin as conditional
additions; their absence from this base haemin/NAD record is not a defect.

The record stores haemin as `10 G_PER_L` and NAD as `2 G_PER_L`. Those are
micrograms-per-milliliter values in the source, so they should be normalized as
10 mg/L and 2 mg/L, or as an equivalent unit-preserving representation.

The record stores the TOGO agar item as `1 G_PER_L`, but TOGO captured it as
`1 (w/v)` from the paper's BHI agar percentage. One percent w/v agar corresponds
to 10 g/L if converted to grams per liter.

The TOGO component `Brain-heart infusion (BHI) agar`, 1 L, has been replaced by
the familiar expanded BHI constituents from a MicrobeNotes page. The inspected
TOGO payload and paper text do not assert calf-brain, beef-heart,
proteose-peptone, dextrose, sodium-chloride, or disodium-phosphate rows.

## Completeness

- Consequential gap: TOGO M2924 lacks primary source metadata in
  `src_url`, and the normalized record only cites TOGO.
- Consequential gap: the 37 C H. influenzae growth condition from the primary
  source is not represented in target-organism or growth-evidence fields.
- Consequential gap: NAD remains ungrounded even though TOGO resolves the row to
  `GMO_001691` / Beta-NAD.
- Conditional Neu5Ac, CMP-Neu5Ac, and kanamycin additions are correctly absent
  from this base haemin/NAD formulation.
- A gitignore-independent exact search under `reports/yaml_record_review` for
  the normalized slug, the M2924 label, and the merge fingerprint found no prior
  report for this target.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Haemin and NAD were imported as grams per liter instead of micrograms per milliliter. | TOGO M2924 lists haemin at 10 ug/ml and NAD at 2 ug/ml; the record stores `10 G_PER_L` and `2 G_PER_L`. | `data/normalized_yaml/bacterial/brain_heart_infusion_bhi_agar_supplemented_with_haemin_and_nad.yaml`; likely also the TOGO unit importer |
| Major | Agar `1% w/v` was imported as `1 G_PER_L`. | TOGO M2924 lists Agar with unit `(w/v)` and volume `1`; this is 1% agar, not 1 g/L agar. | `data/normalized_yaml/bacterial/brain_heart_infusion_bhi_agar_supplemented_with_haemin_and_nad.yaml`; likely also the TOGO unit importer |
| Major | The 1 L BHI agar base was expanded into unsupported inferred constituents. | TOGO M2924 lists a 1 L Brain-heart infusion agar base; neither TOGO nor Hood et al. 1999 gives the expanded internal BD-Difco composition. | `data/normalized_yaml/bacterial/brain_heart_infusion_bhi_agar_supplemented_with_haemin_and_nad.yaml`; likely also the BHI premix expansion importer |
| Major | The primary paper and growth-condition scope are not represented. | The TOGO comment resolves to Hood et al. 1999, which scopes the formulation to H. influenzae strains grown at 37 C, but the record has no primary DOI/PMID metadata, no target-organism entry, and no structured 37 C condition. | `data/normalized_yaml/bacterial/brain_heart_infusion_bhi_agar_supplemented_with_haemin_and_nad.yaml` |
| Minor | NAD lacks a term grounding. | TOGO M2924 resolves NAD to `GMO_001691` with label `Beta-NAD`; the normalized row has only `preferred_term: NAD`. | `data/normalized_yaml/bacterial/brain_heart_infusion_bhi_agar_supplemented_with_haemin_and_nad.yaml` |

## Recommended Edits

1. Convert or preserve the TOGO supplement units: 10 ug/ml haemin and 2 ug/ml
   NAD, not 10 and 2 g/L.
2. Convert `1% w/v` agar to 10 g/L, or preserve percent w/v explicitly if the
   schema supports it.
3. Restore `Brain-heart infusion (BHI) agar`, 1 L, as an opaque BHI agar base
   unless a primary BHI-agar product specification is attached for the expanded
   formula.
4. Add the Hood et al. 1999 DOI/PMID as primary source provenance for the TOGO
   comment, and add narrowly scoped H. influenzae / 37 C growth metadata if the
   current schema has slots for that assertion.
5. Ground NAD to an exact term for Beta-NAD or leave it explicitly unresolved
   with the TOGO GMO identifier as a lead; do not map it to a chemically
   adjacent broad NAD class.
6. Regenerate the merged YAML after the normalized owner or importer is fixed.

## Follow-up Checks

- Rerun focused schema, strict, reference, and term validators on the corrected
  normalized owner.
- Rerun `just validate` after the project `llvmlite` build issue is resolved.
- Regenerate merges and confirm the haemin, NAD, and agar amounts retain the
  source units or convert arithmetically to mg/L and g/L.
- Manually compare the regenerated record against TOGO M2924 and Hood et al.
  1999 to ensure conditional Neu5Ac, CMP-Neu5Ac, and kanamycin remain optional
  rather than being folded into the base recipe.

## Additional Notes

- TOGO M2924 has no upstream URL in `meta.src_url`; the primary paper was found
  from an exact phrase in the TOGO comment.
- Optional empty pH and preparation fields were not treated as defects because
  the inspected source text does not specify them.
