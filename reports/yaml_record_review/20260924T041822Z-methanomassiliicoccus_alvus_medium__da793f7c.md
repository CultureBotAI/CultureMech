# YAML Record Review: Methanomassiliicoccus Alvus Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanomassiliicoccus_alvus_medium__da793f7c.yaml
- Started UTC: 2026-09-24T04:16:34Z
- Finished UTC: 2026-09-24T04:18:22Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:007760 |
| Name | methanomassiliicoccus_alvus_medium |
| Original name | Methanomassiliicoccus Alvus Medium |
| Category | archaea |
| Media term | TOGO:M1231 |
| Source | TOGO M1231 / JCM M1149 |
| Generated path reviewed | data/merge_yaml/merged/methanomassiliicoccus_alvus_medium__da793f7c.yaml |
| Canonical owner | data/normalized_yaml/archaea/TOGO_M1231_Methanomassiliicoccus_Alvus_Medium.yaml |

The reviewed file is a generated merge of one TOGO owner. It preserves a TOGO
M1231 recipe imported from the older JCM 1149 record, but the live JCM 1149 URL
now resolves to `METHANOMETHYLOPHILUS ALVI MEDIUM`, an expanded formulation.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanomassiliicoccus_alvus_medium__da793f7c.yaml` printed `No issues found`. |
| Strict validator | Passed; `scripts/validate_strict.py data/merge_yaml/merged/methanomassiliicoccus_alvus_medium__da793f7c.yaml --out /private/tmp/methanomassiliicoccus_alvus_medium__da793f7c.strict.tsv --workers 1 --quiet` reported 0 error rows. |
| Reference validator | Passed; `linkml-reference-validator validate data data/merge_yaml/merged/methanomassiliicoccus_alvus_medium__da793f7c.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` performed 0 reference checks and passed. |
| Term validator | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/methanomassiliicoccus_alvus_medium__da793f7c.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/` YAML, not embedded `MediaRecipe.curation_history` entries in merged records. |

## Identity and Grounding

- **The TOGO identity is internally consistent.** TOGO M1231 still returns
  `Methanomassiliicoccus Alvus Medium` and links the source to JCM M1149, and
  the reviewed YAML uses the same TOGO ID and label.
- **The stored JCM source URL is no longer an exact identity match.** The same
  `GRMD=1149` endpoint now has the title `METHANOMETHYLOPHILUS ALVI MEDIUM`
  and a broader formulation than the one preserved in TOGO and MediaDive
  snapshots.
- **Simple-salt grounding is mostly exact.** MgSO4 x 7 H2O, CaCl2 x 2 H2O,
  KH2PO4, NH4Cl, L-Cysteine HCl H2O, water, gases, and NaCl use appropriate
  CHEBI terms.
- **One hydrate is grounded too broadly.** The source row is Sodium acetate x
  3H2O, but the YAML grounds it to generic `CHEBI:32954` sodium acetate.

## Evidence

### Supported by inspected sources

- The TOGO M1231 API supports the direct old JCM rows captured in the YAML:
  980 ml water, 0.4 g MgSO4 x 7H2O, 5 g NaCl, 0.05 g CaCl2 x 2H2O, 0.5 g
  KH2PO4, 1 g NH4Cl, 1 mg resazurin, 2.7 g Sodium acetate x 3H2O, and 0.5 g
  L-Cysteine HCl H2O.
- TOGO M1231 supports 1 ml trace element solution from Medium M439, 1 ml
  Selenite--tungstate solution from Medium M431, and post-autoclave additions
  per liter of 20 ml 8 percent NaHCO3 solution and 8 ml 5 percent Na2S x 9H2O
  solution.
- TOGO M1231 supports pH 7.0, boiling and cooling under H2-CO2 4:1 gas,
  distributing under the same gas, sealing with butyl stoppers before
  autoclaving, and anaerobic post-autoclave additions.
- MediaDive `J1149` preserves the old `METHANOMASSILIICOCCUS ALVUS MEDIUM`
  identity and formula, with nested trace element and Selenite--tungstate
  recipes.

### Unsupported or over-scoped in the YAML

- The live JCM 1149 URL now supports an expanded
  `METHANOMETHYLOPHILUS ALVI MEDIUM`, not the old
  `METHANOMASSILIICOCCUS ALVUS MEDIUM` formulation stored here.
- The live JCM page adds 2 g/L each of yeast extract, Bacto peptone, Casamino
  acids, and Trypticase peptone plus a 6.3 ml 50 percent methanol
  post-autoclave addition. Those rows are absent because this record still
  mirrors the older TOGO and MediaDive payloads.
- 980 ml distilled water is represented as `980 G_PER_L`.
- 1 mg resazurin is represented as `1 G_PER_L`.
- Four stock-addition volumes are represented as empty `Unknown solution`
  records with units of `G_PER_L`.
- Preparation context is absent from the YAML even though the TOGO payload
  carries anaerobic gas, pH, autoclave, stopper, and post-autoclave handling
  instructions.

## Completeness

