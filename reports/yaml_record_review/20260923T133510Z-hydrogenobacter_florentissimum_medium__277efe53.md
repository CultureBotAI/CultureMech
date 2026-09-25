# YAML Record Review: HYDROGENOBACTER FLORENTISSIMUM MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/hydrogenobacter_florentissimum_medium__277efe53.yaml
- Started UTC: 2026-09-23T13:32:25Z
- Finished UTC: 2026-09-23T13:35:06Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| ID | CultureMech:002421 |
| Name | hydrogenobacter_florentissimum_medium |
| Original name | HYDROGENOBACTER FLORENTISSIMUM MEDIUM |
| Class | MediaRecipe |
| Category | bacterial |
| Medium type | COMPLEX |
| Composition type | UNDEFINED |
| Physical state | LIQUID |
| pH | 6.7 |
| Source identity | MediaDive/JCM Medium J1255 |
| Generated path reviewed | data/merge_yaml/merged/hydrogenobacter_florentissimum_medium__277efe53.yaml |
| Maintained owner | data/normalized_yaml/bacterial/hydrogenobacter_florentissimum_medium.yaml |

The reviewed file is generated from the maintained MediaDive import at
`data/normalized_yaml/bacterial/hydrogenobacter_florentissimum_medium.yaml`.
Future fixes should update that normalized input and the MediaDive importer that
flattened J1255 stock additions before regenerating `data/merge_yaml/merged/`.

## Validation

