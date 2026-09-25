# YAML Record Review: MRS Medium With 5% NaCl

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mrs_medium_with_5_nacl.yaml
- Started UTC: 2026-09-24T15:10:03Z
- Finished UTC: 2026-09-24T15:11:40Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` record `CultureMech:009901` / `mrs_medium_with_5_nacl` at `data/merge_yaml/merged/mrs_medium_with_5_nacl.yaml`.

- Generated source: `data/normalized_yaml/bacterial/TOGO_M510_MRS_Medium_With_5_NaCl.yaml`
- Merge source: `TOGO_M510_MRS_Medium_With_5_NaCl`
- Merge fingerprint: `7dd44dc280c98a09b584d898ad90a8eedf2bd6df8f9e84db505bd78fb7274c7a`
- Category: `bacterial`
- Medium term: `TOGO:M510`, label `MRS Medium With 5% NaCl`
- Original source: JCM `JCM_M509`, GRMD 509

## Validation

| Check | Result |
|---|---|
| Open LinkML schema with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mrs_medium_with_5_nacl.yaml` | Passed. |
| Strict validator with `scripts/validate_strict.py data/merge_yaml/merged/mrs_medium_with_5_nacl.yaml --out /private/tmp/mrs_medium_with_5_nacl.strict.tsv --workers 1 --quiet` | Passed with 0 error rows. |
| Reference validator with `linkml-reference-validator validate data data/merge_yaml/merged/mrs_medium_with_5_nacl.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks were applicable. |
| Term validator with `linkml-term-validator validate-data data/merge_yaml/merged/mrs_medium_with_5_nacl.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` | Not checked: the documented `just validate-history` target validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` events. |

## Identity and Grounding

The record identifies TOGO M510, a TOGO import of JCM Medium 509, MRS Medium With 5% NaCl. TOGO reports `gm` `http://togomedium.org/medium/M510`, original media ID `JCM_M509`, and source URL `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=509`. JCM GRMD 509 is live and has the same 5% NaCl title.

The sodium chloride, agar, and Lactobacillus MRS broth rows match TOGO and JCM:

| Source row | YAML row | Review |
|---|---|---|
| NaCl, 50 g | `NaCl`, 50 `G_PER_L`, `CHEBI:26710` | Supported. |
| Bacto agar (BD-Difco), 15 g | `Bacto agar (BD-Difco)`, 15 `G_PER_L` | Supported. |
| Lactobacillus MRS broth (BD-Difco), 55 g | same, 55 `G_PER_L` | Supported. |

Distilled water is wrong: both TOGO M510 and JCM GRMD 509 list 1 L distilled water, while the generated and maintained YAML store 1 `G_PER_L`.

The exact `CultureMech:009901` search across `data/normalized_yaml` and `data/merge_yaml` used `rg --no-ignore --hidden`. It found one maintained YAML owner, this generated merge, and generated indexes only.

## Evidence

TOGO M510 and JCM GRMD 509 agree on the 5% NaCl formulation. JCM also states its default sterilization instruction of autoclaving at 121 C for 15 min when no exception is listed; the generated and maintained YAML have no preparation step.

An exact ignored-file-inclusive search for `GRMD=509` using a negative lookahead for following digits found this TOGO M510 owner and `data/normalized_yaml/bacterial/mrs_medium_with_5_nacl.yaml`, the MediaDive/JCM J509 import of the same source. Those two inputs are duplicate imports of the same JCM page.

## Completeness

The record has a dimensionally wrong water row and no preparation step for JCM's default autoclave instruction. Empty pH, target-organism, and growth-metric fields are acceptable because TOGO M510 and JCM GRMD 509 do not specify pH or growth evidence.

## Findings

### Major

1. The 1 L water row uses a mass unit.
   - Evidence: TOGO M510 and JCM GRMD 509 both list 1 L distilled water; the maintained and generated YAML store 1 `G_PER_L`.
   - Impact: the final-volume solvent is dimensionally wrong.
   - Owner: `data/normalized_yaml/bacterial/TOGO_M510_MRS_Medium_With_5_NaCl.yaml`, then regenerate `data/merge_yaml/merged/mrs_medium_with_5_nacl.yaml`.

2. The JCM default autoclave instruction is missing.
   - Evidence: the JCM GRMD 509 page includes the default 121 C for 15 min sterilization statement, and it does not list a contrary exception.
   - Impact: the complete preparation would be missing even after the water row is fixed.
   - Owner: `data/normalized_yaml/bacterial/TOGO_M510_MRS_Medium_With_5_NaCl.yaml`, then regenerate.

3. JCM GRMD 509 remains split across TOGO and MediaDive imports.
   - Evidence: `data/normalized_yaml/bacterial/TOGO_M510_MRS_Medium_With_5_NaCl.yaml` and `data/normalized_yaml/bacterial/mrs_medium_with_5_nacl.yaml` both cite GRMD 509.
   - Impact: the same JCM 5% NaCl MRS medium can publish twice unless equivalent TOGO and MediaDive JCM imports are reconciled.
   - Owner: both normalized records plus the merge/de-duplication rule for equivalent TOGO and MediaDive JCM imports.

### Minor

None found.

### Blocker

None found.

## Recommended Edits

1. Convert distilled water from 1 `G_PER_L` to a supported 1 L volume representation.
2. Add the JCM default 121 C for 15 min autoclave step.
3. Reconcile TOGO M510 with the MediaDive/JCM J509 duplicate.
4. Append curation-history events to changed normalized records and regenerate `data/merge_yaml/merged/`.

## Follow-up Checks

After curation, run the same focused generated-record checks:

- `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mrs_medium_with_5_nacl.yaml`
- `python scripts/validate_strict.py data/merge_yaml/merged/mrs_medium_with_5_nacl.yaml --workers 1 --quiet`
- `linkml-reference-validator validate data data/merge_yaml/merged/mrs_medium_with_5_nacl.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- `linkml-term-validator validate-data data/merge_yaml/merged/mrs_medium_with_5_nacl.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`

Also rerun merge freshness and an exact ignored-file-inclusive `GRMD=509` search to verify the TOGO and MediaDive GRMD 509 imports no longer publish separately.

## Additional Notes

None found.