- **Current-source drift is unresolved.** The maintained TOGO owner either
  needs immutable retrieved-date provenance for the old JCM page or a deliberate
  update to the current `METHANOMETHYLOPHILUS ALVI MEDIUM` identity and formula.
- **Stock recipes are missing.** The Trace element and Selenite--tungstate
  references should link to or expand the referenced JCM/TOGO stock media
  instead of becoming empty solutions.
- **Post-autoclave additions are underspecified.** The NaHCO3 and Na2S x 9H2O
  stocks need stock concentration, addition volume, and post-autoclave scope.
- **Preparation steps are missing.** The record loses pH, gas atmosphere,
  anaerobic distribution, butyl-stopper sealing, autoclaving, and aseptic
  post-autoclave addition instructions.
- Empty target-organism and growth-evidence sections are not defects for this
  provider recipe.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | The cited live JCM URL now resolves to a different 1149 identity and formula. | TOGO M1231 and MediaDive `J1149` preserve the old Methanomassiliicoccus alvus recipe, while live JCM 1149 is `METHANOMETHYLOPHILUS ALVI MEDIUM` with yeast extract, Bacto peptone, Casamino acids, Trypticase peptone, methanol, and extra culture-filtrate instructions. | `data/normalized_yaml/archaea/TOGO_M1231_Methanomassiliicoccus_Alvus_Medium.yaml` |
| Major | Stock additions were migrated into empty solutions with wrong dimensions. | The source has 1 ml M439 trace element stock, 1 ml M431 Selenite--tungstate stock, 20 ml 8 percent NaHCO3 stock, and 8 ml 5 percent Na2S x 9H2O stock; the YAML stores four empty `Unknown solution` entries with those volumes as `G_PER_L`. | `data/normalized_yaml/archaea/TOGO_M1231_Methanomassiliicoccus_Alvus_Medium.yaml` and solution migration |
| Major | Non-g/L source rows were treated as g/L ingredients. | The TOGO source uses 980 ml water and 1 mg resazurin; the YAML records `980 G_PER_L` and `1 G_PER_L`. | `data/normalized_yaml/archaea/TOGO_M1231_Methanomassiliicoccus_Alvus_Medium.yaml` and import unit handling |
| Major | Anaerobic preparation instructions are missing. | TOGO M1231 carries pH 7.0, H2-CO2 4:1 boiling, cooling, distribution, stopper sealing, autoclaving, and post-autoclave addition instructions; the YAML has no `preparation_steps`. | `data/normalized_yaml/archaea/TOGO_M1231_Methanomassiliicoccus_Alvus_Medium.yaml` |
| Minor | Sodium acetate trihydrate is grounded to an anhydrous/broad salt. | The source row is Sodium acetate x 3H2O; the YAML term is `CHEBI:32954` sodium acetate. | Shared ingredient grounding maps |

## Recommended Edits

1. Decide whether TOGO M1231 should remain an archived
   `Methanomassiliicoccus Alvus Medium` import or be updated to the live JCM
   1149 `METHANOMETHYLOPHILUS ALVI MEDIUM` recipe.
2. If the old import is retained, add retrieved-date or snapshot provenance for
   the JCM URL so the record no longer appears to assert the current JCM 1149
   formula.
3. Restore the two referenced stock recipes from Medium M439 and Medium M431,
   with scoped 1 ml addition volumes.
4. Restore the 20 ml 8 percent NaHCO3 and 8 ml 5 percent Na2S x 9H2O
   post-autoclave additions as stock additions, not direct g/L rows or empty
   solutions.
5. Preserve source units for 980 ml water and 1 mg resazurin.
6. Add the pH 7.0, H2-CO2 4:1 anaerobic handling, butyl-stopper sealing,
   autoclave, and post-autoclave addition instructions.
7. Re-ground Sodium acetate x 3H2O to an exact trihydrate term if one is
   available; otherwise leave a qualifier explaining the hydrate mismatch.

## Follow-up Checks

- Re-run schema, strict, term, and reference validation on
  `data/normalized_yaml/archaea/TOGO_M1231_Methanomassiliicoccus_Alvus_Medium.yaml`
  and the regenerated merged record.
- Manually compare the curated owner with TOGO M1231 or, if the provider is
  updated, the live JCM 1149 page.
- Confirm the two referenced stock recipes resolve to the intended TOGO/JCM
  stock medium IDs and are either linked or expanded with their own source
  scopes.
- Confirm generated output contains no empty `Unknown solution` placeholders.

## Additional Notes

- `data/normalized_yaml/archaea/JCM_J1149_METHANOMASSILIICOCCUS_ALVUS_MEDIUM.yaml`
  is a MediaDive-derived snapshot of the old JCM 1149 identity. It already
  flattened Medium 439 and Medium 431 into top-level ingredient rows and is not
  the owner of the reviewed TOGO merge fingerprint.
- `data/normalized_yaml/archaea/methanomassiliicoccus_alvus_medium.yaml` uses
  the same slug for DSMZ 1640, a different medium with Anaerobe Basal Broth,
  methanol, sodium resazurin, N2 handling, and pH 7.4-7.6.
