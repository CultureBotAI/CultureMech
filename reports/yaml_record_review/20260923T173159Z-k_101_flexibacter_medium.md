# YAML Record Review: k_101_flexibacter_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/k_101_flexibacter_medium.yaml
- Started UTC: 2026-09-23T17:31:21Z
- Finished UTC: 2026-09-23T17:32:00Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Path | `data/merge_yaml/merged/k_101_flexibacter_medium.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:009160` |
| Label | `k_101_flexibacter_medium` |
| Original label | `K-101 Flexibacter medium` |
| Source identity | `TOGO:M2593`, ATCC medium 284 |
| Category | `bacterial` |
| Generated from | `data/normalized_yaml/bacterial/k_101_flexibacter_medium.yaml` by `merge_recipes.py` |

An ignored-inclusive exact search for `CultureMech:009160`, `TOGO:M2593`,
`TOGO_M2593_K_101_Flexibacter_medium`, `K-101 Flexibacter`, and the ATCC PDF
hash `8FF72E559CC4471D97C7CF6AAD2E86CE` across `data/normalized_yaml`,
`data/merge_yaml/merged`, `data/import_tracking`, `history`, and
`data/culturemech_recipe_catalog.tsv` found the one maintained owner at
`data/normalized_yaml/bacterial/k_101_flexibacter_medium.yaml`.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/k_101_flexibacter_medium.yaml` | Passed; `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/k_101_flexibacter_medium.yaml --out /private/tmp/k_101_flexibacter_medium.strict.tsv --workers 1 --quiet` | Passed; 0 ERROR rows and a header-only TSV. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/k_101_flexibacter_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks were available because the record has no structured `references`. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/k_101_flexibacter_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: the documented history validator targets standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists in merged YAML. |

## Identity and Grounding

TOGO M2593 and the live ATCC PDF agree that the source is ATCC medium 284,
`K-101 Flexibacter medium`. The bacterial category and `SOLID_AGAR` physical
state are appropriate because the source recipe is a bacterial agar medium.

The root ingredients mix two source scopes. ATCC lists `Trace Elements` as a
1 ml stock-solution addition in the main recipe, then defines a separate Trace
Element Solution per 1 L. The generated YAML also has a `solutions` entry for
Trace Elements, but the stock constituents are present as root medium
ingredients too.

## Evidence

The main ATCC K-101 recipe contains 0.1 g MgSO4.7H2O, 0.1 g KNO3, 0.1 g CaCl2,
0.1 g sodium glycerophosphate, 1 ml Trace Elements, 1 g Tris buffer, 1 mg
thiamine HCl, 1 g Casamino acids, 1 g glucose, 1 microgram vitamin B12, 10 g
agar, and 1 L distilled water. It then says to adjust pH to 7.5 and autoclave
at 121 C for 15 minutes.

The generated record preserves the named main ingredients, but it has three
large amount/unit errors:

- `Distilled water` is `2 G_PER_L`, an August generated artifact of merging
  the main-recipe water row with the trace-solution water row. The maintained
  owner was later collapsed back to `1 G_PER_L`, but the generated output was
  not regenerated and water should be `1 L` in the main recipe.
- `Thiamine . HCl` is `1 G_PER_L`, while ATCC and TOGO state 1 mg.
- `Vitamin B12` is `1 G_PER_L`, while ATCC and TOGO state 1 microgram.

The Trace Element Solution contains H3BO3 2.85 g/L, MnCl2.4H2O 1.8 g/L,
FeSO4 1.36 g/L, sodium tartrate 1.77 g/L, CuCl2.2H2O 26.9 mg/L, ZnCl2
20.8 mg/L, CoCl2.6H2O 40.4 mg/L, Na2MoO4.2H2O 25.2 mg/L, and water to 1 L.
Those stock constituents should not be direct final-medium ingredients, and
the four milligram rows are 1000-fold too high in the generated `G_PER_L`
representation.

## Completeness

The generated record is missing the source pH 7.5 adjustment and the 121 C for
15 minutes autoclave step. Its `solutions` entry for Trace Elements also has a
default `1 G_PER_L` concentration and `Unknown solution` name instead of the
source-stated 1 ml addition of the Trace Element Solution.

No target organisms or incubation conditions are asserted. Those omissions are
acceptable for the inspected TOGO and ATCC formulation sources.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The Trace Element Solution was flattened into final-medium ingredients. | ATCC and TOGO add 1 ml `Trace Elements` to the main recipe and define the stock separately; the generated record stores every trace stock component as a root ingredient. | `data/normalized_yaml/bacterial/k_101_flexibacter_medium.yaml` |
| Major | Several micro- or milligram rows are inflated to grams per liter. | ATCC states 1 mg thiamine HCl, 1 microgram vitamin B12, and four Trace Element Solution rows in mg/L; the generated rows are all `G_PER_L`. | `data/normalized_yaml/bacterial/k_101_flexibacter_medium.yaml` |
| Major | Trace Elements itself has a default concentration and placeholder name. | The source adds 1 ml Trace Elements; the generated `solutions` entry stores `1 G_PER_L` and `Unknown solution`. | `data/normalized_yaml/bacterial/k_101_flexibacter_medium.yaml` |
| Major | pH and sterilization instructions are absent. | TOGO and ATCC say to adjust to pH 7.5 and autoclave at 121 C for 15 minutes. | `data/normalized_yaml/bacterial/k_101_flexibacter_medium.yaml` |
| Major | Distilled water was merged across parent and stock scopes in the generated output. | The August generated file has `2 G_PER_L` with a duplicate-merge note, reflecting one main-recipe water row plus one Trace Element Solution water row. | Already partly fixed in `data/normalized_yaml/bacterial/k_101_flexibacter_medium.yaml`; regenerate after the remaining scope fixes |
| Minor | Source provenance is free text. | The record keeps TOGO M2593 and the ATCC PDF URL in `media_term`/`notes` but has no structured `sources` or `references`. | `data/normalized_yaml/bacterial/k_101_flexibacter_medium.yaml` |

## Recommended Edits

- Move H3BO3, MnCl2.4H2O, FeSO4, sodium tartrate, CuCl2.2H2O, ZnCl2,
  CoCl2.6H2O, Na2MoO4.2H2O, and the second distilled-water row into the
  Trace Element Solution scope.
- Change the Trace Elements solution addition to 1 ml and remove the generated
  `Unknown solution` / `1 G_PER_L` placeholder.
- Correct thiamine HCl to 1 mg and vitamin B12 to 1 microgram in the 1 L main
  medium.
- Represent main-recipe distilled water as 1 L rather than `G_PER_L`.
- Add preparation steps for pH 7.5 adjustment and autoclaving at 121 C for
  15 minutes.
- Add structured TOGO M2593 and ATCC medium 284 source references.
- Regenerate `data/merge_yaml/merged/` after the normalized owner is corrected.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the corrected
  normalized K-101 record and regenerated merge.
- Run `just verify-merges` and `just audit-merge-freshness`.
- Manually compare the regenerated output against TOGO M2593 and the ATCC
  medium 284 PDF, checking that root ingredients and Trace Element Solution
  constituents remain separated.

## Additional Notes

None found.
