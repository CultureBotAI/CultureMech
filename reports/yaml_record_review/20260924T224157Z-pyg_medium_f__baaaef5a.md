# YAML Record Review: PYG MEDIUM (F)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/pyg_medium_f__baaaef5a.yaml
- Started UTC: 2026-09-24T22:41:57Z
- Finished UTC: 2026-09-24T22:43:03Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:003019 |
| Name | pyg_medium_f |
| Original name | PYG MEDIUM (F) |
| Category | bacterial |
| Generated file | data/merge_yaml/merged/pyg_medium_f__baaaef5a.yaml |
| Maintained owner | data/normalized_yaml/bacterial/pyg_medium_f.yaml |
| Merge source | pyg_medium_f |
| Source grounding | JCM 674 |

The reviewed file is a generated merge product. Future corrections should be
made in the maintained direct JCM normalization that flattened JCM 674 stock
solutions into final-medium concentration rows.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/pyg_medium_f__baaaef5a.yaml` | Passed with `No issues found`. |
| Strict CultureMech validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/pyg_medium_f__baaaef5a.yaml --out /private/tmp/pyg_medium_f__baaaef5a.strict.tsv --workers 1 --quiet` | Passed with 0 strict errors; `/private/tmp/pyg_medium_f__baaaef5a.strict.tsv` contained 1 line including the header. |
| LinkML references | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/pyg_medium_f__baaaef5a.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file was validated and no reference checks were emitted. |
| LinkML terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/pyg_medium_f__baaaef5a.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; only the known `eutils`/`pkg_resources` deprecation warning was printed. |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` target validates standalone `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

- `data/merge_yaml/merged/pyg_medium_f__baaaef5a.yaml` is the generated direct
  JCM branch for CultureMech:003019 and JCM 674 `PYG MEDIUM (F)`.
- The live JCM 674 page confirms the PYG MEDIUM (F) identity, pH 7.3, final
  medium recipe, and separate S I and S II solution recipes.
- The TOGO M693 API is grounded to the same original JCM_M674 page and mirrors
  the same stock solution boundaries.
- Exact ignored-file search across `data/**/*.yaml` for `TOGO:M693`, TOGO M693
  URLs, `JCM_M674`, `GRMD=674`, and `TOGO_M693_PYG_Medium_F` found this direct
  JCM branch plus the equivalent TOGO M693 branch.

## Evidence

- JCM 674 defines a final medium containing 75 ml S I solution, 75 ml S II
  solution, 10 g Trypticase peptone, 5 g yeast extract, 10 g glucose, 1 ml
  0.1% sodium resazurin solution, 2.5 ml 8% Na2CO3 solution, 0.3 g
  L-cysteine.HCl.H2O, 850 ml distilled water, and pH 7.3.
- The same JCM page separately defines S I solution as 0.6 g K2HPO4 in 100 ml
  distilled water, and S II solution as 0.6 g KH2PO4, 1.2 g (NH4)2SO4, 1.2 g
  NaCl, 0.12 g MgSO4.7H2O, and 0.12 g CaCl2.2H2O in 100 ml distilled water.
- The reviewed record preserves the JCM 674 identity, pH 7.3, and a terse
  adjust-pH preparation step.
- The reviewed record converts the final dry masses to fractional
  gram-per-liter values and drops the explicit 75 ml S I, 75 ml S II, 1 ml
  sodium resazurin solution, and 2.5 ml Na2CO3 solution aliquots.
- The reviewed record stores S I and S II stock formulas as final ingredient
  concentrations, such as 6 `G_PER_L` K2HPO4 and 12 `G_PER_L` NaCl.

## Completeness

- Empty optional fields beyond general microbial cultivation are not defects.
- The S I and S II stock boundaries are missing entirely.
- Both defined stock-solution aliquots are missing as solutions.
- Main, stock, and solution water rows are missing, even though JCM uses 850 ml
  final-medium water plus 100 ml water in each of S I and S II.
- The equivalent TOGO M693 branch remains separate and carries a different
  stock-flattened representation of the same JCM 674 recipe.
- Exact ignored-file search included ignored files before assessing exact
  TOGO/JCM duplicate scope.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The S I and S II stock recipes were flattened into final-medium concentrations. | JCM 674 defines K2HPO4 under S I and KH2PO4, (NH4)2SO4, NaCl, MgSO4.7H2O, and CaCl2.2H2O under S II. The reviewed YAML stores those stock concentrations as ordinary top-level ingredients and has no S I or S II solution rows. | data/normalized_yaml/bacterial/pyg_medium_f.yaml |
| Major | The two defined stock-solution aliquots were converted to the wrong chemicals and concentrations. | JCM 674 adds 1 ml of 0.1% sodium resazurin solution and 2.5 ml of 8% Na2CO3 solution, but the YAML stores 1 `G_PER_L` `Sodium resazurin` and 2.5 `G_PER_L` `Na2CO3` as if the milliliter aliquot values were dry final-medium masses. | data/normalized_yaml/bacterial/pyg_medium_f.yaml |
| Minor | Water rows are absent. | JCM 674 has 850 ml final-medium water, 100 ml S I stock water, and 100 ml S II stock water; the reviewed YAML has no water ingredient and no stock compositions for the stock water. | data/normalized_yaml/bacterial/pyg_medium_f.yaml |
| Minor | The equivalent TOGO M693 branch remains a separate generated record. | Exact ignored-file search found `data/merge_yaml/merged/pyg_medium_f.yaml` for the same JCM 674 recipe. | data/normalized_yaml/bacterial/pyg_medium_f.yaml; merge_recipes.py |

## Recommended Edits

1. Recurate `data/normalized_yaml/bacterial/pyg_medium_f.yaml` so S I and S II
   are represented as 75 ml stock aliquots with their internal 100 ml recipes
   scoped under `composition`.
2. Represent the 0.1% sodium resazurin and 8% Na2CO3 solution additions as
   liquid aliquots or inline stock equivalents instead of gram-per-liter rows.
3. Add the 850 ml main water, 100 ml S I stock water, and 100 ml S II stock
   water to the appropriate scopes.
4. Regenerate the merged output and verify this direct JCM 674 branch converges
   with a corrected TOGO M693 branch.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation on
  `data/merge_yaml/merged/pyg_medium_f__baaaef5a.yaml`.
- Manually confirm the regenerated record has explicit S I, S II, 0.1% sodium
  resazurin, and 8% Na2CO3 stock solution boundaries.
- Manually compare the regenerated direct JCM branch against
  `data/merge_yaml/merged/pyg_medium_f.yaml` after the TOGO M693 branch is
  fixed.
- Run an exact ignored-file search for `TOGO:M693`, `JCM_M674`, and `GRMD=674`
  to verify no stale duplicate remains after regeneration.

## Additional Notes

None found.
