# YAML Record Review: PYG Medium (J), Modified

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/pyg_medium_j_modified.yaml
- Started UTC: 2026-09-24T22:51:20Z
- Finished UTC: 2026-09-24T22:52:31Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:007835 |
| Name | pyg_medium_j_modified |
| Original name | PYG Medium (J), Modified |
| Category | bacterial |
| Generated file | data/merge_yaml/merged/pyg_medium_j_modified.yaml |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M1300_PYG_Medium_J_Modified.yaml |
| Merge source | TOGO_M1300_PYG_Medium_J_Modified |
| Source grounding | TOGO:M1300, JCM_M1213 |

The reviewed file is a generated merge product. Future corrections should be
made in the maintained TOGO normalization and in the TOGO solution/cross-medium
import logic that currently leaves liquid stock aliquots empty or flattened.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/pyg_medium_j_modified.yaml` | Passed with `No issues found`. |
| Strict CultureMech validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/pyg_medium_j_modified.yaml --out /private/tmp/pyg_medium_j_modified.strict.tsv --workers 1 --quiet` | Passed with 0 strict errors; `/private/tmp/pyg_medium_j_modified.strict.tsv` contained 1 line including the header. |
| LinkML references | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/pyg_medium_j_modified.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file was validated and no reference checks were emitted. |
| LinkML terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/pyg_medium_j_modified.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; only the known `eutils`/`pkg_resources` deprecation warning was printed. |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` target validates standalone `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

- `data/merge_yaml/merged/pyg_medium_j_modified.yaml` is the generated TOGO
  M1300 branch for CultureMech:007835 and JCM_M1213
  `PYG Medium (J), Modified`.
- The TOGO M1300 API reports the same label, original medium `JCM_M1213`, pH
  7.2, and the same JCM GRMD 1213 URL embedded in the YAML.
- The live JCM 1213 page confirms the PYG MEDIUM (J), MODIFIED identity, pH
  7.2, final medium recipe, local Vitamin K1 recipe, and the separate solution
  additions that are added while gassing.
- Exact ignored-file search across `data/**/*.yaml` for `TOGO:M1300`, TOGO
  M1300 URLs, `JCM_M1213`, `GRMD=1213`, and
  `TOGO_M1300_PYG_Medium_J_Modified` found the reviewed TOGO branch, its
  maintained owner, a metal-analysis index entry, and the equivalent direct JCM
  branch.
- Exact ignored-file search across `data/**/*.yaml` for `TOGO:M258`, TOGO M258
  URLs, and JCM 258 found the local TOGO M258 owner that corresponds to the
  clarified-rumen-fluid cross-reference.

## Evidence

- JCM 1213 and TOGO M1300 both define a base containing 5 g Trypticase peptone,
  5 g peptone, 10 g yeast extract, 5 g beef extract, 5 g glucose, 2 g KH2PO4,
  1 ml Tween 80, 1 mg resazurin, 40 ml salt solution from M695, and 890 ml
  distilled water.
- The same sources instruct curators to boil and cool the base under O2-free
  CO2, then add 50 ml clarified rumen fluid from M258, 10 ml 5%
  L-cysteine.HCl.H2O solution, 10 ml hemin solution from M470, and 0.2 ml
  Vitamin K1 solution, adjust to pH 7.2, distribute under N2, seal, and
  autoclave.
- The JCM 1213 and TOGO M1300 Vitamin K1 stock recipe dissolves 0.1 ml Vitamin
  K1 in 20 ml 95% ethanol, filter-sterilizes it, and stores it refrigerated in
  a brown bottle.
- The reviewed record preserves the TOGO M1300 identity and the main dry
  peptide/extract/glucose/KH2PO4 amounts.
- The reviewed record stores all five solution additions as empty `solutions`
  rows using `G_PER_L` values copied from source ml aliquots: 40, 10, 50, 10,
  and 0.2.
- The reviewed record stores Vitamin K1 stock ethanol and Vitamin K1 rows as
  top-level final-medium ingredients.
- The reviewed record stores 1 mg resazurin and 1 ml Tween 80 as 1 `G_PER_L`
  rows and stores CO2 and N2 only as variable-concentration ingredients.

## Completeness

- Empty optional fields beyond general microbial cultivation are not defects.
- The salt, hemin, clarified rumen fluid, and Vitamin K1 solution boundaries
  are all unresolved despite source-provided cross-references or local stock
  composition.
- `ph_value` is missing even though both TOGO and JCM give pH 7.2.
- The O2-free CO2 boiling/cooling step, the while-gassing additions, the N2
  dispensing/sealing/autoclave step, and the Vitamin K1 filter-sterilization
  and storage instructions are missing.
- The equivalent direct JCM branch remains separate and carries a different
  stock-flattened representation of the same JCM 1213 recipe.
