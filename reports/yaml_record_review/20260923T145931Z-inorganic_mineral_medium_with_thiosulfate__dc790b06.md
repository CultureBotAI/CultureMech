# YAML Record Review: INORGANIC MINERAL MEDIUM WITH THIOSULFATE

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/inorganic_mineral_medium_with_thiosulfate__dc790b06.yaml
- Started UTC: 2026-09-23T14:56:05Z
- Finished UTC: 2026-09-23T14:59:35Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| ID | CultureMech:002772 |
| Name | inorganic_mineral_medium_with_thiosulfate |
| Original name | INORGANIC MINERAL MEDIUM WITH THIOSULFATE |
| Class | MediaRecipe |
| Category | bacterial |
| Medium type | DEFINED |
| Composition type | DEFINED |
| Physical state | LIQUID |
| pH | 7.0 |
| Source identity | MediaDive JCM Medium J419 |
| Generated path reviewed | data/merge_yaml/merged/inorganic_mineral_medium_with_thiosulfate__dc790b06.yaml |
| Maintained owner | data/normalized_yaml/bacterial/inorganic_mineral_medium_with_thiosulfate.yaml |

The reviewed file is generated from the maintained MediaDive/JCM owner above.
Future fixes should update that normalized record and MediaDive stock-solution
import logic before regenerating `data/merge_yaml/merged/`.

## Validation

| Check | Result |
|---|---|
| Open LinkML validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/inorganic_mineral_medium_with_thiosulfate__dc790b06.yaml` | Passed; no issues found. |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/inorganic_mineral_medium_with_thiosulfate__dc790b06.yaml --out /private/tmp/inorganic_mineral_medium_with_thiosulfate__dc790b06.strict.tsv --workers 1 --quiet` | Passed; zero ERROR rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/inorganic_mineral_medium_with_thiosulfate__dc790b06.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; zero reference checks were applicable. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/inorganic_mineral_medium_with_thiosulfate__dc790b06.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` entry point validates standalone YAML under `history/`, not embedded MediaRecipe history arrays. |

The focused validators used Python 3.11 and the offline uv cache because the
project-level uv environment currently fails before validation while trying to
build `llvmlite==0.46.0` with Python 3.13.

## Identity and Grounding

- The stable ID, slug, `mediadive.medium:J419` source term, and source URL
  identify the MediaDive import of JCM Medium 419.
- A gitignore-independent exact search for `CultureMech:002772` over bacterial
  normalized records, normalized indexes, and merged records found only this
  MediaDive owner, its generated merged copy, and index entries.
- A gitignore-independent exact search for `mediadive.medium:J419` over the
  same paths found only this MediaDive owner, its generated merged copy, and
  index entries.
- A gitignore-independent exact search for `TOGO:M417` found a separate TOGO
  import of the same JCM medium that has not been merged with this MediaDive
  record.

## Evidence

- JCM 419 and MediaDive J419 list 1 ml trace mineral solution and 1 ml trace
  vitamins in a 1000 ml distilled-water main solution.
- MediaDive resolves the trace mineral and trace-vitamin stocks and includes
  their 1 L stock recipes separately.
- The YAML omits the two 1 ml stock-addition rows and instead records the trace
  mineral salts plus all ten trace-vitamin rows as top-level final ingredients
  at undiluted stock concentrations.
- The 1000 ml distilled-water carrier from the main solution is absent.
- The formula-level pH 7.0 and the JCM instructions for N2-CO2 sparging,
  autoclaving, filter-sterilized trace vitamins and 5% NaHCO3, and final 5%
  O2 in the gas phase are represented in `preparation_steps`.
- NaHCO3 is quantitatively present, but the 5% sterile stock context from the
  preparation instructions is not represented as a stock addition.

## Completeness

- The required main salts, thiosulfate, sodium silicate, low-mass iron, nickel,
  and selenite rows are present.
- The trace-mineral and trace-vitamin stock boundaries are missing, which
  inflates those stock constituents by about three orders of magnitude relative
  to a 1 ml addition into about 1 L final volume.
- The main water carrier is missing.
- Empty optional fields for synonyms, direct publication references, organism
  targets, discussions, variants, and quality flags are acceptable only after
  the stock solution structure and main water row are represented explicitly.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Trace mineral solution was flattened as undiluted final ingredients. | JCM and MediaDive add 1 ml trace mineral solution; the YAML records nitrilotriacetic acid, MnSO4 x n H2O, CoSO4 x 7 H2O, ZnSO4 x 7 H2O, CuSO4 x 5 H2O, AlK(SO4)2, H3BO3, and Na2MoO4 x 2 H2O at stock G_PER_L values. | `data/normalized_yaml/bacterial/inorganic_mineral_medium_with_thiosulfate.yaml`; MediaDive stock import. |
| Major | Trace vitamins were flattened as undiluted final ingredients. | JCM and MediaDive add 1 ml trace vitamins after filter sterilization; the YAML records all ten vitamin stock rows as top-level final ingredients at stock G_PER_L values. | `data/normalized_yaml/bacterial/inorganic_mineral_medium_with_thiosulfate.yaml`; MediaDive stock import. |
| Major | The main distilled-water row is missing. | JCM and MediaDive list 1000 ml distilled water in the main solution, but the YAML has no water ingredient. | `data/normalized_yaml/bacterial/inorganic_mineral_medium_with_thiosulfate.yaml`; MediaDive import. |
| Minor | The 5% NaHCO3 stock-addition context is not structured. | JCM says to filter-sterilize Trace vitamins and 5% NaHCO3 solution and add them to the medium; the YAML represents final NaHCO3 mass but not the stock solution. | `data/normalized_yaml/bacterial/inorganic_mineral_medium_with_thiosulfate.yaml`; MediaDive preparation import. |
| Minor | MediaDive and TOGO imports of the same JCM medium are not deduplicated. | `inorganic_mineral_medium_with_thiosulfate__dc790b06.yaml` comes from `mediadive.medium:J419`, while `INORGANIC_MINERAL_MEDIUM_WITH_THIOSULFATE.yaml` comes from `TOGO:M417` / JCM_M419. | Duplicate detection between the MediaDive and TOGO normalized owners. |

## Recommended Edits

1. Represent Trace mineral solution and Trace vitamins as 1 ml stock additions
   instead of flattened top-level stock ingredients.
2. Restore the 1000 ml distilled-water row from the JCM main solution.
3. Add explicit structure for the filter-sterilized 5% NaHCO3 addition or
   otherwise retain the source stock context alongside the final amount.
4. Keep the pH 7.0, N2-CO2, autoclaving, filter-sterilization, and 5% O2
   preparation text that the MediaDive importer already captured.
5. After both branches are stock-aware, compare MediaDive J419 and TOGO M417
   for source-duplicate merging.
6. Regenerate `data/merge_yaml/merged/` from the corrected MediaDive owner.

## Follow-up Checks

1. Rerun open LinkML, strict, reference, and term validation after correcting
   `data/normalized_yaml/bacterial/inorganic_mineral_medium_with_thiosulfate.yaml`.
2. Recompare the regenerated record to the JCM 419 table and the live MediaDive
   J419 REST payload, checking the 1 ml stock additions and the water row.
3. Recompare the separate TOGO M417 record after TOGO stock-solution cleanup so
   the two JCM Medium 419 imports can be deduplicated intentionally.

## Additional Notes

- This record has no target-organism or literature evidence entries, so no
  organism-grounding, snippet, or DOI checks were applicable.
