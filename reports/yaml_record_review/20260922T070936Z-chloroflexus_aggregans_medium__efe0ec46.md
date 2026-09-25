# YAML Record Review: Chloroflexus Aggregans Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/chloroflexus_aggregans_medium__efe0ec46.yaml
- Started UTC: 2026-09-22T07:08:02Z
- Finished UTC: 2026-09-22T07:09:37Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/chloroflexus_aggregans_medium__efe0ec46.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:009544` |
| Name | `chloroflexus_aggregans_medium` |
| Original name | `Chloroflexus Aggregans Medium` |
| Media term | `TOGO:M3032` / `Chloroflexus Aggregans Medium` |
| Source | TOGO Medium M3032, sourced to JCM `JCM_M1398` |
| Generated status | Single-source derived merge generated from `data/normalized_yaml/bacterial/TOGO_M3032_Chloroflexus_Aggregans_Medium.yaml` |

This is a generated one-record merge. Future scientific corrections belong in
`data/normalized_yaml/bacterial/TOGO_M3032_Chloroflexus_Aggregans_Medium.yaml`
or in the TOGO import and solution migration code that produced its current
flattened shape.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/chloroflexus_aggregans_medium__efe0ec46.yaml` | Passed with no issues reported. |
| Strict closed-schema validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/chloroflexus_aggregans_medium__efe0ec46.yaml --out /private/tmp/chloroflexus_aggregans_medium__efe0ec46.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/chloroflexus_aggregans_medium__efe0ec46.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated with 0 reference checks. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/chloroflexus_aggregans_medium__efe0ec46.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the validator emitted the known `eutils` / `pkg_resources` deprecation warning. |
| Embedded history | `just validate-history` | Not checked: that recipe validates standalone `history/*.yaml` records against `HistoryRecord`, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

I used the offline `uv` validator invocations above instead of the `just`
validator wrappers because the local project lock currently tries to build
`llvmlite==0.46.0` under Python 3.13 and fails inside setuptools before the
CultureMech validators run.

## Identity and Grounding

- The CultureMech ID, TOGO term, and source metadata consistently identify TOGO
  Medium M3032 from JCM `JCM_M1398`, exposed by JCM as medium 1398.
- The JCM page title for medium 1398 is CHLOROFLEXUS AGGREGANS MEDIUM and its
  formula agrees with the TOGO M3032 component tree.
- An ignored-independent `rg --no-ignore --hidden` search for
  `CultureMech:009544`, `TOGO_M3032`, `M3032`, `JCM_M1398`, `GRMD=1398`, and
  the `efe0ec46` merge fingerprint prefix across `data/normalized_yaml` and
  `data/merge_yaml/merged` found only the M3032 normalized owner and this
  generated record for the M3032/JCM 1398 identity.

## Evidence

I inspected the TOGO M3032 JSON and the JCM GRMD 1398 page. They support the
source identity and the simple main-solution rows, but not the record's
solution flattening or amount conversions:

- JCM lists 1 g each yeast extract and glycyl-glycine; 0.10 g each
  Na2HPO4 x 2 H2O, MgSO4 x 7 H2O, KNO3, and NaCl; 0.50 g NaNO3; and 0.05 g
  CaCl2 x 2 H2O in 1050 ml distilled water. The record stores those gram
  amounts as `G_PER_L`, so each main-solute concentration is slightly high
  rather than normalized to the 1050 ml preparation volume.
- JCM adds `5 ml` Fe(III) citrate solution and `1 ml` SL-6 trace element
  solution to that main solution. The YAML preserves both only as empty
  top-level solution stubs with `G_PER_L` units.
- JCM prepares neutralized sulfide solution from 3 g Na2S x 9 H2O in 100 ml
  water, then injects `1.0 ml` of that stock after autoclaving. The record
  stores Na2S x 9 H2O as a direct `3 G_PER_L` ingredient, although the source
  value is a 100 ml stock amount, and also has an empty solution stub at
  `1 G_PER_L`.
- JCM prepares Vitamin solution CA from milligram additions to 100 ml water and
  injects `0.1 ml` sterile stock after autoclaving. The record stores the raw
  milligram numbers as direct `G_PER_L` values: for example, Biotin `5`,
  p-Aminobenzoic acid `50`, Vitamin B12 `1`, Nicotinic acid `100`, and Na3-EDTA
  `200`.
- Three separate source water volumes, `1050 ml`, `100 ml`, and `100 ml`, were
  collapsed into one `1250.0 G_PER_L` Distilled water row.

## Completeness

