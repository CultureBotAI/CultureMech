# YAML Record Review: czapek_dox_agar

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/czapek_dox_agar.yaml`
- Started UTC: 2026-09-22T13:16:00Z
- Finished UTC: 2026-09-22T13:19:44Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `MediaRecipe` |
| Generated ID | `CultureMech:004065` |
| Name | `czapek_dox_agar` |
| Original name | `CZAPEK-DOX AGAR` |
| Primary source term | `komodo.medium:130` / KOMODO Medium 130 |
| DSMZ source | DSMZ Medium 130 / `mediadive.medium:130` |
| Generated from | `czapek_dox_agar`, `czapek_dox_agar`, `czapek_solution_agar_a`, `czapek_solution_agar_b`, `czapeks_solution_agar_with_200_g_sucrose`, `sucrose_nitrate_agar_czapek_dox_agar` |
| Merge fingerprint | `b640cca8b69cfb1b1487732c387d1e68b60fd2695396505e567a64a4e67f9ce5` |

The reviewed file is generated. Equivalent DSMZ/KOMODO source repairs belong
under `data/normalized_yaml/`, and the false JCM synonym merge belongs either
in the affected JCM normalized records or in the merge rules that grouped them
with DSMZ 130.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open-schema LinkML | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/czapek_dox_agar.yaml` | Passed with `No issues found`. |
| Strict closed-schema validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/czapek_dox_agar.yaml --out /private/tmp/czapek_dox_agar.strict.tsv --workers 1 --quiet` | Passed with 0 error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/czapek_dox_agar.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 references were checked. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/czapek_dox_agar.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after a harmless `eutils`/`pkg_resources` deprecation warning. |
| Embedded history | `just validate-history` equivalent for `curation_history` | Not checked: the repository history validator targets standalone `history/*.yaml` records, not embedded generated `MediaRecipe.curation_history` events. |

## Identity and Grounding

- The primary generated record denotes DSMZ/KOMODO 130, `CZAPEK-DOX AGAR`.
  DSMZ Medium 130 and MediaDive 130 agree on sucrose 30 g, NaNO3 3 g,
  MgSO4 x 7 H2O 0.5 g, KCl 0.5 g, FeSO4 x 7 H2O 0.01 g, K2HPO4 1 g, agar
  13 g, distilled water 1000 ml, and pH 7.2.
- The generated record falsely treats four JCM variants as synonyms of DSMZ
  130. Direct JCM checks show that JCM 29 has 20 g agar, JCM 271 has 2 g
  NaNO3 and 15 g agar at pH 7.3, JCM 39 has 200 g sucrose and 20 g agar, and
  JCM 441 has 2 g NaNO3, 15 g agar, and pH 7.0-7.3.
- The generated `NaNO3` ingredient has an exact primary ChEBI grounding to
  sodium nitrate but still carries deprecated `mediaingredientmech_term:
  MediaIngredientMech:000171`; sibling TOGO/JCM imports use
  `mediaingredientmech_chebi_term: CHEBI:63005`.
- The generated `Sucrose`, `MgSO4 x 7 H2O`, `KCl`, `FeSO4 x 7 H2O`, `K2HPO4`,
  and `Agar` ChEBI groundings match the forms in DSMZ 130.
- A gitignore-independent search with `find` over `data/normalized_yaml`
  resolved bacterial and fungal normalized records for each JCM variant name.
  An attempted `rg --no-ignore --hidden` search over `data/raw`,
  `data/normalized_yaml`, and `data/merge_yaml/merged` was too broad because it
  matched every `CultureMech:` identifier in the generated indexes.

## Evidence

- Supported by DSMZ 130 and MediaDive 130: the generated seven non-water
  ingredient amounts and pH 7.2.
- Supported by the fungal DSMZ 130 normalized input but dropped from the
  generated output: `preparation_steps` with `Adjust pH to 7.2.`
- Missing from both DSMZ 130 normalized inputs and from the generated output:
  `Distilled water` at 1000 ml.
- Unsupported by the JCM sources: the generated synonym claims for J29, J271,
  J39, and J441. Those JCM records are Czapek-family variants, not exact
  duplicates of DSMZ 130.
- No organism growth claims or incubation conditions are present.

## Completeness

- Missing source row: DSMZ 130 includes distilled water, but the generated
  record and both normalized DSMZ/KOMODO inputs omit it.
- Missing preparation: DSMZ 130 says to adjust pH to 7.2; the fungal DSMZ
  normalized record preserves this, but the generated merge discards it.
- Missing identity separation: generated synonyms erase meaningful Czapek
  variant differences in agar, nitrate, sucrose, and pH.
- Correctly empty: no target-organism evidence, variant links, quality flags,
  or discussions are present in the reviewed generated record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Blocker | The generated record falsely merges four JCM Czapek variants into DSMZ/KOMODO 130. | J29 differs in agar amount, J39 differs in sucrose and agar amount, J271 differs in NaNO3, agar, and pH, and J441 differs in NaNO3, agar, and pH range. The generated record lists all four as synonyms while preserving only the DSMZ 130 formula. | Keep the JCM variant normalized records out of the DSMZ 130 merge group; adjust `merge_recipes.py` and regenerate `data/merge_yaml/merged/`. |
| Major | DSMZ 130 distilled water is absent. | DSMZ Medium 130 and MediaDive 130 list 1000 ml distilled water; both DSMZ/KOMODO normalized `czapek_dox_agar.yaml` inputs stop at agar. | Add the water row to the maintained DSMZ/KOMODO 130 normalized inputs before regeneration. |
| Major | DSMZ 130 pH preparation is lost in the merge. | `data/normalized_yaml/fungal/czapek_dox_agar.yaml` has `Adjust pH to 7.2.`, but the generated record has no `preparation_steps`. | Preserve preparation steps when merging exact duplicates and regenerate. |
| Major | Sodium nitrate still uses the deprecated legacy MIM slot despite having an exact CHEBI primary term. | The generated NaNO3 ingredient has `term: CHEBI:63005` but retains `mediaingredientmech_term: MediaIngredientMech:000171`; peer TOGO/JCM Czapek records already use `mediaingredientmech_chebi_term: CHEBI:63005`. | Refresh the DSMZ/KOMODO 130 normalized NaNO3 `mediaingredientmech_chebi_term`, then regenerate. |

## Recommended Edits

1. Repair duplicate grouping so `mediadive.medium:J29`, `J271`, `J39`, and
   `J441` remain separate from DSMZ/KOMODO 130 unless a source proves exact
   equivalence.
2. Add 1000 ml distilled water to the DSMZ/KOMODO 130 normalized inputs and
   keep the pH 7.2 adjustment step in the regenerated DSMZ 130 canonical record.
3. Replace the leftover legacy NaNO3 `mediaingredientmech_term` on the DSMZ 130
   inputs with `mediaingredientmech_chebi_term: CHEBI:63005`.
4. Regenerate the merged layer and inspect the resulting Czapek family for
   separate records for DSMZ 130, J29, J39, J271, and J441.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation on the repaired
  normalized inputs and regenerated Czapek-family generated records.
- Run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Manually compare DSMZ 130 with the MediaDive 130 REST payload and DSMZ PDF.
- Manually compare JCM 29, 39, 271, and 441 with their regenerated records to
  confirm agar, sucrose, nitrate, and pH differences are preserved.

## Additional Notes

- The generated `merged_from` list repeats `czapek_dox_agar` because bacterial
  and fungal normalized DSMZ/KOMODO records share the same basename.
- The JCM fungal records already use the correct 0.01 g/L conversion for
  10 mg FeSO4 x 7 H2O. Their TOGO bacterial copies store that same source row
  as `10 G_PER_L` and should be curated separately; those TOGO copies were not
  part of this generated merge.
