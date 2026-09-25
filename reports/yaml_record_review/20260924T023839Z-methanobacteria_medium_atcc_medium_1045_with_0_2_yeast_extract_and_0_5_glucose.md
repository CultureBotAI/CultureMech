# YAML Record Review: Methanobacteria medium with 0.2% yeast extract and 0.5% glucose

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanobacteria_medium_atcc_medium_1045_with_0_2_yeast_extract_and_0_5_glucose.yaml
- Started UTC: 2026-09-24T02:37:51Z
- Finished UTC: 2026-09-24T02:38:39Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009258 |
| Name | methanobacteria_medium_atcc_medium_1045_with_0_2_yeast_extract_and_0_5_glucose |
| Original name | Methanobacteria medium (ATCC medium 1045) with 0.2% yeast extract and 0.5% glucose |
| Category | archaea |
| Medium term | TOGO:M2707 |
| Source | TOGO M2707, derived from an ATCC medium 1118 PDF for ATCC medium 1045 with supplements |
| Source URL | https://www.atcc.org/~/media/A5AC7370FB084A36A7CA2B95EA358AD9.ashx |
| Record status | Generated merge output |
| Maintained owner | data/normalized_yaml/archaea/methanobacteria_medium_atcc_medium_1045_with_0_2_yeast_extract_and_0_5_glucose.yaml |
| Merge fingerprint | c87d2bf0197fcb42667633f73cdc3c1ac2105bb1410379f67b865e0119e22325 |

This generated record is a single-source merge from `data/normalized_yaml/archaea/methanobacteria_medium_atcc_medium_1045_with_0_2_yeast_extract_and_0_5_glucose.yaml`.
Future fixes belong in that maintained TOGO owner or the TOGO/ATCC import path that parsed stock components as final-medium rows, then in regenerated `data/merge_yaml/merged/` outputs.

