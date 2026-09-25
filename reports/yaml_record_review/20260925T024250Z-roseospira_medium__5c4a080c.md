# YAML Record Review: roseospira_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/roseospira_medium__5c4a080c.yaml
- Started UTC: 2026-09-25T02:40:19Z
- Finished UTC: 2026-09-25T02:42:48Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` record:

- Path: `data/merge_yaml/merged/roseospira_medium__5c4a080c.yaml`
- ID: `CultureMech:002917`
- Label: `roseospira_medium`
- Source identity: JCM Medium J568 / MediaDive `J568`
- Source CURIEs: `mediadive.medium:J568`, `mediadive.medium:J648`
- Generated from:
  - `data/normalized_yaml/bacterial/roseospira_medium.yaml`
  - `data/normalized_yaml/bacterial/rhodobacter_dangmalensis_medium.yaml`

The target is a generated merge. Future fixes belong in normalized source
records and merge logic, followed by regeneration of `data/merge_yaml/merged/`.

## Validation

| Check | Result |
| --- | --- |
| Open schema, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/roseospira_medium__5c4a080c.yaml` | Passed; exited 0 with no diagnostics. |
| Strict schema, `scripts/validate_strict.py data/merge_yaml/merged/roseospira_medium__5c4a080c.yaml --out /private/tmp/roseospira_medium__5c4a080c.strict.tsv --workers 1 --quiet` | Passed; 0 error rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/roseospira_medium__5c4a080c.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were present. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/roseospira_medium__5c4a080c.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: `just validate-history` validates standalone `history/` records, not embedded `MediaRecipe.curation_history` entries. |

## Identity and Grounding

- The generated target is internally inconsistent. Its stable ID, media term,
  name, pH 6.8, and post-autoclave instruction come from JCM J568 Roseospira
  Medium, but its CaCl2, MgSO4, and NaCl concentrations come from JCM J648
  Rhodobacter dangmalensis Medium.
- MediaDive J568 and the live JCM `GRMD=568` page agree that Roseospira
  Medium contains MgSO4 x 7 H2O 1.5 g, NaCl 20.0 g, CaCl2 x 2 H2O 0.15 g,
  5 ml ferric citrate 0.1% w/v, 1 ml SL7, 1000 ml water, pH 6.8, and
  post-autoclave vitamin B12 / NaHCO3 / Na2S2O3 additions.
- MediaDive J648 resolves a distinct `RHODOBACTER DANGMALENSIS MEDIUM`
  source with MgSO4 x 7 H2O 0.2 g, NaCl 0.4 g, CaCl2 x 2 H2O 0.05 g, pH 7.0,
  no vitamin B12 / NaHCO3 / Na2S2O3 additions, and the same SL7 and ferric
  citrate stock identities. The live JCM `GRMD=648` page returned
  `Nothing found` on 2026-09-25, so MediaDive is the usable capture for J648.
- TOGO M572 is the TOGO capture of the same JCM `GRMD=568` recipe. It is not
  linked to the MediaDive J568 owner in this generated target.
- The exact source-ID ignored-inclusive search covered `data` and `src` YAML
  and Python files for `mediadive.medium:J568`, `mediadive.medium:J648`,
  `JCM_J568`, `JCM_J648`, `rhodobacter_dangmalensis_medium`, `TOGO:M572`,
  `TOGO_M572_Roseospira_Medium`, `JCM_M568`, `JCM_M648`, `GRMD=568`, and
  `GRMD=648`. It found the MediaDive J568 owner, MediaDive J648 owner, TOGO
  J568 owner, generated targets, and `data/metal_ree_analysis.yaml`.

## Evidence

- JCM J568 supports final-medium masses of KH2PO4 0.5 g, MgSO4 x 7 H2O
  1.5 g, NaCl 20.0 g, NH4Cl 0.6 g, CaCl2 x 2 H2O 0.15 g, sodium pyruvate
  3.0 g, yeast extract 0.4 g, 5.0 ml ferric citrate stock, 1.0 ml
  Micronutrient solution SL7, and 1.0 L distilled water.
- The generated target uses J648 values for MgSO4 x 7 H2O, NaCl, and
  CaCl2 x 2 H2O, producing 0.198807 g/L MgSO4 x 7 H2O, 0.397614 g/L NaCl,
  and 0.0497018 g/L CaCl2 x 2 H2O under a J568 label.
- JCM J568 supports adding 1.0 ml vitamin B12 solution, NaHCO3 to 0.1% final,
  and Na2S2O3 to 2.0 mM final after autoclaving. The target keeps this only
  as prose in a preparation step; the additions are absent from structured
  ingredients or solutions.
- JCM J568 supports 5.0 ml of a 0.1% w/v ferric citrate stock, not direct
  ferric citrate at 5 g/L.
- JCM J568 supports a 1.0 ml SL7 stock addition and a separate SL7 recipe
  made with 1.0 ml 25% v/v HCl, seven trace salts, and 1.0 L distilled water.
  The target flattens HCl and the trace salts into final `G_PER_L` rows and
  omits both the final water and the stock water.

