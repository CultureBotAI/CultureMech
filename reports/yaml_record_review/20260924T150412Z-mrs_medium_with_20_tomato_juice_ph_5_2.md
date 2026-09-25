# YAML Record Review: MRS medium with 20% Tomato Juice (pH 5.2)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mrs_medium_with_20_tomato_juice_ph_5_2.yaml
- Started UTC: 2026-09-24T15:03:01Z
- Finished UTC: 2026-09-24T15:04:12Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` record `CultureMech:008568` / `mrs_medium_with_20_tomato_juice_ph_5_2` at `data/merge_yaml/merged/mrs_medium_with_20_tomato_juice_ph_5_2.yaml`.

- Generated source: `data/normalized_yaml/bacterial/mrs_medium_with_20_tomato_juice_ph_5_2.yaml`
- Merge source: `mrs_medium_with_20_tomato_juice_ph_5_2`
- Merge fingerprint: `8034cad986113b46bc73190a4b8df4f846d874f9fc73b25bee03f1edc8692603`
- Category: `bacterial`
- Medium term: `TOGO:M1985`, label `MRS medium with 20% Tomato Juice (pH 5.2)`
- Original source: NBRC medium 1271

## Validation

| Check | Result |
|---|---|
| Open LinkML schema with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mrs_medium_with_20_tomato_juice_ph_5_2.yaml` | Passed. |
| Strict validator with `scripts/validate_strict.py data/merge_yaml/merged/mrs_medium_with_20_tomato_juice_ph_5_2.yaml --out /private/tmp/mrs_medium_with_20_tomato_juice_ph_5_2.strict.tsv --workers 1 --quiet` | Passed with 0 error rows. |
| Reference validator with `linkml-reference-validator validate data data/merge_yaml/merged/mrs_medium_with_20_tomato_juice_ph_5_2.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks were applicable. |
| Term validator with `linkml-term-validator validate-data data/merge_yaml/merged/mrs_medium_with_20_tomato_juice_ph_5_2.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` | Not checked: the documented `just validate-history` target validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` events. |

## Identity and Grounding

The record identifies TOGO M1985, a TOGO import of NBRC medium 1271. TOGO reports `gm` `http://togomedium.org/medium/M1985`, original media ID `NBRC_M1271`, source URL `https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1271`, and pH 5.2. The inspected NBRC page is for Medium No. 1271 and has the same `MRS medium with 20% Tomato Juice (pH 5.2)` title.

Most dry solute amounts are supported by TOGO and NBRC. Four identity or representation problems remain:

- `Distilled water` is 800 ml in TOGO/NBRC but 800 `G_PER_L` in YAML.
- `Tomato Juice (filtered)` is 200 ml in TOGO/NBRC but 200 `G_PER_L` in YAML.
- Agar is listed as `Agar (if needed)` in TOGO/NBRC, but the generated record is globally `SOLID_AGAR`.
- `MnSO4 nH2O` is a variable manganese sulfate hydrate but is grounded to generic `CHEBI:86360`.

The exact `CultureMech:008568` search across `data/normalized_yaml` and `data/merge_yaml` used `rg --no-ignore --hidden`. It found one maintained YAML owner, this generated merge, and generated indexes only. An exact ignored-file-inclusive search for `NO=1271` likewise found only this owner and generated merge.

## Evidence

The inspected TOGO M1985 JSON and NBRC 1271 HTML agree on all ingredient quantities: 800 ml distilled water, 0.2 g MgSO4 x 7H2O, 5 g yeast extract, 2 g K2HPO4, 5 g sodium acetate, 1 g Tween 80, 0.05 g MnSO4 nH2O, 2 g diammonium hydrogen citrate, 200 ml filtered tomato juice, 20 g glucose, optional 15 g agar, 10 g meat extract, and 10 g peptone.

Both inspected sources state pH 5.2. The generated and maintained YAML omit `ph_value` and have no pH-adjustment preparation step.

## Completeness

The record is incomplete because pH 5.2 and the pH adjustment are absent. The formula is dimensionally wrong for water and tomato juice, and the optional agar supplement is represented as the required physical state.

Empty target-organism and growth-metric fields are not defects; TOGO M1985 and NBRC 1271 only define the medium.

## Findings

### Major

1. Water and tomato juice use mass units instead of source volumes.
   - Evidence: TOGO M1985 and NBRC 1271 list 800 ml distilled water and 200 ml filtered tomato juice; the maintained and generated YAML store them as 800 and 200 `G_PER_L`.
   - Impact: the 20% tomato-juice formulation is dimensionally wrong.
   - Owner: `data/normalized_yaml/bacterial/mrs_medium_with_20_tomato_juice_ph_5_2.yaml`, then regenerate `data/merge_yaml/merged/mrs_medium_with_20_tomato_juice_ph_5_2.yaml`.

2. The pH is missing.
   - Evidence: TOGO M1985 exposes `ph: 5.2`, and the NBRC medium title includes pH 5.2.
   - Impact: the final pH in the record name is not represented in a machine-readable pH field or preparation step.
   - Owner: `data/normalized_yaml/bacterial/mrs_medium_with_20_tomato_juice_ph_5_2.yaml`, then regenerate.

3. Optional agar was promoted to a required solid medium state.
   - Evidence: TOGO M1985 and NBRC 1271 both list `Agar (if needed)`, but the generated record is `physical_state: SOLID_AGAR`.
   - Impact: consumers will interpret the formulation as necessarily solid although NBRC makes agar optional.
   - Owner: `data/normalized_yaml/bacterial/mrs_medium_with_20_tomato_juice_ph_5_2.yaml`, then regenerate.

4. The variable manganese sulfate hydrate is over-grounded.
   - Evidence: TOGO M1985 and NBRC 1271 list `MnSO4 nH2O`; the YAML grounds that variable hydrate row to generic `CHEBI:86360`.
   - Impact: the row presents an exact CHEBI identity for an unresolved hydrate.
   - Owner: `data/normalized_yaml/bacterial/mrs_medium_with_20_tomato_juice_ph_5_2.yaml`, then regenerate.

### Minor

None found.

### Blocker

None found.

## Recommended Edits

1. Convert the water and filtered tomato-juice rows to supported ml volume representations.
2. Add pH 5.2 and a pH-adjustment preparation step.
3. Represent agar as an optional 15 g supplement instead of making the whole record `SOLID_AGAR`.
4. Remove exact CHEBI grounding from `MnSO4 nH2O` unless an exact variable-hydrate term is available.
5. Append a `curation_history` event naming TOGO M1985 and NBRC 1271 evidence, then regenerate `data/merge_yaml/merged/`.

## Follow-up Checks

After curation, run the same focused generated-record checks:

- `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mrs_medium_with_20_tomato_juice_ph_5_2.yaml`
- `python scripts/validate_strict.py data/merge_yaml/merged/mrs_medium_with_20_tomato_juice_ph_5_2.yaml --workers 1 --quiet`
- `linkml-reference-validator validate data data/merge_yaml/merged/mrs_medium_with_20_tomato_juice_ph_5_2.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- `linkml-term-validator validate-data data/merge_yaml/merged/mrs_medium_with_20_tomato_juice_ph_5_2.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`

Also rerun the merge freshness check that owns `data/merge_yaml/merged/` to confirm the generated record reflects the normalized corrections.

## Additional Notes

None found.
