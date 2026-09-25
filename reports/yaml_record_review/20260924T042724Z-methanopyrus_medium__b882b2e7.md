# YAML Record Review: METHANOPYRUS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanopyrus_medium__b882b2e7.yaml
- Started UTC: 2026-09-24T04:25:56Z
- Finished UTC: 2026-09-24T04:27:24Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:001644 |
| Name | methanopyrus_medium |
| Original name | METHANOPYRUS MEDIUM |
| Category | archaea |
| Media term | mediadive.medium:511 |
| Source | DSMZ Medium 511 through MediaDive |
| Generated path reviewed | data/merge_yaml/merged/methanopyrus_medium__b882b2e7.yaml |
| Canonical owner | data/normalized_yaml/archaea/methanopyrus_medium.yaml |

The reviewed file is a generated merge of one DSMZ/MediaDive owner. Its DSMZ
511 identity is correct, but nested stock solutions were flattened into
top-level ingredients and then duplicate-summed with the main solution.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanopyrus_medium__b882b2e7.yaml` exited 0 with no diagnostics. |
| Strict validator | Passed; `scripts/validate_strict.py data/merge_yaml/merged/methanopyrus_medium__b882b2e7.yaml --out /private/tmp/methanopyrus_medium__b882b2e7.strict.tsv --workers 1 --quiet` reported 0 error rows. |
| Reference validator | Passed; `linkml-reference-validator validate data data/merge_yaml/merged/methanopyrus_medium__b882b2e7.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` performed 0 reference checks and passed. |
| Term validator | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/methanopyrus_medium__b882b2e7.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/` YAML, not embedded `MediaRecipe.curation_history` entries in merged records. |

## Identity and Grounding

- **The DSMZ identity is correct.** The DSMZ PDF and MediaDive REST record both
  identify medium 511 as `METHANOPYRUS MEDIUM`, pH 6.5.
- **The recipe is defined rather than complex.** MediaDive marks `complex_medium:
  no`, and the YAML correctly has `medium_type: DEFINED` and
  `composition_type: DEFINED`.
- **Three stock solutions are not represented.** DSMZ 511 adds 10 ml Modified
  Wolin's mineral solution, 10 ml Marine trace elements solution, and 1 ml
  Wolin's vitamin solution (10x); the YAML has no `solutions` block and hoists
  all stock components into the top-level ingredient list.
- **Some ingredient groundings are broad or stale.** KI and KNO3 still use
  legacy `mediaingredientmech_term` entries, K2HPO4 x 3 H2O and Na2HPO4 x
  3 H2O are grounded to anhydrous salts, Sodium resazurin is grounded to
  Resazurin, and NiCl2 x 6H2O is grounded to nickel dichloride.

## Evidence

### Supported by inspected sources

- DSMZ 511 and MediaDive support the main 1007 ml solution: 980 ml water;
  NH4Cl, K2HPO4 x 3 H2O, KH2PO4, NaCl, MgSO4 x 7H2O, MgCl2 x 6H2O, Na2SO4,
  CaCl2 x 2H2O, KCl, NaHCO3, Na2S x 9H2O; 10 ml Modified Wolin's mineral
  solution; 2 ml each of 0.1 percent Fe, Ni, and tungstate stocks; 10 ml Marine
  trace elements solution; 0.5 ml 0.1 percent Sodium resazurin; and 1 ml
  Wolin's vitamin solution (10x).
- DSMZ 511 and MediaDive support three nested stock formulas: Marine trace
  elements solution, Modified Wolin's mineral solution from medium 141, and
  Wolin's vitamin solution (10x) from medium 120.
- The main-medium preparation imported into YAML matches DSMZ: make the medium
  anoxic with H2/CO2, autoclave in serum vials, add vitamins and sulfide from
  sterile anoxic N2 stocks, add bicarbonate from a sterile anoxic N2/CO2 stock,
  adjust pH to 6.5 if needed, and pressurize after inoculation with H2/CO2.
- The Modified Wolin's mineral solution preparation imported into YAML matches
  DSMZ: dissolve NTA, adjust pH to 6.5 with KOH, add minerals, and set final
  pH to 7.0 with KOH.

### Unsupported or over-scoped in the YAML