## Completeness

- The generated target lacks an explicit SL7 solution row.
- The generated target lacks the final and SL7 water rows.
- The generated target lacks structured vitamin B12, NaHCO3, and Na2S2O3
  post-autoclave additions.
- The generated target lacks the valid TOGO M572 duplicate relation for JCM
  J568 and incorrectly merges the distinct JCM J648 recipe.
- The generated target has no target-organism, growth-metric, reference, or
  evidence blocks. These are optional in the schema and the JCM source recipe
  does not by itself establish a specific growth outcome.

## Findings

### Blocker

1. **The generated record is a J568/J648 chimera.**
   `merge_recipes.py` merged Roseospira Medium J568 with Rhodobacter
   dangmalensis Medium J648 because the two records share an ingredient set
   after stock flattening, even though their concentrations, pH values, and
   post-autoclave additions differ. The generated target advertises J568 but
   carries J648 values for three base salts. Future fixes belong in
   `data/normalized_yaml/bacterial/roseospira_medium.yaml`,
   `data/normalized_yaml/bacterial/rhodobacter_dangmalensis_medium.yaml`, and
   the ingredient-fingerprint merge rules in `src/culturemech/merge/`.

### Major

1. **The SL7 micronutrient stock is flattened into the final medium.**
   JCM J568 and J648 add 1 ml of SL7 to the final liter. The generated target
   instead contains the HCl and trace salts from the 1001 ml SL7 stock as
   final `G_PER_L` ingredients and omits the 1 ml stock addition.

2. **Ferric citrate stock volume was converted to 5 g/L ferric citrate.**
   The JCM source says 5 ml of a 0.1% w/v ferric citrate stock. The target
   encodes direct ferric citrate at `5 G_PER_L`, losing both the stock
   concentration and the stock volume.

3. **Post-autoclave additions are only prose.**
   Vitamin B12 solution, NaHCO3 to 0.1% final, and Na2S2O3 to 2.0 mM final
   are source ingredients added after autoclaving. The target includes them
   only in a `preparation_steps` sentence, so the structured recipe is
   incomplete.

4. **Source water rows are omitted.**
   The source has 1.0 L distilled water in the final medium and 1.0 L in the
   SL7 stock. Neither appears in the generated target.

5. **The TOGO M572 duplicate is split from the MediaDive J568 owner.**
   TOGO M572 is the same JCM `GRMD=568` source and should be reconciled with
   MediaDive J568 after both are repaired. It currently remains in a separate
   generated `ROSEOSPIRA_MEDIUM.yaml` target with empty SL7 and vitamin B12
   solution placeholders.

## Recommended Edits

1. Separate JCM J568 Roseospira Medium from JCM J648 Rhodobacter
   dangmalensis Medium by repairing their normalized ingredient/solution
   structures and by preventing ingredient-only fingerprints from merging
   records with different concentration signatures and post-autoclave
   additions.
2. Repair `data/normalized_yaml/bacterial/roseospira_medium.yaml` so its final
   medium contains the JCM J568 base concentrations, 5 ml/L ferric citrate
   stock, 1 ml/L SL7, final water, pH 6.8, and structured post-autoclave
   additions for vitamin B12, NaHCO3, and Na2S2O3.
3. Repair `data/normalized_yaml/bacterial/rhodobacter_dangmalensis_medium.yaml`
   so it keeps the JCM J648 pH 7.0 formulation separate and does not inherit
   J568-specific post-autoclave additions.
4. Repair `data/normalized_yaml/bacterial/TOGO_M572_Roseospira_Medium.yaml`
   to the same JCM J568 structure and add reciprocal `SOURCE_DUPLICATE`
   metadata between it and the repaired MediaDive J568 owner.
5. Regenerate `data/merge_yaml/merged/` and verify that J568 and J648 no
   longer merge, while the J568 MediaDive and TOGO captures do merge or link
   as source duplicates.

## Follow-up Checks

- `just validate data/normalized_yaml/bacterial/roseospira_medium.yaml`
- `just validate data/normalized_yaml/bacterial/rhodobacter_dangmalensis_medium.yaml`
- `just validate data/normalized_yaml/bacterial/TOGO_M572_Roseospira_Medium.yaml`
- The focused open-schema, strict, reference, and term validators used in this
  review against the regenerated generated targets.
- A manual comparison of regenerated J568 and J648 records against the
  inspected MediaDive/JCM J568 and MediaDive J648 payloads, specifically
  checking pH, CaCl2/MgSO4/NaCl concentrations, ferric citrate stock, SL7,
  water, vitamin B12, NaHCO3, and Na2S2O3.
- An exact ignored-inclusive search for J568, J648, TOGO M572, and TOGO M663
  source IDs before adding duplicate links.

## Additional Notes

- The TOGO M572 owner confirms the same JCM J568 source shape but has its own
  unit/import damage: it leaves SL7 and vitamin B12 solution as `Unknown
  solution` placeholders and imports 1 L water as `1 G_PER_L`.
