# YAML Record Review: Desulfohalobium Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/desulfohalobium_medium__d5b3a01d.yaml
- Started UTC: 2026-09-22T18:54:59Z
- Finished UTC: 2026-09-22T18:58:12Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:010275 |
| Name | desulfohalobium_medium |
| Original name | Desulfohalobium Medium |
| Media term | TOGO:M859, TOGO Medium M859 |
| Source | TOGO M859, derived from JCM Medium 824 |
| Category | bacterial |
| Generated status | Generated single-source merge in `data/merge_yaml/merged/`; do not edit directly |
| Maintained parent | `data/normalized_yaml/bacterial/TOGO_M859_Desulfohalobium_Medium.yaml` |
| Merge fingerprint | d5b3a01d3b7db52730e561e0ab9d53ff6274b68109eac2ab313c65eee944b416 |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/desulfohalobium_medium__d5b3a01d.yaml` | Passed: `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/desulfohalobium_medium__d5b3a01d.yaml --out /private/tmp/desulfohalobium_medium__d5b3a01d.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, and only the TSV header was emitted. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/desulfohalobium_medium__d5b3a01d.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 reference checks. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/desulfohalobium_medium__d5b3a01d.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. The run printed the known `eutils`/`pkg_resources` deprecation warning first. |
| Embedded curation history | `just validate-history` equivalent | Not checked: the documented history validator validates standalone `history/*.yaml` records, not `MediaRecipe.curation_history` embedded in merged YAML. |

## Identity and Grounding

The record identity is correct for the JCM formulation: TOGO M859 points to `JCM_M824`, and the live JCM 824 page is titled `DESULFOHALOBIUM MEDIUM`. This is a distinct Solution A/Solution B JCM medium, not the DSMZ Medium 499 formulation reviewed in the neighboring `3018ef1d` and `2d1ac1fa` records.

The maintained TOGO row imported the major Solution A and Solution B ingredients from JCM 824, including 900 ml Solution A water, 100 ml Solution B water, the 1 g yeast extract and 1 g Trypticase peptone in Solution A, and the 20 g MgCl2 / 2.7 g CaCl2 Solution B salts.

## Evidence

The generated record loses the JCM solution hierarchy. JCM Medium 824 first makes the medium from 900 ml Solution A and 100 ml Solution B, then completes each liter under N2 by adding 10 ml of a 3% Na2S x 9 H2O anaerobic stock. The generated record flattens the Solution A and B ingredients into the top-level `ingredients` list while also leaving empty `Unknown solution` stubs for Solution A at 900 G_PER_L, Solution B at 100 G_PER_L, the FeCl2 cross-reference, the trace-element cross-reference, and the 3% sulfide stock.

Two JCM amounts are imported with unit errors: the 1 mg Resazurin row is represented as 1 G_PER_L, and the 3 microgram Na2SeO3 x 5H2O row is represented as 3 G_PER_L. The generated 1000 G_PER_L Distilled water row is also just the sum of Solution A 900 ml water and Solution B 100 ml water, not a final concentration.

The generated record omits all three source preparation statements: mix Solution A and adjust it to pH 7.0 before autoclaving under N2, autoclave Solution B under N2, and combine A and B under N2 before adding the anaerobic sulfide stock.

## Completeness

The record has enough source metadata to find the TOGO and JCM records, but it cannot reconstruct the source recipe because all named solution boundaries are empty or duplicated.

Explicit target-organism growth evidence is correctly absent because the inspected TOGO and JCM recipe sources do not report a growth experiment.

Gitignore-independent `rg --no-ignore --hidden` over normalized YAML, merge YAML, import-tracking reports, the ID registry, and the recipe catalog found the single normalized owner plus generated/import-tracking references for `TOGO:M859`; `find` under `reports/yaml_record_review` found no pre-existing review report for `desulfohalobium_medium__d5b3a01d`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Solution A, Solution B, FeCl2 solution, trace element solution, and 3% sulfide solution are empty stubs with G_PER_L amounts. | JCM 824 gives 900 ml Solution A, 100 ml Solution B, 1 ml FeCl2 solution, 1 ml trace element solution, and 10 ml 3% Na2S x 9 H2O solution; the generated `solutions` entries have `name: Unknown solution`, empty compositions or external notes, and G_PER_L quantities. | `data/normalized_yaml/bacterial/TOGO_M859_Desulfohalobium_Medium.yaml`. |
| Major | Solution A and Solution B contents are flattened into the final ingredient list and water is summed across solutions. | The source scopes 900 ml water to Solution A and 100 ml water to Solution B; the generated YAML has one 1000 G_PER_L water row plus final ingredient rows for the contents of A and B. | `data/normalized_yaml/bacterial/TOGO_M859_Desulfohalobium_Medium.yaml`, or the TOGO importer if repaired globally. |
| Major | Resazurin and selenite quantities have unit slips. | JCM and TOGO list 1 mg Resazurin and 3 micrograms Na2SeO3 x 5H2O in Solution A; the generated YAML represents them as 1 G_PER_L and 3 G_PER_L. | `data/normalized_yaml/bacterial/TOGO_M859_Desulfohalobium_Medium.yaml`. |
| Major | Preparation conditions are missing and N2 is mis-modeled as a top-level ingredient. | JCM 824 has separate N2 autoclaving instructions for Solution A and B plus an N2 completion step; the generated YAML has no `preparation_steps` and only an `N2` ingredient with a default variable concentration. | `data/normalized_yaml/bacterial/TOGO_M859_Desulfohalobium_Medium.yaml`. |

## Recommended Edits

1. Rebuild the normalized TOGO M859 record with explicit Solution A, Solution B, FeCl2 stock, trace-element stock, and 3% sulfide stock boundaries.
2. Remove the duplicated top-level Solution A/Solution B water and ingredient rows once those components are scoped to their solutions.
3. Correct 1 mg Resazurin and 3 micrograms Na2SeO3 x 5H2O to source-supported values in Solution A.
4. Convert Solution A, Solution B, FeCl2 solution, trace element solution, and the 3% sulfide stock from empty G_PER_L `Unknown solution` stubs into ml-based additions or references that resolve to maintained solution recipes.
5. Restore the JCM N2 preparation steps, including Solution A pH 7.0 adjustment, separate N2 autoclaving of A and B, N2 combination, and per-liter sulfide addition from an anaerobic stock.
6. Regenerate `data/merge_yaml/merged/desulfohalobium_medium__d5b3a01d.yaml`.

## Follow-up Checks

1. Re-run open-schema, strict, reference, and term validation on the repaired normalized record and the regenerated merged record.
2. Re-run concentration-plausibility reporting for `CultureMech:010275`; the WATER_AS_VOLUME, INDICATOR_UNIT_SLIP, and TRACE_SALT_AS_STOCK rows should disappear.
3. Manually compare the regenerated record against TOGO M859 and JCM Medium 824 for the Solution A/B split, 900 ml and 100 ml water scopes, FeCl2 and trace stock cross-references, 10 ml sulfide stock addition, and N2 autoclaving/completion steps.

## Additional Notes

TOGO M859 comes from JCM Medium 824, while TOGO M2550 and the KOMODO/DSMZ merge point to DSMZ Medium 499. The shared title is not enough to merge these records without preserving their conflicting solution structures.