| Check | Result |
|---|---|
| Open LinkML validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/hydrogenobacter_florentissimum_medium__277efe53.yaml` | Passed; no issues found. |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/hydrogenobacter_florentissimum_medium__277efe53.yaml --out /private/tmp/hydrogenobacter_florentissimum_medium__277efe53.strict.tsv --workers 1 --quiet` | Passed; the TSV contained only the header and zero ERROR rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/hydrogenobacter_florentissimum_medium__277efe53.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with zero reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/hydrogenobacter_florentissimum_medium__277efe53.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` entry point validates standalone YAML under `history/`, not embedded MediaRecipe history arrays. |

The focused validators used Python 3.11 and the offline uv cache because the
project-level uv environment currently fails before validation while trying to
build `llvmlite==0.46.0` with Python 3.13.

## Identity and Grounding

- The record identity is correct: `CultureMech:002421` denotes JCM Medium
  J1255, `HYDROGENOBACTER FLORENTISSIMUM MEDIUM`.
- The inspected MediaDive REST payload and JCM 1255 page agree that the base
  solution contains NaCl, KCl, Na2SO4, MgSO4 x 7H2O, CaCl2 x 2H2O, NH4Cl,
  NaH2PO4, 5 ml mineral solution, and 1 L distilled water; after autoclaving it
  receives 10 ml 10% yeast extract solution and 5 ml 0.2 M sodium thiosulfate
  solution per liter.
- JCM 1255 points to JCM Medium 976 for mineral solution. The inspected JCM 976
  page confirms that stock's EDTA, FeSO4 x 7H2O, MnCl2 x 4H2O, ZnSO4 x 7H2O,
  CoCl2 x 6H2O, CuCl2 x 2H2O, Na2MoO4 x 2H2O, H3BO3, and 1 L distilled-water
  rows.
- A gitignore-independent exact search for `CultureMech:002421` across
  `data/normalized_yaml`, `data/merge_yaml/merged`, and `reports` found only
  this MediaDive-owned normalized record, generated indexes, generated merged
  YAML, and archival reports for this stable ID.
- Grounding is exact enough for the visible inorganic salts and EDTA rows.
  Yeast extract intentionally remains ungrounded to CHEBI because it is an
  undefined component.

## Evidence

- The base-salt rows and pH are supported by the live MediaDive/JCM sources.
  The MediaDive `g_l` values divide the base masses by the 1020 ml final
  volume after the three 5/10/5 ml post-autoclave additions.
- Mineral-solution members are not supported as top-level final ingredients.
  The source adds 5 ml mineral stock per liter, but the YAML emits EDTA,
  FeSO4 x 7H2O, MnCl2 x 4H2O, ZnSO4 x 7H2O, CoCl2 x 6H2O, CuCl2 x 2H2O,
  Na2MoO4 x 2H2O, and H3BO3 at the undiluted 1 L stock concentrations.
- The 10 ml 10% yeast extract solution and 5 ml 0.2 M sodium thiosulfate
  solution additions are misrepresented as `10 G_PER_L` yeast extract and
  `5 G_PER_L` sodium thiosulfate direct ingredients.
- The 1000 ml distilled-water row from the base recipe and the 1000 ml
  distilled-water row from the mineral stock are both missing.
- The preparation text is mostly retained, including the N2 dispensing, gas
  phase percentages, and stopper pretreatment note. The HTML greater-than-or-
  equal entity was damaged to `&;`, and the mineral-stock pH 6.0 KOH step was
  promoted into the final medium rather than scoped to the nested mineral
  solution.

## Completeness

- The `solutions` array is absent despite three source solution additions:
  Mineral solution, 10% yeast extract solution, and 0.2 M sodium thiosulfate
  solution.
- The mineral stock composition from JCM 976 / MediaDive solution 5001 is
  missing as nested stock structure.
- The source water rows are absent.
- Empty optional fields such as target organisms, synonyms, and publication
  references are not defects for this imported provider recipe.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Three source solution additions were flattened or converted into direct ingredients. | JCM J1255 adds 5 ml mineral solution, 10 ml 10% yeast extract solution, and 5 ml 0.2 M sodium thiosulfate solution after autoclaving; the YAML has no `solutions` and records yeast extract and thiosulfate as direct `G_PER_L` rows. | `data/normalized_yaml/bacterial/hydrogenobacter_florentissimum_medium.yaml`; repair MediaDive solution import and generation. |
| Major | Mineral-stock members are present at stock strength in the final ingredient list. | MediaDive solution 5001 / JCM 976 is a 1 L stock used at 5 ml/L, but the YAML lists EDTA, Fe, Mn, Zn, Co, Cu, molybdate, and borate rows directly at stock g/L values. | `data/normalized_yaml/bacterial/hydrogenobacter_florentissimum_medium.yaml`; preserve solution scope for `mediadive.solution:5001`. |
| Major | Base and mineral water rows are omitted. | The JCM 1255 base recipe and JCM 976 mineral stock each contain 1 L distilled water; neither appears in the reviewed YAML. | `data/normalized_yaml/bacterial/hydrogenobacter_florentissimum_medium.yaml`. |
| Minor | Preparation text contains a damaged comparison symbol and one stock-specific pH step is mis-scoped. | The source says to leave at least 80% gas phase, while the YAML says `leaving &; 80%`; the pH 6.0 KOH step belongs to the mineral stock, not the final medium. | `data/normalized_yaml/bacterial/hydrogenobacter_florentissimum_medium.yaml`. |
| Minor | JCM J1255 is duplicated in a TOGO import with the same normalized name. | Ignored-inclusive search found `TOGO_M1351_Hydrogenobacter_Florentissimum_Medium.yaml`, a separate TOGO/JCM 1255 import with related empty solution references. | Cross-provider JCM/TOGO and MediaDive deduplication. |

## Recommended Edits

1. Restore a structured `solutions` representation with 5 ml/L Mineral
   solution, 10 ml/L 10% yeast extract solution, and 5 ml/L 0.2 M sodium
   thiosulfate solution.
2. Move EDTA, FeSO4 x 7H2O, MnCl2 x 4H2O, ZnSO4 x 7H2O, CoCl2 x 6H2O,
   CuCl2 x 2H2O, Na2MoO4 x 2H2O, and H3BO3 into the nested mineral stock and
   keep the mineral-stock pH 6.0 KOH instruction scoped to that stock.
3. Represent the 10% yeast extract and 0.2 M sodium thiosulfate additions as
   solution additions or as correctly diluted final amounts with retained stock
   metadata, not as `10` and `5 G_PER_L` direct rows.
4. Restore the 1 L distilled-water rows for the base medium and mineral stock.
5. Fix the escaped gas-phase text so the preparation step says the culture
   vessel leaves at least 80% gas phase.
6. Reconcile the MediaDive J1255 and TOGO M1351 records after both source
   imports preserve the same solution boundaries.
7. Regenerate `data/merge_yaml/merged/` from the corrected normalized records.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation for the regenerated
  MediaDive/JCM J1255 merged record.
- Manually compare JCM 1255 and JCM 976 against the regenerated base medium and
  mineral-stock YAML.
- Verify no mineral-stock member appears as a direct final-medium ingredient
  except through the 5 ml/L Mineral solution addition.
- Confirm yeast extract and sodium thiosulfate are represented as
  post-autoclave solution additions with their 10 ml/L and 5 ml/L volumes.
- Search ignored files for `hydrogenobacter_florentissimum_medium` and
  `mediadive.medium:J1255` to confirm the MediaDive and TOGO J1255 copies are
  reconciled or intentionally distinguished.

## Additional Notes

- TOGO M1351 references TOGO M1029 for the same mineral stock because M1029
  mirrors JCM Medium 976.
- The reviewed MediaDive record carries better gas-phase preparation text than
  the sibling TOGO M1351 import, but it loses more solution structure by
  flattening every JCM 976 mineral-stock member into the final medium.
