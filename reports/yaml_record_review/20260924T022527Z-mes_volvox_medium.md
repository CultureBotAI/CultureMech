# YAML Record Review: MES-Volvox Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mes_volvox_medium.yaml
- Started UTC: 2026-09-24T02:24:47Z
- Finished UTC: 2026-09-24T02:25:27Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Record ID | CultureMech:000174 |
| Name | mes_volvox_medium |
| Original name | MES-Volvox Medium |
| Category | algae |
| Medium source | UTEX:mes-volvox-medium |
| Target path | data/merge_yaml/merged/mes_volvox_medium.yaml |
| Maintained owner | data/normalized_yaml/algae/mes_volvox_medium.yaml |
| Generated status | Stale generated merge of 6 normalized sources on fingerprint 52fcd3367ce3e945938923f4b56b81cba26964f2e53d3417b97e6d6301282afd |

## Validation

- `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mes_volvox_medium.yaml`: Passed; exited 0 with no diagnostics.
- `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/mes_volvox_medium.yaml --out /private/tmp/mes_volvox_medium.strict.tsv --workers 1 --quiet`: Passed; 1 file scanned and 0 error rows.
- `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/mes_volvox_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`: Passed; 0 reference checks.
- `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/mes_volvox_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`: Passed after the known `eutils/pkg_resources` warning.
- Embedded history validator: Not checked. The documented `just validate-history` path validates standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated merged YAML.

## Identity and Grounding

- The reviewed generated record currently claims to be UTEX MES-Volvox Medium, but its `merged_from` list contains six distinct UTEX algal media: 1% F/2, 5% F/2, Allen, Bold 3N, BG-11(-N), and MES-Volvox.
- The live UTEX MES-Volvox page supports the repaired maintained owner, not the generated artifact. The maintained owner at `data/normalized_yaml/algae/mes_volvox_medium.yaml` now stores pH 6.7 and the source rows for Ca(NO3)2 x 4 H2O, MgSO4 x 7 H2O, Na2glycerophosphate x 5 H2O, KCl, MES, P-IV Metal Solution, NH4Cl, Vitamin B12, and Biotin Vitamin Solution.
- `rg --no-ignore --hidden` over `data/normalized_yaml` and `data/merge_yaml/merged` for exact UTEX MES-Volvox identifiers found one MES-Volvox maintained owner. The same search also confirmed that the extra generated `merged_from` entries resolve to distinct maintained owners with distinct `media_term` values.
- The numeric placeholder ingredients in the reviewed generated file are not chemical identities or source amounts. They are row numbers parsed from UTEX product tables before the normalized source records were repaired.

## Evidence

- UTEX says MES-Volvox is prepared from about 950 ml dH2O, seven main rows plus two vitamin stocks, adjusted to pH 6.7, brought to 1 L, autoclaved, and then supplemented with vitamins after cooling. For agar medium, UTEX adds 15 g agar before autoclaving and dispenses after the vitamins are mixed in.
- The reviewed generated file has nine ingredients named `1` through `9` with `VARIABLE` values and notes such as `Original amount: NaNO3(Fisher BP360-500)` and `Original amount: Vitamin B12`. Those rows do not match the UTEX MES-Volvox table or the current normalized MES-Volvox owner.
- The generated file's nine preparation steps are generic UTEX site-wide guidance about water quality, natural seawater, dissolving chemicals, stock solutions, and CO2 loss during autoclaving. It omits the MES-Volvox-specific pH 6.7, vitamin-after-cooling instruction, and optional 1.5% agar branch.
- 1% F/2, 5% F/2, Allen, Bold 3N, and BG-11(-N) are not synonyms of MES-Volvox. Their maintained records now have their own UTEX accessions, ingredients, and source-specific notes.

## Completeness

- Consequential gaps: every real MES-Volvox ingredient is missing from the generated record, the specific pH and preparation procedure are missing, and five unrelated UTEX media remain collapsed into the generated artifact.
- Empty optional slots: None found. The problem is stale placeholder content, not validly empty optional arrays.
- Bounded negative checks: The gitignore-independent search covered `data/normalized_yaml` and `data/merge_yaml/merged` and found no additional exact MES-Volvox maintained owner beyond `data/normalized_yaml/algae/mes_volvox_medium.yaml`.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | The generated record is a stale six-way merge of unrelated UTEX media. | `merged_from` lists 1% F/2, 5% F/2, Allen, Bold 3N, BG-11(-N), and MES-Volvox; the current normalized owners for those media now have distinct `media_term` IDs and distinct repaired recipes. | Regenerate `data/merge_yaml/merged/` from the repaired `data/normalized_yaml/algae/*.yaml` owners |
| Major | The generated ingredient list contains row-number placeholders rather than MES-Volvox components. | The reviewed YAML lists `1` through `9` as ingredient names, while the UTEX page and current normalized owner list chemical and stock names such as Ca(NO3)2 x 4 H2O, MES, P-IV Metal Solution, Vitamin B12, and Biotin Vitamin Solution. | Regenerate `data/merge_yaml/merged/mes_volvox_medium.yaml` from `data/normalized_yaml/algae/mes_volvox_medium.yaml` |
| Major | The generated preparation steps are generic UTEX guidance, not the MES-Volvox procedure. | UTEX says to adjust MES-Volvox to pH 6.7, bring to 1 L, autoclave, then add vitamins after cooling; the reviewed YAML carries only generic stock/water/autoclave notes. | Regenerate `data/merge_yaml/merged/mes_volvox_medium.yaml` from `data/normalized_yaml/algae/mes_volvox_medium.yaml` |

## Recommended Edits

- Regenerate `data/merge_yaml/merged/` so the repaired UTEX normalized owners no longer share the old placeholder fingerprint.
- Verify that the regenerated MES-Volvox output contains only `merged_from: [mes_volvox_medium]`.
- Verify that 1% F/2, 5% F/2, Allen, Bold 3N, and BG-11(-N) each generate as their own media records.

## Follow-up Checks

- Rerun the schema, strict, term, and reference validators on the regenerated MES-Volvox record.
- Run `rg --no-ignore --hidden` for `mes-volvox-medium`, `1_F_2_Medium`, `5_F_2_Medium`, `Allen_Medium`, `Bold_3N_Medium`, and `bg_11_n_medium` over `data/merge_yaml/merged` to confirm those identities no longer collapse into one generated YAML.
- Manually compare regenerated `mes_volvox_medium.yaml` with the live UTEX MES-Volvox page because validators cannot detect stale row-number placeholders.

## Additional Notes

- The maintained `data/normalized_yaml/algae/mes_volvox_medium.yaml` already appears to contain the real MES-Volvox recipe. The reviewed generated file is older than that repair.
