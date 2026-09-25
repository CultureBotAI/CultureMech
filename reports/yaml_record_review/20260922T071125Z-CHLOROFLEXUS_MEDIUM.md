# YAML Record Review: Chloroflexus Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml
- Started UTC: 2026-09-22T07:10:10Z
- Finished UTC: 2026-09-22T07:11:26Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:007800` |
| Name | `chloroflexus_medium` |
| Original name | `Chloroflexus Medium` |
| Media term | `TOGO:M1268` / `Chloroflexus Medium` |
| Source | TOGO Medium M1268, sourced to JCM `JCM_M1183` |
| Generated status | Single-source derived merge generated from `data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml` |

This is a generated one-record merge. Future scientific corrections belong in
`data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml` or in the
TOGO import and solution migration code that produced its current flattened
shape.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml` | Passed with no issues reported. |
| Strict closed-schema validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml --out /private/tmp/CHLOROFLEXUS_MEDIUM.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated with 0 reference checks. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the validator emitted the known `eutils` / `pkg_resources` deprecation warning. |
| Embedded history | `just validate-history` | Not checked: that recipe validates standalone `history/*.yaml` records against `HistoryRecord`, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

I used the offline `uv` validator invocations above instead of the `just`
validator wrappers because the local project lock currently tries to build
`llvmlite==0.46.0` under Python 3.13 and fails inside setuptools before the
CultureMech validators run.

## Identity and Grounding

- The CultureMech ID, TOGO term, and source metadata consistently identify TOGO
  Medium M1268 from JCM `JCM_M1183`, exposed by JCM as medium 1183.
- The JCM page title for medium 1183 is CHLOROFLEXUS MEDIUM and its formula
  agrees with the TOGO M1268 component tree.
- An ignored-independent `rg --no-ignore --hidden` search for
  `CultureMech:007800`, `TOGO_M1268`, `M1268`, `JCM_M1183`, `GRMD=1183`, and
  `TOGO:M1268` across `data/normalized_yaml` and `data/merge_yaml/merged`
  found this exact TOGO owner and generated target. The same source URL also
  appears in a separate direct-JCM normalized record,
  `data/normalized_yaml/bacterial/chloroflexus_medium.yaml`, which is not a
  member of this generated merge.

## Evidence

I inspected the TOGO M1268 JSON and the JCM GRMD 1183 page. They support the
TOGO/JCM identity and the main simple ingredient names and amounts, but the
record loses all stock-solution boundaries:

- JCM lists a 1 L main solution containing the direct salt, HEPES, thiosulfate,
  and yeast extract gram amounts that appear in the YAML. These direct amounts
  are source-supported for the 1 L preparation.
- JCM adds `1.0 ml` Trace vitamins solution and `1.0 ml` Trace elements solution
  to the main solution. The record has empty stubs for both at `1 G_PER_L` and
  also flattens every Trace vitamins component into a top-level ingredient.
- JCM says to add, after autoclaving, `1 ml` of 5% Na2S x 9 H2O solution, `1 ml`
  of 5% CaCl2 x 2 H2O solution, and `10 ml` of 3% NaHCO3 solution. The YAML has
  three empty stubs for those stock additions but no bicarbonate ingredient and
  no stock compositions.
- The Trace vitamins stock is prepared from milligram amounts in 100 ml water.
  The record stores those milligram numbers as direct `G_PER_L` values: Biotin
  `2`, p-Aminobenzoic acid `5`, Pyridoxine-HCl `10`, Folic acid `2`, Vitamin
  B12 `0.5`, and the remaining vitamins are all top-level rows rather than
  stock components.
- The 1 L main water and the 100 ml Trace vitamins water were collapsed into one
  `101.0 G_PER_L` Distilled water row with a `Merged 2 duplicates: 1.0, 100.0`
  note.

## Completeness

- Five solution additions are structurally incomplete: NaHCO3 solution, CaCl2 x
  2 H2O solution, Na2S x 9 H2O solution, Trace vitamins solution, and Trace
  elements solution all have empty `composition` arrays.
- The JCM preparation protocol is absent. The record does not encode
  post-autoclave addition of sulfide, calcium chloride, and bicarbonate stocks,
  or adjustment to pH 7.5.
- The Trace elements solution is explicitly a cross-reference to JCM Medium 310
  in the source, but that cross-reference is only a note in the empty solution
  stub.
- Empty `target_organisms` and `growth_metrics` slots are not defects in this
  source-formulation record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Five JCM stock additions were migrated to empty solution stubs, leaving the recipe unable to reproduce the source formulation. | JCM 1183 uses bicarbonate, calcium chloride, sulfide, trace vitamin, and trace element solution additions. The YAML has all five in `solutions`, but every `composition` is empty and every addition amount is encoded as `G_PER_L`. | Rebuild `data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml` from the TOGO/JCM nested component tree, or fix the TOGO importer / solution migrator. |
| major | Trace vitamins and water amounts were flattened into unsupported top-level concentrations. | Trace vitamins are milligram amounts in 100 ml water; the record stores them as direct `G_PER_L` rows. The 1 L main water and 100 ml vitamin-stock water were summed into one `101.0 G_PER_L` water row. | Keep the Trace vitamins stock as a solution and keep the two water volumes scoped to their own solution blocks. |
| major | Source preparation context is missing. | JCM 1183 instructs post-autoclave addition of three stocks and then pH 7.5 adjustment; `preparation_steps` is absent. | Add source-supported preparation steps to the normalized M1268 owner. |

## Recommended Edits

1. Rebuild the M1268 normalized record with nested NaHCO3 solution, CaCl2 x 2
   H2O solution, Na2S x 9 H2O solution, Trace vitamins solution, and Trace
   elements solution. Remove direct top-level rows for Trace vitamins members.
2. Correct amount scopes: main-recipe grams belong in 1 L water, Trace vitamins
   milligram amounts belong in a 100 ml stock, and the NaHCO3/CaCl2/Na2S stock
   addition volumes should remain milliliters with their 3% or 5% stock
   strengths.
3. Follow the JCM Medium 310 cross-reference before filling the Trace elements
   solution composition.
4. Add JCM preparation steps for autoclave-default sterilization, post-autoclave
   stock addition, and pH 7.5 adjustment.
5. Regenerate `data/merge_yaml/merged/CHLOROFLEXUS_MEDIUM.yaml` after the
   normalized M1268 owner is repaired.

## Follow-up Checks

- Run `just validate-strict data/normalized_yaml/bacterial/TOGO_M1268_Chloroflexus_Medium.yaml`.
- Run `just merge-recipes` and `just verify-merges` to prove the generated
  record is refreshed from the repaired normalized owner.
- Re-open the regenerated record and compare the five solution additions, water
  scoping, Trace vitamins arithmetic, JCM Medium 310 cross-reference, and pH
  adjustment against the TOGO JSON and JCM 1183 page.
- Compare repaired M1268 with
  `data/normalized_yaml/bacterial/chloroflexus_medium.yaml`, which cites the
  same JCM GRMD 1183 source, and then decide whether those records should be
  exact source duplicates.

## Additional Notes

- None found.
