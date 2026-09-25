# YAML Record Review: GAM AGAR WITH 0.5% ARGININE

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/gam_agar_with_0_5_arginine__c27f4845.yaml
- Started UTC: 2026-09-23T05:17:32Z
- Finished UTC: 2026-09-23T05:17:58Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:002931`, `gam_agar_with_0_5_arginine`, category `bacterial`, for JCM Medium J583 / MediaDive `mediadive.medium:J583`.

The generated file has one source, `gam_agar_with_0_5_arginine`, with merge fingerprint `c27f484551b8d1b08a49ee20bed75072ec383c83260891aa76c808d05b08b23d`; future YAML edits belong in `data/normalized_yaml/bacterial/gam_agar_with_0_5_arginine.yaml`.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/gam_agar_with_0_5_arginine__c27f4845.yaml` | Passed with `No issues found`. |
| `python scripts/validate_strict.py data/merge_yaml/merged/gam_agar_with_0_5_arginine__c27f4845.yaml --out /private/tmp/gam_agar_with_0_5_arginine_c27f4845.strict.tsv --workers 1 --quiet` | Passed; the TSV had one header row and no error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/gam_agar_with_0_5_arginine__c27f4845.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the reference validator reported zero checks. |
| `linkml-term-validator validate-data data/merge_yaml/merged/gam_agar_with_0_5_arginine__c27f4845.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the repository documents `just validate-history` for standalone files under `history/`, not for generated `MediaRecipe.curation_history` entries. |

## Identity and Grounding

MediaDive REST resolves `J583` to JCM `GAM AGAR WITH 0.5% ARGININE`, complex medium, pH 7.0, and the live JCM `GRMD=583` URL. The live JCM page has the same title, ingredients, amounts, and pH adjustment instruction.

An ignored-file-inclusive search over `data/normalized_yaml` and `data/merge_yaml/merged` for `mediadive.medium:J583`, `CultureMech:002931`, `TOGO:M588`, and `gam_agar_with_0_5_arginine` found this direct JCM import plus a TOGO M588 import that cites `JCM_M583` and the same live JCM URL. They are semantically the same JCM formulation but remain separate CultureMech records.

Arginine is grounded to neutral `CHEBI:29016` / `arginine`, which matches the JCM ingredient better than the argininium grounding on the TOGO sibling.

## Evidence

The direct generated record captures the source masses for the three non-water rows and the pH adjustment:

| JCM ingredient | Source amount | Generated value |
|---|---:|---:|
| GAM broth (Nissui) | 59 g | 59 g/L |
| Arginine | 5 g | 5 g/L |
| Agar | 15 g | 15 g/L |

The generated record loses the `(Nissui)` attribute from the GAM broth row. MediaDive preserves it as `attribute: Nissui`, and the live JCM page prints `GAM broth (Nissui)`. Because GAM broth is an undefined commercial component, the supplier qualifier is part of the recoverable source identity, not just cosmetic punctuation.

The MediaDive representation and the live JCM page both include `Distilled water` at 1000 ml / 1 L. The generated direct-JCM YAML omits that row entirely.

## Completeness

The pH 7.0 scalar and `Adjust pH to 7.0.` preparation step are complete. The undefined commercial `GAM broth` row correctly has no chemical ontology grounding, but it should preserve the Nissui qualifier that JCM and MediaDive provide.

The generated file is incomplete with respect to the source solvent row and to lineage reconciliation with the TOGO M588 snapshot.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | Direct JCM J583 and TOGO M588 remain split despite denoting the same JCM recipe. | TOGO M588 names original medium `JCM_M583` and the same `GRMD=583` URL used by this MediaDive/JCM source, yet the merge emitted two CultureMech IDs and two generated records. | `data/normalized_yaml/bacterial/gam_agar_with_0_5_arginine.yaml`, `data/normalized_yaml/bacterial/TOGO_M588_GAM_Agar_With_0.5_Arginine.yaml`, and merge reconciliation. |
| Major | The Nissui supplier qualifier was dropped from GAM broth. | JCM and MediaDive both identify the row as `GAM broth (Nissui)`; the generated direct import keeps only `GAM broth`. | `data/normalized_yaml/bacterial/gam_agar_with_0_5_arginine.yaml`. |
| Minor | The 1 L distilled-water row is absent. | JCM lists `Distilled water` at 1 L and MediaDive stores it as 1000 ml in the main solution; the generated YAML has no water row. | `data/normalized_yaml/bacterial/gam_agar_with_0_5_arginine.yaml`. |

## Recommended Edits

1. Reconcile the direct JCM J583 and TOGO M588 imports so a regenerated corpus does not keep two separate `GAM AGAR WITH 0.5% ARGININE` records.
2. Preserve `Nissui` as a supplier or source qualifier on the GAM broth ingredient.
3. Decide whether solvent rows should be preserved for simple MediaDive recipes; if they should, add the 1000 ml distilled-water row in this normalized record before regeneration.

## Follow-up Checks

After curation, regenerate `data/merge_yaml/merged/` and rerun focused schema, strict, reference, and term validation on the regenerated direct JCM record or on the merged TOGO/JCM result.

Manually compare the regenerated recipe against:

- JCM `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=583`
- MediaDive REST `https://mediadive.dsmz.de/rest/medium/J583`
- TOGO API `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M588`

## Additional Notes

No stock-solution arithmetic defect was found in this direct JCM import; MediaDive represents J583 as one 1000 ml main solution.
