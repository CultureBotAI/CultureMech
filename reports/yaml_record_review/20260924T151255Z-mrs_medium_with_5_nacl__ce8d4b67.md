# YAML Record Review: MRS MEDIUM WITH 5% NaCl

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mrs_medium_with_5_nacl__ce8d4b67.yaml
- Started UTC: 2026-09-24T15:12:21Z
- Finished UTC: 2026-09-24T15:12:55Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` record `CultureMech:002859` / `mrs_medium_with_5_nacl` at `data/merge_yaml/merged/mrs_medium_with_5_nacl__ce8d4b67.yaml`.

- Generated source: `data/normalized_yaml/bacterial/mrs_medium_with_5_nacl.yaml`
- Merge source: `mrs_medium_with_5_nacl`
- Merge fingerprint: `ce8d4b67cc45c5d7be02ae942286c05099664683a680a9343ac5646ea2ff4037`
- Category: `bacterial`
- Medium term: `mediadive.medium:J509`, label `MRS MEDIUM WITH 5% NaCl`
- Source: JCM GRMD 509

## Validation

| Check | Result |
|---|---|
| Open LinkML schema with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mrs_medium_with_5_nacl__ce8d4b67.yaml` | Passed. |
| Strict validator with `scripts/validate_strict.py data/merge_yaml/merged/mrs_medium_with_5_nacl__ce8d4b67.yaml --out /private/tmp/mrs_medium_with_5_nacl__ce8d4b67.strict.tsv --workers 1 --quiet` | Passed with 0 error rows. |
| Reference validator with `linkml-reference-validator validate data data/merge_yaml/merged/mrs_medium_with_5_nacl__ce8d4b67.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks were applicable. |
| Term validator with `linkml-term-validator validate-data data/merge_yaml/merged/mrs_medium_with_5_nacl__ce8d4b67.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` | Not checked: the documented `just validate-history` target validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` events. |

## Identity and Grounding

The record identifies MediaDive/JCM J509, MRS MEDIUM WITH 5% NaCl. JCM GRMD 509 is live and lists 55 g Lactobacillus MRS broth (BD-Difco), 50 g NaCl, 15 g Bacto agar (BD-Difco), and 1 L distilled water.

The record preserves the two exact gram solutes, but it omits water:

| JCM row | YAML row | Review |
|---|---|---|
| Lactobacillus MRS broth (BD-Difco), 55 g | `Lactobacillus MRS broth`, 55 `G_PER_L` | Amount supported; BD-Difco qualifier missing. |
| NaCl, 50 g | `NaCl`, 50 `G_PER_L`, `CHEBI:26710` | Supported. |
| Bacto agar (BD-Difco), 15 g | `Agar`, 15 `G_PER_L`, `CHEBI:2509` | Amount supported; Bacto / BD-Difco qualifier missing. |
| Distilled water, 1 L | None | Missing. |

The exact `CultureMech:002859` search across `data/normalized_yaml` and `data/merge_yaml` used `rg --no-ignore --hidden`. It found one maintained YAML owner, this generated merge, and generated indexes only.

## Evidence

JCM GRMD 509 and the TOGO M510 mirror both support the same 5% NaCl formula and the 1 L water row. JCM also states its default sterilization instruction of autoclaving at 121 C for 15 min when no exception is listed; the generated and maintained YAML have no preparation step.

An exact ignored-file-inclusive search for `GRMD=509` found this MediaDive/JCM J509 owner and `data/normalized_yaml/bacterial/TOGO_M510_MRS_Medium_With_5_NaCl.yaml`, the TOGO import of the same JCM source. Those two inputs are duplicate imports of GRMD 509.

The `kg_microbe_match` on this maintained MediaDive input points to `mediadive.medium:101`, which resolves to DSMZ Medium 101, NUTRIENT AGAR or BROTH WITH NaCl, a different formula.

## Completeness