- All four solutions are structurally incomplete. Fe(III) citrate solution,
  SL-6 trace element solution, and Neutralized sulfide solution have empty
  `composition` arrays, and Vitamin solution CA has only a note pointing to a
  shared MediaDive solution instead of an embedded or resolvable local
  composition reference.
- The preparation protocol from JCM 1398 is absent. The record does not encode
  pH 8.2 adjustment, nitrogen sparging, 90 ml bottle fill, 121 C autoclaving,
  post-autoclave injection of sulfide and Vitamin solution CA, sulfide stock
  neutralization to about pH 7.0 with sterile 2 M H2SO4, or Vitamin solution CA
  adjustment to pH 7.5 and filter sterilization.
- Empty `target_organisms` and `growth_metrics` slots are not defects in this
  source-formulation record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Four JCM solution additions were flattened into duplicate or empty top-level structures. | Fe(III) citrate, SL-6, neutralized sulfide, and Vitamin solution CA are source-level solutions. The YAML has empty stubs for three of them, a Vitamin solution note, and direct ingredient rows for the stock members. | Rebuild `data/normalized_yaml/bacterial/TOGO_M3032_Chloroflexus_Aggregans_Medium.yaml` from the TOGO/JCM nested component tree, or fix the TOGO importer / solution migrator. |
| major | Stock amount arithmetic is wrong for water, sulfide, and Vitamin solution CA. | JCM's three 100/1050 ml water volumes were summed to `1250.0 G_PER_L`; 3 g Na2S x 9 H2O in 100 ml became a direct `3 G_PER_L` ingredient; Vitamin solution CA milligram values became `G_PER_L` values 100-fold too high even as stock concentrations. | Preserve source units in the M3032 normalized owner and convert only within the scope of each 100 ml or 1050 ml stock. |
| major | JCM preparation and incubation handling is missing. | The source describes pH adjustment, nitrogen handling, autoclaving, post-autoclave injection of neutralized sulfide and sterile Vitamin solution CA, and stock-specific pH/sterilization steps; the record has no `preparation_steps`. | Add source-supported preparation steps to the M3032 normalized owner if it remains a standalone recipe. |
| minor | Two ingredient groundings do not match exact source chemicals. | `Na2HPO4.2H2O` is grounded to anhydrous disodium hydrogen phosphate (`CHEBI:34683`) despite the dihydrate label; `Na3-EDTA` is grounded to disodium EDTA (`CHEBI:64734`) instead of trisodium EDTA (`CHEBI:63125`). | Re-ground those ingredients after the stock topology is corrected. |

## Recommended Edits

1. Rebuild the M3032 normalized record with nested Fe(III) citrate solution,
   SL-6 trace element solution, Neutralized sulfide solution, and Vitamin
   solution CA. Do not also keep the stock members as direct top-level
   final-medium ingredients.
2. Correct all amount scopes: grams in the 1050 ml main solution should be
   represented as source amounts or converted with the 1050 ml denominator;
   Vitamin solution CA milligram rows should be divided by 0.1 L to get stock
   grams per liter; the `0.1 ml` vitamin addition should remain distinct from
   DSMZ 87a's `1 ml/l` addition.
3. Preserve the JCM cross-reference from SL-6 to JCM Medium 167 and inspect
   that source before filling its composition.
4. Add JCM 1398 preparation details, including nitrogen sparging, autoclaving,
   post-autoclave stock injection, sulfide neutralization, and Vitamin solution
   CA filter sterilization.
5. Re-ground Na2HPO4 x 2 H2O and Na3-EDTA to exact hydrated/salt forms.
6. Regenerate `data/merge_yaml/merged/chloroflexus_aggregans_medium__efe0ec46.yaml`
   after the normalized M3032 owner is repaired.

## Follow-up Checks

- Run `just validate-strict data/normalized_yaml/bacterial/TOGO_M3032_Chloroflexus_Aggregans_Medium.yaml`.
- Run `just validate-terms data/normalized_yaml/bacterial/TOGO_M3032_Chloroflexus_Aggregans_Medium.yaml`
  after the Na2HPO4 x 2 H2O and Na3-EDTA grounding corrections.
- Run `just merge-recipes` and `just verify-merges` to prove the hash-suffixed
  generated record was refreshed from the normalized owner.
- Re-open the regenerated M3032 record and compare the four solution additions,
  main-volume arithmetic, Vitamin solution CA `0.1 ml` addition, and JCM 1398
  preparation text against the TOGO JSON and JCM page.

## Additional Notes

- This M3032 record is intentionally not the same as TOGO M2173 / DSMZ 87a:
  M3032 injects `0.1 ml` sterile Vitamin solution CA per bottle, while DSMZ 87a
  adds Vitamin solution CA at `1 ml/litre`.
