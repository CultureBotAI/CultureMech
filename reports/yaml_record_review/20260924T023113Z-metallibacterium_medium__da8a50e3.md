# YAML Record Review: Metallibacterium Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/metallibacterium_medium__da8a50e3.yaml
- Started UTC: 2026-09-24T02:30:52Z
- Finished UTC: 2026-09-24T02:31:13Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:010352 |
| Name | metallibacterium_medium |
| Original name | Metallibacterium Medium |
| Category | bacterial |
| Medium term | TOGO:M930, Metallibacterium Medium |
| Source | TOGO M930, originally JCM_M889 |
| Source URL | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=889 |
| Record status | Generated merge output |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M930_Metallibacterium_Medium.yaml |
| Merge fingerprint | da8a50e39577dd3cabf6dcf3ed38ae7561c55094f2ac461239a49dc76df8d5e9 |

This is a generated single-source merge from `data/normalized_yaml/bacterial/TOGO_M930_Metallibacterium_Medium.yaml`.
Future fixes belong in that maintained TOGO owner, the TOGO import logic that populated it, or the merge/source-alias rules that should unify duplicate JCM 889 imports before regenerating `data/merge_yaml/merged/`.

## Validation

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/metallibacterium_medium__da8a50e3.yaml` | Passed with `No issues found`. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/metallibacterium_medium__da8a50e3.yaml --out /private/tmp/metallibacterium_medium__da8a50e3.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors, and 0 total error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/metallibacterium_medium__da8a50e3.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checkable references. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/metallibacterium_medium__da8a50e3.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known eutils/pkg_resources deprecation warning. |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists in generated YAML. |

The normal `just` validator wrappers were not used because this uv environment tries to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools before any CultureMech validator can run.

## Identity and Grounding

The TOGO identity is correct: the TOGO M930 API names `Metallibacterium Medium`, points to `JCM_M889`, and carries the same JCM `GRMD=889` URL as the YAML.

The live JCM 889 page is available and also names medium 889 `METALLIBACTERIUM MEDIUM`, so JCM could be inspected directly for the main recipe, stock addition rows, and pH/protocol text.

A gitignore-independent exact search over `data/normalized_yaml` and `data/merge_yaml/merged` found three local Metallibacterium Medium owners:

- `data/normalized_yaml/bacterial/TOGO_M930_Metallibacterium_Medium.yaml`, generated as this reviewed TOGO file.
- `data/normalized_yaml/bacterial/JCM_J889_METALLIBACTERIUM_MEDIUM.yaml`, generated as `data/merge_yaml/merged/METALLIBACTERIUM_MEDIUM.yaml`.
- `data/normalized_yaml/bacterial/metallibacterium_medium.yaml`, the DSMZ 1475 MediaDive version, generated as `data/merge_yaml/merged/metallibacterium_medium__f4ff58cd.yaml`.

The first two are duplicate JCM 889 imports. The DSMZ 1475 recipe has a different source URL, pH 5.0, and formula differences, so it needs source-specific reconciliation rather than blind merging with JCM 889.

## Evidence

JCM 889 and TOGO M930 agree on the main formula: 1 L distilled water, 132 mg ammonium sulfate, 53 mg magnesium chloride hexahydrate, 27 mg potassium dihydrogen phosphate, 147 mg calcium chloride dihydrate, 0.5 mg vanadyl sulfate hydrate, 10 mg ferrous sulfate heptahydrate, 1.4 g Trypticase peptone, 1 ml Wolfe's mineral elixir, and 10 ml Trace vitamins.

The generated record preserves the Trypticase peptone amount but misrepresents every milligram main ingredient by storing the numeric milligram amount as `G_PER_L`: for example, 132 mg ammonium sulfate becomes `132 G_PER_L`, 147 mg calcium chloride dihydrate becomes `147 G_PER_L`, and 0.5 mg vanadyl sulfate becomes `0.5 G_PER_L`.

The generated `solutions` entries also have the wrong dimension. JCM 889 and TOGO M930 list 1 ml Wolfe's mineral elixir and 10 ml Trace vitamins as additions to the main recipe; the YAML stores them as empty solutions at `1 G_PER_L` and `10 G_PER_L`.

The JCM page says to mix components except Trace vitamins, adjust pH to 5.5, autoclave, and then aseptically add filter-sterilized Trace vitamins after cooling. The generated TOGO record lacks `ph_value` and `preparation_steps` entirely.

## Completeness

The record has no target-organism, strain, literature growth, or variant claims, so there were no growth-evidence assertions to check.

The TOGO import leaves Wolfe's mineral elixir and Trace vitamins as empty cross-reference stubs. Empty optional composition is not inherently invalid, but these are consequential stocks with resolvable recipes in the JCM/MediaDive path; leaving them empty makes the record unable to reproduce the medium.

The generated TOGO record also lacks a CHEBI grounding for `VOSO4 x H2O`; this is less severe than the amount and stock-reference errors because the source's hydrate count is explicitly variable.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Milligram formula rows are inflated by 1000x. | JCM 889 and TOGO M930 list calcium chloride dihydrate, ammonium sulfate, magnesium chloride hexahydrate, ferrous sulfate heptahydrate, potassium dihydrogen phosphate, and vanadyl sulfate hydrate in mg. The YAML records the same numeric values as `G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M930_Metallibacterium_Medium.yaml` and the TOGO unit parser. |
| Major | Milliliter stock additions were imported as empty gram-per-litre solution concentrations. | The source rows are 1 ml Wolfe's mineral elixir and 10 ml Trace vitamins; the YAML has empty `solutions` with `1 G_PER_L` and `10 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M930_Metallibacterium_Medium.yaml` and the TOGO solution mapping. |
| Major | The pH and preparation procedure are missing. | JCM 889 records pH adjustment to 5.5 before autoclaving and post-autoclave aseptic addition of filter-sterilized Trace vitamins. The TOGO generated record has no `ph_value` or `preparation_steps`. | Prefer de-duplicating with `data/normalized_yaml/bacterial/JCM_J889_METALLIBACTERIUM_MEDIUM.yaml` or enriching the TOGO path from live JCM/MediaDive J889. |
| Major | The same JCM 889 source is represented as two generated records. | The TOGO owner uses `JCM_M889` / `TOGO:M930`; `data/normalized_yaml/bacterial/JCM_J889_METALLIBACTERIUM_MEDIUM.yaml` uses `mediadive.medium:J889` and the same JCM `GRMD=889` URL. Both merge to separate generated files. | Source aliasing for TOGO M930 and MediaDive J889, plus a regenerated merge. |
| Minor | `VOSO4 x H2O` is ungrounded. | The source formula states a variable hydrate vanadyl sulfate row and the YAML keeps it without a `term`. | `data/normalized_yaml/bacterial/TOGO_M930_Metallibacterium_Medium.yaml`. |

## Recommended Edits

1. Fix the TOGO importer so M930 milligram rows become milligram-derived gram-per-litre values rather than raw numeric `G_PER_L` values.
2. Keep 1 ml Wolfe's mineral elixir and 10 ml Trace vitamins as stock additions, not `G_PER_L` concentrations, and resolve their cross-referenced compositions when available.
3. Preserve JCM 889 pH 5.5 and the autoclave/filter-sterile vitamin-addition instructions in the maintained JCM representation.
4. Add a source alias between TOGO M930 and MediaDive J889 so the two JCM 889 records merge before publication.
5. Decide whether DSMZ 1475 is a source variant of the same medium or a separate formulation, and keep the pH 5.0 and pH 5.5 formulas from collapsing silently.
6. Revisit `VOSO4 x H2O` grounding after the source quantities and solution use-sites are fixed.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the maintained TOGO owner after importer fixes and on the regenerated merge.
- Compare the regenerated formula against live JCM `GRMD=889`: all six main mg rows, the 1 ml Wolfe's mineral elixir row, the 10 ml Trace vitamins row, 1.4 g Trypticase peptone, and pH 5.5 must survive with the correct dimensions.
- Search `data/merge_yaml/merged` with ignored files included for exact `GRMD=889`, `TOGO:M930`, and `mediadive.medium:J889` after merge regeneration; the JCM 889 source should appear in one generated record, not both the TOGO and JCM MediaDive outputs.
- Manually compare the regenerated JCM 889 record with DSMZ 1475 before any deduplication that would combine their formulas.

## Additional Notes

The current TOGO-generated file is less internally over-flattened than the MediaDive J889 generated sibling because it keeps Wolfe's mineral elixir and Trace vitamins as solution references. Those stubs are still dimensionally wrong and empty, but they do at least mark the two stock boundaries.