- Exact ignored-file searches included ignored files before assessing exact
  TOGO/JCM/M258 duplicate and reference scope.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Five liquid solution additions use the wrong unit family. | JCM 1213 adds 40 ml salt solution, 10 ml cysteine solution, 50 ml clarified rumen fluid, 10 ml hemin solution, and 0.2 ml Vitamin K1 solution; the YAML stores those empty solution rows as 40, 10, 50, 10, and 0.2 `G_PER_L`. | data/normalized_yaml/bacterial/TOGO_M1300_PYG_Medium_J_Modified.yaml; solution migration |
| Major | Referenced M695, M258, and M470 solution details are unresolved. | The source points the salt solution to M695, clarified rumen fluid to M258, and hemin solution to M470. The YAML stores all three as empty compositions. | data/normalized_yaml/bacterial/TOGO_M1300_PYG_Medium_J_Modified.yaml; TOGO cross-medium import |
| Major | The local Vitamin K1 stock was flattened into final-medium ingredients. | JCM 1213 defines 0.2 ml of a Vitamin K1 solution prepared from 0.1 ml Vitamin K1 in 20 ml 95% ethanol; the reviewed YAML stores ethanol 20 `G_PER_L`, Vitamin K1 0.1 `G_PER_L`, and an empty 0.2 `G_PER_L` stock row at top level. | data/normalized_yaml/bacterial/TOGO_M1300_PYG_Medium_J_Modified.yaml; solution migration |
| Major | Milligram and milliliter main-medium rows were stored as grams per liter. | JCM 1213 uses 1 mg resazurin and 1 ml Tween 80; the YAML stores both rows as 1 `G_PER_L`. | data/normalized_yaml/bacterial/TOGO_M1300_PYG_Medium_J_Modified.yaml |
| Major | pH and all anaerobic preparation instructions are absent. | The source gives pH 7.2, O2-free CO2 boiling and cooling, while-gassing solution additions, N2 dispensing, sealing, autoclaving, and Vitamin K1 filter-sterilization/storage instructions; the reviewed YAML has no `ph_value` or `preparation_steps`. | data/normalized_yaml/bacterial/TOGO_M1300_PYG_Medium_J_Modified.yaml |
| Minor | CO2 and N2 atmospheres are not modeled as preparation context. | The sources use CO2 and N2 as gassing atmospheres, but the YAML only stores them as variable-concentration gas ingredients. | data/normalized_yaml/bacterial/TOGO_M1300_PYG_Medium_J_Modified.yaml |
| Minor | The equivalent direct JCM branch remains a separate generated record. | Exact ignored-file search found `data/merge_yaml/merged/pyg_medium_j_modified__b61bc612.yaml` for the same JCM 1213 recipe. | data/normalized_yaml/bacterial/TOGO_M1300_PYG_Medium_J_Modified.yaml; merge_recipes.py |

## Recommended Edits

1. Recurate `data/normalized_yaml/bacterial/TOGO_M1300_PYG_Medium_J_Modified.yaml`
   so salt, cysteine, rumen-fluid, hemin, and Vitamin K1 additions are modeled
   as liquid aliquots rather than gram-per-liter solution rows.
2. Resolve the M695, M258, and M470 cross-references or link them explicitly so
   their formulas are not represented as empty solutions.
3. Scope 20 ml 95% ethanol and 0.1 ml Vitamin K1 under the 0.2 ml Vitamin K1
   stock addition.
4. Store 1 mg resazurin and 1 ml Tween 80 in source units or correct inline
   equivalents.
5. Add pH 7.2 and preparation steps for O2-free CO2 boiling/cooling,
   while-gassing additions, N2 dispensing, sealing, autoclaving, and Vitamin K1
   filter sterilization/storage.
6. Move CO2 and N2 out of ordinary variable ingredients into explicit
   preparation or gas-atmosphere representations supported by the schema.
7. Regenerate the merged output and verify this TOGO M1300 branch converges
   with a corrected direct JCM GRMD 1213 branch.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation on
  `data/merge_yaml/merged/pyg_medium_j_modified.yaml`.
- Manually confirm the regenerated record keeps every solution aliquot scoped,
  keeps source milligram/milliliter rows in the correct unit family, and
  includes pH 7.2 plus anaerobic preparation.
- Manually compare the regenerated TOGO M1300 branch against
  `data/merge_yaml/merged/pyg_medium_j_modified__b61bc612.yaml` after the
  direct branch is fixed.
- Run exact ignored-file searches for `TOGO:M1300`, `JCM_M1213`, `GRMD=1213`,
  and `TOGO:M258` to verify no stale duplicate or unresolved M258 reference
  remains after regeneration.

## Additional Notes

- The local TOGO M1300 and M258 fetches initially failed with sandbox DNS
  errors. The official URLs were then fetched successfully with the approved
  escalated `curl -L` rule.
