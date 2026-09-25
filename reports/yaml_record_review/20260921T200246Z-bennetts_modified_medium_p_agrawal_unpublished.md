# YAML Record Review: BENNETT'S MODIFIED medium (P. AGRAWAL, UNPUBLISHED)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/bennetts_modified_medium_p_agrawal_unpublished.yaml
- Started UTC: 2026-09-21T20:00:00Z
- Finished UTC: 2026-09-21T20:02:46Z
- Verdict: needs curation

## Target

- Reviewed `data/merge_yaml/merged/bennetts_modified_medium_p_agrawal_unpublished.yaml`.
- Class: `MediaRecipe`.
- ID: `CultureMech:006747`.
- Name: `bennetts_modified_medium_p_agrawal_unpublished`.
- Original name: `BENNETT'S MODIFIED medium (P. AGRAWAL, UNPUBLISHED)`.
- Source identity: canonical KOMODO import `komodo.medium:894`, label `BENNETT'S MODIFIED medium (P. AGRAWAL, UNPUBLISHED)`, with DSMZ Medium 894 provenance in `notes`.
- Generated status: derived merge output under `data/merge_yaml/merged/`.
- Maintained owners merged into this record: `data/normalized_yaml/bacterial/KOMODO_894_BENNETT_S_MODIFIED_medium_P._AGRAWAL_UNPUBLISHED.yaml` and `data/normalized_yaml/bacterial/bennetts_modified_medium_p_agrawal_unpublished.yaml`.
- Merge metadata: two source recipes, `KOMODO_894_BENNETT_S_MODIFIED_medium_P._AGRAWAL_UNPUBLISHED` and `bennetts_modified_medium_p_agrawal_unpublished`, on fingerprint `4003857f95822464d5a87dea1e7bdb1aa3bb70552cc868acb7a046016e4bfed6`.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/bennetts_modified_medium_p_agrawal_unpublished.yaml` via the no-project Python 3.11 workaround | Passed |
| Closed-schema strict validation, `scripts/validate_strict.py data/merge_yaml/merged/bennetts_modified_medium_p_agrawal_unpublished.yaml --out /private/tmp/bennetts_modified_medium_p_agrawal_unpublished.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows |
| `linkml-reference-validator validate data data/merge_yaml/merged/bennetts_modified_medium_p_agrawal_unpublished.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were applicable |
| `linkml-term-validator validate-data data/merge_yaml/merged/bennetts_modified_medium_p_agrawal_unpublished.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded `MediaRecipe.curation_history` validation | Not checked: the repository exposes `just validate-history` for standalone files under `history/`, not a focused embedded-history validator for one merged record |

The documented `just` commands were not run directly because the project runtime currently tries to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'` before target-specific validation.

## Identity and Grounding

- `CultureMech:006747` resolves in `data/culturemech_id_registry.tsv` to `data/normalized_yaml/bacterial/KOMODO_894_BENNETT_S_MODIFIED_medium_P._AGRAWAL_UNPUBLISHED.yaml`.
- KOMODO Medium 894, DSMZ Medium 894, the imported title, and the two source records all denote DSMZ Bennett's Modified Medium (P. Agrawal, unpublished).
- The KOMODO and DSMZ owners agree closely enough to merge as source duplicates; they carry the same main composition and qualitative trace entries.
- Glucose, starch, calcium carbonate, CoCl2, and agar are plausibly grounded. The DSMZ source says `Ferric ammonium` at trace quantity, not ferric ammonium citrate, so `CHEBI:31604` over-resolves a source label that should remain exact or unresolved.

## Evidence

- DSMZ Medium 894 supports 10 g/L Lab Lemco, 2 g/L yeast extract, 10 g/L glucose, 100 mg/L starch, 2 g/L tryptose, 100 mg/L CaCO3, trace CoCl2, trace ferric ammonium, 15 g/L agar, 1000 ml distilled water, pH 7.0, and sterilization at 121 deg C for 15 minutes.
- The generated merge preserves the six quantified non-water ingredients and correctly keeps the two trace rows as `VARIABLE`.
- The generated merge has no `preparation_steps` because it is based on the KOMODO owner, even though the DSMZ owner has the pH 7.0 and 121 deg C for 15 minutes instruction.
- The generated merge and both maintained owners ground DSMZ's `Ferric ammonium` trace row to ferric ammonium citrate. The inspected DSMZ PDF render shows only `Ferric ammonium`, with no citrate qualifier.
- A gitignore-independent exact search over both maintained owners, the generated merge, ID registries, recipe catalogs, and KOMODO/MediaDive indexes found the expected `CultureMech:006747` KOMODO owner, `CultureMech:002057` DSMZ owner, and generated merge references. It did not find a raw KOMODO or DSMZ source payload committed for this source record.

## Completeness

- The quantitative main composition is complete and source-supported.
- Qualitative trace quantities for CoCl2 and ferric ammonium are acceptable here because DSMZ states only `traces`.
- Consequentially incomplete: pH adjustment and sterilization are absent from the generated merge.
- Consequentially incorrect: ferric ammonium is grounded to ferric ammonium citrate without source support.
- Empty target-organism and growth-evidence slots are acceptable here; DSMZ Medium 894 does not name a strain-specific growth result.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | The generated merge drops the DSMZ pH/sterilization instruction because the KOMODO duplicate selected as canonical lacks `preparation_steps`. | `data/normalized_yaml/bacterial/KOMODO_894_BENNETT_S_MODIFIED_medium_P._AGRAWAL_UNPUBLISHED.yaml`; merge preservation logic |
| Major | `Ferric ammonium` is over-resolved to ferric ammonium citrate even though DSMZ Medium 894 does not specify citrate. | `data/normalized_yaml/bacterial/KOMODO_894_BENNETT_S_MODIFIED_medium_P._AGRAWAL_UNPUBLISHED.yaml` and `data/normalized_yaml/bacterial/bennetts_modified_medium_p_agrawal_unpublished.yaml` |

## Recommended Edits

1. Preserve the DSMZ preparation step in the KOMODO duplicate or adjust merge preservation so the canonical generated record keeps the pH 7.0 and 121 deg C for 15 minutes instruction from the DSMZ owner.
2. Replace `Ferric ammonium citrate` with source-faithful unresolved `Ferric ammonium`, unless a primary DSMZ or KOMODO source can show that citrate was intended.
3. Regenerate `data/merge_yaml/merged/bennetts_modified_medium_p_agrawal_unpublished.yaml` after the normalized owners are corrected.

## Follow-up Checks

- Rerun the open schema validator, `scripts/validate_strict.py`, `linkml-term-validator`, and `linkml-reference-validator` on both changed normalized owners and the regenerated merged record.
- Manually compare the regenerated merge against the DSMZ Medium 894 PDF to verify Lab Lemco, yeast extract, glucose, starch, tryptose, CaCO3, trace CoCl2, trace ferric ammonium, agar, pH 7.0, and 121 deg C sterilization survive with source-faithful wording and units.
- Run `just verify-merges` after regeneration to confirm the KOMODO and DSMZ records still merge and no longer drop the DSMZ preparation instruction.

## Additional Notes

- The DSMZ Medium 894 PDF text extraction lost the degree symbol in the sterilization sentence and matched the rendered PDF for the `Ferric ammonium` label; the PDF was rendered with Quick Look for the row-level label check.
- Reports are read-only review artifacts; no normalized recipe, generated merge, page, history entry, or GitHub issue was edited for this review.
