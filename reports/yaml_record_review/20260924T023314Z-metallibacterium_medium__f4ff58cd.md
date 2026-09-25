# YAML Record Review: METALLIBACTERIUM MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/metallibacterium_medium__f4ff58cd.yaml
- Started UTC: 2026-09-24T02:32:37Z
- Finished UTC: 2026-09-24T02:33:14Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:000942 |
| Name | metallibacterium_medium |
| Original name | METALLIBACTERIUM MEDIUM |
| Category | bacterial |
| Medium term | mediadive.medium:1475, DSMZ Medium 1475 |
| Source | DSMZ via MediaDive |
| Source URL | https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1475.pdf |
| Record status | Generated merge output |
| Maintained owner | data/normalized_yaml/bacterial/metallibacterium_medium.yaml |
| Merge fingerprint | f4ff58cdd526d67533036807a338fa0ecc467426f4f998a51e8261f3fe928a84 |

This generated record is a single-source merge from `data/normalized_yaml/bacterial/metallibacterium_medium.yaml`.
Future fixes belong in that maintained MediaDive/DSMZ owner or the MediaDive import logic that flattened nested solutions, then in regenerated `data/merge_yaml/merged/` outputs.

## Validation

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/metallibacterium_medium__f4ff58cd.yaml` | Passed with `No issues found`. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/metallibacterium_medium__f4ff58cd.yaml --out /private/tmp/metallibacterium_medium__f4ff58cd.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors, and 0 total error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/metallibacterium_medium__f4ff58cd.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checkable references. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/metallibacterium_medium__f4ff58cd.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known eutils/pkg_resources deprecation warning. |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists in generated YAML. |

The normal `just` validator wrappers were not used because this uv environment tries to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools before any CultureMech validator can run.

## Identity and Grounding

The source identity is coherent: MediaDive record `1475` and the DSMZ PDF both name `METALLIBACTERIUM MEDIUM`, set pH to 5.0, and define a final volume of 1008 ml.

A gitignore-independent exact search over `data/normalized_yaml` and `data/merge_yaml/merged` found three local Metallibacterium Medium owners: this DSMZ 1475 record plus two JCM 889 copies imported through TOGO M930 and MediaDive J889. The DSMZ formula uses pH 5.0, 5 ml of 0.01% VOSO4 x H2O, 1 ml of 1% FeSO4 x 7 H2O, and 1 ml of Wolin's vitamin solution (10x); the live JCM page instead uses pH 5.5, 0.5 mg VOSO4 x n H2O, 10 mg FeSO4 x 7 H2O, and 10 ml Trace vitamins. Those differences should be preserved as source variation unless a curator finds explicit evidence that one source supersedes the other.

The ChEBI terms for the main salts and most stock components are plausible. Their rows are often attached to the wrong structural level because stock recipes were flattened into final-medium ingredients.

## Evidence

The inspected DSMZ PDF and MediaDive `1475` payload support these main-medium rows over a final 1008 ml: 132 mg ammonium sulfate, 53 mg magnesium chloride hexahydrate, 27 mg potassium dihydrogen phosphate, 147 mg calcium chloride dihydrate, 5 ml of 0.01% vanadyl sulfate hydrate, 1 ml Wolfe's mineral elixir, 1 ml of 1% ferrous sulfate heptahydrate, 1.4 g Trypticase peptone, 1 ml Wolin's vitamin solution (10x), and 1000 ml distilled water.

The record's top-level normalized rows for ammonium sulfate, magnesium chloride hexahydrate, potassium dihydrogen phosphate, vanadyl sulfate hydrate, and Trypticase peptone are supported by MediaDive final-volume arithmetic.

The Wolfe's mineral elixir and Wolin's vitamin solution rows are not final-medium ingredients. The source defines them as separate 1 L stocks dosed into the medium at 1 ml each. The YAML lists every Wolfe and vitamin stock component as a direct final-medium `G_PER_L` ingredient at the undiluted stock concentration.

The flattened Wolfe stock also caused chemically distinct use-sites to collapse. Main-medium calcium is 147 mg in 1008 ml, or `0.145833 G_PER_L`; the stock contains calcium chloride dihydrate at `1 G_PER_L`. The YAML merged those unrelated rows into one `1.145833 G_PER_L` ingredient. The same happened to the 1% ferrous sulfate main addition and the Wolfe stock ferrous sulfate row, yielding `1.00992064 G_PER_L`.

The source preparation step for Wolfe's mineral elixir, pH 1.0 with diluted H2SO4, belongs to that stock. The YAML appends it as a second top-level medium preparation step, after the DSMZ main-medium autoclave and vitamin-addition step.

## Completeness

The generated record has no target-organism, strain, literature growth, or variant claims, so there were no growth-evidence assertions to check.

Wolfe's mineral elixir and Wolin's vitamin solution are consequential stock recipes with explicit DSMZ/MediaDive compositions. Empty solution composition is not a problem here because the importer chose not to make solution stubs at all; the problem is that it converted those stock compositions into final-medium ingredient rows.

The record drops the `BD BBL` source attribute from the Trypticase peptone row and does not preserve the 0.01% and 1% w/v stock attributes on the vanadyl sulfate and ferrous sulfate main-medium additions.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Wolfe's mineral elixir is flattened into final-medium ingredients at stock strength. | DSMZ 1475 adds 1 ml Wolfe's mineral elixir to a 1008 ml final medium. The YAML records the stock's magnesium sulfate, manganese sulfate, sodium chloride, cobalt chloride, calcium chloride, zinc sulfate, copper sulfate, aluminum potassium sulfate, boric acid, molybdate, nickel sulfate, tungstate, and selenate rows as direct final-medium ingredients. | `data/normalized_yaml/bacterial/metallibacterium_medium.yaml` and MediaDive importer stock handling. |
| Major | Wolin's vitamin solution (10x) is flattened into final-medium ingredients at stock strength. | DSMZ 1475 adds 1 ml of a 1 L vitamin stock, but the YAML records the ten vitamin-stock compounds as direct final-medium `G_PER_L` rows at their stock concentrations. | `data/normalized_yaml/bacterial/metallibacterium_medium.yaml` and MediaDive importer stock handling. |
| Major | Calcium chloride and ferrous sulfate from separate use-sites were merged by preferred term. | The YAML's `CaCl2 x 2 H2O` and `FeSO4 x 7 H2O` notes show duplicate merges of `0.145833 + 1.0` and `0.00992064 + 1.0`; the source rows come from the main medium and Wolfe's stock and should remain separate. | `data/normalized_yaml/bacterial/metallibacterium_medium.yaml`; prevent stock flattening before cleanup can merge use-sites. |
| Major | Wolfe's mineral elixir preparation text is scoped to the final medium. | The pH 1.0 H2SO4 step is the source step for Wolfe's mineral elixir, but the YAML places it in top-level `preparation_steps`. | `data/normalized_yaml/bacterial/metallibacterium_medium.yaml` and nested solution preservation in the MediaDive importer. |
| Minor | Stock-strength annotations on main liquid additions are dropped. | The DSMZ source identifies the vanadyl sulfate row as 5 ml of 0.01% w/v solution and the ferrous sulfate row as 1 ml of 1% w/v solution; the YAML keeps only final `G_PER_L` amounts. | `data/normalized_yaml/bacterial/metallibacterium_medium.yaml`. |
| Minor | Trypticase peptone source detail is weakened. | The DSMZ row names `Trypticase peptone (BD BBL)`; the YAML stores only `Trypticase peptone`. | `data/normalized_yaml/bacterial/metallibacterium_medium.yaml`. |

## Recommended Edits

1. Preserve Wolfe's mineral elixir and Wolin's vitamin solution as nested stock solutions dosed at 1 ml into the 1008 ml DSMZ 1475 final medium.
2. Undo the calcium chloride and ferrous sulfate preferred-term sums by retaining their main-medium and Wolfe-stock contexts separately.
3. Keep the Wolfe pH 1.0 / diluted H2SO4 step attached to Wolfe's mineral elixir, not to the final Metallibacterium Medium recipe.
4. Preserve the 0.01% w/v VOSO4 x H2O and 1% w/v FeSO4 x 7 H2O annotations as stock strengths on their main-medium liquid additions.
5. Preserve the `BD BBL` attribute on Trypticase peptone.
6. Add enough source-variant metadata to keep DSMZ 1475 distinct from the JCM 889 / TOGO M930 formula while still making the shared `METALLIBACTERIUM MEDIUM` name discoverable.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on `data/normalized_yaml/bacterial/metallibacterium_medium.yaml` and the regenerated merge output after nested-solution repair.
- Compare regenerated DSMZ 1475 rows against the PDF: final pH 5.0, final volume 1008 ml, 1 ml Wolfe's mineral elixir, 1 ml Wolin's vitamin solution (10x), and the two liquid main additions with their stock strengths must be preserved.
- Search the regenerated DSMZ record for the exact duplicate-merge values `1.145833` and `1.00992064`; neither unsupported summed row should remain.
- Manually compare DSMZ 1475 with JCM 889 before merging or aliasing the same `metallibacterium_medium` name across sources.

## Additional Notes

The source PDF and MediaDive REST payload agree on the DSMZ formula. The disagreement with JCM 889 is source-level variation in pH, liquid-stock strengths, and vitamin stock dose, not a failed PDF extraction.
