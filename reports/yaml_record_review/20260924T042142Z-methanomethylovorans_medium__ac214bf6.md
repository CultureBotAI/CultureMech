# YAML Record Review: Methanomethylovorans medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanomethylovorans_medium__ac214bf6.yaml
- Started UTC: 2026-09-24T04:19:47Z
- Finished UTC: 2026-09-24T04:21:42Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:008490 |
| Name | methanomethylovorans_medium |
| Original name | Methanomethylovorans medium |
| Category | archaea |
| Media term | TOGO:M1912 |
| Source | TOGO M1912 / NBRC M1173 |
| Generated path reviewed | data/merge_yaml/merged/methanomethylovorans_medium__ac214bf6.yaml |
| Canonical owner | data/normalized_yaml/archaea/methanomethylovorans_medium.yaml |

The reviewed file is a generated merge of one TOGO owner. The maintained owner
was repaired after this merge was generated, so this generated file is stale in
addition to preserving older solution-migration defects.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanomethylovorans_medium__ac214bf6.yaml` printed `No issues found`. |
| Strict validator | Passed; `scripts/validate_strict.py data/merge_yaml/merged/methanomethylovorans_medium__ac214bf6.yaml --out /private/tmp/methanomethylovorans_medium__ac214bf6.strict.tsv --workers 1 --quiet` reported 0 error rows. |
| Reference validator | Passed; `linkml-reference-validator validate data data/merge_yaml/merged/methanomethylovorans_medium__ac214bf6.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` performed 0 reference checks and passed. |
| Term validator | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/methanomethylovorans_medium__ac214bf6.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/` YAML, not embedded `MediaRecipe.curation_history` entries in merged records. |

## Identity and Grounding

- **The source identity is correct.** TOGO M1912 and the live NBRC medium 1173
  page both identify the recipe as `Methanomethylovorans medium`.
- **The reviewed file is stale.** It was generated on 2026-08-06 from
  `methanomethylovorans_medium.yaml`; the owner collapsed identical water and
  NaCl duplicate sums on 2026-09-02, but those repairs have not been
  regenerated into this merge.
- **Two stock links point to unrelated generic MediaDive stocks.** NBRC 1173
  defines local `Vitamin solution*` and `Trace elements solution**` recipes.
  MediaDive solution 6241 contains only a three-vitamin 100 ml stock, and
  MediaDive solution 6129 contains ZnSO4, MnCl2, MoO3, CuSO4, and
  Co(NO3)2 salts that do not match the NBRC trace recipe.
- **Several hydrate salts are grounded too broadly.** The CoCl2 x 6H2O and
  NiCl2 x 6H2O rows are grounded to generic cobalt dichloride and nickel
  dichloride. Ca-pantothenate is grounded to pantothenate rather than a calcium
  salt.

## Evidence

### Supported by inspected sources

- TOGO M1912 and NBRC 1173 support a main liter containing KH2PO4, NH4Cl, NaCl,
  MgCl2 x 6H2O, KCl, 0.15 g CaCl2 x 2H2O, 10 ml local vitamin solution, 10 ml
  local trace elements solution, FeSO4 x 7H2O, Trimethylamine-HCl, 0.8 ml
  methanol, 1 mg resazurin, NaHCO3, Na2S x 9H2O, and distilled water.
- NBRC 1173 defines the local vitamin stock as nine vitamins in 1 L water:
  biotin, folic acid, Pyridoxine-HCl, Thiamine-HCl, riboflavin, nicotinic acid,
  Ca-pantothenate, p-Aminobenzoic acid, and Vitamin B12.
- NBRC 1173 defines the local trace stock as Nitrilotriacetic acid, FeCl3 x
  6H2O, MnCl2 x 4H2O, CoCl2 x 6H2O, CaCl2 x 2H2O, ZnCl2, CuCl2 x 2H2O, H3BO3,
  Na2MoO4 x 2H2O, NaCl, NiCl2 x 6H2O, Na2SeO4, Na2WO4, KAl(SO4)2 x 12H2O,
  NaOH, and distilled water.
- TOGO M1912 preserves the NBRC pH 7.2-7.4 and the anaerobic instructions to
  autoclave the partial main solution under N2/CO2 80/20, separately autoclave
  FeSO4 x 7H2O and Na2S x 9H2O solutions under N2, then add the filter-sterile
  vitamin stock, 5 percent NaHCO3, methanol, FeSO4 x 7H2O, and Na2S x 9H2O
  before inoculation.
- TOGO M1912 preserves the local trace-stock preparation note: dissolve NTA,
  adjust to pH 6.5 with NaOH, add minerals, and set final pH 7.0.

### Unsupported or over-scoped in the YAML

- The generated YAML still sums three 1 L water rows to `3.0 G_PER_L` and two
  1 g NaCl rows to `2.0 G_PER_L`; the maintained owner now has both values
  collapsed back to `1.0`.
- The local NBRC vitamin and trace stocks are linked to unrelated MediaDive
  generic solution IDs.
- The local vitamin and trace stock ingredients are flattened into top-level
  ingredient rows, which sums the main and trace CaCl2 x 2H2O rows to
  `0.25 G_PER_L`.
