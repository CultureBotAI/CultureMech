# YAML Record Review: medium_for_erythrobacter_longus__eeab2411

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/medium_for_erythrobacter_longus__eeab2411.yaml
- Started UTC: 2026-09-24T01:37:29Z
- Finished UTC: 2026-09-24T01:38:01Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:008939 |
| Name | medium_for_erythrobacter_longus |
| Generated record | data/merge_yaml/merged/medium_for_erythrobacter_longus__eeab2411.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M2354_Medium_For_Erythrobacter_Longus.yaml |
| Source identity | TOGO:M2354 importing DSMZ Medium 695 |

This generated record is a stale single-source merge for TOGO M2354, "Medium
For Erythrobacter Longus." The TOGO source imports the same DSMZ Medium 695
formula that is also present as a direct MediaDive owner and a KOMODO owner.

## Validation

| Check | Result |
|---|---|
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/medium_for_erythrobacter_longus__eeab2411.yaml` | Passed with no issues found. |
| Strict validation, `scripts/validate_strict.py data/merge_yaml/merged/medium_for_erythrobacter_longus__eeab2411.yaml --workers 1` | Passed; the TSV contained only its header and 0 error rows. |
| Reference validation, `linkml-reference-validator validate data ... --target-class MediaRecipe` | Passed with 0 reference checks. |
| Term validation, `linkml-term-validator validate-data ... -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented history validator targets standalone history files, not embedded generated-record events. |

The focused validators were run with Python 3.11 through `uv --no-project
--offline` to avoid the project-level Python 3.13 `llvmlite` build failure.

## Identity and Grounding

TOGO M2354, the TOGO owner, MediaDive medium 695, and
`data/normalized_yaml/bacterial/medium_for_erythrobacter_longus.yaml` all
identify DSMZ Medium 695, "Medium For Erythrobacter Longus." The reviewed file
has the correct CultureMech ID, TOGO ID, bacterial category, complex/undefined
classification, and liquid physical state for that source.

The generated record is out of date relative to its maintained owner. The owner
was repaired on 2026-09-11 to add pH 7.5, switch artificial seawater and
distilled water from G_PER_L to ML_PER_L, preserve the 2 ml/L 5 percent
Fe(III) citrate stock as a `solutions` row, add curated FOODON/MICRO/CHEBI
groundings, add source references, and link the direct DSMZ Medium 695 record as
a `SOURCE_DUPLICATE` parent. None of those repairs appear in the generated YAML.

A gitignore-independent exact scan for `TOGO:M2354`, `mediadive.medium:695`,
`DSMZ_Medium695.pdf`, `KOMODO_695_medium_FOR_ERYTHROBACTER_LONGUS`, and
`TOGO_M2354_Medium_For_Erythrobacter_Longus` found the expected TOGO owner, the
direct MediaDive owner, the KOMODO owner, their two generated artifacts, and
normalized indexes. The current generated outputs still split TOGO M2354 into
`medium_for_erythrobacter_longus__eeab2411.yaml` instead of merging it into
`MEDIUM_FOR_ERYTHROBACTER_LONGUS.yaml` with MediaDive and KOMODO.

## Evidence

TOGO M2354 and MediaDive 695 agree that DSMZ Medium 695 contains, per liter,
Peptone 2 g, Soytone 1 g, Yeast extract 1 g, Proteose peptone no. 3 1 g,
2 ml of 5 percent Fe(III) citrate, 700 ml artificial seawater, and 300 ml
distilled water, with pH 7.5.

The reviewed generated record preserves the four dry organic nutrients, but it
does not preserve several source quantities and conditions:

- Artificial seawater is 700 G_PER_L instead of 700 ML_PER_L.
- Distilled water is 300 G_PER_L instead of 300 ML_PER_L.
- `5% Fe(III) citrate` is modeled as a 2 G_PER_L ingredient instead of as a
  2 ML_PER_L stock addition with 50 G_PER_L Fe(III) citrate composition.
- `ph_value: 7.5` is absent.

The repaired TOGO owner already matches the inspected sources on those points.

## Completeness

The generated record has no target-organism assertions. That is acceptable here:
the inspected TOGO and MediaDive source records define the medium formula and do
not claim a particular isolate grows on it.

The generated artifact is materially incomplete because it predates the source
reference rows, source-duplicate relationship, pH, stock solution, and volume
unit repairs that are already maintained upstream.

## Findings

| Severity | Finding | Evidence | Maintained owner for future fix |
|---|---|---|---|
| major | The generated TOGO merge is stale and still carries pre-repair source-unit errors. | TOGO and MediaDive list 2 ml 5 percent Fe(III) citrate, 700 ml artificial seawater, 300 ml distilled water, and pH 7.5. The generated record has 2, 700, and 300 G_PER_L rows and no pH, while the normalized TOGO owner repaired those on 2026-09-11. | Regenerate `data/merge_yaml/merged/medium_for_erythrobacter_longus__eeab2411.yaml` from `data/normalized_yaml/bacterial/TOGO_M2354_Medium_For_Erythrobacter_Longus.yaml`. |
| major | TOGO M2354 has not been folded into the existing DSMZ Medium 695 duplicate merge. | The normalized TOGO owner now points to `data/normalized_yaml/bacterial/medium_for_erythrobacter_longus.yaml` as a `SOURCE_DUPLICATE`, and the direct MediaDive owner points back to the TOGO owner. The generated layer still has the TOGO-only `medium_for_erythrobacter_longus__eeab2411.yaml` beside `MEDIUM_FOR_ERYTHROBACTER_LONGUS.yaml`, which only merges the KOMODO and direct MediaDive owners. | Merge regeneration and source-duplicate reconciliation for DSMZ Medium 695. |

## Recommended Edits

1. Regenerate the TOGO M2354 merge so the generated record reflects pH 7.5,
   700/300 ML_PER_L volume rows, the 2 ML_PER_L ferric-citrate stock, curated
   groundings, references, and the Sept. 11 source-duplicate link.
2. Re-run the merge process after regeneration so the TOGO, MediaDive, and
   KOMODO DSMZ Medium 695 owners collapse into one generated record instead of
   leaving a TOGO-only `__eeab2411` artifact.

## Follow-up Checks

- Run the focused open schema, strict, reference, and term validators on the
  repaired normalized owner and regenerated DSMZ Medium 695 merge.
- Run `just verify-merges` to confirm TOGO M2354 no longer produces a stale
  standalone generated artifact.
- Repeat a gitignore-independent exact scan for `TOGO:M2354`,
  `mediadive.medium:695`, and `DSMZ_Medium695.pdf` to confirm the source family
  appears on the reconciled owner set and expected indexes only.
- Manually compare the regenerated formula against TOGO M2354 and MediaDive 695
  to confirm 5 percent Fe(III) citrate, artificial seawater, distilled water,
  and pH 7.5 survived the merge.

## Additional Notes

- `data/normalized_yaml/bacterial/alterythrobacter_medium_216l.yaml` was an
  exact filename lookup hit because its filename contains `erythrobacter`; it is
  DSMZ Medium 1453 for a different medium and was not evidence for this review.
- Exact source-family searches used `rg --no-ignore --hidden`, so ignored files
  were included.
