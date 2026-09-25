# YAML Record Review: Thermoanaerobacter (KoKo) Medium
- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermoanaerobacter_koko_medium__f3bb6f3e.yaml`
- Started UTC: `2026-09-25T09:39:32Z`
- Finished UTC: `2026-09-25T09:40:24Z`
- Verdict: needs curation

## Target
Generated TOGO bacterial recipe `CultureMech:009266`, `thermoanaerobacter_koko_medium`, with medium term `TOGO:M2715` and label `Thermoanaerobacter (KoKo) Medium`.

It is a single-source generated record from `TOGO_M2715_Thermoanaerobacter_KoKo_Medium`.

## Validation
- LinkML schema validation: passed; `linkml-validate` reported `No issues found`.
- Strict validation: passed; `scripts/validate_strict.py` scanned 1 file with 0 files containing errors and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` checked 1 file and reported all checked references passed.
- Term validation: passed; `linkml-term-validator` reported `Validation passed`.
- Embedded `curation_history`: Not checked. The available history validator targets standalone `history/` entries rather than `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding
The TOGO source correctly points to DSMZ Medium 710, `THERMOANAEROBACTER (KoKo) MEDIUM`, through `DSMZ_Medium710.pdf`.

The same DSMZ 710 recipe is already present as the MediaDive/KOMODO generated branch `data/merge_yaml/merged/thermoanaerobacter_koko_medium.yaml`, which carries `mediadive.medium:710`, `komodo.medium:710`, and `komodo.medium:710_12299`.

The chemical groundings for inflated SL-11 rows mostly match their strings, but the concentrations are so large that the generated record is marked `high_metal: true`; this flag is a symptom of source parsing failure rather than a source property.

## Evidence
DSMZ Medium 710 gives Trace element solution SL-11 as a 1 ml/L stock addition and Wolin's vitamin solution 10x as a 1 ml/L stock addition.

The TOGO branch flattens SL-11 into the final ingredient list and misreads milligram stock rows as grams: `ZnCl2` is `70 G_PER_L`, `MnCl2 x 4 H2O` is `100 G_PER_L`, `CoCl2 x 6 H2O` is `190 G_PER_L`, `NiCl2 x 6 H2O` is `24 G_PER_L`, and `Na2MoO4 x 2 H2O` is `36 G_PER_L`.

The generated row for `2 N NaOH` is also a top-level `VARIABLE` ingredient, although DSMZ mentions 2 N NaOH only as the pH adjuster used while preparing SL-11.

The TOGO branch flattens Wolin's vitamin solution 10x with similarly inflated vitamin rows: `Biotin` is `2 G_PER_L`, `Folic acid` is `2 G_PER_L`, `p-Aminobenzoic acid` is `5 G_PER_L`, and `Pyridoxine-HCl` is `10 G_PER_L`.

The record also merged the main water with two stock waters into `3000.0 G_PER_L`, proving that the stock recipes were parsed as if their water bases belonged to the final medium.

## Completeness
Unlike the MediaDive/KOMODO branch, the TOGO generated branch omits the structured DSMZ preparation steps for anoxic stock additions and does not preserve the MOPS supplementation note or the DSM 12299 D-glucose omission variant.

The target does retain solution stubs for sodium resazurin, SL-11, and vitamin solution, but their compositions are empty or external while their ingredients are also duplicated in the top-level final recipe.

## Findings
1. Needs curation: SL-11 was flattened into top-level final ingredients and several milligram rows were converted to gram-per-liter values.
2. Needs curation: Wolin's vitamin solution 10x was flattened into top-level final ingredients with milligram vitamin rows converted to gram-per-liter values.
3. Needs curation: stock waters were merged into the main water row, producing `3000.0 G_PER_L`.
4. Needs curation: `2 N NaOH` was promoted from an SL-11 pH-adjustment reagent to a top-level variable ingredient.
5. Needs curation: this TOGO DSMZ 710 branch is an unmerged duplicate of the MediaDive/KOMODO DSMZ 710 branch.

## Recommended Edits
1. Normalize `TOGO_M2715_Thermoanaerobacter_KoKo_Medium` in `data/normalized_yaml`, not this generated merge file, so SL-11 and Wolin's vitamin solution 10x remain nested 1 ml/L stock additions.
2. Fix unit parsing so milligram quantities inside stock recipes stay milligrams and are not emitted as gram-per-liter final medium rows.
3. Keep `2 N NaOH` scoped to the SL-11 preparation step.
4. Preserve DSMZ preparation text, the MOPS supplementation note, and the DSM 12299 D-glucose omission variant from the canonical DSMZ 710 source.
5. Merge `TOGO:M2715` with `mediadive.medium:710`, `komodo.medium:710`, and `komodo.medium:710_12299` after source normalization.

## Follow-up Checks
After source normalization and merge regeneration, re-run schema, strict, reference, and term validation.

Run an exact duplicate search with ignored files included for `TOGO:M2715`, `mediadive.medium:710`, `komodo.medium:710`, `komodo.medium:710_12299`, and `DSMZ_Medium710.pdf` and confirm there is one canonical DSMZ 710 output.

## Additional Notes
Exact duplicate-source searches included ignored files. A first pass that searched exact `name: koko_medium` values was discarded for duplicate-source purposes because it also matched a separate TOGO M860 KoKo name family outside DSMZ 710.
