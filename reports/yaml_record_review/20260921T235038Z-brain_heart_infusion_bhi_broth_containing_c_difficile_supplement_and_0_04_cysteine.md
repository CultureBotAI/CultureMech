# YAML Record Review: Brain heart infusion (BHI) broth containing C. difficile supplement and 0.04% cysteine

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/brain_heart_infusion_bhi_broth_containing_c_difficile_supplement_and_0_04_cysteine.yaml
- Started UTC: 2026-09-21T23:50:38Z
- Finished UTC: 2026-09-21T23:51:36Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009359 |
| Label | Brain heart infusion (BHI) broth containing C. difficile supplement and 0.04% cysteine |
| Source accession | TOGO:M2811 |
| Merge source | data/normalized_yaml/bacterial/brain_heart_infusion_bhi_broth_containing_c_difficile_supplement_and_0_04_cysteine.yaml |
| Generated status | Generated merge with one normalized owner |
| Merge fingerprint | e36b75f207ee95ac6143abaaf9b6a57a740f0dff56a740dad434b7ab76f1abca |

The reviewed file is generated, and the generated content currently matches its
single normalized owner. Future fixes belong in
`data/normalized_yaml/bacterial/brain_heart_infusion_bhi_broth_containing_c_difficile_supplement_and_0_04_cysteine.yaml`
or in the TOGO import and BHI-premix paths that populated it.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/brain_heart_infusion_bhi_broth_containing_c_difficile_supplement_and_0_04_cysteine.yaml` | Passed |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/brain_heart_infusion_bhi_broth_containing_c_difficile_supplement_and_0_04_cysteine.yaml --out /private/tmp/brain_heart_infusion_bhi_broth_containing_c_difficile_supplement_and_0_04_cysteine.strict.tsv --workers 1 --quiet` | Passed with 0 error rows |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/brain_heart_infusion_bhi_broth_containing_c_difficile_supplement_and_0_04_cysteine.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/brain_heart_infusion_bhi_broth_containing_c_difficile_supplement_and_0_04_cysteine.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` gate validates standalone records under `history/`, not embedded `MediaRecipe.curation_history` entries in one merge file |

The direct `just validate-schema`, `just validate-strict`, and
`just validate-terms` recipes were not rerun for this record because project
environment creation currently stops while building `llvmlite==0.46.0` under
Python 3.13. The equivalent narrow validators above were run in a no-project
Python 3.11 tool environment.

## Identity and Grounding

- `TOGO:M2811` identifies Brain heart infusion broth containing C. difficile
  supplement and 0.04% cysteine.
- The TOGO M2811 API payload has no `src_url`, but its captured medium and
  atmosphere text resolves by exact phrase search to Stabler et al. 2009,
  Genome Biology, PMID 19781061, DOI `10.1186/gb-2009-10-9-r102`.
- TOGO M2811 lists cysteine at 0.04%, Brain heart infusion broth (Oxoid) as a
  1 L base, an anaerobic gas mix of CO2/N2/H2, and a `C. difficile supplement`
  subcomponent with D-cycloserine and cefoxitin.
- A gitignore-independent exact search for `TOGO:M2811`,
  `CultureMech:009359`, the merge fingerprint, and the normalized slug covered
  generated records, normalized records, local indexes, reports, source,
  scripts, `justfile`, and `.claude`; it found only this normalized owner and
  this generated merge for the M2811 source accession.

The record identity is correct, and the 0.04% cysteine amount is preserved. The
record is still source-inaccurate because it flattens the 1 L Oxoid BHI broth
base, the anaerobic incubation atmosphere, and the C. difficile supplement into
unsupported top-level ingredient rows.

## Evidence

The inspected TOGO payload and the primary Stabler et al. article support BHI
broth containing Oxoid C. difficile supplement and 0.04% cysteine for C.
difficile. The cultures were incubated at 37 C in an anaerobic atmosphere with
10% CO2, 10% H2, and 80% N2.

The normalized record correctly preserves cysteine as 0.04% w/v. Its Oxoid BHI
broth base, however, is replaced by inferred BD/Difco BHI constituents from a
MicrobeNotes page. The source calls for an Oxoid broth base and does not list
calf brain, beef heart, proteose peptone, dextrose, sodium chloride, or disodium
phosphate separately.

TOGO imported CO2, N2, and H2 as gas rows because the paper states the anaerobic
growth atmosphere. Those gases are not broth ingredients and their fractions
are known from the source, so `VARIABLE` ingredient rows lose both the
atmosphere boundary and the 10/10/80 composition.

TOGO imported a `C. difficile supplement` reference and nested D-cycloserine and
cefoxitin below that supplement. The generated record stores the supplement and
both antibiotic components as separate top-level variable-concentration
ingredients, even though the inspected paper identifies only the commercial
supplement in the BHI broth recipe and does not give antibiotic amounts.

## Completeness

- Consequential gap: the primary DOI/PMID is absent because TOGO M2811 has an
  empty `src_url` and the normalized record only cites TOGO.
- Consequential gap: the C. difficile / 37 C / anaerobic atmosphere growth
  condition from Stabler et al. is not represented as structured growth or
  incubation metadata.
- Consequential gap: the record does not keep C. difficile supplement as a
  nested or referenced supplement boundary.
- TOGO M2811 carries final pH 7.4 +/- 0.2, but the normalized record only
  mentions pH inside an inferred Disodium phosphate note attached to the
  expanded BHI base.
- A gitignore-independent exact search under `reports/yaml_record_review` for
  the normalized slug, `C. difficile supplement`, and the merge fingerprint
  found no prior report for this target.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The 1 L Oxoid BHI broth base was expanded into unsupported BD/Difco constituent rows. | TOGO M2811 lists `Brain heart infusion (BHI) broth (Oxoid)`, 1 L; Stabler et al. name BHI broth with C. difficile supplement and 0.04% cysteine, not calf-brain, beef-heart, proteose-peptone, dextrose, sodium-chloride, and disodium-phosphate rows. | `data/normalized_yaml/bacterial/brain_heart_infusion_bhi_broth_containing_c_difficile_supplement_and_0_04_cysteine.yaml`; likely also the BHI premix expansion importer |
| Major | The anaerobic incubation atmosphere was imported as variable-concentration medium ingredients. | Stabler et al. state that cultures were grown under 10% CO2, 10% H2, and 80% N2 at 37 C; the record stores CO2, N2, and H2 as `VARIABLE` ingredients. | `data/normalized_yaml/bacterial/brain_heart_infusion_bhi_broth_containing_c_difficile_supplement_and_0_04_cysteine.yaml`; likely also the TOGO gas importer |
| Major | C. difficile supplement, D-cycloserine, and cefoxitin are flattened into separate unquantified top-level rows. | TOGO M2811 has `C. difficile supplement` as a referenced supplement and nests D-cycloserine and Cefoxitin under that supplement; the source paper gives no final antibiotic amounts. | `data/normalized_yaml/bacterial/brain_heart_infusion_bhi_broth_containing_c_difficile_supplement_and_0_04_cysteine.yaml`; likely also the TOGO subcomponent importer |
| Major | Primary source and growth-condition metadata are absent. | The TOGO comments resolve to Stabler et al. 2009, PMID 19781061, DOI `10.1186/gb-2009-10-9-r102`, which scopes the formulation to C. difficile cultures grown at 37 C anaerobically; the record has no primary DOI/PMID, no target-organism entry, and no structured incubation condition. | `data/normalized_yaml/bacterial/brain_heart_infusion_bhi_broth_containing_c_difficile_supplement_and_0_04_cysteine.yaml` |

## Recommended Edits

1. Restore the source base as 1 L Brain heart infusion (BHI) broth (Oxoid) and
   remove inferred BD/Difco BHI constituent rows unless an Oxoid primary product
   specification is attached.
2. Move CO2, H2, and N2 out of ingredients into anaerobic atmosphere metadata
   that preserves the 10%, 10%, and 80% fractions.
3. Keep `C. difficile supplement` as a referenced or nested supplement and avoid
   promoting D-cycloserine and cefoxitin to final-medium ingredients unless
   their amounts are recovered from the supplement formulation.
4. Add Stabler et al. 2009 DOI/PMID provenance and narrowly scoped C. difficile
   / 37 C growth metadata if the current schema has slots for that assertion.
5. Regenerate the merged YAML after the normalized owner or importer is fixed.

## Follow-up Checks

- Rerun focused schema, strict, reference, and term validators on the corrected
  normalized owner.
- Rerun `just validate` after the project `llvmlite` build issue is resolved.
- Regenerate merges and confirm gases are no longer generated as broth
  ingredients for M2811.
- Manually compare the regenerated record against TOGO M2811 and Stabler et al.
  2009 to ensure the C. difficile supplement boundary is retained.

## Additional Notes

- Optional preparation details were not treated as defects because the inspected
  primary text only names the base, supplement, cysteine percentage, organism,
  temperature, and atmosphere.
