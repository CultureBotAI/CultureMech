# YAML Record Review: Hydrogenophilus Hirschii Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/hydrogenophilus_hirschii_medium__62c1e37a.yaml
- Started UTC: 2026-09-23T13:45:51Z
- Finished UTC: 2026-09-23T13:46:29Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| ID | CultureMech:002636 |
| Name | hydrogenophilus_hirschii_medium |
| Original name | HYDROGENOPHILUS HIRSCHII MEDIUM |
| Class | MediaRecipe |
| Category | bacterial |
| Medium type | DEFINED |
| Composition type | DEFINED |
| Physical state | LIQUID |
| pH | 7.0 |
| Source identity | MediaDive/JCM Medium J279, HYDROGENOPHILUS HIRSCHII MEDIUM |
| Generated path reviewed | data/merge_yaml/merged/hydrogenophilus_hirschii_medium__62c1e37a.yaml |
| Maintained owner | data/normalized_yaml/bacterial/hydrogenophilus_hirschii_medium.yaml |

The reviewed file is generated from the maintained MediaDive/JCM import above.
Future fixes should update the normalized record or the shared MediaDive stock
solution import and duplicate-merge handling, then regenerate
`data/merge_yaml/merged/`.

## Validation

| Check | Result |
|---|---|
| Open LinkML validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/hydrogenophilus_hirschii_medium__62c1e37a.yaml` | Passed; no issues found. |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/hydrogenophilus_hirschii_medium__62c1e37a.yaml --out /private/tmp/hydrogenophilus_hirschii_medium__62c1e37a.strict.tsv --workers 1 --quiet` | Passed; zero ERROR rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/hydrogenophilus_hirschii_medium__62c1e37a.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with zero reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/hydrogenophilus_hirschii_medium__62c1e37a.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` entry point validates standalone YAML under `history/`, not embedded MediaRecipe history arrays. |

The focused validators used Python 3.11 and the offline uv cache because the
project-level uv environment currently fails before validation while trying to
build `llvmlite==0.46.0` with Python 3.13.

## Identity and Grounding

- The record identity is coherent: `CultureMech:002636` is the MediaDive import
  of JCM Medium J279, and both the MediaDive REST record and the live JCM 279
  page identify it as HYDROGENOPHILUS HIRSCHII MEDIUM.
- The generated `media_term` points to `mediadive.medium:J279`, matching the
  maintained `notes` field and the inspected MediaDive/JCM source.
- A gitignore-independent exact search for `CultureMech:002636` over
  `data/normalized_yaml`, `data/merge_yaml/merged`, and `reports` found this
  maintained normalized record, generated indexes, generated merged YAML, and
  archival review reports.
- A gitignore-independent exact search for `mediadive.medium:J279` over
  `data/normalized_yaml`, `data/merge_yaml/merged`, and `reports` found only
  this JCM-owned record plus generated outputs and archival reports.
- Final main-solution salts are grounded to exact CHEBI terms where available,
  including MgSO4 x 7H2O, MgCl2 x 6H2O, KCl, NaBr, NaHCO3, NH4Cl, CaCl2 x
  2H2O, ammonium nickel sulfate hexahydrate, sodium tungstate dihydrate,
  sodium selenate, and Na2S2O3 x 5H2O.

## Evidence

- The gram-scale main-solution rows from JCM 279 match MediaDive's
  final-volume-normalized concentrations: 7 g MgSO4 x 7H2O becomes 6.93069
  g/L, 5.5 g MgCl2 x 6H2O becomes 5.44554 g/L, 0.65 g KCl becomes 0.643564
  g/L, 0.1 g NaBr becomes 0.0990099 g/L, 2 g NaHCO3 becomes 1.9802 g/L, 0.15
  g NH4Cl becomes 0.148515 g/L, 0.5 g CaCl2 x 2H2O becomes 0.49505 g/L, 0.02 g
  (NH4)2Ni(SO4)2 x 6H2O becomes 0.019802 g/L, and 1 g Na2S2O3 x 5H2O becomes
  0.990099 g/L.
- The JCM 279 0.1 mg additions of Na2WO4 x 2H2O and Na2SeO4 are correctly
  represented as `9.90099e-05 G_PER_L` after MediaDive's 1010 ml final-volume
  normalization.
- JCM 279 has a 10 ml `Trace minerals` stock addition from Medium 151; the YAML
  instead flattens all MediaDive solution 3804 members into top-level
  ingredients at their undiluted stock g/L values.
- The flattened stock caused chemically identical final and stock rows to be
  summed across solution boundaries: MgSO4 x 7H2O is `9.93069 G_PER_L`
  instead of the supported final-medium `6.93069 G_PER_L` plus a nested
  10 ml trace-stock addition, and CaCl2 x 2H2O is `0.59505 G_PER_L` instead of
  `0.49505 G_PER_L` plus the nested stock row.
- The JCM 279 source has 1 L distilled water in the final medium, and the
  MediaDive 3804 trace stock has 1 L distilled water; neither water volume is
  represented in the generated YAML.
- The JCM bottle, autoclave, overnight stand, filter-sterilized air, and
  H2-CO2 gas-pressurization instructions are preserved on the final medium.
  The NTA/KOH pH adjustment belongs to the Trace minerals stock but appears as
  a second top-level final-medium preparation step.

## Completeness

- The source's Trace minerals addition needs to be preserved as a 10 ml stock
  addition that points at populated JCM 151 / MediaDive solution 3804 content
  instead of expanding the stock directly into the final medium.
- Distilled water volumes are consequential missing rows for both the final
  medium and the Trace minerals stock.
- pH 7.0 and the JCM final-medium preparation note are present.
- Empty optional fields for target organisms, synonyms, variants, direct
  publication references, discussions, and quality flags are acceptable for
  this provider import.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The 10 ml Trace minerals stock is flattened into final-medium ingredients at undiluted stock strength. | JCM 279 lists a 10 ml Trace minerals row that cross-references Medium 151; the YAML has NTA, MnSO4 x nH2O, NaCl, FeSO4 x 7H2O, CoSO4 x 7H2O, ZnSO4 x 7H2O, CuSO4 x 5H2O, AlK(SO4)2, H3BO3, and Na2MoO4 x 2H2O as top-level final ingredients at MediaDive solution 3804 stock concentrations. | `data/normalized_yaml/bacterial/hydrogenophilus_hirschii_medium.yaml`; MediaDive stock-solution import and merge logic. |
| Major | Duplicate merging summed ingredients across final and stock-solution boundaries. | The generated MgSO4 x 7H2O row is `9.93069 G_PER_L`, the sum of the supported 6.93069 final-medium g/L and 3.0 Trace minerals stock g/L; the CaCl2 x 2H2O row similarly sums 0.49505 final-medium g/L with 0.1 stock g/L. | `data/normalized_yaml/bacterial/hydrogenophilus_hirschii_medium.yaml`; duplicate-ingredient cleanup should not merge nested solution members into final-medium rows. |
| Major | Source water volumes are omitted. | JCM 279 and MediaDive J279 include 1000 ml distilled water for the final medium, and MediaDive solution 3804 includes 1000 ml distilled water for the Trace minerals stock; no water rows appear in the YAML. | `data/normalized_yaml/bacterial/hydrogenophilus_hirschii_medium.yaml`; MediaDive volume import. |
| Major | Trace-stock preparation is scoped as a final-medium pH adjustment. | The NTA/KOH pH step belongs to MediaDive solution 3804, but the generated final medium has it as top-level preparation step 2. | `data/normalized_yaml/bacterial/hydrogenophilus_hirschii_medium.yaml`; preparation import should keep stock-solution steps under the stock solution. |

## Recommended Edits

1. Restore `Trace minerals (see Medium No. 151)` as a 10 ml addition of a
   populated stock recipe imported from MediaDive solution 3804.
2. Move the NTA, MgSO4 x 7H2O, MnSO4 x nH2O, NaCl, FeSO4 x 7H2O, CoSO4 x 7H2O,
   CaCl2 x 2H2O, ZnSO4 x 7H2O, CuSO4 x 5H2O, AlK(SO4)2, H3BO3, and Na2MoO4 x
   2H2O rows under that Trace minerals stock instead of the final medium.
3. Repair duplicate handling so main-medium MgSO4 x 7H2O and CaCl2 x 2H2O are
   not summed with Trace minerals stock rows.
4. Represent the final-medium and Trace minerals distilled-water volumes.
5. Keep the NTA/KOH pH adjustment with the Trace minerals stock and keep the
   H2-CO2, air, and autoclave sequence on the final medium.
6. Regenerate `data/merge_yaml/merged/` after the normalized/source-owned fix.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation for the regenerated
  JCM J279 merged record.
- Manually compare every regenerated final-medium row against the live JCM 279
  page and MediaDive REST record.
- Verify that the Trace minerals stock resolves to MediaDive solution 3804 /
  JCM Medium 151 at a 10 ml addition and that its own ingredient list and
  NTA/KOH pH preparation stay inside the nested solution boundary.

## Additional Notes

- The record passed structural validation even though the stock-solution
  boundary is materially wrong; this is a source-arithmetic curation issue, not
  a LinkML shape issue.