- The 980 ml main water row is absent.
- NaCl, MgSO4 x 7H2O, CaCl2 x 2H2O, H3BO3, and Na2WO4 x 2H2O combine
  main-medium amounts with nested stock concentrations.
- Marine trace element, Modified Wolin mineral, and Wolin vitamin ingredients
  are all flattened into the top-level ingredient list at their stock
  concentrations.
- The Fe, Ni, tungstate, sodium resazurin, and vitamin additions lose their
  0.1 percent or 10x stock scopes and ml addition units.

## Completeness

- **Nested solution topology is missing.** Three MediaDive solution IDs are
  required to keep the DSMZ source scopes separate.
- **Main-solution water is missing.** DSMZ lists 980 ml distilled water.
- **Source amounts are replaced by derived g/L values.** MediaDive preserves
  the original g, mg, and ml rows, but the owner keeps only calculated `g_l`
  concentrations.
- **Bounded local search.** A gitignore-independent search for
  `mediadive.medium:511`, `DSMZ Medium 511`, `DSMZ_Medium511`,
  `METHANOPYRUS MEDIUM`, and `methanopyrus_medium` under
  `data/normalized_yaml` and `data/merge_yaml/merged` found this direct DSMZ
  511 owner, a KOMODO 511 copy, TOGO M2663 for DSMZ 511, the TOGO M1655 NBRC
  recipe, and Methanopyrus strain 116 records.
- Empty target-organism and growth-evidence sections are not defects for this
  provider recipe.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The three MediaDive stock solutions were flattened into top-level ingredients. | DSMZ 511 adds Modified Wolin, Marine trace elements, and Wolin vitamin stocks by volume; their components appear in YAML as direct ingredients. | `data/normalized_yaml/archaea/methanopyrus_medium.yaml` and the MediaDive importer |
| Major | Duplicate ingredient merging combined separate solution scopes. | Main-solution NaCl, MgSO4 x 7H2O, and CaCl2 x 2H2O were summed with Modified Wolin rows; Na2WO4 x 2H2O was summed across two stock scopes; H3BO3 was summed across Marine trace and Modified Wolin rows. | `data/normalized_yaml/archaea/methanopyrus_medium.yaml` and cleanup/merge handling |
| Major | Main-solution water and stock-addition source units are missing. | DSMZ 511 lists 980 ml water, 2 ml 0.1 percent Fe/Ni/tungstate stocks, 0.5 ml 0.1 percent Sodium resazurin, and 1 ml Wolin vitamin stock; the YAML keeps calculated final `G_PER_L` values or omits water. | `data/normalized_yaml/archaea/methanopyrus_medium.yaml` and import unit handling |
| Minor | Some chemical groundings are broad or stale. | KI and KNO3 still have legacy MediaIngredientMech links; K2HPO4 x 3 H2O, Na2HPO4 x 3 H2O, Sodium resazurin, and NiCl2 x 6H2O lose hydrate or salt specificity. | Shared ingredient grounding maps |

## Recommended Edits

1. Rebuild `methanopyrus_medium.yaml` with explicit Modified Wolin's mineral,
   Marine trace elements, and Wolin's vitamin stock solutions.
2. Restore 980 ml distilled water to the main solution.
3. Keep NaCl, MgSO4 x 7H2O, CaCl2 x 2H2O, H3BO3, and Na2WO4 x 2H2O scoped to
   their source solutions instead of summing them.
4. Preserve the 2 ml 0.1 percent Fe/Ni/tungstate stocks, 0.5 ml 0.1 percent
   Sodium resazurin stock, and 1 ml Wolin vitamin stock as additions.
5. Replace the stale or broad term links with exact hydrate or salt groundings
   where available.

## Follow-up Checks

- Re-run schema, strict, term, and reference validation on
  `data/normalized_yaml/archaea/methanopyrus_medium.yaml` and the regenerated
  merged record.
- Manually compare the regenerated YAML with DSMZ Medium 511 and MediaDive 511
  to confirm all three nested solution IDs remain scoped and no component is
  summed across solution boundaries.
- Confirm no `mediaingredientmech_term` entries remain.

## Additional Notes

- TOGO M2663 and KOMODO 511 also derive from DSMZ Medium 511 but are separate
  generated records. This report is scoped to the direct MediaDive owner.