## Validation

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanobacteria_medium_atcc_medium_1045_with_0_2_yeast_extract_and_0_5_glucose.yaml` | Passed with `No issues found`. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/methanobacteria_medium_atcc_medium_1045_with_0_2_yeast_extract_and_0_5_glucose.yaml --out /private/tmp/methanobacteria_medium_atcc_medium_1045_with_0_2_yeast_extract_and_0_5_glucose.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors, and 0 total error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/methanobacteria_medium_atcc_medium_1045_with_0_2_yeast_extract_and_0_5_glucose.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checkable references. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/methanobacteria_medium_atcc_medium_1045_with_0_2_yeast_extract_and_0_5_glucose.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known eutils/pkg_resources deprecation warning. |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists in generated YAML. |

The normal `just` validator wrappers were not used because this uv environment tries to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools before any CultureMech validator can run.

## Identity and Grounding

The TOGO M2707 source identity is coherent: the TOGO API names `Methanobacteria medium (ATCC medium 1045) with 0.2% yeast extract and 0.5% glucose`, points to the inspected ATCC PDF, and records pH 7.2.

The ATCC PDF identifies the document as ATCC medium 1118 and says it is ATCC Medium 1045 with 0.2% yeast extract and 0.5% glucose. The YAML should preserve that ATCC 1118 identity somewhere in addition to the TOGO ID so readers can recover the exact ATCC variant.

A gitignore-independent exact search over `data/normalized_yaml` and `data/merge_yaml/merged` found one maintained owner and one generated file for the full slug/full label. Broader percentage-phrase probes also matched unrelated Todd-Hewitt and M17 records; those were not exact owners of this ATCC medium.

## Evidence

The ATCC source defines a complete medium from proportions of 83.5 parts distilled water, 5.0 parts Mineral Solution 2, 2.5 parts Mineral Solution 1, 5.0 parts 8% sodium carbonate solution, optional 20 g/L agar, 1.0 part Wolfe's Mineral Solution, 1.0 part Wolfe's Vitamin Solution, 2.0 parts Cysteine-Sulfide Reducing Agent, and 4.0 ml/L of 0.025% resazurin. It also adds 0.2% yeast extract and 0.5% glucose to ATCC Medium 1045.

The TOGO import loses that structure in several ways:

- It does not include the 0.2% yeast extract or 0.5% glucose that define this ATCC 1118 variant.
- It treats optional agar as a required 20 g/L component and sets `physical_state` to `SOLID_AGAR`.
- It turns stock proportions into `G_PER_L` solution concentrations: for example, Mineral Solution 2 becomes `50 G_PER_L`, Mineral Solution 1 becomes `25 G_PER_L`, Sodium Carbonate Solution becomes `50 G_PER_L`, Wolfe's Mineral Solution and Wolfe's Vitamin Solution become `10 G_PER_L`, and Cysteine-Sulfide Reducing Agent becomes `20 G_PER_L`.
- It copies stock formulations into top-level ingredients at stock strength; the Wolfe vitamin milligram rows become `2`, `5`, `10`, or `0.1 G_PER_L`, and L-Cysteine HCl / Na2S reducer stocks become `300 G_PER_L`.
- It sums water from the main recipe and stock recipes into a single `Distilled water: 959 G_PER_L` row, and sums duplicated salts such as magnesium sulfate and sodium chloride across unrelated stocks.

## Completeness

The pH 7.2 value is present in the TOGO M2707 API and the ATCC PDF tells users to adjust pH to 7.2 if necessary. The generated YAML lacks `ph_value`.

The ATCC PDF includes procedure that matters: mix all ingredients except Wolfe's Vitamin and cysteine/Na2S solutions, autoclave for 15 minutes, cool under 80% N2 and 20% CO2, add those two anaerobic additions, then tube anaerobically and aseptically. The generated record keeps N2 and CO2 as variable gas ingredients but has no preparation steps.

No target-organism, strain, literature growth, or variant claims are present, so there were no growth-evidence assertions to check.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The defining yeast extract and glucose supplements are missing. | The ATCC document title defines the medium as ATCC Medium 1045 with 0.2% yeast extract and 0.5% glucose; neither yeast extract nor glucose is present in `ingredients`. | `data/normalized_yaml/archaea/methanobacteria_medium_atcc_medium_1045_with_0_2_yeast_extract_and_0_5_glucose.yaml` and TOGO/ATCC import. |
| Major | Optional agar was made mandatory. | The ATCC recipe says to add agar only if solid medium is required. The YAML sets `physical_state: SOLID_AGAR` and has `Agar` at `20 G_PER_L`. | Same maintained owner and import path. |
| Major | Stock proportions and volumes were represented as gram-per-litre concentrations. | The source uses volumetric parts for Mineral Solution 1, Mineral Solution 2, sodium carbonate, Wolfe's stocks, resazurin, and Cysteine-Sulfide Reducing Agent. The YAML records those volumes as `G_PER_L` solution concentrations. | Same maintained owner and import path. |
| Major | Stock recipes were flattened into final-medium ingredients and then merged by preferred term. | Wolfe vitamin and Wolfe mineral stock ingredients, Mineral Solution 1/2 contents, and reducer stock contents appear as top-level ingredients at stock strength; water, magnesium sulfate, and sodium chloride were summed across unrelated stock recipes. | Same maintained owner and import path. |
| Major | pH and preparation are missing. | TOGO M2707 carries pH 7.2 and the ATCC PDF describes autoclaving, cooling under N2/CO2, anaerobic addition of Wolfe's Vitamin and reducer, and aseptic anaerobic tubed distribution. The YAML has no `ph_value` or `preparation_steps`. | Same maintained owner and import path. |
| Minor | The ATCC medium number is incomplete. | The inspected ATCC PDF is headed as ATCC medium 1118; the YAML only exposes TOGO M2707 and the prose phrase `ATCC medium 1045` in `original_name`. | Same maintained owner. |

## Recommended Edits

1. Re-curate the ATCC M2707 owner against the PDF as a variant of ATCC Medium 1045 with 0.2% yeast extract and 0.5% glucose.
2. Keep Mineral Solution 1, Mineral Solution 2, Sodium Carbonate Solution, Wolfe's Mineral Solution, Wolfe's Vitamin Solution, and Cysteine-Sulfide Reducing Agent as stock/use-site structures with volumetric proportions.
3. Remove stock-component rows from final-medium `ingredients`, and undo summed rows that combine main water or salts with stock water or salts.
4. Treat agar as optional; do not force `SOLID_AGAR` for the complete liquid medium.
5. Restore pH 7.2 and the anaerobic preparation sequence.
6. Preserve ATCC medium 1118 as source accession or provenance in addition to TOGO M2707.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the maintained ATCC/TOGO owner and regenerated merge output.
- Compare the regenerated record against the ATCC PDF for 83.5 / 5.0 / 2.5 / 5.0 / 1.0 / 1.0 / 2.0 part proportions, 4.0 ml/L resazurin, 0.2% yeast extract, 0.5% glucose, and optional 20 g/L agar.
- Search the regenerated YAML for exact unsupported direct concentrations `959 G_PER_L`, `300 G_PER_L`, `50 G_PER_L`, and `25 G_PER_L`; none should remain as final-medium ingredients or stock-dose concentrations.
- Manually verify that Wolfe's Vitamin stock milligram quantities are stored as stock composition, not as final `G_PER_L` values.

## Additional Notes

The old ATCC asset URL still resolves to a two-page PDF, so the original source is directly recoverable. TOGO M2707 preserves the stock group boundaries in its JSON feed, but the importer collapsed nearly all of them before this YAML was generated.
