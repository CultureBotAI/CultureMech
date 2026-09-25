# YAML Record Review: Methanopyrus Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanopyrus_medium__5e78003d.yaml
- Started UTC: 2026-09-24T04:24:26Z
- Finished UTC: 2026-09-24T04:25:56Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:008212 |
| Name | methanopyrus_medium |
| Original name | Methanopyrus Medium |
| Category | archaea |
| Media term | TOGO:M1655 |
| Source | TOGO M1655 / NBRC M859 |
| Generated path reviewed | data/merge_yaml/merged/methanopyrus_medium__5e78003d.yaml |
| Canonical owner | data/normalized_yaml/archaea/TOGO_M1655_Methanopyrus_Medium.yaml |

The reviewed file is a generated merge of one TOGO owner. The owner already
contains two local NBRC stocks and the full NBRC preparation in the TOGO
payload, but the imported YAML flattens those stocks, links them to unrelated
generic MediaDive stocks, and omits the preparation.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanopyrus_medium__5e78003d.yaml` exited 0 with no diagnostics. |
| Strict validator | Passed; `scripts/validate_strict.py data/merge_yaml/merged/methanopyrus_medium__5e78003d.yaml --out /private/tmp/methanopyrus_medium__5e78003d.strict.tsv --workers 1 --quiet` reported 0 error rows. |
| Reference validator | Passed; `linkml-reference-validator validate data data/merge_yaml/merged/methanopyrus_medium__5e78003d.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` performed 0 reference checks and passed. |
| Term validator | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/methanopyrus_medium__5e78003d.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/` YAML, not embedded `MediaRecipe.curation_history` entries in merged records. |

## Identity and Grounding

- **The source identity is correct.** TOGO M1655 and the live NBRC medium 859
  page both identify the recipe as `Methanopyrus Medium`.
- **The reviewed merge is stale.** It was generated on 2026-08-06 from
  `TOGO_M1655_Methanopyrus_Medium.yaml`; the owner collapsed three identical
  water rows to one value on 2026-09-02, but the merge still has `3.0 G_PER_L`
  water.
- **The stock links point to unrelated generic MediaDive stocks.** NBRC 859
  defines local `Trace elements solution*` and `Vitamin solution**` stocks; the
  YAML links their 10 ml additions to MediaDive 6129 and 6241, which have
  different compositions.
- **Several salt groundings are broad or legacy.** KNO3 still has a legacy
  `mediaingredientmech_term`; CoCl2 x 6H2O, NiCl2 x 6H2O, Ca-pantothenate, and
  Na2HPO4 x 12H2O are not grounded to exact hydrate or salt forms.

## Evidence

### Supported by inspected sources

- TOGO M1655 and NBRC 859 support the main-solution salts: 1 L water, 11.8 g
  NaCl, 1.75 g MgSO4 x 7H2O, 4.5 g MgCl2 x 6H2O, 0.78 g CaCl2 x 2H2O,
  0.81 g Na2SO4, 0.3 g KCl, 0.25 g NH4Cl, 0.09 g KH2PO4, 0.05 g K2HPO4,
  1 g NaHCO3, 0.04 g NaBr, 0.018 g SrCl2 x 6H2O, and 0.013 g H3BO3.
- The same sources support 0.2 g Bacto Yeast Extract, 0.14 g Coenzyme M, 0.5 g
  Na2S x 9H2O, 1 mg resazurin, and seven milligram-scale salts: Fe(NH4)2(SO4)2
  x 6H2O, (NH4)2Ni(SO4)2 x 6H2O, KI, Sodium silicate, NaF, KNO3, and
  Na2HPO4 x 12H2O.
- NBRC 859 defines the local trace stock as NTA, FeCl3 x 6H2O, MnCl2 x 4H2O,
  CoCl2 x 6H2O, CaCl2 x 2H2O, ZnCl2, CuCl2 x 2H2O, H3BO3, Na2MoO4 x 2H2O,
  NaCl, NiCl2 x 6H2O, Na2SeO4, Na2WO4, KAl(SO4)2 x 12H2O, NaOH, and distilled
  water.
- NBRC 859 defines the local vitamin stock as biotin, folic acid,
  Pyridoxine-HCl, Thiamine-HCl, riboflavin, nicotinic acid, Ca-pantothenate,
  p-Aminobenzoic acid, Vitamin B12, and distilled water.
- TOGO M1655 preserves the anaerobic NBRC procedure: mix except Na2S, adjust
  to pH 6.0 with H2SO4, filter sterilize while gassing H2/CO2 80/20,
  separately autoclave 5 percent Na2S x 9H2O under N2, aseptically add the
  sulfide stock before inoculation, pressurize inoculated vessels to 150 kPa
  with H2/CO2 80/20, and prepare the trace stock by dissolving NTA before
  adding minerals.

### Unsupported or over-scoped in the YAML

- The generated water row still sums three 1 L stock waters to `3.0 G_PER_L`;
  the maintained owner has already repaired that identical duplicate sum.
