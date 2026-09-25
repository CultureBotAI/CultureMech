# YAML Record Review: Chloroflexus medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/chloroflexus_medium__cb6e8339.yaml
- Started UTC: 2026-09-22T07:11:31Z
- Finished UTC: 2026-09-22T07:13:20Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/chloroflexus_medium__cb6e8339.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:009610` |
| Name | `chloroflexus_medium` |
| Original name | `Chloroflexus medium` |
| Media term | `TOGO:M3142` / `Chloroflexus medium` |
| Source | TOGO Medium M3142, sourced to ATCC Medium 920 |
| Generated status | Single-source derived merge generated from `data/normalized_yaml/bacterial/TOGO_M3142_Chloroflexus_medium.yaml` |

This is a generated one-record merge. Future scientific corrections belong in
`data/normalized_yaml/bacterial/TOGO_M3142_Chloroflexus_medium.yaml` or in the
TOGO import and solution migration code that produced its current flattened
shape.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/chloroflexus_medium__cb6e8339.yaml` | Passed with no issues reported. |
| Strict closed-schema validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/chloroflexus_medium__cb6e8339.yaml --out /private/tmp/chloroflexus_medium__cb6e8339.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/chloroflexus_medium__cb6e8339.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated with 0 reference checks. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/chloroflexus_medium__cb6e8339.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the validator emitted the known `eutils` / `pkg_resources` deprecation warning. |
| Embedded history | `just validate-history` | Not checked: that recipe validates standalone `history/*.yaml` records against `HistoryRecord`, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

I used the offline `uv` validator invocations above instead of the `just`
validator wrappers because the local project lock currently tries to build
`llvmlite==0.46.0` under Python 3.13 and fails inside setuptools before the
CultureMech validators run.

## Identity and Grounding

- The CultureMech ID and TOGO term consistently identify TOGO Medium M3142.
- TOGO M3142 lists the ATCC Medium 920 PDF as its source, and that PDF is titled
  "ATCC medium: 920 Chloroflexus medium".
- An ignored-independent `rg --no-ignore --hidden` search for
  `CultureMech:009610`, `TOGO_M3142`, `M3142`, `ATCC.*920`,
  `atcc-medium-920`, and `cb6e8339` across `data/normalized_yaml` and
  `data/merge_yaml/merged` found only the M3142 normalized owner and this
  generated target for the ATCC 920 identity.

## Evidence

I inspected the TOGO M3142 JSON and the ATCC Medium 920 PDF. They support the
source identity and most main-solution ingredient names, but several rows are
stock components or stale generated values:

- The ATCC main solution contains nitrilotriacetic acid `0.1 g`, CaSO4 . 2H2O
  `0.06 g`, MgSO4 . 7H2O `0.10 g`, NaCl `0.008 g`, KNO3 `0.103 g`, NaNO3
  `0.689 g`, Na2HPO4 `0.111 g`, NH4Cl `0.2 g`, yeast extract `0.5 g`,
  glycyl-glycine `0.5 g`, and 1 L distilled water. Those direct amounts are
  supported as gram-per-liter rows.
- ATCC adds `1.0 ml` Micronutrient Solution and `1.0 ml` FeCl3 Solution to the
  main medium. The reviewed file keeps both as `Unknown solution` stubs with
  `G_PER_L` units, and it also flattens the FeCl3 and micronutrient stock
  components into direct top-level ingredients.
- The generated file is stale relative to its normalized owner. The reviewed
  August 6 merge still has `Distilled water` at `3.0 G_PER_L` with
  `Merged 3 duplicates: 1.0, 1.0, 1.0`; the normalized owner has the September 2
  `repair_merged_duplicates.py` event and a repaired `1.0 G_PER_L` water row.
- The Micronutrient Solution reference is chemically wrong. ATCC Medium 920
  defines H2SO4, MnSO4 . 7H2O, ZnSO4 . 7H2O, H3BO3, CuSO4 . 2H2O,
  Na2MoO4 . 2H2O, CoCl2 . 6H2O, and water; `mediadive.solution:6236` includes
  a different stock with Co(NO3)2 x 6 H2O, CuSO4 x 5 H2O, FeSO4 x 7 H2O, and
  Na2-EDTA.
- ATCC instructs the curator to adjust pH to 8.2-8.4, add 0.5 g sodium sulfide,
  readjust to pH 8.2-8.4, and filter-sterilize broth. The record has no
  `preparation_steps`.

