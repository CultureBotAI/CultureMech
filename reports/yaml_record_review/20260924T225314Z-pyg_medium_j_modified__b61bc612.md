# YAML Record Review: PYG MEDIUM (J), MODIFIED

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/pyg_medium_j_modified__b61bc612.yaml
- Started UTC: 2026-09-24T22:53:14Z
- Finished UTC: 2026-09-24T22:53:47Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:002382 |
| Name | pyg_medium_j_modified |
| Original name | PYG MEDIUM (J), MODIFIED |
| Category | bacterial |
| Generated file | data/merge_yaml/merged/pyg_medium_j_modified__b61bc612.yaml |
| Maintained owner | data/normalized_yaml/bacterial/pyg_medium_j_modified.yaml |
| Merge source | pyg_medium_j_modified |
| Source grounding | JCM 1213 |

The reviewed file is a generated merge product. Future corrections should be
made in the maintained direct JCM normalization that flattened JCM 1213 stock
solutions into final-medium concentration rows.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/pyg_medium_j_modified__b61bc612.yaml` | Passed with `No issues found`. |
| Strict CultureMech validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/pyg_medium_j_modified__b61bc612.yaml --out /private/tmp/pyg_medium_j_modified__b61bc612.strict.tsv --workers 1 --quiet` | Passed with 0 strict errors; `/private/tmp/pyg_medium_j_modified__b61bc612.strict.tsv` contained 1 line including the header. |
| LinkML references | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/pyg_medium_j_modified__b61bc612.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file was validated and no reference checks were emitted. |
| LinkML terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/pyg_medium_j_modified__b61bc612.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; only the known `eutils`/`pkg_resources` deprecation warning was printed. |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` target validates standalone `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

- `data/merge_yaml/merged/pyg_medium_j_modified__b61bc612.yaml` is the
  generated direct JCM branch for CultureMech:002382 and JCM 1213
  `PYG MEDIUM (J), MODIFIED`.
- The live JCM 1213 page confirms the PYG MEDIUM (J), MODIFIED identity, pH
  7.2, final medium recipe, solution additions, local Vitamin K1 recipe, and
  anaerobic boiling, gassing, dispensing, and autoclaving steps.
- The TOGO M1300 API is grounded to the same original JCM_M1213 page and
  mirrors the same solution boundaries.
- Exact ignored-file search across `data/**/*.yaml` for `TOGO:M1300`, TOGO
  M1300 URLs, `JCM_M1213`, `GRMD=1213`, and
  `TOGO_M1300_PYG_Medium_J_Modified` found this direct JCM branch plus the
  equivalent TOGO M1300 branch.

## Evidence

- JCM 1213 defines a base containing 5 g Trypticase peptone, 5 g peptone,
  10 g yeast extract, 5 g beef extract, 5 g glucose, 2 g KH2PO4, 1 ml
  Tween 80, 1 mg resazurin, 40 ml salt solution from M695, and 890 ml
  distilled water.
- The source then adds 50 ml clarified rumen fluid from M258, 10 ml 5%
  L-cysteine.HCl.H2O solution, 10 ml hemin solution from M470, and 0.2 ml
  Vitamin K1 solution while gassing with O2-free CO2, and adjusts to pH 7.2.
- The JCM 1213 Vitamin K1 stock recipe dissolves 0.1 ml Vitamin K1 in 20 ml
  95% ethanol, filter-sterilizes it, and stores it refrigerated in a brown
  bottle.
- The reviewed record preserves the direct JCM 1213 identity, pH 7.2, and the
  main anaerobic preparation text.
- The reviewed record does not contain the 40 ml salt, 10 ml cysteine, 50 ml
  clarified rumen fluid, 10 ml hemin, or 0.2 ml Vitamin K1 solution aliquots.
- The reviewed record stores the M695 salt-stock formula and local Vitamin K1
  stock formula as ordinary top-level final-medium ingredients.

## Completeness

- Empty optional fields beyond general microbial cultivation are not defects.
- The salt-solution boundary is missing entirely.
- Cysteine, clarified rumen fluid, hemin, and Vitamin K1 are not modeled as
  liquid additions.
