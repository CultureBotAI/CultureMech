# YAML Record Review: Desulfohalobium Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/desulfohalobium_medium__3018ef1d.yaml
- Started UTC: 2026-09-22T18:50:54Z
- Finished UTC: 2026-09-22T18:54:58Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009120 |
| Name | desulfohalobium_medium |
| Original name | Desulfohalobium Medium |
| Media term | TOGO:M2550, TOGO Medium M2550 |
| Source | TOGO M2550, derived from DSMZ Medium 499 |
| Category | bacterial |
| Generated status | Generated single-source merge in `data/merge_yaml/merged/`; do not edit directly |
| Maintained parent | `data/normalized_yaml/bacterial/TOGO_M2550_Desulfohalobium_Medium.yaml` |
| Merge fingerprint | 3018ef1d71cabf962d5b85e50dbae20aec1c5fbeed7b49e0200641316797081e |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/desulfohalobium_medium__3018ef1d.yaml` | Passed: `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/desulfohalobium_medium__3018ef1d.yaml --out /private/tmp/desulfohalobium_medium__3018ef1d.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, and only the TSV header was emitted. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/desulfohalobium_medium__3018ef1d.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 reference checks. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/desulfohalobium_medium__3018ef1d.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. The run printed the known `eutils`/`pkg_resources` deprecation warning first. |
| Embedded curation history | `just validate-history` equivalent | Not checked: the documented history validator validates standalone `history/*.yaml` records, not `MediaRecipe.curation_history` embedded in merged YAML. |

## Identity and Grounding

The record identity is correct: TOGO M2550 names Desulfohalobium Medium and points to DSMZ Medium 499, and the DSMZ PDF confirms the same final-medium formulation. The pH 7.0 value is present in TOGO metadata and the generated record.

The directly added final-medium salts, acetate, L-lactate, Trypticase peptone (BD BBL), and Yeast extract (OXOID) agree with TOGO M2550 and the DSMZ Medium 499 PDF. The source also uses 100% N2 for anaerobic preparation; this is a preparation condition, not a variable final-medium ingredient.

## Evidence

The stock and solution structure is not source-faithful:

- `Distilled water` is represented as 2990.0 G_PER_L because the importer merged 1000 ml final-medium water, 990 ml SL-10 water, and 1000 ml selenite-tungstate water.
- The SL-10 stock components are top-level final-medium ingredients, and most milligram values from the stock were coerced to G_PER_L rows, including 70 G_PER_L `ZnCl2`, 100 G_PER_L `MnCl2 x 4 H2O`, and 36 G_PER_L `Na2MoO4 x 2 H2O`.
- The selenite-tungstate stock components are likewise top-level ingredients with 3 G_PER_L `Na2SeO3 x 5 H2O` and 4 G_PER_L `Na2WO4 x 2 H2O` instead of 3 mg and 4 mg inside a 1000 ml stock.
- The three `solutions` entries are empty `Unknown solution` stubs with amounts in G_PER_L, even though TOGO and DSMZ use 0.5 ml sodium resazurin solution, 1 ml Trace element solution SL-10, and 1 ml Selenite-tungstate solution.

The generated record is also missing preparation evidence that TOGO imports as comments from DSMZ: N2 sparging for 30-45 min, pH adjustment to 6.8-7.0 before autoclaving, Hungate-type tubes or serum vials, sulfide addition from a sterile anoxic stock, final pH checking, the benign white precipitate note, and the SL-10-specific FeCl2/HCl dissolution instruction.

## Completeness

The record cannot be used to reconstruct the source recipe because it erases the final-medium versus stock-solution boundary. The `high_metal: true` flag is a downstream artifact of that error, not a property supported by the DSMZ recipe.

Explicit target-organism growth evidence is correctly absent: the inspected TOGO and DSMZ recipe sources do not assert a growth experiment.

Gitignore-independent `rg --no-ignore --hidden` over normalized YAML, merge YAML, import-tracking reports, the ID registry, and the recipe catalog found the single normalized owner plus generated/import-tracking references for `TOGO:M2550`; `find` under `reports/yaml_record_review` found no pre-existing review report for `desulfohalobium_medium__3018ef1d`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Final water and stock water are collapsed into one impossible 2990.0 G_PER_L final ingredient. | TOGO M2550 has 1000 ml water in the final recipe, 990 ml in SL-10, and 1000 ml in Selenite-tungstate; the generated YAML sums them into one top-level water row. | `data/normalized_yaml/bacterial/TOGO_M2550_Desulfohalobium_Medium.yaml`, or the TOGO importer if repaired globally. |
| Major | SL-10 and selenite-tungstate stock formulas are flattened into final-medium G_PER_L ingredient rows. | TOGO and DSMZ add each stock at 1 ml; the generated YAML records the stock recipe contents as final ingredients and inflates milligram stock amounts by 1000-fold. | `data/normalized_yaml/bacterial/TOGO_M2550_Desulfohalobium_Medium.yaml`. |
| Major | The named solution additions are empty stubs with wrong units. | `Na-resazurin solution (0.1% w/v)`, `Trace element solution SL-10`, and `Selenite-tungstate solution` have `composition: []`, `name: Unknown solution`, and G_PER_L amounts even though the source provides ml additions. | `data/normalized_yaml/bacterial/TOGO_M2550_Desulfohalobium_Medium.yaml`. |
| Major | Source preparation comments are absent from `preparation_steps`, and N2 gas is mis-modeled as a variable ingredient. | TOGO M2550 carries the DSMZ anaerobic preparation comments and SL-10 dissolution comment; the generated YAML has no preparation steps and a top-level `N2 gas` ingredient. | `data/normalized_yaml/bacterial/TOGO_M2550_Desulfohalobium_Medium.yaml`. |

## Recommended Edits

1. Rebuild the maintained TOGO M2550 record so final-medium ingredients, SL-10, and Selenite-tungstate are modeled in separate contexts.
2. Remove the summed 2990.0 G_PER_L water row and keep each water volume in its source solution.
3. Replace the top-level stock chemicals with 1 ml SL-10 and 1 ml Selenite-tungstate additions that link to or embed their stock recipes.
4. Replace the three `Unknown solution` stubs with correctly named ml-based additions, including 0.5 ml Na-resazurin solution at 0.1% w/v.
5. Restore the anaerobic final-medium preparation and SL-10 preparation details, and remove `N2 gas` as a final ingredient.
6. Regenerate `data/merge_yaml/merged/desulfohalobium_medium__3018ef1d.yaml`.

## Follow-up Checks

1. Re-run open-schema, strict, reference, and term validation on the repaired normalized record and the regenerated merged record.
2. Re-run concentration-plausibility reporting for `CultureMech:009120`; the WATER_AS_VOLUME and TRACE_SALT_AS_STOCK rows should disappear.
3. Manually compare the regenerated record against TOGO M2550 and DSMZ Medium 499 for the pH 7.0 target, final-medium ingredient amounts, 0.5 ml resazurin, two 1 ml stock additions, 100% N2 preparation, sulfide addition, and SL-10 stock boundary.

## Additional Notes

The current record is one of several source imports for a Desulfohalobium medium. This report only covers fingerprint `3018ef1d`; the separate KOMODO/DSMZ merge with fingerprint `2d1ac1fa` was reviewed independently.
