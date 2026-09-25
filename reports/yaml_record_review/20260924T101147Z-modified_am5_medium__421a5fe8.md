# YAML Record Review: Modified AM5 Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_am5_medium__421a5fe8.yaml
- Started UTC: 2026-09-24T10:11:47Z
- Finished UTC: 2026-09-24T10:11:47Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Record | `data/merge_yaml/merged/modified_am5_medium__421a5fe8.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:003007` |
| Name | `modified_am5_medium` |
| Original name | `MODIFIED AM5 MEDIUM` |
| Category | `bacterial` |
| Medium source | MediaDive / JCM `J661`; JCM `GRMD=661` |
| Maintained owner | `data/normalized_yaml/bacterial/modified_am5_medium.yaml` |
| Generated status | Generated merge output from one normalized JCM record |

## Validation

| Check | Result |
| --- | --- |
| Open LinkML schema validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_am5_medium__421a5fe8.yaml` | Passed; exited 0 with "No issues found". |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/modified_am5_medium__421a5fe8.yaml --out /private/tmp/modified_am5_medium__421a5fe8.strict.tsv --workers 1 --quiet` | Passed; 0 strict errors were reported and `/private/tmp/modified_am5_medium__421a5fe8.strict.tsv` contained only the header line. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/modified_am5_medium__421a5fe8.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the focused run completed with 0 reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/modified_am5_medium__421a5fe8.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not inline `MediaRecipe.curation_history` entries in a merged YAML record. |

## Identity and Grounding

The record identity is coherent: `CultureMech:003007`, MediaDive `J661`, and JCM `GRMD=661` all identify MODIFIED AM5 MEDIUM.

An exact `find data/normalized_yaml -name 'modified_am5_medium.yaml'` search, which does not honor gitignore exclusions, found `data/normalized_yaml/bacterial/modified_am5_medium.yaml` as the generated record's maintained owner.

Most base-salt groundings preserve the source chemical forms, but `NiCl2 x 6 H2O` is grounded to `CHEBI:34887` with label `nickel dichloride`, which does not preserve the source hexahydrate form. The record also grounds `Fatty acid mixture (see Medium No. 266)` to the generic `fatty acid` class even though the source row denotes a mixture stock, not a single fatty-acid compound.

## Evidence

JCM 661 and MediaDive `J661` support a two-stage protocol. The base solution is 1 L of NaCl, KCl, MgCl2 x 6 H2O, CaCl2 x 2 H2O, NH4Cl, KH2PO4, Na2SO4, 0.4 mg resazurin, and 910 ml distilled water autoclaved under N2-CO2 gas. After cooling, eleven milliliter-scale stock solutions are added aseptically and anaerobically.

| Source claim | Record representation | Review |
| --- | --- | --- |
| The autoclaved base contains 910 ml distilled water. | No water row is present. | Incomplete. |
| 40 ml of 8% NaHCO3 stock is added after cooling. | `NaHCO3` is a top-level `40 G_PER_L` ingredient. | Unsupported unit and stock flattening. |
| 1 ml Trace element solution, 1 ml FeCl2 solution, and 1 ml Selenite-tungstate solution are added after cooling. | Those three MediaDive stock recipes are flattened into top-level ZnCl2, MnCl2, H3BO3, CoCl2, CuCl2, NiCl2, Na2MoO4, HCl, FeCl2, NaOH, Na2SeO3, and Na2WO4 ingredients at their stock concentrations. | Unsupported stock flattening. |
| 10 ml Trace vitamins, 1 ml Vitamin B12 solution, 1 ml Fatty acid mixture, 10 ml 10% yeast extract, 10 ml 10% Casamino acids, 5 ml 1 M glucose, and 10 ml 0.1 M dithiothreitol are added after cooling. | Most of those rows are represented as the same numeric values in `G_PER_L`; Vitamin B12 is an empty solution stub at `1 G_PER_L`. | Unsupported units and incomplete linked-stock representation. |
| Components are mixed, autoclaved under N2-CO2 (4:1), cooled, and supplemented aseptically and anaerobically. | The same preparation instruction is present. | Supported. |

