# YAML Record Review: brain-heart infusion agar (upplemented with 10% calf blood and antibiotics)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/brain_heart_infusion_agar_upplemented_with_10_calf_blood_and_antibiotics.yaml
- Started UTC: 2026-09-21T23:37:26Z
- Finished UTC: 2026-09-21T23:39:11Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009396 |
| Label | brain-heart infusion agar (upplemented with 10% calf blood and antibiotics) |
| Source accession | TOGO:M2854 |
| Merge source | data/normalized_yaml/bacterial/brain_heart_infusion_agar_upplemented_with_10_calf_blood_and_antibiotics.yaml |
| Generated status | Generated merge with one normalized owner |
| Merge fingerprint | 21ad98049c35221ed9fc189cfca6489e88fe6a210ae39ea7515c4ca5ce6d3d89 |

The reviewed file is generated from a single normalized owner. The generated
merge is stale with respect to August 2026 CHEBI groundings in the normalized
owner, but the amount and condition errors still belong in
`data/normalized_yaml/bacterial/brain_heart_infusion_agar_upplemented_with_10_calf_blood_and_antibiotics.yaml`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/brain_heart_infusion_agar_upplemented_with_10_calf_blood_and_antibiotics.yaml` | Passed |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/brain_heart_infusion_agar_upplemented_with_10_calf_blood_and_antibiotics.yaml --out /private/tmp/brain_heart_infusion_agar_upplemented_with_10_calf_blood_and_antibiotics.strict.tsv --workers 1 --quiet` | Passed |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/brain_heart_infusion_agar_upplemented_with_10_calf_blood_and_antibiotics.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/brain_heart_infusion_agar_upplemented_with_10_calf_blood_and_antibiotics.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` gate validates standalone records under `history/`, not embedded `MediaRecipe.curation_history` entries in one merge file |

The direct `just validate-schema`, `just validate-strict`, and
`just validate-terms` recipes were not rerun for this record because project
environment creation currently stops while building `llvmlite==0.46.0` under
Python 3.13. The equivalent narrow validators above were run in a no-project
Python 3.11 tool environment.

## Identity and Grounding

- TOGO:M2854 resolves to the same antibiotic-supplemented BHI agar named by
  the record.
- The TOGO API payload has no `src_url`; the reviewed record also lacks a
  primary literature reference for the source paragraph that TOGO mined.
- A gitignore-independent search for `TOGO:M2854`, `CultureMech:009396`, the
  merge fingerprint, the normalized slug, and `M2854` across `data`, `src`,
  `scripts`, `docs`, `.claude`, and `justfile` found one normalized owner plus
  the generated merge and generated indexes.
- The normalized owner has CHEBI groundings for vancomycin and trimethoprim
  from an August 2026 MIM grounding pass; the generated merge predates that
  grounding.

## Evidence

The TOGO M2854 payload lists amphotericin B at 8 ug/ml, vancomycin at 6 ug/ml,
trimethoprim at 5 ug/ml, calf blood at 10%, brain-heart infusion agar at 1 L,
and carbon dioxide, nitrogen, and oxygen as gas components. Its comment states
that all strains were grown for 48 to 72 h at 37 C under microaerophilic
conditions of 5% O2, 10% CO2, and 85% N2 on BHI agar supplemented with 10%
calf blood and those three antibiotics.

The source supports atmosphere and incubation conditions, not a formulation in
which CO2, N2, and O2 are variable-concentration ingredients.

## Completeness

- Consequential gap: amphotericin B, vancomycin, and trimethoprim are present
  at values 1000-fold too high.
- Consequential gap: the 48 to 72 h, 37 C, 5% O2, 10% CO2, and 85% N2 growth
  conditions from TOGO's mined sentence are absent.
- Consequential gap: no primary citation is present. TOGO's `src_url` for
  M2854 is blank, so the exact source article remains unresolved in this
  record review.
- A target-specific `find` under `reports/yaml_record_review` found no prior
  `brain_heart_infusion_agar_upplemented_with_10_calf_blood_and_antibiotics`
  report, so this report did not overwrite an earlier review.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Antibiotic ug/ml concentrations were imported as g/L. Amphotericin B 8 ug/ml, vancomycin 6 ug/ml, and trimethoprim 5 ug/ml are represented as 8, 6, and 5 `G_PER_L`. | TOGO M2854 records the three antibiotic units as `ug/ml`; 1 ug/ml equals 1 mg/L, so the normalized values are 1000-fold too high. | `data/normalized_yaml/bacterial/brain_heart_infusion_agar_upplemented_with_10_calf_blood_and_antibiotics.yaml` |
| Major | The basal `brain-heart infusion agar` row is a one-liter medium base in TOGO but is represented as `1 G_PER_L`. | TOGO M2854 lists `brain-heart infusion agar` with `volume: 1` and `unit: L`. | `data/normalized_yaml/bacterial/brain_heart_infusion_agar_upplemented_with_10_calf_blood_and_antibiotics.yaml` |
| Major | Gas atmosphere rows are modeled as VARIABLE ingredients. | TOGO's source comment scopes O2, CO2, and N2 to a microaerophilic incubation atmosphere with 5%, 10%, and 85% respectively. | `data/normalized_yaml/bacterial/brain_heart_infusion_agar_upplemented_with_10_calf_blood_and_antibiotics.yaml` |
| Major | `calf blood` is represented as `PERCENT_W_V`, but the source says only 10% calf blood. | TOGO M2854 does not state the percent basis for calf blood. | `data/normalized_yaml/bacterial/brain_heart_infusion_agar_upplemented_with_10_calf_blood_and_antibiotics.yaml` |
| Minor | The generated merge is stale before the August 2026 CHEBI grounding of vancomycin and trimethoprim. | The normalized owner has CHEBI terms for both antimicrobial rows; the generated record lacks them. | Regenerate `data/merge_yaml/merged/brain_heart_infusion_agar_upplemented_with_10_calf_blood_and_antibiotics.yaml` after curation |

## Recommended Edits

1. Convert amphotericin B, vancomycin, and trimethoprim from the unsupported
   `G_PER_L` rows back to the source ug/ml values.
2. Represent the 1 L brain-heart infusion agar base as an opaque basal medium,
   not as `1 G_PER_L`.
3. Move O2, CO2, and N2 out of `ingredients` and record the microaerophilic
   atmosphere as 5% O2, 10% CO2, and 85% N2.
4. Keep calf blood at 10%, but remove the unsupported `PERCENT_W_V` specificity
   unless a source establishes the percent basis.
5. Preserve the 48 to 72 h and 37 C incubation context from TOGO's source
   comment.
6. Resolve and add the primary citation behind TOGO M2854 if available.
7. Regenerate the generated merge after the normalized owner is corrected.

## Follow-up Checks

- Rerun `just validate data/normalized_yaml/bacterial/brain_heart_infusion_agar_upplemented_with_10_calf_blood_and_antibiotics.yaml`
  after curation.
- Rerun the focused LinkML, strict, term, and reference validators on the
  normalized owner and regenerated merge.
- Rerun `just verify-merges` to prove the merged record was regenerated from
  the corrected normalized source.
- Manually compare the corrected row set to TOGO M2854 to confirm the
  antibiotic and gas percentages retain their original units and scope.

## Additional Notes

- The filename and source label misspell `supplemented` as `upplemented`; this
  report preserved the record's current slug while reviewing it.
- `calf blood` and `brain-heart infusion agar` are unresolved in the
  ingredient-grounding report, but this review did not force a CHEBI grounding
  for those complex undefined materials.