- 1 mg resazurin is represented as `1 G_PER_L`.
- 0.8 ml methanol is represented as `0.8 G_PER_L`.
- 10 ml vitamin stock and 10 ml trace stock are represented as empty
  `Unknown solution` entries with units of `G_PER_L`.
- No preparation steps are present.

## Completeness

- **Generated output is stale.** The 2026-09-02 upstream water and NaCl
  duplicate repair is absent from the reviewed generated file.
- **Solution topology is missing.** The local vitamin and trace element stocks
  need their own compositions and 10 ml addition volumes, not generic MediaDive
  links or flattened top-level rows.
- **Staged anaerobic preparation is missing.** The record does not capture the
  partial autoclave, separate FeSO4 and Na2S autoclaves, filter-sterile stock
  additions, pH 7.2-7.4 target, or trace-stock pH adjustment.
- **Bounded local search.** A gitignore-independent search for
  `Methanomethylovorans`, `NBRC_M1173`, `TOGO_M1912`, `TOGO:M1912`, and
  `methanomethylovorans_medium` under `data/normalized_yaml` and
  `data/merge_yaml/merged` found this TOGO M1912 owner, its stale generated
  output, the separate TOGO M1990 medium with the same short label, the
  separate TOGO M1913 thermophila medium, and the TOGO M1038 uponensis medium.
- Empty target-organism and growth-evidence sections are not defects for this
  provider recipe.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated file predates an upstream duplicate-sum repair. | `data/normalized_yaml/archaea/methanomethylovorans_medium.yaml` collapsed identical water and NaCl sums on 2026-09-02; this 2026-08-06 merge still has water `3.0 G_PER_L` and NaCl `2.0 G_PER_L`. | Merge artifacts regenerated from `data/normalized_yaml/archaea/methanomethylovorans_medium.yaml` |
| Major | The two stock solution links are wrong. | NBRC 1173 defines local vitamin and trace recipes under the same medium; MediaDive 6241 and 6129 are unrelated generic stocks with different component lists. | `data/normalized_yaml/archaea/methanomethylovorans_medium.yaml` |
| Major | Local stock recipes were flattened into the final medium. | NBRC adds 10 ml vitamin stock and 10 ml trace stock to the main liter, but the YAML hoists their components into top-level ingredients and leaves only empty solution placeholders. | `data/normalized_yaml/archaea/methanomethylovorans_medium.yaml` and solution migration |
| Major | Several source units were converted to g/L incorrectly. | The source uses 1 mg resazurin, 0.8 ml methanol, and 10 ml additions of each stock; the YAML stores those as `1`, `0.8`, and `10 G_PER_L`. | `data/normalized_yaml/archaea/methanomethylovorans_medium.yaml` and import unit handling |
| Major | NBRC preparation instructions are absent. | TOGO M1912 preserves anaerobic autoclave, filter-sterile addition, final pH, and trace-stock preparation notes; the YAML has no `preparation_steps`. | `data/normalized_yaml/archaea/methanomethylovorans_medium.yaml` |
| Minor | Several salts are grounded too broadly. | CoCl2 x 6H2O, NiCl2 x 6H2O, and Ca-pantothenate lose hydrate or salt specificity in CHEBI grounding. | Shared ingredient grounding maps |

## Recommended Edits

1. Regenerate the merged record after the 2026-09-02 duplicate-sum repair so
   water and NaCl no longer carry stale summed values.
2. Remove the false `mediadive.solution:6241` and `mediadive.solution:6129`
   links from the local NBRC stocks.
3. Represent the NBRC vitamin stock and trace elements stock as local solutions
   with 10 ml additions to the main recipe.
4. Stop flattening local stock rows into final-medium ingredients; keep CaCl2 x
   2H2O, water, NaCl, vitamins, and trace components scoped to their source
   subsolutions.
5. Restore source units for 1 mg resazurin, 0.8 ml methanol, and the two 10 ml
   stock additions.
6. Add the anaerobic preparation instructions and trace-stock pH note from TOGO
   M1912/NBRC 1173.
7. Re-ground CoCl2 x 6H2O, NiCl2 x 6H2O, and Ca-pantothenate to exact terms
   where available.

## Follow-up Checks

- Re-run schema, strict, term, and reference validation on
  `data/normalized_yaml/archaea/methanomethylovorans_medium.yaml` and the
  regenerated merged record.
- Manually compare the regenerated YAML with TOGO M1912 and NBRC 1173 to ensure
  main, vitamin, and trace recipes remain separate and no local row is linked to
  MediaDive 6241 or 6129.
- Confirm generated output has water `1.0` and main NaCl `1.0`, with the trace
  NaCl and CaCl2 rows scoped only to the trace solution.
- Confirm no empty `Unknown solution` placeholder remains for the two local
  stocks.

## Additional Notes

- `data/normalized_yaml/archaea/TOGO_M1990_Methanomethylovorans_medium.yaml`
  has the same `Methanomethylovorans medium` short label but represents TOGO
  M1990 / NBRC M1276, not the reviewed TOGO M1912 / NBRC M1173 recipe.
- `data/normalized_yaml/archaea/methanomethylovorans_thermophila_medium.yaml`
  shares the same local-solution migration pattern and should be reviewed under
  its own generated output.
