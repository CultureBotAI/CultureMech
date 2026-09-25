# YAML Record Review: Brain-heart infusion (BHI) broth supplemented with haemin and NAD

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/brain_heart_infusion_bhi_broth_supplemented_with_haemin_and_nad.yaml
- Started UTC: 2026-09-21T23:55:32Z
- Finished UTC: 2026-09-21T23:56:25Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009459 |
| Label | Brain-heart infusion (BHI) broth supplemented with haemin and NAD |
| Source accessions | TOGO:M2923, TOGO:M2895, TOGO:M2190 |
| Generated status | Generated merge of three normalized owners |
| Merge fingerprint | 2edf459f064afe928b7123970e6d872784530a9e0efcf00210d5ab7d9eaa5f02 |

The reviewed file is generated. Future fixes belong in the normalized owners
named under `merged_from` or in the merge rule that assigned the same
fingerprint to incompatible haemin/NAD supplement concentrations:

- `data/normalized_yaml/bacterial/brain_heart_infusion_bhi_broth_supplemented_with_haemin_and_nad.yaml`
- `data/normalized_yaml/bacterial/bhi_liquid_supplemented_with_haemin_and_nad.yaml`
- `data/normalized_yaml/bacterial/brain_heart_infusion_bhi_broth_supplemented_with_15_g_ml_nad_and_15_g_ml_haemin.yaml`

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/brain_heart_infusion_bhi_broth_supplemented_with_haemin_and_nad.yaml` | Passed |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/brain_heart_infusion_bhi_broth_supplemented_with_haemin_and_nad.yaml --out /private/tmp/brain_heart_infusion_bhi_broth_supplemented_with_haemin_and_nad.strict.tsv --workers 1 --quiet` | Passed with 0 error rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/brain_heart_infusion_bhi_broth_supplemented_with_haemin_and_nad.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/brain_heart_infusion_bhi_broth_supplemented_with_haemin_and_nad.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` gate validates standalone records under `history/`, not embedded `MediaRecipe.curation_history` entries in one merge file |

The direct `just validate-schema`, `just validate-strict`, and
`just validate-terms` recipes were not rerun for this record because project
environment creation currently stops while building `llvmlite==0.46.0` under
Python 3.13. The equivalent narrow validators above were run in a no-project
Python 3.11 tool environment.

## Identity and Grounding

- `TOGO:M2923` identifies BHI broth with 10 ug/ml haemin and 2 ug/ml NAD.
- `TOGO:M2895` identifies BHI liquid with 10 ug/ml haemin and 2 ug/ml NAD.
- `TOGO:M2190` identifies BHI broth with 15 ug/ml haemin and 15 ug/ml NAD.
- TOGO M2923 and M2895 both list a 1 L Brain heart infusion broth base; M2190
  lists the same BHI broth base at 1 L.
- A gitignore-independent exact search for `TOGO:M2923`, `TOGO:M2895`,
  `TOGO:M2190`, `CultureMech:009459`, the merge fingerprint, and the three
  normalized slugs covered generated records, normalized records, local
  indexes, reports, source, scripts, `justfile`, and `.claude`; it found these
  three normalized TOGO owners and their generated/index references.

The generated record keeps the 10/2 ug/ml identity of M2923 but adds M2190 as a
synonym even though M2190 has 15/15 ug/ml supplements. M2923 and M2895 may be
source duplicates after unit repair; M2190 is a distinct concentration variant.

## Evidence

TOGO M2923 preserves the same Hood et al. 1999 H. influenzae growth condition
reviewed in the paired agar record: 37 C BHI broth or 1% agar with 10 ug/ml
haemin and 2 ug/ml NAD. TOGO M2895 preserves a similar 10 ug/ml haemin and
2 ug/ml NAD BHI-liquid statement that resolves by exact phrase search to Power
et al. 2012, BMC Microbiology, DOI `10.1186/1471-2180-12-273`.

TOGO M2190 is not the same formula: it lists both haemin and NAD at 15 ug/ml.
Its payload has no `src_url` and no comments, so the primary source was not
recoverable from TOGO during this review.

All three normalized owners converted the microgram-per-milliliter supplement
amounts to grams per liter: the two 10/2 ug/ml records became `10 G_PER_L` and
`2 G_PER_L`, and the 15/15 ug/ml record became two `15 G_PER_L` rows.

The TOGO BHI broth base is a 1 L opaque complex component. Each normalized owner
replaced that component with inferred BD/Difco BHI constituents from a
MicrobeNotes page; the inspected TOGO payloads do not assert that internal
composition.

## Completeness

- Consequential gap: M2190 should not be hidden as a synonym of a 10/2 ug/ml
  BHI broth record.
- Consequential gap: the haemin and NAD units are off by a factor of 1000 in
  all three merged owners.
- Consequential gap: the 1 L BHI broth base is not represented.
- Consequential gap: NAD remains ungrounded even though all three TOGO payloads
  resolve the row to `GMO_001691` / Beta-NAD.
- Consequential gap: M2923, M2895, and M2190 all lack primary-source metadata
  because their `meta.src_url` values are empty; M2190 also lacks a source
  comment that can be phrase-matched.
- A gitignore-independent exact search under `reports/yaml_record_review` for
  the normalized slug and the merge fingerprint found no prior report for this
  target.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | TOGO M2190 is overmerged with 10/2 ug/ml BHI broth formulas. | M2923 and M2895 list 10 ug/ml haemin and 2 ug/ml NAD; M2190 lists 15 ug/ml of both supplements. | Merge fingerprint/rule plus the three normalized owners |
| Major | Haemin and NAD were imported as grams per liter instead of micrograms per milliliter. | The inspected TOGO payloads use `ug/ml`; the normalized owners store the same numeric values as `G_PER_L`. | All three normalized owners; likely also the TOGO unit importer |
| Major | The 1 L BHI broth base was expanded into unsupported inferred constituents. | M2923, M2895, and M2190 all list Brain heart infusion broth, 1 L; none of the TOGO payloads list calf-brain, beef-heart, proteose-peptone, dextrose, sodium-chloride, or disodium-phosphate rows. | All three normalized owners; likely also the BHI premix expansion importer |
| Major | Primary source provenance and H. influenzae growth scope are absent. | M2923 and M2895 comments resolve to primary H. influenzae papers, but the record keeps only TOGO accessions and has no target-organism or growth-condition fields. | M2923 and M2895 normalized owners |
| Minor | NAD lacks term grounding. | TOGO resolves NAD to `GMO_001691` with label `Beta-NAD`; all three normalized rows have only `preferred_term: NAD`. | All three normalized owners |

## Recommended Edits

1. Split M2190 from the M2923/M2895 fingerprint so the 15/15 ug/ml recipe does
   not merge with 10/2 ug/ml recipes.
2. Convert or preserve all three haemin and NAD supplement amounts in ug/ml.
3. Restore the final BHI broth component as a 1 L opaque base unless a primary
   product specification is attached for the expanded formula.
4. Add primary DOI/PMID provenance for the M2923 and M2895 TOGO comments, and
   add narrow H. influenzae / 37 C growth metadata where the source supports it.
5. Resolve NAD to an exact Beta-NAD term or leave it explicitly unresolved with
   the TOGO GMO identifier as a lead.
6. Regenerate merged YAML after the normalized owners or importers are fixed.

## Follow-up Checks

- Rerun focused schema, strict, reference, and term validators on each corrected
  normalized owner.
- Rerun `just validate` after the project `llvmlite` build issue is resolved.
- Regenerate merges and confirm M2190 no longer merges with M2923/M2895.
- Manually compare the regenerated records against TOGO M2923, M2895, and M2190
  and verify supplement concentrations preserve the distinct 10/2 and 15/15
  ug/ml recipes.

## Additional Notes

- M2190 was not treated as a duplicate source record because its supplement
  amounts differ from the canonical generated record.