## Completeness

- FeCl3 Solution has an empty `composition` array even though ATCC defines
  `0.2905 g` FeCl3 in 1 L distilled water.
- Micronutrient Solution should be a local stock with the ATCC composition, not
  a pointer to unrelated MediaDive solution 6236.
- The ATCC pH and broth/solid-medium preparation branch is missing. The current
  record declares `physical_state: LIQUID`, so the broth filter-sterilization
  path should at least be represented; the 15 g agar solid-medium option can be
  a note or variant candidate.
- Empty `target_organisms` and `growth_metrics` slots are not defects in this
  source-formulation record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The generated record is stale relative to the repaired normalized owner. | `data/merge_yaml/merged/chloroflexus_medium__cb6e8339.yaml` still sums three identical water rows to `3.0 G_PER_L`; `data/normalized_yaml/bacterial/TOGO_M3142_Chloroflexus_medium.yaml` has a 2026-09-02 repair event and the corrected `1.0 G_PER_L` value. | Regenerate `data/merge_yaml/merged/` after the source record is otherwise repaired. |
| major | Micronutrient Solution is linked to the wrong external solution and its ATCC components are flattened as final medium ingredients. | ATCC 920's micronutrient stock contains H2SO4, MnSO4 . 7H2O, ZnSO4 . 7H2O, H3BO3, CuSO4 . 2H2O, Na2MoO4 . 2H2O, and CoCl2 . 6H2O. The record points to `mediadive.solution:6236`, which has a different chemical set, while the ATCC stock components are also direct top-level ingredients. | Replace the `Micronutrient Solution` stub in `data/normalized_yaml/bacterial/TOGO_M3142_Chloroflexus_medium.yaml` with the ATCC 920 stock composition. |
| major | FeCl3 Solution is an empty stub and duplicated as a top-level ingredient. | ATCC defines FeCl3 Solution as 0.2905 g FeCl3 in 1 L water and adds 1 ml of that stock; the YAML has a `FeCl3 Solution` with `composition: []` and a direct `FeCl3` row. | Nest FeCl3 under `FeCl3 Solution` in the normalized M3142 owner. |
| major | Source pH and sterilization instructions are absent. | ATCC 920 gives pH 8.2-8.4 adjustment, sodium sulfide addition and readjustment, and filter sterilization for broth; the record has no `preparation_steps`. | Add ATCC-supported preparation steps to the normalized M3142 owner. |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/` after normalized repair so the reviewed
   file picks up the September 2 water-row correction.
2. Replace the unrelated `mediadive.solution:6236` Micronutrient Solution link
   with an embedded ATCC Medium 920 stock: H2SO4 (concentrated) 0.5 ml, MnSO4 .
   7H2O 2.28 g, ZnSO4 . 7H2O 0.50 g, H3BO3 0.50 g, CuSO4 . 2H2O 0.025 g,
   Na2MoO4 . 2H2O 0.025 g, CoCl2 . 6H2O 0.045 g, and 1 L distilled water.
3. Model `FeCl3 Solution` as 0.2905 g FeCl3 in 1 L distilled water and add it to
   the main medium at 1.0 ml.
4. Remove stock-only FeCl3 and micronutrient rows from the top-level final
   ingredients list.
5. Add preparation steps for pH 8.2-8.4 adjustment, sodium sulfide addition,
   pH readjustment, broth filter sterilization, and the optional 15 g agar
   solid-medium branch if a solid variant is represented later.

## Follow-up Checks

- Run `just validate-strict data/normalized_yaml/bacterial/TOGO_M3142_Chloroflexus_medium.yaml`.
- Run `just validate-terms data/normalized_yaml/bacterial/TOGO_M3142_Chloroflexus_medium.yaml`
  after replacing the micronutrient stock and refreshing hydrate-specific
  groundings for its metals.
- Run `just merge-recipes` and `just verify-merges` to prove the generated
  record is refreshed from the repaired normalized owner.
- Re-open the regenerated M3142 record and compare its two stock solutions,
  water scoping, pH range, sulfide addition, and broth/agar branch against the
  ATCC Medium 920 PDF.

## Additional Notes

- The current top-level direct salts are already normalized to the 1 L ATCC
  recipe volume; the important arithmetic issue is the stock rows, not the
  main-solution rows.
