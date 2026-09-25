# YAML Record Review: Modified Marine Agar 2216

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_marine_agar_2216__a1dd07b7.yaml
- Started UTC: 2026-09-24T11:48:51Z
- Finished UTC: 2026-09-24T11:48:51Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/modified_marine_agar_2216__a1dd07b7.yaml`.

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| CultureMech ID | `CultureMech:007881` |
| Name | `modified_marine_agar_2216` |
| Source identity | `TOGO:M1345`, originally JCM `JCM_M1251` |
| Category | `bacterial` |
| Maintained owner | `data/normalized_yaml/bacterial/modified_marine_agar_2216.yaml` |
| Generated artifact | yes; generated under `data/merge_yaml/merged/` from one TOGO-normalized source |

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_marine_agar_2216__a1dd07b7.yaml` exited 0 with no diagnostics. |
| Strict CultureMech validation | Passed; `scripts/validate_strict.py data/merge_yaml/merged/modified_marine_agar_2216__a1dd07b7.yaml --out /private/tmp/modified_marine_agar_2216__a1dd07b7.strict.tsv --workers 1 --quiet` reported 0 errors and wrote only the TSV header line. |
| Reference validation | Passed; `linkml-reference-validator validate data data/merge_yaml/merged/modified_marine_agar_2216__a1dd07b7.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` checked one file, ran 0 reference checks, and reported no errors. |
| Term validation | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/modified_marine_agar_2216__a1dd07b7.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0 after a harmless `pkg_resources` deprecation warning. |
| Embedded history validation | Not checked: the available `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

## Identity and Grounding

The record denotes TOGO M1345 / JCM 1251, "Modified Marine Agar 2216". Its generated artifact has the correct CultureMech ID and source identity, but it is stale relative to the maintained normalized file.

The maintained source was repaired on 2026-09-11 to preserve the source 1 L water amount, pH 7.5, intentionally unmapped BD complex products, a FOODON grounding for malt extract and Phytone peptone, and references to TOGO M1345 and JCM 1251. The generated YAML still reflects the pre-repair state from 2026-08-06.

## Evidence

The inspected JCM 1251 page lists:

| Ingredient | Amount |
|---|---|
| Marine agar 2216 (BD-Difco) | 55.1 g |
| Casitone (BD-Difco) | 1.0 g |
| Phytone peptone (BD-Difco) | 1.0 g |
| Malt extract (BD-Difco) | 1.0 g |
| Distilled water | 1.0 L |

JCM instructs adjustment to pH 7.5 and applies its default sterilization instruction to autoclave at 121C for 15 min unless otherwise stated. The inspected TOGO M1345 API payload supports the same JCM 1251 source identity, pH 7.5, and ingredient list.

The current normalized YAML agrees with the JCM/TOGO ingredient list, but the generated YAML still has `Distilled water` at `1 G_PER_L`, lacks `ph_value: 7.5`, has no preparation steps, lacks the FOODON groundings added for the repaired complex nutrients, and lacks the curated `references`.

## Completeness

The generated record is incomplete because it omits curated source details that already exist in its maintained owner. The missing pH, source references, repaired water unit, and preparation steps should reappear after regeneration.

No target organism claims were expected from the inspected JCM or TOGO medium records.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The generated record is stale relative to the repaired TOGO M1345 normalized record. | `data/normalized_yaml/bacterial/modified_marine_agar_2216.yaml` was repaired on 2026-09-11, after this generated file's 2026-08-06 `merge_recipes.py` run, and now carries the source pH, 1 L water row, FOODON groundings, source references, roles, and preparation steps that are absent from the generated YAML. | Regenerate `data/merge_yaml/merged/modified_marine_agar_2216__a1dd07b7.yaml` from `data/normalized_yaml/bacterial/modified_marine_agar_2216.yaml`; do not patch the generated YAML directly. |
| major | Distilled water has the wrong unit in the generated artifact. | JCM 1251, TOGO M1345, and the maintained normalized source all say 1 L distilled water; the generated record stores `1 G_PER_L`. | Regenerate from the maintained source after confirming the generator preserves `unit: L`. |
| minor | JCM's default autoclave instruction is not represented. | The direct JCM page says to autoclave media at 121C for 15 min unless otherwise stated; the maintained record currently only mixes and adjusts pH. | Add a source-backed autoclave step to `data/normalized_yaml/bacterial/modified_marine_agar_2216.yaml` if the repository chooses to capture JCM page defaults. |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/` so the September repair to `data/normalized_yaml/bacterial/modified_marine_agar_2216.yaml` reaches the reviewed generated file.
2. Confirm the generated record retains 1 L distilled water, pH 7.5, curated FOODON terms, source references, and role annotations from the maintained YAML.
3. Decide whether JCM default page-level autoclaving belongs in the normalized record, and add an autoclave step if it is in scope.

## Follow-up Checks

- Rerun focused LinkML, strict, reference, and term validation on the regenerated TOGO M1345 YAML.
- Re-open the JCM 1251 page and TOGO M1345 API record and confirm the regenerated YAML still matches the 55.1 g / 1.0 g / 1.0 g / 1.0 g / 1.0 L ingredient table.
- Inspect the regenerated artifact and verify it no longer contains `Distilled water` with `unit: G_PER_L`.
- Confirm JCM 1251 / TOGO M1345 stays distinct from JCM 913 / TOGO M958 because JCM 1251 uses Phytone peptone only, while JCM 913 allows Soytone or Phytone peptone.

## Additional Notes

- `just` validators were not used because project dependency resolution attempts to build `llvmlite==0.46.0` under Python 3.13; the focused validators were run with `/usr/local/bin/python3.11` and the offline review cache instead.
- JCM 913 / TOGO M958 has the same medium name but a different peptone row. It is not automatically a duplicate of JCM 1251 / TOGO M1345.
