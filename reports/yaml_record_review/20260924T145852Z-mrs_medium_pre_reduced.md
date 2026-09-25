# YAML Record Review: MRS MEDIUM (pre-reduced)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mrs_medium_pre_reduced.yaml
- Started UTC: 2026-09-24T14:57:46Z
- Finished UTC: 2026-09-24T14:58:52Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` record `CultureMech:000649` / `mrs_medium_pre_reduced` at `data/merge_yaml/merged/mrs_medium_pre_reduced.yaml`.

- Generated source: `data/normalized_yaml/bacterial/mrs_medium_pre_reduced.yaml`
- Merge source: `mrs_medium_pre_reduced`
- Merge fingerprint: `c5f16cac1163ad857026089523f6262329f73c862c8977bf1d4dc91b6ed384b3`
- Category: `bacterial`
- Medium term: `mediadive.medium:11b`, `DSMZ Medium 11b`, label `MRS MEDIUM (pre-reduced)`
- Source: DSMZ Medium 11b PDF

## Validation

| Check | Result |
|---|---|
| Open LinkML schema with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mrs_medium_pre_reduced.yaml` | Passed. |
| Strict validator with `scripts/validate_strict.py data/merge_yaml/merged/mrs_medium_pre_reduced.yaml --out /private/tmp/mrs_medium_pre_reduced.strict.tsv --workers 1 --quiet` | Passed with 0 error rows. |
| Reference validator with `linkml-reference-validator validate data data/merge_yaml/merged/mrs_medium_pre_reduced.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks were applicable. |
| Term validator with `linkml-term-validator validate-data data/merge_yaml/merged/mrs_medium_pre_reduced.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` | Not checked: the documented `just validate-history` target validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` events. |

## Identity and Grounding

The record denotes DSMZ / MediaDive medium 11b, MRS MEDIUM (pre-reduced). MediaDive REST returned `id` `11b`, the same label, source `DSMZ`, pH 6.2-6.5, the DSMZ Medium 11b PDF link, and a 1000 ml main solution.

The represented solute rows preserve MediaDive and DSMZ amounts:

| Source row | YAML row | Review |
|---|---|---|
| Glucose, 20 g | `Glucose`, 20 `G_PER_L`, `CHEBI:17234` | Supported. |
| Tween 80, 1 g | `Tween 80`, 1 `G_PER_L`, `CHEBI:53426` | Supported. |
| Resazurin, 1 mg | `Resazurin`, 0.001 `G_PER_L`, `CHEBI:8806` | Supported. |
| K2HPO4, 2 g | `K2HPO4`, 2 `G_PER_L`, `CHEBI:131527` | Supported. |
| Na-acetate, 5 g | `Na-acetate`, 5 `G_PER_L`, `CHEBI:32954` | Supported. |
| (NH4)3 citrate, 2 g | `(NH4)3 citrate`, 2 `G_PER_L`, `CHEBI:63037` | Supported. |
| MgSO4 x 7 H2O, 0.2 g | `MgSO4 x 7 H2O`, 0.2 `G_PER_L`, `CHEBI:31795` | Supported. |
| MnSO4 x H2O, 0.05 g | `MnSO4 x H2O`, 0.05 `G_PER_L`, `CHEBI:86364` | Supported. |
| L-Cysteine HCl x H2O, 0.5 g | `L-Cysteine HCl x H2O`, 0.5 `G_PER_L`, `CHEBI:91248` | Supported. |

The extract and peptone rows are intentionally unresolved complex ingredients. Casein peptone still loses MediaDive's `tryptic digest` attribute.

The exact `CultureMech:000649` search across `data/normalized_yaml` and `data/merge_yaml` used `rg --no-ignore --hidden`. It found one maintained YAML owner, this generated merge, and generated indexes only. An exact ignored-file-inclusive search for `DSMZ_Medium11b.pdf` also found only the maintained owner and this generated merge.

## Evidence

The DSMZ PDF lists MRS MEDIUM (pre-reduced) with 12 represented solutes plus 1000 ml distilled water. MediaDive REST medium 11b preserves the same rows and also marks medium 11b as a 1000 ml main solution.

DSMZ and MediaDive both support the pH 6.2-6.5 range and the instruction that cysteine is added after the medium has been boiled and cooled under CO2, then pH adjusted, distributed under N2, and autoclaved. The record preserves that sentence as a preparation step. MediaDive also lists `Autoclave`, `Hungate tubes`, and `Gassing station` equipment; the schema representation has no corresponding structured equipment rows in this YAML.

## Completeness

The recipe is incomplete because `Distilled water`, 1000 ml, is absent from both `data/normalized_yaml/bacterial/mrs_medium_pre_reduced.yaml` and this generated record.

The pH, pre-reduction additions, anaerobic gas handling, and autoclave instruction are present. No target-organism or growth-metric claims are present; their absence is acceptable for a DSMZ source recipe without strain-specific growth evidence.

## Findings

### Major

1. The DSMZ water row is missing.
   - Evidence: DSMZ Medium 11b and MediaDive REST medium 11b both list `Distilled water`, 1000 ml; neither the maintained nor generated YAML has a water ingredient.
   - Impact: the formulation has the pre-reduction solutes but omits the final-volume solvent.
   - Owner: `data/normalized_yaml/bacterial/mrs_medium_pre_reduced.yaml`, then regenerate `data/merge_yaml/merged/mrs_medium_pre_reduced.yaml`.

### Minor

1. The casein-peptone source attribute is not preserved.
   - Evidence: MediaDive annotates `Casein peptone` with attribute `tryptic digest`; the YAML keeps only `Casein peptone`.
   - Impact: the row's amount and broad identity are correct, but source wording that distinguishes the intended peptone form is lost.
   - Owner: `data/normalized_yaml/bacterial/mrs_medium_pre_reduced.yaml`, then regenerate `data/merge_yaml/merged/mrs_medium_pre_reduced.yaml`.

### Blocker

None found.

## Recommended Edits

1. Add the missing `Distilled water`, 1000 ml ingredient to `data/normalized_yaml/bacterial/mrs_medium_pre_reduced.yaml` using a volume representation.
2. Preserve MediaDive's `tryptic digest` attribute on the casein-peptone row, either structurally if supported or in a narrow curation note.
3. Append a `curation_history` event naming DSMZ Medium 11b / MediaDive 11b evidence and regenerate `data/merge_yaml/merged/mrs_medium_pre_reduced.yaml`.

## Follow-up Checks

After curation, run the same focused generated-record checks:

- `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mrs_medium_pre_reduced.yaml`
- `python scripts/validate_strict.py data/merge_yaml/merged/mrs_medium_pre_reduced.yaml --workers 1 --quiet`
- `linkml-reference-validator validate data data/merge_yaml/merged/mrs_medium_pre_reduced.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- `linkml-term-validator validate-data data/merge_yaml/merged/mrs_medium_pre_reduced.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`

Also rerun the merge freshness check that owns `data/merge_yaml/merged/` to confirm the generated record reflects the maintained water-row addition.

## Additional Notes

- MediaDive's equipment context is visible in the inspected REST response, but the text preparation step already preserves the gassing and autoclaving requirements in the DSMZ sentence.
