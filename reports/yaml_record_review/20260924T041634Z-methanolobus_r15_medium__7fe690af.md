# YAML Record Review: METHANOLOBUS R15 MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanolobus_r15_medium__7fe690af.yaml
- Started UTC: 2026-09-24T04:15:15Z
- Finished UTC: 2026-09-24T04:16:34Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:002983 |
| Name | methanolobus_r15_medium |
| Original name | METHANOLOBUS R15 MEDIUM |
| Category | archaea |
| Media term | mediadive.medium:J636 |
| Source | JCM Medium 636 through MediaDive J636 |
| Generated path reviewed | data/merge_yaml/merged/methanolobus_r15_medium__7fe690af.yaml |
| Canonical owner | data/normalized_yaml/archaea/methanolobus_r15_medium.yaml |

The reviewed file merged three MediaDive/JCM owners:
`methanolobus_r15_medium`, `clostridium_r6_medium`, and
`clostridium_sw_medium`. JCM pages 636, 637, and 640 show that those are not
source duplicates, so the generated record currently conflates three provider
identities.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanolobus_r15_medium__7fe690af.yaml` printed `No issues found`. |
| Strict validator | Passed; `scripts/validate_strict.py data/merge_yaml/merged/methanolobus_r15_medium__7fe690af.yaml --out /private/tmp/methanolobus_r15_medium__7fe690af.strict.tsv --workers 1 --quiet` reported 0 error rows. |
| Reference validator | Passed; `linkml-reference-validator validate data data/merge_yaml/merged/methanolobus_r15_medium__7fe690af.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` performed 0 reference checks and passed. |
| Term validator | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/methanolobus_r15_medium__7fe690af.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/` YAML, not embedded `MediaRecipe.curation_history` entries in merged records. |

## Identity and Grounding

- **The primary source identity is JCM 636.** The live JCM `GRMD=636` page and
  MediaDive `J636` identify this recipe as `METHANOLOBUS R15 MEDIUM`.
- **The merge contains two wrong identities.** JCM 637 is `CLOSTRIDIUM R6
  MEDIUM`, a variant that uses Medium 636 without methanol and with H2/CO2
  80/20 gas. JCM 640 is `CLOSTRIDIUM SW MEDIUM`, a variant that uses Medium 636
  with 5.0 g/L glucose instead of methanol.
- **The three media were merged because the child variants copied the JCM 636
  chemistry.** `clostridium_r6_medium.yaml` and `clostridium_sw_medium.yaml`
  copied 30 ingredients from `CultureMech:002983`, including methanol, and were
  then treated as source duplicates by fingerprint.
- **Ingredient grounding is mostly specific, but one hydrate is broad.**
  `NiCl2 x 6 H2O` is grounded to `CHEBI:34887` nickel dichloride rather than an
  exact hexahydrate term.

## Evidence

### Supported by inspected sources

- JCM 636 and MediaDive `J636` support a local Solution A with KH2PO4,
  Na2HPO4, yeast extract, tryptone, 1 mg resazurin, and 860 ml water; a local
  Solution B with NH4Cl, NaCl, CaCl2 x 2 H2O, MgCl2 x 6 H2O, 1 ml FeCl2
  solution, 1 ml trace element solution, and 100 ml water; and Solution C with
  3.5 ml 50 percent methanol.
- JCM 636 supports post-autoclave filter-sterilized additions of 10.0 ml trace
  vitamins from Medium 197 and 30.0 ml 8 percent NaHCO3 solution.
- JCM 636 supports autoclaving Solutions A and B separately, autoclaving
  Solution C in a closed tube or vial, combining the three under N2/CO2 80/20,
  distributing under the same gas mixture, sealing with butyl rubber stoppers,
  and reducing before inoculation with 0.025 percent L-cysteine HCl H2O and
  0.025 percent Na2S x 9H2O made as 5 percent autoclaved N2 stocks.
- JCM 637 and MediaDive `J637` support a different Clostridium R6 recipe: use
  Medium 636 without methanol and replace the gas phase with H2/CO2 80/20.
- JCM 640 and MediaDive `J640` support a different Clostridium SW recipe: use
  Medium 636 with 5.0 g/L glucose instead of methanol.

### Unsupported or over-scoped in the YAML

- `parent_media`, `variant_relationship: SOURCE_DUPLICATE`, the Clostridium
  synonyms, and the `categories: [archaea, bacterial]` list all imply that JCM
  637 and JCM 640 are source duplicates of JCM 636. The inspected JCM pages
  contradict that.
- Solution A, Solution B, FeCl2 solution, trace element solution, and trace
  vitamins are flattened into top-level ingredients.
