# YAML Record Review: desulfohimalaya_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/desulfohimalaya_medium__75893ec1.yaml
- Started UTC: 2026-09-22T19:08:10Z
- Finished UTC: 2026-09-22T19:12:06Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Reviewed file | `data/merge_yaml/merged/desulfohimalaya_medium__75893ec1.yaml` |
| Generated or maintained | Generated merge output |
| Maintained owner | `data/normalized_yaml/bacterial/desulfohimalaya_medium.yaml` |
| Related normalized records | `data/normalized_yaml/bacterial/mediadive_4425_Main_sol_J587.yaml`, `data/normalized_yaml/bacterial/TOGO_M592_Desulfohimalaya_Medium.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:002934` |
| Label | `desulfohimalaya_medium` |
| Original label | `DESULFOHIMALAYA MEDIUM` |
| Source identity | JCM / MediaDive medium J587 |
| Merge lineage | `merge_recipes.py` merged one source record, `desulfohimalaya_medium.yaml`, into fingerprint `75893ec19ad268f4044ec9b516e462551ff5ebbd7a9a4bd64edd619b869d203b` |

I read the full generated record. A gitignore-independent search for the label, source IDs, and original JCM URL found one additional generated Desulfohimalaya record, `data/merge_yaml/merged/DESULFOHIMALAYA_MEDIUM.yaml`, imported from TOGO M592 but pointing back to the same original JCM M587 recipe.

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/desulfohimalaya_medium__75893ec1.yaml` | Passed; no issues found |
| Strict schema, `scripts/validate_strict.py data/merge_yaml/merged/desulfohimalaya_medium__75893ec1.yaml --out /private/tmp/desulfohimalaya_medium__75893ec1.strict.tsv --workers 1 --quiet` | Passed; 0 errors |
| Reference validator, `linkml-reference-validator validate data data/merge_yaml/merged/desulfohimalaya_medium__75893ec1.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks |
| Term validator, `linkml-term-validator validate-data data/merge_yaml/merged/desulfohimalaya_medium__75893ec1.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; only the known `eutils` / `pkg_resources` deprecation warning was emitted |
| Embedded `curation_history` | Not checked: `just validate-history` validates standalone YAML records under `history/`, not embedded `MediaRecipe.curation_history` entries |

The documented `just` wrappers were not used for this focused record check because the local project `uv` environment currently tries to build `llvmlite==0.46.0` under Python 3.13 and fails inside `setuptools`. The equivalent validators above were run offline with Python 3.11 and the cached `linkml`, `pyyaml`, `linkml-reference-validator`, and `linkml-term-validator` packages.

## Identity and Grounding

The generated record denotes the intended MediaDive mirror of JCM medium 587: `mediadive.medium:J587`, the MediaDive REST payload, and the imported `Source: JCM, ID: J587` curation note all identify `DESULFOHIMALAYA MEDIUM`.

This is not a distinct variant of `data/merge_yaml/merged/DESULFOHIMALAYA_MEDIUM.yaml`. The TOGO M592 record has the same normalized name, records `Original source: JCM - JCM_M587`, and preserves the same JCM URL, so the two generated records represent duplicate imports of the same upstream JCM recipe rather than two source formulations.

Most chemical groundings in the generated J587 record are exact or otherwise plausible for the named hydrated salts. `Thioglycollic acid` is ungrounded in this generated file even though the maintained normalized J587 parent now carries `CHEBI:30065`; the generated merge predates that 2026-08-20 grounding event.

## Evidence

The inspected MediaDive REST payload supports the nine non-water component rows and the two preparation notes in this generated record. It also explicitly includes `Distilled water` at 1000 ml in `Main sol. J587`; the generated medium omitted that component.

The TOGO M592 API payload independently carries the same original JCM M587 source URL and the same Desulfohimalaya ingredient list, including distilled water and the two reducing-agent instructions. TOGO reports the final pH as 7.3.

The inspected JCM URL saved in both imports is stale as a live source. `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=587`, its `GRMD=J587` variant, and the HTTP redirect path all returned a JCM page saying nothing was found for medium 587, so MediaDive and TOGO were the available inspected mirrors of the original JCM formulation.

## Completeness

The ingredient list is incomplete because the MediaDive source has a tenth main-solution ingredient, 1000 ml distilled water. The related `data/normalized_yaml/bacterial/mediadive_4425_Main_sol_J587.yaml` solution record preserves that water row, but with the malformed `1000 PERCENT_V_V` concentration and an `incomplete_composition` placeholder ingredient.

The pH representation is internally inconsistent and source-conflicted. The target record stores `ph_value: 7.2`, but its first imported preparation note says to adjust pH to 7.3, the second gives a 7.0-7.5 adjustment range before thioglycollic acid and ascorbic acid are added, and TOGO M592 reports pH 7.3 for the same original JCM M587 recipe.

A gitignore-independent search of the target and sibling generated files found no top-level `solutions:`, `references:`, or `target_organisms:` keys. Empty target organisms and references are not defects here because neither MediaDive nor TOGO supplies strain-level growth evidence; the absent solution linkage is relevant only because the MediaDive import already has a separate Main sol. J587 record that did not remain linked to this parent medium.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated J587 parent omitted the 1000 ml distilled-water row from MediaDive Main sol. J587. | MediaDive J587 solution 4425 lists distilled water after the nine solute rows. `data/merge_yaml/merged/desulfohimalaya_medium__75893ec1.yaml` stops at thioglycollic acid and has no water component. | `data/normalized_yaml/bacterial/desulfohimalaya_medium.yaml`; reusable repair belongs in the MediaDive import/normalization path that projects main-solution water into parent media. |
| Major | The same upstream JCM M587 recipe is represented by two unmerged generated media records. | `desulfohimalaya_medium__75893ec1.yaml` is MediaDive `J587`; `DESULFOHIMALAYA_MEDIUM.yaml` is TOGO `M592` and states `Original source: JCM - JCM_M587`. Both carry the same Desulfohimalaya formulation and original JCM URL. | `data/normalized_yaml/bacterial/desulfohimalaya_medium.yaml`, `data/normalized_yaml/bacterial/TOGO_M592_Desulfohimalaya_Medium.yaml`, and merge source crosswalk logic. |
| Major | Final pH needs curation instead of a bare `7.2` scalar. | MediaDive top-level metadata says 7.2, MediaDive/JCM prep text says 7.3 and 7.0-7.5, and TOGO M592 says 7.3. The generated record preserves two contradictory pH instructions with no discussion or quality flag. | `data/normalized_yaml/bacterial/desulfohimalaya_medium.yaml` and `data/normalized_yaml/bacterial/TOGO_M592_Desulfohimalaya_Medium.yaml`. |
| Minor | The generated merge is stale for thioglycollic acid grounding. | The normalized owner now grounds `Thioglycollic acid` to `CHEBI:30065`; the generated record has no `term` for that ingredient because its merge event predates the 2026-08-20 MIM grounding event. | Regenerate `data/merge_yaml/merged/desulfohimalaya_medium__75893ec1.yaml` from `data/normalized_yaml/bacterial/desulfohimalaya_medium.yaml` after the substantive fixes. |
| Minor | The saved JCM source URL is no longer directly retrievable. | Exact `curl -L` checks of the recorded HTTPS URL, the `GRMD=J587` variant, and the HTTP redirect returned JCM "Nothing found" pages. | Source provenance on the two normalized Desulfohimalaya records. |

## Recommended Edits

1. Add the missing 1000 ml distilled-water row, or a correctly linked 1000 ml Main sol. J587 solution, to `data/normalized_yaml/bacterial/desulfohimalaya_medium.yaml`.
2. Fix or retire `data/normalized_yaml/bacterial/mediadive_4425_Main_sol_J587.yaml`: if it remains a solution record, represent distilled water as 1000 ml, keep the J587 preparation notes on the solution, and remove the placeholder `ingredients` / `incomplete_composition` scaffold.
3. Merge or cross-link `data/normalized_yaml/bacterial/desulfohimalaya_medium.yaml` and `data/normalized_yaml/bacterial/TOGO_M592_Desulfohimalaya_Medium.yaml` as duplicate imports of JCM M587 so the generated corpus no longer exposes two separate Desulfohimalaya media.
4. Curate the final pH conflict by preserving MediaDive's 7.2 metadata, the 7.3 instruction, the 7.0-7.5 adjustment range, and TOGO's 7.3 value in the appropriate scalar/range plus a discussion or quality flag.
5. Regenerate the merged media so the current `CHEBI:30065` grounding for thioglycollic acid propagates into the generated file.

## Follow-up Checks

1. Rerun open schema, strict schema, term, and reference validation on every edited normalized record and the regenerated merged record.
2. Rerun the merge step and confirm there is only one generated Desulfohimalaya canonical record for original JCM M587.
3. Compare the regenerated Desulfohimalaya record against MediaDive REST J587 and TOGO M592, checking the water amount, pH handling, thioglycollic acid row, and preparation notes.
4. Re-fetch the recorded JCM URL to see whether the stale upstream page was transient; if it still returns nothing found, keep MediaDive and TOGO as inspected mirrors and flag the original URL as stale.

## Additional Notes

- `find` and `rg --no-ignore --hidden` were used for absence-sensitive searches, so ignored review reports and generated files were included where relevant.
- No report for `desulfohimalaya_medium__75893ec1` existed under `reports/yaml_record_review/` before this one; that ignored directory was checked with `find`.