The generated record is incomplete because it omits the source water and lacks the JCM default autoclave preparation step. Empty pH, target-organism, and growth-metric fields are acceptable because JCM GRMD 509 does not specify pH or growth evidence.

## Findings

### Major

1. The JCM/MediaDive import omits the 1 L water row.
   - Evidence: JCM GRMD 509 and TOGO M510 both list 1 L distilled water; `data/normalized_yaml/bacterial/mrs_medium_with_5_nacl.yaml` and this generated record have no water ingredient.
   - Impact: the base solvent is absent from the J509 formula.
   - Owner: `data/normalized_yaml/bacterial/mrs_medium_with_5_nacl.yaml`, then regenerate `data/merge_yaml/merged/mrs_medium_with_5_nacl__ce8d4b67.yaml`.

2. The JCM default autoclave instruction is missing.
   - Evidence: the JCM GRMD 509 page includes the default 121 C for 15 min sterilization statement, and it does not list a contrary exception.
   - Impact: the complete preparation is absent.
   - Owner: `data/normalized_yaml/bacterial/mrs_medium_with_5_nacl.yaml`, then regenerate.

3. `kg_microbe_match` points to a different medium.
   - Evidence: this J509 record carries `kg_microbe_match: mediadive.medium:101`; `mediadive.medium:101` is DSMZ Medium 101, NUTRIENT AGAR or BROTH WITH NaCl.
   - Impact: the 5% NaCl MRS record is linked to an unrelated DSMZ nutrient agar or broth recipe.
   - Owner: `data/normalized_yaml/bacterial/mrs_medium_with_5_nacl.yaml`.

4. JCM GRMD 509 remains split across TOGO and MediaDive imports.
   - Evidence: `data/normalized_yaml/bacterial/mrs_medium_with_5_nacl.yaml` and `data/normalized_yaml/bacterial/TOGO_M510_MRS_Medium_With_5_NaCl.yaml` both cite GRMD 509.
   - Impact: the same JCM 5% NaCl MRS medium can publish twice unless equivalent TOGO and MediaDive JCM imports are reconciled.
   - Owner: both normalized records plus the merge/de-duplication rule for equivalent TOGO and MediaDive JCM imports.

### Minor

1. BD-Difco qualifiers are not preserved on the imported product rows.
   - Evidence: JCM GRMD 509 lists `Lactobacillus MRS broth (BD-Difco)` and `Bacto agar (BD-Difco)`; the MediaDive/JCM record stores only `Lactobacillus MRS broth` and `Agar`.
   - Impact: the formula amounts are correct, but source supplier wording is lost.
   - Owner: `data/normalized_yaml/bacterial/mrs_medium_with_5_nacl.yaml`.

### Blocker

None found.

## Recommended Edits

1. Add the missing 1 L distilled-water row to `data/normalized_yaml/bacterial/mrs_medium_with_5_nacl.yaml`.
2. Add the JCM default 121 C for 15 min autoclave step.
3. Remove or correct the unrelated `mediadive.medium:101` KG-Microbe match.
4. Preserve the BD-Difco qualifiers on the MRS broth and agar product rows.
5. Reconcile MediaDive/JCM J509 with the TOGO M510 duplicate.
6. Append curation-history events to changed normalized inputs and regenerate `data/merge_yaml/merged/`.

## Follow-up Checks

After curation, run the same focused generated-record checks:

- `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mrs_medium_with_5_nacl__ce8d4b67.yaml`
- `python scripts/validate_strict.py data/merge_yaml/merged/mrs_medium_with_5_nacl__ce8d4b67.yaml --workers 1 --quiet`
- `linkml-reference-validator validate data data/merge_yaml/merged/mrs_medium_with_5_nacl__ce8d4b67.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- `linkml-term-validator validate-data data/merge_yaml/merged/mrs_medium_with_5_nacl__ce8d4b67.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`

Also rerun merge freshness and an exact ignored-file-inclusive `GRMD=509` search to verify the J509 and M510 duplicate is resolved.

## Additional Notes

None found.