- The source water rows for 860 ml and 100 ml are absent.
- 3.5 ml of 50 percent methanol is represented as 3.5 g/L methanol.
- 30 ml of 8 percent NaHCO3 solution is represented as 30 g/L NaHCO3.
- The reducing-agent additions are present only inside preparation prose, not
  as scoped solution additions.

## Completeness

- **Solution topology is missing.** The generated record cannot distinguish
  Solution A, Solution B, Solution C, the FeCl2 stock, trace element stock,
  trace vitamin stock, NaHCO3 stock, or reducing-agent stocks.
- **Water is missing.** JCM 636 lists water in Solution A and Solution B.
- **The Clostridium variants are incomplete in their own owners.** Both JCM 637
  and JCM 640 copied Medium 636 wholesale. JCM 637 should remove methanol and
  change gas; JCM 640 should replace methanol with 5.0 g/L glucose.
- **Bounded local search.** A gitignore-independent search for
  `methanolobus_r15_medium|Methanolobus R15|METHANOLOBUS R15|Methanolobus`
  under `data/normalized_yaml` and the reviewed merge found the MediaDive/JCM
  owner, the TOGO M650 owner, and the bacterial records that copied this owner.
- Empty target-organism and growth-evidence sections are not defects for this
  provider recipe.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | Three distinct JCM media were merged into one Methanolobus R15 record. | JCM 637 removes methanol and changes gas; JCM 640 replaces methanol with glucose. The reviewed merge includes both as source duplicates of JCM 636. | Merge/fingerprint logic plus `data/normalized_yaml/bacterial/clostridium_r6_medium.yaml` and `data/normalized_yaml/bacterial/clostridium_sw_medium.yaml` |
| Major | JCM 636 local solutions were flattened into final-medium ingredients. | MediaDive J636 and JCM 636 keep Solution A, B, C, FeCl2, trace element, trace vitamins, bicarbonate, and reducing-agent stocks scoped separately. | `data/normalized_yaml/archaea/methanolobus_r15_medium.yaml` and the MediaDive importer |
| Major | Source amounts were converted to derived or wrong dimensions. | Methanol is 3.5 ml of a 50 percent solution, NaHCO3 is 30 ml of an 8 percent solution, and several MediaDive rows preserve 860 ml or 102 ml normalized `g_l` values instead of source amounts. | `data/normalized_yaml/archaea/methanolobus_r15_medium.yaml` and import unit handling |
| Major | Water and reducing-agent solution rows are missing. | JCM 636 lists 860 ml water in Solution A, 100 ml in Solution B, and two 0.025 percent reducing agents before inoculation. | `data/normalized_yaml/archaea/methanolobus_r15_medium.yaml` |
| Minor | The nickel salt is grounded too broadly. | The source row is `NiCl2 x 6 H2O`; the term is `CHEBI:34887` nickel dichloride. | Shared ingredient grounding maps |

## Recommended Edits

1. Break the false `SOURCE_DUPLICATE` merge between JCM 636, JCM 637, and JCM
   640. Keep JCM 637 and JCM 640 as variants of JCM 636 with explicit
   modifications.
2. Repair `data/normalized_yaml/bacterial/clostridium_r6_medium.yaml` by
   removing methanol from the inherited Medium 636 formulation and changing the
   gas phase to H2/CO2 80/20.
3. Repair `data/normalized_yaml/bacterial/clostridium_sw_medium.yaml` by
   replacing methanol with 5.0 g/L glucose.
4. Rework `data/normalized_yaml/archaea/methanolobus_r15_medium.yaml` so JCM
   636 keeps Solution A, Solution B, Solution C, Medium 187 stocks, Medium 197
   trace vitamins, 8 percent NaHCO3, and 5 percent N2-stored reducing stocks in
   their correct scopes.
5. Restore source dimensions for water, 50 percent methanol, 8 percent NaHCO3,
   FeCl2/trace-element/trace-vitamin additions, and the two reducing-agent
   stocks.
6. Re-ground `NiCl2 x 6 H2O` to an exact nickel chloride hexahydrate term.

## Follow-up Checks

- Re-run schema, strict, term, and reference validation on the three repaired
  normalized owners and regenerated merged outputs.
- Re-run merge verification and confirm the three JCM accessions no longer
  share one `merge_fingerprint`.
- Manually compare JCM 636, 637, and 640 with their regenerated files to confirm
  methanol remains only in Methanolobus R15, Clostridium R6 has H2/CO2 gas and
  no methanol, and Clostridium SW has glucose instead of methanol.

## Additional Notes

- TOGO M650 imports the same JCM 636 identity but has its own older
  solution-migration problems, including wrong links to unrelated generic
  `Solution A` and `Solution B` records. This report is scoped to the
  MediaDive/JCM merge fingerprint.