- The main 11.8 g NaCl, 0.78 g CaCl2 x 2H2O, and 0.013 g H3BO3 rows are summed
  with local trace-stock rows.
- Seven milligram-scale salts are stored as `G_PER_L`.
- Local trace and vitamin stock ingredients are flattened into the final medium
  and also represented as empty `Unknown solution` rows with 10 ml volumes as
  `10 G_PER_L`.
- The local stock rows are linked to unrelated MediaDive solutions 6129 and
  6241.
- Preparation steps are absent.

## Completeness

- **Generated output is stale.** The 2026-09-02 owner repair is not reflected
  in the reviewed 2026-08-06 generated merge.
- **Two local stocks are missing.** Trace elements and Vitamin solution need
  scoped local compositions and 10 ml addition volumes.
- **Preparation is missing.** The record lacks filter sterilization under
  H2/CO2, pH 6.0 adjustment with H2SO4, separate sulfide autoclaving, anaerobic
  sulfide addition, 150 kPa overpressure, and trace-stock pH 6.5/7.0 handling.
- **Bounded local search.** A gitignore-independent search for
  `TOGO_M1655_Methanopyrus_Medium`, `NBRC_M859`, and `Methanopyrus Medium`
  under `data/normalized_yaml` and `data/merge_yaml/merged` found this TOGO
  M1655 owner, its generated record, the separate TOGO M2663 same-label record,
  and the separate TOGO M692 strain 116 medium.
- Empty target-organism and growth-evidence sections are not defects for this
  provider recipe.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated file predates an upstream duplicate-sum repair. | `data/normalized_yaml/archaea/TOGO_M1655_Methanopyrus_Medium.yaml` collapsed three identical water rows on 2026-09-02; this merge still has water `3.0 G_PER_L`. | Merge artifacts regenerated from `data/normalized_yaml/archaea/TOGO_M1655_Methanopyrus_Medium.yaml` |
| Major | Local NBRC stocks are linked to wrong generic MediaDive stocks. | The NBRC 859 trace and vitamin stock recipes do not match MediaDive 6129 or 6241. | `data/normalized_yaml/archaea/TOGO_M1655_Methanopyrus_Medium.yaml` |
| Major | Trace and vitamin stocks were flattened into the main medium. | NaCl, CaCl2 x 2H2O, H3BO3, trace salts, vitamin rows, and water from the two stocks appear as top-level ingredients. | `data/normalized_yaml/archaea/TOGO_M1655_Methanopyrus_Medium.yaml` and solution migration |
| Major | Seven milligram rows were imported as g/L values. | The source lists KNO3 0.4 mg, Fe/Ni salts 2 mg, KI 0.0125 mg, Sodium silicate 1 mg, NaF 0.6 mg, and Na2HPO4 x 12H2O 4.6 mg; the YAML stores each as `G_PER_L`. | `data/normalized_yaml/archaea/TOGO_M1655_Methanopyrus_Medium.yaml` and import unit handling |
| Major | NBRC preparation instructions are absent. | TOGO M1655 has filter sterilization under H2/CO2, separate sulfide stock handling, overpressure, and trace-stock pH instructions; the YAML has no `preparation_steps`. | `data/normalized_yaml/archaea/TOGO_M1655_Methanopyrus_Medium.yaml` |
| Minor | Several term links are stale or broad. | KNO3 still has `mediaingredientmech_term`; CoCl2 x 6H2O, NiCl2 x 6H2O, Ca-pantothenate, and Na2HPO4 x 12H2O need exact salt or hydrate groundings. | Shared ingredient grounding maps |

## Recommended Edits

1. Regenerate the merged record after the 2026-09-02 water duplicate repair.
2. Remove the false `mediadive.solution:6129` and `mediadive.solution:6241`
   links from the local NBRC stocks.
3. Represent NBRC's Trace elements solution and Vitamin solution as local
   subsolutions, not flattened top-level ingredients.
4. Restore milligram units for KNO3, the Fe/Ni salts, KI, Sodium silicate, NaF,
   Na2HPO4 x 12H2O, and resazurin.
5. Keep the trace-stock NaCl, CaCl2 x 2H2O, H3BO3, and water scoped to Trace
   elements solution.
6. Add the NBRC preparation instructions for filter sterilization, H2SO4 pH
   adjustment, sulfide stock addition, overpressure, and trace-stock assembly.
7. Replace the legacy or broad groundings with exact CHEBI keying where exact
   hydrate or salt terms are available.

## Follow-up Checks

- Re-run schema, strict, term, and reference validation on
  `data/normalized_yaml/archaea/TOGO_M1655_Methanopyrus_Medium.yaml` and the
  regenerated merged record.
- Manually compare the regenerated YAML with TOGO M1655 and NBRC 859 to ensure
  the main, trace, and vitamin recipes are separate.
- Confirm no empty `Unknown solution` placeholders remain and no
  `mediaingredientmech_term` entries remain.

## Additional Notes

- TOGO M2663 is a same-label `Methanopyrus Medium` from a different source and
  should be reviewed independently in
  `data/merge_yaml/merged/methanopyrus_medium__c796d637.yaml`.