## Completeness

The generated record carries every visible JCM row except the 910 ml distilled-water base row, but many post-autoclave stock additions have been converted from milliliter additions into gram-per-liter final ingredients. The MediaDive stock compositions for Trace element solution, FeCl2 solution, and Selenite-tungstate solution are present only as flattened final-medium rows.

Empty target-organism and growth-evidence fields were not treated as defects. JCM 661 is a medium formulation page, not a growth-evidence page.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | Post-autoclave milliliter stock additions are stored as gram-per-liter final ingredients. | JCM 661 lists NaHCO3, trace vitamins, fatty acid mixture, yeast extract, Casamino acids, glucose, and dithiothreitol as 40, 10, 1, 10, 10, 5, and 10 ml additions; the record stores those same numeric values as `G_PER_L`. | `data/normalized_yaml/bacterial/modified_am5_medium.yaml`; JCM/MediaDive stock migration. |
| major | Three linked solution recipes are flattened to top-level final-medium rows. | MediaDive stores Trace element solution, FeCl2 solution, and Selenite-tungstate solution as separate solutions added at 1 ml each; the record flattens their stock concentrations into final medium. | `data/normalized_yaml/bacterial/modified_am5_medium.yaml`; MediaDive stock migration. |
| major | The 910 ml distilled-water row is absent. | JCM 661 and MediaDive `J661` both include 910 ml distilled water in the autoclaved base; the YAML has no water row. | `data/normalized_yaml/bacterial/modified_am5_medium.yaml`; JCM/MediaDive import. |
| major | `Vitamin B12 solution (see Medium No. 403)` is an empty `1 G_PER_L` solution. | JCM specifies 1 ml Vitamin B12 solution after cooling; the record migrated it to a solution stub with no composition and the wrong unit. | `data/normalized_yaml/bacterial/modified_am5_medium.yaml`; solution migration. |
| major | `NiCl2 x 6 H2O` is grounded to anhydrous nickel dichloride. | MediaDive specifies `NiCl2 x 6 H2O`; the record links `CHEBI:34887` / `nickel dichloride`. | `data/normalized_yaml/bacterial/modified_am5_medium.yaml`; compound grounding. |

## Recommended Edits

1. Re-curate `data/normalized_yaml/bacterial/modified_am5_medium.yaml` from JCM 661 so the base formula includes 910 ml distilled water and only source base salts plus 0.4 mg resazurin before autoclaving.
2. Represent each post-autoclave JCM addition in milliliters, preserving 40 ml 8% NaHCO3, 10 ml trace vitamins, 1 ml Vitamin B12, 1 ml fatty acid mixture, 10 ml 10% yeast extract, 10 ml 10% Casamino acids, 5 ml 1 M glucose, and 10 ml 0.1 M dithiothreitol.
3. Preserve the Trace element, FeCl2, and Selenite-tungstate stock recipes as separate compartments or referenced solution records, not flattened final-medium ingredients.
4. Re-ground `NiCl2 x 6 H2O` to the exact hexahydrate form or leave it unresolved.
5. Regenerate `data/merge_yaml/merged/modified_am5_medium__421a5fe8.yaml` after the normalized source is corrected.

## Follow-up Checks

1. Re-run focused open-schema, strict, reference, and term validators on `data/normalized_yaml/bacterial/modified_am5_medium.yaml` and the regenerated merge output.
2. Manually compare the regenerated record against JCM `GRMD=661`, checking the 910 ml water row, the 0.4 mg resazurin row, all post-autoclave ml additions, the linked Medium No. references, and the N2-CO2 anaerobic autoclave instruction.
3. Verify that no ingredient from Trace element solution, FeCl2 solution, or Selenite-tungstate solution remains as a top-level final-medium ingredient unless a final concentration is explicitly calculated and marked as such.

## Additional Notes

The repository-level `just` validators were not used for this focused record review because the project currently attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The focused validators above were run with Python 3.11 and the offline uv cache.