- The retained hemin preparation sentence is orphaned because no hemin solution
  row refers to it.
- The equivalent TOGO M1300 branch remains separate and carries a different
  empty-solution representation of the same JCM 1213 recipe.
- Exact ignored-file searches included ignored files before assessing exact
  TOGO/JCM duplicate scope.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Referenced salt, rumen-fluid, hemin, and Vitamin K1 additions are missing as solution rows. | JCM 1213 adds 40 ml salt solution, 50 ml clarified rumen fluid, 10 ml hemin solution, and 0.2 ml Vitamin K1 solution; the YAML has no corresponding solution or ingredient aliquot rows. | data/normalized_yaml/bacterial/pyg_medium_j_modified.yaml |
| Major | The local Vitamin K1 stock was flattened into final-medium ingredients. | JCM 1213 defines 0.2 ml of a Vitamin K1 solution prepared from 0.1 ml Vitamin K1 in 20 ml 95% ethanol; the reviewed YAML stores Vitamin K1 0.1 `G_PER_L` and Ethanol 950 `G_PER_L` at top level. | data/normalized_yaml/bacterial/pyg_medium_j_modified.yaml |
| Major | The M695 salt stock was flattened into final-medium concentrations. | JCM 1213 adds a 40 ml salt solution from the PYG G stock; the YAML stores the stock salts as top-level ingredients and has no salt solution row. | data/normalized_yaml/bacterial/pyg_medium_j_modified.yaml |
| Major | The 5% cysteine solution was converted to the wrong concentration. | JCM 1213 adds 10 ml of 5% L-cysteine.HCl.H2O solution; the YAML stores L-cysteine.HCl.H2O as 10 `G_PER_L`. | data/normalized_yaml/bacterial/pyg_medium_j_modified.yaml |
| Minor | Tween 80 has the wrong unit family. | JCM 1213 uses 1 ml Tween 80; the YAML stores `Tween 80` as 1 `G_PER_L`. | data/normalized_yaml/bacterial/pyg_medium_j_modified.yaml |
| Minor | Main and stock water rows are absent. | JCM 1213 has 890 ml main water and the referenced M695 stock has its own 1 L water row; the reviewed YAML has no water ingredient and no stock composition for the stock water. | data/normalized_yaml/bacterial/pyg_medium_j_modified.yaml |
| Minor | The equivalent TOGO M1300 branch remains a separate generated record. | Exact ignored-file search found `data/merge_yaml/merged/pyg_medium_j_modified.yaml` for the same JCM 1213 recipe. | data/normalized_yaml/bacterial/pyg_medium_j_modified.yaml; merge_recipes.py |

## Recommended Edits

1. Recurate `data/normalized_yaml/bacterial/pyg_medium_j_modified.yaml` so
   salt, cysteine, rumen-fluid, hemin, and Vitamin K1 additions are modeled as
   liquid aliquots rather than flattened gram-per-liter ingredients.
2. Resolve the M695, M258, and M470 cross-references or link them explicitly so
   their formulas are not represented by top-level ingredient rows.
3. Scope 20 ml 95% ethanol and 0.1 ml Vitamin K1 under the 0.2 ml Vitamin K1
   stock addition.
4. Store Tween 80 as 1 ml and restore 890 ml main water to the correct scope.
5. Regenerate the merged output and verify this direct JCM 1213 branch
   converges with a corrected TOGO M1300 branch.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation on
  `data/merge_yaml/merged/pyg_medium_j_modified__b61bc612.yaml`.
- Manually confirm the regenerated record has explicit salt, cysteine,
  rumen-fluid, hemin, and Vitamin K1 solution boundaries.
- Manually compare the regenerated direct JCM branch against
  `data/merge_yaml/merged/pyg_medium_j_modified.yaml` after the TOGO M1300
  branch is fixed.
- Run exact ignored-file searches for `TOGO:M1300`, `JCM_M1213`, `GRMD=1213`,
  and `TOGO:M258` to verify no stale duplicate or unresolved M258 reference
  remains after regeneration.

## Additional Notes

None found.
